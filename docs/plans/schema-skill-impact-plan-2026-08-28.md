# CodexWriter — File-by-File Schema and Skill Impact Plan

**Date:** August 28, 2026
**Branch:** `planning/schema-skill-impact-plan`
**Base commit:** `c416472035ad6a4fdf7cfe47b5232e068e671e5f` (clean integration commit)
**Status:** Planning document only — no implementation authorized
**Single deliverable:** `docs/plans/schema-skill-impact-plan-2026-08-28.md`

> **Planning-only notice.** This document maps the ratified CodexWriter architecture to every existing schema, skill, and template. It identifies gaps, proposes implementation sequences, and registers decisions required from Dave. It does not authorize, describe as complete, or begin any implementation. Creation of this planning branch and document was explicitly authorized; implementation, schema modification, skill modification, template modification, validator creation, test creation, CI work, dependency installation, and Dust & Ash extraction remain unauthorized.

---

## 1. Executive Summary

### What the ratified architecture requires

The CodexWriter ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3` (Blocks A, B, and C) and framework decisions F1 and F2 establish a layered hybrid model with three authorities — approved Markdown for exact narrative wording, approved structured JSON state for explicitly designated machine-checkable canon and workflow fields, and rebuildable derived views containing no unique facts — plus ratified requirements for transactions, stale-revision rejection, audit history, provenance on promoted facts, context assembly minimum responsibility, host-neutral versus host-adapter boundaries, two-host portability evidence, schema-aware portability, context-blind reader simulation, separate diagnosis/repair, batch-level editorial approval, two-mode HITL with no silent switching, and framework/story-gate separation.

### The most consequential gaps in the prototype

1. **No transaction, stale-revision, audit, or provenance mechanism exists.** The four schemas define revision counters but no update protocol, no expected-revision guard, no audit record, and no structured canon provenance. The orchestrator skill describes incrementing `state_revision` and validating, but no tooling or contract enforces this as an atomic applied transaction.

2. **Author memory is embedded in story-state, not separated.** `author_preferences` lives inside `story-state.schema.json` as a sub-object, contradicting the ratified separate-authority category. The ratified model requires author memory to be a distinct store outside story canon.

3. **Reader simulation contradicts the ratified context-blind baseline.** The current `skills/reader-simulation/SKILL.md` lists character dossiers, story bible, continuity report, and narrative architecture as inputs — all privileged author context. Block C requires a manuscript-only first pass.

4. **Continuity claims mechanical checking but operates on model judgment.** The skill describes voice consistency, emotional progression, pressure-system consistency, and payoff timing as continuity checks. None of these are verifiable mechanically by the current schemas or any existing validator.

5. **Prose editing applies revisions directly without the ratified diagnosis/repair separation and batch-approval model.** The skill describes diagnosing findings and applying revisions in one workflow; it does not enforce separate diagnostic output, exact-batch presentation, per-item author disposition, or application of only approved changes.

6. **Context assembly does not exist.** Skills list inputs but define no reload contracts, no LOD strategy, no near/far policy, no provenance labeling for assembled context, and no conflict honoring rule between summaries and canonical sources.

7. **Dust & Ash–specific material (Thread Pull design, V4 pipeline, epistemic verb discipline, pressure-system vocabulary, Stephen King craft stance) remains embedded in the reusable core.** F2 designates extraction into an optional profile; extraction has not occurred.

### The smallest coherent implementation workstream

The smallest coherent workstream that exercises the ratified model end-to-end is a generic vertical slice that starts with a minimal project scaffold (story bible, one scene draft, one approved structured fact, one state file), exercises project initialization, one canonical promotion with a valid transaction and a rejected stale-revision transaction, one derived-view rebuild, one context-blind reader report, one editorial batch with diagnosis and per-change author disposition, schema and continuity validation, and execution on a second host for deterministic-invariant comparison. This slice does not require full LOD thresholds, full host adapters, all eleven skills, or Dust & Ash extraction.

### Decisions Dave must make before implementation

See Section 12 for the full decision register. The three highest-impact decisions are:

1. Whether `author_preferences` moves out of story-state.json into a separate author-memory store, or stays in place under a clarified non-canon authority label.
2. Whether the existing four-schema set is retained as the structured-state layer with field reclassification, or partially restructured (for example, extracting author memory, adding transaction/audit fields, adding cross-file reference integrity fields).
3. Whether the reader-simulation skill is required to implement a context-blind first pass now, or whether that is deferred until after the vertical slice.

### Recommendation for sequencing

Sequence from authority classification through schema responsibility and field alignment, then transaction/revision/audit contract, then validation and fixtures, then canon-promotion workflow, then derived-view rebuilding, then context assembly, then skill-contract alignment, then reader/editor HITL alignment, then Dust & Ash extraction, then host adapters and two-host evidence, then a generic vertical slice and CI. This order minimizes rework because later stages depend on the field responsibility map and the transaction contract; reversing the order would require reworking skill contracts and schema fields after the authority classification changes.

---

## 2. Scope and Authority

### Governing commit and documents

- **Ratification addendum:** commit `70861e660d7d7e5261482834397f5f6a97aa43d3`, files `docs/architecture/seven-source-synthesis-ratification-addendum.md`. This is the governing decision instrument. Where the addendum and the decision record address the same subject, the addendum controls.
- **Synthesis:** `docs/architecture/seven-source-synthesis-2026-08-27.md` (provisional recommendation, not ratified on its own).
- **Crosswalk:** `docs/crosswalk.md` (ratified patterns, deferred detail, prototype-only, source-informed candidates, rejected).
- **Decision record:** `docs/decisions/2026-08-26-alignment-evaluation.md` (historical August 26 record plus August 27 ratification note; superseded section handling applies).
- **Architecture overview:** `ARCHITECTURE.md` (ratified architecture, provisional prototype, deferred detail, unimplemented capabilities).
- **Source-analysis index:** `docs/source-analysis/README.md`.

### Planning-branch base

- **Base commit:** `c416472035ad6a4fdf7cfe47b5232e068e671e5f` — the clean integration commit that reproduces the accepted six-file documentation tree from `development@0e999a9`.
- **Parentage:** `c416472` has parent `0e999a9392683878a8cca9b1760cf92c81176c85`. The planning branch descends from the clean integration commit so it will retain normal ancestry after documentation merges into `development`.

### Files inspected

**Governing documents (all read in full):**
`ARCHITECTURE.md`, `docs/architecture/seven-source-synthesis-2026-08-27.md`, `docs/architecture/seven-source-synthesis-ratification-addendum.md`, `docs/crosswalk.md`, `docs/decisions/2026-08-26-alignment-evaluation.md`, `docs/source-analysis/README.md`.

**Schemas (all read in full):**
`schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, `schemas/continuity.schema.json`.

**Skills (all 11 read in full):**
`skills/fiction-orchestrator/SKILL.md`, `skills/concept-development/SKILL.md`, `skills/worldbuilding/SKILL.md`, `skills/character-development/SKILL.md`, `skills/narrative-architecture/SKILL.md`, `skills/scene-planning/SKILL.md`, `skills/scene-writing/SKILL.md`, `skills/continuity/SKILL.md`, `skills/prose-editing/SKILL.md`, `skills/reader-simulation/SKILL.md`, `skills/export/SKILL.md`.

**Templates (all 4 read in full):**
`templates/SKILL_TEMPLATE.md`, `templates/story-bible-template.md`, `templates/character-dossier-template.md`, `templates/scene-template.md`.

### Planning-only status

This is a planning and analysis document. It identifies proposed changes, confirmed gaps, ratified requirements, existing prototype behavior, deferred decisions, and recommended sequences. It does not implement any change. It does not modify any existing file.

### Explicit exclusions

- No existing file is modified by this document.
- No schema, skill, or template is changed.
- No validator, script, fixture, test, or CI artifact is created.
- No dependency is added or installed.
- No README, ATTRIBUTION, LICENSE, build report, or PROGRESS.md update is proposed here as an action item (licensing and provenance impacts are noted for awareness only).
- No merge, integration-branch push, pull request, or implementation is authorized by this document.
- No `development`, `main`, or disconnected architecture branch is altered.
- No force-push, rebase, reset, or history deletion occurs.
- No Dust & Ash extraction is begun.
- No deferred architectural decision is made on Dave's behalf.
- No proposed capability is described as already implemented.
- No validation pass is claimed based on JSON parsing alone.
- No judgment-based literary evaluation is presented as a deterministic claim.

---

## 3. Ratified Requirement Traceability

Each row identifies a ratified requirement, its governing clause, the files it affects, and current status. Status labels: **Ratified requirement**, **Existing prototype behavior**, **Confirmed gap**, **Proposed implementation detail**, **Deferred decision**, **No change required**.

| Requirement ID | Ratified requirement | Governing clause | Affected files | Current status |
|---|---|---|---|---|
| RR-1 | Approved Markdown manuscript files are authoritative for exact narrative wording and for what the reader encounters; no structured state field may silently rewrite approved prose. | Addendum Block A; ARCHITECTURE.md §1.1; crosswalk "Markdown authority for exact approved narrative wording" | All Markdown templates and manuscript outputs; all skills that produce or read prose | **Ratified requirement.** Prototype Markdown templates and skill outputs exist; the authority rule is ratified but not yet enforced by any tooling. |
| RR-2 | Approved structured state is authoritative for explicitly designated, approved machine-checkable canon facts and workflow fields only. These include state revisions, phase, phase_gate, character status, chapter sequence, scene outline/draft status, schema-validity fields, TODO type enums, and IDs used to route and cross-reference work. | Addendum Block A; ARCHITECTURE.md §1.1; crosswalk "Structured-state authority for explicitly governed, approved machine-checkable canon and workflow fields" | All four schemas; all skills that read or write structured state | **Ratified requirement.** The schemas define these categories. The exact field-by-field canon classification is not yet specified — it is the subject of this plan's schema impact analysis and remains a **proposed implementation detail** until Dave approves the reclassification. |
| RR-3 | A fact that first appears in prose is proposed structured state, not canon; it must pass the same gate as any other promotion candidate. | Addendum Block A; crosswalk "Canon-promotion requires author approval and provenance" | Character-state, scene-state, story-state schemas; narrative-architecture, scene-writing, continuity skills | **Ratified requirement.** The prototype does not yet implement a promotion gate or provenance capture for prose-originated facts. **Confirmed gap.** |
| RR-4 | Promotion into canon requires author approval for narrative content plus transaction validation for structured fields. A syntactically valid but semantically wrong update must still be resolved before it is written. | Addendum Block A; ARCHITECTURE.md §1.2 | All four schemas; orchestrator; concept-development; scene-planning; scene-writing; prose-editing; continuity | **Ratified requirement.** No transaction validation or approval-gated promotion exists in the prototype. **Confirmed gap.** |
| RR-5 | When Markdown and structured state disagree, the disagreement blocks publication or state promotion until an explicit reconciliation is recorded. The reconciliation must state which artifact wins and why; the loser's subsequent reads must report the same ruling. No layer may silently overwrite another. | Addendum Block A; ARCHITECTURE.md §1.1; crosswalk "Explicit conflict reconciliation; no silent overwrites" | All schemas; all skills; continuity skill; orchestrator | **Ratified requirement.** The prototype does not implement conflict blocking, reconciliation recording, or loser-side ruling propagation. **Confirmed gap.** |
| RR-6 | Derived views, summaries, indexes, registries, reports, and context packages are never authoritative and contain no unique facts; they are rebuildable projections from canonical project files. | Addendum Block A; ARCHITECTURE.md §1.1; crosswalk "Derived views and registries as non-authoritative and rebuildable" and "No unique facts in derived views" | All derived artifacts; context assembly; continuity reports; reader reports; export manuscript compilation | **Ratified requirement.** The prototype does not mark any current derived artifact as non-authoritative or rebuildable. **Confirmed gap.** |
| RR-7 | One transaction owns the transition from one canonical authority state to the next; the canonical authority advances only via that transaction. An expected-revision guard rejects stale sequential writes. The audit record captures who submitted what, what was applied, and what the check marked. | Addendum Block A; ARCHITECTURE.md §1.2; crosswalk "Transaction boundary and atomic-application requirement," "Expected-revision stale-write rejection," "Audit-history requirement" | All four schemas; orchestrator; concept-development; scene-planning; scene-writing; prose-editing; continuity; export | **Ratified requirement.** The schemas contain revision counters but no transaction boundary, expected-revision guard, or audit record. The orchestrator skill describes incrementing `state_revision` and validating, but no contract or tooling enforces atomic application. **Confirmed gap.** |
| RR-8 | A rollback is the establishment of the prior canonical revision or the application of a new compensating transaction that returns the canonical state to the prior intended revision. Partial failure is detected by schema/validation/coherence checks, the expected-revision guard, and any host-level write verification; if any part cannot be committed atomically, the system applies nothing to the canonical authority and records the rejection. | Addendum Block A; ARCHITECTURE.md §1.2 | All schemas; transaction tooling (not yet existing) | **Ratified requirement.** No rollback definition, failure detection, or rejection recording exists in the prototype. **Confirmed gap.** |
| RR-9 | The structured canon record must retain provenance pointing to the source passage, decision, or approval that established each promoted fact. Approval alone is not enough; the transaction must capture why the fact is now intended canon and where it came from. | Addendum Block A; crosswalk "Canon-promotion requires author approval and provenance" | Character-state (`source_lineage_note` exists), scene-state (`source_lineage_note` exists), story-state (no per-fact provenance field) | **Ratified requirement.** `source_lineage_note` exists on character-state and scene-state as a free-text field, but there is no structured provenance capture tying a promoted fact to a source passage, decision, or approval record. **Confirmed gap** between the ratified provenance requirement and the current free-text note. |
| RR-10 | The context-assembly layer has a minimum responsibility: identify the task and pull the smallest set of inputs that could plausibly change the output if omitted; separate current prose from structured or summarized material; keep derived overlays explicitly labeled; preserve a compact reviewable provenance note for what was assembled, from which revisions, and what was excluded; honor the conflict rule from Block A. | Addendum Block B; ARCHITECTURE.md §1.3 and §14; crosswalk "Minimum context-assembly responsibility," "Source-revision/provenance labeling in context packages," "Full prose when exact wording, voice, ambiguity, or rhythm matters" | All skills that receive context; orchestrator context package construction; reader-simulation; continuity; scene-writing | **Ratified requirement.** No context assembler exists. Skills list inputs but do not define reload contracts, LOD strategy, provenance labeling, or conflict honoring. **Confirmed gap.** |
| RR-11 | Every context package records the project/book identifiers, the scope, a compact source map, and the revision markers for the loaded items. The package does not assert authority beyond what the source map shows. | Addendum Block B; crosswalk "Source-revision/provenance labeling in context packages" | Orchestrator context package; all specialist skills | **Ratified requirement.** The orchestrator skill describes a context package that includes project identity, phase, relevant state excerpts, and existing artifact refs, but does not record revision markers or assert a source map with explicit authority boundaries. **Confirmed gap.** |
| RR-12 | Derived views serve different consumers differently: authors get readable drafts, story bible, dossiers, outline, chapter prose; writers get tight scene-oriented context with current character/state and relevant world facts; continuity/editors get structured state plus relevant prose windows and registry/current-state entries; readers via reader simulation get a manuscript-only view for the baseline pass and a separate labeled overlay only for the optional second pass. | Addendum Block B; ARCHITECTURE.md §1.3; crosswalk "Context-blind manuscript-only reader baseline" and "Optional informed second reader pass" | Reader-simulation skill; context assembly; continuity; scene-planning; scene-writing | **Ratified requirement.** The reader-simulation skill currently lists character dossiers, story bible, continuity report, and narrative architecture as inputs — the opposite of the mandated manuscript-only baseline. **Confirmed gap.** |
| RR-13 | A host is schema-aware if it can validate JSON against the schemas, apply defined structural/frontmatter/contract checks to Markdown where such rules exist, use judgment-based review for narrative content that cannot be mechanically validated, respect the authority and conflict rules, route by structure and IDs, run or reject operations whose required state is missing or invalid, and regenerate derived views from canonical files. | Addendum Block B; ARCHITECTURE.md §1.3; crosswalk "Host-neutral versus host-adapter boundary," "Deterministic versus judgment-based portability evidence," "Two-host evidence requirement" | All schemas; all skills; validator (not yet existing); continuity checker (not yet existing); derived-view rebuild (not yet existing) | **Ratified requirement.** No schema validator, no Markdown contract checks, no ID-based routing enforcement, no missing-state rejection, and no derived-view regeneration exist. **Confirmed gap.** |
| RR-14 | Host-neutral: Markdown/JSON inputs/outputs, schema validation, authority rules, conflict rules, derived-view regeneration, transaction record shape. Host adapter: prompt delivery, tool invocation, file access conventions, agent subprocess management, runtime logging, interaction surfaces, and any capability a particular runtime surfaces better than another. | Addendum Block B; ARCHITECTURE.md §1.3; crosswalk "Host-neutral versus host-adapter boundary" | All skills; orchestrator portability section; export skill | **Ratified requirement.** The orchestrator and export skills describe portability in general terms; no explicit host-neutral versus host-adapter boundary is drawn in the prototype. **Proposed implementation detail.** |
| RR-15 | Portability is demonstrated when the same generic project and same task produce comparable results on two hosts, the differences are documented and explainable as host-adaptation gaps rather than different canon, the authority/conflict rules produce the same resolution decisions on both hosts, and a derived view rebuild yields the same content from the same canonical files on both hosts. | Addendum Block B; ARCHITECTURE.md §1.3; crosswalk "Two-host evidence requirement" | All skills; vertical slice; CI | **Ratified requirement.** No two-host evidence exists. **Confirmed gap.** |
| RR-16 | Deterministic invariants — schema results, transaction acceptance or rejection, revision counters, promoted fact values, provenance records, audit entries, and regenerated registry contents — must match across hosts. | Addendum Block B; ARCHITECTURE.md §1.3; crosswalk "Deterministic versus judgment-based portability evidence" | Validator; transaction tooling; audit record; derived-view rebuild | **Ratified requirement.** No implementation exists to test deterministic invariants across hosts. **Confirmed gap.** |
| RR-17 | Judgment-based outputs — prose, editorial diagnosis, reader-simulation findings — must comply with the same scope and output contracts, but need not match in wording, emphasis, or conclusions. | Addendum Block B; ARCHITECTURE.md §1.3 and §16; crosswalk "Deterministic versus judgment-based portability evidence" | Prose-editing; reader-simulation; continuity (judgment-based categories) | **Ratified requirement.** The prototype does not formally separate deterministic from judgment-based output contracts. **Proposed implementation detail.** |
| RR-18 | Reader simulation begins with a context-blind manuscript-only pass. The blind pass delivers a reader's experiential report in its own words: what it understood, what it missed, where it lost interest, where it felt engaged, where it was confused, and where the ending landed. An optional second pass may load selected author context and add diagnostic interpretation, but the first pass stands alone and can be read without author privilege. | Addendum Block C; ARCHITECTURE.md §1.4 and §15; crosswalk "Context-blind manuscript-only reader baseline," "Optional informed second reader pass" | `skills/reader-simulation/SKILL.md` | **Ratified requirement.** The current reader-simulation skill loads character dossiers, story bible, continuity report, and narrative architecture as inputs. This contradicts the ratified baseline. **Confirmed gap.** |
| RR-19 | Editorial passes each have a declared scope and a declared stopping rule. Diagnosis and repair are separate: one pass produces findings; another pathway applies approved changes. | Addendum Block C; ARCHITECTURE.md §1.4 and §15; crosswalk "Focused editorial scopes and stopping rules," "Diagnosis separated from repair" | `skills/continuity/SKILL.md`, `skills/prose-editing/SKILL.md`, `skills/reader-simulation/SKILL.md` | **Ratified requirement.** The continuity and prose-editing skills describe finding production and revision, but do not enforce separate diagnosis output, declared stopping rules, or a separate repair pathway. **Confirmed gap.** |
| RR-20 | The substantive prose editing model is batch-approval: diagnose the scene/chapter for the declared editorial scope; present one coherent batch of exact proposed changes, each change localized enough to accept or reject individually; author accepts, rejects, or modifies individual changes; apply only the approved changes; approval of a general editing goal is not permission for unrestricted rewriting. | Addendum Block C; ARCHITECTURE.md §1.4 and §15; crosswalk "Exact batch-level editorial approval" | `skills/prose-editing/SKILL.md`; orchestrator; scene-writing | **Ratified requirement.** The prose-editing skill describes diagnosing findings and applying revisions in one workflow; it does not enforce exact-batch presentation, per-item author disposition, or application of only approved changes. **Confirmed gap.** |
| RR-21 | The system operates in one of two HITL modes. It must declare the mode before work begins, and it must not switch modes silently during a workflow. | Addendum Block C; ARCHITECTURE.md §1.4 and §15; crosswalk "Interactive and PR-boundary HITL modes," "No silent HITL mode switching" | Orchestrator; all skills that apply canon-affecting changes | **Ratified requirement.** No mode declaration, mode selection criteria, or anti-switching rule exists in the prototype. **Confirmed gap.** |
| RR-22 | Interactive mode: the author reviews and approves a proposed batch before it is applied to the working canonical artifact or state. Required when a change will be applied directly to the current canonical artifact or state before a branch/diff review, when the action has an external or destructive effect, or when the author has reserved that decision for interactive review. | Addendum Block C; ARCHITECTURE.md §1.4; crosswalk "Interactive and PR-boundary HITL modes" | Orchestrator; concept-development; scene-planning; scene-writing; prose-editing; continuity; export | **Ratified requirement.** The prototype does not distinguish interactive from PR-boundary mode. **Confirmed gap.** |
| RR-23 | PR-boundary mode: the agent may produce bounded canon-affecting proposals — prose edits, state patches, promotions, deletions, continuity updates — on an isolated non-canonical branch. Those proposals do not become canon unless the author approves and merges them. Permitted when no direct canonical mutation or external destructive action occurs before review. | Addendum Block C; ARCHITECTURE.md §1.4; crosswalk "Interactive and PR-boundary HITL modes" | Orchestrator; all canon-affecting skills | **Ratified requirement.** The prototype does not implement PR-boundary mode or a branch-based approval workflow. **Confirmed gap.** |
| RR-24 | Both HITL modes preserve the batch-approval rule. They differ in when and where the author reviews, not in whether substantive changes require approval. | Addendum Block C; crosswalk "Exact batch-level editorial approval" | Orchestrator; prose-editing; continuity; scene-writing | **Ratified requirement.** The batch-approval rule is not yet enforced in either mode. **Confirmed gap.** |
| RR-25 | Silent mode switching is not permitted; if new information during a workflow changes the appropriate mode, the system stops and asks for a fresh decision on the new scope before continuing. | Addendum Block C; ARCHITECTURE.md §1.4; crosswalk "No silent HITL mode switching" | Orchestrator; all skills | **Ratified requirement.** No anti-switching rule exists. **Confirmed gap.** |
| RR-26 | Framework approvals — state model, schema set, skill contracts, release decisions — belong to the framework track. Dust & Ash story phase gates belong to the Dust & Ash project track. They use different decision subjects and different approval records. | Addendum Block C; F2; ARCHITECTURE.md §1.4; crosswalk "Framework approvals separated from story gates" | Orchestrator phase gates; concept-development; scene-planning; scene-writing | **Ratified requirement.** The orchestrator skill describes phase gates without distinguishing framework-track approvals from Dust & Ash project-track approvals. **Proposed implementation detail** for clarifying which gate records belong to which track. |
| RR-27 | Existing JSON state model is a provisional implementation prototype, preserved but not ratified, until separately reviewed by a future, separately authorized file-by-file schema and skill impact plan. | F1; addendum context; ARCHITECTURE.md §2.2 and §13; crosswalk "Existing JSON state model is a provisional implementation prototype" | All four schemas | **Ratified requirement.** The schemas exist as a provisional prototype. No schema change is authorized by this document. **No change required** to the existing files; the impact analysis is the planned review. |
| RR-28 | Reusable core separated from optional Dust & Ash profile. Biblical/ANE/Stephen King/Gemini/Thread Pull requirements are designated for extraction into the optional Dust & Ash profile; generalizable reasoning principles remain in the core. | F2; addendum recommendation; ARCHITECTURE.md §13; crosswalk "Reusable core separated from optional Dust & Ash profile" | `skills/character-development/SKILL.md` (V4 pipeline), `skills/narrative-architecture/SKILL.md` (Thread Pull design), `skills/scene-planning/SKILL.md` (Thread Pull, dread/symbolic catalogs), `skills/scene-writing/SKILL.md` (Thread Pull execution, dread/symbolic deployment), `templates/scene-template.md` (thread_pulls, dread/symbolic columns), `templates/character-dossier-template.md` (Biblical/Historical Evidence Base, King Style-and-Craft Pressure Integration), `schemas/scene-state.schema.json` (dread_elements_used, symbolic_elements_used, thread_pulls_triggered) | **Ratified requirement.** The extraction has not occurred. Dust & Ash–specific material remains embedded in the reusable core. **Confirmed gap** between F2's designation and current file contents. |
| RR-29 | Separate author-memory authority category: author memory and preferences are a separate authority category from story canon and workflow state. | Addendum Block A; ARCHITECTURE.md §1.1; crosswalk "Separate author-memory authority category" | `schemas/story-state.schema.json` (`author_preferences` sub-object); author-memory store (not yet existing) | **Ratified requirement.** The authority category is ratified, but the author-profile store is not yet implemented. The current placement of `author_preferences` inside story-state.json conflicts with the ratified separate-authority category. **Confirmed gap.** |

---

## 4. Schema-by-Schema Impact Matrix

### 4.1 `schemas/story-state.schema.json`

**Current responsibility.** Top-level persistent state for a CodexWriter fiction project. One file per book. Holds project identity, phase, phase_gate, state_revision, characters, world, plot, timeline, chapters, open_questions, promises_payoffs, author_preferences, continuity_risks.

**Fields currently defined.** `project_id`, `book_id`, `title`, `phase`, `phase_gate`, `state_revision`, `created_at`, `updated_at`, `characters` (map of CharacterRef), `world` (WorldState), `plot` (PlotState), `timeline` (array), `chapters` (array of ChapterRef), `open_questions` (array), `promises_payoffs` (array), `author_preferences` (AuthorPreferences), `continuity_risks` (array).

**Authority category of each relevant field (proposed classification, not yet ratified):**

- `project_id`, `book_id`, `title` — **intended canon** (project identity, unlikely to derive from prose; if it does, promotion path applies).
- `phase`, `phase_gate` — **workflow/control state** (ratified workflow fields governed by the schema).
- `state_revision` — **workflow/control state** (ratified revision counter; must advance only via a validated transaction).
- `created_at`, `updated_at` — **workflow/control state** (metadata; not canon facts).
- `characters` — **intended canon references** (character_id, name, role_label, status, knowledge_level, current_state_ref, voice_ref, first_appearance_chapter, last_appearance_chapter, pressure_system). The map itself is a registry; individual character detail lives in character-state and Markdown dossiers.
- `world` — **intended canon** (settings, rules, cultural_context). World rules are machine-checkable canon; location status is workflow-flavored.
- `plot` — **intended canon** (arc_summary, arcs, beats). Beat order and arc status are machine-checkable intended canon.
- `timeline` — **intended canon** (event_id, description, canonical_order, textual_status, chapter_refs, sources). Timeline order and textual status are intended canon; sources carry provenance.
- `chapters` — **intended canon + workflow** (chapter_id, title, sequence_order, status, pov_character_ref, outline_ref, draft_ref, word_count, phase_when_written, state_revision_when_written). Sequence order and chapter existence are canon; status is workflow.
- `open_questions` — **workflow/control state** (question status, author decision). These track author decisions, not story truth.
- `promises_payoffs` — **intended canon** (promise_id, promise, type, setup_chapter_refs, payoff_status, payoff_chapter_ref, notes).
- `author_preferences` — **author memory** (style_profile, tone_axioms, forbidden_tropes, preferred_pov, tense, narrative_principles, evidence_labels, king_craft_stance). Under the ratified model, this is author memory, not story canon. Its current nesting inside story-state.json is the central conflict.
- `continuity_risks` — **editorial/diagnostic state** (flagged concerns from reviews). Not canon; rebuildable from continuity checks.

**Confirmed conflicts with the ratified model.**

1. `author_preferences` is nested inside story-state.json as a sub-object. The ratified model places author memory in a separate store outside story canon. This is a **confirmed gap** between the schema structure and the ratified authority category.
2. The schema has no transaction, expected-revision, or audit fields. The ratified model requires a transaction boundary, an expected-revision guard, and an audit record. This is a **confirmed gap**.
3. The schema has no per-fact provenance structure tying a promoted fact to a source passage, decision, or approval. `source_lineage_note` exists on character-state and scene-state but not on story-state fields that carry promoted canon facts. This is a **confirmed gap** with the ratified provenance requirement.
4. Cross-file reference integrity is not enforced by the schema. `pov_character_ref` in ChapterRef and `current_state_ref`/`voice_ref` in CharacterRef are free-text paths/IDs with no schema-level cross-reference validation. This is a **confirmed gap** with the ratified schema-aware portability requirement (routing by structure and IDs, rejecting operations whose required state is missing or invalid).

**Proposed field additions, removals, moves, or reclassification (proposed implementation detail, not ratified).**

- **Move:** Extract `author_preferences` from story-state.json into a separate author-memory schema/store. Recommended candidate path: `schemas/author-memory.schema.json` or an equivalent author-profile structure. This is a **proposed implementation detail**; the ratified requirement is the separation, not the exact path.
- **Add:** Transaction envelope fields to the state-update contract (not necessarily to the schema itself as stored fields — the transaction may be a separate record). Proposed candidate fields: `expected_revision`, `transaction_id`, `applied_by`, `applied_at`, `check_summary`, `audit_entry_ref`. This is a **proposed implementation detail**; the ratified requirement is the transaction boundary and audit record, not these exact field names.
- **Reclassify:** Mark `continuity_risks` explicitly as editorial/diagnostic state rather than canon. This is a **proposed reclassification** consistent with the ratified authority model.
- **Add:** Cross-file reference integrity fields or validation rules (for example, `chapter_id` references in timeline and promises_payoffs should be validated against the chapters array; `pov_character_ref` should match a known character_id). This is a **proposed implementation detail** consistent with the ratified schema-aware portability requirement.

**Revision and stale-write implications.** `state_revision` is the canonical counter for story-state. Any transaction that advances story-state must carry an expected_revision and must be rejected if it does not match. The orchestrator skill currently describes incrementing `state_revision` without an expected-revision guard. The ratified model requires rejection of stale writes.

**Provenance and audit implications.** If `author_preferences` moves out of story-state, the story-state audit record no longer carries author-preference changes as story-state transactions. Author-memory updates would carry their own provenance and audit trail. If `continuity_risks` is reclassified as editorial/diagnostic state, its provenance should point to the review or check that produced it, not to story canon.

**Cross-file references.** Story-state references character-state via `characters[].current_state_ref` and `characters[].voice_ref`; references scene-state via `chapters[].outline_ref` and `chapters[].draft_ref`; references continuity-state indirectly via `continuity_risks`. These references are currently free-text; the ratified model requires routing by structure and IDs.

**Migration/backward-compatibility concerns.** If `author_preferences` is removed from story-state.json, any existing project instance that relies on that field would need a migration path — either a co-existence period where both locations are read, or a one-time migration. This is a **deferred decision** (whether to support a migration window, and what the default author-memory content should be for existing projects).

**Tests eventually required.** Schema validation of story-state instances; transaction acceptance/rejection based on expected_revision; rejection of semantically invalid but syntactically valid updates; audit-record creation on each applied transaction; cross-file reference integrity checks; reclassification consistency (author_preferences is no longer read as story canon).

**Deferred decisions.** Whether `author_preferences` moves to a separate file, a separate schema, or a separate store; whether transaction/audit fields are stored inside story-state.json or in a separate transaction/audit log; whether `continuity_risks` stays in story-state.json under a clearer editorial label or moves to a derived continuity view.

---

### 4.2 `schemas/character-state.schema.json`

**Current responsibility.** Current dynamic state for a character — what they know, feel, and carry into the next scene. Separate from static dossier (voice, backstory, design).

**Fields currently defined.** `character_id`, `name`, `current_state_revision`, `knowledge` (knows_about, does_not_know, misconceptions, uncertain_about), `emotional_state` (dominant_emotions, pressure_level, recent_trigger, suppressed_feelings), `physical_state` (injured, injury_description, fatigue_level, physical_tells, carried_objects), `carried_pressure`, `last_seen_chapter`, `last_updated_by`, `updated_at`, `source_lineage_note`.

**Authority category of each relevant field (proposed classification):**

- `character_id`, `name` — **intended canon** (identity facts; `character_id` must match the character_id in story-state).
- `current_state_revision` — **workflow/control state** (monotonic counter; must advance only via a validated transaction).
- `knowledge` — **intended canon** (what the character knows at this point). This is machine-checkable intended canon for continuity knowledge checks. Knowledge items that originate in prose are proposed canon until promoted.
- `emotional_state` — **derivation boundary.** Dominant emotions, pressure_level, recent_trigger, suppressed_feelings are partly observable from prose and partly inference. Under the ratified model, inferred emotional state should carry provenance and should be treated as proposed structured state until approved. This is a **proposed reclassification**; the current schema treats emotional_state as a single field without a canon/derived distinction.
- `physical_state` — **intended canon where observable; derivation where inferred.** injured, injury_description, fatigue_level, physical_tells, carried_objects may be directly observable in prose or may be inferred. The schema does not currently distinguish these.
- `carried_pressure` — **intended canon** (the pressure the character carries into the next scene; this is a machine-checkable narrative fact).
- `last_seen_chapter` — **workflow/control state + cross-file reference** (chapter_id where the character was last active; must match an existing chapter_id).
- `last_updated_by` — **workflow/control state** (which skill or agent last updated the state).
- `updated_at` — **workflow/control state** (timestamp).
- `source_lineage_note` — **provenance / editorial state** (how the state was derived). This is the closest existing field to the ratified provenance requirement, but it is free-text and not structured enough to serve as a promotion-linked provenance record.

**Confirmed conflicts with the ratified model.**

1. `source_lineage_note` is free-text and does not capture structured provenance linking a promoted fact to a source passage, decision, or approval. This is a **confirmed gap** with the ratified provenance requirement.
2. `emotional_state` and parts of `physical_state` mix observable canon with inference without a derived/approved distinction. The ratified model requires promoted facts to be approved and requires inference to be labeled. This is a **confirmed gap**.
3. No transaction, expected-revision, or audit fields. `current_state_revision` exists but no guard rejects stale updates. This is a **confirmed gap**.
4. `last_seen_chapter` is a free-text string with no schema-level cross-reference validation against the chapters array in story-state. This is a **confirmed gap** with the ratified schema-aware portability requirement.

**Proposed field additions, removals, moves, or reclassification (proposed implementation detail).**

- **Add:** Structured provenance fields for promoted knowledge and state changes (for example, `promotion_ref`, `source_passage_ref`, `approval_record_ref`, or a nested `provenance` object). This is a **proposed implementation detail** consistent with the ratified provenance requirement.
- **Reclassify:** Split `emotional_state` and `physical_state` into observable canon sub-fields and inference sub-fields, with inference fields carrying provenance and approval status. This is a **proposed reclassification**.
- **Add:** Transaction envelope fields for character-state updates (`expected_current_state_revision`, `transaction_id`, `audit_entry_ref`). This is a **proposed implementation detail**.
- **Add:** Cross-reference validation for `last_seen_chapter` against known chapter_ids. This is a **proposed implementation detail** consistent with the ratified schema-aware portability requirement.

**Revision and stale-write implications.** `current_state_revision` is the canonical counter for character-state. Any transaction that advances character-state must carry an expected_current_state_revision and be rejected if it does not match. A character-state update that changes knowledge, emotional_state, or physical_state without a valid transaction must be rejected.

**Provenance and audit implications.** Each promoted knowledge item should carry provenance. The existing `source_lineage_note` may become a human-readable summary of a structured provenance record, but it cannot replace structured provenance.

**Cross-file references.** `character_id` must match story-state's characters map; `last_seen_chapter` must reference a valid chapter_id. The schema does not currently enforce these cross-file relationships.

**Migration/backward-compatibility concerns.** If `knowledge`, `emotional_state`, or `physical_state` are reclassified into canon/inference sub-structures, existing instances would need migration or a reader that understands both shapes during a transition window. This is a **deferred decision**.

**Tests eventually required.** Schema validation; transaction acceptance/rejection; provenance capture on promotion; cross-file reference integrity; distinction between observable canon and inference; rejection of stale character-state updates.

**Deferred decisions.** Whether inference fields are stored in the same file under a distinct sub-structure or in a separate inference/derived record; whether `source_lineage_note` is replaced by structured provenance or retained as a summary; whether emotional_state and physical_state are split now or after the first vertical slice.

---

### 4.3 `schemas/scene-state.schema.json`

**Current responsibility.** State tracking for a single scene — outline, draft status, continuity notes, and beat-level tracking.

**Fields currently defined.** `scene_id`, `chapter_id`, `scene_number_in_chapter`, `title`, `pov_character_id`, `setting_ref`, `outline_status`, `draft_status`, `scene_revision`, `beats`, `outline_ref`, `draft_ref`, `word_count`, `dread_elements_used`, `symbolic_elements_used`, `thread_pulls_triggered`, `continuity_notes`, `evaluation_notes`, `author_approval`, `updated_at`, `source_lineage_note`.

**Authority category of each relevant field (proposed classification):**

- `scene_id`, `chapter_id`, `scene_number_in_chapter` — **intended canon + workflow** (scene identity and position; `scene_id` and `chapter_id` must match known IDs).
- `title` — **derived or convenience data** (optional scene title; not narrative prose; may be editorial convenience).
- `pov_character_id` — **intended canon** (which character's perspective the scene is anchored to; machine-checkable).
- `setting_ref` — **intended canon reference** (location_id where the scene takes place).
- `outline_status`, `draft_status` — **workflow/control state** (ratified workflow fields; must advance via approved transitions).
- `scene_revision` — **workflow/control state** (monotonic counter; must advance only via a validated transaction).
- `beats` — **intended canon** (beat_number, description, emotional_target, dread_element, symbolic_element, thread_pull_ref, knowledge_state_before, knowledge_state_after). Beat descriptions are planning canon; emotional_target, dread_element, symbolic_element are planning intent, not narrative prose.
- `outline_ref`, `draft_ref` — **workflow/control state references** (paths to outline and draft documents).
- `word_count` — **derived or convenience data** (measurable count; not canon prose).
- `dread_elements_used`, `symbolic_elements_used` — **Dust & Ash profile material** (these fields exist to track Stephen King–style dread and symbolic deployment; under F2 they are designated for extraction into the optional Dust & Ash profile). In the reusable core, they may become optional or profile-specific.
- `thread_pulls_triggered` — **Dust & Ash profile material** (Thread Pull design is F2-designated for extraction). The schema field is currently in the reusable core.
- `continuity_notes` — **editorial/diagnostic state** (notes about what changed during the scene; recorded by scene-writing for continuity input). Not canon; rebuildable from the draft and state.
- `evaluation_notes` — **editorial/diagnostic state** (evaluator findings). Not canon.
- `author_approval` — **workflow/control state** (human gate status for outline and draft).
- `updated_at` — **workflow/control state** (timestamp).
- `source_lineage_note` — **provenance / editorial state** (how the scene state was derived).

**Confirmed conflicts with the ratified model.**

1. `dread_elements_used`, `symbolic_elements_used`, and `thread_pulls_triggered` are Dust & Ash–specific fields embedded in the reusable core schema. This conflicts with F2's designation of Thread Pull and Stephen King craft material for extraction into the optional Dust & Ash profile. This is a **confirmed gap** between F2 and the current schema.
2. `continuity_notes` and `evaluation_notes` are editorial/diagnostic state but are stored alongside canon and workflow fields without a clear authority boundary. The ratified model requires derived and editorial state to be clearly non-authoritative. This is a **confirmed gap** in classification, though not necessarily a field removal.
3. `source_lineage_note` is free-text and does not capture structured provenance for promoted facts. This is a **confirmed gap** with the ratified provenance requirement.
4. No transaction, expected-revision, or audit fields. `scene_revision` exists but no guard rejects stale updates. This is a **confirmed gap**.
5. `pov_character_id` and `setting_ref` are free-text references with no schema-level cross-reference validation against character-state and worldbuilding. This is a **confirmed gap** with the ratified schema-aware portability requirement.

**Proposed field additions, removals, moves, or reclassification (proposed implementation detail).**

- **Extract / move:** `dread_elements_used`, `symbolic_elements_used`, and `thread_pulls_triggered` should be evaluated for placement in a Dust & Ash profile schema or a profile-specific extension rather than the reusable core schema. This is a **proposed implementation detail** driven by F2.
- **Reclassify:** Mark `continuity_notes`, `evaluation_notes`, `word_count`, and `title` explicitly as non-authoritative (editorial/derived/convenience). This is a **proposed reclassification** consistent with the ratified authority model.
- **Add:** Transaction envelope fields for scene-state updates (`expected_scene_revision`, `transaction_id`, `audit_entry_ref`). This is a **proposed implementation detail**.
- **Add:** Cross-reference validation for `pov_character_id` against known character_ids and `setting_ref` against known location_ids. This is a **proposed implementation detail** consistent with the ratified schema-aware portability requirement.
- **Add:** Structured provenance for beat-level knowledge_state_before/knowledge_state_after changes if those are promoted canon facts. This is a **proposed implementation detail**.

**Revision and stale-write implications.** `scene_revision` is the canonical counter for scene-state. Any transaction that advances scene-state must carry an expected_scene_revision and be rejected if it does not match. Scene-state updates after drafting and after revision must both go through the transaction guard.

**Provenance and audit implications.** If beat-level knowledge changes are promoted canon, they need provenance. `source_lineage_note` may summarize provenance but cannot replace it.

**Cross-file references.** `scene_id` must be unique within the project; `chapter_id` must reference a valid chapter; `pov_character_id` must reference a valid character; `setting_ref` must reference a valid location; `thread_pull_ref` in beats must reference a known thread pull definition (if Thread Pulls are retained in core or moved to profile).

**Migration/backward-compatibility concerns.** If Dust & Ash fields are extracted, existing scene-state instances that contain those fields would need a profile-aware reader or a migration. This is a **deferred decision**.

**Tests eventually required.** Schema validation; transaction acceptance/rejection; cross-file reference integrity; reclassification consistency; Dust & Ash field portability between core and profile; rejection of stale scene-state updates.

**Deferred decisions.** Whether Dust & Ash fields are removed from the core schema, retained under a profile-conditional marker, or moved to a profile schema; whether `continuity_notes` stays in scene-state.json or moves to a derived continuity view; whether `evaluation_notes` is standardized into the shared findings/disposition schema.

---

### 4.4 `schemas/continuity.schema.json`

**Current responsibility.** Continuity tracking — cross-scene contradictions, knowledge consistency, timeline ordering, and promise/payoff validation.

**Fields currently defined.** `continuity_revision`, `last_check_at`, `last_check_by`, `character_consistency`, `timeline_consistency`, `knowledge_consistency`, `promise_consistency`, `open_contradictions`, `check_history`.

**Authority category of each relevant field:**

- `continuity_revision` — **workflow/control state** (monotonic counter for continuity checks; must advance only via a validated check transaction).
- `last_check_at`, `last_check_by` — **workflow/control state** (check metadata).
- `character_consistency`, `timeline_consistency`, `knowledge_consistency`, `promise_consistency` — **editorial/diagnostic state** (check results). These are findings, not canon. They are rebuildable from the canonical state and the manuscript.
- `open_contradictions` — **editorial/diagnostic state** (known unresolved contradictions). Not canon; flagged for author resolution.
- `check_history` — **audit history** (log of each continuity check run). This is the closest existing structure to the ratified audit-history requirement, but it is a continuity-specific log, not a general canonical audit record.

**Confirmed conflicts with the ratified model.**

1. The continuity schema is diagnostic/editorial state, but the ratified model requires a general audit record for canonical transactions, not only continuity checks. The current `check_history` is a continuity log, not a canonical audit record. This is a **confirmed gap** with the ratified audit-history requirement.
2. The continuity schema does not distinguish mechanically checkable categories from judgment-based categories. The skill describes voice consistency, emotional progression, pressure-system consistency, and payoff timing as continuity checks; these are judgment-based. The schema has no field that classifies a check as deterministic versus judgment-based. This is a **confirmed gap** with the ratified deterministic-versus-judgment-based distinction.
3. The continuity schema does not carry structured provenance for how a finding was produced (which source passage, which state field, which check rule). This is a **confirmed gap** with the ratified provenance requirement as applied to diagnostic output.
4. No transaction, expected-revision, or audit fields for the continuity update itself. `continuity_revision` exists but no guard rejects stale continuity writes. This is a **confirmed gap**.

**Proposed field additions, removals, moves, or reclassification (proposed implementation detail).**

- **Add:** A `check_type_classification` field (or equivalent) on each check item to distinguish deterministic from judgment-based checks. This is a **proposed implementation detail** consistent with the ratified quality principle.
- **Add:** Shared finding envelope fields consistent across continuity, prose-editing, and any other diagnostic skill (for example, `finding_id`, `scope`, `location`, `description`, `evidence`, `confidence`, `determinism`, `recommended_action`, `author_disposition`, `resolution_notes`). The ratification addendum references a shared envelope with confidence/determinism classification as deferred detail. This is a **proposed implementation detail**.
- **Add:** Transaction envelope fields for continuity updates (`expected_continuity_revision`, `transaction_id`, `audit_entry_ref`). This is a **proposed implementation detail**.
- **Reclassify:** Mark continuity check results explicitly as non-authoritative derived/editorial state. This is a **proposed reclassification** consistent with the ratified authority model.
- **Add:** Cross-reference fields linking findings to canonical locations (character_id, chapter_id, scene_id, event_id, promise_id) with validated IDs. This is a **proposed implementation detail** consistent with the ratified schema-aware portability requirement.

**Revision and stale-write implications.** `continuity_revision` is the canonical counter for continuity-state. A continuity check that writes a new continuity-state must carry an expected_continuity_revision and be rejected if it does not match.

**Provenance and audit implications.** Each finding should record what was checked, against which canonical revision, with what rule, and with what classification. The existing `check_history` should be aligned with the general audit record so that continuity checks are part of the canonical audit trail, not a separate log.

**Cross-file references.** Findings in `character_consistency` reference `character_id`; `timeline_consistency` references event pairs; `knowledge_consistency` references `character_id` and `knowledge_item`; `promise_consistency` references `promise_id`. These references should be validated against the canonical state.

**Migration/backward-compatibility concerns.** If a shared finding envelope is adopted, existing continuity-state instances would need migration or a reader that handles both shapes. This is a **deferred decision**.

**Tests eventually required.** Schema validation; transaction acceptance/rejection; deterministic versus judgment-based classification; cross-file reference integrity; audit-history creation; reproducibility of continuity findings from canonical state plus manuscript.

**Deferred decisions.** Whether continuity-state becomes a derived view rebuilt from canonical state plus manuscript rather than a separately written state file; whether `check_history` is merged into a general audit log; whether the shared finding envelope is defined now or after the vertical slice.

---

## 5. Skill-by-Skill Impact Matrix

### 5.1 `skills/fiction-orchestrator/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| fiction-orchestrator | Entry point, intent routing, phase-gate enforcement, context-package construction, state-update coordination, specialist handoffs. | RR-1 through RR-29; especially RR-2, RR-4, RR-5, RR-7, RR-10, RR-11, RR-21, RR-22, RR-23, RR-24, RR-25, RR-26, RR-28, RR-29. | 1. Context package does not record revision markers or a source map with authority boundaries (RR-11). 2. State updates are described as increment-and-validate without a transaction boundary, expected-revision guard, or audit record (RR-7, RR-9). 3. No HITL mode declaration, mode selection criteria, or anti-switching rule (RR-21, RR-22, RR-23, RR-24, RR-25). 4. Phase gates are described without distinguishing framework-track approvals from Dust & Ash project-track approvals (RR-26). 5. `story-state.json` is described as "the canonical machine-readable state" without the layered hybrid nuance that Markdown is authoritative for exact wording and structured state is authoritative only for explicitly governed fields (RR-1, RR-2). | 1. Redefine context-package contract to include project/book identifiers, scope, compact source map, revision markers, and explicit authority boundaries. 2. Redefine state-update contract as a transaction: propose patch, check expected_revision, validate against schema and cross-file consistency, apply atomically, rebuild derived views, record audit entry. 3. Add HITL mode declaration and selection criteria to the orchestrator contract; require mode to be stated before work begins; forbid silent switching. 4. Split phase-gate records into framework-track and Dust & Ash project-track approval records. 5. Update authority language to reflect the layered hybrid model: Markdown authoritative for exact wording; structured state authoritative only for explicitly governed fields; derived views non-authoritative. | Interactive for direct canonical mutation; PR-boundary for bounded proposals on an isolated branch. Mode must be declared before work begins. | All four schemas; all specialist skills; author-memory store (proposed); transaction/audit contract (proposed); context-package contract (proposed); derived-view rebuild (proposed). | Schema validation of story-state; transaction acceptance/rejection; stale-revision rejection; audit-record creation; context-package provenance; HITL mode declaration; framework-vs-project-gate separation. | **Proposed contract changes required.** The orchestrator is the central skill affected by the ratified model. Its current contract is prototype behavior; the ratified requirements affect routing, context assembly, state updates, HITL mode, and gate separation. |

### 5.2 `skills/concept-development/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| concept-development | Phase 1 concept exploration, story bible assembly, story-state.json initialization, Gate 1 approval. | RR-1, RR-2, RR-3, RR-4, RR-5, RR-7, RR-9, RR-10, RR-11, RR-18 (indirect, because concept output becomes manuscript later), RR-26, RR-28 (if story bible tone/style fields carry Dust & Ash content). | 1. Initialization writes story-state.json with `state_revision = 1` and `phase = concept` but does not go through a transaction with expected_revision, audit, or provenance (RR-7, RR-9). 2. The story bible template includes Dust & Ash–adjacent fields (style profile, tone axioms, narrative principles) but does not separate reusable-core preference fields from project-profile fields (RR-28, RR-29). 3. No structured provenance for the creative contract's approved facts (RR-9). | 1. Treat project initialization as a canonical transaction: initialize state, set expected_revision, validate, apply atomically, record audit entry. 2. Clarify which story-bible fields are reusable-core canon/workflow versus optional profile content. 3. Add provenance capture for author-approved concept facts that later become structured canon. | Interactive (initialization is a direct canonical mutation before any branch/diff review). | Story-bible template; story-state schema; orchestrator; author-memory store (proposed). | Initialization validation; transaction acceptance; audit entry; story-bible field classification; provenance for approved concept facts. | **Proposed contract changes required.** Initialization is a canonical transaction under the ratified model; the current skill describes it as a direct write. |

### 5.3 `skills/worldbuilding/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| worldbuilding | Phase 2 worldbuilding artifacts, world rules codification, story-state.json world field updates. | RR-1, RR-2, RR-3, RR-4, RR-5, RR-7, RR-9, RR-10, RR-11, RR-28 (if world rules carry project-specific content). | 1. State updates (world.settings, world.rules, world.cultural_context) are described as direct writes without a transaction boundary, expected-revision guard, or audit record (RR-7, RR-9). 2. World rules are codified for continuity checking but the codified rules are not linked to provenance or approval (RR-9). 3. No context reload contract or provenance labeling for the assembled world context (RR-10, RR-11). | 1. Treat worldbuilding state updates as canonical transactions. 2. Add provenance for codified world rules (source, rationale, approval). 3. Define reload context for worldbuilding-dependent skills. | Interactive for direct canonical mutation. | Story-state schema; worldbuilding Markdown artifacts; continuity skill; orchestrator. | Transaction acceptance; provenance for world rules; cross-file reference integrity (location_id, rule_id). | **Proposed contract changes required.** The skill's state-update path needs transaction alignment. |

### 5.4 `skills/character-development/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| character-development | Phase 2 character dossier creation using the V4 pipeline; story-state.json character reference updates; character-state creation. | RR-1, RR-2, RR-3, RR-4, RR-5, RR-7, RR-9, RR-10, RR-11, RR-28 (V4 pipeline, Biblical evidence extraction, King craft integration, epistemic verb discipline, pressure-system vocabulary are F2-designated for extraction), RR-29. | 1. The V4 pipeline is Dust & Ash–specific (Biblical evidence tiers, King corpus as style engine, Stephen King craft stance, Abram-as-format-reference rule) and remains embedded in the reusable core skill (RR-28). 2. State updates (story-state character references, character-state creation) are not transacted (RR-7, RR-9). 3. `source_lineage_note` exists but is free-text and does not capture structured promotion provenance (RR-9). 4. Character-state emotional_state and physical_state mix observable canon with inference without a derived/approved distinction (RR-2, RR-9). 5. The dossier template includes Biblical/Historical Evidence Base and King Style-and-Craft Pressure Integration sections that are Dust & Ash profile material (RR-28). | 1. Extract the V4 pipeline, Biblical evidence tiers, King craft integration, and epistemic verb discipline into the optional Dust & Ash profile; retain generalizable pressure-system and contamination-prevention principles in the core. 2. Treat character-state creation and updates as canonical transactions with provenance. 3. Reclassify character-state fields into observable canon and inference sub-structures with provenance. 4. Move or profile-condition the dossier template's Biblical/Historical Evidence Base and King Style-and-Craft Pressure Integration sections. | Interactive for direct canonical mutation. | Character-dossier template; character-state schema; story-state schema; orchestrator; author-memory store (proposed). | Transaction acceptance; provenance for promoted character facts; Dust & Ash field extraction; cross-file reference integrity (character_id). | **Proposed contract changes required.** This skill carries the largest Dust & Ash contamination in the reusable core; F2 extraction is a confirmed gap. |

### 5.5 `skills/narrative-architecture/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| narrative-architecture | Phase 3 plot architecture, arc/beat/scene/chapter outline, Thread Pull integration, promise/payoff mapping, story-state.json plot/timeline updates. | RR-1, RR-2, RR-3, RR-4, RR-5, RR-7, RR-9, RR-10, RR-11, RR-28 (Thread Pull design is F2-designated for extraction). | 1. Thread Pull design (trigger artifacts, thread types, sensory ghosts, felt-by-character) is embedded in the reusable core skill (RR-28). 2. State updates (plot.arcs, plot.beats, timeline) are not transacted (RR-7, RR-9). 3. Promise/payoff mapping is intended canon but has no structured provenance for setup/payoff approval (RR-9). 4. No context reload contract or provenance labeling for the assembled architecture context (RR-10, RR-11). | 1. Extract Thread Pull design into the optional Dust & Ash profile; retain arc/beat/scene/chapter structure and promise/payoff tracking in the core. 2. Treat architecture state updates as canonical transactions with provenance. 3. Add provenance for approved promise/payoff status. | Interactive for direct canonical mutation. | Story-state schema; narrative architecture Markdown artifacts; scene-planning; scene-writing; continuity. | Transaction acceptance; provenance for promise/payoff; cross-file reference integrity (arc_id, beat_id, chapter_id, promise_id). | **Proposed contract changes required.** Thread Pull extraction is a confirmed gap under F2. |

### 5.6 `skills/scene-planning/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| scene-planning | Phase 3/4 scene outline creation, beat-level breakdown, dread/symbolic/Thread Pull planning, continuity note mapping, scene-state.json updates. | RR-1, RR-2, RR-3, RR-4, RR-5, RR-7, RR-9, RR-10, RR-11, RR-28 (dread elements, symbolic elements, Thread Pull planning are F2-designated for extraction). | 1. Dread element catalog, symbolic element catalog, and Thread Pull planning are Dust & Ash–specific and embedded in the reusable core skill (RR-28). 2. State updates (scene entry creation, beats) are not transacted (RR-7, RR-9). 3. Outline approval is described as setting `outline_status → outline_approved` without a transaction or audit record (RR-7). 4. No context reload contract or provenance labeling for the assembled scene context (RR-10, RR-11). | 1. Extract dread/symbolic/Thread Pull planning into the optional Dust & Ash profile; retain beat-level planning, knowledge-state change mapping, and continuity note mapping in the core. 2. Treat scene-state updates as canonical transactions with provenance. 3. Reconcile outline approval with the ratified batch-approval and HITL mode rules. | Interactive for direct canonical mutation. | Scene template; scene-state schema; character-state schema; story-state schema; character dossier; worldbuilding. | Transaction acceptance; outline approval audit; cross-file reference integrity (scene_id, chapter_id, pov_character_id); Dust & Ash field extraction. | **Proposed contract changes required.** Dread/symbolic/Thread Pull extraction is a confirmed gap under F2. |

### 5.7 `skills/scene-writing/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| scene-writing | Phase 4 prose drafting from approved scene outline; voice preservation; knowledge-constraint respect; Thread Pull execution; continuity note recording; scene-state.json and story-state.json updates. | RR-1, RR-2, RR-3, RR-4, RR-5, RR-7, RR-9, RR-10, RR-11, RR-20 (indirect, because scene-writing produces the draft that prose-editing later diagnoses), RR-21, RR-22, RR-28 (Thread Pull execution, dread/symbolic deployment are F2-designated for extraction). | 1. Thread Pull execution and dread/symbolic deployment instructions are Dust & Ash–specific and embedded in the reusable core skill (RR-28). 2. State updates (draft_status, draft_ref, word_count, scene_revision, dread_elements_used, symbolic_elements_used, thread_pulls_triggered, continuity_notes) are not transacted (RR-7, RR-9). 3. Continuity notes are recorded as scene-state fields but are editorial/diagnostic state without a clear non-authoritative classification (RR-6, RR-2). 4. No HITL mode declaration for the drafting operation (RR-21, RR-22). 5. No provenance for knowledge-state changes that become canon (RR-9). | 1. Extract Thread Pull execution and dread/symbolic deployment into the optional Dust & Ash profile; retain beat execution, emotional target rendering, voice preservation, knowledge-constraint respect, and continuity-note recording in the core. 2. Treat scene-state and story-state updates after drafting as canonical transactions. 3. Reclassify continuity_notes as editorial/diagnostic state. 4. Declare HITL mode for drafting (interactive if the draft is applied to canonical before review; PR-boundary if the draft is proposed on a branch). 5. Add provenance for knowledge-state changes that are promoted canon. | Interactive if the draft becomes canonical before review; PR-boundary if the draft is proposed on a branch. | Scene template; scene-state schema; character-state schema; story-state schema; character dossier; worldbuilding; scene outline. | Transaction acceptance; cross-file reference integrity (scene_id, chapter_id, pov_character_id); Dust & Ash field extraction; voice preservation judgment-contract compliance; knowledge-constraint deterministic checks. | **Proposed contract changes required.** Thread Pull extraction is a confirmed gap under F2; state updates need transaction alignment. |

### 5.8 `skills/continuity/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| continuity | Phase 4/5 continuity checking: schema validation, character/timeline/knowledge/promise consistency checks, continuity-state.json update, continuity report. | RR-1, RR-2, RR-4, RR-5, RR-6, RR-7, RR-9, RR-10, RR-11, RR-13, RR-18 (indirect), RR-19, RR-20, RR-21, RR-22, RR-28 (indirect, because continuity checks may evaluate Dust & Ash profile content). | 1. The skill describes checks that the orchestrator calls "mechanical" but that require model judgment — voice consistency, emotional progression, pressure-system consistency, payoff timing. The schema has no deterministic-versus-judgment-based classification (RR-17, RR-19). 2. Continuity-state is written as a separate state file without a transaction boundary, expected-revision guard, or audit record (RR-7). 3. `check_history` is a continuity log, not a general canonical audit record (RR-7, RR-9). 4. Findings are not structured with a shared envelope that includes confidence/determinism classification (RR-19). 5. No declared stopping rule for the continuity pass (RR-19). 6. Continuity results are described as blocking progression without distinguishing interactive from PR-boundary mode (RR-21, RR-22, RR-23). 7. Continuity checks are described as if they are deterministic; the ratified model requires explicit classification of which findings are mechanical and which are judgment-based (RR-16, RR-17). | 1. Add deterministic-versus-judgment-based classification to each check type. 2. Treat continuity-state updates as canonical transactions with expected-revision and audit. 3. Align continuity findings with a shared finding envelope (confidence, determinism, scope, location, evidence, recommended action, author disposition, resolution notes). 4. Declare a stopping rule for the continuity pass. 5. Require HITL mode declaration for continuity findings that block progression. 6. Evaluate whether continuity-state becomes a derived view rebuilt from canonical state plus manuscript rather than a separately written state file. 7. Ensure continuity checks do not silently resolve Markdown/structured-state conflicts (RR-5). | Interactive if findings are applied to canonical state before review; PR-boundary if findings are proposed on a branch. Mode must be declared. | Continuity schema; story-state schema; character-state schema; scene-state schema; manuscript; orchestrator; transaction/audit contract (proposed); shared finding envelope (proposed). | Schema validation; deterministic check reproducibility; judgment-based output contract compliance; transaction acceptance/rejection; audit-history creation; cross-file reference integrity; conflict-blocking enforcement; derived-view rebuild alignment. | **Proposed contract changes required.** Continuity is the skill most affected by the deterministic-versus-judgment-based gap and the transaction/audit gap. |

### 5.9 `skills/prose-editing/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| prose-editing | Phase 5 prose revision: voice fidelity, pacing, clarity, emotional impact, style consistency assessment; revision application; editing notes recording; scene-state.json updates. | RR-1, RR-2, RR-4, RR-5, RR-6, RR-7, RR-9, RR-10, RR-11, RR-19, RR-20, RR-21, RR-22, RR-23, RR-24, RR-25. | 1. The skill describes diagnosing findings and applying revisions in one workflow; it does not enforce separate diagnostic output, declared stopping rules, or a separate repair pathway (RR-19). 2. The skill does not enforce exact-batch presentation, per-item author disposition, or application of only approved changes (RR-20). 3. The skill applies revisions directly to the draft without HITL mode declaration or interactive/PR-boundary distinction (RR-21, RR-22, RR-23, RR-24, RR-25). 4. `evaluation_notes` are recorded in scene-state but are editorial/diagnostic state without a clear non-authoritative classification or shared envelope (RR-6, RR-19). 5. No provenance for approved editorial changes that affect canonical state (RR-9). | 1. Separate diagnosis from repair: one pass produces findings; another pathway applies approved changes. 2. Enforce batch-approval: diagnose the scene/chapter for the declared editorial scope; present one coherent batch of exact proposed changes, each localized enough to accept or reject individually; author accepts, rejects, or modifies individual changes; apply only the approved changes. 3. Declare HITL mode before work begins; forbid silent switching. 4. Reclassify evaluation_notes as editorial/diagnostic state and align with the shared finding envelope. 5. Add provenance for approved editorial changes that affect canonical state. 6. Distinguish mechanical fixes (clarity, voice-rule violations) from judgment calls (emotional impact, pacing) in the output contract (RR-17). | Interactive if changes are applied to canonical draft before review; PR-boundary if changes are proposed on a branch. Mode must be declared. | Prose-editing outputs; scene-state schema; story-state schema; character dossier; story bible; continuity report; scene outline; shared finding envelope (proposed). | Diagnosis/repair separation; batch-approval enforcement; HITL mode declaration; per-change author disposition; application of only approved changes; mechanical-versus-judgment contract compliance; audit entry for approved editorial changes. | **Proposed contract changes required.** Prose-editing is the skill most affected by the diagnosis/repair separation and batch-approval gaps. |

### 5.10 `skills/reader-simulation/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| reader-simulation | Phase 5 reader simulation: reader-persona definition, manuscript reading, observation organization, reader report. | RR-1, RR-2, RR-5, RR-6, RR-10, RR-11, RR-12, RR-17, RR-18, RR-19, RR-21, RR-22. | 1. The skill lists character dossiers, story bible, continuity report, and narrative architecture as inputs — all privileged author context. This contradicts the ratified context-blind manuscript-only baseline (RR-18). 2. The skill does not provide an optional informed second pass with selected author context as a labeled overlay (RR-18). 3. The skill does not label its report as a derived view with no unique facts (RR-6). 4. The skill does not record context-package provenance for what was assembled and what was excluded (RR-10, RR-11). 5. The skill does not declare HITL mode for the reader report (RR-21, RR-22). 6. Reader simulation is judgment-based but the skill does not formalize the judgment-based output contract (RR-17). | 1. Redefine the first pass as manuscript-only, no Story Bible, no outline, no dossier, no continuity report, no narrative architecture. 2. Add an optional second pass that loads selected author context as a labeled overlay, with the first pass standing alone. 3. Label the reader report as a derived view with no unique facts. 4. Add context-package provenance labeling for the assembled context. 5. Declare HITL mode for reader simulation (usually PR-boundary, since the report is a derived view, but mode must still be declared). 6. Formalize the judgment-based output contract: observations, not directives; specific; distinguish observation from recommendation; flag critical issues; comparable but not identical across hosts. | PR-boundary is the natural mode for reader simulation (the report is a derived view), but mode must still be declared before work begins. | Manuscript; context assembly (proposed); shared finding envelope (proposed, if reader findings are structured); orchestrator. | Context-blind isolation reproducibility; manuscript-only first-pass contract compliance; derived-view labeling; context-package provenance; judgment-based output contract compliance; two-host comparison (deterministic invariants vs. judgment-based outputs). | **Proposed contract changes required.** Reader-simulation is the skill most directly contradicted by the ratified context-blind baseline. |

### 5.11 `skills/export/SKILL.md`

| Skill | Current responsibility | Ratified requirements affecting it | Confirmed gaps | Proposed contract changes | Approval mode | Dependencies | Tests eventually required | Disposition |
|---|---|---|---|---|---|---|---|---|
| export | Phase 5 manuscript compilation to Markdown (default) and optional DOCX/PDF/ePub; manuscript readiness verification; metadata generation. | RR-1, RR-2, RR-4, RR-5, RR-6, RR-7, RR-9, RR-13, RR-21, RR-22, RR-23. | 1. Export compiles a Markdown manuscript from approved chapter drafts, but the compiled manuscript is a derived view and is not labeled as non-authoritative or rebuildable (RR-6). 2. Export does not go through a transaction boundary or audit record for the compilation step (RR-7, RR-9). 3. Export verifies manuscript readiness (all chapters approved, continuity clean, reader simulation complete, Gate 5 approved) but does not classify these readiness checks as schema-aware portability checks or link them to audit (RR-13). 4. Export does not declare HITL mode (RR-21, RR-22). 5. Export's readiness check references continuity-clean and reader-simulation-complete without specifying which authority rule governs those preconditions (RR-5). | 1. Label the compiled Markdown manuscript as a derived view that is non-authoritative and rebuildable from canonical chapter drafts and story-state metadata. 2. Treat export compilation as a derived-view rebuild, not a canonical transaction; the canonical artifacts remain the approved chapter drafts. 3. Align export readiness checks with the ratified authority and conflict rules. 4. Declare HITL mode for export (Gate 5 approval is the author-facing gate; the compilation itself is a rebuild). 5. Add provenance for the export snapshot (which canonical revisions were compiled, which gate approved them). | PR-boundary for the compilation (derived view); Gate 5 approval is the author-facing gate. | Story-state schema; chapter drafts; orchestrator; Gate 5 approval record. | Derived-view rebuild reproducibility; manifest order validation against story-state chapters; metadata accuracy; snapshot provenance; readiness-check alignment with authority rules. | **Proposed contract changes required.** Export's output is a derived view under the ratified model; the current skill does not label it as such. |

---

## 6. Template-by-Template Impact Matrix

### 6.1 `templates/SKILL_TEMPLATE.md`

**Current responsibility.** Generic template for documenting skills. Provides Purpose, Inputs, Outputs, Dependencies, State Updates, Instructions, Quality Checklist, Notes.

**Authoritative versus derived content.** This template is a documentation scaffold, not a project artifact. It is neither authoritative nor derived in the story-authority sense; it is a meta-template.

**Project-specific contamination.** None. The template is generic.

**IDs and references.** No IDs or story references.

**Approval and revision metadata.** None.

**Provenance needs.** The template is a CodexWriter authoring aid; its provenance is the skill-writing convention, not story canon.

**Compatibility with proposed schema responsibilities.** Compatible. The template's State Updates section is where a skill would document its transaction, audit, and provenance behavior once those contracts exist.

**Changes required, if any.** **No change required** to the template itself. The template should be updated only if the skill contract sections need new fields (for example, a HITL mode field, a transaction/approval field, a provenance field). That is a **proposed implementation detail**, not a ratified requirement for the template.

### 6.2 `templates/story-bible-template.md`

**Current responsibility.** Canonical creative contract for a CodexWriter fiction project. Completed during Phase 1 and approved by the author at Gate 1. Referenced by all downstream skills.

**Authoritative versus derived content.** The story bible is a Markdown creative expression. Under the ratified model, approved Markdown is authoritative for exact wording. The story bible's approved content is authoritative for what it says, but it is not the structured canon store.

**Project-specific contamination.** The template includes Style Profile, Tone Axioms, Narrative Principles, and Source Lineage sections. Under F2, some of these fields may carry Dust & Ash–specific content (for example, Stephen King craft stance, epistemic verb discipline flag). The template does not separate reusable-core fields from optional profile fields.

**IDs and references.** The template includes a Character List table (Character ID, Name, Role Label, Status, First Chapter) and a Timeline table (Event ID, Description, Canonical Order, Textual Status) and a Promise/Payoff table (Promise ID, Promise, Type, Setup Chapter, Payoff Status). These IDs should align with the structured-state IDs once both exist.

**Approval and revision metadata.** The template includes an Approval section (Author, Date, Gate). This is a manual approval record, not a structured transaction or audit record.

**Provenance needs.** The Source Lineage section captures provenance for the story bible as a whole, but not per-fact provenance for individual approved facts that later become structured canon.

**Compatibility with proposed schema responsibilities.** The Story Bible's fields map to story-state fields (project identity, world, plot, timeline, characters, promises, open questions, author preferences). The current template does not distinguish which fields are intended canon, workflow/control state, editorial/diagnostic state, author memory, or derived/convenience data.

**Changes required, if any.**

- **Proposed reclassification:** Add an explicit authority classification guide to the template (or to its accompanying schema guidance) distinguishing canon, workflow, editorial/diagnostic, author memory, and derived content. This is a **proposed implementation detail**.
- **Proposed extraction:** Evaluate whether Style Profile, Tone Axioms, Narrative Principles, and Source Lineage should carry optional Dust & Ash profile content and whether a profile-conditional marker is needed. This is a **proposed implementation detail** driven by F2.
- **Proposed provenance:** Add per-fact provenance capture guidance for approved facts that later become structured canon. This is a **proposed implementation detail** consistent with the ratified provenance requirement.
- **No change required** to the Approval section's existence, but its manual record should eventually be alignable with the structured audit record.

### 6.3 `templates/character-dossier-template.md`

**Current responsibility.** Complete character reference for a single character. Combines static design (voice, backstory, traits) with the pressure system that drives their dramatic function. Created during Phase 2.

**Authoritative versus derived content.** The dossier is a Markdown creative expression. Under the ratified model, approved Markdown is authoritative for exact wording. The dossier is not the structured character-state store; it is the human-readable character reference.

**Project-specific contamination.** The template includes Biblical/Historical Evidence Base and King Style-and-Craft Pressure Integration sections. These are Dust & Ash–specific (Biblical evidence tiers, epistemic verb discipline, Stephen King craft integration). Under F2, they are designated for extraction into the optional Dust & Ash profile.

**IDs and references.** The Character Identity table includes Character ID, Name, Role Label, Dramatic Function, Status. These should align with character-state's character_id and story-state's characters map.

**Approval and revision metadata.** The template includes an Approval section (Author, Date, Gate). Manual record, not a structured transaction or audit record.

**Provenance needs.** The template's Source Lineage section captures provenance for the dossier as a whole. The V4 pipeline's per-section source lineage notes are more granular, but they are free-text and not structured promotion provenance.

**Compatibility with proposed schema responsibilities.** The dossier's pressure system, voice and speech rules, relationships, symbolic vocabulary, and character arc are the human-readable expression of what character-state records as dynamic state. The current template does not separate observable canon from inference, and it does not distinguish reusable-core fields from Dust & Ash profile fields.

**Changes required, if any.**

- **Proposed extraction:** Move or profile-condition the Biblical/Historical Evidence Base and King Style-and-Craft Pressure Integration sections into the optional Dust & Ash profile. This is a **proposed implementation detail** driven by F2.
- **Proposed reclassification:** Add guidance distinguishing observable character facts from inference, and indicate which sections map to character-state canon fields versus inference/derived fields. This is a **proposed implementation detail**.
- **No change required** to the Approval section's existence, but its manual record should eventually be alignable with the structured audit record.

### 6.4 `templates/scene-template.md`

**Current responsibility.** Template for drafting a single scene. Completed during Phase 4. Includes outline approval and draft approval gates.

**Authoritative versus derived content.** The scene template holds the outline (beat-by-beat breakdown, thread pulls, knowledge state changes, continuity notes) and the draft (prose). The draft is the Markdown manuscript authoritative for exact wording. The outline is planning intent, not narrative prose.

**Project-specific contamination.** The template's Beat-by-Beat Breakdown includes Dread Element and Symbolic Element columns, and the template includes a Thread Pulls section. These are Dust & Ash–specific (Stephen King dread mechanics, symbolic deployment, Thread Pull design). Under F2, they are designated for extraction into the optional Dust & Ash profile.

**IDs and references.** The Scene Identity table includes Scene ID, Chapter ID, Scene Number in Chapter, POV Character, Setting. These should align with scene-state's scene_id, chapter_id, pov_character_id, and setting_ref.

**Approval and revision metadata.** The template includes Outline Approved and Draft Approved lines with dates and a Gate reference. Manual records, not structured transaction/audit records.

**Provenance needs.** The template does not capture per-fact provenance for beat-level knowledge changes or continuity notes that later become structured canon.

**Compatibility with proposed schema responsibilities.** The template's fields map to scene-state fields (scene_id, chapter_id, scene_number_in_chapter, pov_character_id, setting_ref, outline_status, draft_status, beats, outline_ref, draft_ref, word_count, dread_elements_used, symbolic_elements_used, thread_pulls_triggered, continuity_notes, evaluation_notes, author_approval). The current template does not distinguish canon, workflow, editorial/diagnostic, author memory, or derived content.

**Changes required, if any.**

- **Proposed extraction:** Move or profile-condition the Dread Element column, Symbolic Element column, and Thread Pulls section into the optional Dust & Ash profile. This is a **proposed implementation detail** driven by F2.
- **Proposed reclassification:** Add guidance distinguishing the draft (authoritative Markdown) from the outline (planning intent), continuity notes (editorial/diagnostic state), and evaluation notes (editorial/diagnostic state). This is a **proposed implementation detail**.
- **No change required** to the Approval section's existence, but its manual records should eventually be alignable with the structured audit record and the ratified batch-approval model.

---

## 7. New Artifact Candidates

Each candidate is labeled as **required by ratified architecture**, **proposed implementation mechanism**, or **deferred decision**. Filenames are illustrative, not ratified.

### 7.1 Transaction/state-update contract

- **Label:** Required by ratified architecture (RR-7, RR-8, RR-24); proposed implementation mechanism for the exact contract shape.
- **Purpose:** Define the transaction boundary for structured-state updates: propose patch, check expected_revision, validate against schema and cross-file consistency, apply atomically, rebuild derived views, record audit entry.
- **Affected files:** All four schemas (indirectly, because the contract governs their updates); orchestrator; concept-development; worldbuilding; character-development; narrative-architecture; scene-planning; scene-writing; continuity; prose-editing; export.
- **Decision needed:** Whether the transaction contract is expressed as a separate transaction record, as fields on the state file, as a Git commit/merge boundary, or as a combination. The ratified model allows a Git commit or merge to be the transaction boundary on Git-based workflows, but the exact serialization, locking, and host-level atomicity guarantees are deferred.

### 7.2 Audit-log schema or store

- **Label:** Required by ratified architecture (RR-7, RR-9); proposed implementation mechanism for the exact schema.
- **Purpose:** Record who submitted what, what was applied, and what the check marked, for canonical transactions and for promoted facts.
- **Affected files:** All schemas; all canon-affecting skills; continuity check_history would be aligned with this audit record.
- **Decision needed:** Whether the audit log is a separate file/store or is embedded in story-state or a transaction record; whether continuity check_history is merged into the general audit log or retained as a specialized log.

### 7.3 Canon-promotion mechanism

- **Label:** Required by ratified architecture (RR-3, RR-4, RR-5, RR-9); proposed implementation mechanism for the exact flow.
- **Purpose:** Govern the transition from prose-originated fact or proposed structured state to approved structured canon, including author approval, transaction validation, provenance capture, and conflict blocking.
- **Affected files:** Character-state; scene-state; story-state; narrative-architecture; scene-writing; scene-planning; continuity; orchestrator.
- **Decision needed:** The exact promotion path for each skill and each field category.

### 7.4 Author-memory schema or store

- **Label:** Required by ratified architecture (RR-29); proposed implementation mechanism for the exact schema/store.
- **Purpose:** Separate author-profile store for author preferences, style profile, tone axioms, forbidden tropes, decision history, and project-profile choices; read by relevant skills; not story canon.
- **Affected files:** Story-state schema (author_preferences removal or reclassification); orchestrator; concept-development; scene-writing; prose-editing; context assembly.
- **Decision needed:** Whether author memory is a separate JSON schema, a separate Markdown file, a separate store, or a combination; what the default content is for existing projects; whether author memory is project-scoped or author-scoped.

### 7.5 Derived-view definitions

- **Label:** Required by ratified architecture (RR-6, RR-12); proposed implementation mechanism for the exact projection schemas.
- **Purpose:** Define which derived views exist (reader-simulation manuscript-only view, continuity-report view, scene-outline view, compiled manuscript, context packages), that they are non-authoritative and rebuildable, and that they contain no unique facts.
- **Affected files:** Reader-simulation; continuity; export; context assembly; orchestrator; all skills that consume derived views.
- **Decision needed:** The exact set of derived views, their projection schemas, and their rebuild triggers.

### 7.6 Context-package contract

- **Label:** Required by ratified architecture (RR-10, RR-11); proposed implementation mechanism for the exact contract.
- **Purpose:** Define how context packages are assembled: project/book identifiers, scope, compact source map, revision markers, explicit authority boundaries, derived-overlay labeling, and provenance note for what was assembled, from which revisions, and what was excluded.
- **Affected files:** Orchestrator; all specialist skills; reader-simulation; continuity; scene-writing.
- **Decision needed:** The exact reload contracts per skill, the LOD strategy, the near/far policy, and the provenance-labeling format. These are deferred until after the first vertical slice per the ratified model.

### 7.7 Validator

- **Label:** Required by ratified architecture (RR-13, RR-16); proposed implementation mechanism for the exact validator.
- **Purpose:** Validate JSON against the four schemas; apply defined structural/frontmatter/contract checks to Markdown where such rules exist; reject operations whose required state is missing or invalid.
- **Affected files:** All four schemas; all skills; CI.
- **Decision needed:** The validator implementation language, the CI integration, and the exact Markdown contract checks. The alignment evaluation pointed to a Python validator.

### 7.8 Continuity checker

- **Label:** Required by ratified architecture (RR-13, RR-16, RR-19); proposed implementation mechanism for the exact checker.
- **Purpose:** Perform deterministic continuity checks (character_id pattern checks, phase/phase_gate consistency, state_revision monotonicity, cross-file reference integrity, cast membership, location consistency, promise timing, chapter numbering) and classify judgment-based checks separately.
- **Affected files:** Continuity schema; continuity skill; story-state schema; character-state schema; scene-state schema.
- **Decision needed:** Which checks are deterministic and which are judgment-based; the exact checker scope; whether continuity-state becomes a derived view rebuilt from canonical state plus manuscript.

### 7.9 Fixtures

- **Label:** Required by ratified architecture (RR-13, RR-16); proposed implementation mechanism for the exact fixtures.
- **Purpose:** Provide valid and invalid project instances for schema validation, transaction acceptance/rejection, continuity checking, and derived-view rebuild testing.
- **Affected files:** Validator; continuity checker; CI; vertical slice.
- **Decision needed:** The fixture set and the generic project scenario used for the vertical slice.

### 7.10 Tests

- **Label:** Required by ratified architecture (RR-13, RR-16); proposed implementation mechanism for the exact test suite.
- **Purpose:** Schema validation tests, cross-file consistency tests, stale-revision rejection tests, conflict-blocking tests, audit-history creation tests, derived-view reproducibility tests, context provenance tests, context-blind reader isolation tests, editorial approval enforcement tests, HITL mode declaration tests, no-silent-switching tests, deterministic two-host equality tests, judgment-contract compliance tests.
- **Affected files:** All schemas; all skills; validator; continuity checker; CI; vertical slice.
- **Decision needed:** The test framework, the smoke-test scope, and the two-host test arrangement. The alignment evaluation raised tests and CI to High priority.

### 7.11 CI configuration

- **Label:** Required by ratified architecture (RR-13, RR-16); proposed implementation mechanism for the exact CI.
- **Purpose:** Run schema validation, transaction tests, continuity checks, and derived-view reproducibility checks on every commit; validate that the schemas and validator are internally consistent.
- **Affected files:** CI workflow; tests; fixtures; validator; continuity checker.
- **Decision needed:** The CI platform, the trigger policy, and the pass/fail gates.

### 7.12 Host-adapter boundary

- **Label:** Required by ratified architecture (RR-13, RR-14); proposed implementation mechanism for the exact boundary.
- **Purpose:** Separate host-neutral contracts (Markdown/JSON inputs/outputs, schema validation, authority rules, conflict rules, derived-view regeneration, transaction record shape) from host-adapter concerns (prompt delivery, tool invocation, file access conventions, agent subprocess management, runtime logging, interaction surfaces).
- **Affected files:** All skills; orchestrator portability section; export skill; CI; vertical slice.
- **Decision needed:** The exact host-adapter interface and the capability-detection contract. Deferred until after the vertical slice per the ratified model.

### 7.13 Dust & Ash profile structure

- **Label:** Required by ratified architecture (RR-28, F2); proposed implementation mechanism for the exact profile structure.
- **Purpose:** Define the optional Dust & Ash profile that contains Thread Pull design, V4 pipeline, Biblical evidence tiers, Stephen King craft integration, epistemic verb discipline, pressure-system vocabulary, dread/symbolic element catalogs, and any other project-specific material extracted from the reusable core.
- **Affected files:** Character-development skill; narrative-architecture skill; scene-planning skill; scene-writing skill; scene template; character-dossier template; scene-state schema (dread_elements_used, symbolic_elements_used, thread_pulls_triggered); story-state schema (author_preferences fields that are Dust & Ash specific, if any).
- **Decision needed:** Whether the profile is a separate schema extension, a separate skill variant, a profile-conditional marker on existing fields, or a combination; what remains in the core versus what moves to the profile.

---

## 8. Dependency and Implementation Sequence

The recommended sequence minimizes rework by establishing authority classification and schema responsibility before skill contracts, and by establishing the transaction/revision/audit contract before canon-promotion workflow and derived-view rebuilding.

### Stage 1 — Authority classification

**Goal:** Classify every existing schema field and template field as intended canon, workflow/control state, editorial/diagnostic state, author memory, or derived/convenience data. This classification is the foundation for every later stage.

**Why first:** Skill contracts, transaction design, derived-view definitions, and Dust & Ash extraction all depend on which fields are canon and which are not. Doing this later would require reworking earlier stages.

**Parallelizable:** None of the later stages can proceed before the field responsibility map exists. Within Stage 1, schema field classification and template field classification can proceed in parallel.

### Stage 2 — Schema responsibility and field alignment

**Goal:** Propose the exact field additions, removals, moves, and reclassifications for each schema, aligned with the Stage 1 classification. This includes the transaction/audit field proposals, the provenance field proposals, the cross-file reference integrity proposals, and the Dust & Ash field extraction proposals.

**Why second:** The field alignment is the concrete output of the authority classification. It is the handoff to the transaction contract and to the skill-contract alignment.

**Dependencies:** Stage 1.

**Parallelizable:** The four schemas can be analyzed in parallel once Stage 1 is complete.

### Stage 3 — Transaction/revision/audit contract

**Goal:** Define the transaction boundary, expected-revision guard, atomic-application rule, rollback rule, and audit record. This is the contract that governs every canonical state update.

**Why third:** The transaction contract needs the field responsibility map and the aligned schema fields. It is the prerequisite for canon-promotion workflow, derived-view rebuilding, and skill-contract alignment.

**Dependencies:** Stage 2.

**Parallelizable:** The audit-log schema and the transaction contract can be designed together.

### Stage 4 — Validation and fixtures

**Goal:** Build the schema validator, the minimum viable continuity checker, and the generic fixtures. This is the High-priority infrastructure workstream (tasks A4–A6 + A17 in the alignment evaluation).

**Why fourth:** Validation and fixtures need the aligned schemas and the transaction contract. They are the proof mechanism for the later stages.

**Dependencies:** Stage 2 and Stage 3.

**Parallelizable:** Validator and continuity checker can proceed in parallel once the schemas and transaction contract are defined. Fixtures can be built alongside them.

### Stage 5 — Canon-promotion workflow

**Goal:** Define the promotion path for each skill and each field category: prose/proposed fact → author approval + transaction validation → canon state field, with provenance capture and conflict blocking.

**Why fifth:** Canon-promotion workflow needs the transaction contract, the audit record, and the provenance fields.

**Dependencies:** Stage 3 and Stage 4 (validation must be able to reject invalid promotions).

**Parallelizable:** Promotion workflow for different skills can be designed in parallel.

### Stage 6 — Derived-view rebuilding

**Goal:** Define the derived views (reader-simulation manuscript-only view, continuity-report view, scene-outline view, compiled manuscript, context packages), their rebuild triggers, and their non-authoritative/rebuildable labeling.

**Why sixth:** Derived views need the canonical state shape, the context-package contract, and the canon-promotion workflow.

**Dependencies:** Stage 4 and Stage 5.

**Parallelizable:** Derived-view definitions for different consumers can proceed in parallel.

### Stage 7 — Context assembly

**Goal:** Define reload contracts per skill, LOD strategy, near/far policy, provenance labeling for assembled context, and conflict honoring between summaries and canonical sources.

**Why seventh:** Context assembly needs the derived-view definitions and the canon-promotion workflow. Per the ratified model, exact LOD thresholds are deferred until after the first vertical slice, so this stage defines the minimum responsibility and the reload contracts, not the final LOD budgets.

**Dependencies:** Stage 5 and Stage 6.

**Parallelizable:** Reload contracts for different skills can be designed in parallel.

### Stage 8 — Skill-contract alignment

**Goal:** Update each skill's contract to reflect the ratified requirements: orchestrator context-package contract and HITL mode declaration; concept-development initialization as a canonical transaction; worldbuilding and character-development state updates as transactions with provenance; narrative-architecture Thread Pull extraction; scene-planning dread/symbolic/Thread Pull extraction; scene-writing Thread Pull extraction and transaction-aligned state updates; continuity deterministic-versus-judgment-based classification, transaction alignment, shared finding envelope, stopping rule, and HITL mode declaration; prose-editing diagnosis/repair separation, batch-approval model, HITL mode declaration, and mechanical-versus-judgment contract; reader-simulation context-blind first pass, optional informed second pass, derived-view labeling, and context-package provenance; export derived-view labeling and rebuild semantics.

**Why eighth:** Skill-contract alignment needs the transaction contract, the audit record, the provenance fields, the derived-view definitions, and the context-package contract.

**Dependencies:** Stage 5, Stage 6, Stage 7.

**Parallelizable:** Most skill contracts can be updated in parallel once their dependencies are defined. The orchestrator contract should be updated first because the other skills depend on its context-package and HITL-mode contracts.

### Stage 9 — Reader/editor HITL alignment

**Goal:** Align the HITL mode declaration, interactive versus PR-boundary selection criteria, anti-switching rule, and batch-approval enforcement across the orchestrator, continuity, prose-editing, reader-simulation, and export.

**Why ninth:** HITL alignment needs the skill contracts from Stage 8 and the transaction/audit contract from Stage 3.

**Dependencies:** Stage 3 and Stage 8.

**Parallelizable:** HITL alignment for different skills can proceed in parallel.

### Stage 10 — Dust & Ash extraction

**Goal:** Extract Thread Pull design, V4 pipeline, Biblical evidence tiers, Stephen King craft integration, epistemic verb discipline, pressure-system vocabulary, dread/symbolic element catalogs, and any other project-specific material into the optional Dust & Ash profile.

**Why tenth:** Extraction needs the field responsibility map (Stage 1), the schema field alignment (Stage 2), and the skill-contract alignment (Stage 8) so that the profile's boundaries are clear and the core's remaining fields are coherent.

**Dependencies:** Stage 1, Stage 2, Stage 8.

**Parallelizable:** Profile structure design can proceed in parallel with the core's field reclassification, but the extraction itself should follow the skill-contract alignment.

### Stage 11 — Host adapters and two-host evidence

**Goal:** Define the host-adapter boundary, build the second-host evidence, and demonstrate deterministic-invariant equality and judgment-based output contract compliance across two hosts.

**Why eleventh:** Two-host evidence needs the validator, the continuity checker, the fixtures, the skill contracts, and the vertical slice. Per the ratified model, the exact porting checklist is deferred until after the vertical slice.

**Dependencies:** Stage 4, Stage 8, Stage 12.

**Parallelizable:** Host-adapter boundary design can proceed in parallel with the vertical slice, but the two-host evidence run should follow the vertical slice.

### Stage 12 — Generic vertical slice and CI

**Goal:** Build the staged representative workflow on at least two hosts, with fixtures, validators, tests, and CI. This is the smallest end-to-end exercise of the ratified model.

**Why twelfth:** The vertical slice needs the validator, the continuity checker, the fixtures, the skill contracts, the transaction contract, the audit record, the provenance fields, the derived-view definitions, the context-package contract, and the HITL alignment. It is the integration point for all earlier stages.

**Dependencies:** Stage 4, Stage 5, Stage 6, Stage 7, Stage 8, Stage 9.

**Parallelizable:** CI configuration can proceed in parallel with the vertical slice once the tests and validator exist.

### Alternative order justification

If Dave prefers to extract Dust & Ash material before the vertical slice, Stage 10 can move earlier, but only after Stage 1 and Stage 2 are complete, because the extraction depends on the field responsibility map and the schema field alignment. Moving Stage 10 before Stage 8 would risk extracting material that the skill contracts have not yet aligned, which would require rework.

If Dave prefers to build the vertical slice before full skill-contract alignment, that is possible for the minimal slice (which exercises only initialization, one promotion, one derived-view rebuild, one reader report, one editorial batch, and validation), but the slice's skill contracts would still need the transaction contract, the audit record, and the provenance fields from Stages 2 and 3. The slice cannot skip Stage 3.

---

## 9. Proposed Minimal Vertical Slice

This section defines — but does not build — the smallest representative workflow that could validate the architecture.

### Starting artifacts

- A minimal generic project scaffold: one story bible (Markdown), one scene draft (Markdown), one approved structured fact (for example, a character knowledge item approved for promotion), one story-state.json instance, one character-state.json instance, one scene-state.json instance, one continuity-state.json instance.
- All four schemas.
- A validator.
- A continuity checker.
- A shared finding/disposition envelope (if adopted).
- A context-package contract (if adopted).
- A second host capable of executing the same prompts against the same fixture files.

The generic fixture should not use Dust & Ash story content. It should be a small, neutral scenario that exercises the ratified model without requiring profile-specific material.

### One state-changing operation

- Promote one approved fact into structured canon: a character knowledge item that was approved by the author is written into character-state.json as intended canon, with provenance pointing to the approval record and the source passage, via a validated transaction with expected_revision, schema validation, and cross-file reference integrity checks.

### Human approval point

- The promotion requires author approval before the transaction applies. The approval is recorded as part of the provenance and the audit entry.

### Revision check

- The transaction carries an expected_revision. A second, stale transaction that attempts to promote a different fact from an outdated baseline is rejected, and the rejection reason is recorded.

### Validation

- The validator validates the schema instance before the transaction applies and after the transaction applies.
- A deliberately broken state instance is rejected by the validator.

### Atomic-application expectation

- If any part of the transaction fails (schema validation, expected-revision mismatch, cross-file reference integrity, missing required state), the canonical authority is not advanced and the rejection is recorded. The promoted fact does not partially appear.

### Audit entry

- The audit record captures who submitted the promotion, what was applied, the expected_revision, the check summary, and the resulting state revision.

### Derived-view rebuild

- A derived view (for example, a character-knowledge summary or a scene-outline view) is rebuilt from the canonical files after the promotion, and the rebuilt content matches the canonical source. The derived view is labeled as non-authoritative and rebuildable.

### Deterministic checks

- Schema validation results, transaction acceptance/rejection, revision counters, cross-file reference integrity, and the rebuilt derived-view content are deterministic and must match across hosts.

### Judgment-based output

- Reader-simulation observations and any editorial diagnosis are judgment-based. They must comply with the same scope and output contracts across hosts but need not match in wording, emphasis, or conclusions.

### Second-host evidence

- The same generic project and the same promotion task are executed on a second host. The deterministic invariants match; the judgment-based outputs comply with the same contracts but may differ in wording. Differences are documented and explained as host-adaptation gaps, not as different canon.

### Pass/fail criteria

- The initialized project is valid and clearly scoped.
- The promoted fact is in the state and is traceable to the approval and the source passage.
- The valid transaction is applied and auditable.
- The stale transaction is rejected and the rejection reason is recorded.
- The derived view is regenerated without loss of unique facts and matches its canonical source.
- The context package is locally correct and provenance-labeled (if context assembly is in scope for the slice).
- The blind reader report is reproducible in contract: manuscript-only isolation and reader-report structure are reproducible; the reader's exact judgments, wording, and conclusions need not be identical across runs or hosts.
- Editorial changes are applied only after explicit per-change disposition (if editorial is in scope for the slice).
- Validation passes for the intended state and fails appropriately for a deliberately broken input.
- Two-host results are comparable and differences are documented.

---

## 10. Testing and Evidence Plan

Each proposed change is mapped to eventual evidence. The tests are not created tonight.

### Schema validation

- **Change:** Aligned schemas; transaction/audit fields; provenance fields; cross-file reference integrity fields; Dust & Ash field extraction.
- **Evidence:** Schema validator confirms that valid instances pass and that deliberately broken instances fail. The validator is run in CI on every commit.

### Cross-file consistency

- **Change:** Cross-file reference integrity fields and validation rules; transaction contract that checks references before apply.
- **Evidence:** Validator or continuity checker confirms that character_id, chapter_id, scene_id, event_id, promise_id, location_id references resolve to known canonical IDs. Broken references are rejected.

### Stale-revision rejection

- **Change:** Transaction contract with expected_revision guard.
- **Evidence:** A stale transaction is rejected and the rejection reason is recorded. The canonical authority is not advanced. The same test is run on both hosts and produces the same result.

### Conflict blocking

- **Change:** Authority model enforcement; reconciliation record; loser-side ruling propagation.
- **Evidence:** A Markdown/structured-state conflict blocks the dependent operation until a reconciliation record is created. After reconciliation, the resolved side wins and the other side is flagged or revised. The same conflict produces the same resolution decision on both hosts.

### Audit-history creation

- **Change:** Audit-log schema or store; transaction contract that records audit entries.
- **Evidence:** Every applied canonical transaction produces an audit entry capturing who submitted what, what was applied, the expected_revision, the check summary, and the resulting revision. The audit entry is reproducible from the canonical transaction record.

### Derived-view reproducibility

- **Change:** Derived-view definitions; rebuild triggers; non-authoritative/rebuildable labeling.
- **Evidence:** A derived view rebuilt from the same canonical files produces the same content on both hosts. Discarding and regenerating the derived view loses no unique facts.

### Context provenance

- **Change:** Context-package contract; provenance labeling.
- **Evidence:** Every context package records project/book identifiers, scope, compact source map, revision markers, and a provenance note for what was assembled, from which revisions, and what was excluded. The package does not assert authority beyond what the source map shows.

### Context-blind reader isolation

- **Change:** Reader-simulation context-blind first pass.
- **Evidence:** The first pass uses manuscript only, with no Story Bible, no outline, no dossier, no continuity report, no narrative architecture. The manuscript-only isolation and the reader-report structure are reproducible across runs and hosts.

### Editorial approval enforcement

- **Change:** Diagnosis/repair separation; batch-approval model; per-change author disposition; apply-only-approved-changes rule.
- **Evidence:** A prose-editing batch presents exact proposed changes; the author accepts, rejects, or modifies individual changes; only the approved changes are applied. A general editing-goal approval does not authorize unrestricted rewriting.

### HITL mode declaration

- **Change:** Mode declaration before work begins; interactive versus PR-boundary selection criteria; anti-switching rule.
- **Evidence:** The system declares the mode before work begins and records the mode in the audit entry. If new information changes the appropriate mode, the system stops and asks for a fresh decision. The same operation produces the same mode decision on both hosts.

### No silent switching

- **Change:** Anti-switching rule.
- **Evidence:** A workflow that encounters new information requiring a mode change stops and requests a fresh decision rather than continuing silently.

### Deterministic two-host equality

- **Change:** Validator; transaction contract; audit record; derived-view rebuild; cross-file consistency.
- **Evidence:** Schema results, transaction acceptance/rejection, revision counters, promoted fact values, provenance records, audit entries, and regenerated registry contents match across hosts.

### Judgment-contract compliance

- **Change:** Prose-editing mechanical-versus-judgment distinction; reader-simulation judgment-based output contract; continuity deterministic-versus-judgment-based classification.
- **Evidence:** Judgment-based outputs comply with the same scope and output contracts on both hosts but need not match in wording, emphasis, or conclusions. The outputs are labeled as judgment-based and are not claimed as mechanically proven.

---

## 11. Licensing and Provenance Impact

### Architectural inspiration is not copied implementation

The ratified architecture is a synthesis of patterns from seven sources. The synthesis and ratification documents record the sources and the proposed dispositions. Architectural inspiration — for example, the specialist role taxonomy from Lensetek, the transaction semantics from Zenstory, the context-blind reader testing from Rhavekost, the exact-text editor gate from JeroTan, the prose-over-summary rule from wgwtest, the Markdown/YAML state discipline from Dewhurst, the cognitive-role separation from Haowjy — is not, by itself, copied implementation. Implementation-level borrowing requires separate license and provenance review.

### Lensetek's missing root license remains unresolved

The Lensetek source analysis records that the root LICENSE returns 404 and that GitHub metadata reports `license: null`. The intended license appears to be MIT, but the intended license and an actually granted license should not be treated as identical while the referenced license text is missing. If implementation-level borrowing from Lensetek is contemplated, the license ambiguity must be resolved first. The specialist role taxonomy as an ideas inventory does not require a license grant; copied or adapted implementation text would.

### Rhavekost vendored material retains separate licensing

The Rhavekost source analysis records that the toolkit's MIT license covers the toolkit itself, but the vendored `avoid-ai-writing` material retains its own license. Any borrowing from vendored material must follow that component's license. ATTRIBUTION.md documents the vendored material and its upstream commit.

### Moving dependencies require lineage review

The Haowjy and Zenstory source analyses record that some effective behavior comes from moving dependencies (Haowjy's `meridian-base`, Zenstory's `meridian-base`) whose exact resolved commits are not fully traceable from the pinned application commits. If implementation-level borrowing from those sources is contemplated, the dependency lineage must be examined.

### Moving dependencies require lineage review

The Haowjy and Zenstory source analyses record that some effective behavior comes from moving dependencies (Haowjy's `meridian-base`, Zenstory's `meridian-base`) whose exact resolved commits are not fully traceable from the pinned application commits. If implementation-level borrowing from those sources is contemplated, the dependency lineage must be examined.

### The repository's own licensing decision is separate from source-level provenance

The repository currently has no LICENSE file. The licensing decision for the repository is separate from the source-level provenance review. This plan does not select or add a repository license; it only flags that implementation-level borrowing may require license or attribution review and that Lensetek's missing root license remains unresolved.

### Attribution records should be pinned

The alignment evaluation flagged that ATTRIBUTION.md uses mutable `main` links. If implementation-level borrowing occurs, the attribution should be pinned to specific source revisions, not to mutable branch references.

---

## 12. Decisions Required From Dave

Each entry contains the decision question, why it is needed, options, a recommended option, consequences of each option, and whether implementation is blocked until the decision is made.

### D1: Author-memory placement

**Decision question:** Should `author_preferences` move out of `story-state.schema.json` into a separate author-memory schema or store, or should it remain in story-state under a clarified non-canon authority label?

**Why it is needed:** The ratified model requires author memory to be a separate authority category from story canon. The current placement of `author_preferences` inside story-state.json conflicts with that requirement. The conflict must be resolved before the schema alignment and the skill-contract alignment can be finalized.

**Options:**
1. Move `author_preferences` to a separate author-memory schema/store.
2. Keep `author_preferences` in story-state.json but reclassify it as author memory with a clear boundary that it is not story canon and does not enter story truth.
3. Split `author_preferences`: move the author-memory portions (style profile, tone axioms, forbidden tropes, preferred POV, tense, narrative principles, evidence_labels, king_craft_stance) to a separate store and retain only workflow-metadata portions in story-state, if any.

**Recommended option:** Option 1 or Option 3, because both preserve the ratified separation. Option 1 is cleaner; Option 3 is more conservative if some preference fields are expected to be referenced during story-state transactions.

**Consequences:**
- Option 1: Cleanest separation; requires a migration path for existing project instances; requires author-memory reads in orchestrator, concept-development, scene-writing, prose-editing, and context assembly.
- Option 2: Least file changes; risks the author-memory category being treated as story canon by downstream consumers unless the boundary is heavily documented; does not fully satisfy the ratified separation.
- Option 3: Balances separation and minimal migration; adds complexity in deciding which fields stay and which move.

**Blocked until decided:** Yes, for the schema alignment and the skill-contract alignment. The transaction contract and the context-package contract can proceed with a placeholder author-memory boundary, but the final schema alignment cannot.

### D2: Schema retention versus restructuring

**Decision question:** Should the existing four-schema set be retained as the structured-state layer with field reclassification, transaction/audit field additions, provenance field additions, cross-file reference integrity additions, and Dust & Ash field extraction, or should any schema be partially restructured (for example, splitting character-state emotional_state and physical_state into observable canon and inference sub-structures, or splitting continuity-state into a derived view plus a check log)?

**Why it is needed:** The ratified model requires schemas to distinguish canon fields from editorial fields, but the exact field-by-field reclassification is deferred to the schema and skill impact plan. This plan proposes classifications and additions, but the exact schema shape is Dave's decision.

**Options:**
1. Retain the four schemas with reclassifications, additions, and Dust & Ash extraction, keeping the same file structure.
2. Retain the four schemas but split selected fields into sub-structures (for example, observable versus inference in character-state; deterministic versus judgment-based in continuity).
3. Introduce one or more additional schemas (for example, author-memory.schema.json, transaction.schema.json, audit.schema.json, shared-finding.schema.json) alongside the existing four.

**Recommended option:** Option 1 with selective sub-structures from Option 2, because it preserves the existing schema set while satisfying the ratified requirements. Option 3 should be used only for artifacts that are clearly separate from the four existing schemas (for example, author-memory, audit).

**Consequences:**
- Option 1: Minimal schema count change; easier migration; may require careful documentation of reclassified fields.
- Option 2: Clearer canon/inference and deterministic/judgment-based boundaries; more field restructuring; more migration complexity.
- Option 3: Cleanest separation for new concerns; more schema files; more cross-schema references to maintain.

**Blocked until decided:** Yes, for the schema alignment. The transaction contract and the skill contracts can proceed with a proposed field map, but the final schema shape is Dave's decision.

### D3: Reader-simulation context-blind implementation timing

**Decision question:** Should the reader-simulation skill be required to implement a context-blind first pass now (as part of the skill-contract alignment), or should the context-blind baseline be deferred until after the vertical slice?

**Why it is needed:** The ratified model requires a context-blind manuscript-only first pass. The current skill contradicts this. The question is whether to align the skill now or to defer the full implementation until after the vertical slice, while still correcting the skill's claims to stop asserting the contradictory behavior as present.

**Options:**
1. Align the reader-simulation skill contract now to require a manuscript-only first pass and an optional informed second pass, even if the full context assembler is not yet built.
2. Defer the full context-blind implementation until after the vertical slice, but correct the skill's documentation now to stop claiming the context-loaded behavior as compliant.
3. Implement a partial context-blind pass now (for example, a manual manifest that excludes author context) and refine it after the vertical slice.

**Recommended option:** Option 1 for the contract and Option 2 for the full implementation, because the ratified requirement is already in force and the skill's claims should be corrected now, but the full context assembler may not be needed for a minimal blind pass.

**Consequences:**
- Option 1: Brings the skill into compliance with the ratified requirement sooner; may require a provisional context-exclusion mechanism before the full context assembler exists.
- Option 2: Lower immediate implementation burden; leaves a documented contradiction in place until the vertical slice.
- Option 3: Pragmatic middle ground; risks a provisional mechanism becoming de facto permanent if not revisited.

**Blocked until decided:** No, for the documentation correction (the skill should stop claiming the contradictory behavior as present regardless). Yes, for the full implementation approach, if Dave wants to decide whether the blind pass is a vertical-slice deliverable or a skill-contract deliverable.

### D4: Continuity-state as a derived view

**Decision question:** Should continuity-state.json become a derived view rebuilt from canonical state plus manuscript, rather than a separately written state file updated by the continuity skill?

**Why it is needed:** The ratified model requires derived views to be rebuildable and non-authoritative. Continuity check results are diagnostic/editorial state, not canon. If continuity-state becomes a derived view, it would be rebuilt from the canonical state and the manuscript on change or on explicit rebuild, and would carry no unique facts. If it remains a separately written state file, it must be clearly classified as non-authoritative diagnostic state and must still go through the transaction/audit contract.

**Options:**
1. Make continuity-state a derived view rebuilt from canonical state plus manuscript.
2. Keep continuity-state as a separately written state file, but classify it as non-authoritative diagnostic state and route its updates through the transaction/audit contract.
3. Split continuity-state into a derived view for the findings and a separate check log for the audit history.

**Recommended option:** Option 1 or Option 3, because both align with the ratified derived-view requirement. Option 1 is simpler; Option 3 preserves a dedicated check-history log if Dave wants continuity checks to have their own audit trail separate from the general canonical audit record.

**Consequences:**
- Option 1: Cleanest alignment with the ratified derived-view model; continuity findings become reproducible from canonical state plus manuscript; continuity-state is not a separate canonical artifact.
- Option 2: Less rework for the current continuity skill; requires transaction/audit alignment for continuity writes; requires clear non-authoritative labeling.
- Option 3: Preserves a continuity-specific audit trail; adds a second artifact to maintain.

**Blocked until decided:** Yes, for the continuity skill contract and the continuity schema alignment. The decision affects whether continuity-state updates are transactions or derived-view rebuilds.

### D5: Transaction boundary expression

**Decision question:** Should the transaction boundary be expressed as a separate transaction record, as fields on the state file, as a Git commit/merge boundary, or as a combination?

**Why it is needed:** The ratified model specifies the transaction boundary, the failure detection, the recovery rule, and the counter coordination, but not the exact serialization, locking, or host-level atomicity guarantees. The exact expression affects the schema design, the audit record, and the skill contracts.

**Options:**
1. Separate transaction record that wraps the prior authority, the new authority, the summary, and the check information, with the canonical state advancing only when the transaction is applied.
2. Fields on the state file (expected_revision, transaction_id, applied_by, applied_at, check_summary) plus a separate audit log.
3. Git commit/merge as the transaction boundary on Git-based workflows, with the commit/merge being the atomic application step.
4. Combination: a transaction record for the runtime contract, a Git commit/merge for the Git-based boundary, and a separate audit log.

**Recommended option:** Option 4, because it matches the ratified model's allowance for a Git commit or merge to be the transaction boundary on Git-based workflows while still providing a runtime transaction record and an audit log.

**Consequences:**
- Option 1: Cleanest runtime contract; separates transaction from state; may be heavier to implement.
- Option 2: Simpler; keeps transaction metadata near the state; may blur the boundary between state and transaction record.
- Option 3: Leverages Git as the atomic boundary; works well on Git-based workflows; may be less portable to non-Git hosts.
- Option 4: Most flexible; may require coordinating multiple representations.

**Blocked until decided:** Yes, for the transaction contract and the audit record design. The exact expression affects the schema additions and the skill contracts.

### D6: Shared finding envelope adoption

**Decision question:** Should continuity, prose-editing, and reader-simulation findings all use a shared finding/disposition envelope (with finding_id, scope, location, description, evidence, confidence, determinism, recommended_action, author_disposition, resolution_notes), or should each skill keep its own finding format?

**Why it is needed:** The ratification addendum references a shared envelope with confidence and determinism classification as deferred detail. A shared envelope would align diagnostic output across skills and would support the diagnosis/repair separation and the batch-approval model.

**Options:**
1. Adopt a shared finding envelope across continuity, prose-editing, and reader-simulation.
2. Keep separate finding formats but align on a common set of fields (confidence, determinism, scope, location, author disposition).
3. Defer the shared envelope until after the vertical slice.

**Recommended option:** Option 1 for continuity and prose-editing (which both produce findings that may block progression), and a lighter observation format for reader-simulation (which produces observations, not directives). Option 3 is acceptable if Dave wants to defer the envelope until the vertical slice demonstrates the need.

**Consequences:**
- Option 1: Strongest alignment with the ratified diagnosis/repair separation and batch-approval model; more schema/contract work up front.
- Option 2: Less upfront work; risk of drift between formats.
- Option 3: Lowest immediate burden; leaves the finding-format question open.

**Blocked until decided:** No, for the diagnosis/repair separation and batch-approval principles (those are ratified). Yes, for the exact shared envelope shape, if Dave wants to decide whether to adopt it now or defer it.

### D7: Dust & Ash profile mechanism

**Decision question:** Should the Dust & Ash profile be a separate schema extension, a separate skill variant, a profile-conditional marker on existing fields, or a combination?

**Why it is needed:** F2 designates Thread Pull design, the V4 pipeline, Biblical evidence tiers, Stephen King craft integration, epistemic verb discipline, pressure-system vocabulary, dread/symbolic element catalogs, and any other project-specific material for extraction into the optional Dust & Ash profile. The exact profile mechanism affects which fields move, which skills split, and which templates change.

**Options:**
1. Separate Dust & Ash schema extension(s) for profile-specific fields.
2. Separate Dust & Ash skill variant(s) for profile-specific behavior (for example, a Dust & Ash character-development variant that includes the V4 pipeline).
3. Profile-conditional markers on existing fields and skills (for example, a `profile: dust-and-ash` flag that activates Thread Pull, dread/symbolic, and V4 behavior).
4. Combination: profile-conditioned fields plus separate skill variants for the most distinctive behavior.

**Recommended option:** Option 4, because it preserves the reusable core's coherence while giving the Dust & Ash profile a clear mechanism for its distinctive material. The exact split between core and profile is the key decision.

**Consequences:**
- Option 1: Cleanest field separation; adds profile schema files; requires profile-aware readers.
- Option 2: Cleanest behavior separation; adds profile skill variants; requires the orchestrator to route to profile variants.
- Option 3: Least file proliferation; risks core files retaining profile-conditioned branches that complicate the reusable core.
- Option 4: Balanced; may require both schema and skill changes.

**Blocked until decided:** Yes, for the Dust & Ash extraction. The extraction cannot be implemented without a profile mechanism.

### D8: Transaction/audit field placement

**Decision question:** Should transaction and audit fields be stored on the state files (for example, `state_revision`, `expected_revision`, `transaction_id`, `applied_by`, `applied_at`, `check_summary`), in a separate transaction record, or in a separate audit log?

**Why it is needed:** The ratified model requires a transaction boundary, an expected-revision guard, and an audit record. The exact placement affects the schema additions, the audit-record design, and the skill contracts.

**Options:**
1. Transaction fields on the state files; audit log separate.
2. Transaction record separate; audit log separate; state files carry only the canonical revision counters.
3. Transaction and audit fields on the state files; no separate audit log (the state file history serves as the audit trail).
4. Combination: state files carry revision counters and a reference to the transaction/audit record; transaction and audit records are separate.

**Recommended option:** Option 4, because it keeps the canonical revision counters on the state files (where they already are) while separating the transaction and audit records (which are not canon and should not be treated as story truth).

**Consequences:**
- Option 1: Keeps transaction metadata near the state; may blur canon and transaction metadata.
- Option 2: Cleanest separation; more artifacts to maintain.
- Option 3: Simplest; risks treating transaction metadata as canon.
- Option 4: Balanced; requires cross-references between state and transaction/audit records.

**Blocked until decided:** Yes, for the transaction contract and the audit record design.

### D9: Author-memory scope

**Decision question:** Should the author-memory store be project-scoped (one author profile per project) or author-scoped (one author profile shared across projects, with project-specific overrides)?

**Why it is needed:** The ratified model requires author memory to be a separate store outside story canon. The scope of that store affects the schema/store design and the skill contracts.

**Options:**
1. Project-scoped author memory (one profile per project).
2. Author-scoped author memory (one profile per author, with project-specific overrides).
3. Hybrid: author-scoped base profile with project-scoped overrides.

**Recommended option:** Option 3, because it matches the likely use case (an author has consistent style preferences across projects but may override them per project) and because it preserves the ratified separation.

**Consequences:**
- Option 1: Simplest; ties author preferences to a single project; may duplicate preferences across projects.
- Option 2: Most reusable; may require project-specific override logic.
- Option 3: Most flexible; slightly more complex.

**Blocked until decided:** Yes, for the author-memory schema/store design.

### D10: Generic vertical slice scope

**Decision question:** Should the generic vertical slice exercise all ratified minimum responsibilities (initialization, promotion, transaction, stale-write rejection, audit, derived-view rebuild, context assembly, context-blind reader, editorial batch with diagnosis and per-change disposition, validation, two-host evidence), or should it be smaller (for example, state spine only first, then creative/HITL path later)?

**Why it is needed:** The ratification addendum proposes a three-checkpoint vertical slice. The question is whether to build all three checkpoints together or sequentially.

**Options:**
1. Build all three checkpoints as one slice.
2. Build Checkpoint 1 (deterministic state spine) first, then Checkpoint 2 (creative and HITL path), then Checkpoint 3 (portability evidence).
3. Build a smaller slice that exercises only initialization, one promotion, one stale-write rejection, one audit entry, and one derived-view rebuild, deferring reader simulation and editorial batch to a later slice.

**Recommended option:** Option 2, because it matches the addendum's checkpoint structure and reduces the risk of a large slice failing for multiple independent reasons.

**Consequences:**
- Option 1: Fastest end-to-end validation if it succeeds; hardest to debug if it fails.
- Option 2: Staged validation; each checkpoint can be reviewed before the next begins.
- Option 3: Smallest first slice; may need a second slice to exercise reader simulation and editorial batch.

**Blocked until decided:** No, for the decision to build a vertical slice at all (that is a future implementation authorization). Yes, for the slice scope, if Dave wants to decide the checkpoint granularity before implementation.

### D11: Export as a derived view

**Decision question:** Should the exported Markdown manuscript be labeled as a derived view that is non-authoritative and rebuildable from canonical chapter drafts and story-state metadata, or should it be treated as the authoritative snapshot of the approved manuscript at Gate 5?

**Why it is needed:** The ratified model requires derived views to be non-authoritative and rebuildable. The export skill compiles a Markdown manuscript from approved chapter drafts. The compiled manuscript is a projection of the canonical chapter drafts; it is not itself the canonical prose. The question is whether to label it as a derived view or as the authoritative export snapshot.

**Options:**
1. Label the exported manuscript as a derived view that is non-authoritative and rebuildable from canonical chapter drafts and story-state metadata.
2. Treat the exported manuscript as the authoritative snapshot of the approved manuscript at Gate 5, with the canonical chapter drafts remaining the authoritative prose.
3. Label the exported manuscript as a derived view for rebuild purposes, but treat the Gate 5 approval as the authority point for the exported snapshot.

**Recommended option:** Option 3, because it aligns with the ratified derived-view model (the compilation is rebuildable from canonical files) while recognizing that the Gate 5 approval is the authority point for the exported snapshot.

**Consequences:**
- Option 1: Cleanest alignment with the ratified derived-view model; the export is not itself canon.
- Option 2: Risks treating the compiled manuscript as authoritative in a way that conflicts with the ratified model (the canonical prose remains the chapter drafts).
- Option 3: Balances derived-view rebuildability with the Gate 5 snapshot authority.

**Blocked until decided:** No, for the export skill's existing behavior (it already compiles from approved drafts). Yes, for the labeling and the provenance record for the export snapshot.

### D12: Two-host evidence timing

**Decision question:** Should the two-host evidence be gathered as part of the vertical slice, or should it be a separate later activity?

**Why it is needed:** The ratified model requires two-host evidence. The question is whether to include it in the vertical slice or to defer it.

**Options:**
1. Include two-host evidence in the vertical slice.
2. Build the vertical slice on one host first, then gather two-host evidence as a separate activity.
3. Defer two-host evidence until after the vertical slice and after the host-adapter boundary is defined.

**Recommended option:** Option 2, because the vertical slice should demonstrate the deterministic state spine and the creative/HITL path on the primary host first, with two-host evidence as a subsequent checkpoint.

**Consequences:**
- Option 1: Fastest portability evidence if it succeeds; may be harder to isolate host-adaptation gaps.
- Option 2: Staged portability evidence; each host can be compared after the primary-host slice is stable.
- Option 3: Lowest immediate burden; leaves portability evidence open longer.

**Blocked until decided:** No, for the requirement to gather two-host evidence eventually. Yes, for the timing, if Dave wants to decide whether portability evidence is a vertical-slice deliverable or a separate activity.

---

## 13. File-Level Change Inventory

This is the handoff map for a future implementation branch. It lists proposed paths, whether each is existing or new, the proposed action, the ratified driver, dependencies, whether a decision is needed, and the implementation phase.

| Proposed path | Existing or new | Proposed action | Ratified driver | Dependencies | Decision needed | Implementation phase |
|---|---|---|---|---|---|---|
| `schemas/story-state.schema.json` | Existing | Reclassify `author_preferences` as author memory; add transaction/audit field references; add cross-file reference integrity; possibly remove or profile-condition Dust & Ash–specific preference fields; align `continuity_risks` as editorial/diagnostic state | RR-2, RR-7, RR-9, RR-13, RR-28, RR-29 | Stage 1, Stage 2, D1, D2, D8, D11 | D1, D2, D8 | Stage 2 |
| `schemas/character-state.schema.json` | Existing | Add structured provenance fields; split `emotional_state`/`physical_state` into observable canon and inference sub-structures (proposed); add transaction/audit field references; add cross-file reference integrity for `last_seen_chapter` and `character_id`; align `source_lineage_note` as summary of structured provenance | RR-2, RR-7, RR-9, RR-13, RR-28 | Stage 1, Stage 2, D2, D8 | D2, D8 | Stage 2 |
| `schemas/scene-state.schema.json` | Existing | Add transaction/audit field references; reclassify `continuity_notes`, `evaluation_notes`, `word_count`, `title` as non-authoritative; add cross-file reference integrity for `pov_character_id`, `setting_ref`, `chapter_id`; extract or profile-condition `dread_elements_used`, `symbolic_elements_used`, `thread_pulls_triggered` | RR-2, RR-6, RR-7, RR-9, RR-13, RR-28 | Stage 1, Stage 2, D2, D7, D8 | D2, D7, D8 | Stage 2 |
| `schemas/continuity.schema.json` | Existing | Add deterministic-versus-judgment-based classification; add shared finding envelope fields (proposed); add transaction/audit field references; reclassify check results as non-authoritative diagnostic state; add cross-file reference integrity for `character_id`, `event_id`, `promise_id`; align `check_history` with general audit record | RR-2, RR-6, RR-7, RR-9, RR-13, RR-17, RR-19 | Stage 1, Stage 2, D2, D4, D6, D8 | D2, D4, D6, D8 | Stage 2 |
| `schemas/author-memory.schema.json` (proposed) | New | Define author-memory schema/store for author preferences, style profile, tone axioms, forbidden tropes, decision history, project-profile choices; read by relevant skills; not story canon | RR-29 | Stage 1, Stage 2, D1, D9 | D1, D9 | Stage 2 |
| `schemas/audit.schema.json` or audit store (proposed) | New | Define audit record for canonical transactions and promoted facts: who submitted what, what was applied, expected_revision, check summary, resulting revision | RR-7, RR-9 | Stage 2, Stage 3, D5, D8 | D5, D8 | Stage 3 |
| `schemas/shared-finding.schema.json` or shared envelope (proposed) | New | Define shared finding/disposition envelope with confidence and determinism classification for continuity, prose-editing, and reader-simulation findings | RR-19, RR-20 | Stage 2, Stage 3, D6 | D6 | Stage 3 |
| Transaction/state-update contract (proposed) | New | Define transaction boundary, expected-revision guard, atomic-application rule, rollback rule, and audit record entry for structured-state updates | RR-7, RR-8 | Stage 2, Stage 3, D5, D8 | D5, D8 | Stage 3 |
| Canon-promotion mechanism (proposed) | New | Define promotion path for each skill and field category: prose/proposed fact → author approval + transaction validation → canon state field, with provenance capture and conflict blocking | RR-3, RR-4, RR-5, RR-9 | Stage 3, Stage 4, D5 | D5 | Stage 5 |
| Derived-view definitions (proposed) | New | Define derived views (reader-simulation manuscript-only view, continuity-report view, scene-outline view, compiled manuscript, context packages), rebuild triggers, and non-authoritative/rebuildable labeling | RR-6, RR-12 | Stage 4, Stage 5, Stage 6, D4, D11 | D4, D11 | Stage 6 |
| Context-package contract (proposed) | New | Define context-package contract: project/book identifiers, scope, compact source map, revision markers, authority boundaries, derived-overlay labeling, provenance note | RR-10, RR-11 | Stage 5, Stage 6, Stage 7 | D3 (for timing) | Stage 7 |
| Validator (proposed) | New | Build schema validator and Markdown contract checks; reject operations whose required state is missing or invalid | RR-13, RR-16 | Stage 2, Stage 3, Stage 4 | None beyond implementation authorization | Stage 4 |
| Continuity checker (proposed) | New | Build minimum viable continuity checker with deterministic checks and judgment-based classification | RR-13, RR-16, RR-19 | Stage 2, Stage 3, Stage 4 | None beyond implementation authorization | Stage 4 |
| Fixtures (proposed) | New | Build valid and invalid project instances for validation, transaction, continuity, and derived-view testing | RR-13, RR-16 | Stage 2, Stage 3, Stage 4 | D10 (for scope) | Stage 4 |
| Tests (proposed) | New | Build schema validation tests, cross-file consistency tests, stale-revision rejection tests, conflict-blocking tests, audit-history tests, derived-view reproducibility tests, context provenance tests, context-blind reader isolation tests, editorial approval enforcement tests, HITL mode declaration tests, no-silent-switching tests, deterministic two-host equality tests, judgment-contract compliance tests | RR-13, RR-16 | Stage 4, Stage 5, Stage 6, Stage 7, Stage 8, Stage 9 | D10 (for scope) | Stage 4 onward |
| CI configuration (proposed) | New | Run schema validation, transaction tests, continuity checks, and derived-view reproducibility checks on every commit | RR-13, RR-16 | Stage 4, Stage 12 | None beyond implementation authorization | Stage 12 |
| Host-adapter boundary (proposed) | New | Separate host-neutral contracts from host-adapter concerns; define capability-detection contract | RR-13, RR-14 | Stage 8, Stage 11 | D12 (for timing) | Stage 11 |
| `skills/fiction-orchestrator/SKILL.md` | Existing | Redefine context-package contract, state-update transaction contract, HITL mode declaration and selection criteria, anti-switching rule, framework-vs-project-gate separation, layered-hybrid authority language | RR-2, RR-4, RR-5, RR-7, RR-10, RR-11, RR-21, RR-22, RR-23, RR-24, RR-25, RR-26 | Stage 1, Stage 2, Stage 3, Stage 5, Stage 6, Stage 7, Stage 8, Stage 9 | D3, D5, D8 | Stage 8 |
| `skills/concept-development/SKILL.md` | Existing | Treat initialization as a canonical transaction; add provenance for approved concept facts; clarify reusable-core versus profile fields in story bible | RR-4, RR-7, RR-9, RR-28 | Stage 1, Stage 2, Stage 3, Stage 5 | D1, D2, D7 | Stage 5 |
| `skills/worldbuilding/SKILL.md` | Existing | Treat worldbuilding state updates as canonical transactions; add provenance for codified world rules; define reload context | RR-4, RR-7, RR-9, RR-10 | Stage 1, Stage 2, Stage 3, Stage 5 | D1, D2, D7 | Stage 5 |
| `skills/character-development/SKILL.md` | Existing | Extract V4 pipeline, Biblical evidence tiers, King craft integration, epistemic verb discipline into Dust & Ash profile; treat character-state creation/updates as transactions with provenance; reclassify observable canon vs inference | RR-4, RR-7, RR-9, RR-10, RR-28 | Stage 1, Stage 2, Stage 3, Stage 5, Stage 10 | D1, D2, D7, D9 | Stage 5, then Stage 10 |
| `skills/narrative-architecture/SKILL.md` | Existing | Extract Thread Pull design into Dust & Ash profile; treat architecture state updates as transactions with provenance; add provenance for approved promise/payoff status | RR-4, RR-7, RR-9, RR-10, RR-28 | Stage 1, Stage 2, Stage 3, Stage 5, Stage 10 | D2, D7 | Stage 5, then Stage 10 |
| `skills/scene-planning/SKILL.md` | Existing | Extract dread/symbolic/Thread Pull planning into Dust & Ash profile; treat scene-state updates as transactions; reconcile outline approval with batch-approval and HITL mode rules | RR-4, RR-7, RR-9, RR-10, RR-20, RR-28 | Stage 1, Stage 2, Stage 3, Stage 5, Stage 10 | D2, D7 | Stage 5, then Stage 10 |
| `skills/scene-writing/SKILL.md` | Existing | Extract Thread Pull execution and dread/symbolic deployment into Dust & Ash profile; treat scene-state and story-state updates as transactions; reclassify continuity_notes as editorial/diagnostic state; declare HITL mode for drafting; add provenance for knowledge-state changes | RR-4, RR-7, RR-9, RR-10, RR-20, RR-21, RR-22, RR-28 | Stage 1, Stage 2, Stage 3, Stage 5, Stage 10 | D2, D7 | Stage 5, then Stage 10 |
| `skills/continuity/SKILL.md` | Existing | Add deterministic-versus-judgment-based classification; align continuity-state updates with transaction/audit contract; align findings with shared finding envelope; declare stopping rule; declare HITL mode; ensure conflict-blocking enforcement; evaluate derived-view rebuild for continuity-state | RR-4, RR-5, RR-6, RR-7, RR-9, RR-13, RR-17, RR-19, RR-20, RR-21, RR-22, RR-23 | Stage 1, Stage 2, Stage 3, Stage 4, Stage 5, Stage 8, Stage 9 | D2, D4, D5, D6 | Stage 4, then Stage 8, then Stage 9 |
| `skills/prose-editing/SKILL.md` | Existing | Separate diagnosis from repair; enforce batch-approval model; declare HITL mode; enforce per-change author disposition and apply-only-approved-changes; reclassify evaluation_notes as editorial/diagnostic state; align with shared finding envelope; add provenance for approved editorial changes; distinguish mechanical fixes from judgment calls | RR-4, RR-6, RR-7, RR-9, RR-17, RR-19, RR-20, RR-21, RR-22, RR-23, RR-24, RR-25 | Stage 1, Stage 2, Stage 3, Stage 5, Stage 8, Stage 9 | D2, D6 | Stage 5, then Stage 8, then Stage 9 |
| `skills/reader-simulation/SKILL.md` | Existing | Redefine first pass as manuscript-only, no Story Bible, no outline, no dossier, no continuity report, no narrative architecture; add optional informed second pass as labeled overlay; label report as derived view with no unique facts; add context-package provenance labeling; declare HITL mode; formalize judgment-based output contract | RR-6, RR-10, RR-11, RR-12, RR-17, RR-18, RR-21, RR-22 | Stage 1, Stage 2, Stage 3, Stage 6, Stage 7, Stage 8, Stage 9 | D3, D11 | Stage 6, then Stage 8, then Stage 9 |
| `skills/export/SKILL.md` | Existing | Label compiled Markdown manuscript as derived view that is non-authoritative and rebuildable; treat export compilation as derived-view rebuild; align readiness checks with authority and conflict rules; declare HITL mode; add provenance for export snapshot | RR-4, RR-6, RR-7, RR-9, RR-13, RR-21, RR-22, RR-23, RR-24 | Stage 1, Stage 2, Stage 3, Stage 6, Stage 8, Stage 9 | D11 | Stage 6, then Stage 8, then Stage 9 |
| `templates/SKILL_TEMPLATE.md` | Existing | Possibly add fields for HITL mode, transaction/approval, and provenance (proposed); no change required to the template's core structure | RR-21, RR-22, RR-23, RR-24, RR-9 | Stage 8 | D6 (for envelope fields) | Stage 8 |
| `templates/story-bible-template.md` | Existing | Add authority classification guide (proposed); evaluate profile-conditional marker for Dust & Ash–specific fields; add per-fact provenance capture guidance | RR-9, RR-28 | Stage 1, Stage 2, Stage 5, Stage 10 | D1, D2, D7 | Stage 5, then Stage 10 |
| `templates/character-dossier-template.md` | Existing | Move or profile-condition Biblical/Historical Evidence Base and King Style-and-Craft Pressure Integration sections; add observable-canon vs inference guidance | RR-9, RR-28 | Stage 1, Stage 2, Stage 5, Stage 10 | D1, D2, D7 | Stage 5, then Stage 10 |
| `templates/scene-template.md` | Existing | Move or profile-condition Dread Element column, Symbolic Element column, and Thread Pulls section; add guidance distinguishing draft (authoritative Markdown) from outline, continuity notes, and evaluation notes | RR-6, RR-9, RR-28 | Stage 1, Stage 2, Stage 5, Stage 10 | D2, D7 | Stage 5, then Stage 10 |

---

## 14. Acceptance Criteria for the Impact Plan

The plan itself can be accepted or rejected without beginning implementation. Acceptance criteria:

1. **Completeness.** The plan reads every governing document, all four schemas, all eleven skills, and all four templates, and it says so in Section 2.
2. **Distinction discipline.** Every conclusion is labeled as a ratified requirement, existing prototype behavior, confirmed gap, proposed implementation detail, deferred decision, or no change required, and the labels are used consistently in Sections 3 through 6.
3. **Evidence grounding.** Every claimed prototype behavior cites a concrete tracked path and, where useful, the relevant field or section.
4. **Traceability.** Every proposed change traces to a ratified requirement, a confirmed prototype gap, or an explicitly labeled recommendation.
5. **No unauthorized claims.** The plan does not describe any proposed capability as already implemented, does not claim validation passed because JSON parses, and does not turn judgment-based literary evaluation into a deterministic claim.
6. **Decision register.** The plan provides a numbered decision register with decision question, why it is needed, options, recommended option, consequences, and whether implementation is blocked.
7. **File-level handoff map.** The plan concludes with a definitive file-level change inventory that a future implementation agent can use as a handoff map.
8. **No implementation.** The plan does not modify, create, or authorize any schema, skill, template, validator, script, fixture, test, CI artifact, dependency, or Dust & Ash extraction.
9. **No merge or branch manipulation.** The plan does not merge the integration branch, merge the planning branch, create or merge a pull request, alter `development`, `main`, or either disconnected architecture branch, or force-push, rebase, reset, or delete history.
10. **Decision-preserving.** The plan records uncertainty and decisions required where evidence is missing or contradictory, and does not fill gaps through assumption.

---

*End of plan. This document is planning and analysis only. It does not authorize implementation, schema changes, skill changes, template changes, validator creation, test creation, CI work, dependency installation, or Dust & Ash extraction. A separate explicit authorization is required before any implementation begins.*
