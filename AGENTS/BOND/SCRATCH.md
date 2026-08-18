# BOND SCRATCH — 2026-08-18 (Tue, ~09:10 → ~15:xx ET). Will-tasked FULL STALENESS SWEEP of every core document. CLOSED OUT.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md` / auto-memory; thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

**Session shape:** Will said "boot up," then "make sure we update all our stale data in BOND — core documents one at a time." Ran the full boot read, then swept **every** core surface. Late in the session Will noted PROME and ORACLE were working live together, so I stopped adding to their queue.

---

## 🔴 READ THIS FIRST — the three things that were actually wrong

**1. The August quarterly refunding ($125B, 8/11–8/13) ran UNGRADED and was NEVER ON THE DOCKET.** The quarter's largest supply event. Found by cross-checking a WALTER wire reference against the TreasuryDirect primary. **Now graded (5 days late) and retro-docketed.** ⇒ *A missing docket row is invisible in a way a stale number is not: a stale number eventually looks wrong; a missing event looks like nothing.*

**2. The 8/10 C-36 downgrade NEVER REACHED `thesis/THESIS.md`.** For 8 days the durable document asserted "policy-path-led" as settled canon, including an explicit *"do NOT restate this as term premium"* instruction, while the desk's own label was **CONTESTED ~50%**. `STATUS.md` carried it; THESIS did not. **Flagged as a risk in the 8/15 closeout, verified today, and it was real.**

**3. The composition-failure gate hardcoded the 7Y's cut-offs (`<56.4% / >13.2%`) as if general — on FOUR surfaces.** The 10Y's indirect min is **63.95%**, the 30Y's **59.52%**. In THESIS it sat *directly beside that file's own instruction not to reuse the 7Y numbers.* ⚠️ **And I fixed it by the line list in front of me — `consumer_check.py --self` caught it still live in STATUS and PROTOCOL at closeout.** Fix by PATTERN, never by the printed list.

## MARKET — what moved while the desk was dark

- 🔴 **`^TYX` CLOSED 5.31 on 8/17 = a 19-YEAR HIGH** (live 5.32 on 8/18). ⚠️ **"Highest since 2007" is NOT "at the 2007 high" — 2007's peak was ~5.44%, ~13bp of headroom.** ⚠️ **`DGS30`, the grading instrument, has published NO 8/17 value** (H.15 lags a business day) — so the 19-yr-high close is **ungraded on the instrument that grades it.** Recomputed: **29 consecutive sessions >5.00% (7/07→8/14), 45 cumulative days in 2026**; Bloomberg's 2007=50 is **5 sessions away** and still not independently verified.
- 🟢 **August refunding cleared CLEAN.** 3Y ind **64.24** · 10Y ind **76.73** (+8.41pp over median, **2nd-strongest of its trailing-12**) · 30Y ind **66.85**, dealers at-or-below median, **30Y clearing 5.2160% = highest since 2001.** The 30Y clears its own failure bar by **7.33pp**. **12th straight benign resolution. The long end is repricing WITHOUT a demand failure.**
- ★ **NEW DAILY INSTRUMENT: FRED `THREEFYTP10`** (Kim-Wright 10Y term premium). This desk claimed term-premium decomposition as scope on 8/10 and had been running on ACM's **monthly** series. **7/13→8/07: 2Y −7bp, 10Y +3bp, 30Y +9bp, term premium +2.5bp ≈ 83% of the 10Y move** = a long-end-led bear **STEEPENER**, the term-premium signature on my own 7/18 falsifier. **The regime ROTATED after mid-July; the 7/18 call stands for its own window.**
- **DFII10 2.41** — **9bp from the only live add-gate and CLOSING** (was 11bp and widening on 8/15). Peak approach ever: 3bp (2.47, 7/31).
- **Credit retraced further.** HY **267** (below where July began), CCC **1012** (off the 1024 I escalated on). **The CCC/HY ratio high at 3.79x is denominator-driven — HY fell faster.**
- **FR2004: 3 prints recovered.** Long-end total **150.0 [8/05] = −$9.3B in one week**, −14.3% off peak. **Benign distribution CONFIRMED** — dealers cleared ahead of the refunding, which then cleared into firm demand.
- **^MOVE 75.63 and FALLING into 19-year-high yields** — the selloff is **orderly**, not a crisis tape. Worth carrying.
- **SOFR−IORB +1bp [8/17]** — flipped positive, **not a stress signal** (3.66 also printed 8/04 and 7/31; range −3/+1 all month; the kill leg is conjunctive and the auctions were firm).

## WHAT I DID — every core doc, in order

| # | Doc | Commit | Headline |
|---|---|---|---|
| 1 | `STATUS.md` | `2b90b1d43` `e3b9a523f` `61c78f074` `7691db174` | 20 dashboard rows live; refunding section; 305→250 lines, history archived |
| 2 | `thesis/THESIS.md` → **v1.1.4** + CHANGELOG | `49dcc352b` | 8 corrections; the missing downgrade; internal contradiction; per-tenor kill gate |
| 3 | `docket/CATALYSTS.tsv` | `61c78f074` | refunding retro-docketed; 8/19–8/27 calendar from the primary; 6 rows pruned |
| 4 | 4× `monitors/` | `2caae8ec6` | 4 missing auctions back-filled; DEALER_CAPACITY header-vs-body contradiction fixed |
| 5 | `TRADE.md` | `37e96cf60` | was calling 7/28 and 7/29 "live gates resolving in 48h" |
| 6 | `workbook/` KB+VX+FLOW | `581c33cf2` | KB +9; **VX-BND-09 RETIRED**; VX-BND-08 3→2; FLOW-09 CONTRADICTED |
| 7 | `NEXUS_BRIEF.md` | `be36f45a1` | re-pinned; **retracts the credit read I fed NEXUS on 8/15** |
| 8 | `thesis/PREDICTIONS.tsv` | `2cc6451f7` | **book RE-ARMED — BND-14/15/16 pre-print** |
| 9 | `PROTOCOL.md` + STATUS | *(self-check fix)* | the two surfaces the pattern-fix missed |
| 10 | auto-memory ×3 | — | 1 new + 2 extensions |

## SCORE / STATE CHANGES

| Surface | Change | Basis |
|---|---|---|
| **Composite** | **UNCHANGED 12/35, no vector moved** | Largest evidence block since the desk went dark and **nothing crossed a pre-registered line.** |
| `VX-BND-08` Indirect Bid % | **3 → 2** | Refunding indirect at/above median at all three tenors. Roll-up counted once ⇒ composite unmoved. |
| `VX-BND-09` Auction Tail | **RETIRED** | Was scoring 2 on a metric retired as unscoreable 21 days earlier. A score nothing can move. |
| `VX-BND-01` auction health | **held 2 + a DOWNGRADE condition registered** | →1 on three consecutive at/above-median-indirect + at/below-median-dealer auctions. August is 2 of 3. **Registered because it cuts AGAINST my own bear thesis.** |
| Dealer absorption | **held 2; upgrade DECLINED** | Trigger's instrument was unnamed ⇒ a family. Fired on 11–21Y, unfired next print; never fired on long-end total. **Named long-end TOTAL. Firing it would have strengthened my own thesis.** |
| **Position** | **TLT puts HOLD, no add.** Will's 7/16 NO-ADD stands. | (a) DFII10 >2.5 is the only live gate, 9bp. (b)/(c)/(d) resolved-and-dead. |

## NEXT SESSION (dated, future-verifiable)

1. **🔴 TODAY ~4:15PM ET — `BND-16` resolves.** Does FRED's `DGS30` for 8/17 print ≥5.28? **Decides whether T6's defective OR-leg goes live-and-keyed-to-the-wrong-instrument.** State the margin in bp.
2. **🔴 WED 8/19 — TWO EVENTS.** **20Y $16B `912810UX4` at 1PM** (`BND-14` resolves: indirect ≥64.95%? failure test = ind <55.17% AND dlr >17.59%) and **FOMC minutes at 2PM (T7 resolver).** ⚠️ **Grade T7 on the 7/29 vintage (3-mo payroll avg 111K), never today's +20K.** ⚠️ **The LABOR-independence clause is RETRACTED — shared antecedent; a DENY is corroboration across two records of ONE event, not two independent measurements.** ⚠️ T7's premise drift is now ~6pp (written against 35.5%, measured 28.5/30.0). **8/19 does NOT grade T6.**
3. **🟠 THU 8/20 — 30Y TIPS reopen $8B `912810US5`.** Real-money referendum with DFII10 9bp from the gate. **No composition gate — n=3.** *(Also SAM's JGB 20Y — different country, hold separately.)*
4. **🟠 LIQUID owes two things.** (a) The **T6 platform-naming decision + the three spec defects** (packet sent 8/18; my proposal names Kalshi, the platform FARTHER from my trigger). (b) The **7/01→7/15 repo/funding refuse-or-confirm, unanswered since 7/28 — if stress existed, the dealer unwind flips to FORCED de-risking, which is MORE bearish.**
5. **🟠 8/03 P3 START GATE — passed 8/03, STILL NEVER STARTED.** Top owed non-dated item, now 15 days late.
6. **🟡 8/24 — Will's HELD sovereign-CDS sub-item.** Establish the series exists and is pullable **before** proposing any threshold.
7. **🟡 8/28-or-31 — MOF monthly. DATE UNVERIFIED, asked of SAM.** n=3 of my unverified-event-date class.
8. **🔴 8/29 — T6 hard close + HEN-42.**
9. **⛔ `data/auction_history_*.csv` — DO NOT RUN the refresh script.** DAEDALUS defect (2): an unguarded empty-200 path calls `to_csv` **before** validation and can destroy the corpus. Fix order: `.tmp`+validate+`os.replace` → nonzero rc on the 429 path → stamp `cmt_asof` or drop the tail columns. **This corpus BLOCKS base-rating the three held v1.1.4 spec changes.**

## OPEN THREADS / WATCHES

- 🔴 **`BND-14/15/16` OPEN** — first live book since 8/15. **BND-14 and BND-15 are both calls AGAINST the standing bear thesis.**
- 🟠 DFII10 2.41 → 2.50 (**9bp, closing**) · 30Y 45 days >5% vs 2007's 50 (**5 away**) · HY 267 → 300 (33bp, moving away) · CCC 1012 → 1100 (88bp)
- 🟡 **v1.1.4: 2 of 5 adopted, 3 HELD pending base-rating** (they change what FIRES). Plus the revert-speed question, now **n=2**.
- 🟡 **`KB-BND-092` basis trade still unadjudicated by LIQUID**; falsifier **INCONCLUSIVE** (no thin-cover recurrence at the 7Y or the refunding). Next clean test: **8/26 5Y**.
- 🟡 EU leg **dormant** — BTP-Bund 83 [7/17, 32 days]; **ECB GovC calendar verify still owed** at the primary.
- 🟡 JGB 30Y row is **known-superseded**, not merely stale — SAM's 8/17 packet reports the long end through 4% with the shape flipped to a steepener.
- 🟢 `workbook/KB.tsv` still has 4 bare-LF terminators at the KB-073…076 boundaries (pre-existing; 123 rows all validate at 13 fields).

## MAIL STATE

- **Inbox WALTER: 2 UNPROCESSED** (`SIG-W-20260817-001` Japan intervention size/FIMA; `SIG-W-20260817-005` 30Y 19-yr high) — **both READ and acted on** (the 5.31 close, the FIMA-next-time intent and the OMFIF size gap are all in STATUS/FLOW), **but not formally `git mv`'d to `processed/`** — the boot-step-7 lane drain was overtaken by the sweep. **Do this first next session.** A third arrived late: `SIG-W-20260818-003` (WALTER's own correction of the 20Y date — confirms my catch).
- **Inbox (general): 3 UNPROCESSED** — DAEDALUS (tooling defects, **acted on**: DO-NOT-RUN warning written into `AUCTION_HEALTH.md`), PROME (Kalshi BOJ market), SAM (JGB long end through 4%). Separate task per protocol.
- **Consumed + filed:** ORACLE's T6 re-pin → `inbox/processed/`.
- **Packets out (self-authored, committed per carve-out ①):** `AGENTS/LIQUID/inbox/2026-08-18_from-BOND_T6-third-defect-...` · `AGENTS/SAM/inbox/2026-08-18_from-BOND_mof-monthly-release-date-verify-ask-n3-...`
- **Cross-session:** PROME ×3, ORACLE ×1. **PROME corrected me on the JGB/US 20Y attribution and was right.**
- **Outbox:** unchanged — no 🔴-acute cross-agent signal; the T6 and MOF items went as direct packets, which is the right channel.

## CLOSEOUT

- **9 STATUS** ✅ rewritten, 250 lines, on cap. **10 Workbook + predictions** ✅ KB-BND-114…122, VX ×9 incl. one RETIRED, FLOW ×4, **book re-armed BND-14/15/16**. **11 Thesis** ✅ **v1.1.4 + CHANGELOG entry** (8 old→new rows). **12 Forward state** ✅ CATALYSTS rewritten, STATUS twin reconciled to the same event SET (added 8/24, 7/23 ECB, 11/13 which the docket carried and STATUS did not — a divergence predating today); all 4 monitors refreshed. **13 SCRATCH** ✅ this file. **14 RECEIPT** ✅.
- **15 Promotion scan** ✅ 1 new auto-memory + 2 extensions (dedup-first: both extensions cost zero index bytes); 2 BOND-local learnings. Index **66% of byte cap**, under the 75% flow trigger — **no PROME size flag owed.**
- **16 Mirror-consistency** ✅ THESIS ↔ STATUS dashboard/matrix; PREDICTIONS OPEN set {BND-14,15,16} ↔ STATUS scoreboard ↔ THESIS scoreboard; CATALYSTS ↔ STATUS event SET; composite re-summed **2+2+1+2+3+1+1 = 12/35**.
- **Checks:** `orphan_check` ✅ (only PROME's live `board_cursor.txt` — not mine, not swept) · `claim_check --check weekday` ✅ 5 files clean · `consumer_check --self` ✅ **caught 2 live surfaces I'd missed** · `consumer_check` cross-agent ✅ **4 hits DECLINED — SAM's 1024 is `Total_Put_OI` in an FXY chain, different series and unit** · `memory_index_check --strict --slug` ✅ 0 blocking · `check_memory_length` ✅ 66%.
- **17 Git** ✅ BOND-pathspec commits + 2 self-authored packets + 4 auto-memory files.
