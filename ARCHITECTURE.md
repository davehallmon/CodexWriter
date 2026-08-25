# CodexWriter — Architecture

> This document describes the high-level design of CodexWriter.  
> It is a working draft and will evolve as we analyze source repositories and implement skills.

## 1. Goals

- Provide a modular, version-controlled suite of AI fiction-writing skills.
- Preserve persistent story state and deterministic continuity checks.
- Support specialist agent roles (planner, writer, editor, critic, reader simulator, etc.).
- Manage long-context projects through sharding, summaries, and level‑of‑detail loading.
- Keep a human author in the loop at key decision points.

## 2. Source Repositories Under Review

| Repository | Primary Strength | License Status |
|------------|------------------|----------------|
| lensetek/Fiction-book-agent-skills | Specialist role taxonomy | MIT badge, missing file |
| danjdewhurst/story-skills | Persistent story state, deterministic continuity | MIT |
| haowjy/creative-writing-skills | Writer/critic/editor separation, voice preservation | Apache 2.0 |
| JeroTan/novel-writer-english | Constitution, context reload, document sharding | MIT (translation) |
| wgwtest/novel-writing | Narrative epistemology, POV boundaries, context LOD | MIT |
| rhavekost/author-toolkit | Context-blind reader testing, separate editorial passes | To be confirmed |
| zenstory-ai | Additional inspiration | To be reviewed |

## 3. Proposed Skill Modules

The system will be organized into modular skills. The current tentative list includes:

- `fiction-orchestrator` — central coordinator
- `concept-development` — story idea intake and refinement
- `worldbuilding` — setting, rules, history
- `character-development` — psychology, voice, arcs
- `narrative-architecture` — plot and structure
- `scene-planning` — beat-by-beat outlines
- `scene-writing` — prose drafting
- `continuity` — canon tracking and validation
- `prose-editing` — line editing and polishing
- `reader-simulation` — context-blind beta reading

Additional skills may be added or split as the design matures.

## 4. Persistent Story State

CodexWriter will maintain structured artifacts for the story, including:

- Story Bible / Constitution
- Character state (including knowledge, voice, arcs)
- World facts and rules
- Timeline
- Plot arcs and promises/payoffs
- Scene state
- Continuity records

These will be stored as Markdown and/or structured JSON (schemas to be defined).

## 5. Context Management Strategy

Long projects will be handled through:

- Document sharding (splitting large files)
- Level-of-detail (LOD) loading: full prose near the current scene, summaries for distant material
- Pre-write context reload: only necessary state is loaded before each writing session
- Post-write state updates: ensure the persistent state reflects new developments

## 6. Workflow / Branch Strategy

- `main` — stable, reviewed releases
- `development` — ongoing integration branch
- Feature branches — per task or skill (created from `development`, merged via PR)

## 7. Next Steps

- Complete source analysis documents in `docs/source-analysis/`
- Build the cross-walk table in `docs/crosswalk.md`
- Define skill templates and schemas
- Implement first prototype skills (orchestrator + state manager)

---

*This document will be updated as decisions are made.*
