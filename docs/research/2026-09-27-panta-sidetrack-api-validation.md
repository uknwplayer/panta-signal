# Panta API Sidetrack and API Validation

**Checked:** 2026-09-27  
**Status:** PARTIALLY VERIFIED — sponsor brief and public docs verified; test authentication and one live list/detail pair validated; categories, trades, and broader pagination/schema behavior remain unverified  
**Scope:** Panta Sidetrack requirements, public API contract, security/branding constraints, and MVP-relevant read endpoints

## Sources

### Sidetrack / sponsor sources

1. Superteam Earn Panta API Sidetrack listing: `https://superteam.fun/earn/listing/panta-api-side-track`
2. Panta website: `https://panta.market`
3. Panta public announcement through PantaHQ linking builders to the Superteam Earn sidetrack listing.

### API sources

1. Public docs URL published by the sidetrack: `https://docs.panta.market/`
2. API playground published by the sidetrack: `https://github.com/Kaito-HQ/panta-api-playground`
3. Public API documentation repository referenced by the playground: `https://github.com/Kaito-HQ/panta-api-pub`
4. Live API base published in the docs/playground: `https://live-api.panta.market/api/v1`

The `docs.panta.market` website was not directly retrievable by the browsing tool during this block. The published GitHub documentation/playground were therefore used as the inspectable contract surface. No undocumented behavior is treated as fact.

The operator also supplied a website Terms of Use copy dated August 5, 2026. It contains no support email, form, or contact address. The API Terms previously found in the published API docs have a different stated effective date (September 7, 2026); keep these as distinct document versions unless Panta confirms they are the same terms.

## VERIFIED — Panta Sidetrack Reward

The sponsor listing states a **5,000 USDG** total prize pool:

- 1st: **2,000 USDG**
- 2nd: **1,000 USDG**
- 3rd: **1,000 USDG**
- 4th: **1,000 USDG**

The listing schedules the Panta Sidetrack winner announcement for **October 27, 2026**.

## VERIFIED — Sidetrack Eligibility / Submission Requirements

The sponsor listing requires builders to:

- register for the official Colosseum Crypto World's Fair hackathon;
- submit the project through the official Colosseum platform;
- meet Colosseum eligibility rules;
- also submit the project to the Panta Sidetrack through Superteam Earn;
- meaningfully integrate the Panta API;
- provide a working demonstration;
- explain what was built and the problem/use case;
- explain how the Panta API is integrated;
- submit in English.

The listing explicitly states that submitting to the Panta Sidetrack does **not** replace the official Colosseum submission.

## VERIFIED — Panta Sidetrack Judging Criteria

The sponsor listing judges submissions on:

1. **Panta API Integration** — meaningful use of the API in the product.
2. **Technical Execution** — quality, functionality, and implementation.
3. **Product & User Experience** — clarity, intuitiveness, usefulness.
4. **Originality** — novelty/interest of the use case.
5. **Impact Potential** — potential for real-world use beyond the hackathon.
6. **Traction** — evidence of users, usage, or early traction.

### Product implication

Panta Signal aligns directly with categories named in the brief, especially:

- Trading & Analytics;
- AI + Prediction Markets;
- market discovery / analytics products;
- new prediction-market experiences.

The design should emphasize a useful intelligence workflow rather than a generic raw-data mirror.

## VERIFIED — Public API Base and Authentication Model

The public docs/playground publish:

- live base: `https://live-api.panta.market/api/v1`
- staging base: `https://staging-api.panta.market/api/v1`

Documented authentication flow:

1. `POST /auth/register/` or `POST /auth/token/` returns a JWT pair.
2. `POST /account/keys/` with Bearer JWT creates an API key.
3. Product routes accept either `X-Api-Key` or `Authorization: Bearer <access>`.
4. `X-Api-Key` is preferred for server-to-server product calls.
5. Test keys use the `pk_test_…` prefix; live keys use `pk_live_…`.
6. The plaintext API secret is shown only once.
7. API keys in query parameters are rejected; credentials belong in headers.

The flow remains **documentation-verified but not live-validated**. On 2026-09-27 the operator submitted the documented registration from Termux after explicitly authorizing account creation; the API returned HTTP 403. The script's recovery file was absent when checked, so no API JWT/key is available. The exact API error body and remote account state are unverified. The user can sign into the website and sees a profile/wallet, which does not by itself validate API auth or API-key creation.

## VERIFIED — MVP-Relevant Read Endpoints

The following documented endpoints are enough to begin Panta Signal's read-only intelligence design without trading or custody:

### `GET /categories/`

Provides category values used to filter market discovery.

### `GET /markets/`

Purpose: paginated market catalog.

Documented properties:

- API key or Bearer required;
- optional `category`, `status`, `createdBy`, `cursor`, `limit`;
- `limit` defaults to 20 and is capped at 50;
- phases include `primary`, `secondary`, `resolved`, `cancelled`;
- list data comes from the USDC market catalog/registry;
- list rows do not live-RPC prices;
- fields include `marketId`, category, title, description, images, phase, market type, start/end/resolution times, region, resolution/status state, `volumeUsdc`, and partner-creation metadata;
- price fields on list rows may be null.

### `GET /markets/{marketId}/`

Purpose: market detail.

Documented behavior:

- same base market shape as list;
- fills spot/phase price fields from on-chain state when RPC is available;
- can expose `yesPrice`, `noPrice`, primary prices and secondary prices.

### `GET /markets/{marketId}/trades/`

Purpose: public market trade tape.

Documented behavior:

- API key or Bearer required;
- `limit` defaults to 50 and is capped at 200;
- rows include market ID, wallet, primary/secondary marker, YES/NO share amounts, fee, block time, transaction signature, quote asset.

### MVP decision

Panta Signal does **not** need market creation, buying, wallet positions, claims, transaction building, wallet signing, or capital movement for the initial product proof.

Initial ingestion can be built around:

`categories -> market list -> selected market detail -> market trade tape -> local snapshots -> deterministic signals`

## VERIFIED — Rate Limits and Error Contract

The published docs specify structured errors with `code` and `message` and recommend switching on the API `code`, not only HTTP status.

Relevant status classes include 401, 403, 404, 429, and 500.

Documented default limits may be overridden by deployment, but the current public docs state:

- read routes: **120 requests / 60 seconds**;
- positions: 60 / 60s;
- quote: 30 / 60s;
- build: 20 / 60s;
- register/auth/report: 40 / 60s;
- upload: 10 / 60s.

Rate-limit headers include limit, remaining, reset, and `Retry-After` on 429.

### MVP decision

The Panta Signal collector should operate materially below the published read ceiling, honor `Retry-After`, add jitter to retries, and distinguish API failure from stale local data.

## VERIFIED — Security / Custody Model

The API documentation states:

- wallet private keys / seed phrases must not be sent to the API;
- API credentials must remain protected;
- the playground architecture proxies requests through a server route rather than exposing upstream secrets directly;
- Panta builds unsigned transactions for write flows and clients sign/broadcast them.

Panta Signal's initial read-only architecture is therefore compatible with a no-wallet/no-custody MVP.

## VERIFIED — Mandatory Panta Attribution

The Panta Public API Terms of Use and playground contribution rules require developer products using the API to display:

**Powered by Panta**

The attribution must be clear, legible, associated with Panta-powered functionality, and linked to Panta where hyperlinks are supported unless otherwise approved.

This requirement must be included in UI acceptance criteria and the final submission checklist.

## VERIFIED — Data / Caching / Representation Constraints

The Panta Public API Terms state that developers must not:

- materially misrepresent Panta market information;
- present simulated, cached, or stale information as live;
- bypass access controls/rate limits;
- resell raw API access, credentials, or substantially unmodified Panta data as a substitute for Panta's own service without permission.

Developers should preserve attribution and material context, and clearly identify stale/delayed information when appropriate.

### Panta Signal implication

This strengthens the existing provenance design:

- store observation timestamps;
- expose source age/staleness;
- distinguish source fields from locally derived signals;
- avoid presenting Panta data as proprietary Panta Signal source data;
- provide added analytical value rather than simply republishing the raw catalog.

## UNVERIFIED / Still Needed

1. Live categories response and exact current category endpoint behavior.
2. Live trade-tape response and fields for a selected market.
3. Cursor/page behavior across a second controlled list read; one call returned one item without a `nextCursor` field, which is insufficient to establish a pagination defect.
4. Whether optional detail fields vary across representative markets; the first sampled detail response omitted `question`, `resolutionRule`, `sources`, and `totalTrades`, while it included `onChain`.
5. Current effective account-level rate limits and response headers.
6. Exact Panta Sidetrack submission deadline/time and submission-form fields/media requirements.
7. Operator-specific eligibility confirmation.

## Exact Next Technical Validation

The operator now has a test key, stored only on-device. Registration and test-key creation each returned HTTP 201. A read-only `GET /account/` returned HTTP 200 with an active key and `canCreateMarkets: true`.

One bounded `GET /markets/?limit=1` returned HTTP 200 with one item and no `nextCursor` field in that invocation. The corresponding detail request returned HTTP 200 and the returned `marketId` matched the requested ID. The sampled detail contained `onChain` and omitted `question`, `resolutionRule`, `sources`, and `totalTrades`. This is a single sample and does not establish a general response shape or pagination defect. No raw response or identifier was saved in the repository.

Next, make bounded read-only requests to categories and the selected market's trade tape, then repeat one small list read to check cursor/page behavior. Record status, counts, field names, cursor presence, and any rate-limit headers without printing secrets or personal/account identifiers. Do not create markets, call quote endpoints, trade, claim funds, sign transactions, or move capital. Keep the normalized data contract provisional pending representative live samples.

## VERIFIED — Official Developer Support Route for API Signup 403

The Panta Sidetrack listing identifies the official **#dev-chat** channel in the Panta Discord as the contact route for technical questions, integration support, and clarification during Crypto World's Fair.

- Official listing: https://superteam.fun/earn/listing/panta-api-side-track
- Discord invite published by that listing: https://discord.gg/M76nH6fUwc

This establishes where to ask about the observed HTTP 403. It does **not** establish why registration failed or confirm that the API account exists. No support message was sent, and the registration POST was not repeated. The account holder should ask whether API registration is restricted or whether the website account needs separate enablement, and request the supported test-key path without sharing passwords, JWTs, API keys, or wallet secrets.


## Operator-Provided Support Interaction Evidence — 2026-09-27

The operator provided a screenshot showing the prepared HTTP 403/API test-key question posted in Panta's `#dev-chat` at approximately 02:04 local time. The same screenshot shows a community reply advising another user to open a support ticket to connect with the team. The operator's own question has no visible answer in the screenshot.

This is evidence of the question being posted and of the displayed ticket guidance only. It does not establish that the guidance came from Panta staff, explain the 403, or confirm account/API access. Recommended next step: open the server's support-ticket channel/flow and ask the same question there without reposting account secrets. No new registration POST was made.


## Private Support Ticket Opened — 2026-09-27

A second operator-provided screenshot shows private Discord channel `#ticket-0160` open with the API HTTP 403/test-key question posted. The Ticket Tool bot acknowledged the request and said a Panta team member would join shortly.

This is an automated ticket acknowledgement, not a response from Panta support and not an explanation of the failure. No registration retry was made. Wait for the Panta team reply in the private ticket; provide only non-secret diagnostics if requested.


## External API Behavior Report — 2026-09-27 (Not Independently Validated)

The operator supplied a correction to earlier API notes and linked the public reproduction repository:
https://github.com/bisale24-ops/settlement-check

The repository README's section **“Five things this project got wrong”** explicitly withdraws or narrows these earlier conclusions:

1. The claim that most markets lack questions was based on the wrong listing fields; market cards and Panta pages expose the question and resolution criteria.
2. The claim that buyers cannot find the resolution rule is withdrawn; the page displays it.
3. The `sentToUma` flag alone does not establish UMA settlement. The README says Panta's page describes agent resolution with confidence, rationale, and a dispute window; no conclusion should be drawn from that flag alone.

The same README reports the following observations. These are **externally reported and reproducible according to that repository, but have not been independently reproduced by Panta Signal**:

- 13 of 100 sampled catalogue markets were in primary/secondary phases without a Solana account; the Panta page displayed “Market not found on-chain”. The report proposes exposing an `onChain` indicator or filtering these from listing clients.
- Market cards appeared in complete and stripped shapes, with fields such as `question`, `resolutionRule`, `sources`, and `totalTrades` omitted in the stripped shape without an explicit shape indicator.
- Seven API behaviors were reported: cursor pagination not advancing; `GET /markets/categories/` returning `MARKET_NOT_FOUND`; `status=resolved` and `status=cancelled` returning zero rows; volume fields varying between calls; listing/card question disagreement; non-stable catalogue slices between reads; and `POST /markets/create/quote/` intermittently rejecting drafts with `INVALID_MARKET_PARAMS`, without fields, where the documented code reportedly says `DUPLICATE_MARKET`.

The README describes read-only catalogue and Solana checks, plus a quote POST that does not sign, submit, or pay but may reserve a create session. Panta Signal will not repeat that POST or make authenticated probes until API access is resolved and the request's side effects are understood. No private keys or wallet signing are needed for the report's stated reproduction.

Source reviewed: current README on the linked repository, fetched 2026-09-27. Exact independent live verification remains blocked because Panta Signal has no API credential.


## Live Read-only Validation Update — 2026-09-27 (Block 012)

This update supersedes the earlier "no API key obtained" status above. The documented account/key flow has now succeeded: registration and test-key creation each returned HTTP 201. Authenticated `GET /account/` returned HTTP 200. One list/detail pair also returned HTTP 200 as described in "Exact Next Technical Validation". The test secret remains on the operator's device and is not recorded here.

Only that one list/detail sample is independently validated by this project so far. The external `settlement-check` catalogue and seven-behavior report remains externally reported pending additional controlled reproduction. No quote or other write endpoint was called.


## Isolated Categories and List GETs — 2026-09-27 (Block 013)

The operator reported:
- `GET /categories/` returned HTTP 200 via Termux `curl`;
- `GET /markets/?limit=2` returned HTTP 200 with one item and a `nextCursor` field.

The cursor value was not printed; its truthiness and any page movement remain unverified. A prior combined Python `urllib` probe ended in HTTP 403 without per-request results. Because the isolated routes succeeded via `curl`, a client-dependent difference is plausible, but the exact failed request/cause is unknown. No IDs, raw payloads, or credentials were recorded.

Next read-only checks: determine whether the cursor is nonempty, request one next page if available, and query one market's trade tape with `curl`.
