# Provisional Data Contract — Panta Signal

**Status:** PROVISIONAL — documentation-derived; not live-validated  
**Created:** 2026-09-27  
**Purpose:** allow parser and UI work to proceed using synthetic examples while Panta API registration is blocked.

## Safety and interpretation

The JSON files alongside this document are synthetic internal-contract fixtures. They are not copied from Panta, do not describe real markets or trades, and must never be shown as live Panta data.

The public API documentation identifies market and trade fields, but the live signup flow currently returns HTTP 403. Exact response types, nullability, field nesting, timestamp formats, category values, and response envelopes remain unverified. Do not use these examples to claim API compatibility.

## Provisional market observation

One market observation represents the latest accepted state for one market at one fetch time.

| Field | Provisional meaning | Basis / limitation |
|---|---|---|
| `schemaVersion` | Internal contract version | Local metadata |
| `fixtureStatus` | Must read `synthetic_not_provider_response` in fixtures | Prevents fixture/live confusion |
| `provider` | Source provider identifier; `panta` for planned ingestion | Planned |
| `route` | Relative source route used for the observation | Route documented; exact request metadata not yet validated |
| `fetchedAt` | Local UTC time when data was fetched/fixture was created | Local ingestion metadata |
| `liveValidated` | Always `false` for these fixtures | Explicitly blocks live claims |
| `market.marketId` | Source market identifier | Documented field; exact JSON type still to verify |
| `market.title` | Market title | Documented field |
| `market.category` | Category value or `null` | Documented field; enumeration not verified |
| `market.phase` | Source phase string | Docs describe primary/secondary/resolved/cancelled; live values not verified |
| `market.marketType` | Source market type string or `null` | Documented concept; live values not verified |
| `market.volumeUsdc` | Normalized decimal string or `null` | Docs identify volume; numeric representation not verified |
| `market.yesPrice`, `market.noPrice` | Normalized decimal string or `null` | Detail may expose spot/phase prices; list prices may be null; do not turn null into zero |

The provisional shape is for internal normalization, not a prediction of the upstream JSON envelope. Final field mapping requires live evidence.

## Provisional trade observation

A trade observation should preserve the source market identifier, transaction signature where present, primary/secondary marker, YES/NO share amounts, fee, block time, and quote asset. Decimal-like values are represented as strings internally until the provider's wire types and precision are verified. The precise normalized field names and nullability remain provisional.

## Deliberately deferred

Do not freeze these items from fixtures alone:

- upstream response envelopes and pagination cursor shape;
- provider timestamp type/time zone and nullability;
- decimal precision and rounding rules;
- category and market-type enumerations;
- spot-price freshness guarantees;
- trade identifier uniqueness and ordering;
- final persistence schema;
- signal formulas, thresholds, or composite score.

## Fixture acceptance checks

- Every fixture is explicitly marked synthetic and `liveValidated: false`.
- Missing list prices remain `null`, never zero.
- Synthetic market IDs, titles, signatures, and values cannot be mistaken for captured source records.
- Tests and UI must display a synthetic-data label when these fixtures are used.
- Promote this contract from provisional only after controlled read-only calls to categories, markets, one market detail, and one trade tape have been recorded in the checkpoint.
