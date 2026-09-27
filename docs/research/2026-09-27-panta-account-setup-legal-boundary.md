# Panta Account Setup and Terms Boundary

**Checked:** 2026-09-27  
**Branch:** `research/phase1-authoritative-validation-2026-09-27`  
**Status:** BLOCKED before account registration; no account or API credential created  
**Scope:** Official Panta docs index, account registration, API-key creation, documented account permissions, and API Terms

## Documentation discovery

The requested documentation index URL, `https://docs.panta.market/llms.txt`, could not be retrieved through the available web retrieval tool. As a source-backed fallback, the official documentation repository's current `docs.json` navigation was read as the full published page index. It lists the Guides and API Reference pages for auth, account, market catalog, market creation, orders, positions, claims, and trades. Relevant pages were selected from that index.

## Verified account registration contract

The official `POST /auth/register/` page specifies:

- required unique login email;
- required password (8–128 characters, subject to password validators);
- optional display name;
- response includes a new account ID, email/name, access JWT, and refresh JWT;
- new accounts default to `canCreateMarkets: true`.

No registration request has been sent. This is a documentation finding, not live account verification.

## Verified API-key contract and access limitation

The official `POST /account/keys/` page allows `env=test` or `env=live`, an optional label, and `revokeOthers`. The plaintext key secret is returned only in the creation response. The page does not document permission scopes or read-only key creation.

The indexed account-update page documents changing only the display name. It does not document an operation to turn off `canCreateMarkets`. Therefore the published contract does not currently establish a least-privilege, read-only credential. Treat any account/key as potentially able to reach broader API operations; never call write/trading/claim endpoints in this project.

## Terms that apply before credential issuance

The official Panta API Terms of Use are effective September 7, 2026. They state that obtaining API credentials, calling an endpoint, integrating the API, or making an API-powered product available constitutes agreement to the Terms.

Material points for the operator to review before registration include:

- mandatory visible attribution: **Powered by Panta**;
- responsibility for the developer product, security, legal compliance, disclosures, and privacy practices;
- no misleading live-data claims, unauthorized access, rate-limit circumvention, or raw-data resale as a substitute for Panta;
- Panta may introduce or change fees prospectively subject to notice where required by an agreement or law;
- an indemnity obligation for certain third-party claims, including reasonable legal fees;
- liability limitation, with the stated aggregate cap generally being the greater of fees paid in the prior six months or USD 100, subject to non-excludable liability;
- British Virgin Islands governing law and confidential UNCITRAL arbitration in English, seated in Road Town, Tortola, unless the parties agree otherwise in writing.

This is a summary of the published Terms, not legal advice. On 2026-09-27, the operator explicitly confirmed acceptance and authorized creation of a free test account with the documented default `canCreateMarkets: true` capability. No account has yet been created.

## Security and execution boundary

- The operator explicitly accepted the binding API Terms and authorized creating a free test account with `canCreateMarkets: true` on 2026-09-27.
- Do not collect the operator's password, JWT, or API key in chat.
- The one-time API secret must remain in a secure store or be entered by the operator into a local execution environment. A safe secret handoff to this execution environment is not available at this checkpoint.
- No funds have been deposited or moved. No market creation, trading, claim, or other write endpoint has been called.

## Exact next step

Terms acceptance and account creation with the documented default capability were explicitly authorized by the operator on 2026-09-27. The remaining registration step requires the operator to enter their email and new password directly in a secure provider flow; never collect the password, JWT, or API key in chat. Keep the one-time test key outside the public repository. Resolve a safe local execution path for the four planned read-only GETs; do not call write/trading/claim endpoints.

## Sources

- [Official docs navigation](https://github.com/Kaito-HQ/panta-api-pub/blob/main/docs.json)
- [Register](https://github.com/Kaito-HQ/panta-api-pub/blob/main/api-reference/auth/register.mdx)
- [Create API key](https://github.com/Kaito-HQ/panta-api-pub/blob/main/api-reference/account/create-key.mdx)
- [Update account](https://github.com/Kaito-HQ/panta-api-pub/blob/main/api-reference/account/update.mdx)
- [Terms of Use](https://github.com/Kaito-HQ/panta-api-pub/blob/main/guides/terms-of-use.mdx)
