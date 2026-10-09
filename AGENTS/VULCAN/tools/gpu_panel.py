#!/usr/bin/env python3
"""
gpu_panel.py — VULCAN GPU-rental price instrument, panel GPU-PANEL-01.

WHY THIS EXISTS
  PROME ruled 2026-09-03 that VULCAN owns the GPU-rental price instrument.
  WATT then INVERTED the tier that same day: H100 1-year contract +40% while
  on-demand ran flat-to-down over the same window. A spot-only series would have
  read "softening demand" over a window contracted pricing rose 40% in. So the
  panel registers BOTH tiers plus the spread, and publishes its composition —
  because a flat lead against a +40% lag is either a genuine leading divergence
  or a broken panel, and only the spread-plus-panel distinguishes them.

  The panel was FROZEN 2026-09-13 (workbook/GPU_INSTRUMENT_SPEC.md §9) after the
  contract-tier reconnaissance the 9/11 addendum demanded. That reconnaissance
  returned a NEGATIVE and the negative is the finding: there is no publicly
  quoted 12-month H100 contract price at ANY of the four named vendors. Tier
  `contract` is therefore an EMPTY SET and writes an ERR: sentinel every reading
  until a member qualifies — it is never left blank and never faked by
  differencing a single-term row against a term-normalized index.

WHAT IS MECHANIZED AND WHAT IS NOT — stated so nobody mistakes one for the other
  MECHANIZED: tier `marketplace` (Vast.ai public bundles API — deterministic,
    reproducible, no login).
  NOT MECHANIZED: tiers `on_demand` and `index` are read by hand from vendor and
    index-vendor pages and supplied in the input JSON. They are HTML marketing
    surfaces whose format can change without notice; scraping them would fail
    silently in the one direction that matters. The tool VALIDATES what it is
    given and REFUSES to write when a check fails. `finding_adoption_is_not_
    validation` — the input being present is not the input being right.

VALIDATIONS (§9.6) — refuse to write, never degrade silently
  V1 unit      every price USD per GPU-hour; a node quote is divided by its
               stated GPU count and the divisor is recorded.       REFUSE
  V2 model     gpu_model == H100_SXM, direct or via the declared HGX mapping.
                                                                    REFUSE
  V3 purity    no tier mixes price_basis across its member cells.   REFUSE
  V4 spread    spread_pct written ONLY when both legs carry an identical
               declared price_basis; else the literal UNGRADEABLE.
  V5 n-floor   a cell under its floor writes an ERR: sentinel, not a number.
  V7 fresh     every hand-read cell is from THIS slot: a dated vintage must lie in
               [reading_date - 7d, reading_date + 1d] (7d = one weekly cadence
               interval, derived); vintage UNSPECIFIED requires `read_on` within
               +-1d of reading_date. A stale carry-forward is the L-16 failure —
               drop the vendor and let V5 write the sentinel.       REFUSE
  V6 cross     dispersion between the two index constructions is RECORDED every
               reading. NO BAND IS SET — §6 forbids any threshold on this
               instrument until >=4 rows exist AND a base rate is stated. A band
               picked from a sample of one is a free parameter.

USAGE
  python3 tools/gpu_panel.py --selftest
  python3 tools/gpu_panel.py --reading-date 2026-09-18 --input <panel_input.json>
  python3 tools/gpu_panel.py --reading-date 2026-09-18 --input <...> --write

  Without --write nothing is appended: the run prints the rows it WOULD write
  plus every validation verdict. Default is dry.
"""
from __future__ import annotations
import argparse, json, sys, urllib.request, urllib.parse
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LEDGER = HERE / "workbook" / "GPU_SERIES.tsv"
SPEC = "workbook/GPU_INSTRUMENT_SPEC.md §9"

PANEL_ID = "GPU-PANEL-01"

# --- the frozen composition (§9.3). Changing ANY of this mints a NEW panel id. ---
TIER_A_VENDORS = ("Lambda", "CoreWeave", "Nebius", "Crusoe")   # neocloud, directly quoted
TIER_A_MIN_N   = 3          # of 4
TIER_B_VENDOR  = "Vast.ai"
TIER_B_MIN_N   = 5          # offers
TIER_D_INDICES = ("SDH100RT", "OCPI-H100")
GPU_MODEL      = "H100_SXM"
UNIT           = "USD_per_GPU_hour"

# registered cadence. Reading 1 (2026-09-11) was MISSED.
# ⚠️ FIXED 2026-10-09: this was a hardcoded tuple ending 2026-10-02, so every slot of
# the 9/29 extension (10/09 → 11/27) would have been stamped OFF-CADENCE — a dated carry
# item that went stale without saying so. The cadence is now READ from the register it is
# registered in (live + fired archives); the seed below is only the original four.
CADENCE_SEED = ("2026-09-11", "2026-09-18", "2026-09-25", "2026-10-02")
CADENCE_MARK = "gpu-rental panel reading"


def load_cadence():
    """Registered slot dates from docket/CATALYSTS.tsv + archive/CATALYSTS_FIRED_*.tsv.
    Returns (set_of_dates, error_or_None). An unreadable register is REPORTED, never
    treated as 'everything is on cadence'."""
    dates, err = set(CADENCE_SEED), None
    paths = [HERE / "docket" / "CATALYSTS.tsv"] + sorted((HERE / "archive").glob("CATALYSTS_FIRED_*.tsv"))
    try:
        for pth in paths:
            for line in pth.read_text(encoding="utf-8").splitlines()[1:]:
                f = line.split("\t")
                if len(f) > 1 and CADENCE_MARK in f[1].lower():
                    dates.add(f[0].strip()[:10])
    except Exception as e:  # noqa: BLE001 — report, never swallow
        err = f"CADENCE-REGISTER-UNREADABLE:{type(e).__name__}"
    return dates, err


CADENCE, CADENCE_ERR = load_cadence()

# --- V7 freshness (added 2026-10-09, DAEDALUS profile refresh item 6: the tool accepted a
# 26-day-old hand-read price as a new reading). The bound is DERIVED, not picked: the cadence
# is weekly, so a hand-read older than one cadence interval belongs to an earlier slot.
MAX_AGE_DAYS = 7

VAST_URL = ("https://console.vast.ai/api/v0/bundles/?q=" + urllib.parse.quote(json.dumps(
    {"gpu_name": {"eq": "H100 SXM"}, "rentable": {"eq": True},
     "num_gpus": {"eq": 1}, "limit": 200})))

HEADER = ("asof_utc\treading_date\ttier\tinstrument\tvendor\tgpu_model\tunit\tprice_usd\t"
          "n_observations\tpanel_spec_id\tprice_basis\tspread_vs_other_tier_usd\tspread_pct\t"
          "source_class\tsource_url\tvalidation\tnotes")


class Refuse(Exception):
    """A REFUSE-class validation failed. Nothing is written."""


def median_lower(xs):
    """§9.5 tie convention: for even n the median is the LOWER of the two middle
    values. Deterministic and exact on a decimal series — never a float average.
    `finding_float_precision_empties_the_tie_set_and_voids_the_operator`."""
    s = sorted(xs)
    n = len(s)
    if n == 0:
        raise ValueError("median of empty set")
    return s[(n - 1) // 2]


def fetch_vast(timeout=45):
    """Tier `marketplace`: live per-GPU-hour asks, 1-GPU rentable H100 SXM."""
    req = urllib.request.Request(VAST_URL, headers={"User-Agent": "VULCAN/gpu_panel"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read().decode())
    out = []
    for o in d.get("offers", []):
        if o.get("gpu_name") != "H100 SXM":
            continue                      # V2 at the source
        ng = int(o.get("num_gpus") or 1)
        dph = o.get("dph_total")
        if dph is None or ng < 1:
            continue
        out.append(round(float(dph) / ng, 4))   # V1: per GPU-hour
    return out


# ----------------------------- validations -----------------------------------
def v1_unit(cells):
    for c in cells:
        if c.get("unit") != UNIT:
            raise Refuse(f"V1 unit: {c['vendor']} unit={c.get('unit')!r}, expected {UNIT}")
        if c.get("num_gpus", 1) != 1 and "divisor" not in c:
            raise Refuse(f"V1 unit: {c['vendor']} is a node quote with no recorded divisor")


def v2_model(cells):
    for c in cells:
        if c.get("gpu_model") != GPU_MODEL:
            raise Refuse(f"V2 model: {c['vendor']} gpu_model={c.get('gpu_model')!r}, "
                         f"expected {GPU_MODEL} (bare 'H100' does not map — §9.3)")


def v3_purity(cells):
    bases = {}
    for c in cells:
        bases.setdefault(c["tier"], set()).add(c["price_basis"])
    for tier, bs in bases.items():
        if len(bs) > 1:
            raise Refuse(f"V3 purity: tier {tier} mixes price_basis {sorted(bs)}")


def v4_spread(leg_a, leg_b):
    """Returns (spread_usd, spread_pct_as_text). UNGRADEABLE unless the bases match."""
    if leg_a["price_basis"] != leg_b["price_basis"]:
        return "", "UNGRADEABLE"
    d = round(leg_a["price"] - leg_b["price"], 4)
    base = (leg_a["price"] + leg_b["price"]) / 2.0
    return d, f"{round(100.0 * d / base, 2)}"


def v7_fresh(cells, reading_date):
    from datetime import date as _date, timedelta as _td
    rd = _date.fromisoformat(reading_date)

    def parse(v, what, c):
        try:
            return _date.fromisoformat(str(v)[:10])
        except ValueError:
            raise Refuse(f"V7 fresh: {c['vendor']} {what}={v!r} is not an ISO date")

    for c in cells:
        v = c.get("vintage", "")
        if str(v).upper() == "UNSPECIFIED":
            if "read_on" not in c:
                raise Refuse(f"V7 fresh: {c['vendor']} vintage UNSPECIFIED and no read_on — "
                             f"nothing proves the level was read at this slot")
            ro = parse(c["read_on"], "read_on", c)
            if abs((ro - rd).days) > 1:
                raise Refuse(f"V7 fresh: {c['vendor']} read_on {ro} is {abs((ro - rd).days)}d "
                             f"from reading_date {rd} (allowed +-1d)")
            continue
        vd = parse(v, "vintage", c)
        if vd > rd + _td(days=1):
            raise Refuse(f"V7 fresh: {c['vendor']} vintage {vd} is AFTER reading_date {rd} — typo?")
        if (rd - vd).days > MAX_AGE_DAYS:
            raise Refuse(f"V7 fresh: {c['vendor']} vintage {vd} is {(rd - vd).days}d old at "
                         f"reading_date {rd} (max {MAX_AGE_DAYS}d) — a stale carry-forward; "
                         f"re-read the page or drop the vendor [L-16]")


def v5_floor(n, floor, label):
    return None if n >= floor else f"ERR:UNGRADEABLE-n{n}-below-floor{floor}-{label}"


def v6_dispersion(levels):
    """RECORD ONLY. No band, by design — see the module docstring."""
    if len(levels) < 2:
        return None, "UNGRADEABLE-n1"
    lo, hi = min(levels), max(levels)
    return round(hi - lo, 4), f"{round(100.0 * (hi - lo) / ((hi + lo) / 2.0), 2)}"


# ------------------------------- row build -----------------------------------
def build_rows(reading_date, tier_a, tier_d, vast_asks, now=None):
    now = now or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    offc = "" if reading_date in CADENCE else \
        " OFF-CADENCE: reading_date is not a registered slot — whoever chooses the run times chooses the readings [L-21]."
    if CADENCE_ERR:
        offc += f" {CADENCE_ERR}: on/off-cadence status UNVERIFIED."

    cells = list(tier_a) + list(tier_d)
    v1_unit(cells); v2_model(cells); v3_purity(cells); v7_fresh(cells, reading_date)

    rows = []

    # --- tier on_demand: ONE ROW PER VENDOR. vendor is never aggregated away. ---
    for c in tier_a:
        note = (f"tier on_demand · {c['vendor']} · {UNIT} · vintage {c['vintage']} · "
                f"as quoted, not re-rounded.{offc}")
        if "divisor" in c:
            note += f" Node quote {c['node_price']}/{c['divisor']} GPUs."
        rows.append([now, reading_date, "on_demand", "dealer_quote", c["vendor"], GPU_MODEL,
                     UNIT, f"{c['price']}", "1", PANEL_ID, c["price_basis"], "", "",
                     "vendor_primary", c["url"], "V1 unit OK · V2 model OK · V3 purity OK", note])

    n_a = len(tier_a)
    floor_a = v5_floor(n_a, TIER_A_MIN_N, "tier-on_demand-vendors")

    # --- tier marketplace ---
    n_b = len(vast_asks)
    floor_b = v5_floor(n_b, TIER_B_MIN_N, "tier-marketplace-offers")
    if floor_b:
        rows.append([now, reading_date, "marketplace", "marketplace_quote", TIER_B_VENDOR,
                     GPU_MODEL, UNIT, floor_b, floor_b, PANEL_ID, "spot", "", "UNGRADEABLE",
                     "marketplace_api", VAST_URL, "V5 n-floor FAILED — ERR sentinel, not a number",
                     f"tier marketplace · {TIER_B_VENDOR} · {UNIT} · vintage {reading_date} · n={n_b} below floor {TIER_B_MIN_N}.{offc}"])
        b_med = None
    else:
        b_med = median_lower(vast_asks)
        rows.append([now, reading_date, "marketplace", "marketplace_quote", TIER_B_VENDOR,
                     GPU_MODEL, UNIT, f"{b_med}", f"{n_b}", PANEL_ID, "spot", "", "",
                     "marketplace_api", VAST_URL,
                     f"V1 unit OK · V2 model OK · V5 n={n_b}>={TIER_B_MIN_N} OK",
                     (f"tier marketplace · {TIER_B_VENDOR} · {UNIT} · vintage {reading_date} · 4dp · "
                      f"median under the lower-of-two-middle convention (§9.5); min {min(vast_asks)} max {max(vast_asks)}.{offc}")])

    # --- tier contract: THE EMPTY SET. Recorded every reading, never blank. ---
    rows.append([now, reading_date, "contract", "dealer_quote", "NONE-ADMISSIBLE", GPU_MODEL,
                 UNIT, "ERR:UNGRADEABLE-no-public-contract-quote",
                 "ERR:UNGRADEABLE-0-admissible-cells", PANEL_ID, "12mo", "", "UNGRADEABLE",
                 "vendor_primary", "SEARCH-NOT-FOUND:public-12mo-H100-SXM-quote-at-Lambda-CoreWeave-Nebius-Crusoe",
                 "V5 n-floor FAILED — empty set by reconnaissance, not by omission",
                 ("tier contract · no admissible vendor · reconnaissance 2026-09-13: Lambda fails C3 (term is a RANGE, "
                  "'2wk-1yr') and C1 (1yr+ = contact sales); CoreWeave/Crusoe fail C1 (contact sales); Nebius publishes no "
                  "committed tier; SemiAnalysis 1-yr series fails C1 (paid research). §9.4." + offc)])

    # --- tier index: one row per index, segment recorded (§3b res. 3) ---
    for c in tier_d:
        rows.append([now, reading_date, "index", "rental_index", c["vendor"], GPU_MODEL, UNIT,
                     f"{c['price']}", "1", PANEL_ID, c["price_basis"], "", "",
                     "index_vendor", c["url"],
                     "V1 unit OK · V2 model OK · V3 purity OK · reference contract UNSPECIFIED ⇒ term_normalized",
                     (f"tier index · {c['vendor']} segment={c['segment']} · {UNIT} · vintage {c['vintage']} · "
                      f"reference contract not published by the vendor ⇒ price_basis term_normalized; "
                      f"MAY NOT be differenced against a single-term row (§3b res. 2).{offc}")])

    # --- spread: on_demand vs marketplace. Both legs `spot` ⇒ gradeable. ---
    if floor_a or b_med is None:
        rows.append([now, reading_date, "spread", "marketplace_quote",
                     "on_demand-mean|" + TIER_B_VENDOR, GPU_MODEL, UNIT,
                     "ERR:UNGRADEABLE-leg-below-floor", "ERR:UNGRADEABLE-leg-below-floor",
                     PANEL_ID, "spot", "", "UNGRADEABLE", "vendor_primary",
                     "see the tier rows above", "V5 n-floor FAILED on a leg",
                     f"spread on_demand-minus-marketplace ungradeable: {floor_a or ''} {floor_b or ''}.{offc}"])
    else:
        a_mean = round(sum(c["price"] for c in tier_a) / n_a, 4)
        d, pct = v4_spread({"price": a_mean, "price_basis": "spot"},
                           {"price": b_med, "price_basis": "spot"})
        rows.append([now, reading_date, "spread", "dealer_quote",
                     "|".join(c["vendor"] for c in tier_a) + " vs " + TIER_B_VENDOR,
                     GPU_MODEL, UNIT, f"{a_mean}", f"{n_a + n_b}", PANEL_ID, "spot",
                     f"{d}", pct, "vendor_primary", "see the tier rows above",
                     f"V4 spread OK — both legs price_basis=spot · V1 unit OK",
                     (f"spread on_demand-mean {a_mean} minus marketplace-median {b_med} · members "
                      f"{'|'.join(c['vendor'] for c in tier_a)} · 4dp.{offc}")])

    # --- V6 index dispersion: RECORDED, no band ---
    lv = [c["price"] for c in tier_d]
    dsp, dpct = v6_dispersion(lv)
    rows.append([now, reading_date, "spread", "rental_index", "|".join(c["vendor"] for c in tier_d),
                 GPU_MODEL, UNIT,
                 f"{round(sum(lv)/len(lv),4)}" if lv else "ERR:UNGRADEABLE-no-index-leg",
                 f"{len(lv)}" if lv else "ERR:UNGRADEABLE-no-index-leg", PANEL_ID,
                 "term_normalized", f"{dsp}" if dsp is not None else "", dpct,
                 "index_vendor", "see the tier index rows above",
                 "V6 dispersion RECORDED — NO BAND SET (§6: no threshold until >=4 rows AND a stated base rate)",
                 (f"dispersion_index between {' and '.join(c['vendor'] for c in tier_d)} · both term_normalized · "
                  f"diagnostic only, never a market call; base rate to be stated at reading 4 (2026-10-02).{offc}")])
    return rows


def append(rows):
    if not LEDGER.exists():
        LEDGER.write_text(HEADER + "\n", encoding="utf-8")
    cur = LEDGER.read_text(encoding="utf-8")
    if not cur.endswith("\n"):
        cur += "\n"
    LEDGER.write_text(cur + "".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")


# -------------------------------- selftest -----------------------------------
def selftest():
    """Falsify the guards. A guard's own v1 fails on first RUN — so it is tested
    here on FIXTURES, not by observing that nothing has gone wrong in the field
    (`finding_test_the_guard_not_just_the_guarded`)."""
    ok = True

    def chk(label, cond):
        nonlocal ok
        print(("  ok   " if cond else "  FAIL ") + label)
        ok = ok and cond

    print("gpu_panel selftest — falsifying each guard on fixtures")
    # median tie convention: exact boundary fixture, not absence
    chk("median_lower even-n takes the LOWER middle (1.8689, not 1.93555)",
        median_lower([1.7356, 1.7356, 1.8022, 1.8455, 1.8689, 2.0022, 2.6681, 3.2329, 3.338, 4.5471]) == 1.8689)
    chk("median_lower odd-n is the true middle", median_lower([1.0, 2.0, 3.0]) == 2.0)

    base = dict(vendor="X", gpu_model=GPU_MODEL, unit=UNIT, tier="on_demand",
                price_basis="spot", price=1.0, vintage="2026-09-18", url="u")
    # V1 must FIRE on a wrong unit
    try:
        v1_unit([dict(base, unit="USD_per_node_hour")]); chk("V1 fires on a node unit", False)
    except Refuse: chk("V1 fires on a node unit", True)
    # V1 must FIRE on an undivided node quote
    try:
        v1_unit([dict(base, num_gpus=8)]); chk("V1 fires on a node quote with no divisor", False)
    except Refuse: chk("V1 fires on a node quote with no divisor", True)
    # V2 must FIRE on a bare H100
    try:
        v2_model([dict(base, gpu_model="H100")]); chk("V2 fires on bare 'H100'", False)
    except Refuse: chk("V2 fires on bare 'H100'", True)
    # V3 must FIRE on a mixed-basis tier
    try:
        v3_purity([dict(base), dict(base, vendor="Y", price_basis="12mo")])
        chk("V3 fires on a tier mixing price_basis", False)
    except Refuse: chk("V3 fires on a tier mixing price_basis", True)
    # V3 must NOT fire across DIFFERENT tiers with different bases (the neighbour case)
    try:
        v3_purity([dict(base), dict(base, vendor="Z", tier="index", price_basis="term_normalized")])
        chk("V3 does NOT fire across different tiers (neighbour case)", True)
    except Refuse: chk("V3 does NOT fire across different tiers (neighbour case)", False)
    # V4 must refuse to difference a term_normalized leg against a spot leg
    chk("V4 returns UNGRADEABLE on mismatched bases",
        v4_spread({"price": 3.9, "price_basis": "spot"},
                  {"price": 2.53, "price_basis": "term_normalized"})[1] == "UNGRADEABLE")
    chk("V4 grades when both legs are spot",
        v4_spread({"price": 4.0, "price_basis": "spot"},
                  {"price": 2.0, "price_basis": "spot"})[1] != "UNGRADEABLE")
    # V5 boundary fixture, exactly AT the floor
    chk("V5 passes exactly AT the floor (n==floor)", v5_floor(5, 5, "x") is None)
    chk("V5 fires one below the floor", v5_floor(4, 5, "x") is not None)
    # V6 records, and is ungradeable on a single index
    chk("V6 dispersion on the freeze levels 2.53/2.78 is 9.42%",
        v6_dispersion([2.53, 2.78])[1] == "9.42")
    chk("V6 is UNGRADEABLE with one index", v6_dispersion([2.53])[1] == "UNGRADEABLE-n1")
    # the empty contract tier must appear in EVERY build, never be dropped
    rows = build_rows("2026-09-18",
                      [dict(base, vendor=v, price=p) for v, p in
                       zip(TIER_A_VENDORS, (3.99, 6.155, 3.85, 3.90))],
                      [dict(base, vendor="SDH100RT", tier="index", price_basis="term_normalized",
                            price=2.53, segment="neo-cloud", vintage="UNSPECIFIED",
                            read_on="2026-09-18"),
                       dict(base, vendor="OCPI-H100", tier="index", price_basis="term_normalized",
                            price=2.78, segment="all", vintage="2026-09-18")],
                      [1.7356, 1.8022, 1.8455, 1.8689, 2.0022, 2.6681], now="T")
    chk("every build emits the empty contract tier",
        any(r[2] == "contract" and r[7].startswith("ERR:") for r in rows))
    chk("no row is blank in a required column",
        all(all(r[i].strip() for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15)) for r in rows))
    chk("off-cadence reading_date is declared in notes",
        "OFF-CADENCE" in build_rows("2026-09-14", [dict(base, vendor=v, price=1.0, vintage="2026-09-14") for v in TIER_A_VENDORS],
                                    [dict(base, vendor="SDH100RT", tier="index",
                                          price_basis="term_normalized", price=2.5,
                                          segment="neo-cloud", vintage="2026-09-14")],
                                    [1.0] * 6, now="T")[0][16])
    # V7 must FIRE on the exact defect DAEDALUS found: a 26-day-old hand price
    def v7(cells, rd):
        try:
            v7_fresh(cells, rd); return False
        except Refuse:
            return True
    chk("V7 fires on a 26-day-old vintage (the DAEDALUS case)",
        v7([dict(base, vintage="2026-09-13")], "2026-10-09"))
    chk("V7 passes exactly AT the bound (7d)", not v7([dict(base, vintage="2026-10-02")], "2026-10-09"))
    chk("V7 fires one day past the bound (8d)", v7([dict(base, vintage="2026-10-01")], "2026-10-09"))
    chk("V7 fires on a future vintage", v7([dict(base, vintage="2026-10-12")], "2026-10-09"))
    chk("V7 fires on UNSPECIFIED with no read_on", v7([dict(base, vintage="UNSPECIFIED")], "2026-10-09"))
    chk("V7 fires on UNSPECIFIED read 3 days off-slot",
        v7([dict(base, vintage="UNSPECIFIED", read_on="2026-10-06")], "2026-10-09"))
    chk("V7 passes UNSPECIFIED read at the slot",
        not v7([dict(base, vintage="UNSPECIFIED", read_on="2026-10-09")], "2026-10-09"))
    chk("V7 fires on a garbage vintage", v7([dict(base, vintage="last week")], "2026-10-09"))
    # the shipped TEMPLATE is the 9/13 freeze — fed unedited at a later slot it must be REFUSED
    try:
        tpl = json.loads((HERE / "workbook" / "GPU_PANEL_INPUT_TEMPLATE.json").read_text(encoding="utf-8"))
        chk("the unedited template is REFUSED at the 10/09 slot (stale carry-forward)",
            v7(tpl["tier_a"] + tpl["tier_d"], "2026-10-09"))
    except Exception as e:  # noqa: BLE001
        chk(f"template readable for the V7 test ({type(e).__name__})", False)
    # cadence must come from the register: the 9/29 extension slots are ON-cadence
    chk("cadence register readable", CADENCE_ERR is None)
    chk("2026-10-09 (reading 5) is a registered slot", "2026-10-09" in CADENCE)
    chk("2026-11-27 (reading 12) is a registered slot", "2026-11-27" in CADENCE)
    chk("an unregistered Saturday is NOT on cadence", "2026-10-10" not in CADENCE)
    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=f"GPU-rental panel reading ({PANEL_ID}); spec {SPEC}")
    ap.add_argument("--reading-date")
    ap.add_argument("--input", help="JSON with tier_a[] and tier_d[] hand-read levels")
    ap.add_argument("--write", action="store_true", help="append to the ledger (default: dry run)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.reading_date and a.input):
        ap.error("--reading-date and --input are required (or --selftest)")
    cfg = json.loads(Path(a.input).read_text(encoding="utf-8"))
    print(f"fetching tier marketplace live: {TIER_B_VENDOR} H100 SXM 1-GPU rentable offers ...")
    asks = fetch_vast()
    print(f"  n={len(asks)} offers")
    try:
        rows = build_rows(a.reading_date, cfg["tier_a"], cfg["tier_d"], asks)
    except Refuse as e:
        print(f"\nREFUSED — nothing written.\n  {e}")
        return 2
    for r in rows:
        print(f"  {r[2]:<12} {r[4][:34]:<34} {r[7]:<38} n={r[8]}")
    if a.write:
        append(rows)
        print(f"\nappended {len(rows)} rows -> {LEDGER}")
    else:
        print(f"\nDRY RUN — nothing written. Re-run with --write to append.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
