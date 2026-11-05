# One-time late-loan scan, Q2 → Q3 2026, 139 banks (2026-11-05, 11:47 ET onward)

**Authority:** Will in this session, 11:47 ET, "yes run the scan". One-time and descriptive: not a registered instrument, no threshold, no recurring check. $0. No score, gate, prediction or trade change.

## 1. Bottom line

**Preferred Bank is the only true outlier.** ⚠️ *Corrected 11/05 after the 12-quarter review: Flagstar's 30–89 move is a rebound, not a new high; the 90+ and modification points stand → `reports/2026-11-05_FLG_late-loan-review.md`. Original text said "Flagstar is the one that matters."* Of 139 banks, four met the rule, and one is the control. The others mostly thin out at the issuer. The largest dollar move among names with tradable options is outside the rule: **Flagstar multifamily 30–89 $233M → $392M, plus all-loan 90+ accruing $51M → $107M (multifamily $38M → $50M).** That was in its 10/23 release table and my 10/23 grade did not read it. Late-loan totals on the list rose 7.9%, $13.43B → $14.49B, which includes consumer loans and Santander's acquired book, so that aggregate is a size, not a trend.

**Method:** `domain/sources/2026-11-05_late-loan-scan/` (`scan.py`, `audit.py`, raw JSON, outputs). FFIEC Call Report RC-N, 6/30 and 9/30, own pull. Rule written before any result: a loan class leads if 30–89 is up ≥$25M and ≥50%, and is ≥2.0% of that class's loans at 9/30.

**Checks:**
- **Positive control passed:** Preferred Bank, added for this purpose, was the top hit.
- **The script's "UNTIED" label is my design error, not a data problem.** It tests six classes against a total that also holds consumer and other loans, so 115 banks print UNTIED. `audit.py` replaces it: in no bank do the six classes exceed the total, and they carry **62.1% of all 30–89 dollars**.
- **Blind spots:** consumer, card, auto and other loans are not scanned. Four small banks' C&I has no book figure and could not lead. A bank that absorbed a merger inflates; 4 acquirers are excluded by the rule's spirit, and none led.
- **Universe:** the short list's 138 live banks (largest small banks, cohort, Q2 movers) plus Preferred. **Most banks under ~$10B are not in it,** and Preferred itself was not on the list until I added it. This cannot say "only these".
- **Not a credit grade.** 30–89 is the noisiest bucket; timing and renewals move it. A quarter-end snapshot.

## 2. Rule hits

| Bank | Class | 30–89, $M | % of class | Nonaccrual, $M | Read at the issuer | Verdict |
|---|---|---|---|---|---:|---|
| **Preferred** (control) | Multifamily | 62.8 → **143.1** | 26.5% | 27.4 → 80.0 | Not explained; `reports/2026-11-05_PFBC_and_open-threads.md` | **Open.** Q3 10-Q ~11/7–11/10 |
| **NexBank** (Dallas, $14.0B, private) | Multifamily | 24.9 → **75.2** | 8.6% | 1.9 flat | **No public filing found;** private | Unreadable. Call Report only. Lead stays open with no route |
| **Flagstar** | Construction | 8.0 → **46.4** | 3.6% | 119.8 → 116.1 | Release's table folds this into CRE: CRE 30–89 $30M → $79M | **Open;** see §3 |
| **First Hawaiian** | Multifamily | 0.8 → **28.3** | 3.1% | 0 | 10-Q filed 11/02 has no multifamily line. CRE: 30–59 $32.5M, 60–89 only $2.8M, 90+ $2.3M of $4.7B | **Weak.** Sits in the earliest bucket; no nonaccrual |

## 3. Outside the rule, larger in dollars (labelled NOT the rule; the rule is not re-cut)

| Bank | Class | 30–89, $M | % of class | Read |
|---|---|---|---|---|
| ★ **Flagstar** | Multifamily | 233 → **392** | 1.5% | Own Q3 release table: 90+ accruing multifamily $38M → $50M; CRE $13M → $53M; total 90+ $51M → $107M; nonaccrual flat $2,800M → $2,817M. ⚠️ A year earlier multifamily 30–89 was $344M, so this bucket has been high before. Book falling, $26.9B → $25.9B |
| **Citizens** | Non-owner CRE | 29 → **194** | 1.9% | 10-Q 10/28: CRE 30–59 $178M, 60–89 only $23M, so nearly all in the earliest bucket. 0.1pp under the rule's line. No explanation read. CRE nonaccrual $578M |
| **City National** (RBC-owned) | Non-owner CRE | 11 → 87 | 1.3% | No issuer read; parent is foreign |
| **Rockland Trust** | Non-owner CRE | 13 → 54 | 1.2% | No issuer read |
| **The Bancorp** | Multifamily | 0 → 27.6 | 1.1% | ✅ **Likely closed.** Q3 release: "In October 2026, $27.6 million of the REBL criticized loans were recapitalized with new counterparties." Same figure; the match is my inference. Also on the 10/31 borrowing flags |
| **Customers** | Owner CRE | 0 → 26.9 | 1.3% | No issuer read; total 30–89 $29.6M → $80.0M; 10-Q not filed |

Also listed in `audit_output.txt`, unread: Hancock Whitney, Popular, Arvest, WesBanco, Enterprise.

## 4. What this means

- **For Will's question:** yes, release-only reads were missing things. Flagstar's was in a table I did not grade, and Preferred's was in no release at all. That changes how I read filings at the 11/07 run; it needs no new checker.
- **Flagstar:** my 10/23 "0 of 4 readable lines met" stands, because the frozen lines do not include 30–89. It is thinner comfort than it sounded. It goes to the FLG desk. The Q3 10-Q (not filed at 10:33 ET) carries the multifamily special-mention and modification cells that decide it.
- **Not a sector read.** Few banks hit; the pattern is scattered, with no shared geography beyond what the small sample allows. **Severity stays concentrated**, and FLG is already the top of the matrix.
- **Matrix, thresholds, gates:** unchanged. FLG's score stays until the 11/07 re-score.

## 5. Routing

| To | What |
|---|---|
| **TERRY** | FLG NOT-FIRED lead, evidence only. Listed puts show open interest 828 on Dec-18 (vendor 11/05). Preferred and NexBank: no candidate. Will holds FLG 10P Mar-19-2027 ×1 on the 11/5 capture |
| **FLG desk** | The release-table figures, for its own read |
| **WALTER** | Citizens, Flagstar and NexBank facts for routing to CREED, HOMER, BROCK |

**Not done:** issuer reads for City National, Rockland, Customers and the five names unread above; consumer classes; any bank outside the list. Cohort selection: this adds Preferred and NexBank to the side-list argument; Will's ruling stays open.
