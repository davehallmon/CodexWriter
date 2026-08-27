# Crosswalk: Source Patterns → CodexWriter Layers

> This crosswalk maps patterns from the seven source analyses to the CodexWriter layers they inform, against the actual decision boundary established by the CodexWriter ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3` and the previously accepted F1/F2 decisions.
>
> **Decision boundary test:** A pattern may be labeled `Ratified` only if it is explicitly established by Blocks A, B, or C of the ratification addendum, or by the previously accepted F1/F2 decisions. Compatibility with the ratified architecture is not enough. Appearance in the seven-source synthesis is not enough. Presence in the prototype is not enough.
>
> **Disposition definitions:**
> - `Ratified` — explicitly established by the ratification addendum (Blocks A/B/C) or by F1/F2.
> - `Deferred detail` — the direction itself was ratified; the remaining detail was deferred until later review or implementation.
> - `Prototype only` — present in the existing provisional prototype, but not yet ratified as architectural.
> - `Unratified source-informed candidate` — suggested by source evidence or synthesis, compatible with the ratified model, but not itself ratified.
> - `Rejected` — a candidate considered and set aside.
>
> **Category definitions:**
> - `Architecture` — part of the ratified architectural model or authority structure.
> - `Workflow policy` — a ratified or prototype workflow rule.
> - `Implementation guidance` — source-informed guidance for eventual implementation.
> - `Optional project-profile behavior` — Dust & Ash profile-specific, not ratified reusable-core architecture.
>
> Adopting a pattern in this crosswalk does not authorize copying source implementation text; implementation-level borrowing requires separate license/provenance handling in the relevant source analysis and `ATTRIBUTION.md`.

## Ratified patterns

| Adopted pattern | Source(s) | CodexWriter layer | Disposition | Category | Supporting decision |
|---|---|---|---|---|---|
| Layered hybrid authority model | Synthesis of seven sources | Authority model | Ratified | Architecture | Addendum Block A |
| Markdown authority for exact approved narrative wording | Synthesis; wgwtest prose-over-summary; Rhavekost reader isolation | Authority model | Ratified | Architecture | Addendum Block A — approved Markdown manuscript files are authoritative for exact narrative wording |
| Structured-state authority for explicitly governed, approved machine-checkable canon and workflow fields | Synthesis; Zenstory layered state; Dewhurst state-vocabulary | Authority model | Ratified | Architecture | Addendum Block A — approved structured state is authoritative for machine-checkable intended canon facts and workflow fields the schema explicitly governs |
| Derived views and registries as non-authoritative and rebuildable | Synthesis; Zenstory derived views | Authority model | Ratified | Architecture | Addendum Block A — derived views are never authoritative and contain no unique facts |
| No unique facts in derived views | Synthesis; Zenstory derived views | Authority model | Ratified | Architecture | Addendum Block A |
| Canon-promotion requires author approval and provenance | Synthesis | Authority model | Ratified | Architecture | Addendum Block A — promotion into canon requires author approval for narrative content plus transaction validation; structured canon record must retain provenance |
| Explicit conflict reconciliation and no silent overwrites | Synthesis; wgwtest prose-over-summary; Dewhurst warnings | Authority model | Ratified | Architecture | Addendum Block A — disagreement blocks promotion until reconciliation recorded; no layer may silently overwrite another |
| Transaction boundary and atomic-application requirement | Synthesis; Zenstory transactions | Durable state | Ratified | Architecture | Addendum Block A — one transaction owns the canonical transition; either the whole canonical transition is applied, or none of it is |
| Expected-revision stale-write rejection | Synthesis; Zenstory stale-revision protection | Durable state | Ratified | Architecture | Addendum Block A — expected-revision guard rejects stale sequential writes |
| Audit-history requirement | Synthesis; Dewhurst audit vs. edit intent separation | Durable state | Ratified | Architecture | Addendum Block A — audit record captures who submitted what, what was applied, and what the check marked |
| Separate author-memory authority category | Synthesis; Zenstory author memory; Haowjy style references | Authority model | Ratified | Architecture | Addendum Block A — author memory and preferences are a separate author-profile store, not story canon |
| Minimum context-assembly responsibility | Synthesis | Context assembly | Ratified | Workflow policy | Addendum Block B — minimum responsibility, five enumerated responsibilities |
| Source-revision/provenance labeling in context packages | Synthesis | Context assembly | Ratified | Workflow policy | Addendum Block B — every package records project/book identifiers, scope, source map, and revision markers |
| Full prose when exact wording, voice, ambiguity, or rhythm matters | Synthesis; wgwtest targeted full-text expansion | Context assembly | Ratified | Workflow policy | Addendum Block B — it may load full prose when language, voice, dialogue rhythm, ambiguity, or exact wording is the point |
| Context-blind manuscript-only reader baseline | Rhavekost; synthesis | Reader simulation | Ratified | Workflow policy | Addendum Block C — first pass is context-blind: manuscript only |
| Optional informed second reader pass | Rhavekost; synthesis | Reader simulation | Ratified | Workflow policy | Addendum Block C — optional second pass may load selected author context |
| Focused editorial scopes and stopping rules | Rhavekost; synthesis | Editorial behavior | Ratified | Workflow policy | Addendum Block C — each pass has a declared scope and a declared stopping rule |
| Diagnosis separated from repair | Rhavekost; synthesis | Editorial behavior | Ratified | Workflow policy | Addendum Block C — diagnosis and repair are separate |
| Exact batch-level editorial approval | JeroTan exact-text gate; synthesis | Editorial behavior | Ratified | Workflow policy | Addendum Block C — one coherent batch of exact proposed changes; author accepts, rejects, or modifies individual changes; apply only approved changes |
| Interactive and PR-boundary HITL modes | Synthesis | HITL behavior | Ratified | Workflow policy | Addendum Block C — two HITL modes with objective selection criteria |
| No silent HITL mode switching | Synthesis | HITL behavior | Ratified | Workflow policy | Addendum Block C — system must not switch modes silently |
| Framework approvals separated from story gates | F2; synthesis | Workflow policy | Ratified | Workflow policy | Addendum Block C + F2 — framework approvals belong to framework track; Dust & Ash story phase gates belong to Dust & Ash project track |
| Host-neutral versus host-adapter boundary | Synthesis; Zenstory runtime portability | Portability | Ratified | Architecture | Addendum Block B — host-neutral vs. host adapter |
| Deterministic versus judgment-based portability evidence | Synthesis | Portability | Ratified | Architecture | Addendum Block B — two explicit evidence classes |
| Two-host evidence requirement | Synthesis; portability reframed | Portability | Ratified | Architecture | Addendum Block B — portability demonstrated when same project/task produce comparable results on two hosts |
| Existing JSON state model is a provisional implementation prototype | F1; synthesis | Durable state | Ratified (as provisional) | Architecture | Addendum Block A context + F1 — current schemas remain provisional; not ratified |
| Reusable core separated from optional Dust & Ash profile | F2 | Framework scope | Ratified | Architecture | F2 — CodexWriter remains a reusable fiction-authoring core with optional project profiles |

## Deferred detail (ratified direction, deferred specification)

| Adopted pattern | Source(s) | CodexWriter layer | Disposition | Category | What is deferred |
|---|---|---|---|---|---|
| Exact schemas affected by the authority model | Synthesis | Durable state | Deferred detail | Architecture | Exact field-by-field reclassification into canon vs. editorial vs. derived is deferred until schema/skill-alignment review |
| Exact derived-view projection schemas | Synthesis | Authority model | Deferred detail | Architecture | Rebuildability is ratified; exact shapes of each derived view are deferred until implementation |
| Exact LOD thresholds and projection sizes for context sharding | Synthesis | Context assembly | Deferred detail | Architecture | Minimum responsibility is ratified; exact sharding boundaries, LOD levels, and projection sizes are deferred until after the vertical slice |
| Exact porting checklist | Synthesis; Zenstory | Portability | Deferred detail | Architecture | Host-neutral/host-adapter boundary and two-host evidence requirement are ratified; exact checklist is deferred until after the vertical slice |
| Exact continuity finding schema envelope | Rhavekost | Editorial behavior / continuity | Deferred detail | Implementation guidance | Shared envelope with confidence and determinism classification is recommended; exact envelope is deferred |

## Prototype-only patterns

These patterns exist in the existing provisional prototype but are **not** ratified as architectural. They are preserved as prototype behavior and may become ratified later only through a separate decision.

| Prototype pattern | Source(s) | CodexWriter layer | Disposition | Category | Notes |
|---|---|---|---|---|---|
| Current working skill set of eleven `SKILL.md` files (ten core + one export extension) | Prototype | Skill inventory | Prototype only | Implementation guidance | Ten core skills plus the optional `export` extension; not a ratified skill count |
| JSON state model defined by four schema files and related skill contracts | Prototype; Zenstory influence | Durable state | Prototype only | Implementation guidance | `schemas/story-state.schema.json`, `schemas/character-state.schema.json`, `schemas/scene-state.schema.json`, `schemas/continuity.schema.json`; no project state instances exist; F1 classifies this as provisional |
| Five-phase pipeline shape with phase gates | Lensetek; prototype | Workflow policy | Prototype only | Workflow policy | Present in the prototype; only the framework/story gate separation is ratified |
| Specialist role taxonomy present in the prototype | Lensetek; prototype | Control/coordination | Prototype only | Architecture | Present in the prototype; not a ratified taxonomy |
| Story-state vocabulary present in the prototype (POV, knows/doesn't-know, promise/payoff) | Lensetek; wgwtest; prototype | Creative core | Prototype only | Architecture | Present in the prototype vocabulary; not separately ratified beyond the authority model |
| Thread Pull design | Project-specific Dust & Ash material | Optional project-profile behavior | Prototype only | Optional project-profile behavior | Designated Dust & Ash profile material; not ratified reusable-core architecture |
| Voice-preservation guidance in scene-writing and prose-editing | Haowjy; prototype | Creative core | Prototype only | Implementation guidance | Present in the prototype; voice guidance exists; the separate author-memory authority category was ratified, but the exact voice guidance implementation was not |
| Phase approval gates as used in the prototype | Lensetek; prototype | Workflow policy | Prototype only | Workflow policy | Reference behavior; exact gate set is prototype- or profile-specific, not ratified universal policy |
| Story constitution or creative contract as a prototype concept | JeroTan; prototype exploration | Creative core | Prototype only | Workflow policy | Source-informed candidate concept; not a ratified core concept or finalized artifact/step boundary |
| Clarification gate as a prototype concept | JeroTan; prototype exploration | Workflow policy | Prototype only | Workflow policy | Source-informed candidate concept; not a ratified workflow rule |
| Project-root binding as a prototype behavior | JeroTan; prototype | Control/coordination | Prototype only | Architecture | Source-informed candidate; not ratified |
| Editorial exact-text gate and escalation to author | JeroTan; prototype exploration | Editorial behavior | Prototype only | Workflow policy | Source-informed candidate; the ratified editorial model is batch-level approval, not an exact-text-match retry rule |
| Writer/critic/editor functional separation (vs. staffing distinct roles) | Haowjy; prototype exploration | Editorial behavior / reader simulation | Prototype only | Workflow policy | Functional separation is compatible with Block C; staffing those functions as distinct agents or roles was not ratified |
| Non-canonical work sandbox as a prototype concept | Haowjy; JeroTan; prototype exploration | Authority model | Prototype only | Architecture | Source-informed candidate; the ratified model establishes non-canonical working material as outside canon, but the exact sandbox mechanism is not ratified |
| Pre-write context reload as a prototype strategy | JeroTan; prototype | Context assembly | Prototype only | Workflow policy | Permitted strategy under the minimum responsibility; not a mandated contract |
| Post-write state/context updates as a prototype strategy | Zenstory; prototype | Context assembly | Prototype only | Workflow policy | Permitted strategy under the minimum responsibility; not a mandated contract |
| Document sharding as a prototype concept | JeroTan; prototype | Context assembly | Prototype only | Architecture | Permitted under the minimum responsibility; exact sharding boundaries are deferred |
| Targeted full-text expansion as a prototype strategy | wgwtest; prototype | Context assembly | Prototype only | Workflow policy | The minimum responsibility establishes when full prose may be loaded; the exact expansion mechanism is not ratified |
| Outline approval as a prototype workflow concept | Dewhurst; prototype | Workflow policy | Prototype only | Workflow policy | Source-informed reference behavior; not a ratified universal policy |
| Audit vs. edit intent separation as a prototype concept | Dewhurst; prototype | Editorial behavior | Prototype only | Workflow policy | Source-informed candidate; the ratified model separates diagnosis and repair, but the exact audit/intent separation is not ratified |
| Warnings that should be surfaced rather than silently rewritten | Dewhurst; prototype | Authority model / editorial behavior | Prototype only | Workflow policy | Source-informed candidate; the ratified model forbids silent overwrites, but the specific warning mechanism is not ratified |
| Development/story review as a prototype candidate module | Haowjy; Rhavekost; JeroTan; prototype exploration | Evaluation | Prototype only | Workflow policy | Source-informed candidate; not a ratified distinct module |
| World/character/plot iteration as a prototype workflow observation | Prototype | Creative core | Prototype only | Workflow policy | Existing prototype behavior; not a ratified workflow rule |
| Narrative epistemology, POV-boundary machinery, and broader craft review concepts | wgwtest; prototype exploration | Creative core + evaluation | Prototype only | Architecture + workflow policy | Source-informed candidates; the ratified model establishes machine-checkable authority principles, not the broader craft machinery |
| Deterministic checker concept as a prototype goal | wgwtest; prototype | Evaluation | Prototype only | Architecture | Ratified quality principle distinguishes deterministic from judgment-based; executable checker not yet implemented |
| Context LOD policy as a prototype goal | wgwtest; prototype | Context assembly | Prototype only | Workflow policy | The minimum responsibility is ratified; broader LOD policy is not |
| Persistent story state and deterministic continuity tooling goal | Dewhurst; prototype | Durable state / continuity | Prototype only | Architecture | Persistent hybrid authority is ratified; the continuity implementation is not |

## Unratified source-informed candidates

These patterns are suggested by source evidence or synthesis, are compatible with the ratified model, but are **not** themselves ratified and are not yet present as prototype behavior. They are candidates for later decisions, not current architecture.

| Candidate pattern | Source(s) | CodexWriter layer | Disposition | Category |
|---|---|---|---|---|
| Story constitution / creative contract as a finalized core artifact or step | JeroTan | Creative core | Unratified source-informed candidate | Architecture (unresolved module/workflow question) |
| Clarification gate as a workflow stage or behavior | JeroTan | Workflow policy | Unratified source-informed candidate | Workflow policy (unresolved placement question) |
| Exact-text-match retry behavior | JeroTan | Editorial behavior | Unratified source-informed candidate | Workflow policy (not ratified; ratified model is batch-level approval) |
| Project-root binding as a ratified control rule | JeroTan | Control/coordination | Unratified source-informed candidate | Architecture |
| Writer/critic/editor staffing as distinct agent roles | Haowjy | Creative core | Unratified source-informed candidate | Workflow policy (functional separation is compatible with Block C; staffing distinct roles is not ratified) |
| Exact LOD schedule or universal pre-write/post-write procedure | wgwtest; JeroTan; Zenstory | Context assembly | Unratified source-informed candidate | Workflow policy (minimum responsibility is ratified; exact schedule/procedure is not) |
| Specific state-last write ordering | Zenstory | Durable state | Unratified source-informed candidate | Architecture (transaction boundary and atomic-application requirement are ratified; specific ordering is not) |
| Specific replay/recovery tests as a ratified implementation design | Zenstory | Durable state | Unratified source-informed candidate | Architecture (failure-detection and recovery rule are ratified; specific tests are not) |
| A distinct developmental/story-review skill or mode | Haowjy; Rhavekost; JeroTan | Evaluation | Unratified source-informed candidate | Workflow policy (unresolved module/workflow question) |
| A canonical state design other than the ratified layered hybrid | Various | Durable state | Rejected | Architecture (the layered hybrid is the ratified decision) |

## Rejected models

| Candidate model | Source(s) | CodexWalker layer | Disposition | Category |
|---|---|---|---|---|
| Single-authoritative-JSON-state model | Zenstory (candidate only) | Durable state | Rejected | Architecture (rejected candidate) |
| Markdown-alone-authoritative model | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |
| JSON-alone-authoritative model | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |
| Fully delegated PR-only mode without interactive gates | Candidate considered and set aside | HITL behavior | Rejected | Workflow policy (rejected candidate) |
| Fully interactive per-sentence edit model | Candidate considered and set aside | HITL behavior | Rejected | Workflow policy (rejected candidate) |
| Single-authority model collapsing canon/experience distinction | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |

## Crosswalk usage

- Keep this file concise: map patterns to their sources, layers, dispositions, categories, and supporting decisions.
- Use `Ratified` only for patterns explicitly established by Block A, Block B, Block C, F1, or F2. Every `Ratified` row above names its supporting decision.
- Use `Deferred detail` only when the direction itself was ratified and the remaining detail was deferred.
- Use `Prototype only` for patterns present in the existing provisional prototype but not ratified.
- Use `Unratified source-informed candidate` for source-suggested patterns that are compatible with the ratified model but not themselves ratified and not yet present as prototype behavior.
- Do not imply that a ratified disposition authorizes copying source implementation text; implementation-level borrowing requires separate license/provenance handling.
- Put detailed architectural reasoning in `ARCHITECTURE.md`; keep this file as a compact evidence-backed cross-reference.

## State architecture note

Do **not** choose a canonical storage model from this crosswalk. The ratified authority model is the layered hybrid recorded in the CodexWriter ratification addendum. The existing JSON state model is a provisional implementation prototype pending separately reviewed schema alignment. The exact schema set is deferred until the prospective file-by-file schema and skill impact plan is approved.
