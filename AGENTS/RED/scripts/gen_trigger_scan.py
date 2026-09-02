#!/usr/bin/env python3
"""Generate the compact SCAN view of RED's trigger registry — never hand-edit the view.

Canon:  registry/FALSIFICATION_TRIGGERS.tsv   (18 cols; the ONLY authority)
View:   registry/FALSIFICATION_TRIGGERS_SCAN.tsv (13 cols; deterministic projection)

Why (WALTER proposal 2026-08-31, RED S39 2026-09-02): WALTER's boot step 6b reads the
registry WHOLE and it is 45 KB = 139% of the read-cap budget, 89% of which is three prose
columns. The 12 columns the scan executes on total ~2.5 KB. `instrument_basis` is
LOAD-BEARING (series / unit / lag / which date governs) so it is NOT dropped — its operative
clause is authored ONCE in canon as `instrument_basis_operative` and copied here verbatim.
Rationale stays in canon. Any fire, dispatch citation or ruling goes to CANON, not this view.

The view is deterministic: same canon bytes -> same view bytes (no timestamps). The header
comment carries the canon sha256 so a stale view is detectable without a diff.

Usage:
  python3 AGENTS/RED/scripts/gen_trigger_scan.py           # (re)generate the view
  python3 AGENTS/RED/scripts/gen_trigger_scan.py --check   # exit 1 if the view is stale/absent

Never parse RED TSVs with the csv module (literal '"' in prose cells) — split on tab.
"""
from __future__ import annotations
import hashlib, sys
from pathlib import Path

RED = Path(__file__).resolve().parents[1]
CANON = RED / "registry" / "FALSIFICATION_TRIGGERS.tsv"
VIEW = RED / "registry" / "FALSIFICATION_TRIGGERS_SCAN.tsv"
SCAN_COLS = [
    "trigger_id", "metric", "threshold_op", "threshold_value", "sustain_window", "action",
    "state", "recipient_chain", "exit_op", "exit_threshold", "exit_sustain", "last_reviewed",
    "instrument_basis_operative",
]


def render(canon_bytes: bytes) -> str:
    text = canon_bytes.decode("utf-8")
    rows = [l for l in text.split("\n") if l and not l.startswith("#")]
    header = rows[0].split("\t")
    missing = [c for c in SCAN_COLS if c not in header]
    if missing:
        raise SystemExit(f"EXCEPTION: canon lacks column(s) {missing} — view not generated")
    idx = [header.index(c) for c in SCAN_COLS]
    out = [
        "# GENERATED VIEW — do not hand-edit. Regenerate: python3 AGENTS/RED/scripts/gen_trigger_scan.py"
        f" | canon=registry/FALSIFICATION_TRIGGERS.tsv sha256={hashlib.sha256(canon_bytes).hexdigest()}"
        " | CANON GOVERNS every fire, citation and ruling; this view exists to keep WALTER boot 6b/6c under the read cap.",
        "\t".join(SCAN_COLS),
    ]
    for r in rows[1:]:
        cells = r.split("\t")
        if len(cells) != len(header):
            raise SystemExit(f"EXCEPTION: canon row {cells[0]!r} has {len(cells)} cols, header {len(header)}")
        out.append("\t".join(cells[i] for i in idx))
    return "\n".join(out) + "\n"


def main() -> int:
    canon_bytes = CANON.read_bytes()
    expected = render(canon_bytes)
    if "--check" in sys.argv:
        if not VIEW.exists():
            print(f"🔴 SCAN VIEW ABSENT: {VIEW.relative_to(RED)} — run gen_trigger_scan.py")
            return 1
        if VIEW.read_text(encoding="utf-8") != expected:
            print(f"🔴 SCAN VIEW STALE vs canon — run gen_trigger_scan.py (canon sha256 {hashlib.sha256(canon_bytes).hexdigest()[:12]})")
            return 1
        n = len([l for l in expected.split("\n") if l and not l.startswith("#")]) - 1
        print(f"✅ SCAN VIEW current: {n} rows, {len(expected.encode())} B (canon {len(canon_bytes)} B)")
        return 0
    VIEW.write_text(expected, encoding="utf-8")
    n = len([l for l in expected.split("\n") if l and not l.startswith("#")]) - 1
    print(f"generated {VIEW.relative_to(RED)}: {n} rows, {len(expected.encode())} B (canon {len(canon_bytes)} B, {100*len(expected.encode())//len(canon_bytes)}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
