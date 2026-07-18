# FALCON — Iraq/PMF Backlash Discriminator (CONFIRM-D #5) — Sourcing Review
**Built:** 2026-07-18 ~20:00 ET (Sat-eve wave #2, Will-selected) · **Owner:** FALCON · **Consumers:** PROME (D-confirm gate), HAWK (synthesis), BRENT (Basra/Iraq oil-infra tail)
**Trigger:** SCRATCH 7/17 item 4 — `baghdad_watch.py` embassy feed **34d silent** while the embassy is on **ordered departure**; I was reporting "QUIET" as if it were evidence, when it may be measuring a **dead channel, not the theater.**

> ### 🎯 VERDICT: the concern was RIGHT — the embassy feed was a degraded false-quiet channel — and an independent route both REPLACES it AND changes the read from "QUIET" to **"genuinely unfired, but ACTIVE standoff underneath."** Discriminator kept at meaningful weight (NOT downgraded to noise); the embassy feed is DEMOTED to a backstop whose *silence is not evidence.*

---

## 1. The problem, confirmed

`scripts/baghdad_watch.py` monitors the **US Embassy Baghdad alert feed** for the CONFIRM-D #5 discriminator (Iraq/PMF-Kataib Hezbollah backlash triggered by US strikes on Iran). The feed has been **silent 34 days** and the embassy is on **ordered departure** — so its silence is **structurally uninformative** (a drawdown artifact, not a quiet theater). Reporting "QUIET" off it was measuring the channel. **Confirmed a real epistemic hole**, not a hypothetical one: everything in §3 below was invisible to the embassy feed.

## 2. The 2nd sourcing route (durable, free, web-readable) — REPLACES the embassy feed as primary

| Rank | Source | What it covers | Cadence / access |
|---|---|---|---|
| **PRIMARY** | **Critical Threats Project (CTP/ISW) "Iran Update"** — `criticalthreats.org/analysis/iran-update-<date>` | Daily section on the **Islamic Resistance in Iraq / Kataib Hezbollah / PMF**: attacks, disarmament standoff, militia posture, threats to Iraqi oil infra | **Daily**, free, web-readable. Gold-standard for Iraqi-militia tracking. |
| **CORROB 1** | **Shafaq News** (shafaq.com/en) | Iraqi outlet, English — militia statements, attacks, security incidents | Continuous, free |
| **CORROB 2** | **PressTV / militia-aligned channels** | Militia *messaging/intent* (e.g. "ready to support Iran if war erupts", 7/14) — read as intent-signal, weight for incentive per `[[feedback_trump_rhetoric_tape_not_info]]` | Continuous |
| **BACKSTOP (DEMOTED)** | `baghdad_watch.py` embassy feed | An embassy alert, IF issued, is still signal (a real evacuation-grade event). **But its SILENCE is NOT evidence** while on ordered departure. | Keep running; never cite "QUIET" as a datum. |

**Operational rule going forward:** grade the discriminator off **CTP Iran Update (primary) + Shafaq (corrob)**, cross-check the embassy backstop only for *positive* alerts. Stop reporting embassy silence as "QUIET."

## 3. What the independent route shows RIGHT NOW [as-of CTP Iran Update July 15, 2026]

**CONFIRM-D #5 = UNFIRED — but genuinely unfired, not channel-artifact-unfired.** The independent route is populated (unlike the dead embassy feed) and shows:

- **NO new kinetic attacks** by Iraqi militias / Islamic Resistance in Iraq on US forces, bases, the Green Zone, or Basra oil infra on 7/14–15 — **despite six US strike nights on Iran.** (The "600+ attacks" figure Hegseth cited 7/14 is **historical/war-cumulative**, not fresh.)
- **Militias in a CONDITIONAL / rhetorical / deterred posture**, not kinetic: Kataib Hezbollah "**ready to support Iran IF war erupts**" (PressTV 7/14) and "**will attack US bases IF Washington joins the conflict**" (Shafaq) — i.e. they do **not** yet treat the current US strike campaign as the trigger, or are being restrained.
- **Active disarmament STANDOFF** is the real dynamic: Hegseth (7/14) demanded Iraq disarm the Iranian-backed militias; **Kataib Hezbollah, Harakat al-Nujaba, Kataib Sayyid al-Shuhada REFUSE** (conditioned on US withdrawal). A parallel **US-Iraq investment-for-disarmament deal** (curb Iranian influence, remove militia-aligned officials) is the carrot. Militias suspect it precedes a US "grand plan" to topple Tehran (7/15).
- **NO direct threat to Basra / southern oil infrastructure** in-window.

**Honest read:** the Iraqi-militia front is **ACTIVE but restrained/deterred** — a standoff, not a backlash. That is a *richer and more decision-relevant* signal than the embassy feed's false "QUIET": it says the modal path so far is **militia restraint (deal-driven and/or deterrence-driven) despite maximal provocation next door**, which *reinforces* the FAL-01 / D=65 "calibrated escalation, physical gates unfired" read — the Iraq gate is one of the four physical D→75 gates, and it is unfired for a *reason I can now see*, not because I was blind.

## 4. Gradable fire tells for the 2nd route (what flips CONFIRM-D #5)

Fires (→ D toward 75 on the Iraq rung) on **any** of, live-dated via CTP/Shafaq:
1. A **claimed/confirmed kinetic attack** by the Islamic Resistance in Iraq / Kataib Hezbollah on US forces, bases, or the Green Zone, **attributed to the current strike campaign** (not war-cumulative history).
2. A **PMF general-mobilization order** or a formal declaration of joining the war.
3. An **attack or credible threat on Basra / southern oil infrastructure** (this also intersects BRENT's Iraq oil tail and the export-terminal trap register — hand off).
4. **Collapse of the US-Iraq disarmament deal into open US–militia confrontation** on Iraqi soil.

De-escalation-relevant (the standoff resolving the *other* way): the disarmament deal **holds / advances** → militia restraint durable → Iraq gate stays cold.

## 5. Disposition
- **Discriminator RETAINED at meaningful weight** (not downgraded to noise) — because an independent route gives it real signal.
- **Sourcing PRIMARY switched** embassy-feed → CTP Iran Update + Shafaq; embassy `baghdad_watch.py` demoted to positive-alert backstop, **silence ≠ evidence.**
- **Current state:** UNFIRED, genuinely restrained; **watch item = the disarmament standoff**, not embassy alerts.
- **Boot integration (deferred to Monday):** replace/augment boot step 5b so the discriminator is read off CTP, not the dead feed. Left as a next-session item — no boot-doc edit tonight.
