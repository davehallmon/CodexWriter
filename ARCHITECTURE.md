# CodexWriter — Architecture

> This document describes the ratified high-level architecture of CodexWriter, **the existing provisional prototype that already exists in the repository**, and the design detail that remains deferred or unimplemented.
>
> **Reading rule:** This document labels each concept as one of four classes. When a concept is unbuilt, it is labeled as such; unbuilt validators, transaction tooling, context assemblers, registries, adapters, or tests are documented as design targets, not as operational capabilities.

## 1. Ratified architecture

The ratified architecture is the layered hybrid model recorded in the CodexWriter ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3`. It is described in four parts: authority, durable state, context and portability, and editorial and HITL behavior.

### 1.1 Authority model

The ratified authority model is a layered hybrid with three distinct authorities for approved project material:

- **Approved Markdown manuscript files are authoritative for exact narrative wording and for what the reader encounters.** No structured state field may silently rewrite a paragraph, sentence, dialogue line, or chapter that the author wrote or approved.
- **Approved structured state is authoritative for machine-checkable intended canon facts and for workflow fields that the schema explicitly governs.** These include state revisions, phase, phase_gate, character status, chapter sequence, scene outline/draft status, schema-validity fields, and IDs that the system uses to route and cross-reference work. A machine-checkable fact may originate in prose, but it becomes intended project canon only after author approval and a validated promotion transaction.
- **Derived views, summaries, indexes, registries, reports, and context packages are never authoritative and contain no unique facts.** They are rebuildable projections from canonical project files. A derived artifact may be discarded or regenerated without loss of unique facts.

When Markdown and structured state disagree, the disagreement blocks publication or state promotion until an explicit reconciliation is recorded. The reconciliation must say which artifact wins and why; the loser's subsequent reads must report the same ruling. No layer may silently overwrite another. The only exceptions are deterministic derived artifacts that are explicitly documented as rebuildable views and contain no unique facts.

### 1.2 Durable state and transactions

One transaction owns the transition from one canonical authority state to the next canonical authority state. It wraps the prior authority, the new authority, a human-readable summary, and runnable check information into one observed change. The canonical authority advances only via that transaction. An expected-revision guard rejects stale sequential writes. The audit record captures who submitted what, what was applied, and what the check marked.

At the architecture level, one transaction is one application step that advances the canonical state or a canonical artifact in a way the schema and the approved authority model recognize. A transaction may touch several files or several state fields, but it is one atomic commitment from the system's point of view: either the whole canonical transition is applied, or none of it is. Canonical advancement occurs through the declared transaction mechanism. On Git-based workflows, that may be expressed as one commit or one merge, but the commit/merge is the transaction boundary, not an open-ended editing session.

Promotion into canon requires author approval for narrative content, plus transaction validation for structured fields. A structured update that is syntactically valid but semantically wrong must still be resolved before it is written. A fact that first appears in prose is proposed structured state, not canon; it must pass the same gate as any other promotion candidate.

A rollback is not necessarily a literal undo of file bytes; it is the establishment of the prior canonical revision or the application of a new compensating transaction that returns the canonical state to the prior intended revision. Partial failure is detected by the schema/validation/coherence checks that must all pass for the transaction to apply, by the expected-revision guard on the canonical authority, and by any host-level write verification. If any part cannot be committed atomically, the system applies nothing to the canonical authority and records the rejection.

The addendum does not yet specify the exact serialization, locking, or host-level atomicity guarantees; it specifies that the boundary, the failure detection, the recovery rule, and the counter coordination must be defined before any implementation claims atomic multi-file or rollback behavior.

### 1.3 Context, views, and portability

The context-assembly layer has a minimum responsibility that is ratified, with detailed LOD thresholds deferred until after the first vertical slice:

1. Identify the task and pull the smallest set of inputs that could plausibly change the output if omitted.
2. Separate what must be current prose from what can be structured or summarized.
3. Keep derived overlays explicitly labeled so they never masquerade as primary content.
4. Preserve a compact, reviewable provenance note for what was assembled, from which revisions, and what was excluded.
5. Honor the conflict rule from the authority model: if a loaded summary conflicts with the declared canonical source, the declared canonical source controls the derived artifact. If the underlying approved prose and structured canon conflict, apply the authority-model reconciliation rule rather than choosing either automatically.

The context layer may include, exclude, summarize, or shard as follows:

- It may load full prose when language, voice, dialogue rhythm, ambiguity, or exact wording is the point.
- It may load structured state, registries, indexes, and summaries for far-field information.
- It may shard by book/scene/character/state domain and assemble only the shards relevant to the task.
- It may exclude material that is cold, irrelevant, or lower-authority for the task.
- It must not exclude information whose omission could make the task wrong.

Every context package records the project/book identifiers, the scope, a compact source map, and the revision markers for the loaded items. The package does not assert authority beyond what the source map shows.

Derived views serve different consumers differently:

- Authors: readable drafts, story bible, dossiers, outline, chapter prose.
- Writers: tight scene-oriented context with current character/state and relevant world facts.
- Continuity/editors: structured state plus the relevant prose windows and the relevant registry/current-state entries.
- Readers via reader simulation: manuscript-only view for the baseline pass; a separate labeled overlay only for the optional second pass.

Schema-aware portability means a host can validate JSON against the schemas, apply defined structural or contract checks to Markdown where such rules exist, use judgment-based review for narrative content that cannot be mechanically validated, respect the authority and conflict rules, route by structure and IDs, run or reject operations whose required state is missing or invalid, and regenerate derived views from canonical files.

Host-neutral: Markdown/JSON inputs/outputs, schema validation, authority rules, conflict rules, derived-view regeneration, transaction record shape.

Host adapter: prompt delivery, tool invocation, file access conventions, agent subprocess management, runtime logging, interaction surfaces, and any capability that a particular runtime surfaces better than another.

Portability evidence falls into two classes:

- **Deterministic invariants.** Schema results, transaction acceptance or rejection, revision counters, promoted fact values, provenance records, audit entries, and regenerated registry contents must match across hosts.
- **Judgment-based outputs.** Prose, editorial diagnosis, and reader-simulation findings must comply with the same scope and output contracts, but need not match in wording, emphasis, or conclusions.

Portability is demonstrated when the same generic project and same task produce comparable results on two hosts, the differences are documented and explainable as host-adaptation gaps rather than different canon, the authority/conflict rules produce the same resolution decisions on both hosts, and a derived view rebuild yields the same content from the same canonical files on both hosts.

### 1.4 Editorial and HITL behavior

Reader simulation begins with a context-blind manuscript-only pass. The blind pass delivers a reader's experiential report in its own words: what it understood, what it missed, where it lost interest, where it felt engaged, where it was confused, and where the ending landed. An optional second pass may load selected author context and add diagnostic interpretation, but the first pass stands alone and can be read without author privilege.

Editorial passes each have a declared scope and a declared stopping rule. Diagnosis and repair are separate: one pass produces findings; another pathway applies approved changes.

The substantive prose editing model is batch-approval:

- Diagnose the scene/chapter for the declared editorial scope.
- Present one coherent batch of exact proposed changes, each change localized enough to accept or reject individually.
- Author accepts, rejects, or modifies individual changes.
- Apply only the approved changes.
- Approval of a general editing goal is not permission for unrestricted rewriting. Each change still needs its own disposition unless the author explicitly authorizes a broader move with a clear boundary.

The system operates in one of two HITL modes. It must declare the mode before work begins, and it must not switch modes silently during a workflow.

**Interactive mode.** The author reviews and approves a proposed batch before it is applied to the working canonical artifact or state. Interactive mode is required when a change will be applied directly to the current canonical artifact or state before a branch/diff review, when the action has an external or destructive effect, or when the author has reserved that decision for interactive review.

**PR-boundary mode.** The agent may produce bounded canon-affecting proposals—including prose edits, state patches, promotions, deletions, and continuity updates—on an isolated non-canonical branch. Those proposals do not become canon unless the author approves and merges them. PR-boundary mode is permitted when no direct canonical mutation or external destructive action occurs before review.

Both modes preserve the batch-approval rule. They differ in when and where the author reviews, not in whether substantive changes require approval. Silent mode switching is not permitted; if new information during a workflow changes the appropriate mode, the system stops and asks for a fresh decision on the new scope before continuing.

Framework approvals (state model, schema set, skill contracts, release decisions) belong to the framework track. Dust & Ash story phase gates belong to the Dust & Ash project track. They use different decision subjects and different approval records.

## 2. Existing provisional prototype

The repository already contains a provisional implementation prototype. It was built before the seven-source synthesis and before this ratification. It is preserved, but the ratified architecture controls what the prototype is allowed to claim about itself.

### 2.1 What the prototype provides

- **A working skill set of eleven `SKILL.md` files total**: ten in the current working core (`fiction-orchestrator`, `concept-development`, `worldbuilding`, `character-development`, `narrative-architecture`, `scene-planning`, `scene-writing`, `continuity`, `prose-editing`, `reader-simulation`) plus one optional `export` extension.
- **A proposed JSON state model defined through four schema files** — `schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, and `schemas/continuity.schema.json` — plus related skill contracts. The repository does not contain project instances named `story-state.json`, `character-state.json`, `scene-state.json`, or `continuity-state.json`.
- **A specialist role taxonomy** derived from Lensetek, present in the prototype.
- **A five-phase pipeline shape** with phase gates, present in the prototype.
- **Example voice-preservation guidance** in scene-writing and prose-editing, present in the prototype.
- **Story-state vocabulary present in the prototype** including POV assignments, knows/doesn't-know lists, and promise/payoff tracking. Thread Pull design is designated Dust & Ash profile material, not ratified reusable-core architecture.

### 2.2 What the prototype is not

- The JSON state model is a **provisional implementation prototype**, not ratified architecture. It is preserved but not ratified. Its classification was established by the alignment evaluation decision record.
- The prototype does not yet implement the transaction mechanism, stale-revision protection, provenance capture, audit records, rebuildable derived views, an author-memory layer, a context assembler, schema-aware portability adapters, a context-blind reader-simulation baseline, the separate diagnosis/repair editorial model, the batch-approval editorial model, or the two-mode HITL distinction.
- The prototype does not yet implement validators, transaction tooling, continuity checks beyond described-but-not-executed rules, a shared structured finding schema, or the generic vertical slice.

### 2.3 How the prototype relates to the ratified model

The prototype is the provisional substrate on which the ratified model is to be aligned. Where the prototype already embodies a ratified pattern, that pattern may be treated as present in prototype form and described as such. Where the prototype describes behavior that contradicts the ratified model, the prototype description must be corrected to stop claiming the contradictory behavior as present. Where the ratified model requires new capabilities, those capabilities are deferred or unimplemented until built.

This ratification does not authorize schema or skill-contract changes. Documentation alignment is now complete on the isolated branch `architecture/ratified-alignment` and pending review. The file-by-file schema and skill impact plan is the next **prospective** deliverable, subject to explicit authorization after documentation alignment is reviewed. It is not presently authorized.

## 3. Not yet implemented

The following ratified elements have no implementation in the current prototype. They are described here as architecture, not as operational capability.

- **Transaction mechanism.** One observed transaction plus one atomic filesystem write of the new canonical authority; on Git-based workflows, the commit or merge is the transaction boundary. No transaction tooling exists yet.
- **Stale-revision protection.** An expected-revision guard that rejects stale sequential writes. None exists yet.
- **Audit history.** A record that captures who submitted what, what was applied, and what the check marked. None exists yet.
- **Provenance on promoted facts.** A structured canon record that retains provenance pointing to the source passage, decision, or approval that established each promoted fact. None exists yet.
- **Rebuildable derived views.** Indexes, registries, check reports, derived summaries, and context packages that are explicitly documented as rebuildable projections from canonical project files with no unique facts. The prototype does not yet mark any derived view this way, does not yet rebuild any derived view from canonical files on change, and does not yet assert that any current derived artifact is non-authoritative.
- **Context assembly.** A smallest-sufficient-context layer with the ratified minimum responsibility, explicit provenance, derived-overlay labeling, and conflict honoring. None exists yet.
- **LOD sharding and projection size thresholds.** Deferred until after the first vertical slice.
- **Author-memory layer.** A separate author-profile store, not story canon, read by relevant skills. None exists yet.
- **Schema-aware portability.** Schema validation against the schemas, defined structural/frontmatter/contract checks on Markdown where such rules exist, judgment-based review for narrative content, routing by structure and IDs, and rejection of operations whose required state is missing or invalid. None exists yet as an implemented capability.
- **Context-blind reader-simulation baseline.** A first pass with manuscript only, no Story Bible, no outline, no dossier, no continuity report, no narrative architecture. The current prototype reader-simulation skill does not yet operate this way.
- **Separate diagnosis and repair.** Editorial passes that produce findings, plus a separate pathway that applies approved changes. The current prototype describes continuity checks and editorial guidance but does not yet enforce the separate-diagnose/repair split as built behavior.
- **Batch-approval editorial model.** One coherent batch of exact proposed changes, with per-change author disposition and application of only the approved changes. None exists yet as enforced behavior.
- **Two-mode HITL distinction.** Interactive mode and PR-boundary mode, declared before work begins, with the objective selection criteria from the ratified model. None exists yet as built behavior.
- **Validators and test harness.** Schema validator, minimum viable continuity validator, generic fixtures, smoke tests, and CI. None exist yet.
- **Generic vertical slice.** A staged representative workflow on two hosts with fixtures, validators, tests, and CI. Not yet implemented.

## 4. Deferred design detail

The following design details are not yet frozen. They are correct as direction, but they are not yet specified enough to claim as finalized architecture.

- **Exact serialization, locking, and host-level atomicity guarantees for transactions.** The ratified model specifies the boundary, failure detection, recovery rule, and counter coordination, but not the exact mechanism.
- **Exact LOD thresholds and projection sizes for context sharding.** The minimum responsibility is ratified; the exact sharding boundaries, LOD levels, and projection sizes are deferred until after the first vertical slice.
- **Exact derived-view projection schemas.** Rebuildability is ratified; the exact shapes of each derived view are deferred until implementation.
- **Exact porting checklist.** The host-neutral/host-adapter boundary and two-host evidence requirement are ratified; the exact checklist is deferred until after the vertical slice.
- **Exact schemas affected by the authority model.** The authority model requires schemas to distinguish canon fields from editorial fields, but the exact field-by-field reclassification is not yet specified; it is the subject of the authorized file-by-file impact plan that comes after documentation alignment.
- **Exact continuity finding schema.** A shared envelope with confidence and determinism classification is recommended, but not yet specified in detail.
- **Exact promotion and approval paths for project initialization, state-update, and editorial skills.** The paths are ratified in principle; the exact per-skill contract is deferred until schema and skill-alignment review.

## 5. Goals

- Provide a modular, version-controlled suite of AI fiction-writing skills.
- Preserve persistent story state and support deterministic continuity checks where the underlying facts are machine-checkable.
- Support specialist agent roles for planning, drafting, reviewing, editing, continuity, and reader testing.
- Manage long-context projects through sharding, summaries, selective loading, and level-of-detail strategies.
- Keep a human author in the loop at meaningful creative and scope-transition points.
- Separate core authoring skills from cross-cutting infrastructure and optional publishing/adaptation extensions.

## 6. Source repositories reviewed

The seven source repositories that informed the ratified architecture are:

| Repository | Primary strength | License status |
|---|---|---|
| lensetek/Fiction-book-agent-skills | Specialist role taxonomy and end-to-end workflow breadth | MIT badge/link; LICENSE currently missing |
| danjdewhurst/story-skills | Persistent story state and deterministic continuity tooling | MIT |
| haowjy/creative-writing-skills | Writer/critic/editor separation, voice preservation, story memory | Apache 2.0 |
| JeroTan/novel-writer-english | Constitution, clarification, context reload, document sharding | MIT; translated/re-architected derivative |
| wgwtest/novel-writing | Narrative epistemology, POV boundaries, context LOD, craft review | MIT |
| rhavekost/author-toolkit | Context-blind reader testing, focused editorial passes, stopping points | MIT; includes separately attributed vendored material |
| zenstory-ai/oh-story-claudecode | Layered state management, transactions, runtime portability, author memory | MIT |

See `docs/architecture-audit.md` for direct evidence, licensing links, and audit notes.

## 7. Phase 1 guardrails that produced the synthesis

The Phase 1 source analyses established the evidence base that led to ratification:

- Lensetek supplied the initial responsibility taxonomy, not automatically the implementation model.
- The seven source analyses had to document observed state-storage and workflow behavior before CodexWriter chose a canonical state design. **That guardrail existed, was violated when the prototype declared JSON canonical prematurely (before Rhavekost was analyzed), and was restored through the seven-source synthesis and the subsequent architecture ratification.**
- Zenstory's single-authoritative-JSON state was a candidate pattern only, not the adopted design. The ratified model is a layered hybrid, not a single-authority JSON model.
- `continuity` remained one CodexWriter skill during Phase 1. A future split between state maintenance and validation is deferred.
- Candidate capabilities could be documented before they became final skill names.

## 8. Control and coordination

- `fiction-orchestrator` — routes work, enforces workflow boundaries, and coordinates specialist capabilities.
- Project setup / runtime capability detection — candidate infrastructure capability.
- Context assembly — ratified as a minimum-responsibility cross-cutting capability, with detailed thresholds deferred.
- Persistent-state maintenance — ratified in principle as transactional canonical-state maintenance; exact tooling is not yet implemented.

## 9. Creative pipeline

The current prototype creative pipeline includes:

- `concept-development`
- `worldbuilding`
- `character-development`
- `narrative-architecture`
- `scene-planning`
- `scene-writing`

A story constitution or creative contract is a **source-informed candidate concept from JeroTan**, not a ratified core concept. Clarification gates are a **source-informed candidate from JeroTan**, not a ratified workflow rule. Whether the constitution and clarification concepts become CodexWriter artifacts, stages, or responsibilities is an unresolved module/workflow question.

**World, character, and plot work may iterate rather than execute in a rigid one-way order** is existing prototype behavior, not a ratified workflow rule. The prototype does not impose a rigid one-way order; whether iteration should be treated as an architectural principle is not yet decided.

## 10. Evaluation and revision

The current prototype evaluation and revision skills are:

- `prose-editing`
- `continuity` — kept as one skill during Phase 1
- `reader-simulation`

A developmental/story review distinct from `prose-editing` is a **source-informed candidate** (Haowjy, Rhavekost, JeroTan), not a ratified distinct module. Whether it becomes a separate skill or a mode inside editing is unresolved.

Deliberate context isolation for reader simulation is a ratified requirement: the first pass is context-blind, manuscript only.

## 11. Optional extensions

Candidate capabilities present in one or more source repositories but not currently proposed as mandatory stages in the initial novel-authoring core:

- market/trend research
- benchmark/story deconstruction
- existing-manuscript import
- style/voice profiling
- comic/webtoon adaptation
- children's-fiction adaptation
- accessibility formatting
- publishing/export
- project/update maintenance

## 12. Current proposed skill modules

The working prototype skill set consists of the eleven `SKILL.md` files in the repository:

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

The exact specialist-role taxonomy and current skill count are prototype behavior, not ratified architecture.

Potential additions such as `story-review`, `context-manager`, `story-state-manager`, `story-constitution`, or `project-maintenance` remain research hypotheses. The source analyses are complete; whether any of these become CodexWriter modules depends on the schema and skill-alignment review, not on the source analyses alone.

## 13. Persistent story state — ratified hybrid model

CodexWriter preserves durable story knowledge through the ratified layered hybrid model, not through a single authoritative JSON file and not through Markdown alone.

The ratified state model distinguishes:

- **Approved Markdown manuscript files** — authoritative for exact narrative wording.
- **Approved structured state** — authoritative for explicitly designated, approved machine-checkable intended canon and workflow fields.
- **Derived views** — rebuildable projections with no unique facts.

The existing JSON state model is defined by four schema files — `schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, and `schemas/continuity.schema.json` — and related skill contracts. It is a **provisional implementation prototype** pending separately reviewed schema alignment. It is preserved but not ratified. It may prove correct, partially correct, or in need of revision; that determination requires the prospective file-by-file schema and skill impact plan and a separate approval.

Only after the ratified model and the authorized schema review should CodexWriter finalize the exact schema set. The hybrid model is the ratified decision; the exact schemas are a deferred implementation detail until the impact plan is approved.

## 14. Context management strategy

The ratified minimum responsibilities of a context-assembly layer are:

1. Identify the task and pull the smallest set of inputs that could plausibly change the output if omitted.
2. Separate what must be current prose from what can be structured or summarized.
3. Keep derived overlays explicitly labeled so they never masquerade as primary content.
4. Preserve a compact, reviewable provenance note for what was assembled, from which revisions, and what was excluded.
5. Honor the conflict rule from the authority model: if a loaded summary conflicts with the declared canonical source, the declared canonical source controls the derived artifact. If the underlying approved prose and structured canon conflict, apply the authority-model reconciliation rule rather than choosing either automatically.

The following context strategies are **permitted** under that minimum responsibility, but are not ratified as exact contracts:

- **Sharding** for large projects.
- **Level-of-detail loading**: full prose near the current task and structured/summary context for distant material.
- **Pre-write context reload** rather than trusting conversational memory — a permitted strategy, not a mandated procedure.
- **Targeted full-text expansion** when style, ambiguity, dialogue rhythm, or exact prose matters.
- **Post-write state/context updates** when durable facts change — a permitted strategy, not a mandated procedure.
- A **smallest-sufficient-context rule**: load information whose omission could cause the current task to be wrong, while excluding unrelated cold context.

Source-informed implementation guidance (from wgwtest, JeroTan, and Zenstory) suggests LOD levels, sharding boundaries, reload contracts, and conflict-precedence rules. Those remain guidance for the eventual implementation, not ratified architecture.

When summaries, structured state, and manuscript prose disagree, the ratified authority model applies: neither Markdown nor structured state automatically wins across the board, derived summaries are rebuildable and non-authoritative, and conflicts block the dependent operation until reconciliation is recorded.

## 15. Human-in-the-loop strategy

The ratified HITL rules are:

- **Batch approval** — diagnose first, present one coherent batch of exact proposed changes, and apply only the approved changes.
- **Diagnosis before repair** — editorial passes produce findings; a separate pathway applies approved changes.
- **Context-blind reader baseline** — the first reader-simulation pass uses manuscript only.
- **Interactive versus PR-boundary review** — the system declares the mode before work begins; the modes differ in when and where approval occurs, not in whether substantive changes require approval.
- **No silent mode switching** — if new information changes the appropriate mode, the system stops and asks for a fresh decision.
- **Framework approvals separate from story gates** — framework approvals belong to the framework track; Dust & Ash story phase gates belong to the Dust & Ash project track.

Lensetek's phase approval gates remain an important reference. The exact phase-gate set remains **prototype- or profile-specific**: the ratified model does not mandate a specific list of gates, only the rules above about how approval, diagnosis, review, and separation work.

## 16. Deterministic vs. judgment-based evaluation

The ratified quality principle is that CodexWriter should distinguish mechanically verified findings from judgment-based assessments rather than presenting the latter as mechanically proven.

Examples that may be deterministic when backed by schemas or scripts:

- file/schema validity
- reference integrity
- timeline ordering
- known character/object state
- promise/setup/payoff ordering
- measurable counts

Examples that remain model/human judgment:

- character motivation quality
- scene effectiveness
- pacing quality
- prose/style quality
- emotional payoff
- voice fidelity

Portability evidence also splits this way: deterministic invariants must match across hosts; judgment-based outputs must comply with the same scope and output contracts but need not match in wording, emphasis, or conclusions.

## 17. Workflow / branch strategy

- `main` — stable, reviewed releases
- `development` — ongoing integration branch
- Feature branches — bounded architecture, research, or skill work created from `development`

The ratification addendum lives on `architecture/seven-source-synthesis`. The ratification baseline is commit `70861e660d7d7e5261482834397f5f6a97aa43d3`. Documentation alignment now proceeds on the isolated branch `architecture/ratified-alignment`, created from that baseline. That branch is not merged until reviewed and approved.

## 18. Next steps

Documentation alignment is complete on the isolated branch `architecture/ratified-alignment` and pending review. The file-by-file schema and skill impact plan is the next **prospective** deliverable, subject to explicit authorization after that review. It is not presently authorized.

This document will be updated as evidence-based design decisions are made and as deferred design detail is specified.

---

*This document distinguishes ratified architecture from the existing provisional prototype, from capabilities that are not yet implemented, and from design detail that remains deferred.*
