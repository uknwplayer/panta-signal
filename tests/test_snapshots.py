import json
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from panta_signal.snapshots import (
    SNAPSHOT_RECORD_TYPE,
    SNAPSHOT_VERSION,
    SnapshotError,
    append_snapshot,
    build_snapshot_record,
    iter_snapshots,
    validate_snapshot_record,
)


def sample_response():
    return {
        "provider": "panta",
        "sourceRoute": "/markets/?limit=2",
        "observedAt": "2026-09-27T18:00:00Z",
        "items": [
            {
                "provider": "panta",
                "marketId": "synthetic-market-001",
                "market": {
                    "marketId": "synthetic-market-001",
                    "title": "Synthetic example",
                    "onChain": False,
                    "question": None,
                },
                "presentFields": ["marketId", "onChain", "question", "title"],
                "sourceRoute": "/markets/?limit=2",
                "observedAt": "2026-09-27T18:00:00Z",
            }
        ],
        "cursorPresent": True,
        "nextCursor": None,
    }


class SnapshotRecordTests(unittest.TestCase):
    def test_build_record_wraps_response_without_rewriting_or_mutating(self):
        response = sample_response()
        original = deepcopy(response)

        record = build_snapshot_record(response)

        self.assertEqual(
            record,
            {
                "recordType": SNAPSHOT_RECORD_TYPE,
                "snapshotVersion": SNAPSHOT_VERSION,
                "response": original,
            },
        )
        self.assertEqual(response, original)
        self.assertIs(record["response"], response)

    def test_validator_accepts_sparse_provider_response_and_returns_same_record(self):
        record = build_snapshot_record(sample_response())

        self.assertIs(validate_snapshot_record(record), record)

    def test_validator_rejects_unknown_type_or_version(self):
        record = build_snapshot_record(sample_response())
        record["recordType"] = "derived-signal"
        with self.assertRaises(SnapshotError):
            validate_snapshot_record(record)

        record = build_snapshot_record(sample_response())
        record["snapshotVersion"] = True
        with self.assertRaises(SnapshotError):
            validate_snapshot_record(record)

    def test_validator_requires_panta_provenance_in_response(self):
        record = build_snapshot_record(sample_response())
        del record["response"]["sourceRoute"]
        with self.assertRaises(SnapshotError):
            validate_snapshot_record(record)

        record = build_snapshot_record(sample_response())
        record["response"]["provider"] = "other"
        with self.assertRaises(SnapshotError):
            validate_snapshot_record(record)

    def test_jsonl_append_and_read_round_trip_multiple_observations(self):
        first = sample_response()
        second = {
            "provider": "panta",
            "marketId": "synthetic-market-001",
            "market": {"marketId": "synthetic-market-001", "yesPrice": "0.5800"},
            "presentFields": ["marketId", "yesPrice"],
            "sourceRoute": "/markets/synthetic-market-001/",
            "observedAt": "2026-09-27T18:01:00Z",
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "snapshots.jsonl"

            first_record = append_snapshot(path, first)
            second_record = append_snapshot(path, second)

            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lines), 2)
            self.assertTrue(all(json.loads(line)["recordType"] == SNAPSHOT_RECORD_TYPE for line in lines))
            self.assertEqual(list(iter_snapshots(path)), [first_record, second_record])
            self.assertEqual(first_record["response"], first)
            self.assertEqual(second_record["response"], second)
            self.assertEqual(first_record["response"]["items"][0]["market"]["question"], None)
            self.assertEqual(second_record["response"]["market"]["yesPrice"], "0.5800")

    def test_reader_reports_malformed_jsonl_line_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "broken.jsonl"
            path.write_text("{}\nnot-json\n", encoding="utf-8")

            with self.assertRaisesRegex(SnapshotError, "line 2"):
                list(iter_snapshots(path))

    def test_reader_rejects_invalid_envelope(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "invalid.jsonl"
            path.write_text(
                json.dumps({"recordType": "panta-read-snapshot", "snapshotVersion": 2, "response": {}}) + "\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(SnapshotError, "snapshotVersion"):
                list(iter_snapshots(path))

    def test_empty_file_yields_no_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.jsonl"
            path.write_text("", encoding="utf-8")
            self.assertEqual(list(iter_snapshots(path)), [])


if __name__ == "__main__":
    unittest.main()
