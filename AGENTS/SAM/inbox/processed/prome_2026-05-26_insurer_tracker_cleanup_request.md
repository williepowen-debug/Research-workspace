# PROME → SAM: Insurer Tracker Cleanup / Channel 1 Rule Fix

**Date:** 2026-05-26
**From:** Prome / Will discussion
**Priority:** High, but not emergency
**Target file:** `AGENTS/SAM/insurers/TRACKER.md`

## Why this matters

Will and Prome walked through the SAM domain to understand Channel 1. The insurer tracker is still useful as the best mechanics map for JGB-loss / ESR / lifer behavior, but parts of it are stale after the May 26 Nippon + Meiji prints.

Main finding: **ESR level alone is no longer a valid alert trigger. Mechanism matters.** Nippon Life printed below 200% but did NOT validate forced repatriation — the driver was Resolution Life M&A capital action, while foreign securities remained in unrealized gain.

## Current read

The tracker is still relevant for:

1. **JGB losses are real**
   - Nippon: JGB unrealized loss worsened to `-¥5.73T`.
   - Meiji Yasuda: JGB unrealized loss worsened to `-¥2.16T`.

2. **J-ICS / lifer long-end abandonment remains important**
   - Super-long JGB avoidance can itself drive long-end instability.
   - This domestic-curve mechanism is separate from forced UST/foreign-bond selling.

3. **Channel 1 has changed shape**
   - Insurers are not cleanly cutting foreign bonds in aggregate.
   - Better framing: rotation within the book — unhedged → hedged, repacks, avoiding super-long JGB duration.
   - Cross-border forced-repatriation leg is deferred, not dead.

## Stale / needs correction

### 1. Fix alert / routing rules

Current tracker rule says roughly:

> ANY insurer ESR <200% → signal LIQUID + PROME 🔴

This is now too crude and should be revised.

Suggested replacement logic:

| Condition | Signal |
|---|---|
| ESR <200% **via market losses / forced asset sales / foreign-book stress** | 🔴 LIQUID + PROME |
| ESR <200% via **M&A/capital action/sub-debt**, with foreign book still in unrealized gain | 🟡 counter-thesis / mechanism-not-fired note |
| ESR 200-220% with deteriorating JGB marks but foreign book intact | 🟠 watch; confirms squeeze but not forced repatriation |
| Foreign bond / UST reduction target explicitly announced | 🔴 LIQUID + PROME |
| J-ICS cited as reason to avoid 30Y/40Y JGBs | 🟠 confirms domestic-curve mechanism |

### 2. Refresh “What we’re waiting for”

This section still says FY2026 plans and ESR disclosures are pending. Update to current state:

- FY2026 plans: resolved / zero clean foreign-bond cuts; rotation-within confirmed.
- ESR disclosures: Dai-ichi, Nippon, Meiji done; Sumitomo is immediate remaining Big 3 mutual pattern-confirmation test; late-June mid-tier names remain secondary.

### 3. Refresh Key Dates

Stale entries:

- May 22 CPI listed as upcoming. It resolved soft; June BOJ pricing moved from ~74% to 55-65%.
- May 26 Nippon/Meiji resolved, already mostly updated.
- May 27 Sumitomo remains live.

### 4. Down-weight older survey evidence

The Oct 2025 “50% planned overseas debt cuts” survey should be retained as context but explicitly subordinated to the Apr/May 2026 actual disclosures, which showed rotation-within rather than clean cuts.

### 5. Reword Channel 1 status banner

Recommended language:

> Channel 1 is downgraded, not dead. JGB-loss / ESR pressure is real, and J-ICS long-end abandonment remains active. But the cross-border forced-repatriation mechanism did not fire in Nippon/Meiji: foreign books were in unrealized gain and ESR pressure was absorbed via capital actions. Future alerts must distinguish **threshold breach** from **forced-selling mechanism**.

## Requested output

Please update `insurers/TRACKER.md` accordingly and, if the changes alter thesis framing, make any necessary pointer update in:

- `STATUS.md` if current Channel 1 status changes
- `thesis/THESIS.md` only if this becomes v1.5 after Sumitomo
- `thesis/CHANGELOG.md` if an analytical version change is made
- `MAINTENANCE.md` if this is treated as structural/doc cleanup rather than thesis update

## Completion note requested

When done, please leave a short note in SAM completion/handoff style answering:

1. What changed?
2. Did Sumitomo need to be checked first, or can this cleanup happen now?
3. Does Channel 1 remain downgraded, reactivated, or pending?
