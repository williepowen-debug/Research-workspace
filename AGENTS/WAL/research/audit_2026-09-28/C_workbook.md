# C — WAL workbook ledger audit (READ-ONLY) — 2026-09-28

Scope: `AGENTS/WAL/workbook/{KB.tsv, KB_INDEX.md, PREDICTIONS.tsv, MI3_SERIES.tsv, RETIRED_CLAIMS.tsv}`, `board_log.tsv`, `registry/corrections_receipts.tsv`.
KB.tsv line N = row KB-WAL-(N-2) (header is L1 comment + L2 column row; KB-WAL-001 = L3, KB-WAL-209 = L211).
Parsed with python on tabs. 209 rows, all 13 columns wide. 167 ACTIVE / 42 SUPERSEDED. Last KB commit `899f4952a` 2026-09-28.
Reference truth used: v2.4 EV $75.96, PT $52-76. Last named close $77.61 (9/25). Cantor residual $72.4M gross / $3.5M allowance. Live book is the Dec-18 $70P ×1.

Severity count, Section 1 (38 findings): **HIGH 3 · MED 21 · LOW 14**.

---

## Section 1 — ACTIVE rows that are STALE or INCORRECT as of 2026-09-28

| # | Row (file:line) | Quoted claim (short) | Why it is wrong, with evidence | Sev | Suggested disposition |
|---|---|---|---|---|---|
| 1 | KB-WAL-121 (KB.tsv:123), ACTIVE, SB 2026-10-31, A2 | "The NDFI/warehouse book is SHRINKING … by management choice" | Refuted at A1 by later rows that are also ACTIVE. KB-146 (L148): Q2 10-Q NDFI $15,812M = 25.9% of HFI, a record; all three sub-lines grew QoQ. KB-168 (L170): FFIEC RCONJ454 ties to the dollar and has risen for 12 quarters. KB_INDEX itself says "121 … REFUTED by 146". The row was never re-marked. | HIGH | SUPERSEDED → KB-146/168. The management-intent half ("won't be as active") already lives at KB-196. |
| 2 | KB-WAL-137 (KB.tsv:139), ACTIVE, SB 2026-10-31 | Notes: "bearish for the **~$46-70M** residual carrying value". Fact: "Los Angeles County Superior Court … Judge Terry A. Green". Venue note: "Search the adversary docket, not LA Superior" | (a) Carries the retired "~$46M" residual (RETIRED_CLAIMS 2026-09-24). The retired regex `(residual ~?\$46M\|~\$46M (Cantor\|\+)\|\$46M residual)` does **not** match "~$46-70M", so derived_drift_check can never flag it. (b) KB-208 (L210, A1, RECAP primary): only the **guaranty** claims were removed. Claims against Cantor V stayed in LA Superior before Hon. Cherol J. Nellon with a JAMS referee, not Judge Green. The 9/27 venue note ("not LA Superior") over-corrects the other way. | HIGH | Re-verify and rewrite. Supersede the venue and judge → KB-206/208 and the residual → KB-143 ($72.4M). Add a RETIRED_CLAIMS pattern covering `46-70M`. |
| 3 | KB-WAL-004 (KB.tsv:6), ACTIVE, **blank SB**, A1, DerivedFrom blank | "Reality: True CRE stable at ~$36.8B, labeled CRE fell — relabeled, not reduced." | "True CRE" is the MI3 add-back built on KB-002 ($2.73B) and KB-003, both SUPERSEDED-INPUT on 8/28. MI3 later fell to $2.55B (KB-164). The blank DerivedFrom is why the 8/28 dependency sweep (which caught 003/007) missed it. The row is A1-tagged but the "Reality:" clause is a derivation. | HIGH | SUPERSEDED-INPUT, like 003/007. Keep the two management quotes as dated history. |
| 4 | KB-WAL-082 (KB.tsv:84), ACTIVE, SB 11/10, **A1** | "~$70M residual on book … $13M senior liens" | KB-143 (L145, A1 primary Q1 10-Q) gives $98.5M − $26.1M = **$72.4M** gross with $3.5M specific allowance left. The row's own Notes say "Cite as Q1-vintage **A2**", but the Conf column says A1. | MED | SUPERSEDED → KB-143 for the figure. At minimum re-tier to A2. |
| 5 | KB-WAL-123 (KB.tsv:125), ACTIVE, SB 10/31, **A1** | "$98.6M = revolver/suit total commitment; ~$70M = residual carrying value" | KB-143 corrects both ($98.5M, $72.4M) and says it "UPGRADES KB-WAL-123 from **A2-secondary**". The source is the Alphastreet transcript plus the REGINALD grade, which is A2 by KB_INDEX's own tier convention. KB_INDEX's CANTOR key-fact still repeats "$98.6M / ~$70M" beside "$72.4M". | MED | Re-tier to A2. Point the figures → KB-143. Keep the zero-mention absence finding. |
| 6 | KB-WAL-061 (KB.tsv:63), ACTIVE, SB **2026-10-13**, **A1** | "Short float 3.54% … Lightly shorted — thesis is NOT consensus" | (a) Contradicted by the later ACTIVE KB-126 (4.91% at FINRA 6/30, up 27.75%). Neither row is superseded. (b) The source is Finviz, a secondary aggregator, but it is tagged A1. (c) The Stale_By equals the Q3 frame deadline its own Notes name ("10/13 = the Q3 frame deadline, where SI is a frame input"), so it fires on the day it is needed. | MED | SUPERSEDED → KB-126. Re-tier. Refresh from the FINRA file before the frame, not on its deadline. |
| 7 | KB-WAL-126 (KB.tsv:128), ACTIVE, SB 10/31 | "Short interest 4.91% of float … (FINRA settlement date 2026-06-30)" | This is the newest short-interest datum on file and it is ~3 months old. FINRA publishes twice a month. The SB of 10/31 lets it age past the print. | MED | Re-verify at the latest FINRA settlement before the 10/13 frame. |
| 8 | KB-WAL-138 (KB.tsv:140), ACTIVE, SB 10/31 | "both new PTs sit ABOVE our EV of **$73.92** … Citi's $98 is above even the **v2.3** Bull-range top of $94" | The EV is v2.3-vintage; v2.4 EV is $75.96. Citi was cut $98→$95 on 9/22 (KB-197, L199). KB_INDEX ANALYST key-fact repeats both stale tokens. | MED | SUPERSEDED → KB-197. Keep as the dated post-Q2 record. |
| 9 | KB-WAL-091 (KB.tsv:93), ACTIVE, SB 2026-12-31 | "$946M Office matures during 2026 = 43% of $2.2B Office book" | KB-163 (L165, A1 Q2 10-Q): **$686M** remains to mature in 2026 and CRE-NOO office is $2,139M. The $946M still travels into WAL-01 Notes and KB_INDEX HIDDEN_CRE / Thesis-layer cells. | MED | SUPERSEDED → KB-163 (full-year figure kept as history). |
| 10 | KB-WAL-136 (KB.tsv:138), ACTIVE, SB 10/31 | "Jefferies missed a **$42.1M installment due 2026-02-27**" | KB-144 (L146, A1): "$42.1M was the payment WAL RECEIVED on 2026-01-15, NOT a missed installment". Row 136 carries no pointer to that correction. | MED | Annotate or partially supersede → KB-144. |
| 11 | KB-WAL-124 (KB.tsv:126), ACTIVE, **blank SB** | "The P&L arc is closed; WAL v. Jefferies … continues as a forward RECOVERY question **only**" | Made two-way by KB-135 (a $25M countersuit) and KB-136 (non-recourse defense). The Q2 10-Q is silent on the countersuit (KB-153). KB_INDEX JEFFERIES key-fact still says "recovery upside only". | MED | Annotate. SB 2026-11-10 (Q3 10-Q legal note), with that reason. |
| 12 | KB-WAL-024 (KB.tsv:26), ACTIVE, **blank SB**, A1 EMPIRICAL | "Gibbons dual-hatted during **exact quarter hidden CRE ratio grew fastest**" | MI3_SERIES.tsv: 2024Q4 (the Dec-2024 leave) is +5.85pp, but **2024Q1 was +6.64pp**, the largest step. KB-023 (L25) and LEADERSHIP.md:22 repeat "accelerated". This is an inference labelled EMPIRICAL. | MED | Re-verify and strike "fastest". Re-label as an assessment. |
| 13 | KB-WAL-023 (KB.tsv:25), ACTIVE, **blank SB** | "Gibbons … moved to '**VP** Deposit Initiatives and Innovation' — parking title" | KB-130 (L132, Form 4 primary) says "**Vice Chair** & CBO Deposits". LEADERSHIP.md:45 says "Vice Chairman, Deposit Initiatives & Innovation". The "parking title" inference rests on a mis-stated title. | MED | Re-verify the title at the 8-K or proxy. SB at the 2027 proxy. |
| 14 | KB-WAL-133 (KB.tsv:135), ACTIVE, SB 10/31 | "the people who exercised discretion did so at **worse prices than the market now offers**" (7/24 close $83.11) | Inverted by price. The sales were at $81.00–$82.64; the 9/25 close was $77.61, so both sellers now look to have sold **above** market. The "two-way read" has flipped sign. | MED | Annotate with the window endpoint. Re-grade the V4 read at the next insider pass. |
| 15 | KB-WAL-160 (KB.tsv:162), ACTIVE, SB 2027-08-07 | Notes: "The ~Aug 14 13F season row remains **genuinely unexamined**." | This is a RETIRED claim (RETIRED_CLAIMS 2026-08-20, pattern `/13f…genuinely unexamined/` matches). The Q2 13F aggregate was done 9/24 (KB-199). It is **absent from derived_drift_check output** (4 KB.tsv hits, none is L162), probably suppressed by a marker inside the 220-char window. | MED | Annotate → KB-199. Flag the checker false-suppression. |
| 16 | KB-WAL-180 (KB.tsv:182), ACTIVE, SB 2026-09-30 | "$79.89 close 8/20 … Buffer … +2.6% … IT IS NOT THE COHORT … grind is name-specific" | Carries three retired tokens (`79.89 close`, `+2.6%`, `NOT the cohort`). KB-190 corrects the close to $79.15. KB-185 (8/20→9/2 WAL beat KRE by 59bp) and KB-197 (sector + rates) overturn "name-specific". | MED | SUPERSEDED → KB-190 / 185 / 197 when it expires 9/30. Do not extend it. |
| 17 | KB-WAL-080 (KB.tsv:82), ACTIVE, **blank SB** | "All three WAL fraud vectors (Cantor/First Brands/Tricolor) … three gatekeeper failures" | The row's own 9/24 Note says "WRONG AS A COUNT": First Brands **is** the LAM charge-off (KB-135/186), Tricolor exposure was never evidenced, and the mechanism was perfection or priority, not audit. It is still ACTIVE. | MED | SUPERSEDED → KB-144/186 + FRAUD/FIRST_BRANDS.md §FOLD. |
| 18 | KB-WAL-048 (KB.tsv:50), ACTIVE, SB 11/10 | Fact: "74% of loans pledged ($23.9B). Worst in SVB/FRC comparison set." | **Confirmed:** the do-not-cite marker is in the row, but only in **Notes** ("DO NOT CITE until re-derived"). The Fact cell reads clean, the Status is ACTIVE, and the SB was extended. KB_INDEX CAPITAL key-fact still says "74% pledged" with no caveat. KB-049 (L51) shares the defect (noted in its row). | MED | Put DO-NOT-CITE into the Fact or Status, or mark SUPERSEDED pending re-derivation from the Call Report (RC-M, desktop). Fix the KB_INDEX cell. |
| 19 | KB-WAL-058 (KB.tsv:60), ACTIVE, **blank SB** | "May 2025 low = $57.08. **Current ~$68.** … -16% downside to revisit" | Asserts a March price as "current". The 9/25 close is $77.61, so the distance to $57.08 is now −26.5%. | MED | Strike "current" / SUPERSEDED. Keep the $57.08 low as a timeless fact. |
| 20 | KB-WAL-008..012 (KB.tsv:10-14), SB **2026-11-05** | "EXTENDED to 2026-11-05 … 11/05 = the PWS JWT expiry, the last date the refresh route is guaranteed" | The Stale_By is set **equal to the event it waits for**. The rows expire on the day their only refresh route dies, so the flag cannot trigger a refresh. | MED | Re-date **with reason** to before JWT expiry (e.g. ~10/23, a desktop-session target). Per-row, not bulk. |
| 21 | KB-WAL-205 (KB.tsv:207), SB 2026-11-10 | Notes: "Observable: Plaza Continental hearing Tue 9/29/2026 1:30pm (Judge Houle)" | The row's own named observable lands **tomorrow**, but its Stale_By is 6 weeks later. Nothing forces a re-read of the lien-ownership branches after the hearing. | MED | SB 2026-09-30, reason "read 9/29 hearing docket (research §10)". |
| 22 | **Cluster:** 54 ACTIVE rows with SB 2026-10-31 (27 are Q2-10-Q-carried: 111, 121, 123, 133, 140-159, 162, 163, 177) | e.g. KB-123 "Final ledger tie-out owed at the Q3 10-Q footnote" | The Q3 10-Q is due ~11/9 (40 days after 9/30; the Q2 10-Q came 10 days after the print). These 27 rows expire **before their refresh instrument can exist**. That is 54 simultaneous expiries, which invites the bulk re-date the desk forbids. | MED | Per row: rows carried by the 10-Q go to the desk's own Q3-10-Q backstop, **2026-11-10** (as already used on 022/048/082), each with a reason. Rows carried by the print keep 10/31. |
| 23 | Tier overstatement class | KB-068 (L70) A1 "Will signals"; KB-069 (L71) A1 "BROCK OUTBOX"; KB-070 (L72) A1 "CARL SIG"; KB-175 (L177) A1 "REGINALD packet" (the KB header itself calls 175 "SECONDARY"); KB-111/117/119 (L113/119/121) A1 while mixing the Alphastreet transcript | KB_INDEX convention: "`A2` = live-dated secondary or fleet-internal derivation (Alphastreet call transcript, FINRA via a grade report…)". Relayed or fleet-internal rows are tagged A1. | MED | Re-tier per row (A2/B). For mixed rows, tag the call-only figures A2 in Source. |
| 24 | KB-WAL-188 (KB.tsv:190), SB 2026-10-13 | "WAL closed $75.60 … BELOW the v2.4 EV $75.96 for the FIRST time" | Correct as a dated fact, but it is the **newest tape row**. The 9/25 close of $77.61 is **+2.17% ABOVE** EV. No KB row records the move back above EV, so a reader taking the latest tape row as state gets the sign wrong. The SB also equals the frame deadline (see #6). | MED | Add a tape row for the 9/24–9/25 closes. SB → ~10/9. |
| 25 | KB-WAL-176 (KB.tsv:178), ACTIVE, B2 | "NOT filing-confirmed — **no 8-K carries it**" ($0.42, record 8/13, payable 8/27) | False. The 8-K of 7/30 (acc 0001628280-26-051146) declared exactly this dividend (KB-161, L163, A1). This is a duplicate with an understated tier, filed in the OWNERSHIP group. | LOW | SUPERSEDED → KB-161. |
| 26 | KB-WAL-085 (KB.tsv:87), ACTIVE, **blank SB** | Notes: "**No incremental disclosure expected.** Investor Day May 12 = only near-term forcing window" | The Q2 10-Q disclosed an **amended**, broadened complaint (KB-152, L154). The expectation was falsified. | LOW | SUPERSEDED → KB-152 (keep the quote as history). |
| 27 | KB-WAL-079 (KB.tsv:81), ACTIVE, **blank SB** | "WAL exposed via NDFI/warehouse/BDC chain (unquantified)" | The row's own Note says "UNVERIFIED HYPOTHESIS … no WAL Tricolor exposure evidenced across four filings". The Fact still asserts exposure. | LOW | Re-label the Epistemic as hypothesis, or SUPERSEDED. |
| 28 | KB-WAL-075 (KB.tsv:77), ACTIVE, blank SB | "despite … three concurrent fraud exposures (Cantor, First Brands, Tricolor)" | Tricolor was never evidenced (KB-079 Note), and First Brands = LAM. The count is wrong, as in #17. | LOW | Annotate. |
| 29 | KB-WAL-115 (KB.tsv:117), ACTIVE, SB 10/31 | "EPS $2.36 vs $2.33 consensus (**beat**)" | KB-149 (L151): GAAP = adjusted = $2.36, and "the consensus leg is STRUCTURALLY UNRESOLVABLE". KB-139 finds three contested consensus figures. KB_INDEX EARNINGS still says "$2.36 vs $2.33". The drift check flags L117 as a v2.3 token. | LOW | Annotate → KB-149 and strike "beat". |
| 30 | KB-WAL-017 (KB.tsv:19), ACTIVE, **blank SB** | "Total ring exposure ~$270M across WAL, ZION, BANC, Enterprise Bank" | KB-137 says ">$270M across WAL + Zions". Nano Banc is now evidenced as a further senior lender (KB-202). The composition is inconsistent across rows. | LOW | Re-verify and reconcile. |
| 31 | KB-WAL-099 (KB.tsv:101), SB 12/31 | "$4.5B Hotel Franchise Finance = 44% of CRE Investor" | KB-145: $4,684M = 45.3% at 3/31. No 6/30 hotel figure on file. | LOW | Point → KB-145. Add the Q2 table (see Gap 10). |
| 32 | KB-WAL-077 (KB.tsv:79), SB 11/10 | "WAL **30%** Cantor reserve rests on RSM collateral work…" | Present tense. The reserve is now $3.5M specific; recognized loss is 26.5% of exposure (KB-143). The row is correctly restored ACTIVE, but the Fact reads as current state. | LOW | Annotate the Fact with its Q3-25 vintage. |
| 33 | KB-WAL-203 (KB.tsv:205), SB 10/31 | Fact: "Trial set 2026-08-11 … Current status … UNKNOWN at 9/27" | The same row's Notes (DEWEY O2) show the trial **continued to 2027-01-12**, a status conference on 11/30, and **detained** 8/17. The Fact body was never updated, so the correction sits beside the stale instruction. | LOW | Fold the update into the Fact. SB 2026-11-30 (status conference). |
| 34 | KB-WAL-151 (KB.tsv:153) | Notes: "STATUS EXIT RULES **currently** name 'Q3 deck slide 12 + Q3 10-Q Schedule O'" | This has not been current since the 8/20 P2 re-spec. | LOW | Annotate "as of 8/7". |
| 35 | KB-WAL-059 (KB.tsv:61), blank SB, A1 "Chart analysis" | "Distribution at top … **Now lower highs**." | A March chart read asserted as current, and an interpretation tagged A1 EMPIRICAL. | LOW | SUPERSEDED / strike "now". |
| 36 | KB-WAL-013 (KB.tsv:15), blank SB | "Basel III Endgame proposed tightening SSFA … No current regulatory action" | A regulatory-state claim 6 months old with no expiry. | LOW | SB 2026-11-05 alongside 008-012, reason "re-check rule status + Q3 RC-R". |
| 37 | KB-WAL-021 / -057 (KB.tsv:23/59), blank SB (duplicates) | "Class action investigation by Rosen … Portnoy Law also investigating" | Current legal state as of March. Whether any complaint was filed is unknown. | LOW | Re-verify (Stanford SCAC/PACER). SB 2026-11-10 (Q3 10-Q legal note). Merge the duplicates. |
| 38 | KB.tsv header (L1) | Newest clock entries are 9/27 | The 9/28 commit `899f4952a` re-wrote the KB-202/205 Notes ("corrected 2026-09-28") and is recorded in **neither** clock. It is a hygiene edit and should advance only the sweep clock. | LOW | Add a 9/28 hygiene entry. The data clock stays put. |

Not counted, noted only: KB-130 and KB-133 carry "$83.11" (a retired token) inside a dated 7/24 context, which is correct history. KB-169's "BEAR-FAST'S 10% WEIGHT" is correct history. KB-181's rank is already fenced "DO NOT CITE THE RANK", which is adequate.

---

## Section 2 — BLANK Stale_By triage (41 ACTIVE rows, list verified independently = checker's 41)

### 2a. MATTERS: the row asserts a current state, price, legal status or next event, or its content is contradicted (18)

| Row | Why it matters | Suggested SB + reason (row-by-row, never bulk) |
|---|---|---|
| KB-004 | Derived "true CRE" on a superseded input (§1 #3) | Don't date it: SUPERSEDED-INPUT |
| KB-013 | Regulatory state (Basel III / SSFA) | 2026-11-05, re-check rule status with the Q3 RC-R |
| KB-015 | "WAL at 30% recognition vs ZION 83%" is a live comparison; now 26.5% | 2026-11-10, Q3 10-Q Cantor paragraph |
| KB-017 | Ring-exposure composition conflicts with KB-137; Nano now a party | 2026-10-31, reconcile against complaint KB-202 |
| KB-021 | Class-action status (legal state) | 2026-11-10, Q3 10-Q legal proceedings |
| KB-023 | Title mis-stated vs KB-130 | 2027-04-30, 2027 proxy |
| KB-024 | "Grew fastest" contradicted by MI3_SERIES | Correct the claim, then 2027-04-30 |
| KB-034 | Thesis-level method claim ("works for OZK but NOT WAL") | 2026-11-30, with the QBP rows 030-033 |
| KB-045 | "Transmission chain, not yet activated" is current state | 2027-03-01, with the NV group (041) |
| KB-057 | Duplicate of 021 (Portnoy) | Merge into 021 |
| KB-058 | "Current ~$68" price | Strike the current-price clause; the low is timeless |
| KB-059 | "Now lower highs" | SUPERSEDED |
| KB-070 | March macro "accelerates WAL mortgage book stress" | 2026-10-31 or SUPERSEDED; A1 tier also wrong |
| KB-074 | "RSM has audited WAL for 32 years" (auditor could change) | 2027-03-01, FY26 10-K auditor report |
| KB-079 | Asserts an unevidenced Tricolor exposure | Re-label as a hypothesis, else SUPERSEDED |
| KB-080 | Its own Notes say it is wrong | SUPERSEDED |
| KB-085 | "No incremental disclosure expected" was falsified by KB-152 | SUPERSEDED |
| KB-124 | "Recovery question only" is qualified by 135/136 | 2026-11-10, Q3 10-Q legal note |

### 2b. BORDERLINE (5)

| Row | Note | Suggestion |
|---|---|---|
| KB-029 | Cross-bank insider assessment (B1); OZK dormant | 2027-04-30 or leave, with a "timeless assessment" reason |
| KB-035 | OZK/WAL complement assessment | Same |
| KB-068 | "largest single CMBS office action in 2026 so far" (a March superlative); A1 on a Will relay | Strike "so far" or date it; re-tier |
| KB-087 | "Largest single-quarter fraud charge in current cycle" + OTTO ledger "~$535-565M" (another desk's number) | Pointer to OTTO; 2026-12-31 |
| KB-129 | Cash-settled RSU mechanic (a structural current fact, re-observed 9/17 in KB-193) | 2027-04-30, proxy |

### 2c. TIMELESS dated facts: blank Stale_By is fine, but give each an explicit "no-decay" reason (as KB-190 did) so blank ≠ unreviewed (18)

KB-025 (Dec-2025 board adds), 026 (Ardrey/Mucha Feb sale), 028 (comp plan Dec-2025), 038 / 054 / 055 (dated tape events; 038 = 055 duplicate), 039 / 056 (Madison; duplicates, and the fund letter is **undated in the row**), 042 (Circa facility), 043 (gaming line), 044 (2012 history), 072 / 073 / 076 (PCAOB release facts), 075 (FY25 opinion; content defect in §1 #28), 084 (LAM $126.4M), 100 (Q1 securities gain), 125 (Q2 print tape).

---

## Section 3 — PREDICTIONS / INDEX / MI3 checks

### 3a. PREDICTIONS.tsv (L5 header; WAL-01 L6, WAL-02 L7, REG-15 L8)

| Check | WAL-01 (OPEN, 25%) | WAL-02 (OPEN, 50%) | REG-15 (RESOLVED-FAILED 8/20) |
|---|---|---|---|
| Resolve_By present | ✅ 2026-11-15 (48d; not overdue; after the ~11/9 Q3 10-Q deadline) | ✅ 2026-11-15 | ✅ 2026-08-31 (retro-filled, stated) |
| Anchor type stated | ✅ "ANCHOR TYPE = EXPECTED-EVENT" (Notes) | ✅ EXPECTED-EVENT | ✅ SCHEDULED-FILING |
| Carrier named in the row | ✅ Invalidation names the Q3 deck "Classified Assets Mix" slide (A2-visual) + a 10-Q total-classified cross-check + a NO-VERDICT band | ⚠️ **Not in the row.** Invalidation says only "Q3-2026 ex-fraud NCO <= 40bps". The carrier (EX-99.1 NCO line, 10-Q confirms) is named only in `Q3_PRINT_GRADING_FRAME_2026-09-24.md:17` and `Q3_10Q_GRADING_FRAME:23` | ✅ FFIEC RCON2746/RC-C item 4 |
| Defects | (LOW) The Notes keep the 7/21 instruction "Canonical >$500M resolution stays Q3 10-Q CRE-NOO arithmetic" beside the 8/20 re-spec, so two live instructions exist. The Notes also carry the superseded "$946M" (KB-163 → $686M). The row's NO-VERDICT band omits the **INSTRUMENT-CONFLICT** outcome the 10-Q frame §1 adds. | (LOW) The Prediction text "Q2 or Q3" and Timeframe "Q2-Q3 2026" are unchanged although the re-spec made the row Q3-only. Consistent with the frame, but the cell misleads a cold reader. | (LOW-MED) **Shell-expansion corruption:** the Notes read "the secured office book, **the 9M life-science credit**" (should be $99M). This is the same unquoted-heredoc defect repaired on KB-173..177 on 9/24, and it was missed here. |
| Overdue | No | No | n/a |

**Header two-clock:** L1 "Last real data refresh: 2026-08-20" records re-specs and a scoring against 8/7 FFIEC data. No new data landed on 8/20, so this is defensible as "the row content changed", but it labels a ruling-application as a data refresh (LOW). L2 sweeps (9/27, 9/24, 9/02) are honest and say "NO ROW CHANGED". The **8/28 Resolve_By column addition** is absent from both clocks and recorded only in the row Notes (LOW). The 9/16 guide tension (mgmt "NCO under Q2" vs a 50% chance of >40bps) is recorded as a benchmark, not graded. That is correct under R3.

### 3b. KB_INDEX.md vs KB.tsv

| Check | Result |
|---|---|
| Header token | "**209 rows \| 20 groups**", which matches the TSV (209 rows, 20 groups) ✅ |
| Group-map sum | The group table sums to **200**, not 209 ❌ (MED) |
| CANTOR_FRAUD | Index 16 vs TSV **24**. **KB-201..208 missing** from the IDs column (Nano receivership, Nano DOTs, Makhijani, Fed C&D, removal/Stupin, Marcil lender, removal scope) ❌ |
| CRE_MACRO | Index 4 vs TSV **5**. **KB-209 missing** ❌ |
| All other 18 groups | Counts and ID lists match exactly ✅ |
| Stale key-fact cells (MED as a class) | CANTOR: "three-figure reconcile RESOLVED ($98.6M revolver / ~$70M residual…)" beside "$72.4M". ANALYST: "ABOVE our EV $73.92", Citi $98. HIDDEN_CRE: "**ACL/NPL 96%**", which KB-157 says is ACL/**nonaccrual** (NPL basis 69.1%), plus "$946M Office matures 2026". JEFFERIES: "forward V2 = litigation/recovery upside only". CAPITAL: "74% pledged" (do-not-cite). EARNINGS: "$2.36 vs $2.33". Vector-map V2: "Cantor docket identified" (venue stale). |
| Unstruck residue in Thesis-Layer table | V1a cell: "~~STILL UNTESTED (127).~~ **Four months, zero confirmations and zero disconfirmations. The standing embarrassment**", where the second half is unstruck and false. V3 cell: "**The lone confirming sub-vector is shrinking by management choice**" (refuted by 146/168). Insider cell: "both *below* today's price" (inverted, §1 #14). |
| Format notes | "Old rows retain `ACTIVE` even when superseded — KB is event log" contradicts current practice (42 SUPERSEDED rows). "verified 127/127" is a stale count. |
| Staleness table | Explicitly bannered "8/20 snapshot", which is acceptable. |

### 3c. MI3_SERIES.tsv

| Check | Result |
|---|---|
| Completeness | 12 quarters, 2023-09-30 → 2026-06-30, no gaps ✅ |
| 23.88% / 21.20% | Recomputed 2,722,527/11,399,418 = 23.883% and 2,554,610/12,047,671 = 21.204% ✅ |
| Every row | Recomputed MI3%, QoQ delta and NDFI% of loans. **All 12 match to ±0.01** ✅. All-time high 24.24% (2025Q4); never ≥25% ✅ |
| Uniform-basis cross-check | (item4+9a) Q2 9.17% / Q1 10.34% reproduce KB-167 ✅ |
| Gaps | (LOW) No item **9.b (RCONJ464)** column, which is the component behind REGINALD's 8.99% vs this desk's 9.17% (KB-182). (LOW) The header "Next real data: Q3-2026 Call Report ~Oct-Nov" does not mention that the **JWT expires 11/05**: Call Reports are due 10/30, leaving a ~6-day desktop window. STATUS:14 and MEMORY:5 carry it; the ledger and KB-164..170 (SB 11/30) do not. |
| Two-clock header | Honest: data 8/7, sweep 8/7, no later touch ✅ |

### 3d. board_log.tsv / corrections_receipts.tsv / RETIRED_CLAIMS.tsv

- board_log: v0.2 header correct. 6 rows = the 6 SIGs in `inbox/WALTER/processed/`. Nothing is unrowed ✅
- corrections: `corrections_boot_check.py WAL` rc=0, 0 unreceipted NAMED rows. There is 1 broadcast ALL-row warn (COR-20260925-13, the HY-280 arbiter), which is not WAL-relevant and is "warn-never-block" (info).
- RETIRED_CLAIMS: 23 rows. **Pattern gap:** the `~$46M` row does not catch "~$46-70M" (KB-137). The 9/28 Ontario/Chino row lists KB-205 as owner surface but not KB-202, although KB-202's Notes carry the same "forced seller" conditional (now correctly conditional, so this is LOW).

---

## Section 4 — GAPS (evidence classes the KB lacks for a WAL short thesis)

| # | Missing evidence | Why it matters | Cheapest source |
|---|---|---|---|
| 1 | **Q2 deposit balance** (6/30 total deposits, LTD) *(known)* | KB-102 (Q1) is still the newest balance. KB-122 is cost only. The funding-fragility leg is "CLOSED benign" without a Q2 balance. | SEC XBRL companyconcept `us-gaap:Deposits` (one call) |
| 2 | **Q1 V2 inventory-clean result** *(known; KB-086 Note "never got its own KB row")* | The supersession of 086/089 rests on an un-rowed finding | Q1 10-Q already on file / STATUS_ARCHIVE V2 detail → one A1 row |
| 3 | **Uninsured deposits % (current)** | Only KB-049 (Q4-25, basis-defective) | Q2 10-Q MD&A liquidity or Call Report RC-O memo |
| 4 | **Pledged collateral / contingent liquidity capacity** (FHLB + FRB) | KB-048 is do-not-cite. There is no valid liquidity-coverage row at all. | Q2 10-Q liquidity section (borrowing capacity table) |
| 5 | **FHLB advances / short-term borrowings / brokered deposits** | Zero rows. Wholesale funding reliance is a core bank-short input. | XBRL (`ShortTermBorrowings`, `AdvancesFromFederalHomeLoanBanks`); Call Report RC-E brokered |
| 6 | **CRE concentration vs total risk-based capital (SR 07-1 300%/50%)** | The only regulatory red-line rows (003/007) were superseded on 8/28 with **no replacement** | Call Report RC-C/RC-R (desktop, before 11/05), or REGINALD cohort |
| 7 | **Q2 RC-R refresh: CET1, RWA, SSFA exposures** | 008-012 are Q4-25 vintage. The CET1 11.0% comes only from call/EX-99 text. | FFIEC CDR Q2 RC-R Part II (desktop) |
| 8 | **HTM unrealized losses + AFS duration** | AOCI (KB-120) covers AFS only. The Category IV phased-AOCI leg (KB-198) needs duration. | Q2 10-Q Note 3 (securities) |
| 9 | **Office maturities 2027+** | KB-163 has a 2027 CRE-NOO total ($2,972M) but no office-specific 2027 bucket | Q2 10-Q maturity table / Q3 deck |
| 10 | **Q2 CRE-NOO full property-type table** (Hotel, Multifamily, Medical… at 6/30) | Only Office, Life sciences and the total were captured. KB-145 (Q1) is declared "the base for Q3 comparisons". | Q2 10-Q p.76-77 (already read 8/7) |
| 11 | **$99M building identity / appraisal timing** | KB-140 says "NOT yet identified". This is the single most-dated Q3 catalyst. | USGBC LEED directory × gateway-market press; county assessor |
| 12 | **Current short interest** (FINRA 9/15 or 9/30 settlement) | The newest is 6/30 (KB-126). The yfinance route is defective (KB-192). | FINRA equity short-interest file |
| 13 | **Options-implied vol / put pricing** | Zero rows, yet the live book is a Dec-18 $70P | Live option chain (verify the instrument first; yfinance defects logged) |
| 14 | **Credit-rating actions** (Moody's/S&P/Fitch/KBRA on WAL/WAB) | Zero rows. A downgrade is a classic bank-short catalyst. | Agency press releases / KBRA public site |
| 15 | **WAL v. Jefferies NY index number + Point Bonita countersuit docket** | The Cantor docket is held (137); the LAM rail has no docket number, so developments can't be watched | NYSCEF public search |
| 16 | **Tape after 9/23** (9/24–9/25; 9/25 close $77.61, back above EV) | See §1 #24 | market.py / REGINALD exit log |
| 17 | **Q2 13F aggregate** | ✅ present (KB-199, 9/24). Only KB-160's stale Note contradicts it. | — |
| 18 | **Q3 13F** | Correctly absent: not due until **2026-11-14** (45 days after 9/30). KB-199 SB 11/16 is aligned. | — |
| 19 | **MSR valuation / AmeriHome mortgage-banking hedge** | Not tracked. Mortgage banking was the Q2 fee-guide cut driver (KB-117). | 10-Q MSR fair-value note |
| 20 | **ECR-deposit balance (A1)** | The "$4B moved off-balance-sheet" is B2 only (KB-196) | Q3 10-Q deposit table |

---

## Section 5 — Checked clean / could not verify

**Checked clean**
- kb_expiry_check "0 past expiry" is independently verified. The earliest ACTIVE SB is 2026-09-30 (KB-180).
- Blank-SB list: 41, verified ID-by-ID. ACTIVE 167 / SUPERSEDED 42 / 209 rows; all rows have 13 columns.
- predictions_due_check: 2 open, both due 11/15, none overdue. Verified.
- MI3_SERIES arithmetic: all 12 rows (§3c).
- KB-001/002/003/007/127 SUPERSEDED with successors; KB-173 → KB-200 (−0.08%); KB-180's close corrected by KB-190 ($79.15). All match reference truth.
- KB-202/205 carry the 9/28 correction "ownership at failure NOT PROVEN", consistent with reference truth.
- KB-184/188: REG-T-02 fired 9/1 with the sub-78 closes suppressed, consistent with "GATE-REG-T02 terminal". KB-191: Sep-18 pair OTM and live book = Dec-18 $70P ×1, consistent.
- Cantor residual $72.4M / $3.5M is correct on KB-143. The "~$46M" survives only on KB-137 (§1 #2).
- board_log ↔ inbox/WALTER/processed is complete. corrections_boot_check rc=0.
- KB-048: the do-not-cite marker **is present in the row's Notes** (confirmed). Its placement is the defect (§1 #18).

**Could not verify (external or off-slice)**
- Gibbons' exact current title (KB-023 vs KB-130). Needs an 8-K or proxy.
- Basel III endgame / SSFA rule status (KB-013). Class-action filing status (KB-021/057).
- Makhijani docket beyond DEWEY's read (KB-203). Citi's 9/22 PT date (KB-197 says unconfirmed).
- Sep-18 broker booking (FORGE D-58, off-slice).
- Why derived_drift_check suppressed KB-160. Inferred as marker-window suppression (the script's own MARKER_WINDOW=220), not traced line by line.
- Whether the $316M "office classified" vs $316M company-wide Special Mention is a coincidence (KB-151 self-flag). Needs the deck image.
