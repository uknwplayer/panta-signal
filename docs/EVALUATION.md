# Evaluation — Panta Signal

## Purpose

Panta Signal must be evaluated on mechanical correctness and on whether the product actually helps a user identify and understand meaningful prediction-market movement.

## 1. Mechanical Correctness

### Determinism
For identical source observations, algorithm version, and parameters, signal output must be identical.

### Provenance completeness
Material signal records should contain required source identifiers, timestamps, algorithm/version, and input-window metadata.

### Missing-data behavior
Known gaps, stale observations, and malformed inputs must produce explicit states/errors rather than invented values.

### Ordering/time behavior
Out-of-order or delayed snapshots must be handled according to the frozen data contract.

### Secret boundary
Build/client artifacts and logs must not expose provider credentials.

## 2. Signal Quality

Signal quality should be assessed using curated fixtures and sampled real observations after the API is validated.

Questions include:
- Does the ranking surface large/rapid changes as expected?
- Does it over-rank tiny changes in very short intervals?
- Does sparse history produce misleading scores?
- Do persistence rules distinguish one-off spikes from sustained movement?
- Are component values understandable enough to explain a composite score?

No claim of predictive accuracy or statistical significance should be made without a separate, valid evaluation supporting it.

## 3. Explainability

A reviewer should be able to inspect a signal and answer:
- which market is involved;
- what changed;
- over what time window;
- which observations were used;
- which algorithm/version produced the result;
- whether data was complete/current;
- why the item ranked where it did.

## 4. AI Analyst Evaluation

Core test questions should eventually include:
- “Which markets moved most in the selected window?”
- “Why is this market ranked highly?”
- “Show the supporting numbers and timestamps.”
- “Which signals have incomplete or stale data?”
- “What do you know versus what are you inferring?”

Evaluate for:
- factual consistency with structured records;
- unsupported claims;
- provenance/evidence references;
- handling of missing evidence;
- prompt-injection resistance from source-market text;
- refusal to alter deterministic values.

## 5. Performance and Latency

After implementation, record:
- Panta fetch latency;
- ingestion/normalization latency;
- signal calculation latency;
- dashboard response latency;
- AI response latency separately.

Mechanical signal generation should not depend on an AI call.

## 6. Resilience

Test future implementation under:
- upstream timeout;
- rate limit;
- malformed provider response;
- missing timestamps;
- snapshot gap;
- duplicate observation;
- out-of-order observation;
- database unavailable;
- AI provider unavailable.

The non-AI product should degrade independently where feasible.

## 7. Demo and User-Value Evaluation

A strong demo should let a new viewer understand within a short sequence:
1. what changed in the market universe;
2. why the system surfaced it;
3. what source observations support it;
4. what the AI adds beyond the deterministic layer.

Subjective review questions:
- Is this clearly more useful than a generic market list/dashboard?
- Can a judge find the differentiating feature quickly?
- Is provenance visible without reading source code?
- Does the AI Analyst feel grounded rather than ornamental?
- Are limitations/staleness clear?

## 8. Hackathon Evidence

Evaluation results used in a submission should link to reproducible repository evidence when possible: tests, fixtures, screenshots, demo build/commit, and public URL.

## Current State

This is the evaluation framework only. No signal-quality benchmark, latency benchmark, production test suite, or public-demo evaluation has been completed yet.
