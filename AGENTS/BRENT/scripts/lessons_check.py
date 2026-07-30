#!/usr/bin/env python3
"""
lessons_check.py — mechanize the lesson-conflict problem.

WHY THIS EXISTS
---------------
On 2026-07-30 four separate defects traced to the same root cause: my own LESSONS
contradicted each other or contradicted a live spec, nothing ever forced a
reconciliation, and so WHICHEVER LESSON WAS WRITTEN FIRST won by default when a
spec got drafted.

  * L18 vs L19  — tanker check direction. L18 written first, copied into the
                  off-ramp Stage A gate; L19 (with the empirical record) ignored.
  * L11 vs L18  — "crash at ANNOUNCEMENT not delivery" vs "require physical
                  verification". The spec sided with L18 silently.
  * L21 vs the diesel falsifier — "match each leg's window to its own response
                  time"; the falsifier forced a weekly survey and a daily price
                  into one shared week (1 fire in 155 weeks).
  * L15 SCOPE   — a 60-90 DTE tenor written for the slow Phase-2 demand short was
                  inherited by the fast off-ramp premium-unwind short.

A remembered ritual is not a check (`finding_mechanize_the_cap_not_the_ritual`),
so this runs at BOOT and reports UNRESOLVED tensions every session.

MODES
-----
  (default)            boot mode — report UNRESOLVED tensions only. Advisory, exit 0.
  --contradictions     full pairwise scan, including resolved ones (shows the audit trail).
  --concept <tag>      every lesson governing a concept. RUN THIS BEFORE WRITING A SPEC.
  --spec <file>        scan a spec file for concept keywords and list the lessons
                       that govern it -> "which of my own lessons does this spec owe?"
  --strict             exit 1 if any UNRESOLVED contradiction exists (for a gate).

INDEX: workbook/LESSONS_INDEX.tsv  (id, headline, scope, concepts, asserts,
       status, tension_with, resolution, last_verified)
A contradiction = two lessons sharing an ASSERT KEY with DIFFERENT VALUES.
That is the machine-detectable form of "these two lessons disagree".
"""
import csv, sys, argparse, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INDEX = ROOT / "AGENTS/BRENT/workbook/LESSONS_INDEX.tsv"

# concept -> keywords that betray the concept's presence in a prose spec
CONCEPT_KEYWORDS = {
    "tanker_equity":          ["stng", "tanker", "fro ", "dht ", "ton-mile"],
    "announcement_vs_physical": ["announcement", "operational", "rhetorical", "signature", "sovereign"],
    "entry_timing":           ["entry", "fires on", "trigger", "stage a", "deploy"],
    "option_structure":       ["put spread", "call spread", "naked", "vertical", "debit"],
    "tenor":                  ["dte", "expiry", "tenor"],
    "vol":                    ["ovx", "iv ", "implied vol", "vol-crush", "vega"],
    "gate_design":            ["gate", "leg", "threshold", "falsifier"],
    "threshold_spec":         ["threshold", "frozen", "percentile"],
    "data_latency":           ["lag", "window", "trading days", "same week", "survey"],
    "inventory":              ["distillate", "cushing", "stocks", "inventory", "spr"],
    "demand_measurement":     ["product supplied", "demand", "yoy"],
    "crack_spread":           ["crack", "diesel", "gasoline crack", "3-2-1"],
    "instrument_choice":      ["instrument", "proxy"],
    "opec":                   ["opec", "quota", "spare"],
    "price_freshness":        ["live price", "spot", "settle"],
}


def load():
    rows = []
    with open(INDEX, encoding="utf-8") as f:
        for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"):
            if r.get("id"):
                rows.append(r)
    return rows


def parse_asserts(s):
    out = {}
    for part in (s or "").split("|"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def find_contradictions(rows):
    """Two lessons sharing an assert KEY with different VALUES."""
    hits = []
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            aa, ba = parse_asserts(a["asserts"]), parse_asserts(b["asserts"])
            for k in set(aa) & set(ba):
                if aa[k] != ba[k]:
                    declared = (b["id"] in (a.get("tension_with") or "")) or \
                               (a["id"] in (b.get("tension_with") or ""))
                    # resolution must name the OTHER lesson's assert-key to count for THIS pair
                    ra, rb = (a.get("resolution") or ""), (b.get("resolution") or "")
                    res = " || ".join(x for x in (f"{a['id']}: {ra}" if ra else "",
                                                  f"{b['id']}: {rb}" if rb else "") if x)
                    # PER-KEY resolution tags: a resolution speaks for ONE tension, not all of them.
                    # Convention: "[<assert_key>:RESOLVED]" or "[<assert_key>:OPEN]" in the text.
                    tags = re.findall(rf"\[{re.escape(k)}:(RESOLVED|OPEN)\]", ra + " " + rb)
                    resolved = bool(tags) and all(t == "RESOLVED" for t in tags)
                    hits.append(dict(a=a, b=b, key=k, va=aa[k], vb=ba[k],
                                     declared=declared, resolved=resolved, res=res))
    return hits


def show(h, verbose=True):
    if h["resolved"]:
        tag = "\033[92m✅ RESOLVED\033[0m"
    elif h["declared"]:
        tag = "\033[93m⚠️  KNOWN, UNRESOLVED\033[0m"
    else:
        tag = "\033[91m🔴 UNDECLARED CONTRADICTION\033[0m"
    print(f"\n  {tag}  on assert `{h['key']}`")
    print(f"     {h['a']['id']}: {h['a']['headline'][:88]}")
    print(f"         -> {h['key']} = {h['va']}   [scope: {h['a']['scope']}]")
    print(f"     {h['b']['id']}: {h['b']['headline'][:88]}")
    print(f"         -> {h['key']} = {h['vb']}   [scope: {h['b']['scope']}]")
    if verbose and h["res"].strip():
        for line in h["res"].split(" || "):
            print(f"     resolution: {line.strip()[:260]}")
    if not h["declared"]:
        print("     ⚠️  NEITHER lesson declares the other in `tension_with` — this pair has")
        print("        never been reconciled. Whichever was written first will win by default.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contradictions", action="store_true")
    ap.add_argument("--concept")
    ap.add_argument("--spec")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    rows = load()

    if a.concept:
        c = a.concept.lower()
        m = [r for r in rows if c in (r["concepts"] or "").lower()]
        print(f"\n  LESSONS GOVERNING CONCEPT '{a.concept}'  ({len(m)} found)")
        print("  " + "-" * 74)
        for r in m:
            print(f"  {r['id']} [{r['status']}] scope={r['scope']}")
            print(f"      {r['headline']}")
            if r["asserts"]:
                print(f"      asserts: {r['asserts']}")
            if (r.get("resolution") or "").strip():
                print(f"      ⚠️  {r['resolution'][:220]}")
        if not m:
            print("  (none — concept tag not in the index; check spelling or add the tag)")
        return 0

    if a.spec:
        txt = Path(a.spec).read_text(encoding="utf-8").lower()
        present = {c for c, kws in CONCEPT_KEYWORDS.items() if any(k in txt for k in kws)}
        print(f"\n  SPEC SWEEP — {a.spec}")
        print(f"  concepts detected: {', '.join(sorted(present)) or '(none)'}")
        gov = [r for r in rows if set((r['concepts'] or '').split('|')) & present]
        print(f"\n  {len(gov)} LESSON(S) GOVERN THIS SPEC — reconcile each before shipping:")
        print("  " + "-" * 74)
        for r in sorted(gov, key=lambda x: x["id"]):
            cited = r["id"].lower() in txt or f"lessons #{r['id'][1:].lstrip('0')}" in txt
            mark = "cited " if cited else "❗NOT CITED"
            print(f"  {mark} {r['id']} [{r['status']}] {r['headline'][:80]}")
            if (r.get("resolution") or "").strip().startswith("🔴"):
                print(f"          🔴 {r['resolution'][:200]}")
        print("\n  'NOT CITED' is not automatically wrong — it means the spec never says")
        print("  whether it honours or overrides that lesson. That silence is the failure mode.")
        return 0

    hits = find_contradictions(rows)
    unresolved = [h for h in hits if not h["resolved"]]
    undeclared = [h for h in hits if not h["declared"]]

    if a.contradictions:
        print(f"\n  FULL PAIRWISE SCAN — {len(hits)} assert-level conflict(s) across {len(rows)} lessons")
        print("  " + "=" * 74)
        for h in hits:
            show(h)
    else:
        print(f"\n  LESSON-CONFLICT CHECK — {len(rows)} lessons indexed")
        if not unresolved:
            print("  ✅ no unresolved contradictions")
        else:
            print(f"  ⚠️  {len(unresolved)} UNRESOLVED contradiction(s):")
            print("  " + "=" * 74)
            for h in unresolved:
                show(h)
    if undeclared:
        print(f"\n  🔴 {len(undeclared)} pair(s) with NO declared tension — the silent-default class.")
    print()
    if a.strict and unresolved:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
