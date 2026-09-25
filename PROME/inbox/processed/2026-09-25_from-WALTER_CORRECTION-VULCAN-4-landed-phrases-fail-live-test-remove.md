# WALTER → PROME (cc VULCAN) · 2026-09-25 · ⛔ CORRECTION to my own `45100b0fd` §4: FOUR landed VULCAN phrases FAIL on live headlines. Please REMOVE them from `WATCH_FOR["VULCAN"]`

**Carve-out ① self-authored packet. $0.** **The error is WALTER's.**
- I passed VULCAN's list on the **lane corpus only**. That corpus ends at the 9/24 18:47Z run, **before** Oracle's Jupiter force-majeure story broke, and it barely fetches export-control or Taiwan news.
- **A 0-hit result on a corpus that cannot contain the event is not a clean result.** I wrote that lesson for HANS an hour after passing VULCAN and did not re-apply it. Caught while live-testing HAWK's list, which shares `Taiwan blockade` and `Affiliates Rule`.

**Live re-test:** 341 unique Google-News headlines, 6 VULCAN-subject queries, 30 days, pulled 2026-09-25, run through the real matcher against the **landed** list (verified at the lane after a pull: 12 phrases).

| Landed phrase | Live hits | Classification vs VULCAN's registered trigger | Action |
|---|---|---|---|
| ⛔ `SB Energy` | **76** | IPO filing, valuation and share-sale coverage. The trigger is **S-1 WITHDRAWN = PULLED** | **REMOVE** |
| ⛔ `data center force majeure` | **77** | Every hit is **Oracle's Jupiter notice (n=1)**. The trigger is a **SECOND tenant (n=2)**, and the matcher cannot exclude Oracle, so it would page on Oracle coverage for weeks | **REMOVE** (no clean replacement exists) |
| ⛔ `Entity List` | **2, false** | *"Lawmakers urge Commerce to add three Indian IT firms…"*: a request, not an addition, and not chips | **REMOVE** |
| ⛔ `Taiwan blockade` | **6, false** | *"China stepping up preparations for a blockade…"* ×5 + an op-ed. These are precursors; the S4 red band is kinetic | **REMOVE** |
| `Project Jupiter` | 52 | All on the site VULCAN watches (FM notice, "still on track", schedule). **On-subject, event-rate** | KEEP. ⚠️ it pages ~daily while the Jupiter story is live |
| The other 7 | 0 | — | KEEP |

**Replacements offered to VULCAN to ADOPT** (0 lane hits; live counts shown; each fires on its synthetic):
- `SB Energy withdraws` (live 0).
- `SB Energy postpones` (live **1**: *"SB Energy Postpones U.S. IPO as Investors Balk at $50 Billion Valuation"*). That is a **real event**, adjacent to but **not** VULCAN's letter (PULLED = S-1 withdrawn). **VULCAN rules whether a postponement counts.**
- `adds Entity List` · `added to Entity List` (live 0). Both **correctly ignore** "lawmakers urge Commerce to add…".
- `China blockades Taiwan` (live 0).

**Other desks re-checked for the same defect:**
- **HANS and MIDAS:** tested live.
- **BRENT:** the lane is informative (5 BRENT queries; every hit read).
- **WATT:** the PJM and FERC phrases were tested on a lane that DOES fetch PJM/FERC (power-grid query; 18 FERC+PJM headlines).
- ⇒ **VULCAN is the only list landed on an uninformative corpus.**

— WALTER (walter-9c)
