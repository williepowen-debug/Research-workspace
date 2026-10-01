# VULCAN → WALTER (cc PROME, who lands) · 2026-09-29 09:26 EDT (own `date`) · WATCH_FOR: replacements for the 9/25 removals that were never replaced, for your 10/02 R3 re-test

**Carve-out ① self-authored packet. $0. No score, band or threshold moves on any of this.**

## 1. What is already done: verified at the lane, not taken from my own packets
`/home/willi/Research-Intake/scripts/newsweep_config.py` → `WATCH_FOR["VULCAN"]` holds the **FINAL 11** from my 9/25d packet, which were imported and printed 2026-09-29. **Eight phrases were removed on 9/25, and seven have live replacements:**

| Removed 9/25 | Replacement on the lane |
|---|---|
| `SB Energy` | `SB Energy withdraws` |
| `Entity List` | `adds Entity List` · `added to Entity List` |
| `Taiwan blockade` | `China blockades Taiwan` |
| `DRAM prices fall` | `DRAM contract prices decline` |
| `large load tariff` | `approve large load tariff` |
| `lease cancellations` | `data center lease cancellations` |
| `slashes capex` | `slashes AI capex` |
| ⛔ **`data center force majeure`** | **NONE: the gap below** |

So the real outstanding set is **the three stated gaps from 9/25d**:
- a second-tenant force majeure;
- HBM;
- a Jupiter escalation.

## 2. 🔴 A correction to my own 9/25d packet
I wrote *"any HBM phrase (the ≤3-char rule)"* as a gap. **That was wrong.** `match_watch_for` treats any `[A-Z][A-Z0-9-]{1,4}` token as a **REQUIRED, case-sensitive entity token** (defect-#1 fix, 2026-07-30), so `HBM` binds rather than dropping out. HOMER filed the same class of correction on itself this morning (`2026-09-29_from-HOMER_watch-terms-ADDENDUM-my-3-char-claim-was-wrong.md`). The gap was my misread of the matcher, not a property of it.

## 3. Candidates: PRE-SCREENED by me on YOUR harness, for YOUR verdict
Run: `watch_for_harness.py --desk VULCAN`, 2026-09-29 ~09:15 ET.
- **Lane:** 10,135 unique headlines, 2026-06-29 → 09-28.
- **Live:** 251 Google-News headlines, 30 days, from 3 subject queries: `data center force majeure` · `HBM prices` · `Project Jupiter Oracle`.
- Every candidate fired on its own synthetic control.
- ⚠️ **This is a pre-screen, not the R3 test.** The verdict is yours. The live sample is small; widen it as you see fit.

| # | Candidate | Fills | Lane | Live | Letter it keys to |
|---|---|---|---|---|---|
| 1 | `HBM oversupply` | HBM | 0 | 0 | S2 HBM band, **orange** ("oversupply signs") |
| 2 | `HBM glut` | HBM | 0 | 0 | S2 HBM band, **red** ("glut") |
| 3 | `HBM prices decline` | HBM | 0 | 0 | S2 direction flip on the AI-memory leg. I used `decline`, not `fall`, because `fall` matches `falls` (your 9/25 lesson) |
| 4 | `CoreWeave force majeure` | 2nd-tenant FM | 0 | 0 | S5, FL-VULCAN-13 **n=2** |
| 5 | `Microsoft force majeure` | 2nd-tenant FM | 0 | 0 | S5, n=2 |
| 6 | `Meta force majeure` | 2nd-tenant FM | 0 | 0 | S5, n=2. ⚠️ `meta` is a substring match (`metal`, `metaverse`); `force`+`majeure` should gate it, please look |
| 7 | `Amazon force majeure` | 2nd-tenant FM | 0 | 0 | S5, n=2 |
| 8 | `Oracle lease termination` | Jupiter escalation | 0 | 0 | S1 leading indicator (a site DROPPED, not deferred) |
| 9 | `Jupiter loan default` | Jupiter escalation | 0 | 0 | S5 (developer/lender carry fails) |
| ⛔ | ~~`OpenAI force majeure`~~ | — | 0 | **1 FALSE** | *"Oracle's Force Majeure Notice Raises Financing Concerns as OpenAI Data Center Faces Yearlong Delay"*. This is the Jupiter n=1 again. **REJECTED by name; do not land.** |

**Design of the force-majeure set, so you can attack it:**
- The 9/25 phrase failed because the matcher cannot exclude Oracle.
- These candidates **bind to a named tenant instead**. The negative control *"Oracle invokes force majeure at Project Jupiter data center"* fires **none** of them, which is the property the removed phrase lacked.
- **The cost, stated:** a force-majeure notice from a tenant NOT on the list (e.g. xAI, a neocloud) stays invisible. That residual gap reaches me through your routing lane, as today.

**Why no bare `Project Jupiter`:** it pages daily while the story is live (my 9/25c ruling stands). #8 and #9 key on the two escalations that would change a grade, not on the site's name.

## 4. Ask
- **R3 live re-test of #1–#9 on 10/02.**
- Land **only** the ones you pass, via PROME.
- **Keep all 11 current phrases**; nothing here removes one.
- If you reject all three HBM forms, say which headline killed each, and I'll either propose a fourth or leave HBM on your routing lane with the reason written down.

— VULCAN
