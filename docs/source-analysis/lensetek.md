# Source Analysis: lensetek/Fiction-book-agent-skills

**Status:** Draft ready for review  
**Source analyzed:** [`lensetek/Fiction-book-agent-skills`](https://github.com/lensetek/Fiction-book-agent-skills)  
**Analysis date:** 2026-08-25  

## Evidence Labels

This document deliberately separates source facts from interpretation.

- **Observed** — directly established by a repository file, script, manifest, or GitHub metadata.
- **Inference** — an analytical interpretation supported by multiple observations but not explicitly stated by the source.
- **Uncertainty** — not established by the inspected files, or a source claim that requires additional validation.

CodexWriter dispositions in this document are **Phase 1 candidates**, not final architecture decisions.

---

## 1. Repository Snapshot

### Observed

- **Repository:** [`lensetek/Fiction-book-agent-skills`](https://github.com/lensetek/Fiction-book-agent-skills)
- **Visibility:** Public.
- **Created:** 2026-08-09.
- **Last push observed in repository metadata:** 2026-08-09.
- **Default branch:** `main`.
- **Primary implementation/documentation language:** Skill frontmatter and many headings are English, but most `SKILL.md` instructions are Bahasa Indonesia. The README is bilingual.
- **Skill count:** `plugin.json` enumerates **16 skills** and reports version `1.4.0`.
- **Metadata discrepancy:** GitHub's repository description says **14 AI agent skills**, while the README and `plugin.json` enumerate 16.
- **GitHub metadata at analysis time:** 0 stars, 0 forks, 0 open issues; GitHub's detected license field is `null`.
- **Detected repository language:** HTML, largely because the repository includes a substantial `index.html`/GitHub Pages presentation.
- **Runtime claims:** README advertises Agent Skills CLI installation and prompt-based use in environments including Claude Code, Codex, Cursor, ChatGPT, and Google Antigravity.
- **Runtime integration files:** `plugin.json` plus `mcp_config.json`, the latter configuring a Fal.ai image-generation MCP server using `FAL_KEY`.
- **No `.github/` directory was found at analysis time**, so no repository-native GitHub Actions CI workflow was observed.

### Inference

The repository appears to be an **early, rapidly assembled architecture/demo snapshot rather than a mature, iteratively validated framework**. The evidence is its same-day creation/push window, internal 14-vs-16 skill metadata drift, broad feature claims, and lack of observed CI/test infrastructure.

### Uncertainty

Repository activity may change after this analysis. Re-check metadata during any later implementation or licensing decision.

---

## 2. Licensing and Provenance

### Observed

- README displays an MIT badge and links to [`LICENSE`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/LICENSE).
- `plugin.json` declares `"license": "MIT"`.
- The actual root `LICENSE` path returned **404 / Not Found** during this analysis.
- GitHub repository metadata reports `license: null`.
- Root [`NOTICE`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/NOTICE) was **not found**.
- Root [`ATTRIBUTION.md`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/ATTRIBUTION.md) was **not found**.
- No upstream/fork/translation lineage is declared in the inspected root files.

### Inference

The repository likely **intends** to use MIT, but the intended license and an actually granted license should not be treated as identical while the referenced license text is missing.

### CodexWriter implication

- **Do not publicly redistribute a translated or substantially copied derivative yet.**
- Architectural responsibilities and ideas can be analyzed and independently reimplemented, but implementation-level copying/translation should remain blocked pending license clarification or permission.
- Preserve links and snapshots of the discrepancy in CodexWriter provenance records.

This is a project-risk note, not legal advice.

---

## 3. Architectural Thesis

### Observed

Lensetek describes itself as an **orchestrator + specialist agents** system covering the fiction lifecycle from story concept through publication. Its README enumerates 16 roles spanning:

1. orchestration,
2. concept intake,
3. market/trend research,
4. worldbuilding,
5. character psychology,
6. plot architecture,
7. scene planning,
8. novel prose drafting,
9. comic/webtoon scripting,
10. children's storytelling,
11. accessibility/Braille formatting,
12. continuity auditing,
13. prose/dialogue polishing,
14. beta-reader simulation,
15. publishing/layout export,
16. repository update/security maintenance.

The [`fiction-book-orchestrator`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-book-orchestrator/SKILL.md) defines a five-phase pipeline:

`Concept → World/Character → Plot/Scenes → Draft/Edit → Continuity/Beta/Export`

with human approval gates between major phases.

### Inference

Lensetek's strongest contribution is its **responsibility taxonomy and end-to-end breadth**, not a deeply integrated stateful implementation. It treats many fiction-production responsibilities as first-class specialists that other repositories often omit.

---

## 4. Workflow and Orchestration

### Observed: five routed phases

The orchestrator explicitly routes:

1. **Phase 1 — Story Concept Intake**
   - invokes `story-concept-intake`
   - produces `story_brief.md`
   - requests HITL Gate 1

2. **Phase 2 — Worldbuilding & Character Psychology**
   - invokes `worldbuilding-architect`
   - invokes `character-designer-psychologist`
   - produces `worldbuilding_codex.md` and `character_sheets/`
   - requests HITL Gate 2

3. **Phase 3 — Plot Architecture & Scene Beats**
   - invokes `plot-narrative-architect`
   - invokes `storyboard-scene-planner`
   - produces `plot_outline.md` and `scene_breakdown.md`
   - requests HITL Gate 3

4. **Phase 4 — Scene Drafting & Editing**
   - invokes `novel-scene-writer`, or comic/children alternatives based on form
   - invokes `prose-dialogue-polisher`
   - requests HITL Gate 4

5. **Phase 5 — Continuity, Beta Feedback & Export**
   - invokes `plot-hole-continuity-checker`
   - runs `check_timeline_continuity.py`
   - invokes `beta-reader-critique-simulator`
   - invokes `fiction-layout-exporter`
   - requests HITL Gate 5

### Observed: skills not integrated into the main orchestrator route

The 16-skill manifest includes capabilities that the five-phase orchestrator does **not explicitly route**:

- `fiction-market-trend-analyst`
- `braille-accessibility-formatter`
- `fiction-agent-update-manager`

Market research therefore exists as a specialist but is not specified as a prerequisite/optional branch in the orchestrator. Accessibility is separately implemented but not explicitly included in Phase 5 routing. Update management operates outside the authoring pipeline.

### Observed: HITL phase mismatch

[`hitl_fiction_checklist.md`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/hitl_fiction_checklist.md) does not align perfectly with the orchestrator's five gates:

- The checklist's **Phase 1** includes worldbuilding approval, although the orchestrator performs worldbuilding in Phase 2 after Gate 1.
- The checklist's **Phase 4** includes continuity auditing and beta-reader simulation, although the orchestrator places those in Phase 5 after Gate 4.

### Inference

The orchestrator is a useful **workflow map**, but handoff contracts are mostly conceptual. It identifies which specialist comes next without formally specifying shared state, validated inputs, error behavior, or what each downstream skill must reload.

---

## 5. State Storage Model

### Observed: artifact-oriented Markdown state

Lensetek stores project knowledge primarily as separate Markdown artifacts:

- `story_brief.md`
- `worldbuilding_codex.md`
- `character_sheets/*.md`
- `plot_outline.md`
- `scene_breakdown.md`
- `chapters/*.md`
- `chapters_polished/`
- `continuity_report.md`
- `beta_reader_feedback.md`
- output/build artifacts

The templates make some story information structurally regular:

- [`character_sheet_template.md`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/templates/character_sheet_template.md) stores character identity, appearance, Want/Need/Lie/Ghost, planned arc states, voice, and relationships.
- [`plot_outline_template.md`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/templates/plot_outline_template.md) contains a Foreshadowing & Chekhov's Gun matrix with introduced/payoff chapter fields.

### Observed: Markdown can be parsed transiently

[`parse_character_sheet.py`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/parse_character_sheet.py) extracts bold `**Field**: value` entries from a character sheet and prints JSON. It does **not** write or maintain a persistent canonical JSON character-state store.

### Observed: no dedicated dynamic current-state artifact identified

Within the inspected skill definitions, templates, helper scripts, and repository tree, no explicit artifact was found for:

- current character state after each chapter,
- current object/location state,
- character knowledge state,
- a canonical event registry,
- state revision numbers,
- chapter deltas/transactions,
- stale-update protection,
- author preference memory.

Character sheets include planned **Starting State → Ending State** arc fields, but these are part of the static character design document rather than a demonstrated per-chapter current-state mechanism.

### Observed: no stated authority rule

No inspected file defines what is authoritative if, for example, a character sheet, worldbuilding codex, plot outline, continuity report, and written manuscript conflict.

### Observed: revision propagation is unspecified

No inspected source defines how revising an earlier chapter should recalculate or update later character, timeline, relationship, foreshadowing, or world state.

### Uncertainty

Absence claims here are limited to the repository files inspected on 2026-08-25. If new files are added later, this section should be rechecked.

### Phase 1 implication

Lensetek should be treated as evidence for **which state categories matter**, but not yet as the preferred implementation for persistent state.

---

## 6. Context Management

### Observed

- `novel-scene-writer` says it transforms **Scene Beats** into prose, establishing `scene_breakdown.md` as an implied immediate input.
- `plot-hole-continuity-checker` explicitly references `worldbuilding_codex.md` and `character_sheets/` during audits.
- Individual skills have named output artifacts that downstream agents can conceptually consume.

### Not observed

No inspected skill defines a systematic pre-task reload contract such as:

- read the story brief,
- read current character state,
- read relevant world facts,
- read plot/scene plan,
- read previous chapter,
- load unresolved promises/questions,
- exclude unrelated distant context.

No sharding, indexing, level-of-detail loading, near-field/far-field strategy, context budget, or summary-versus-prose authority rule was found.

No explicit cross-agent handoff payload/schema was found beyond artifact names.

### Inference

Lensetek's context model is primarily **artifact-by-convention**: specialist outputs are expected to be available to later specialists, but context selection/retrieval is left to the host agent rather than engineered as a first-class mechanism.

---

## 7. Creative-Craft Model

### Observed

Lensetek combines several familiar craft frameworks:

- `story-concept-intake`: genre/subgenre, audience, logline, moral theme, tropes, tone.
- `worldbuilding-architect`: magic/technology rules, costs/consequences, geography, factions, economy, beliefs, history.
- `character-designer-psychologist`: Want / Need / Lie / Ghost, positive/flat/negative arcs, voice and relationships.
- `plot-narrative-architect`: Save the Cat, 3-Act, Hero's Journey, Kishōtenketsu; subplot and foreshadowing mapping.
- `storyboard-scene-planner`: Swain Scene/Sequel — Goal, Conflict, Disaster, Reaction, Dilemma, Decision.
- `novel-scene-writer`: Show-Don't-Tell, sensory detail, dialogue subtext, sentence-length/pacing heuristics.
- `prose-dialogue-polisher`: cliché/purple-prose trimming, dialogue tags/action beats, sentence rhythm.

Form-specific craft also exists:

- comics/webtoons: panel pacing, camera shots, balloons, SFX, visual prompts;
- children's fiction: age bands, sentence density, rhyme/illustration briefs;
- accessibility/output: Braille-oriented and audio/digital presentation claims.

### Observed: voice treatment

Character-level dialogue voice is explicitly designed in character sheets, but no source-level author voice/style profile or prose-sample calibration mechanism was found.

### Inference

The craft guidance has **good categorical breadth but limited depth per skill**. Many rules are compact heuristics rather than a layered craft/evaluation system. For CodexWriter, these skills are useful as a taxonomy of craft responsibilities but should be compared against deeper English implementations before reuse.

### Candidate concern

Some prose rules are highly prescriptive (for example, requiring at least three sensory details per scene). CodexWriter should test whether such rules improve output or encourage formulaic prose before adopting them.

---

## 8. Evaluation and Continuity

### 8.1 Continuity

#### Observed skill-level audit

[`plot-hole-continuity-checker`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/plot-hole-continuity-checker/SKILL.md) defines four audit categories:

1. timeline,
2. worldbuilding rules,
3. character integrity,
4. foreshadowing/unanswered hooks.

It produces `continuity_report.md` with contradictions and suggested repairs.

#### Observed helper behavior

[`check_timeline_continuity.py`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/check_timeline_continuity.py) is described as a timeline/continuity validator, but its implementation:

- splits a Markdown manuscript by `#` chapter headings,
- searches for temporal keywords such as morning/night/tomorrow/yesterday/year patterns,
- logs which temporal markers appear in each chapter,
- warns when no explicit temporal markers are found.

It does **not** calculate temporal ordering, character ages, elapsed time, contradictory dates, world-rule violations, or state transitions.

#### Observed discrepancy

The HITL checklist says the script plus continuity checker should confirm **zero timeline contradictions** and **zero world-rule violations**. The helper script itself does not implement those validations.

### Inference

Lensetek's continuity architecture is therefore **primarily model-judgment auditing with a lightweight temporal-marker extraction helper**, not deterministic continuity enforcement in the stronger sense used by systems with structured contracts and validators.

### 8.2 Prose review

`prose-dialogue-polisher` produces a separately polished manuscript plus style notes. It does not define developmental-editing vs. line-editing passes, issue severity, approval per edit, or a structured findings schema.

### 8.3 Reader simulation

`beta-reader-critique-simulator` defines four reader personas and outputs hook/emotion/pacing feedback.

Not observed:

- a fresh/context-blind agent requirement,
- separation from author/story-bible knowledge,
- a reproducible scoring rubric,
- explicit stop/repair semantics after the report.

### 8.4 Audit vs. repair

The continuity skill produces findings plus suggestions; it does not state that it automatically edits the manuscript. This provides some audit/repair separation, although no formal author-resolution workflow is defined.

---

## 9. Human-in-the-Loop Model

### Observed

Human approval is a first-class principle.

The orchestrator requests five phase gates, and [`hitl_fiction_checklist.md`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/hitl_fiction_checklist.md) expands approval items for:

- premise/audience/tone/world,
- character psychology/voice/relationships,
- structure/subplots/scene beats,
- prose/continuity/beta feedback,
- print/digital output and final publication.

Separately, `fiction-agent-update-manager` prohibits `git pull` until the user explicitly approves the update.

### Not observed

- explicit rules preventing automatic scope expansion after each gate,
- canon-promotion semantics for brainstorms or alternatives,
- per-change editorial approvals,
- handling of intentional continuity exceptions,
- rollback semantics after approval.

### Observed inconsistency

As noted above, the standalone HITL checklist's phase grouping does not perfectly match the orchestrator's phase/gate sequence.

### Inference

Lensetek strongly values **human sign-off**, but approval semantics are checklist-oriented rather than transaction/scope-oriented.

---

## 10. Runtime and Maintenance

### Observed: Agent Skills packaging

- `plugin.json` enumerates the 16 skills and version `1.4.0`.
- README advertises installation through `npx skills` and direct repository/prompt import.
- `mcp_config.json` configures a Fal.ai image generator requiring `FAL_KEY`.

### Observed: environment-specific assumptions

Several skills reference host-specific tools without capability detection or a standardized fallback:

- `fiction-market-trend-analyst` requires `search_web` and `read_url_content`.
- `comic-webtoon-scriptwriter` refers to an internal `generate_image` tool in some environments or a Fal.ai Python helper.
- `fiction-agent-update-manager` assumes a `schedule` function and `/schedule` command for daily checks.

No orchestrator-level capability negotiation/fallback contract was found.

### Observed: update manager

[`fiction-agent-update-manager`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-agent-update-manager/SKILL.md) and [`check_fiction_updates.py`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/check_fiction_updates.py) implement:

- a credential-pattern scan over modified/untracked files,
- `git fetch origin`,
- local-vs-remote hash comparison,
- commit-log reporting,
- explicit user approval before `git pull`.

### Observed: no CI/test harness found

No `.github/` workflow directory was present, and no dedicated test suite was identified in the inspected tree.

### Observed: export implementation mismatch

`fiction-layout-exporter` claims DOCX/PDF plus EPUB/mobile-reader outputs. [`generate_fiction_docx.py`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/generate_fiction_docx.py) implements DOCX generation and accessibility flags; the inspected helper does not generate PDF or EPUB. A `web_reader/` directory exists, but no EPUB build helper was identified in the inspected helper set.

### Observed: accessibility implementation

[`generate_braille_text.py`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/generate_braille_text.py) implements a direct Latin-character-to-Unicode-Braille substitution map and dual/braille-only Markdown output.

### Uncertainty

The repository's claims of UEB, embosser readiness, EPUB3 accessibility, and publisher-grade accessibility compliance were **not independently validated** in this analysis. The helper code alone does not demonstrate conformance testing against those external standards.

---

## 11. Strengths

### Observed strengths

1. **Unusually broad specialist taxonomy.** Lensetek treats research, planning, drafting, editing, continuity, reader feedback, alternate forms, accessibility, publication, and maintenance as explicit responsibilities.
2. **Clear artifact names.** Each major skill usually has a named output, making the intended handoff chain easy to understand.
3. **Visible human approval philosophy.** HITL is present in the orchestrator and a dedicated checklist rather than being implicit.
4. **Multi-format thinking.** Novel, comic/webtoon, children's fiction, print/digital, and accessibility are modeled as distinct concerns.
5. **Some executable helpers.** Character parsing, timeline-marker extraction, market-keyword extraction, DOCX generation, image-generation integration, Braille substitution, and update checks move the repository beyond prompt-only instructions.
6. **Good baseline decomposition for comparison.** The 16-role list gives CodexWriter a practical coordinate system for asking which responsibilities should remain core, become extensions, or be replaced by stronger implementations.

### Inference

Lensetek is particularly useful as a **requirements inventory**: it raises questions that narrower fiction-writing repositories may never surface.

---

## 12. Weaknesses / Gaps

### Observed gaps

1. **No demonstrated dynamic current-state system.** Static planning artifacts exist, but no per-chapter current-state registry or revision model was identified.
2. **No explicit context-loading discipline.** Skills name artifacts but do not define robust pre-write reload, LOD, sharding, or near/far context behavior.
3. **Continuity helper does not perform the validation its surrounding documentation implies.** It extracts temporal markers rather than proving chronology consistency.
4. **No authority/conflict rule between manuscript and planning artifacts.**
5. **No old-chapter revision propagation protocol.**
6. **No structured author-preference/prose-voice memory.**
7. **No explicit non-canonical exploration workspace.**
8. **Orchestrator coverage is incomplete.** Market research, accessibility, and maintenance are in the taxonomy but not cleanly routed through the five-phase authoring workflow.
9. **HITL documents disagree on phase grouping.**
10. **Runtime portability is asserted more strongly than it is enforced.** Multiple skills assume tool names/capabilities without detection/fallback.
11. **No observed automated test/CI layer.**
12. **Implementation/claim drift exists.** Examples include 14-vs-16 metadata and export/continuity claims that exceed the inspected helper behavior.
13. **License intent is unresolved at file level.**

### Inference

The repository's **architecture is broader than its implementation depth**. It should not be copied wholesale as CodexWriter's execution model even if its specialist-role taxonomy remains influential.

---

## 13. Relevance to CodexWriter

### Observed reusable responsibilities

CodexWriter should continue evaluating all 16 responsibilities because each corresponds to a real function in Lensetek's workflow, even when the current implementation is shallow.

Especially relevant to the initial novel-authoring core:

- orchestration,
- concept development,
- worldbuilding,
- character development,
- narrative architecture,
- scene planning,
- scene writing,
- continuity,
- prose editing,
- reader simulation.

Likely extension/infrastructure responsibilities to evaluate separately:

- market research,
- comics/webtoon adaptation,
- children's adaptation,
- accessibility,
- publishing/export,
- update/runtime maintenance.

### Candidate architectural borrowing

- specialist-role breadth,
- explicit named output artifacts,
- phase-level human approvals,
- form-specific specialists rather than one universal writer,
- accessibility/publication as explicit lifecycle concerns.

### Implementation-level borrowing requiring license/provenance handling

Any direct translation or substantial reuse of:

- `SKILL.md` wording,
- templates,
- helper scripts,
- `hitl_fiction_checklist.md`,
- plugin/runtime files

should remain deferred while the missing `LICENSE` discrepancy is unresolved.

### Patterns CodexWriter should avoid unless later evidence changes the assessment

- presenting lightweight keyword extraction as deterministic continuity validation,
- assuming host-specific tools exist without capability checks,
- allowing multiple artifacts to imply canon without an authority rule,
- adopting prescriptive prose heuristics without evaluation,
- claiming standards compliance/export formats beyond tested implementation.

---

## 14. Skill-by-Skill Responsibility Matrix

| Lensetek Skill | Observed Responsibility | Observed Primary Output | Observed Dependencies / Tools | Observed State / Context Behavior | Phase 1 CodexWriter Disposition |
|---|---|---|---|---|---|
| [`fiction-book-orchestrator`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-book-orchestrator/SKILL.md) | Route the end-to-end fiction workflow and request five author gates | Coordinated project/manuscript workflow | Calls other named skills | Names artifacts/sequence; no shared state schema | **Retain responsibility**; implementation to be rebuilt from comparative evidence |
| [`story-concept-intake`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/story-concept-intake/SKILL.md) | Refine genre, audience, logline, theme, tropes, tone | `story_brief.md` | None explicit | Creates static project brief | **Retain responsibility** |
| [`fiction-market-trend-analyst`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-market-trend-analyst/SKILL.md) | Live trend/benchmark/title/tag research | `market_research_report.md`, keyword JSON | `search_web`, `read_url_content`, `generate_market_keywords.py` | External research; no canon boundary specified | **Extension candidate** |
| [`worldbuilding-architect`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/worldbuilding-architect/SKILL.md) | Define setting, systems, rules, geography, factions, history | `worldbuilding_codex.md` | Worldbuilding template | Static world canon candidate; no dynamic world-state updates | **Retain responsibility** |
| [`character-designer-psychologist`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/character-designer-psychologist/SKILL.md) | Design psychology, arc, voice, relationships | `character_sheets/` | Character template; `parse_character_sheet.py` | Static profile/arc; parser emits transient JSON | **Retain responsibility** |
| [`plot-narrative-architect`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/plot-narrative-architect/SKILL.md) | Structure plot/subplots and foreshadowing | `plot_outline.md` | Plot template | Planned foreshadow/payoff matrix; no live promise state | **Retain responsibility** |
| [`storyboard-scene-planner`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/storyboard-scene-planner/SKILL.md) | Convert chapters into Scene/Sequel beats | `scene_breakdown.md` | Scene-beat template | Provides immediate drafting plan | **Retain responsibility** |
| [`novel-scene-writer`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/novel-scene-writer/SKILL.md) | Turn scene beats into prose | `chapters/chapter_*.md` | Implied scene beats | No explicit pre-write state/context reload | **Retain responsibility; deepen heavily** |
| [`comic-webtoon-scriptwriter`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/comic-webtoon-scriptwriter/SKILL.md) | Adapt/write visual panel scripts and prompts | `comic_script.md`, prompt JSON/images | `generate_image` or Fal.ai helpers | No explicit shared-canon synchronization | **Extension candidate** |
| [`children-story-creator`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/children-story-creator/SKILL.md) | Create age-calibrated children's stories/illustration briefs | `children_storybook.md`, DOCX | formatter helper | Form-specific artifact | **Extension candidate** |
| [`braille-accessibility-formatter`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/braille-accessibility-formatter/SKILL.md) | Produce claimed Braille/audio/accessible outputs | `accessibility_plan.md`, build artifacts | Braille/DOCX helpers | Output transformation, not story state | **Extension candidate; standards validation required** |
| [`plot-hole-continuity-checker`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/plot-hole-continuity-checker/SKILL.md) | Audit timeline, world rules, character integrity, hooks | `continuity_report.md` | `check_timeline_continuity.py` | Reads manuscript/world/character artifacts; no persistent current-state contract | **Retain as one `continuity` responsibility for Phase 1; replace/deepen implementation** |
| [`prose-dialogue-polisher`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/prose-dialogue-polisher/SKILL.md) | Line-level prose/dialogue polish | `chapters_polished/`, notes | None explicit | Produces alternate polished artifact; no approval protocol | **Retain as `prose-editing`; deepen** |
| [`beta-reader-critique-simulator`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/beta-reader-critique-simulator/SKILL.md) | Simulate reader-persona reactions | `beta_reader_feedback.md` | Persona prompting | No context-isolation contract | **Retain as `reader-simulation`; deepen** |
| [`fiction-layout-exporter`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-layout-exporter/SKILL.md) | Build print/digital publication outputs | DOCX/PDF/EPUB/web-reader claimed | `generate_fiction_docx.py`, `web_reader/` | Disposable output layer | **Publishing extension candidate** |
| [`fiction-agent-update-manager`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-agent-update-manager/SKILL.md) | Check/update the skill repository safely | Update status/approval prompt | Git, `check_fiction_updates.py`, assumed `schedule` | Repository maintenance, not story state | **Infrastructure responsibility candidate; likely generalize rather than retain as fiction skill** |

### Matrix uncertainties

- Many skill files do not explicitly declare inputs; dependencies above are limited to those named in source files or directly implied by the orchestrator's artifact chain.
- “CodexWriter disposition” is a **candidate planning label**, not an implementation decision.

---

## 15. Detailed Evidence Index

### Repository / packaging

- [README.md](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/README.md)
- [plugin.json](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/plugin.json)
- [mcp_config.json](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/mcp_config.json)
- [HITL checklist](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/hitl_fiction_checklist.md)
- [LICENSE path — currently missing](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/LICENSE)

### Core workflow skills

- [fiction-book-orchestrator](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-book-orchestrator/SKILL.md)
- [story-concept-intake](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/story-concept-intake/SKILL.md)
- [worldbuilding-architect](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/worldbuilding-architect/SKILL.md)
- [character-designer-psychologist](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/character-designer-psychologist/SKILL.md)
- [plot-narrative-architect](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/plot-narrative-architect/SKILL.md)
- [storyboard-scene-planner](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/storyboard-scene-planner/SKILL.md)
- [novel-scene-writer](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/novel-scene-writer/SKILL.md)
- [plot-hole-continuity-checker](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/plot-hole-continuity-checker/SKILL.md)
- [prose-dialogue-polisher](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/prose-dialogue-polisher/SKILL.md)
- [beta-reader-critique-simulator](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/beta-reader-critique-simulator/SKILL.md)

### Extension / infrastructure skills

- [fiction-market-trend-analyst](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-market-trend-analyst/SKILL.md)
- [comic-webtoon-scriptwriter](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/comic-webtoon-scriptwriter/SKILL.md)
- [children-story-creator](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/children-story-creator/SKILL.md)
- [braille-accessibility-formatter](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/braille-accessibility-formatter/SKILL.md)
- [fiction-layout-exporter](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-layout-exporter/SKILL.md)
- [fiction-agent-update-manager](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/skills/fiction-agent-update-manager/SKILL.md)

### Templates and helper implementations

- [character_sheet_template.md](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/templates/character_sheet_template.md)
- [plot_outline_template.md](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/templates/plot_outline_template.md)
- [check_timeline_continuity.py](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/check_timeline_continuity.py)
- [parse_character_sheet.py](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/parse_character_sheet.py)
- [check_fiction_updates.py](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/check_fiction_updates.py)
- [generate_fiction_docx.py](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/generate_fiction_docx.py)
- [generate_braille_text.py](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/helpers/python/generate_braille_text.py)

---

## 16. CodexWriter Disposition — Provisional Baseline

This section is deliberately conservative because Lensetek is the first source analysis.

### Retain responsibility for comparative analysis

- orchestrator
- concept development
- worldbuilding
- character development
- narrative architecture
- scene planning
- scene writing
- continuity
- prose editing
- reader simulation

### Extension candidates

- market/trend research
- comic/webtoon adaptation
- children's-fiction adaptation
- accessibility
- publishing/export

### Infrastructure candidate

- repository/project maintenance, generalized beyond Lensetek's fiction-specific update manager

### Defer implementation decisions

- canonical state format
- continuity/state split
- context manager as a separate skill
- developmental review as a separate skill
- exact HITL gate taxonomy
- exact orchestration order beyond the current Phase 1 working model

### Replace/deepen candidate implementations

Based on the observed source behavior, the following Lensetek implementations should be treated as responsibilities to preserve but mechanisms to challenge in later source comparisons:

- deterministic continuity validation,
- persistent current-state tracking,
- context loading/handoffs,
- reader simulation methodology,
- prose/editorial depth,
- runtime capability handling.

### Next comparative question

The Dewhurst analysis should now test the most important unresolved Lensetek question:

> **What changes when story continuity is backed by explicit persistent state and deterministic contracts rather than primarily by static planning artifacts plus model review?**

That comparison may confirm, modify, or reject the provisional dispositions above.
