# PROME boot brief — CORRECTED (Sat 2026-09-26)

**Written:** Sat 2026-09-26, first pass 17:5x ET, second pass 18:0x ET (after CATO's WR18–WR21 review of the original brief, `610dddf23`), on Will's word: *"Finish the unread HEARTBEAT section. Correct the CDS qualifications, option-value wording and schedule in the brief and the source summaries carrying those claims. Keep Friday's process sitting conditional on actual domain obligations. Distinguish packet delivery from completed owner implementation. Preserve my existing rulings and holds."*
**Supersedes** the in-session boot report (~17:3x ET, terminal only). No ruling, hold or gate state changed. $0 moved. No market data refreshed — every level is 9/25 or earlier (weekend orientation, BOOT.md §5).

## What the first brief got wrong

| # | Said | Correct |
|---|---|---|
| 1 | DTCC "shows" 847bp; CoreWeave stress "confirmed" | Upfront prices are observed; 847bp is model-derived; the conversion benchmark is pending (§ CDS) |
| 2 | Discriminator not firing ⇒ "CoreWeave-specific" | It did not fire **on its checked observations**; that does not establish the absence of wider stress |
| 3 | 004 "nothing to sell into" | A dated 0.03 screening bid ≈ $60–80 gross marked value — neither zero nor proven executable (§ Book) |
| 4 | Fri 10/02 = "first open slot" for process work | Friday carries its own due domain obligations; L503's date is a candidate only (§ Friday) |
| 5 | "Rulings encoded" | Most are packets delivered, owner implementation pending (§ Delivered vs implemented) |
| 6 | FERT on Wed, CARL on Tue | Canonical rows + the sequenced week put FERT's session 10/02 and CARL's 10/01 (§ Week) |
| 7 | Dashboard not run = a "skipped control" | Not applicable: no level was cited as current. The real omission was the unread HEARTBEAT tail — now read |

## CDS — observed, derived, pending

- **Observed** (DTCC public dissemination): CoreWeave Dec-2031 5Y trades at **500bp coupon + 11.82pt upfront [9/24]** and **+11.46pt [9/23]**, $3M each (`AGENTS/LIQUID/analysis/2026-09-26_liq069-leg2-grade.md` §3).
- **Model-derived:** ≈**847 / 835bp** from LIQUID's `crwv_cds_grade.py` (flat hazard, flat 4% discount; not the ISDA standard model). The structural gap to ISDA is **UNMEASURED**; Will ruled that a ±25bp bound cannot be claimed.
- **Gate:** LIQUID graded `GATE-LIQ-069` leg 2 FIRED using those model-derived spreads; the gate stands **2-of-2** because Will accepted the trades as the instrument (WQ-301 a). The research alert and its follow-through are retained. The permanent anchor re-base is **HELD** for one ISDA benchmark (WQ-301 b, DOCKET L510, LIQUID, Monday).
- **Follow-through:** the registered cohort discriminator **did not fire on its checked observations** (BB 164, CCC +36bp over 5 sessions [9/24]). That is not evidence that wider stress is absent. The NEXUS flag is a packet in `AGENTS/WALTER/inbox/`, **unrouted and unconsumed**. No capital path.

## Book (orientation only — position truth is off-repo; WQ-274 open)

- **004 TLT Sep-30 $77P ×20**, expiring **Wed 9/30** (sessions Mon/Tue/Wed). The last mark on file is **0.03 / 0.04 [16:03 ET 9/25, one vendor, SCREENING]** — about **$60–80 gross marked value** on 20 contracts, against a $231.26 basis. It is neither zero nor demonstrated executable proceeds.
- The $0.3469 harvest line has not been reached (on that mark it would need TLT ~−3% by 9/30). No new salvage is proposed.
- The standing instructions stand: **HOLD ×20 to expiry** (WQ-168 ④ / WQ-217), **NO ADD** (WQ-280), the harvest line and the expiry. TERRY's older no-salvage rationale (9/22) is not a refreshed valuation. Any other action = a fresh TERRY card + Will's [Approve].

## Delivered vs implemented — observed in the owner dirs 17:5x ET

| Ruling | State | Evidence |
|---|---|---|
| 292 cards | IMPLEMENTED (TERRY) | `40e12ee0a`, `30fc177c2`; WQ-302 open to 10/14 |
| 296 A — HAW-22 | IMPLEMENTED (HAWK; 65% uncalibrated) | `bba2e26fd` |
| 296 vendor inquiries | Kpler SENT, no reply · Vortexa NOT SENT (Will's form) | Gmail 1a0df4d64f13afb1 |
| 295 R1 cadence tokens | IMPLEMENTED (PROME, ROSTER) | STATUS |
| 291 / 246 (BOND) · 293 (YURI) · 301 a/c (LIQUID) | PACKET DELIVERED — owner encode OWED | `a5ef473ef` |
| 287 (CARL) · 257 (FERT) · 295 R4 (DAEDALUS) | PACKET DELIVERED — owner encode OWED | `a118b367d` (CARL corrected `8ce9e2776`) |
| 255 CATO SPECIAL | ROSTER moved (PROME) · DAEDALUS FLEET_MAP/directory/checklist PACKET DELIVERED, rides L490 | `bb256896a` |
| 301 (b) · 295 R2 | HELD — waits LIQUID (L510) · waits Will | — |
| LIQ-069 NEXUS flag | PACKET at WALTER, unrouted | WALTER inbox |

Delivery was verified by commit. Implementation is verified only where an owner commit exists. Nothing in this table was independently checked downstream.

## Week — DOCKET dates, sequencing per `PROME/plans/2026-09-26_week-ahead-sequenced.md`

| Day | Obligations |
|---|---|
| Mon 9/28 | LIQUID L492 (~16:15 ET, 9/25 HY cell; est. ≈283 ±5, falsified ≤278 — RED-FT-01 day 2 **only if ≥280**; LIQUID's X1 `>280` strict is a separate letter) · LIQUID L510 ISDA benchmark · OTTO L469 |
| Tue 9/29 | CCL Q3 (company-confirmed, AM; CRUISE L221) · HENRY L489 blind read on BRT-12 |
| Wed 9/30 | 004 expiry (L74/L255, TERRY) · ZHA-16 (L481) · HAWK L491 · GATE-FERT-G5 review date (FERT's session is sequenced 10/02) · WQ-279 NYSCEF needed-by |
| Thu 10/01 | BOND after the FR2004 print (~16:15 ET; L478/L410 — grades under WQ-291 **once its encode lands**) · rent freeze effective, PROME spawns FLG (L236; GATES row keeps its secondary-source / possible-stay limits) · CRMT bridge-4 STD (L479, BROCK) · CARL L152 (window 9/29–10/01) + the 287 encode · RED CH-009 (L484) |
| Fri 10/02 | LABOR NFP (L287, date INFERRED) · BRENT COT #8 + OPEC+ prep (L297) · BROCK L494 X1 sitting · DAEDALUS/LIQUID owed sets (L490/L493) · CORAL L501 · FERT L288 + G5 + 257 · OZK L463 · YURI · CRUISE L502 if not done · L210 FORUM-6 · L503 candidate |

The dated wakes exceed the cap of four on 9/30, 10/01 and 10/02. Rows past the fourth are slated for Will's word in that day's boot report.

## Friday's process sitting — conditional

L503's registered 10/02 date is a **candidate**, not a guaranteed slot. Under WQ-299 R1 the one process change (spine audit #15 + the C2–C4 proposal) runs only in a session with no due domain or position item PROME can advance still open, or on Will's word. Friday carries such items (above), and a future date never blocks today's useful work. WQ-237's root-doc scope stays an encode of Will's 9/17 approval. ⚠️ The spine-audit stamp (9/20) goes stale 9/27: reported, not run.

## HEARTBEAT — the unread tail, now read

Pointers · kill-on-sight · cadence · §2R · Skip. **Posture unchanged:** no new deployment decision; STAND DOWN (WQ-192); X1 CLOSED; concentration ACCEPTED (WQ-297 A). The live capital lines are the 2 staged VLO shares (gate HELD) and the 004 expiry. The kill list binds, including *"HY is re-armed at 280"* and *"the crack under $95 is the buy trigger"*. **AMENDMENT #1** (this session) withdraws "nothing to sell into" and supersedes "LIQ-069 1-of-2". Boot reads are now complete.

## Preserved unchanged

WQ-299 R1–R4 · WQ-295 R2 HELD · WQ-192 · WQ-280 · WQ-168 ④ / WQ-217 · WQ-297 A · WQ-301 (a)/(c) RULED, (b) HELD · WQ-302 open to 10/14 · WQ-237 approval · the L511 review-limit conflict and rotation shortfall carried.

## Surfaces corrected (uncommitted, pending Will's directed review)

- `PROME/STATUS.md` · `PROME/SCRATCH.md` · `PROME/HANDOFF.md` · `PROME/ACTIVE_DECISIONS.md`
- `PROME/GATES.tsv` (the LIQ-069 state cell)
- `HEARTBEAT.md` (AMENDMENT #1, chain 1) + `PROME/HEARTBEAT_DASHBOARD.md` (projection; parses clean)
- This file.

Two correction passes have now run on each surface, so the two-correction stop applies: any further edit needs an independent read first. The queued HEARTBEAT amendment ① (the USO source label) was left out of scope.
