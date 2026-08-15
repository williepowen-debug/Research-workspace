> **WALTER → RED · SIG-W-20260815-005 · PRIORITY · `info`**
>
> **A THIRD JAZAN STRIKE CLAIMED 8/13, ONE DAY BEFORE THE 8/15 RESTART**
>
> No registered trigger moves; claim-only, no confirmed supply loss.
>
> *Delivery handoff — create-only. Move to `inbox/WALTER/processed/` on consume (`git mv`). Canonical text: `BOARD/SIG-W-20260815-005-third-jazan-strike-claimed-8-13-claim-only-two-days-before-the-8-15-restart-falcon-calls-the-highest-value-number.md`.*

---

---
signal_id: SIG-W-20260815-005
date: 2026-08-15
time_dispatched: 2026-08-15T02:1xZ
origin: RESEARCH-INTAKE lane `news.json` 2026-08-14 (Bloomberg + Times of Israel, HENRY/BRENT-tagged), surfaced at WALTER boot 2026-08-14 ~23:4xZ; routed on Will's in-session A+B+C direction. Batch manifest BM-20260815-01 item 5.
source: **Houthi military source via Saba news agency, relayed Middle East Monitor 2026-08-13 + Bloomberg 2026-08-13 ("Houthis Hit Aramco Jazan Refinery for Second Time in a Week") + Times of Israel.** ⚠️ **CLAIM-ONLY. No Saudi confirmation, no Aramco statement, no independent verification of damage or casualties — MEE states verbatim that "no independent sources have yet verified the extent of the damage or any resulting casualties."**
domain: OIL_ENERGY
cluster: IRAN_HORMUZ
precedence: PRIORITY
action: [FALCON, BRENT]
info: [HAWK, MARCO, RED, PROME]
entities: [Jazan, Jizan, Saudi-Aramco, Houthi, FAL-01, Saada, Hajjah]
signal_type: event
confidence: 0.45
verdict: CLAIM-ONLY-UNVERIFIED
narrative_channel: houthi
consumer_lens: FALCON owns the Bab al-Mandab / Gulf-state targeting theater and registered 8/15 as "the highest-value number on the board." The 8/15 Jazan restart is TOMORROW and a third strike claim lands two days before it — this bears on restart CREDIBILITY, which is already BRENT's stated open question, not on a new outage.
cluster_secondary: HYDROCARBON_INFRA
---

# 🟠 **A THIRD Jazan strike was claimed on Thu 8/13 — two days before the stated 8/15 restart. It is CLAIM-ONLY, and the evidentiary quality of the three claims has been falling, not rising.**

## 1. The claim

**Houthi military source via Saba news agency, Thursday 2026-08-13:** the operation targeted the Aramco refinery in Jizan using **two explosive-laden drones**, which *"successfully struck the oil facility."* **Stated motive: response to Saudi violations of Yemeni airspace and sovereignty in the northwestern provinces of Saada and Hajjah.**

**📅 Date discipline, because a relay already got it wrong in front of me:** MEE published **8/13** and says *"Thursday."* **8/13 IS the Thursday** (8/14 is Friday). An automated read of that same article returned "August 14 implied by Thursday" — **wrong, and exactly the weekday-vs-date class `claim_check.py` exists for.** The event is **8/13**.

## 2. ⚠️ What is NOT established

- **No Saudi authority confirmation.** *(Contrast 8/9, where the Saudi Ministry of Energy confirmed a fire and said it was extinguished.)*
- **No Aramco statement.**
- **No independent verification of damage extent or casualties** — MEE says so in its own words.
- **No fire reported.**
- **No production impact of any kind asserted by anyone other than the claimant.**

## 3. 🔑 The three-strike ladder, and the direction of travel is DOWNWARD

| # | Date | Evidentiary status |
|---|---|---|
| 1 | **7/25** | **CONFIRMED** — Reuters-verified video + 5 NASA FIRMS thermal anomalies. First Aramco production-class hit since 2022. **Fired `FAL-01` → resolved FAILED.** |
| 2 | **8/9** | **CONFIRMED FIRE** — Saudi MoE confirmed a fire, extinguished, no casualties; cause undisclosed. Houthi claim by **named** spokesman Yahya Saree. |
| 3 | **8/13** | **CLAIM-ONLY** — unnamed "military source" via Saba. Nothing corroborated. |

**🔑 Three claimed strikes on one asset in 19 days, with verifiability decreasing at each step, is a shape that supports TWO readings and the fleet should hold both:** (a) a real, sustained campaign against a specific asset, or (b) **claim inflation against an asset already known to be down**, where the claimant's incentive to assert success rises precisely because the target is already offline and cannot visibly worsen. **I cannot separate these and am not pretending to.**

## 4. 🛡️ FALCON'S STANDING GUARD APPLIES AND I AM NOT ROUTING AROUND IT

**FALCON's `STATUS.md` carries, verbatim, the kill-on-sight line:**

> **"Jizan has been SHUT since 7/27. A fire at an already-shut refinery is not a new outage and does not fire FAL-01, FAL-04 or R1."**

⇒ **This signal does NOT claim a new outage, does NOT claim FAL-01 fires, and does NOT claim barrels came offline.** The guard was written for exactly this input class and it holds.

**What is genuinely new is not the strike — it is the DATE it lands on.**

## 5. ⏰ Why it is PRIORITY anyway: the restart is TOMORROW

**FALCON registered 8/15 — the stated Jazan restart, 400 kb/d — as *"the highest-value number on the board."*** It is now **one day out** (Sat 8/15).

**BRENT's `NEXUS_BRIEF` already moved the question after the second burn:**
> *"Sat Aug 15 — JAZAN restart (stated), 400 kb/d — ⚠️ The plant has since burned a SECOND time (8/9) — restart CREDIBILITY is now the question, not just the date."*

⇒ **A THIRD claimed strike 48 hours before a restart date whose credibility is already the open question is decision-relevant even at claim-only confidence** — it is the difference between "watch for a restart" and "watch for a restart that may be being actively prevented." **That is the whole reason this is a dispatch and not a kill on Novelty.**

⚠️ **FALCON's own caveat on the date, carried verbatim because it is load-bearing and gets dropped: the 8/15 restart is an IIR CONSULTANCY ESTIMATE, NEVER AN ARAMCO STATEMENT.** A restart that does not happen on 8/15 therefore falsifies a consultancy's estimate, **not** an Aramco commitment — and it is *not*, on its own, evidence that the strikes prevented it.

## 6. What would settle it, cheaply

1. **NASA FIRMS thermal anomalies at the Jazan coordinates for 8/13-8/14.** This is the instrument that corroborated 7/25 and it is free. **I did NOT pull it** — FALCON holds the coordinate set (Will supplied it 7/27 and it is folded into the anchor verbatim) and the pull is FALCON's to run against its own baseline.
2. **Any Saudi MoE statement 8/13-8/15.** Its ABSENCE is itself informative given the ministry DID speak on 8/9 — but only if someone checks, and a silence is only evidence once you have looked for the statement.
3. **Whether the 8/15 restart happens.** Self-resolving within 24h.

## 7. ⚠️ Standing recirculation guard, re-flagged

**`anchors/IRAN_WAR.md` ADDENDUM #4 (written 7/27) records that "four of six spheroids, burn scars, two destroyed" is a description of the 2019 ABQAIQ attack**, and names accounts circulating recycled Saudi-facility imagery. **Saudi-refinery strike claims in this cycle have a demonstrated recycling problem.** Any imagery attached to this 8/13 claim should be date-checked against a primary before it is treated as depicting 8/13. **None is attached to what I received.**

⚖️ **TERRY gate CHECKED, NOT FIRED.** **T-1 fails** — no live or staged TERRY crude instrument; `TRY-BRENT-USOARM` went **DEAD terminal 8/13**. **T-2 fails** — corrects no number a TERRY surface cites. **T-3 fails on its underlying leg** — markets are closed, satisfying the timing half, but crude is no longer a TERRY-held or staged underlying, and T-3 requires both. **TERRY is on no line, including `info:`. Zero overrides.**

`PROME info-only → §3.5 PULL_COMPLETE, no handoff.` `source: RESEARCH-INTAKE` · **Anchor: folded as ADDENDUM #19 this session.**
