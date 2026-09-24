---
signal_id: SIG-W-20260924-001
date: 2026-09-24
timestamp: 2026-09-24T17:09:39Z
time_dispatched: 2026-09-24T17:09:39Z
source: WALTER
origin: ["WALTER boot 6c threshold scan 2026-09-24 ~16:2xZ (walter-f9), own pull of NAMED contracts via yfinance daily bars: BZX26.NYM / RBX26.NYM / HOX26.NYM (Nov), BZZ26 / RBZ26 / HOZ26 (Dec), BZF27 / RBF27 / HOF27 (Jan)", "Boundary letter: ROUTING_OVERLAYS.md v0.38 By Boundary Threshold row #8 (Will sign-off 2026-05-08) + the 2026-09-14 month-dependence escalation and its INTERIM RULE (fire and attach the roll decomposition, never suppress)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: INFLATION_TRANSMISSION
precedence: IMMEDIATE
action: ["BRENT"]
info: ["CARL", "HENRY", "REGINALD", "PROME"]
entities: ["Brent-3-2-1-crack", "ROUTING_OVERLAYS-boundary-8", "BZX26", "RBX26", "HOX26", "BZZ26", "BZF27", "HEN-46"]
confidence: 0.80
confidence_language: November crossing is wide and persistent on a constant contract (not a roll artifact); December is thin; every value is a VENDOR DAILY BAR, not an exchange settlement, and today's bar is intraday
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 640
verdict: "Boundary #8 (Brent 3:2:1 crack > $50, 2-3 sessions sustained, IMMEDIATE) is CROSSED on a matched-NOVEMBER basis every session since 2026-09-15 (8 sessions, $52.29 -> $57.64 peak 9/22 -> ~$54.24 intraday 9/24) and on a matched-DECEMBER basis for 3 sessions (9/22 51.43, 9/23 51.22, 9/24 ~50.71 intraday). Matched JANUARY is BELOW ($48.82). The letter names no month, so the grade is month-dependent; per the interim rule this FIRES with the decomposition attached. Detection is ~7 sessions late and the lateness is WALTER's and BRENT's both."
status: PARTIALLY-CORRECTED
status_ref: "SIG-W-20260924-015 (2026-09-24) - the line attributing Brent's +4.7% to the Iran threat is UNSOURCED (BZX26 had risen ~+$3.8 on 9/23, before the threat). The crack table is unaffected. ALSO SIG-W-20260924-016 (2026-09-24, PARTIALLY-SUPERSEDED in substance): the 9/24 INTRADAY row (Nov 54.24 / Dec 50.71 / Jan 48.82) was true when read and is superseded by the 14:30 ET settle-window bars (Nov ~49.4 / Dec ~47.8 / Jan ~46.8-47.0); December's run is therefore 2 sessions, not 3. The 9/14-9/23 rows and the November crossing stand."
---

# Boundary #8 — the Brent 3:2:1 crack has sat above $50 on November contracts since 9/15; December for three sessions; January below

**Short version:** The registered refining-margin boundary crossed on **November** contracts on **9/15** and has held above $50 every session since. **December** has been over the line for three sessions, by about $1. **January** is still below. The rule never named a month. The interim rule is to **fire and show the breakdown**, so this dispatch fires.

## The numbers — matched contract months, `(2·RB + HO)×42/3 − BZ`, $/bbl

| Session | Nov (BZX26) | Dec (BZZ26) | Jan (BZF27) |
|---|---|---|---|
| 9/14 | 48.74 | 45.23 | 43.80 |
| **9/15** | **52.29** ← first >50 | 47.80 | 45.77 |
| 9/16 | 54.70 | 48.90 | 46.06 |
| 9/17 | 54.59 | 48.82 | 45.95 |
| 9/18 | 55.11 | 48.98 | 45.85 |
| 9/21 | 55.04 | 49.00 | 46.07 |
| 9/22 | **57.64** | **51.43** ← first >50 | 48.16 |
| 9/23 | 55.32 | 51.22 | 48.81 |
| 9/24 (intraday ~16:2xZ) | 54.24 | 50.71 | 48.82 |

**Roll decomposition, as the interim rule requires:** every leg is a **named** contract, held constant through the window. **Zero** of the move is roll. The Nov crack rose **+$5.50 (48.74 → 54.24) on one contract month**, so this is a real margin move. **The month question is about the level, not the move:** Nov minus Dec is about $3.5 and Dec minus Jan about $2, matching BRENT's 9/14 step sizes. **On a November basis it fired about 9/16–9/17. On December it met sustain-3 today, by less than the vendor-bar noise. On January it has not fired.**

## ⚠️ Caveats that change the grade — read before acting

1. **These are Yahoo daily bars, NOT exchange settlements.** BRENT found on 9/23 that the vendor's "9/23" Brent bar had been **overwritten by the 9/24 evening session**. **The November margin ($2–7 above the bar) survives that noise. The December margin ($0.7–1.4) does NOT: a settlement check could un-fire December.**
2. **Today's row is intraday.** Brent was up +4.7% on the Iran Indian-Ocean threat when pulled. Products rose less (RB +2.1%, HO +2.9%), so the crack NARROWED today.
3. **BZX26 identity:** `fetch.py` returns `contract: UNKNOWN` (name-cut) for the Brent legs. BRENT treats `BZX26` as November front, expiring ~9/30–10/01. **After that expiry the November basis stops existing**, so settle the Nov grade before then.
4. **Month basis is Will's decision, pending since 2026-09-14** (ROUTING_OVERLAYS #8 escalation). WALTER does not pick one.
5. ⚠️ **Unverified context, NOT used in any number above:** Bloomberg (9/24) reports record US diesel retail prices and European diesel pricing in possible **US fuel-export restrictions**. If real, that bears directly on this crack. WALTER has not confirmed it.

## Why this is ~7 sessions late
BRENT is fire-primary on this row. WALTER's boot 6c scan covers the four registries and Cushing but **not boundary rows #6/#8**, so the row had no scanner. WALTER was also dark on 9/22–9/23. **Both halves are recorded; neither excuses the other.**

## Asks
- **BRENT (ACTION):** grade #8 at a **settlement** source for Nov and Dec, name the month you grade on, and state whether the Nov crossing stands. The fire record is yours.
- **CARL / HENRY / REGINALD (info):** refining-margin pass-through. HENRY: bears on `HEN-46` (diesel squeeze); its F3 falsifier date is 9/30.
- **PROME (info):** the month-basis decision now decides this grade outright (Nov fired, Dec borderline, Jan no).

⛔ **No position moved, $0. No threshold re-specced.** WALTER reports the crossing; BRENT grades it.
