# Operations — Panta Signal

## Current Operational State

Panta Signal is **not deployed**. No public application, live Panta API integration, background ingestion service, or production AI integration is currently claimed.

This document defines the operational requirements that later implementation must satisfy.

## Local Development

Exact local commands do not exist yet because no application runtime has been selected or scaffolded.

When implementation begins, this document must be updated with verified commands for:
- dependency installation;
- local development server;
- tests;
- type/static checks;
- build;
- database setup/migrations if applicable;
- production-equivalent smoke test.

Do not invent commands before those files and scripts exist.

## Configuration

Configuration should be supplied through environment variables or provider-managed secret storage. `.env.example` is a template only.

Expected configuration classes include:
- Panta API connection/authentication;
- application/public URL;
- persistence connection;
- AI provider configuration;
- operational limits/timeouts.

Exact names may change when the technical specification is frozen.

## Reachability and Health

Before public deployment, provide an inexpensive health/reachability signal that does not require expensive AI work.

A health response should eventually distinguish, where useful:
- application process reachable;
- build/version;
- database connectivity state;
- upstream Panta connectivity state without leaking credentials.

Health checks must not expose secrets or detailed internal configuration.

## Upstream Panta Failure

Future ingestion must define explicit behavior for:
- timeout;
- authentication failure;
- rate limiting;
- malformed response;
- partial response;
- provider outage.

The UI/API should preserve timestamps and must not silently present stale data as a successful current refresh.

## Snapshot Gaps

If scheduled observation intervals are missed:
- record the gap where practical;
- do not synthesize fake source observations;
- allow signal calculations to report insufficient/partial history;
- prevent the AI Analyst from treating missing intervals as observed facts.

## Logging

Operational logging should be minimal and sanitized. Useful fields may include:
- correlation/request ID;
- operation name;
- status/error class;
- duration;
- build/version;
- sanitized upstream state.

Never log API keys, authorization headers, private keys, wallet seeds, or unnecessary complete source payloads.

## Incident Recording

Material incidents should be recorded in the execution ledger/checkpoint, including:
- date/time;
- affected build/version;
- observed failure;
- user/demo impact;
- mitigation;
- unresolved follow-up.

Never include compromised secret values in incident records.

## Credential Rotation

If a credential is suspected exposed, revoke/rotate at the provider before relying on repository cleanup. Update deployed secrets and record the incident without reproducing the credential.

## Deployment Requirements

The initial deployment target should prioritize:
- zero or minimal cost;
- public HTTPS;
- server-side secret handling;
- compatibility with Panta API requirements;
- persistent storage compatibility;
- enough stability for public judging/demo;
- straightforward rollback/redeploy.

No provider is selected yet.

## Demo Readiness

Before a judged/public demo:
- verify public URL from a clean session/device;
- verify Panta data path is functioning;
- verify timestamps/provenance display;
- verify signal calculations on known fixtures/examples;
- verify AI answers use structured supporting evidence;
- verify no test credentials or debug-only shortcuts are active;
- record the build/commit used for the demo.

## Maintenance Rule

Whenever runtime, scripts, deployment, storage, or health behavior changes, update this document in the same work block and close with a new current checkpoint.
