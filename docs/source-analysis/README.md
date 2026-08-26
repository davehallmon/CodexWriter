# Source Analysis

This folder contains detailed analysis documents for each source repository reviewed during the development of CodexWriter.

## Purpose

Each source repository will be examined for architecture, workflow, state storage, context management, strengths, weaknesses, human-in-the-loop behavior, and licensing/provenance. The source analyses are the evidence base for later decisions in `ARCHITECTURE.md` and `docs/crosswalk.md`.

During Phase 1, **observed source behavior must be separated from CodexWriter recommendations**. Attractive patterns should be documented as candidates until the comparative analysis supports adopting them.

## Files

- `lensetek.md`
- `danjdewhurst-story-skills.md`
- `zenstory-ai.md`
- `haowjy-creative-writing-skills.md`
- `jero-tan-novel-writer-english.md`
- `wgwtest-novel-writing.md`
- `rhavekost-author-toolkit.md`

## Required Analysis Structure

Each source analysis should include the following sections.

### 1. Repository Snapshot

- Repository URL
- Primary language
- Project maturity / activity observations
- Skill/agent/module count where relevant
- Runtime/platform compatibility

### 2. Licensing and Provenance

- Direct `LICENSE` link and detected license
- Direct `NOTICE` link if present; otherwise record `Not found`
- Direct `ATTRIBUTION.md` or equivalent if present; otherwise record `Not found`
- Upstream/derivative lineage when the repository is itself a translation, fork, vendor bundle, or re-architecture
- Any discrepancy between README badges/claims and actual repository files

### 3. Architectural Thesis

- What problem is the repository designed to solve?
- What is its primary organizing principle?
- What responsibilities are treated as first-class modules/skills/agents?

### 4. Workflow and Orchestration

- Entry points / routing
- Workflow phases or stages
- Specialist role boundaries
- Required vs. optional stages
- Stop conditions and handoffs
- Human approval gates

### 5. State Storage Model

Document actual implementation rather than inferring a preferred CodexWriter model.

- Static/canonical story facts: where are they stored?
- Dynamic/current story state: where is it stored?
- Which artifact is authoritative when files disagree?
- Human-readable vs. machine-readable state
- Story-history representation: snapshots, deltas, logs, rewritten current state, etc.
- How state is updated after drafting
- How state is updated after revising an earlier chapter
- Stale/conflicting update protections, if any
- Promises/payoffs, questions, foreshadowing, timeline, relationships, objects, and character-knowledge representation
- Author preference/voice memory and whether it is separated from story canon
- Treatment of exploratory/non-canonical material

**Important:** Zenstory's single `_tracking-state.json` model is only one hypothesis to compare. Do not assume CodexWriter will use it.

### 6. Context Management

- What is loaded before a task?
- What is excluded?
- Full-text vs. summary/structured context
- Sharding/indexing strategy
- Near-field vs. far-field behavior
- Context-budget limits where explicit
- What happens when summaries/state conflict with manuscript prose?
- Cross-agent handoff context

### 7. Creative-Craft Model

- Planning methodology
- Character/world/plot guidance
- Scene/prose rules
- Voice/style preservation
- Genre-specific knowledge
- Narrative epistemology / POV / causality rules where relevant

### 8. Evaluation and Continuity

- Continuity checks
- Deterministic scripts/validators
- Model-judgment review
- Critic/editor separation
- Reader simulation/testing
- Finding/report formats
- Whether audit and repair are separated

### 9. Human-in-the-Loop Model

- Mandatory approval gates
- Optional confirmations
- Scope-transition rules
- Canon-promotion decisions
- Edit-application behavior
- Explicit stopping points

### 10. Runtime and Maintenance

- Setup/bootstrap behavior
- Capability detection
- Multi-agent vs. solo fallbacks
- Import/migration/doctor/reindex/update tools
- CI/test integration
- Runtime assumptions and failure modes

### 11. Strengths

What the repository does especially well, supported by concrete files or workflow evidence.

### 12. Weaknesses / Gaps

What is shallow, missing, over-opinionated, brittle, domain-specific, or poorly enforced.

### 13. Relevance to CodexWriter

Separate:

- **Observed reusable responsibility**
- **Candidate architectural borrowing**
- **Implementation-level borrowing requiring license/provenance handling**
- **Patterns CodexWriter should avoid**

### 14. Detailed Evidence

Include direct links to relevant `SKILL.md`, reference, schema, script, LICENSE, NOTICE, and attribution files. Use short quotes only when they materially establish an implementation claim.

### 15. CodexWriter Disposition

Summarize decisions only after the evidence sections are complete. Use terms such as:

- Retain responsibility
- Adapt
- Merge candidate
- Split candidate
- Extension candidate
- Defer
- Reject

## Status

| Order | Source | Status |
|---:|---|---|
| 1 | lensetek/Fiction-book-agent-skills | Merged baseline complete |
| 2 | danjdewhurst/story-skills | Merged analysis complete |
| 3 | zenstory-ai/oh-story-claudecode | Merged analysis complete |
| 4 | haowjy/creative-writing-skills | Merged analysis complete |
| 5 | JeroTan/novel-writer-english | Merged analysis complete |
| 6 | wgwtest/novel-writing | Analysis complete; ready for review |
|| 7 | rhavekost/author-toolkit | In progress — pinned at `b78287003edf52e5f0784ee2b4a00411173358f` |

## Next Step

Review `wgwtest-novel-writing.md`. After it is approved and merged, continue the provisional source order with Rhavekost unless review explicitly authorizes a separate synthesis step. No architecture or crosswalk decision is made in this status update.
