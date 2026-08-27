# CodexWriter — Ratification Addendum

**Date:** August 27, 2026
**Branch:** `architecture/seven-source-synthesis`
**Supplementary to:** `docs/architecture/seven-source-synthesis-2026-08-27.md`
**Status:** Awaiting ratification — no implementation file or merge affected

This addendum consolidates the twelve open decisions (D1–D12) into three ratification-ready decision blocks and one proposed vertical slice. It does not modify schemas, skills, templates, `ARCHITECTURE.md`, the crosswalk, or any implementation file. It does not merge the branch or begin infrastructure work.

---

## Block A — Authority and Durable State (covers D1–D3, D9–D10)

### Recommended default: the layered hybrid model

- **Markdown is the authoritative expression for exact narrative wording.** No structured state field may silently rewrite a paragraph the author wrote.
- **Schema-validated structured state is authoritative for explicitly designated, approved machine-checkable facts and workflow fields only.** These include state revisions, phase, phase_gate, character status, chapter sequence, scene outline/draft status, schema validity fields, TODO type enums, and IDs that the system uses to route and cross-reference work.
- **A fact that first appears in prose is proposed structured state, not canon.** It must pass the same gate as any other promotion candidate.
- **Promotion into canon requires author approval for narrative content, plus transaction validation for structured fields.** A structured update that is syntactically valid but semantically wrong must still be resolved before it is written.
- **When Markdown and structured state disagree, the disagreement blocks publication or state promotion until an explicit reconciliation is recorded.** The reconciliation must say which artifact wins and why; the loser's subsequent reads must report the same ruling.
- **No layer may silently overwrite another.** The only exceptions are deterministic derived artifacts that are explicitly documented as rebuildable views and zero unique facts.
- **Stale revisions, concurrent changes, rollback, and audit history follow the layered transactional model:** a structured write wraps the old authority, the new authority, a human-readable summary, and runnable check information into one observed transaction; the canonical authority advances only via that transaction; an expected-revision guard rejects stale sequential writes; audit records identify who submitted what, what was applied, and what the check marked.

### Authority matrix

| Information category | Canonical source | Permitted writer | Promotion path | Conflict behavior | Derived consumers |
|---|---|---|---|---|---|
| Narrative prose (paragraphs, scenes, chapters) | Markdown files the author writes or approves | Author; authoring skill as draft until approval | Draft → author approval → canon | Canon wins; draft is discarded or revised | Reader, prose editor, reader-sim (when in overlay) |
| Editorial state (changes approved by author) | Markdown + recorded author decision | Prose editor proposes; author approves per change | Diagnose → batch of exact changes → author accept/reject/modify individually → apply only approved changes | Approved final wording wins over drafting draft | Continuity, reader-sim, export |
| Approved canon story facts (what happened, order, relationships, world rules) | Structured state (or an explicit Markdown canonical with provenance), after promotion | Author approves promotion; structured transaction applies validated state | Prose/proposed fact → author approval + transaction validation → canon state field | Conflict blocks promotion until reconciliation recorded | Continuity, reader-sim, scene-planner, architect |
| Workflow status (phase, phase_gate, outline/draft status, revisions, TODO type) | Structured state via schema-validated transaction | Orchestrator or authorized skill via atomic write | Business rule passes schema and coherence check → transaction applied | Structured state wins for status; any prose that contradicts blocked workflow is flagged | Orchestrator, continuity, export gating |
| Author memory and preferences (style, voice, habits) | Separate author-profile store, not story canon | Author or profile builder | Author sets or updates; profile is read by relevant skills | Author preference never overrides story canon; does not enter story truth | Relevant skills, context assembly |
| Non-canonical working material (brainstorms, drafts, rejected takes) | Sandbox/workspace, outside canon | Author or assistant inside sandbox | Only concrete, approved material may be promoted | Stays non-canon until explicitly promoted | None, until promoted |
| Indexes, registries, check reports, derived summaries | Rebuildable derived views produced from canonical project files | Automation | Rebuild on change or explicit rebuild command | Can be discarded or regenerated with no loss of unique facts | Review, continuity, context assembly |

### Tested rules against concrete examples

- **A manuscript says Avram is afraid of the divine encounter; the JSON character state currently records him as confident about it.** Conflict. Not silent overwrite. Block until the author resolves: either prose is wrong, state is wrong, or the state is stale and needs correction through the same promotion path. After resolution, the resolved side wins and the other side is flagged or revised.
- **Orchestrator increments `state_revision` and sets `phase_gate = approved`, but no author approval record exists.** Transaction validation fails. The status change is not applied. The author must approve or record the approval before the workflow field becomes canon.
- **A reader-sim prompt loads a derived summary of character knowledge from a persistently rebuilt index rather than requiring the author to paste the prose.** Permitted, because the summary has no unique facts. If the summary conflicts with the actual prose, the prose wins; the summary is rebuilt or corrected before next use.
- **Brainstorm commentary and a rejected alternate take live in a workspace.** Non-canon. They must not be promoted by accident. A promotion operation starts a gate for the specific material.
- **An earlier chapter is revised; later continuity facts depend on it.** Earlier-chapter revision triggers a recalculation of affected state; the affected facts do not silently persist. The updated transaction includes the recalculated current values; downstream checks see the current state, not the outdated inference.

---

## Block B — Context, Views, and Portability (covers D4, D11, D12)

### Ratification posture

Ratify now at a **minimum-responsibility** level, but defer the detailed LOD schedules until after the first vertical slice. The minimum layer is useful before implementation; the exact sharding thresholds and projection sizes are not yet worth freezing.

### Minimum responsibility of a context-assembly layer

1. Identify the task and pull the smallest set of inputs that could plausibly change the output if omitted.
2. Separate what must be current prose from what can be structured or summarized.
3. Keep derived overlays explicitly labeled so they never masquerade as primary content.
4. Preserve a compact, reviewable provenance note for what was assembled, from which revisions, and what was excluded.
5. Honor the conflict rule from Block A: if a loaded summary conflicts with the primary artifact, the primary artifact wins and the summary is corrected or excluded.

### What it may include, exclude, summarize, or shard

- It may load full prose when language, voice, dialogue rhythm, ambiguity, or exact wording is the point.
- It may load structured state, registries, indexes, and summaries for far-field information.
- It may shard by book/scene/character/state domain and assemble only the shards relevant to the task.
- It may exclude material that is cold, irrelevant, or lower-authority for the task.
- It must not exclude information whose omission could make the task wrong.

### How context packages identify their source revisions

- Every package records the project/book identifiers, the scope, a compact source map (which files, which state fields, which derived overlays), and the revision markers for the loaded items (file revisions or state revisions where available).
- The package does not assert authority beyond what the source map shows.

### Which derived views serve which consumers

- Authors: readable drafts, story bible, dossiers, outline, chapter prose.
- Writers: tight scene-oriented context with current character/state and relevant world facts.
- Continuity/editors: structured state plus the relevant prose windows and the relevant registry/current-state entries.
- Readers via reader simulation: manuscript-only view for the baseline pass; a separate labeled overlay only for the optional second pass.

### What “schema-aware portability” means operationally

A host is schema-aware if it can:
- validate Markdown against the project templates/templates and JSON against the schemas;
- respect the authority and conflict rules from Block A;
- route by structure and IDs, not only by free text;
- run or reject operations whose required state is missing or invalid;
- regenerate derived views from canonical files.

### What must remain host-neutral vs. what may require a host adapter

Host-neutral: Markdown/JSON inputs/outputs, schema validation, authority rules, conflict rules, derived-view regeneration, transaction record shape.

Host adapter: prompt delivery, tool invocation, file access conventions, agent subprocess management, runtime logging, interaction surfaces, and any capability that a particular runtime surfaces better than another.

### Evidence that demonstrates portability

Portability is demonstrated when:
- the same generic project and same task produce comparable results on two hosts;
- the differences are documented and explainable as host-adaptation gaps, not as different canon;
- the authority/conflict rules produce the same resolution decisions on both hosts;
- a derived view rebuild yields the same content from the same canonical files on both hosts.

### Decision on D4, D11, D12

- **D4 (context assembly and LOD):** Ratify the minimum responsibility now; defer thresholds until after the vertical slice.
- **D11 (derived views):** Ratify that derived views are rebuildable and non-authoritative; defer exact projection schemas until implementation.
- **D12 (portability):** Ratify the host-neutral vs. host-adapter boundary and the two-host evidence requirement; defer the exact porting checklist until after the vertical slice.

---

## Block C — Editorial and HITL Behavior (covers D5–D8)

### Reconciliation with accepted decisions

The settlement from yesterday’s decision record is kept: reader simulation can begin with a context-blind manuscript-only pass, editorial diagnosis and repair stay separate, passes have distinct scopes and stopping rules, and framework approvals stay separate from Dust & Ash story gates. This addendum does not reopen those decisions; it operationalizes them.

### Reader simulation

1. First pass is context-blind: manuscript only, no Story Bible, no outline, no dossier, no continuity report, no narrative architecture.
2. The blind pass delivers a reader’s experiential report in its own words: what it understood, what it missed, where it lost interest, where it felt engaged, where it was confused, and where the ending landed.
3. An optional second pass may load selected author context and add diagnostic interpretation, but the first pass stands alone and can be read without author privilege.

### Editorial passes

- Each pass has a declared scope: chapter, scene, continuity domain, prose domain, or specific review type.
- Each pass has a declared stopping rule: it stops when its review objective is met and it has produced the findings or proposed changes for that scope; it does not expand freely into unrelated concerns.
- Diagnosis and repair are separate: one pass produces findings; another pathway applies approved changes.

### Framework approvals vs. story gates

Framework approvals (state model, schema set, skill contracts, release decisions) belong to the framework track. Dust & Ash story phase gates belong to the Dust & Ash project track. They use different decision subjects and different approval records.

### Substantive prose editing: batch-approval model

- **Diagnose** the scene/chapter for the declared editorial scope.
- **Present one coherent batch of exact proposed changes**, each change localized enough to accept or reject individually.
- **Author accepts, rejects, or modifies individual changes.**
- **Apply only the approved changes.**
- Approval of a general editing goal is not permission for unrestricted rewriting. Each change still needs its own disposition unless the author explicitly authorizes a broader move with a clear boundary.

### Two HITL modes: objective selection criteria

#### Interactive approval required when

- the operation can change canon narrative content;
- the operation can change workflow status that gates other work;
- the operation can promote content into canon;
- the operation deletes or overwrites approved author material;
- the operation is the first promotion of a brainstorm/draft into canon;
- the operation is an earlier-chapter revision that may affect later state;
- the operation is a new project initialization that creates durable state;
- the author has not previously authorized an equivalent envelope for this kind of change.

#### PR-boundary review sufficient when

- the change is within already-approved story scope;
- the change is localized and reviewable as a bounded diff;
- the change does not cross a canon-promotion or canon-deletion boundary;
- the author has a usable review surface for the specific artifact;
- the change does not touch workflow gates, initialization, or canon promotion.

#### Operations that can never be deferred to the PR boundary

- creating or initializing a project’s durable state;
- promoting non-canon material into canon;
- deleting approved canon;
- overwriting an approved state field with an unapproved value;
- changing workflow status used for gating without an approval record;
- earlier-chapter canon revisions that require downstream recalculation;
- any operation where the author has asked for interactive approval for this specific decision.

#### How the selected mode is declared and recorded

Before the operation, the system states:
- the operation type;
- the scope;
- the proposed HITL mode, with the criterion that makes that mode appropriate;
- what will not be done without further approval.

After the operation, the record shows:
- the approval mode used;
- what was approved, rejected, or modified;
- the resulting state or artifact change;
- the audit entry identifying submission, disposition, and check output where applicable.

#### Why the system may not switch modes silently during a workflow

Silent mode switching would let a bounded assumption become a broad one without the author knowing. If new information during a workflow changes the appropriate mode, the system stops and asks for a fresh decision on the new scope before continuing.

---

## Decision quality requirements (applied to each block)

For each block, the packet contains:

- **Exact proposed rule** — stated above for each block.
- **Evidence-based rationale** — drawn from the seven sources' observed behavior rather than from one descriptive pass. The strongest direct signals are: JeroTan's exact-editor gate, escalation-to-author, exact-text-match retry, and project-root binding; Rhavekost's blind-reader isolation, diagnose/stop/author-disposition/repair pattern, and shared finding format with `confidence`; Zenstory's bounded state authority, derived views, expected-revision stale rejection, atomic write ordering with state-last and replay/recovery tests, and separate author memory; wgwtest's author overrides, prose-over-summary rule, and targeted full-text expansion; Dewhurst's outline approval, audit vs. edit intent separation, and warnings that should be surfaced rather than silently rewritten; Haowjy's author-as-final-judge framing and reader/critic/editor separation. These are synthesized, not copied.
- **Strongest alternative** — a simpler single-authority model, a more document-only model, a fully interactive per-sentence edit model, or a fully delegated PR-only model. Each is weaker: a single authority collapses the canon/experience distinction; a document-only model abandons machine-checkable operations; a fully interactive model is impractical for real drafting; a fully delegated model loses the gates that prevent accidental canon mutation.
- **Tradeoff or downside** — more ceremony at promotion and evaluation boundaries; authors and reviewers must understand the authority distinction; the two-pass reader model adds a deliverable; the batch model requires localized changes and explicit per-item disposition; the HITL criteria are more rules to maintain and to document per host.
- **Files and schemas affected if ratified** — schemas must distinguish canon fields from editorial fields; the continuity finding format should adopt a shared envelope with confidence/determinism classification; derived-view specs must record rebuildability; project initialization, state-update, and editorial skills must reflect promotion and approval paths; README/status/docs must not claim any layer as canon that is not ratified.
- **Migration impact on the existing prototype** — the prototype is provisional, so migration is mostly clarification and enforcement, not wholesale rewrite; a small number of existing fields can be reclassified under the authority matrix; derived views must be marked rebuildable or removed; continuity and editorial skills must be re-described to match the separate-diagnose/repair model rather than being claimed as already obeying it.
- **Acceptance test that would prove the rule works** — a generic test fixture exercises initialization, one editorial batch, and one canonical promotion; the system must refuse the unapproved promotion and the stale-revision transaction; the derived view rebuild must reproduce the same content from the same canonical files; the blind reader pass must be reproducible from manuscript only; and the same expressions should be evaluable on a second host without the authority/conflict outcomes changing.

---

## Decision dependency map

Genuinely independent decisions:

- The authority model (Block A).
- The minimum context-assembly responsibility and the host-neutral/host-adapter boundary (Block B).
- The reader-first blind pass (Block C).
- The batch-approval editorial model (Block C).
- The framework-vs-story gate separation (already accepted; this addendum preserves it rather than reopening it).

Decisions that follow from others:

- Derived view rebuildability and the exact LOD thresholds depend on the authority model.
- Which HITL mode applies to a given operation depends on the authority model and the canon-promotion/deletion rules.
- The exact schemas affected depend on which fields are canon versus editorial versus derived.
- The vertical slice scope depends on the ratified minimum responsibilities above; it does not require every detailed rule to be frozen first.

Decisions that are not yet equal standalone choices:

- D4 in full form depends on the authority model and the minimum context layer.
- D11 in full form depends on authority and derived-view ratification.
- D12 in full form depends on the host-neutral boundary.
- D5–D8 gain their stopping rules and batch model from the same editorial/HITL settlement; they are not twelve unrelated opinions.

---

## Proposed generic vertical slice (not yet implemented)

### Purpose

Exercise the layered hybrid model with one small generic project before Dust & Ash-specific work resumes.

### Scope

1. **Project initialization** — create a minimal book, project_id, book_id, title, initial phase, initial state_revision, and a declared empty state appropriate to the start.
2. **Markdown creative content** — author drafts a very short scene in prose using the story-bible and scene outline templates.
3. **Promotion of one approved fact into structured state** — take one concrete fact from prose/approval and promote it into the appropriate state field through a transaction.
4. **A valid transaction** — apply a structured state update that passes schema and coherence checks and records the audit entry.
5. **A rejected stale-revision transaction** — submit a stale write against the wrong expected revision and demonstrate that it is rejected.
6. **Registry rebuilding** — derive at least one registry/summary from the canonical files and confirm it is reproducible.
7. **Context assembly** — assemble a minimal context package for the scene, including what is prose, what is state, and what is derived.
8. **Context-blind reader simulation** — run one blind pass on the scene manuscript only and produce a reader report.
9. **Batch-approved editorial repair** — diagnose a small set of issues, present exact proposed changes, have the author accept/reject/modify one or more, and apply only the approved ones.
10. **Schema and continuity validation** — validate the state and the scene against their schemas and record a continuity/state coherence result.
11. **Execution on at least two supported hosts** — run the slice on two AI hosts and document differences and fallbacks.

### Acceptance criteria

- The initialized project is valid and clearly scoped.
- The prose scene is created and reviewable.
- The promoted fact is in the state and is traceable to the approval.
- The valid transaction is applied and auditable.
- The stale transaction is rejected and the rejection reason is recorded.
- The derived registry/summary is regenerated without loss of unique facts.
- The context package is locally correct and provenance-labeled.
- The blind reader report is reproducible from manuscript only.
- Editorial changes are applied only after explicit per-change disposition.
- Validation passes for the intended state and fails appropriately for a deliberately broken input.
- Two-host results are comparable and differences are documented.

### Fixtures

- A minimal project scaffold: one story bible, one scene draft, one approved fact, one state file, one derived view, one reader report, one editorial batch, one stale transaction attempt.
- A deliberately broken state instance for the validation-negatives test.
- A second host that can execute the same prompts against the same fixture files.

### Expected outputs

- An initialized and valid project directory.
- One approved Markdown scene.
- One promoted structured fact with promotion record.
- One successfully applied transaction and one rejected stale transaction.
- One rebuilt derived view whose content matches its canonical source.
- One assembled context package.
- One blind reader report.
- One batch of editorial changes with at least one accept and one reject/modify.
- Schema validation results for valid and broken inputs.
- Two-host comparison notes, including what the second host could or could not do and where a host adapter would help.

---

## Recommendation for ratification

If the layered hybrid model and the three blocks above are accepted, the first concrete next step is to update `ARCHITECTURE.md`, the crosswalk, the relevant schemas, and the affected skill contracts to reflect:

- the authority matrix and the no-silent-overwrite rule;
- the separate canon vs. editorial vs. derived categories;
- the minimum context-assembly responsibility;
- the host-neutral vs. host-adapter boundary and the two-host evidence requirement;
- the blind-reader first pass;
- the batch-approval editorial model;
- the HITL mode criteria and the prohibition on silent mode switching;
- the framework-vs-story gate separation as a standing rule.

No implementation file, schema instance, or merge is authorized by this addendum alone. Ratification unlocks maintenance updates and downstream schema/skill alignment; implementation begins only after that.

---

**Suggested approval statement if accepted:**

> I accept the layered hybrid model as the default authority model for CodexWriter and I accept this ratification addendum into Blocks A, B, and C as the basis for updating ARCHITECTURE.md, the crosswalk, the schemas, and the affected skill contracts. I am not yet authorizing implementation, merging the branch, or beginning the infrastructure workstream. The next authorized step is to make the maintenance and alignment updates that the ratified rules require; implementation begins only after those updates are reviewed.
