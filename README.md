# Panta Signal

Panta Signal is a prediction-market intelligence layer designed to turn market movement into explainable, queryable signals for humans and AI agents.

## Project Language

**English is the official language of this repository.** Source code, comments, documentation, API fields, public errors, issues, releases, and public-facing communication must be written in English. Private working conversation with the operator may remain in Portuguese.

## Current Status

**Current phase:** documentation foundation.

No live Panta API integration, signal engine implementation, public deployment, or hackathon submission is claimed yet. This repository currently defines the product direction, security boundaries, provenance rules, roadmap, and continuity model required before implementation begins.

## Product Thesis

Prediction markets can act as information sensors. Panta Signal aims to transform raw market state and movement into structured intelligence that is easier to inspect, rank, explain, and query.

The initial product has three layers:

1. **Market Intelligence** — markets, probabilities, categories, activity, snapshots, search, filtering, and watchlists.
2. **Signal Engine** — deterministic, reproducible indicators derived from market changes.
3. **AI Analyst** — natural-language explanation and querying over structured market and signal data.

The AI layer is downstream of deterministic analysis. AI-generated text is not the source of truth for numerical market signals.

## Initial MVP Boundaries

The first MVP does **not** require personal capital, real-money trading, autonomous execution, wallet custody, private keys, swaps, or fund movement.

It also does not initially target:
- native mobile applications;
- social features;
- complex multi-tenant accounts;
- support for every prediction-market provider;
- paid infrastructure unless free options prove insufficient.

## Planned Logical Flow

```text
Panta API
   |
   v
Server-side ingestion
   |
   v
Normalized market data
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
            +--> AI Analyst
```

## Documentation

Always consult:
- [Current checkpoint](docs/checkpoints/CHECKPOINT_CURRENT.md)
- [Roadmap](docs/ROADMAP.md)
- [Whitepaper](docs/WHITEPAPER.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Product specification](docs/PRODUCT_SPEC.md)
- [Signal Engine](docs/SIGNAL_ENGINE.md)
- [Security](docs/SECURITY.md)
- [Data provenance](docs/DATA_PROVENANCE.md)
- [Evaluation](docs/EVALUATION.md)
- [Hackathon criteria](docs/HACKATHON_CRITERIA.md)
- [Submission checklist](docs/SUBMISSION_CHECKLIST.md)
- [Continuity rules](docs/CONTINUITY_RULES.md)
- [Decision log](docs/DECISIONS.md)
- [Execution ledger](docs/EXECUTION_LEDGER.md)

## Continuity Rule

Every work block must end by updating `docs/checkpoints/CHECKPOINT_CURRENT.md`.

A new chat, agent, or contributor should resume in this order:
1. read `docs/checkpoints/CHECKPOINT_CURRENT.md`;
2. read `docs/ROADMAP.md`;
3. inspect files and evidence referenced by the checkpoint;
4. verify that claimed repository state actually exists;
5. execute only the recorded next step or explicitly document a plan revision.

Repository status must distinguish **COMPLETED**, **PLANNED**, **BLOCKED**, and **UNVERIFIED** work. Planned work must never be presented as completed work.

## Security

Panta and AI credentials must remain server-side and must never be committed. `.env.example` contains placeholders only. External API responses are treated as untrusted input, and AI interpretation must never override structured provenance or deterministic calculations.

## Design and Implementation Planning

The approved foundation design is stored at:

`docs/superpowers/specs/2026-09-26-panta-signal-foundation-design.md`

The documentation-foundation implementation plan is stored at:

`docs/superpowers/plans/2026-09-26-documentation-foundation.md`

Documentation defines what should be built; it does not prove that the product has already been implemented, deployed, validated, or submitted.
