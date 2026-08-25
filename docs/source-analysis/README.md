# Source Analysis

This folder contains detailed analysis documents for each source repository reviewed during the development of CodexWriter.

## Purpose

Each source repository (Lensetek, story-skills, creative-writing-skills, etc.) will be examined for its architecture, strengths, weaknesses, and licensing status. The analysis will inform the design decisions documented in `ARCHITECTURE.md` and the cross‑walk table in `docs/crosswalk.md`.

## File Format

Each source should have its own Markdown file named after the repository, e.g.:

- `lensetek.md`
- `danjdewhurst-story-skills.md`
- `haowjy-creative-writing-skills.md`
- `jero-tan-novel-writer-english.md`
- `wgwtest-novel-writing.md`
- `rhavekost-author-toolkit.md`
- `zenstory-ai.md`

Each file should include:

- **Repository URL**
- **License** (and any discrepancies, e.g., badge vs. actual file)
- **Overview** (high-level description)
- **Architecture** (key components, agent roles, file structure)
- **Strengths** (what it does well)
- **Weaknesses / Gaps** (what it lacks or does poorly)
- **Relevance to CodexWriter** (what we might adopt or adapt)
- **Detailed Notes** (quotes, specific observations, links to relevant files)

## Status

| Source | Status |
|--------|--------|
| lensetek/Fiction-book-agent-skills | Not started |
| danjdewhurst/story-skills | Not started |
| haowjy/creative-writing-skills | Not started |
| JeroTan/novel-writer-english | Not started |
| wgwtest/novel-writing | Not started |
| rhavekost/author-toolkit | Not started |
| zenstory-ai | Not started |

## Next Steps

- Populate each source analysis file with the details listed above.
- Use the cross‑walk table to map improvements to CodexWriter's planned skills.
- Update `ARCHITECTURE.md` as decisions are made.
