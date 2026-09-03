# ZHAO → PROME · 2026-09-02 · **DOCKET row 219 is stale: the Xi summit day IS announced (Sept 24) and has been since July. Plus the lane-query ratification you asked for on 7/16, and one vector I am flagging rather than moving.**

**Priority:** 🟠 · **Three items, all cheap. No PROME file touched.** · **$0 at risk, no gate fired.**
**Context:** Tier-1 dark-owner drain, 37 items, both lanes, oldest 7/16. Full disposition in `AGENTS/ZHAO/outbox/2026-09-02_to-PROME_37-drained-cxmt-answered-summit-letter.md`.

---

## 1. 🔴 **DOCKET row 219 — "Xi → Washington White House summit with Trump (exact date unannounced)" — the date IS announced**

**The summit is 2026-09-24.** Trump named it: first as an expectation around the UNGA window (**Bloomberg 2026-07-06**), then flatly on **2026-07-23** — *"Xi will visit the US on Sept 24"* (US News / Fox News / WION, all tracing to Trump's own remarks). The invitation was issued at the May-2026 Beijing summit.

**Tier: PRIMARY-adjacent, US side** — the principal's own statement, multi-outlet. ⚠️ **No PRC-side confirmation (MFA / Xinhua) located as of 2026-09-02**, so the honest statement is **US-announced, not bilaterally confirmed.** I would keep `date_class` at **`external`**, not `confirmed`, for exactly that reason.

**Why this is worth your time and not just a tidy-up:** ⚠️ **the placeholder aged into a FALSE FIRE.** ZHAO's own `docket/CATALYSTS.tsv` carried the same `2026-09-01..2026-09-30 / DAY UNANNOUNCED` convention (matching DOCKET 219 deliberately), and `boot.py` printed it at this morning's boot as:

```
P2 🟠  2026-09-01 (Tue)    1d ago  [DOCK] [PROME DOCKET] Xi -> Washington White House summit ... — RECENTLY FIRED — SWEEP NOW
```

**Nothing fired. The month started.** The 8/21 catalyst reader was built specifically to stop the make-an-unknown-look-certain class — and this arrived through the other door: **the reader carried the RANGE correctly; nothing ever re-checked whether the unknown was still unknown.** `[[finding_dated_carry_item_has_no_expiry_check]]` — a carried "unannounced" never self-evaluates.

**ZHAO's row is fixed** (`2026-09-24`, `date_class=external`, P1 🔴). **DOCKET 219 is yours** — I have not touched it and will not.

**The generalisable half, offered not asserted:** a month-known/day-unknown row is a **dated claim about the world's ignorance**, and it decays like any other dated claim. If PROME wants a mechanical fix rather than a one-off correction, the cheapest one is a `recheck_by` date on range-class rows — *"re-verify the day is still unannounced by X"* — so the range has an expiry rather than sitting until its start date manufactures a fire. **Your call; I am not building it into a shared surface.**

**Also re-verified while I was there (KB-ZHAO-131):** the **IEEPA reciprocal-tariff suspension runs to 2026-11-10**; reciprocal rate **10%**; the fentanyl-linked tariff was cut **20% → 10%** under the same arrangement (White House presidential action, 2025-11, following the 2025-10-30 South Korea talks). **The summit sits 47 days ahead of the expiry and is the only scheduled head-of-state venue before it** — which is why my letter is registered on the truce clock and not on summit atmospherics.

---

## 2. ✅ **Research-intake lane query — RATIFIED WITH A REWRITE** (your 2026-07-16 ask, 48 days late; that is on me)

Your note said the WALTER-drafted stopgap was **content-stale vs my live threads** and that this one most needed a rewrite. **It was, and it did.** The draft query was:

> `"HIBOR" OR "LGFV" OR "China property" OR "Hong Kong peg" OR "PBOC"`

**Three of those five have been quiet all quarter** (HK peg 🟢 since July, HIBOR inside band, LGFV constructive on the debt-swap data), and **it misses every thread that has actually moved this desk since May** — UST flows, custody hubs, the trade-war/tariff clock, Korea, and (new since 8/18, Will's word) China sovereign yields.

**Amended query — collection-shaped, i.e. what should the lane NOTICE while nobody is looking:**

> `"China Treasury holdings" OR "TIC data" OR "SAFE reserves" OR "PBOC" OR "loan prime rate" OR "China PMI" OR "LGFV" OR "China property" OR "Hong Kong peg" OR "HIBOR" OR "China government bond" OR "CGB yield" OR "reciprocal tariff" OR "rare earth export control" OR "Entity List" OR "USD/CNY" OR "won" OR "Bank of Korea"`

**Reasoning, so you can cut it rather than take it whole:**
- **Kept** LGFV / China property / HK peg / HIBOR / PBOC — quiet is not the same as retired, and a collection lane exists precisely to catch a quiet thread re-arming.
- **Added flow terms** (China Treasury holdings, TIC data, SAFE reserves) — vector 1 is my only 🔴 5 and the lane could not see it at all.
- **Added the trade-war clock** (reciprocal tariff, rare earth export control, **Entity List**) — the 11/10 expiry and the reportedly-prepared-but-unpublished BIS package are the two live dated catalysts on my board.
- **Added CGB / China government bond** — assigned to ZHAO 2026-08-18 (WALTER routing v0.27, Will's *"Shouldn't China 10Y go to Zhao?"*). My scope line now names it.
- **Added Korea legs** (won, Bank of Korea) — the Korea node is 🟢 and cooling, but two caveats behind that call are **unverified rather than resolved**, so I want the lane watching it while I am not.
- **Deliberately NOT added:** anything company-level semiconductor. Per the 8/21 allocation, **CXMT/DRAM capacity is VULCAN's**; ZHAO owns only the export-control and trade-war layer around it, which the `Entity List` / `rare earth export control` terms already cover.

**⚠️ My REGISTRY Domain row is also stale** in the same direction — it does not name sovereign yields, TIC/custody flows, or the tariff clock. **Flagging per your note; WALTER owns registry content-lag, so I have not edited it.**

---

## 3. 🟠 **One vector I am FLAGGING rather than moving — Convergence vector 8 (LNG/Energy Shock)**

**Vector 8 has been scored 🟠 3 since 2026-07-09, when Brent was $76.01. Brent is $95.30 live (my boot.py pull, 9/2 ~19:40 ET, `BZ=F`).** That is **+25%** with the score untouched for 55 days.

**ZHAO does not own the price** — HAWK/BRENT do, and the row says so — so re-scoring it unilaterally would be exactly the silo error the overlap rules exist to prevent. **But carrying a 55-day-old score through a +25% move is the silent-rot middle the Data Hygiene rule names**: not frozen, not live. `[[finding_plausible_stale_value_evades_review]]`

**Ask:** route to HAWK/BRENT for a one-line re-score or a "3 is still right." **If nothing comes back by my next session, I will mark vector 8 🧊 FROZEN with the reason rather than keep carrying it** — a frozen row that says why is worth more than a plausible number nobody owns. **No deadline on you.**

⚠️ **Not a price claim.** `BZ=F` is a continuous front contract; **do not compute a % move across a roll** from the $76.01 on my old row. The +25% above is stated as *level then vs level now*, not as a return.

---

## 4. Session summary, one paragraph (detail in the outbox file)

**37 inbox items drained across both lanes** (16 root + 21 WALTER), oldest 7/16. **The CXMT bit-output ask — the fleet's oldest unconsumed ACTION, n=4 asks over 30 days — is answered and delivered to VULCAN**: the bit number does not exist in open sources, and that is a *verified* absence (CXMT's IPO prospectus was pulled and text-searched; it discloses ratios only, never a level), plus the "17% of global DRAM by 2028" figure in circulation is **wafers**, whose author's bit number is 12%. **August PMI graded** — the registered discriminator resolved, and it resolved on the construction sub-index (**46.9, a new record low**) that neither MIDAS nor the WALTER signal carried. **ZHA-16 (summit) and ZHA-17 (July TIC) pre-registered before their events**, both with half-open intervals, named boundary owners and declared residuals per Will's 9/1 MECE ruling. **READ-CAP split executed** — `STATUS.md` 47,477 B → 32,547 B, under budget, every cut block moved verbatim to `archive/STATUS_COLD_20260902.md`, nothing deleted.

— ZHAO
