"""Explicit one-request Panta snapshot ingestion command.

Run with: python -m panta_signal.snapshot_cli {list,detail,trades} ...
The command performs exactly one bounded read and appends one local JSONL record.
"""

import argparse
import os
import sys
from pathlib import Path

from panta_signal.providers.panta import PantaReadClient, ProviderError
from panta_signal.snapshots import SnapshotError, append_snapshot


DEFAULT_OUTPUT_PATH = (
    Path.home() / ".local" / "share" / "panta-signal" / "snapshots.jsonl"
)


def _bounded_integer(maximum):
    def parse(value):
        try:
            parsed = int(value)
        except ValueError as exc:
            raise argparse.ArgumentTypeError("must be an integer") from exc
        if not 1 <= parsed <= maximum:
            raise argparse.ArgumentTypeError(f"must be between 1 and {maximum}")
        return parsed

    return parse


def _add_output_argument(parser):
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f"JSONL destination (default: {DEFAULT_OUTPUT_PATH})",
    )


def build_parser():
    parser = argparse.ArgumentParser(
        description="Make one bounded, read-only Panta market-data request and append a snapshot."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    listing = commands.add_parser("list", help="fetch one market-list page")
    listing.add_argument("--limit", type=_bounded_integer(50), default=20)
    listing.add_argument("--cursor")
    listing.add_argument("--category")
    listing.add_argument("--status")
    _add_output_argument(listing)

    detail = commands.add_parser("detail", help="fetch one market detail")
    detail.add_argument("market_id")
    _add_output_argument(detail)

    trades = commands.add_parser("trades", help="fetch one trade-tape page")
    trades.add_argument("market_id")
    trades.add_argument("--limit", type=_bounded_integer(200), default=50)
    _add_output_argument(trades)

    return parser


def main(argv=None, *, client_factory=None, environ=None, stdout=None, stderr=None):
    """Run one explicit read and persist its result; return a process status code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    env = os.environ if environ is None else environ
    output = sys.stdout if stdout is None else stdout
    errors = sys.stderr if stderr is None else stderr
    api_key = env.get("PANTA_API_KEY")
    if not api_key:
        print("PANTA_API_KEY is required in the environment.", file=errors)
        return 2

    factory = PantaReadClient if client_factory is None else client_factory
    try:
        client = factory(api_key)
        if args.command == "list":
            response = client.list_markets(
                limit=args.limit,
                cursor=args.cursor,
                category=args.category,
                status=args.status,
            )
        elif args.command == "detail":
            response = client.get_market(args.market_id)
        else:
            response = client.get_trades(args.market_id, limit=args.limit)
        destination = args.output.expanduser()
        append_snapshot(destination, response)
    except (ProviderError, SnapshotError, OSError) as exc:
        print(f"Snapshot ingestion failed: {exc}", file=errors)
        return 1

    print(f"Saved one Panta {args.command} snapshot to {destination}.", file=output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
