# Crosswalk: Source Patterns → CodexWriter Layers

> This crosswalk maps patterns from the seven source analyses to the CodexWriter layers they inform. It is updated from source-analysis evidence and the ratified CodexWriter architecture recorded in the ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3`.
>
> **Decision boundary test:** A pattern may be labeled `Ratified` only if it was explicitly established by Blocks A, B, or C of the ratification addendum, or by F1 or F2. Compatibility with the ratified architecture is not enough. Appearance in the seven-source synthesis is not enough. Presence in the existing prototype is not enough.
>
> **Key:**
> - `Ratified` — explicitly established by the ratification addendum (Blocks A/B/C) or by F1/F2.
> - `Deferred detail` — the direction itself was ratified; specific thresholds, schemas, or contracts were deferred for later decision.
> - `Prototype only` — present in the existing provisional prototype; not yet ratified as architectural.
> - `Rejected` — a candidate considered and set aside.
> - `Source-informed candidate` — suggested by source evidence or synthesis, compatible with the ratified model, but not ratified.

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

These patterns exist in the existing provisional prototype but are not ratified as architectural. They may become ratified only through a separate decision.

| Prototype pattern | Source(s) | CodexWriter layer | Disposition | Category | Notes |
|---|---|---|---|---|---|
| Current working skill set of 11 `SKILL.md` files (10 core + 1 export extension) | Prototype | Skill inventory | Prototype only | Implementation guidance | Ten skills in the current working core (`fiction-orchestrator`, `concept-development`, `worldbuilding`, `character-development`, `narrative-architecture`, `scene-planning`, `scene-writing`, `continuity`, `prose-editing`, `reader-simulation`) plus one optional `export` extension. Not a ratified skill count. |
| JSON state model defined by four schema files and related skill contracts | Prototype, Zenstory influence | Durable state | Prototype only | Implementation guidance | `schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, `schemas/continuity.schema.json` with their skill contracts. The repository does not contain project instances named `story-state.json`, `character-state.json`, `scene-state.json`, or `continuity-state.json`. F1 classifies this as a provisional implementation prototype, not ratified. |
| Five-phase pipeline shape with phase gates | Lensetek, prototype | Workflow policy | Prototype only | Workflow policy | Present in the prototype; only the framework/story gate separation is ratified. |
| Specialist role taxonomy present in the prototype | Lensetek, prototype | Creative core + control/coordination | Prototype only | Architecture | Present in the prototype; not a ratified taxonomy. |
| Story-state vocabulary present in the prototype (POV, knows/doesn't-know, promise/payoff) | Lensetek, wgwtest, prototype | Creative core | Prototype only | Architecture | Present in the prototype vocabulary; not separately ratified beyond the authority model. |
| Thread Pull design | Project-specific Dust & Ash material | Optional project-profile behavior | Prototype only | Optional project-profile behavior | Designated Dust & Ash profile material; not ratified reusable-core architecture. |
| Voice-preservation guidance in scene-writing and prose-editing | Haowjy, prototype | Creative core | Prototype only | Implementation guidance | Present in the prototype. The separate author-memory authority category was ratified (above), but the exact voice-guidance implementation was not. |
| Phase approval gates as used in the prototype | Lensetek, prototype | Workflow policy | Prototype only | Workflow policy | Reference behavior; the exact gate set is prototype- or profile-specific, not ratified universal policy. |
| Story constitution or creative contract as a prototype concept | JeroTan, prototype exploration | Creative core | Prototype only | Workflow policy | Source-informed candidate concept; not a ratified core concept or finalized artifact/step boundary. |
| Clarification gate as a prototype concept | JeroTan, prototype exploration | Workflow policy | Prototype only | Workflow policy | Source-informed candidate concept; not a ratified workflow rule. |
| Project-root binding as a prototype behavior | JeroTan, prototype | Control/coordination | Prototype only | Architecture | Source-informed candidate; not ratified. |
| Editorial exact-text gate and escalation to author | JeroTan, prototype exploration | Editorial behavior | Prototype only | Workflow policy | Source-informed candidate; the ratified editorial model is batch-level approval, not an exact-text-match retry rule. |
| Exact-text-match retry | JeroTan, prototype exploration | Editorial behavior | Prototype only | Workflow policy | Source-informed candidate; not ratified. |
| Writer/critic/editor functional separation (vs. staffing distinct roles) | Haowjy, prototype exploration | Editorial behavior / reader simulation | Prototype only | Workflow policy | Functional separation is compatible with Block C; staffing those functions as distinct agents or roles was not ratified. |
| Non-canonical work sandbox as a prototype concept | Haowjy, JeroTan, prototype exploration | Authority model | Prototype only | Architecture | Source-informed candidate; the ratified model establishes non-canonical working material as outside canon, but the exact sandbox mechanism is not ratified. |
| Pre-write context reload as a prototype strategy | JeroTan, prototype | Context assembly | Prototype only | Workflow policy | Permitted strategy under the minimum responsibility; not a mandated contract. |
| Post-write state/context updates as a prototype strategy | Zenstory, prototype | Context assembly | Prototype only | Workflow policy | Permitted strategy under the minimum responsibility; not a mandated contract. |
| Document sharding as a prototype concept | JeroTan, prototype | Context assembly | Prototype only | Architecture | Permitted under the minimum responsibility; exact sharding boundaries are deferred. |
| Targeted full-text expansion as a prototype strategy | wgwtest, prototype | Context assembly | Prototype only | Workflow policy | The minimum responsibility establishes when full prose may be loaded; the exact expansion mechanism is not ratified. |
| Outline approval as a prototype workflow concept | Dewhurst, prototype | Workflow policy | Prototype only | Workflow policy | Source-informed reference behavior; not a ratified universal policy. |
| Audit vs. edit intent separation as a prototype concept | Dewhurst, prototype | Editorial behavior | Prototype only | Workflow policy | Source-informed candidate; the ratified model separates diagnosis and repair, but the exact audit/intent separation is not ratified. |
| Warnings that should be surfaced rather than silently rewritten | Dewhurst, prototype | Authority model / editorial behavior | Prototype only | Workflow policy | Source-informed candidate; the ratified model forbids silent overwrites, but the specific warning mechanism is not ratified. |
| Developmental/story review as a prototype candidate module | Haowjy, Rhavekost, JeroTan, prototype exploration | Evaluation | Prototype only | Workflow policy | Source-informed candidate; not a ratified distinct module. |
| World/character/plot iteration as a prototype workflow observation | Prototype | Creative core | Prototype only | Workflow policy | Existing prototype behavior; not a ratified workflow rule. |
| Narrative epistemology, POV-boundary machinery, and broader craft-review concepts | wgwtest, prototype exploration | Creative core + evaluation | Prototype only | Architecture + workflow policy | Source-informed candidates; the ratified model establishes machine-checkable authority principles, not the broader craft machinery. |
| Deterministic checker concept as a prototype goal | wgwtest, prototype | Evaluation | Prototype only | Architecture | The ratified quality principle distinguishes deterministic from judgment-based; an executable checker is not yet implemented. |
| Context LOD policy as a prototype goal | wgwtest, prototype | Context assembly | Prototype only | Workflow policy | The minimum responsibility is ratified; broader LOD policy is not. |
| Persistent story state and deterministic continuity tooling goal | Dewhurst, prototype | Durable state / continuity | Prototype only | Architecture | Persistent hybrid authority is ratified; the continuity implementation is not. |
| Atomic write ordering with state-last and replay/recovery tests (specific ordering and tests) | Zenstory, prototype exploration | Durable state / transactions | Prototype only | Architecture | Transaction boundary and atomic-application requirement are ratified (above). Specific state-last ordering and replay/recovery tests are source-informed implementation guidance, not ratified design. |

## Unratified source-informed candidates

These patterns were suggested by source evidence or synthesis, are compatible with the ratified model, but are not themselves ratified and are not yet present as prototype behavior. They are candidates for later decisions, not current architecture.

| Candidate pattern | Source(s) | CodexWriter layer | Disposition | Category |
|---|---|---|---|---|
| Story constitution / creative contract as a finalized core artifact or step | JeroTan | Creative core | Unratified source-informed candidate | Architecture (unresolved module/workflow question) |
| Clarification gate as a workflow stage or behavior | JeroTan | Workflow policy | Unratified source-informed candidate | Workflow policy (unresolved placement question) |
| Exact-text-match retry behavior | JeroTan | Editorial behavior | Unratified source-informed candidate | Workflow policy (not ratified; ratified model is batch-level approval) |
| Project-root binding as a ratified control rule | JeroTan | Control/coordination | Unratified source-informed candidate | Architecture |
| Writer/critic/editor staffing as distinct agent roles | Haowjy | Creative core | Unratified source-informed candidate | Workflow policy (functional separation is compatible with Block C; staffing distinct roles is not ratified) |
| Exact LOD schedule or universal pre-write/post-write procedure | wgwtest, JeroTan, Zenstory | Context assembly | Unratified source-informed candidate | Workflow policy (minimum responsibility is ratified; exact schedule/procedure is not) |
| Specific state-last write ordering | Zenstory | Durable state | Unratified source-informed candidate | Architecture (transaction boundary and atomic-application requirement are ratified; specific ordering is not) |
| Specific replay/recovery tests as a ratified implementation design | Zenstory | Durable state | Unratified source-informed candidate | Architecture (failure-detection and recovery rule are ratified; specific tests are not) |
| A distinct developmental/story-review skill or mode | Haowjy, Rhavekost, JeroTan | Evaluation | Unratified source-informed candidate | Workflow policy (unresolved module/workflow question) |

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
- Use `Ratified`, `Deferred detail`, `Prototype only`, and `Rejected` consistently.
- Do not imply that a ratified disposition authorizes copying source implementation text; implementation-level borrowing requires separate license/provenance handling.
- Put detailed architectural reasoning in `ARCHITECTURE.md`; keep this file as a compact evidence-backed cross-reference.

## State-architecture note

Do **not** choose a canonical storage model from this crosswalk. The ratified authority model is the layered hybrid recorded in the CodexWriter ratification addendum. The existing JSON state model is a provisional implementation prototype pending separately reviewed schema alignment. The exact schema set is deferred until the authorized file-by-file schema and skill impact plan is approved.
