# Source Analysis: danjdewhurst/story-skills

**Status:** Draft ready for review  
**Source analyzed:** [`danjdewhurst/story-skills`](https://github.com/danjdewhurst/story-skills)  
**Analysis date:** 2026-08-25  

## Evidence Labels

This document deliberately separates source facts from interpretation.

- **Observed** — directly established by a repository file, script, test, workflow, manifest, or GitHub metadata.
- **Inference** — an analytical interpretation supported by multiple observations but not explicitly stated by the source.
- **Uncertainty** — not established by the inspected files, or a source behavior whose precedence/semantics are not fully specified.

CodexWriter dispositions in this document are **Phase 1 candidates**, not final architecture decisions.

---

## 1. Repository Snapshot

### Observed

- **Repository:** [`danjdewhurst/story-skills`](https://github.com/danjdewhurst/story-skills)
- **Visibility:** Public.
- **Created:** 2026-02-12.
- **Repository metadata updated:** 2026-08-25 at analysis time.
- **Last source push shown by GitHub metadata:** 2026-06-11.
- **Default branch:** `main`.
- **Primary repository language:** JavaScript.
- **Stars at analysis time:** 188.
- **Forks at analysis time:** 24.
- **Open issues at analysis time:** 1.
- **Package/plugin version:** `0.3.1` in `package.json` and `.codex-plugin/plugin.json`.
- **Core skill count:** **7**:
  1. `story-init`
  2. `character-management`
  3. `worldbuilding`
  4. `plot-structure`
  5. `chapter-writing`
  6. `revision-continuity`
  7. `story-maintenance`
- **Companion implementation:** a JavaScript/Node/Bun `story` CLI for deterministic project maintenance.
- **Runtime support documented in README:** Codex, Claude Code, GitHub Copilot, Cursor, Windsurf, Gemini CLI, OpenCode, Agent Skills CLI, and manual/project-knowledge use.
- **Codex plugin packaging:** `.codex-plugin/plugin.json` points to `./skills/` and describes the bundle as end-to-end fiction writing with markdown registries, YAML frontmatter, revision/continuity, and deterministic maintenance.
- **Repository CI:** `.github/workflows/ci.yml` runs metadata checks, tests, coverage/fallback checks, example validation, and a Node fallback-CLI smoke check.

### Inference

Compared with Lensetek, Dewhurst is a **narrower but more implementation-focused system**. It has fewer creative specialist roles, but the shared project format, CLI, tests, schemas, examples, and CI make its continuity/state claims substantially more operationalized.

### Uncertainty

Repository metadata and implementation may change after this analysis. Re-check the source before any implementation-level borrowing or release decision.

---

## 2. Licensing and Provenance

### Observed

- Root [`LICENSE`](https://github.com/danjdewhurst/story-skills/blob/main/LICENSE) exists and contains the **MIT License**, copyright Daniel Dewhurst, 2026.
- GitHub repository metadata identifies the license as MIT.
- `package.json` declares `"license": "MIT"`.
- `.codex-plugin/plugin.json` declares `"license": "MIT"`.
- Root [`NOTICE`](https://github.com/danjdewhurst/story-skills/blob/main/NOTICE) was **not found** during this analysis.
- Root [`ATTRIBUTION.md`](https://github.com/danjdewhurst/story-skills/blob/main/ATTRIBUTION.md) was **not found** during this analysis.
- The repository is not marked as a GitHub fork.
- The README recommends the separate [`forjd/better-writing`](https://github.com/forjd/better-writing) skill for stronger prose, but that companion is referenced rather than presented as part of the seven Story Skills modules inspected here.

### CodexWriter implication

- MIT permits implementation-level reuse subject to preservation of the copyright and license notice in copies or substantial portions.
- If CodexWriter copies or substantially adapts Dewhurst implementation text/code rather than independently reimplementing the concept, record the specific source file and preserve required MIT attribution.
- The separately recommended `forjd/better-writing` project should be treated as its own provenance/licensing source if CodexWriter later decides to inspect or borrow from it.

This is a project-risk note, not legal advice.

---

## 3. Architectural Thesis

### Observed

The README describes Story Skills as a shared **markdown fiction project format** plus Agent Skills plus a deterministic maintenance CLI.

The project format treats the following as durable, cross-referenced story artifacts:

- story bible,
- characters,
- worldbuilding locations/systems/factions/artifacts,
- plot arcs,
- timeline,
- chapter drafts,
- scene records,
- current continuity state,
- open questions,
- promises/payoffs,
- glossary terms.

[`docs/schema-v2.md`](https://github.com/danjdewhurst/story-skills/blob/main/docs/schema-v2.md) states that Schema v2 preserves a **markdown-first model** while adding durable state for longer works. Every project artifact remains Markdown with YAML frontmatter; the CLI validates the mechanical contract while agents retain creative judgment.

The system therefore establishes a deliberate boundary:

- **Agent Skills / human author:** creative decisions, planning, prose, interpretation.
- **Story CLI:** deterministic validation, indexing, cross-reference checks, state-contract checks, migration, import/export, reporting, and build operations.

### Inference

Dewhurst's primary organizing principle is not specialist-role breadth. It is **a shared story data contract that creative workflows must maintain**.

That makes it especially relevant to CodexWriter's unresolved state question because Dewhurst demonstrates a distributed, Markdown/YAML state architecture rather than a single canonical JSON store.

---

## 4. Workflow and Orchestration

### Observed: no single creative orchestrator skill

Unlike Lensetek, Story Skills does not include a dedicated `fiction-orchestrator` module. Routing occurs through skill descriptions, project state, and CLI actions such as `story next`.

The practical workflow is:

1. **Initialize** — `story-init`
2. **Develop story domains** — `character-management`, `worldbuilding`, `plot-structure`
3. **Draft** — `chapter-writing`
4. **Revise/audit** — `revision-continuity`
5. **Maintain/check** — `story-maintenance` / `story` CLI throughout

### Observed: initialization creates the shared contract

`story-init` creates:

```text
story.md
characters/_index.md
worldbuilding/_index.md
worldbuilding/{locations,systems,factions,artifacts}/
plot/_index.md
plot/arcs/
plot/timeline.md
scenes/_index.md
continuity/state.md
continuity/questions/_index.md
continuity/promises/_index.md
glossary/_index.md
chapters/_index.md
```

It also defines project-wide conventions such as kebab-case identifiers, YAML frontmatter, bidirectional links, death tracking, `characters` vs `mentions`, scene identifiers, and Markdown-first artifacts.

### Observed: chapter drafting is outline-first

[`chapter-writing/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/chapter-writing/SKILL.md) uses this sequence:

1. Gather story and continuity context.
2. Determine chapter scope/POV/location.
3. Build a beat-by-beat outline.
4. **Present the outline to the user for approval.**
5. Write chapter prose.
6. Create/update machine-readable scene records.
7. Update registries, timeline, arcs, continuity state, questions/promises, and foreshadowing.
8. Run maintenance checks.

### Observed: revision has an explicit ownership boundary

`chapter-writing` owns new drafting. [`revision-continuity/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/revision-continuity/SKILL.md) owns targeted chapter edits, continuity audits, developmental revision, line edits, polish, and post-draft cleanup.

### Observed: maintenance is a distinct mechanical responsibility

[`story-maintenance/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/story-maintenance/SKILL.md) says creative skills own story decisions while maintenance handles mechanical consistency.

The CLI exposes operations including:

- `init`
- `add`
- `rename`
- `remove`
- `migrate`
- `validate`
- `reindex`
- `wordcount`
- `links`
- `continuity`
- `import`
- `report`
- `next`
- `doctor`
- `export`
- `build`

### Observed: two HITL operating modes

Interactive chapter-writing requires outline approval before prose.

The optional [`templates/github/draft-next-chapter.yml`](https://github.com/danjdewhurst/story-skills/blob/main/templates/github/draft-next-chapter.yml) demonstrates a different automated mode: a scheduled Claude Code action asks `story next` for the next deterministic action, outlines and drafts the chapter in the same run, updates state, runs maintenance, then opens a PR for human review.

### Inference

Story Skills therefore supports both:

- **interactive approval before drafting**, and
- **automated drafting with approval/review shifted to the pull request boundary**.

That is useful evidence for CodexWriter's HITL design: the same authoring framework may legitimately use different stopping points depending on execution mode, but those modes should be explicit.

---

## 5. State Storage Model

### Observed: distributed Markdown/YAML state

Dewhurst does **not** use a single canonical JSON story-state file.

Its state is distributed across plain Markdown files with structured YAML frontmatter.

### 5.1 Static / relatively durable story knowledge

- `story.md` — title, genre, themes, POV, tense, status, synopsis/style notes.
- `characters/*.md` — character profiles, status, relationships, locations, tags, death chapter.
- `worldbuilding/locations/*.md`
- `worldbuilding/systems/*.md`
- `worldbuilding/factions/*.md`
- `worldbuilding/artifacts/*.md`
- `plot/arcs/*.md`
- glossary term files.

`story-init` explicitly calls `story.md` the **top-level bible read by all skills for context**.

### 5.2 Dynamic / current continuity state

[`continuity/state.md`](https://github.com/danjdewhurst/story-skills/blob/main/examples/harbor-of-second-light/continuity/state.md) stores YAML fields:

- `current-chapter`
- `character-state`
- `object-state`
- `knowledge-state`

The example state records current character location/physical/emotional state, artifact ownership/location/status, and character knowledge plus the chapter in which it was learned.

The same file may also contain human-readable Markdown tables and prose summaries beneath the frontmatter.

### 5.3 Scene-level state changes

[`scene-template.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/chapter-writing/references/scene-template.md) gives each scene a structured `state-changes` list and continuity notes.

Scene frontmatter may include:

- POV,
- location,
- characters,
- arcs advanced,
- status,
- state changes.

This creates a structured record of what changed in a scene, while `continuity/state.md` represents current durable state.

### 5.4 Questions / mysteries

Each durable open question can be its own Markdown file under `continuity/questions/`.

The example [`what-happened-on-blackout-night.md`](https://github.com/danjdewhurst/story-skills/blob/main/examples/harbor-of-second-light/continuity/questions/what-happened-on-blackout-night.md) records:

- title,
- status,
- introduced chapter,
- resolved chapter,
- associated characters,
- evidence,
- resolution plan.

### 5.5 Promises / setup-payoff contracts

Each promise can be its own file under `continuity/promises/`.

The example [`the-bell-failsafe.md`](https://github.com/danjdewhurst/story-skills/blob/main/examples/harbor-of-second-light/continuity/promises/the-bell-failsafe.md) records:

- title,
- status,
- planted chapter,
- payoff chapter,
- arcs,
- characters,
- setup/payoff notes.

### 5.6 Timeline and history

`plot/timeline.md` is a chronological master list of story events.

Chapter files and scene files preserve written/scene history. Promises/questions preserve their own lifecycle fields.

The inspected source does **not** implement a general transaction log or immutable per-chapter state-delta history equivalent to Zenstory's transactional state protocol.

### 5.7 Authority and conflict behavior

#### Observed

`story-init` says domain `_index.md` files are **authoritative registries**.

The README and maintenance skill also say `story reindex` **rebuilds registry tables from current Markdown files**.

The CLI can report cross-artifact conflict rather than silently resolving it. For example, `src/continuity.js` warns when an `object-state` status conflicts with the corresponding artifact file status.

#### Uncertainty

The inspected documentation does not define one universal precedence rule for every kind of conflict among:

- prose,
- entity files,
- registries,
- `continuity/state.md`,
- timeline,
- scene records.

Calling `_index.md` files authoritative while also rebuilding them from entity files creates an **authority nuance** that should be examined before adopting the pattern literally.

### 5.8 Post-draft updates

`chapter-writing` explicitly requires updating after a chapter:

- chapter registry / word count,
- timeline,
- active arcs,
- scene records,
- current continuity state,
- questions,
- promises/payoffs,
- foreshadowing,
- character changes where relevant.

### 5.9 Revision propagation

`revision-continuity` explicitly instructs the agent to update affected metadata when revising a chapter, including timeline, scenes, continuity state, questions/promises, arcs/foreshadowing, character/location files, then run deterministic maintenance.

### Observed limitation

This propagation is **workflow-driven rather than transactionally derived**. The source does not show a mechanism that automatically replays later chapters to recompute all current state after an old chapter changes.

### 5.10 Stale/conflicting updates

No state-revision counter, optimistic-lock field, stale transaction rejection, or concurrency-lock protocol was found in the inspected story format.

The CLI catches structural and semantic-contract inconsistencies after files are written, but it does not establish Zenstory-style stale-write prevention.

### 5.11 Author preference memory

No separate persistent author-preference memory system was found in the seven core skills or Schema v2 project format.

Story voice/tone can live in `story.md` and character files. Stronger voice calibration is delegated/recommended through the optional external `better-writing` skill.

### 5.12 Non-canonical working material

No dedicated brainstorm/alternate-take sandbox or explicit canon-promotion mechanism was found in the standard Story Skills project layout.

### Phase 1 implication

Dewhurst is strong evidence that **persistent fiction state can remain Markdown-first and distributed while still supporting deterministic validation**.

It should therefore be treated as a serious alternative to the Zenstory single-authoritative-state hypothesis rather than merely as a continuity checker to add on top of another state model.

---

## 6. Context Management

### Observed: explicit chapter pre-write context contract

Before drafting, `chapter-writing` requires reading:

- `story.md`,
- `chapters/_index.md`,
- `plot/_index.md`,
- `plot/timeline.md`,
- `scenes/_index.md`,
- `continuity/state.md`,
- open questions,
- promises/payoffs.

For later chapters it also requires:

- previous chapter,
- active arc files.

Then it loads the POV character file for voice and relevant location files for setting details.

### Observed: revision context is targeted

`revision-continuity` reads:

- target chapter(s),
- previous and next chapters when present,
- relevant character/location/system/arc files referenced by frontmatter,
- matching scene records,
- current continuity state,
- questions/promises,
- timeline and active arcs when continuity-sensitive.

### Inference

Dewhurst has a stronger context contract than Lensetek because it specifies **what to reload and when**, and it uses structured frontmatter to narrow some downstream lookups.

### Not observed

No explicit:

- context-token budget,
- sharding threshold,
- near-field/far-field LOD hierarchy,
- summary compression protocol,
- cold-context exclusion tier,
- rule for resolving prose vs summary conflicts.

### Candidate scaling concern

The chapter pre-write list is manageable for modest projects, but several registry/state files could grow substantially in long novels or series. CodexWriter should not assume Dewhurst's full-file reload pattern scales indefinitely without testing or additional context selection.

---

## 7. Creative-Craft Model

### Observed: concept/intake is lightweight

`story-init` gathers title, genre/subgenre, synopsis, setting era, themes, POV, and tense. It does not provide a dedicated high-concept/premise specialist comparable to Lensetek's `story-concept-intake`.

### Observed: character model

`character-management` covers:

- appearance,
- personality,
- backstory,
- external wants vs internal needs,
- voice/speech patterns,
- character arc,
- life events,
- bidirectional relationships,
- family trees,
- cross-links to locations/factions/artifacts/arcs.

### Observed: world model

`worldbuilding` treats these as distinct entity types:

- locations,
- systems,
- factions,
- artifacts.

It includes current state, rules/constraints, resources, membership, ownership, and cross-links.

### Observed: plot model

`plot-structure` supports multiple familiar structures and separately models:

- arcs,
- plot points,
- timeline,
- foreshadowing,
- durable promises,
- durable questions.

### Observed: scene/chapter model

`chapter-writing` combines chapter planning and prose drafting but creates separate scene records for continuity.

[`writing-guidelines.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/chapter-writing/references/writing-guidelines.md) covers:

- show-don't-tell,
- POV consistency,
- dialogue,
- pacing,
- scene goal/conflict/outcome,
- sensory grounding,
- chapter openings/endings,
- continuity checks before writing.

### Observed: prose specialization is intentionally limited

The README and chapter skill recommend `forjd/better-writing` for stronger voice calibration, anti-generic writing checks, and final prose-quality passes.

### Inference

Dewhurst's strongest creative contribution is **workflow grounding and state-aware drafting**, not deep stylistic instruction. It is more valuable to CodexWriter as a project/state/continuity architecture than as the final prose-craft model.

---

## 8. Evaluation and Continuity

## 8.1 Deterministic continuity engine

### Observed implementation

[`src/continuity.js`](https://github.com/danjdewhurst/story-skills/blob/main/src/continuity.js) performs executable checks including:

- character `died-in` references,
- deceased characters appearing later in chapter/scene casts,
- POV characters missing from casts,
- scene cast vs chapter cast/mentions mismatches,
- scene location vs chapter location mismatch warnings,
- chapter numbering gaps,
- promise payoff before planting,
- invalid promise status/chapter combinations,
- long-planted promises without payoff warnings,
- question resolution before introduction,
- invalid question status/chapter combinations,
- story marked complete while promises/questions remain unresolved,
- continuity-state chapter ahead/behind written chapters,
- missing character/location/artifact/owner/chapter references in current state,
- artifact status conflict between current state and artifact file.

### Observed: tests substantiate the checks

[`test/continuity.test.js`](https://github.com/danjdewhurst/story-skills/blob/main/test/continuity.test.js) constructs broken temporary projects and asserts exact continuity errors/warnings for deaths, promise/question ordering, stale state, missing references, object status conflicts, cast mismatches, and chapter gaps.

The tests also distinguish:

- schema/validation errors,
- link errors,
- continuity errors.

### Observed: CI exercises the implementation

[`.github/workflows/ci.yml`](https://github.com/danjdewhurst/story-skills/blob/main/.github/workflows/ci.yml) runs tests, coverage/fallback checks, and example validation on pull requests and pushes to `main`.

### Observed: story-project CI template

[`templates/github/story-checks.yml`](https://github.com/danjdewhurst/story-skills/blob/main/templates/github/story-checks.yml) is intended for repositories containing actual fiction projects. It runs:

1. `story validate`
2. `story links`
3. `story continuity`
4. actionable project report

on push/PR.

### Inference

This is a substantially stronger implementation of **deterministic continuity** than Lensetek's `check_timeline_continuity.py`, because the rules operate over structured story contracts and are backed by tests.

## 8.2 Boundary of deterministic checking

`revision-continuity` explicitly says to run `story continuity` first and then check what the CLI cannot judge, including:

- whether a character acts on unknown information,
- nuanced injury/emotional/alliance continuity,
- travel time and cause/effect,
- whether plot arcs meaningfully advance,
- semantic foreshadowing correctness,
- world-rule consistency with prose.

### Inference

Dewhurst demonstrates a useful boundary for CodexWriter:

**deterministic checks validate structured facts/contracts; model/human review evaluates semantic narrative truth and quality.**

## 8.3 Audit vs repair

### Observed

When asked for an audit, `revision-continuity` returns findings by severity with file references and fixes.

When asked for revision, it directly edits the requested files and then reports changed continuity facts and maintenance results.

`story-maintenance` explicitly says not to overwrite creative prose merely to satisfy a mechanical check; intentional warnings should be reported rather than silently changed.

### Inference

Audit/repair separation is stronger here than in Lensetek, although there is no universal requirement for a second author approval after every proposed repair when the user initially requested revision.

## 8.4 Reader simulation

No dedicated beta-reader or context-blind reader-simulation skill exists in the seven-skill architecture.

This remains a Lensetek/Haowjy/Rhavekost contribution area rather than a Dewhurst strength.

---

## 9. Human-in-the-Loop Model

### Observed: interactive drafting gate

The chapter-writing workflow requires the beat-by-beat outline to be presented for user approval before full prose is written.

### Observed: revision behavior follows user intent

- If the user asks for an **audit**, return findings.
- If the user asks for **revision**, make targeted edits and report them.

### Observed: intentional mechanical exceptions are surfaced

`story-maintenance` instructs the agent to report validation warnings that reflect intentional user data rather than silently rewriting the story.

### Observed: PR review can act as the human gate in automation mode

The scheduled `draft-next-chapter.yml` workflow drafts autonomously, runs maintenance, and opens a PR. Its comments explicitly state that the human reviews the chapter as a PR before merge.

### Not observed

- formal canon-promotion gates for brainstorms/alternatives,
- separate approval for every state mutation,
- explicit rollback/transaction semantics,
- a general rule preventing all scope transitions without confirmation.

### Inference

Dewhurst's HITL philosophy is **task-specific rather than phase-based**:

- approve outline before interactive prose,
- review PR after automated prose,
- respect audit-vs-edit intent,
- surface mechanical exceptions for human judgment.

This is a useful counterpoint to Lensetek's fixed five phase gates.

---

## 10. Runtime and Maintenance

### Observed: runtime portability

The README documents installation/use across Codex, Claude Code, GitHub Copilot, Cursor, Windsurf, Gemini CLI, OpenCode, and generic Agent Skills environments.

### Observed: layered CLI fallback

Skills prefer:

1. installed `story` command,
2. `bun run story --` in the source repository,
3. bundled Node fallback under `story-maintenance/scripts/story.js`,
4. manual maintenance where executable CLI access is unavailable.

### Observed: Node/Bun packaging

`package.json`:

- sets Node `>=18`,
- exposes `bin/story.js`,
- has no runtime dependencies listed,
- uses Bun for source-development tests/coverage,
- bundles a Node fallback into the maintenance skill.

### Observed: maintenance breadth

The CLI includes:

- scaffold/init,
- entity add/rename/remove,
- schema migration,
- validation,
- reindexing,
- word-count synchronization,
- backlink/reference validation,
- continuity validation,
- manuscript import,
- reports/next actions/doctor,
- manuscript export,
- EPUB/DOCX/Markdown builds.

### Observed: import

The README says `story import` can split an existing manuscript on chapter headings or chapter files, create the standard project shape, calculate word counts/registries, and report recurring proper-name candidates for later entity creation.

### Observed: migration

`docs/schema-v2.md` says migration creates v2 directories/registry files, upgrades `story.md` to schema version 2, and reindexes without inventing creative content.

### Observed: CI / automation

The repository has both:

- CI for Story Skills itself, and
- templates for CI/automated chapter PRs in downstream story repositories.

### Inference

Dewhurst treats maintenance and observability as first-class runtime concerns more convincingly than Lensetek. Its fallback model is also explicit: if the CLI is unavailable, skills specify manual behavior rather than assuming a nonexistent tool.

---

## 11. Strengths

### 11.1 Strong shared project contract

The Markdown/YAML format gives every creative skill a common vocabulary for identity, references, state, arcs, chapters, and continuity.

### 11.2 Deterministic checks are genuinely executable

The continuity claims are backed by source code, tests, examples, and CI rather than prompt wording alone.

### 11.3 Clear deterministic-vs-judgment boundary

The source explicitly separates what the CLI can prove from what an agent/editor must still evaluate semantically.

### 11.4 Current state is more explicit than Lensetek

Character/object/knowledge state has a dedicated structured artifact (`continuity/state.md`).

### 11.5 Promises and questions are first-class objects

Setup/payoff commitments and mysteries have independent lifecycle records and validation rules.

### 11.6 State-aware chapter workflow

Chapter writing loads current state before drafting and requires post-write updates to continuity artifacts.

### 11.7 Scene records preserve machine-readable continuity

Scene metadata records POV, location, cast, arcs advanced, and state changes separately from prose.

### 11.8 Maintenance is isolated from creative prose

The maintenance skill explicitly avoids changing creative text merely to appease a mechanical validator.

### 11.9 Tests and CI reduce architecture drift

The repository validates its own continuity engine, examples, fallback CLI, and metadata.

### 11.10 Portable implementation

Agent Skills plus Node/Bun fallback makes the design usable across multiple runtimes without requiring one proprietary host.

---

## 12. Weaknesses / Gaps

### 12.1 Creative specialist breadth is narrower than Lensetek

There are no dedicated modules for:

- market/trend research,
- concept/high-concept development beyond initialization,
- beta-reader simulation,
- comics/webtoon writing,
- children's fiction,
- accessibility,
- deep prose polishing as a core skill.

### 12.2 Prose craft is not the system's strongest layer

The built-in writing guidelines are useful but compact; the README recommends an external skill for stronger prose/voice work.

### 12.3 State authority is not universally explicit

The system calls `_index.md` files authoritative registries but also rebuilds them from entity files. Cross-file conflicts may be reported rather than resolved by a documented universal precedence rule.

### 12.4 Revision propagation is not transactional

Older-chapter edits require agents to update affected later/current metadata correctly. No replay/recompute engine for downstream state was found.

### 12.5 No stale-write / concurrency protection

No revision counter or stale transaction rejection was observed.

### 12.6 Context loading may become large

The chapter workflow specifies many full artifacts to load but does not define LOD, sharding, budget limits, or cold-context exclusion.

### 12.7 No separate author-preference memory

Story style lives in project documents, but user-level author preferences are not separated as a reusable memory layer.

### 12.8 No explicit non-canonical workspace

Brainstorms, rejected alternatives, and experiments do not have a standard sandbox/canon-promotion protocol.

### 12.9 Reader knowledge is only partially represented

Character knowledge is explicitly tracked; questions/promises represent reader-facing obligations, but the inspected architecture does not maintain a general structured `reader-knows` state distinct from objective author truth.

### 12.10 Interactive and autonomous HITL modes differ

Interactive chapter-writing pauses for outline approval; the automated PR workflow moves human review after drafting. This is defensible, but CodexWriter should make execution-mode-specific HITL policy explicit rather than accidental.

---

## 13. Relevance to CodexWriter

## 13.1 Observed reusable responsibilities

Dewhurst provides strong evidence for these responsibilities regardless of final implementation:

- project initialization and schema/version handling,
- story bible plus domain registries,
- structured character/world/plot cross-links,
- current character/object/knowledge state,
- scene-level continuity records,
- open questions as durable records,
- promises/payoffs as durable records,
- pre-write context reload,
- post-write state updates,
- deterministic validation,
- deterministic link checking,
- import/migration/reindex/report/doctor tooling,
- CI-able story checks.

## 13.2 Candidate architectural borrowings

These remain candidates, not decisions:

1. **Markdown/YAML story contract** as one state architecture option.
2. **Separate current continuity state** from static character/world profiles.
3. **First-class questions and promises/payoffs** rather than burying them only in outlines.
4. **Scene continuity records** separate from prose.
5. **Pre-write context contract** and explicit post-write maintenance checklist.
6. **Deterministic CLI boundary** for mechanically provable facts.
7. **Validation / links / continuity as different classes of checks.**
8. **CI integration** for continuity contracts.
9. **Maintenance skill/tooling separated from creative writing.**
10. **Execution-mode-specific HITL**: interactive pre-draft approval vs PR-based post-draft review.

## 13.3 Implementation-level borrowing requiring provenance handling

Potential implementation sources that would require MIT attribution if substantially copied/adapted include:

- `src/continuity.js`
- Schema v2 structures
- `story-maintenance` CLI behavior/code
- exact frontmatter schemas/templates
- CI workflow templates
- source skill workflow text

CodexWriter can instead independently implement similar concepts from the evidence without copying source expression.

## 13.4 Patterns to avoid adopting blindly

- Treating every `_index.md` as authoritative without a precise source-of-truth/derivation rule.
- Assuming full pre-write reloads will scale to very long series without LOD/context-budget design.
- Treating scene `state-changes` as sufficient unless current-state propagation is guaranteed.
- Assuming deterministic continuity can judge semantic knowledge, causality, pacing, or world-rule logic not encoded in structured fields.
- Coupling prose-quality architecture to an external dependency without deciding whether CodexWriter should own that responsibility itself.

---

## 14. Skill-by-Skill Responsibility Matrix

This matrix documents **Dewhurst's own implemented responsibilities**. It is not a replacement for `docs/crosswalk.md` and does not finalize CodexWriter architecture.

| Dewhurst Skill | Observed Responsibility | Primary Inputs | Primary Outputs / State Touched | Deterministic Tooling | Provisional CodexWriter Disposition |
|---|---|---|---|---|---|
| `story-init` | Scaffold the shared story project and conventions | User story metadata | `story.md`; registries; continuity directories/state; timeline; scene/glossary structure | `story init`, `validate` | **Adapt** — strong setup/state-contract evidence; not a replacement for concept development |
| `character-management` | Create/update characters, relationships, voice, arcs, cross-links | `story.md`; character registry; user input | character files; character registry; backlinks | `add`, `reindex`, `links`, `validate` | **Retain responsibility / Adapt** — useful structured identity/reference contract |
| `worldbuilding` | Create/manage locations, systems, factions, artifacts | `story.md`; world registry; user input | world entity files; registry; character/world backlinks | `add`, `reindex`, `links`, `validate` | **Retain responsibility / Adapt** — particularly useful artifact ownership/status modeling |
| `plot-structure` | Build structures/arcs/timeline/foreshadowing and durable questions/promises | story/themes; characters; plot registry | arc files; timeline; questions; promises; theme tracking | `reindex`, `links`, `validate`, later `continuity` | **Retain responsibility / Adapt** — promises/questions are high-value candidates |
| `chapter-writing` | Gather state, obtain outline approval, draft prose/scenes, update state | bible; registries; current state; questions/promises; previous chapter; active arcs; relevant entities | chapter; scene records; registry; timeline; arcs; continuity state; promise/question updates | wordcount/reindex/links/validate/next | **Adapt** — preserve CodexWriter's separate planning/writing skills while borrowing context/post-write contracts |
| `revision-continuity` | Audit or revise prose while preserving cross-file continuity | target/adjacent chapters; related entities; scenes; state; timeline; arcs | revised chapter(s); metadata/state updates; audit findings | `continuity`, `links`, `validate`, `doctor` | **Adapt** — strong evidence for current unified `continuity`; editing overlap remains for later comparison |
| `story-maintenance` | Deterministic project health, migration, import/export/build, repair support | full project structure/frontmatter | rebuilt registries, reports, validation findings, exports/builds | full `story` CLI | **Infrastructure candidate** — strong candidate for maintenance/tool layer, not creative core |

### Matrix observations

- Dewhurst **combines scene planning and chapter writing** inside `chapter-writing`; CodexWriter currently separates them. This analysis does **not** recommend merging them yet.
- Dewhurst **combines revision/editing and continuity** in `revision-continuity`; CodexWriter currently keeps `continuity` and `prose-editing` separate. This analysis does **not** recommend merging them yet.
- Dewhurst has no dedicated concept-development or reader-simulation skill, reinforcing why its seven skills should not become CodexWriter's full specialist taxonomy.

---

## 15. Lensetek → Dewhurst Comparative Baseline

This is the first direct source-to-source comparison in Phase 1.

| Dimension | Lensetek | Dewhurst | Phase 1 Observation |
|---|---|---|---|
| Specialist breadth | 16 roles across authoring/publishing/extensions | 7 core skills plus CLI | Lensetek is broader |
| Orchestration | Dedicated five-phase orchestrator | No central orchestrator; skill routing + project/CLI state | Different coordination models |
| HITL | Five phase gates/checklist | Outline approval; intent-based audit/edit; optional PR review mode | Dewhurst is more task/mode-specific |
| Canon/project format | Separate named Markdown artifacts | Standardized Markdown/YAML schema and registries | Dewhurst is more formally contracted |
| Dynamic current state | No dedicated current-state artifact identified | `continuity/state.md` for character/object/knowledge state | Dewhurst is materially deeper |
| Scene state | Scene breakdown for planning | Machine-readable scene files with state changes | Dewhurst preserves post-draft scene state |
| Promises/questions | Foreshadowing/Chekhov matrix | Independent durable promise/question records | Dewhurst is more addressable/checkable |
| Continuity tooling | Model audit + temporal-marker scanner | Structured executable checks with tests | Dewhurst is substantially more deterministic |
| Context contract | Mostly artifact-by-convention | Explicit pre-write/revision reload lists | Dewhurst is stronger |
| Long-context LOD | Not observed | Not observed | Gap remains in both |
| Revision propagation | Not specified | Explicit workflow updates but no transactional replay | Dewhurst improves process, not full derivation |
| Stale-write protection | Not observed | Not observed | Gap remains in both |
| Prose craft | Dedicated polisher plus drafting heuristics | Compact built-in guidelines; recommends external better-writing | Neither is sufficient alone for CodexWriter's final craft layer |
| Reader simulation | Dedicated beta-reader role | No dedicated reader-sim | Lensetek contributes this responsibility |
| Maintenance/runtime | Update manager + assorted helpers | Broad tested CLI, migration/import/doctor/CI | Dewhurst is stronger operationally |
| Publishing/extensions | Comics, children, Braille, layout, market research | Generic export/build; no equivalent creative extensions | Lensetek is broader |

### Phase 1 inference

The comparison supports the original synthesis direction:

- **Lensetek is a stronger responsibility taxonomy.**
- **Dewhurst is a stronger implementation reference for state-backed continuity and deterministic maintenance.**

It does **not** yet answer whether CodexWriter should use Dewhurst's distributed Markdown/YAML state, Zenstory's authoritative structured state, or another hybrid. That state decision remains deferred.

---

## 16. Detailed Evidence Index

### Repository / package

- [`README.md`](https://github.com/danjdewhurst/story-skills/blob/main/README.md)
- [`LICENSE`](https://github.com/danjdewhurst/story-skills/blob/main/LICENSE)
- [`package.json`](https://github.com/danjdewhurst/story-skills/blob/main/package.json)
- [`.codex-plugin/plugin.json`](https://github.com/danjdewhurst/story-skills/blob/main/.codex-plugin/plugin.json)
- [`AGENTS.md`](https://github.com/danjdewhurst/story-skills/blob/main/AGENTS.md)

### Project/state contract

- [`docs/schema-v2.md`](https://github.com/danjdewhurst/story-skills/blob/main/docs/schema-v2.md)
- [`schemas/story.schema.json`](https://github.com/danjdewhurst/story-skills/blob/main/schemas/story.schema.json)
- [`examples/harbor-of-second-light/continuity/state.md`](https://github.com/danjdewhurst/story-skills/blob/main/examples/harbor-of-second-light/continuity/state.md)
- [`examples/harbor-of-second-light/continuity/promises/the-bell-failsafe.md`](https://github.com/danjdewhurst/story-skills/blob/main/examples/harbor-of-second-light/continuity/promises/the-bell-failsafe.md)
- [`examples/harbor-of-second-light/continuity/questions/what-happened-on-blackout-night.md`](https://github.com/danjdewhurst/story-skills/blob/main/examples/harbor-of-second-light/continuity/questions/what-happened-on-blackout-night.md)
- [`skills/chapter-writing/references/scene-template.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/chapter-writing/references/scene-template.md)

### Skills

- [`skills/story-init/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/story-init/SKILL.md)
- [`skills/character-management/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/character-management/SKILL.md)
- [`skills/worldbuilding/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/worldbuilding/SKILL.md)
- [`skills/plot-structure/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/plot-structure/SKILL.md)
- [`skills/chapter-writing/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/chapter-writing/SKILL.md)
- [`skills/revision-continuity/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/revision-continuity/SKILL.md)
- [`skills/story-maintenance/SKILL.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/story-maintenance/SKILL.md)
- [`skills/chapter-writing/references/writing-guidelines.md`](https://github.com/danjdewhurst/story-skills/blob/main/skills/chapter-writing/references/writing-guidelines.md)

### Deterministic implementation / tests

- [`src/continuity.js`](https://github.com/danjdewhurst/story-skills/blob/main/src/continuity.js)
- [`src/story.js`](https://github.com/danjdewhurst/story-skills/blob/main/src/story.js)
- [`test/continuity.test.js`](https://github.com/danjdewhurst/story-skills/blob/main/test/continuity.test.js)
- [`.github/workflows/ci.yml`](https://github.com/danjdewhurst/story-skills/blob/main/.github/workflows/ci.yml)

### Downstream story automation

- [`templates/github/story-checks.yml`](https://github.com/danjdewhurst/story-skills/blob/main/templates/github/story-checks.yml)
- [`templates/github/draft-next-chapter.yml`](https://github.com/danjdewhurst/story-skills/blob/main/templates/github/draft-next-chapter.yml)

### Licensing/provenance paths checked

- [`LICENSE`](https://github.com/danjdewhurst/story-skills/blob/main/LICENSE) — present, MIT
- [`NOTICE`](https://github.com/danjdewhurst/story-skills/blob/main/NOTICE) — not found at analysis time
- [`ATTRIBUTION.md`](https://github.com/danjdewhurst/story-skills/blob/main/ATTRIBUTION.md) — not found at analysis time

---

## 17. Provisional CodexWriter Disposition

The following are **candidate Phase 1 dispositions**, not final architecture commitments.

### Retain / strongly investigate

- Shared structured story contract.
- Dedicated current continuity state.
- Character/object/knowledge state categories.
- Durable promise/payoff records.
- Durable open-question records.
- Scene-level state/change records.
- Explicit pre-write context reload.
- Explicit post-write state maintenance.
- Deterministic continuity checks backed by structured metadata.
- Separate validation, link integrity, and continuity checks.
- Mechanical maintenance tooling isolated from prose decisions.
- CI-able fiction continuity contracts.
- Import/migrate/reindex/doctor/report operational capabilities.

### Adapt rather than copy directly

- Markdown/YAML storage model — compare with Zenstory and other sources before deciding.
- `_index.md` registry architecture — clarify whether registries are source-of-truth or derived views.
- Chapter-writing workflow — preserve CodexWriter's current scene-planning/scene-writing distinction until later comparison.
- Revision-continuity combined skill — keep CodexWriter `continuity` unified for now, but do not merge prose editing into it solely because Dewhurst does.
- Automated chapter PR workflow — useful HITL mode, but execution-specific.

### Defer

- Final canonical state authority model.
- State history/delta strategy.
- Concurrency/stale-write controls.
- Long-context LOD strategy.
- Whether maintenance becomes a first-class CodexWriter skill, CLI/tool layer, or orchestrator support capability.

### Avoid

- Claiming deterministic validation for semantic narrative qualities not encoded in machine-checkable fields.
- Treating mechanically clean state as proof that a chapter is narratively coherent or well written.
- Allowing registry/entity/current-state authority to remain ambiguous in CodexWriter's final design.

---

## 18. Questions to Carry Into Zenstory Analysis

Dewhurst sharpens several questions for the third analysis:

1. Does Zenstory's single authoritative structured state solve real ambiguity present in Dewhurst's distributed Markdown model, or does it add unnecessary centralization?
2. How does Zenstory handle state history and earlier-chapter revisions compared with Dewhurst's workflow-driven updates?
3. Does Zenstory provide stale-update/concurrency safeguards absent here?
4. Can Dewhurst's human-readable Markdown-first model offer better author inspectability than Zenstory's derived-view approach?
5. Which system has the stronger context-loading strategy for long novels?
6. Which responsibilities belong in deterministic tooling versus agent skills?
7. Can CodexWriter combine Dewhurst-style author-editable artifacts with stronger state transaction guarantees without creating two competing sources of truth?

These questions should guide `docs/source-analysis/zenstory-ai.md` without pre-deciding the answer.
