# Whitepaper — Panta Signal

## Abstract

Panta Signal is a prediction-market intelligence layer designed to transform market state and movement into explainable, queryable signals for humans and AI agents. The initial product uses Panta as its primary market-data source and keeps numerical analysis deterministic and auditable before any AI-generated explanation is added.

## Problem

Prediction markets compress distributed expectations into continuously changing probabilities, but raw market pages are difficult to monitor at scale. Important changes can be buried across many markets, movement speed is not always obvious, related markets may diverge, and natural-language analysis can easily overstate unsupported conclusions.

## Proposal

Panta Signal separates the product into three layers:

1. **Market Intelligence** — normalize market metadata and observations, maintain snapshots, support search/filtering/watchlists, and expose relevant activity.
2. **Signal Engine** — derive reproducible indicators such as probability movement, movement velocity, abnormal change, persistence, and related-market divergence.
3. **AI Analyst** — answer questions and explain signals using structured evidence, without replacing deterministic calculations with model guesses.

## Product Thesis

Prediction markets can be treated as information sensors rather than merely trading venues. A useful intelligence product should make changes discoverable, rankable, traceable, and explainable while preserving the boundary between source data, deterministic derivation, and interpretation.

## Desired Properties

- explainable signals;
- reproducible calculations;
- explicit provenance;
- low operating cost;
- server-side credential handling;
- resilience to missing or delayed observations;
- clear separation between facts, derived metrics, and AI interpretation;
- usable by both humans and agents.

## Initial Scope

The MVP is planned to provide:
- ingestion of selected Panta market data;
- normalized market records;
- historical snapshots collected by the application;
- deterministic signal generation;
- ranked signal views;
- dashboard search/filtering;
- natural-language analysis over structured records.

Exact Panta API contracts remain **UNVERIFIED** until authoritative API documentation and live behavior are validated in a later work block.

## Non-Goals

The initial MVP does not require:
- real-money trading;
- autonomous trade execution;
- wallet custody or private keys;
- swaps or fund movement;
- native mobile applications;
- generalized support for all prediction-market providers;
- complex multi-tenant account infrastructure.

## Zero-Capital Constraint

The core product must be useful without requiring the operator to place trades or commit personal capital. Any future transactional capability would require a separate approved design and security review.

## Evidence Model

Panta Signal treats data as three distinct classes:
1. external/source data;
2. deterministic derived data;
3. AI-generated interpretation.

Important signals should be traceable to source market identifiers, timestamps, observations, algorithm version, and calculation time.

## Success Criteria

The product reaches an MVP-quality state only when verified evidence shows that:
- authoritative Panta data can be ingested safely;
- normalized snapshots are stored consistently;
- signal calculations are deterministic and tested;
- provenance is preserved from source observation to displayed signal;
- the dashboard exposes useful ranked intelligence;
- the AI Analyst cites supporting structured data rather than inventing facts;
- a public deployment can be reproduced and demonstrated;
- hackathon submission requirements are verified and satisfied.

Documentation alone does not satisfy these criteria.
