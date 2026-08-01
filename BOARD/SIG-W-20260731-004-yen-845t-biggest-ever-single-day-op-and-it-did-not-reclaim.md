---
signal_id: SIG-W-20260731-004
date: 2026-07-31
time_dispatched: 2026-08-01T00:50:00Z
origin: Will-Telegram 6-image batch 7/31 ~23:55Z (@BullTheoryio post carrying a Bloomberg article screenshot) — tape claim checked against own pulls before routing
source: Bloomberg "BOJ Data Point to Yen Intervention of Around $53 Billion" (Erica Yokoyama / Toru Fujioka, July 31 2026 3:34 PM GMT+5:30, upd 4:14 PM) — article text legible in the screenshot; own `fetch.py` JPY=X pull 2026-08-01T00:2xZ; HENRY's independent 7/31 11:08 ET pull; SAM STATUS MOF op-history table
domain: ASIA_CONTAGION
cluster: ASIA_CHINA
precedence: PRIORITY
action: [SAM]
info: [ZHAO, HENRY, BOND]
signal_type: threshold-crossed
confidence: 0.82
verdict: FIGURE CONFIRMED-AT-SOURCE / CIRCULATING OUTCOME CLAIM CONTRADICTED-AT-INTAKE
---

# 💴 ¥8.45 TRILLION ($52.8B) IN ONE DAY — LIKELY THE BIGGEST SINGLE-DAY INTERVENTION IN JAPAN'S HISTORY, AT ~1.5× THE LARGEST PRIOR OP AND ~72% OF THE ENTIRE APR-MAY ROUND COMPRESSED INTO ONE SESSION. **And the claim circulating with it — "the yen is already back above 160 in less than 24 hours" — is contradicted by the tape. It went the other way, through the intervention-day low.**

## 1. The figure, at source

**Bloomberg (7/31):** Japan likely spent **~$53 billion** intervening on **Thursday** to prop up the yen, per a Bloomberg analysis of central-bank accounts. **The operation is estimated at ~¥8.45 trillion ($52.8B)**, based on a comparison of BOJ accounts released Friday against money brokers' forecasts. Bloomberg's own characterization: ***"would likely be the biggest ever intervention on a single day by Tokyo,"*** and *"the growing scale of intervention shows both the determination and the increasing difficulty for authorities in Japan to peg back speculators betting on the yen."*

**⚠️ Method caveat that must travel with the number: this is a BOJ-current-account *estimate*, not an MOF disclosure.** It is the standard market method for detecting intervention ahead of the monthly figure — but the MOF has not confirmed it and, per SAM's own reporting, the window covering **7/30 does not disclose until ~Aug 31.**

## 2. 🔑 The scale, against SAM's own op history — this is the part the headline doesn't carry

| Date | Size | USD/JPY | Outcome (SAM's column) |
|---|---|---|---|
| Apr 30 | ~¥5.48T ($35B) | 160.70 → 155.55 | **same-day reclaim** |
| May 6 | ~¥4.3T ($28B) | 157.89 → 155.05 | **same-day reclaim** |
| Official aggregate **Apr 28 – May 27** | **¥11,734.9B ($73B)** | — | largest round since 2022 |
| **Jul 30 (this op)** | **~¥8.45T ($52.8B)** | 163.49 → 157.92 low | **see §3** |

⇒ **~1.5× the largest prior single-day operation, and ~72% of the entire month-long Apr-May round spent in a single session.** Bloomberg's "biggest ever single day" is consistent with SAM's own table rather than resting on it.

## 3. 🔴 THE OUTCOME CLAIM IS BACKWARDS — and it matters because SAM's registered base rate points the same wrong way

The circulating framing is *"possibly the biggest one-day intervention in its history, and the yen already back above 160 in less than 24 hours"* — i.e. **a record op that failed immediately.** The observed path:

| When | USD/JPY | Source |
|---|---|---|
| Pre-op Thu 7/30 | **163.49** | SAM |
| Thu 7/30 intraday low | **157.92** | SAM |
| Thu 7/30 NY settle | **159.46** | SAM |
| Fri 7/31 BOJ statement (12:45 JST) | **160.42** | SAM |
| Fri 7/31 11:08 ET | **159.25 (−2.48%)** | HENRY, independent pull |
| **Fri 7/31 close** | **~157.40 (−1.74%)** | own `fetch.py` ⚠ stale-flagged |

**The yen touched 160.42 at the BOJ statement and then strengthened for the rest of Friday, ending BELOW the intervention-day low of 157.92.** So "back above 160" was true for a window around the statement and is **false as of the close and as of when the post was written.** Classic `finding_relayed_level_predates_the_event` — the relayed level is real but predates the state it is being used to describe.

**🔑 Why this is SAM's and not a curiosity: SAM's own Outcome column reads "same-day reclaim" for BOTH prior ops (n=2).** That is a registered base rate, and it is the default a reader fills the empty 7/30 cell with. **The tape refutes it for this op** — no same-day reclaim, and continued yen strength on day two. **A record-size op that is NOT being reclaimed is a different object from a record-size op that failed, and the two imply opposite things about MOF's capacity and about a crowded short.**

⚠️ **Honest limits, stated before anyone marks anything:** my close pull carries fetch's **stale flag** (as-of 2026-08-01) — HENRY's 11:08 ET 159.25 corroborates the *direction* independently, but **SAM should re-pull the settle before writing it into the table.** Two sessions is not a durable outcome. And attribution of Friday's continued strength is **not** established here — the BOJ's hawkish-lean hold and Ueda naming September are live competing causes, and those are SAM's to weigh, not mine.

## 4. Routing note — this is a DELTA, not a re-route

**PROME already routed the ¥8.45T headline to SAM this morning** (`inbox/2026-07-31_from-PROME_boj-data-intervention-estimate-lane-surfaced.md`), explicitly stating *"headline-level — I have NOT read the article"* and flagging *"verify at the BOJ primary before use."* **This adds the three things that packet could not:** (a) **the article's own text**, including Bloomberg's "biggest ever single day" characterization and the ¥8.45T/$52.8B reconciliation; (b) **the scale comparison against SAM's own op table** (1.5× / 72%); (c) **the refutation of the circulating outcome claim**, which is the half that would have propagated wrong. **SAM keeps the action; nothing here re-opens what PROME routed.**

**ZHAO:** bears on the intervention-vs-flows attribution question left open on `SIG-W-20260730-009` (the SK-hynix-repatriation counter-attribution). **HENRY / BOND:** a ~$53B one-day FX operation is a reserve-asset transaction with a UST-sales leg; **nobody has established whether it shows up in the Treasury market, and I am not asserting that it does.**
