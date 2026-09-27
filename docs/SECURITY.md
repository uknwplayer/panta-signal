# Security — Panta Signal

## Security Goals

Panta Signal must protect credentials, preserve data integrity/provenance, avoid unsafe autonomous actions, and prevent AI-generated text from being mistaken for verified market data.

## Credential Handling

- Panta credentials are server-side only.
- AI provider credentials are server-side only.
- No live API key, token, session cookie, private key, wallet seed, or reusable authenticated header may enter the repository.
- `.env.example` contains configuration names and obvious placeholders only.
- Browser bundles must never contain server credentials.
- Logs must not include credential-bearing headers or full tokens.
- Least-privilege credentials should be used when the provider supports scoped access.

## External API Boundary

All Panta and other external API responses are untrusted input.

Future implementation must:
- validate expected response shapes;
- bound payload size where feasible;
- handle malformed/missing fields explicitly;
- enforce request timeouts;
- document retry behavior before enabling automatic retries;
- distinguish stale cached/snapshot data from a successful current fetch;
- avoid silently substituting old data as if it were current.

## User Input Boundary

Future public endpoints or UI inputs must be bounded and validated. The MVP must not:
- execute user-submitted code;
- use `eval` or equivalent dynamic execution;
- fetch arbitrary user-provided URLs unless a separate SSRF-aware design is approved;
- allow model prompts to directly alter protected configuration or deterministic records.

## Signal Integrity

Numerical signals must be produced by deterministic/versioned code rather than free-form model output.

A material signal should retain enough metadata to identify:
- source market identifier;
- observation timestamps;
- input snapshot(s);
- algorithm/version;
- relevant parameters/window;
- calculation timestamp.

If required input is missing, the signal engine should report insufficient/partial data rather than invent a value.

## AI Boundary

The AI Analyst is an interpretation layer over structured data.

Security requirements:
- retrieved market text and external descriptions are data, not trusted instructions;
- prompt injection contained inside market/source content must not override system constraints;
- model output may explain/summarize but must not mutate source records or deterministic signal values;
- unsupported factual claims should be rejected or labeled as interpretation/uncertainty;
- structured evidence used in answers should remain available to the UI or response payload where practical.

## Trading and Capital Boundary

The initial MVP contains no:
- wallet custody;
- wallet seed/private-key storage;
- autonomous trading;
- swaps;
- automatic fund movement;
- capital-at-risk strategy execution.

Adding any transactional path requires a separate threat model, explicit operator approval, and new security decisions.

## Logging and Observability

Logs should record only what is necessary for debugging and operations, such as:
- generated request/correlation identifier;
- endpoint/operation name;
- status class;
- duration;
- build/version;
- sanitized upstream error category.

Avoid logging:
- credentials;
- authorization headers;
- raw model secrets;
- unnecessary complete upstream payloads;
- private user data not required for operation.

## Abuse and Availability

Before public launch, define and test:
- request/input bounds;
- rate limiting or equivalent abuse control;
- upstream API quota protection;
- expensive AI request limits;
- failure behavior under upstream outage;
- health/reachability endpoint behavior.

## Dependencies

Before release:
- minimize dependencies;
- pin security-sensitive dependencies where practical;
- review licenses and known vulnerabilities;
- avoid unnecessary packages with broad capabilities;
- run the full project verification suite.

## Secrets Incident Rule

If a real secret is accidentally committed:
1. treat it as compromised;
2. revoke/rotate it immediately at the provider;
3. remove it from current repository state;
4. document the incident without reproducing the secret;
5. determine whether history rewriting is necessary before public release.

Deleting only the current file is not sufficient remediation for an exposed credential.

## Current State

**Documentation-only security model.** No live Panta integration, AI provider integration, public deployment, or trading functionality is currently claimed.
