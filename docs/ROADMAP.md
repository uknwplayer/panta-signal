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
- [ ] Resolve the observed API signup HTTP 403 with Panta; verify the API auth path and create a test key without committing credentials.
- [x] Inventory MVP-relevant read endpoints: categories, markets list, market detail, market trade tape.
- [x] Confirm documented pagination/limits, market identifiers, Unix timestamps, error envelope, rate-limit headers, and default limits.
- [x] Record Panta Terms constraints for credentials, attribution, stale data, caching/context, and raw-data resale.
- [ ] Execute controlled live read-only calls and record real response shapes/rate-limit headers.

### Evidence

- [x] Record main-hackathon authoritative research in `docs/research/2026-09-27-crypto-worlds-fair-official-validation.md`.
- [x] Record Panta Sidetrack/API research in `docs/research/2026-09-27-panta-sidetrack-api-validation.md`.
- [x] Update `docs/HACKATHON_CRITERIA.md` from verified evidence.

**Phase 1 state:** IN PROGRESS / API AUTH BLOCKED. Documentation-level external validation is substantially complete. On 2026-09-27 the authorized local signup attempt returned HTTP 403; no recovery JSON or API key is available. Website email/wallet sign-in works, but does not prove API authentication. Do not repeat the signup POST until the error path or an official alternative is established.

## Phase 2 — Technical Specification and Data Contracts

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

- [ ] Implement server-side Panta API client.
- [ ] Implement response validation.
- [ ] Normalize verified market fields.
- [ ] Preserve source identifiers/timestamps.
- [ ] Add API error and malformed-response tests.
- [ ] Verify no credentials reach client bundles or logs.

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

The operator posted the API signup question in #dev-chat; a reply visible in the operator-provided screenshot advises opening a support ticket. Follow that guidance without reposting the same details publicly. The cause remains unknown. Do not repeat the registration POST while waiting. The offline fixture validator is available with `python -m unittest discover -s tests -v`; use it while continuing UI/data work with synthetic fixtures only. Keep the docs-derived contract provisional and do not present fixtures as captured Panta payloads. Resume live validation only after obtaining a valid test credential; keep the probe small (categories, up to five markets, one detail, up to ten trades). Do not create markets, trade, sign transactions, claim funds, or freeze final schemas until live reads are evidenced.
