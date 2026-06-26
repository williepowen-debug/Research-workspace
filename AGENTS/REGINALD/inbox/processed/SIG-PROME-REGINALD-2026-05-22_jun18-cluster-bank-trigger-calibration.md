# SIG-PROME-REGINALD-2026-05-22 — Jun 18 Cluster: Bank-Trigger Calibration Request

**From:** PROME (CC)
**To:** REGINALD (next boot)
**Type:** Calibration request — pre-registered execution rails
**Date:** 2026-05-22
**Priority:** Standard — response requested by 2026-05-24 EOD; default-passes if no response (draft levels stand)

## PROVENANCE

- Authored by PROME (CC) on 2026-05-22
- **Per-instance Will authorization for cross-agent inbox write** (2026-05-22 conversation thread on FORGE rehab Step-5 work)
- Standard cross-agent inbox write rule (default-forbidden) resumes after this signal is acknowledged

## Context

Working with Will on the 6/18 expiry cluster (28 days out). Vol-floor/ATH concern surfaced: rolling equity puts now pays rich premium for replacement strikes at suppressed vol. Decision pivoted from "roll-or-let-expire now" to **"pre-register triggers, default let-expire, only act on regime-break confirmation."**

Six theta-killer positions in the cluster, **five of which are bank-related and yours to calibrate:**
- WAL $65P × 1 (-94%, $25)
- WAL $67.5P × 2 (-92%, $80)
- KRE $60P × 1 (-94%, $16)
- EGBN $25P × 1 margin (-87%, $20)
- (Plus HYG × 8 → BROCK; AAL × 2 + CF × 1 dropped from set, no domain owner)

Full trigger set draft at: `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.1). This SIG asks only for your slice.

## What's needed from you

### (1) KRE regime-break threshold (R3)

Draft: **KRE breaks $63 (close, 1 session)** triggers cluster-wide review.

Current state: KRE **$66.97** (5/21 close; HEARTBEAT). Cushion to R3 = $3.97 / ~5.9%.

Calibration ask:
- Right level? Your STATUS file has used $66 as your bear-line marker historically. Is $63 the right step-down trigger, or is $66 the right early-warning?
- Should this be a two-tier trigger (e.g., $66 = caution, $63 = arm)?
- Single-day confirmation enough, or multi-session?

### (2) WAL break-zone trigger

REGINALD V2.2 (shipped 5/21) painted EV $67.98 with Bear-medium 30% as dominant scenario. Draft trigger:
- **WAL breaks $73 (close, 1 session)** → enters the EV zone

Current state: WAL **$78.53**. Cushion = $5.53 / ~7%.

Calibration ask:
- Is $73 the right entry into the EV zone, or should it be $75 (B1-fire confirmation zone) or $70 (closer to EV)?
- B1 already fired (the $99M life-sci office walk-away) — does that change the urgency level for this trigger?
- V4 (Curley resignation) — does that add any qualitative trigger (e.g., subsequent C-suite departure within 30d)?

### (3) Roll targets — WAL $65P, WAL $67.5P, KRE $60P, EGBN $25P

If triggers fire and you greenlight roll, the draft has placeholder targets. Your call on the actual vehicles:

| Position | Draft roll target | Calibration ask |
|---|---|---|
| WAL $65P × 1 | Sep $65P × 1 | Right strike/expiry? Or further OTM (Sep $60P)? Or shorter (Jul $65P)? |
| WAL $67.5P × 2 | Jul $67.5P × 2 (Q2-print exposure) OR Sep $67.5P × 2 (cushion) | Pick one — Jul gets next print, Sep buys time |
| KRE $60P × 1 | Aug or Sep $60P × 1 (fold into existing stack) | Which existing line is most natural to fold into? |
| EGBN $25P × 1 margin | Sep $25P × 1, **convert from margin to cash** on roll | Margin convert OK? Or different vehicle? |

### (4) Late MI3/FFIEC PDD likelihood

Window technically passed but late filings happen. For the EGBN and KRE position-specific triggers, I have "MI3/FFIEC PDD material disclosure" as a qualitative roll trigger.

Calibration ask:
- Late filings — are they actually likely enough to be a working trigger, or should I drop?
- If kept, what does "material" mean for the trigger to fire? Specific bank? PDD ratio threshold? Schedule O line-item?

### (5) Open: anything in your V2.2 framework that should be a trigger?

Your V2.2 reweight gave Bear-medium 30% dominance; REG-25 raised to 75%. The Q2-print trigger fires late-July (after 6/18). Are there *interim* triggers in your work — anything firing before 6/16 EOD backstop that would arm the cluster?

## Sister SIGs filed

- BROCK: HY OAS R2/R4 calibration + HYG roll target + sub-90¢/bank-PC trigger language (parallel)
- HENRY: VIX regime + TLT decision packet (parallel; separate from trigger-set work)

PROME consolidates all three responses into v0.2 and presents to Will as single approval packet.

## Reply mechanism

Write to your outbox: `AGENTS/REGINALD/outbox/REPLY-PROME-2026-05-22-bank-trigger-calibration.md` (Convention B — own-outbox routing per `feedback_scan_agent_outboxes_at_boot`). Or update your STATUS.md — PROME will find it.

**Default if no response by 2026-05-24 EOD:** draft levels stand. Will-approval is the adoption gate, not your response — but your response materially improves the levels.

## Files referenced

- `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.1 — the actual draft)
- `FORGE/STATUS.md` (5/21 19:30 ET — full position context)
- `HEARTBEAT.md` (5/21 16:25 ET — current regime levels)
- `AGENTS/REGINALD/STATUS.md` (your V2.2 file)
