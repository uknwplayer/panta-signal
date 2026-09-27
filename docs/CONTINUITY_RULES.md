# Continuity Rules — Panta Signal

These rules allow Panta Signal to survive changes of chat, agent, session, device, or tool without depending on conversation memory.

## Project Language

English is the official language for repository artifacts, source code, comments, API surfaces, public errors, operational documentation, issues, releases, and public-facing communication. Portuguese may be used in private working conversation with the operator.

## Primary Rule

**`docs/checkpoints/CHECKPOINT_CURRENT.md` must be updated at the end of every work block.**

A work block is any unit that:
- changes code or documentation;
- makes or revises a product/technical decision;
- performs meaningful API or hackathon research;
- completes or fails a test;
- changes configuration or deployment state;
- discovers a blocker or material risk;
- creates demo/submission evidence.

## Resume Order

Any new agent or contributor must:
1. read `docs/checkpoints/CHECKPOINT_CURRENT.md`;
2. read `docs/ROADMAP.md`;
3. inspect documents/evidence referenced by the checkpoint;
4. verify that claimed repository state actually exists;
5. execute only the recorded next step, or explicitly record why the plan was revised.

## Required Status Vocabulary

Use:
- **COMPLETED** only for verified work;
- **PLANNED** for intended work;
- **BLOCKED** for unresolved dependencies;
- **UNVERIFIED** where evidence is insufficient.

Never convert intention, prior chat memory, or an untested assumption into a completed fact.

## Minimum Checkpoint Content

Every current checkpoint must include:
- date and block identifier;
- overall current state;
- work completed in the block;
- evidence/tests performed and results;
- active decisions;
- relevant files and commit/PR references where available;
- pending work;
- blockers and risks;
- exact next step;
- items requiring operator confirmation;
- explicit unverified claims that could affect execution.

## Historical Checkpoints

Material milestones should be snapshotted to:

`docs/checkpoints/history/YYYY-MM-DD_NNN.md`

`CHECKPOINT_CURRENT.md` is mutable. Historical snapshots should not be rewritten except for an explicitly documented correction.

## Evidence Rules

- Prefer authoritative primary sources for external API, competition, deadline, eligibility, and judging claims.
- Record source URL/title, access date, and what was verified in `docs/research/` or another linked evidence document.
- A prior chat summary may guide research but is not authoritative external evidence by itself.
- Product behavior is not considered verified until code/tests or public execution evidence support it.
- A screenshot or demo claim should identify the build/version and date when practical.

## Data Truth Boundary

Keep the following distinct:
1. Panta/external source data;
2. deterministic derived data;
3. AI-generated interpretation.

AI-generated prose must never be used to silently fill missing source values or replace deterministic signal calculations.

## Secrets

Never record or commit:
- Panta API keys;
- AI provider keys;
- session tokens;
- deployment credentials;
- private keys or wallet seeds;
- reusable authenticated headers.

`.env.example` may contain configuration names and obvious non-secret placeholders only.

## Work-Block Closure

Before closing a block:
1. verify the files/actions actually exist;
2. verify status words match the evidence;
3. record failures/blockers rather than hiding them;
4. update `CHECKPOINT_CURRENT.md`;
5. create a historical checkpoint when a material milestone has been reached.

## Branch and Review Discipline

Implementation or substantial documentation work should normally happen on an isolated branch/workspace when available. Merging into the default branch is a separate integration action and should occur only after the work has been reviewed to the required level.
