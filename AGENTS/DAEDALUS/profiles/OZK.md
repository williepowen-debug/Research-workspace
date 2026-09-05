# Agent Profile — OZK

**Built by:** DAEDALUS · **Body:** 2026-08-07, **refreshed 2026-09-05** · **Method:** solo read + each named L5 item re-measured
**Staleness:** 21-day clock → checkpoint **2026-09-26**

## 1. Identity
**Bank OZK specialist** — RESG construction book / classified-migration watch. Market class, ACTIVE, single-name depth desk. **Spawnable by:** PROME / Will.

## 2. State
Last session **2026-08-31** (IQHQ Aug window CLOSED — disclosure sweep RUN, **swept and empty**, inbox drained). STATUS **163 ln**. Still one of the most current desks in the fleet.

## 3. The three mechanical L5 items — re-measured
| # | Item | Status 2026-09-05 |
|---|---|---|
| 1 | **KB_INDEX group tables not re-rolled** | 🔴 **STILL OPEN, and now precisely located.** `KB_INDEX.md:3` header was updated **8/28** and explicitly names **+228** and **+229** — but the **group tables inside max out at 227**, while `KB.tsv` runs to **229**. So two KB rows exist in the ledger and appear in **no group table**. The debt is not the span (the header's `218–229` is correct); it is the body the header vouches for. |
| 2 | **outbox/ root not drained to delivered/** | 🔴 **STILL OPEN and GREW: 10 → 13 files**, oldest **2026-07-18**, and the 7/23 `ozk09-remark-proposal` citation target is still among them. |
| 3 | **Two-clock headers on KB.tsv + PREDICTIONS.tsv** | ✅ **DONE.** Both carry `# Last real data refresh:` — KB.tsv `2026-08-23 (rows 223-227, MI3 2025Q3 adjudication)`, PREDICTIONS.tsv `2026-07-23`. |

## 4. Finding
**🟠 F-1 — item 1 is a textbook header-over-stale-body.** The `KB_INDEX.md` header was edited on 8/28 to announce the two newest rows, which is the edit most easily mistaken for maintenance: **a fresh header over an unrefreshed body certifies the body** `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`. A reader checking currency sees an 8/28 stamp naming 228/229 and stops. **Cost is two group-table rows.**

**🟡 F-2 — the outbox debt is now aging past its own usefulness.** Thirteen files, oldest 49 days. `outbox/` root is supposed to signal OPEN loops only; at 13 it signals nothing. Note the delivery-verification rule applies: `delivered/` is a claim only the **recipient's** tree can settle.

## 5. Grade — **L4 (H) HELD**
| Leg | Verdict | Basis |
|---|---|---|
| L1–L2 floor | **PASS** | STATUS + BOTTOM LINE; KB 229 rows, PREDICTIONS, ledgers accruing with two-clock headers |
| L3 convergence / exit / predictions / dated falsification | **PASS** | P-OZK cards; IQHQ window discharged on its last business day |
| L4 signals flowing / consumed | **PASS** | BROCK + REGINALD packets delivered; MI3 adjudication consumed |
| L5 clean closeouts | **PASS** | 8/31 closeout clean, window discharged on time |
| L5 zero YEYOU flags | **WAIVED** | no live feed |
| L5 current | **PASS** | 5 days |
| **L5 structural hygiene** | **FAIL** | items 1 + 2 above — **two mechanical items, one session** |

**L5 next-upgrade line:** *re-roll the KB_INDEX group tables through 229 (the header already claims them) + drain outbox/ root to delivered/ verifying at each recipient's tree. Two items, one session. The two-clock headers are done.*

## 6. DO NOT TOUCH
1. **P-OZK card numbering** and the KB-OZK id sequence (cited across STATUS/INDEX/research).
2. **The frozen Option-2 IQHQ framing** — the Aug window resolves nothing under it; a swept-and-empty result is a real result, not a gap.
3. **`boot.py` staleness basis is git-commit-first and prints its basis** (:278-292) — resolved 8/07; don't re-key it to mtime.
4. **The 8/23 retraction inside `KB_INDEX.md:3`** (the false "no 10-Q" note) — it is a correction record, not clutter.
