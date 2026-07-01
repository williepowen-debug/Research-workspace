# 6/18 Cluster Trigger Set v0.2 — Will-Approval Packet
**Created:** 2026-05-25 ET
**State:** `WILL_APPROVED` (2026-05-26 ~17:00 ET — see § Decision Log)
**Owner:** Prome (daily monitor) → Will (approval at any trigger fire)
**Source artifact:** `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.2 PROPOSED)
**Operational tracker:** `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md`
**Spec:** `PROME/EXECUTION_RAILS.md`

---

## The Ask

Adopt the 6/18 cluster trigger set as **execution rail v0.2**. Once approved:

- Every 6/18 theta-killer line has a pre-registered rule: no trigger = let expire; trigger = named review/roll action with named owner.
- Daily dashboard monitor checks R1-R4 + position-specific levels.
- Hard backstop 2026-06-16 16:00 ET clears the field on any line that never triggered.
- v0.2 becomes the live monitoring rail; this card becomes `WILL_APPROVED`.

**This packet is a Will-decision artifact, not a trade order.** Approval authorizes the *rail*, not any specific roll trade. Any actual roll trade requires its own Will approval at trigger fire.

---

## What changed from v0.1 → v0.2

v0.1 was Will-authorized 5/22 with three pieces left "pending calibration" from BROCK / REGINALD / HENRY. By the 5/24 EOD default-pass deadline:

- **HENRY replied 5/22** — TLT decision routed to its own action card; R1/R4-VIX calibration not addressed, locked to v0.1 default.
- **BROCK did not reply.**
- **REGINALD did not reply.**

Default-pass applied 2026-05-25 per the JUN18 action card C1 branch. **v0.2 is a pure pending-language-strip + default-pick lock pass — no threshold edits, no new trigger IDs, no positions added or removed.**

### The three default-picks PROME made (review these)

| ID | v0.1 status | v0.2 lock | Why this default |
|---|---|---|---|
| **A1 HYG** | "Dec 18 $75P or further OTM (BROCK to spec)" | **No pre-spec; BROCK validates at trigger fire** | HYG roll target is regime-sensitive — depends on the credit-cycle leg the trigger lands in. Pre-committing now bakes in an assumption. Routing already sends R2 fire → BROCK validation → Will approval. |
| **A5 WAL $67.5P × 2** | "Jul or Sep — REGINALD to pick" | **Sep $67.5P × 2** | REGINALD V2.2 Q2-print fire is **late-July**, *after* Jul expiry. Jul wouldn't catch the print. Sep does. REGINALD may override at trigger fire if framing changes. |
| **A6 KRE $60P × 1** | "Aug or Sep" | **Aug 21 $60P × 1** | Folds into existing Aug 21 stack via weighted-cost roll, per v0.1 source-trigger-set guidance. Sep would create a new isolated basis. |

### What stayed identical to v0.1

| Item | v0.1 = v0.2 |
|---|---|
| **R1** VIX ≥ 22 (intraday close, 2 sessions) | Out of vol-floor regime |
| **R2** HY OAS ≥ 290 (FRED close, 2 sessions) | Inverse of BROCK kill <270 sustained |
| **R3** KRE breaks $63 (close, 1 session) | Regional bank bear-line (KRE $69.37 5/22 close — 6.37 cushion) |
| **R4** HY OAS ≥ 320 (single close) | Cascade-onset; arms full review same-day |
| **A2** EGBN $25P → Sep $25P, convert margin→cash | unchanged |
| **A4** WAL $65P → Sep $65P | unchanged |
| **Dropped positions** (AAL ×2 Jun 18, CF Jun 18) | mechanical let-expire on 6/18, no triggers |
| **Hard backstop** 2026-06-16 16:00 ET | unchanged |
| **TLT $85P × 3** | already routed to separate action card (`BROKER_PENDING`) |
| **Cluster vol-floor principle** | unchanged — bias toward let-expire when triggers ambiguous |

---

## Outside this rail (no v0.2 coverage — disclosed for scope clarity)

v0.2 is intentionally scoped to *theta-killer loss-management at 6/18 expiry*. Two known forward decisions sit **outside** this rail and will be surfaced as separate action cards in their own time:

- **AAL Jul 17 $10P × 1 standalone:** Per source trigger set, decision deferred until the Jun 18 sweep clears. No rail in v0.2. PROME brings this as a separate one-line decision after the 6/16 backstop fires.
- **WAL Sep $67.5P × N fresh-open for REGINALD V2.2 Q2 print exposure (late-July):** v0.2 is silent on this gap by design. **If WAL holds above $73 through 6/18, A4/A5 mechanically expire and you lose WAL put exposure for the Q2 print catalyst.** The fresh-open is a new-exposure decision (different category from loss-management) and wants fresh marks/IV/sizing in front of you at the time. Logged as a candidate row in `ACTIVE_DECISIONS.md`; PROME surfaces it as its own action card around 6/13 EOD review or paired with the 6/16 backstop sweep, whichever fires first.

---

## Current tape vs triggers (refreshed 2026-05-26 16:10 ET)

| Trigger | Threshold | Current | Cushion | Status |
|---|---|---|---:|---|
| R1 VIX ≥ 22 (×2 sessions) | 22 | 16.92 | -5.08 | 🟢 not firing |
| R2 HY OAS ≥ 290 (×2 sessions) | 290 | 274 [5/25] | -16 | 🟢 not firing |
| R3 KRE breaks $63 (close) | 63 | $70.24 | -7.24 | 🟢 not firing |
| R4 HY OAS ≥ 320 (single) | 320 | 274 [5/25] | -46 | 🟢 not firing |

**No regime trigger fires at refresh time.** Position-specific levels also not firing: WAL **$79.56** vs $73 trigger (-$6.56 cushion, moving *away* from trigger since v0.2 ship); KRE **$70.24** vs $63 trigger. All cushions equal or larger vs v0.2 ship (5/22) — tape direction confirms v0.2's let-expire bias and also widens the Q2-print gap noted above.

---

## What approval does

On `[Approve]`:

1. JUN18 action card moves `PROPOSED` → `WILL_APPROVED`.
2. v0.2 source trigger set becomes the live monitoring rail.
3. ACTIVE_DECISIONS.md row updates accordingly.
4. Daily monitor scans R1-R4 + position levels via dashboard.
5. Any trigger fire spawns the named domain agent for roll-target validation → Will-approval for actual trade.
6. Hard backstop 2026-06-16 16:00 ET clears untriggered lines via let-expire default.

On `[Reject]` or `[Amend]`:

1. PROME notes which element changed (default-pick, threshold, position) in TRADE_DECISIONS log.
2. Card stays `PROPOSED` pending revision OR moves `REJECTED` if Will abandons the rail framework.
3. If amend: PROME drafts v0.3 with specified changes; same approval loop.

---

## Open Will-decisions in this packet

1. **Approve v0.2 as drafted?**
2. **Override any of the three default-picks?**
   - A1 HYG: keep "BROCK validates at trigger fire" (recommended) vs. pre-spec a target now?
   - A5 WAL $67.5P: keep Sep (recommended) vs. switch to Jul?
   - A6 KRE: keep Aug 21 stack-fold (recommended) vs. switch to Sep?
3. **Threshold sanity check** — any of R1-R4 read wrong to you given the 5/22 tape?
4. **Position scope** — any 6/18 line that should be added to or removed from the rail?

---

## Default-pass discipline note

Per `feedback_consolidate_domain_pressure` memory finding (5/22): when 3+ agents need to weigh in on the same Will-decision, file async SIGs with default-pass deadlines and consolidate into ONE Will-facing packet. This is that consolidation. BROCK and REGINALD chose silence; v0.2 doesn't penalize them — it just doesn't wait. They can override at trigger fire if their framing changes by then.

Per `feedback_front_load_planning` memory finding (5/21): 6 default-pick questions surfaced + Will-approved en bloc before any file edits. Execution then ran mechanical with proceed-pacing across Tasks 7-10. Zero mid-execution review escalations.

---

## Expiration / Supersession

This packet expires on:

- Will approves → packet logged in TRADE_DECISIONS, archive to `PROME/archive/` after 30 days. OR
- Will rejects / amends → packet superseded by v0.3 packet. OR
- 2026-06-16 16:00 ET hard backstop fires → packet auto-expires; backstop default applied.

---

## Decision Log

**2026-05-26 ~17:00 ET — Will approved v0.2 as drafted.**

Approval followed a Prome pre-approval review pass earlier the same session which surfaced two scope-limits (added to § "Outside this rail"):
- WAL Q2-print gap: if WAL holds >$73 through 6/18, A4/A5 expire mechanically and lose exposure for the late-July REGINALD V2.2 Q2 print catalyst. Fresh-open routed to its own action card.
- AAL Jul 17 standalone: orphan, no rail until post-6/16 sweep.

Tape table refreshed 5/22 → 5/26 16:10 ET (VIX 16.92 / HY OAS 274 / KRE $70.24 / WAL $79.56 vs $73 trigger). All cushions equal or larger vs v0.2 ship.

**Default-picks adopted as drafted:**
- A1 HYG → no pre-spec; BROCK validates at trigger fire ✅
- A5 WAL $67.5P × 2 → Sep $67.5P × 2 ✅
- A6 KRE $60P × 1 → Aug 21 $60P × 1 (fold into existing Aug 21 stack of 3 @ $2.70 wt avg) ✅

**State transitions completed:**
- `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` → `WILL_APPROVED`
- `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` → v0.2 `WILL_APPROVED`
- `PROME/ACTIVE_DECISIONS.md` 6/18 cluster row → `WILL_APPROVED`
- `PROME/TRADE_DECISIONS.md` → new entry logged
- Two Next Candidate rows added (WAL Q2-print fresh-open + AAL Jul 17 orphan)

**Operational next:** daily dashboard scan of R1-R4 + position-specific levels. No trade pending. Any trigger fire spawns domain agent → fresh Will approval for actual roll.
