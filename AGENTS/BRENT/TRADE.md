# BRENT TRADE.md — domain trade surface

**Updated:** 2026-06-29 Mon PM ET | **THESIS v5.0 (asymmetry flipped UPSIDE-CONVEX)** | **LIVE surface** (not frozen — keep current at every closeout or it rots).
**Rule:** calls on red days, puts on green days. **Trade proposals → Will [Approve]; never execute without it.**
**Ownership / one-source-of-truth:** THIS file owns *position status* + *trade plans*. **STATUS** owns live market data (prices/storage/levels). **THESIS** owns the conviction. Do NOT restate live prices here — reference STATUS. **No cost-basis / P/L from state files** — ask Will (`[[feedback_position_cost_basis_not_authoritative]]`).

---

## CURRENT STANCE (v5.0)

**Direction-NEUTRAL near-term; risk-skew ASYMMETRIC TO THE UPSIDE medium-term.** Downside capped (record-low inventories + SPR-refill bid → gentle-normalization floor ~high-$70s/$80); upside tail fat AND rising (reopening weeks-to-months, rising Russian crude fuses, spent buffers, near-record spec short = squeeze fuel). **Phase-2-short bias RETIRED; no flat-price length EITHER WAY.** Forward expression = **defined-risk long-convexity, deploy-on-trigger** (below). **⚠️ SKEW flip, not a direction call — we are NOT calling oil up; the convexity is up, not the forecast.**

---

## POSITIONS (live)

| Position | Type | Status | Note |
|----------|------|--------|------|
| **XLE $65C Sep 30** | Call (2) | **LAPSE** | Deep-OTM (~20% to strike), ~$0 salvage. Its narrow re-escalation-snap path fired Jun 27-28 (kinetic test) and did NOT pay. Now the deep-OTM **backstop** to the convex arm below — do NOT defend/add; re-arm only on a DURABLE ceasefire collapse. |
| **CF $130C Jun 18** | Call (1) | **EXPIRED WORTHLESS (Jun 18)** | Closed; record only. |

**No flat-price length (no new longs, no fresh shorts).** A fresh short fights both the priced-in reopening and the new upside skew; flat-price longs are the wrong vehicle for a tail (theta). Express via convexity only.

---

## ⚑ ACTIVE TRADE PLAN — v5.0 CONVEX ARM (deploy-on-trigger)

*This is the standing pre-registration for the upside-convex expression (the rolling successor to the resolved single-event `PREREG_20260628_CME_reopen.md`). Written before the trigger so execution is pre-thought, not scrambled.*

**Status:** 🟡 **ARMED, NOT deployed. No capital committed today.**
**Thesis (one-liner):** the squeeze never physically resolved + the buffer is nearly spent → the dominant medium-term risk is a **Phase-1 RE-SQUEEZE (up)**, not Phase-2 (down); express the rising, no-cushion upside tail with defined risk. (Full: THESIS v5.0.)

| Field | Spec |
|-------|------|
| **Vehicle** | **USO call spread** (cleanest direct WTI/oil; vol-aware *spread*, never naked — LESSONS #15). XLE call spread = softer equity-beta alternative if Will prefers. |
| **Structure** | ~45–90 DTE; long ~5% OTM / short ~12–15% OTM. Exact strikes + premiums pulled from a **LIVE chain at arm time** (don't pin off a stale screen — `[[finding_option_marks_need_live_chain]]`). USO ref ~$105.48 (Jun-28 close). |
| **Sizing / max-loss** | **~$500 total, defined.** ~$300 on a Tier-1 arm; add ~$200 on a Tier-2 confirm. |
| **Execution authority** | **PRE-NEGOTIATED PROPOSAL.** On a fired trigger I pull a live chain + bring Will a one-line fill; Will gives a fast **[Approve/No]**. Structure + max-loss are pre-agreed so the approval is a yes/no, not a fresh design. **NOT** pre-authorized auto-fire. |

**Arm triggers (tiered — leading-cheap-first; deploy convexity while vol is still calm, don't chase the confirmed spike):**
- **TIER-1 (preferred entry, ~$300):** HAW-15 crude-export pivot **confirmed** (HAWK ledger), **OR** reopening visibly **stalls** (P&I pull / liners stay Cape 2+ wks / transit re-collapse) **while** Cushing/SPR at hard floors.
- **TIER-2 (add/initiate, ~$200, vol pricier):** Brent **sustains >$75 into 2 consecutive closes** (RED-FT-04 inverts), **OR** a **durable** ceasefire collapse / confirmed Hormuz physical re-closure.

**Disarm / horizon:**
- **Auto-disarm** if the reopening **COMPLETES** (P&I resumes + liners off Cape + sustained transits) **AND** buffers begin refilling — the whipsaw setup dissolves.
- **Disarm to neutral** if Brent breaks **<$70 on confirmed DEMAND collapse** (the *other* tail → revisit a short, not a long).
- **Horizon ~end-August** (by then SPR refill + reopening likely resolve); the XLE $65C Sep-30 expiry brackets the window. Review at each disarm condition.

**Why convex, not flat-price:** the upside is a TAIL that *just failed a live test* (Jun 27-28 — price fell through a tanker strike). We capture the up-skew with limited premium; if it never fires we lose only the debit. The plan *survives its own steelman*.

---

## EXECUTION LOG

| Date | Action | Detail |
|------|--------|--------|
| 2026-06-18 | CF $130C expired worthless | Last fill this regime. |
| — | (no convex-arm deployment yet) | Deploy-on-trigger; Will [Approve] at fire. |

---

## CATALYSTS bearing on the arm (the trigger watch — calendar twin in STATUS/docket)

| Date | Event | Bears on |
|------|-------|----------|
| Wed Jul 1 | EIA WPSR | Cushing import-surge vs continued draw = race read |
| Fri Jul 3 | CFTC COT (Jun-30) | kinetic-week covering (Tier-2 lean) vs continued liquidation |
| ~Jul 3 | SPR 172M auth withdrawal | the buffer-clock deadline |
| Wed Jul 8 | EIA STEO (July) | first post-deal price path |
| Rolling | **HAW-15** pivot / P&I resumption / reopening 2nd-derivative | **Tier-1 arm triggers** |

---

## RESOLVED / HISTORY
- **`PREREG_20260628_CME_reopen.md`** → RESOLVED **HOLDS** (Jun 29) — the Sunday CME-reopen pre-reg; structural confirmed.
- **BRT-15** (STNG reopen short) → FAILED Jun 20 (reopen was tanker-*bullish*).
- **Pre-Jun-29 Phase-1 long-energy book** (LNG/EOG/USO/STNG calls, Mar–Jun, $90→$73 regime) → **SUPERSEDED**; full prior content in git history (this file was wholesale-rewritten Jun-29 from its Mar-07 Phase-1 vintage).
