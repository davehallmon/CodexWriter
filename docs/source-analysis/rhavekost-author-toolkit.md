# Source Analysis: rhavekost/author-toolkit

**Status:** Ready for review — not yet accepted  
**Source analyzed:** [`rhavekost/author-toolkit`](https://github.com/rhavekost/author-toolkit)  
**Analysis date:** 2026-08-26  
**Pinned commit:** `b78287003edf52e5f0784ee2b4a004111173358f` (2026-07-14)  
**Decision status:** Evidence review only; every CodexWriter disposition is provisional

## Evidence Labels

This document deliberately separates source facts from interpretation.

- **Observed** — directly established by a repository file or complete-tree inventory at the pinned commit.
- **Inference** — an analytical interpretation supported by multiple observations but not explicitly stated by the source.
- **Uncertainty** — not established by the pinned artifacts, or a source claim that requires additional validation.

CodexWriter dispositions in this document are **Phase 1 candidates**, not final architecture decisions.

---

## 1. Repository Snapshot

### Observed

- **Repository:** [`rhavekost/author-toolkit`](https://github.com/rhavekost/author-toolkit)
- **Visibility:** Public.
- **Created:** 2026-07-09.
- **Last push:** 2026-07-22 (from repository metadata; pinned commit is 2026-07-14).
- **Default branch:** `main`.
- **Primary implementation/documentation language:** Markdown (`SKILL.md` frontmatter + prose instructions). No code runtime.
- **Plugin manifest:** `.claude-plugin/plugin.json` declares version `1.3.1`, author `rhavekost` (rob@kostlabs.com), license `MIT`, platform `Claude Code` only.
- **Marketplace manifest:** `.claude-plugin/marketplace.json` declares the same.
- **Skill count:** 6 top-level skills tracked in the pinned tree: `fiction-workshop`, `character-archetypes`, `story-structure`, `narrative-nonfiction`, `prose-mechanics`, and the vendored `avoid-ai-writing`.
- **GitHub metadata at analysis time:** 13 stars, 3 forks, 0 open issues (from commits page); GitHub's detected license field is `MIT`.
- **Detected repository language:** Markdown.
- **Runtime claims:** README and plugin.json target Claude Code only. No CLI tool, no cross-host support, no agentskills.io or OpenClaw compatibility claimed in the pinned manifests (the `avoid-ai-writing/SKILL.md` header claims broader compatibility, but that is the vendored skill's own claim, not the toolkit's).
- **No `.github/` directory exists at the pinned commit**, so no repository-native GitHub Actions CI workflow was observed.
- **Tree inventory:** 79 tracked files at the pinned commit. This analysis directly read the manifest, README, LICENSE, ATTRIBUTION.md, finding-schema.json, all six `SKILL.md` files, all reference files for `fiction-workshop` (9), `character-archetypes` (6), `narrative-nonfiction` (7 plus the skill itself), and `prose-mechanics` (SKILL.md plus `audit-tracker-template.md`, `sentence-length-variance.md`, `cliches-audit.md`, and the full 17 `references/*.md` audit-reference files). The remaining `prose-mechanics` exemplar files (14) and `story-structure` reference files (3 plus the skill itself) were not individually read in this pass but are listed in the tree inventory below.

### Observed tree inventory (79 files, pinned commit)

```
.claude-plugin/marketplace.json
.claude-plugin/plugin.json
ATTRIBUTION.md
LICENSE
README.md
references/finding-schema.json
skills/avoid-ai-writing/.gitignore
skills/avoid-ai-writing/CHANGELOG.md
skills/avoid-ai-writing/LICENSE
skills/avoid-ai-writing/README.md
skills/avoid-ai-writing/SKILL.md
skills/character-archetypes/SKILL.md
skills/character-archetypes/assets/archetype-profile-template.md
skills/character-archetypes/references/archetype-analyzer.md
skills/character-archetypes/references/archetype-audit.md
skills/character-archetypes/references/archetype-conformance.md
skills/character-archetypes/references/archetype-ensemble.md
skills/character-archetypes/references/narrative-role-archetypes.md
skills/character-archetypes/references/personality-archetypes.md
skills/fiction-workshop/SKILL.md
skills/fiction-workshop/assets/scene-worksheet.md
skills/fiction-workshop/assets/story-bible-template.md
skills/fiction-workshop/references/brainstorming.md
skills/fiction-workshop/references/character-work.md
skills/fiction-workshop/references/continuity-tracking.md
skills/fiction-workshop/references/developmental-editing.md
skills/fiction-workshop/references/line-editing.md
skills/fiction-workshop/references/scifi-worldbuilding.md
skills/fiction-workshop/references/thriller-craft.md
skills/narrative-nonfiction/SKILL.md
skills/narrative-nonfiction/assets/book-blueprint-template.md
skills/narrative-nonfiction/assets/chapter-template.md
skills/narrative-nonfiction/references/conceptual-reveal.md
skills/narrative-nonfiction/references/empirical-reveal.md
skills/narrative-nonfiction/references/exercise-design.md
skills/narrative-nonfiction/references/metaphor-consistency.md
skills/narrative-nonfiction/references/reveal-engineering.md
skills/narrative-nonfiction/references/structural-reveal.md
skills/narrative-nonfiction/references/transformation-arc.md
skills/narrative-nonfiction/references/voice-editing.md
skills/prose-mechanics/SKILL.md
skills/prose-mechanics/assets/audit-tracker-template.md
skills/prose-mechanics/references/accessibility-audit.md
skills/prose-mechanics/references/active-passive-audit.md
skills/prose-mechanics/references/adverb-audit.md
skills/prose-mechanics/references/cliches-audit.md
skills/prose-mechanics/references/crutch-words-audit.md
skills/prose-mechanics/references/dialogue-tags-audit.md
skills/prose-mechanics/references/echoes-audit.md
skills/prose-mechanics/references/exemplars/active-voice/agent-restored-01.md
skills/prose-mechanics/references/exemplars/deep-pov/filter-removal-01.md
skills/prose-mechanics/references/exemplars/dialogue-tags/invisible-tag-01.md
skills/prose-mechanics/references/exemplars/echoes/varied-diction-01.md
skills/prose-mechanics/references/exemplars/frequency/lexical-range-01.md
skills/prose-mechanics/references/exemplars/fresh-language/cliche-replacement-01.md
skills/prose-mechanics/references/exemplars/glue-words/tightened-sentence-01.md
skills/prose-mechanics/references/exemplars/readability/grade-consistency-01.md
skills/prose-mechanics/references/exemplars/readability/paragraph-break-01.md
skills/prose-mechanics/references/exemplars/sentence-openers/varied-starts-01.md
skills/prose-mechanics/references/exemplars/sentence-variance/mixed-rhythm-01.md
skills/prose-mechanics/references/exemplars/verb-choice/adverb-removal-01.md
skills/prose-mechanics/references/filter-words-audit.md
skills/prose-mechanics/references/frequency-audit.md
skills/prose-mechanics/references/invented-term-consistency-audit.md
skills/prose-mechanics/references/parallel-structure-audit.md
skills/prose-mechanics/references/pov-consistency-audit.md
skills/prose-mechanics/references/pronoun-clarity-audit.md
skills/prose-mechanics/references/sentence-length-variance.md
skills/prose-mechanics/references/sentence-starters-audit.md
skills/prose-mechanics/references/show-vs-tell-audit.md
skills/prose-mechanics/references/sticky-sentences-audit.md
skills/prose-mechanics/references/tense-consistency-audit.md
skills/story-structure/SKILL.md
skills/story-structure/assets/structure-profile-template.md
skills/story-structure/references/landmark-beats.md
skills/story-structure/references/signposts.md
skills/story-structure/references/structure-audit.md
skills/story-structure/references/structure-map.md
```

### Inference

The toolkit is a **Claude Code plugin of markdown-based editorial skills**, not a multi-agent runtime, not a general-purpose authoring framework, and not a code project. Its value to CodexWriter is in its behavioral patterns — particularly reader testing, audit stopping, and the finding-format contract — not in any runtime architecture.

### Uncertainty

The pinned commit is a documentation/scope-commit on top of a larger `feature/finding-contract-prose-mechanics-v2` branch. The full branch history (dozens of merge commits visible on the commits page) was not rebased into the pinned tree; only the tip commit's tree was inventoried. Conclusions here are about the pinned state, not about the development process behind it.

---

## 2. Licensing and Provenance

### Observed

- **Root `LICENSE`:** [`LICENSE`](https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/LICENSE) — MIT, Copyright (c) 2026 rhavekost. Full text present.
- **Plugin manifests:** `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` both declare `"license": "MIT"`.
- **`ATTRIBUTION.md`:** [`ATTRIBUTION.md`](https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/ATTRIBUTION.md) — present, 18 lines. Documents one vendored skill:
  - **Skill:** `avoid-ai-writing`
  - **Author:** Conor Bronsdon ([@ConorBronsdon](https://github.com/conorbronsdon))
  - **Source:** <https://github.com/conorbronsdon/avoid-ai-writing>
  - **License:** MIT
  - **Vendored commit:** [`b38ee9f8f529476ac2d4f870d2dce2d9a155f34d`](https://github.com/conorbronsdon/avoid-ai-writing/commit/b38ee9f8f529476ac2d4f870d2dce2d9a155f34d)
  - **Upstream LICENSE:** [`skills/avoid-ai-writing/LICENSE`](https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/avoid-ai-writing/LICENSE) — MIT, Copyright (c) 2026 Conor Bronsdon. Full text present.
  - **Upstream README:** [`skills/avoid-ai-writing/UPSTREAM-README.md`](https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/avoid-ai-writing/UPSTREAM-README.md) — present.
- **Vendored `avoid-ai-writing/` subtree:** SKILL.md, LICENSE, CHANGELOG.md, README.md, .gitignore, and UPSTREAM-README.md all present in the pinned tree.
- **No `NOTICE` file** at the root.

### Inference

Provenance hygiene for the one vendored component is **sound and explicitly documented**. The root project and the vendored skill are both MIT. There is no multi-origin tangle, no Apache-2.0-compatibility concern, and no missing upstream license. This is cleaner than several CodexWriter sources (e.g., Lensetek's missing root LICENSE).

### Uncertainty

Only one vendored component is documented. If `avoid-ai-writing` itself vendors anything, that is not visible in the pinned tree.

---

## 3. Architectural Thesis

### Observed

The toolkit is an **editorial-companion plugin**, not a project-management framework and not a writing engine. Its README frames the problem as:

> Book projects span weeks or months, and Claude has no memory between sessions.

The solution is a set of editorial personas and diagnostic modes that run inside a single Claude Code session, with persistent state handled by convention — a Story Bible Markdown file, session-end notes in a `sessions/` folder, and a prose audit tracker — not by any runtime or schema.

The organizing principle is **persona/mode invocation by the author**, not autonomous routing. The author says "As developmental editor..." or "Run active/passive audit on chapter 3," and the skill responds within that lens. There is no orchestrator, no phase gating, no automatic progression.

The responsibilities treated as first-class are:

- Five editorial personas in `fiction-workshop` (Developmental Editor, Line Editor, Character Consultant, Continuity Tracker, Brainstorm Partner)
- Four diagnostic modes in `character-archetypes` (Analyzer, Audit, Conformance, Ensemble)
- Two modes in `story-structure` (Map, Audit)
- Mode-specific guidance in `narrative-nonfiction` (Voice Editor, Content Editor, Exercise Designer, Metaphor Consultant, Reveal Engineer)
- 19 diagnostic audit passes in `prose-mechanics`, each a separate focused pass
- A vendored `avoid-ai-writing` audit/rewrite skill

### Inference

This is a **role-guidance layer on top of a single LLM session**, not an agentic architecture. Every "persona" is a set of instructions the same Claude instance follows when invoked. The skill's value is in what it teaches the LLM to do and not do within a session — stopping points, focused scope, finding format, and the discipline of not auto-advancing — not in any multi-agent parallelism.

---

## 4. Workflow and Orchestration

### Observed

#### Entry points

The skill is invoked by Claude Code slash commands:

```
/author-toolkit:fiction-workshop
/author-toolkit:character-archetypes
/author-toolkit:story-structure
/author-toolkit:narrative-nonfiction
/author-toolkit:prose-mechanics
/author-toolkit:avoid-ai-writing
```

After activation, the author works by invoking a persona or audit mode in natural language: "As developmental editor, analyze Chapter 3," "Run active/passive audit on chapter 7," "What archetype is this character?"

There is **no internal router**. The author chooses the skill and the persona/mode. The skill's job is to respond correctly within that lens.

#### Workflow stages

`fiction-workshop` has three numbered stages:

1. **Story Bible Building (Stage 1):** Establish shared story foundation. Freeform, no persona invocation required.
2. **Chapter Development (Stage 2):** Draft or refine chapters through brainstorm → curate → draft → refine cycles (creation workflow) or read/diagnose/propose/implement/iterate cycles (editing workflow).
3. **Reader Testing (Stage 3):** Verify manuscript works without author context, using a fresh sub-agent without the Story Bible.

`prose-mechanics` is a parallel diagnostic track, not a stage of `fiction-workshop`. Its workflow is audit-by-audit: run one pass, produce a flagged-issues report, stop, wait for author review, apply approved fixes, update tracker, move to next audit.

`character-archetypes`, `story-structure`, and `narrative-nonfiction` each have their own mode tables and stop conditions but are not staged within `fiction-workshop`.

#### Specialist role boundaries

Each persona/mode has a defined focus. From `fiction-workshop/SKILL.md`:

| Role | Invocation | Focus |
|------|------------|-------|
| **Developmental Editor** | "As developmental editor..." | Plot, pacing, structure, stakes, theme |
| **Line Editor** | "As line editor..." | Prose rhythm, word choice, "show don't tell" |
| **Character Consultant** | "As character consultant..." | Voice consistency, motivation, arc, relationships |
| **Continuity Tracker** | "As continuity tracker..." | Timeline, world facts, internal consistency |
| **Brainstorm Partner** | "Brainstorm mode..." | "What if" exploration, problem-solving |

The skill explicitly warns against mixing personas in one pass: "Invoke one persona per pass. Developmental → Character → Line → Continuity. Focused feedback is actionable feedback."

#### Stop conditions and handoffs

Every persona, mode, and audit has a documented stopping point. The stopping-points table in `fiction-workshop/SKILL.md` (lines 203-213) defines for each tool/stage: **Stop when...** and **Then...**.

Key examples:

- **Developmental Editor:** One full structural pass on the requested scope is complete and issues list is delivered → Wait for author to apply edits. Do not loop into rewriting unless explicitly asked.
- **Line Editor:** One chapter is line-edited; after 3 passes with minimal changes, ask "what could be cut?" once → If no further direction, stop.
- **Character Consultant:** One consult on the named character/scene is complete → Do not reflexively check other characters or scenes.
- **Continuity Tracker:** Audit produces flag list → Stop. Do not fix automatically. Author decides which flags are real and how to resolve.
- **Reader Testing:** Fresh sub-agent's report is delivered → Stop. Author decides whether to return to Stage 2 and on which findings.

The handoff is always **author-mediated**. No persona hands off to another persona automatically. The orchestrator role, if any, is the author.

#### Human approval gates

The author is the gate at multiple points:

- After each persona pass, the author decides whether to continue, revise, or stop.
- After each prose audit, the author reviews the flagged-issues report and approves or dismisses each flag before any fix is applied.
- After reader testing, the author decides whether to return to Stage 2 and on which findings.
- Before a change in scope (e.g., moving from continuity audit to applying fixes), the skill is instructed to name what's about to happen so the scope shift is visible.

### Inference

The "human-in-the-loop gate" in this source is not a phase gate in the CodexWriter sense. It is a **stop-and-wait discipline** applied continuously across the session. Every tool has a stopping point; the author decides what happens next each time. This is softer than CodexWriter's five-gate pipeline but is applied far more granularly.

### Uncertainty

It is unclear how consistently this stop discipline is enforced in practice. The skill defines it; whether Claude Code reliably stops is a behavioral claim about the LLM, not a structural guarantee from the repository.

---

## 5. State Storage Model

### Observed

The state model is **document-oriented and convention-based**, not schema-driven.

#### Static/canonical story facts

The **Story Bible** is the source of truth. From `fiction-workshop/SKILL.md`:

> Novel projects span weeks or months. Claude has no memory between sessions, so the Story Bible is your persistent state.
> - **At session start:** Read `story-bible.md` (or whatever the project calls it) before doing any other work. Skim recent files in `sessions/` for unresolved threads.
> - **At session end:** Write a brief note at `sessions/YYYY-MM-DD_topic-slug.md` summarizing what was done, decisions made, and the stopping point. Two to five sentences is enough.
> - **When foundations shift:** Update the Story Bible immediately when premise, character bios, world rules, or major plot turns change. The Story Bible is the source of truth, not a one-time template.

The Story Bible contains plot, characters (protagonist Want/Need/Wound/Arc, antagonist, supporting cast, POV voice notes), world, and theme. `assets/story-bible-template.md` provides a blank structure.

Character archetypes are stored in the Story Bible as "Archetype Profile" blocks. The `character-archetypes/SKILL.md` says explicitly: "this skill does not write to the Story Bible directly."

Story structure profiles are stored in the Story Bible's "Plot Foundation" section as "Structure Profile" blocks. `story-structure/SKILL.md` says: "this skill does not write to the Story Bible directly."

#### Dynamic/current story state

There is **no current-character-state artifact, no timeline.json, no scene-state file, no promise/payoff schema, no revision counter**. The current state of the manuscript is the manuscript itself. The current state of the project's knowledge is the Story Bible plus the `sessions/` notes.

#### Which artifact is authoritative when files disagree

The **Story Bible** is authoritative for story facts. The manuscript is authoritative for what was actually written. If prose and Story Bible conflict, the skill doesn't define a resolution mechanism — the Continuity Tracker flags the inconsistency and stops.

#### Human-readable vs. machine-readable state

All state is Markdown, intended to be read by a human author and by an LLM in the next session. There is no machine-facing schema, no JSON state file, no indexing.

#### Story-history representation

Session-end notes in `sessions/YYYY-MM-DD_topic-slug.md` provide a lightweight chronological record. The prose audit tracker (`audit-tracker.md`) tracks which audits have run on which chapters. Full findings live in `reports/prose/<chapter>--<audit>--<stamp>.md`. There is no versioned story state, no delta log, no snapshot chain.

#### How state is updated after drafting

The author updates the Story Bible manually when foundations change. The skill doesn't write to the Story Bible directly (this is stated explicitly in `character-archetypes` and `story-structure`). The skill writes session notes and audit reports.

#### How state is updated after revising an earlier chapter

Not addressed. The skill acknowledges that continuity tracking exists (a Continuity Tracker persona), but does not define a process for what happens to the Story Bible, the audit tracker, or downstream audits when an earlier chapter is revised.

#### Stale/conflicting update protections

The Continuity Tracker is the primary mechanism for catching inconsistencies. From its reference file (`fiction-workshop/references/continuity-tracking.md`):

> When invoked as "continuity tracker," focus on internal consistency of facts, timeline, and world rules.

Categories: Physical Continuity, Timeline Continuity, Character Continuity (knowledge states, relationship status, emotional carryover, injuries/fatigue/hunger), World Rules Continuity.

Red-flag patterns include: "She said" when only men are present, characters referring to information they haven't learned yet, time passing faster or slower than physical travel allows, characters in two places at once, objects appearing/disappearing without explanation.

There is **no automated stale-data detection**. The skill relies on the author invoking the Continuity Tracker and on the LLM's judgment during that invocation.

#### Promises/payoffs, questions, foreshadowing, timeline, relationships, objects, and character-knowledge representation

Not represented as structured artifacts. The Story Bible's character entries include Want/Need/Wound/Arc and voice notes; its plot section includes premise, three-act structure/beat sheet, major turns, ending. That's the extent of structured representation. Promises, payoffs, foreshadowing, and character-knowledge states are tracked by the author's and LLM's memory within the session and by the Continuity Tracker when invoked.

#### Author preference/voice memory

Not separated from story canon. There is no author-preferences artifact. The skill's voice guidance is embedded in the Line Editor and Character Consultant personas.

#### Treatment of exploratory/non-canonical material

Not addressed. The skill's scope is canonical story work. There is no divergence-control mechanism.

### Inference

This is a **file-and-convention model**, not a state engine. Its strengths are simplicity and readability. Its weaknesses are exactly the gaps CodexWriter's structured-state hypothesis is designed to fill: no authoritative dynamic state, no revision tracking, no structured knowledge representation, no stale-data protection, no author-memory separation.

---

## 6. Context Management

### Observed

Context management is **implicit and session-scoped**, not a designed subsystem.

#### What is loaded before a task

For `fiction-workshop` Stage 1: read the Story Bible (if it exists). For Stage 2: invoke a persona and load the corresponding reference file. The skill says: "Load only the reference file matching the currently invoked persona. Do not preload all references at session start — it wastes context budget."

For `prose-mechanics`: read `audit-tracker.md` at session start; load only the reference file matching the currently invoked audit.

For `character-archetypes`: if a Story Bible exists, check each main character's entry for an existing Archetype Profile block. Load only the reference file matching the currently invoked mode.

#### What is excluded

The skill explicitly says to load only one reference file per invocation, not all of them. It does not define sharding, indexing, near-field/far-field, or summary-vs-prose tradeoffs.

#### Full-text vs. summary/structured context

The skill reads the full manuscript text when auditing or editing. There is no summary layer, no index, no "near-field" of detailed context and "far-field" of summarized context. The entire chapter or scope is loaded as raw text.

#### Sharding/indexing strategy

None. The skill does not address large-project scaling.

#### Near-field vs. far-field behavior

Not defined. The skill operates on whatever scope the author names ("Chapter 3," "chapters 4-8," "this scene").

### Inference

Context management in this source is **the absence of a designed system**. The skill's guidance is "load less, not more" — one reference file per invocation — and the Story Bible serves as a human-readable index into the project. For a large project, this model would need significant supplementation to avoid context overflow.

---

## 7. Strengths, Weaknesses, HITL Behavior

### Observed strengths

1. **Reader testing as context-isolated pass with explicit stopping.** `fiction-workshop/SKILL.md` Stage 3 (lines 147-161):
   > **Goal:** Verify manuscript works without author context.
   > **Using fresh sub-agent (no story bible):**
   > 1. **Comprehension:** Can they summarize plot, understand motivations, identify stakes?
   > 2. **Engagement:** Where did they lose interest, have questions, feel confused?
   > 3. **Emotional:** Did key moments land? Ending satisfying? Theme clear?
   > **Exit condition:** Reader understands and engages without author explanations.

   The stopping point (line 211): "Fresh sub-agent's report is delivered → Stop. Author decides whether to return to Stage 2 and on which findings."

   This is the single most directly reusable pattern for CodexWriter. It is the strongest available evidence for **separating reader testing from author context**, and it directly contradicts CodexWriter's current reader-simulation skill, which loads the revised manuscript, scene outlines, character dossiers, Story Bible, continuity report, and narrative architecture. This is a behavioral contradiction, not an artifact gap.

2. **Prose auditing as diagnose → stop → author disposition → approved repair.** `prose-mechanics/SKILL.md` (lines 106-110):
   > 4. **Stop. Wait for author review.** Do not apply fixes automatically. The author decides which flags are real and which are stylistic choices.
   > 5. **Apply approved fixes:** Use `str_replace` for surgical edits on the flags the author confirms. Skip the rest without comment.

   The stopping-points table (lines 160-167) defines for each audit: "Flagged-issues report for the requested scope is delivered → Wait for author review. Do not apply fixes. Do not start the next audit."

   And `continuity-tracking.md`'s Continuity Tracker likewise: "Audit produces flag list → Stop. Do not fix automatically. Author decides which flags are real and how to resolve."

   This pattern is **consistent across two independent skills** in the same toolkit. It is the strongest available evidence for separating diagnosis from repair with an explicit author gate. It directly contradicts CodexWriter's current prose-editing design, which proceeds from assessment to revision in a single run.

3. **Finding contract with `confidence` field distinguishing `deterministic` from `judgment`.** `references/finding-schema.json` (lines 1-25):
   ```json
   {
     "$schema": "https://json-schema.org/draft/2020-12/schema",
     "title": "author-toolkit finding",
     "type": "object",
     "required": ["audit", "technique", "severity", "location", "issue", "confidence"],
     "additionalProperties": false,
     "properties": {
       "audit":       { "type": "string", "minLength": 1 },
       "technique":   { "type": "string", "minLength": 1 },
       "severity":    { "enum": ["note", "suggestion", "warning"] },
       "location":    {
         "type": "object",
         "required": ["file", "line", "quote"],
         "additionalProperties": false,
         "properties": {
           "file":  { "type": "string", "minLength": 1 },
           "line":  { "type": "integer", "minimum": 1 },
           "quote": { "type": "string", "minLength": 1 }
         }
       },
       "issue":      { "type": "string", "minLength": 1 },
       "exemplar":   { "type": "string" },
       "confidence": { "enum": ["deterministic", "judgment"] }
     }
   }
   ```

   Every skill's reference files reproduce this contract. `fiction-workshop/SKILL.md` lines 265-277: "emit them conforming to `../../references/finding-schema.json`... `confidence` ("judgment" — this skill has no deterministic component)." `prose-mechanics/SKILL.md` lines 67-73: same contract. `story-structure/SKILL.md` lines 79-87: same contract, with `confidence: "judgment"`.

   This is the single most important artifact for CodexWriter's continuity architecture. It provides a **shared finding vocabulary** and, critically, an **explicit vocabulary for classifying whether a finding is mechanically verifiable (deterministic) or model-judgment-based (judgment)**. This directly supports CodexWriter's need to distinguish executable continuity checks (schema validation, ID pattern checks, revision monotonicity) from interpretive ones (voice consistency, emotional progression, pressure-system adherence).

4. **Per-audit stopping discipline applied granularly, not just at phase boundaries.** The prose-mechanics stopping-points table defines a stop condition for each of 19 audits. This is finer-grained than CodexWriter's five-phase gates and may be more practical for prose work.

5. **Session continuity via Story Bible + session-end notes.** A lightweight, practical pattern for cross-session persistence without a state engine. Not a substitute for structured state, but a useful complement.

6. **Explicit "do not write to Story Bible" discipline.** Two skills (`character-archetypes`, `story-structure`) explicitly refuse to write to the Story Bible, handing results back to the author to paste. This models a clean separation between diagnostic output and canonical state.

7. **Proper provenance and licensing.** One vendored component, fully documented with upstream commit SHA, upstream LICENSE preserved, MIT throughout. Cleaner than several CodexWriter sources.

### Observed weaknesses

1. **Claude Code platform only.** Plugin manifests, slash commands, and the `scriptorium` engine hook (noted in `prose-mechanics/SKILL.md`) all target Claude Code. The plugin.json declares no cross-host compatibility. This source provides no portability evidence for CodexWriter's multi-host goal.

2. **No structured state model.** Document-oriented, convention-based. No schema, no JSON state, no revision tracking, no authoritative dynamic state. This is the gap CodexWriter's structured-state hypothesis is designed to fill.

3. **No deterministic validator.** The prose-mechanics audits include deterministic components (sentence-length variance, echoes, frequency, crutch words, filter words, adverb density, sticky sentences, etc.) and the `finding-schema.json` provides a `confidence: deterministic` vocabulary, but the source does not implement a deterministic validator. It describes an engine hook (`scriptorium prose audit <name> <chapter>`) as something to call if available, and otherwise says to perform the audit conversationally. There is no guarantee the engine exists in the pinned state.

4. **No CI/tests.** No test suite, no continuous integration. The quality bar is the LLM's adherence to the skill instructions, which is not verifiable without running the plugin.

5. **Continuity Tracker is a model-judgment persona.** The Continuity Tracker flags inconsistencies by judgment, not by schema validation or automated cross-reference. Its findings are `confidence: "judgment"`. There is no deterministic continuity checking.

6. **No author-memory separation.** No author-preferences artifact, no separation of author voice memory from story canon.

7. **Reader testing is a one-shot pass, not a diagnostic-to-repair loop.** The reader report stops; the author decides what to do. There is no structured reader-report format that drives specific revisions, no reader-persona calibration, no multi-pass reader refinement. This is appropriate for the source's scope but less developed than a dedicated reader-simulation skill might be.

8. **No large-project context management.** No sharding, no indexing, no near/far policy. The model assumes the project fits in a single Claude Code session context.

### HITL behavior

The HITL model in this source is **continuous stop-and-wait**, not phase-gate-based. The author is the gate after every persona pass, every audit, and every reader test. The skill's contribution is a disciplined stopping-point vocabulary — every tool defines "Stop when" and "Then" — that makes the stop points explicit rather than implicit.

This is a softer, more granular HITL model than CodexWriter's five-gate pipeline. It does not define phase transitions (drafting begins after architecture approval, etc.); it defines per-tool stopping points within an un-staged session.

---

## 8. CodexWriter Relevance

### Directly usable (high confidence)

1. **Reader-test isolation.** Stage 3 of `fiction-workshop` is the best available evidence that context-isolated reader testing is a practical pattern. It should drive a redesign of CodexWriter's reader-simulation skill to separate manuscript-only first pass from author-context-aware diagnostic pass.

2. **Audit-contract pattern.** `prose-mechanics/SKILL.md` defines a clear diagnose → report → stop → author disposition → approved repair loop. This is the strongest available evidence for separating prose diagnosis from prose revision, and should drive a redesign of CodexWriter's prose-editing skill.

3. **`finding-schema.json` as shared finding vocabulary.** The schema's `confidence: ["deterministic", "judgment"]` field is the cleanest available vocabulary for CodexWriter's need to classify continuity and prose checks as executable vs. judgment-based. CodexWriter should adopt or adapt this schema rather than invent its own.

4. **Granular stopping points as HITL vocabulary.** The per-tool "Stop when / Then" table is a useful pattern for CodexWriter's gate definitions, even if CodexWriter retains its phase-gate structure on top.

5. **Session continuity via Story Bible + session notes.** A lightweight complement to CodexWriter's structured state, not a replacement. Useful to document as an optional pattern for projects that don't need full structured state.

6. **"Do not write to canonical state" discipline.** The two skills that refuse to write to the Story Bible model a useful separation between diagnostic output and canonical state that CodexWriter should preserve.

### Conditional / needs caution

7. **Prose-mechanics audit types and detection patterns.** The 19-audit list and the individual reference files are rich and directly useful as a prose-diagnostic checklist. However, the `scriptorium` engine hook is an external dependency whose availability in the pinned state is not verified. CodexWriter should treat the audit *concepts* as reusable and the engine hook as platform-specific.

8. **Archetype taxonomy.** The Vogler/Campbell and Jungian taxonomies in `character-archetypes` are standard reference material, not a novel contribution. Useful as reference content, not as architectural guidance.

9. **Story-structure landmark-beat and signpost model.** Weiland's 11-beat skeleton and Bell's 14 signposts are standard craft references. Useful as content for a story-structure skill, not as a CodexWriter architectural pattern.

### Mostly irrelevant to CodexWriter's core architecture

10. **Claude Code platform specifics.** Slash commands, plugin manifests, `scriptorium` hook. Not portable and not architectural.

11. **Vendored `avoid-ai-writing`.** A useful skill in its own right, but the fact that the toolkit vendors it is a provenance example, not an architectural pattern. The skill's AI-ism detection rules are content, not structure.

12. **Session-end note format.** "Two to five sentences" is a lightweight convention. Not a CodexWriter artifact, but a useful optional pattern for low-state projects.

---

## 9. Licensing Impact on CodexWriter

### Observed

- Root project: MIT, Copyright (c) 2026 rhavekost.
- One vendored component (`avoid-ai-writing`): MIT, Copyright (c) 2026 Conor Bronsdon.
- No Apache-2.0, no GPL, no multi-origin tangle, no missing upstream license.

### Inference

The licensing situation for this source is **the cleanest of any CodexWriter source analyzed to date**. The root project is MIT. The one vendored component is MIT. Full upstream LICENSE is preserved. `ATTRIBUTION.md` documents the vendored commit SHA. There is no licensing friction for CodexWriter to adopt patterns from this source, beyond the general MIT attribution requirement.

This source's provenance hygiene is an example CodexWriter should emulate: document vendored components with upstream commit SHA, preserve upstream LICENSE, and record the relationship in an `ATTRIBUTION.md`.

---

## 10. CodexWriter Dispositions

All dispositions below are **Phase 1 candidates, not final decisions**.

### A. Reader testing — **redesign required**

**Disposition:** CodexWriter's reader-simulation skill should be redesigned to separate a **context-blind first pass** (manuscript only, no Story Bible, no outlines, no dossiers, no continuity report) from an **optional author-context-aware diagnostic pass**. The context-blind pass is the primary deliverable; the author-context pass is supplementary.

**Evidence:** `fiction-workshop/SKILL.md` Stage 3, lines 147-161, lines 211-212.

**Rationale:** This is the strongest directly-observed contradiction between a reviewed source and CodexWriter's current design. Reader simulation currently loads privileged author context (Story Bible, outlines, dossiers, continuity report, narrative architecture) as inputs. The Rhavekost source demonstrates that context-isolated reader testing is a defined, stoppable stage with a clear exit condition.

### B. Prose editing — **audit-contract redesign required**

**Disposition:** CodexWriter's prose-editing skill should be redesigned to separate **diagnostic pass** (flagged-issues report, stop, wait for author disposition) from **approved-repair pass** (apply only confirmed flags). The diagnostic pass should conform to a shared finding schema.

**Evidence:** `prose-mechanics/SKILL.md`, lines 106-110, stopping-points table lines 160-167; `fiction-workshop/references/continuity-tracking.md`, line 5.

**Rationale:** Two independent skills in the same toolkit define the same diagnose → stop → author disposition → approved repair pattern. This is the strongest available evidence that this pattern is practical and worth adopting.

### C. Shared finding schema — **adopt or adapt `finding-schema.json`**

**Disposition:** CodexWriter should adopt or adapt `references/finding-schema.json` as its shared finding vocabulary, including the `confidence: ["deterministic", "judgment"]` field. This schema should be the contract for continuity findings, prose-audit findings, and reader-test findings.

**Evidence:** `references/finding-schema.json`, lines 1-25; reproduced by `fiction-workshop/SKILL.md`, `prose-mechanics/SKILL.md`, `story-structure/SKILL.md`.

**Rationale:** The schema provides a shared vocabulary and, critically, an explicit classification of findings as deterministic vs. judgment-based. This directly supports CodexWriter's need to distinguish executable continuity checks from interpretive ones. Adopting an existing, tested schema is preferable to inventing a new one.

### D. Granular stopping points — **adopt as HITL vocabulary**

**Disposition:** CodexWriter should adopt the "Stop when / Then" table format as a standard section in each skill definition, even while retaining its five-phase gate structure. Each skill should define its per-tool stopping points in addition to the phase gates.

**Evidence:** `fiction-workshop/SKILL.md`, lines 203-213; `prose-mechanics/SKILL.md`, lines 160-167; `character-archetypes/SKILL.md`, lines 74-79.

**Rationale:** Granular stopping points make the stop discipline explicit rather than implicit. They complement phase gates without replacing them.

### E. "Do not write to canonical state" — **adopt as discipline**

**Disposition:** CodexWriter skills that produce diagnostic or proposed output should follow the Rhavekost discipline of handing results back to the author rather than writing to canonical state directly. The orchestrator or a designated skill handles canonical-state updates after author review.

**Evidence:** `character-archetypes/SKILL.md`, lines 33-35; `story-structure/SKILL.md`, lines 33-35.

**Rationale:** This separates diagnostic output from canonical state and prevents unsupervised mutation of the project's authoritative files.

### F. Session continuity — **document as optional pattern**

**Disposition:** CodexWriter should document the Story Bible + session-end-notes pattern as an optional lightweight continuity approach for projects that do not require full structured state. This is a complement to, not a replacement for, CodexWriter's structured-state model.

**Evidence:** `fiction-workshop/SKILL.md`, lines 10-17; `README.md`, lines 5-7.

**Rationale:** Some projects will not need or want a full structured-state engine. A documented lightweight alternative is useful.

### G. Prose-audit checklist — **adopt as reference content**

**Disposition:** CodexWriter should adopt the 19-audit list and individual detection patterns from `prose-mechanics/references/*.md` as reference content for its prose-editing or prose-audit skill. The audit *concepts* are reusable; the `scriptorium` engine hook is platform-specific and should not be assumed.

**Evidence:** `prose-mechanics/SKILL.md`, lines 39-63; individual reference files in `skills/prose-mechanics/references/`.

**Rationale:** The audit types are a well-curated prose-diagnostic checklist. They are portable content, not platform-specific architecture.

### H. Archetype and story-structure content — **adopt as reference content**

**Disposition:** CodexWriter should adopt the Vogler/Campbell and Jungian archetype taxonomies and the Weiland/Bell structure model as reference content for relevant skills, not as architectural guidance.

**Evidence:** `character-archetypes/SKILL.md`, lines 36-44; `story-structure/SKILL.md`, lines 6-10.

**Rationale:** These are standard craft references, useful as content but not as architectural patterns.

### I. Provenance hygiene — **emulate as standard**

**Disposition:** CodexWriter should adopt Rhavekost's vendored-component documentation as the standard for its own `ATTRIBUTION.md`: document each vendored or inherited component with upstream commit SHA, preserve upstream LICENSE, and record the relationship explicitly.

**Evidence:** `ATTRIBUTION.md`, lines 1-18; `LICENSE` (root), lines 23-29.

**Rationale:** This source's provenance hygiene is the cleanest of any CodexWriter source. Adopting the same standard improves CodexWriter's own provenance documentation.

### J. What NOT to adopt

- **Platform-specific Claude Code integration.** Not portable.
- **Document-oriented state model as CodexWriter's state model.** This is the gap CodexWriter's structured-state hypothesis is designed to fill; adopting it would abandon the structured-state work.
- **No orchestrator / author-as-router model as CodexWriter's orchestration model.** CodexWriter's value proposition includes automated phase routing; adopting a pure author-routing model would abandon that.
- **`scriptorium` engine dependency.** Platform-specific and not verified as available in the pinned state.

---

## 11. Unverified Claims That Need Direct Inspection

These were noted during the analysis but not directly verified because the relevant files were not individually read in this pass. They are flagged for a follow-up inspection pass before CodexWriter relies on them.

1. **`skills/prose-mechanics/references/*.md` and exemplar files.** 18 reference files and 12 exemplar files are tracked in the pinned tree. The 6 reference files and 1 asset (audit-tracker-template.md) that were directly read are documented in their respective SKILL.md or reference sections; the remaining 12 reference files and 12 exemplar files were not individually opened. The audit detection patterns, judgment protocols, and exemplar content for the unopened files should be read before CodexWriter adopts specific audit types.

2. **`skills/narrative-nonfiction/references/*.md` and asset files.** 8 reference files and 2 asset files are tracked in the pinned tree. 2 reference files were directly read (`reveal-engineering.md` and `transformation-arc.md`); the remaining 6 reference files and 2 asset files were not individually opened. The metaphor-consistency, empirical-reveal, structural-reveal, conceptual-reveal, voice-editing, and exercise-design patterns should be inspected before CodexWriter relies on them.

4. **`skills/avoid-ai-writing/SKILL.md` full detection rules.** The skill is 492 lines and was read in part. The specific AI-ism detection patterns (em-dash substitution, bold overuse, hollow intensifiers, hedging, etc.) should be reviewed before CodexWriter adopts or adapts them.

5. **`scriptorium` engine availability in pinned state.** The `prose-mechanics/SKILL.md` engine hook says: "Before running any audit, check `command -v scriptorium`." It is unclear whether `scriptorium` is part of the pinned repository or an external tool the skill expects to be installed separately.

---

## 12. Cross-Reference to Source Analyses

| Source | Analysis | Status |
|--------|----------|--------|
| Lensetek/Fiction-book-agent-skills | `lensetek.md` | Complete, ready for review |
| danjdewhurst/story-skills | `danjdewhurst-story-skills.md` | Complete, ready for review |
| zenstory-ai | `zenstory-ai.md` | Complete, ready for review |
| haowjy/creative-writing-skills | `haowjy-creative-writing-skills.md` | Merged analysis complete |
| JeroTan/novel-writer-english | `jero-tan-novel-writer-english.md` | Complete, ready for review |
| wgwtest/novel-writing | `wgwtest-novel-writing.md` | Merged analysis complete, ready for review |
| **rhavekost/author-toolkit** | **this document** | **Ready for review (not yet accepted)** |

---

## Appendix A: Pinned-Source Links

All links below point to the pinned commit `b78287003edf52e5f0784ee2b4a00411173358f`.

### Repository-level

- README: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/README.md>
- LICENSE: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/LICENSE>
- ATTRIBUTION.md: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/ATTRIBUTION.md>
- finding-schema.json: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/references/finding-schema.json>
- `.claude-plugin/plugin.json`: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/.claude-plugin/plugin.json>
- `.claude-plugin/marketplace.json`: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/.claude-plugin/marketplace.json>

### Skill files

- fiction-workshop: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/fiction-workshop/SKILL.md>
- character-archetypes: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/character-archetypes/SKILL.md>
- story-structure: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/story-structure/SKILL.md>
- narrative-nonfiction: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/narrative-nonfiction/SKILL.md>
- prose-mechanics: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/prose-mechanics/SKILL.md>
- avoid-ai-writing: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/avoid-ai-writing/SKILL.md>
- avoid-ai-writing LICENSE: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/avoid-ai-writing/LICENSE>
- avoid-ai-writing CHANGELOG: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/avoid-ai-writing/CHANGELOG.md>

### Key reference files (directly read in this pass)

- fiction-workshop/continuity-tracking: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/fiction-workshop/references/continuity-tracking.md>
- fiction-workshop/developmental-editing: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/fiction-workshop/references/developmental-editing.md>
- prose-mechanics/sentence-length-variance: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/prose-mechanics/references/sentence-length-variance.md>
- prose-mechanics/cliches-audit: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/prose-mechanics/references/cliches-audit.md>
- prose-mechanics/audit-tracker-template: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/prose-mechanics/assets/audit-tracker-template.md>
- character-archetypes/archetype-audit: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/character-archetypes/references/archetype-audit.md>
- character-archetypes/archetype-conformance: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/character-archetypes/references/archetype-conformance.md>
- narrative-nonfiction/reveal-engineering: <https://github.com/rhavekost/author-toolkit/blob/b78287003edf52e5f0784ee2b4a00411173358f/skills/narrative-nonfiction/references/reveal-engineering.md>

---

## Appendix B: ChatGPT-5 Sol Corroboration

ChatGPT-5 Sol's earlier independent review of this same pinned commit provided line-range quotations that this analysis has now verified against directly-read primary sources:

- The five editorial personas and their focus areas: verified against `fiction-workshop/SKILL.md` lines 42-48.
- Reader testing as context-isolated pass with explicit stopping: verified against `fiction-workshop/SKILL.md` lines 147-161, 211-212.
- Prose audits explicitly diagnose, stop, wait for author disposition, then apply approved fixes: verified against `prose-mechanics/SKILL.md` lines 106-110, 160-167.
- Continuity Tracker stops and does not fix automatically: verified against `fiction-workshop/references/continuity-tracking.md` (context lines 1-5) and `fiction-workshop/SKILL.md` line 209.
- `finding-schema.json` with `confidence` distinguishing `deterministic` from `judgment`: verified against `references/finding-schema.json` lines 1-25; reproduced in three skill files.
- Two skills (`character-archetypes`, `story-structure`) explicitly refuse to write to the Story Bible: verified against `character-archetypes/SKILL.md` lines 33-35 and `story-structure/SKILL.md` lines 33-35.

Where this analysis adds to the ChatGPT-5 Sol corroboration: direct verification of the `finding-schema.json` schema structure, the `ATTRIBUTION.md` existence and content (ChatGPT-5 Sol had noted the file existed but this analysis confirms the full content), the `scriptorium` engine hook as a platform-specific dependency, and the explicit "do not write to Story Bible" discipline in two skills.

Where this analysis corrects the ChatGPT-5 Sol corroboration: the ChatGPT-5 Sol review's characterization of prose-mechanics stopping behavior is confirmed, but its reliance on the `scriptorium` engine as the deterministic pass was not verified — the engine hook is described as conditional ("if available") and the reference files are the full specification "not an abbreviated fallback." This analysis treats the engine as an unverified external dependency.

---

*End of source analysis. Ready for review; not yet accepted as a final CodexWriter disposition.*