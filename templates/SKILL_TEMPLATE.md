# Skill Name

> Replace this line with a short summary of what the skill does and when it should be used.

## Purpose

Describe the specific role or outcome this skill produces.  
Example: “Generates a detailed world bible from a high‑level concept.”

## Inputs

- What context, files, or state does this skill require?
- Example: `story-concept.md`, `worldbuilding.md`, current story state

## Outputs

- What files or artifacts does this skill create or update?
- Example: new chapter draft, updated character state, continuity report

## Dependencies

- Which other skills or schemas does this skill rely on?
- Example: `worldbuilding`, `character-development`, `schema/story-state.schema.json`

## State Updates

- What persistent story state is updated by this skill?
- Example: updates `timeline.md`, adds new scene to `scene-index.md`

## Instructions

Provide clear, step‑by‑step instructions for the agent.  
Use numbered steps, include quality checks, and define any constraints.

1. Load required context and state.
2. Perform the primary task (e.g., draft a scene).
3. Self‑review against the skill’s quality checklist.
4. Update persistent story state.
5. Save outputs to the specified locations.

## Quality Checklist

- [ ] Does the output align with the story bible and current canon?
- [ ] Are all required files created/updated?
- [ ] Are continuity risks flagged or resolved?
- [ ] Is the output formatted according to project conventions?

## Notes

Any additional guidance, edge cases, or examples.
