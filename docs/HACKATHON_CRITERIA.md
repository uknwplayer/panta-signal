# Hackathon Criteria Traceability — Panta Signal

## Purpose

This document converts externally verified competition requirements into traceable product/repository/demo requirements.

Primary evidence is stored under `docs/research/` and should be rechecked before final submission.

## Status Vocabulary

- **VERIFIED** — confirmed from a current authoritative/controlling source and evidence recorded.
- **UNVERIFIED** — not yet sufficiently confirmed.
- **SATISFIED** — verified criterion with repository/demo evidence proving completion.
- **GAP** — verified criterion not yet satisfied.
- **NOT REQUIRED** — specifically not established as a mandatory requirement by the reviewed source, though it may still improve judging.

## Current Competition Context

Panta Signal targets:

1. the **Colosseum Crypto World's Fair** main hackathon; and
2. the separate **Panta API Sidetrack** submitted through Superteam Earn.

Submitting to the Panta Sidetrack does **not** replace the required Colosseum submission.

Current research evidence:

- `docs/research/2026-09-27-crypto-worlds-fair-official-validation.md`
- `docs/research/2026-09-27-panta-sidetrack-api-validation.md`

## Verified Main-Hackathon Facts

- Contest ends **October 12, 2026 at 11:59 PM PT**.
- All members must register by that cutoff.
- The team leader must upload the Project Submission before the end of the Entry Period.
- All submitted Content must be in **English**.
- Entrants may belong to only one team; a team may have only one Project Submission at a time.
- Main judging criteria are Functionality, Potential Impact, Novelty, UX, Open-source, and Business Plan.
- Colosseum does not claim ownership of entrant Project Submissions.

## Verified Panta-Sidetrack Facts

- Total reward: **5,000 USDG**.
- 1st: 2,000 USDG; 2nd–4th: 1,000 USDG each.
- Requires official Colosseum registration/submission **and** Panta Sidetrack submission on Superteam Earn.
- Requires meaningful Panta API integration.
- Requires a working demonstration.
- Requires an explanation of the product/problem and how Panta API is integrated.
- Submission must be in English.
- Sidetrack judging criteria: Panta API Integration, Technical Execution, Product & UX, Originality, Impact Potential, Traction.
- Sponsor listing schedules winner announcement for **October 27, 2026**.

## Traceability Matrix

| Criterion / requirement | Source status | Current project state | Evidence / target | Gap |
|---|---|---|---|---|
| Submit official Colosseum project before Oct 12, 2026 11:59 PM PT | VERIFIED | GAP | Final Colosseum submission confirmation | Product not built/submitted |
| Submit separately to Panta Sidetrack on Superteam Earn | VERIFIED | GAP | Final Superteam submission confirmation | Product not built/submitted |
| Meaningfully integrate Panta API | VERIFIED | GAP | Live Panta-backed data flow + technical explanation | Live API integration not implemented |
| Working demo or compelling prototype | VERIFIED | GAP | Public/usable demo flow | No implementation/deployment yet |
| Submission-facing content in English | VERIFIED | PARTIALLY SATISFIED | Repository/docs already English; final form/assets pending | Final assets not produced |
| Functionality / technical execution | VERIFIED | GAP | End-to-end tested application | No runtime yet |
| Product & UX quality | VERIFIED | GAP | Clear ranked-signal and evidence workflow | UI not implemented |
| Novelty / originality | VERIFIED | DESIGN SATISFIED, DEMO GAP | Prediction-market-as-information-sensor thesis + Signal Engine | Must prove in working product |
| Potential impact / real-world usefulness | VERIFIED | DESIGN SATISFIED, EVIDENCE GAP | Product thesis + evaluation/demo evidence | Usage/traction absent |
| Traction | VERIFIED for Panta Sidetrack | GAP | Real users/usage or credible early evidence | No users yet |
| Open-source quality/composability | VERIFIED as main judging criterion | PARTIALLY SATISFIED | Public repo + reproducible setup | Product code not yet present |
| Business viability / execution ability | VERIFIED as main judging criterion | GAP | Business model/narrative + functioning product | Business case not finalized |
| AI + Prediction Markets is an accepted build category | VERIFIED in Panta brief | DESIGN SATISFIED | AI Analyst design | AI Analyst not implemented |
| Trading & Analytics is an accepted build category | VERIFIED in Panta brief | DESIGN SATISFIED | Market Intelligence + Signal Engine | Product not implemented |
| Public repository strictly mandatory | NOT REQUIRED by reviewed controlling rules | Public repo already exists | `uknwplayer/panta-signal` | Keep public unless rules change |
| Public deployment strictly mandatory | UNVERIFIED | Planned | Deployment URL | Working demo is required; exact hosting/public-access wording still to be checked |
| Specific video format/duration required | UNVERIFIED | Not produced | Final Arena/Superteam form | Inspect live forms before submission |
| Exact Panta Sidetrack deadline/time if distinct from main deadline | UNVERIFIED | Operationally use main cutoff | Sponsor listing + direct confirmation if available | Treat Oct 12 11:59 PM PT as hard stop until clarified |
| Operator-specific eligibility | UNVERIFIED | Pending check | Official eligibility rules + operator confirmation | Rule verified; personal applicability not asserted here |
| Panta reward/payout terms | VERIFIED at prize-structure level | N/A | Sponsor listing | Tax/payment logistics only matter if selected |
| Main-event prize pool / accelerator opportunity | VERIFIED | N/A | Colosseum event page/rules | Not a product acceptance criterion |

## Product Decisions Driven by Verified Criteria

Panta Signal should optimize for:

- a working product rather than a static mockup;
- meaningful use of live Panta data;
- clear differentiation from a raw market catalog;
- deterministic, explainable signals;
- visible source provenance and freshness;
- a useful, intuitive demo flow;
- an open-source/reproducible implementation;
- a credible business/use-case narrative;
- early usage evidence if feasible before submission;
- a concise English explanation of how Panta powers the product.

## Panta-Specific Compliance Requirements

The public Panta API Terms add product constraints that must be treated as acceptance criteria:

- display **Powered by Panta** with required visibility/association;
- keep API credentials protected and server-side;
- do not present stale/cached/simulated data as live;
- preserve source attribution/material context;
- do not bypass rate limits or access controls;
- do not simply resell substantially unmodified raw Panta data as a substitute for Panta's service.

These requirements reinforce Panta Signal's differentiation: the product must create real analytical value on top of Panta source data.

## Remaining Verification Gates

Before final submission, recheck:

1. the live Colosseum Arena submission form and required fields;
2. the live Superteam Earn Panta Sidetrack submission form;
3. exact video/screenshot/link requirements;
4. whether the Panta Sidetrack has a distinct cutoff from the main hackathon;
5. any rule or Terms changes after 2026-09-27;
6. operator-specific eligibility.

## Next Step

Complete live **read-only** API validation with a valid Panta test credential. Do not freeze the internal data contract until real `/categories/`, `/markets/`, market-detail, and trade-tape responses have been observed and recorded.
