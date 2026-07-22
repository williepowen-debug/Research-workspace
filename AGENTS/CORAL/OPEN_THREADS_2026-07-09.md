# CORAL — Open Threads Report (2026-07-09)

*Will-directed follow-on to tonight's 3-pass catch-up. Grounded in STATUS/SCRATCH/CALENDAR/board_log as of commit 2ea2b321. No trade recs.*

## 1. OPEN QUESTIONS — unresolved, matter now

| # | Question | Why it matters | Status |
|---|----------|-----------------|--------|
| 1 | Citizens 294,253 (CORAL, personal-lines) vs ~395K (AEOLUS, scope unspecified) | ✅ **RESOLVED 7/21 (primary):** both were TOTALS at different dates (CORAL's label wrong; AEOLUS's Jan-31 vintage). Canonical: 278,246 total / 273,684 personal, Jun 30 2026. KB ML-CORAL-035 | Closed 7/21 |
| 2 | Parcl builder-MSI tripwire (MSI >6.0 across ≥5 FL metros, 2+ wks) | Pre-registered 🟠→🔴 escalation trigger, **never checked against a live pull across 3 sessions now** | Hard deadline set: next CORAL session |
| 3 | Lost `CORAL_SPINOUT_2026-06-19.md` | No record anywhere of the REGINALD→CORAL spinout rationale/scope decision survives | Confirmed lost, not recoverable from repo |
| 4 | FL labor "2nd-worst YoY" rank claim | Never independently verified (PROME 6/26 flag); currently unused, but sitting in the wings | Unverified |
| 5 | Fannie/Freddie condo blacklist (1,400+) | Dashboard's own tag says "STALE-ish," sourced Mar-2025, claimed quarterly cadence not actually run | Aging, no refresh mechanism |
| 6 | Receivership/termination count beyond *Biscayne 21* | The cleanest "household stress → distressed asset" tell CORAL doesn't have | NOT FOUND (open since 6/19) |
| 7 | Did 2026 FL legislative session amend/delay the SIRS reserve mandate? | Could soften or harden the whole condo pillar | NOT FOUND (open since 6/19) |

## 2. GAPS — coverage holes, no instrument

- **No repeatable pull for the Parcl MSI tripwire.** CORAL tracks the threshold conceptually; no script/cadence exists to actually check it (same root cause as #2 above).
- **No per-metro convergence grid** (Miami/Tampa/Orlando/Jax/SW-FL). This is CORAL's stated edge — "channels stacking on the same geography" — and it's been a stub since 6/19, three sessions running.
- **No interim USCB condo-association read between 10-Qs.** USCB is "the cleanest condo→bank canary" on the watchlist; CORAL only sees it quarterly, same cadence as everyone else — no early-warning channel.
- **No FL-specific NFIP/flood-policy data source in `DATA_SOURCES.md`.** Tonight's flood-uninsured collateral thread (SIG-627-030) has no live FL instrument behind it.
- **No recurring Ch.7 per-capita pull.** Bankruptcy tripwire (>230/100k) exists on paper; sourcing has been one-off AOUSC pulls, not a schedule.
- **Sargassum (record-tier, ~28.9M MT) has no dollar linkage** to any FL bank or insurance metric — tracked as a "2nd-order overlay" and left there.

## 3. THREADS TO PULL — leads nobody has chased

| Thread | Why it matters | What pulling it takes | Urgency |
|---|---|---|---|
| **Property-tax CRE/MF burden-shift → which banks/associations absorb it?** The 10%→5% non-homestead cap + burden-shift (verified tonight) hasn't been cross-walked against FL_BANK_WATCHLIST's condo-assoc/CRE books (USCB, SBCF, AMTB) | Could be a *second* independent forcing mechanism landing on the same collateral the insurance-timing chain already tracks — could compress the H2-2026/2027 timing | Read the amendment fiscal note by property class; overlay against USCB/SBCF/AMTB CRE + condo-assoc exposure | this-month |
| **MF concession bifurcation (Jax/Tampa oversupply vs Miami tight) × the same tax burden-shift** | Sharpest geography-convergence read CORAL is positioned to make — two stress channels possibly stacking on the same metros | Metro-level reassessment impact by property type, overlaid on SIG-627-025's Jax/Tampa data | this-month |
| **Construction-insurance availability block (Damac $1.6B tower) — one-off or pattern?** | Availability blocks are harder-edge than premium rises; if systemic (not developer-specific), it's a bigger FL CRE pipeline story | Scan CRE trade press (Bisnow/Real Deal/CRE Daily) for other FL large-project insurance-availability stories, last ~90 days | this-month |
| **Flood-uninsured collateral (SIG-627-030) → which specific bank(s)?** | Named forward tail flagged tonight but not operationalized to a bank-level read | Cross-walk First Street/Moody's RMS county exposure against FL_BANK_WATCHLIST footprints | background |
| **NIST Surfside report — does it name specific buildings/portfolios?** | Could sharpen "structural/durable" condo-reserve thesis into an address-level early-warning list | Read full NIST report (not WALTER's summary); cross-ref against USCB's disclosed association list if available | background |

---
*Compiled from tonight's 3 passes (Pass-1/Pass-2 catch-up, self-sweep). Dated calendar gates (Q2 earnings, Nov-3 vote, FL employment print) live in `CALENDAR.md`, not repeated here as threads.*
