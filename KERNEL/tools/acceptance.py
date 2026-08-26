#!/usr/bin/env python3
"""Integrated fixture-only Kernel acceptance runner with explicit check claims."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable

from core import REJECTION_REASONS, Finding, replay, validate_command, validate_transition
from native import GitBoundary, SubprocessGitBoundary, verify_native_references
from permissions import PermissionRegistry, authorize_command
from writer import FixtureResultStore, FixtureResultWriter, ResultConstructionError, WriteOutcome


CheckHook = Callable[[dict[str, Any]], "AcceptanceCheck"]
LIVE_REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class AcceptanceCheck:
    name: str
    status: str
    perimeter: str
    pass_proves: str
    pass_does_not_prove: str
    findings: tuple[Finding, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in {"PASS", "EXCEPTION", "UNKNOWN"}:
            raise ValueError("acceptance check status must be PASS, EXCEPTION, or UNKNOWN")


@dataclass
class AcceptanceRun:
    checks: list[AcceptanceCheck] = field(default_factory=list)
    outcomes: dict[str, WriteOutcome] = field(default_factory=dict)
    completed: set[str] = field(default_factory=set)
    waiting: dict[str, tuple[str, ...]] = field(default_factory=dict)

    @property
    def status(self) -> str:
        if any(check.status == "UNKNOWN" for check in self.checks):
            return "UNKNOWN"
        if any(check.status == "EXCEPTION" for check in self.checks):
            return "EXCEPTION"
        if any(outcome.state in {"BLOCKED", "REJECTED"} for outcome in self.outcomes.values()):
            return "EXCEPTION"
        if any(
            outcome.document is not None and outcome.document.get("command_result") == "REJECTED"
            for outcome in self.outcomes.values()
        ):
            return "EXCEPTION"
        return "PASS"


CLAIMS = {
    "schema": (
        "the supplied command matches the registered strict command contract",
        "research truth, authorization, native fidelity, or lifecycle legality",
    ),
    "permissions": (
        "the actor, owned path, identity, activity window, and capabilities satisfy the injected policy",
        "actor competence, substantive independence beyond policy, or native fidelity",
    ),
    "native-reference": (
        "the exact cited synthetic bytes and implemented material terms reconcile",
        "research quality, analytical persuasiveness, or trusted-history reachability beyond the supplied commit",
    ),
    "planning": (
        "the explicit submission/result inventories have the reported deterministic dependency disposition",
        "filesystem completeness, live submission discovery, or execution of any non-ready command",
    ),
    "lifecycle": (
        "the command is legal against the explicitly replayed accepted fixture history",
        "permission, native fidelity, or the absence of unsubmitted commands",
    ),
    "writer": (
        "the reported fixture result was atomically published or matched one prior durable result",
        "checks not listed as PASS for this command or authority outside the injected fixture store",
    ),
    "durability": (
        "the command has exactly one valid durable fixture result in the explicit store inventory",
        "that every native action was submitted or that the inventory covers undisclosed state",
    ),
    "aggregate": (
        "every required check instantiated by this fixture run passed and no selected command remains waiting",
        "live readiness, research truth, Gate C authorization, or state outside the printed fixture perimeter",
    ),
}


class FixtureAcceptanceRunner:
    """Orchestrate every required fixture check under one existing local lock."""

    def __init__(
        self,
        store: FixtureResultStore,
        *,
        writer_id: str,
        registry: PermissionRegistry,
        git: GitBoundary,
        event_id_for: Callable[[dict[str, Any]], str],
        recorded_at_for: Callable[[dict[str, Any]], str],
        required_hooks: Iterable[CheckHook] = (),
    ):
        self.store = store
        self.writer = FixtureResultWriter(store, writer_id=writer_id)
        self.registry = registry
        self.git = git
        self.event_id_for = event_id_for
        self.recorded_at_for = recorded_at_for
        self.required_hooks = tuple(required_hooks)

    def run(
        self,
        submissions: Iterable[dict[str, Any]],
        submission_paths: dict[str, str],
    ) -> AcceptanceRun:
        supplied = tuple(submissions)
        run = AcceptanceRun()
        grouped: dict[str, list[dict[str, Any]]] = {}
        invalid_ids: set[str] = set()
        halted_by_unknown: str | None = None

        for index, command in enumerate(supplied):
            command_id = command.get("command_id") if isinstance(command, dict) else None
            perimeter = f"submission_index={index} command_id={command_id!r}"
            validation = validate_command(command)
            if validation.valid:
                run.checks.append(self._check("schema", "PASS", perimeter))
                assert isinstance(command_id, str)
                grouped.setdefault(command_id, []).append(command)
            else:
                run.checks.append(self._check("schema", "EXCEPTION", perimeter, validation.findings))
                if isinstance(command_id, str):
                    grouped.setdefault(command_id, []).append(command)
                    invalid_ids.add(command_id)

        duplicates = {command_id for command_id, values in grouped.items() if len(values) != 1}
        for command_id in sorted(duplicates):
            run.checks.append(self._check(
                "planning",
                "EXCEPTION",
                f"command_id={command_id} explicit_duplicates={len(grouped[command_id])}",
                [Finding("DUPLICATE_COMMAND", command_id, "$submissions")],
            ))

        try:
            with self.writer.acceptance_pass(supplied) as acceptance:
                self._record_plan(run, acceptance.plan)

                for command_id in sorted(set(acceptance.plan.completed) & set(grouped) - duplicates):
                    command = grouped[command_id][0]
                    prior = acceptance.prior(command)
                    if prior is None:
                        run.checks.append(self._check(
                            "durability",
                            "EXCEPTION",
                            f"command_id={command_id} completed_without_lookup_result=true",
                            [Finding("AUDIT_GAP", "planner reported completion without a matching result", "$results")],
                        ))
                        continue
                    run.outcomes[command_id] = prior
                    if prior.document is not None and prior.document.get("command_result") == "ACCEPTED":
                        self._recheck_completed_acceptance(run, command, submission_paths)
                    else:
                        run.checks.append(self._check(
                            "planning",
                            "EXCEPTION",
                            f"command_id={command_id} prior_disposition=REJECTED",
                            [Finding("DEPENDENCY_REJECTED", "command already has a durable rejection", "$results")],
                        ))
                    self._record_write_and_durability(run, command_id, prior)

                for command_id in sorted(invalid_ids - duplicates):
                    if command_id in run.outcomes:
                        continue
                    command = grouped[command_id][0]
                    outcome = acceptance.reject(
                        command,
                        recorded_at=self.recorded_at_for(command),
                        reason_code="COMMAND_SCHEMA_INVALID",
                        reason_detail="command failed the registered schema check",
                    )
                    run.outcomes[command_id] = outcome
                    self._record_write_and_durability(run, command_id, outcome)

                acceptance.refresh()
                stalled: set[str] = set()
                while True:
                    progress = False

                    planned_rejections = [
                        (command_id, reason_code)
                        for command_id, reason_code in acceptance.plan.rejections.items()
                        if command_id not in run.outcomes and command_id not in duplicates
                    ]
                    for command_id, reason_code in planned_rejections:
                        command = grouped[command_id][0]
                        outcome = acceptance.reject(
                            command,
                            recorded_at=self.recorded_at_for(command),
                            reason_code=reason_code,
                            reason_detail=f"dependency planner disposition: {reason_code}",
                        )
                        run.checks.append(self._check(
                            "planning",
                            "EXCEPTION",
                            f"command_id={command_id} disposition={reason_code}",
                            [Finding(reason_code, "planned terminal dependency rejection", "$.depends_on")],
                        ))
                        run.outcomes[command_id] = outcome
                        self._record_write_and_durability(run, command_id, outcome)
                        progress = True
                    if planned_rejections:
                        acceptance.refresh()
                    if progress:
                        continue

                    ready = [
                        command
                        for command in acceptance.plan.ready
                        if command["command_id"] not in run.outcomes
                        and command["command_id"] not in stalled
                        and command["command_id"] not in duplicates
                    ]
                    if not ready:
                        break
                    command = ready[0]
                    command_id = command["command_id"]
                    outcome = self._process_ready(run, acceptance, command, submission_paths)
                    if outcome is None:
                        stalled.add(command_id)
                        halted_by_unknown = command_id
                        break
                    else:
                        run.outcomes[command_id] = outcome
                        self._record_write_and_durability(run, command_id, outcome)
                        acceptance.refresh()

                final_plan = acceptance.refresh()
                run.completed = set(final_plan.completed)
                run.waiting = dict(final_plan.waiting)
                if halted_by_unknown is not None:
                    for command in final_plan.ready:
                        command_id = command["command_id"]
                        if command_id not in run.outcomes:
                            run.waiting.setdefault(
                                command_id,
                                (f"REQUIRED_CHECK_UNKNOWN:{halted_by_unknown}",),
                            )
                for command_id, blockers in sorted(run.waiting.items()):
                    run.checks.append(self._check(
                        "planning",
                        "UNKNOWN",
                        f"command_id={command_id} waiting_on={','.join(blockers)}",
                        [Finding("DEPENDENCY_MISSING", "command remains visible and unprocessed", "$.depends_on")],
                    ))
        except ResultConstructionError as exc:
            run.checks.append(self._check("durability", "EXCEPTION", f"store={self.store.root}", exc.findings))

        aggregate_status = "PASS"
        if any(check.status == "UNKNOWN" for check in run.checks):
            aggregate_status = "UNKNOWN"
        elif any(check.status == "EXCEPTION" for check in run.checks):
            aggregate_status = "EXCEPTION"
        run.checks.append(self._check(
            "aggregate",
            aggregate_status,
            f"explicit_submissions={len(supplied)} durable_outcomes={len(run.outcomes)} waiting={len(run.waiting)}",
        ))
        return run

    def _process_ready(self, run, acceptance, command, submission_paths) -> WriteOutcome | None:
        command_id = command["command_id"]
        path = submission_paths.get(command_id, "")
        permission = authorize_command(command, path, self.registry)
        if not permission.valid:
            run.checks.append(self._check("permissions", "EXCEPTION", f"command_id={command_id} path={path}", permission.findings))
            return acceptance.reject(
                command,
                recorded_at=self.recorded_at_for(command),
                reason_code=_registered_reason(permission.findings, "PERMISSION_DENIED"),
                reason_detail=_finding_codes(permission.findings),
            )
        run.checks.append(self._check("permissions", "PASS", f"command_id={command_id} path={path}"))

        native = verify_native_references(command, self.git)
        if not native.valid:
            run.checks.append(self._check(
                "native-reference",
                "EXCEPTION",
                f"command_id={command_id} references={len(command.get('native_refs', []))}",
                native.findings,
            ))
            return acceptance.reject(
                command,
                recorded_at=self.recorded_at_for(command),
                reason_code=_native_reason(native.findings),
                reason_detail=_finding_codes(native.findings),
            )
        run.checks.append(self._check(
            "native-reference",
            "PASS",
            f"command_id={command_id} references={len(command.get('native_refs', []))}",
        ))

        for hook in self.required_hooks:
            check = hook(command)
            run.checks.append(check)
            if check.status == "UNKNOWN":
                return None
            if check.status == "EXCEPTION":
                return acceptance.reject(
                    command,
                    recorded_at=self.recorded_at_for(command),
                    reason_code=_registered_reason(check.findings, "COMMAND_SCHEMA_INVALID"),
                    reason_detail=_finding_codes(check.findings),
                )

        history = self.store.accepted_events()
        lifecycle = validate_transition(command, history)
        if not lifecycle.valid:
            run.checks.append(self._check(
                "lifecycle",
                "EXCEPTION",
                f"command_id={command_id} accepted_history={len(history)}",
                lifecycle.findings,
            ))
            return acceptance.reject(
                command,
                recorded_at=self.recorded_at_for(command),
                reason_code=_registered_reason(lifecycle.findings, "TRANSITION_FORBIDDEN"),
                reason_detail=_finding_codes(lifecycle.findings),
            )
        run.checks.append(self._check("lifecycle", "PASS", f"command_id={command_id} accepted_history={len(history)}"))
        return acceptance.accept(
            command,
            event_id=self.event_id_for(command),
            recorded_at=self.recorded_at_for(command),
        )

    def _recheck_completed_acceptance(self, run, command, submission_paths) -> None:
        """Re-establish the printed verification perimeter for an accepted retry."""

        command_id = command["command_id"]
        path = submission_paths.get(command_id, "")
        permission = authorize_command(command, path, self.registry)
        run.checks.append(self._check(
            "permissions",
            "PASS" if permission.valid else "EXCEPTION",
            f"command_id={command_id} path={path} prior_result=ACCEPTED",
            permission.findings,
        ))

        native = verify_native_references(command, self.git)
        run.checks.append(self._check(
            "native-reference",
            "PASS" if native.valid else "EXCEPTION",
            f"command_id={command_id} references={len(command.get('native_refs', []))} prior_result=ACCEPTED",
            native.findings,
        ))

        for hook in self.required_hooks:
            run.checks.append(hook(command))

        history = self.store.accepted_events()
        replayed = replay(history)
        run.checks.append(self._check(
            "lifecycle",
            "PASS" if not replayed.findings else "EXCEPTION",
            f"command_id={command_id} accepted_history={len(history)} prior_result=ACCEPTED replay_check=true",
            replayed.findings,
        ))

    def _record_plan(self, run: AcceptanceRun, plan) -> None:
        status = "PASS" if plan.valid else "EXCEPTION"
        perimeter = (
            f"completed={len(plan.completed)} ready={len(plan.ready)} "
            f"waiting={len(plan.waiting)} rejections={len(plan.rejections)}"
        )
        run.checks.append(self._check("planning", status, perimeter, plan.findings))

    def _record_write_and_durability(self, run: AcceptanceRun, command_id: str, outcome: WriteOutcome) -> None:
        writer_status = (
            "PASS"
            if outcome.state in {"WRITTEN", "EXISTING"}
            and outcome.document is not None
            and outcome.document.get("command_result") == "ACCEPTED"
            else "EXCEPTION"
        )
        writer_findings = [outcome.finding] if outcome.finding is not None else []
        run.checks.append(self._check("writer", writer_status, f"command_id={command_id} outcome={outcome.state}", writer_findings))
        inventory = self.store.inventory()
        stored = inventory.results.get(command_id) if inventory.valid else None
        durable_status = "PASS" if stored is not None else "EXCEPTION"
        run.checks.append(self._check(
            "durability",
            durable_status,
            f"command_id={command_id} store={self.store.root}",
            inventory.findings if not inventory.valid else (),
        ))

    @staticmethod
    def _check(name, status, perimeter, findings=()) -> AcceptanceCheck:
        proves, does_not = CLAIMS[name]
        return AcceptanceCheck(name, status, perimeter, proves, does_not, tuple(findings))


def format_acceptance_run(run: AcceptanceRun) -> str:
    lines: list[str] = []
    for check in run.checks:
        lines.append(f"perimeter: check={check.name} {check.perimeter}")
        lines.append(f"{check.status}: {check.name}")
        lines.append(f"PASS proves: {check.pass_proves}")
        lines.append(f"PASS does not prove: {check.pass_does_not_prove}")
        for finding in check.findings:
            lines.append(f"{finding.code}\t{finding.location}\t{finding.message}")
    return "\n".join(lines) + "\n"


def _registered_reason(findings: Iterable[Finding], fallback: str) -> str:
    for finding in findings:
        if finding.code in REJECTION_REASONS:
            return finding.code
    return fallback


def _native_reason(findings: Iterable[Finding]) -> str:
    mapping = {
        "NATIVE_COMMIT_MISSING": "NATIVE_RECORD_MISSING",
        "NATIVE_PATH_MISSING": "NATIVE_RECORD_MISSING",
        "NATIVE_LOCATOR_INVALID": "NATIVE_RECORD_INVALID",
        "NATIVE_JSON_POINTER_INVALID": "NATIVE_RECORD_INVALID",
    }
    for finding in findings:
        reason = mapping.get(finding.code, finding.code)
        if reason in REJECTION_REASONS:
            return reason
    return "NATIVE_RECORD_INVALID"


def _finding_codes(findings: Iterable[Finding]) -> str:
    return ",".join(sorted({finding.code for finding in findings}))


def _strict_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run one integrated fixture-only Kernel acceptance pass")
    parser.add_argument("--inventory", type=Path, required=True, help="JSON array of {path, command} fixture submissions")
    parser.add_argument("--actors", type=Path, required=True)
    parser.add_argument("--capabilities", type=Path, required=True)
    parser.add_argument("--repository", type=Path, required=True, help="injected synthetic Git repository")
    parser.add_argument("--store", type=Path, required=True, help="injected fixture KERNEL result root")
    parser.add_argument("--event-ids", type=Path, required=True, help="JSON object mapping command IDs to event IDs")
    parser.add_argument("--recorded-at", required=True)
    args = parser.parse_args(argv)

    try:
        inventory = _strict_json(args.inventory)
        event_ids = _strict_json(args.event_ids)
        if not isinstance(inventory, list) or not isinstance(event_ids, dict):
            raise ValueError("inventory must be an array and event IDs must be an object")
        repository = args.repository.resolve()
        live_repository = LIVE_REPOSITORY_ROOT.resolve()
        if repository == live_repository or live_repository in repository.parents or repository in live_repository.parents:
            raise ValueError("integrated fixture acceptance refuses the live repository boundary")
        commands = [item["command"] for item in inventory]
        paths = {item["command"]["command_id"]: item["path"] for item in inventory}
        registry = PermissionRegistry.from_files(args.actors, args.capabilities)
        runner = FixtureAcceptanceRunner(
            FixtureResultStore(args.store),
            writer_id="PROME",
            registry=registry,
            git=SubprocessGitBoundary(repository),
            event_id_for=lambda command: event_ids[command["command_id"]],
            recorded_at_for=lambda _command: args.recorded_at,
        )
        run = runner.run(commands, paths)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        check = AcceptanceCheck(
            "aggregate",
            "EXCEPTION",
            f"inventory={args.inventory} store={args.store} repository={args.repository}",
            *CLAIMS["aggregate"],
            (Finding("ACCEPTANCE_INPUT_INVALID", str(exc), "$input"),),
        )
        run = AcceptanceRun(checks=[check])
    print(format_acceptance_run(run), end="")
    return 0 if run.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
