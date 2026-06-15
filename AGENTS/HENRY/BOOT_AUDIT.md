# HENRY BOOT-PROCEDURE AUDIT — vs VIOLET / SAM / BRENT

**Date:** 2026-06-15 · **Prompted by:** Will (after this session's 5-session staleness gap + the VIOLET "stale 6/1" re-violation)

## VERDICT
HENRY runs the **leanest, most manual boot in the macro cluster** — a 3-step *read-only* boot (STATUS / LESSONS / MEMORY) with **no boot script, no live-data pull, no predictions-due scan, no catalyst countdown, and no cross-agent surface**. VIOLET, SAM, and BRENT have all moved to an **automated boot kit + symmetric read↔write closeout + NEXUS_BRIEF cross-agent feed**. HENRY's two failures this session both trace directly to these missing boot steps. HENRY has been *named as a target* for the upgrades in three fleet auto-memories and hasn't executed them (parked in MODERNIZATION_PLAN.md, "paused for market work").

## INVENTORY (the gap, at a glance)
| Capability | HENRY | VIOLET | SAM | BRENT |
|---|:--:|:--:|:--:|:--:|
| `scripts/boot.py` (live tape + FRED + catalyst countdown, ~10s) | ❌ | ✅ | ✅ | ✅ |
| Predictions-due scan at boot | ❌ | — | ✅ (step 6, w/ calibration preamble) | ✅ (eyeball OPEN past-timeframe) |
| Catalyst countdown / machine docket (`CATALYSTS.tsv`) | ❌ | ✅ | ✅ | ✅ |
| `NEXUS_BRIEF.md` (cross-agent synthesis feed) | ❌ | ✅ | ✅ | ✅ |
| Live-event EXECUTE-stays-open override | ❌ (boot says "CLOSEOUT every session") | ✅ | ✅ | ✅ |
| Symmetric read↔write boot/closeout framing | partial | ✅ | ✅ | ✅ (explicit pairings) |
| `MAINTENANCE.md` structural-change log | ❌ | ✅ | ✅ | ❌ |
| Internal sub-agents (docket/workbook/trade-doc stewards) | ❌ | — | ✅ (KOYOMI/METSUKE/KURA) | ✅ (FASTOW) |
| Canonical handoff doc | LAST_COMPLETION + MEMORY | SCRATCH | MEMORY | SCRATCH (+ LAST_COMPL) |
| State-claim convention (`[src M/D]` + `STATE [as-of @ level]`) | ✅ **(HENRY-pioneered)** | partial | partial | partial |
| Bespoke domain tool (credit bifurcation monitor) | ✅ | ✅ (vol surface) | ✅ (JGB/CFTC) | ✅ (EIA/storage) |

*HENRY already HAS the raw materials* — `scripts/refresh_status.py`, `scripts/update_data.py`, `scripts/credit_monitor.py` — they're just **not assembled into a boot.py and not invoked as a boot step.**

## BOOT READ-PHASE, SIDE BY SIDE
- **HENRY (3 steps, read-only):** STATUS → LESSONS → MEMORY → *Execute*. No data is pulled, nothing is scanned. Freshness depends entirely on the operator remembering to pull live.
- **SAM (6 steps):** THESIS → STATUS → CALENDAR → TIMELINE → MEMORY → **PREDICTIONS scan (+calibration scoreboard)**, then `boot.py` (live data + countdown).
- **BRENT:** STATUS-led read + `boot.py` (prices+FRED+EIA+countdown) + **eyeball OPEN predictions past timeframe**; boot/closeout declared "one symmetric sequence."
- **VIOLET:** read phase + `boot.py` (vol surface+FRED+countdown) + **live-event override** (EXECUTE stays open through an active regime/catalyst window — don't force closeout mid-event).

## THIS SESSION'S FAILURES → ROOT-CAUSED TO BOOT GAPS
1. **5-session staleness gap** (didn't register that CPI 6/10 + PPI 6/11 had fired and HEN-32 was due). → **No predictions-due scan + no catalyst countdown at boot.** SAM/BRENT both flag a passed-timeframe OPEN prediction at boot; HEN-32 (resolve 6/10) would have surfaced DUE on the first read. A countdown would have shown both prints already passed.
2. **VIOLET "stale 6/1" re-violation** (cited her as stale when she was current to 6/12 — and her update was already in my clone). → **No "one-source-of-truth / stale-marked > carried-forward" discipline overlay at boot/closeout, and no NEXUS_BRIEF cross-feed.** VIOLET & BRENT carry that overlay explicitly; HENRY's is scattered in LESSONS, not enforced in the protocol. Had HENRY read peer NEXUS_BRIEFs (or NEXUS synthesis) at boot, her 6/12 reads would have been in front of me. Prome/ORC had to hand-deliver SAM's + VIOLET's reads this session — exactly the cross-pollination NEXUS_BRIEF automates.

## WHAT HENRY DOES WELL (keep)
- **State-claim convention** (`[src M/D]`, `STATE [as-of @ level]`, STANDING-vs-STATE) — the fleet's best *in-document* anti-staleness discipline; HENRY pioneered it (others could adopt). *Irony: it catches a stale read inside a refresh, but nothing forces the refresh to happen on schedule — that's the boot.py gap.*
- **credit_monitor.py** — genuinely differentiated bifurcation tooling (CCC−BB, fund-flow proxy).
- **LESSONS.md** as a dedicated boot-read file (others fold lessons into MEMORY) — explicit mistake-pattern surface.
- **Cascade methodology** depth (mechanical selling layers, gamma/0DTE feedback).

## RECOMMENDATIONS (priority-ordered)
1. **🔴 Build `scripts/boot.py`** (highest leverage; ~½ session). Assemble the existing scripts into one ~10s boot kit: live tape (refresh_status), FRED credit (credit_monitor --json), **predictions-due scan** (parse PREDICTIONS.tsv for Resolve_Date ≤ today + status OPEN/ACTIVE), and a **catalyst countdown**. Directly prevents failure #1. Pattern proven by SAM/BRENT/VIOLET + auto-memory `[[finding_boot_py_cadence_skip_pattern]]`.
2. **🔴 Adopt `NEXUS_BRIEF.md`** (mandatory-every-session). Without it HENRY is invisible to the NEXUS cross-agent synthesis layer and gets peer reads only when someone hand-delivers them (as happened today). Prevents failure #2's class.
3. **🟠 Add a single-source catalyst docket** (`CATALYSTS.tsv` machine feed + human twin), so a passed/upcoming print can't be silently missed. (SAM/BRENT pattern; auto-memory `[[finding_boot_predictions_scan]]` names HENRY.)
4. **🟠 Add the live-event EXECUTE-override** to the protocol (VIOLET/SAM/BRENT have it; my boot still says "CLOSEOUT every session end," which pulls toward closing out mid-event — auto-memory `[[finding_boot_protocol_live_event_override]]`).
5. **🟡 Promote the discipline overlay into the protocol** (not just LESSONS): "one source of truth per metric; reference the owner's value with `[CONF <agent> M/D]`; stale-marked > carried-forward; re-verify any '[agent] is stale' claim against that agent's file header before repeating it."
6. **🟡 Reconcile the handoff convention** with the fleet. VIOLET/BRENT retired LAST_COMPLETION → SCRATCH (canonical handoff) + NEXUS_BRIEF + MEMORY. Decide: migrate HENRY to that model, or keep LAST_COMPLETION and document why. (Don't drift by default.)

*All of #1-4 are already in MODERNIZATION_PLAN.md / flagged in fleet auto-memories — the gap is execution, not design. PROME owns any fleet-wide rollout; HENRY owns building its own boot.py + NEXUS_BRIEF.*
