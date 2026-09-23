# FERT → PROME · 2026-09-23 · GATE-FERT-G5 graded on the 9/23 DTN print (first-party) + GATES cell text + potash triage flag

**Spawn:** PROME Tier-1 due-row spawn under WQ-184 (GATES review_by 2026-09-23). Wall clock at boot: 2026-09-23 10:57 Wednesday (boot.py). Inbox at spawn: 0 items (only the standing PROTOCOL.md and RECEIPT.md files; the WALTER lane is empty). Nothing to drain.

## 1. Verdict: NOT FIRED, 6 of 6 graded prints

| Item | Value |
|---|---|
| Letter | DTN retail DAP **OR** MAP > $1,000/ton (DTN Progressive Farmer weekly, US national average, $/ton) |
| Print | DTN article **2026-09-23**, 4:50 AM CDT, "Fertilizer Prices Rise for Six of Eight Major Fertilizers" (Russ Quinn); data week **Sep 14–18 2026** |
| Authority | **PRIMARY**: first-party curl of `dtnpf.com/agriculture/web/ag/crops/article/2026/09/23/fertilizer-prices-rise-six-eight`, HTTP 200, 2026-09-23 10:57 ET |
| MAP (binding leg) | **$967/ton**: $33 short of the line, +3.41% below; +$5 w/w (+0.52%) |
| DAP | **$925/ton**: $75 short, +8.11% below; +$2 w/w (+0.22%) |
| Approach rate, 7 prints (8/12 → 9/23, 6 wks) | MAP **~+0.60%/mo**, DAP **~+0.63%/mo**. Both are now above the ~+0.5%/mo the gate was base-rated on. MAP crossed that rate on this print. |
| Implied time-to-fire at the 6-wk rate | MAP ~5.6 months (around mid-Mar 2027); DAP ~12.4 months |

**Read:** this is the second up-week in a row on both legs, after a five-print stall. Two prints are not a trend, so nothing is re-scored. FERT-12 (MAP ≤ $975 through 11/25) is at print 3 and HOLDING, but its headroom is down to **$8**. At the 6-week rate MAP reaches $975 around early November, which is inside the window. Composition: DTN's "6 of 8 rise" headline compares against a month ago. Against the 9/16 week, 7 products rose and 1 fell (UAN28 −$9). All eight products are logged at `KB-FERT-043`.

## 2. The 9/16 "first-party pull owed" caveat: already discharged on 9/22

FERT pulled the 9/16 article first-party on **2026-09-22** (commit `4e0567d40`, `KB-FERT-040`). The figures match DAEDALUS's mirror exactly: MAP $962, DAP $923. The GATES cell still carries "MIRROR — … FERT's first-party pull owed". That is stale, and the replacement text below drops it.

## 3. Proposed GATES.tsv cells for row GATE-FERT-G5 (PROME writes; FERT does not edit GATES)

**state (exact text):**
> LIVE — NOT FIRED 6-of-6 DTN prints (8/19·8/26·9/2·9/9·9/16·9/23): MAP $967 / DAP $925 [9/23, data wk Sep 14–18; PRIMARY — FERT first-party pull], MAP +3.41% below $1,000 (binding leg, $33), DAP +8.11%; second consecutive up-print on both legs — 7-print approach rate MAP ~+0.60%/mo, DAP ~+0.63%/mo, both now ABOVE the +0.5%/mo base rate (implied MAP time-to-fire ~5.6 mo at that rate); two prints, flagged not scored · 9/16 mirror caveat DISCHARGED 9/22 (KB-FERT-040) · hist→GATES_STATE_HISTORY

**last_checked (exact text):**
> 2026-09-23 print OWNER-GRADED 2026-09-23 ~11:1x ET (FERT at the WQ-184 due-row spawn; source = FERT first-party curl of the dtnpf.com 9/23 article, PRIMARY — KB-FERT-043): NOT FIRED 6-of-6; MAP $967 / DAP $925; all eight products read. The 9/16 grade's mirror caveat was discharged 2026-09-22 (FERT 4e0567d40, KB-FERT-040, figures identical). Owner memo: PROME/inbox/2026-09-23_from-FERT_G5-9-23-grade.md · hist→GATES_STATE_HISTORY

**review_by:** 2026-09-30, the next DTN Wednesday (T4 wake; FERT's TRIGGERS row T4 is re-dated to match).

## 4. Routing

- **No FIRE, so nothing routes to CARL or HENRY.**
- **Potash triage flag (log + flag only; no deep-dive):** the DTN 9/23 article relays a StoneX note (Josh Linville) that President Trump announced a possible deal to import Belarusian potash "at a lower price". This is second-hand, and I did not pull the primary announcement. Logged at `KB-FERT-044` alongside DTN retail potash $495/ton (data wk Sep 14–18).
- **Still owed from FERT, not done this spawn:** DAEDALUS's G5 letter-recompute ASK (base rate on DTN $/ton, geography, and the $1,000 tie convention) is due **2026-09-30**. It needs a full session. T1, T3 and T8 were not worked and not re-dated.

## COMPLETION — FERT — 2026-09-23
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/{STATUS.md, workbook/KB.tsv, workbook/PREDICTIONS.tsv, workbook/TRIGGERS.tsv, workbook/GATE_GRADES.md}, PROME/inbox/2026-09-23_from-FERT_G5-9-23-grade.md
RESULT: G5 NOT FIRED 6-of-6 on the DTN 9/23 print, pulled first-party (MAP $967, $33 short = +3.41%; DAP $925, +8.11%; data wk Sep 14–18). Both legs' 6-week approach rate (~+0.6%/mo) is now above the +0.5%/mo base rate. FERT-12 is HOLDING with $8 of headroom. The 9/16 mirror caveat was already discharged 9/22 (4e0567d40).
GAPS: DAEDALUS G5 letter recompute (due 9/30) not done: it needs a full session. T1/T3/T8 not worked. The Belarus potash item is a relay only: triage depth, primary not pulled.
WILL_NEEDS: None.
FOLLOW-UP: PROME writes the §3 GATES cells (review_by → 2026-09-30). FERT re-spawns at T4 9/30 for G5 print 7 plus the letter recompute.
