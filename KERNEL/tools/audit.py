#!/usr/bin/env python3
"""Fixture-only additions-only and durable-result audit checks."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Protocol

from core import ID_PATTERNS, Finding, validate_command


LIVE_KERNEL_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = LIVE_KERNEL_ROOT.parent
FULL_SHA = re.compile(r"[0-9a-f]{40}")
PROTECTED_PREFIXES = (
    "KERNEL/audit/commands/",
    "KERNEL/shadow/events/",
)
RESULT_SUMMARY_FIELDS = {"command_id", "command_result", "reason_code"}


@dataclass
class AuditCheck:
    """One check result with an explicit evidence perimeter."""

    name: str
    perimeter: str
    findings: list[Finding] = field(default_factory=list)
    unknowns: list[Finding] = field(default_factory=list)
    checked_commits: tuple[str, ...] = ()

    @property
    def status(self) -> str:
        if self.findings:
            return "EXCEPTION"
        if self.unknowns:
            return "UNKNOWN"
        return "PASS"

    @property
    def blocking(self) -> bool:
        return self.status != "PASS"


class GitHistoryBoundary(Protocol):
    """Minimum injected Git surface needed by the additions-only check."""

    def resolve_commit(self, commit: str) -> str | None: ...

    def is_ancestor(self, base: str, head: str) -> bool | None: ...

    def commits_between(self, base: str, head: str) -> list[str] | None: ...

    def commit_changes(self, commit: str) -> list[tuple[str, str]] | None: ...


class SubprocessGitHistoryBoundary:
    """Read an injected synthetic Git history without consulting live history."""

    def __init__(
        self,
        repository: str | Path,
        *,
        forbidden_repository_root: str | Path = REPOSITORY_ROOT,
    ):
        self.repository = Path(repository).resolve()
        repository_root = Path(forbidden_repository_root).resolve()
        if (
            self.repository == repository_root
            or repository_root in self.repository.parents
            or self.repository in repository_root.parents
        ):
            raise ValueError("fixture audit cannot inspect the live repository tree")

    def _run(self, *args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["git", "-C", str(self.repository), *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )

    def resolve_commit(self, commit: str) -> str | None:
        if not FULL_SHA.fullmatch(commit):
            return None
        completed = self._run("rev-parse", "--verify", f"{commit}^{{commit}}")
        resolved = completed.stdout.strip().decode("ascii", errors="ignore")
        return resolved if completed.returncode == 0 and FULL_SHA.fullmatch(resolved) else None

    def is_ancestor(self, base: str, head: str) -> bool | None:
        completed = self._run("merge-base", "--is-ancestor", base, head)
        if completed.returncode == 0:
            return True
        if completed.returncode == 1:
            return False
        return None

    def commits_between(self, base: str, head: str) -> list[str] | None:
        completed = self._run("rev-list", "--reverse", "--topo-order", f"{base}..{head}")
        if completed.returncode != 0:
            return None
        commits = completed.stdout.decode("ascii", errors="ignore").splitlines()
        return commits if all(FULL_SHA.fullmatch(commit) for commit in commits) else None

    def commit_changes(self, commit: str) -> list[tuple[str, str]] | None:
        completed = self._run(
            "diff-tree",
            "--no-commit-id",
            "--name-status",
            "-z",
            "-r",
            "-m",
            "--no-renames",
            commit,
        )
        if completed.returncode != 0:
            return None
        fields = completed.stdout.split(b"\0")
        if fields and fields[-1] == b"":
            fields.pop()
        if len(fields) % 2:
            return None
        changes: list[tuple[str, str]] = []
        try:
            for index in range(0, len(fields), 2):
                status = fields[index].decode("ascii")
                path = fields[index + 1].decode("utf-8")
                changes.append((status, path))
        except UnicodeDecodeError:
            return None
        return changes


def verify_additions_only(
    git: GitHistoryBoundary,
    base: str,
    head: str,
    *,
    protected_prefixes: tuple[str, ...] = PROTECTED_PREFIXES,
) -> AuditCheck:
    """Block any non-addition to protected result paths in ``base..head``."""

    perimeter = (
        f"history={base}..{head} "
        f"protected={','.join(protected_prefixes)}"
    )
    check = AuditCheck("additions-only", perimeter)
    if git.resolve_commit(base) != base or git.resolve_commit(head) != head:
        check.unknowns.append(
            Finding("AUDIT_HISTORY_UNKNOWN", "base and head must resolve as exact full commits", "$history")
        )
        return check
    ancestor = git.is_ancestor(base, head)
    if ancestor is not True:
        message = "base is not an ancestor of head" if ancestor is False else "ancestry could not be read"
        check.unknowns.append(Finding("AUDIT_HISTORY_UNKNOWN", message, "$history"))
        return check
    commits = git.commits_between(base, head)
    if commits is None:
        check.unknowns.append(Finding("AUDIT_HISTORY_UNKNOWN", "commit range could not be read", "$history"))
        return check
    check.checked_commits = tuple(commits)
    for commit in commits:
        changes = git.commit_changes(commit)
        if changes is None:
            check.unknowns.append(
                Finding("AUDIT_HISTORY_UNKNOWN", f"changes could not be read for {commit}", "$history")
            )
            continue
        for status, path in changes:
            if not path.startswith(protected_prefixes) or status == "A":
                continue
            check.findings.append(
                Finding(
                    "ADDITIONS_ONLY_VIOLATION",
                    f"{status} {path} at {commit}",
                    path,
                )
            )
    check.findings.sort(key=lambda finding: (finding.location, finding.message))
    check.unknowns.sort(key=lambda finding: (finding.location, finding.message))
    return check


def verify_durable_results(
    submissions: Iterable[dict[str, Any]],
    durable_results: Iterable[dict[str, Any]],
    *,
    pass_reported_success: bool,
) -> AuditCheck:
    """Reconcile explicit fixture inventories against the durable-result invariant."""

    submission_values = list(submissions)
    result_values = list(durable_results)
    check = AuditCheck(
        "durable-results",
        (
            f"explicit_submissions={len(submission_values)} "
            f"explicit_results={len(result_values)} "
            f"pass_reported_success={str(pass_reported_success).lower()}"
        ),
    )
    submission_ids: dict[str, int] = {}
    for index, submission in enumerate(submission_values):
        if not isinstance(submission, dict) or not isinstance(submission.get("command_id"), str):
            check.findings.append(
                Finding("COMMAND_SCHEMA_INVALID", "submission has no usable command_id", f"$submissions[{index}]")
            )
            continue
        command_id = submission["command_id"]
        validation = validate_command(submission)
        if not validation.valid:
            codes = ",".join(sorted({finding.code for finding in validation.findings}))
            check.findings.append(
                Finding("COMMAND_SCHEMA_INVALID", f"{command_id}: {codes}", f"$submissions[{index}]")
            )
            continue
        submission_ids[command_id] = submission_ids.get(command_id, 0) + 1

    for command_id, count in sorted(submission_ids.items()):
        if count > 1:
            check.findings.append(Finding("DUPLICATE_COMMAND", command_id, "$submissions"))

    result_ids: dict[str, int] = {}
    for index, result in enumerate(result_values):
        if not _valid_result_summary(result):
            check.findings.append(
                Finding("RESULT_INVENTORY_INVALID", "durable result summary is invalid", f"$results[{index}]")
            )
            continue
        command_id = result["command_id"]
        result_ids[command_id] = result_ids.get(command_id, 0) + 1

    for command_id, count in sorted(result_ids.items()):
        if count > 1:
            check.findings.append(Finding("AUDIT_DUPLICATE_RESULT", command_id, "$results"))
        if command_id not in submission_ids:
            check.findings.append(Finding("AUDIT_UNEXPECTED_RESULT", command_id, "$results"))

    for command_id in sorted(submission_ids):
        count = result_ids.get(command_id, 0)
        if count == 0 and pass_reported_success:
            check.findings.append(Finding("AUDIT_GAP", command_id, "$results"))
        elif count == 0:
            check.unknowns.append(
                Finding(
                    "AUDIT_COMPLETENESS_UNKNOWN",
                    f"no result and no successful-pass claim for {command_id}",
                    "$results",
                )
            )

    check.findings.sort(key=lambda finding: (finding.code, finding.message, finding.location))
    check.unknowns.sort(key=lambda finding: (finding.code, finding.message, finding.location))
    return check


def _valid_result_summary(value: Any) -> bool:
    if not isinstance(value, dict) or set(value) != RESULT_SUMMARY_FIELDS:
        return False
    command_id = value["command_id"]
    command_result = value["command_result"]
    reason_code = value["reason_code"]
    if not isinstance(command_id, str) or not ID_PATTERNS["command_id"].fullmatch(command_id):
        return False
    if command_result == "ACCEPTED":
        return reason_code is None
    if command_result == "REJECTED":
        return isinstance(reason_code, str) and bool(reason_code)
    return False


def _print_check(check: AuditCheck, pass_message: str) -> int:
    print(f"perimeter: check={check.name} {check.perimeter}")
    if check.status == "PASS":
        print(f"PASS: {pass_message}")
        return 0
    print(f"{check.status}: {check.name} verification did not pass")
    for finding in check.findings + check.unknowns:
        print(f"{finding.code}\t{finding.location}\t{finding.message}")
    return 1


def _fixture_json(
    path: Path,
    *,
    forbidden_repository_root: str | Path = REPOSITORY_ROOT,
) -> Any:
    resolved = path.resolve()
    repository_root = Path(forbidden_repository_root).resolve()
    if resolved == repository_root or repository_root in resolved.parents:
        raise ValueError("fixture audit inventories cannot be read from the live repository tree")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="check", required=True)
    additions = subparsers.add_parser("additions-only")
    additions.add_argument("--repository", type=Path, required=True)
    additions.add_argument("--live-repository-root", type=Path, required=True)
    additions.add_argument("--base", required=True)
    additions.add_argument("--head", required=True)
    results = subparsers.add_parser("durable-results")
    results.add_argument("--submissions", type=Path, required=True)
    results.add_argument("--results", type=Path, required=True)
    results.add_argument("--live-repository-root", type=Path, required=True)
    results.add_argument("--pass-reported-success", action="store_true")
    args = parser.parse_args()

    if args.check == "additions-only":
        try:
            check = verify_additions_only(
                SubprocessGitHistoryBoundary(
                    args.repository,
                    forbidden_repository_root=args.live_repository_root,
                ),
                args.base,
                args.head,
            )
            check.perimeter = f"repository={args.repository.resolve()} {check.perimeter}"
        except ValueError as exc:
            check = AuditCheck(
                "additions-only",
                f"repository={args.repository.resolve()} history={args.base}..{args.head}",
                findings=[Finding("AUDIT_BOUNDARY_REFUSED", str(exc), "$history")],
            )
        return _print_check(
            check,
            "protected accepted-event and receipt paths contain additions only in the compared history",
        )

    try:
        submissions = _fixture_json(
            args.submissions,
            forbidden_repository_root=args.live_repository_root,
        )
        durable_results = _fixture_json(
            args.results,
            forbidden_repository_root=args.live_repository_root,
        )
        if not isinstance(submissions, list) or not isinstance(durable_results, list):
            raise ValueError("fixture audit inventories must be JSON arrays")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        check = AuditCheck(
            "durable-results",
            f"submissions={args.submissions.resolve()} results={args.results.resolve()}",
            findings=[Finding("AUDIT_INVENTORY_UNREADABLE", str(exc), "$inventories")],
        )
        return _print_check(check, "every explicit fixture submission has exactly one durable result")
    check = verify_durable_results(
        submissions,
        durable_results,
        pass_reported_success=args.pass_reported_success,
    )
    return _print_check(
        check,
        "every explicit fixture submission has exactly one durable result",
    )


if __name__ == "__main__":
    raise SystemExit(main())
