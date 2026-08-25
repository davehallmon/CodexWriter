# Phase 1 Architecture Audit

**Status:** Working audit — architecture hypotheses, not final design decisions.  
**Date:** 2026-08-25  
**Scope:** Seven reference repositories currently under review.

## Purpose

This audit compares the seven reference repositories against CodexWriter's current architecture before deep source-by-source analysis begins. It distinguishes **observed implementation patterns** from **CodexWriter hypotheses** so that attractive ideas are not promoted into design decisions before the source analyses establish how each repository actually works.

> **Interpretation rule:** unless a statement is explicitly identified as an observed source fact or an existing CodexWriter Phase 1 principle, new architectural concepts in this audit are **candidate, provisional, or for discussion only**. They should not be treated as adopted design decisions.

## Reference Set

1. `lensetek/Fiction-book-agent-skills`
2. `danjdewhurst/story-skills`
3. `haowjy/creative-writing-skills`
4. `JeroTan/novel-writer-english`
5. `wgwtest/novel-writing`
6. `rhavekost/author-toolkit`
7. `zenstory-ai/oh-story-claudecode`

## Guardrails From This Audit

- Lensetek remains the baseline responsibility taxonomy for the first crosswalk pass.
- Dewhurst remains the initial second source analysis after Lensetek because it directly operationalizes continuity and persistent story state; this order may change if the Lensetek analysis reveals a better comparison path.
- Zenstory's single-authoritative-state design is a **candidate pattern only** until all source analyses document their actual storage models.
- `continuity` remains one CodexWriter skill for now. Whether state maintenance and continuity validation should eventually split is deferred.
- Architectural layers may be documented now, but module boundaries remain provisional until the source analyses are complete.

## High-Level Findings

The current CodexWriter creative pipeline is directionally sound, but the source repositories expose cross-cutting responsibilities that are not represented cleanly by a single linear sequence of authoring skills.

### Patterns to Evaluate More Explicitly

| Pattern | Evidence Source(s) | Current CodexWriter Coverage | Audit Disposition |
|---|---|---|---|
| Non-canonical exploration workspace | Haowjy, JeroTan | Weak | Add as candidate architecture concept |
| Story constitution / creative contract | JeroTan | Partial via Story Bible | Add as candidate artifact/capability |
| Clarification before planning | JeroTan | Implicit | Evaluate during source analysis |
| Durable story-memory / fact-extraction layer | Haowjy | Partial | Evaluate as cross-cutting capability |
| Explicit issues/open-questions tracking | Haowjy, Dewhurst, Rhavekost | Partial | Add to state-analysis checklist |
| Deterministic continuity tooling | Dewhurst, Lensetek | Present in principle | Deepen after source analysis |
| Context LOD and targeted full-text expansion | wgwtest | Present in principle | Preserve and specify evidence |
| Context-blind reader testing | Rhavekost | Present only by name | Add isolation requirement candidate |
| Explicit stopping points / no silent scope advance | Rhavekost, Zenstory | Weak | Add HITL candidate principle |
| Runtime capability detection / fallback | Zenstory | Missing | Evaluate as infrastructure layer |
| Project setup/import/migration/doctor operations | Dewhurst, Zenstory | Missing | Evaluate as infrastructure capabilities |
| Author preference memory separated from story state | Zenstory | Missing | Evaluate; do not adopt yet |
| Style/voice reference artifacts | Haowjy, JeroTan | Partial | Evaluate as durable reference type |
| Structured review finding schema | Rhavekost | Missing | Candidate QA contract |
| Market/deconstruction workflow | Lensetek, Zenstory | Missing from core | Treat as optional extension until analyzed |
| Publishing/adaptation/accessibility outputs | Lensetek, Dewhurst | Missing from core list | Treat as extensions rather than mandatory core stages |

## Provisional Layered Model

The audit supports documenting a layered architecture as a **research scaffold**, but not freezing skill boundaries.

### Control / Coordination

- `fiction-orchestrator`
- project setup / capability detection (candidate infrastructure capability)
- context assembly (candidate cross-cutting capability)
- persistent state maintenance (candidate cross-cutting capability)

### Creative Pipeline

- story constitution / creative contract (candidate)
- `concept-development`
- `worldbuilding`
- `character-development`
- `narrative-architecture`
- `scene-planning`
- `scene-writing`

### Evaluation / Revision

- developmental or story review (candidate; may be a distinct skill or mode)
- `prose-editing`
- `continuity` (kept as one skill for now)
- `reader-simulation`

### Optional Extensions

- market/trend research
- benchmark/story deconstruction
- existing-manuscript import
- style/voice profiling
- comics/webtoon adaptation
- children's-fiction adaptation
- accessibility formatting
- publishing/export

This model is provisional and for discussion. Final module names and boundaries should be decided after the seven source analyses.

## State Architecture: Hypotheses, Not Decisions

CodexWriter currently proposes Markdown and/or JSON state artifacts. The audit found multiple plausible patterns, but it is too early to choose one.

Every source analysis must therefore document:

1. What files or stores hold canonical/static facts?
2. What files hold dynamic/current story state?
3. What is authoritative when two artifacts disagree?
4. Are human-readable views and machine-readable state separated?
5. How are state changes committed after a chapter or revision?
6. Is history stored as snapshots, deltas, logs, or rewritten current state?
7. How are stale or conflicting updates handled?
8. How are promises, questions, foreshadowing, timeline facts, and character knowledge represented?
9. How is author preference/voice memory separated from story canon, if at all?
10. How is working/non-canonical material prevented from becoming canon accidentally?

### Candidate Pattern: Zenstory Single Authoritative State

Zenstory is notable because it explicitly documents one structured authoritative tracking state with deterministic derived views. This is **evidence for a candidate design**, not a CodexWriter decision.

Direct evidence:

- [`tracking-transaction.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/skills/story-long-write/references/tracking-transaction.md) states that tracking uses "one structured authoritative state + multiple deterministic derived views." It identifies `_tracking-state.json` as the sole authoritative layer and says Markdown views are generated from it rather than parsed back as program input.
- The same file documents `init`, `commit`, and `check` operations. `commit` merges and validates the transaction, renders the derived views, then atomically replaces `_tracking-state.json` as the single commit point.
- It also documents `expected_state_revision`, which rejects a sequential stale transaction built from an older state revision.
- [`state-tracking.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/skills/story-long-write/references/state-tracking.md) defines chapter-context filtering and says to retain only information that would cause the chapter to be written incorrectly if omitted. It filters for current character state, directly relevant causal history/foreshadowing, and applicable world constraints.
- [`story-long-write/SKILL.md`](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/skills/story-long-write/SKILL.md) independently states the principle "load only necessary information" and describes author-memory retrieval as separate from per-book tracking.

### Why Zenstory Is Not the Initial Analysis #2

The files substantiate the state-engine claims, but Dewhurst is the current initial recommendation for the second analysis because:

1. Dewhurst's central thesis is directly about continuity as a deterministic story contract, making it the cleanest contrast with Lensetek's continuity checker.
2. Its `story` CLI exposes explicit validation, links, continuity, import, migration, doctor, and CI behaviors around a plain-text project format.
3. Comparing Lensetek → Dewhurst first would let us establish the difference between after-the-fact continuity auditing and state-backed deterministic continuity before introducing Zenstory's more opinionated transactional state engine.
4. Zenstory also combines market/deconstruction assumptions, runtime adapters, hooks, multi-agent deployment, and a web-novel-specific workflow. Those are valuable, but they make it harder to isolate the state design until the simpler continuity comparison has been documented.

**Initial recommended order:** Lensetek → Dewhurst → Zenstory → Haowjy → JeroTan → wgwtest → Rhavekost. This sequence is intentionally adjustable based on findings from earlier analyses.

## Skill-List Audit

The current skill list should remain recognizable during Phase 1. The audit does **not** recommend splitting `continuity` yet.

| Current Skill | Phase 1 Disposition |
|---|---|
| `fiction-orchestrator` | Keep; treat as routing/control rather than a linear first step |
| `concept-development` | Keep; evaluate whether constitution/clarification should be separate capabilities |
| `worldbuilding` | Keep |
| `character-development` | Keep |
| `narrative-architecture` | Keep |
| `scene-planning` | Keep |
| `scene-writing` | Keep |
| `continuity` | Keep as one skill pending source comparisons |
| `prose-editing` | Keep; evaluate whether developmental review needs a distinct skill/mode |
| `reader-simulation` | Keep; evaluate explicit context-isolation requirements |

Potential additions such as `story-review`, `context-manager`, `story-state-manager`, or `project-maintenance` should remain **candidate capabilities** rather than committed skill names until the analyses are complete.

## Core-Principle Improvements to Evaluate

### Persistent State

Current principle: persistent, checkable story state.

Candidate refinements to test against the source analyses:

- distinguish static canon from dynamic current state;
- explicitly track unresolved questions, promises/payoffs, and continuity risks;
- define authority when summaries, structured state, and prose disagree;
- define how revision of an earlier chapter propagates into later state;
- distinguish author preferences/style memory from story truth.

### Context Management

Current LOD/sharding principle should be preserved. Candidate refinements:

- define a smallest-sufficient-context rule;
- load near-field prose when language/style fidelity matters;
- use summaries/structured cards for distant material;
- define what wins when a summary conflicts with manuscript prose;
- make context selection observable enough to diagnose omissions.

### Human-in-the-Loop

Lensetek's phase gates remain valuable. Candidate refinements from Rhavekost and Zenstory:

- direction-selection gates before committing among creative alternatives;
- canon-promotion gates for exploratory material;
- explicit scope-transition gates (planning → drafting, diagnosis → rewriting);
- stop after an audit unless the author asks to apply fixes;
- surface fallback or degraded runtime behavior instead of silently changing modes.

### Deterministic vs. Judgment-Based Evaluation

A useful **candidate principle for discussion** is: **deterministic means executable; judgment means judgment.**

Schema validation, reference integrity, timeline ordering, known state, and measurable counts can be deterministic when backed by executable tooling. Character motivation, pacing quality, prose quality, emotional payoff, and voice fidelity remain model/human judgment and should not be presented as mechanically proven if this principle is adopted.

## Licensing and Attribution Register

The following links should be preserved in the source analyses and later attribution decisions.

| Repository | License | NOTICE / Attribution | Notes |
|---|---|---|---|
| `lensetek/Fiction-book-agent-skills` | README links to [`LICENSE`](https://github.com/lensetek/Fiction-book-agent-skills/blob/main/LICENSE), but the file currently returns 404 | No root `ATTRIBUTION.md` found | Treat public derivative redistribution as unresolved until license is clarified |
| `danjdewhurst/story-skills` | [`LICENSE`](https://github.com/danjdewhurst/story-skills/blob/main/LICENSE) — MIT | No root `ATTRIBUTION.md` found in this audit | Preserve MIT notice for copied/substantial portions |
| `haowjy/creative-writing-skills` | [`LICENSE`](https://github.com/haowjy/creative-writing-skills/blob/main/LICENSE) — Apache 2.0 | No root `NOTICE` or `ATTRIBUTION.md` found in this audit | Apache redistribution/modification obligations require special care if implementation text is reused |
| `JeroTan/novel-writer-english` | [`LICENSE`](https://github.com/JeroTan/novel-writer-english/blob/main/LICENSE) — MIT | [`ATTRIBUTION.md`](https://github.com/JeroTan/novel-writer-english/blob/main/ATTRIBUTION.md); no root NOTICE found | Preserve provenance to both JeroTan and upstream `wordflowlab/novel-writer-skills` for implementation-level reuse |
| `wgwtest/novel-writing` | [`LICENSE`](https://github.com/wgwtest/novel-writing/blob/main/LICENSE) — MIT | No root `NOTICE` or `ATTRIBUTION.md` found in this audit | Standard MIT notice obligations for copied/substantial portions |
| `rhavekost/author-toolkit` | [`LICENSE`](https://github.com/rhavekost/author-toolkit/blob/main/LICENSE) — MIT | [`ATTRIBUTION.md`](https://github.com/rhavekost/author-toolkit/blob/main/ATTRIBUTION.md); no root NOTICE found | Repository vendors third-party skills that retain their own licenses; provenance must be preserved when borrowing vendored material |
| `zenstory-ai/oh-story-claudecode` | [`LICENSE`](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/LICENSE) — MIT | No root `NOTICE` or `ATTRIBUTION.md` found in this audit | Standard MIT notice obligations for copied/substantial portions |

This table is a research record, not legal advice. Each source analysis should verify license state again at the time of analysis because repositories can change.

## Initial Recommended Phase 1 Source Order

This is a working comparison sequence, not a fixed commitment. It may be adjusted based on what earlier analyses reveal.

1. `lensetek/Fiction-book-agent-skills` — establish the baseline taxonomy, workflow phases, HITL gates, and all 16 responsibilities.
2. `danjdewhurst/story-skills` — compare persistent state and deterministic continuity directly against the Lensetek model.
3. `zenstory-ai/oh-story-claudecode` — evaluate layered state, transaction semantics, context filtering, runtime fallback, and author-memory separation after the simpler continuity comparison exists.
4. `haowjy/creative-writing-skills`
5. `JeroTan/novel-writer-english`
6. `wgwtest/novel-writing`
7. `rhavekost/author-toolkit`

## Time-Boxed Next Step

Once this audit branch is reviewed, stop architecture expansion and begin `docs/source-analysis/lensetek.md`. The Lensetek analysis should populate observed facts first; architecture and crosswalk decisions should be updated incrementally from evidence rather than continuing abstract design work.
