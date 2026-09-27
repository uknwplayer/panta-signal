# Signal Engine — Panta Signal

## Purpose

The Signal Engine converts timestamped market observations into deterministic, explainable indicators. It must remain reproducible and separate from AI-generated prose.

## Design Rules

Every implemented signal must:
- use explicit, versioned formulas;
- identify required input observations/windows;
- define missing-data behavior;
- be deterministic for the same input;
- preserve enough provenance to reproduce the result;
- have tests before it is marked implemented;
- expose limitations where interpretation may be misleading.

Exact formulas and thresholds in this document are currently **PLANNED** unless explicitly marked implemented in a later checkpoint.

## Planned Signal Families

### 1. Probability Movement

Measures change in market-implied probability across a defined window.

Candidate structure:
- current probability;
- reference probability at window start or nearest valid observation;
- absolute delta;
- signed delta;
- window duration;
- data-completeness state.

No production formula is frozen yet.

### 2. Movement Velocity

Measures how quickly probability is changing relative to elapsed time.

Requirements:
- avoid divide-by-zero/near-zero intervals;
- define minimum observation spacing;
- distinguish large slow changes from rapid smaller changes;
- preserve the exact window used.

### 3. Abnormal Change

Attempts to identify movements that are unusual relative to a market’s recent behavior.

Possible approaches to evaluate later include:
- rolling absolute-change distribution;
- robust z-score style normalization;
- percentile/rank against recent market history.

The chosen approach must tolerate sparse/outlier-prone data and must not claim statistical significance unless that claim is actually supported.

### 4. Recency and Persistence

Distinguishes a fresh spike from a movement that remains elevated or continues across multiple observations.

Planned outputs may include:
- time since first detected movement;
- time since latest qualifying movement;
- number/fraction of observations sustaining direction;
- persistence class/score.

### 5. Related-Market Divergence

Compares markets that are meaningfully related and identifies disagreement or inconsistent movement.

This signal remains conditional on a trustworthy market-relationship model. The relationship itself must carry provenance and confidence/method metadata.

### 6. Composite Signal Score

A composite score may combine validated component signals to rank attention-worthy markets.

It must not be implemented as an arbitrary opaque weighted sum without evaluation. Before freezing a score:
- component scales must be defined;
- normalization must be documented;
- weights/aggregation must be justified;
- missing components must have explicit behavior;
- examples/fixtures must show ranking behavior;
- score version must be included in outputs.

## Required Signal Record Metadata

A future signal record should include at least:
- signal ID;
- market ID;
- signal type;
- algorithm name/version;
- calculation timestamp;
- source observation timestamps/IDs;
- input window/parameters;
- output value/score;
- completeness/staleness state;
- provider/source identity.

Exact machine-readable schema will be frozen in Phase 2.

## Missing Data

Signals must not silently interpolate or fabricate source observations unless a future algorithm explicitly defines a deterministic interpolation method and marks interpolated values distinctly.

Possible states should include concepts such as:
- sufficient;
- partial;
- stale;
- insufficient.

Exact enum names are not yet frozen.

## Out-of-Order Observations

Implementation must define ordering by source/provider timestamps and/or ingestion timestamps. Late-arriving observations must not silently corrupt existing windows. The eventual data contract must specify conflict handling.

## Versioning

Signal algorithms must have stable versions. Changing formula semantics requires a new version or a clearly documented migration, so old results are not silently reinterpreted.

## AI Boundary

The AI Analyst may:
- explain a signal;
- compare signal records;
- summarize ranked results.

The AI Analyst may not:
- create authoritative signal values;
- rewrite algorithm outputs;
- invent missing observations;
- classify an algorithm as statistically valid without supporting evaluation.

## Validation Before Implementation

Before any signal family is marked implemented:
1. authoritative Panta probability/timestamp semantics must be verified;
2. test fixtures must be defined;
3. missing/stale behavior must be frozen;
4. formula/version must be documented;
5. tests must demonstrate deterministic output;
6. evaluation must check whether rankings are useful and not obviously pathological.
