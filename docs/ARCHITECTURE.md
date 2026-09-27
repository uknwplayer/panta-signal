# Architecture — Panta Signal

## Logical View

```text
Panta API
   |
   v
Server-side API client / ingestion
   |
   v
Validation + normalization
   |
   +--> Snapshot store
   |
   v
Deterministic Signal Engine
   |
   +--> Signal records / rankings
   |
   +--> Internal API
            |
            +--> Web dashboard
            |
            +--> AI Analyst
```

## Components

### 1. Panta API Client

Responsible for authenticated server-side requests to Panta. Credentials must never be exposed to the browser or committed to source control.

Exact endpoints, authentication rules, limits, and response schemas remain **UNVERIFIED** until authoritative API validation is completed.

### 2. Validation and Normalization

Treat external responses as untrusted input. Convert accepted source fields into an internal market schema while preserving source identifiers and timestamps.

Normalization must not silently change the semantic meaning of source values. Unknown or unsupported fields should be retained only when they are safe and useful, or explicitly ignored.

### 3. Snapshot Store

Stores time-indexed observations required to calculate change over time. The storage provider is not yet selected.

Snapshots should preserve enough evidence to reproduce material signals without requiring full indefinite retention of every upstream payload.

### 4. Signal Engine

A deterministic analytical layer. Planned signal families include:
- probability movement;
- movement velocity;
- abnormal change;
- recency and persistence;
- related-market divergence;
- composite signal scoring.

Exact formulas and thresholds are **PLANNED**, not implemented. Each algorithm must be versioned and testable before production use.

### 5. Internal API

Provides structured market and signal data to the user interface and AI Analyst. The internal API should expose provenance metadata with material signals.

### 6. Web Dashboard

Presents market intelligence, ranked signals, filters, watchlists, evidence, and explanations. It must distinguish source facts from derived metrics and AI-generated text.

### 7. AI Analyst

Consumes structured internal data to answer natural-language questions. The model may summarize or explain evidence, but it must not override deterministic records or manufacture missing market facts.

## Data Classes

The architecture recognizes three mandatory classes:

1. **Source data** — received from Panta or another documented external source.
2. **Deterministic derived data** — normalized fields, deltas, rates, rankings, scores, and other reproducible calculations.
3. **AI-generated interpretation** — prose explanations, summaries, and suggested lines of inquiry.

These classes must remain distinguishable in storage contracts and UI presentation.

## Planned Signal Traceability

A material signal should be traceable to:
- market identifier;
- source/provider;
- source observation timestamp;
- stored observation/snapshot identifiers;
- algorithm name and version;
- calculation timestamp;
- relevant parameters/window.

## Security Boundary

The initial architecture:
- keeps Panta and AI credentials server-side;
- does not place secrets in browser bundles;
- does not execute user-submitted code;
- does not fetch arbitrary user-supplied URLs unless separately designed;
- treats upstream data and model output as untrusted;
- sanitizes operational logs;
- excludes wallet custody, private keys, swaps, and autonomous trading.

## Persistence

A persistent store is expected for snapshots and derived signals, but the exact database/runtime is an open decision. Selection criteria include:
- free or minimal-cost operation;
- simple deployment;
- timestamped historical queries;
- deterministic migrations/schema handling;
- compatibility with the selected web runtime;
- enough reliability for a public demo.

## Deployment

No deployment provider has been selected and no public deployment currently exists. Runtime selection will follow authoritative Panta API validation and the first technical specification.

## Failure Principles

Future implementation should:
- surface upstream API failure explicitly;
- avoid presenting stale data as current without timestamps;
- tolerate missing snapshot intervals where possible;
- prevent AI-generated claims from filling unknown structured values;
- preserve the last known verified state separately from current-fetch status.
