# ORACLE — NEXUS Brief

**As of:** market levels 2026-09-25T01:35–01:48Z (**2026-09-24 21:35–21:48 ET**, full update, both venues) · **amended 2026-09-25 ~01:2x ET**: KXRECSSNBER-26 rules read (no NBER leg, KB-ORC-099) + Oct-hike aligned with HENRY in expected bp (KB-ORC-100) — no re-pull | **STATUS commit:** `c3695ad88` | **Box:** DESKTOP, authed Kalshi lane LIVE (rc=0).
**Status:** 🔴 — rates and Fed repricing hawkish; Iran theater got more complicated, not calmer.
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities and crowd-vs-thesis divergence. Inbound routed by WALTER.
**Constraint honored:** no trade implied, no P&L, no position language. No new gate registered.

> **★ THE ONE THING — THE CROWD NOW PRICES A SECOND FED HIKE SOON, ON BOTH VENUES.**
> October hike: PM **66.5%** (Δ7d +16.0, $3.4M) / Kalshi `KXFED-26OCT` differenced **≈65.0** (OI 33.3K) — agreement ~1.5pp. Two more hikes by December: Kalshi `KXFED-26DEC >4.25` **50.0%** / PM end-2026 ≥4.5% **50.3%**. Hike-count "3 hikes in 2026" **41.9% (Δ7d +23.4)**. VX-ORC-08's Alert cell (>66%) is met on Polymarket on one print. (KB-ORC-093)
>
> ⚠️ **Aligned with HENRY (9/25):** at 15:00 ET 9/24 in expected bp — futures ZQX26 **+18.0bp** · PM **+16.5** · Kalshi **+16.1–16.6** ⇒ venues ~1.5–2bp under, **inside the event basis** (Nov-avg EFFR vs upper bound) — not a lag finding. The earlier "~11–12pp under CME 77.5%" (secondary, time-unmatched) is **superseded**. P(hike) cannot be matched to futures. Drivers: Barr + flash PMI (9/23), Williams (9/24). (KB-ORC-100; 097 SUPERSEDED)
>
> **★ THE 10-YEAR CROSSED 5.1%.** PM before-2027 ladder: **5.1% SETTLED** (72.5% on 9/17) · **5.2% 91.6%** (⚠️ $4.0K liq — do not mark a touch) · 5.5% 29.1%. `^TNX` 5.16 / `^TYX` 5.46 (2026-09-24, proxies — the contract resolves on the Treasury par curve). Par==DGS10 still unconfirmed. (KB-ORC-094)
>
> **★ IRAN: FIRST US–IRAN ROUND HAPPENED 9/22 (UN, New York, Qatar mediating) WHILE SHIP ATTACKS INTENSIFIED.** Attendance legs settled YES (Kushner/Witkoff/Araghchi, Δ7d ~+70). ⚠️ Witkoff says the US side talked **through mediators**, not face-to-face — do not cite the settle as proof of direct talks. Next meeting: by 9/30 29.0% · by 10/31 45.5% · **by 12/31 69.0%**. Hormuz-normal-by-Dec **22.5% (+5.0/7d)** — but "shipping targeted" settled YES 9/18, 92.8% 9/21, 98.0% 9/23 (thin books, real volume), and the end-Sept 0–5 transits band is 88.5% (+24.5). **Near term worse, year-end slightly better.** ⚠️ Hormuz legs resolve on the IMF PortWatch PRINT. HAWK owns the reality. (KB-ORC-095)
>
> **★ IRAN'S 5-DAY ULTIMATUM (9/24, ≈9/29) IS PRICED AS LEVERAGE:** ceasefire holds thru 9/30 **85.5%** ($830K vol) / 10/31 56.5% / 12/31 41.0%; US ends blockade by 9/30 **8.5%** / 10/31 30.5% / 12/31 61.5%. Both ladders newly pinned — invisible to ORACLE's coverage sweep until a same-night fix (Gamma caps requests at 100 rows, silently). (KB-ORC-098)
>
> **★ v5 SUPPLY SPREAD +74.10pp @ 2026-09-25T01:35Z** (77.5 − WTI-$110-Sept 3.4%, liq $85.2K). The September leg decays to 0 by expiry — **meaningful from the October leg**, which is **not yet listed** (L299 9/28; v5 dies at the 10/01 close if none lists — a new strike is Will's call). Never compare to v4.

---

## Cross-agent tensions

1. 🟠 **ORACLE ↔ BOND/TERRY — 10Y resolution basis.** The before-2027 ladder resolves on the Treasury Daily Par Yield Curve "10 Yr"; the gate keys on DGS10. I believe they are the same series; **a gate must not consume a believed equivalence** — BOND/TERRY confirm at the primary. Carried since 9/17.
2. 🟠 **ORACLE ↔ RED, recession — my Kalshi label was wrong.** Rules read 2026-09-25T03:39Z: `KXRECSSNBER-26` has **no NBER leg** — it resolves on two consecutive negative BEA GDP quarters in 2025/2026. PM **10.5%** = that same GDP rule **or** an NBER announcement ⇒ the ~**5.0pp** gap vs Kalshi **5.5 mid** (957.4K OI) is structurally expected (PM's extra NBER leg + noise). **Neither venue is an NBER-dated read**; RED's 4–12% (NBER recession *beginning* 2026) is matched in kind by neither. RED's KB-RED-096 inherited my "NBER-only" label — correction packet sent. (KB-ORC-099; 096 CORRECTED) ⚠️ My VX-ORC-02 bands (>20/40/60pp) still cannot see a gap this size — belongs in DAEDALUS F-1. (KB-ORC-096)
3. 🟠 **ORACLE ↔ HAWK/BRENT/FALCON, Iran.** Talks, tempo and the year-end Hormuz leg point three ways. I own the crowd read only. ⚠️ `BZ=F` printed $105.70 vs WTI $93.34 with contract UNKNOWN in the fetcher — flagged, not verified; BRENT owns the tape.
4. ✅ **Closed:** WQ-260 (v5 at $110) encoded 9/24; PROME's 9/24 script-residue packet (three "$100" strings) fixed this session.

---

## Forward catalysts (dated)

| Date | Event | Instrument | Note |
|---|---|---|---|
| **~Tue 9/29** | **Iran's 5-day deadline for the US to accept its road map** | ceasefire thru 9/30 85.5% · blockade-end by 9/30 8.5% | → HAWK, BRENT, FALCON |
| **Mon 9/28** | **DOCKET L299 — October WTI $110 re-pin** | `polymarket.py search` | name the within-v5 roll rule before rolling |
| ~Mon 9/28 | Hormuz weekly → wk-of-9/28 roll | listed, $7.1K | |
| Wed 9/30 | Sept Hormuz ladders · 10Y/30Y Sept ladders · Houthi · Saudi on-date · Kalshi Brent Sep-30 resolve | | → BRENT, HAWK, FALCON, BOND |
| **Wed 9/30** | **DAEDALUS PR#6 ①+② due** | VX-ORC-04 bands (v5 thresholds UNSET) · VX-ORC-09 un-fireable NEH leg | |
| Thu 10/01 | WTI $110 Sept leg closes (03:59Z) | v5 | |
| ~Thu 10/01 | Coverage sweep due | `polymarket.py coverage` | |
| Fri 10/02 | Sept jobs — Kalshi U3 `>4.2` 11.0 / `>4.3` 10.0 mid | `KXU3-26SEP` | → LABOR, HENRY |
| **Sat 10/10** | Sept CPI T-4 re-read (clean like-for-like vs August) | `KXCPIYOY-26SEP` | "+73pp" not quotable until then |
| **Wed 10/14** | September CPI prints | Kalshi `>3.6` 46.0 (modal boundary) | → HENRY, LIQUID, BOND |
| **Wed 10/28** | FOMC | Kalshi `>4.00` 67.0 / PM 66.5 | → LIQUID, HENRY, BOND |
| Thu 10/29 | BOJ October MPM | hold 83.0 both venues | → SAM, BOND |
