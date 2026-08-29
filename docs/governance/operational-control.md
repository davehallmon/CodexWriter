# Operational Control Model

CodexWriter stores operational authority as canonical JSON under
`project/control/`. The root governance Markdown files are generated views and
must not contain unique facts.

## Authority boundaries

- `roadmap.json` is human-approved, change-controlled roadmap authority.
- `tasks.json` is the task and verification ledger.
- `decisions.json` records accepted governance and architectural decisions.
- `environment.json` is the human-owned environment baseline and drift policy.
- `snapshot.json` identifies the source state, active run, blockers, and short history.
- `PROGRESS.md`, `STATUS.md`, `ROADMAP.md`, and `ENVIRONMENT.md` are derived views.

The worker may update task, run, or evidence records only within an explicitly
authorized task. Roadmap, environment, architecture, merge, and release changes
require repository-owner review.

## Regeneration

Run:

```bash
python3 scripts/generate_operational_views.py
python3 scripts/generate_operational_views.py --check
python3 -m unittest discover -s tests -p "test_*.py"
```

The check command exits nonzero if a root view differs from the deterministic
projection of the control data. CI runs both the stale-view check and tests.

## Commit references

A tracked file cannot contain the SHA of the commit that contains that exact
file: changing the file changes the commit SHA. Generated views therefore use
`Source State Commit`, which identifies the input repository state. The result
commit is resolved from Git history after the commit exists.

## Repository settings

`CODEOWNERS` routes review but does not by itself require it. Repository owners
must enable branch protection or a ruleset for the canonical branch, require
pull requests and the `Governance Views / verify` check, prevent force pushes,
and require code-owner review.
