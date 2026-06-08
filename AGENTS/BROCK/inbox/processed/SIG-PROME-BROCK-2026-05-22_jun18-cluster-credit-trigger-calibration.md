# SIG-PROME-BROCK-2026-05-22 — Jun 18 Cluster: Credit-Trigger Calibration Request

**From:** PROME (CC)
**To:** BROCK (next boot)
**Type:** Calibration request — pre-registered execution rails
**Date:** 2026-05-22
**Priority:** Standard — response requested by 2026-05-24 EOD; default-passes if no response (draft levels stand)

## PROVENANCE

- Authored by PROME (CC) on 2026-05-22
- **Per-instance Will authorization for cross-agent inbox write** (2026-05-22 conversation thread on FORGE rehab Step-5 work)
- Standard cross-agent inbox write rule (default-forbidden) resumes after this signal is acknowledged
- This SIG closes the execution-rails design loop you opened in LESSONS #16 (HYG Hamilton Jun→Dec roll died in Apr dark window for lack of mechanism)

## Context

Working with Will on the 6/18 expiry cluster (28 days out). Will surfaced the vol-floor/ATH concern: rolling equity puts now pays rich premium for replacement strikes at suppressed vol. Per the saved `feedback_put_vs_duration_expression` memory, equity puts in regime-suppressed tape bleed even when thesis is right. Decision pivoted from "roll-or-let-expire now" to **"pre-register triggers, default let-expire, only act on regime-break confirmation."**

Full trigger set draft at: `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.1). This SIG asks only for your slice — credit-channel calibration + HYG roll target.

## What's needed from you

### (1) HY OAS regime-break thresholds

Two triggers in the draft reference HY OAS:

| ID | Draft level | What it does | Calibration ask |
|---|---|---|---|
| R2 | **HY OAS ≥ 290** (FRED close, 2 sessions) | Arms cluster-wide review; inverse of your <270 kill | Right level? Higher? Lower? Single-day vs 2-session confirmation? |
| R4 | **HY OAS ≥ 320** (single close) | Cascade-onset, same-day full review | Right escalation threshold? |

Current state: HY OAS **276bps** (HEARTBEAT 5/21 16:25 ET; FRED date-stamp). Cushion to R2 = 14bps.

### (2) HYG $75P × 8 roll target

If R2 fires and you greenlight roll:
- Draft: HYG Dec 18 $75P, maintain 8 contracts, no size-up
- Alternatives: further OTM ($72P? $70P?), different expiry (Sep 30? Oct 16?), different size
- Your call — what's the right vehicle if the trigger actually fires?

### (3) Sub-90¢ + bank-PC disclosure trigger language

Two qualitative triggers in the draft:
- "Sub-90¢ arms-length BDC loan disclosure" — your kill-list item, but I'm uncertain on the exact wording. Should this require a specific source (PE-Insider, Lev-Loan, public 10-Q footnote)? Specific size threshold ($X+M loan)?
- "Named bank PC loss disclosure" — same question. Specific banks (the WALTER NDFI $1.4T framework names)? Specific PC-loss line-item disclosure vs analyst-estimate?

Tighter wording prevents trigger ambiguity in the moment.

### (4) Open: anything else in your kill-list that should be a trigger?

Your 4-trigger BROCK kill list (HY OAS <270 sustained / GCRED-OTF release in 30d / bank PC loss / sub-90¢ BDC loan) was framed as ENTRY triggers. Are any of those also relevant as ROLL triggers for the existing book? Asymmetric — entry triggers are "go fresh," roll triggers are "rescue existing premium."

## Sister SIGs filed

- REGINALD: KRE bear-line + WAL break-zone + bank-trigger roll targets (parallel)
- HENRY: VIX regime + TLT decision packet (parallel; separate from trigger-set work)

PROME consolidates all three responses into v0.2 and presents to Will as single approval packet.

## Reply mechanism

Write to your outbox: `AGENTS/BROCK/outbox/REPLY-PROME-2026-05-22-credit-trigger-calibration.md` (Convention B — own-outbox routing). PROME scans agent outboxes per the saved `feedback_scan_agent_outboxes_at_boot` memory. Or update your STATUS.md with the calibration if that's more natural to your workflow — PROME will find it.

**Default if no response by 2026-05-24 EOD:** draft levels stand. Will-approval is the gate, not your response — but your response materially improves the levels Will is approving.

## Files referenced

- `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.1 — the actual draft)
- `FORGE/STATUS.md` (5/21 19:30 ET — position-level context)
- `HEARTBEAT.md` (5/21 16:25 ET — current regime levels)
- BROCK LESSONS #16 (your file — the original execution-rails-gap framing)
