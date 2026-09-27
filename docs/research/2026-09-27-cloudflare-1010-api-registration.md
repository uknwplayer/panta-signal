# Panta API registration 403 — Cloudflare 1010 diagnostic

**Date:** 2026-09-27  
**Branch:** `research/phase1-authoritative-validation-2026-09-27`  
**Status:** Strong indication of an edge/browser-signature block; registration itself remains unverified.

## Evidence

1. The operator's earlier Termux registration attempt used the documented `POST https://live-api.panta.market/api/v1/auth/register/` route and reported only `HTTP 403: HTTP_ERROR`. The script did not expose the HTTP response body or Cloudflare diagnostics. No credential or token was captured in this investigation.
2. On 2026-09-27 at 16:29:59Z, a credential-free Python `urllib` `GET` to that same route from the research environment returned HTTP 403 with a Cloudflare JSON body:
   - `error_code: 1010`
   - `error_name: browser_signature_banned`
   - detail: access blocked based on the client/browser signature
   - Cloudflare Ray ID: `a41be3f04849fafa-ORD`
3. The API base `GET /api/v1/` timed out from the same environment. No authenticated request was made.

Cloudflare's official Error 1010 guidance describes this as a site-owner browser-signature block and directs visitors to notify the site owner. The GET result strongly suggests the direct Python client can be blocked at Cloudflare before application-level auth. It does **not** prove that the earlier Termux POST received the same response: the original POST response body was not saved, and GET and POST are different requests.

## Documented alternative path

The current official Panta API Quickstart says to use **Try it** on the Register and Create API key documentation pages; the published `docs.json` enables the interactive playground with proxy mode. This is the next supported path to try in the operator's browser, entering the password directly on Panta's HTTPS page and never sharing it in chat.

- Quickstart: <https://docs.panta.market/quickstart>
- Register page: <https://docs.panta.market/api-reference/auth/register>
- Create API key page: <https://docs.panta.market/api-reference/account/create-key>
- Cloudflare Error 1010: <https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1010/>

## Safe next steps

1. Do not repeat a direct Termux signup POST merely to reveal the same failure body.
2. Try the official documentation playground's Register **Try it** form over HTTPS. The user should enter credentials directly there.
3. Record only the HTTP status, public error code/message, and any Cloudflare Ray ID. Never send passwords, JWTs, API-key secrets, cookies, or full auth responses in chat/support.
4. If the official browser playground is also blocked, give Panta support the timestamp and Ray ID above and ask for a supported registration path or an origin-side rule correction. Cloudflare's visitor guidance says the site owner controls this block; changing the payload or attempting to imitate a browser is not the right remediation.
5. Treat account creation as unverified until a successful Register/Token response is observed. Treat API-key creation and authenticated read validation as separate pending steps.

No new signup POST, login request, key creation, quote, trade, or wallet action was made in this diagnostic.
