#!/usr/bin/env python3
"""Check live instruction surfaces for unsafe Gate C Git prescriptions."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


NEGATION = re.compile(r"\b(?:never|no|not|must\s+not|do\s+not|cannot|prohibit(?:ed|s)?)\b", re.I)
KERNEL_CONTEXT = re.compile(r"\bkernel\b|KERNEL/|outbox/kernel/submissions", re.I)


@dataclass(frozen=True)
class PolicyFinding:
    path: Path
    line_number: int
    code: str
    line: str


def _is_negated(line: str) -> bool:
    return bool(NEGATION.search(line))


def check_text(text: str, path: Path = Path("<text>")) -> list[PolicyFinding]:
    findings: list[PolicyFinding] = []
    kernel_nearby = False
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            kernel_nearby = False
            continue
        has_kernel_context = bool(KERNEL_CONTEXT.search(line))
        relevant = has_kernel_context or kernel_nearby
        negated = _is_negated(line)

        unsafe_stage = (
            re.search(r"\bgit\s+add\s+(?:-A|\.|KERNEL/?(?:\s|$)|AGENTS/<[^>]+>/?(?:\s|$))", line)
            or re.search(r"\bgit\s+commit\s+-a\b", line)
            or re.search(r"\bgit\s+(?:add|commit)\b.*(?:\*|\$\(|`)", line)
        )
        if relevant and unsafe_stage and not negated:
            findings.append(PolicyFinding(path, line_number, "KERNEL_UNSAFE_PATHSPEC", raw_line))

        automatic_write = re.search(
            r"\b(?:automatically|automatic|auto[- ]?)\b.*\b(?:commit|push)(?:es|ed|ing)?\b"
            r"|\b(?:commit|push)(?:es|ed|ing)?\b.*\b(?:automatically|automatic|auto[- ]?)\b",
            line,
            re.I,
        )
        if relevant and automatic_write and not negated:
            findings.append(PolicyFinding(path, line_number, "KERNEL_AUTO_GIT", raw_line))

        agent_kernel_grant = re.search(
            r"\b(?:agents?|domain agents?)\b.*\b(?:may|can|shall|are allowed to)\b.*"
            r"\b(?:edit|write|modify|commit|stage)\b",
            line,
            re.I,
        )
        if agent_kernel_grant and "KERNEL/" in line and not negated:
            findings.append(PolicyFinding(path, line_number, "AGENT_KERNEL_WRITE_GRANT", raw_line))

        kernel_nearby = has_kernel_context
    return findings


def check_paths(paths: Iterable[Path]) -> list[PolicyFinding]:
    findings: list[PolicyFinding] = []
    for path in paths:
        findings.extend(check_text(path.read_text(encoding="utf-8"), path))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="explicit instruction files to check")
    args = parser.parse_args()
    findings = check_paths(args.paths)
    if findings:
        print(f"EXCEPTION: Gate C Git policy; {len(findings)} unsafe prescription(s)")
        for finding in findings:
            print(f"{finding.path}:{finding.line_number}: {finding.code}: {finding.line.strip()}")
        print("perimeter: " + ", ".join(str(path) for path in args.paths))
        print("proves: listed instruction lines do not pass the registered Gate C Git policy patterns")
        print("does_not_prove: runtime Git enforcement or absence of unsafe instructions outside the perimeter")
        return 1
    print("PASS: Gate C Git policy instruction check")
    print("perimeter: " + ", ".join(str(path) for path in args.paths))
    print("proves: no registered unsafe Gate C Git prescription appears in the explicit instruction files")
    print("does_not_prove: runtime Git enforcement or absence of unsafe instructions outside the perimeter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
