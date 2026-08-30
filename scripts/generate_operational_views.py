#!/usr/bin/env python3
"""Generate CodexWriter root operational views from canonical JSON control data."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "project" / "control"
GENERATED_NOTICE = "<!-- GENERATED FILE. Edit project/control/*.json, then run scripts/generate_operational_views.py. -->"
TASK_ID = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
VALID_TASK_STATES = {"pending", "in_progress", "verified", "blocked", "deferred"}


def label(key: str) -> str:
    return {"os": "OS"}.get(key, key.replace("_", " ").title())


def load(name: str) -> dict[str, Any]:
    with (CONTROL / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def _commit_sha(sha: str) -> bool:
    """Return True when sha is a 40-character hexadecimal Git SHA."""
    if not isinstance(sha, str) or len(sha) != 40:
        return False
    try:
        int(sha, 16)
    except (TypeError, ValueError):
        return False
    return True


def validate(
    roadmap: dict[str, Any],
    tasks: dict[str, Any],
    snapshot: dict[str, Any],
    decisions: dict[str, Any] | None = None,
) -> None:
    milestones = roadmap.get("milestones", [])
    milestone_ids = [item.get("id") for item in milestones]
    if len(milestone_ids) != len(set(milestone_ids)):
        raise ValueError("roadmap milestone IDs must be unique")

    task_ids: set[str] = set()
    for task in tasks.get("tasks", []):
        task_id = task.get("id", "")
        if not TASK_ID.fullmatch(task_id):
            raise ValueError(f"invalid task ID: {task_id!r}")
        if task_id in task_ids:
            raise ValueError(f"duplicate task ID: {task_id}")
        task_ids.add(task_id)
        if task.get("milestone") not in milestone_ids:
            raise ValueError(f"task {task_id} has unknown milestone")
        if task.get("status") not in VALID_TASK_STATES:
            raise ValueError(f"task {task_id} has invalid status")
        if task.get("status") == "verified":
            if not task.get("commit") or not task.get("evidence"):
                raise ValueError(f"verified task {task_id} requires commit and evidence")

    # history entries must carry a valid 40-character hex commit SHA
    for index, item in enumerate(snapshot.get("history", [])):
        sha = item.get("commit")
        if not _commit_sha(sha):
            raise ValueError(
                f"history entry {index} has invalid commit: {sha!r}"
            )

    # every blocked task must have a corresponding blocker entry
    blocker_task_ids = {b.get("task_id") for b in snapshot.get("blockers", [])}
    for task in tasks.get("tasks", []):
        if task.get("status") == "blocked":
            if task["id"] not in blocker_task_ids:
                raise ValueError(
                    f"blocked task {task['id']!r} has no snapshot blocker entry"
                )

    # every blocker task_id must reference an existing task
    for blocker in snapshot.get("blockers", []):
        tid = blocker.get("task_id")
        if not tid or tid not in task_ids:
            raise ValueError(
                f"blocker task_id {tid!r} does not reference an existing task"
            )

    # ruleset records must contain required fields with expected types
    for index, ruleset in enumerate(snapshot.get("rulesets", [])):
        if not isinstance(ruleset.get("id"), str) or not ruleset["id"]:
            raise ValueError(f"ruleset {index} missing string id")
        if not isinstance(ruleset.get("name"), str) or not ruleset["name"]:
            raise ValueError(f"ruleset {index} missing string name")
        if not isinstance(ruleset.get("status"), str) or not ruleset["status"]:
            raise ValueError(f"ruleset {index} missing string status")
        if not isinstance(ruleset.get("target"), str) or not ruleset["target"]:
            raise ValueError(f"ruleset {index} missing string target")
        if not isinstance(ruleset.get("requires_pull_requests"), bool):
            raise ValueError(f"ruleset {index} requires_pull_requests must be bool")
        if not isinstance(ruleset.get("requires_review_thread_resolution"), bool):
            raise ValueError(f"ruleset {index} requires_review_thread_resolution must be bool")
        if not isinstance(ruleset.get("requires_strict_verify_status_checks"), bool):
            raise ValueError(f"ruleset {index} requires_strict_verify_status_checks must be bool")
        if not isinstance(ruleset.get("blocks_force_pushes"), bool):
            raise ValueError(f"ruleset {index} blocks_force_pushes must be bool")
        if not isinstance(ruleset.get("blocks_deletion"), bool):
            raise ValueError(f"ruleset {index} blocks_deletion must be bool")
        if not isinstance(ruleset.get("requires_approvals"), int) or isinstance(ruleset.get("requires_approvals"), bool):
            raise ValueError(f"ruleset {index} requires_approvals must be int")
        if ruleset.get("requires_approvals", 0) < 0:
            raise ValueError(f"ruleset {index} requires_approvals must be non-negative")
        if not isinstance(ruleset.get("bypass_actors"), list):
            raise ValueError(f"ruleset {index} bypass_actors must be list")

    if tasks.get("source_state_commit") != snapshot.get("source_state_commit"):
        raise ValueError("tasks and snapshot must identify the same source state commit")

    # decision IDs must be unique
    if decisions is not None:
        decision_ids = [d.get("id") for d in decisions.get("decisions", [])]
        if len(decision_ids) != len(set(decision_ids)):
            raise ValueError("decision IDs must be unique")


def progress_view(tasks: dict[str, Any], snapshot: dict[str, Any]) -> str:
    run = snapshot["run"]
    lines = [
        GENERATED_NOTICE,
        "",
        "# CodexWriter Operational Progress Log",
        "",
        "## 1. System State Reference",
        f"- Generated At: {snapshot['generated_at']}",
        f"- Active Branch: `{snapshot['active_branch']}`",
        f"- Active Profile: `{snapshot['active_profile']}`",
        f"- Source State Commit: `{snapshot['source_state_commit']}`",
        "- Commit Semantics: Source State Commit is the input state used to generate this view; it is not the self-referential commit containing this file.",
        "",
        "## 2. Active Run Delta",
        f"- Run ID: `{run['id']}`",
        f"- Status: `{run['status']}`",
        f"- Summary: {run['summary']}",
        "",
        "### Work Completed This Session",
    ]
    lines.extend(f"- {item}" for item in run.get("completed", []))
    lines.extend(["", "### Work In Progress"])
    lines.extend(f"- {item}" for item in run.get("work_in_progress", []))
    lines.extend([
        "",
        "### Result Reference",
        f"- Commit Reference: `{run['result_commit']}`" if run.get("result_commit") else "- Commit Reference: Resolved from Git history after commit",
        f"- Note: {run['result_reference']}",
        "",
        "## 3. Active Blockers & Open Decisions",
    ])
    for blocker in snapshot.get("blockers", []):
        task_link = f" (task `{blocker['task_id']}`)" if blocker.get("task_id") else ""
        lines.append(f"- [{blocker['id']}] ({blocker['severity']}): {blocker['description']}{task_link}")
    lines.extend(["", "## 4. Current Task Queue"])
    for task in tasks.get("tasks", []):
        marker = "x" if task["status"] == "verified" else " "
        lines.append(f"- [{marker}] `{task['id']}` — {task['title']} (`{task['status']}`)")
    lines.extend(["", "## 5. Short Log History"])
    for item in snapshot.get("history", []):
        lines.append(f"- [{item['date']}]: Commit `{item['commit']}` — {item['summary']}")
    return "\n".join(lines) + "\n"


def status_view(roadmap: dict[str, Any], tasks: dict[str, Any], snapshot: dict[str, Any]) -> str:
    all_tasks = tasks.get("tasks", [])
    lines = [
        GENERATED_NOTICE,
        "",
        "# CodexWriter Metric Snapshots",
        "",
        f"Generated from source state `{snapshot['source_state_commit']}` at {snapshot['generated_at']}.",
        "",
        "## 1. Milestone Metrics",
    ]
    for milestone in roadmap.get("milestones", []):
        members = [task for task in all_tasks if task["milestone"] == milestone["id"]]
        verified = sum(task["status"] == "verified" for task in members)
        total = len(members)
        percentage = round((verified / total) * 100) if total else 0
        lines.append(f"- {milestone['id']}: {milestone['name']}: {verified} / {total} Tasks Verified ({percentage}%)")
    lines.extend(["", "## 2. Itemized Verification Checklist"])
    for task in all_tasks:
        marker = "x" if task["status"] == "verified" else " "
        suffix = f" (`{task['commit'][:7]}`)" if task.get("commit") else ""
        lines.append(f"- [{marker}] {task['id']}: {task['title']}{suffix} — `{task['status']}`")
    lines.extend([
        "",
        "## 3. Metric Rules",
        "- Only tasks with status `verified` count toward completion.",
        "- A verified task must identify both a commit and at least one evidence path.",
        "- Percentages are computed from `project/control/tasks.json`; they are never manually entered here.",
    ])
    return "\n".join(lines) + "\n"


def roadmap_view(roadmap: dict[str, Any]) -> str:
    approval = roadmap["approval"]
    lines = [
        GENERATED_NOTICE,
        "",
        f"# {roadmap['title']}",
        "",
        f"- Roadmap Version: `{roadmap['roadmap_version']}`",
        f"- Status: `{roadmap['status']}`",
        f"- Approved By: {approval['approved_by']}",
        f"- Approved At: {approval['approved_at']}",
        f"- Approval Basis: {approval['basis']}",
        f"- Governing Source Commit: `{roadmap['governing_source_commit']}`",
        f"- Amendment Policy: {roadmap['amendment_policy']}",
        "",
        "## Core Architecture Milestones",
    ]
    for milestone in roadmap.get("milestones", []):
        lines.extend([
            "",
            f"### {milestone['id']}: {milestone['name']}",
            f"- Status: `{milestone['status']}`",
        ])
        for index, deliverable in enumerate(milestone.get("deliverables", []), start=1):
            lines.append(f"- Deliverable {milestone['id']}.{index}: {deliverable}")
        lines.append(f"- Exit Criteria: {milestone['exit_criteria']}")
    return "\n".join(lines) + "\n"


def environment_view(environment: dict[str, Any]) -> str:
    governance = environment["stable_governance"]
    snapshot = environment["current_snapshot"]
    lines = [
        GENERATED_NOTICE,
        "",
        "# CodexWriter Host Environment Configuration",
        "",
        f"- Document Version: `{environment['document_version']}`",
        f"- Owner: {environment['owner']}",
        f"- Ownership: {environment['ownership_policy']}",
        f"- Last Verified: {environment['last_verified']}",
        "",
        "## 1. Operating Governance",
        f"- Operating Model: {governance['operating_model']}",
        f"- Human Authority: {governance['human_authority']}",
        f"- Drift Policy: {environment['drift_policy']}",
        "",
        "## 2. Connected AI Agents",
    ]
    for key in ("worker", "judge"):
        agent = governance[key]
        lines.extend([
            f"### {agent['name']} — {key.title()}",
            f"- Role: {agent['role']}",
            f"- Repository Access: {agent['repository_access']}",
            "",
        ])
    host = snapshot["host"]
    lines.extend(["## 3. Hardware & OS Profile"])
    for key, value in host.items():
        lines.append(f"- {label(key)}: {value}")
    lines.extend(["", "## 4. Integrated Tooling Stack"])
    for key, value in snapshot["tooling"].items():
        lines.append(f"- {label(key)}: {value}")
    lines.extend(["", "## 5. Hermes Execution Limits"])
    for key, value in snapshot["hermes_limits"].items():
        lines.append(f"- {label(key)}: {value}")
    lines.extend(["", "## 6. Browser Baseline"])
    for key, value in snapshot["browser"].items():
        lines.append(f"- {label(key)}: {value}")
    lines.extend(["", "## 7. Security and Data Handling"])
    lines.extend(f"- {rule}" for rule in environment.get("security_rules", []))
    return "\n".join(lines) + "\n"


def render_all() -> dict[Path, str]:
    roadmap = load("roadmap.json")
    tasks = load("tasks.json")
    snapshot = load("snapshot.json")
    decisions = load("decisions.json")
    environment = load("environment.json")
    validate(roadmap, tasks, snapshot, decisions)
    return {
        ROOT / "PROGRESS.md": progress_view(tasks, snapshot),
        ROOT / "STATUS.md": status_view(roadmap, tasks, snapshot),
        ROOT / "ROADMAP.md": roadmap_view(roadmap),
        ROOT / "ENVIRONMENT.md": environment_view(environment),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when generated views are stale")
    args = parser.parse_args()
    rendered = render_all()
    stale: list[str] = []
    for path, content in rendered.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.name)
        else:
            path.write_text(content, encoding="utf-8")
    if stale:
        print("stale generated views: " + ", ".join(stale), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
