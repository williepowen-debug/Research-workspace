# FERT → PROME — G:GATE-FERT-G5 print 10 + D:L576 IPL tender outcome — 2026-10-21

**Spawn:** WQ-184 due-row wake, PROME session `af287aee` (WQ-465 A). Boot wall clock 2026-10-21 08:55 Wed (boot.py). Runtime: Claude Code Agent tool, Opus 5.5. API connection lost ~09:00 ET; uncommitted edits re-verified intact on resume (row widths, LF endings) and finished.

## 1 · G:GATE-FERT-G5 — NOT FIRED, 10 of 10 graded prints

| Field | Value |
|---|---|
| Print | DTN Progressive Farmer 2026-10-21 "UAN32, UAN28 and Anhydrous Lead Fertilizer Prices Higher" (datePublished 2026-10-21T11:43Z), data wk Oct 12–16 2026 |
| Fetch | first-party curl dtnpf.com 2026-10-21 08:56 ET, HTTP 200, 185,204 B — PRIMARY |
| MAP / DAP (US natl avg, $/ton) | **$981** (+$2 w/w) / **$937** (+$3 w/w) |
| Distance to strictly-greater $1,000 | MAP **$19 (+1.94%)** binding; DAP $63 (+6.72%) |
| Pace (11 prints 8/12→10/21, log) | MAP ~+0.99%/mo → ~1.9 months (≈ mid-to-late Dec); not scored |
| Grade | **NOT FIRED** — `KB-FERT-079`, `workbook/GATE_GRADES.md` 10/21/26 row |
| Owner-set review_by | **2026-10-28** (next DTN Wednesday) |

## 2 · D:L576 — IPL urea tender (1.7 Mt: 1.0 Mt West + 0.7 Mt East)

⛔ From the row, verbatim: "The EXIT_PROTOCOL nitrogen re-open test keys on the AWARDED CFR, which follows days later — the 10/07 offers are a READ, never a fire."

| Item | Read | Source |
|---|---|---|
| Lowest CFR offers (= IPL counters) | $352.10/mt CFR East (Millennium, 60,000 t) · $356.25/mt CFR West (Aditya Birla, 350,000 t) | AFC w/e 9.10 (stated) — unchanged from 10/15, `KB-FERT-071` |
| **Outcome (new)** | **India "secured approximately 410,000 metric tonnes (MT) against its intended purchase of 1.7 million MT"**; Chinese suppliers declined ~$320–325/mt FOB netbacks, selling prilled elsewhere up to $340/mt FOB; "another tender will be required" | AFC weekly w/e 16.10.2026, datePublished 2026-10-19 — **MIRROR, single source** |
| **Awarded CFR** | **NOT STATED** in any free source reached (Google News RSS ×3, Profercy free index, WebSearch extended ×2, 08:56–08:57 ET). INFERRED from the counter mechanism: ≤ $352.10 E / $356.25 W ⇒ **$244–248/mt (~41%) under $600** | `KB-FERT-080` |
| G2 / re-open test | Not gradeable on a stated award price; on the inference, far below. **Nitrogen channel DEAD. Nothing fires; no CARL/HENRY routing.** | EXIT_PROTOCOL §1A |
| Traps | ⛔ Profercy "Urea: IPL issues counter offers…" = 2026-04-16 (the April tender) — discarded. ⚠️ a WebSearch summary tied "410,000 t" to China June–July export customs data; the AFC sentence ties its figure to this tender explicitly, used single-sourced | `KB-FERT-080` |

**Suggested docket disposition (PROME's call):** L576's award read is answered as far as free sources allow (volume yes, price no). FERT T1 now watches the likely **follow-on IPL tender** at 10/28 (rides T4) — no new DOCKET row requested; register one only if PROME wants the follow-on tender to wake an idle FERT.

## 3 · Ride-along T12 + potash triage

- Q4 Tampa molten sulfur **still unsettled** per the Green Markets 10/16 post (teaser; body walled). Intl phosphate flat ~2 months: Brazil MAP $830–850/mt CFR, India DAP $890–905/mt CFR [AFC w/e 16.10]. `KB-FERT-081`.
- **Potash triage flag (charter §POTASH, no deep-dive):** DTN retail potash $503/ton [wk Oct 12–16]; Brazil MOP $355–375/mt CFR, SE Asia standard MOP $370–420/mt CFR, SE Asia granular MOP $425–435/mt CFR [AFC w/e 16.10]. `KB-FERT-082`.

## 4 · Inbox — whole drain (7 files by census = 5 WALTER signals + 2 standing desk files)

| Signal | Disposition |
|---|---|
| SIG-W-20261015-016 (API crude) | info-only |
| SIG-W-20261016-004 (EIA crude) | info-only |
| SIG-W-20261019-003 (HY 331bp) | info-only |
| SIG-W-20261019-019 (repeat losers / MOS sulfur) | noted — matches T12, no new research |
| SIG-W-20261020-024 (USDA $8B fuel relief) | noted — ag-input context, no grade |

`PROTOCOL.md` + `RECEIPT.md` = standing desk files, not packets. All five logged in `board_log.tsv`, `git mv`'d to `inbox/WALTER/processed/`.

No trade, threshold, or score change. Convergence 16/40 held. FERT desk commit: 41e60e5ef (not pushed, per brief).

## COMPLETION — FERT — 2026-10-21
STATUS: ✅ DONE
CHANGED: AGENTS/FERT/{STATUS.md, workbook/KB.tsv, workbook/TRIGGERS.tsv, workbook/GATE_GRADES.md, board_log.tsv, inbox/RECEIPT.md, archive/STATUS_whatchanged_2026-10-15_ROTATED.md, inbox/WALTER/processed/ ×5}, this memo
RESULT: G:GATE-FERT-G5 NOT FIRED 10-of-10 on DTN 10/21 first-party (MAP $981, $19 under $1,000; DAP $937); review_by → 10/28. D:L576: India booked ~410,000 t of 1.7 Mt [AFC w/e 16.10, single MIRROR], awarded CFR not stated — inferred ≤ $352–356/mt CFR, ~$245 under $600; nitrogen channel DEAD, nothing fires. Inbox 5/5 drained; KB-FERT-079…082 added.
GAPS: IPL awarded CFR not printed in any free source reached (Argus/Profercy award items walled); Q4 Tampa sulfur body walled; Mosaic South Fort Meade not re-read (theledger.com refuses this box).
WILL_NEEDS: None.
FOLLOW-UP: FERT T4/T1/T12 all 10/28 — G5 print 11, follow-on IPL tender, Q4 sulfur. PROME: disposition DOCKET L576; GATES G5 review_by 10/28.
