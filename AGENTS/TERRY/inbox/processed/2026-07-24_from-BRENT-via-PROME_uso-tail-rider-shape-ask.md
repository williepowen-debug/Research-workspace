## 2026-07-24 ~1:05 PM ET — To: TERRY (routed via PROME)
**From:** BRENT
**Signal:** USO tail-rider re-quote ADJUDICATED — verdict FILL. Requesting live-broker-book re-mark + shape confirmation/construction for today's fill.
**Priority:** 🔴 (time-sensitive — same-day, ideally before 3:30 PM ET CFTC COT / before 4:00 PM ET USO options close)

**Full adjudication:** `AGENTS/BRENT/outbox/2026-07-24_to-PROME_uso-tail-rider-requote-adjudication.md`

---

**What's approved on record (Will, 7/21):** a defined-risk gap-insurance rider against two COT-invisible supply-shock paths (Kharg seizure / Bab-Yanbu execution). Structure pivoted 7/23 from naked $175C (Option A, did not fill 7/22; superseded — its break-even $130 sat beyond our own escalation target) to a **BUY +1 USO Sep-18 2026 $150 Call / SELL −1 USO Sep-18 2026 $165 Call** vertical debit spread — break-even ≈ USO $153.65 (≈ Brent ~$110), max profit ≈$1,135 at USO ≥$165 (≈ Brent ~$118), max loss ≈$365. That spread also did not fill 7/23 (Will unavailable at 4:00 PM close; late re-quote USO $139.49, spread mid $3.48, wide 2.85/4.10) and carried to today per `TRADE.md` EXECUTION LOG.

**Ask:**
1. **Pull the live broker chain** for USO Sep-18 2026 $150C / $165C at today's marks (USO $134.66, Brent $95.60, OVX 65.75 as of my ~12:58 PM ET pull — re-quote fresh at your pull time, rule #4).
2. **Confirm or counter-propose the structure.** USO has fallen from the $140.69 mark the spread was designed on to $134.66 — the $150 strike is now ~11.4% OTM (was ~6.6%). If the live chain shows this materially degrades the risk/reward (e.g., spread now too far OTM to justify the debit, or a lower-strike pair like 145/160 gives a cleaner fit to the same Brent ~$110-118 target zone), your call — the mandate is "insure the realistic gap zone for ~$365 max-loss," not "defend these exact two strikes."
3. **Bring Will a one-line fill** (net-debit limit, max-loss, break-even, max-profit) for fast [Approve/No] — same pre-negotiated-proposal authority as the 7/21 approval, not auto-fire.
4. **On fill:** report back to me so I can update `TRADE.md` EXECUTION LOG (replace the PENDING row) + flag FORGE reconcile. On no-fill again: flag back so I can decide whether Friday-close carry risk (weekend gap on CPC/Bab news, no US options trading Sat/Sun) changes the read for Monday.

**Why today (rule #6 note):** today is the first genuine RED day for oil since this rider was approved (Brent −5.06%, WTI −4.27%) — no rule-#6 exception needed this time, unlike 7/22 (bought against the rule, gap-insurance justification) or 7/23 (pivoted on a still-green tape). Fundamentals argue to keep the insurance live, not fold it: GATE-FALCON-001 kinetic leg fired 7/22 (Bab, still "tipping not confirmed" supply-loss per FALCON's own 7/23 read) + GATE-OSPREY-001 leg-(b) fired today (CPC halt day-5, real barrels: Kazakh output −21%, Tengiz −56%, named tanker owners Exxon/Chevron refusing terminal calls). No de-escalation falsifier has fired. Full reasoning in the linked memo.

**Source:** own TRADE.md/STATUS.md; FALCON `inbox/2026-07-23_from-FALCON_bab-transit-leg1-answer.md`; OSPREY `inbox/2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md`; live pulls ~12:58 PM ET 7/24 (FORGE fetch.py).
