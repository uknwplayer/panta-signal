import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from panta_signal.snapshot_cli import DEFAULT_OUTPUT_PATH, build_parser, main
from panta_signal.providers.panta import ProviderError


def sample_response():
    return {
        "provider": "panta",
        "sourceRoute": "/markets/?limit=2",
        "observedAt": "2026-09-27T18:30:00Z",
        "items": [],
        "cursorPresent": True,
        "nextCursor": None,
    }


class SnapshotCliTests(unittest.TestCase):
    def run_cli(self, argv, response=None, env=None, client=None):
        output = StringIO()
        errors = StringIO()
        client = client or Mock()
        if response is not None:
            if argv[0] == "list":
                client.list_markets.return_value = response
            elif argv[0] == "detail":
                client.get_market.return_value = response
            else:
                client.get_trades.return_value = response
        factory = Mock(return_value=client)
        status = main(
            argv,
            client_factory=factory,
            environ={} if env is None else env,
            stdout=output,
            stderr=errors,
        )
        return status, output.getvalue(), errors.getvalue(), client, factory

    def test_requires_api_key_without_constructing_client(self):
        factory = Mock()
        status = main(
            ["list"],
            client_factory=factory,
            environ={},
            stdout=StringIO(),
            stderr=(errors := StringIO()),
        )

        self.assertEqual(status, 2)
        self.assertIn("PANTA_API_KEY", errors.getvalue())
        factory.assert_not_called()

    def test_list_fetches_one_page_and_appends_one_snapshot(self):
        response = sample_response()
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "nested" / "snapshots.jsonl"
            status, output, errors, client, factory = self.run_cli(
                ["list", "--limit", "7", "--cursor", "cursor-input",
                 "--category", "crypto", "--status", "active",
                 "--output", str(destination)],
                response=response,
                env={"PANTA_API_KEY": "pk_test_example"},
            )

            self.assertEqual(status, 0, errors)
            client.list_markets.assert_called_once_with(
                limit=7, cursor="cursor-input", category="crypto", status="active"
            )
            client.get_market.assert_not_called()
            client.get_trades.assert_not_called()
            factory.assert_called_once_with("pk_test_example")
            lines = destination.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 1)
            self.assertIn("Saved one Panta list snapshot", output)
            self.assertEqual(errors, "")

    def test_detail_fetches_only_requested_market(self):
        response = {
            "provider": "panta",
            "marketId": "synthetic-market-001",
            "market": {"marketId": "synthetic-market-001"},
            "presentFields": ["marketId"],
            "sourceRoute": "/markets/synthetic-market-001/",
            "observedAt": "2026-09-27T18:31:00Z",
        }
        with tempfile.TemporaryDirectory() as tmp:
            status, _, errors, client, _ = self.run_cli(
                ["detail", "synthetic-market-001", "--output", str(Path(tmp) / "x.jsonl")],
                response=response,
                env={"PANTA_API_KEY": "pk_test_example"},
            )

            self.assertEqual(status, 0, errors)
            client.get_market.assert_called_once_with("synthetic-market-001")
            client.list_markets.assert_not_called()
            client.get_trades.assert_not_called()

    def test_trades_fetches_one_bounded_page(self):
        response = {
            "provider": "panta",
            "marketId": "synthetic-market-001",
            "sourceRoute": "/markets/synthetic-market-001/trades/?limit=9",
            "observedAt": "2026-09-27T18:32:00Z",
            "trades": [],
            "presentFields": ["items", "marketId"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            status, _, errors, client, _ = self.run_cli(
                ["trades", "synthetic-market-001", "--limit", "9",
                 "--output", str(Path(tmp) / "x.jsonl")],
                response=response,
                env={"PANTA_API_KEY": "pk_test_example"},
            )

            self.assertEqual(status, 0, errors)
            client.get_trades.assert_called_once_with("synthetic-market-001", limit=9)
            client.list_markets.assert_not_called()
            client.get_market.assert_not_called()

    def test_limits_are_bounded_before_a_client_can_be_created(self):
        with self.assertRaises(SystemExit):
            build_parser().parse_args(["list", "--limit", "51"])
        with self.assertRaises(SystemExit):
            build_parser().parse_args(["trades", "synthetic-market-001", "--limit", "201"])

    def test_missing_output_uses_private_home_data_location(self):
        self.assertEqual(
            DEFAULT_OUTPUT_PATH,
            Path.home() / ".local" / "share" / "panta-signal" / "snapshots.jsonl",
        )

    def test_provider_error_does_not_append_and_does_not_echo_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "failed.jsonl"
            client = Mock()
            client.list_markets.side_effect = ProviderError("sanitized provider failure")
            status, output, errors, _, _ = self.run_cli(
                ["list", "--output", str(destination)],
                env={"PANTA_API_KEY": "pk_test_secret_example"},
                client=client,
            )

            self.assertEqual(status, 1)
            self.assertEqual(output, "")
            self.assertIn("sanitized provider failure", errors)
            self.assertNotIn("pk_test_secret_example", errors)
            self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
