# Hackathon Criteria Traceability — Panta Signal

## Purpose

This document converts externally verified competition requirements into traceable product/repository/demo requirements.

**Important:** No hackathon criterion in this file is authoritative until it is revalidated from a current primary source and linked in `docs/research/`.

## Status Vocabulary

- **VERIFIED** — confirmed from a current authoritative source and evidence recorded.
- **UNVERIFIED** — known/suspected from prior research or conversation but not freshly confirmed in this repository work block.
- **SATISFIED** — verified criterion with repository/demo evidence proving completion.
- **GAP** — verified criterion not yet satisfied.

## Current Competition Context

Panta Signal is being designed for a Panta-focused prediction-market build opportunity and a broader hackathon context previously identified during project research.

Current authoritative details such as exact prize amounts, deadline, eligibility, judging weights, required links, submission fields, and cross-submission rules are **UNVERIFIED** in this repository and must be revalidated before implementation decisions depend on them.

## Traceability Matrix

| Criterion / requirement | Source status | Product capability | Repository evidence | Demo evidence | Current gap |
|---|---|---|---|---|---|
| Build a product using Panta data/API | UNVERIFIED | Server-side Panta ingestion + market intelligence | Architecture / Product Spec | Live Panta-backed dashboard | Authoritative API/competition rule not yet recorded; implementation not started |
| Original/useful product rather than raw API wrapper | UNVERIFIED | Signal Engine + explainable intelligence | Whitepaper / Signal Engine | Ranked signals with evidence | Implementation/evaluation pending |
| AI integration recognized/valuable | UNVERIFIED | Grounded AI Analyst | Product Spec / Security / Evaluation | Natural-language analysis with supporting records | Provider/interface not selected |
| Public working application required | UNVERIFIED | Deployable web product | Roadmap / Operations | Public HTTPS URL | Runtime/provider not selected; not deployed |
| Public/source repository required | UNVERIFIED | Public GitHub repository | `uknwplayer/panta-signal` | Repository link | Requirement itself needs authoritative verification |
| Demo/video required | UNVERIFIED | Demo-ready product flow | Submission Checklist | Video/demo asset | Exact format/duration not verified |
| Judging values product quality/UX | UNVERIFIED | Dashboard + clear evidence/provenance | Product Spec / Evaluation | Fast understandable demo flow | Exact judging language/weight not verified |
| Judging values originality/impact | UNVERIFIED | Prediction-market-as-information-sensor thesis | Whitepaper | Differentiated signal workflow | Exact judging language/weight not verified |
| Submission deadline | UNVERIFIED | Delivery schedule | Roadmap | Submission confirmation | Must verify authoritative date/time/timezone |
| Eligibility / geographic rules | UNVERIFIED | Operator eligibility | Research evidence | N/A | Must verify authoritative rules |
| Prize / payout terms | UNVERIFIED | N/A | Research evidence | N/A | Must verify exact current amounts/currency/conditions |
| Cross-entry into broader event | UNVERIFIED | Same product may be eligible | Research evidence | Submission records | Must verify current rules and duplicate/cross-submission policy |

## Verification Procedure

For each external criterion:
1. locate the current authoritative source;
2. record source title, URL, access date, and relevant rule in `docs/research/`;
3. update this table from `UNVERIFIED` to `VERIFIED`;
4. map the rule to product/repository/demo evidence;
5. mark it `SATISFIED` only after the evidence actually exists.

## Design Implications Already Approved Internally

Regardless of external judging rules, Panta Signal currently optimizes for:
- a complete end-to-end product rather than a static mockup;
- clear differentiation from a generic market dashboard;
- deterministic and explainable signals;
- visible Panta/source provenance;
- useful AI integration grounded in structured evidence;
- a public reproducible repository;
- a concise demo path.

These are internal product choices, not claims about official judging criteria.

## Next Step

Phase 1 must revalidate the official competition page(s), Panta API documentation, eligibility, deadline, judging criteria, submission requirements, and prize/cross-submission rules before this document is used as an authoritative submission checklist.
