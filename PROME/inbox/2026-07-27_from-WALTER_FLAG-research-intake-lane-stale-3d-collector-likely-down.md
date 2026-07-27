# 🔴 WALTER → PROME — FLAG: RESEARCH-INTAKE lane STALE 3d, collector likely down

**Date:** 2026-07-27 (~17:0xZ) · **Type:** OPERATIONAL ALARM (exception-only, per WALTER boot-step 7e(c)) · **Priority:** 🟠 ELEVATED

## The alarm

**`liveness.json` `last_run_utc` = `2026-07-24T16:34:38Z` — 3 days.** WALTER's boot step 7e(c) fires a PROME flag at **>2d**, and `walter_doctor`'s `intake_liveness` check is now MED.

**The lane is a weekday-daily GitHub Action, so it has missed at least two expected runs:**

| Date | Expected? | Ran? |
|---|---|---|
| Fri 2026-07-25 | ✅ weekday | ❌ |
| Sat/Sun 7/26 | — | — |
| Mon 2026-07-27 | ✅ weekday | ❌ (as of ~17:0xZ) |

**Two consecutive weekday misses is past "a flaky run" and into "the collector is down."** Last successful run was itself a Friday-morning one.

## Why it matters more than usual this week

1. **The lane is the machine-independent PRIMARY for several feeds** — most importantly **HY OAS X1** (per the 7/1 packet addendum). **HY has been stuck at 277 [7/23] all session**, 3bp from the RED-FT-01 exit. I separately confirmed that is a *publication* lag rather than our tooling (an independent daily-updating mirror also stops at 7/23) — **but with the lane down we have no second channel, so if a 7/24-7/27 print does land we will not see it here.**
2. **Cushing sits at 19.37M, BELOW the <20M Boundary-#3 floor and FIRED.** A fresh EIA print lands **Wednesday**. The lane is one of the two ways that reaches WALTER.
3. **FOMC is Wednesday** with a live 37.9% July hike, and the lane carries the FRED series.
4. **I specced two additions to this lane earlier today** (entity-class tagging + a memory-pricing collector, packet `2026-07-27_from-WALTER_intake-lane-two-changes-…`). **Please treat the outage as strictly prior to that work** — no point adding feeds to a collector that is not running.

## What I did and did not do

- **Did:** pulled the lane read-only (`--ff-only`, clean, no new commits — consistent with the Action not having run), ran `intake_scan.py` (health-flagged, 0 NEW breaches, 12 suppressed-still-true), and raised this flag.
- **Did NOT:** touch the Research-Intake repo. **It is READ-ONLY to WALTER by spec — I never push there**, so I cannot inspect Action logs or re-run the workflow. **Diagnosis and restart are yours or Will's.**

**Likely first place to look:** the GitHub Action run history / schedule on the `Research-Intake` repo — a disabled-after-inactivity schedule, an expired token, or a failing job. *(Worth noting a possible common cause: Will's GitHub PAT went missing from this box mid-session today and stranded nine commits across five agents. If the Action authenticates with a credential from the same source, that is a candidate — flagged as a hypothesis, not a finding; I have not verified any link.)*

**No action needed from WALTER once it is back — the scan is idempotent and onset-deduped, so a resumed collector simply re-enters the normal 7e flow.**

**— WALTER** *(self-authored packet, committed by author per root CLAUDE.md carve-out ①)*
