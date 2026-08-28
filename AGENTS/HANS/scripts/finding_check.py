#!/usr/bin/env python3
"""
finding_check — a SHIP-GATE for empirical findings.

WHY THIS EXISTS (and why another memory would not have worked):
On 2026-08-28 HANS shipped a finding, corrected a peer on it, and amended its own
charter. One verification pass killed three of its four claims. The fleet ALREADY
had four hot-index memories describing that exact failure —
  finding_confounds_align_with_the_prior_you_brought
  finding_crosscheck_with_free_parameter_validates_nothing
  finding_self_attack_defends_the_argument_not_the_apparatus
  finding_adoption_is_not_validation
— all four were loaded in context at boot. NONE fired. They were cited afterwards
as post-mortem tags.

  ⇒ IT IS NOT A KNOWLEDGE GAP, IT IS A TRIGGER GAP. Memories fire on RECOGNITION,
    and a finding that confirms your prior does not feel wrong. The failure state
    and the success state are subjectively identical, so nothing prompts the lookup.

So this is deliberately NOT a checklist. It RUNS. It does not ask you to suspect
anything, because suspicion is exactly the thing that is missing at ship time.

TWO GATES:
  [A] INDEPENDENCE — does your robustness check vary something INDEPENDENT of the
      dimension your claim is about? HANS cited "five consecutive lags" as
      robustness for a claim ABOUT lag structure. That is one result viewed five
      ways, not five results.
  [B] SUBSAMPLE STABILITY — re-computes your statistic on hostile subsamples
      (ex-crisis, halves, ex-decade). Mechanical: no judgement required.

USE AS A LIBRARY (preferred — put it in the research script itself):
    from finding_check import gate, stability
    gate(claim="capex-led moves are a weaker lead",
         about="lag", varied="lag",              # -> FAILS gate A
         stat=my_fn, keys=all_months)

RUN THE WORKED EXAMPLE (HANS's own failure, reproduced):
    .venv/bin/python AGENTS/HANS/scripts/finding_check.py --demo
"""
import argparse, sys

# Known macro dislocations. Any of these dominating a result is a red flag, because
# cross-series correlations inflate during them REGARDLESS of the mechanism claimed.
CRISES = {
    "dotcom-2001":  ("2001", "2002"),
    "GFC-2008":     ("2008", "2009"),
    "EZ-2011":      ("2011", "2012"),
    "COVID-2020":   ("2020", "2021"),
}

# Dimensions a claim can be ABOUT / a robustness check can VARY.
DIMS = {"lag", "horizon", "sample", "period", "era", "specification", "spec",
        "threshold", "subgroup", "source", "definition", "universe", "window"}
# varying these does NOT establish independence from a claim about the same thing
SAME = {"lag": {"lag", "horizon", "window"}, "horizon": {"lag", "horizon", "window"},
        "window": {"lag", "horizon", "window"},
        "sample": {"sample", "period", "era"}, "period": {"sample", "period", "era"},
        "era": {"sample", "period", "era"},
        "specification": {"specification", "spec"}, "spec": {"specification", "spec"}}


def _yr(k):
    return str(k)[:4]


def independence(about, varied):
    """Gate A. Returns (ok, message)."""
    a, v = about.lower().strip(), varied.lower().strip()
    if a not in DIMS:
        return None, f"unknown dimension '{about}' — use one of {sorted(DIMS)}"
    if v not in DIMS:
        return None, f"unknown dimension '{varied}' — use one of {sorted(DIMS)}"
    if v in SAME.get(a, {a}):
        return False, (f"NOT INDEPENDENT: your claim is about '{about}' and your robustness "
                       f"check varies '{varied}'. That is ONE result viewed several ways. "
                       f"Vary something else — sample/period is the usual answer.")
    return True, f"independent: claim about '{about}', robustness varies '{varied}'"


def stability(stat, keys, label="statistic", min_ratio=0.5, verbose=True):
    """
    Gate B. `stat(subset_of_keys) -> float or None`. Keys must start 'YYYY'.
    Re-runs on hostile subsamples. Returns (verdict, rows).
    """
    keys = set(keys)
    full = stat(keys)
    rows = [("FULL SAMPLE", full, len(keys))]
    if full is None:
        return "UNCOMPUTABLE", rows

    for name, (y0, y1) in CRISES.items():
        sub = {k for k in keys if not (y0 <= _yr(k) <= y1)}
        if len(sub) < len(keys) * 0.5:
            continue
        if len(sub) == len(keys):
            continue  # crisis not in sample; skip rather than pad the table
        rows.append((f"ex-{name}", stat(sub), len(sub)))

    allc = {k for k in keys if not any(y0 <= _yr(k) <= y1 for y0, y1 in CRISES.values())}
    if len(allc) >= len(keys) * 0.4:
        rows.append(("ex-ALL-crises", stat(allc), len(allc)))

    ys = sorted({_yr(k) for k in keys})
    if len(ys) >= 8:
        mid = ys[len(ys) // 2]
        rows.append(("first half", stat({k for k in keys if _yr(k) < mid}), 0))
        rows.append(("second half", stat({k for k in keys if _yr(k) >= mid}), 0))

    vals = [(n, v) for n, v in [(r[0], r[1]) for r in rows[1:]] if v is not None]
    verdict = "STABLE"
    flips = [n for n, v in vals if (v > 0) != (full > 0)]
    shrinks = [n for n, v in vals if abs(v) < abs(full) * min_ratio and (v > 0) == (full > 0)]
    if flips:
        verdict = "FAILS — SIGN FLIPS"
    elif shrinks:
        verdict = "FAILS — COLLAPSES"

    if verbose:
        print(f"\n  [B] SUBSAMPLE STABILITY — {label}")
        for n, v, c in rows:
            cs = f"n={c}" if c else ""
            vs = f"{v:+.3f}" if v is not None else "  n/a"
            mark = ""
            if v is not None and n != "FULL SAMPLE":
                if (v > 0) != (full > 0): mark = "  🔴 SIGN FLIP"
                elif abs(v) < abs(full) * min_ratio: mark = "  🔴 COLLAPSES"
            print(f"      {n:<20} {vs}  {cs:<8}{mark}")
        print(f"      => {verdict}")
        if verdict != "STABLE":
            print("      ⚠️  DO NOT SHIP. The result is carried by the excluded periods,")
            print("         not by the mechanism you are claiming.")
    return verdict, rows


def gate(claim, about, varied, stat=None, keys=None, label=None, min_ratio=0.5):
    """Both gates. Returns True only if BOTH pass. Prints a verdict."""
    print("\n" + "=" * 74)
    print(f" FINDING CHECK — {claim[:64]}")
    print("=" * 74)
    ok_a, msg_a = independence(about, varied)
    print(f"\n  [A] INDEPENDENCE")
    print(f"      {'✅' if ok_a else '🔴'} {msg_a}")
    ok_b = True
    if stat is not None and keys is not None:
        v, _ = stability(stat, keys, label or claim[:40], min_ratio)
        ok_b = (v == "STABLE")
    else:
        print("\n  [B] SUBSAMPLE STABILITY — 🟡 NOT RUN (no stat/keys supplied).")
        print("      A finding shipped without this is UNVERIFIED, not verified-clean.")
        ok_b = None
    final = bool(ok_a) and (ok_b is True)
    print(f"\n  VERDICT: {'✅ SHIP' if final else '🔴 DO NOT SHIP AS ESTABLISHED'}")
    if not final:
        print("  A failing gate does not mean the claim is false — it means you have not")
        print("  shown it. Ship it as a HYPOTHESIS, or fix the check.\n")
    else:
        print()
    return final


def _demo():
    """Reproduce HANS's 2026-08-28 failure and confirm this tool catches it."""
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
    from pmi_ism_lead_test import eurostat, fred, yoy, corr, shift
    print("  loading the real series used in the 8/28 finding…")
    conf = eurostat("ei_bsin_m_r2", geo="DE", indic="BS-ICI", s_adj="SA")
    cag = eurostat("sts_inpr_m", geo="DE", nace_r2="MIG_CAG", indic_bt="PRD", s_adj="SCA", unit="I21")
    dcog = eurostat("sts_inpr_m", geo="DE", nace_r2="MIG_DCOG", indic_bt="PRD", s_adj="SCA", unit="I21")
    us = yoy(fred("IPMAN"))
    dconf = {k: conf[k] - conf[f"{int(k[:4])-1}-{k[5:]}"] for k in conf if f"{int(k[:4])-1}-{k[5:]}" in conf}
    cy, dy = yoy(cag), yoy(dcog)
    inten = {k: cy[k] - dy[k] for k in set(cy) & set(dy)}

    def gap(keys):
        sub = {k: v for k, v in inten.items() if k in keys}
        if len(sub) < 60: return None
        vals = sorted(sub.values()); hi = vals[int(len(vals) * 2 / 3)]; lo = vals[int(len(vals) / 3)]
        cap = {k for k in sub if sub[k] >= hi}; dem = {k for k in sub if sub[k] <= lo}
        gs = []
        for lag in (2, 3, 4, 5, 6):
            sh = shift(dconf, lag)
            ra, _ = corr({k: v for k, v in sh.items() if k in cap}, us)
            rb, _ = corr({k: v for k, v in sh.items() if k in dem}, us)
            if ra is not None and rb is not None: gs.append(rb - ra)
        return sum(gs) / len(gs) if gs else None

    gate(claim="capex-led German moves are a weaker lead on US manufacturing",
         about="lag", varied="lag",
         stat=gap, keys=set(inten), label="mean (demand-capex) r-gap, lags 2-6mo")
    print("  ⇧ Both gates fire on the real 8/28 data. This tool would have stopped that ship.\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="ship-gate for empirical findings")
    ap.add_argument("--demo", action="store_true", help="reproduce HANS's 8/28 failure")
    ap.add_argument("--claim"); ap.add_argument("--about"); ap.add_argument("--varied")
    a = ap.parse_args()
    if a.demo: _demo()
    elif a.claim and a.about and a.varied:
        gate(a.claim, a.about, a.varied)
    else:
        ap.print_help()
