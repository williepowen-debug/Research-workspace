# CYPHER — EXIT PROTOCOL (dated kill rail)

**Kill rail re-derived: 2026-10-22** (by CYPHER at its first live session, 22:39 ET; supersedes the DAEDALUS build draft of the same date)

Two rails. **R0** asks whether the desk should exist, and is unusual here because a named cheaper alternative exists. **R1** asks, per wave, whether the wave stays mechanical or becomes systemic. At build there is a strong prior and no thesis. This file says so rather than inventing one.

## R0 — the desk's premise (scheduled review)

| Field | Content |
|---|---|
| Premise | A dedicated event owner changes consequence-owner judgments sooner or more correctly than DEWEY's alternative: the 9-row checklist run as a WALTER watch, with a desk only if a row fires (REQ-008 closing section) |
| Review date | **2026-12-17** (eight weeks after build; after the MOVEit +14-day anchor 11/04 and the 20-trading-day anchor 11/18) |
| Instrument (positive) | At the consequence owners' own artifacts — REGINALD · GIBBS · SHADE · VULCAN · LIQUID · HENRY STATUS, KB, board_log, predictions: a judgment, threshold, prediction or tag that **cites a CYPHER incident or watch row** and moved because of it. Healthy reading = ≥1 such cite. A packet merely moved to `processed/` is NOT consumption (Class 11: `CONSUMED` ≠ `ENCODE-CONFIRMED`) |
| Second instrument | Count of watch rows CYPHER moved to `FIRED` or `NOT-FIRED` **before** WALTER's routing carried the same fact. Zero means the desk added no speed over the watch it replaced |
| If both are 0 | DAEDALUS + PROME **recommend** to Will folding back to DEWEY's WALTER-watch form. **Never automatic** — dormancy is a ROSTER change (Will's) and a registration event (REGISTRATION_CHECKLIST § Dormancy) |
| If ≥1 | Continue. Record the cites here |
| Base rate | None for the desk — first cycle. For waves: 0 of 5 past waves were systemic for banks (KB-CYP-001). A quiet first cycle is therefore the EXPECTED outcome and does not by itself fail R0 |

## R1 — WAVE-2026-10 (PHP2Shell / "Black October"): mechanical or systemic? (per wave)

| Field | Content |
|---|---|
| State 2026-10-22 (CYPHER) | **OPEN QUESTION — prior: mechanical.** Closest precedent is Log4Shell (ubiquitous open-source flaw; attempts in the millions per Cloudflare; no named successful compromise at 2026-10-22). It shares MOVEit's one dangerous feature, exploitation before disclosure (AWS MadPot 10/17 vs disclosure 10/21), and the Dutch NCSC is investigating "first signals of successful misuse" (primary, 10/22 16:01 CEST). Composite 21/40 raw, 15/40 shared-root-adjusted (`VX.tsv`) |
| Instrument | `ESCALATION_WATCH.tsv` rows 1–9 for WAVE-2026-10; each row's own healthy reading |
| Flip toward MOVEit (systemic-for-vendors shape) | **Fires when** escalation row 1 or row 3 moves from NOT-FIRED to FIRED on or before **2026-11-20** (disclosure +30 days): a named organisation's successful PHP2Shell compromise confirmed by the victim, an incident-response report, a national CERT, or a leak-site claim the victim does not deny. Instrument: rows 1 and 3, re-checked at least every 7 days (boot.py leg 4 enforces the clock). Window check: MOVEit satisfied it at +14 days (KB-CYP-004); Log4Shell did not (no named mass compromise at +30). **Consequence:** R1 state becomes SYSTEMIC-WATCH; P1 packets to REGINALD, GIBBS, SHADE, PROME the same session |
| Flip toward Log4Shell (loud and small) | **Fires when**, at **2026-11-20**, rows 1, 3 and 4 are all still NOT-FIRED (the state it fires FROM is their 2026-10-22 NOT-FIRED), each with a dated re-check inside 2026-11-13..2026-11-20 at its named instrument (row 1 national CERT and IR primaries; row 3 victim and vendor statements; row 4 EDGAR Item 1.05 via boot.py leg 8). A search outside that window is NO-VERDICT, not a pass. Window check: Log4Shell (disclosed 2021-12-09) satisfies it at 2022-01-08; MOVEit fails it, so the test discriminates. **Consequence:** R1 state becomes MECHANICAL (Log4Shell-shaped); rows stay open, nothing is closed by it — MOVEit's list grew 13+ months and SolarWinds' victims surfaced at +66 days, so a row 1 FIRE after 11/20 still flips the stance back |
| Kill (wave) | A wave closes when every row is `STOOD-DOWN` with a dated reason. Closing a wave does not touch R0 |
| ⚠️ Conjunction warning | "Rows 1, 3, 4 all NOT-FIRED for N days" is a multi-channel quiet-period conjunction — the highest-risk kill shape (blueprint §4). It must state the state it fires FROM and name one historical window that would have satisfied it (Log4Shell's) before it is used to close a wave |

## R1 context note — 2026-10-23 (not a re-derivation; the flips above are unchanged)

- **Chokepoint map built** (`workbook/CHOKEPOINTS.tsv`): today's threats touch the EDGES of US finance's shared suppliers (perimeter appliances, the MSP layer, file-transfer products), not a core processor or market utility.
- **The MOVEit-shaped node now has a name: Kiteworks** (file transfer), confirmed AFFECTED by PHP2Shell (own advisory 10/22), no exploitation statement. A Kiteworks victim confirmed by the victim, an IR report or a CERT would satisfy the toward-MOVEit flip through row 1 (any named PHP2Shell compromise). Check 2026-11-06.
- **Not a flip input:** CYP-03/04 (registered 10/23) grade the map's deductions, not this wave.

## Rules (blueprint §4 — cite, don't restate)

Every `AND` in a kill states the state it fires FROM. No threshold already breached at write time. A falsification leg names a positively-measured instrument. A retraction is a claim and gets graded like one.

## R1 context note — 2026-10-26 (registered flips unchanged)

CISA KEV v2026.10.26 lists both PHP2Shell root CVEs (dateAdded 10/26): row 2 FIRED, VX-CYP-06 4/5. Composite 22/40 raw and 16/40 after counting the PHP2Shell cluster once. CONFIRMED now describes root-flaw exploitation; no named organisation is supplied by KEV. Row 2 alone does not satisfy the R1 named-victim test in row 1 or 3, so no SYSTEMIC-WATCH flip is recorded. Other owner rows retain their actual check dates; the full re-check remains due 10/29. Evidence: `research/2026-10-26_startup/RECORD.md#kev`.
