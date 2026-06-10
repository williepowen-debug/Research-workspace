#!/usr/bin/env python3
"""
SAM Japan Trade Balance Parser — Phase 1 stability lag-test feed

Sources (MOF Customs / Trade Statistics of Japan — primary):
  Headline series : https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv
                    (monthly world exp/imp, ¥ thousands, CP932, 1979→present;
                     raw/original series — press headlines cite this basis)
  Press-release XML: https://www.customs.go.jp/toukei/shinbun/trade-st/{YYYY}/{YYYY}{MM}{S}.xml
                    stage digit S: 4=速報(provisional) 5=確速 6=確報 7=確々報
                    (all stages stay online; provisional lands 08:50 JST per
                     MOF release calendar /toukei/calendar/calend_e.htm —
                     pin dates from the calendar, do not pattern-match)

Extracts per month:
  - Headline: exports / imports / balance (¥M exact from XML 総額 row) + YoY
  - World imports decomposition: crude & partly-refined oil (千KL volume,
    value, MOF's own YoY), petroleum products, LNG
  - Middle East: total imports + YoY; ME crude volume + YoY (the
    supply-destruction series — Apr 2026 printed −67.2%)
  - Implied crude unit cost: ¥/KL → $/bbl via 6.29 bbl/KL + monthly-avg USDJPY,
    sanity-banded vs Brent averaged over t−1..t−2 months (cargo pricing lag),
    ±20% gross-error band — NOT a calibration check

Routing (labels verbatim from docket/CALENDAR.md Jun-17 row — this script
MEASURES the pre-registered branches; SAM adjudicates the verdict):
  (a) deficit re-opens with Brent <$100  → 🟠 Phase 1 mechanism back online
  (b) surplus persists, ME volumes recovering → 🟢 inversion is structural
  (c) surplus persists, ME volumes still depressed → 🟡 inconclusive; defer to June TB (Jul 22)
  ME-volume "recovering" proxy: ME crude vol YoY ≥ −20% (stated assumption,
  printed with the suggestion; not part of the pre-registered text).

Appends to workbook/TRADE_BALANCE.tsv keyed (month, stage) — provisional and
confirmed are SEPARATE rows; when a later stage lands, the verdict re-prints
with a "revised from" comparison.

Fixtures (--selftest; re-anchored to MOF's own figures 2026-06-10):
  Apr 2026 stage-4: balance +301,905 ¥M EXACT (press "¥+301.9B" ✓);
                    crude vol YoY −63.7 (press "−64%" ✓); ME crude vol YoY −67.2 ✓
  Jan 2026 cross-source: XML best-stage totals vs d41ma.csv within ±1%
                    (normal-month layout + parser-vs-CSV independence check)

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/trade_balance_japan.py              # check for new release
  .venv/bin/python3 AGENTS/SAM/scripts/trade_balance_japan.py --boot      # quiet fast-exit mode
  .venv/bin/python3 AGENTS/SAM/scripts/trade_balance_japan.py --month 2026-04 [--stage 4]
  .venv/bin/python3 AGENTS/SAM/scripts/trade_balance_japan.py --backfill 14
  .venv/bin/python3 AGENTS/SAM/scripts/trade_balance_japan.py --selftest
  .venv/bin/python3 AGENTS/SAM/scripts/trade_balance_japan.py --consensus -350
                    (consensus balance, ¥B, hand-fed from wire on print day)
"""

import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
TSV = WORKBOOK / "TRADE_BALANCE.tsv"

CSV_URL = "https://www.customs.go.jp/toukei/suii/html/data/d41ma.csv"
XML_URL = "https://www.customs.go.jp/toukei/shinbun/trade-st/{yyyy}/{yyyy}{mm}{stage}.xml"
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

STAGE_NAMES = {4: "sokuho", 5: "kakusoku", 6: "kakuho", 7: "kakukakuho"}
BBL_PER_KL = 6.29

TSV_HEADER = (
    "Month\tStage\tExp_B\tExp_YoY\tImp_B\tImp_YoY\tBal_B\t"
    "Crude_Vol_kKL\tCrude_Vol_YoY\tCrude_Val_B\tCrude_Val_YoY\tCrude_USD_bbl\t"
    "LNG_Vol_kt\tLNG_Vol_YoY\tLNG_Val_B\tLNG_Val_YoY\t"
    "ME_Imp_B\tME_Imp_YoY\tME_Crude_Vol_kKL\tME_Crude_Vol_YoY\t"
    "Brent_avg_lag\tUSDJPY_avg\tRouting\tPulled\n"
)


def jst_today():
    return (datetime.now(timezone.utc) + timedelta(hours=9)).date()


def _fetch(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.HTTPError:
        return None
    except Exception:
        return None


def _num(s):
    if s is None:
        return None
    s = s.replace(",", "").replace("%", "").strip()
    if s in ("", "-", "−", "△"):
        return None
    s = s.replace("△", "-")  # MOF negative marker
    try:
        return float(s)
    except ValueError:
        return None


# ---------------------------------------------------------------- headline CSV

def fetch_csv_headline():
    """d41ma.csv → {('YYYY-MM'): (exp_M, imp_M)} in ¥ millions. Raw series."""
    raw = _fetch(CSV_URL)
    if raw is None:
        return None
    text = raw.decode("cp932", errors="replace")
    out = {}
    for line in text.splitlines():
        parts = line.split(",")
        if re.match(r"^\d{4}/\d{2}$", parts[0].strip()) and len(parts) >= 3:
            exp = _num(parts[1])
            imp = _num(parts[2])
            if exp and imp and exp > 0:
                ym = parts[0].strip().replace("/", "-")
                out[ym] = (exp / 1000.0, imp / 1000.0)  # ¥ thousand → ¥ million
    return out


# ---------------------------------------------------------------- XML parsing

def fetch_xml(ym, stage):
    yyyy, mm = ym.split("-")
    raw = _fetch(XML_URL.format(yyyy=yyyy, mm=mm, stage=stage))
    if raw is None:
        return None
    return raw.decode("utf-8", errors="replace")


def best_stage(ym, max_stage=7):
    """Probe descending stage digits; return (stage, xml_text) of most final."""
    for stage in range(max_stage, 3, -1):
        text = fetch_xml(ym, stage)
        if text:
            return stage, text
    return None, None


def _tag(block, name):
    m = re.search(rf"<{name}>([^<]*)</{name}>", block)
    return m.group(1).strip() if m else None


def _commodity_row(section, label):
    """Find a shuyochiikikunihininfo block whose shuyoshohin contains label."""
    for m in re.finditer(r"<shuyochiikikunihininfo>(.*?)</shuyochiikikunihininfo>",
                         section, re.DOTALL):
        block = m.group(1)
        name = _tag(block, "shuyoshohin") or ""
        if label in name:
            return {
                "vol": _num(_tag(block, "suryo")),
                "vol_yoy": _num(_tag(block, "suryonobiritsu")),
                "val_M": _num(_tag(block, "kagaku")),       # ¥ millions
                "val_yoy": _num(_tag(block, "kagakunobiritsu")),
            }
    return None


def parse_xml(text):
    """Parse one press-release XML → dict. Sections are <title>-delimited."""
    out = {}

    # publication + target month
    out["kohyoymd"] = _tag(text, "kohyoymd")
    taishoym = _tag(text, "taishoym") or ""
    m = re.search(r"令和\s*(\d+)年\s*(\d+)月", taishoym)
    if m:
        out["month"] = f"{2018 + int(m.group(1))}-{int(m.group(2)):02d}"

    # region totals (総額 / 中東) — values are ¥ millions
    for m2 in re.finditer(r"<chiikikunisogakuinfo>(.*?)</chiikikunisogakuinfo>",
                          text, re.DOTALL):
        block = m2.group(1)
        region = _tag(block, "chiikikuni") or ""
        row = {
            "exp_M": _num(_tag(block, "exportkagakue")),
            "exp_yoy": _num(_tag(block, "exportnobiritsu")),
            "imp_M": _num(_tag(block, "importkagakue")),
            "imp_yoy": _num(_tag(block, "importnobiritsu")),
            "bal_M": _num(_tag(block, "sashihikikagakue")),
        }
        if region == "総額":
            out["total"] = row
        elif region == "中東":
            out["me_total"] = row

    # title-delimited sections — normalize full/half-width parens (body uses
    # half-width "(世界)", TOC pagemei uses full-width "（世界）")
    def _norm(s):
        return s.replace("（", "(").replace("）", ")")

    titles = [(m3.start(), _norm(m3.group(1)))
              for m3 in re.finditer(r"<title>([^<]*)</title>", text)]

    def section(title_substr):
        needle = _norm(title_substr)
        for i, (pos, title) in enumerate(titles):
            if needle in title:
                end = titles[i + 1][0] if i + 1 < len(titles) else len(text)
                return text[pos:end]
        return ""

    world_imp = section("主要商品別輸入(世界)")
    me_imp = section("主要地域(国)別商品別輸入(中東)")

    if world_imp:
        out["crude"] = _commodity_row(world_imp, "原油及び粗油")
        out["petprod"] = _commodity_row(world_imp, "石油製品")
        out["lng"] = _commodity_row(world_imp, "液化天然ガス")
    if me_imp:
        out["me_crude"] = _commodity_row(me_imp, "原油及び粗油")

    return out if out.get("total") else None


# ---------------------------------------------------------------- market data

def market_context(ym):
    """Monthly-avg USDJPY for target month; Brent avg over t−1..t−2 (cargo lag);
    live Brent spot. Returns (usdjpy_avg, brent_lag_avg, brent_spot) — any may
    be None; degrade gracefully (decomposition does not depend on this)."""
    try:
        import yfinance as yf
    except ImportError:
        return None, None, None
    try:
        y, mth = (int(p) for p in ym.split("-"))
        t0 = datetime(y, mth, 1)
        nxt = datetime(y + (mth == 12), (mth % 12) + 1, 1)
        lag_start = datetime(y if mth > 2 else y - 1, ((mth - 3) % 12) + 1, 1)

        fx = yf.Ticker("USDJPY=X").history(start=t0, end=nxt)
        usdjpy_avg = float(fx["Close"].mean()) if len(fx) else None

        bz = yf.Ticker("BZ=F").history(start=lag_start, end=t0)
        brent_lag = float(bz["Close"].mean()) if len(bz) else None

        spot_hist = yf.Ticker("BZ=F").history(period="5d")
        brent_spot = float(spot_hist["Close"].iloc[-1]) if len(spot_hist) else None
        return usdjpy_avg, brent_lag, brent_spot
    except Exception:
        return None, None, None


def unit_cost_usd_bbl(crude, usdjpy_avg):
    """Implied crude import cost: ¥M / 千KL → $/bbl (6.29 bbl per KL)."""
    if not crude or not crude.get("val_M") or not crude.get("vol") or not usdjpy_avg:
        return None
    yen_per_kl = crude["val_M"] * 1e6 / (crude["vol"] * 1000.0)
    return yen_per_kl / usdjpy_avg / BBL_PER_KL


# ---------------------------------------------------------------- routing

def routing_suggestion(bal_M, me_crude, brent_spot):
    """Suggested branch per pre-registered CALENDAR routing. SAM adjudicates.
    Labels verbatim from docket/CALENDAR.md; the −20% ME-vol normalization
    proxy is a stated assumption, NOT part of the pre-registered text."""
    if bal_M is None:
        return "—", ""
    me_yoy = me_crude.get("vol_yoy") if me_crude else None
    if bal_M < 0:
        if brent_spot is not None and brent_spot < 100:
            return ("(a)", "🟠 Phase 1 mechanism back online (inversion was transient) "
                           f"— deficit re-opened with Brent <$100 (${brent_spot:.0f})")
        return ("(a?)", "🟠 deficit re-opened; Brent leg "
                        + (f"${brent_spot:.0f} ≥ $100 — check framing" if brent_spot else "UNAVAILABLE — verify Brent <$100 manually"))
    # surplus persists
    if me_yoy is not None and me_yoy >= -20:
        return ("(b)", f"🟢 inversion is structural — surplus persists with ME volumes recovering "
                       f"(ME crude vol YoY {me_yoy:+.1f}% vs Apr −67.2%; proxy: ≥ −20%)")
    if me_yoy is not None:
        return ("(c)", f"🟡 inconclusive; defer to June TB (provisional Jul 22) — surplus persists "
                       f"but ME volumes still depressed (ME crude vol YoY {me_yoy:+.1f}%; proxy: < −20%)")
    return ("(c?)", "🟡 surplus persists; ME volume leg UNAVAILABLE — verify manually")


# ---------------------------------------------------------------- TSV

def _f(v, spec=".1f"):
    return format(v, spec) if v is not None else ""


def tsv_rows():
    rows = {}
    if TSV.exists():
        with open(TSV) as f:
            next(f, None)
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 2:
                    rows[(parts[0], parts[1])] = parts
    return rows


def append_row(month, stage_name, data, crude_cost, brent_lag, usdjpy_avg, routing):
    existing = tsv_rows()
    if not TSV.exists():
        with open(TSV, "w") as f:
            f.write(TSV_HEADER)
    key = (month, stage_name)
    if key in existing:
        return False, None

    # revised-from: prior stage row for same month
    prior = None
    for (m, s), parts in existing.items():
        if m == month and s != stage_name:
            prior = (s, parts)

    t = data["total"]
    crude = data.get("crude") or {}
    lng = data.get("lng") or {}
    me_t = data.get("me_total") or {}
    me_c = data.get("me_crude") or {}

    def b(val_M):  # ¥M → ¥B
        return val_M / 1000.0 if val_M is not None else None

    with open(TSV, "a") as f:
        f.write("\t".join([
            month, stage_name,
            _f(b(t["exp_M"])), _f(t["exp_yoy"]), _f(b(t["imp_M"])), _f(t["imp_yoy"]),
            _f(b(t["bal_M"])),
            _f(crude.get("vol"), ".0f"), _f(crude.get("vol_yoy")),
            _f(b(crude.get("val_M"))), _f(crude.get("val_yoy")),
            _f(crude_cost),
            _f(lng.get("vol"), ".0f"), _f(lng.get("vol_yoy")),
            _f(b(lng.get("val_M"))), _f(lng.get("val_yoy")),
            _f(b(me_t.get("imp_M"))), _f(me_t.get("imp_yoy")),
            _f(me_c.get("vol"), ".0f"), _f(me_c.get("vol_yoy")),
            _f(brent_lag), _f(usdjpy_avg),
            routing or "—",
            datetime.now().strftime("%Y-%m-%d"),
        ]) + "\n")
    return True, prior


# ---------------------------------------------------------------- report

def print_report(month, stage, data, crude_cost, brent_lag, brent_spot,
                 usdjpy_avg, consensus_B=None, prior=None):
    t = data["total"]
    bal_B = t["bal_M"] / 1000.0
    sign = "SURPLUS" if bal_B >= 0 else "DEFICIT"
    stage_name = STAGE_NAMES.get(stage, str(stage))

    print(f"\n  {month} Japan Trade Balance — stage {stage} ({stage_name})"
          f"  [published {data.get('kohyoymd', '?')}]")
    print(f"  {'-'*64}")
    print(f"  Balance:   ¥{bal_B:+,.1f}B  ({sign})", end="")
    if consensus_B is not None:
        print(f"   vs consensus ¥{consensus_B:+,.1f}B  (surprise {bal_B - consensus_B:+,.1f}B)")
    else:
        print()
    print(f"  Exports:   ¥{t['exp_M']/1000:,.1f}B  ({t['exp_yoy']:+.1f}% YoY)")
    print(f"  Imports:   ¥{t['imp_M']/1000:,.1f}B  ({t['imp_yoy']:+.1f}% YoY)")

    crude = data.get("crude")
    if crude:
        print(f"\n  Crude & partly-refined oil (world imports):")
        print(f"    Volume:  {crude['vol']:,.0f} 千KL  ({crude['vol_yoy']:+.1f}% YoY)   ← mechanism leg")
        print(f"    Value:   ¥{crude['val_M']/1000:,.1f}B  ({crude['val_yoy']:+.1f}% YoY)")
        if crude_cost:
            band = ""
            if brent_lag:
                dev = (crude_cost / brent_lag - 1) * 100
                band = f"  vs Brent t−1..t−2 avg ${brent_lag:.0f} ({dev:+.0f}%)"
                if abs(dev) > 20:
                    band += "  ⚠️ OUTSIDE ±20% gross-error band — check FX/lag/parse"
            print(f"    Implied unit cost: ${crude_cost:.0f}/bbl{band}")
    lng = data.get("lng")
    if lng:
        print(f"  LNG: {lng['vol']:,.0f} kt ({lng['vol_yoy']:+.1f}% YoY), "
              f"¥{lng['val_M']/1000:,.1f}B ({lng['val_yoy']:+.1f}%)")

    me_t, me_c = data.get("me_total"), data.get("me_crude")
    if me_t:
        print(f"  Middle East imports: ¥{me_t['imp_M']/1000:,.1f}B ({me_t['imp_yoy']:+.1f}% YoY)")
    if me_c:
        print(f"  ME crude volume: {me_c['vol']:,.0f} 千KL ({me_c['vol_yoy']:+.1f}% YoY)"
              f"   [Apr 2026 anchor: −67.2%]")

    branch, desc = routing_suggestion(t["bal_M"], me_c, brent_spot)
    print(f"\n  ROUTING (pre-registered, CALENDAR Jun-17 row — suggestion only, SAM adjudicates):")
    print(f"    Branch {branch}: {desc}")

    if prior:
        ps, pp = prior
        try:
            prior_bal = float(pp[6])
            print(f"\n  ⚠️ REVISED FROM stage '{ps}': balance ¥{prior_bal:+,.1f}B → ¥{bal_B:+,.1f}B"
                  f" — re-adjudicate routing if decomposition moved materially")
        except (ValueError, IndexError):
            print(f"\n  ⚠️ REVISED FROM stage '{ps}' — compare rows in TRADE_BALANCE.tsv")


# ---------------------------------------------------------------- selftest

def selftest():
    print("\n  SELFTEST — fixtures re-anchored to MOF primary 2026-06-10")
    ok = True

    # Fixture 1: Apr 2026 stage 4 (anomaly month, press-corroborated)
    text = fetch_xml("2026-04", 4)
    data = parse_xml(text) if text else None
    if not data:
        print("  ❌ F1: could not fetch/parse 2026044.xml")
        ok = False
    else:
        checks = [
            ("balance ¥M == 301905 (press ¥+301.9B)", data["total"]["bal_M"] == 301905),
            ("crude vol YoY == −63.7 (press −64%)",
             data.get("crude", {}).get("vol_yoy") == -63.7),
            ("ME crude vol YoY == −67.2",
             data.get("me_crude", {}).get("vol_yoy") == -67.2),
            ("exports YoY == +14.8 (THESIS cite)", data["total"]["exp_yoy"] == 14.8),
        ]
        for label, passed in checks:
            print(f"  {'✅' if passed else '❌'} F1 Apr-2026/s4: {label}")
            ok = ok and passed

    # Fixture 2: Jan 2026 (normal month) — XML best stage vs CSV cross-source ±1%
    csv = fetch_csv_headline()
    stage, text2 = best_stage("2026-01")
    data2 = parse_xml(text2) if text2 else None
    if not csv or not data2:
        print("  ❌ F2: missing CSV or Jan-2026 XML")
        ok = False
    else:
        ce, ci = csv["2026-01"]
        xe, xi = data2["total"]["exp_M"], data2["total"]["imp_M"]
        for label, c, x in [("exports", ce, xe), ("imports", ci, xi)]:
            dev = abs(x / c - 1) * 100
            passed = dev <= 1.0
            print(f"  {'✅' if passed else '❌'} F2 Jan-2026/s{stage} {label}: XML {x:,.0f} vs CSV {c:,.0f} ¥M (Δ{dev:.2f}%)")
            ok = ok and passed

    print(f"\n  SELFTEST: {'✅ ALL PASS' if ok else '❌ FAILURES — do not trust parser output'}")
    return 0 if ok else 1


# ---------------------------------------------------------------- main

def expected_latest_month():
    """Most recent statistic month whose provisional could exist. Provisional
    lands ~mid/late following month — probe (today − 1mo) then (today − 2mo)."""
    today = jst_today()
    months = []
    y, mth = today.year, today.month
    for back in (1, 2):
        yy, mm2 = y, mth - back
        while mm2 < 1:
            mm2 += 12
            yy -= 1
        months.append(f"{yy}-{mm2:02d}")
    return months


def process_month(ym, stage=None, consensus_B=None, quiet=False):
    if stage:
        text = fetch_xml(ym, stage)
        if not text:
            if not quiet:
                print(f"  ⚪ no XML for {ym} stage {stage}")
            return False
    else:
        stage, text = best_stage(ym)
        if not text:
            if not quiet:
                print(f"  ⚪ no XML found for {ym} (stages 7..4)")
            return False

    stage_name = STAGE_NAMES.get(stage, str(stage))
    if (ym, stage_name) in tsv_rows():
        if not quiet:
            print(f"  · {ym} stage {stage_name} already in TSV")
        return False

    data = parse_xml(text)
    if not data:
        print(f"  ⚠️ {ym} stage {stage}: page found but parse FAILED")
        return False

    usdjpy_avg, brent_lag, brent_spot = market_context(ym)
    crude_cost = unit_cost_usd_bbl(data.get("crude"), usdjpy_avg)
    branch, desc = routing_suggestion(data["total"]["bal_M"], data.get("me_crude"), brent_spot)

    appended, prior = append_row(ym, stage_name, data, crude_cost, brent_lag,
                                 usdjpy_avg, f"{branch} {desc.split('—')[0].strip()}")
    print_report(ym, stage, data, crude_cost, brent_lag, brent_spot,
                 usdjpy_avg, consensus_B, prior)
    if appended:
        print(f"\n  ✅ Appended to TRADE_BALANCE.tsv  ({ym}, {stage_name})")
    return True


def main():
    args = sys.argv[1:]
    boot_mode = "--boot" in args

    if "--selftest" in args:
        return selftest()

    consensus_B = None
    if "--consensus" in args:
        i = args.index("--consensus")
        if i + 1 < len(args):
            consensus_B = float(args[i + 1])

    if not boot_mode:
        print(f"\n{'='*70}")
        print(f"  SAM Japan Trade Balance — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'='*70}")

    if "--month" in args:
        i = args.index("--month")
        ym = args[i + 1]
        stage = None
        if "--stage" in args:
            stage = int(args[args.index("--stage") + 1])
        process_month(ym, stage, consensus_B)
        print()
        return 0

    if "--backfill" in args:
        i = args.index("--backfill")
        n = int(args[i + 1]) if i + 1 < len(args) else 14
        today = jst_today()
        y, mth = today.year, today.month
        months = []
        for back in range(1, n + 1):
            yy, mm2 = y, mth - back
            while mm2 < 1:
                mm2 += 12
                yy -= 1
            months.append(f"{yy}-{mm2:02d}")
        for ym in reversed(months):
            process_month(ym, consensus_B=None, quiet=True)
        print()
        return 0

    # default / boot: probe for a new release among last 2 statistic months
    found_new = False
    for ym in expected_latest_month():
        if process_month(ym, consensus_B=consensus_B, quiet=True):
            found_new = True
            break
    if not found_new:
        latest = sorted(tsv_rows().keys())
        latest_str = f"{latest[-1][0]} ({latest[-1][1]})" if latest else "none"
        print(f"  ⚪ No new trade-balance release. Latest in TSV: {latest_str}."
              f"  Next: May provisional Wed Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16).")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
