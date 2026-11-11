# LIQUID — Wednesday November 11 catch-up (Veterans Day: bond market shut, NYSE open)

**Launched by** PROME prome-2b on WQ-184 and Will's 09:24 ET word, desktop, Claude Code / Opus 5.5. Research only, $0. No trade, card, gate, band, threshold, letter or charter moved.

## 1. November 10 HY cell (first-published)

**PENDING: not published by 10:53 ET.** FRED is updating (VIXCLS and T10Y2Y for November 10 posted), but the whole ICE family (HY, IG, BBB, BB, B, CCC) still ends at November 9, and SOFR and H.15 for November 10 have not posted either (Fed holiday). A poll runs every 60 s until 17:00 ET; most likely first publication is Thursday about 10:10 ET (KB-LIQ-151 says T+1 morning; the holiday makes it T+2). PROME prome-2b told at 10:06 and 10:53 ET.

**Rules ready for the cell (no rule changed):** >320 first-published run goes to 9 at 321 or more, resets at 320 or less (8 through November 9). REG-T-04 (>350 ×3) is REGINALD's count; 348 [November 5] is the high. GATE-HY-REKILL needs <260 ×2. Tier rule (September 25 order) on d/d against November 9 (IG 91, BBB 113, BB 200, B 350, CCC 1,311) and the 15-session base.

**Veterans Day session rule (398a946b9a, owner-tested only):** today's handling matches it. November 10 is a priced ICE session and will count as an observation when it posts. Any November 11 cell FRED prints is a carry and counts for nothing; 069 L4 is UNGRADEABLE for the November 11 and 12 sessions. Nothing was graded off the absent cell.

**Context, grades nothing:** HYG $77.25 (+0.09%), JNK $92.71 (+0.08%) at about 10:06 ET with the bond market shut (vendor last trades; ETF prices mix duration and spread). T10Y2Y 0.25 [November 10, FRED] from 0.32: the curve flattened 7 bp on the rate repricing. December Fed-meeting pricing is ORACLE's (WQ-671 A): hold 3.5, +25 bp 85.5, +50 bp or more 11.8, futures about +28.9 bp [ORACLE KB-ORC-133, 09:45 ET 11/11].

## 2. SoftBank Group: Tokyo-hours credit after the Q2 results (D:L1110, LIQUID leg)

**Answer: credit took the results calmly. CDS came in, yen bonds slipped about 1.5 bp against peers. No rating action.**

### 2a. CDS, DTCC public dissemination (SEC regime), intraday slices 1 to 224 of November 11, read about 10:00 ET

The November 11 cumulative file is not posted until about 20:15 ET; the intraday slices (`ppd/api/report/intraday/sec/SEC_SLICE_CREDITS_2026_11_11_<n>.zip`) carry the same rows as they are reported. All SoftBank rows are yen, 100 bp coupon, quoted as an upfront. Conversion: flat hazard, rate 1% (yen), recovery 40%, not the ISDA model, good to about ±10 bp (method checked 11/10 against a disseminated 438 and Reuters 466; `research/2026-11-10_softbank-credit/REPORT.md` §1a).

| Execution (UTC / JST) | Tenor (maturity) | Upfront, points | Converted bp | Platform | Comparison |
|---|---|---|---|---|---|
| 03:40Z / 12:40 JST, Tokyo hours | 3Y (Dec 2029) | 9.51 on ¥500M | **464** | UTSL | 459 [11/10 02:10Z, before results] |
| 06:00Z / 15:00 JST, Tokyo close | 3Y (Dec 2029) | 9.25 on ¥500M | **453** | UTSL | same |
| 08:10Z / 17:10 JST, London morning | 8Y (Jun 2034) | 21.66 on ¥550M | **508** | BILT | no earlier print read |
| 08:13Z / 17:13 JST, London morning | **5Y (Dec 2031)** | 14.95 on ¥500M | **475** | BILT | **497** median [11/9], **496** [11/10 08:01Z, one print] |

The 5-year row appears four times (NEWT plus CORR copies of one trade, same identifier time and upfront); counted once. A late-reported 11/9 5-year row (08:32Z, 513) also sits in these slices; it is the top of the 11/9 range already recorded.

**Read:** the 5-year printed about **21 bp tighter** than the one after-results print of 11/10 and 22 bp under the 11/9 median, on one trade, just after the Tokyo close. The 3-year inside Tokyo hours ran 464 then 453 against 459 before the results: flat. n = 3 trades on dissemination with a US nexus; most SoftBank CDS trades Tokyo and Hong Kong between non-US dealers and does not appear. A sample, not the market.

### 2b. Yen bonds, JSDA OTC reference prices (the 429 block has cleared)

Files `ES261110.csv` (quotes 15:00 JST 11/10, **before** the 15:30 JST results) and `ES261111.csv` (15:00 JST 11/11, after the results and the first session), fetched about 10:00 ET 11/11, one request each. Average compound yield, column 7.

| Group | n | Yield change 11/10 → 11/11 | Basis |
|---|---|---|---|
| SoftBank Group senior (No. 58 to 70, 2027 to 2033) | 13 | **+1.3 to +2.6 bp, median +2.2** | JSDA |
| SoftBank Group subordinated 3, 4, 5 (2028 to 2029) | 3 | +1.8 to +2.5 bp | JSDA |
| SoftBank Group perpetual-style subordinated 6 to 9 | 4 | price −0.03 to −0.12 points; no yield quoted | JSDA |
| JGBs, 2029 to 2030 / 2031 to 2033 | 48 / 53 | +0.5 / +1.0 bp median | JSDA |
| All other corporates, 2029 to 2030 / 2031 to 2033 | 1,013 / 866 | +0.5 / +0.9 bp median (90th percentile +0.9 / +2.2) | JSDA |

**Read:** SoftBank's yen senior curve moved up in parallel by about 2 bp, about **1.5 bp more than JGBs and other corporates** of the same maturity; in the 2029 to 2030 bucket every SoftBank line sat above the other corporates' 90th percentile. Price cost about 0.05 to 0.10 points. A small, orderly, issuer-specific cheapening, not a dislocation, on reference quotes (dealer-reported, not trades). The 2031 No. 64 3.15% at 95.91 yields 4.048%.

### 2c. Ratings since the results (searched 10:03 ET)

| Agency | Read | Basis |
|---|---|---|
| JCR | A/Negative, J-1; latest release September 4 (bond assignment); **no action since the results** | JCR rating list page, fetched 10:04 ET |
| S&P | BB+/Stable (Negative → Stable July 16) per issuer page "as of November 10"; no new action found | SoftBank IR ratings page fetched 10:04 ET; web search, no November item |
| Fitch | BB+/Stable (assigned September 11); no new action found | same |
| Moody's (unsolicited, disputed by SoftBank) | Ba2 last verified action September 2025; nothing new found | search only |

**RED's ask (11/10 packet, S&P outlook conflict):** already corrected in STATUS §1 on 11/10 (BB+/Stable from 7/16, from SoftBank's deck p.71 and IR page); confirmed again today on the IR page. The "Negative since 3/3" in my 11/10 packet was a stale relay. S&P's own page not read.

## 3. Skydance (Paramount Skydance) after the Q3 10-Q (WALTER SIG-W-20261111-007, ACTION LIQUID)

### 3a. Legacy Paramount Global 5-year CDS, DTCC (USD, 100 coupon, converted rate 4%, ±10 to 20 bp at these upfronts)

| Date | Dec 2031 contract, median converted | n |
|---|---|---|
| September 15 | 300 | 1 |
| October 1 | 428 | 13 |
| October 6 (close of the merger) | 437 | 4 |
| **October 15 (high)** | **614** | 5 |
| October 28 (low since) | 430 | 7 |
| November 3 / 4 | 479 / 443 | 4 / 3 |
| **November 9 (latest print)** | **529** | 2 |
| November 10 / 11 to about 09:40 ET | no print | — |

Debtwire quoted 577 on October 13 (secondary); my October 13 median 584. **Read:** the legacy CDS doubled from mid-September to the October 15 high, gave back a third, and was re-widening into the 10-Q (529 [November 9] against 443 [November 4]). Nothing printed after the filing. "Paramount Global" is the legacy reference entity; whether the new obligor's debt delivers into it is a succession question I have not read. Discovery Global 5-year: 590 [November 9, one print].

### 3b. The new first- and second-lien notes

No free primary for secondary prices on this box: TRACE unreachable, no vendor. The only levels are secondary and dated: USD second-lien notes 93.58 to 96.88 and EUR second-lien 98.10 **[October 13]**; 7.050% first-lien 2031 272 bp OAS and 8.875% second-lien 2034 483 bp OAS **[undated]** (all Debtwire via ION Analytics, 14 October). Not current; not a grade.

**Ratings (as reported, secondary):** S&P issuer BB (cut from BB+ September 24), first lien BBB-, second lien BB; Fitch issuer BB (cut from BB+); Moody's Ba3 CFR, first lien Ba1, second lien B1, stable. No action since the 10-Q found.

### 3c. A post-close leverage figure: yes, three, on different bases (none from the company)

| Figure | Basis | Source, date |
|---|---|---|
| **about 4.51x total net**, first-lien net **2.38x** | **covenant definition**: Consolidated Adjusted EBITDA adds back run-rate synergies uncapped, so the full $6.0B counts; LTM June 2026 | Debtwire estimate, October 14 (secondary) |
| 4.63x total net | covenant basis, 2027E | same |
| **6.16x net** | economic: 2027E adjusted EBITDA $13.7B with only $1.75B realized synergies; net debt $84.3B (gross $89.3B, cash $5.0B est.) | same |
| **7.6x** adjusted debt / EBITDA, 2026 | S&P projection, synergies counted only when realized; not below 5x until 2029 | S&P via Variety/Yahoo, May 20 (pre-close) |

Covenants (filed): total net ≤ 5.50x, first-lien net ≤ 3.25x. **⚠️ The direction of the answer depends on the basis.** On the covenant's own definition the estimate is about 4.5x, about 1.0x of headroom. On any economic basis it is already above 5.50x (6.16x, 7.6x). TERRY's re-open condition names "a leverage figure near 5.50x"; which basis that means is TERRY's call. **Gross debt check:** Debtwire's $89.3B against PROME's inferred $86.6B face, a $2.7B gap that is the WBD notes' treatment or fees; not reconciled. None of these is a filed figure; the 10-Q states no post-close leverage or headroom (PROME's read, confirmed by WALTER card).

## 4. CoreWeave after its results (DDTL 5.5 $2.6B closed, ATM up to 35M shares) against Oracle

**Answer: no CDS has printed since the results yet, so credit's verdict is not in. Pre-results, CoreWeave 5-year sat about 850 bp over Oracle's. The equity market cheered both names.**

| | CoreWeave 5Y (Dec 2031; USD, 500 coupon) | Oracle 5Y (Dec 2031; USD, 100 coupon) | Basis |
|---|---|---|---|
| November 6 | about 1,227 to 1,252 | 305 disseminated | DTCC, prior reports |
| November 9 | about 1,136 (one print) | 301.5 disseminated | same |
| **November 10, before results** | **1,143 to 1,166, median 1,154** (7 prints, 16:49Z to 20:41Z) | **300 and 302 disseminated** (TPSB ×2, GSBS ×2); 302 converted (BILT ×2) | DTCC November 10 final file (last execution 23:17Z), read 10:00 ET 11/11 |
| **November 11, after results** | **no print** through 15:30Z | **no print** | DTCC intraday slices 1 to 232 |
| CoreWeave other tenors 11/10 | 1Y 811, 3Y 1,061, 4Y 1,093 to 1,105 | 1Y 108, 3.5Y 246, 4Y 271, 4.5Y 288 | converted |

CoreWeave's conversion is the probe default (rate 4%, recovery 40%, buyer-pays upfront), good to tens of bp at this distance from the coupon. Ratio about 3.8x; gap about 850 bp, pre-results.

**Why no read yet:** the bond market is shut. DTCC disseminated about 9 credit rows an hour this morning, a fraction of a normal day. The first after-results CoreWeave and Oracle CDS should come in Thursday's US session; the November 11 cumulative file (about 20:15 ET) will show any late prints.

**Equity, context only:** CRWV $58.58 (+20.22%), ORCL $125.89 (+6.70%) at about 10:06 ET (vendor last trades). **What the results add to the credit question:** DDTL 5.5 ($2.6B) closed, so committed secured debt keeps arriving; an ATM of up to 35M shares is equity issuance, which helps creditors (about $2.05B at $58.58, my arithmetic, if all sold at that price). Nothing pulled or flexed (VULCAN KB-417). On the AI-HY spread tells (KB-LIQ-069/073) nothing re-arms on what is read. The 10-Q (about 11/12) is VULCAN's primary.

## 5. Inbox drain (every sender)

| Item | Disposition |
|---|---|
| WALTER SIG-W-20261110-012 (card 010 correction, SoftBank loss at Silver Bands 7) | noted; COR-20261110-12 receipted NO-OP (no LIQUID record carried the Ohio line) |
| WALTER SIG-W-20261111-004 (small items) | noted; SoftBank close used as context in §2 |
| WALTER SIG-W-20261111-007 (Skydance 10-Q, ACTION LIQUID) | acted, §3 |
| WALTER SIG-W-20261111-011 (ORACLE December Fed odds) | noted; cited in §1 under WQ-671 A |
| RED 11/10 (S&P outlook conflict) | answered: already corrected 11/10 to BB+/Stable; re-confirmed on SoftBank's IR page 11/11 (§2c) |
| PROME 11/11 WQ-671 RULED A (ORACLE owns December Fed pricing) | applied: STATUS, MEMORY and CALENDAR carry no December-meeting price; today's report cites ORACLE. The 11/10 report §19.2 attributed it to HENRY; that is a dated record, left as written. |

## 6. Sources and method notes

- DTCC intraday slice endpoint `pddata.dtcc.com/ppd/api/report/intraday/sec/SEC_SLICE_CREDITS_<date>_<n>.zip` gives same-day rows before the cumulative file; numbered from 1 and 404 past the last. New to this desk; worth a KB row.
- JSDA served both files today with a browser user-agent, one request each; the 429 of 11/10 has cleared.
- Leverage estimates for Skydance came through a web-fetch helper reading ION Analytics/Debtwire (October 14), Variety via Yahoo (May 20), RBR (paywalled), fi-desk (November 10); Moody's page returned empty. All secondary.
