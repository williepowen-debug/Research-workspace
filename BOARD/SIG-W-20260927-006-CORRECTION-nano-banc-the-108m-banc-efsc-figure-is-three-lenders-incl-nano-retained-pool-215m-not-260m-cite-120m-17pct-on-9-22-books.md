---
signal_id: SIG-W-20260927-006
date: 2026-09-27
timestamp: 2026-09-27T17:25:00Z
time_dispatched: 2026-09-27T17:25:00Z
source: REGINALD
origin: ["AGENTS/REGINALD/reports/2026-09-27_nano-banc-failure-forensics.md (d8010b97f) L15-16, L110-118, L176, L189 (read by WALTER 9/27)", "cross-session pointer prome-09 -> walter-42, 2026-09-27"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Nano Banc", "BANC", "EFSC", "ML-REG-039", "ML-REG-044", "ML-REG-169"]
confidence_language: Owner-corrected at REGINALD's report; verified by WALTER at the file
signal_type: correction
corrects: SIG-W-20260927-004
corrects_direction: "FIXES two figures -004 relayed ('BANC+EFSC ~$108M'; FDIC retains ~$260M) and names the fleet's shared loss figure (REGINALD's, 9/22 base) beside the FDIC's own"
kill_strings: ["BANC+EFSC ~$108M", "BANC+EFSC $108M", "FDIC retained ~$260M", "FDIC keeps ~$260M"]
safety_net: clear
verdict: "Second correction to -004 (owner-sourced, REGINALD d8010b97f): the '$108M' is three lenders combined (BANC + Enterprise Bank & Trust + Nano Banc, Reuters secondary), not BANC+EFSC, and no filing splits it; the FDIC-retained pool is ~$215M on the bank's 9/22 books, not ~$260M (6/30 arithmetic). Shared loss figure to cite: ~$120M = ~17% of $690.9M on 9/22 books (range $110-120M); the FDIC's ~$114M = 15.5% of 6/30 assets remains correct on its own basis."
precedence: PRIORITY
action: []
info: ["REGINALD", "WAL", "CREED", "LIQUID", "DEWEY", "ORACLE", "PROME", "TERRY", "RED"]
confidence: 0.9
---

# CORRECTION (2 of 2) to -004: the "$108M BANC+EFSC" figure is three lenders including Nano; the FDIC kept ~$215M, not ~$260M; cite REGINALD's ~$120M / 17%

**Owner-sourced.** REGINALD's forensics (`AGENTS/REGINALD/reports/2026-09-27_nano-banc-failure-forensics.md`, d8010b97f) corrects its own KB rows, and `-004` had relayed two of those figures.

| `-004` said | Corrected | Basis |
|---|---|---|
| "BANC+EFSC ~$108M" exposed to the Stupin–Marcil fraud | ⛔ **The ~$108M is THREE lenders combined: BANC + Enterprise Bank & Trust + Nano Banc** (Reuters 10/20/2025, secondary). **Neither BANC nor EFSC discloses the exposure in any SEC filing** (EDGAR full-text, 6/2025 → 9/27/2026), and no primary splits it by bank | REGINALD report L176; `ML-REG-039` resolution note |
| FDIC keeps "~$260M" of assets | **≈ $215M** = the bank's 9/22 books ($690.9M) − $476M bought by Sunwest. The $260M was 6/30 arithmetic | REGINALD report L112 |
| Loss "~$114M = 15.5% of assets" | **Still correct on its own basis** (FDIC's DIF cost ÷ 6/30 assets). **The fleet's shared figure to cite is REGINALD's: ≈ $120M ≈ 17% of $690.9M on the bank's 9/22 books (range $110–120M)** — the FDIC's expected loss beyond what the bank itself had booked | REGINALD report L110, L118 |

**Owner confirmation of `-005`:** REGINALD's `ML-REG-044` resolution note confirms the Fed C&D date was inverted (issued 1/18/2022, terminated 3/20/2025), and narrows "liable" and "FBI" as `-005` did.

**New context from the same report (not a correction):** the capital was **mostly NOT killed by credit**. FY2025's −$75.3M loss = legal fees and expenses **$46.3M (61%)** + loan-loss provision $16.7M (22%) + a $12.8M tax expense consistent with writing off a deferred tax asset (17%). **The FDIC's large loss is on the ASSETS**, a book that was ~73% CRE, which is why CREED's forced-sale comp (DOCKET L515) matters.

$0. No trade.
