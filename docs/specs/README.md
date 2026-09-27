# Technical Specification Rules

This directory stores technical specifications that freeze implementable contracts after product intent and external assumptions are sufficiently verified.

## Every Technical Specification Should Define

- purpose and scope;
- upstream design/decision references;
- interfaces and data contracts;
- exact field names/types where applicable;
- authentication/security boundary;
- error and timeout behavior;
- persistence/state behavior;
- provenance requirements;
- testable acceptance criteria;
- non-goals;
- open decisions/blockers;
- migration/versioning implications where applicable.

## Evidence Rule

A technical specification must not freeze an external API assumption as fact unless the relevant contract has been verified from authoritative documentation or controlled live validation and linked to research evidence.

## Implementation Rule

Implementation plans should reference the specification they implement. Material changes to a frozen contract require an explicit decision/spec update rather than silent drift.

## Initial Planned Specs

After Phase 1 external validation, likely first specifications include:
- Panta API ingestion/authentication contract;
- normalized market schema;
- snapshot schema;
- Signal Engine V0.1 contract;
- internal API/dashboard data contract;
- AI Analyst evidence/tool contract.

None of these are currently frozen or implemented.
