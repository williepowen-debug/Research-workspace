"""Pure dependency planning for explicitly supplied fixture commands and results."""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import Any, Iterable

from core import ID_PATTERNS, Finding, validate_command


RESULT_SUMMARY_FIELDS = {"command_id", "command_result", "reason_code"}


@dataclass(frozen=True)
class DurableResultSummary:
    command_id: str
    command_result: str
    reason_code: str | None


@dataclass
class DependencyPlan:
    completed: dict[str, DurableResultSummary] = field(default_factory=dict)
    ready: list[dict[str, Any]] = field(default_factory=list)
    waiting: dict[str, tuple[str, ...]] = field(default_factory=dict)
    rejections: dict[str, str] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        """Whether the supplied inventories are structurally usable."""
        return not self.findings


def plan_commands(
    submissions: Iterable[dict[str, Any]],
    durable_results: Iterable[dict[str, Any]] = (),
) -> DependencyPlan:
    """Plan one fixture acceptance pass without reading paths or writing results."""

    plan = DependencyPlan()
    commands, unavailable_commands = _inventory_commands(submissions, plan.findings)
    results, unavailable_results = _inventory_results(durable_results, plan.findings)
    plan.completed = dict(sorted(results.items()))

    pending = {
        command_id: command
        for command_id, command in commands.items()
        if command_id not in results and command_id not in unavailable_results
    }
    unavailable = unavailable_commands | unavailable_results

    rejected_results = {
        command_id
        for command_id, summary in results.items()
        if summary.command_result == "REJECTED"
    }
    accepted_results = set(results) - rejected_results

    for command_id in _cycle_members(pending):
        plan.rejections[command_id] = "DEPENDENCY_CYCLE"

    changed = True
    while changed:
        changed = False
        for command_id in sorted(pending):
            if command_id in plan.rejections:
                continue
            dependencies = pending[command_id]["depends_on"]
            if any(dependency in rejected_results or dependency in plan.rejections for dependency in dependencies):
                plan.rejections[command_id] = "DEPENDENCY_REJECTED"
                changed = True

    active = {
        command_id: command
        for command_id, command in pending.items()
        if command_id not in plan.rejections
    }
    direct_missing: dict[str, set[str]] = {}
    indegree = {command_id: 0 for command_id in active}
    successors: dict[str, set[str]] = {command_id: set() for command_id in active}

    for command_id, command in active.items():
        missing: set[str] = set()
        for dependency in command["depends_on"]:
            if dependency in accepted_results:
                continue
            if dependency in active:
                indegree[command_id] += 1
                successors[dependency].add(command_id)
            else:
                missing.add(dependency)
        direct_missing[command_id] = missing

    ready_heap = [
        (_command_key(command), command_id)
        for command_id, command in active.items()
        if indegree[command_id] == 0 and not direct_missing[command_id]
    ]
    heapq.heapify(ready_heap)
    ready_ids: set[str] = set()
    while ready_heap:
        _, command_id = heapq.heappop(ready_heap)
        ready_ids.add(command_id)
        plan.ready.append(active[command_id])
        for successor in sorted(successors[command_id]):
            indegree[successor] -= 1
            if indegree[successor] == 0 and not direct_missing[successor]:
                heapq.heappush(ready_heap, (_command_key(active[successor]), successor))

    waiting_ids = set(active) - ready_ids
    blockers = _waiting_blockers(waiting_ids, active, ready_ids, accepted_results, unavailable)
    plan.waiting = {
        command_id: tuple(sorted(blockers[command_id]))
        for command_id in sorted(waiting_ids)
    }

    plan.rejections = dict(sorted(plan.rejections.items()))
    plan.findings.sort(key=lambda finding: (finding.code, finding.message, finding.location))
    return plan


def _inventory_commands(
    submissions: Iterable[dict[str, Any]],
    findings: list[Finding],
) -> tuple[dict[str, dict[str, Any]], set[str]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    unavailable: set[str] = set()
    for command in submissions:
        if not isinstance(command, dict) or not isinstance(command.get("command_id"), str):
            findings.append(Finding("COMMAND_SCHEMA_INVALID", "submission has no usable command_id", "$submissions"))
            continue
        command_id = command["command_id"]
        grouped.setdefault(command_id, []).append(command)

    commands: dict[str, dict[str, Any]] = {}
    for command_id in sorted(grouped):
        candidates = grouped[command_id]
        if len(candidates) != 1:
            findings.append(Finding("DUPLICATE_COMMAND", command_id, "$submissions"))
            unavailable.add(command_id)
            continue
        command = candidates[0]
        validation = validate_command(command)
        if not validation.valid:
            codes = ",".join(sorted({finding.code for finding in validation.findings}))
            findings.append(Finding("COMMAND_SCHEMA_INVALID", f"{command_id}: {codes}", "$submissions"))
            unavailable.add(command_id)
            continue
        commands[command_id] = command
    return commands, unavailable


def _inventory_results(
    durable_results: Iterable[dict[str, Any]],
    findings: list[Finding],
) -> tuple[dict[str, DurableResultSummary], set[str]]:
    grouped: dict[str, list[DurableResultSummary]] = {}
    unavailable: set[str] = set()
    for value in durable_results:
        summary = _result_summary(value)
        if summary is None:
            command_id = value.get("command_id") if isinstance(value, dict) else None
            if isinstance(command_id, str) and ID_PATTERNS["command_id"].fullmatch(command_id):
                unavailable.add(command_id)
            findings.append(Finding("RESULT_INVENTORY_INVALID", "durable result summary is invalid", "$results"))
            continue
        grouped.setdefault(summary.command_id, []).append(summary)

    results: dict[str, DurableResultSummary] = {}
    for command_id in sorted(grouped):
        candidates = grouped[command_id]
        if len(candidates) != 1:
            findings.append(Finding("AUDIT_DUPLICATE_RESULT", command_id, "$results"))
            unavailable.add(command_id)
            continue
        results[command_id] = candidates[0]
    return results, unavailable


def _result_summary(value: Any) -> DurableResultSummary | None:
    if not isinstance(value, dict) or set(value) != RESULT_SUMMARY_FIELDS:
        return None
    command_id = value["command_id"]
    command_result = value["command_result"]
    reason_code = value["reason_code"]
    if not isinstance(command_id, str) or not ID_PATTERNS["command_id"].fullmatch(command_id):
        return None
    if command_result == "ACCEPTED" and reason_code is not None:
        return None
    if command_result == "REJECTED" and (not isinstance(reason_code, str) or not reason_code):
        return None
    if command_result not in {"ACCEPTED", "REJECTED"}:
        return None
    return DurableResultSummary(command_id, command_result, reason_code)


def _cycle_members(pending: dict[str, dict[str, Any]]) -> set[str]:
    adjacency = {
        command_id: tuple(
            sorted(
                dependency
                for dependency in command["depends_on"]
                if dependency in pending
            )
        )
        for command_id, command in pending.items()
    }
    reverse: dict[str, list[str]] = {command_id: [] for command_id in pending}
    for command_id, dependencies in adjacency.items():
        for dependency in dependencies:
            reverse[dependency].append(command_id)
    for command_id in reverse:
        reverse[command_id].sort()

    visited: set[str] = set()
    finish_order: list[str] = []
    for root in sorted(pending):
        if root in visited:
            continue
        visited.add(root)
        stack: list[tuple[str, int]] = [(root, 0)]
        while stack:
            command_id, next_index = stack[-1]
            dependencies = adjacency[command_id]
            if next_index < len(dependencies):
                dependency = dependencies[next_index]
                stack[-1] = (command_id, next_index + 1)
                if dependency not in visited:
                    visited.add(dependency)
                    stack.append((dependency, 0))
                continue
            finish_order.append(command_id)
            stack.pop()

    members: set[str] = set()
    assigned: set[str] = set()
    for root in reversed(finish_order):
        if root in assigned:
            continue
        component: list[str] = []
        stack = [root]
        assigned.add(root)
        while stack:
            command_id = stack.pop()
            component.append(command_id)
            for successor in reversed(reverse[command_id]):
                if successor not in assigned:
                    assigned.add(successor)
                    stack.append(successor)
        if len(component) > 1 or root in adjacency[root]:
            members.update(component)
    return members


def _waiting_blockers(
    waiting_ids: set[str],
    active: dict[str, dict[str, Any]],
    ready_ids: set[str],
    accepted_results: set[str],
    unavailable: set[str],
) -> dict[str, set[str]]:
    blockers: dict[str, set[str]] = {command_id: set() for command_id in waiting_ids}
    indegree = {command_id: 0 for command_id in waiting_ids}
    successors: dict[str, set[str]] = {command_id: set() for command_id in waiting_ids}
    for command_id in waiting_ids:
        for dependency in active[command_id]["depends_on"]:
            if dependency in accepted_results or dependency in ready_ids:
                continue
            if dependency in waiting_ids:
                indegree[command_id] += 1
                successors[dependency].add(command_id)
            else:
                blockers[command_id].add(dependency)

    queue = [command_id for command_id in waiting_ids if indegree[command_id] == 0]
    heapq.heapify(queue)
    visited: set[str] = set()
    while queue:
        command_id = heapq.heappop(queue)
        visited.add(command_id)
        for successor in sorted(successors[command_id]):
            blockers[successor].update(blockers[command_id])
            indegree[successor] -= 1
            if indegree[successor] == 0:
                heapq.heappush(queue, successor)

    for command_id in waiting_ids - visited:
        blockers[command_id].update(
            dependency
            for dependency in active[command_id]["depends_on"]
            if dependency in unavailable or dependency not in ready_ids
        )
    return blockers


def _command_key(command: dict[str, Any]) -> tuple[str, str]:
    return command["submitted_at"], command["command_id"]
