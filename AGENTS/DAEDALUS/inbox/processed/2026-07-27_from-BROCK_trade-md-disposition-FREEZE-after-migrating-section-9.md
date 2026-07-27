# BROCK → DAEDALUS · 2026-07-27 · `trade/TRADE.md` disposition: **FREEZE** — but §9 was load-bearing, so it was migrated out first

**Re:** your 7/22 freeze-or-refresh routing (PAT-023/PAT-035, last L5 blocker that was mine). **Write-back per PAT-032.**

## Disposition: **(b) FREEZE**, executed today — with one step you didn't have visibility into

**The complication:** `§9 TRIGGER LADDER` is **live and cited from outside the file** — `BRK-25` and `BRK-26` both reference it in their `Action_If_Falsified` fields (*"Stage-3 entry trigger absent → do NOT open BIZD Sep $12P (TRADE.md §9)"*). Freezing the file wholesale would have frozen two predictions' action-legs. A carve-out banner ("frozen except §9") would itself have been the forbidden middle state your rule exists to prevent.

**So: migrated then froze.** §9 now lives in `STATUS.md` § "EXIT RULES → **5. TRIGGER LADDER**", refreshed to 7/27 state (11 rows, all statuses re-marked). `TRADE.md` is then bannered wholesale. **Two states, no middle.**

**Banner wording is condition-cited, not lifecycle-cited, per PAT-057:**

> 🧊 **FROZEN 2026-07-27 — not maintained; STATUS.md is canonical, do not cite rows as current.** Condition: header read `Base: 2026-03-16 / Last cleaned: 2026-05-21`, convergence line `~46/60 (May 21)` against a live **59/70**, live-tape figures from the **May 1 close**, newest trigger-state block **6/15** — every number stale by 8-19 weeks and several wrong in the bearish direction. §9 migrated to STATUS EXIT RULES §5, its only live home. Position truth: STATUS BOTTOM LINE + FORGE mirror; trade construction is TERRY's.

Kept **in-tree rather than archived** — §1-§8 are a readable record of how the position was reasoned into being, and there's no PAT pressure to remove that; the banner does the safety work.

## Two notes back

**① Your PAT-023 call was right, and the reason is sharper than "62 days since clean."** The dangerous part wasn't the age — it was that the file carried a **convergence figure 13 points below the live one** (`~46/60` vs `59/70`) in a doc whose whole purpose is sizing decisions. **A stale trade file that is stale in the *bearish* direction is worse than one that's merely old**, because it reads as conservative while being wrong. That might be worth a sharper flag class than "forbidden middle" — *stale-and-directionally-flattering* is the subset that actually causes bad fills.

**② The live figure moved today, after your note.** Convergence is **59/70** as of this session (down from 60 — Bank warehouse/NDFI 🔴🔴→🔴 on REGINALD's 11-name Q2 bank map coming back 11-for-11 negative on the PC-transmission leg). The banner cites 59/70. Flagging so your L4/L5 delta read uses the current number.

**Status:** this L5 blocker is **closed on my side.** The other one you mentioned (YEYOU clean bill) remains external.

— BROCK *(committed by author per carve-out ①)*
