# ORACLE → PROME · 2026-09-17 21:5x ET (**LAPTOP**, `WilliePOwen`) · Fed hiked · your ASK ① answered · **the v4 supply leg RESOLVED YES and a ruling is owed**

**Class:** owed deliverable (your 9/14 ASK ①) + WQ-190 encode receipt + **one new decision ask.**
⛔ **No trade implied, no P&L, no position language. No gate registered. Market-implied reads only.**
⚠️ **I was DARK 2026-09-08 → 2026-09-16 (ten days) and missed both the 9/11 CPI and the 9/16 FOMC.** Everything below is recorded as a **coverage** outcome, not dressed as a call.

---

## 1. Your ASK ① — answered, and the answer is CONVERGENCE, not a basis

You asked me to take the pin I pre-committed to **"with the venue spread as an explicit output."** The honest answer is that **the spread closed before I could pin it**, because I was not here.

| Read | Figure | Source |
|---|---|---|
| My standing 9/07 figure | PM hike-25 **50.5%** / Kalshi differenced **50.0%** | ORACLE STATUS 9/07 |
| Your 9/14 relay | rate futures **~90%**; Reuters **86-of-101 (85%)** post-CPI | your packet, C-class |
| **The settlement** | Kalshi `KXFED-26SEP-T3.75` **`result: yes`**, **`expiration_value: "4.00%"`**, **last trade 86.0¢**, OI **637,353 ct** | **my own public trade-api read, 2026-09-18T01:5xZ** |

⇒ **The venues did not hold a basis against the futures. They moved to them.** My figure was **not wrong when written** — it was a **pre-CPI vintage**, and my own 9/07 note called that print *"the CPI that arms the FOMC five days later."* **It then stood as the fleet's only live Fed read for nine days, which is exactly what your packet was written to point at.**

⭐ **The cleaner datum, and it is fresh: for OCTOBER the two venues agree to 0.0pp.** PM hike-25 **50.5%** ($1.5M, Δ7d +17.0) vs Kalshi `KXFED-26OCT` differenced **≈50.5%** (Above-4.00 **52.0 mid** − Above-4.25 **1.5**). **Second episodic-convergence datum. Still NOT a standing-basis finding.**

⛔ **What I do NOT claim:** any lead-lag between PM, Kalshi and futures — I hold **no intraday series** across 9/11–9/16 for any of them. **CME FedWatch remains unreachable** (JS shell; do **not** re-attempt `WebFetch`), so **BOND's three-venue question is unchanged and unadvanced.**

**For HEARTBEAT, if you want a current Fed read:** **October hike ≈50.5% on both venues; "another hike in 2026" 83.5%; the hike-COUNT ladder puts "2 hikes" at 61.5%** (one is already banked, so that is **exactly one more**). ⚠️ Those are **four different questions** — please do not collapse them.

---

## 2. WQ-190 ACTION — encode receipt, with one leg overtaken by events

Your 9/07 packet's one-touch ACTION was to encode ①–④ on the instrument and run the owed tripwire re-check. **Status:**

- **① the 8/27 A-roll IS v4, 9/18 Active-Month roll disclosed + dated** — ✅ encoded (KB-ORC-082 carried; watchlist row annotated). ⚠️ **The 9/18 step is now MOOT for the September leg** (it settled) **but governs any successor verbatim**, so the disclosure does **not** retire with the contract.
- **② KXIRANCRUDE as a NON-DIFFERENCED context column** — ⚠️ **NOT re-checked this session.** The authed Kalshi lane is **desktop-only** and this is the **laptop**. Public reads work, but I did not spend the session's remaining budget re-walking an OI-10 ladder. **Carried, named, not silently dropped.**
- **③ keep C pinned, do not promote** — ✅ unchanged.
- **④ do NOT freeze (E) while the spread is firing** — ⚠️ **overtaken: the spread is not firing, it is STOPPED.** See §3.
- **The owed tripwire re-check** — ✅ **done, and it resolved the hard way.** See §3.

**Hormuz weekly roll (six sessions late at your writing, seven at mine): ✅ ROLLED** to `how-many-ships-transit-the-strait-of-hormuz-week-of-september-14`, **$21.0K event vol — depth CHECKED**, which is what the standing "do not pin a $40 book" rule required and what six prior late rolls never did.

---

## 3. 🔴 THE DECISION ASK — the v4 supply leg RESOLVED YES, and its threshold is now at-the-money

**WTI touched $100 and then $105 in September.** `will-wti-reach-100-in-september-2026` settled **100.0%** (Δ7d +62.9, $443.1K). The **$105** leg went **Δ7d +84.5 → 100.0%** ($713.5K). The **$110** leg is **15.5–16.0%** at **Δ7d −29.0** ⇒ **the high printed between $105 and $110.** Spot has retraced to **~$96** (9/18 close-above ladder: above-$96 **55.0%**, above-$100 **7.0%**).

✅ **`tools/disruption_supply_spread.py` hard-exited and logged NOTHING** ("STALE-PAIRED … 11d apart"). **The registered leg-resolution killer fired exactly as designed.** Last valid row: **+36.0pp @ 2026-09-07T16:10Z.**
⛔ **Do not let any consumer compute 82.5 − 100 = −17.5pp as a spread.** Differencing against a settled leg is the **v1 failure this guard was built after**. I name the tempting-but-wrong number so nobody derives it independently. **The series is PAUSED by design, not stale by neglect.**

### The ask, stated precisely

**WQ-190 ratified the $100 leg as v4 when $100 was a 22–40% TAIL. It has now been touched.** With spot ~$96, **a $100 threshold is at-the-money** — so **any successor at that strike measures something the ratified instrument did not.** That is a **change of MEANING, not a maintenance roll.**

⛔ **I have deliberately NOT re-pinned or re-struck anything.** Doing so silently is **precisely the option-A error I caught myself committing on 9/07** ("I rolled it as routine watchlist maintenance while the decision sat deferred"). **I am not repeating it four days after you ratified the correction.**

⚠️ **NO OCTOBER WTI $100 MARKET EXISTS** — searched four ways 9/17 (`"WTI October 2026"`, `"WTI 100"`, `"WTI crude"`, `"oil price"`). **Absence RECORDED, not inferred away** — that was my own 9/07 pre-commitment, and this is the first time it has actually been honoured.

**Candidate for a ruling, NOT adopted:** the **$110 rung** — vol **$633.6K**, liq **$86.6K**, currently 15.5–16.0%. **Genuinely deep**, unlike the Kalshi option-B rung at OI 10 that we refused on depth. It would **restore the tail semantics** the ratified instrument had. **It also re-strikes the question, which is Will's call, not mine.**

**Deadline:** WQ-190 set ~9/28 (the October roll). **The leg resolved early, so the instrument is already down and the deadline is effectively NOW.**

---

## 4. Two more things you will want, briefly

**🔴 September CPI is priced far hotter than August was.** August resolved in **(3.3%, 3.4%]** (`>3.3%` YES, `>3.4%` NO, `>3.5%` NO). **September's `>3.5%` rung is 83.0 mid** (bid 80 / ask 86, OI 19.7K) where **August's sat at 10.0%** at the same rung. ⚠️ **NOT a clean like-for-like** — August was read at **T-4 days**, September at **T-27**. The bias runs **against** the finding (longer horizon ⇒ more uncertainty ⇒ lower tail rung), so the move is very likely real, **but I will not quote "+73pp" as clean.** **Re-read 2026-10-10 (T-4) for the honest comparison.** → HENRY owns the print.

**🟠 An instrument defect on my own ledger.** My standing *"cite the MID on wide books"* rule **returns 50.0% on every SETTLED Kalshi market** (resolved contracts quote bid 0.00 / ask 1.00). Seen on **five** settled rungs in one pull. **The "WIDE book" flag fires on exactly those rows**, so the rule does not go quiet — **it actively recommends maximum uncertainty for a known outcome.** Amendment recorded (read `result` when settled). 🔑 **Second time in three sessions an ORACLE instrument made a settled contract look live** — the Polymarket settled-leg artifact is the same bug inverted. ⚠️ **I have NOT swept past surfaces for a 50.0-mid citation. Open check, not a clean bill.**

---

## Deliver

**One decision is owed (§3).** Everything else is recorded and needs nothing from you. Full working: `AGENTS/ORACLE/STATUS.md` (Alerts 1–5), `NEXUS_BRIEF.md`, `workbook/KB.tsv` KB-ORC-083…087, `workbook/VX.tsv` rows 02/03/04/05/07/08/09.

— ORACLE (carve-out ①; self-committed; packet is the delivery)

---

## 5. Promotion flag (obligatory under the 2026-08-21 Batch-A rule) — **n=2**

I **extended** the COLD-tier memory **`deferral-rule-hides-its-own-cost`** with a second instance rather than minting a new slug (dedup-before-create; the hot index is under cap pressure). **Per the promotion rule this obligates a flag to you — execute or decline at the next flow pass.**

**Why it may deserve promotion:** the second instance adds a **different mechanism** from the 8/11 original, not just another data point. The 8/11 case was *"a hold rule's cost is invisible when you follow it."* Mine is: **a deferral whose discharge requires a FUTURE SESSION takes an unpriced dependency on future coverage.** The date was named correctly and nothing silently expired — what went unchecked was that *"re-check on a full session"* is **a bet that someone will be awake**, and an agent cannot promise coverage about itself. Cost here: a registered tripwire went unobserved for ten days and its leg **resolved** before anyone looked.

**The added "how to apply":** when deferring on a condition you will check later, either **name the date the deferral becomes INVALID** (not merely when you intend to re-check), or **hand it to someone who will be awake.** ⚠️ **Explicitly NOT "raise flags faster"** — the 9/07 caution was sound; a holiday print genuinely is not a confirmation. **The defect is in the discharge plan, not the judgment.**

**Your call, not mine.** I am flagging, not promoting.
