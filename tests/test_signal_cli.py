import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from panta_signal.signal_cli import main
from panta_signal.snapshots import append_snapshot


def response(observed_at, yes_price):
    return {
        "provider": "panta",
        "sourceRoute": "/markets/?limit=2",
        "observedAt": observed_at,
        "items": [
            {
                "marketId": "market-a",
                "market": {"marketId": "market-a", "yesPrice": yes_price},
            }
        ],
    }


class SignalCliTests(unittest.TestCase):
    def test_auto_selects_repeated_market_and_prints_delta_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "snapshots.jsonl"
            append_snapshot(path, response("2026-09-27T18:00:00Z", "0.40"))
            append_snapshot(path, response("2026-09-27T18:10:00Z", "0.43"))
            output = io.StringIO()
            errors = io.StringIO()

            code = main(["price-delta", "--input", str(path)], stdout=output, stderr=errors)

            self.assertEqual(code, 0)
            self.assertEqual(errors.getvalue(), "")
            result = json.loads(output.getvalue())
            self.assertEqual(result["algorithm"], "source-price-delta")
            self.assertEqual(result["marketId"], "market-a")
            self.assertEqual(result["delta"], "0.03")
            self.assertEqual(result["direction"], "up")

    def test_returns_clear_error_when_no_price_observations_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.jsonl"
            path.write_text("", encoding="utf-8")
            output = io.StringIO()
            errors = io.StringIO()

            code = main(["price-delta", "--input", str(path)], stdout=output, stderr=errors)

            self.assertEqual(code, 2)
            self.assertEqual(output.getvalue(), "")
            self.assertIn("no market observations with yesprice", errors.getvalue().lower())


if __name__ == "__main__":
    unittest.main()
