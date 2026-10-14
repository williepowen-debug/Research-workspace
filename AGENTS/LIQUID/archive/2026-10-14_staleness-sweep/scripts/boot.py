#!/usr/bin/env python3
"""
LIQUID Boot — live 3-dashboard sweep (Credit / Domestic / Foreign) in one command.

Pulls every load-bearing LIQUID figure from primary sources (FRED + yfinance via
FORGE/tools/market-data/fetch.py), classifies each against LIQUID thresholds, and
prints an alert-collapsed boot brief. Replaces ~13 manual `fetch.py` calls.

Alert labels are tied to LIQUID's actual thesis triggers (KILL / CONFIRM /
PRE-TRIGGER / TRIGGER-A / UNWIND / co-trigger), not invented independently.

⚠️  Run with the venv (yfinance lives there):
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --verbose   # every value + 6-print trend
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --quick     # FRED only (skip slow yfinance)
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --selftest  # validate CATALYSTS/PREDICTIONS/KB + fetch import

Basis canon (declare when citing a number downstream): FRED OAS / H.15 are end-of-day
computed and publish T+1 — the latest print may be 1-2 sessions back, more over a
weekend. yfinance = last close (raw). Brent BZ=F front-month is NOT the ICE settle;
USD/JPY JPY=X is NOT the 5pm-ET NY close. H.4.1 series (WRESBAL) are dated by their
as-of Wednesday. Verify load-bearing triggers against the canonical basis before acting.

Exit code = FETCH health only (non-zero if any series failed to pull) — NOT alert state:
a red thesis trigger (HY >280 or <260, USD/JPY >160, SRF >50) still exits 0. Parse stdout for alerts.
"""

import calendar
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LIQUID_DIR = SCRIPTS_DIR.parent                    # AGENTS/LIQUID
WORKSPACE = SCRIPTS_DIR.parents[2]                 # AGENTS/LIQUID/scripts -> Research-workspace
FETCH_DIR = WORKSPACE / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(FETCH_DIR))

try:
    from fetch import fred_fetch, price_fetch
except Exception as e:                              # pragma: no cover
    print(f"FATAL: cannot import FORGE fetch.py from {FETCH_DIR}: {e}")
    sys.exit(2)

RESULTS = []   # list of row dicts: dashboard,label,display,marker,note,asof,trend,headline
ERRORS = 0


def add(dashboard, label, display, marker, note, asof="", trend="", headline=False, ref=False):
    """`ref=True` marks a REFERENCE-ONLY ⚪ row (grades nothing) — the only ⚪ the collapsed view may
    hide. Every other ⚪ is an UNGRADEABLE/STALE-BASIS/DATE-UNVERIFIED row and is ALWAYS shown
    (CATO 9/17 §2, repaired 2026-09-22: ⚪ carried both meanings and the default view hid both, so a
    gate leg that failed CLOSED to ⚪ vanished and the dashboard printed "all clear")."""
    RESULTS.append(dict(dashboard=dashboard, label=label, display=display, marker=marker,
                        note=note, asof=asof, trend=trend, headline=headline, ref=ref))


def fred_series(sid, n=6):
    """Return (latest_float, asof_date, [recent floats newest-first], error_or_None)."""
    global ERRORS
    obs = fred_fetch(sid, limit=n)
    if not obs or (isinstance(obs[0], dict) and "error" in obs[0]):
        ERRORS += 1
        return None, None, [], (obs[0]["error"] if obs else "no data")
    vals = []
    for o in obs:
        try:
            vals.append(float(o["value"]))
        except (ValueError, KeyError, TypeError):
            pass
    if not vals:
        ERRORS += 1
        return None, None, [], "no numeric values"
    return vals[0], obs[0]["date"], vals, None


def fred_pairs(sid, n=14):
    """Return ([(date, value)] newest-first, error_or_None) — dates PRESERVED.

    fred_series() keeps only obs[0]["date"] and throws the rest away. That is
    exactly what let the IORB basis mismatch below run unseen: a spread built
    from two series' *latest* values is only a measurement when both latests
    fall on the same day.
    """
    obs = fred_fetch(sid, limit=n)
    if not obs or (isinstance(obs[0], dict) and "error" in obs[0]):
        return [], (obs[0]["error"] if obs else "no data")
    out = []
    for o in obs:
        try:
            out.append((o["date"], float(o["value"])))
        except (ValueError, KeyError, TypeError):
            pass
    return out, (None if out else "no numeric values")


def as_of(pairs, target):
    """Value of a series ON or BEFORE `target` (pairs newest-first). -> (value, date)."""
    for dt, val in pairs:
        if dt <= target:
            return val, dt
    return None, None


def diff_dated(dash, label, a, a_d, b, b_d, classify, headline=False):
    """Difference two series that MUST share an observation date. Fails CLOSED.

    Generalises the repo-vs-IORB repair (KB-LIQ-126) to EVERY two-leg composite in this
    brief. THE RULE WAS NEVER ABOUT IORB: any two legs differenced must come from the same
    session, or the difference is a cross-date artifact rendered as a level. Written after
    WALTER pointed out (2026-09-17) that its own version of this guard existed but was
    scoped to CONTRACT MONTHS and therefore missed every case that night -- "the right rule
    and the wrong noun." I had just done the same thing: fixed the repo block and left three
    identical defects in the credit block of this same file, all three rendering with NO
    date at all. Any event that re-dates ONE leg is the same bug: a policy change, a
    publisher revision, a fill-forward, a different market calendar.
    """
    if a is None or b is None:
        add(dash, label, "N/A", "🟠",
            f"UNAVAILABLE — a leg failed to fetch; {label} missing this boot", headline=headline)
        return None
    val = a - b
    if a_d and b_d and a_d != b_d:
        add(dash, label, f"{val:.0f}bps", "⚪",
            f"UNGRADEABLE — legs are DIFFERENT SESSIONS ({a_d} vs {b_d}); a cross-date "
            f"difference is an artifact, not a level, and is NOT graded this boot",
            a_d, headline=headline)
        return None
    if not (a_d and b_d):
        # Falsification run 2026-09-17 caught this branch grading 🟢 on "[both date?]".
        # If a date is missing the legs CANNOT be shown to share a session, so grading it
        # is the same benign-looking-number-on-an-unverifiable-basis pattern this helper
        # exists to remove. Keep the value (FORGE's fail-safe: never null a number on a
        # failed date lookup), withhold the GRADE.
        add(dash, label, f"{val:.0f}bps", "⚪",
            f"NOT GRADED — a leg has no observation date ({a_d or 'none'} / {b_d or 'none'}), "
            f"so the legs cannot be shown to share a session. Value kept, grade withheld",
            a_d or b_d or "date?", headline=headline)
        return None
    m, n = classify(val)
    add(dash, label, f"{val:.0f}bps", m, f"{n}  [both {a_d}]", a_d, headline=headline)
    return val


def trend_str(vals, mult=1.0, dp=0):
    return " → ".join(f"{v * mult:.{dp}f}" for v in reversed(vals[:6]))


# ---------------------------------------------------------------------------
# Dashboard 1 — CREDIT SPREADS
# ---------------------------------------------------------------------------

def build_credit():
    ccc = bb = hy_bps = None  # for the CCC-BB tail-gap + HY-IG basis composites
    ccc_d = bb_d = hy_d = ig_d = None   # each leg's OWN obs date — see diff_dated()

    # HY OAS (macro) — config.py bands (SENTRY retune 6/26): 🟢<265 / 🟡265-280 / 🔴>280 X1 master.
    # <260 ×2 closes = bear-axis KILL — a TWO-WAY secondary the single-sided config.classify can't
    # encode (config kill_below=260), overlaid here as red; mirrors the live hy_oas_watch.py.  [headline]
    v, d, tr, err = fred_series("BAMLH0A0HYM2")
    if err:
        add("CREDIT", "HY OAS", "ERR", "🔴", f"fetch error: {err}", headline=True)
    else:
        bps = round(v * 100)   # whole bp (FRED 0.01 pct) — DAEDALUS #2/#5 rounding rule, 9/29
        hy_bps = bps
        hy_d = d
        # crun HOISTED 2026-09-02 (blind cold read, finding B7). It was defined inside the
        # 260-265 else-block, so the `bps < 260` branch above it had NO RUN CHECK AVAILABLE and
        # printed a two-close label off a ONE-close observation. See the <260 branch below.
        # tr is newest-first; count the CURRENT consecutive run only.
        def crun(lim):
            c = 0
            for x in (tr or []):
                if round(x * 100) < lim: c += 1
                else: break
            return c
        # Label corrected 2026-07-30 (stale-data sweep). THRESHOLD UNCHANGED at >=280 — string only.
        # Two defects in the old label, both load-bearing and printed at EVERY boot:
        #   (1) "X1 MASTER TRIGGER FIRED" violates GATE-LIQ-079 rider R1 — X1 is CONJUNCTIVE
        #       (level leg + BROCK's wrapper-leads leg) and a 280 print alone must never be
        #       reported anywhere as "X1 MET". BROCK's half is independently NOT MET.
        #   (2) "credit-recognition" is refuted by analysis/2026-07-30_hy-attribution.md —
        #       the +19bp to 287 is 68-84% broad DM HY beta, ~0% bank/CRE, and BB-led/flow-shaped,
        #       i.e. the opposite of a quality-recognition event.
        # ⛔ ONE SPELLING, 2026-09-29 (DOCKET L493 ②; CATO MEDIUM open since 9/22). The X1 letter
        # (KILL_MEMO ladder + §B) is STRICT `>280`; this branch printed "HY >=280 LEVEL LEG MET",
        # so 280.0 [9/24] rendered as X1-level-met when the letter says NOT met. Now: X1 rungs are
        # strict `>` as lettered; exactly 280.0 gets its own line naming the THREE rules that read
        # it differently (config zone >=280 red · RED-FT-01 >=280 counts · X1 >280 does NOT).
        # The ladder's >300 / >320 rungs (absent here, CATO) are rendered as LEVEL labels only —
        # "sustained" is a count this label does not make. No state is restated: the 7/30
        # attribution and the arbiter answer were dated reads printed on EVERY boot; they now
        # live at their surfaces (KILL_MEMO header + §D), and this line points there. The letter is
        # '>280 SUSTAINED' with no session count, so a label TAGS and never says MET (reader rd 2).
        # Compare at 0.1bp: FRED publishes 0.01 pct, so rounding removes any float residue.
        b1 = round(bps, 1)
        X1_TAIL = "X1 half ONLY, never 'X1 MET' (conjunctive with BROCK's wrapper-leads half; live state → KILL_MEMO header + §D; RED-FT-01 ≥280 is RED's count)"
        if   b1 > 320: m, n = "🔴", f"HY >320 — CONFIRMATION rung TAGGED (letter: >320 SUSTAINED, counted on KILL_MEMO, not here); X1 level leg also tagged: {X1_TAIL}"
        elif b1 > 300: m, n = "🔴", f"HY >300 — approaching the 320 confirmation ({320 - bps:.0f}bp); X1 level leg TAGGED (letter: >280 SUSTAINED): {X1_TAIL}"
        elif b1 > 280: m, n = "🔴", f"HY >280 (strict) — X1 level leg TAGGED, not met: the letter is >280 SUSTAINED, counted on KILL_MEMO, not by this label — {X1_TAIL}"
        elif b1 == 280: m, n = "🔴", "HY AT 280.0 — red zone (config ≥280) and RED-FT-01 counts it (≥280), but it never counts toward the X1 level leg (letter is strict >280 sustained)"
        elif bps >= 265: m, n = "🟡", f"X1 APPROACH (265-280 band) — {280 - bps:.0f}bps to the 280 line (X1 level leg = >280 sustained)"
        elif bps < 260:
            # ---- CORRECTED 2026-09-02, BLIND COLD READ FINDING B7. NO THRESHOLD INVENTED OR MOVED. ----
            # This branch printed "BEAR-AXIS KILL (<260 x2 closes)" off a SINGLE sub-260 print.
            # It had no run check at all -- crun() was defined below, inside the 260-265 else-block,
            # and was wired to the 265 and 270 rungs but NOT to the kill line itself. So the
            # DECLARED "machine primary" for GATE-HY-REKILL implemented a ONE-close condition
            # wearing a TWO-close label: the exact inverse of KB-LIQ-109's dead-QUIET defect on the
            # same surface, and the more dangerous direction because it FIRES rather than misses.
            # Found by a blind reader briefed to GRADE the gate, not review it -- three desks had
            # read this file the same evening and none of us saw it.
            r260 = crun(260)
            if r260 >= 2:
                m, n = "🔴", f"BEAR-AXIS KILL FIRED — HY <260 on {r260} CONSECUTIVE closes (GATE-HY-REKILL). Credit-thesis invalidation, NOT a stress event. ⚠️ KB-LIQ-105 two-sided guard applies: confirm SUBSTANCE with BROCK before acting; a tape-only compression is a tape-kill"
            else:
                m, n = "🟠", f"HY <260 on the LATEST print only ({bps:.0f}) — GATE-HY-REKILL 1-of-2, NOT FIRED. The gate needs TWO CONSECUTIVE closes strictly <260; one print is not a kill"
        else:
            # ---- KILL-SIDE LADDER WIRED 2026-08-28 (KB-LIQ-109). NO THRESHOLD INVENTED HERE. ----
            # This band rendered a flat 🟢 "green (260-265)" while workbook/KILL_MEMO_HY_OAS_260.md
            # § KILL/EXIT side already registered TWO rungs inside it, in a table whose own column
            # is headed "boot.py label":
            #     <270 sustained >=2 sessions -> 🟡 PRE-TRIGGER
            #     <265 sustained >=2 sessions -> 🟠 TRIGGER A
            # The memo asserted a rendering that did not exist. DEAD-QUIET direction (misses a
            # signal), found live at 263bps [8/27] = 3bp from the kill and with PRE-TRIGGER already
            # satisfied (267 [8/26] -> 263 [8/27]) while this line printed GREEN.
            # Sibling class: KB-LIQ-104 / 106 / 107 (dead bands), but those were dead-LOUD.
            # crun() is hoisted above the if-chain (2026-09-02, cold-read B7).
            r265, r270 = crun(265), crun(270)
            if bps < 265 and r265 >= 2:
                m, n = "🟠", f"TRIGGER A — HY <265 sustained {r265} sessions (KILL_MEMO ladder). Thesis-confidence event; book FLAT so no cut to make. {bps - 260:.0f}bps to the 260 kill"
            elif bps < 265:
                m, n = "🟠", f"TRIGGER A 1-of-2 — HY <265 on the latest print only ({bps:.0f}). {bps - 260:.0f}bps to the 260 kill / {280 - bps:.0f}bps to 280. ⚠️ read against the tail: a tape-only compression is what KB-LIQ-105 blocks"
            elif r270 >= 2:
                m, n = "🟡", f"PRE-TRIGGER — HY <270 sustained {r270} sessions (KILL_MEMO ladder). {bps - 260:.0f}bps to the 260 kill"
            else:
                m, n = "🟢", f"260-265 band, ladder rungs NOT sustained — {bps - 260:.0f}bps to 260 kill / {280 - bps:.0f}bps to 280 X1 trigger"
        add("CREDIT", "HY OAS", f"{bps:.0f}bps", m, n, d, trend_str(tr, 100, 0), headline=True)

    # CCC OAS — >1000 trip
    v, d, tr, err = fred_series("BAMLH0A3HYC")
    if not err:
        ccc = round(v * 100)
        ccc_d = d
        # YELLOW FLOOR SOURCED FROM THE SHARED CONFIG 2026-08-28 (DAEDALUS wiring-sweep item 2).
        # Was hand-typed 960 while FORGE config.py carries CCC yellow (900, 1000) — a fork a
        # SENTRY retune would propagate to hy_oas_watch.py and NOT to here. Not diverging on
        # today's 1031bps print; wired before it does. If the import fails we fall back to the
        # historical 960 and SAY SO on the row rather than showing a silently-forked band.
        try:
            from config import SERIES as _CFG   # NB: a LIST of dicts, not a dict — search by "name"
            _lo = float(next(x for x in _CFG if x.get("name") == "CCC OAS")["yellow"][0]); _src = ""
        except Exception as _e:
            _lo = 960.0; _src = " ⚠️ band = LOCAL FALLBACK 960 (config.py unreachable)"
        if ccc > 1000:  m, n = "🔴", "CCC tail >1000 trip" + _src
        elif ccc > _lo: m, n = "🟡", f"{1000 - ccc:.0f}bps below 1000 trip (yellow floor {_lo:.0f})" + _src
        else:           m, n = "🟢", ""
        add("CREDIT", "CCC OAS", f"{ccc:.0f}bps", m, n, d, trend_str(tr, 100, 0))
    else:
        add("CREDIT", "CCC OAS", "ERR", "🟠", f"fetch error: {err}")

    # BB OAS — feeds the CCC-BB tail-gap (NEXUS R3 pin)
    v, d, tr, err = fred_series("BAMLH0A1HYBB")
    if not err:
        bb = round(v * 100)
        bb_d = d
        add("CREDIT", "BB OAS", f"{bb:.0f}bps", "🟢", "(feeds CCC-BB gap)", d, trend_str(tr, 100, 0))
    else:
        add("CREDIT", "BB OAS", "ERR", "🟠", f"fetch error: {err}")

    # CCC-BB tail-gap — NEXUS R3 / KB-LIQ-058 pin; falsifier <~400  [headline]
    def _gap_band(g):
        if g < 400:   return "🔴", "PIN BROKEN (<400) — bifurcation falsified (NEXUS R3 falsifier)"
        elif g < 500: return "🟠", "tail-gap compressing toward the <400 falsifier"
        return "🟢", "pin INTACT — quality bifurcation wide (KB-LIQ-058)"
    diff_dated("CREDIT", "CCC-BB gap", ccc, ccc_d, bb, bb_d, _gap_band, headline=True)

    # IG OAS — mandate-extension SECONDARY row (7/1): IG widening while HY compressed = credit-cycle
    # inflection LEADING the HY>280 watch. 2026 range 73-94; >94 = range break, >110 = regime.
    ig_bps = None
    v, d, tr, err = fred_series("BAMLC0A0CM")
    if not err:
        ig_bps = round(v * 100)
        ig_d = d
        if ig_bps > 110:  m, n = "🔴", "REGIME (>110) — IG leads when transmission is balance-sheet, not credit"
        elif ig_bps > 94: m, n = "🟠", "2026-HIGH BREAK (>94) — leading-indicator inflection candidate"
        else:             m, n = "🟢", f"benign ({94 - ig_bps:.0f}bps below the 94 range-high)"
        add("CREDIT", "IG OAS", f"{ig_bps:.0f}bps", m, n, d, trend_str(tr, 100, 0))
    else:
        add("CREDIT", "IG OAS", "ERR", "🟠", f"fetch error: {err}")

    # HY−IG basis (mandate ext.) — 2026 range 189-253; flat basis + wide tail = bifurcation signature
    def _basis_band(b):
        if b > 250:   return "🟠", "junk-specific DECOMPRESSION (2026 high 253, 3/30 stress)"
        elif b < 180: return "🟡", "complacency extreme (below the 2026 low 189)"
        return "🟢", "flat — no aggregate decompression (stress stays tail-only)"
    diff_dated("CREDIT", "HY-IG basis", hy_bps, hy_d, ig_bps, ig_d, _basis_band)

    # Euro HY (mandate ext. TERTIARY, coordinate BOND) — EU-led credit divergence watch
    v, d, tr, err = fred_series("BAMLHE00EHYIOAS")
    if not err:
        eu = round(v * 100)
        # ⚠️ HIGHEST cross-date risk of any composite in this brief, and the reason the
        # diff_dated() rule is not an IORB story: Euro HY follows the EUROPEAN holiday
        # calendar and US HY the US one, so these two legs are GUARANTEED to disagree on
        # dates several times a year — Easter Monday, Whit Monday, Boxing Day, July 4th.
        # On each of those the old inline `eu - hy_bps` silently differenced two different
        # sessions and printed the result as a level. Unlike the repo case this needs no
        # policy event to fire; the calendar does it unprompted.
        if hy_bps is None:
            m, n = "🟢", "(US HY unavailable for the differential)"
        elif d and hy_d and d != hy_d:
            m, n = "⚪", (f"Euro−US differential UNGRADEABLE — Euro HY [{d}] and US HY [{hy_d}] are "
                         f"DIFFERENT SESSIONS (European vs US holiday calendar). The LEVEL below "
                         f"stands; the differential is not computed this boot")
        else:
            diff = eu - hy_bps
            m, n = (("🟠", f"EU-led divergence (Euro−US {diff:+.0f}bps > +50) [both {d}]") if diff > 50
                    else ("🟢", f"(Euro−US {diff:+.0f}bps) [both {d}]"))
        add("CREDIT", "Euro HY OAS", f"{eu:.0f}bps", m, n, d, trend_str(tr, 100, 0))


# ---------------------------------------------------------------------------
# Dashboard 2 — DOMESTIC PLUMBING
# ---------------------------------------------------------------------------

def build_domestic():
    sofr = iorb = None

    v, d, tr, err = fred_series("SOFR")
    if err:
        add("DOMESTIC", "SOFR", "ERR", "🔴", f"fetch error: {err}")
    else:
        sofr = v
        m, n = ("🟠", "above 3.70") if v > 3.70 else ("🟢", "")
        add("DOMESTIC", "SOFR", f"{v:.2f}%", m, n, d, trend_str(tr, 1, 2))

    # ---- BASIS REPAIR 2026-09-17 (see the repo-vs-IORB block below). IORB is now carried
    # as DATED PAIRS, because every spread under it must be aligned to its own leg's
    # observation date rather than to IORB's latest.
    iorb_pairs, iorb_err = fred_pairs("IORB", n=14)
    if iorb_err or not iorb_pairs:
        add("DOMESTIC", "IORB", "ERR", "🔴", f"fetch error: {iorb_err or 'no data'}")
        iorb_pairs = []
    else:
        d_iorb, iorb = iorb_pairs[0][0], iorb_pairs[0][1]
        add("DOMESTIC", "IORB", f"{iorb:.2f}%", "🟢", "(ceiling ref)", d_iorb)
        # A policy move is a REGIME event and used to print nowhere in this brief.
        prior = next(((dt, val) for dt, val in iorb_pairs if val != iorb), None)
        if prior:
            dmove = (iorb - prior[1]) * 100
            # first observation at the NEW level = the move's effective date (pairs newest-first)
            eff = min(dt for dt, val in iorb_pairs if val == iorb and dt > prior[0])
            if d is None or d < eff:
                add("DOMESTIC", "IORB Δ (policy)", f"{dmove:+.0f}bps", "🔴",
                    f"POLICY RATE MOVED — {prior[1]:.2f}% [{prior[0]}] → {iorb:.2f}% [eff. {eff}]. "
                    f"Latest SOFR [{d}] PRE-DATES the move: every repo-vs-IORB spread below "
                    f"straddles it until the post-move repo print publishes", eff)
            else:
                # 2026-09-22: this row used to stay 🔴 "straddles" for as long as the move sat in
                # the 14-obs window (~2 weeks), days after post-move repo had published — a stale
                # alarm, and a 🔴 that means nothing trains the reader to skip 🔴.
                add("DOMESTIC", "IORB Δ (policy)", f"{dmove:+.0f}bps", "🟡",
                    f"policy move {prior[1]:.2f}% → {iorb:.2f}% effective {eff}; post-move SOFR has "
                    f"published [{d}] so repo-vs-IORB spreads are on the new ceiling", eff)

    # ---- BASIS REPAIR 2026-09-17 (KB-LIQ-126). Every repo-vs-IORB spread in this block
    # was `latest_repo - latest_IORB`, with NO date check and (for SOFR-IORB) no date
    # printed at all. IORB is stamped on its EFFECTIVE date and runs 1-2 days AHEAD of
    # the T+1 repo prints, so the two legs are routinely a different day.
    #   On an unchanged policy rate that mismatch is worth 0bp and is INVISIBLE. On a
    #   policy-change date it is worth the full move — and in the BENIGN direction: a
    #   hike lifts IORB, driving every spread sharply negative and printing
    #   "no funding stress" at maximum confidence on the one day the funding regime
    #   actually shifted. Error correlated with the event the gate exists to catch.
    #   Measured 2026-09-17, the 9/16 FOMC +25bp (IORB 3.65 [9/16] -> 3.90 [9/17]):
    #     row            printed   date-matched
    #     SOFR-IORB       -28bp      -3bp
    #     SOFR75-IORB     -23bp      +2bp
    #     SOFR99-IORB     -20bp      +5bp   <-- GATE-LIQ-079 ARM leg
    #   All three off by exactly the 25bp hike. The 079 cushion to its +30 ARM line
    #   printed 50bp against an actual 25bp: HALF THE CUSHION WAS AN ARTIFACT.
    # Same family and same dead-quiet direction as KB-LIQ-113 four rows down — that
    # repair fixed WHICH SERIES the leg used and never asked WHICH DAY it came from.
    def _iorb_aligned(leg_date):
        """IORB on the repo leg's OWN observation date. -> (value, date, matched_exactly)."""
        if not leg_date or not iorb_pairs:
            return None, None, False
        val, dt = as_of(iorb_pairs, leg_date)
        return val, dt, (dt == leg_date)

    # SOFR-IORB spread — sustained >0 = funding stress
    if sofr is not None:
        i_al, i_d, exact = _iorb_aligned(d)
        if i_al is None:
            add("DOMESTIC", "SOFR-IORB", "UNGRADEABLE", "⚪",
                "no IORB observation on or before the SOFR print — NOT graded; "
                "do not read the absence of a marker as clean", d)
        else:
            spr = round((sofr - i_al) * 100)
            if spr > 0:  m, n = "🟠", "ABOVE ceiling (>0) — re-open KB-LIQ-051 (verify non-mechanical, 3+ sessions)"
            else:        m, n = "🟢", "negative/clean — no funding stress"
            n += f"  [date-matched: SOFR {sofr:.2f} − IORB {i_al:.2f}, both {d}]"
            if not exact:
                m = "⚪"
                n = (f"STALE-BASIS: nearest IORB is [{i_d}], SOFR is [{d}] — spread NOT "
                     f"date-matched, treat as UNGRADEABLE, not clean")
            add("DOMESTIC", "SOFR-IORB", f"{spr:+.0f}bps", m, n, d)

    # SOFR dispersion (mandate ext. 7/1) — the tail is the stress read, not the median.
    # Alerts require NON-quarter-end sustain (Q-end turns print wide mechanically: 6/30 = 75th +8 / 99th +12).
    p75, d75, _, e75 = fred_series("SOFR75")
    p99, d99, _, e99 = fred_series("SOFR99")
    i75, i75_d, i75_exact = _iorb_aligned(d75)
    if not e75 and i75 is not None:
        s75 = round((p75 - i75) * 100)
        # KB-LIQ-106 (2026-08-27): the old ">= 0 = broad pressure" line is DEAD — it was
        # cleared by the MEDIAN 2026 day (89.5% of sessions) and printed a false 🟠 here
        # every boot. It died of a five-year regime migration, not bad construction, so a
        # replacement FIXED band would re-die on the same schedule. Deviation-vs-regime
        # (base-rated z) now drives the marker; the drift is reported, never banded.
        try:
            import sofr_dispersion as _sd
            _a = _sd.analyze(_sd._load())
            _m, _n = _sd.classify(_a)
            if not i75_exact:
                _m, _n = "⚪", (f"STALE-BASIS: SOFR75 [{d75}] vs nearest IORB [{i75_d}] — "
                               f"NOT date-matched, UNGRADEABLE, not calm")
            add("DOMESTIC", "SOFR75-IORB", f"{s75:+.0f}bps", _m, _n, d75)
        except Exception as _e:                       # fail LOUD, never silently back to the dead band
            add("DOMESTIC", "SOFR75-IORB", f"{s75:+.0f}bps", "⚪",
                f"dispersion instrument UNAVAILABLE ({type(_e).__name__}) — level shown raw, "
                f"NOT graded; do not read the absence of a marker as calm", d75)
    if e75 or e99:
        add("DOMESTIC", "SOFR dispersion", "ERR", "🔴",
            f"fetch error (SOFR75={e75 or 'ok'} / SOFR99={e99 or 'ok'}) — dispersion rows BLIND; "
            f"do not read their absence as calm")
    # ---- BASIS REPAIR 2026-08-28 (KB-LIQ-113; DAEDALUS GATES audit row 14). ----
    # This line rendered SOFR99 MINUS SOFR (the median) and was read as GATE-LIQ-079's ARM
    # leg. The gate is specified on SOFR99 MINUS IORB — the 99th percentile of repo against
    # the POLICY CEILING — and its definition surface has said so explicitly since 2026-07-17
    # (FUNDING_SEIZURE_GATE_SCOPED.md item 5: "acute leg = SOFR99-IORB ... not 99pct-SOFR.
    # This spec adopts SOFR99-IORB throughout"). THE SPEC WAS ALREADY CORRECT; the instrument
    # was never brought along, so a live gate could not fire correctly for 42 days.
    #   Why nobody caught it: median wedge between the two bases = +0.0bp (n=273). They agree
    #   on the ordinary day and diverge -15 to +32bp in the tail — a spread LARGER than the
    #   30bp ARM line itself. Measured: days >= +30bp on the CORRECT basis 6/273 (2.2%); on
    #   the rendered basis 0/273 (0.0%). The wrong instrument would have missed EVERY arm-day
    #   in the sample. Dead-QUIET direction: it under-reports exactly when the gate matters.
    #   Note the SOFR75 line four rows above ALREADY used IORB — the correct pattern was
    #   sitting one line up from the wrong one.
    # Both quantities now render; ONLY the IORB-based row is labelled as the gate leg.
    i99, i99_d, i99_exact = _iorb_aligned(d99)
    if not e99 and i99 is not None:
        # DAEDALUS #5 rounding order (2026-09-29): legs AS PUBLISHED (2dp %), subtract, ×100, ROUND to whole bp,
        # THEN compare. Unrounded, 118 plausible pairs (e.g. 3.00−2.70) compute 29.999999… and MISS an exact +30.
        s99 = round((p99 - i99) * 100)
        if s99 >= 30:   m, n = "🔴", f"GATE-LIQ-079 ACUTE LEG AT/ABOVE +30bp — check non-calendar AND ≥2 consecutive before calling ARMED"
        elif s99 >= 20: m, n = "🟠", f"tail elevated — {30 - s99:.0f}bps under the +30 ARM line"
        else:           m, n = "🟢", f"tail contained — {30 - s99:.0f}bps under the +30 ARM line"
        n += f"  [date-matched: SOFR99 {p99:.2f} − IORB {i99:.2f}, both {d99}]"
        # This is a LIVE GATE leg — it fails CLOSED, never to a benign-looking number.
        if not i99_exact:
            m, n = "⚪", (f"UNGRADEABLE — SOFR99 [{d99}] vs nearest IORB [{i99_d}] are different "
                         f"days; GATE-LIQ-079's ARM leg is NOT graded this boot. An unaligned "
                         f"spread is not a cushion — do not read it as contained")
        add("DOMESTIC", "SOFR99−IORB (079 ARM leg)", f"{s99:+.0f}bps", m, n, d99)
    elif not e99:
        add("DOMESTIC", "SOFR99−IORB (079 ARM leg)", "UNGRADEABLE", "⚪",
            "no IORB observation on or before the SOFR99 print — GATE-LIQ-079 ARM leg NOT "
            "graded; absence of a marker is not calm", d99)
    if not e99 and sofr is not None:
        s99m = round((p99 - sofr) * 100)
        add("DOMESTIC", "SOFR99−SOFR (dispersion)", f"{s99m:+.0f}bps", "⚪",
            "intra-distribution spread — NOT the 079 leg (that is SOFR99−IORB, above)", d99, ref=True)

    # 2Y — front-end reference (FOMC-day hawkish reprice tell)
    v, d, tr, err = fred_series("DGS2")
    if err:
        add("DOMESTIC", "2Y (DGS2)", "ERR", "🔴", f"fetch error: {err}")
    else:
        add("DOMESTIC", "2Y (DGS2)", f"{v:.2f}%", "🟢", "(front-end ref / bear-flattener tell)", d, trend_str(tr, 1, 2))

    # 10Y — >4.50 sustained
    v, d, tr, err = fred_series("DGS10")
    if err:
        add("DOMESTIC", "10Y (DGS10)", "ERR", "🔴", f"fetch error: {err}")
    else:
        m, n = ("🟠", "ABOVE 4.50 pivot") if v > 4.50 else ("🟢", "below 4.50 pivot")
        add("DOMESTIC", "10Y (DGS10)", f"{v:.2f}%", m, n, d, trend_str(tr, 1, 2))

    # 30Y — >5.00 re-establish / <4.90 unwind  [headline]
    v, d, tr, err = fred_series("DGS30")
    if err:
        add("DOMESTIC", "30Y (DGS30)", "ERR", "🔴", f"fetch error: {err} — headline duration row is BLIND; do not read its absence as calm", headline=True)
    else:
        if v > 5.00:    m, n = "🟠", "ABOVE 5.00 — duration regime re-establishing (need ≥5 closes)"
        elif v < 4.90:  m, n = "🟠", "BELOW 4.90 — duration UNWIND test firing"
        else:           m, n = "🟢", f"5.00-pivot oscillation ({v - 4.90:.2f} above the 4.90 unwind)"
        add("DOMESTIC", "30Y (DGS30)", f"{v:.2f}%", m, n, d, trend_str(tr, 1, 2), headline=True)

    # Reserves WRESBAL ($ millions on FRED) — <2.8T floor. Canonical WRESBAL only —
    # NOT the FFIEC bank-reported reserves figure (different measure; see STATUS 6/20).
    v, d, tr, err = fred_series("WRESBAL")
    if err:
        add("DOMESTIC", "Reserves", "ERR", "🔴", f"fetch error: {err}")
    else:
        t = v / 1e6  # $millions -> $T
        if t < 2.8:   m, n = "🟠", "BELOW $2.8T floor — escalate PROME"
        elif t < 2.9: m, n = "🟡", f"cushion ${(t - 2.8) * 1000:.0f}B (<$100B) — Leg-A drain watch (KB-LIQ-067: RRP drained, QT hits reserves directly)"
        else:         m, n = "🟢", f"cushion ${(t - 2.8) * 1000:.0f}B above floor"
        add("DOMESTIC", "Reserves", f"${t:.3f}T", m, n, d + " (as-of Wed)")

    # RRP (billions) — >5 signal; structural zero now
    v, d, tr, err = fred_series("RRPONTSYD")
    if err:
        add("DOMESTIC", "RRP", "ERR", "🔴", f"fetch error: {err}")
    else:
        m, n = ("🟡", "ABOVE $5B — buffer re-activating? (check sustained vs month-end noise)") if v > 5 else ("🟢", "structural zero")
        add("DOMESTIC", "RRP", f"${v:.2f}B", m, n, d)

    # SRF = Treasury leg + MBS leg (billions) — >50 stress
    t_v, t_d, _, t_err = fred_series("RPONTSYD")
    m_v, m_d, _, m_err = fred_series("RPONMBSD")
    if not t_err and not m_err:
        srf = t_v + m_v
        note = "no funding stress (both legs)" if srf <= 50 else "ABOVE $50B — escalate REGINALD/HENRY/PROME"
        if t_d != m_d:
            note += f" [legs differ: T {t_d} / MBS {m_d}]"
        add("DOMESTIC", "SRF usage", f"${srf:.2f}B", "🔴" if srf > 50 else "🟢", note, max(t_d, m_d))
    else:
        leg = f"T ${t_v:.2f}B" if not t_err else f"MBS ${m_v:.2f}B" if not m_err else "neither leg"
        add("DOMESTIC", "SRF usage", "PARTIAL", "🟠", f"leg fetch failed — only {leg} available")


# ---------------------------------------------------------------------------
# Dashboard 3 — FOREIGN OFFICIAL + position/vol prices (yfinance)
# ---------------------------------------------------------------------------

PRICE_SPECS = [
    # ticker, dashboard, label, check(price) -> (marker, note)
    ("APO",  "CREDIT",  "APO",     lambda p: ("🟡", "co-trigger satisfied (>$130) — NOT Trigger C absent HY compression") if p > 130 else ("🟠", "BROKE <$130 — alts-crack DEEPENING (PC→public transmission); recovery co-trigger moot, NOT all-clear")),
    ("BIZD", "CREDIT",  "BIZD",    lambda p: ("🟡", "above $12.50 mark-stress line") if p > 12.50 else ("🟢", "below $12.50")),
    ("^VIX", "CREDIT",  "VIX",     lambda p: ("🟠", ">25") if p > 25 else (("🟡", "elevated >20") if p > 20 else ("🟢", "calm"))),
    ("HYG",  "CREDIT",  "HYG",     lambda p: ("🟢", "(price ref — HY ETF)")),
    ("TLT",  "DOMESTIC", "TLT",    lambda p: ("🟢", "(price ref — 20Y+ UST)")),
    ("JPY=X", "FOREIGN", "USD/JPY", lambda p: ("🔴", "TRIGGERED (>160) — awaiting flow confirm (SAM owns)") if p > 160 else ("🟢", "below 160")),
    ("BZ=F", "FOREIGN", "Brent",    lambda p: ("🟢", "(price ref — BZ=F ≠ ICE settle)")),
]


def build_prices():
    global ERRORS
    tickers = [s[0] for s in PRICE_SPECS]
    try:
        res = price_fetch(tickers)
    except ModuleNotFoundError as e:
        print(f"  ⚠️  yfinance unavailable ({e}) — re-run with .venv/bin/python3 for prices (FRED dashboards still render below).")
        return
    except Exception as e:
        print(f"  ⚠️  price fetch failed: {e} (FRED dashboards still render below).")
        return
    stale = {}
    for ticker, dash, label, check in PRICE_SPECS:
        d = res.get(ticker, {})
        if "error" in d:
            ERRORS += 1
            add(dash, label, "ERR", "🟠", f"fetch error: {str(d['error'])[:40]}")
            continue
        p = d["price"]
        chg = d.get("change_pct")
        m, n = check(p)
        disp = f"{p:,.2f}" if (label in ("USD/JPY",) or p >= 1000) else f"${p:,.2f}"
        if chg is not None:
            disp += f" ({chg:+.2f}%)"
        head = label in ("USD/JPY",)
        # ---- BASIS REPAIR 2026-09-17 #2 (KB-LIQ-130; hazard supplied by VIOLET via
        # WALTER SIG-W-20260917-010). This row stamped the literal string "last close"
        # and DISCARDED FORGE's verified `asof`. yfinance `fast_info` SILENTLY
        # FILL-FORWARDS the prior session on a pre-open / off-RTH pull, with no
        # staleness signal, so "last close" was an ASSERTION about a date this script
        # never checked -- on a pre-open boot it names the wrong session and nothing
        # in the brief disagrees. FORGE fetch.py ALREADY verifies the date against a
        # dated history() bar and returns it; the truth was being computed upstream
        # and thrown away here. Same family as the IORB repair above: a value rendered
        # without its real observation date, failing silent and benign.
        asof = d.get("asof")
        if not asof:
            m, n = "⚪", (f"DATE UNVERIFIED — vendor would not confirm the bar date; the price is kept "
                         f"(FORGE fail-safe) but is NOT graded. {n}")
            asof = "date?"
        else:
            stale.setdefault(asof, []).append(label)
        add(dash, label, disp, m, n, asof, headline=head)
    # A split WITHIN one session calendar is the fill-forward signature. A split BETWEEN
    # calendars is not: FX (JPY=X) and futures (BZ=F) trade ~24h and roll into the next
    # session hours before US cash equities do, so an evening boot ALWAYS shows them a day
    # ahead. This guard's v1 (written minutes earlier) compared the whole batch and fired
    # 🟠 on that benign, structural difference on its FIRST real run — i.e. it would have
    # cried wolf on every post-close boot, which is when I boot. Scope the comparison to
    # the US cash-equity group; report the others' dates without grading them.
    # [[finding_test_the_guard_not_just_the_guarded]]
    EQUITY_CAL = {"APO", "BIZD", "VIX", "HYG", "TLT"}      # one NYSE/Cboe session
    eq = {d_: [l for l in ls if l in EQUITY_CAL] for d_, ls in stale.items()}
    eq = {d_: ls for d_, ls in eq.items() if ls}
    if len(eq) > 1:
        newest = max(eq)
        add("DOMESTIC", "⚠️ PRICE BASIS SPLIT", f"{len(eq)} session dates", "🟠",
            f"US cash-equity tickers did NOT all come from one session — newest {newest} "
            f"({', '.join(eq[newest])}); "
            + "; ".join(f"{d_}: {', '.join(ls)}" for d_, ls in sorted(eq.items()) if d_ != newest)
            + ". On a pre-open/off-RTH pull yfinance fill-forwards the prior session silently "
              "(VIOLET via WALTER SIG-W-20260917-010) — grade off the DATED bar, never an intraday witness")
    elif len(stale) > 1:
        add("DOMESTIC", "price basis (multi-calendar)", f"{len(stale)} session dates", "⚪",
            "; ".join(f"{d_}: {', '.join(ls)}" for d_, ls in sorted(stale.items()))
            + " — EXPECTED: FX/futures roll into the next session ahead of US cash equities. "
              "Not a staleness flag; declare the date when citing across the two", ref=True)


# ---------------------------------------------------------------------------
# GATE-LIQ-076 legs (dealer-positioning nexus) — wired 2026-09-29
# ---------------------------------------------------------------------------
# WHY THIS EXISTS: the conjunction was MET from the 9/25 CFTC print and graded only on 9/29,
# because nothing at boot read this gate — it was touched at `review_by` and nowhere else
# (analysis/2026-09-29_GATE-LIQ-076-conjunction-MET.md §2). Letter:
# workbook/DEALER_POSITIONING_NEXUS_WATCH.md §Fire conditions; GATES L6 condition text.
#   W1  CME SOFR-3M lev-fund NET <= -2,950,000 (GATES spelling; letter "beyond")  OR  one-week cover > 300,000
#   W2  NY Fed PD PDPOSCSBND-G10 < -12,000 $mm OR PDPOSCSBND-G5L10 < -800 $mm on 2 consecutive weekly as-of dates
#       (IG CORPORATE buckets, SBN2024 — keyids named 2026-09-29, DAEDALUS #4)
#   W3  MOVE > 85 while VIX < 20, same session (VIOLET's figure governs; yfinance here is a WITNESS and may grade
#       a session only when both are >1.00 point from their lines — nearer = EDGE, not graded; letter 9/29)
#   CONJUNCTION  any 2 of 3 with a met observation inside a rolling 14-calendar-day window
# The action on MET is a WRITE-UP, never a position. A window read is not a latch: whether a met
# conjunction resets or latches is undefined in the letter (DAEDALUS #4) — this prints the window.
G076_CME = "SOFR-3M - CHICAGO MERCANTILE EXCHANGE"   # FULL name: KB-LIQ-116 venue collision (FMX)
G076_LEVEL, G076_COVER, G076_WINDOW = -2_950_000, 300_000, 14


def grade_076(w1, w3, w2=None):
    """PURE. w1 = [(asof 'YYYY-MM-DD', net int)] oldest-first (CME only); w3 = [(date, move, vix)];
    w2 = [(asof, g10 $mm, g5l10 $mm)] oldest-first, or None when the PD pull failed.
    ⛔ CATO 9/29 (two findings, both fixed here): (1) a weekly change is taken ONLY against the row dated
    EXACTLY 7 days earlier, and every weekly as-of date REQUIRED by the calendar inside the window must be
    present — surviving rows never define the calendar (a missing middle week turned +200k,+200k into one
    "+400k week"); (2) an UNKNOWN leg is carried through: MET needs 2 met legs; if met + unknown >= 2 the
    verdict is INDETERMINATE, never NOT MET.
    Returns dict: state, legs {W1,W2,W3: MET|UNKNOWN|NOT}, w1_hits, w2_hits, w3_hits, w3_edge, unknown, anchor, window_start."""
    from datetime import date as _d, timedelta as _td
    D = _d.fromisoformat
    wk = lambda a, b: (D(b) - D(a)).days == 7
    w1d = {d: n for d, n in w1}
    w1_hits, w1_unk = [], []
    for i, (d, net) in enumerate(w1):
        why = []
        if net <= G076_LEVEL:
            why.append(f"net {net:,} <= {G076_LEVEL:,}")
        if i > 0 and wk(w1[i - 1][0], d):
            if net - w1[i - 1][1] > G076_COVER:
                why.append(f"cover {net - w1[i - 1][1]:+,} > {G076_COVER:,}")
        elif not why:
            w1_unk.append(d)            # cover UNGRADEABLE: the prior week's row is not exactly 7 days back
        if why:
            w1_hits.append((d, "; ".join(why)))
    w3_edge = [d for d, mv, vx in w3 if abs(mv - 85) <= 1.0 or abs(vx - 20) <= 1.0]
    w3_hits = [d for d, mv, vx in w3 if d not in w3_edge and mv > 85 and vx < 20]
    w2_hits, w2_unk = [], []
    for i, (d, g10, g5) in enumerate(w2 or []):
        if g10 < -12_000:
            w2_hits.append((d, f"G10 {g10:,} < -12,000"))
        elif g5 < -800:
            if i > 0 and wk(w2[i - 1][0], d):
                if w2[i - 1][2] < -800:
                    w2_hits.append((d, f"G5L10 {w2[i - 1][2]:,} then {g5:,} < -800 x2"))
            else:
                w2_unk.append(d)        # x2 condition UNGRADEABLE: prior week missing
    dates = [d for d, _ in w1] + [d for d, _, _ in w3] + [d for d, _, _ in (w2 or [])]
    base = {"w1_hits": w1_hits, "w2_hits": w2_hits, "w3_hits": w3_hits, "w3_edge": w3_edge}
    if not dates:
        return {**base, "state": "UNGRADEABLE", "legs": {}, "unknown": {}, "legs_met": 0,
                "anchor": None, "window_start": None}
    anchor = max(dates)
    start = (D(anchor) - _td(days=G076_WINDOW - 1)).isoformat()
    # calendar-REQUIRED observation dates inside the window (published by the anchor date)
    days = [(D(start) + _td(days=k)).isoformat() for k in range(G076_WINDOW)]
    req_w1 = [x for x in days if D(x).weekday() == 1 and (D(x) + _td(days=3)).isoformat() <= anchor]   # Tue, pub Fri
    req_w2 = [x for x in days if D(x).weekday() == 2 and (D(x) + _td(days=8)).isoformat() <= anchor]   # Wed, pub +8d
    try:
        from gate069_legs import is_session
    except Exception:
        is_session = lambda x: D(x).weekday() < 5
    req_w3 = [x for x in days if is_session(x)]
    w3d = {d for d, _, _ in w3}
    unk = {"W1": sorted({x for x in req_w1 if x not in w1d} | {x for x in w1_unk if x >= start}),
           "W2": (["no PD data"] if w2 is None else
                  sorted({x for x in req_w2 if x not in {d for d, _, _ in w2}} | {x for x in w2_unk if x >= start})),
           "W3": sorted({x for x in req_w3 if x not in w3d} | {x for x in w3_edge if x >= start})}
    hit = {"W1": any(d >= start for d, _ in w1_hits), "W2": any(d >= start for d, _ in w2_hits),
           "W3": any(d >= start for d in w3_hits)}
    legs = {k: ("MET" if hit[k] else ("UNKNOWN" if unk[k] else "NOT")) for k in ("W1", "W2", "W3")}
    met = sum(v == "MET" for v in legs.values()); un = sum(v == "UNKNOWN" for v in legs.values())
    if met >= 2:
        state = "MET"
    elif met + un >= 2:
        state = f"INDETERMINATE ({met} met, {un} ungraded: " + ", ".join(k for k, v in legs.items() if v == "UNKNOWN") + ")"
    else:
        state = f"NOT MET ({met} of 3)"
    return {**base, "state": state, "legs": legs, "unknown": unk, "legs_met": met,
            "anchor": anchor, "window_start": start}


def build_gate076():
    """Fetch layer for grade_076. Fails CLOSED: a leg that cannot be read is INSTRUMENT-FAULT, and the
    conjunction is then UNGRADEABLE, never 'NOT MET' (an unmeasured leg is not a quiet leg)."""
    global ERRORS
    faults, w1, w3 = [], [], []
    try:
        import cftc_tff_rates as _c
        rows, src_h, src_w, _seen = _c.load_rows()
        if "FAILED" in src_h or "FAILED" in src_w:
            faults.append(f"CFTC {src_h if 'FAILED' in src_h else src_w}")
        for (k, d), r in rows.items():
            if k == G076_CME:
                w1.append((d, int(r[_c.I_LF_L].strip()) - int(r[_c.I_LF_S].strip())))
        w1 = sorted(set(w1))[-8:]
        if not w1:
            faults.append(f"no '{G076_CME}' rows")
    except Exception as e:
        faults.append(f"CFTC fetch {type(e).__name__}: {str(e)[:40]}")
    try:
        import yfinance as yf, warnings
        warnings.filterwarnings("ignore")
        px = yf.download(["^MOVE", "^VIX"], period="1mo", auto_adjust=False, progress=False)["Close"]
        for ts, row in px.iterrows():
            mv, vx = row.get("^MOVE"), row.get("^VIX")
            if mv == mv and vx == vx:                     # both present (NaN != NaN): same-session pairs only
                w3.append((ts.strftime("%Y-%m-%d"), float(mv), float(vx)))
        if not w3:
            faults.append("no same-session MOVE/VIX pairs")
    except Exception as e:
        faults.append(f"MOVE/VIX fetch {type(e).__name__}: {str(e)[:40]}")
    w2, w2_err = None, None
    try:
        import json as _j, urllib.request as _u
        got = {}
        for key in ("PDPOSCSBND-G10", "PDPOSCSBND-G5L10"):
            req = _u.Request(f"https://markets.newyorkfed.org/api/pd/get/{key}.json",
                             headers={"User-Agent": "Mozilla/5.0 (LIQUID-Research)"})
            with _u.urlopen(req, timeout=60) as r:
                ts = _j.load(r)["pd"]["timeseries"]
            got[key] = {t["asofdate"]: int(float(t["value"])) for t in ts
                        if t.get("keyid") == key and t.get("value") not in ("", "*", None)}
        common = sorted(set(got["PDPOSCSBND-G10"]) & set(got["PDPOSCSBND-G5L10"]))[-8:]
        w2 = [(d, got["PDPOSCSBND-G10"][d], got["PDPOSCSBND-G5L10"][d]) for d in common] or None
        if w2 is None:
            w2_err = "no common PD as-of dates"
    except Exception as e:
        w2_err = f"PD fetch {type(e).__name__}: {str(e)[:40]}"

    g = grade_076(w1, w3, w2)
    if w1:
        d, net = w1[-1]
        ww = f", w/w {net - w1[-2][1]:+,}" if len(w1) > 1 else ""
        hit = [h for h in g["w1_hits"] if h[0] == d]
        add("DOMESTIC", "076 W1 SOFR-3M LevF", f"{net:,}{ww}", "🔴" if hit else "🟢",
            (f"MET — {hit[0][1]}" if hit else f"not met (level {G076_LEVEL:,} · cover >{G076_COVER:,})")
            + " · CME pinned; as-of TUESDAY, publishes Fri ~15:30 ET", d)
    if w3:
        d, mv, vx = w3[-1]
        edge = d in g["w3_edge"]
        add("DOMESTIC", "076 W3 MOVE/VIX", f"{mv:.2f} / {vx:.2f}",
            "⚪" if edge else ("🔴" if d in g["w3_hits"] else "🟢"),
            ("EDGE — within 1.00pt of a line: VIOLET's figure required, NOT graded off the witness" if edge
             else ("MET" if d in g["w3_hits"] else "not met")) + " (MOVE>85 while VIX<20) · yfinance WITNESS — VIOLET's figure governs", d)
    if w2:
        d, g10, g5 = w2[-1]
        hit = [h for h in g["w2_hits"] if h[0] == d]
        add("DOMESTIC", "076 W2 NY Fed PD", f"G10 {g10:,} · G5L10 {g5:,} $mm", "🔴" if hit else "🟢",
            (f"MET — {hit[0][1]}" if hit else "not met (G10 < -12,000 · G5L10 < -800 x2)")
            + " · IG CORPORATE buckets PDPOSCSBND-G10/-G5L10 (SBN2024); as-of WEDNESDAY, ~8d lag", d)
    else:
        add("DOMESTIC", "076 W2 NY Fed PD", "UNMEASURED", "⚪",
            f"{w2_err} — W2 not read this boot; never read as 'not met'", "n/a (fetch)")
    if faults:
        ERRORS += 1
        add("DOMESTIC", "GATE-LIQ-076", "INSTRUMENT-FAULT", "🔴",
            "UNGRADEABLE — " + "; ".join(faults) + ". An unread leg is UNMEASURED, never NOT MET", headline=True)
        return
    w1s = ", ".join(d for d, _ in g["w1_hits"] if d >= g["window_start"]) or "—"
    w3s = ", ".join(d for d in g["w3_hits"] if d >= g["window_start"]) or "—"
    w2s = ("UNMEASURED" if w2 is None else
           ("met " + ", ".join(d for d, _ in g["w2_hits"] if d >= g["window_start"]) if any(d >= g["window_start"] for d, _ in g["w2_hits"]) else "not met"))
    edg = [d for d in g["w3_edge"] if d >= g["window_start"]]
    mk = "🔴" if g["state"] == "MET" else ("⚪" if g["state"].startswith("INDETERMINATE") else ("🟠" if g["legs_met"] == 1 else "🟢"))
    unk_s = "; ".join(f"{k} ungraded {', '.join(v)}" for k, v in g["unknown"].items() if v and g["legs"].get(k) != "MET")
    add("DOMESTIC", "GATE-LIQ-076", g["state"], mk,
        f"window {g['window_start']}→{g['anchor']} · W1 met {w1s} · W3 met {w3s} · W2 {w2s}"
        + (f" · W3 EDGE (ungraded) {', '.join(edg)}" if edg else "") + (f" · {unk_s}" if unk_s else "") + ". "
        "MET ⇒ WRITE-UP (PROME + NEXUS/HENRY via WALTER), NEVER a position. Window read, not a latch: a 2nd write-up needs "
        "10 business days with no leg met (letter 9/29)",
        g["anchor"], headline=g["legs_met"] >= 1)


# ---------------------------------------------------------------------------
# Forward state — catalyst countdown + predictions due-scan
# ---------------------------------------------------------------------------

def _trading_days(start, end):
    """Weekdays strictly after `start` through `end` inclusive (US holidays ignored)."""
    if end <= start:
        return 0
    n, cur = 0, start + timedelta(days=1)
    while cur <= end:
        if cur.weekday() < 5:
            n += 1
        cur += timedelta(days=1)
    return n


def catalyst_countdown(horizon=60):
    """Print dated catalysts within `horizon` days. Returns count flagged imminent (<=5 trd)."""
    path = LIQUID_DIR / "workbook" / "CATALYSTS.tsv"
    if not path.exists():
        print("    (no workbook/CATALYSTS.tsv)")
        return 0
    rows = path.read_text().splitlines()
    if len(rows) < 2:
        print("    (CATALYSTS.tsv empty)")
        return 0
    hdr = rows[0].split("\t")
    today = datetime.now().date()
    cutoff = today + timedelta(days=horizon)
    upcoming, unparsed = [], 0
    for ln in rows[1:]:
        parts = ln.split("\t")
        if len(parts) != len(hdr):
            unparsed += 1   # wrong field count -> would render misaligned; flag, don't skip silently
            continue
        c = dict(zip(hdr, parts))
        try:
            ed = datetime.strptime(c.get("date", ""), "%Y-%m-%d").date()
        except ValueError:
            unparsed += 1   # fail loud — a malformed date silently drops from the countdown
            continue
        if today <= ed <= cutoff:
            upcoming.append((ed, c))
    if unparsed:
        print(f"    ⚠️  {unparsed} malformed row(s) (bad date or field count) — fix CATALYSTS.tsv (silently skipped otherwise)")
    if not upcoming:
        print(f"    no dated catalysts within {horizon}d")
        return 0
    upcoming.sort(key=lambda x: x[0])
    imminent = 0
    for ed, c in upcoming:
        trd = _trading_days(today, ed)
        cal = (ed - today).days
        mk = "~" if c.get("date_class", "").strip() == "modeled" else " "
        pri = c.get("priority", "").strip() or "  "
        flag = "  ⏰ IMMINENT" if trd <= 5 else ""
        if trd <= 5:
            imminent += 1
        print(f"    {pri} {mk}{c['date']} {ed.strftime('%a')}  {cal:>3}d cal /{trd:>3}d trd  {c.get('event', '')[:50]}{flag}")
    return imminent


_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
# full month names also accepted; the parser requires the WHOLE word be a month, so 'Junk' != 'Jun'
_MONTH_WORDS = dict(_MONTHS)
_MONTH_WORDS.update({m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], 1)})


def _parse_timeframe(tf):
    """Best-effort resolve-date from a free-text Timeframe. Returns (date|None, parsed_bool)."""
    tf = (tf or "").strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", tf)             # explicit ISO
    if m:
        try:
            return date(*map(int, m.groups())), True
        except ValueError:
            pass
    m = re.search(r"H([12])\s*(\d{4})", tf)                   # H1/H2 YYYY
    if m:
        y = int(m.group(2))
        return (date(y, 6, 30) if m.group(1) == "1" else date(y, 12, 31)), True
    m = re.search(r"Q([1-4])\s*(\d{4})", tf)                  # Q1-Q4 YYYY
    if m:
        y = int(m.group(2))
        return date(y, *{1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}[int(m.group(1))]), True
    m = re.search(r"\b([A-Za-z]{3,9})\b\.?\s*(?:(\d{1,2})\s*-\s*(\d{1,2}))?\s*,?\s*(\d{4})", tf)  # Month [DD-DD] YYYY
    if m and m.group(1).lower() in _MONTH_WORDS:   # whole word must BE a month ('Junk' rejected)
        mo, y = _MONTH_WORDS[m.group(1).lower()], int(m.group(4))
        last = calendar.monthrange(y, mo)[1]
        day = min(int(m.group(3)), last) if m.group(3) else last
        return date(y, mo, day), True
    return None, False


def predictions_scan():
    """Flag OPEN predictions whose timeframe is due/overdue. Returns overdue count."""
    path = LIQUID_DIR / "workbook" / "PREDICTIONS.tsv"
    if not path.exists():
        print("    (no workbook/PREDICTIONS.tsv)")
        return 0
    rows = path.read_text().splitlines()
    if len(rows) < 2:
        print("    (PREDICTIONS.tsv empty)")
        return 0
    hdr = rows[0].split("\t")
    today = datetime.now().date()
    open_rows = [d for d in (dict(zip(hdr, ln.split("\t"))) for ln in rows[1:])
                 if d.get("Status", "").strip().upper() == "OPEN"]
    if not open_rows:
        print("    ✓ no OPEN predictions")
        return 0
    overdue = 0
    for p in open_rows:
        pid, tf, pred = p.get("Pred_ID", "?"), p.get("Timeframe", ""), p.get("Prediction", "")[:52]
        due, parsed = _parse_timeframe(tf)
        if not parsed:
            print(f"    ⚠️  {pid}: OPEN — timeframe '{tf}' unparsed; check manually — {pred}")
            continue
        d = (due - today).days
        if d < 0:
            overdue += 1
            print(f"    🔴 {pid}: OVERDUE {-d}d (resolve now — don't let it rot like LIQ-02) — {pred}")
        elif d <= 7:
            print(f"    🟠 {pid}: DUE in {d}d ({due}) — {pred}")
        else:
            print(f"    🟡 {pid}: due {due} ({d}d) — {pred}")
    return overdue


def watcher_echo():
    """Echo the unattended hy_oas_watch.py last state — surfaces a between-session HY OAS
    cross to a human at next boot (closes the reaches-a-human loop; P1b)."""
    import json
    sp = LIQUID_DIR / "alerts" / "HY_OAS_STATE"
    if not sp.exists():
        print("    (watcher has not run yet — no HY_OAS_STATE)")
        return
    try:
        st = json.loads(sp.read_text())
    except Exception as e:
        print(f"    ⚠️  HY_OAS_STATE unreadable: {e}")
        return
    flag = "  ⚠️ ELEVATED — check alerts/HY_OAS_ALERTS.log" if st.get("sev", 0) >= 1 else ""
    print(f"    {st.get('marker','?')} HY OAS last {st.get('zone','?')} {st.get('bps','?')}bps "
          f"(obs {st.get('obs_date','?')}, checked {st.get('checked','?')}){flag}")


def selftest():
    """Validate the data files + fetch import (fail-loud parser test). Returns 0 pass / 1 fail."""
    ok = True
    print("  ✓ FORGE fetch.py import OK")   # module-load would have exited 2 otherwise

    cat = LIQUID_DIR / "workbook" / "CATALYSTS.tsv"
    if not cat.exists():
        print("  ⚠️  CATALYSTS.tsv not found")
    else:
        rows = cat.read_text().splitlines()
        exp = ["date", "event", "what_to_check", "threshold_signal",
               "priority", "who_cares", "notes", "date_class"]
        if rows[0].split("\t") != exp:
            print(f"  ✗ CATALYSTS.tsv header mismatch: {rows[0].split(chr(9))}")
            ok = False
        bad = 0
        for i, ln in enumerate(rows[1:], 2):
            p = ln.split("\t")
            if len(p) != 8:
                print(f"  ✗ CATALYSTS.tsv line {i}: {len(p)} fields (expect 8)")
                ok = False; bad += 1; continue
            try:
                datetime.strptime(p[0], "%Y-%m-%d")
            except ValueError:
                print(f"  ✗ CATALYSTS.tsv line {i}: bad date {p[0]!r}")
                ok = False; bad += 1
        if not bad and ok:
            print(f"  ✓ CATALYSTS.tsv OK ({len(rows) - 1} rows, 8 cols, dates parse)")

    pred = LIQUID_DIR / "workbook" / "PREDICTIONS.tsv"
    if not pred.exists():
        print("  ⚠️  PREDICTIONS.tsv not found")
    else:
        rows = pred.read_text().splitlines()
        hdr = rows[0].split("\t")
        unparsed = [d.get("Pred_ID", "?") for d in (dict(zip(hdr, ln.split("\t"))) for ln in rows[1:])
                    if d.get("Status", "").strip().upper() == "OPEN" and not _parse_timeframe(d.get("Timeframe", ""))[1]]
        if unparsed:
            print(f"  ⚠️  PREDICTIONS.tsv OPEN rows with unparseable Timeframe: {unparsed} (scan flags manual-check)")
        else:
            print("  ✓ PREDICTIONS.tsv OK (all OPEN timeframes parse)")

    kb = LIQUID_DIR / "workbook" / "KB.tsv"
    if not kb.exists():
        print("  ⚠️  KB.tsv not found")
    else:
        rows = [ln for ln in kb.read_text().split("\n") if ln != ""]
        exp = ["ID", "Date", "Group", "Entity", "Fact", "Source", "Conf",
               "Epistemic", "Status", "Stale_By", "DerivedFrom", "Vectors", "Notes"]
        if rows[0].split("\t") != exp:
            print(f"  ✗ KB.tsv header mismatch ({len(rows[0].split(chr(9)))} cols, expect 13): {rows[0].split(chr(9))}")
            ok = False
        bad = 0
        for i, ln in enumerate(rows[1:], 2):
            p = ln.split("\t")
            if len(p) != 13:
                print(f"  ✗ KB.tsv line {i} ({p[0] if p else '?'}): {len(p)} fields (expect 13 — column drift)")
                ok = False; bad += 1; continue
            sid = p[0]
            if not (sid.startswith("KB-LIQ-") and len(sid) == 10 and sid[7:].isdigit()):
                print(f"  ✗ KB.tsv line {i}: malformed ID {sid!r}")
                ok = False; bad += 1
        if not bad and ok:
            print(f"  ✓ KB.tsv OK ({len(rows) - 1} rows, 13 cols, IDs well-formed)")

    # GATE-LIQ-076 grader (pure; 2026-09-29). Fixture = the real CME series around the 9/25 MET.
    W1 = [("2026-09-08", -2_803_445), ("2026-09-15", -2_774_148), ("2026-09-22", -2_444_986)]
    W3 = [("2026-09-22", 78.56, 14.21), ("2026-09-23", 95.45, 15.18), ("2026-09-24", 104.58, 15.67),
          ("2026-09-25", 96.00, 14.87), ("2026-09-28", 101.82, 16.07)]
    def g076(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
        print(f"  {'✓' if got == want else '✗'} 076 {label}: got {got!r}, want {want!r}")
    g076("real 9/22 cover + 9/23-9/28 rates vol → MET", grade_076(W1, W3)["state"], "MET")
    SESS = ["2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-21", "2026-09-22", "2026-09-23",
            "2026-09-24", "2026-09-25", "2026-09-28"]
    W3Q = [(d, 70.0, 15.0) for d in SESS]                      # a full, quiet W3 window
    g076("W1 met + W2 NO DATA + W3 quiet → INDETERMINATE, never 'NOT MET'",
         grade_076(W1, W3Q)["state"].startswith("INDETERMINATE"), True)
    g076("cover of exactly +300,000 is NOT > 300,000",
         grade_076([("2026-09-15", -2_800_000), ("2026-09-22", -2_500_000)], [])["w1_hits"], [])
    g076("cover +300,001 is met",
         len(grade_076([("2026-09-15", -2_800_000), ("2026-09-22", -2_499_999)], [])["w1_hits"]), 1)
    g076("level -2,950,000 is met (<=)", len(grade_076([("2026-09-22", -2_950_000)], [])["w1_hits"]), 1)
    g076("level -2,949,999 is not", grade_076([("2026-09-22", -2_949_999)], [])["w1_hits"], [])
    g076("MOVE exactly 85.0 is not >85", grade_076([], [("2026-09-23", 85.0, 15.0)])["w3_hits"], [])
    g076("VIX exactly 20.0 is not <20", grade_076([], [("2026-09-23", 90.0, 20.0)])["w3_hits"], [])
    g076("W1 15 days before the latest W3 hit is OUTSIDE the 14-day window",
         grade_076([("2026-09-01", -2_800_000), ("2026-09-08", -2_400_000)],
                   [("2026-09-23", 95.0, 15.0)])["legs_met"], 1)
    g076("W1 13 days before is INSIDE", grade_076([("2026-09-03", -2_800_000), ("2026-09-10", -2_400_000)],
                                                [("2026-09-23", 95.0, 15.0)])["legs_met"], 2)
    g076("no data → UNGRADEABLE", grade_076([], [])["state"], "UNGRADEABLE")
    g076("first W1 row cannot be a cover (no prior week)", grade_076([("2026-09-22", -1_000_000)], [])["w1_hits"], [])
    W2 = [("2026-09-09", -8_648, 703), ("2026-09-16", -9_286, 564)]
    g076("real W2 [9/16] → not met; conjunction still MET on W1+W3", (grade_076(W1, W3, W2)["w2_hits"], grade_076(W1, W3, W2)["state"]), ([], "MET"))
    g076("W2 G10 exactly -12,000 is NOT < -12,000", grade_076([], [], [("2026-09-16", -12_000, 0)])["w2_hits"], [])
    g076("W2 G5L10 -801 ONE week only → not met", grade_076([], [], [("2026-09-09", 0, 500), ("2026-09-16", 0, -801)])["w2_hits"], [])
    g076("W2 G5L10 -801 two consecutive → met", len(grade_076([], [], [("2026-09-09", 0, -801), ("2026-09-16", 0, -801)])["w2_hits"]), 1)
    g076("W1 met, W2 measured not met, W3 full & quiet → 'NOT MET (1 of 3)'",
         grade_076(W1, W3Q, W2)["state"], "NOT MET (1 of 3)")
    # CATO 9/29 finding 1: a missing MIDDLE week must not turn two +200k weeks into one "+400k week"
    W1g = [("2026-09-08", -2_800_000), ("2026-09-22", -2_400_000)]          # 9/15 row missing
    r = grade_076(W1g, W3Q, W2)
    g076("CATO: missing middle W1 week → no cover hit; W1 UNKNOWN", (r["w1_hits"], r["legs"]["W1"]), ([], "UNKNOWN"))
    W2g = [("2026-09-02", 0, -900), ("2026-09-16", 0, -900)]                 # 9/09 missing
    r = grade_076(W1, W3Q, W2g)
    g076("CATO: G5L10 x2 across a missing week → no hit; W2 UNKNOWN", (r["w2_hits"], r["legs"]["W2"]), ([], "UNKNOWN"))
    # CATO 9/29 finding 2: W1 met + W2 quiet + W3 EDGE (ungraded) → INDETERMINATE, not NOT MET
    W3e = [(d, 70.0, 15.0) for d in SESS[:-1]] + [("2026-09-28", 85.5, 15.0)]
    g076("CATO: one met, one quiet, W3 at the edge → INDETERMINATE", grade_076(W1, W3e, W2)["state"].startswith("INDETERMINATE"), True)
    g076("a missing W3 session in the window → W3 UNKNOWN", grade_076(W1, W3Q[:3] + W3Q[4:], W2)["legs"]["W3"], "UNKNOWN")
    g076("a required W1 Tuesday absent (9/22 not in rows) → W1 UNKNOWN",
         grade_076(W1[:2], W3Q, W2)["legs"]["W1"], "UNKNOWN")
    g076("W3 witness at MOVE 85.9 is EDGE, not a hit", (grade_076([], [("2026-09-23", 85.9, 15.0)])["w3_hits"],
         grade_076([], [("2026-09-23", 85.9, 15.0)])["w3_edge"]), ([], ["2026-09-23"]))

    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

SEV = {"🔴": 3, "🟠": 2, "🟡": 1, "🟢": 0}
DASH_ORDER = ["CREDIT", "DOMESTIC", "FOREIGN"]
DASH_TITLE = {"CREDIT": "Dashboard 1 — Credit Spreads",
              "DOMESTIC": "Dashboard 2 — Domestic Plumbing",
              "FOREIGN": "Dashboard 3 — Foreign Official"}


def render(verbose):
    for dash in DASH_ORDER:
        rows = [r for r in RESULTS if r["dashboard"] == dash]
        if not rows:
            continue
        # collapsed: show alerts (non-🟢) + headline rows; verbose: show all
        # ⚪ = reference-only rows (a number rendered so it is not MISSING, but which grades
        # nothing). Suppressed with 🟢 in the default view 2026-08-28: the SOFR99−SOFR
        # dispersion row was showing while its 🟢 sibling SOFR99−IORB — the actual
        # GATE-LIQ-079 ARM leg — was hidden, i.e. the default view displayed the
        # NON-gate number and concealed the gate one. That is KB-LIQ-109/113 inverted.
        # 2026-09-22 (CATO 9/17 §2): hide only 🟢 and REFERENCE-ONLY ⚪ (ref=True). An ungradeable
        # ⚪ is a fail-closed read and must never be concealed behind "all clear".
        shown = [r for r in rows if (verbose or r["headline"]
                                     or not (r["marker"] == "🟢" or (r["marker"] == "⚪" and r.get("ref"))))]
        print(f"\n  {DASH_TITLE[dash]}")
        if not shown:
            print("    🟢 all clear")
            continue
        for r in shown:
            line = f"    {r['marker']} {r['label']:<12} {r['display']:<20}"
            if r["note"]:
                line += f" {r['note']}"
            # every rendered value carries its observation date, in BOTH modes (CATO 9/17 §2:
            # price rows have no trend, so the old verbose-trend-only print never dated them)
            line += f"  (obs {r['asof'] or 'date?'})"
            print(line)
            if verbose and r["trend"]:
                print(f"       trend: {r['trend']}   [{r['asof']}]")


def summary(elapsed, imminent=0, overdue=0):
    reds = [r for r in RESULTS if r["marker"] == "🔴"]
    oranges = [r for r in RESULTS if r["marker"] == "🟠"]
    yellows = [r for r in RESULTS if r["marker"] == "🟡"]
    hy = next((r for r in RESULTS if r["label"] == "HY OAS"), None)

    print(f"\n  {'=' * 66}")
    print(f"  BOOT SUMMARY   🔴 {len(reds)}   🟠 {len(oranges)}   🟡 {len(yellows)}   "
          f"⏰ {imminent} imminent   📋 {overdue} overdue-pred   "
          f"({len(RESULTS)} series, {ERRORS} fetch errors, {elapsed:.1f}s)")
    if hy and hy["display"] != "ERR":
        print(f"  Headline: HY OAS {hy['display']} — {hy['note']}")
    for r in reds:
        print(f"    🔴 {r['label']}: {r['note']}")
    print(f"\n  ⚠️  Basis: FRED prints lag T+1 (latest may be 1-2 sessions back, more on a weekend);")
    print(f"      yfinance = last close; Brent BZ=F ≠ ICE settle; USD/JPY ≠ 5pm-ET NY close.")
    print(f"      Declare the basis when citing any figure downstream.")


def main():
    if "--selftest" in sys.argv:
        print("\n  LIQUID boot.py --selftest")
        return selftest()
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    t0 = datetime.now()

    print(f"\n{'#' * 68}")
    print(f"#{'LIQUID BOOT — 3-dashboard live sweep':^66}#")
    print(f"#{t0.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print(f"{'#' * 68}")

    build_credit()
    build_domestic()
    if quick:
        print("\n  ⏩ --quick: skipping yfinance prices (APO/BIZD/VIX/HYG/TLT/USDJPY/Brent) and GATE-LIQ-076 legs (UNGRADED this run)")
    else:
        build_prices()
        build_gate076()     # CFTC + MOVE/VIX network pulls — skipped under --quick with the prices

    render(verbose)

    print("\n  Catalyst Countdown (workbook/CATALYSTS.tsv, 60d horizon)")
    imminent = catalyst_countdown()
    print("\n  Predictions Due-Scan (workbook/PREDICTIONS.tsv)")
    overdue = predictions_scan()

    print("\n  Unattended Watcher (AGENTS/LIQUID/alerts/HY_OAS_STATE)")
    watcher_echo()

    elapsed = (datetime.now() - t0).total_seconds()
    summary(elapsed, imminent, overdue)
    print()
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
