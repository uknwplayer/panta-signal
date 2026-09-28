import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from panta_signal.signals import calculate_source_price_delta


def record(observed_at, value, market_id="m-1", route="/markets/"):
    market = {"marketId": market_id, "yesPrice": value}
    response = {
        "provider": "panta",
        "sourceRoute": route,
        "observedAt": observed_at,
    }
    if route == "/markets/":
        response["items"] = [{"marketId": market_id, "market": market}]
    else:
        response["market"] = market
    return {"recordType": "panta-read-snapshot", "snapshotVersion": 1, "response": response}


class SourcePriceDeltaTests(unittest.TestCase):
    def test_calculates_sorted_first_to_last_delta_for_one_market(self):
        records = [
            record("2026-09-27T18:02:00Z", "0.6150"),
            record("2026-09-27T18:00:00Z", "0.58", route="/markets/m-1/"),
            record("2026-09-27T18:01:00Z", "0.7", market_id="other"),
        ]

        result = calculate_source_price_delta(records, "m-1")

        self.assertEqual(result["algorithm"], "source-price-delta")
        self.assertEqual(result["version"], 1)
        self.assertEqual(result["status"], "sufficient")
        self.assertEqual(result["observationCount"], 2)
        self.assertEqual(result["startObservedAt"], "2026-09-27T18:00:00Z")
        self.assertEqual(result["endObservedAt"], "2026-09-27T18:02:00Z")
        self.assertEqual(result["startValue"], "0.58")
        self.assertEqual(result["endValue"], "0.615")
        self.assertEqual(result["delta"], "0.035")
        self.assertEqual(result["direction"], "up")
        self.assertEqual(result["startSourceRoute"], "/markets/m-1/")
        self.assertEqual(result["endSourceRoute"], "/markets/")

    def test_reports_insufficient_when_fewer_than_two_valid_observations(self):
        result = calculate_source_price_delta(
            [record("2026-09-27T18:00:00Z", "0.58")], "m-1"
        )

        self.assertEqual(result["status"], "insufficient")
        self.assertEqual(result["observationCount"], 1)
        self.assertIsNone(result["delta"])
        self.assertIsNone(result["direction"])

    def test_rejects_malformed_price_and_naive_timestamp(self):
        with self.assertRaises(ValueError):
            calculate_source_price_delta(
                [record("2026-09-27T18:00:00Z", "not-a-number")], "m-1"
            )
        with self.assertRaises(ValueError):
            calculate_source_price_delta(
                [record("2026-09-27T18:00:00", "0.58")], "m-1"
            )

    def test_identical_values_report_unchanged(self):
        result = calculate_source_price_delta(
            [
                record("2026-09-27T18:00:00Z", "0.5800"),
                record("2026-09-27T18:01:00Z", "0.58", route="/markets/m-1/"),
            ],
            "m-1",
        )

        self.assertEqual(result["delta"], "0")
        self.assertEqual(result["direction"], "unchanged")


if __name__ == "__main__":
    unittest.main()
