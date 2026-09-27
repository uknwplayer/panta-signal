# CURRENT CHECKPOINT — Panta Signal

**Date:** 2026-09-27  
**Block:** 009 — External API report corrected and recorded  
**Overall state:** PHASE 0 MERGED / PHASE 1 IN PROGRESS / OFFLINE FIXTURE VALIDATOR TESTED / PRIVATE SUPPORT TICKET OPEN / EXTERNAL API DEFECT REPORT RECORDED / LIVE API BLOCKED  
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
- `docs/ROADMAP.md` records Phase 0 as merged, the API-auth blocker, and provisional contract work.
- `docs/PROVISIONAL_DATA_CONTRACT.md` defines docs-derived normalized market/trade observation shapes and deferred decisions.
- Added synthetic fixtures under `fixtures/panta/v0-provisional/` for market list, market detail, and trade tape. They are explicitly marked synthetic and `liveValidated: false`; no live API response was captured.
- Added `panta_signal/contracts.py` and `tests/test_contracts.py`, using only Python's standard library, to validate the explicitly synthetic fixture contract.

## Evidence / Verification Performed

- TDD red/green check: the new seven-test suite first failed because the validator was absent; after implementation, `python -m unittest discover -s tests -v` passed all 7 tests.
- The test suite exercises the actual synthetic fixture files and rejects a live-validation claim, missing market identity, malformed decimal strings, and a trade linked to another market. No Panta API calls were made in this block.

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

The API contract remains documentation-verified, not live-validated. On 2026-09-27, the operator submitted the authorized registration through the local Termux script; Panta returned HTTP 403. A local existence-only check found no `registration-recovery.json` at the script's expected path. No API JWT or test key is available to the project. The exact server-side stage/error body was not captured, so remote account state is unverified. The website session is signed in by email/wallet and shows a profile, but this does not establish API authentication or key issuance.

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

- On 2026-09-27, the operator explicitly accepted the Panta API Terms and authorized creating a free test account with the documented default `canCreateMarkets: true` capability. A local signup attempt later returned HTTP 403; no API credential is available. The operator can sign into the Panta website by email/wallet, with a profile visible and wallet balance 0.00 USDC; that confirms a website session, not API credential issuance.
- Direct retrieval of `https://docs.panta.market/llms.txt` was unavailable through the current web retrieval tool. The official docs source repository's `docs.json` navigation was used as the complete page index instead; relevant auth, account, and Terms pages were read.
- The Panta API Terms previously reviewed and explicitly accepted state that obtaining API credentials or calling an endpoint constitutes agreement to the Terms. Registration returns JWT credentials. The operator's authorization to create a free test account remains in effect. The separate user-uploaded website Terms copy (last updated August 5, 2026) contains no support contact details; it may not be the same document/version as the API Terms, so retain the version distinction.
- Registration requires an email and password. Do not request or handle the operator's password in chat; the account holder must enter it through a secure provider flow.
- The official docs state that new accounts default to `canCreateMarkets: true`. The documented account PATCH only changes the display name, and the API-key creation contract documents no permission scopes. Treat the created key/account as capable of broader write operations than this project's read-only probe; this is an unresolved least-privilege limitation.
- The API key's plaintext secret is returned only once. Do not ask the operator to paste it into chat. A secure execution-time secret handoff is still needed before authenticated GET validation.

## BLOCKED

Live API authentication is blocked after the authorized `POST /auth/register/` attempt returned HTTP 403. The local recovery-file check returned `SEM_RECOVERY`; no API JWT or test key is available. Do not repeat signup attempts until the failure path is understood or an official alternative is confirmed.

Final schema freezing and live-dependent implementation remain gated on observed API responses. Documentation-derived provisional contracts, parsers, and clearly synthetic local fixtures may proceed, with no claim of live compatibility.

## Risks

- Competition or sponsor requirements can change before October 12.
- Published API docs may differ from live behavior until tested.
- List endpoints explicitly do not live-RPC prices; a signal engine must not interpret null list prices as zero probabilities.
- API Terms require stale/delayed data labeling and source attribution.
- A high-frequency collector could exhaust account rate limits or create unnecessary operational load.

## Official Support Route Found — Block 006

The Panta Sidetrack listing names **#dev-chat** in the Panta Discord for technical questions and integration support during the hackathon: https://superteam.fun/earn/listing/panta-api-side-track. Its listed Discord invite is https://discord.gg/M76nH6fUwc.

The operator posted the API question in #dev-chat and then opened private Discord channel #ticket-0160, as shown in two operator-provided screenshots from approximately 02:04–02:07 local time on 2026-09-27. The ticket bot acknowledged the issue and stated that a Panta team member would join shortly. This is an automated acknowledgement, not a technical answer. The cause remains unknown; no registration retry was made. Do not post credentials, wallet secrets, or private account details.

## Exact Next Step

**Wait for the Panta team response in private ticket #ticket-0160 for the signup 403. File the separate external API behavior report in a dedicated ticket, linking https://github.com/bisale24-ops/settlement-check and explicitly noting the three withdrawn claims. Continue offline work only with clearly labeled synthetic fixtures. Do not retry registration or call the quote POST until support clarifies the paths and effects.**

For any later live validation, after a valid Panta test credential is available:

1. `GET /categories/`;
2. `GET /markets/?limit=5`;
3. select one returned market and call `GET /markets/{marketId}/`;
4. call `GET /markets/{marketId}/trades/?limit=10`;
5. record HTTP status, response fields, nullability, source timestamps, pagination cursor behavior, request/rate-limit headers, and errors if any;
6. do not retry aggressively and honor any `Retry-After`;
7. do not call write/trading/claim endpoints.

Only after live read-only validation may the provisional data contract be promoted/frozen.

## Operator Confirmation

Read-only research and the free test-account creation remain explicitly authorized. No further registration retry is authorized by implication after the observed 403; first determine the correct recovery/support path. No monetary-cost, trading, wallet-signing, market-creation, or claim action is authorized.

## Continuity

Run the fixture checks with `python -m unittest discover -s tests -v`. Resume with this file, then `docs/ROADMAP.md`, then the provisional contract and the 2026-09-27 research files. Planned or documentation-verified behavior must not be reported as live-tested behavior.


## External API Report Correction — Block 009

Reviewed the operator-linked `bisale24-ops/settlement-check` README and recorded its corrections and seven reported API behaviors in the research note. The withdrawn statements about missing questions, invisible resolution criteria, and inferring UMA settlement from `sentToUma` are no longer treated as findings.

The README reports 13/100 sampled tradeable listings without Solana accounts, inconsistent complete/stripped cards, and seven API behaviors. These remain externally reported, not independently live-validated by Panta Signal. The quote endpoint item involves a POST; do not repeat it in this project until its reservation/session side effects are clarified.
