# CodexWriter — Architecture

> This document describes the high-level design direction of CodexWriter.  
> It is a working draft. During Phase 1, architectural patterns are hypotheses until the source analyses establish how each reference repository actually works.

## 1. Goals

- Provide a modular, version-controlled suite of AI fiction-writing skills.
- Preserve persistent story state and support deterministic continuity checks where the underlying facts are machine-checkable.
- Support specialist agent roles for planning, drafting, reviewing, editing, continuity, and reader testing.
- Manage long-context projects through sharding, summaries, selective loading, and level-of-detail strategies.
- Keep a human author in the loop at meaningful creative and scope-transition points.
- Separate core authoring skills from cross-cutting infrastructure and optional publishing/adaptation extensions.

## 2. Source Repositories Under Review

| Repository | Primary Strength | License Status |
|------------|------------------|----------------|
| lensetek/Fiction-book-agent-skills | Specialist role taxonomy and end-to-end workflow breadth | MIT badge/link, LICENSE currently missing |
| danjdewhurst/story-skills | Persistent story state and deterministic continuity tooling | MIT |
| haowjy/creative-writing-skills | Writer/critic/editor separation, voice preservation, story memory | Apache 2.0 |
| JeroTan/novel-writer-english | Constitution, clarification, context reload, document sharding | MIT; translated/re-architected derivative |
| wgwtest/novel-writing | Narrative epistemology, POV boundaries, context LOD, craft review | MIT |
| rhavekost/author-toolkit | Context-blind reader testing, focused editorial passes, stopping points | MIT; includes separately attributed vendored material |
| zenstory-ai/oh-story-claudecode | Layered state management, transactions, runtime portability, author memory | MIT |

See `docs/architecture-audit.md` for direct evidence, licensing links, and audit notes.

## 3. Phase 1 Architecture Guardrails

- Lensetek is the initial responsibility taxonomy, not automatically the implementation model.
- The seven source analyses must document observed state-storage and workflow behavior before CodexWriter chooses a canonical state design.
- Zenstory's single-authoritative-JSON state is a candidate pattern only.
- `continuity` remains one CodexWriter skill during Phase 1; a future split between state maintenance and validation is deferred.
- Candidate capabilities may be documented before they become final skill names.

## 4. Provisional Layered Model

The current evidence suggests that CodexWriter should be understood as layers rather than one strictly linear chain. This model is provisional.

### 4.1 Control / Coordination

- `fiction-orchestrator` — routes work, enforces workflow boundaries, and coordinates specialist capabilities.
- Project setup / runtime capability detection — candidate infrastructure capability.
- Context assembly — candidate cross-cutting capability responsible for loading the smallest sufficient context for a task.
- Persistent-state maintenance — candidate cross-cutting capability; exact storage model is undecided.

### 4.2 Creative Pipeline

Current author-facing core:

- story constitution / creative contract — candidate capability or artifact; final module boundary undecided
- `concept-development`
- `worldbuilding`
- `character-development`
- `narrative-architecture`
- `scene-planning`
- `scene-writing`

World, character, and plot work may iterate rather than execute in a rigid one-way order.

### 4.3 Evaluation / Revision

- developmental/story review — candidate distinct capability or mode
- `prose-editing`
- `continuity` — kept as one skill during Phase 1
- `reader-simulation`

Reader simulation should be evaluated for deliberate context isolation rather than merely persona prompting.

### 4.4 Optional Extensions

Capabilities present in one or more source repositories but not required in the initial novel-authoring core:

- market/trend research
- benchmark/story deconstruction
- existing-manuscript import
- style/voice profiling
- comic/webtoon adaptation
- children's-fiction adaptation
- accessibility formatting
- publishing/export
- project/update maintenance

## 5. Current Proposed Skill Modules

The stable Phase 1 working list remains:

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

Potential additions such as `story-review`, `context-manager`, `story-state-manager`, `story-constitution`, or `project-maintenance` remain research hypotheses until the source analyses are complete.

## 6. Persistent Story State — Decision Deferred

CodexWriter must preserve durable story knowledge, but the exact storage model is intentionally undecided during Phase 1.

Candidate state categories to compare across repositories include:

- Story Bible / Constitution
- Static character profiles and voice references
- Dynamic character state and knowledge
- World facts and rules
- Timeline / chronology
- Plot arcs and promises/payoffs
- Scene/chapter state
- Open questions and continuity risks
- Author preferences / style memory
- Non-canonical working material

Each source analysis must document what is authoritative, how updates occur, how revisions propagate, and whether machine-readable and human-readable representations are separated.

Only after comparing all seven sources should CodexWriter decide among alternatives such as Markdown-first state, structured JSON/YAML state, hybrid models, or an authoritative structured state with derived views.

## 7. Context Management Strategy

Current principles to preserve and test:

- Document sharding for large projects.
- Level-of-detail loading: full prose near the current task and structured/summary context for distant material.
- Pre-write context reload rather than trusting conversational memory.
- Targeted full-text expansion when style, ambiguity, dialogue rhythm, or exact prose matters.
- Post-write state/context updates when durable facts change.
- A smallest-sufficient-context rule: load information whose omission could cause the current task to be wrong, while excluding unrelated cold context.

The source analyses must also document what wins when summaries, structured state, and manuscript prose disagree.

## 8. Human-in-the-Loop Strategy

Lensetek's phase approval gates remain an important reference, but CodexWriter should also evaluate event-based stopping points found in other repositories.

Candidate HITL gate types:

- direction selection among meaningful creative alternatives
- promotion of exploratory material into canon
- transition from planning to drafting
- transition from diagnosis/audit to applying changes
- exception handling when a deterministic check flags something that may be intentional
- final publication/export approval

Agents should not silently expand scope simply because another workflow stage is available.

## 9. Deterministic vs. Judgment-Based Evaluation

Candidate design rule: **deterministic means executable; judgment means judgment.**

Examples that may be deterministic when backed by schemas/scripts:

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

CodexWriter should never present a judgment-based score as mechanically proven.

## 10. Workflow / Branch Strategy

- `main` — stable, reviewed releases
- `development` — ongoing integration branch
- Feature branches — bounded architecture, research, or skill work created from `development`

The current Phase 1 audit is isolated on `architecture/phase1-audit` and is intentionally time-boxed before source analysis begins.

## 11. Phase 1 Source Order

1. `lensetek/Fiction-book-agent-skills`
2. `danjdewhurst/story-skills`
3. `zenstory-ai/oh-story-claudecode`
4. `haowjy/creative-writing-skills`
5. `JeroTan/novel-writer-english`
6. `wgwtest/novel-writing`
7. `rhavekost/author-toolkit`

## 12. Next Steps

- Review the bounded Phase 1 architecture audit.
- Begin `docs/source-analysis/lensetek.md`.
- Document observed state, context, workflow, HITL, and licensing behavior for each source before promoting candidate patterns into decisions.
- Update the crosswalk incrementally from source evidence.
- Define schemas and prototype skills only after the relevant source comparisons are sufficiently complete.

---

*This document will be updated as evidence-based design decisions are made.*
