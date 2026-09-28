"""Offline command for deriving provisional signals from local snapshots."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from panta_signal.signals import calculate_source_price_delta
from panta_signal.snapshots import SnapshotError, iter_snapshots


DEFAULT_INPUT_PATH = (
    Path.home() / ".local" / "share" / "panta-signal" / "snapshots.jsonl"
)


def _market_counts(records):
    counts = Counter()
    for record in records:
        response = record.get("response", {})
        candidates = []
        items = response.get("items", [])
        if isinstance(items, list):
            candidates.extend(items)
        market = response.get("market")
        if isinstance(market, dict):
            candidates.append({"marketId": market.get("marketId"), "market": market})
        for item in candidates:
            if not isinstance(item, dict):
                continue
            data = item.get("market")
            if not isinstance(data, dict) or data.get("yesPrice") is None:
                continue
            market_id = item.get("marketId") or data.get("marketId")
            if isinstance(market_id, str) and market_id:
                counts[market_id] += 1
    return counts


def build_parser():
    parser = argparse.ArgumentParser(
        description="Calculate a provisional yesPrice delta from local Panta snapshots."
    )
    commands = parser.add_subparsers(dest="command", required=True)
    price_delta = commands.add_parser(
        "price-delta", help="compare the earliest and latest observations for one market"
    )
    price_delta.add_argument("--market-id", help="market to analyze; default selects the most observed market")
    price_delta.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help=f"JSONL snapshot file (default: {DEFAULT_INPUT_PATH})",
    )
    return parser


def main(argv=None, *, stdout=None, stderr=None):
    args = build_parser().parse_args(argv)
    output = sys.stdout if stdout is None else stdout
    errors = sys.stderr if stderr is None else stderr
    try:
        records = list(iter_snapshots(args.input.expanduser()))
        market_id = args.market_id
        if market_id is None:
            counts = _market_counts(records)
            if not counts:
                print("No market observations with yesPrice were found.", file=errors)
                return 2
            market_id = sorted(counts, key=lambda item: (-counts[item], item))[0]
        result = calculate_source_price_delta(records, market_id)
    except (OSError, SnapshotError, ValueError) as exc:
        print(f"Signal calculation failed: {exc}", file=errors)
        return 1

    print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2), file=output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
