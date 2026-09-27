# Research Evidence Rules

This directory stores external research that materially affects Panta Signal design, implementation, operation, or submission.

## Required Metadata

Each research note should record:
- topic;
- source title;
- source URL;
- source/provider;
- access date;
- whether the source is primary/authoritative or secondary;
- exact claims verified;
- unresolved questions;
- downstream project documents affected.

## Evidence Hierarchy

Prefer:
1. official Panta documentation/source repositories;
2. official hackathon/competition rules and organizer pages;
3. official platform/provider documentation;
4. secondary sources only when primary evidence is unavailable, clearly labeled as secondary.

## Rules

- Do not treat prior chat summaries as authoritative external evidence.
- Do not copy secrets, tokens, authenticated headers, or private account data into research notes.
- Clearly distinguish quotation/factual extraction from project interpretation.
- Revalidate time-sensitive facts such as deadlines, prizes, rules, API versions, rate limits, and eligibility before relying on them.
- Preserve enough context to let another agent reproduce the verification.

## Suggested Naming

Use dated, topic-specific files, for example:

`YYYY-MM-DD_panta-api-validation.md`

`YYYY-MM-DD_hackathon-rules.md`

Material conclusions should be reflected in the decision log, roadmap, hackathon criteria matrix, or technical specification as appropriate.
