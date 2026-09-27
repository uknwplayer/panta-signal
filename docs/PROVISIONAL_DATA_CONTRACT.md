# Provisional Data Contract — Panta Signal

**Status:** PROVISIONAL — limited live routes observed; provider implementation offline-tested; full compatibility unverified  
**Created:** 2026-09-27  
**Purpose:** guide parsing and UI work using synthetic examples while keeping the limited live evidence distinct from fixture data.

## Safety and interpretation

The JSON files alongside this document are synthetic internal-contract fixtures. They are not copied from Panta, do not describe real markets or trades, and must never be shown as live Panta data.

The documented account and test-key flow succeeded. Operator-run bounded reads through Termux `curl` returned HTTP 200 for categories, list, detail, and a trade tape. The sampled list returned one primary market with `nextCursor: null`; its detail included `onChain` but omitted `question`, `resolutionRule`, `sources`, and `totalTrades`; its trade tape was empty. This is limited live evidence, not a representative catalog or populated trade sample. Exact field types, many nullability rules, populated trade-row shape, cursor advancement, and cross-market variation remain unverified. The adjacent fixtures remain synthetic and must not be represented as live responses.

## Provisional market observation

One market observation represents the latest accepted state for one market at one fetch time.

| Field | Provisional meaning | Basis / limitation |
|---|---|---|
| `schemaVersion` | Internal contract version | Local metadata |
| `fixtureStatus` | Must read `synthetic_not_provider_response` in fixtures | Prevents fixture/live confusion |
| `provider` | Source provider identifier; `panta` for Panta ingestion | Implemented in the research-branch reader |
| `route` | Relative source route used for the observation | Documented routes exercised in bounded live reads; provider attaches route metadata |
| `fetchedAt` | Local UTC time when data was fetched/fixture was created | Local ingestion metadata |
| `liveValidated` | Always `false` for these fixtures | Explicitly blocks live claims |
| `market.marketId` | Source market identifier | Present as a string in the sampled live list/detail responses |
| `market.title` | Market title | Documented field |
| `market.category` | Category value or `null` | Documented field; enumeration not verified |
| `market.phase` | Source phase string | `primary` observed in one live list item; other values unverified |
| `market.marketType` | Source market type string or `null` | Documented concept; live values not verified |
| `market.volumeUsdc` | Normalized decimal string or `null` | Docs identify volume; numeric representation not verified |
| `market.yesPrice`, `market.noPrice` | Normalized decimal string or `null` | Detail may expose spot/phase prices; list prices may be null; do not turn null into zero |

The provider preserves the source market object and reports its actual `presentFields`; it does not synthesize omitted fields. The internal wrapper is not a claim that all upstream records have the same shape. Broader field mapping requires more live samples.

## Provisional trade observation

A trade observation should preserve the source market identifier, transaction signature where present, primary/secondary marker, YES/NO share amounts, fee, block time, and quote asset. Decimal-like values are represented as strings internally until the provider's wire types and precision are verified. The provider currently retains populated trade rows without field renaming; no populated live row has been observed, so trade field mapping and nullability remain provisional.

## Provisional snapshot record and local format

**Status:** DESIGN ONLY — persistence is not implemented.

A snapshot is one complete return value from a single PantaReadClient market-list, market-detail, or trade-tape call, wrapped as one versioned record. Store records as UTF-8 JSON Lines (JSONL), one record per line, in append-only order. A market-list page stays one record containing that page's items; do not split it into invented per-market responses or overwrite earlier observations. Detail and trade-tape calls are separate records. Category allowlists are configuration observations and are outside this market snapshot format.

The envelope is:

| Field | Type | Meaning |
|---|---|---|
| recordType | string | Constant panta-read-snapshot |
| snapshotVersion | integer | Envelope format version; starts at 1 |
| response | object | The complete object returned by one supported PantaReadClient market read method, stored without further edits |

The response object retains the provider wrapper fields, including provider, sourceRoute, and observedAt. For list/detail responses, the nested source market object and its reported presentFields are retained as returned. For trades, source trade rows are retained as returned; the current client adapts the API envelope's items array to trades and reports response presentFields. Therefore this format is faithful to the client observation, not a byte-for-byte HTTP archive. It must not be described as raw API capture.

Keep source field names and JSON values, missing fields, nulls, array order, decimal-like strings, and route query parameters intact; do not coerce numbers. Do not fill omitted values, coerce numbers, deduplicate observations, or mix derived signals into response. Future derived records must use a distinct record type and version. A change to envelope semantics requires a new snapshotVersion; this does not freeze the upstream market schema.

This choice is provisional and bounded to the current Panta client. A standard-library module now appends and reads the versioned JSONL envelope, validating the envelope and minimal Panta provenance without validating upstream market or trade schemas. Offline tests verify round trips with synthetic responses; no live payload has been persisted. This is not a commitment to a database, rotation policy, retention period, or cross-provider storage design.

## Deliberately deferred

Do not freeze these items from fixtures alone:

- cursor advancement and response behavior across multiple pages/markets;
- source timestamp type/time zone and nullability;
- populated trade-row fields, precision, and rounding rules;
- category and market-type enumerations;
- spot-price freshness guarantees;
- trade identifier uniqueness and ordering;
- final persistence schema;
- signal formulas, thresholds, or composite score.

## Local validator

Run from the repository root:

```sh
python -m unittest discover -s tests -v
```

`panta_signal/contracts.py` validates only the marked synthetic fixtures. It does not validate upstream responses and does not make the provisional contract authoritative. The separate `panta_signal/snapshots.py` validator checks only the local snapshot envelope and minimal provider provenance.

## Fixture acceptance checks

- Every fixture is explicitly marked synthetic and `liveValidated: false`.
- Missing list prices remain `null`, never zero.
- Synthetic market IDs, titles, signatures, and values cannot be mistaken for captured source records.
- Tests and UI must display a synthetic-data label when these fixtures are used.
- Promote this contract from provisional only after the provider is smoke-tested on-device and representative reads include multiple markets, a nonempty trade tape, and verified page movement where available.
