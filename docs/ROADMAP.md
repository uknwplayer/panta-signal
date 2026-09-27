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

**Phase 0 state:** COMPLETED on review branch `docs/foundation-2026-09-26`; merge/integration into `main` remains a separate review action.

## Phase 1 — Authoritative External Validation

- [ ] Revalidate official Panta hackathon/side-track requirements.
- [ ] Revalidate authoritative deadline, eligibility, judging criteria, and required submission artifacts.
- [ ] Read authoritative Panta API documentation.
- [ ] Validate authentication method and test-key flow without committing credentials.
- [ ] Inventory read-only market endpoints relevant to the MVP.
- [ ] Confirm rate limits, pagination, timestamps, identifiers, and error behavior.
- [ ] Record authoritative research evidence in `docs/research/`.

## Phase 2 — Technical Specification and Data Contracts

- [ ] Freeze internal market schema.
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

Begin Phase 1 with authoritative Panta/hackathon/API validation. Do not start product implementation from prior chat summaries or unverified API assumptions.
