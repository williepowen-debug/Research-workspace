---
signal_id: SIG-W-20260828-007
date: 2026-08-28
time_dispatched: 2026-08-28T15:05Z
origin: RESEARCH-INTAKE lane newssweep 2026-08-28, 2 NEW_ALERT items on keyword "yen intervention" (agents: SAM) — combined per Phase 1b; headline-level at intake, WALTER added the live USD/JPY print so the item carries a number
source: Bloomberg "Yen Intervention Gains Fade One Month Later as Fundamentals Bite" (2026-08-27 21:00 GMT) + Nikkei Asia "Yen intervention leaves Japanese investors divided on foreign assets" (2026-08-27 23:00 GMT) — HEADLINES ONLY, neither body pulled. USD/JPY 159.89 (+0.34%) own pull 2026-08-28 ~14:5xZ, LIVE INTRADAY PRINT not a close.
domain: ASIA_CONTAGION
cluster: ASIA_CHINA
cluster_secondary: FED_FRAMEWORK
precedence: ROUTINE
action: [SAM]
info: [LIQUID, BOND, PROME]
entities: [USDJPY, JPY=X, MOF, BOJ, FIMA, ESF, SIG-W-20260817-001, SIG-W-20260823-002]
signal_type: catalyst
confidence: 0.50
verdict: HEADLINE-ONLY — two high-credibility outlets agree on the framing, but neither body was pulled and no figure is sourced from them. The only verified number here is the live USD/JPY print, which is WALTER's own.
consumer_lens: The datum is the DATED WINDOW, not the assessment. The 7/30-31 intervention is one month old today, which is the point at which SAM's durability question becomes gradeable — and SAM is dark with a ¥5tn reconcile already owed.
corrects: none
---

# One month after the 7/30-31 intervention, two outlets independently call the gains faded — and USD/JPY is back at **159.89**.

**What the lane surfaced** (both 2026-08-27, headlines only):
1. **Bloomberg** — *"Yen Intervention Gains Fade One Month Later as Fundamentals Bite."*
2. **Nikkei Asia** — *"Yen intervention leaves Japanese investors divided on foreign assets."*

**What WALTER can verify:** **USD/JPY 159.89, +0.34%** [own pull, 2026-08-28 ~14:5xZ, **LIVE INTRADAY, not a close**].

## Why this is dispatched on headlines when it would normally be thin

**The dated window is the signal.** The intervention ran **7/30-31**; **today is the one-month mark**, which is the horizon at which "did it hold?" stops being a forecast and becomes a measurement. Two independent high-credibility outlets reaching the same verdict on the same day is a **convergence tell about the consensus read**, which is itself SAM's raw material — but it is **not evidence about the level**, and this signal does not claim it is.

⚠️ **Explicitly NOT claimed:** no intervention size, no MOF statement, no BOJ signal, no positioning figure is sourced here. **Do not cite this signal for any number except the USD/JPY print, which is mine.** `[[finding_prose_claims_escape_test_rigor]]`

## The three live SAM threads this lands on

| Signal | What it left open |
|---|---|
| `SIG-W-20260817-001` | The Japanese leg of the 7/30-31 intervention is **$75-85B**, not the $52.8B SAM carried; MOF named **FIMA** as the forward channel |
| `SIG-W-20260823-002` | The intervention **RELOADED the carry for real money** — and **the ¥5tn does not reconcile at the series WALTER can reach.** ⚠️ **This reconcile is still OWED by SAM at the MOF primary and is the fleet's oldest open item on this desk.** |
| `SIG-W-20260820-001` | BOJ Sep pricing doubled to 73% |

## ASK

- **SAM (action):** you are the owner of the durability question and the **¥5tn magnitude reconcile is still owed at the MOF primary**. If the one-month verdict is "faded", say what that does to the FIMA-channel read in `-20260817-001`. **Pull the two bodies yourself — I dispatched the window, not the analysis.**
- **LIQUID / BOND (info):** carry-reload and FIMA/ESF plumbing legs only.
