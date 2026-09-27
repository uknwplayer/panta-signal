# Roadmap — Panta Signal

## Operating Rule

Every work block ends by updating `docs/checkpoints/CHECKPOINT_CURRENT.md`. Material milestones also receive a historical snapshot under `docs/checkpoints/history/`.

Status vocabulary:
- **COMPLETED** — verified work;
- **PLANNED** — intended work;
- **BLOCKED** — unresolved dependency;
- **UNVERIFIED** — insufficient evidence.

## Phase 0 — Documentation Foundation

- [x] Create public repository.
- [x] Approve foundation design.
- [x] Create documentation-foundation implementation plan.
- [x] Establish safe root configuration template and ignore rules.
- [x] Create README entrypoint.
- [x] Complete all core documentation.
- [x] Complete product/hackathon-specific documentation.
- [x] Create current and historical checkpoints.
- [x] Verify foundation links, status claims, and secret boundaries.
- [x] Merge reviewed documentation foundation into `main` through PR #1.

**Phase 0 state:** COMPLETED and merged into `main` on 2026-09-27 via merge commit `152d1e143033829ae79ee07a6a41dcf604d41095`.

## Phase 1 — Authoritative External Validation

### Competition / sidetrack

- [x] Revalidate official Colosseum Crypto World's Fair timing and controlling rules.
- [x] Revalidate main-hackathon eligibility framework, judging criteria, language rule, team/submission limits, and IP treatment.
- [x] Revalidate Panta API Sidetrack reward structure, eligibility, submission requirements, and judging criteria.
- [ ] Revalidate exact live Colosseum Arena submission-field/media checklist.
- [ ] Confirm whether the Panta Sidetrack has a distinct submission cutoff/time from the main hackathon deadline.
- [ ] Confirm operator-specific eligibility against the official rule set.

### Panta API

- [x] Read the published Panta public API documentation and playground contract.
- [x] Document live/staging API base URLs and documented authentication model.
- [x] Find and verify the official support route for the observed API signup HTTP 403 (#dev-chat in the Panta Discord).
- [x] Diagnose the direct Python-client 403 as Cloudflare Error 1010 on a credential-free GET to the register route (not proof of the original POST's exact response).
- [x] Complete the documented browser registration and test-key flow; registration and key creation returned HTTP 201, and authenticated account access returned HTTP 200.
- [x] Inventory MVP-relevant read endpoints: categories, markets list, market detail, market trade tape.
- [x] Confirm documented pagination/limits, market identifiers, Unix timestamps, error envelope, rate-limit headers, and default limits.
- [x] Record Panta Terms constraints for credentials, attribution, stale data, caching/context, and raw-data resale.
- [x] Execute controlled live read-only calls and record bounded response shapes for categories, list, detail, and the trade tape.
- [ ] Assess response rate-limit headers and effective account limits.

### Evidence

- [x] Record main-hackathon authoritative research in `docs/research/2026-09-27-crypto-worlds-fair-official-validation.md`.
- [x] Record Panta Sidetrack/API research in `docs/research/2026-09-27-panta-sidetrack-api-validation.md`.
- [x] Update `docs/HACKATHON_CRITERIA.md` from verified evidence.

**Phase 1 state:** IN PROGRESS / AUTHENTICATED READ-ONLY API ACCESS VERIFIED. The earlier Termux registration 403 and credential-free Cloudflare 1010 remain historical evidence. The documented browser flow later returned HTTP 201 for registration and test-key creation; authenticated account access and bounded GET reads succeeded. Provider smoke tests on Termux now pass for categories (HTTP 200, four categories), a one-item market list (HTTP 200, primary phase, cursor null/empty), matching market detail (HTTP 200), and the selected market's empty trade tape (HTTP 200, zero rows). Live coverage remains narrow: one listed market, no populated trade rows, no cursor advancement, and rate-limit headers/effective limits are not yet assessed.

## Phase 2 — Technical Specification and Data Contracts

- [x] Prototype an isolated, public-GET-only Polymarket Gamma reader for market lists and details; six offline tests use synthetic responses. Not live-validated and not wired into the product.
- [ ] Define a provider-neutral internal market record with explicit provider/source provenance before connecting alternate providers to the product.

- [x] Draft a documentation-derived provisional market/trade contract and three synthetic fixtures (`docs/PROVISIONAL_DATA_CONTRACT.md`, `fixtures/panta/v0-provisional/`).
- [x] Implement and test a standard-library validator for the explicitly synthetic fixtures (`panta_signal/contracts.py`, `tests/test_contracts.py`).
- [ ] Freeze internal market schema only after live response validation.
- [ ] Freeze snapshot schema.
- [ ] Freeze signal record schema.
- [ ] Define source/derived/AI provenance metadata in machine-readable contracts.
- [ ] Select runtime and persistence provider.
- [ ] Define API-client timeout, retry, caching, and stale-data policy.
- [ ] Produce implementation plan for ingestion and normalization.

## Phase 3 — Ingestion and Normalization

- [x] Implement bounded server-side Panta API client with GET-only routes.
- [x] Validate list/detail/trade response envelopes and handle sparse fields and empty trade arrays.
- [x] Preserve upstream identifiers and fields while adding provider, route, and observation-time provenance.
- [x] Keep the API key out of URLs, process arguments, client output, and error messages.
- [ ] Expand malformed-response and provider-error tests.
- [ ] Build local snapshot/ingestion flow around the verified provider methods.

## Phase 4 — Snapshots and Signal Engine

- [ ] Implement snapshot persistence.
- [ ] Implement probability movement.
- [ ] Implement movement velocity.
- [ ] Implement abnormal-change detection.
- [ ] Implement recency/persistence logic.
- [ ] Evaluate related-market divergence model.
- [ ] Freeze versioned composite Signal Score only after evaluation.
- [ ] Test missing/late/out-of-order snapshot behavior.

## Phase 5 — Dashboard and Internal API

- [ ] Build ranked signal view.
- [ ] Build market detail/evidence view.
- [ ] Add search and filters.
- [ ] Add watchlist capability if it fits the MVP time budget.
- [ ] Expose provenance and timestamps clearly.
- [ ] Add health/build-version visibility.

## Phase 6 — AI Analyst

- [ ] Define constrained analyst tool/data interface.
- [ ] Require structured evidence in responses.
- [ ] Prevent model output from mutating deterministic records.
- [ ] Add questions for market movers, categories, and signal explanations.
- [ ] Evaluate unsupported-claim behavior and prompt-injection resistance.

## Phase 7 — Public Deployment and Evaluation

- [ ] Select zero/minimal-cost deployment target.
- [ ] Deploy public application.
- [ ] Verify production secret handling.
- [ ] Verify public Panta-data flow.
- [ ] Run mechanical evaluation suite.
- [ ] Run demo/usability evaluation.
- [ ] Record incidents and limitations.

## Phase 8 — Hackathon Evidence and Submission

- [ ] Re-check all official submission requirements immediately before submission.
- [ ] Complete judging-criteria evidence matrix.
- [ ] Record public repository URL.
- [ ] Record working deployment URL.
- [ ] Produce screenshots/demo assets.
- [ ] Produce required video if applicable.
- [ ] Run final secret/reproducibility check.
- [ ] Submit only after every mandatory gate is evidenced.
- [ ] Record submission confirmation in execution ledger/checkpoint.

## Current Next Stage

Authenticated test credentials and bounded live reads are verified. The Panta provider has passed authenticated Termux smoke tests for categories, a one-page market list, one detail, and one empty trade tape. It preserves sparse fields, cursor presence/value, and empty trade arrays; the API key stays out of URLs and process arguments. The complete local suite passes 19 offline tests on Python 3.12.14; those tests use synthetic responses and a fake runner.

Next, proceed to local snapshot/ingestion design using only source-backed fields and explicit provenance. Broaden live samples when available, especially a populated trade tape and a nonempty cursor. Keep these coverage limits visible. No write routes are in scope.

### Development fallback prototype

A read-only Polymarket Gamma adapter now exists for development experiments while Panta API authentication is blocked. It makes one bounded list request or one detail request per call and does not fetch prices, trades, or order books. Do not treat it as Panta data or as a replacement for the Panta Sidetrack integration requirement. See `docs/POLYMARKET_PROVIDER.md`.
