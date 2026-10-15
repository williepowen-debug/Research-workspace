# LIQ-07 (LIQUID's funding-accompaniment verdict, due Fri 10/16) — RED's pre-written reading

**Written:** 2026-10-14 ~22:45 EDT (S52, on Will's word: "go ahead with #7 the LIQ-07 check"). **PRE-DATA:** the funding observations that decide the verdict publish 10/15–10/16. **LIQUID owns the grade.** RED checks that its own 10/1 asks were answered, verifies the legs it can pull, and pre-states what RED does with each answer.

**What LIQ-07 is:** credit spreads triggered on 9/30 (ICE B 15-session change +36, CCC widening). Did funding stress accompany it within ±10 sessions?
- **S1 (yes):** a funding leg reads: SOFR dispersion z ≥4, GATE079 ARM, or SRF ≥ $50B.
- **S2 (no):** all three absent on both completed session lists.

Letter: `AGENTS/LIQUID/reports/2026-09-25_Q2_first-observation-of-spreading.md` §3. LIQUID's verdict plan: `AGENTS/LIQUID/research/2026-10-14_credit-funding-refresh/REPORT.md` §"October16 LIQ-07 verdict".

## 1. RED's four asks from 10/1 (packet 4b0a16d64): all answered, checked at LIQUID's artifacts

| # | Ask | LIQUID's answer | Checked |
|---|---|---|---|
| 1 | Fix the S1 base-rate date (10/31 → 11/28–12/01) | **ACCEPTED, VERIFIED**; erratum written into the letter 10/01 (`analysis/2026-10-01_9-30-cell-grades-LIQ-07-trigger.md`:106; letter §3 line 65). RED later conceded the z leg *did* read inside 10/14's window (ML-RED-272). | ✅ |
| 2 | HYG/JNK shares outstanding 9/24→10/14 | Official issuer histories (no longer "no free history"): **HYG 197.3M → 236.5M [10/6] → 229.1M [10/13] (+16.1%)**; **JNK 71.27M → 62.87M → 61.67M (−13.5%)**. Indicative net creations 9/25–10/13: **HYG +$2.45B, JNK −$0.89B, combined +$1.56B**. To be refreshed through the verdict window. | ✅ (through 10/13) |
| 3 | Context rows: SWPT/WORAL, A2P2−AA CP, October long-end auctions | CP gap **20bp [10/13]** (matched dates 18–22) · **WORAL $2M [10/7]** · **SWPT withheld under WQ-404** (offshore dollar NOT GRADED) · 10/8 30Y auction **clean** (BOND) | ✅, **with a correction to RED** (below) |
| 4 | State that S2 means "no reserve-scarcity loop", not "no loop" | *"The verdict must say 'no reserve-channel loop observed,' not 'no loop.'"* RED's caveat is carried. | ✅ |

**⚠️ Correction accepted (RED was wrong):** RED's 10/1 packet labelled WORAL "foreign/official repo." FRED's title is **"Assets: Other: Repurchase Agreements: Wednesday Level"**. It is the Fed's repo *lending* (it moves with SRF: $1,200M on 9/30 equals RPONTTLD $1.2B that day), not the foreign-official reverse-repo pool. LIQUID's correction stands.

**⚠️ Concession (RED's "one live-looking channel" did not confirm):** on 10/1 RED named credit-fund *redemptions* as the loop LIQUID's three legs could not see. Across the window the two big HY ETFs saw **net creations of +$1.56B combined**. HYG creations outweighed JNK redemptions, so **no aggregate redemption loop is visible.** The one honest qualifier: both share counts have fallen since 10/6 (HYG −3.1% from its peak, JNK −1.9%). Recorded, not argued.

## 2. The legs RED can pull itself, through the latest published day

| Leg | RED pull (FRED, 10/14 ~22:40 ET) | Reads |
|---|---|---|
| SRF ≥ $50B (`RPONTTLD`, $B) | max **1.2 [9/30, quarter-end]**; 0.000–0.004 on every day 10/1→10/14 | **absent** |
| SOFR99 − IORB (GATE079's input) | **5–9bp** 9/28→10/13 (3.95–3.99 vs 3.90); in-sample alarms ran 9–33bp | **absent** on any plausible bar (RED does not grade ARM; LIQUID owns the rule) |
| SOFR dispersion z ≥4 | LIQUID's `sofr_dispersion.py`; **RED cannot run it** | LIQUID reports absent; **UNVERIFIED by RED** |

LIQUID reports **0 of 3 through 10/13**. RED's two pullable legs agree.

## 3. A pre-data point on LIQUID's session list (LIQUID's call; raised before the 10/15 data)

LIQUID counts the ±10-session window on two lists and pre-registered **AMBIGUOUS-BY-SESSION-LIST** for a funding event on 10/15 that only one list contains.

**The ICE list counts 10/12 (Columbus Day) as session 9.** That bar is a forward-fill: ICE B 3.10 [10/9] = 3.10 [10/12]. The bond market was closed (SIFMA full close), and SOFR correctly has no 10/12 print. So:
- **With 10/12 counted:** the ICE list's 10th session is **10/14**, while the SOFR list's is **10/15**. The lists disagree on whether 10/15 is inside the window.
- **With 10/12 treated as a non-session:** both lists end on **10/15**. The ambiguity branch **cannot arise.**

RED adopted exactly this rule for its own registry tonight (Will-approved, P1: a bar dated on a closed-market day is a non-session). It is offered to LIQUID **before** the 10/15 data and without knowing whether 10/15 reads. **Direction, stated:** in the one case where it matters (a 10/15-only funding event), it resolves toward **S1**.

## 4. What RED does with each verdict (pre-stated)

| LIQUID's verdict | RED's action |
|---|---|
| **S2** | Record it, with "no reserve-channel loop observed" carried verbatim. **No RED weight moves.** The S52c pre-stated Acute +1 needs S1, so it does not fire. |
| **S1** | Check the S52c conjunction: if 10/15 H.4.1 primary credit (WLCFLPCL) rose for a **4th straight week** above $9.965B [10/7] **and** LIQ-07 = S1, then **Acute +1** (discretionary, as pre-labelled) on 10/16. FT-02 keeps its own +3, not netted. |
| **AMBIGUOUS-BY-SESSION-LIST** | Record it; no RED move. RED notes whether §3's point would have resolved it. |
| **Delayed / not adjudicable** | Record it. LIQUID's letter is Resolve_By 11/10; RED does not grade it for them. |

**Discount-window context:** $6.2B [9/23] → $8.7B [9/30] → $10.0B [10/7]. The 10/14 point publishes Thu 10/15 ~16:30 ET.

Sources: LIQUID REPORT 10/14 lines 9/51–57/62–75 · LIQUID letter §3 · LIQUID `analysis/2026-10-01_…`:106 · RED packet 4b0a16d64 · FRED `BAMLH0A2HYB`, `RPONTTLD`, `SOFR99`, `IORB`, `SOFR`, `WLCFLPCL`, and the WORAL series page (pulled 2026-10-14 ~22:40 ET) · ML-RED-270/272 · `reports/2026-10-14_S52_weight_rederivation.md` §3.
