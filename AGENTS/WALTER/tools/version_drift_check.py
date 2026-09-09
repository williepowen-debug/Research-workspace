#!/usr/bin/env python3
"""Version-drift guard — diffs each core spec's self-declared version against the
version STATE.md §1 claims for it. Fail-loud; exit 1 on any drift.

Root cause this closes (2026-06-16 WALTER audit): spec version-bumps land
correctly in the owning spec, but the directory doc that POINTS at them
(`design/STATE.md` §1) doesn't get swept on the same commit — so STATE.md, the
doc whose whole job is "what's shipped at what version," silently rots. The
6/16 audit found STATE.md 2 versions stale on all four core specs plus a missing
CLUSTER_TAXONOMY row. This is the mechanical check that catches that class.

Run at closeout (and optionally boot) — see WALTER CLAUDE.md closeout step.
Zero cost, stdlib only, read-only.

  $ python3 tools/version_drift_check.py
  exit 0 = STATE.md §1 matches every spec's own header
  exit 1 = drift (mismatch or spec missing from §1) — names what to fix

Adding a spec? Add it to SPECS below.
"""
import re
import sys
from pathlib import Path

WALTER = Path(__file__).resolve().parents[1]

# Specs whose self-declared header version must match STATE.md §1.
# Key = path as it appears in STATE.md §1 (relative to AGENTS/WALTER/).
SPECS = [
    "design/SIGNAL_FORMAT_SPEC.md",
    "design/ROUTING_TABLE.md",
    "design/FILTER_SPEC.md",
    "design/SIGNAL_PROCESSING_CHECKLIST.md",
    "design/CLUSTER_TAXONOMY.md",
    "design/BOARD_CONSUMPTION_SPEC.md",
]

# COMPANION SPECS (added 2026-08-30, Codex finding 3): files that are ONE spec split
# across two paths for read-cap reasons. They must declare the SAME version and move in
# lockstep. Without this, a ROUTING_CARVEOUTS.md edit could change WHO RECEIVES A SIGNAL
# while ROUTING_TABLE.md still reads v0.31 and every existing drift check passes clean —
# the split created a synchronisation boundary that no instrument was watching.
COMPANIONS = {
    "design/ROUTING_CARVEOUTS.md": "design/ROUTING_TABLE.md",
    "design/ROUTING_OVERLAYS.md": "design/ROUTING_TABLE.md",
    "design/THRESHOLD_SCAN.md": "design/SIGNAL_PROCESSING_CHECKLIST.md",
}

# version token: title form `# ... vX.Y` OR `**Version:** [v]X.Y`
_TITLE = re.compile(r"^#.*?\bv(\d+\.\d+)\b")
_FIELD = re.compile(r"\*\*Version:\*\*\s*v?(\d+\.\d+)\b")


def spec_version(path: Path) -> str | None:
    """First version token in the spec's header (first 6 lines)."""
    for line in path.read_text(errors="replace").splitlines()[:6]:
        m = _TITLE.match(line) or _FIELD.search(line)
        if m:
            return m.group(1)
    return None


def state_versions() -> dict[str, str]:
    """Parse STATE.md §1 'Active design specs' table → {path: version}."""
    text = (WALTER / "design" / "STATE.md").read_text(errors="replace")
    # isolate §1 up to the next "## " header
    sec = re.search(r"##\s*1\.\s*Active design specs(.*?)(?:\n##\s|\Z)",
                    text, re.S)
    body = sec.group(1) if sec else ""
    out = {}
    for line in body.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        pm = re.search(r"`([^`]+\.md)`", line)
        if not pm:
            continue
        # first **vX.Y** after the path = the "Current" column
        after = line[pm.end():]
        vm = re.search(r"\*\*v?(\d+\.\d+)\*\*", after)
        if vm:
            out[pm.group(1)] = vm.group(1)
    return out


def main() -> int:
    state = state_versions()
    drift = []
    print(f"{'spec':<40} {'spec-header':>11} {'STATE §1':>9}  status")
    print("-" * 74)
    for rel in SPECS:
        sv = spec_version(WALTER / rel)
        stv = state.get(rel)
        if sv is None:
            status, bad = "?? no version in header", True
        elif stv is None:
            status, bad = "DRIFT — missing from STATE §1", True
        elif sv != stv:
            status, bad = f"DRIFT — STATE says v{stv}, spec is v{sv}", True
        else:
            status, bad = "ok", False
        if bad:
            drift.append(rel)
        print(f"{rel:<40} {('v'+sv) if sv else '—':>11} "
              f"{('v'+stv) if stv else '—':>9}  {status}")
    print("-" * 74)

    # COMPANION LOCKSTEP — a split spec must not drift against its parent.
    for rel, parent in COMPANIONS.items():
        cv, pv = spec_version(WALTER / rel), spec_version(WALTER / parent)
        if cv is None:
            print(f"{rel:<40} {'—':>11} {'—':>9}  ?? no version header (companion of {parent})")
            drift.append(rel)
        elif cv != pv:
            print(f"{rel:<40} {'v'+cv:>11} {'v'+(pv or '?'):>9}  "
                  f"COMPANION DRIFT — {parent} is v{pv}")
            drift.append(rel)
        else:
            print(f"{rel:<40} {'v'+cv:>11} {'v'+pv:>9}  ok (lockstep with {parent})")
    if COMPANIONS:
        print("-" * 74)

    if drift:
        print(f"\n✗ {len(drift)} drift: {', '.join(drift)}")
        print("  → fix STATE.md §1 (or the spec header) so they agree.")
        print("  → COMPANION DRIFT means one spec was split across two paths and only one")
        print("    half was bumped: routing behaviour can change with the parent version")
        print("    unmoved. Bump BOTH; they are one spec.")
        return 1
    print("\n✓ STATE.md §1 matches every spec header; companions in lockstep.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
