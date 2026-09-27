"""Versioned JSONL storage for Panta client observations.

This module validates the local snapshot envelope and minimal provenance only.
It does not validate Panta's upstream market or trade schemas.
"""

import json
from pathlib import Path


SNAPSHOT_RECORD_TYPE = "panta-read-snapshot"
SNAPSHOT_VERSION = 1


class SnapshotError(ValueError):
    """Raised when a local snapshot record cannot be validated or serialized."""


def _nonempty_string(value, field):
    if not isinstance(value, str) or not value.strip():
        raise SnapshotError(f"{field} must be a non-empty string")


def _validate_response(response):
    if not isinstance(response, dict):
        raise SnapshotError("response must be an object")
    if response.get("provider") != "panta":
        raise SnapshotError("response.provider must be panta")
    _nonempty_string(response.get("sourceRoute"), "response.sourceRoute")
    _nonempty_string(response.get("observedAt"), "response.observedAt")


def validate_snapshot_record(record):
    """Validate one versioned envelope without rewriting its response."""
    if not isinstance(record, dict):
        raise SnapshotError("snapshot record must be an object")
    if record.get("recordType") != SNAPSHOT_RECORD_TYPE:
        raise SnapshotError(f"recordType must be {SNAPSHOT_RECORD_TYPE}")
    version = record.get("snapshotVersion")
    if isinstance(version, bool) or version != SNAPSHOT_VERSION:
        raise SnapshotError(f"snapshotVersion must be {SNAPSHOT_VERSION}")
    _validate_response(record.get("response"))
    return record


def build_snapshot_record(response):
    """Wrap a Panta client observation, retaining the response object as-is."""
    _validate_response(response)
    return {
        "recordType": SNAPSHOT_RECORD_TYPE,
        "snapshotVersion": SNAPSHOT_VERSION,
        "response": response,
    }


def append_snapshot(path, response):
    """Append one complete client observation as a UTF-8 JSONL record."""
    record = build_snapshot_record(response)
    try:
        line = json.dumps(
            record,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        )
    except (TypeError, ValueError) as exc:
        raise SnapshotError("snapshot record is not JSON serializable") from exc

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(line)
        stream.write("\n")
    return record


def iter_snapshots(path):
    """Yield validated records from a JSONL file in stored order."""
    source = Path(path)
    with source.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SnapshotError(f"invalid JSON at line {line_number}") from exc
            try:
                validate_snapshot_record(record)
            except SnapshotError as exc:
                raise SnapshotError(f"invalid snapshot at line {line_number}: {exc}") from exc
            yield record
