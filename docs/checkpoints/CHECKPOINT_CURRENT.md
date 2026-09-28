# CURRENT CHECKPOINT — Panta Signal

**Date:** 2026-09-27  
**Block:** 042 — Sparse onChain consumer classifier implemented  
**Overall state:** PHASE 0 MERGED / PHASE 1 LIVE ROUTES VALIDATED ON A NARROW SAMPLE / READ-ONLY PANTA PROVIDER IMPLEMENTED / VERSIONED JSONL SNAPSHOT LIBRARY AND SINGLE-READ CLI IMPLEMENTED / 34 OFFLINE TESTS PASS / SAME MARKET: LIST onChain OMITTED, DETAIL onChain NULL
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

## Historical status at end of Block 011 — superseded in part by Block 012

The statements below accurately record Block 011. Block 012 subsequently verified test authentication and one list/detail pair; see the current status and Block 012 section below.


The API contract remains documentation-verified, not live-validated. On 2026-09-27, the operator submitted the authorized registration through the local Termux script; Panta returned HTTP 403. A local existence-only check found no `registration-recovery.json` at the script's expected path. No API JWT or test key is available to the project. The exact server-side response body for that POST was not captured, so remote account state is unverified. A later no-credential GET to the same route produced Cloudflare Error 1010; this is evidence of a client-signature block in the research environment, not a captured response to the original POST. The website session is signed in by email/wallet and shows a profile, but this does not establish API authentication or key issuance.

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

- on-device smoke test of the new `PantaReadClient` with the locally stored test key;
- representative samples across multiple markets, including at least one populated trade tape where available;
- cursor advancement when the live catalog returns a nonempty cursor;
- current effective account-level rate limits and response headers;
- exact Colosseum Arena and Superteam Earn submission-form fields/media requirements;
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

The first Termux signup attempt returned HTTP 403, as recorded in the historical entries below. That status was superseded in Block 012: the documented browser flow returned HTTP 201 for registration and key creation, and authenticated read-only calls succeeded. The test key is active, stored on the operator's device, and reported `canCreateMarkets: true`.

- On 2026-09-27, the operator explicitly accepted the Panta API Terms and authorized creating a free test account with the documented default `canCreateMarkets: true` capability. The website session and API credential flow are now separately validated; see Block 012 for the bounded API evidence.
- Direct retrieval of `https://docs.panta.market/llms.txt` was unavailable through the current web retrieval tool. The official docs source repository's `docs.json` navigation was used as the complete page index instead; relevant auth, account, and Terms pages were read.
- The Panta API Terms previously reviewed and explicitly accepted state that obtaining API credentials or calling an endpoint constitutes agreement to the Terms. Registration returns JWT credentials. The operator's authorization to create a free test account remains in effect. The separate user-uploaded website Terms copy (last updated August 5, 2026) contains no support contact details; it may not be the same document/version as the API Terms, so retain the version distinction.
- Registration requires an email and password. Do not request or handle the operator's password in chat; the account holder must enter it through a secure provider flow.
- The official docs state that new accounts default to `canCreateMarkets: true`. The documented account PATCH only changes the display name, and the API-key creation contract documents no permission scopes. Treat the created key/account as capable of broader write operations than this project's read-only probe; this is an unresolved least-privilege limitation.
- The API key's plaintext secret is returned only once. Do not ask the operator to paste it into chat. A secure execution-time secret handoff is still needed before authenticated GET validation.

## BLOCKED AT END OF BLOCK 011 — SUPERSEDED IN PART BY BLOCK 012

The signup/authentication block was resolved through the documented browser flow during Block 012. Earlier diagnostic details below remain historical evidence only.

Live API authentication remains blocked. The earlier authorized `POST /auth/register/` returned HTTP 403, but its response body was not captured. A later credential-free Python urllib `GET` to the same route returned Cloudflare Error 1010 (`browser_signature_banned`) with Ray ID `a41be3f04849fafa-ORD` at `2026-09-27T16:29:59Z`; this points to a Cloudflare edge/browser-signature block for that client but does not prove the earlier POST was blocked identically. The official Panta Quickstart documents a Register-page Try it playground with proxy mode enabled. Use this documented path next; do not retry the direct Termux POST. If the official playground is blocked too, send the Ray ID and timestamp to Panta support for an owner-side fix.

Final schema freezing and live-dependent implementation remain gated on observed API responses. Documentation-derived provisional contracts, parsers, and clearly synthetic local fixtures may proceed, with no claim of live compatibility.

## Risks

- Competition or sponsor requirements can change before October 12.
- Published API docs may differ from live behavior until tested.
- List endpoints explicitly do not live-RPC prices; a signal engine must not interpret null list prices as zero probabilities.
- API Terms require stale/delayed data labeling and source attribution.
- A high-frequency collector could exhaust account rate limits or create unnecessary operational load.

## Official Support Route Found — Block 006

The Panta Sidetrack listing names **#dev-chat** in the Panta Discord for technical questions and integration support during the hackathon: https://superteam.fun/earn/listing/panta-api-side-track. Its listed Discord invite is https://discord.gg/M76nH6fUwc.

The operator posted the API question in #dev-chat and then opened private Discord channel #ticket-0160, as shown in two operator-provided screenshots from approximately 02:04–02:07 local time on 2026-09-27. The ticket bot acknowledged the issue and stated that a Panta team member would join shortly. This is an automated acknowledgement, not a technical answer. The exact cause of the original POST remains unconfirmed; no registration POST retry was made. Do not post credentials, wallet secrets, or private account details.

## Exact Next Step

Smoke-test the new read-only Panta provider from the operator's Termux after checking out this research branch. Start with `get_categories()`, then test one market-list request and one detail request. Use the test key from a local environment variable or private file; print only success/count and sanitized errors. Do not display the key or raw account/market identifiers. Keep live compatibility partial until the new client is smoke-tested and representative data is available.

## Operator Confirmation

Read-only research, free test-account creation, and bounded read-only API validation remain explicitly authorized. Credentials stay on the operator's device and out of chat. The next block is a local smoke test of the new GET-only Panta provider. No monetary-cost, trading, wallet-signing, market-creation, quote, or claim action is authorized.

## Continuity

Run the fixture checks with `python -m unittest discover -s tests -v`. Resume with this file, then `docs/ROADMAP.md`, then the provisional contract and the 2026-09-27 research files. Planned or documentation-verified behavior must not be reported as live-tested behavior.


## External API Report Correction — Block 009

Reviewed the operator-linked `bisale24-ops/settlement-check` README and recorded its corrections and seven reported API behaviors in the research note. The withdrawn statements about missing questions, invisible resolution criteria, and inferring UMA settlement from `sentToUma` are no longer treated as findings.

The README reports 13/100 sampled tradeable listings without Solana accounts, inconsistent complete/stripped cards, and seven API behaviors. These remain externally reported, not independently live-validated by Panta Signal. The quote endpoint item involves a POST; do not repeat it in this project until its reservation/session side effects are clarified.


## Read-only Polymarket development prototype — Block 010

An isolated standard-library client was added on this research branch at `panta_signal/providers/polymarket.py`. It uses only public HTTP GET requests to Gamma API market keyset listing and market detail routes. List calls are limited to one page (1–20 records) and never auto-fetch another page. Normalized output labels `provider: polymarket`, source route, observation time, condition id, question, and outcome token IDs when provided. Missing values are not synthesized. No prices, trades, order books, wallet, signing, order, or transaction features are implemented.

Six new offline tests use synthetic Polymarket-like responses. The available local test suite passed all 13 tests (the existing seven synthetic Panta contract tests plus the six new provider tests). These results do not establish live compatibility. A direct API read was not completed: the browsing tool could not access the Gamma API host. The code is not wired into application flows and does not fulfill the Panta Sidetrack's meaningful Panta API integration requirement.

Added `docs/POLYMARKET_PROVIDER.md` to state scope, status, and exclusions. README and roadmap distinguish this development fallback from the blocked Panta integration. No changes were made to `main`; the prototype and documentation updates are on `research/phase1-authoritative-validation-2026-09-27`.

### Next

Keep the Panta signup 403 and support ticket #ticket-0160 open without retrying registration. For product development, define a provider-neutral market record with source provenance before connecting any provider; keep the Panta contract provisional until authenticated live reads are available. Continue using synthetic fixtures for offline work and keep this Polymarket prototype isolated until its live schema can be checked safely.


## Cloudflare 1010 registration diagnostic — Block 011

Current official sources were rechecked through Panta's published docs repository: the Quickstart explicitly offers **Try it** on Register and Create API key pages, and the published docs configuration sets the interactive playground to proxy mode. This is the supported alternative to direct Termux registration to try next.

A credential-free Python `urllib` `GET` to `https://live-api.panta.market/api/v1/auth/register/` returned HTTP 403 with Cloudflare JSON `error_code: 1010`, `error_name: browser_signature_banned`, at `2026-09-27T16:29:59Z`; Ray ID `a41be3f04849fafa-ORD`. The API base `GET /api/v1/` timed out. No registration POST, login, key creation, quote, or wallet action was made in this diagnostic.

Cloudflare's official Error 1010 guidance says the site owner blocked access based on the client/browser signature and directs visitors to notify that owner. The GET strongly suggests a Python-client/browser-signature rule at the edge, but the earlier Termux POST's error body was not recorded, so the two responses must not be represented as identical. Research note: `docs/research/2026-09-27-cloudflare-1010-api-registration.md`.

### Next action

The operator should use the Register-page Try it flow in their HTTPS browser and enter credentials directly there. If registration succeeds, store tokens on-device and proceed to Create API key using the documented interface. If the email is already registered, use the Token/login endpoint. If the official playground returns 1010, provide support with the Ray ID and timestamp and request an owner-side allow/adjustment or another supported API-client route. Do not spoof browser signatures or repeatedly POST through Termux.


## Block 012 — Live Panta Authentication and Read-only Calls

The operator completed the documented account and test-key flow: registration and key creation each returned HTTP 201. A read-only `GET /account/` returned HTTP 200 with an active test key, `canCreateMarkets: true`, and a key ID present. The secret remains on the operator's device.

A bounded `GET /markets/?limit=1` returned HTTP 200 with one item and no `nextCursor` field in that invocation. The corresponding detail request returned HTTP 200 with a matching `marketId`. The sampled detail fields included `onChain` and omitted `question`, `resolutionRule`, `sources`, and `totalTrades`. This is one sample only; it does not establish a global response shape or pagination defect. The externally reported catalogue findings remain unverified by this project.

No credentials, email, user ID, market ID, or raw response were saved to the repository. No write, quote, trading, claim, wallet-signing, or monetary action was performed. See `docs/checkpoints/history/CHECKPOINT_2026-09-27_012.md`.

### Next

Make bounded read-only calls to categories and the selected market's trade tape, then repeat one small list read to investigate cursor behavior. Record statuses, counts, field names, and cursor presence without exposing identifiers or secrets.


## Block 013 — Isolated GET Statuses

A standalone `GET /categories/` through Termux `curl` returned HTTP 200. A standalone `GET /markets/?limit=2` through `curl` returned HTTP 200 with one item and a `nextCursor` field. The cursor value was not printed and may be null/empty; cursor-based page movement remains unverified.

A previous combined probe using Python `urllib` ended with HTTP 403 before per-request results were reported. The categories and list calls have now succeeded via `curl`; a client-dependent difference is plausible, but the exact failed request/cause has not been established. Avoid Python `urllib` for further probes; use `curl` while keeping the secret read from the local file.

See `docs/checkpoints/history/CHECKPOINT_2026-09-27_013.md`. Next: inspect cursor truthiness and test one market trade-tape GET with curl.


## Block 014 — Market Cursor Value

A bounded `GET /markets/?limit=2` returned HTTP 200 with one item. The response included `nextCursor` with a null value (`cursor_field=True`, `cursor_nonempty=False`, `cursor_type=NoneType`). This response provides no next-page token. It does not reproduce the reported pagination defect because no next page can be requested from this response.

The result is recorded in `docs/checkpoints/history/CHECKPOINT_2026-09-27_014.md`. Next: make one bounded catalog read with `limit=50`, reporting only total count, phase counts, and whether `nextCursor` is nonempty.


## Block 015 — Trade Tape Read

A matching market-list bootstrap returned HTTP 200 with one item. The selected market's `GET /markets/{marketId}/trades/?limit=10` returned HTTP 200 with zero items. This confirms access to the trade-tape route and an empty result for that market. No trade-row fields can be inferred from an empty array, and trade pagination remains unverified.

The result is recorded in `docs/checkpoints/history/CHECKPOINT_2026-09-27_015.md`. Next: one `GET /markets/?limit=50` read to report total item count, phase counts, and cursor truthiness only.


## Block 016 — Bounded Live Read Set Complete

The operator reported `GET /markets/?limit=50` returned HTTP 200 with one item, phase `primary`, and no nonempty cursor. Across the bounded live checks, categories, list, matching detail, and trade-tape routes returned HTTP 200. The sampled detail included `onChain` and omitted `question`, `resolutionRule`, `sources`, and `totalTrades`; the sampled trade tape returned zero items.

This is a narrow sample, not a statement about the full catalogue. It does not validate pagination advancement, populated trade-row fields, or optional-field variation across multiple markets. See `docs/checkpoints/history/CHECKPOINT_2026-09-27_016.md`.

Next block: implement the read-only Panta provider with sparse-field and empty-trade handling; do not add write routes.


## Block 017 — Read-only Panta Provider Implemented

Added `panta_signal/providers/panta.py` with GET-only methods for categories, a bounded single market-list page, market detail, and trade tape. It uses cURL with configuration supplied through stdin, keeps the key out of the URL and process arguments, and allows only Panta live/staging API bases. Limits are enforced; pagination is caller-controlled. Market fields are preserved as received with `presentFields`; omitted values are not invented. Empty trade arrays are accepted.

Added `tests/test_panta.py` with six synthetic-response tests. The complete local test suite passed 19 tests on Python 3.12.14. These are offline tests using a fake subprocess runner; the new provider has not made a live API request. Operator-run cURL calls separately validated route access, with limited samples as described above.

Documentation: `docs/PANTA_PROVIDER.md`, `docs/PROVISIONAL_DATA_CONTRACT.md`, `docs/ROADMAP.md`, and history file `docs/checkpoints/history/CHECKPOINT_2026-09-27_017.md`.

### Next

Run a one-call smoke test of `PantaReadClient.get_categories()` from Termux after checking out this branch. Read the test key only from the device-local file/environment and print no secret. Then smoke-test list and detail. Keep compatibility marked partial until these new client calls and broader samples are verified.


## Block 018 — Termux cURL Configuration Diagnostic

The operator's first provider smoke test failed before receiving an HTTP response: Termux cURL exited with status 2 and reported unsupported trailing garbage while processing `--config`. A minimal read-only request using `curl -q --config -` then returned HTTP 401 without an API key. This confirms that the cURL configuration was parsed and the request reached the API; 401 is expected for this unauthenticated diagnostic and does not validate the provider's authenticated call.

Updated the provider to pass `-q` as cURL's first argument, preventing user-level `.curlrc` settings from interfering. Updated the request-construction test to assert this behavior. The complete offline suite passes all 19 tests on Python 3.12.14. Commit: `b7db7668d1a4660ade05ab2e13bfac4be3773904`.

### Next

Pull the research branch in Termux, then repeat the sanitized `get_categories()` smoke test with the device-local test key. Report only success/count or the sanitized error. Keep live-client compatibility partial until that authenticated call succeeds.


## Block 019 — Minimal Termux cURL Configuration

The operator ran a bounded authenticated GET to `/categories/` using cURL with only the URL and `X-Api-Key` header in its stdin config and returned `exit=0, HTTP 200`. This confirms the device-local key and authenticated route work with the minimal cURL configuration.

The provider still failed when its config also held request, timeout, quiet/error, and write-out options. The exact individual directive was not isolated; the evidenced incompatibility is in the extra cURL config content. Updated the client to keep only URL and headers in stdin config and pass non-secret GET, timeout, output, and status-marker options as cURL arguments. The key remains out of process arguments. Updated its synthetic request test and provider documentation. The full local suite passes all 19 tests on Python 3.12.14.

### Next

Pull the latest research branch and rerun the sanitized `PantaReadClient.get_categories()` smoke test from Termux. If it succeeds, record the returned count and proceed to the bounded list and detail smoke tests. If it fails, report the sanitized error; the current generic transport message still does not expose cURL stderr.


## Block 020 — Authenticated Provider Categories Smoke Test

After pulling the latest research branch on Termux, the operator ran the updated `PantaReadClient.get_categories()` with the local test key. It returned `categories HTTP 200 count 4`. This is the first successful authenticated live call made through the project provider. The previously recorded Termux `curl` list/detail/trade results remain separate manual probes.

The provider status remains partial: only its categories method has been smoke-tested live. The provider's market-list and market-detail methods still need bounded smoke tests. Existing offline suite status remains 19 passing tests on Python 3.12.14.

### Next

Using the same updated checkout and local environment key, call `list_markets(limit=2)`. Print only HTTP success, item count, cursor-present/nonempty booleans, and the selected market's phase. If at least one item exists, call `get_market(marketId)` for the first item and print only whether IDs match and the field names. Do not print the market ID, title, raw response, or key.


## Block 021 — Authenticated Provider List and Detail Smoke Tests

The operator ran the updated `PantaReadClient` in Termux with the local test key. `list_markets(limit=2)` returned HTTP 200 with one item. The page reported `cursorPresent=true` and an empty cursor; its first item was phase `primary`. A subsequent `get_market()` returned HTTP 200 and its `marketId` matched the selected list item. The output included the actual detail field names without printing an identifier, title, or raw payload.

Together with Block 020, the provider's categories, one-page list, and market-detail methods now have successful authenticated live smoke tests. The provider's trade method still needs an on-device smoke test. Catalog coverage remains a one-item sample; the empty cursor does not exercise cursor advancement. Offline tests remain 19 passing tests.

### Next

Repeat the small list bootstrap and call `get_trades(market_id, limit=10)` for its first item. Print only list status/count and trade status/count/field names; do not print IDs, titles, raw trade rows, or the key. The previous standalone cURL call to this route returned HTTP 200 with zero items, so an empty tape is an expected possible result.


## Block 022 — Authenticated Provider Trade Smoke Test

The operator reran the bounded list bootstrap and called `PantaReadClient.get_trades(market_id, limit=10)` for its first item. The list returned HTTP 200 with one item; the trade call returned HTTP 200 with zero trades and response fields `disclaimer`, `items`, and `marketId`. This confirms the updated provider's authenticated trade route and empty-array handling. It does not validate populated trade-row fields.

All four provider methods (categories, list, detail, trades) have now passed authenticated Termux smoke tests. The sample remains narrow: one primary market, no usable cursor, one empty trade tape, and no rate-limit-header assessment. The 19-test offline suite remains green. The roadmap now marks authentication and provider implementation as verified and points to snapshot/ingestion design.

### Next

Begin the local snapshot/ingestion block: review the existing provisional contract and validator, then define the smallest source-faithful snapshot record and storage format before adding any persistence. Keep observed source values distinct from derived signals and synthetic fixtures. Do not add write routes or infer populated-trade behavior from the empty tape.


## Block 023 — Provisional Snapshot Record Defined

Reviewed docs/PROVISIONAL_DATA_CONTRACT.md, panta_signal/contracts.py, and the Panta client contract. The existing validator only checks explicitly synthetic fixtures; it is not a live-response validator. The client retains source market objects and trade rows while adding provenance metadata and adapting endpoint envelopes, so stored client observations must not be called byte-for-byte raw API captures.

Defined a provisional snapshot envelope (recordType: panta-read-snapshot, snapshotVersion: 1, response) and UTF-8 JSONL as the local storage format. One complete list page, detail response, or trade-tape response is one append-only line. Source values, omitted fields, nulls, array ordering, and route query parameters stay intact; derived signals remain separate. This is a design only: no persistence code or live payload was added. Upstream schema freezing remains deferred because live coverage is one market and one empty trade tape.

### Next

Implement a small offline-tested JSONL snapshot writer/reader that validates only the versioned local envelope and round-trips provider observations without rewriting them. Keep it separate from the synthetic fixture validator and do not add signal derivation or automatic live polling yet.


## Block 024 — JSONL Snapshot Library Implemented

Added panta_signal/snapshots.py with a versioned panta-read-snapshot envelope, one-record-per-line UTF-8 JSONL append, ordered reading, envelope/version checks, and minimal Panta provenance checks. The response object is wrapped without mutation; market and trade schemas are not normalized or validated by this module. Malformed JSON and invalid envelopes report the line number. The library has no network behavior and is not wired to polling or a CLI.

Added eight offline tests for sparse/null observations, unchanged decimal-like strings, append/read round trips, invalid version/type/provenance, malformed lines, and empty files. The full suite passed: 27 tests. Tests use synthetic data only; no live payload was persisted and no live API call was made. Updated the provisional contract, provider docs, and roadmap. Upstream payload schema remains provisional.

### Next

Add a small explicit ingestion command that performs one bounded read at a time and appends its provider result through this library, with no scheduler or automatic page traversal. Keep test-key configuration device-local and do not commit secrets or captured live payloads.


## Block 025 — Explicit One-Read Snapshot CLI Implemented

Added panta_signal/snapshot_cli.py with list, detail, and trades commands. Each invocation makes exactly one bounded provider call and appends one versioned JSONL record. List limits are capped at 50, trade limits at 200, and each page is caller-controlled. The CLI reads PANTA_API_KEY from the environment, does not accept a key argument, and defaults snapshots to ~/.local/share/panta-signal/snapshots.jsonl outside the repository. No scheduler, automatic cursor traversal, category snapshot, or write endpoint is included.

Added CLI tests for one-call dispatch, snapshot append, key-required behavior, error handling without key output, default storage location, and pre-network limit bounds. The complete offline suite passed 34 tests on Python 3.12.14. Updated README, provider guide, roadmap, and this checkpoint. No live API call or payload persistence was performed in this block. The CLI itself still needs one Termux smoke test.

### Next

In Termux, pull this research branch and run one bounded list snapshot using the device-local test key. Keep the key out of chat and terminal output. Verify only the success message and line count; do not print or share the JSONL contents. Report the command status and record count, then stop before adding automatic polling or pagination.


## Block 026 — Termux Snapshot CLI Smoke Test

The operator pulled the research branch on Termux and ran panta_signal.snapshot_cli list with limit 2. The command reported that one Panta list snapshot was saved under ~/.local/share/panta-signal/snapshots.jsonl. A separate local check reported the file exists and contains exactly one JSONL record.

This confirms one bounded list request completed through the CLI and its result was persisted on the operator's device. The screenshot did not expose the stored response contents, market ID, or API key; no live snapshot was uploaded or committed to the repository. It is a single sample and does not establish broader catalogue coverage, cursor advancement, populated trades, or signal validity. The 34-test offline suite remains green.

### Next

Use panta_signal.snapshots.iter_snapshots on the device to inspect only a sanitized summary of the local record (record count, provider, and item count), without printing the record or identifiers. Then decide whether to make one additional bounded detail or trade-tape read for the same market. Keep all snapshots device-local.


## Block 027 — Termux JSONL Reader Verified

After the list CLI smoke test, the operator ran the project snapshot reader against the local file and reported only: records 1, provider panta, items 1. This confirms that the saved record can be read and summarized by the implementation on-device. No market identifier or snapshot contents were shared.

### Next

Use the market identifier already stored in the local list snapshot to run exactly one CLI detail read. Keep the identifier and response local. Report only the success message and the updated record count.


## Block 028 — Termux CLI Detail Read

After the list snapshot and local reader check, the operator ran the detail CLI command using the market ID from the device-local list snapshot. The subsequent JSONL count was 2, up from 1, confirming the detail observation was appended. The market ID and response were not shared. No snapshot was committed to the repository.

### Next

Run one bounded CLI trade-tape read for the same market, obtaining its ID from the most recent local JSONL record without printing it. Report only whether the CLI saved the record and the updated line count. Keep all snapshot contents and identifiers on-device.


## Block 029 — Termux CLI Trades Read

Following the successful list and detail commands, the operator ran the bounded CLI trades command. The local JSONL record count increased from 2 to 3, indicating a third snapshot was appended. The operator did not share the market identifier or stored response. The current Termux checkout has now exercised all three CLI read modes: list, detail, and trades.

This verifies command dispatch and append behavior on the device for the three route types. It does not establish whether the latest tape was empty or populated because no row count was reported. The existing separate Panta provider probe returned an empty tape, but this CLI record is not independently characterized. No snapshot was committed.

### Next

Read all three device-local records with panta_signal.snapshots.iter_snapshots and print only counts by route class (list/detail/trades) and the trade-row count. Keep IDs and response payloads private. Do not infer movement or trade-based signals from this one-market, three-call sample.


## Block 030 — Three Snapshot Records Summarized

The operator read all three local JSONL records through the snapshot reader and reported only aggregate metadata: three records with one list, one detail, and one trades response; the trade-row count is zero. This confirms the three route types can be read from the stored file. No market ID, price, title, or raw response was shared.

The observed trade tape remains empty. No trade-based calculation is possible from this sample. The one-market records also do not establish probability movement, which requires repeated observations of the same source price field at different times.

### Next

Inspect the saved list/detail snapshots locally and report only price-related field names, JSON types, and whether values are null or present. Do not print numeric values or identifiers. Then confirm that a price field is available across repeated list observations before designing a movement signal.


## Block 031 — Price Field Types Inventoried

The operator ran a local type-only summary over the list and matching detail snapshots. For both records, yesPrice, noPrice, and primaryYesPrice were strings; primaryNoPrice, secondaryYesPrice, and secondaryNoPrice were null. The operator did not report numeric values or a market ID.

This confirms those fields' presence and JSON types for one market sample only. It does not establish semantics across the catalogue, price freshness, or price movement over time. The trades record contains zero rows, so no trade-based signal can be evaluated.

### Next

After at least 15 minutes from the first list observation, append one more bounded market-list snapshot. Compare the same market's yesPrice locally and report only whether the field exists and whether its numeric value changed. Keep the value and identifier on-device.


## Block 032 — Repeated List Price Comparison

The operator confirmed the second bounded market-list snapshot was saved. The local JSONL file contains four records total, including two list observations. A local-only comparison found the same market in both list snapshots and found yesPrice present in both; its source value was unchanged between the observations. No numeric price, market identifier, credential, or raw snapshot was shared.

This is one unchanged comparison over the observed interval for one market. It does not establish that the source field is a reliable probability, that its value is current, or that the market is representative. The empty trade tape and null secondary price fields still provide no alternative movement evidence. No movement signal is implemented.

### Next

After at least 15 minutes from the second list observation, append one more bounded list snapshot. Compare the same market against the latest observation locally and report only record/list counts, same-market availability, yesPrice availability, and whether it changed. Keep values and identifiers on-device.


## Block 033 — Third List Snapshot Saved

The operator reported that the device-local JSONL snapshot file now contains five records, up from four. The just-completed command was the next bounded list read, so this records a third list snapshot alongside the earlier detail and trades observations. No payload, price, market identifier, or credential was shared.

The new list observation is saved locally, but its same-market price comparison has not yet been reported. No conclusion about movement is made in this block.

### Next

Compare the two latest list observations locally for the same market. Report only total/list record counts, same-market availability, yesPrice availability, and whether its numeric value changed. Keep values and identifiers on-device.


## Block 034 — Second Unchanged List Comparison

The operator compared the two latest list snapshots locally. The JSONL file has five records, including three list observations. The same market was present in the second and third list observations; yesPrice was present in both and its numeric value was unchanged. No market identifier, price, credential, or raw payload was shared.

Together, the two adjacent comparisons across three list observations show no yesPrice change for this one market over the observed intervals. They do not establish how the field behaves across other markets or longer periods, nor prove that it represents a fresh tradable probability. No movement signal is implemented.

### Next

After at least 15 minutes from the third list observation, append one final bounded list snapshot and compare it locally with the latest prior list observation. Report only sanitized counts, same-market availability, field availability, and whether yesPrice changed. Keep values and identifiers on-device.


## Block 035 — Fourth List Snapshot Saved

The operator reported that the device-local JSONL snapshot count increased from five to six after the next bounded market-list request. This is the fourth list observation, alongside the earlier detail and trades records. The newly appended response and identifiers remain on the operator's device.

The latest same-market yesPrice comparison is pending. No conclusion about price movement is made here.

### Next

Compare the two latest list snapshots locally. Report only record/list counts, same-market availability, yesPrice availability, and whether its numeric value changed. Keep all prices and identifiers on-device.


## Block 036 — Third Consecutive Unchanged Comparison

The operator compared the two latest list snapshots locally. The file has six records, including four market-list observations. The same market appeared in both latest pages; yesPrice was present and its numeric value was unchanged. Across the four list observations there are now three consecutive unchanged comparisons for this one market. No price values, market identifiers, credentials, or raw payloads were shared.

This supports only that the sampled field did not change across the observed intervals for the one market returned so far. It does not prove staleness, field meaning, or API-wide behavior. The sample's zero-row trade tape remains insufficient for trade-based analysis.

### Next

Run one bounded market-list request with limit 50 (maximum one page, no cursor traversal). Report only item count and whether a cursor is present/nonempty. Keep market IDs and response values on-device. Use this to determine whether the narrow sample resulted from the small page limit.


## Block 037 — Large List Limit Still Returned One Item

The operator ran one bounded list request with limit 50 and summarized the saved response locally. It contained one item. The response included a nextCursor field, but its value was empty. This indicates that increasing the requested page size did not increase the returned sample in this invocation; it does not establish the total catalogue size or prove a pagination defect. No item identifier, title, prices, or raw response were shared.

### Next

Inspect the single returned item's phase, status, onChain, and resolved values locally, without printing identifiers, title, dates, or price fields. Report only those four fields or their types/nullness so the sample's operational state can be understood.


## Block 038 — Single Returned Market State Inspected

The operator locally summarized the sole item returned by the limit-50 list request. Its phase and status were both reported as primary, resolved was false, and onChain was null. The null value is absence of a positive/negative on-chain assertion; it must not be converted to false. No title, identifier, date, price, credential, or raw payload was shared.

This is one authenticated API sample and does not establish the item's actual Solana-account state or the catalogue-wide prevalence of null onChain values.

### Next

Compare the already-saved detail response with the list response for phase, status, onChain, and resolved. Report only field presence, JSON type, and nullness for the detail response; keep IDs, titles, dates, and prices private.


## Block 039 — List/Detail Field Presence Matches

The operator summarized the already-saved detail response locally. It contains phase and status as strings, resolved as a boolean, and onChain as null. This matched the earlier list/detail pair's field presence and JSON types/nullness; the detail values themselves were not printed, so equality of the non-null values was not claimed. No identifiers, titles, dates, prices, credentials, or raw response were shared.

The live sample supports a tri-state treatment for onChain: true, false, or unknown/null. Null must remain unknown and must not be converted to false. The current evidence is one market only.

### Next

Compare the already-saved list and detail responses locally for equality of phase, status, onChain, and resolved, reporting only field-match booleans and same-market availability. Keep IDs, titles, dates, and prices private.


## Block 040 — Latest List/Detail onChain Field Match Is Indeterminate

The operator compared the latest limit-50 list item with the saved detail response for the same market. The comparison reported same_market=true; phase, status, and resolved matched; onChain_match was null. The comparison command returns null for a field if it is missing from either response, so the onChain result is indeterminate due to field absence in at least one of the compared objects, not a comparison of two explicit nulls.

The earlier list/detail type-only observation remains scoped to its original pair. Do not generalize it to the later limit-50 list response. No ID, title, date, price, credential, or raw payload was shared.

### Next

Inspect onChain key presence/type/nullness separately in the latest matching list item and saved detail response. Print only these two sanitized field summaries, with no identifier or other payload values.


## Block 041 — List Omits onChain; Detail Returns Null

The operator inspected the matched list/detail pair's field presence locally. The same market was confirmed in both. The list response omitted onChain; the detail response included onChain with JSON null. This is an endpoint representation difference, not evidence of a false on-chain state. Other compared fields phase, status, and resolved matched. No identifiers, titles, dates, prices, credentials, or raw payloads were shared.

The local consumer rule is: only explicit boolean values may be interpreted as affirmative or negative on-chain assertions; both a missing field and explicit null map to semantic unknown, while preserving the source distinction (omitted versus null) in stored data and presence metadata. The sample is limited to one market and two routes.

### Next

Use this rule in the internal field-mapping/UI contract: show on-chain state as unknown when absent or null, and never imply that such a market is confirmed on-chain or confirmed off-chain. Keep the source observation unchanged and retain presentFields provenance.


## Block 042 — Sparse onChain Consumer Classifier Implemented

Added panta_signal/market_state.py with a pure classify_on_chain helper. It returns a consumer-facing state of reported_on_chain, reported_off_chain, or unknown, plus sourceFieldState distinguishing missing, explicit null, boolean, and non-boolean values. Missing/null/non-boolean values remain unknown. Explicit true/false are reported as source assertions, not independently verified chain state. The helper does not mutate or replace the source market object; callers retain the provider snapshot and presentFields.

Added seven offline unit tests covering missing, null, true, false, string and numeric non-booleans, non-mutation, and non-object input. TDD red/green was verified in an isolated local harness: tests failed while the module was absent, then all seven passed after implementation. The repository's prior full 34-test suite was green before this change; the full suite has not yet been rerun with the new test file.

Updated provider/data-contract documentation to distinguish raw source representation from derived display state. No live Panta call was made and no API payload was added to the repository.

### Next

Pull this research branch in Termux and run the full offline unittest suite. Report only the final test count and pass/fail summary. Then wire the helper into a consumer/UI when that layer is built.
