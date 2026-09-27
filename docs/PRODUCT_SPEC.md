# Product Specification — Panta Signal MVP

## Product Goal

Build a public, explainable prediction-market intelligence product that turns Panta market observations into ranked signals and natural-language analysis without requiring the operator or user to trade.

## Primary Users

### Human analyst
Needs to quickly identify markets with meaningful movement, inspect why they were ranked, compare related events, and understand the supporting timestamps/data.

### AI/agent consumer
Needs structured market and signal records that can be queried without scraping the visual dashboard or trusting unsupported prose.

## Core User Stories

1. As a user, I can see which markets have moved most meaningfully over a chosen recent window.
2. As a user, I can inspect a signal and see the source market, timestamps, input observations, and calculation rationale.
3. As a user, I can filter/search markets and signals by available metadata.
4. As a user, I can distinguish current/source values from locally derived metrics.
5. As a user, I can ask the AI Analyst questions such as “what moved most?” and receive answers grounded in structured records.
6. As a user, I can tell when data is stale, incomplete, or unavailable.

## Product Layers

### 1. Market Intelligence

**Planned capabilities:**
- ingest verified Panta market data;
- normalize market identity/state;
- persist time-indexed observations;
- show recent market state and timestamps;
- search/filter by verified metadata;
- rank/filter by activity and signal state;
- optionally support watchlists if schedule permits.

### 2. Signal Engine

**Planned capabilities:**
- probability movement;
- movement velocity;
- abnormal-change detection;
- recency/persistence;
- related-market divergence where relationship quality is sufficient;
- composite Signal Score only after component behavior is evaluated.

Every implemented signal must be deterministic, versioned, testable, and traceable to source observations.

### 3. AI Analyst

**Planned capabilities:**
- answer questions over structured market/signal data;
- explain why a signal ranked highly;
- summarize selected categories/windows;
- identify evidence used in each answer;
- explicitly handle insufficient evidence.

The model must not mutate deterministic records or fabricate missing market facts.

## Primary MVP Flow

```text
Fetch verified Panta market data
        |
        v
Validate + normalize
        |
        v
Store timestamped snapshot
        |
        v
Calculate deterministic signals
        |
        v
Rank / expose through internal API
        |
        +--> Dashboard inspection
        +--> AI Analyst query
```

## Functional Requirements

### FR-1 Source ingestion
The system must retrieve only API contracts that have been validated from authoritative Panta documentation/live behavior.

### FR-2 Normalization
Normalized records must preserve source identity/timestamps and must not silently invent missing values.

### FR-3 Snapshot history
The system must retain enough timestamped observations to calculate implemented time-window signals.

### FR-4 Deterministic signals
Signal outputs must be reproducible from recorded inputs, algorithm version, and parameters.

### FR-5 Provenance display
Material signals must expose or link to source market identity, observation times, algorithm/version, and data completeness.

### FR-6 Ranked intelligence
The UI must support a ranked view that surfaces meaningful signals rather than simply listing markets alphabetically or by provider defaults.

### FR-7 Detail view
A user must be able to inspect a market/signal and understand what changed and over what period.

### FR-8 AI evidence grounding
AI answers must be built from structured records and should identify the relevant market/signal evidence.

### FR-9 Staleness visibility
Current-fetch failures and stale/partial history must be visible to the user and downstream analyst.

### FR-10 Secret isolation
Provider credentials must remain server-side and out of browser bundles, repository history, and logs.

## Non-Functional Requirements

- low-cost or free initial deployment;
- public HTTPS for the demo;
- responsive dashboard suitable for desktop/mobile browsers;
- deterministic mechanical calculations;
- reproducible repository setup;
- bounded external calls and AI usage;
- clear operational failure states;
- no required financial transaction to experience core product value.

## Acceptance Criteria for MVP

The MVP is considered implemented only when evidence confirms:
- a verified Panta read-only data flow works end to end;
- at least one meaningful time-based signal is calculated from stored snapshots and tested;
- signal detail includes provenance/timestamps;
- ranked signals are visible in the dashboard;
- AI Analyst answers at least the defined core questions using structured evidence;
- stale/missing data is handled explicitly;
- public deployment is reachable;
- secrets are not exposed;
- repository instructions reproduce the validated setup.

## Non-Goals

The initial MVP does not include:
- autonomous trading;
- swaps;
- wallet custody/private keys;
- portfolio execution;
- native mobile application;
- social/community feed;
- full multi-provider abstraction;
- complex billing;
- advanced user organizations/roles.

## Open Product Decisions

- exact first signal windows/thresholds;
- whether watchlists require accounts or local persistence;
- whether related-market divergence fits the MVP after data inspection;
- AI provider/model;
- which market metadata can be reliably filtered based on verified Panta fields.
