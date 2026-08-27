# Crosswalk: Source Patterns → CodexWriter Layers

> This crosswalk maps patterns from the seven source analyses to the CodexWriter layers they inform. It is updated from source-analysis evidence and the ratified CodexWriter architecture recorded in the ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3`.
>
> **Decision boundary test:** A pattern may be labeled `Ratified` only if it was explicitly established by Blocks A, B, or C of the ratification addendum, or by F1 or F2. Compatibility with the ratified architecture is not enough. Appearance in the seven-source synthesis is not enough. Presence in the existing prototype is not enough.
>
> **Key:**
> - `Ratified` — explicitly established by the ratification addendum (Blocks A/B/C) or by F1/F2.
> - `Deferred detail` — the direction itself was ratified; specific thresholds, schemas, or contracts were deferred for later decision.
> - `Prototype only` — verifiably present in the tracked repository prototype, with a concrete file or contract as evidence; not yet ratified as architectural.
> - `Rejected` — a candidate considered and set aside.
> - `Source-informed candidate` — discussed, explored, recommended, or contemplated in source evidence or synthesis, compatible with the ratified model, but not ratified and not verifiably implemented in the tracked prototype.

## Historical snapshot notice

Sections 1–9 preserve the August 26 historical record; their operational
statuses and next steps are superseded. The August 27 ratification note
governs current status. Readers must not execute the old task list or
immediate sequence as current instructions.

## Ratified patterns

These are the patterns explicitly established by Blocks A, B, and C of the ratification addendum and by F1/F2.

| Adopted pattern | Source(s) | CodexWriter layer | Disposition | Category | Supporting decision |
|---|---|---|---|---|---|
| Layered hybrid authority model | Synthesis of seven sources | Core authority model | Ratified | Architecture | Addendum Block A |
| Markdown authority for exact approved narrative wording | Synthesis, wgwtest, Rhavekost reader isolation | Authority model | Ratified | Architecture | Addendum Block A |
| Structured-state authority for explicitly governed, approved machine-checkable canon and workflow fields | Synthesis, Zenstory, Dewhurst | Authority model | Ratified | Architecture | Addendum Block A |
| Derived views and registries as non-authoritative and rebuildable | Synthesis, Zenstory | Authority model | Ratified | Architecture | Addendum Block A |
| No unique facts in derived views | Synthesis, Zenstory | Authority model | Ratified | Architecture | Addendum Block A |
| Canon-promotion requires author approval and provenance | Synthesis | Authority model | Ratified | Architecture | Addendum Block A |
| Explicit conflict reconciliation; no silent overwrites | Synthesis, wgwtest, Dewhurst | Authority model | Ratified | Architecture | Addendum Block A |
| Transaction boundary and atomic-application requirement | Synthesis, Zenstory | Durable state | Ratified (rule only; tooling not yet built) | Architecture (not yet implemented) | Addendum Block A |
| Expected-revision stale-write rejection | Synthesis, Zenstory | Durable state | Ratified (rule only; tooling not yet built) | Architecture (not yet implemented) | Addendum Block A |
| Audit-history requirement | Synthesis, Dewhurst | Durable state | Ratified (rule only; tooling not yet built) | Architecture (not yet implemented) | Addendum Block A |
| Separate author-memory authority category | Synthesis, Zenstory, Haowjy | Authority model | Ratified (authority category); author-profile store not yet implemented | Architecture (not yet implemented) | Addendum Block A |
| Minimum context-assembly responsibility | Synthesis | Context assembly | Ratified | Architecture | Addendum Block B |
| Source-revision/provenance labeling in context packages | Synthesis | Context assembly | Ratified | Architecture | Addendum Block B |
| Full prose when exact wording, voice, ambiguity, or rhythm matters | Synthesis, wgwtest | Context assembly | Ratified (minimum responsibility) | Architecture | Addendum Block B |
| Context-blind manuscript-only reader baseline | Rhavekost, synthesis | Reader simulation | Ratified | Workflow policy | Addendum Block C |
| Optional informed second reader pass | Rhavekost, synthesis | Reader simulation | Ratified | Workflow policy | Addendum Block C |
| Focused editorial scopes and stopping rules | Rhavekost, synthesis | Editorial behavior | Ratified | Workflow policy | Addendum Block C |
| Diagnosis separated from repair | Rhavekost, synthesis | Editorial behavior | Ratified | Workflow policy | Addendum Block C |
| Exact batch-level editorial approval | JeroTan exact-text gate, synthesis | Editorial behavior | Ratified | Workflow policy | Addendum Block C |
| Interactive and PR-boundary HITL modes | Synthesis | HITL behavior | Ratified | Workflow policy | Addendum Block C |
| No silent HITL mode switching | Synthesis | HITL behavior | Ratified | Workflow policy | Addendum Block C |
| Framework approvals separated from story gates | F2, synthesis | Workflow policy | Ratified | Workflow policy | Addendum Block C + F2 |
| Host-neutral versus host-adapter boundary | Synthesis, Zenstory | Portability | Ratified | Architecture | Addendum Block B |
| Deterministic versus judgment-based portability evidence | Synthesis | Portability | Ratified | Architecture | Addendum Block B |
| Two-host evidence requirement | Synthesis | Portability | Ratified | Architecture | Addendum Block B |
| Existing JSON state model is a provisional implementation prototype | F1, synthesis | Durable state | Ratified (as provisional) | Architecture | Addendum Block A context + F1 |
| Reusable core separated from optional Dust & Ash profile | F2 | Framework scope | Ratified | Architecture | F2 |

## Deferred detail

The direction itself was ratified; the remaining detail was deferred for later decision.

| Adopted pattern | Source(s) | CodexWriter layer | Disposition | Category | What is deferred |
|---|---|---|---|---|---|
| Exact schemas affected by the authority model | Synthesis | Durable state | Deferred detail | Architecture | Field-by-field reclassification into canon vs. editorial vs. derived |
| Exact derived-view projection schemas | Synthesis | Authority model | Deferred detail | Architecture | Shapes of each derived view |
| Exact LOD thresholds and projection sizes for context sharding | Synthesis | Context assembly | Deferred detail | Architecture | Sharding boundaries, LOD levels, projection sizes |
| Exact porting checklist | Synthesis, Zenstory | Portability | Deferred detail | Architecture | Steps and tools for the second-host evidence |
| Exact continuity finding schema envelope | Rhavekost | Editorial behavior / continuity | Deferred detail | Implementation guidance | Shared envelope with confidence and determinism classification |

## Prototype-only patterns

These patterns are verifiably present in the existing provisional prototype in the tracked repository. They are not ratified as architectural. They may become ratified only through a separate decision.

| Prototype pattern | Source(s) | CodexWriter layer | Disposition | Category | Notes |
|---|---|---|---|---|---|
| Current working skill set of 11 `SKILL.md` files (10 core + 1 export extension) | Prototype | Skill inventory | Prototype only | Implementation guidance | **Evidence:** 11 `SKILL.md` files in `skills/` — `fiction-orchestrator`, `concept-development`, `worldbuilding`, `character-development`, `narrative-architecture`, `scene-planning`, `scene-writing`, `continuity`, `prose-editing`, `reader-simulation`, and `export`. Not a ratified skill count. |
| JSON state model defined by four schema files and related skill contracts | Prototype, Zenstory influence | Durable state | Prototype only | Implementation guidance | **Evidence:** `schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, `schemas/continuity.schema.json`. The repository does not contain project instances named `story-state.json`, `character-state.json`, `scene-state.json`, or `continuity-state.json`. F1 classifies this as a provisional implementation prototype, not ratified. |
| Five-phase pipeline shape with phase gates | Lensetek, prototype | Workflow policy | Prototype only | Workflow policy | **Evidence:** Phase structure and gate language in `skills/fiction-orchestrator/SKILL.md` (intent classification routing table and phase compatibility matrix referencing Gates 1–5) and `schemas/story-state.schema.json` (phase and phase_gate fields). Only the framework/story gate separation is ratified; exact gate set is prototype- or profile-specific and not yet executed. |
| Specialist role taxonomy present in the prototype | Lensetek, prototype | Creative core + control/coordination | Prototype only | Architecture | **Evidence:** Distinct `SKILL.md` files in `skills/` for each role. Present in the prototype; not a ratified taxonomy. |
| Story-state vocabulary present in the prototype (POV, knows/doesn't-know, promise/payoff) | Lensetek, wgwtest, prototype | Creative core | Prototype only | Architecture | **Evidence:** Vocabulary appears in `schemas/*.schema.json` and `skills/*/SKILL.md` files. Present in the prototype vocabulary; not separately ratified beyond the authority model. |
| Thread Pull design | Project-specific Dust & Ash material | Optional project-profile behavior | Prototype only | Optional project-profile behavior | **Evidence:** Three temporal threads (present/past/future "Thread Pulls") with no conventional flashbacks, tracked in `templates/scene-template.md`, `skills/narrative-architecture/SKILL.md`, `skills/scene-planning/SKILL.md`, and `skills/scene-writing/SKILL.md`. F2 designates this material for future extraction into the optional Dust & Ash project profile, but that extraction has not occurred. Not ratified reusable-core architecture. |
| Voice-preservation guidance in scene-writing and prose-editing | Haowjy, prototype | Creative core | Prototype only | Implementation guidance | **Evidence:** Guidance present in `skills/scene-writing/SKILL.md` and `skills/prose-editing/SKILL.md`. The separate author-memory authority category was ratified (above), but the exact voice-guidance implementation was not. |
| Phase approval gates as used in the prototype | Lensetek, prototype | Workflow policy | Prototype only | Workflow policy | **Evidence:** Gate structure referenced in `skills/*/SKILL.md` files and skill contracts. Reference behavior; exact gate set is prototype- or profile-specific, not ratified universal policy. |

## Unratified source-informed candidates

These patterns were discussed, explored, recommended, or contemplated in source evidence or synthesis. They are compatible with the ratified model, but are not themselves ratified and are not verifiably implemented in the tracked prototype. They are candidates for later decisions, not current architecture.

| Candidate pattern | Source(s) | CodexWriter layer | Disposition | Category |
|---|---|---|---|---|
| Story constitution / creative contract as a finalized core artifact or step | JeroTan | Creative core | Unratified source-informed candidate | Architecture (unresolved module/workflow question) |
| Clarification gate as a workflow stage or behavior | JeroTan | Workflow policy | Unratified source-informed candidate | Workflow policy (unresolved placement question) |
| Editorial exact-text gate and escalation to author | JeroTan | Editorial behavior | Unratified source-informed candidate | Workflow policy (not ratified; ratified model is batch-level approval) |
| Exact-text-match retry behavior | JeroTan | Editorial behavior | Unratified source-informed candidate | Workflow policy (not ratified; ratified model is batch-level approval) |
| Project-root binding as a ratified control rule | JeroTan | Control/coordination | Unratified source-informed candidate | Architecture |
| Writer/critic/editor staffing as distinct agent roles | Haowjy | Creative core | Unratified source-informed candidate | Workflow policy (functional separation is compatible with Block C; staffing distinct roles is not ratified) |
| Non-canonical work sandbox as a prototype concept | Haowjy, JeroTan | Authority model | Unratified source-informed candidate | Architecture (the ratified model establishes non-canonical working material as outside canon; the exact sandbox mechanism is not ratified) |
| Pre-write context reload as a prototype strategy | JeroTan, prototype | Context assembly | Unratified source-informed candidate | Workflow policy (permitted strategy under the minimum responsibility; not a mandated contract) |
| Post-write state/context updates as a prototype strategy | Zenstory, prototype | Context assembly | Unratified source-informed candidate | Workflow policy (permitted strategy under the minimum responsibility; not a mandated contract) |
| Document sharding as a prototype concept | JeroTan, prototype | Context assembly | Unratified source-informed candidate | Architecture (permitted under the minimum responsibility; exact sharding boundaries are deferred) |
| Targeted full-text expansion as a prototype strategy | wgwtest, prototype | Context assembly | Unratified source-informed candidate | Workflow policy (the minimum responsibility establishes when full prose may be loaded; the exact expansion mechanism is not ratified) |
| Outline approval as a prototype workflow concept | Dewhurst, prototype | Workflow policy | Unratified source-informed candidate | Workflow policy (source-informed reference behavior; not a ratified universal policy) |
| Audit vs. edit intent separation as a prototype concept | Dewhurst, prototype | Editorial behavior | Unratified source-informed candidate | Workflow policy (source-informed candidate; the ratified model separates diagnosis and repair, but the exact audit/intent separation is not ratified) |
| Warnings that should be surfaced rather than silently rewritten | Dewhurst, prototype | Authority model / editorial behavior | Unratified source-informed candidate | Workflow policy (source-informed candidate; the ratified model forbids silent overwrites, but the specific warning mechanism is not ratified) |
| Developmental/story review as a prototype candidate module | Haowjy, Rhavekost, JeroTan | Evaluation | Unratified source-informed candidate | Workflow policy (unresolved module/workflow question) |
| Narrative epistemology, POV-boundary machinery, and broader craft-review concepts | wgwtest, prototype exploration | Creative core + evaluation | Unratified source-informed candidate | Architecture + workflow policy (source-informed candidates; the ratified model establishes machine-checkable authority principles, not the broader craft machinery) |
| Deterministic checker concept as a prototype goal | wgwtest, prototype | Evaluation | Unratified source-informed candidate | Architecture (the ratified quality principle distinguishes deterministic from judgment-based; an executable checker is not yet implemented) |
| Context LOD policy as a prototype goal | wgwtest, prototype | Context assembly | Unratified source-informed candidate | Workflow policy (the minimum responsibility is ratified; broader LOD policy is not) |
| Persistent story state and deterministic continuity tooling goal | Dewhurst, prototype | Durable state / continuity | Unratified source-informed candidate | Architecture (persistent hybrid authority is ratified; the continuity implementation is not) |
| Atomic write ordering with state-last and replay/recovery tests | Zenstory, prototype exploration | Durable state / transactions | Unratified source-informed candidate | Architecture (transaction boundary and atomic-application requirement are ratified; specific state-last ordering and replay/recovery tests are source-informed implementation guidance, not ratified design) |
| Exact LOD schedule or universal pre-write/post-write procedure | wgwtest, JeroTan, Zenstory | Context assembly | Unratified source-informed candidate | Workflow policy (minimum responsibility is ratified; exact schedule/procedure is not) |

## Rejected models

These candidates were explicitly considered and set aside.

| Candidate model | Source(s) | CodexWriter layer | Disposition | Category |
|---|---|---|---|---|
| Single-authoritative-JSON-state model | Zenstory (candidate only) | Durable state | Rejected | Architecture (rejected candidate) |
| Markdown-alone-authoritative model | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |
| JSON-alone-authoritative model | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |
| Fully delegated PR-only mode without interactive gates | Candidate considered and set aside | HITL behavior | Rejected | Workflow policy (rejected candidate) |
| Fully interactive per-sentence edit model | Candidate considered and set aside | HITL behavior | Rejected | Workflow policy (rejected candidate) |
| Single-authority model collapsing canon/experience distinction | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |

## Crosswalk usage

- Keep this file concise: map adopted patterns to their sources, layers, dispositions, categories, and supporting decisions.
- Update rows only when source-analysis evidence or the ratified architecture supports the change.
- Use `Ratified`, `Deferred detail`, `Prototype only`, `Source-informed candidate`, and `Rejected` consistently.
- Do not imply that a ratified disposition authorizes copying source implementation text; implementation-level borrowing requires separate license/provenance handling.
- Put detailed architectural reasoning in `ARCHITECTURE.md`; keep this file as a compact evidence-backed cross-reference.

## State-architecture note

Do **not** choose a canonical storage model from this crosswalk. The ratified authority model is the layered hybrid recorded in the CodexWriter ratification addendum. The existing JSON state model is a provisional implementation prototype pending separately reviewed schema alignment. The exact schema set is deferred until a future, separately authorized file-by-file schema and skill impact plan is approved.
