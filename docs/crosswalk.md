# Crosswalk: Source Patterns → CodexWriter Layers

> This crosswalk maps the adopted patterns from the seven source analyses to the CodexWriter layers they inform. It is updated from source-analysis evidence and the ratified architecture recorded in the CodexWriter ratification addendum at commit `70861e660d7d7e5261482834397f5f6a97aa43d3`.
>
> **Reading rule:** A pattern that is `Ratified` is part of the ratified architecture or the ratified minimum responsibility. A pattern that is `Deferred detail` is ratified in direction but not yet specified in full. A pattern that is `Prototype only` exists in the existing provisional prototype but is not yet ratified as architectural. A pattern that is `Rejected` is a candidate considered and set aside. Adopting a pattern in this crosswalk does not authorize copying source implementation text; implementation-level borrowing requires separate license/provenance handling in the relevant source analysis and `ATTRIBUTION.md`.

## Adopted-pattern crosswalk

| Adopted pattern | Source(s) | CodexWriter layer | Disposition | Category |
|---|---|---|---|---|
| Specialist role taxonomy (11-skill list + orchestrator) | Lensetek | Creative core + control/coordination | Ratified | Architecture |
| Five-phase pipeline with phase gates | Lensetek | Workflow policy | Ratified | Workflow policy |
| Story-state vocabulary (POV, knows/doesn't-know, promise/payoff, Thread Pull) | Lensetek, wgwtest, project-specific Dust & Ash material | Creative core | Ratified (vocabulary); project-profile behavior is Dust & Ash-specific | Architecture + optional project-profile behavior |
| Constitution / creative contract concept | JeroTan | Creative core | Ratified (concept); exact artifact/step boundary deferred | Architecture (deferred detail) |
| Clarification gate | JeroTan | Workflow policy | Ratified (concept); exact placement deferred | Workflow policy (deferred detail) |
| Document sharding | JeroTan | Context assembly | Ratified (minimum responsibility); exact sharding boundaries deferred | Architecture (deferred detail) |
| Context reload before writing | JeroTan | Context assembly | Ratified (minimum responsibility) | Workflow policy |
| Editorial exact-text gate and escalation to author | JeroTan | Editorial behavior | Ratified | Workflow policy |
| Exact-text-match retry | JeroTan | Editorial behavior | Ratified | Workflow policy |
| Project-root binding | JeroTan | Control/coordination | Ratified | Architecture |
| Context-blind reader testing (manuscript-only first pass) | Rhavekost | Reader simulation | Ratified | Workflow policy |
| Focused editorial passes with stopping points | Rhavekost | Editorial behavior | Ratified | Workflow policy |
| Shared finding format with confidence | Rhavekost | Editorial behavior / continuity | Ratified (concept); exact shared envelope deferred | Implementation guidance (deferred detail) |
| Diagnostic-to-repair approval flow | Rhavekost | Editorial behavior | Ratified | Workflow policy |
| Reader/critic/editor separation | Haowjy | Reader simulation / editorial behavior | Ratified | Workflow policy |
| Voice preservation and style references | Haowjy | Creative core + author memory | Ratified (voice guidance in skills); author-memory layer ratified in principle, not yet implemented | Architecture (author-memory layer not yet implemented) |
| Writer/critic/editor staffing roles | Haowjy | Creative core | Ratified (concept) | Workflow policy |
| Bounded state authority and derived views | Zenstory | Authority model | Ratified | Architecture |
| Expected-revision stale rejection | Zenstory | Durable state / transactions | Ratified (rule); transaction tooling not yet implemented | Architecture (not yet implemented) |
| Atomic write ordering with state-last and replay/recovery tests | Zenstory | Durable state / transactions | Ratified (rule); transaction tooling not yet implemented | Architecture (not yet implemented) |
| Separate author memory | Zenstory | Authority model | Ratified (authority category); author-profile store not yet implemented | Architecture (not yet implemented) |
| Runtime portability and host adapter boundary | Zenstory | Portability | Ratified | Architecture |
| Layered state management and revision counters | Zenstory | Durable state | Ratified (authority model); exact schema reclassification deferred | Architecture (deferred detail) |
| Narrative epistemology, POV boundaries, context LOD | wgwtest | Creative core + context assembly | Ratified (concept + minimum responsibility) | Architecture + workflow policy |
| Deterministic checker concept | wgwtest | Evaluation | Ratified (quality principle); executable validator not yet implemented | Architecture (not yet implemented) |
| Author overrides and prose-over-summary rule | wgwtest | Authority model | Ratified | Architecture |
| Targeted full-text expansion | wgwtest | Context assembly | Ratified (minimum responsibility) | Workflow policy |
| Outline approval | Dewhurst | Workflow policy | Ratified | Workflow policy |
| Audit vs. edit intent separation | Dewhurst | Editorial behavior | Ratified | Workflow policy |
| Warnings that should be surfaced rather than silently rewritten | Dewhurst | Authority model / editorial behavior | Ratified | Workflow policy |
| Persistent story state and deterministic continuity tooling concept | Dewhurst | Durable state / continuity | Ratified (concept + priority); executable continuity engine, tests, CLI, CI not yet implemented | Architecture (not yet implemented) |
| Phase approval gates as reference | Lensetek | Workflow policy | Ratified (reference); exact gate set is project/profile-specific | Workflow policy |
| Existing JSON state model (`story-state.json`, `character-state.json`, `scene-state.json`, `continuity-state.json`) | Existing prototype, influenced by Zenstory | Durable state | Prototype only (provisional implementation prototype, not ratified) | Implementation guidance (provisional prototype) |
| Single-authoritative-JSON-state model | Zenstory (candidate only) | Durable state | Rejected as the ratified model | Architecture (rejected candidate) |
| Markdown-alone-authoritative model | Candidate considered and set aside | Authority model | Rejected as the ratified model | Architecture (rejected candidate) |
| JSON-alone-authoritative model | Candidate considered and set aside | Authority model | Rejected as the ratified model | Architecture (rejected candidate) |
| Fully delegated PR-only mode without interactive gates | Candidate considered and set aside | HITL behavior | Rejected | Workflow policy (rejected candidate) |
| Fully interactive per-sentence edit model | Candidate considered and set aside | HITL behavior | Rejected | Workflow policy (rejected candidate) |
| Single-authority model collapsing canon/experience distinction | Candidate considered and set aside | Authority model | Rejected | Architecture (rejected candidate) |

## Crosswalk usage

- Keep this file concise: map adopted patterns to their sources, layers, dispositions, and categories.
- Update rows only when source-analysis evidence or the ratified architecture supports the change.
- Use `Ratified`, `Deferred detail`, `Prototype only`, and `Rejected` consistently.
- Do not imply that a ratified disposition authorizes copying source implementation text; implementation-level borrowing requires separate license/provenance handling.
- Put detailed architectural reasoning in `ARCHITECTURE.md`; keep this file as a compact evidence-backed cross-reference.

## State architecture note

Do **not** choose a canonical storage model from this crosswalk. The ratified authority model is the layered hybrid recorded in the CodexWriter ratification addendum. The existing JSON state model is a provisional implementation prototype pending separately reviewed schema alignment. The exact schema set is deferred until the authorized file-by-file schema and skill impact plan is approved.
