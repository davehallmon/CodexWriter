# Seven-Source Synthesis — CodexWriter Architecture Review

**Date:** 2026-08-27  
**Branch:** `architecture/seven-source-synthesis`  
**Branch-point SHA:** `0e999a9392683878a8cca9b1760cf92c81176c85`  
**Status:** Draft — awaiting Dave's ratification  
**Decision status:** Every conclusion in this document is provisional. Nothing here modifies `ARCHITECTURE.md`, `docs/crosswalk.md`, schemas, skills, templates, README, or the build report. The synthesis weighs evidence from all seven source analyses and existing CodexWriter artifacts to recommend an architecture direction. It does not ratify that direction.

---

## 1. Executive Thesis

The seven sources collectively support a **layered, specialist-routed fiction-authoring system** in which three architectural commitments reinforce each other: (1) distinct cognitive roles with bounded responsibilities, (2) persistent story state that is both human-readable and machine-checkable, and (3) deterministic validation layered beneath judgment-based creative work. No single source delivers all three; each solves a different layer of the same problem.

The strongest synthesis signal is this: **Markdown/document-first sources (Dewhurst, JeroTan, wgwtest) and JSON/structured-state sources (Zenstory) are not incompatible.** They represent different answers to the same question — how to make story state persistent, checkable, and portable — and a hybrid model can adopt the process discipline of the document-first sources while retaining the mechanical rigor of structured state. The current CodexWriter prototype already leans in this direction: 11 SKILL.md files define specialist roles and creative workflows (Lensetek-class breadth, Dewhurst-class grounding), while 4 JSON schemas and a Zenstory-influenced state model provide the structured layer. What is missing is the explicit authority rule that reconciles the two, the transaction/update discipline that prevents state rot, and the context assembly layer that makes the whole system scalable.

The synthesis does **not** recommend adopting any source wholesale. It recommends extracting patterns: specialist role taxonomy from Lensetek, Markdown/YAML state discipline and deterministic continuity from Dewhurst, cognitive-role separation and Muse-like coordination from Haowjy, constitution and pre-write context reload from JeroTan, narrative epistemology and LOD context from wgwtest, context-blind reader testing and editorial stopping rules from Rhavekost, and transaction semantics and stale-revision protection from Zenstory. The resulting architecture is a mosaic, not a copy.

---

## 2. Seven-Source Contribution Matrix

### 2.1 Lensetek/Fiction-book-agent-skills

**Pinned evidence:** `docs/source-analysis/lensetek.md`; upstream `main` at analysis time; 16 skills, version 1.4.0; MIT badge/link but LICENSE 404.

**Distinctive contribution:** The broadest specialist-role taxonomy among the seven sources — 16 roles covering orchestration, concept intake, market research, worldbuilding, character psychology, plot architecture, scene planning, novel drafting, comic/webtoon scripting, children's storytelling, accessibility/Braille, continuity auditing, prose polishing, beta-reader simulation, publishing/export, and update/security maintenance. Its five-phase orchestrator with human gates (Concept → World/Character → Plot/Scenes → Draft/Edit → Continuity/Beta/Export) is the clearest end-to-end workflow map in the set.

**Overlapping contributions:** Five-phase pipeline with phase gates (overlaps with CodexWriter's current architecture, Dewhurst's workflow, and Haowjy's Muse→Writer→diagnostic→Writer loop). Specialist role decomposition (overlaps with all sources). Named output artifacts per skill (overlaps with Dewhurst's registry pattern and JeroTan's file-oriented design).

**Limitations:** Shallow implementation depth relative to taxonomy breadth. No demonstrated dynamic current-state system. No explicit context-loading discipline. Continuity helper (temporal marker extraction) does not perform the validation its documentation implies. No authority/conflict rule between manuscript and planning artifacts. No old-chapter revision propagation protocol. No structured author-preference memory. Orchestrator coverage incomplete — market research, accessibility, and maintenance exist in the taxonomy but are not cleanly routed through the five-phase workflow. HITL checklist phase grouping does not perfectly match the orchestrator's gates.

**Licensing constraints:** Root LICENSE returns 404. GitHub metadata reports `license: null`. Intent appears to be MIT, but the intended license and an actually granted license should not be treated as identical while the referenced license text is missing. CodexWriter should not publicly redistribute a translated or substantially copied derivative pending license clarification.

**Proposed CodexWriter disposition:** Retain as the initial responsibility taxonomy and workflow map, not as the implementation model. Use the 16-role list as a comparison coordinate for asking which responsibilities should be core, extensions, or replaced by stronger implementations. Do not copy implementation text. Treat as a requirements inventory.

### 2.2 danjdewhurst/story-skills

**Pinned evidence:** `docs/source-analysis/danjdewhurst-story-skills.md`; upstream `main` at analysis time; 7 core skills, version 0.3.1; MIT license; JavaScript/Node/Bun CLI.

**Distinctive contribution:** A shared Markdown/YAML fiction project format with a deterministic maintenance CLI. Its state architecture is distributed across plain Markdown files with structured YAML frontmatter — `story.md` as the top-level bible, `characters/*.md`, `worldbuilding/{locations,systems,factions,artifacts}/*.md`, `plot/arcs/*.md`, `plot/timeline.md`, `scenes/_index.md`, `continuity/state.md` with current character/object/knowledge state, `continuity/questions/` and `continuity/promises/` as individual files, and `glossary/`. The CLI validates the mechanical contract (cross-reference checks, state-contract checks, conflict warnings), while agents retain creative judgment. Explicit pre-write context reload contracts (read story.md, chapter index, plot index, timeline, scene index, continuity state, open questions, promises/payoffs, previous chapter, active arcs, POV character file, location files). Explicit revision propagation instructions. Two HITL operating modes: interactive outline approval before drafting, and automated drafting with approval shifted to the PR boundary.

**Overlapping contributions:** Markdown-first state with structured frontmatter (overlaps with JeroTan's file-oriented design and CodexWriter's current Markdown skill files). Deterministic continuity validation (overlaps with CodexWriter's continuity goal and Zenstory's validation layer). Explicit context reloading (overlaps with JeroTan's pre-write context and wgwtest's LOD policy). Revision propagation awareness (overlaps with Zenstory's derived-view concern).

**Limitations:** No single creative orchestrator skill — routing occurs through skill descriptions, project state, and CLI actions. No transactional state model — workflow-driven propagation rather than derived replay. No stale-write prevention or concurrency lock. No separate persistent author-preference memory. `_index.md` files are called authoritative but also rebuilt from entity files — an authority nuance. The full-file reload pattern may not scale to long novels without additional context selection. Creative craft model is intentionally limited — delegates stronger prose quality to the external `forjd/better-writing` skill.

**Licensing constraints:** MIT license, clear and present. Implementation-level reuse is permitted subject to preservation of copyright and license notice. If CodexWriter copies or substantially adapts Dewhurst implementation text/code, record the specific source file and preserve required MIT attribution.

**Proposed CodexWriter disposition:** Strongest evidence that persistent fiction state can remain Markdown-first and distributed while supporting deterministic validation. Treat as a serious alternative to the single-authoritative-JSON hypothesis, not merely as a continuity checker. Adopt the explicit context reload contract pattern. Adopt the `_index.md` registry concept with clarified authority rules. Adopt the two-mode HITL pattern (interactive approval vs. PR-boundary review).

### 2.3 haowjy/creative-writing-skills

**Pinned evidence:** `docs/source-analysis/haowjy-creative-writing-skills.md`; upstream `main` at `fd7a3ad`; version 0.5.9; Apache 2.0 license; Mars/Meridian runtime with 11 canonical skills and 11 agent definitions.

**Distinctive contribution:** Deliberate cognitive-role separation — Muse (coordination, intent interpretation, staffing, author-facing verdict), Writer (prose production, all production modes owned by one worker to reduce voice drift), Critic (focused critique), Editor (holistic editing), Reader-Sim (experiential reading), Continuity-Checker, Brainstormer, Outliner, Style-Creator, Web-Researcher. The core draft loop is Muse → Writer → one or more diagnostic roles → Writer. Production vs. diagnosis boundary is explicit: diagnostic roles are read-only in their agent profiles. Durable knowledge base (`kb/`) vs. working material (`work/`). Thin agent bodies (role contracts) + rich skill/method resources. Multi-agent isolation when available; cognitive stance switching in one conversation when subagents are unavailable.

**Overlapping contributions:** Specialist role decomposition with clear boundaries (overlaps with Lensetek and CodexWriter). Writer/critic/editor separation (partially reflected in CodexWriter's prose-editing vs. reader-simulation distinction). Voice preservation concern (overlaps with CodexWriter's voice guidance in scene-writing and prose-editing). Durable knowledge vs. working material distinction (overlaps with Dewhurst's static vs. dynamic state distinction).

**Limitations:** Pre-1.0 version. Repository structure and CI do not establish literary quality, long-project reliability, or user adoption. Some effective Mars behavior comes from the moving `meridian-base` dependency — the pinned application commit alone does not identify every runtime component. README inventory drift makes component counts discoverable from source but less clear to users. Flattened `cw/` distribution includes dependency-provided components whose exact upstream lineage is not fully traceable from the pinned tree. No controlled evaluation demonstrating the benefit of separate process contexts. One production writer improves voice continuity — a design rationale, not a measured result.

**Licensing constraints:** Apache 2.0 license, clear and present. Sufficient for architectural comparison. Any implementation-level copying into CodexWriter would require a separate Apache compliance and provenance review. Substantial prompt, script, or adapter borrowing should remain blocked on file-level provenance review.

**Proposed CodexWriter disposition:** Adopt the cognitive-role separation principle, especially the production vs. diagnosis boundary and the Muse-like coordination role. Adopt the durable knowledge vs. working material distinction. Adopt the thin-agent/rich-skill pattern as a portability consideration. Do not adopt the Mars/Meridian runtime dependency. Treat Haowjy's coordination model as a candidate for the orchestrator's author-facing behavior, not as a runtime requirement.

### 2.4 JeroTan/novel-writer-english

**Pinned evidence:** `docs/source-analysis/jero-tan-novel-writer-english.md`; upstream `main` at `6d836f2`; version 1.5.1; MIT license (translated/re-architected derivative from wordflowlab); JavaScript/Node.js; 86 non-`.old/` blobs including 29 command prompts, 26 SKILL.md files, 13 templates; `npm test` passes 11 tests.

**Distinctive contribution:** A structured eight-step writing workflow — Constitution → Specify → Clarify → Plan → Tasks → Write → Edit → Review — that explicitly separates author-facing constitution and clarification stages from drafting. Anti-god-file sharding contracts: large documents are split into manageable pieces with cross-reference discipline. A tightly gated chapter editor: outline approval before prose, exact-text editing gate. Typed-but-partly prompt-maintained tracking files. Tested, source-locating, read-only access to a subset of story data via MCP. Multi-platform delivery: Claude Code, Gemini CLI, OpenCode, Codex CLI, and manual copy/paste.

**Overlapping contributions:** Phase gates with explicit approval (overlaps with Lensetek, Dewhurst, and CodexWriter). Document sharding (overlaps with wgwtest's LOD and Dewhurst's registry pattern). Pre-write context reload (overlaps with Dewhurst). Specialist role decomposition (overlaps with all sources). Constitution concept (overlaps with CodexWriter's story-bible concept and Haowjy's Muse intent interpretation).

**Limitations:** Prompt-heavy — most creative operations remain prompt contracts executed by the selected assistant; JavaScript supplies installation, format parsing, chapter discovery, search, and MCP transport rather than an autonomous multi-agent story engine. No dynamic current-state system. No deterministic continuity validation beyond format checks. No transactional state model. No structured author-preference memory. Translation/derivative lineage requires separate provenance attention.

**Licensing constraints:** MIT license, clear and present. Translated/re-architected derivative from wordflowlab — the lineage reference pin (`wordflowlab/novel-writer-skills@5bc9b373`) should be tracked separately. Implementation-level reuse is permitted subject to preservation of copyright and license notice.

**Proposed CodexWriter disposition:** Adopt the constitution → specification → clarification sequence as a Phase 1 refinement. Adopt the anti-god-file sharding discipline. Adopt the exact-text editor gate as a prose-editing constraint. Adopt the read-only MCP lookup pattern as a portability consideration for context access. Treat JeroTan as strong evidence for workflow grounding and document discipline, not as the state-architecture model.

### 2.5 wgwtest/novel-writing

**Pinned evidence:** `docs/source-analysis/wgwtest-novel-writing.md`; upstream `main` at `b6382cf`; MIT license; single Codex fiction skill with ten Markdown references, one Python manuscript checker; `python -m unittest` passes 20 tests.

**Distinctive contribution:** An explicit separation among three knowledge layers: author truth (what actually happened in the story world), character knowledge (what a specific character knows at a specific point), and reveal boundary (what the reader is allowed to know at a specific point). A two-axis cognition model distinguishing what the model knows from what the character knows. Causal role separation among viewpoint, decision, expertise, and execution. Level-of-detail context policy with a prose-over-summary conflict rule (prose beats summary when they conflict within the current task's scope). Behavior-focused dialogue guidance that rejects mechanical gesture insertion. Explicit delegation of persistent project state to a separate `novel-project-strategy` responsibility — this package stays focused on narrative work and adjacent-prose continuity.

**Overlapping contributions:** POV boundaries and knowledge constraints (overlaps with CodexWriter's knows/doesn't-know lists and continuity knowledge checks). Context LOD policy (overlaps with Dewhurst's context reload and JeroTan's sharding). Deterministic checker pattern (overlaps with Dewhurst's CLI and CodexWriter's continuity goal). Narrative epistemology (overlaps with CodexWriter's epistemic verb discipline and Dust & Ash's evidence-before-inference requirement).

**Limitations:** Single skill — not a novel workspace, persistent story-state service, multi-agent system, or full editing transaction engine. No persistent state of its own; explicitly delegates project-state responsibility elsewhere. No dynamic current-state system. No transactional model. No author memory. No specialist role decomposition beyond the single skill.

**Licensing constraints:** MIT license, clear and present. Implementation-level reuse is permitted subject to preservation of copyright and license notice. No copying has occurred — CodexWriter's epistemic vocabulary and LOD policy are independent syntheses informed by wgwtest's patterns.

**Proposed CodexWriter disposition:** Adopt the three-layer knowledge model (author truth / character knowledge / reveal boundary) as a core architectural concept, especially for continuity knowledge checks and reader simulation design. Adopt the prose-over-summary conflict rule as a context-management principle. Adopt the causal role separation as a drafting discipline. Treat wgwtest as the strongest single source for narrative epistemology and context LOD, and as evidence that a focused single-skill approach can deliver deep craft reasoning without a full workspace.

### 2.6 rhavekost/author-toolkit

**Pinned evidence:** `docs/source-analysis/rhavekost-author-toolkit.md`; pinned commit `b78287003edf52e5f0784ee2b4a004111173358f` (2026-07-14); MIT license with separately attributed vendored material; 6 top-level skills (fiction-workshop, character-archetypes, story-structure, narrative-nonfiction, prose-mechanics, vendored avoid-ai-writing); 79 tracked files; Claude Code only; no code runtime.

**Distinctive contribution:** Context-blind reader testing as a designed pattern: a fresh agent instance with minimal context, the manuscript alone, no author context, and an optional informed diagnostic pass afterward. Separate editorial passes with distinct stopping points: continuity audit first, then prose editing, then macro/structural review, then line editing — each with its own scope and stopping rule. A prose-mechanics audit contract that separates diagnostic findings from repair decisions. Emphasis on stopping points and author approval gates between passes.

**Overlapping contributions:** Phase gates with explicit approval (overlaps with all sources). Separate editorial passes (overlaps with CodexWriter's continuity → prose-editing → reader-simulation sequence and Haowjy's production vs. diagnosis boundary). Reader simulation as a distinct phase (overlaps with Lensetek's beta-reader simulator and CodexWriter's reader-simulation skill). Diagnostic-to-repair separation (overlaps with Dewhurst's mechanical vs. creative boundary and Haowjy's read-only diagnostic roles).

**Limitations (from CodexWriter's own inspection):** Claude Code only — no cross-host support, no CLI tool. No code runtime — all skills are Markdown prompting patterns. No dynamic current-state system. No transactional model. No context assembly layer. No author memory. The full tree (79 files) was inventoried but not all files were individually inspected — Section 11 of the Rhavekost analysis records consequential exclusions, including unread prose-mechanics exemplars and unverified avoid-ai-writing claims. The `avoid-ai-writing/SKILL.md` compatibility claims are the vendored skill's own claims, not the toolkit's.

**Licensing constraints:** MIT license for the toolkit itself. Vendored `avoid-ai-writing` material retains its own license — any borrowing from vendored material must follow that component's license. ATTRIBUTION.md documents the vendored material and its upstream commit.

**Proposed CodexWriter disposition:** Adopt context-blind reader testing as a required pattern for the reader-simulation skill — a first pass with the manuscript only, isolated context, and an optional informed diagnostic pass afterward. Adopt separate editorial passes with distinct stopping rules. Adopt the diagnostic-to-repair approval flow. Do not adopt the Claude Code-only runtime constraint. Treat the unread portions of the Rhavekost tree as unresolved evidence — see Section 10.

### 2.7 zenstory-ai/oh-story-claudecode

**Pinned evidence:** `docs/source-analysis/zenstory-ai.md`; pinned commit `d1f88587c0b88abdb0a62b101b850300e0617d7b`; version 0.7.6; MIT license; 13 top-level skills, 7 specialist agent templates; JavaScript/Python/shell/JSON/TOML adapters; 6,063 stars, 898 forks at analysis time; multi-environment configuration for Claude Code, OpenCode, ZCode, Codex CLI, OpenClaw, Reasonix, and generic file-reading agents.

**Distinctive contribution:** A layered state management architecture with a transaction protocol: patch → validate → apply → publish. Stale-revision protection — attempts to update from an outdated baseline are rejected rather than silently overwriting concurrent changes. Atomic commits at the state level. Derived views — the same underlying state can produce different presentations for different consumers. Cross-field consistency checks that go beyond single-artifact validation. Author memory as a separate, persistent layer. Runtime portability across materially different capability levels — from full agentic environments to generic file-reading agents — with explicit capability detection and fallback patterns. A large regression suite and explicit upgrade procedures.

**Overlapping contributions:** Layered state model (overlaps with CodexWriter's current schema design, which was influenced by Zenstory). Revision counters (overlaps with CodexWriter's state_revision, scene_revision, continuity_revision). Structured checks (overlaps with CodexWriter's continuity checks array and Dewhurst's CLI validation). Author-facing gates (overlaps with all sources). Specialist role decomposition (overlaps with Lensetek and CodexWriter).

**Limitations:** Complexity — the layered state model with transaction semantics is more elaborate than the other sources. The `meridian-base` dependency is moving — some effective behavior comes from a dependency, not the pinned application commit. Prerequisite material may be needed to fully understand the state model. Repository activity is high and recent — architectural conclusions are a point-in-time reading, not a stable description of a slow-moving system.

**Licensing constraints:** MIT license, clear and present. Implementation-level reuse is permitted subject to preservation of copyright and license notice.

**Proposed CodexWriter disposition:** Adopt transaction semantics (patch → validate → apply → publish) as the update discipline for structured state. Adopt stale-revision protection as a concurrency-safety mechanism. Adopt derived views as a pattern for separating machine-readable state from human-readable expressions. Adopt author memory as a separate persistent layer. Adopt runtime portability as a design requirement, not an afterthought. Treat Zenstory as the strongest single source for state-architecture mechanics, and as evidence that structured state can be made portable across hosts with explicit capability detection.

---

## 3. Core-Principle Crosswalk

Evaluate the six README principles against all seven sources and the current CodexWriter build.

### Principle 1: Specialist agents over monolithic prompts

| Source | Disposition |
|--------|------------|
| Lensetek | **Strong positive.** 16-role taxonomy is the clearest expression of this principle in the set. |
| Dewhurst | **Positive.** 7 specialist skills with clear boundaries, though no single orchestrator. |
| Haowjy | **Strong positive.** Muse/Writer/Critic/Editor/Reader-Sim/Continuity-Checker separation with explicit production vs. diagnosis boundary. |
| JeroTan | **Positive.** 26 SKILL.md files with distinct command prompts, though many are workflow steps rather than independent cognitive specialists. |
| wgwtest | **Neutral.** Single skill with deep craft reasoning — demonstrates that a focused single-skill approach can deliver depth, but does not argue for specialist decomposition. |
| Rhavekost | **Positive.** 6 skills with distinct purposes (fiction-workshop, character-archetypes, story-structure, narrative-nonfiction, prose-mechanics, avoid-ai-writing). |
| Zenstory | **Positive.** 13 skills and 7 specialist agent templates with distinct responsibilities. |
| CodexWriter current | **Strongly reflected.** 11 SKILL.md files plus orchestrator, with clear boundaries. This is the principle most visibly realized in the current build. |

**Crosswalk finding:** All seven sources support specialist decomposition to some degree. Lensetek, Haowjy, and Zenstory offer the strongest role taxonomies. wgwtest is the counterexample that proves the rule: depth does not require breadth, but breadth does require clear boundaries. CodexWriter's current 11-skill taxonomy is well-supported by the evidence.

### Principle 2: Persistent, checkable story state

| Source | Disposition |
|--------|------------|
| Lensetek | **Weak.** Static planning artifacts exist, but no demonstrated dynamic current-state system. No per-chapter current-state registry. No revision model. |
| Dewhurst | **Strong positive.** Distributed Markdown/YAML state with current character/object/knowledge state, scene-level state changes, questions, promises, timeline, and registry indexes. Explicit post-draft and revision propagation. |
| Haowjy | **Moderate.** Durable knowledge base (`kb/`) vs. working material (`work/`), but no dynamic current-state system and no transactional model. |
| JeroTan | **Weak-to-moderate.** File-oriented design with tracking files, but no dynamic current-state system and no deterministic continuity validation. |
| wgwtest | **Weak.** Explicitly delegates persistent project state to a separate responsibility. No state of its own. |
| Rhavekost | **Weak.** No dynamic current-state system. No transactional model. |
| Zenstory | **Strong positive.** Layered state management, revision counters, transaction protocol, stale-revision protection, derived views, cross-field consistency, author memory. |
| CodexWriter current | **Moderate.** 4 JSON schemas define state categories and revision counters. The model is structurally sound but operationalized only as schemas — no validator, no instance management, no transaction discipline. The model is provisional (F1 decision). |

**Crosswalk finding:** This is the principle with the widest dispersion. Dewhurst and Zenstory represent two viable answers — Markdown-first distributed state and JSON-structured state with transactions. The others either lack dynamic state or delegate it elsewhere. CodexWriter's current JSON prototype is a plausible structured-state answer, but it adopted Zenstory's influence before all seven sources were analyzed (F1 violation), and it has not yet been tested against Dewhurst's Markdown-first alternative. The synthesis must weigh both.

### Principle 3: Deterministic continuity validation

| Source | Disposition |
|--------|------------|
| Lensetek | **Weak.** Continuity checker produces findings and suggestions; helper script extracts temporal markers but does not calculate temporal ordering, character ages, elapsed time, contradictory dates, or state transitions. Documentation implies more than the helper delivers. |
| Dewhurst | **Strong positive.** Executable continuity engine (`src/continuity.js`) performs deterministic checks: deceased character appearances, POV cast membership, scene cast vs. chapter cast mismatches, location mismatches, chapter numbering gaps, promise payoff before planting, invalid promise status/chapter combinations. CLI validates mechanical contract. |
| Haowjy | **Moderate.** Dedicated continuity-checker role, but no evidence of deterministic executable validation — the role is described as a diagnostic stance, not a mechanical validator. |
| JeroTan | **Weak.** Format checks and tracking-file validation, but no deterministic continuity validation against story state. |
| wgwtest | **Moderate.** Python manuscript checker with 20 tests, but the checker is a hygiene sidecar — manuscript format and adjacent-prose continuity — not a full state-consistency validator. |
| Rhavekost | **Weak.** No code runtime. All skills are Markdown prompting patterns. Continuity is a prompted audit, not a deterministic check. |
| Zenstory | **Strong positive.** Cross-field consistency checks, validation before apply, stale-revision rejection. The validation layer is integrated into the transaction protocol. |
| CodexWriter current | **Weak-to-moderate.** Continuity skill describes checks that the orchestrator calls "mechanical" but that require model judgment — voice consistency, "reasonable" emotional progression, pressure-system consistency, payoff timing. No executable validator. No test harness. No schema validation implementation. This is the single largest operational gap (alignment evaluation finding). |

**Crosswalk finding:** Dewhurst and Zenstory are the only sources with genuine deterministic continuity validation. Dewhurst's is Markdown/YAML-oriented and CLI-driven; Zenstory's is integrated into a transaction protocol. Lensetek's continuity helper does not deliver what its documentation implies. CodexWriter's continuity skill is currently judgment-based, not deterministic — the alignment evaluation flagged this as the single largest operational gap. The synthesis should recommend a Dewhurst-style executable validator for mechanically checkable categories (cast membership, location consistency, promise timing, chapter numbering) and acknowledge that judgment-based categories (voice consistency, emotional progression, pressure-system consistency) cannot be fully deterministic.

### Principle 4: Context management by design

| Source | Disposition |
|--------|------------|
| Lensetek | **Weak.** Skills name output artifacts that downstream agents can conceptually consume, but no systematic pre-task reload contract, no sharding, no LOD, no context budget, no near/far strategy. Context selection is left to the host agent. |
| Dewhurst | **Strong positive.** Explicit chapter pre-write context contract: read story.md, chapter index, plot index, timeline, scene index, continuity state, open questions, promises/payoffs, previous chapter, active arcs, POV character file, location files. Revision context is targeted. The contract specifies what to reload and when. Limitation: full-file reload pattern may not scale to long novels without additional context selection. |
| Haowjy | **Moderate.** Multi-agent isolation when available; scoped files; cognitive stance switching. Context discipline is process-oriented rather than explicit reload contracts. |
| JeroTan | **Strong positive.** Anti-god-file sharding contracts. Pre-write context reload. Document-oriented LOD through file splitting. Read-only MCP lookup for targeted access to a subset of story data. |
| wgwtest | **Strong positive.** Explicit LOD context policy with a prose-over-summary conflict rule. Two-axis cognition model. Causal role separation. The LOD policy is the most articulated context strategy in the set. |
| Rhavekost | **Weak.** No context assembly layer. No LOD strategy. No context budget. |
| Zenstory | **Moderate.** Runtime portability across materially different capability levels implies context adaptation, but the source does not articulate a general LOD or context budget strategy for creative work. |
| CodexWriter current | **Weak.** Skills list inputs but do not define how much to load, how to narrow, or what to exclude. No context assembler, no LOD strategy, no context budget, no near/far policy, no index. This is the largest scalability gap (alignment evaluation finding). |

**Crosswalk finding:** Dewhurst, JeroTan, and wgwtest each offer distinct context-management evidence. Dewhurst provides explicit reload contracts. JeroTan provides sharding discipline and targeted lookup. wgwtest provides the most articulated LOD policy with a prose-over-summary conflict rule. CodexWriter currently has none of these — skills list inputs but do not define how much to load. The synthesis should recommend adopting all three patterns: Dewhurst-style reload contracts, JeroTan-style sharding, and wgwtest-style LOD with the prose-over-summary rule.

### Principle 5: Human-in-the-loop gates

| Source | Disposition |
|--------|------------|
| Lensetek | **Strong positive.** Five phase gates with human approval. HITL checklist expands approval items. Limitation: HITL checklist phase grouping does not perfectly match the orchestrator's gates. Approval semantics are checklist-oriented rather than transaction/scope-oriented. |
| Dewhurst | **Strong positive.** Interactive chapter-writing requires outline approval before prose. Optional automated mode with approval shifted to PR boundary. Two HITL operating modes are explicitly documented. |
| Haowjy | **Moderate.** Author-facing Muse interprets intent and owns the verdict, but the source does not articulate formal phase gates. The process is more continuous than gated. |
| JeroTan | **Strong positive.** Constitution → Specify → Clarify → Plan → Tasks → Write → Edit → Review workflow with explicit gates. Tightly gated chapter editor: outline approval before prose, exact-text editing gate. |
| wgwtest | **Weak.** No formal phase gates. The source is a single skill focused on narrative reasoning, not a workflow with approval points. |
| Rhavekost | **Strong positive.** Stopping points and author approval gates between editorial passes. Diagnostic-to-repair approval flow. |
| Zenstory | **Moderate.** Author-facing gates exist but are integrated into the state-transaction model rather than articulated as a standalone workflow concept. |
| CodexWriter current | **Strongly reflected.** Five phase gates (Gates 1–5) with explicit approval protocol. This is well-supported by the evidence. The synthesis should recommend adopting Dewhurst's two-mode HITL pattern (interactive approval vs. PR-boundary review) and JeroTan's exact-text editor gate. |

**Crosswalk finding:** Lensetek, Dewhurst, JeroTan, and Rhavekost all support human-in-the-loop gates, but with different granularities and operating modes. Lensetek and JeroTan provide the clearest phase-gate structures. Dewhurst provides the valuable two-mode distinction (interactive vs. automated-with-PR-review). Rhavekost provides stopping rules between editorial passes. CodexWriter's current five-gate structure is well-supported. The synthesis should recommend enriching it with Dewhurst's two-mode pattern and JeroTan's editor gate.

### Principle 6: Modular and version-controlled

| Source | Disposition |
|--------|------------|
| Lensetek | **Moderate.** 16 skills in separate directories, but no observed CI/test harness. Plugin.json and mcp_config.json provide some packaging structure. Version 1.4.0 declared. |
| Dewhurst | **Strong positive.** Each skill in its own directory with SKILL.md. JavaScript CLI with CI (`.github/workflows/ci.yml` runs metadata checks, tests, coverage/fallback checks, example validation, Node fallback-CLI smoke check). Version 0.3.1. Tests exist and pass. Migration tooling (`story migrate`). |
| Haowjy | **Strong positive.** Skills and agents in separate directories. CI validates package/plugin structure and builds skill archives. Version 0.5.9. Packaging discipline is evident, though the `cw/` distribution includes dependency-provided components with imperfect lineage. |
| JeroTan | **Strong positive.** 26 SKILL.md files, 13 templates, installer, MCP server, package, docs, attribution, license, tests. `npm test` passes 11 tests. Version 1.5.1. Archived `.old/v1/` tree provides provenance history. |
| wgwtest | **Moderate.** Single skill package with ten references and one checker. `python -m unittest` passes 20 tests. Version not clearly declared in the same way as the others. |
| Rhavekost | **Weak.** No code runtime. No CI. No tests. Plugin.json and marketplace.json provide packaging structure but no executable verification. |
| Zenstory | **Strong positive.** 13 skills, 7 agent templates, large regression suite, explicit upgrade procedures, generated-adapter parity checks, rapid release history (0.7.6). Version and release discipline are evident. |
| CodexWriter current | **Moderate.** 11 SKILL.md files in separate directories. 4 JSON schemas. 4 templates. No tests. No CI. No validator. `tests/` directory exists but is empty. This is a documented gap (task A17). |

**Crosswalk finding:** Dewhurst, Haowjy, JeroTan, and Zenstory each demonstrate modular, version-controlled systems with varying degrees of executable verification. Dewhurst and JeroTan have passing test suites. Zenstory has a large regression suite. Lensetek and Rhavekost lack observable CI/tests. CodexWriter currently has no tests or CI — this is a documented gap that the alignment evaluation raised to High priority (tasks A4–A6 + A17). The synthesis should recommend adopting Dewhurst's and JeroTan's test patterns as the minimum viable test baseline.

---

## 4. Convergence and Conflict Analysis

### 4.1 Where the sources agree

**Specialist role decomposition is broadly endorsed.** All seven sources support dividing fiction-authoring work into distinct roles with bounded responsibilities. The disagreement is about granularity (Lensetek's 16 roles vs. wgwtest's single skill) and about whether coordination is a separate role (Lensetek's orchestrator, Haowjy's Muse, Zenstory's control plane) or emergent from skill descriptions (Dewhurst's routing through project state and CLI actions).

**Human approval at phase transitions is broadly endorsed.** Lensetek, Dewhurst, JeroTan, Rhavekost, and Zenstory all include explicit human approval points. The disagreement is about granularity (phase-level gates vs. scene-level editor gates vs. pass-level stopping rules) and about operating mode (interactive approval vs. automated drafting with PR-boundary review).

**Persistent state is recognized as necessary, but the form is contested.** Dewhurst and Zenstory offer the most complete state architectures. The others either lack dynamic state, delegate it elsewhere, or treat it as a future concern. Even the sources that lack dynamic state recognize that questions, promises, timeline, and character knowledge need durable tracking.

**Deterministic validation is valued where possible, but its scope is contested.** Dewhurst and Zenstory provide executable validation. Lensetek intends more validation than its helper delivers. Haowjy, JeroTan, wgwtest, and Rhavekost treat validation as prompted judgment rather than executable checks. The question is not whether validation should exist, but which categories are mechanically checkable and which require model judgment.

### 4.2 Where the sources contradict

**Markdown-first vs. structured-state-first.** This is the deepest architectural disagreement in the set. Dewhurst and JeroTan argue that Markdown with structured frontmatter is sufficient for persistent state, with a CLI or tooling layer for validation. Zenstory argues for a layered JSON state model with transaction semantics. Lensetek, Haowjy, wgwtest, and Rhavekost are largely silent on the question or delegate it elsewhere. CodexWriter's current prototype leans JSON/structured (4 schemas, Zenstory-influenced), but the F1 decision explicitly says this is provisional and not ratified. The conflict is real: if Dewhurst's Markdown-first model is sufficient, CodexWriter's JSON schemas may be premature complexity. If Zenstory's structured model is necessary, Dewhurst's Markdown-only approach may not scale to the continuity and revision-propagation requirements.

**Process discipline vs. state-machine enforcement.** Haowjy and JeroTan argue that process discipline (Muse coordination, cognitive stance separation, editorial gates, exact-text editor gate) reduces errors. Zenstory argues that transaction semantics (patch → validate → apply → publish, stale-revision rejection) reduce errors. These are not mutually exclusive — process discipline and state-machine enforcement can complement each other — but they represent different answers to the same question: how do you prevent contamination, voice drift, and state inconsistency? The sources that emphasize process (Haowjy, JeroTan, Rhavekost) tend to lack transactional state. The source that emphasizes state transactions (Zenstory) tends to have less articulated process discipline. CodexWriter currently has neither fully realized.

**Context-blind vs. context-loaded reader testing.** Rhavekost explicitly argues for context-blind reader testing: a fresh agent with minimal context, the manuscript alone, no author context, with an optional informed diagnostic pass afterward. CodexWriter's current reader-simulation skill loads the revised manuscript, scene outlines, character dossiers, story bible, continuity report, and narrative architecture — all privileged author context. The alignment evaluation flagged this contradiction: the current design contradicts the best practice found in Rhavekost. This is not a theoretical disagreement; it is a documented contradiction between CodexWriter's built system and one of its seven source analyses.

**Depth vs. breadth of specialist roles.** Lensetek offers 16 roles with shallow implementation depth. wgwtest offers 1 skill with deep craft reasoning. Dewhurst offers 7 roles with operationalized state and continuity. Haowjy offers 11 roles with cognitive separation. JeroTan offers 26 SKILL.md files with workflow-step granularity. Zenstory offers 13 skills and 7 agent templates with layered state. The disagreement is not about whether specialist roles are valuable, but about how many are needed and how deep each should be. CodexWriter's current 11-skill taxonomy leans toward Lensetek's breadth, but the alignment evaluation noted that not all 11 have equal evidence support.

### 4.3 Where the sources solve different layers of the same problem

**State persistence layer.** Dewhurst solves the Markdown/YAML state layer. Zenstory solves the structured JSON state layer with transactions. Dewhurst and Zenstory are not competing at the same layer — Dewhurst's state is file-oriented and human-readable; Zenstory's state is structured and machine-validated. A hybrid model can adopt Dewhurst's file discipline for human-readable artifacts and Zenstory's transaction semantics for the structured layer.

**Context management layer.** Dewhurst solves the reload-contract layer. JeroTan solves the sharding and targeted-lookup layer. wgwtest solves the LOD and prose-over-summary layer. These are complementary, not competing. A full context assembly layer should incorporate all three.

**Process discipline layer.** Haowjy solves the cognitive-role separation layer. JeroTan solves the editorial-gate layer. Rhavekost solves the stopping-rule and diagnostic-to-repair layer. These are complementary. A full process discipline layer should incorporate all three.

**Reader testing layer.** Rhavekost solves the context-blind reader testing layer. Lensetek's beta-reader simulator and Haowjy's reader-sim are context-loaded alternatives. The disagreement is about whether reader testing should be blind or informed. The synthesis should recommend Rhavekost's pattern: blind first pass, optional informed diagnostic pass afterward.

**Continuity validation layer.** Dewhurst solves the executable mechanical-checks layer. Zenstory solves the cross-field consistency layer integrated into transactions. The sources agree that continuity validation should exist; they disagree on scope (Dewhurst's cast/membership/location/promise checks vs. Zenstory's cross-field consistency) and on integration (Dewhurst's CLI-driven checks vs. Zenstory's transaction-embedded validation).

---

## 5. Current JSON Prototype Assessment

### 5.1 What the current prototype gets right

**State categories are well-chosen.** The four schemas define: story-level metadata and phase tracking (`story-state.schema.json`), dynamic character state with knowledge/emotional/physical dimensions (`character-state.schema.json`), scene-level state with beats, outline/draft status, dread/symbolic elements, thread pulls, continuity notes, and evaluation notes (`scene-state.schema.json`), and continuity tracking with character/timeline/knowledge/promise consistency checks, open contradictions, and check history (`continuity.schema.json`). These categories are supported by the source evidence: Dewhurst's `continuity/state.md` captures current character/object/knowledge state; Zenstory's layered model captures similar categories with revision counters; wgwtest's three-layer knowledge model (author truth / character knowledge / reveal boundary) maps to the knowledge and character-state schemas.

**Revision counters are present.** `state_revision` in story-state, `current_state_revision` in character-state, `scene_revision` in scene-state, and `continuity_revision` in continuity-state provide monotonic counters that support the revision-tracking concern from Zenstory and the post-draft/revision-propagation concern from Dewhurst.

**Structured fields support machine checking.** The schemas define patterns, enums, and required fields that enable schema validation. Character IDs use a `^[a-z0-9-]+$` pattern. Chapter IDs use a `^[0-9]+-[a-z0-9-]+$` pattern. Phase and status fields use enums. These are the mechanical categories that Dewhurst's CLI validates and that Zenstory's transaction protocol validates before apply.

**Checks arrays are defined.** The continuity schema defines `character_consistency`, `timeline_consistency`, `knowledge_consistency`, and `promise_consistency` arrays with check types, statuses, findings, and severities. This is the right structure for a continuity report, and it maps to Dewhurst's continuity categories and Zenstory's consistency checks.

**Source lineage and evaluation notes are included.** Character-state has `source_lineage_note`. Scene-state has `source_lineage_note` and `evaluation_notes`. These support the evidence-before-inference discipline from wgwtest and the Dust & Ash epistemic verb requirement.

### 5.2 What the current prototype lacks

**No transaction semantics.** The schemas define state structures but not update protocols. There is no patch/validate/apply/publish pattern. There is no stale-revision protection. An update can overwrite a newer state_revision without detection. This is the gap between CodexWriter's current model and Zenstory's transaction protocol.

**No author memory layer.** The schemas capture story state, character state, scene state, and continuity state, but not author preferences, style memory, or decision history as a separate persistent layer. Haowjy's `kb/` vs. `work/` distinction and Zenstory's author memory layer are not represented.

**No derived views.** The schemas define the canonical state structures, but there is no concept of derived views — different presentations of the same underlying state for different consumers (e.g., a reader-simulation view that excludes privileged author context, or a continuity-report view that surfaces only flagged findings). Zenstory's derived-view pattern is not represented.

**No cross-file consistency enforcement.** The schemas validate individual files against their structures, but there is no mechanism for cross-file consistency checks: does a character's `last_seen_chapter` match the chapter's `pov_character_ref`? Does a scene's `pov_character_id` match the character's current state? Does a promise's `payoff_chapter_ref` exist in the chapters array? Dewhurst's CLI performs some of these checks; Zenstory's cross-field consistency checks perform others. CodexWriter's schemas do not.

**No context assembly integration.** The schemas define what state exists, but not how it is loaded for a given task. There is no LOD strategy, no reload contract, no near/far policy, no index. This is the gap between the state model and the context management principle.

**No judgment-based vs. mechanical distinction.** The continuity schema defines checks with statuses and severities, but it does not distinguish mechanically checkable categories (cast membership, location consistency, promise timing, chapter numbering) from judgment-based categories (voice consistency, emotional progression, pressure-system consistency). Dewhurst's CLI performs the former; the latter remain prompted judgment. The prototype does not make this distinction explicit.

### 5.3 Where it adopted decisions prematurely

**Zenstory's influence on the layered schema design was adopted before all seven sources were analyzed.** The F1 decision acknowledges this: "The ARCHITECTURE.md guardrails required all seven source analyses before CodexWriter chose a canonical state design. That guardrail was violated." The result is not necessarily wrong — the JSON model may prove correct or partially correct — but the decision was premature. The synthesis must weigh the JSON model against Dewhurst's Markdown-first alternative before ratification.

**The orchestrator declared `story-state.json` canonical before the state model was ratified.** This established a single-authoritative-state precedent that may or may not be correct. Dewhurst's model is distributed and registry-based, not single-canonical. If Dewhurst's model is adopted, the orchestrator's current authority assumption needs revision.

**The continuity skill is described as deterministic but operates on model judgment.** The alignment evaluation flagged this as the single largest operational gap. The prototype's continuity schema is structurally sound, but the skill that populates it does not yet deliver deterministic validation for the categories it claims to check.

---

## 6. State-Architecture Options

### 6.1 Option A: Markdown/Document-First State

**Description:** Story state lives in Markdown files with structured YAML/JSON frontmatter, following the Dewhurst and JeroTan pattern. `story.md` is the top-level bible. `characters/*.md`, `worldbuilding/*.md`, `plot/arcs/*.md`, `plot/timeline.md`, `scenes/*.md`, `continuity/state.md`, `continuity/questions/*.md`, and `continuity/promises/*.md` are individual Markdown files. A CLI or tooling layer performs deterministic validation against the frontmatter structures. The Markdown files are authoritative for human-readable content; the CLI validates the mechanical contract.

**Authority:** Human-readable Markdown files are authoritative. The CLI or validator checks the mechanical contract (frontmatter structure, cross-references, pattern compliance) and warns about conflicts, but does not silently resolve them. Where prose and frontmatter conflict, the conflict is flagged for author resolution — the frontmatter is not automatically authoritative over the prose, and the prose is not automatically authoritative over the frontmatter.

**Revision handling:** Revision is file-level. Each Markdown file can carry a `revision` field in its frontmatter, incremented when the file changes. The CLI can detect stale frontmatter (e.g., a character file's `last_seen_chapter` not matching the chapter's POV). There is no transactional guarantee — two agents editing different files can produce inconsistent state, and the CLI detects the inconsistency after the fact rather than preventing it.

**Conflict resolution:** After-the-fact detection. The CLI or validator warns about conflicts (character died-in appearing in later chapters, scene cast vs. chapter cast mismatches, promise payoff before planting, location mismatches). Conflicts are flagged for author resolution. There is no stale-write prevention — if two agents write to the same file simultaneously, the last write wins.

**Human approval:** Document-level review gates. Outline approval before drafting (JeroTan pattern). Phase gates (Lensetek pattern). Editorial pass stopping rules (Rhavekost pattern). The gates are artifact-oriented: approve this outline, approve this chapter, approve this revision. Dewhurst's two-mode pattern (interactive approval vs. PR-boundary review) is available.

**Portability:** High. Markdown files are universally readable. Any AI host can read and write them. The CLI or validator is a tooling dependency that may not be available on all hosts, but the state itself is portable. This is the strongest portability story among the three options.

**Inspectability:** High. Humans can read and edit the state directly. The frontmatter provides structure; the Markdown provides narrative. This is the strongest inspectability story.

**Migration:** Low implementation cost, moderate evolutionary cost. Files are portable; schema evolution may require manual frontmatter updates or migration scripts. The absence of a canonical JSON store means there is no single instance to migrate, but there are many files to keep consistent.

**Implementation cost:** Low. No custom storage layer is needed. The state is files. The CLI or validator is the main tooling investment. Dewhurst's `src/continuity.js` and JeroTan's format-checking JavaScript provide reference implementations.

**Evidence support:** Dewhurst (strongest), JeroTan (strong), Lensetek (partial — artifact-oriented Markdown, but no current-state system), Haowjy (partial — `kb/` vs. `work/` distinction), wgwtest (weak — delegates state elsewhere), Rhavekost (weak — no current-state system), Zenstory (partial — derived views, but structured state is JSON not Markdown).

### 6.2 Option B: JSON/Structured State

**Description:** Story state lives in a canonical JSON store, following the Zenstory pattern. `story-state.json`, `character-state.json`, `scene-state.json`, and `continuity-state.json` are the authoritative state files, validated against their schemas. Markdown artifacts (story bible, character dossiers, scene drafts, continuity reports) are derived views or supplementary human-readable expressions. A state manager or transaction protocol handles updates: patch → validate → apply → publish, with stale-revision protection. Cross-field consistency checks run as part of the validation step.

**Authority:** The canonical JSON store is authoritative for machine-checkable state. Markdown artifacts are derived views or human-readable expressions. Where Markdown and JSON conflict, the JSON is authoritative for the structured fields it covers, and the conflict is flagged for author resolution. The orchestrator maintains the JSON store as the single source of truth for state queries.

**Revision handling:** Monotonic revision counters with transactional semantics. Each update increments the relevant revision counter. The state manager rejects updates that are based on a stale revision. Atomic commits at the state level are possible. Derived views are invalidated or regenerated when the underlying state changes.

**Conflict resolution:** Preventive — stale-revision rejection prevents concurrent-update conflicts at the structured-state level. Cross-field consistency checks catch logical conflicts (character state vs. scene POV, promise timing vs. chapter sequence). Conflicts that cannot be resolved mechanically are flagged for author resolution.

**Human approval:** Gate records are stored in the structured state (phase, phase_gate fields in story-state). Author approval is a state transition: `phase_gate: pending` → `phase_gate: approved`. The state manager can enforce that certain transitions require approval. Editorial pass stopping rules are state transitions: a pass runs, produces findings, and stops for author approval before repairs begin.

**Portability:** Moderate. JSON is universally parseable, but the structured state's value depends on schema awareness. A host that cannot validate against the schemas can still read the JSON, but cannot reliably update it. The state manager or transaction protocol is a tooling dependency that may not be available on all hosts. Portability is achievable but requires more tooling support than Option A.

**Inspectability:** Moderate. Humans can read JSON, but it is less readable than Markdown for narrative content. Derived Markdown views (story bible, character dossiers, continuity reports) are needed for human consumption. The derived-view pattern from Zenstory is essential here — without it, the structured state is opaque to human readers.

**Migration:** Higher implementation cost, higher evolutionary cost. A canonical JSON store means schema evolution requires careful versioning and possibly migration scripts. The state manager must handle schema upgrades. The benefit is that migration is centralized — one store to migrate, not many files.

**Implementation cost:** Higher. Requires a schema validator (Python, validates all 4 schemas against instances — task A5). Requires a state manager or transaction protocol (task A6). Requires derived-view generation. Requires cross-field consistency checks. The investment is larger than Option A, but the benefit is stronger consistency guarantees and a clearer authority model.

**Evidence support:** Zenstory (strongest), CodexWriter current prototype (partial — schemas exist, but no transaction semantics, no state manager, no derived views), Lensetek (weak — artifact-oriented Markdown, no current-state system), Dewhurst (partial — argues for Markdown-first, but its CLI validates mechanical contracts in a way that maps to structured-state validation), Haowjy (weak — no structured state), JeroTan (weak — no structured state), wgwtest (weak — delegates state elsewhere), Rhavekost (weak — no structured state).

### 6.3 Option C: Layered Hybrid Model

**Description:** Story state is split into layers, each with its own authority rule, storage form, and validation strategy. The layers are:

1. **Creative expression layer (Markdown, document-first).** Story bible, character dossiers, scene drafts, prose. These are human-readable, human-authored (or human-approved) creative expressions. They are authoritative for what the story says — the prose, the dialogue, the narrative. They are not mechanically validated for consistency; they are reviewed by humans and by reader simulation.

2. **Structured state layer (JSON/YAML, schema-validated).** Story-state.json, character-state.json, scene-state.json, continuity-state.json. These capture the machine-checkable aspects of the story: phase, revision counters, character knowledge, scene beats, continuity findings, promise/payoff status. They are validated against schemas. They are updated through a transaction-like protocol (patch → validate → apply → publish) with stale-revision protection. They are derived from or reconciled with the creative expression layer, but they are authoritative for the structured fields they cover.

3. **Index and registry layer (Markdown with frontmatter, Dewhurst-style).** `_index.md` files or equivalent registries that list characters, scenes, chapters, arcs, questions, promises, locations. These are rebuilt from the underlying files (Dewhurst's `story reindex` pattern) and serve as cross-reference indexes. They are authoritative for what exists (which characters, which scenes, which chapters) but are rebuilt from the files, not independently edited.

4. **Author memory and preference layer (structured, separate from story state).** Author preferences, style profile, decision history, forbidden tropes, tone axioms. This is separate from the story-state layer — it persists across projects or across a project's lifetime, but it is not part of the story's canonical state. Haowjy's `kb/` vs. `work/` distinction and Zenstory's author memory layer support this.

5. **Derived view layer.** Different presentations of the same underlying state for different consumers. A reader-simulation view that excludes privileged author context (character dossiers, story bible, continuity report, narrative architecture) and presents only the manuscript. A continuity-report view that surfaces only flagged findings. A scene-outline view for scene planning. These are generated from the structured state and the creative expression layer, not independently edited.

**Authority:** Each layer has its own authority rule. The creative expression layer is authoritative for narrative content. The structured state layer is authoritative for machine-checkable state fields. The index layer is rebuilt from underlying files. The author memory layer is authoritative for preferences and decisions. The derived view layer is generated, not authoritative. Where layers conflict (e.g., a character dossier says the character knows X, but character-state.json says the character does not know X), the conflict is flagged for author resolution — the structured state is not automatically authoritative over the creative expression, and the creative expression is not automatically authoritative over the structured state. The conflict rule is: when prose and structured state conflict, flag for author; do not silently resolve.

**Revision handling:** Each layer handles its own revision: Markdown files carry file-level revision fields; structured state uses monotonic counters with stale-revision protection; indexes are rebuilt and carry a rebuild timestamp; author memory carries its own revision; derived views are regenerated on demand or when underlying state changes.

**Conflict resolution:** Cross-layer conflicts are detected by validators (cross-file consistency checks, cross-field consistency checks) and flagged for author resolution. Within the structured state layer, stale-revision rejection prevents concurrent-update conflicts. Within the creative expression layer, last-write-wins at the file level, with Git providing version history and merge conflict detection.

**Human approval:** Document-level gates (outline approval, chapter approval, revision approval) are supported by the creative expression layer. Phase gates are supported by the structured state layer (phase, phase_gate fields). Editorial pass stopping rules are supported by the structured state layer (findings → stop for approval → repairs). Dewhurst's two-mode pattern (interactive approval vs. PR-boundary review) is supported: the PR boundary is a Git concept, not a state concept.

**Portability:** High for the creative expression and index layers (Markdown). Moderate for the structured state layer (JSON is parseable, but schema awareness and transaction protocol are tooling dependencies). High for the author memory layer (structured but separable). The hybrid model's portability is better than pure structured state and slightly worse than pure Markdown, because the structured layer requires tooling support.

**Inspectability:** High for the creative expression and index layers. Moderate for the structured state layer (JSON is readable, but derived Markdown views are needed for human consumption). High for the author memory layer. High for derived views (they are designed for human or consumer readability).

**Migration:** Modular. Each layer can evolve independently. The creative expression layer migrates like any Markdown files. The structured state layer migrates like any JSON schema — versioning and migration scripts. The index layer is rebuilt, not migrated. The author memory layer is separable and can be versioned independently. The hybrid model's migration cost is higher than pure Markdown (because the structured layer needs schema evolution) but lower than pure structured state (because the creative expression layer does not depend on the structured layer's schema).

**Implementation cost:** Moderate. Higher than pure Markdown (because the structured layer needs a validator, transaction protocol, and derived views) but lower than pure structured state (because the creative expression layer does not depend on the structured layer, and the index layer is rebuilt from files). The investment is in: schema validator (task A5), minimum viable continuity validator (task A6), cross-file consistency checks, derived-view generation, and the conflict-detection rules between layers.

**Evidence support:** This option synthesizes evidence from all seven sources: Dewhurst's Markdown-first state and indexes, JeroTan's sharding and document discipline, wgwtest's LOD and prose-over-summary rule, Haowjy's cognitive-role separation and durable-knowledge vs. working-material distinction, Rhavekost's context-blind reader testing (which maps to the derived-view layer's reader-simulation view), Lensetek's specialist role taxonomy and phase gates, and Zenstory's structured state, transaction semantics, stale-revision protection, derived views, and author memory. No single source supports the full hybrid model, but each contributes a layer.

---

## 7. Provisional Recommendation

**Recommended architecture: Option C, the layered hybrid model.**

The hybrid model is recommended because it is the only option that reconciles the Markdown-first evidence (Dewhurst, JeroTan) with the structured-state evidence (Zenstory, CodexWriter's current prototype) instead of choosing one over the other. It preserves the human readability and portability of Markdown for creative expression, while adopting structured JSON state with transaction semantics for machine-checkable continuity and revision tracking. It adopts Dewhurst's index/registry pattern as a cross-reference layer that is rebuilt from files rather than independently edited. It adopts Haowjy's author-memory-as-separate-layer pattern. It adopts Rhavekost's context-blind reader testing as a derived view (reader-simulation view that excludes privileged author context). It adopts Zenstory's stale-revision protection and cross-field consistency checks for the structured layer.

The hybrid model does not require abandoning CodexWriter's current JSON schemas. The schemas define the structured state layer; they are a good start. What is missing is the transaction protocol, the stale-revision protection, the cross-file consistency checks, the derived views, the author memory layer, the index/registry layer, and the explicit conflict-resolution rules between layers. These are additions, not replacements.

The hybrid model also does not require abandoning the Markdown skill files and templates that CodexWriter has already built. The creative expression layer is already Markdown. The structured state layer is already JSON. The gap is the integration layer — the authority rules, the update discipline, the context assembly, and the cross-layer consistency checks.

**This recommendation is provisional and awaits Dave's ratification.** It is based on evidence from all seven sources and the current build, but it is not final. Dave may prefer a pure Markdown model (Option A) if he values simplicity and portability over structured-state guarantees, or a pure structured-state model (Option B) if he values consistency guarantees over Markdown simplicity. The recommendation exists to focus the ratification discussion, not to preempt it.

---

## 8. Decision Register for Dave

The following decisions require Dave's explicit acceptance, rejection, or modification before implementation continues. Each decision is listed with what it governs, what the synthesis recommends, and what the alternatives are.

### D1: State architecture — hybrid model vs. Markdown-first vs. structured-state-first

**Governs:** What is authoritative state, how state is stored, how updates are validated, how conflicts are resolved, how state is migrated.

**Synthesis recommends:** Option C, the layered hybrid model, with the creative expression layer (Markdown) authoritative for narrative content, the structured state layer (JSON) authoritative for machine-checkable fields, the index/registry layer rebuilt from files, the author memory layer separate, and derived views for different consumers. Conflicts between layers are flagged for author resolution, not silently resolved.

**Alternatives:** Option A (pure Markdown/document-first, Dewhurst/JeroTan model) — simpler, more portable, weaker consistency guarantees. Option B (pure JSON/structured-state-first, Zenstory model) — stronger consistency guarantees, weaker human readability and portability, higher implementation cost.

**Decision type:** Accept / Reject / Modify.

### D2: Authority rule for prose vs. structured state conflicts

**Governs:** When the creative expression layer and the structured state layer disagree (e.g., a character dossier says the character knows X, but character-state.json says the character does not know X), which is authoritative, or how is the conflict resolved?

**Synthesis recommends:** Neither is automatically authoritative. Conflicts are flagged for author resolution. The structured state layer is authoritative for the structured fields it covers (revision counters, phase, knowledge lists, promise status), but the creative expression layer is authoritative for narrative content. Where a structured field can be derived from narrative content (e.g., a character's knowledge can be inferred from the prose), the derivation is recorded as an inference with source lineage, not treated as authoritative.

**Alternatives:** Structured state is always authoritative over prose (simpler, but risks silencing author creative choices). Prose is always authoritative over structured state (simpler, but risks state drift). Conflicts are resolved by last-write-wins (simplest, but risks silent inconsistency).

**Decision type:** Accept / Reject / Modify.

### D3: Transaction protocol for structured state updates

**Governs:** How updates to story-state.json, character-state.json, scene-state.json, and continuity-state.json are validated before being applied, and how stale-revision conflicts are handled.

**Synthesis recommends:** Adopt Zenstory's patch → validate → apply → publish pattern for the structured state layer. Updates are proposed as patches, validated against schemas and cross-field consistency checks, applied only if the current revision matches the expected revision (stale-revision protection), and published with incremented revision counters. Failed validations produce structured error reports, not silent failures.

**Alternatives:** No transaction protocol — updates are applied directly, with validation as a separate post-hoc check (Dewhurst pattern). This is simpler but lacks stale-revision protection and atomicity. Partial protocol — some validations are enforced, others are not.

**Decision type:** Accept / Reject / Modify.

### D4: Context assembly layer — adopt or defer

**Governs:** Whether CodexWriter builds an explicit context assembly layer with reload contracts, LOD strategy, sharding, near/far policy, and context budget, or defers context management as a skill-level concern.

**Synthesis recommends:** Adopt a context assembly layer, drawing on Dewhurst's explicit reload contracts, JeroTan's sharding and targeted lookup, and wgwtest's LOD policy with the prose-over-summary conflict rule. The context assembler is a cross-cutting capability (candidate infrastructure, as noted in ARCHITECTURE.md Section 4.1) that loads the smallest sufficient context for a given task, with explicit reload contracts per skill and a prose-over-summary rule for conflicts.

**Alternatives:** Defer context assembly as a skill-level concern — each skill defines its own inputs, and context management is left to the host agent (Lensetek pattern). This is simpler but does not scale to long projects and leaves the largest scalability gap unaddressed.

**Decision type:** Accept / Reject / Modify.

### D5: Reader simulation — context-blind first pass

**Governs:** Whether the reader-simulation skill adopts Rhavekost's context-blind testing pattern: a first pass with the manuscript only, isolated context, no author context, with an optional informed diagnostic pass afterward.

**Synthesis recommends:** Adopt Rhavekost's context-blind pattern for the reader-simulation skill. The first pass is context-blind: the reader sees only the manuscript, with no character dossiers, story bible, continuity report, or narrative architecture. An optional informed diagnostic pass can follow, loading author context to diagnose specific issues. This resolves the documented contradiction between CodexWriter's current context-loaded reader simulation and Rhavekost's best practice.

**Alternatives:** Keep the current context-loaded pattern (simpler, but contradicted by Rhavekost and flagged by the alignment evaluation). Adopt a middle ground — partial context, with some author context excluded (compromise, but not clearly defined).

**Decision type:** Accept / Reject / Modify.

### D6: Editor gate — exact-text approval before prose edits

**Governs:** Whether the prose-editing skill adopts JeroTan's exact-text editor gate: before editing a passage, the editor presents the exact text to be changed and receives author approval for that specific change, rather than describing the change in general terms and proceeding.

**Synthesis recommends:** Adopt JeroTan's exact-text editor gate as a prose-editing constraint for significant changes. For trivial changes (typo fixes, obvious grammar), the gate may be relaxed. For substantive changes (rewriting a passage, altering dialogue, changing narrative content), the editor presents the exact original text, the exact proposed text, and the reason for the change, and receives author approval before applying the edit.

**Alternatives:** Keep the current prose-editing pattern (describe changes, apply them, report what was changed). Adopt a lighter gate — describe changes and receive general approval, without exact-text presentation. Adopt the gate for all changes, including trivial ones.

**Decision type:** Accept / Reject / Modify.

### D7: Editorial stopping rules — separate passes with distinct scopes

**Synthesis recommends:** Adopt Rhavekost's separate-pass pattern: continuity audit first (stop for author review of findings), then prose editing (stop for author review of significant changes), then macro/structural review (stop for author review of structural issues), then line editing (stop for author review of final polish). Each pass has a distinct scope, stopping rule, and author approval gate.

**Alternatives:** Keep the current sequence (continuity → prose-editing → reader-simulation) without distinct stopping rules between passes. Combine passes (e.g., continuity and prose editing in one pass). Keep the current sequence but add stopping rules.

**Decision type:** Accept / Reject / Modify.

### D8: Two-mode HITL — interactive approval vs. PR-boundary review

**Synthesis recommends:** Adopt Dewhurst's two-mode pattern. Interactive mode: outline approval before drafting, chapter approval after drafting, revision approval after editing — each gate is a human approval point before the next step. Automated mode (for future automation): drafting proceeds with approval shifted to the PR boundary — the agent outlines, drafts, updates state, runs continuity, and opens a PR for human review before the work is merged.

**Alternatives:** Keep only interactive mode (simpler, but does not support future automation). Keep only PR-boundary mode (supports automation, but less human control during the creative process). Keep the current single-mode pattern.

**Decision type:** Accept / Reject / Modify.

### D9: Author memory layer — separate from story state

**Synthesis recommends:** Adopt a separate author memory layer, drawing on Haowjy's `kb/` vs. `work/` distinction and Zenstory's author memory pattern. Author preferences, style profile, tone axioms, forbidden tropes, decision history, and project-profile choices live in a separate layer that persists across story state updates and, optionally, across projects. This layer is not part of the story's canonical state — it is the author's persistent context, not the story's.

**Alternatives:** Fold author preferences into story-state.json's `author_preferences` field (current pattern). Keep author preferences in Markdown files (story bible, separate preference document). Do not maintain a persistent author memory layer — preferences are stated per task.

**Decision type:** Accept / Reject / Modify.

### D10: Index/registry layer — rebuilt from files

**Synthesis recommends:** Adopt Dewhurst's index/registry pattern. `_index.md` files (or equivalent) list characters, scenes, chapters, arcs, questions, promises, locations. These indexes are rebuilt from the underlying files (Dewhurst's `story reindex` pattern), not independently edited. The indexes serve as cross-reference maps for context assembly and continuity checking.

**Alternatives:** Maintain indexes as independently edited files (current CodexWriter pattern — chapter lists, scene lists, character lists in story-state.json). Do not maintain indexes — context assembly scans files as needed. Maintain indexes in the structured state layer (JSON arrays in story-state.json).

**Decision type:** Accept / Reject / Modify.

### D11: Derived views — separate presentations for different consumers

**Synthesis recommends:** Adopt Zenstory's derived-view pattern. Different consumers see different presentations of the same underlying state. The reader-simulation view excludes privileged author context. The continuity-report view surfaces only flagged findings. The scene-outline view presents beats, emotional targets, dread elements, and symbolic elements. Derived views are generated from the structured state and the creative expression layer, not independently edited.

**Alternatives:** Keep a single representation for all consumers (current pattern — the same state files are read by all skills). Generate derived views on demand for some consumers but not others. Do not generate derived views — each skill reads the state it needs and filters as best it can.

**Decision type:** Accept / Reject / Modify.

### D12: Portable state — schema awareness as a portability requirement

**Synthesis recommends:** Treat schema awareness as a portability requirement for the structured state layer. Any host that updates the structured state must be able to validate against the schemas. Hosts that cannot validate should read but not write the structured state, or should write only through a host that can validate. This is a stronger requirement than the current portability claim (which asserts that Markdown and JSON are universally parseable, but does not address update validation).

**Alternatives:** Treat portability as read-only — any host can read the state, but only hosts with schema awareness can update it (de facto current pattern). Treat portability as universal — any host can read and write, with validation as a best-effort check. Treat portability as host-specific — the system is designed for specific hosts and portability is not a primary requirement.

**Decision type:** Accept / Reject / Modify.

---

## 9. Implementation Consequences

The following shows the dependency order for the implementation workstream, assuming Dave ratifies the hybrid model recommendation (Option C). If Dave chooses Option A or Option B, the order shifts accordingly.

### Phase 0: Ratification (this gate)

- Dave accepts, rejects, or modifies the 12 decisions in Section 8.
- The synthesis document is not merged into `development` until ratification is complete.

### Phase 1: Schema hardening (tasks A4–A6, A17 — High priority, built and tested together)

**Dependencies:** None. This phase can begin after ratification of D1 (state architecture) and D3 (transaction protocol), because the schemas need to encode the transaction fields (expected revision, patch/apply/publish markers), the cross-field consistency check categories, and the derived-view metadata.

**Work:**
- Add stable IDs to all schema fields that need to be referenced across files (character_id, chapter_id, scene_id, event_id, promise_id, question_id, location_id, rule_id).
- Add cross-file reference fields (e.g., character-state's `last_seen_chapter` references a chapter_id; scene-state's `pov_character_id` references a character_id; continuity checks reference character_ids, chapter_ids, promise_ids).
- Add gate audit records to story-state (who approved each gate, when, what was approved).
- Add knowledge provenance to character-state (how each knowledge item was derived — from prose, from inference, from author statement).
- Add revision history to story-state (log of each state_revision increment with what changed and who changed it).
- Add cross-file consistency check categories to continuity schema (the checks that Dewhurst's CLI performs and that Zenstory's cross-field consistency performs).
- Build schema validator (Python, validates all 4 schemas against instances — task A5).
- Build minimum viable continuity validator (schema validation + character_id pattern checks + phase/phase_gate consistency + state_revision monotonicity — task A6).
- Build generic fixtures + smoke tests + CI (task A17).

**Assumptions:** The hybrid model is ratified. The structured state layer uses the existing 4 schemas as a starting point, with additions for transaction fields and cross-file references. The validator is Python, per the alignment evaluation.

### Phase 2: Context assembly layer (task A7 — Medium priority)

**Dependencies:** Phase 1 schema hardening, because the context assembler needs to know what state exists, what the schemas cover, and what the cross-file references are.

**Work:**
- Define reload contracts per skill (Dewhurst pattern): what each skill reads before it runs.
- Define LOD strategy (wgwtest pattern): full prose near the current task, structured/summary context for distant material, with the prose-over-summary conflict rule.
- Define sharding boundaries (JeroTan pattern): how large documents are split, what cross-references are maintained across shards.
- Define near-field/far-field policy: what is loaded in full, what is loaded as summary, what is excluded.
- Define context budget: maximum context per task, with fallback behavior when the budget is exceeded.
- Define summary compression protocol: how summaries are generated, who generates them, how they are validated against the source material.
- Define cold-context exclusion tier: what is never loaded unless explicitly requested.

**Assumptions:** The hybrid model is ratified. The context assembly layer is a cross-cutting capability, not a skill. The reload contracts are defined per skill, not globally.

### Phase 3: Reader isolation and editorial stopping rules (tasks A8, A9 — Medium priority)

**Dependencies:** Phase 2 context assembly, because the reader-simulation context-blind view is a derived view that depends on the context assembler's ability to exclude privileged author context. Editorial stopping rules depend on the transaction protocol (Phase 1) for the state transitions that stop and resume passes.

**Work:**
- Redesign reader-simulation for context-blind model (task A8): first pass with manuscript only, isolated context, no author context; optional informed diagnostic pass afterward. Implement as a derived view (reader-simulation view) that the context assembler generates by excluding character dossiers, story bible, continuity report, narrative architecture, and other privileged author context.
- Define shared findings/disposition schema (task A9): a standard format for audit findings that stops for author review before repairs. The schema covers: finding ID, category, severity, location, description, evidence, recommended action, author decision (accept, reject, modify, defer), and resolution notes. The schema is used by continuity findings, prose-editing findings, and structural review findings.

**Assumptions:** Rhavekost's context-blind pattern is ratified (D5). Rhavekost's separate-pass pattern is ratified (D7). The findings/disposition schema is shared across continuity, prose-editing, and structural review.

### Phase 4: Project profiles (task A3 — Medium priority, contingent on F2)

**Dependencies:** Phase 1 schema hardening, because project profiles may add profile-specific fields to the schemas (e.g., Dust & Ash's epistemic verb discipline requirement, Thread Pull design, source lineage notes).

**Work:**
- Extract Dust & Ash profile from the core (F2 decision): Biblical/ANE/Stephen King/Gemini/Thread Pull requirements are extracted into a Dust & Ash profile. Generalizable reasoning principles (evidence before inference, pressure systems, source lineage notes, contamination review) remain in the core.
- Define profile mechanism: how profiles add fields, constraints, and skill variants to the core system. Profiles are optional layers that extend the core, not separate systems.
- Define profile-specific skill variants: the character-development skill's V4 pipeline is a Dust & Ash profile variant, not the core character-development skill.

**Assumptions:** F2 is ratified (framework scope: reusable core with optional project profiles). The V4 pipeline is extracted into the Dust & Ash profile, not retained in the core character-development skill.

### Phase 5: Portability validation (task A16 — Medium priority)

**Dependencies:** Phase 2 context assembly, Phase 3 reader isolation, because portability testing requires a representative workflow that exercises context assembly and reader simulation on multiple hosts.

**Work:**
- Build an initial portability smoke test: one skill on a second host (initial signal).
- Build a representative workflow on at least two hosts, with differences and fallbacks documented (Alpha requirement).
- Document host-specific differences: context loading behavior, file I/O patterns, schema validation availability, transaction protocol support.
- Document fallbacks: what happens when a host cannot validate against schemas, cannot run the transaction protocol, cannot assemble context as designed.

**Assumptions:** Portability is reframed as a representative-workflow requirement (alignment evaluation D4.2), not an initial smoke test. The smoke test is a starting point, not the final portability validation.

### Phase 6: Tests and CI (task A17 — High priority, built with Phase 1)

**Dependencies:** Phase 1 schema hardening and validator. Tests validate the schemas, the validator, the continuity validator, and the fixtures.

**Work:**
- Build generic fixtures (example instances of story-state.json, character-state.json, scene-state.json, continuity-state.json that validate against the schemas).
- Build smoke tests (validate fixtures against schemas, run continuity validator against fixtures, test transaction protocol with stale-revision scenarios).
- Build CI (run tests on every commit, validate that the schemas and validator are internally consistent).

**Assumptions:** Tests and CI are built together with Phase 1 (alignment evaluation D4.1), not sequentially.

### Phase 7: Export (task A18 — Low priority, deferred)

**Dependencies:** Phase 1 (schemas provide metadata for export: title, author, project ID, book ID, word count, chapter list with sequence order). Phase 5 (portability validation ensures export works on the target hosts).

**Work:**
- Build Markdown manuscript compilation (default export): assemble all chapters in canonical order with front matter.
- Build DOCX export (extension): formatted Word document, if the DOCX export capability is implemented.
- Build PDF export (extension): formatted PDF, if the PDF export capability is implemented.
- Build ePub export (extension): ePub file, if the ePub export capability is implemented.

**Assumptions:** Export is deferred until the core authoring pipeline is operational. Markdown is the default; other formats are extensions. The export skill is the last step in the pipeline, after all creative work is complete.

---

## 10. Risks and Unresolved Evidence

### 10.1 Rhavekost §11 limitations

The Rhavekost source analysis (`docs/source-analysis/rhavekost-author-toolkit.md`) records consequential exclusions in Section 11. The analysis inventoried all 79 tracked files at the pinned commit but did not individually inspect all of them. The exclusions include:

- **Prose-mechanics exemplars:** 12 exemplar files under `skills/prose-mechanics/references/exemplars/` were not individually inspected. The analysis read the prose-mechanics SKILL.md and audit-tracker-template.md, plus 6 of 18 top-level prose-mechanics reference files, but the exemplars — which are the strongest available evidence about what prose-mechanics actually demonstrates in practice (before/after pairs, diagnostic rule illustrations, real text samples) — were not read. The analysis's conclusions about prose-mechanics are therefore based on the SKILL.md's described behavior, not on verified exemplar content.

- **Avoid-ai-writing claims:** The `avoid-ai-writing/SKILL.md` was partially inspected, not fully read. The analysis verified the file's existence and structure, and checked the vendored material's license and attribution, but did not read the full SKILL.md content. The compatibility claims in the avoid-ai-writing header are the vendored skill's own claims, not the toolkit's, and the analysis could not fully verify them.

- **Character-archetypes and narrative-nonfiction supporting files:** 5 of 8 character-archetypes supporting files and 8 of 10 narrative-nonfiction supporting files were not individually inspected. The analysis read the SKILL.md files for both, plus some supporting files, but not all.

- **Fiction-workshop supporting files:** All 9 fiction-workshop supporting files were inspected, making fiction-workshop the most fully inspected skill. This is a positive data point, but it does not extend to the other skills.

**Impact on synthesis:** The Rhavekost evidence in this synthesis is therefore partial. The analysis's conclusions about context-blind reader testing, separate editorial passes, stopping rules, and the prose-mechanics audit contract are based on the files that were inspected, and the §11 exclusions mean that some of those conclusions may not be fully supported by the full Rhavekost tree. Specifically:

- The context-blind reader testing pattern is well-supported by the portions of Rhavekost that were inspected (the reader-test methodology is described in the SKILL.md files that were read, and the alignment evaluation's ChatGPT-5 Sol independent inspection confirmed the pattern). The §11 exclusions do not undermine this conclusion.
- The separate editorial passes and stopping rules pattern is described in the portions of Rhavekost that were inspected, but the full scope of the pattern (how many passes, what each pass covers, what the stopping rules are) may be more detailed in the unread portions. The synthesis's recommendation to adopt separate passes with distinct stopping rules is provisional pending fuller Rhavekost inspection.
- The prose-mechanics audit contract is described in the portions of Rhavekost that were inspected, but the exemplars — which would show what the contract actually produces in practice — were not read. The synthesis's recommendation to adopt a diagnostic-to-repair approval flow is provisional pending exemplar inspection.

**Recommendation:** Before implementing the editorial stopping rules and prose-mechanics audit contract, the unread Rhavekost portions (especially the prose-mechanics exemplars and the avoid-ai-writing SKILL.md) should be inspected. The context-blind reader testing pattern can be adopted now, because it is well-supported by the inspected portions and confirmed by independent inspection.

### 10.2 Other source-analysis uncertainties

**Lensetek LICENSE.** The root LICENSE returns 404. The intended license appears to be MIT, but the intended license and an actually granted license should not be treated as identical while the referenced license text is missing. If CodexWriter adopts Lensetek's specialist role taxonomy (which the synthesis recommends), the taxonomy itself is not implementation text and does not require a license grant. But if CodexWriter later decides to copy or adapt Lensetek implementation text, the license ambiguity must be resolved first.

**Dewhurst's `_index.md` authority nuance.** Dewhurst calls `_index.md` files authoritative registries, but the CLI rebuilds them from entity files (`story reindex`). This means the indexes are both authoritative and rebuilt — an authority nuance that should be examined before adopting the pattern literally. The synthesis recommends adopting the pattern with the clarification that indexes are rebuilt from files and are authoritative for what exists, but are not independently edited.

**Haowjy's dependency-derived `cw/` distribution.** The pinned tree includes `cw/` components that are generated or adapted from the `meridian-base` dependency, but the unbounded dependency range and absent lock file do not prove which exact `meridian-base` commit supplied each component. The synthesis recommends adopting Haowjy's cognitive-role separation and process discipline patterns, not its dependency-derived components. If CodexWriter later decides to copy or adapt Haowjy implementation text, file-level provenance review is required.

**JeroTan's translation/derivative lineage.** JeroTan is a translated/re-architected derivative from wordflowlab (`wordflowlab/novel-writer-skills@5bc9b373`). The lineage reference pin should be tracked separately. The synthesis recommends adopting JeroTan's workflow patterns (constitution, sharding, editor gate), not its implementation text. The translation lineage does not affect the architecture recommendations, but it should be tracked for provenance.

**wgwtest's delegated state responsibility.** wgwtest explicitly delegates persistent project state to a separate `novel-project-strategy` responsibility. The synthesis recommends adopting wgwtest's narrative epistemology and LOD context policy, not its state delegation pattern. The delegation pattern is relevant to the question of whether state should be a separate service, but the synthesis's hybrid model assumes state is part of the same project, not a separate service.

**Zenstory's moving dependency.** Some effective Zenstory behavior comes from the `meridian-base` dependency, which is moving. The pinned application commit alone does not identify every runtime component actually resolved in a fresh installation. The synthesis recommends adopting Zenstory's state-architecture patterns (transaction semantics, stale-revision protection, derived views, author memory), not its dependency-based runtime. If CodexWriter later decides to copy or adapt Zenstory implementation text, the dependency lineage must be examined.

**CodexWriter's own F1 violation.** The ARCHITECTURE.md guardrails required all seven source analyses before CodexWriter chose a canonical state design. That guardrail was violated: the orchestrator declared `story-state.json` canonical and the build proceeded before Rhavekost was analyzed. The violation is procedural; it does not establish that the JSON model is wrong. It establishes that the decision was premature. The synthesis treats the current JSON model as a provisional prototype, not the default winner, and weighs it against Dewhurst's Markdown-first alternative before making a recommendation.

### 10.3 Evidence conflicts that prevent a fully confident recommendation

**Conflict 1: Markdown-first vs. structured-state-first.** This is the deepest conflict in the evidence. Dewhurst and JeroTan argue that Markdown with structured frontmatter is sufficient, with a CLI or tooling layer for validation. Zenstory argues for structured JSON state with transaction semantics. The conflict is real, and the synthesis cannot fully resolve it without knowing which categories of state CodexWriter needs to track, how often they change, and how much consistency guarantee is required. The hybrid model recommendation is an attempt to reconcile the two, but it is provisional. Dave may reasonably prefer a pure Markdown model (simpler, more portable, weaker guarantees) or a pure structured-state model (stronger guarantees, more complex, less portable).

**Conflict 2: Context-blind vs. context-loaded reader testing.** Rhavekost explicitly argues for context-blind reader testing. CodexWriter's current reader-simulation skill is context-loaded. The alignment evaluation flagged this as a contradiction. The synthesis recommends adopting Rhavekost's pattern, but this recommendation depends on Rhavekost's pattern being fully supported by the inspected portions of the Rhavekost tree — and the §11 exclusions mean that some of the pattern's details may be in the unread portions. The recommendation is provisionally confident, but not fully confident until the unread portions are inspected.

**Conflict 3: Process discipline vs. state-machine enforcement.** Haowjy and JeroTan argue that process discipline (Muse coordination, editorial gates, exact-text editor gate) reduces errors. Zenstory argues that transaction semantics (patch → validate → apply → publish, stale-revision rejection) reduce errors. The synthesis recommends both, but the interaction between process discipline and state-machine enforcement is not fully specified by any single source. The hybrid model assumes they complement each other, but the exact interaction — when process discipline is sufficient and when state-machine enforcement is necessary — is not fully resolved by the evidence.

**Conflict 4: Depth vs. breadth of specialist roles.** Lensetek offers 16 roles with shallow implementation. wgwtest offers 1 skill with deep craft reasoning. Dewhurst offers 7 roles with operationalized state. The disagreement is about how many specialist roles are needed and how deep each should be. The synthesis recommends retaining CodexWriter's current 11-skill taxonomy (which leans toward Lensetek's breadth), but this recommendation assumes that 11 roles is the right number. Dave may prefer fewer roles with deeper implementation (Dewhurst/wgwtest model) or more roles with broader coverage (Lensetek model).

**Conflict 5: Two-mode HITL — interactive vs. PR-boundary.** Dewhurst documents both modes. The synthesis recommends adopting both, but the interaction between the two modes — when to use which, how to switch between them, whether the same state architecture supports both — is not fully specified by the evidence. The recommendation is provisional pending operational experience with both modes.

---

## Appendix A: Evidence Source Index

| Source | CodexWriter analysis file | Upstream pin | License status | Inspection completeness |
|--------|---------------------------|--------------|----------------|------------------------|
| Lensetek/Fiction-book-agent-skills | `docs/source-analysis/lensetek.md` | `main` at analysis time | MIT badge/link; LICENSE 404 | Full repository inspection; LICENSE unresolved |
| danjdewhurst/story-skills | `docs/source-analysis/danjdewhurst-story-skills.md` | `main` at analysis time | MIT, clear and present | Full repository inspection; CLI, tests, CI inspected |
| haowjy/creative-writing-skills | `docs/source-analysis/haowjy-creative-writing-skills.md` | `fd7a3ad9cd7697a0645ff6ff4bd5e809cf7673a3` | Apache 2.0, clear and present | Full repository inspection; dependency lineage partially unresolved |
| JeroTan/novel-writer-english | `docs/source-analysis/jero-tan-novel-writer-english.md` | `6d836f23281e240eed36d50529424e086c8ff42d` | MIT; translated derivative from wordflowlab | Full repository inspection; lineage tracked separately |
| wgwtest/novel-writing | `docs/source-analysis/wgwtest-novel-writing.md` | `b6382cf7ff29caa83830646432d8010ca96120f5` | MIT, clear and present | Full repository inspection; single-skill scope |
| rhavekost/author-toolkit | `docs/source-analysis/rhavekost-author-toolkit.md` | `b78287003edf52e5f0784ee2b4a004111173358f` | MIT; vendored material separately licensed | Partial; 79 files inventoried, §11 exclusions recorded |
| zenstory-ai/oh-story-claudecode | `docs/source-analysis/zenstory-ai.md` | `d1f88587c0b88abdb0a62b101b850300e0617d7b` | MIT, clear and present | Full repository inspection; dependency lineage partially unresolved |

---

## Appendix B: Existing CodexWriter Artifacts Referenced

| Artifact | Path | Purpose in synthesis |
|----------|------|---------------------|
| README.md | `README.md` | Six core principles evaluated in Section 3 |
| ARCHITECTURE.md | `ARCHITECTURE.md` | Provisional layered model; F1 and F2 decisions; Phase 1 guardrails |
| Alignment evaluation | `docs/decisions/2026-08-26-alignment-evaluation.md` | Accepted decisions (F1, F2); four priority adjustments; source representation wording; framework task list |
| Build report | `docs/build-report-2026-08-26.md` | Foundation phase completion; nlm CLI fix; Dust & Ash private repo; Gemini V4 pipeline extraction |
| Story-state schema | `schemas/story-state.schema.json` | Structured state layer prototype; state categories, revision counters, phase tracking |
| Character-state schema | `schemas/character-state.schema.json` | Dynamic character state; knowledge, emotional, physical dimensions |
| Scene-state schema | `schemas/scene-state.schema.json` | Scene-level state; beats, outline/draft status, dread/symbolic elements, thread pulls, continuity notes |
| Continuity schema | `schemas/continuity.schema.json` | Continuity tracking; character/timeline/knowledge/promise checks, open contradictions, check history |
| Orchestrator skill | `skills/fiction-orchestrator/SKILL.md` | Routing and phase-gate logic; specialist role taxonomy |
| Concept-development skill | `skills/concept-development/SKILL.md` | Phase 1 concept and story bible creation |
| Worldbuilding skill | `skills/worldbuilding/SKILL.md` | Phase 2 worldbuilding artifacts |
| Character-development skill | `skills/character-development/SKILL.md` | Phase 2 V4 dossier pipeline; epistemic verb discipline; contamination prevention |
| Narrative-architecture skill | `skills/narrative-architecture/SKILL.md` | Phase 3 plot architecture; Thread Pull design; promise/payoff mapping |
| Scene-planning skill | `skills/scene-planning/SKILL.md` | Phase 3/4 scene outlines; beat-by-beat breakdown; dread and symbolic elements |
| Scene-writing skill | `skills/scene-writing/SKILL.md` | Phase 4 prose drafting; voice preservation; knowledge constraints |
| Continuity skill | `skills/continuity/SKILL.md` | Phase 4/5 continuity checks; severity levels; mechanical vs. judgment distinction |
| Prose-editing skill | `skills/prose-editing/SKILL.md` | Phase 5 prose revision; voice fidelity; pacing; clarity; style consistency |
| Reader-simulation skill | `skills/reader-simulation/SKILL.md` | Phase 5 reader testing; context-loaded (current); reader personas |
| Export skill | `skills/export/SKILL.md` | Phase 5 manuscript compilation; Markdown default; DOCX/PDF/ePub extensions |
| Story-bible template | `templates/story-bible-template.md` | Phase 1 output template |
| Character-dossier template | `templates/character-dossier-template.md` | Phase 2 output template |
| Scene template | `templates/scene-template.md` | Phase 4 output template |
| Skill template | `templates/SKILL_TEMPLATE.md` | Generic skill template |

---

*End of synthesis. This document is provisional and awaits Dave's ratification. No architecture has been ratified. No implementation has begun. The branch `architecture/seven-source-synthesis` is isolated from `development` and will not be merged until the ratification gate is complete.*
