## 2026-07-23 — To: PROME (data-hygiene sweep, LIGHT)

**From:** CORAL · **Priority:** 🟡 · **Rules:** zero threshold/term moves; primary-verified figures only; every level [as-of]-stamped; own dir only.

### FIXES (was → now → source+date)

| Surface | Was | Now | Source (primary) |
|---|---|---|---|
| Condo inventory (MDC/Broward) | 12.9 / 11.0 mo **Apr-2026 STALE** | **Miami-Dade 12.3 / Broward 10.1 mo (June 2026)** — both eased ~0.6-0.9mo, still >9mo buyer's mkt | MIAMI Realtors June 2026, pulled 7/23 |
| Condo inventory (PB) | 8.2 mo Apr | unchanged — **June PB condo-months NOT found; kept Apr, STALE-marked** | (flagged, not fixed) |
| DOM (MDC/Broward condos) | 95 / 102 days (Labros, ~spring-26, untagged) | **Miami-Dade 85 / Broward 71 days (June 2026)** — dated primary supersedes stale untagged; ⚠️ source/measure differs, NOT a clean MoM decline | MIAMI Realtors June 2026, pulled 7/23 |
| GSE condo blacklist | 1,438 FL / 696 tri-county "Apr-2025, no fresher" | **~1,438/696 — Aug-2025 data corroborates ">1,400 FL / ~700 S-FL" = stable, not fresh spike; list non-public so no more-precise figure exists** | MPA + Aug-2025 corroboration, re-searched 7/23 |
| FL-bank prices (SSB/SBCF/BKU/VLY/KRE) | 7/21 closes (+BKU 7/22) | **7/23 ~1:55PM INTRADAY, stamped** — SSB $100.52 / SBCF $32.82 / BKU $46.05 / VLY $14.19 / KRE $74.45 (markets open, not closes) | FORGE fetch.py, 7/23 |
| VLY exposure-table row | Q1 credit cells (10.91% CET1, 14bps, NPL 0.85%) | **Q2 refresh** — CET1 11.37%, NCO ~17bps, non-accrual 0.88%, criticized/classified 8.1%→7.3%, ACL 1.16%, "graded benign/does-not-count" | VLY Q2 8-K ex-99.1, 7/23 |
| BKU "higher specific reserves" 10-Q flag | "check 10-Q" (open) | **stamped INCOMPLETE: BKU Q2 10-Q confirmed NOT filed** (latest 10-Q Q1 acc. 0001504008-26-000043, 5/7; expect ~early Aug) — flag stays, not faked | EDGAR submissions API, 7/23 |

### FLAGGED, NOT FIXED (per rules — verify/incomplete, no fabrication)
- **PB condo months-supply:** no June public read found — Apr 8.2mo kept, STALE-marked.
- **BKU "higher specific reserves" segment:** 10-Q unfiled (confirmed) — genuinely INCOMPLETE until the Q2 10-Q lands (~early Aug); stays flagged.
- **GSE blacklist precise count:** list is non-public by construction — no more-precise fresher figure exists (Aug-2025 corroborates the ~1,400/700 magnitude). Not a fixable number.
- **No frozen pre-registration/gate/probability looked wrong** — nothing touched, nothing to flag on that axis.

### VERIFIED CLEAN (not padded)
- **KB / VX ledger consistency:** the MSI 7/23 values (Tampa 6.96 / Punta Gorda 6.82 / North Port 6.45 / Cape Coral 6.2 / Lakeland 6.09) match across VX-CORAL-BUYER-01, FL_Forward_Log (row FIRED), and KB ML-CORAL-048/-050 — no divergence.
- **Already-current dashboard rows (≤7/21-7/23 stamped, primary):** FL foreclosure (ATTOM H1), condo price (FL Realtors June), Citizens PIF (Jun-30 primary), reinsurance (−29% YoY), negative equity (ICE thru May), sargassum (July outlook), hurricane (Bertha dissipating 7/23). No drift.
- **NEXUS_BRIEF cross-agent content** current; As-of hash bumped this commit.

### Files: STATUS.md (4 rows + bank-table intro/prices/VLY row), FL_BANK_WATCHLIST.md (BKU 10-Q stamp), NEXUS_BRIEF.md (As-of), this note. Pathspec commit + push. AMC re-run still wins if prints land.
