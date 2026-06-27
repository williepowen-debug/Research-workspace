#!/usr/bin/env python3
"""
TERRY Bank-Print Grader.

Turns PROME/synthesis/2026-06-25_Q2-bank-print-grading-instrument.md into a
checkable instrument. Grades a Q2 bank print as it lands:
  MASTER   : Provision$ vs NCO$  -> BUILD (transmission) / RELEASE (mask-defer)
  DISC-1   : SPECIFIC vs COLLECTIVE -> does a build count toward path (a)?
  DISC-2   : AOCI/NIM/TBV axis (path b), graded independently of NCO
Then --tally rolls graded names into the path (a)/(b)/(c) diagnostics and echoes
which of the 6 decision rules triggers.

NO market data — only filing numbers you type in. Pure, deterministic logic.
PROPOSE-only: any trade still requires Will approval (RISK_SCORING.md).

The 3 documented mis-grade traps are HARD GUARDS:
  - WAL  : --basis required; ERRORs on adjusted-vs-GAAP mismatch (Q1 39bps was NON-GAAP adj).
  - ZION : path-b requires --aoci-basis total-afs; rejects muni-only (~$869M FV is NOT the mechanism).
  - ALLY : --build-type required; collective build -> NON-COUNTING for path (a).

Examples:
  python3 AGENTS/TERRY/scripts/grade_print.py --list
  python3 AGENTS/TERRY/scripts/grade_print.py EGBN --provision 60 --nco 20 --build-type specific
  python3 AGENTS/TERRY/scripts/grade_print.py WAL --provision 80 --nco 60 --nco-bps 58 --basis adjusted \
      --build-type specific --life-sci-chargeoff yes
  python3 AGENTS/TERRY/scripts/grade_print.py ZION --provision 30 --nco 5 --aoci-direction worse \
      --tbv-direction down --aoci-basis total-afs
  python3 AGENTS/TERRY/scripts/grade_print.py --tally
  python3 AGENTS/TERRY/scripts/grade_print.py --selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TERRY_DIR = Path(__file__).resolve().parent.parent
CONFIG = TERRY_DIR / "grade_config.json"
GRADES_DIR = TERRY_DIR / "grades"


class GradeError(Exception):
    pass


def load_config():
    return json.loads(CONFIG.read_text())


# ---------------------------------------------------------------------------
# Trap guards (hard — raise GradeError or warn)
# ---------------------------------------------------------------------------

def apply_traps(name, cfg, args, warnings):
    """Enforce the documented mis-grade guards. Raises GradeError on hard traps."""
    traps = cfg["names"].get(name, {}).get("traps", [])
    tdefs = cfg["traps"]

    if "basis_required" in traps:
        # WAL: must grade adjusted-vs-adjusted.
        if args.basis is None:
            raise GradeError(
                f"[TRAP basis_required/{name}] --basis is REQUIRED. "
                + tdefs["basis_required"]["guard"] + " FIX: " + tdefs["basis_required"]["fix"])
        if args.basis != "adjusted":
            raise GradeError(
                f"[TRAP basis_required/{name}] --basis '{args.basis}' rejected. "
                "Q1 baseline is NON-GAAP ADJUSTED (39bps); a GAAP Q2 NCO (~1.45% basis) is a UNIT MISMATCH. "
                + tdefs["basis_required"]["fix"])

    if "total_afs_required" in traps:
        # ZION: only enforce when a path-b grade is actually being attempted.
        grading_path_b = args.aoci_direction is not None or args.tbv_direction is not None
        if grading_path_b:
            if args.aoci_basis is None:
                raise GradeError(
                    f"[TRAP total_afs_required/{name}] --aoci-basis is REQUIRED for path-b. "
                    + tdefs["total_afs_required"]["guard"] + " FIX: " + tdefs["total_afs_required"]["fix"])
            if args.aoci_basis != "total-afs":
                raise GradeError(
                    f"[TRAP total_afs_required/{name}] --aoci-basis '{args.aoci_basis}' rejected. "
                    + tdefs["total_afs_required"]["guard"])

    if "build_type_required" in traps:
        # ALLY (and any path-a member on a build): require build-type when a build is present.
        prov = args.provision
        nco = args.nco
        is_build = prov is not None and nco is not None and prov > nco
        if is_build and args.build_type is None:
            raise GradeError(
                f"[TRAP build_type_required/{name}] a BUILD with no --build-type. "
                + tdefs["build_type_required"]["guard"] + " FIX: " + tdefs["build_type_required"]["fix"])

    if "discover_conforming_flag" in traps:
        warnings.append(f"[WARN discover_conforming/{name}] " + tdefs["discover_conforming_flag"]["guard"])
    if "no_10q_research_grade" in traps:
        warnings.append(f"[WARN no_10q/{name}] " + tdefs["no_10q_research_grade"]["guard"])


# ---------------------------------------------------------------------------
# Grading
# ---------------------------------------------------------------------------

def grade(name, cfg, args):
    name = name.upper()
    if name not in cfg["names"]:
        raise GradeError(f"unknown name '{name}'. Known: {', '.join(sorted(cfg['names']))}")

    nmeta = cfg["names"][name]
    paths = cfg["paths"]
    warnings = []
    apply_traps(name, cfg, args, warnings)

    result = {
        "name": name, "print": nmeta.get("print"),
        "warnings": warnings, "notes": args.note,
        "master": None, "disc1": None, "path_a": None, "path_b": None, "path_c": None,
        "path_m": None, "path_m_tells": 0,
    }

    # MASTER — provision vs NCO
    prov, nco = args.provision, args.nco
    if prov is not None and nco is not None:
        if prov > nco:
            result["master"] = f"BUILD (Prov ${prov}M > NCO ${nco}M) -> transmission live"
        elif prov < nco:
            result["master"] = f"RELEASE (Prov ${prov}M < NCO ${nco}M) -> mask/defer"
        else:
            result["master"] = f"FLAT (Prov ${prov}M = NCO ${nco}M)"
    else:
        result["master"] = "N/A (need --provision and --nco)"
    is_build = prov is not None and nco is not None and prov > nco

    # DISC-1 — specific vs collective, reported for ANY name showing a build
    if not is_build:
        result["disc1"] = "no build -> Disc-1 n/a"
    elif args.build_type == "specific":
        result["disc1"] = "SPECIFIC build (named-credit migration) -> genuine transmission"
    elif args.build_type == "collective":
        result["disc1"] = "COLLECTIVE/macro-overlay build = BETA -> NON-COUNTING (Disc-1, not credit substance)"
    else:
        result["disc1"] = "build present but --build-type unknown -> cannot classify"

    # path (a) tally membership — only the regional members feed the >=2 tally
    if name in paths["a"]["members"]:
        if not is_build:
            result["path_a"] = "no build -> does not count"
        elif args.build_type == "specific":
            result["path_a"] = "COUNTS (specific build) -> path-(a) member fires"
        elif args.build_type == "collective":
            result["path_a"] = "NON-COUNTING (collective = BETA, Disc-1)"
        else:
            result["path_a"] = "build present but --build-type unknown -> cannot count"
    else:
        result["path_a"] = f"n/a — gate/consumer name, not a path-(a) tally member (members={paths['a']['members']})"

    # DISC-2 / path (b) — AOCI/NIM/TBV axis, independent of NCO
    if name in paths["b"]["members"]:
        deteriorates = args.aoci_direction == "worse" or args.tbv_direction == "down"
        if args.aoci_direction is None and args.tbv_direction is None:
            result["path_b"] = "not graded (pass --aoci-direction / --tbv-direction)"
        elif deteriorates:
            result["path_b"] = (f"DETERIORATION (AOCI={args.aoci_direction}, TBV={args.tbv_direction}) "
                                "-> path-(b) member fires (counts even on clean NCO)")
        else:
            result["path_b"] = f"stable (AOCI={args.aoci_direction}, TBV={args.tbv_direction})"
    else:
        result["path_b"] = f"n/a (not a path-(b) member; members={paths['b']['members']})"

    # path (c) — WAL standalone full charge-off
    if name in paths["c"]["members"]:
        th = nmeta["thresholds"]
        ncob = args.nco_bps
        chargeoff = (args.life_sci_chargeoff or "").lower() in ("yes", "y", "true")
        if ncob is None:
            result["path_c"] = "not graded (pass --nco-bps adjusted ex-fraud)"
        elif ncob > th["exfraud_nco_bps_fire"] and chargeoff:
            result["path_c"] = (f"FULL CHARGE-OFF / BEAR-CONFIRM (ex-fraud NCO {ncob}bps > "
                                f"{th['exfraud_nco_bps_fire']}bps AND life-sci majority charged off)")
        elif th["build_defer_nco_bps_lo"] <= ncob <= th["build_defer_nco_bps_hi"]:
            result["path_c"] = (f"BUILD-BUT-DEFER (NCO {ncob}bps in {th['build_defer_nco_bps_lo']}-"
                                f"{th['build_defer_nco_bps_hi']}bps) -> partial; counts toward (a), NOT (c)")
        else:
            result["path_c"] = f"no full charge-off (NCO {ncob}bps, chargeoff={chargeoff})"
    else:
        result["path_c"] = "n/a (path-(c) is WAL only)"

    # path (m) — MONOLINE un-mask tally (SYF/COF/ALLY): grade un-maskable sub-signals, NOT headline NCO.
    # Monolines composition-mask (book-shrinkage suppresses NCO), so a build on a flat/shrinking book is
    # unambiguous deterioration (not growth-beta); a raised NCO guide or rising DQ formation are mask-proof.
    if name in paths.get("m", {}).get("members", []):
        book = (args.book_direction or "")
        tells = []
        if is_build and book in ("shrinking", "flat"):
            tells.append(f"build-on-{book}-book")
        elif is_build and args.build_type == "specific":
            tells.append("specific-build")
        if args.nco_guide == "raised":
            tells.append("nco-guide-raised")
        if args.dq_formation == "rising":
            tells.append("dq-formation-rising")
        result["path_m_tells"] = len(tells)
        if tells:
            result["path_m"] = f"COUNTS (un-masked: {', '.join(tells)}) -> monoline tally fires"
        elif is_build and book == "growing" and args.build_type != "specific":
            result["path_m"] = "NON-COUNTING (build on a GROWING book w/o specific = growth-beta mask)"
        elif is_build and not book:
            result["path_m"] = "build present but --book-direction unknown -> cannot classify (growth-beta vs deterioration)"
        else:
            result["path_m"] = "NON-COUNTING (release/clean headline = masked; no un-mask tell)"
    else:
        result["path_m"] = f"n/a (not a monoline tally member; members={paths.get('m', {}).get('members', [])})"

    return result


def nmeta_get(d, k):
    return d.get(k)


def save_grade(result):
    GRADES_DIR.mkdir(exist_ok=True)
    p = GRADES_DIR / f"{result['name']}.json"
    p.write_text(json.dumps(result, indent=2))
    return p


def print_grade(result, cfg):
    name = result["name"]
    nmeta = cfg["names"][name]
    print(f"\n=== GRADE: {name} (print {result['print']}) ===")
    print(f"axis: {nmeta['axis']}")
    print(f"Q1 posture: {nmeta['q1_posture']}")
    print(f"\n  MASTER  : {result['master']}")
    print(f"  DISC-1  : {result['disc1']}")
    print(f"  PATH(a) : {result['path_a']}")
    print(f"  PATH(b) : {result['path_b']}")
    print(f"  PATH(c) : {result['path_c']}")
    print(f"  PATH(m) : {result['path_m']}")
    for w in result["warnings"]:
        print(f"  {w}")
    if result.get("notes"):
        print(f"  note: {result['notes']}")
    print("\n  PROPOSE-only — verify vs the 10-Q/release; trade requires Will approval.")


# ---------------------------------------------------------------------------
# Tally
# ---------------------------------------------------------------------------

def tally(cfg):
    paths = cfg["paths"]
    if not GRADES_DIR.exists():
        print("No grades yet. Grade names first, then --tally.")
        return 0
    graded = {}
    for f in sorted(GRADES_DIR.glob("*.json")):
        try:
            g = json.loads(f.read_text())
            graded[g["name"]] = g
        except (json.JSONDecodeError, OSError):
            continue

    print(f"\n=== PATH TALLY ({len(graded)} graded: {', '.join(sorted(graded))}) ===\n")

    a_hits = [n for n, g in graded.items()
              if n in paths["a"]["members"] and "COUNTS" in (g.get("path_a") or "")]
    b_hits = [n for n, g in graded.items()
              if n in paths["b"]["members"] and "DETERIORATION" in (g.get("path_b") or "")]
    c_hit = ["WAL"] if "WAL" in graded and "FULL CHARGE-OFF" in (graded["WAL"].get("path_c") or "") else []

    m_members = paths.get("m", {}).get("members", [])
    m_hits = [n for n, g in graded.items()
              if n in m_members and "COUNTS" in (g.get("path_m") or "")]
    m_strong = [n for n in m_hits if (graded[n].get("path_m_tells") or 0) >= 2]

    a_fires = len(a_hits) >= paths["a"]["need"]
    b_fires = len(b_hits) >= paths["b"]["need"]
    c_fires = len(c_hit) >= paths["c"]["need"]
    m_fires = bool(m_members) and (len(m_hits) >= paths["m"]["need"] or len(m_strong) >= 1)

    print(f"  PATH (a) SPECIFIC-build [{paths['a']['base_odds']}]: {len(a_hits)}/{paths['a']['need']} "
          f"{a_hits} -> {'FIRES' if a_fires else 'no'}")
    print(f"  PATH (b) AOCI/NIM/TBV  [{paths['b']['base_odds']}]: {len(b_hits)}/{paths['b']['need']} "
          f"{b_hits} -> {'FIRES' if b_fires else 'no'}")
    print(f"  PATH (c) WAL standalone[{paths['c']['base_odds']}]: {len(c_hit)}/{paths['c']['need']} "
          f"{c_hit} -> {'FIRES' if c_fires else 'no'}")
    if m_members:
        strong = f" +strong-single{m_strong}" if m_strong else ""
        print(f"  PATH (m) monoline un-mask [{paths['m']['base_odds']}]: {len(m_hits)}/{paths['m']['need']} "
              f"{m_hits}{strong} -> {'FIRES' if m_fires else 'no'}")

    # COF bridge
    if "COF" in graded:
        cof = graded["COF"]
        print(f"\n  COF bridge: {cof.get('master')} | path(a)={cof.get('path_a')}")

    print("\n  DECISION RULE TRIGGERED:")
    rules = cfg["decision_rules"]
    if m_fires and len(rules) > 6:
        print(f"    -> {rules[6]}")
    if c_fires:
        print(f"    -> {rules[3]}")
    if a_fires:
        print(f"    -> {rules[2]}")
    if b_fires:
        print(f"    -> {rules[1]}")
    if not (a_fires or b_fires or c_fires or m_fires):
        print(f"    -> {rules[0]}")
        print(f"    (beta guard) {rules[5]}")
    print("\n  PROPOSE-only -> Will/FORGE. Confirm builds specific-not-collective before escalating.")
    return 0


# ---------------------------------------------------------------------------
# Self-test (reproduces known Q1 grades)
# ---------------------------------------------------------------------------

def selftest():
    cfg = load_config()

    class A:  # arg stub
        provision = nco = nco_bps = None
        build_type = aoci_direction = tbv_direction = aoci_basis = basis = None
        life_sci_chargeoff = note = None
        book_direction = nco_guide = dq_formation = None

    # 1) ALLY Q1: +$50M collective build -> BUILD but path-a NON-COUNTING
    a = A(); a.provision = 467; a.nco = 417; a.build_type = "collective"
    r = grade("ALLY", cfg, a)
    assert r["master"].startswith("BUILD"), r["master"]
    assert "NON-COUNTING" in r["disc1"], r["disc1"]

    # 2) ALLY build with NO build-type -> hard trap
    try:
        a2 = A(); a2.provision = 467; a2.nco = 417
        grade("ALLY", cfg, a2)
        assert False, "expected build_type trap"
    except GradeError as e:
        assert "build_type_required" in str(e)

    # 3) WAL with --basis gaap -> hard trap (unit mismatch)
    try:
        w = A(); w.provision = 80; w.nco = 60; w.basis = "gaap"; w.build_type = "specific"
        grade("WAL", cfg, w)
        assert False, "expected basis trap"
    except GradeError as e:
        assert "basis_required" in str(e)

    # 4) WAL adjusted, NCO 58bps + life-sci chargeoff -> path(c) full charge-off
    w2 = A(); w2.provision = 90; w2.nco = 70; w2.nco_bps = 58; w2.basis = "adjusted"
    w2.build_type = "specific"; w2.life_sci_chargeoff = "yes"
    rw = grade("WAL", cfg, w2)
    assert "FULL CHARGE-OFF" in rw["path_c"], rw["path_c"]

    # 5) WAL build-but-defer (42bps) -> partial, counts toward a not c
    w3 = A(); w3.provision = 90; w3.nco = 70; w3.nco_bps = 42; w3.basis = "adjusted"; w3.build_type = "specific"
    rw3 = grade("WAL", cfg, w3)
    assert "BUILD-BUT-DEFER" in rw3["path_c"], rw3["path_c"]

    # 6) ZION path-b with muni basis -> hard trap
    try:
        z = A(); z.provision = 30; z.nco = 5; z.aoci_direction = "worse"; z.aoci_basis = "muni"
        grade("ZION", cfg, z)
        assert False, "expected total_afs trap"
    except GradeError as e:
        assert "total_afs_required" in str(e)

    # 7) ZION path-b total-afs worse -> deterioration counts
    z2 = A(); z2.provision = 30; z2.nco = 5; z2.aoci_direction = "worse"; z2.tbv_direction = "down"; z2.aoci_basis = "total-afs"
    rz = grade("ZION", cfg, z2)
    assert "DETERIORATION" in rz["path_b"], rz["path_b"]

    # 8) EGBN specific build -> path(a) counts
    e2 = A(); e2.provision = 60; e2.nco = 20; e2.build_type = "specific"
    re = grade("EGBN", cfg, e2)
    assert "COUNTS" in re["path_a"], re["path_a"]

    # 9) SYF build on a SHRINKING book -> path(m) COUNTS (un-masked, not growth-beta)
    s = A(); s.provision = 50; s.nco = 40; s.book_direction = "shrinking"
    rs = grade("SYF", cfg, s)
    assert "COUNTS" in rs["path_m"], rs["path_m"]
    assert rs["path_m_tells"] >= 1, rs["path_m_tells"]

    # 10) SYF build on a GROWING book, collective -> path(m) NON-COUNTING (growth-beta mask)
    s2 = A(); s2.provision = 50; s2.nco = 40; s2.book_direction = "growing"; s2.build_type = "collective"
    rs2 = grade("SYF", cfg, s2)
    assert "NON-COUNTING" in rs2["path_m"], rs2["path_m"]

    # 11) COF release (clean masked headline) -> path(m) NON-COUNTING
    c = A(); c.provision = 30; c.nco = 50
    rc = grade("COF", cfg, c)
    assert "NON-COUNTING" in rc["path_m"], rc["path_m"]

    # 12) SYF two tells (build-on-flat-book + guide raised) -> strong single (tells >= 2)
    s3 = A(); s3.provision = 50; s3.nco = 40; s3.book_direction = "flat"; s3.nco_guide = "raised"
    rs3 = grade("SYF", cfg, s3)
    assert rs3["path_m_tells"] >= 2, rs3["path_m_tells"]

    # 13) ALLY build on shrinking book, specific -> path(m) COUNTS (build-type clears the ALLY trap)
    al = A(); al.provision = 60; al.nco = 40; al.book_direction = "shrinking"; al.build_type = "specific"
    ral = grade("ALLY", cfg, al)
    assert "COUNTS" in ral["path_m"], ral["path_m"]

    print("grade_print.py SELFTEST: PASS")
    print("  ALLY collective build -> BUILD + path-a NON-COUNTING ✓")
    print("  ALLY no build-type -> TRAP ✓ | WAL --basis gaap -> TRAP ✓ | ZION muni -> TRAP ✓")
    print("  WAL 58bps+chargeoff -> path(c) FULL CHARGE-OFF ✓ | WAL 42bps -> BUILD-BUT-DEFER ✓")
    print("  ZION total-afs worse -> path(b) DETERIORATION ✓ | EGBN specific -> path(a) COUNTS ✓")
    print("  SYF build-on-shrinking-book -> path(m) COUNTS ✓ | growing+collective -> NON-COUNTING ✓")
    print("  COF release -> path(m) NON-COUNTING ✓ | SYF 2-tells -> strong-single ✓ | ALLY shrinking+specific -> COUNTS ✓")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="TERRY bank-print grader")
    ap.add_argument("name", nargs="?", help="bank name (e.g. WAL, EGBN, ZION)")
    ap.add_argument("--provision", type=float, help="provision expense $M this quarter")
    ap.add_argument("--nco", type=float, help="net charge-offs $M this quarter")
    ap.add_argument("--nco-bps", type=float, help="NCO in bps (WAL path-c; ex-fraud ADJUSTED)")
    ap.add_argument("--build-type", choices=["specific", "collective"], help="Disc-1 classification")
    ap.add_argument("--aoci-direction", choices=["worse", "stable", "better"], help="path-b AOCI move")
    ap.add_argument("--tbv-direction", choices=["down", "flat", "up"], help="path-b TBV/sh move")
    ap.add_argument("--aoci-basis", choices=["total-afs", "muni"], help="ZION path-b basis (must be total-afs)")
    ap.add_argument("--basis", choices=["adjusted", "gaap"], help="WAL NCO basis (must be adjusted)")
    ap.add_argument("--life-sci-chargeoff", help="WAL: was majority of $99M life-sci charged off? yes/no")
    ap.add_argument("--book-direction", choices=["shrinking", "flat", "growing"],
                    help="monoline (path-m) receivables trajectory — build on shrinking/flat = deterioration, not growth-beta")
    ap.add_argument("--nco-guide", choices=["raised", "affirmed", "cut"], help="monoline (path-m) NCO guidance change — raised = un-mask tell")
    ap.add_argument("--dq-formation", choices=["rising", "stable", "falling"], help="monoline (path-m) early-stage DQ formation QoQ ex-seasonal — rising = un-mask tell")
    ap.add_argument("--note", help="free-text grader note")
    ap.add_argument("--no-save", action="store_true", help="grade without persisting to grades/")
    ap.add_argument("--tally", action="store_true", help="roll all saved grades into path diagnostics")
    ap.add_argument("--list", action="store_true", help="list configured names")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    cfg = load_config()

    if args.list:
        print("Configured names:")
        for n, m in cfg["names"].items():
            print(f"  {n:<6} print {m['print']:<12} {m['axis']}")
        return 0

    if args.tally:
        return tally(cfg)

    if not args.name:
        ap.error("name required (or use --tally / --list / --selftest)")

    try:
        result = grade(args.name, cfg, args)
    except GradeError as e:
        print(f"GRADE ERROR: {e}", file=sys.stderr)
        return 2

    print_grade(result, cfg)
    if not args.no_save:
        p = save_grade(result)
        print(f"\n  saved -> {p.relative_to(TERRY_DIR.parent.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
