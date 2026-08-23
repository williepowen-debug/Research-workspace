# MIDAS — TRADE

**NO OPEN POSITIONS.** No book yet; placeholder feeding PROME synthesis once MIDAS forms tradeable ideas.

**2026-07-12 update:** first live baseline landed (STATUS.md). M1's trigger ("divergence confirmed + quantified") is now quantified as **NOT confirmed** — trailing 90d shows real-rate-consistent gold decline, not a debasement premium. No candidate below triggers yet.

**2026-07-23 update (still NO position):** M1 **v2 was confirmed** (7/17, both catalyst tests) — the frame is now "gold re-coupled to & capped by real rates; premium in the LEVEL not the delta." The v2 tradeable trigger is a sustained (3+wk) **DIVERGE** (gold rising through rising real yields = premium reassertion) — currently a **nascent WATCH, not fired** (DFII10 hit a new high 2.37 [7/21] with gold firm, but only ~4 days). MIDAS-05 (LPR) graded NO-FIRE, so the I1 copper trigger did not arm either. **No candidate triggers; nothing to TERRY.**

*(Banner-compliant per blueprint §8 / PAT-023: a trade surface carries a FROZEN/NOT-CURRENT banner OR a live mtime alert — never the silent-rot middle. Exempts the surface until MIDAS opens its first idea; `boot.py` runs `ledger_staleness.py MIDAS --trade` regardless.)*


> ⚠️ **THE 8/07 BLOCK BELOW CARRIES SUPERSEDED FIGURES ($4,401.30 · +9.68% · +12bp · −4bp · +8.70%). Preserved VERBATIM by the dated-re-spec rider — do NOT cite it as current. Corrected figures are in the 8/14 update directly beneath it.**

**2026-08-07 update — M1's tradeable trigger has FIRED (still NO MIDAS position).** The v2 tradeable trigger named in the 7/23 update — *a sustained (3+wk) DIVERGE (gold rising through rising real yields = premium reassertion)* — **fired on 8/7**: gold **$4,401.30** (+9.68% over the 3wk window 7/17->8/7) through DFII10 **+12bp** (2.31 -> 2.43) including a **2.47 cycle high [7/31]**. The magnitude test is what makes it a signal rather than a rates bid: empirical beta **-0.0513%/bp** (R^2=0.023, n=647) means the -4bp of the melt-up week explains **~2.4%** of a +8.70% move. M1 **2 -> 3 (Orange)**.

**What that does and does NOT mean for the book:**
- The M1 "long debasement" candidate row below now has its **trigger satisfied** for the first time. Per my charter I produce the signal, **not** the construction: this goes to **TERRY** for expression/sizing and **Will** for approval (root rules #5-#8). **MIDAS proposes no position and takes none.**
- ⚠️ **Timing caveat that belongs on any card built off this:** the trigger fired **after** an 8.7% four-session run. Root rule #6 (puts on green days, calls on red days) and rule #7 (roll duration, don't trim size) are TERRY's to apply, but the honest framing from the signal side is that **entry is arriving late in a fast move**, and a premium regime is the most volatile in both directions (my own precedent: the Jan-2026 blow-off peaked $5,318.40 [1/29/26] and gave back 22.7%).
- **Will already carries the exposure off-rail:** GLD 16 sh = **15.0% of the account**, largest non-cash holding [PROME/ANVIL 8/2 FORGE reconcile]. So the practical question is **not** "should we get long gold" — it is **sizing an existing 15% position in a regime my own signal just called more volatile**. That is a TERRY/Will question; my input is in the 8/7 memo (③).
- **Falsifier for anyone building on this:** gold back below **~$4,050** (7/31 pre-melt-up shelf) while DFII10 holds **>=2.40** re-instates the "re-coupled/capped" frame and takes M1 to 2. Registered as **MIDAS-06**, resolves **8/28**.

**2026-08-14 update — figures above are RE-BASED; `MIDAS-07` graded INDETERMINATE; still NO MIDAS position.**
- ⚠️ **The 8/7 numbers in the block above are superseded by HEARTBEAT Am.#2 (8/10, Will-approved) — they were unsettled bars.** Corrected: gold **$4,340.70** (not $4,401.30), 3wk **+8.18%** (not +9.68%) through **+9bp** (not +12bp); leg-B **+7.20%** against **−7bp**, which at beta −0.0513%/bp explains **~0.4%** of it. **The trigger still FIRED and the magnitude case is STRONGER, not weaker** — real yields rose across the window, the wrong direction for a rates-bid explanation. **Superseded text preserved above verbatim, not rewritten.**
- **Falsifier correction that matters to anyone building a card off this:** the 8/18-line above cites MIDAS-06's branch (a) at **`gold >= $4,401.30`** — **that close never printed on the corrected record.** The boundary was **WILL_QUEUE row 51** and it is **outcome-determinative** (at the 8/13 close it fires on $4,340.70 and not on $4,401.30). ✅ **RULED by Will in-session 2026-08-14** (`PROME/proposals/2026-08-14_afternoon-batch-RULED.md` §1) and **ENCODED 2026-08-20** into `workbook/PREDICTIONS.tsv` — branch (a) now reads **`gold closes ≥ $4,340.70`**, with the superseded `$4,401.30` spec preserved verbatim in-cell per the dated-re-spec rider. **The block on building a card off branch (a) is LIFTED** — the boundary is live and single-valued. The **downside** falsifier (~$4,050 while DFII10 ≥2.40) is unaffected and stands.
- **New, and it belongs on any card:** the 8/11 COT shows the premium now has a **measurable spec-funded component** — OI **+7.74%** in one week on **fresh longs while shorts ADDED**, with crowding in the **top 5% of the 1986–2026 record** (net/OI 54.44% vs 26.3% median). **This is not a fired trigger and I am not treating it as one** — `MIDAS-07` graded **(d) INDETERMINATE** and no score moved. But "entry arriving late in a fast move" (the 8/7 caveat) now has positioning evidence behind it, and that is material to **sizing an existing 15% position**. Sizing = **TERRY**, decision = **Will**. **MIDAS proposes nothing and takes nothing.**

**2026-08-23 update (orch touch 1; still NO MIDAS position):**
- **`MIDAS-06` grades 2026-08-28 ON THE FROZEN LETTER — Will-ruled 2026-08-21 (WILL_QUEUE row 68, record `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`): NO mid-flight edit, no duration clause added, and (d) INDETERMINATE is a legitimate outcome, not a defect.** Anyone building a card off branch (a) must price that in: on the 8/21 finals the row grades **(d)** — gold clears $4,340.70 by **+6.5%** ($4,624.10 [8/21 close, GC=F continuous daily bar]) while **DFII10 2.35 [8/20] FAILS the ≥2.40 leg by 5bp**. One FRED print (8/28) decides it.
- ⚠️ **Instrument note for any card:** the GC=F front-month pointer **rolled to GCZ26 (Dec-26)**; GCZ26's 8/21 last was **$4,680.60** vs the continuous bar's **$4,624.10** (+$56.50 contango). Quote which basis you're on; the roll is not outcome-determinative for MIDAS-06 but a naive "+3.64% Friday" read mixes contracts (like-for-like +2.39%; GLD +1.95% corroborates).
- **COT vintage #2 [as-of 8/18]: the crowding ratchet continued at ~1/5 the prior week's pace** — net/OI **54.69%** (new cycle extreme, top-5% of the 40yr record, 3.0pp off the all-time 57.7%), net **222,189** (+4,249 WoW), OI **406,260** (+1.49%). This snapshot **predates the 8/19–8/21 +5.9% price surge** — vintage #3 (as-of 8/25, releases 8/28) shows whether that leg was chased, and lands the SAME session MIDAS-06 grades. Sizing = TERRY, decision = Will; MIDAS proposes nothing and takes nothing.

---

## Candidate expressions (thesis → instrument, not yet proposed)

| Channel | Direction | Candidate surface | Trigger to propose |
|---|---|---|---|
| M1 | long debasement | gold exposure (**GLD / metal only — miner equities ruled OUT OF SCOPE 8/14**, KB-039) | ✅ **TRIGGER FIRED 8/7** (divergence confirmed + quantified: **+8.18%/3wk vs +9bp** — re-based 8/14 per Am.#2, was +9.68%/+12bp; beta test still isolates **~95%+** as unexplained by real rates). -> TERRY for construction, Will for approval. MIDAS takes no position. ⚠️ **`MIDAS-07` (8/14) = INDETERMINATE — no confirmation added, and the premium is now partly spec-funded (see 8/14 update).** |
| M2 | GSR | gold/silver ratio trade | GSR extreme (>95 risk-off or <75 risk-on) |
| I1 | growth read | copper exposure (CPER) as China-growth expression | demand inflection confirmed w/ LME |
| I2 | supply tail | PGM supply-shock tail | SA/Russia disruption (HAWK) |

*All candidates route through TERRY for construction + Will approval before any position (root rules #5–#8). MIDAS produces the signal, not the execution.*
