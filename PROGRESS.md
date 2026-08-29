# CodexWriter — Progress and Handoff

**Active branch:** `planning/schema-skill-impact-plan`
**Active HEAD:** `1c4117a02848a5fe142508509759cd360cca67e7`
**Remote:** `origin` — `https://github.com/davehallmon/CodexWriter.git`
**Current date:** 2026-08-28
**Status:** Read-only planning and audit work; no implementation, merge, schema/skill/template change, dependency installation, test creation, CI work, or Dust & Ash extraction authorized by current branch state.

---

## 1. Current Report

### Project state

CodexWriter is currently a ratified architecture plus a provisional documentation-and-schema-and-skill prototype. The authoritative architecture is the layered hybrid model recorded in the ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3`. The existing JSON state model, eleven skills, four templates, and four schemas are a provisional implementation prototype, not ratified architecture.

### What exists

1. **Ratified architecture materials**
   - `ARCHITECTURE.md`
   - `docs/architecture/seven-source-synthesis-2026-08-27.md`
   - `docs/architecture/seven-source-synthesis-ratification-addendum.md`
   - `docs/crosswalk.md`
   - `docs/decisions/2026-08-26-alignment-evaluation.md`
   - `docs/source-analysis/README.md`
   - Seven completed source analyses under `docs/source-analysis/`

2. **Provisional prototype**
   - 11 `SKILL.md` files under `skills/`
   - 4 JSON schemas under `schemas/`
   - 4 templates under `templates/`
   - No project-state instances exist in the repository

3. **Documentation integration**
   - Clean integration base: `c416472035ad6a4fdf7cfe47b5232e068e671e5f`
   - Parent of that base: `0e999a9392683878a8cca9b1760cf92c81176c85`

4. **Planning deliverable**
   - Branch: `planning/schema-skill-impact-plan`
   - HEAD: `1c4117a02848a5fe142508509759cd360cca67e7`
   - Single file: `docs/plans/schema-skill-impact-plan-2026-08-28.md`
   - This branch is read-only planning and is not merged

5. **Checkpoint 1A**
   - Authorized implementation scope exists in the last exchange
   - A separate worktree at `/home/davehallmon/codexwriter-cp1a` contains untracked implementation files
   - That work was not committed, not pushed, and not proven correct; it is not part of the main repository
   - Recovery audit found no contamination and no committed implementation in the main repository

### What does not exist yet

- Schema validator
- Continuity checker
- Transaction tooling, audit store, or provenance capture
- Derived-view rebuild mechanism
- Author-memory store
- Context assembler
- Fixtures, smoke tests, CI
- Generic vertical slice
- Host B portability evidence
- Dust & Ash extraction
- LICENSE file
- Project-state instances

---

## 2. Current Decisions

These are the decisions in force from the most recent explicit exchange:

- **D1 — Author-memory placement:** Option 1 — move `author_preferences` out of story-state into a separate author-memory store.
- **D2 — Schema direction:** Evolve the four existing schemas; do not ratify them as-is and do not replace them wholesale; add separate artifacts for genuinely different authority or lifecycle boundaries, most clearly author memory and audit history.
- **D3 — Reader-simulation timing:** Correct the contract in the first authorized schema-and-skill alignment phase; prove full isolation in the vertical slice; do not leave the contradictory contract in place merely because the supporting runtime does not yet exist.

All other decisions (D4–D12) remain pending and are documented in `docs/plans/schema-skill-impact-plan-2026-08-28.md §12`. A revised D4–D12 closure packet was produced in the last read-only exchange; it is conversation record only and is not a repository file.

---

## 3. Ratified Architecture Summary

### Authority model

- Approved Markdown is authoritative for exact narrative wording and for what the reader encounters.
- Approved structured state is authoritative for explicitly governed, approved machine-checkable canon and workflow fields only.
- Derived views, summaries, indexes, registries, reports, and context packages are never authoritative and contain no unique facts; they are rebuildable projections from canonical project files.
- Author memory is a separate authority category outside story canon.
- Conflicts between approved Markdown and approved structured canon block publication or state promotion until explicit reconciliation is recorded.
- No layer may silently overwrite another.

### Durable state and transactions

- One transaction owns the transition from one canonical authority state to the next.
- Expected-revision guard rejects stale sequential writes.
- Audit record captures who submitted what, what was applied, and what the check marked.
- Canonical advancement occurs only via the declared transaction mechanism.
- Git commit/merge may express the transaction boundary on Git-based workflows, but is not itself the transaction semantic.

### Context, views, and portability

- Context-assembly layer has a ratified minimum responsibility; exact LOD thresholds deferred until after the first vertical slice.
- Derived views serve different consumers differently.
- Schema-aware portability, host-neutral versus host-adapter boundary, and two-host evidence requirement are ratified.
- Deterministic invariants must match across hosts; judgment-based outputs need contract compliance, not identical wording.

### Editorial and HITL behavior

- Reader simulation begins with a context-blind manuscript-only pass; optional informed second pass is separately declared.
- Diagnosis and repair are separate; editorial passes have declared scope and stopping rules.
- Substantive prose editing uses batch-approval: diagnose, present one coherent batch of exact proposed changes, author accepts/rejects/modifies individually, apply only approved changes.
- Interactive and PR-boundary HITL modes are distinct; mode must be declared before work begins; silent mode switching is not permitted.
- Framework approvals belong to the framework track; Dust & Ash story phase gates belong to the Dust & Ash project track.

---

## 4. Provisional Prototype Summary

### Skills

- `fiction-orchestrator`
- `concept-development`
- `worldbuilding`
- `character-development`
- `narrative-architecture`
- `scene-planning`
- `scene-writing`
- `continuity`
- `prose-editing`
- `reader-simulation`
- `export` (optional extension)

### Schemas

- `schemas/story-state.schema.json`
- `schemas/character-state.schema.json`
- `schemas/scene-state.schema.json`
- `schemas/continuity.schema.json`

### Templates

- `templates/SKILL_TEMPLATE.md`
- `templates/story-bible-template.md`
- `templates/character-dossier-template.md`
- `templates/scene-template.md`

### Known prototype weaknesses relative to ratified architecture

- No transaction, stale-revision, audit, or provenance mechanism
- Author preferences embedded in story-state instead of a separate author-memory store
- Reader-simulation inputs contradict the context-blind baseline
- Continuity describes judgment-based checks as if mechanical
- Prose-editing does not enforce diagnosis/repair separation or batch-approval
- No context assembly, derived-view labeling, or provenance for assembled context
- Dust & Ash-specific material embedded in reusable-core files and schema fields

---

## 5. Pending Workstreams

1. Documentation alignment review — was pending at ratification; impact plan created; ratification status of individual findings still open
2. File-by-file impact plan — created and pushed; pending Dave's review and decisions on D2 field classification, D7 profile mechanism, D8 transaction/audit placement, D9 author-memory scope, D11 export/manifest choice
3. Checkpoint 1A — authorized scope exists; implementation was started in a separate worktree but not committed, not pushed, and not proven correct
4. Schema/skill/implementation changes — unauthorized until explicit approval of impact plan and relevant decisions
5. Dust & Ash extraction — authorized direction only; no extraction begun

---

## 6. Repository Notes

- No environment/session logs in tracked tree
- Private _LOG transcripts preserved outside repository at `/home/davehallmon/.codexwriter-private/logs/`
- No credentials in tracked files
- This file is now the root handoff file; nightly handoffs should live here going forward
- Superseded historical documents: `docs/build-report-2026-08-26.md` and Sections 1–9 of `docs/decisions/2026-08-26-alignment-evaluation.md` are historical and should not be executed as current instructions

---

## 7. Handoff Origin

This `PROGRESS.md` consolidates and replaces:

- `docs/build-report-2026-08-26.md`
- The stale portions of `docs/source-analysis/README.md`
- The stale portions of `docs/decisions/2026-08-26-alignment-evaluation.md`
- The authoritative architecture, decisions, and status from `ARCHITECTURE.md`, the ratification addendum, the August 27 ratification note, and the August 28 impact plan

Superseded material is preserved in place where it already exists, but is explicitly marked historical within this file. From this moment on, all nightly handoffs live here.

---

Commit: `docs: establish root PROGRESS.md as canonical handoff file`

This commit creates a single root-level `PROGRESS.md` that consolidates the ratified architecture state, provisional prototype state, current decisions, pending workstreams, repository notes, superseded-document status, and handoff origin. It does not modify any schema, skill, template, existing documentation, or implementation file. It does not begin Checkpoint 1A, Dust & Ash extraction, or any other implementation.