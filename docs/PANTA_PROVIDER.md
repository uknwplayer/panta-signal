# Panta Read-only Provider

**Status:** IMPLEMENTED; OFFLINE-TESTED; ALL FOUR METHODS LIVE-SMOKE-TESTED ON ONE NARROW SAMPLE; DATA COVERAGE PARTIAL  
**Scope:** Authenticated, bounded GET requests for Panta categories, market list, market detail, and a market trade tape.

## Safety boundary

`PantaReadClient` issues GET requests only. It has no market-creation, quote, order, trade-submission, wallet, signing, claim, or capital-movement methods.

Pass the API key to the client from a server-side secret source, such as an environment variable. Never commit a real key or place it in a query string. The transport sends only the URL and headers through cURL configuration on stdin, keeping the key out of the URL and process arguments. Non-secret transport options are command-line arguments, and `-q` is first so user-level `.curlrc` settings are ignored. This keeps the stdin configuration small for Termux compatibility. HTTP errors omit the response body and key.

The client requires the `curl` executable. It allows only Panta's published live and staging API base URLs.

## Supported reads

| Method | Route | Bound |
|---|---|---|
| `get_categories()` | `GET /categories/` | one response |
| `list_markets(limit=20, cursor=None, category=None, status=None)` | `GET /markets/` | limit 1–50; one page per call |
| `get_market(market_id)` | `GET /markets/{marketId}/` | one market |
| `get_trades(market_id, limit=50)` | `GET /markets/{marketId}/trades/` | limit 1–200; one response |

The client does not automatically fetch another page. It preserves whether the `nextCursor` field was present and its value. An absent cursor and an explicit null cursor remain distinguishable through `cursorPresent`.

## Response handling

Market wrappers keep the source object under `market` and expose the actual upstream keys in `presentFields`. Optional fields are not filled in. This supports complete and stripped response shapes without turning missing fields into invented values.

Trade rows are retained as received. An empty `items` array is a valid result and becomes `trades: []`. Since the live sample so far had no rows, a populated trade row has not been validated by Panta Signal.

Every normalized result includes `provider`, `sourceRoute`, and a local UTC `observedAt` timestamp. These describe ingestion metadata and do not replace source timestamps.

## Example

```python
import os
from panta_signal.providers.panta import PantaReadClient

client = PantaReadClient(os.environ["PANTA_API_KEY"])
categories = client.get_categories()
page = client.list_markets(limit=20)
if page["items"]:
    market_id = page["items"][0]["marketId"]
    detail = client.get_market(market_id)
    tape = client.get_trades(market_id, limit=10)
```

Set `PANTA_API_KEY` only in the server-side environment. Do not print it or include it in logs.

## Verification status

The Panta client tests use synthetic responses and a fake subprocess runner. The complete repository suite passed 34 offline tests on Python 3.12.14, including snapshot-library and CLI tests. Tests validate request construction, read-only method configuration, sparse-field preservation, cursor handling, empty tapes, bounds, sanitized HTTP errors, and JSONL round trips. They do not make live calls.

Operator-run live reads through Termux `curl` validated HTTP 200 for categories, list, detail, and an empty trade tape. The provider itself has now completed authenticated Termux smoke tests for all four methods: `get_categories()` returned HTTP 200 with four categories; `list_markets(limit=2)` returned HTTP 200 with one primary item and a present but empty cursor; `get_market()` returned HTTP 200 with a matching market ID; and `get_trades(market_id, limit=10)` returned HTTP 200 with zero trades and response fields `disclaimer`, `items`, and `marketId`. This validates the empty-tape path, not the shape of populated trade rows. The live catalogue sample is one market and has no usable cursor, so broader coverage, cursor advancement, and populated trade-row handling remain unverified.


## Local snapshot storage

The panta_signal.snapshots module appends one Panta market-list, detail, or trade-tape client response per line to UTF-8 JSONL and reads records back in order. It validates the local versioned envelope and minimal provider provenance, not the upstream response schema.

The explicit CLI makes exactly one bounded read per invocation and appends one record. It does not schedule requests, automatically follow cursors, or call write endpoints. By default, the JSONL file is stored outside the repository at ~/.local/share/panta-signal/snapshots.jsonl.

Usage:

    python -m panta_signal.snapshot_cli --help
    python -m panta_signal.snapshot_cli list --limit 2
    python -m panta_signal.snapshot_cli detail MARKET_ID
    python -m panta_signal.snapshot_cli trades MARKET_ID --limit 10

Set PANTA_API_KEY in the environment from a device-local secret source before running the command. Never pass the key as a command-line argument, print it, or commit snapshots. The CLI has passed offline tests and the operator ran Termux list, detail, and trades smoke tests. The three calls appended three local JSONL records. A sanitized read through the project reader reported one record per route type and zero trade rows. No snapshot content or market identifier was shared or committed to the repository. This remains one market and an empty trade sample.
