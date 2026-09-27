# CURRENT CHECKPOINT — Panta Signal

**Date:** 2026-09-27  
**Block:** 002 — Phase 1 authoritative validation  
**Overall state:** PHASE 0 MERGED / PHASE 1 IN PROGRESS / PRODUCT IMPLEMENTATION NOT STARTED  
**Branch:** `research/phase1-authoritative-validation-2026-09-27`

## COMPLETED

### Foundation integration

- Documentation foundation was reviewed through PR #1.
- PR #1 was merged into `main` on 2026-09-27.
- Merge commit: `152d1e143033829ae79ee07a6a41dcf604d41095`.
- Phase 0 is now complete on `main`; the previous "complete on review branch" state is obsolete.

### Phase 1 research branch

- Created `research/phase1-authoritative-validation-2026-09-27` from current `main`.

### Main Crypto World's Fair validation

Verified from current Colosseum sources and recorded in:

`docs/research/2026-09-27-crypto-worlds-fair-official-validation.md`

Verified facts include:

- contest period ends **October 12, 2026 at 11:59 PM PT**;
- registration and Project Submission must be completed by the cutoff;
- all submitted Content must be English;
- one team per entrant and one Project Submission per team at a time;
- judging criteria: Functionality, Potential Impact, Novelty, UX, Open-source, Business Plan;
- entrant IP remains with the entrant subject to third-party-rights obligations;
- main awards/opportunities and winner timing were separated from the Panta Sidetrack.

### Panta Sidetrack validation

Verified from the current sponsor listing/Panta-linked sources and recorded in:

`docs/research/2026-09-27-panta-sidetrack-api-validation.md`

Verified facts include:

- **5,000 USDG** Panta Sidetrack pool;
- 2,000 USDG first place and 1,000 USDG each for second through fourth;
- official Colosseum submission **plus** Panta Sidetrack submission on Superteam Earn;
- meaningful Panta API integration;
- working demonstration;
- English submission;
- judging on Panta API Integration, Technical Execution, Product & UX, Originality, Impact Potential, and Traction;
- scheduled Panta Sidetrack winner announcement: October 27, 2026.

### Panta public API contract validation

The sponsor-published API resources were inspected, including:

- `https://docs.panta.market/` as the published documentation URL;
- `Kaito-HQ/panta-api-playground`;
- `Kaito-HQ/panta-api-pub`, referenced by the playground as its public docs source.

The direct `docs.panta.market` site was not retrievable through the browsing tool in this block, so the inspectable published GitHub documentation/playground were used instead. This limitation is documented rather than guessed around.

Documented API facts now verified include:

- live base: `https://live-api.panta.market/api/v1`;
- staging base: `https://staging-api.panta.market/api/v1`;
- public signup/login -> JWT -> API-key creation flow;
- product routes accept `X-Api-Key` or Bearer JWT;
- `pk_test_…` and `pk_live_…` key prefixes;
- API secret shown once and must remain protected;
- API keys in URLs/query parameters are rejected;
- MVP-relevant read endpoints:
  - `GET /categories/`;
  - `GET /markets/`;
  - `GET /markets/{marketId}/`;
  - `GET /markets/{marketId}/trades/`;
- list pagination and documented maximums;
- market/trade timestamp and identifier fields;
- structured error envelope and default rate-limit families;
- mandatory **Powered by Panta** attribution;
- stale/cached data must not be represented as live;
- source context/attribution must be preserved;
- substantially unmodified raw Panta data must not be resold as a substitute for Panta without permission.

### Project documents updated

- `docs/HACKATHON_CRITERIA.md` now distinguishes VERIFIED, GAP, UNVERIFIED, and NOT REQUIRED items from real sources.
- `docs/ROADMAP.md` now records Phase 0 as merged and Phase 1 as partially complete.

## Evidence / Verification Performed

- Colosseum event page and official rules were read during this block.
- Relevant official-rules PDF pages for timing, registration/judging, English-content rules, and prizes were visually inspected as well as text-extracted.
- Current Panta Sidetrack sponsor listing was re-read with eligibility, submission, judging, prize, API-resource, and developer-support sections.
- Current public Panta API docs/playground repositories were inspected directly through GitHub.
- Public API docs commits show documentation updated during September 2026, including authentication/playground fixes.
- `quickstart.mdx`, authentication, markets list/detail/trades, errors/rate limits, and Terms of Use were inspected.

## Accepted Decisions

- Treat **October 12, 2026 at 11:59 PM PT** as the hard main-hackathon deadline.
- Until a distinct Panta Sidetrack cutoff is directly confirmed, do not plan later than the main deadline.
- Initial Panta Signal integration remains read-only: no market creation, buying, claims, wallet signing, custody, or capital movement.
- First ingestion contract should be based on categories, market list, market detail, market trade tape, and local snapshots.
- API keys remain server-side and must never enter client bundles, query strings, repository history, prompts, or logs.
- The UI must eventually include **Powered by Panta** attribution.
- Panta Signal must add analytical value and must not behave as a raw-data resale/mirror product.

## COMPLETED BUT NOT LIVE-VALIDATED

The API contract and authentication flow are documentation-verified, but no Panta account, JWT, test key, or live response was created/observed in this block.

Therefore the following are **not** claimed:

- successful live authentication;
- successful API-key creation;
- current effective account-level rate limits;
- live market payload shape;
- live spot-price availability;
- live trade-tape availability;
- actual response headers.

## UNVERIFIED / Open

### Phase 1 remaining

- live signup/login and `pk_test_…` creation;
- controlled live calls to categories, markets, one market detail, and one trade tape;
- exact current live response fields/nullability and rate-limit headers;
- exact Colosseum Arena submission-form fields/media requirements;
- exact Superteam Earn Panta submission-form fields/media requirements;
- whether the Panta Sidetrack has a distinct cutoff/time from the main hackathon deadline;
- operator-specific eligibility confirmation.

### Later architectural choices

- runtime/deployment provider;
- persistence provider/schema technology;
- exact internal market/snapshot/signal schemas;
- exact signal formulas and thresholds;
- related-market matching method;
- AI model/provider and tool interface;
- license.

## Account Creation and Legal Boundary

- On 2026-09-27, the operator explicitly accepted the Panta API Terms and authorized creating a free test account with the documented default `canCreateMarkets: true` capability. No registration or API credential has been created yet.
- Direct retrieval of `https://docs.panta.market/llms.txt` was unavailable through the current web retrieval tool. The official docs source repository's `docs.json` navigation was used as the complete page index instead; relevant auth, account, and Terms pages were read.
- The current Panta API Terms of Use say that obtaining API credentials or calling an endpoint constitutes agreement to the Terms. Registration returns JWT credentials. Stop before `POST /auth/register/` until the operator has reviewed the Terms and explicitly confirms acceptance immediately before the binding action.
- Registration requires an email and password. Do not request or handle the operator's password in chat; the account holder must enter it through a secure provider flow.
- The official docs state that new accounts default to `canCreateMarkets: true`. The documented account PATCH only changes the display name, and the API-key creation contract documents no permission scopes. Treat the created key/account as capable of broader write operations than this project's read-only probe; this is an unresolved least-privilege limitation.
- The API key's plaintext secret is returned only once. Do not ask the operator to paste it into chat. A secure execution-time secret handoff is still needed before authenticated GET validation.

## BLOCKED

Phase 2 schema freezing and product implementation are intentionally blocked until live read-only Panta responses are observed.

If no existing Panta credential is available, creating a new external Panta account/test credential is an account-creation side effect and should be explicitly authorized before execution.

## Risks

- Competition or sponsor requirements can change before October 12.
- Published API docs may differ from live behavior until tested.
- List endpoints explicitly do not live-RPC prices; a signal engine must not interpret null list prices as zero probabilities.
- API Terms require stale/delayed data labeling and source attribution.
- A high-frequency collector could exhaust account rate limits or create unnecessary operational load.

## Exact Next Step

**Finish Phase 1 with controlled live read-only validation.**

After a valid Panta test credential is available:

1. `GET /categories/`;
2. `GET /markets/?limit=5`;
3. select one returned market and call `GET /markets/{marketId}/`;
4. call `GET /markets/{marketId}/trades/?limit=10`;
5. record HTTP status, response fields, nullability, source timestamps, pagination cursor behavior, request/rate-limit headers, and errors if any;
6. do not retry aggressively and honor any `Retry-After`;
7. do not call write/trading/claim endpoints.

Only then freeze the first Phase 2 internal data contract.

## Operator Confirmation

Read-only research remains authorized. If completing the next step requires creating a new Panta account or credential, obtain explicit operator approval for that external account action first. No monetary-cost action is authorized by this checkpoint.

## Continuity

Resume with this file, then `docs/ROADMAP.md`, then the two 2026-09-27 research files. Planned or documentation-verified behavior must not be reported as live-tested behavior.
