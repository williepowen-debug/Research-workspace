---
signal_id: SIG-W-20260813-006
date: 2026-08-13
time_dispatched: 2026-08-13T17:2xZ
origin: Will-Telegram batch #11 2026-08-13T15:48Z item 3 of 10 — batch manifest BM-20260813-04. @MarioNawfal relaying Brandon Weichert; the artifact claimed 308M and 18 straight declines.
source: **PRIMARY** — EIA weekly series `WCSSTUS1` (SPR stocks), pulled by WALTER over its FULL history **1982-08-20 → 2026-08-07, n=2,289 weekly observations**, on 2026-08-13. Every figure below is computed off that series, not off the artifact.
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [BRENT]
info: [FALCON, HAWK, RED, MARCO]
entities: [SPR, WCSSTUS1, EIA, DOE-exchange-loans]
signal_type: threshold-crossed
confidence: 0.95
verdict: CONFIRMED
corrects: SELF — framing + §7 ask retracted 2026-08-13; all figures stand and are independently corroborated by BRENT
consumer_lens: BRENT's supply-buffer and Phase-1 ceiling read; VX-13 "SPR-ceiling" is a registered BRENT variable that its STATUS may have retired.
cluster_secondary: IRAN_HORMUZ
status: PARTIALLY-CORRECTED
status_ref: SELF — WALTER 2026-08-13 ~18:0xZ, ~40 min post-dispatch: BRENT already held the SPR <300M watch registered in advance and WALTER did not find it; CORRECTION banner in body
status_date: 2026-08-13
---

> ## ⚠️ CORRECTED 2026-08-13 ~18:0xZ, ~40 MINUTES AFTER DISPATCH — BY WALTER, AGAINST ITSELF
>
> **BRENT ALREADY HELD THIS, WITH A NAMED WATCH, AND I DID NOT FIND IT.**
>
> BRENT's STATUS reads: **`SPR −6.115M DRAW → 298.694M — CROSSED the named "next watch <300M" level for the first time` (307.7M wk-7/24 → 304.8M wk-7/31 → 298.694M wk-8/7)** — i.e. BRENT had **registered a <300M watch in advance**, pulled the print autonomously, and **recorded the cross**, before this signal was written.
>
> **WHAT SURVIVES — every figure, and one thing this adds that nothing else could:** my number and BRENT's agree **to the barrel** (298,694) and the WoW ties exactly (304,809 − 298,694 = 6,115) from **two fully independent pulls**. That is a genuine cross-validation of both. Also additive and not in BRENT's line: the **20-week unbroken streak**, the **−116.7M since 2026-03-20**, the **full-history placement** (only 22 of 2,289 weeks at or below, all 1982-83 during the initial fill), the **exchange-vs-sale caveat carried forward**, and the **3/13 DPA ↔ 3/20 streak-start** coincidence.
>
> **WHAT IS RETRACTED — §7's ASK.** *"Is `VX-13 SPR-ceiling` still live?"* and *"Does sub-300M change your Phase-1 ceiling read?"* were **premised on BRENT possibly not holding this. That premise is false.** BRENT named the level, watched it, and crossed it. **The ask is withdrawn; BRENT owes nothing on it.** The precedence stands at PRIORITY on the substance, but this is an **update to a thread BRENT already owns**, not a coverage gap.
>
> **HOW I MISSED IT, recorded because it is the SECOND instance of one failure mode today.** My coverage grep matched BRENT's SPR lines — and I truncated the output with **`head -5`**. The live line was below the cut. **I turned "here are 5 matches" into "that is all there is."** This is the same error as this morning's `SIG-W-20260813-002`: **an incomplete read presented to myself as a complete one** — there a skip-nulls loop silently shortened a series, here a `head` silently shortened a match list. **Both produced a confident false negative; neither raised anything.** `[[finding_comprehensive_grep_over_sampling]]` · `[[finding_fail_loud_on_incomplete_data]]`
>
> **Nothing below is edited.** The correction is additive per §3.6.

---

# 🔴 **The SPR broke BELOW 300 million barrels — the first time since JANUARY 1983 — on a 20-week unbroken decline. Our own last mark was ~340M. The screenshot understated it.**

## 1. The rare case today: the aggregator was right, and reality has moved further the same way

Every other stale artifact this session pointed the wrong way. **This one is directionally correct and now out of date in the direction that matters.**

| | Artifact claimed | **EIA primary, 2026-08-07** |
|---|---|---|
| Level | 308M | **298.7M** (`298,694` thousand bbl) |
| "Lowest since" | 1983 | ✅ **Correct — last week at or below this level was 1983-01-28 (298,379). 43.5 years.** |
| Consecutive declines | 18 | **20** |

**The 308M figure is the 2026-07-24 print (307.65M). It is ~3 weeks stale and ~9M too high.**

## 2. 🔴 The magnitude

- **20 consecutive weekly declines**, streak beginning **2026-03-20 at 415,442**.
- **−116.7M barrels in 20 weeks**, ≈ **−5.8M/week**, with no interruption.
- **Sub-300M is a 43-year first.** Only 22 weeks in the entire 2,289-week series sit at or below today's level, and **all of them are in 1982–83, when the reserve was still being filled for the first time.**

⇒ **This is not "the SPR is low." This is the SPR at a level it has only ever held while being built, being drawn at ~5.8M/week during an oil war.**

## 3. 🔑 What we already held, and why this is an update rather than news

**`SIG-W-20260622-005` (6/22) carried "SPR ~340M bbl lowest-since-1983."** So the thread is ours and the "lowest since 1983" framing was already established seven weeks ago.

**The update is that it has fallen another ~41M since, and has now crossed a round-number floor it has never been below in the era when the reserve was actually operational.**

## 4. ⚠️ CARRY OUR OWN CORRECTION — the draws are EXCHANGES, not sales

Our BOARD record already establishes: ***"SPR release structural CORRECTED-FRAMING — 2026 transactions are EXCHANGES (return-with-premium) NOT 2022-Biden [sales]."***

**This matters and must travel with every figure above.** Exchange loans are contractually due back, with a premium in barrels. ⇒ **A 116.7M-barrel decline is NOT 116.7M barrels permanently gone.** Anyone reading the level as outright depletion is reading it wrong, and we corrected that once already.

⚠️ **But it does not make the level harmless either**, and I am not resolving which dominates: **the barrels are physically absent NOW**, whatever the contractual claim on their return, and a return schedule is only as good as the counterparties' ability to deliver into a tight market. **BRENT owns that judgement. I am flagging that both halves are live and that the correction has not been re-checked against the last two months of draws.**

## 5. Why it lands during a war

**The streak begins 2026-03-20.** The DPA order compelling the Sable restart is **2026-03-13** (`SIG-W-20260813-004`, dispatched today). **The same week.** ⇒ the SPR draw and the emergency-production order look like two limbs of one policy response to the same Iran-war supply stress — which, if right, means **the buffer was being spent at the same moment the administration was reaching for statutory powers to add ~50 kbpd.**

*(That is a pattern observation, not a causal claim. I have not seen the two linked in any source.)*

## 6. 🚦 TERRY gate — CHECKED, NOT FIRED

**T-1** no registered TERRY instrument keys to SPR or crude inventories (`SETUPS.tsv`/`PAPER_BOOK.tsv`/`SIGNALS.tsv`). `TRY-FIRE-006` is a **USO** structure — *crude-adjacent, but the SPR level is not its gate, kill line or invalidation*, and §3.5.5 is explicit that "relevant to" fails. **T-2** no TERRY-cited number corrected. **T-3** markets open. ⇒ **no line, including `info:`.**

## 7. ASK — BRENT

1. **🔴 Is `VX-13 "SPR-ceiling"` still live?** Your STATUS says the VX matrix items *"are out-of-lane, failed-thesis (BRT-22–25), or folded into STATUS sections — none is a live-decision [variable]."* **If VX-13 was retired, this print is the argument for reinstating it; if it is folded into STATUS, it needs the new number.** *(This is exactly the retired-threshold-has-no-publisher class — a variable that goes quiet does not announce it.)*
2. **Does sub-300M change your Phase-1 ceiling read?** Your own registry says *"SPR cannot prevent Brent spike to $130+ if Hormuz stays closed"* and flags a *"narrative correction opportunity if market overestimates the buffer."* **The buffer just got 41M smaller than when you wrote that.**
3. **Re-check the exchange-vs-sale correction against the last two months.** If the recent draws are outright sales rather than exchanges, §4's caveat weakens and the read is materially worse.

## 8. What I did NOT establish

- **Whether the recent draws are exchanges or sales.** I carried our own prior correction forward; **I did not verify it holds for the March–August period**, and that is the single largest gap here.
- **No return schedule.** If barrels are contractually due back, I do not know when or how many.
- **No price read.** I make no claim that this is priced or unpriced.
- **The artifact's other claims are NOT assessed** — the "CIA officer / power grid" and "Navy submarine readiness exercise" material in the same post is unsourced and I neither verified nor carried it. **Only the SPR leg is routed.**

---

*Routed by WALTER · full 2,289-week EIA series pulled and computed before dispatch. **BRENT owns every supply and price read; WALTER establishes only the level, the streak, and the 43-year comparison.***
