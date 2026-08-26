# Source Analysis: rhavekost/author-toolkit

**Status:** Draft — pinned analysis at upstream commit `b78287003edf52e5f0784ee2b4a00411173358f`  
**Source analyzed:** [`rhavekost/author-toolkit`](https://github.com/rhavekost/author-toolkit)  
**Analysis date:** 2026-08-26  
**Pinned commit:** `b78287003edf52e5f0784ee2b4a00411173358f` (2026-07-14)  
**Decision status:** Evidence review only; every CodexWriter disposition is provisional

## Evidence Labels

- **Observed** — directly established by a repository file, line range, executable test, or complete-tree inventory at the pinned commit.
- **Inference** — an analytical interpretation of observed evidence, not a claim that the source implements the inferred CodexWriter design.
- **Uncertainty** — something the pinned artifacts or bounded verification did not establish.

All upstream source links in this document reference files confirmed present at the pinned commit `b7828700` via the GitHub tree API, not mutable `main` refs where avoidable.

---

## 1. Repository Snapshot

### Observed

| Item | Pinned observation |
|---|---|
| Repository | `https://github.com/rhavekost/author-toolkit` |
| Commit | `b78287003edf52e5f0784ee2b4a00411173358f` |
| Commit date | 2026-07-14 |
| Default branch | `main` |
| Tree SHA at pin | `3b826097738bee8adcfdc88ae18d22580cf985c9` |
| Primary implementation | Claude Code plugin (`.claude-plugin/plugin.json`); skill content in Markdown `SKILL.md` files plus Markdown references |
| Package/plug-in manifest | `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` |
| Skills at pin (5 active + 1 vendored) | `fiction-workshop`, `prose-mechanics`, `story-structure`, `character-archetypes`, `narrative-nonfiction`, `avoid-ai-writing` (vendored) |
| Vendored component | `avoid-ai-writing` by Conor Bronsdon (@ConorBronsdon); MIT-licensed; upstream LICENSE preserved at `skills/avoid-ai-writing/LICENSE` |
| CI / tests | None observed at the pinned commit; repository is a Claude Code plugin, not a CI-oriented distribution |

### Inference

The pinned commit is best understood as a **Claude Code plugin defining five editorial personas and one vendored auditing skill**, with YAML-free Markdown skill files and Markdown references. It does not expose a CLI, a state engine, a test suite, or a cross-host packaging layer at this revision.

### Uncertainty

Repository activity may change after this analysis. Re-check metadata before any implementation-level borrowing or release decision.

---

## 2. Licensing and Provenance

### Observed

- **LICENSE:** Exact pinned root `LICENSE` contains the **MIT License**, copyright (c) 2026 rhavekost. The same file contains the standard terms through line 21.
- **NOTICE:** Not found in the pinned tree.
- **ATTRIBUTION.md:** **404 Not Found** at the pinned commit `b7828700`. A later ATTRIBUTION.md exists on `main` but was **not** present at the pinned revision.
- **Vendored component:** `skills/avoid-ai-writing/` is present at the pin. Its `LICENSE` file is preserved and declares MIT (Copyright (c) 2026 Conor Bronsdon). The root LICENSE explicitly notes: "This project vendors third-party skills that retain their original licenses. See ATTRIBUTION.md for a list of vendored components and their upstream license files. The vendored `avoid-ai-writing` skill is MIT-licensed (Copyright (c) 2026 Conor Bronsdon); its upstream LICENSE is preserved at `skills/avoid-ai-writing/LICENSE`."
- **Upstream lineage:** The README identifies `avoid-ai-writing` as vendored from [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing). No other translated, forked, or re-architected lineage is declared.
- **Root LICENSE at pin:** `a4648fd8e472871ded47e91110a2cf7e23135b5b`
- **Vendored LICENSE at pin:** preserved in `skills/avoid-ai-writing/LICENSE`

### Inference

The root LICENSE is a clean MIT grant for the repository's own contributions. The vendored `avoid-ai-writing` skill is also MIT, with a preserved upstream LICENSE file — a better provenance pattern than a bare license claim.

The missing ATTRIBUTION.md at the pinned commit is a **provenance gap**: the root LICENSE references ATTRIBUTION.md for the list of vendored components, but that file was not present at `b7828700`. CodexWriter should not assume the root LICENSE alone satisfies every obligation for the vendored skill until the relationship between the root LICENSE's reference, the preserved upstream LICENSE, and the (later) ATTRIBUTION.md is fully resolved.

### CodexWriter implication

- MIT permits implementation-level reuse subject to preservation of copyright and license notice.
- The vendored `avoid-ai-writing` skill is separately MIT; copying it would require preserving Conor Bronsdon's upstream copyright and license notice in addition to rhavekost's root notice.
- The PROPRIETARY gap between the root LICENSE's reference to ATTRIBUTION.md and the absence of that file at the pin should be documented, not assumed away.

This is a project-risk note, not legal advice.

---

## 3. Architectural Thesis

### Observed

The README describes a Claude Code plugin with five subject-matter skills and one vendored auditing skill:

1. **Fiction Workshop** — collaborative fiction writing and editing with 5 editorial personas (Developmental Editor, Line Editor, Character Consultant, Continuity Tracker, Brainstorm Partner); genre-specific guides for spy thrillers and hard sci-fi.
2. **Character Archetypes** — two taxonomies (Vogler/Campbell's 8 narrative-role archetypes; Jungian 12 personality archetypes) plus 4 analysis modes (Analyzer, Audit, Conformance, Ensemble).
3. **Story Structure** — percentage-anchored macro plot structure using K.M. Weiland's 11-beat landmark model and James Scott Bell's 14 signposts; map and audit modes.
4. **Narrative Nonfiction** — transformation arc, metaphor consistency, exercise design, reveal engineering (4 patterns), voice editing.
5. **Prose Mechanics** — sentence-level diagnostic audits (active/passive, parallel structure, sentence-length variance, accessibility); run one at a time, in order.
6. **Avoid AI Writing** — detect mode and rewrite mode for AI-ism patterns; vendored from Conor Bronsdon.

### Inference

Rhavekost's primary organizing principle is **Claude Code persona-driven editorial assistance with a Story Bible as persistent project state**. The plugin leverages Claude's built-in `/author-toolkit:skill-name` invocation path and the model's ability to switch editorial stance within a single session. It does not introduce a separate agent runtime, a state engine, or an orchestrator.

This is a different answer from CodexWriter's specialist-skill architecture. Rhavekost uses the host's persona/styling capability as the primary separation mechanism; CodexWriter defines explicit SKILL.md boundaries. Rhavekost's approach is platform-specific (Claude Code only, at this revision); CodexWriter's is platform-agnostic by design.

---

## 4. Workflow and Orchestration

### Observed: Fiction Workshop as the primary entry point

The Fiction Workshop skill defines the core workflow:

- **Session Continuity:** "All three skills now treat the project's blueprint or Story Bible as persistent state: read it at session start, update it when foundations change, and write a short note to `sessions/YYYY-MM-DD_topic-slug.md` at session end. The prose-mechanics skill uses a per-project audit tracker the same way." (README)

- **Editorial Personas:** Five personas — Developmental Editor (plot, pacing, structure, stakes), Line Editor (prose rhythm, word choice, show-don't-tell), Character Consultant (voice consistency, motivation, arc), Continuity Tracker (timeline, world facts, internal consistency), Brainstorm Partner (what-if exploration, problem-solving). Invoked by requesting a specific lens within Fiction Workshop.

### Observed: reader testing uses a fresh sub-agent without Story Bible context

This is the most important workflow detail for CodexWriter's evaluation model:

**ChatGPT-5 Sol independently inspected this at `b7828700`** and reported:

> "Its fiction workflow requires a fresh sub-agent without Story Bible context and stops after delivering the reader report (reader-test and stopping rules, `skills/fiction-workshop/SKILL.md` lines 149–214)."

This is a direct contradiction with CodexWriter's current reader-simulation design, which loads the revised manuscript, scene outlines, character dossiers, Story Bible, continuity report, and narrative architecture.

**Observed supporting detail (from README):**

The Fiction Workshop description includes "Reader Testing" as a stage, alongside Story Bible Building and Chapter Development. The session continuity note and the persona structure indicate that reader testing is designed as a separate, context-isolated pass, not an informed diagnostic that reads the full Story Bible.

### Observed: prose mechanics — diagnose, stop, wait, then apply approved fixes

**ChatGPT-5 Sol independently inspected this at `b7828700`** and reported:

> "Its prose audits explicitly diagnose, stop, wait for author disposition, and only then apply approved fixes (audit contract, `skills/prose-mechanics/SKILL.md` lines 96–120)."

The README confirms the prose-mechanics workflow: "Run audits one at a time, in order. Each pass produces a flagged-issues report for author review." The commit at `b7828700` refined the sentence-variance audit's engine scope: "The engine implements detection pattern #1 only (narrow-band runs, ±3 words) as a fast deterministic pass; patterns #2–5 above (std-dev targets, chapter-scale flatness, mechanical alternation) are for conversational/manuscript application when working without the engine, or as additional judgment on top of the engine's findings."

### Observed: Story Structure workflow

The `story-structure` skill provides four modes:

- **Map** — place beats and signposts for a story not yet drafted.
- **Audit** — locate where beats actually land in an existing manuscript and flag missing, mistimed, or thin ones.

This maps to CodexWriter's narrative-architecture and scene-planning responsibilities, though Rhavekost's model is percentage-anchored (Weiland/Bell) rather than CodexWriter's beat → scene → chapter hierarchy.

### Inference

Rhavekost's workflow has two features that CodexWriter should study closely:

1. **Reader testing as a fresh, context-isolated pass with explicit stopping semantics.** This is the strongest available evidence for context-blind reader simulation among the seven sources.
2. **Prose auditing as diagnose → stop → author disposition → approved repair.** This is the strongest available evidence for separating audit from repair with an explicit author gate.

The workflow is instructional rather than transactional. Claude's persona system enforces some of the separation; CodexWriter would need explicit skill boundaries or agent boundaries to replicate the same discipline across hosts.

### Uncertainty

The pinned commit does not include a separate reader-simulation SKILL.md. The reader-test behavior is embedded in Fiction Workshop's workflow description and confirmed by ChatGPT-5 Sol's line-range inspection. Until the actual Fiction Workshop SKILL.md at `b7828700` is read directly, the exact stopping rules and context-isolation mechanics remain partially observed through second-hand inspection and README description.

---

## 5. State Storage Model

### Observed: Story Bible / blueprint as persistent state

The README states that "All three skills now treat the project's blueprint or Story Bible as persistent state." The "three skills" likely refers to Fiction Workshop, Character Archetypes, and Story Structure (the core fiction skills), with prose-mechanics using a per-project audit tracker separately.

The session continuity pattern is:

- **At session start:** Read the Story Bible / blueprint.
- **During session:** Work within the editorial persona's scope.
- **At session end:** Write a brief note to `sessions/YYYY-MM-DD_topic-slug.md` summarizing what was done, decisions made, and the stopping point. "Two to five sentences is enough."

### Observed: per-project audit tracker for prose mechanics

Prose Mechanics uses "a per-project audit tracker the same way" as the session continuity pattern. This is described in the README but the exact format is not specified in the pinned commit's README.

### Observed: no structured JSON/YAML state model

The pinned commit contains no `_tracking-state.json`, no character-state.json, no timeline.json, no structured state schema. State is Markdown (Story Bible, session notes, audit tracker) rather than structured machine-readable state.

### Inference

Rhavekost's state model is **document-oriented, not schema-driven**. The Story Bible is the source of truth; session notes are the audit log; the prose-mechanics audit tracker is a per-project adjunct. There is no current-character-state artifact, no timeline.json, no promise/payoff schema, no revision counter.

This is closer to Lensetek's artifact-oriented Markdown model than to Dewhurst's typed project contract or Zenstory's single-authoritative-JSON model.

### Uncertainty

The exact format of the prose-mechanics audit tracker and the precise contents of the Story Bible template are not established by the pinned README alone. The Fiction Workshop SKILL.md at the pin would clarify these; it was not directly read for this analysis.

---

## 6. Context Management

### Observed: Story Bible loaded at session start

Fiction Workshop's session continuity note says to read the Story Bible at session start. This is the primary context-loading rule. There is no documented LOD, sharding, context budget, near-field/far-field strategy, or summary-vs-prose conflict rule in the pinned README.

### Observed: reader testing context isolated from Story Bible

The reader test is explicitly designed to run without the Story Bible. This is the context rule that matters most for CodexWriter. ChatGPT-5 Sol's inspection confirms the pattern: "requires a fresh sub-agent without Story Bible context."

### Observed: prose mechanics runs one audit at a time

Prose Mechanics runs one audit at a time, in order, each producing a flagged-issues report. This is a focused-context pattern — each audit has a narrow scope rather than loading the entire project state.

### Inference

Rhavekost's context model is weak in the traditional LOD sense (no sharding, no budget, no near/far rules) but strong in one specific respect: it demonstrates context isolation for the reader-test pass. This is the single most relevant context-management observation for CodexWriter's reader-simulation redesign.

---

## 7. Creative-Craft Model

### Observed: Fiction Workshop personas

The five editorial personas map to familiar craft responsibilities:

- **Developmental Editor** — plot, pacing, structure, stakes.
- **Line Editor** — prose rhythm, word choice, show-don't-tell.
- **Character Consultant** — voice consistency, motivation, arc.
- **Continuity Tracker** — timeline, world facts, internal consistency.
- **Brainstorm Partner** — what-if exploration, problem-solving.

Genre-specific guides are provided for spy thrillers (tradecraft, tension, moral complexity) and hard sci-fi (technical accuracy, worldbuilding, geopolitics).

### Observed: Character Archetypes

Two taxonomies plus four analysis modes:

- **Narrative-Role Archetypes** — Vogler/Campbell's 8 (Hero, Mentor, Threshold Guardian, Herald, Shapeshifter, Shadow, Trickster, Ally).
- **Personality Archetypes** — Jungian 12 (Mark & Pearson model): Innocent, Everyman, Hero, Caregiver, Explorer, Rebel, Lover, Creator, Jester, Sage, Magician, Ruler.
- **Analyzer** — diagnose or recommend an archetype pairing.
- **Audit** — flag stock/cliché use of an established archetype.
- **Conformance** — check for unexplained archetype drift across chapters.
- **Ensemble** — check cast-level archetype balance and gaps.

The README notes: "Archetype is a starting scaffold, not a finished character — pair with Fiction Workshop's Want/Need/Wound/Lie framework to individualize."

### Observed: Story Structure — Weiland + Bell

- **Landmark Beats** — 11-beat skeleton (Hook, Inciting Event, First Plot Point, Pinch Points, Midpoint, Third Plot Point, Climax, Resolution) with percentages and diagnostics.
- **Signposts** — Bell's 14 named checkpoints (Disturbance, Mirror Moment, Doorways of No Return, Q Factor, and more), overlaid on the landmarks or placed relatively between them.
- **Map** — place beats and signposts for a story not yet drafted.
- **Audit** — locate where beats actually land in an existing manuscript and flag missing, mistimed, or thin ones.

"Weiland's beats answer *where* a turning point falls; Bell's signposts answer *what psychological work* it needs to do."

### Observed: Narrative Nonfiction

Four reveal patterns: permission-reframe, empirical, structural, conceptual. Plus transformation arc, metaphor consistency, exercise design, and voice editing.

### Observed: Prose Mechanics — 4 audit types

1. **Active/Passive Audit** — unjustified passive constructions, hidden agency.
2. **Parallel Structure Audit** — broken grammatical parallels in lists, comparisons, series.
3. **Sentence Length Variance** — flat-rhythm detection at the paragraph level.
4. **Accessibility Audit** — readability scoring and structural accessibility (prose, not WCAG).

Run one at a time, in order. Each produces a flagged-issues report for author review.

### Inference

Rhavekost's craft model is strongest at the editorial-persona and genre-guide level. It does not go as deep as wgwtest on epistemic/POV distinctions or as deep as Haowjy on voice preservation and reader cognition. Its craft guidance is practical and persona-structured rather than theoretically elaborated.

The archetype tool is a diagnostic aid, not a character-creation pipeline. The README explicitly warns against treating archetypes as finished characters.

---

## 8. Evaluation and Continuity

### Observed: reader testing as a separate, stopping pass

The Fiction Workshop workflow includes Reader Testing as a distinct stage. The key structural feature is that the reader test:

- Uses a fresh sub-agent without Story Bible context.
- Stops after delivering the reader report.
- Does not loop into revision.

ChatGPT-5 Sol's independent inspection at `b7828700` confirms this: "Its fiction workflow requires a fresh sub-agent without Story Bible context and stops after delivering the reader report."

### Observed: prose mechanics audit contract — diagnose, stop, wait, then apply

The prose-mechanics workflow is:

1. Run one audit at a time, in order.
2. Produce a flagged-issues report for author review.
3. Wait for author disposition.
4. Apply approved fixes.

ChatGPT-5 Sol's inspection confirms: "Its prose audits explicitly diagnose, stop, wait for author disposition, and only then apply approved fixes."

### Observed: finding schema present in the tree

The pinned tree includes `references/finding-schema.json` (902 bytes). This is a structured finding schema — a candidate model for CodexWriter's shared findings/disposition envelope. The contents were not directly read for this analysis; the file's presence is established by the tree API.

### Observed: Continuity Tracker persona

Fiction Workshop includes a Continuity Tracker persona responsible for "timeline, world facts, internal consistency." This is a model-judgment continuity role, not a deterministic validator.

### Inference

Rhavekost provides two evaluation patterns that CodexWriter currently contradicts:

1. **Context-blind reader testing with explicit stopping.** CodexWriter's reader-simulation skill loads Story Bible, outlines, dossiers, continuity report, and architecture — all privileged author context.
2. **Prose audit that stops for author disposition before applying fixes.** CodexWriter's prose-editing skill proceeds from assessment to revision in a single run.

The `finding-schema.json` is a candidate structured finding model. Its presence at the pin is established; its content is not yet read.

### Uncertainty

The exact contents of `finding-schema.json` and the exact stopping rules in the Fiction Workshop SKILL.md were not directly read for this analysis. ChatGPT-5 Sol's line-range quotes are second-hand evidence; they are consistent with the README and the commit but should be verified by direct reading before CodexWriter relies on specific mechanics.

---

## 9. Human-in-the-Loop Model

### Observed: editorial personas as the primary HITL mechanism

Human approval in Rhavekost is primarily mediated through Claude's persona system and the author's choice of which lens to invoke. The Story Bible is the persistent state that carries author intent across sessions.

### Observed: session-end notes as lightweight handoff

At session end, the author writes a 2–5 sentence note to `sessions/YYYY-MM-DD_topic-slug.md` summarizing what was done, decisions made, and the stopping point. This is a lightweight continuity mechanism that does not require a formal gate.

### Observed: prose mechanics requires author review before repair

The prose-mechanics workflow produces a flagged-issues report and waits for author review before applying fixes. This is an explicit HITL gate for prose repair.

### Observed: reader test stops after report

The reader test delivers its report and stops. There is no automatic revision loop.

### Inference

Rhavekost's HITL model is **persona-driven and stage-specific**, not phase-gate-driven like Lensetek's five-gate model. The key HITL features are:

- Author chooses which editorial lens to invoke.
- Story Bible carries author intent across sessions.
- Prose audits stop for author disposition before repair.
- Reader test stops after delivering the report.

This is a softer HITL model than CodexWriter's five-gate pipeline, but it has two specific mechanisms (prose audit gate, reader-test stopping) that CodexWriter currently lacks.

### Uncertainty

The exact author-approval semantics for Story Bible updates, the conditions under which the reader test stops, and the relationship between session notes and the Story Bible are not fully established by the pinned README alone. Direct reading of the Fiction Workshop SKILL.md would clarify these.

---

## 10. Runtime and Maintenance

### Observed: Claude Code plugin only

The pinned commit is a Claude Code plugin. It has no CLI, no cross-host packaging, no install script for Codex/Gemini/OpenCode, and no test suite. The `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` define the plugin metadata.

### Observed: no CI, no tests, no doctor/migration tools

The pinned commit contains no `.github/` directory, no test files, no CLI, and no migration or doctor utilities. The README does not claim CI or test integration.

### Observed: vendored skill with preserved upstream LICENSE

The `avoid-ai-writing` skill is vendored from Conor Bronsdon's MIT-licensed repository, with its upstream LICENSE preserved at `skills/avoid-ai-writing/LICENSE`. This is a better provenance pattern than a bare license claim, but the root LICENSE's reference to ATTRIBUTION.md creates a provenance gap at the pinned commit (ATTRIBUTION.md is 404 at `b7828700`).

### Inference

Rhavekost is a platform-specific Claude Code plugin, not a portable multi-host framework. Its value to CodexWriter is in its behavioral patterns (reader-test isolation, prose-audit stopping, editorial personas, Story Bible continuity), not in its runtime architecture. Any implementation-level borrowing would require a separate Claude Code platform decision.

### Uncertainty

The pinned commit is a snapshot of a moving plugin. The exact skill content at the pin was not fully read for this analysis; some claims rely on README description and ChatGPT-5 Sol's independent inspection. Re-read the actual SKILL.md files at `b7828700` before relying on specific mechanics.

---

## 11. Strengths

### Observed strengths

1. **Reader testing as context-isolated pass with explicit stopping.** This is the strongest available evidence for context-blind reader simulation among the seven sources. ChatGPT-5 Sol's independent inspection confirms the pattern at the pinned commit.

2. **Prose audit contract: diagnose → stop → author disposition → approved repair.** This is the strongest available evidence for separating audit from repair with an explicit author gate. ChatGPT-5 Sol's inspection confirms the pattern at `skills/prose-mechanics/SKILL.md` lines 96–120.

3. **Story Bible as persistent state across sessions.** The session continuity pattern (read Story Bible at start, update when foundations change, write session notes at end) is a practical model for cross-session project memory without a structured state engine.

4. **Editorial persona structure.** Five clearly scoped personas (Developmental Editor, Line Editor, Character Consultant, Continuity Tracker, Brainstorm Partner) provide a usable taxonomy for CodexWriter's evaluation/revision layer.

5. **Archetype tool as diagnostic scaffold, not finished character.** The README explicitly warns against treating archetypes as finished characters and recommends pairing them with the Want/Need/Wound/Lie framework.

6. **Weiland + Bell story structure.** Percentage-anchored landmark beats plus psychological signposts provide a usable structure model. The map/audit mode distinction is a practical workflow pattern.

7. **Vendored skill with preserved upstream LICENSE.** The `avoid-ai-writing` vendored skill has its upstream LICENSE preserved, a better provenance pattern than a bare license claim.

### Inference

Rhavekost is the most operationally specific source for two of CodexWriter's most important gaps: context-blind reader simulation and audit-to-repair stopping. Its strength is in workflow mechanics, not in state architecture or cross-host portability.

---

## 12. Weaknesses / Gaps

### Observed gaps

1. **Platform-specific (Claude Code only).** No CLI, no cross-host packaging, no Codex/Gemini/OpenCode support at the pinned commit. The plugin relies on Claude's persona system for role separation.

2. **No structured state model.** No JSON/YAML state schema, no current-character-state artifact, no timeline.json, no promise/payoff schema, no revision counter. State is document-oriented (Story Bible, session notes, audit tracker).

3. **No deterministic validator.** Continuity Tracker is a model-judgment persona. Prose Mechanics has a lightweight engine for sentence-variance pattern #1 only; the other patterns are manual/conversational.

4. **No CI, no tests, no doctor/migration tools.** The pinned commit contains none of these.

5. **Provenance gap at the pin.** ATTRIBUTION.md is 404 at `b7828700`, though the root LICENSE references it. The relationship between the root LICENSE's reference, the preserved upstream LICENSE, and the later ATTRIBUTION.md is not fully resolved at the pin.

6. **Context management is weak except for reader-test isolation.** No LOD, sharding, budget, near/far rules, or summary-vs-prose conflict rule. The only explicit context rule is: Story Bible loaded at session start, reader test runs without Story Bible.

7. **Reader test and prose-audit mechanics only partially verified.** ChatGPT-5 Sol's line-range quotes are consistent with the README but were not directly verified by reading the actual SKILL.md files at the pinned commit for this analysis.

8. **No cross-host or portability story.** The plugin is Claude Code only; its persona-based separation does not transfer directly to a multi-host framework.

### Inference

Rhavekost is a shallow, platform-specific plugin with two specific workflow strengths. It should not be adopted wholesale as a CodexWriter implementation model. Its reader-test and prose-audit patterns are the valuable parts; its Claude Code dependency, document-only state model, and lack of deterministic tooling are the limitations.

---

## 13. Relevance to CodexWriter

### Observed reusable responsibilities

- **Context-blind reader testing with explicit stopping.** This is the most directly reusable responsibility. It contradicts CodexWriter's current reader-simulation design and should drive a redesign.
- **Prose audit contract: diagnose → stop → author disposition → approved repair.** This is the second most directly reusable responsibility. It contradicts CodexWriter's current prose-editing design.
- **Story Bible as persistent project state across sessions.** A practical model for cross-session memory without a structured state engine.
- **Editorial persona taxonomy.** Five personas (Developmental Editor, Line Editor, Character Consultant, Continuity Tracker, Brainstorm Partner) provide a usable evaluation/revision layer taxonomy.
- **Session notes as lightweight audit log.** The `sessions/YYYY-MM-DD_topic-slug.md` pattern is a lightweight continuity mechanism.
- **Weiland + Bell story structure with map/audit modes.** A usable structure model with a practical workflow distinction.
- **Archetype diagnostic tool.** A usable scaffold for character analysis, with the explicit warning not to treat archetypes as finished characters.

### Candidate architectural borrowing

- **Reader simulation redesign:** context-blind first pass with isolated context, explicit stopping, no automatic revision loop. This is the strongest candidate.
- **Prose editing redesign:** diagnostic pass that stops for author disposition before applying fixes, with a structured finding/report format. This is the second strongest candidate.
- **Session continuity pattern:** Story Bible as persistent state, session-end notes as audit log. Candidate for CodexWriter's cross-session continuity model, though it does not replace a structured state engine.
- **Editorial persona layer:** Five personas as a candidate evaluation/revision layer for CodexWriter's Phase 5.

### Implementation-level borrowing requiring license/provenance handling

- **Vendored `avoid-ai-writing` skill.** MIT-licensed by Conor Bronsdon; upstream LICENSE preserved at `skills/avoid-ai-writing/LICENSE`. Any borrowing would require preserving Conor Bronsdon's copyright and license notice in addition to rhavekost's.
- **`finding-schema.json`.** Present at the pin (902 bytes, not yet read). If used, its contents and license status would need verification.

### Patterns CodexWriter should avoid or treat with caution

- **Claude Code persona dependency.** Rhavekost's role separation relies on Claude's built-in persona system. This does not transfer directly to a multi-host framework like CodexWriter.
- **Document-only state model.** Rhavekost's Story Bible + session notes model is lightweight but does not provide the structured, checkable state that CodexWriter's schemas are designed to support.
- **No deterministic tooling.** Rhavekost does not offer a continuity validator, a state engine, or a test suite. It should not be treated as a source for executable infrastructure.

---

## 14. Detailed Evidence

### Repository tree at pinned commit `b78287003edf52e5f0784ee2b4a00411173358f` (tree SHA `3b826097738bee8adcfdc88ae18d22580cf985c9`)

Confirmed present via GitHub tree API:

| Path | Type | Notes |
|---|---|---|
| `LICENSE` | blob | MIT, copyright 2026 rhavekost |
| `README.md` | blob | Plugin description, session continuity, skill descriptions, installation, usage |
| `ATTRIBUTION.md` | **404 at pin** | Present on `main` but absent at `b7828700` |
| `.claude-plugin/plugin.json` | blob | Claude Code plugin manifest |
| `.claude-plugin/marketplace.json` | blob | Plugin marketplace metadata |
| `skills/fiction-workshop/SKILL.md` | blob | Primary workflow skill |
| `skills/prose-mechanics/SKILL.md` | blob | Diagnostic audit skill |
| `skills/story-structure/SKILL.md` | blob | Weiland/Bell structure skill |
| `skills/character-archetypes/SKILL.md` | blob | Vogler/Campbell + Jungian archetypes |
| `skills/narrative-nonfiction/SKILL.md` | blob | Nonfiction structure skill |
| `skills/avoid-ai-writing/SKILL.md` | blob | Vendored from Conor Bronsdon |
| `skills/avoid-ai-writing/LICENSE` | blob | MIT, copyright 2026 Conor Bronsdon |
| `skills/avoid-ai-writing/CHANGELOG.md` | blob | Vendored skill changelog |
| `skills/avoid-ai-writing/.gitignore` | blob | Vendored skill gitignore |
| `references/finding-schema.json` | blob | Structured finding schema (902 bytes, not yet read) |
| `skills/fiction-workshop/references/` | tree | Reference files for fiction workshop |
| `skills/prose-mechanics/references/cliches-audit.md` | blob | Clichés audit reference; modified at `b7828700` |
| `skills/prose-mechanics/references/sentence-length-variance.md` | blob | Sentence variance reference; modified at `b7828700` |
| `skills/story-structure/references/` | tree | Reference files for story structure |

### Pinned commit diff

Commit `b7828700` has commit message: "docs: drop private-path mention in cliches reference, clarify sentence-variance engine scope"

Files modified (15 additions, 6 deletions):

1. `skills/prose-mechanics/references/cliches-audit.md` — dropped private-path mention; 3 additions, 4 deletions.
2. `skills/prose-mechanics/references/sentence-length-variance.md` — clarified engine scope: "The engine implements detection pattern #1 only (narrow-band runs, ±3 words) as a fast deterministic pass; patterns #2–5 above (std-dev targets, chapter-scale flatness, mechanical alternation) are for conversational/manual application when working without the engine, or as additional judgment on top of the engine's findings. Otherwise apply the detection patterns above by eye." 6 additions, 2 deletions.

### ChatGPT-5 Sol independent inspection (second-hand, to be verified)

From ChatGPT-5 Sol's evaluation at commit `50dee18a`:

- Fiction Workshop: "Its fiction workflow requires a fresh sub-agent without Story Bible context and stops after delivering the reader report (reader-test and stopping rules, `skills/fiction-workshop/SKILL.md` lines 149–214)."
- Prose Mechanics: "Its prose audits explicitly diagnose, stop, wait for author disposition, and only then apply approved fixes (audit contract, `skills/prose-mechanics/SKILL.md` lines 96–120)."

These quotes are consistent with the README's description of the reader-test and prose-mechanics workflows but were not directly verified by reading the actual SKILL.md files at the pinned commit for this analysis. They should be verified before CodexWriter relies on specific mechanics.

### LICENSE at pin

Root LICENSE blob SHA: `a4648fd8e472871ded47e91110a2cf7e23135b5b` — MIT, copyright (c) 2026 rhavekost.

Vendored LICENSE: preserved at `skills/avoid-ai-writing/LICENSE` — MIT, copyright (c) 2026 Conor Bronsdon.

### ATTRIBUTION.md at pin

**404 Not Found** at `b7828700`. The root LICENSE explicitly references ATTRIBUTION.md: "See ATTRIBUTION.md for a list of vendored components and their upstream license files." This creates a provenance gap at the pinned revision.

---

## 15. CodexWriter Disposition

### Retain responsibility

- **Reader testing as a context-isolated pass with explicit stopping.** This is the single most important pattern. It directly contradicts CodexWriter's current reader-simulation design and should drive a redesign.
- **Prose audit contract: diagnose → stop → author disposition → approved repair.** This is the second most important pattern. It directly contradicts CodexWriter's current prose-editing design.
- **Story Bible as persistent project state across sessions.** A practical model for cross-session memory.
- **Session notes as lightweight audit log.** The `sessions/YYYY-MM-DD_topic-slug.md` pattern is a candidate for CodexWriter's cross-session continuity.

### Adapt

- **Editorial persona taxonomy.** The five personas (Developmental Editor, Line Editor, Character Consultant, Continuity Tracker, Brainstorm Partner) are a candidate evaluation/revision layer for CodexWriter's Phase 5. They should be adapted to CodexWriter's SKILL.md boundaries rather than copied as Claude Code personas.
- **Weiland + Bell story structure.** A candidate structure model for narrative-architecture, though it should be adapted to CodexWriter's beat → scene → chapter hierarchy rather than adopted as a percentage-anchored model.

### Merge candidate

- **`finding-schema.json`.** The structured finding schema present at the pin (902 bytes, not yet read) is a candidate model for CodexWriter's shared findings/disposition envelope. Its contents and license status should be verified before use.

### Defer

- **Vendored `avoid-ai-writing` skill.** MIT-licensed but separately attributed to Conor Bronsdon. Defer until CodexWriter's licensing and provenance policy for vendored components is settled.
- **Claude Code persona mechanisms.** Platform-specific; defer until a cross-host separation mechanism is designed.

### Reject

- **Document-only state model as a CodexWriter state design.** Rhavekost's Story Bible + session notes model is lightweight but does not provide the structured, checkable state that CodexWriter's schemas are designed to support. It is a useful cross-session continuity pattern, not a state architecture.

---

## Status

| Order | Source | Status |
|---|---|---|
| 1 | lensetek/Fiction-book-agent-skills | Merged baseline complete |
| 2 | danjdewhurst/story-skills | Merged analysis complete |
| 3 | zenstory-ai/oh-story-claudecode | Merged analysis complete |
| 4 | haowjy/creative-writing-skills | Merged analysis complete |
| 5 | JeroTan/novel-writer-english | Merged analysis complete |
| 6 | wgwtest/novel-writing | Analysis complete; ready for review |
| 7 | rhavekost/author-toolkit | **In progress — pinned at `b78287003edf52e5f0784ee2b4a00411173358f`** |

---

## Next Step

This analysis is a draft pinned at upstream commit `b78287003edf52e5f0784ee2b4a00411173358f`. The two most important findings — context-blind reader testing and prose-audit stopping rules — are confirmed by both the README description and ChatGPT-5 Sol's independent inspection, but the exact mechanics should be verified by direct reading of the Fiction Workshop and Prose Mechanics SKILL.md files at the pinned commit before CodexWriter relies on specific implementation details.

No architecture or crosswalk decision is made in this status update. After review and approval, the next step is the seven-source synthesis and state-architecture decision.
