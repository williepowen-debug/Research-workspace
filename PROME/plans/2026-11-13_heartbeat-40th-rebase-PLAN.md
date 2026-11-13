# HEARTBEAT 40th base — plan and acceptance record

Friday November 13, 2026, PROME prome-72 (desktop, Fable 5.2). Registered as DOCKET line 1137 (decide whether the 11/12 owner records warrant the 40th re-base). Decision: yes. The 39th base is Tuesday 11/10 with two amendments and sits at 74% of its read budget, so the next change is a re-base, never a third amendment. It is stale on the 10-year over 5.0, the 30-year auction, Nvidia's chief-executive exit, the yen's touch of 160, HY back at 320, the oil claims and Friday's chip-led selloff. DOMAIN change; no process-rule change.

## Proposed artifacts and operation
Read the complete proposed text at `PROME/reports/2026-11-13_heartbeat-rebase/candidate.md` against `PROME/reports/2026-11-13_heartbeat-rebase/before.md` (the exact pre-edit HEARTBEAT: 39th base + Amendments 1 and 2). Evidence: `sources.md`, `dashboard.txt` and `fetch_prices.txt` in that directory. On acceptance: `before.md` is copied byte-exact to `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-11-13.md`, then the candidate replaces `HEARTBEAT.md` in one write; `PROME/HEARTBEAT_COLD.md` is not touched.

## Assertions and verification
| Claim | Artifact | Verification | Observed basis | Change |
|---|---|---|---|---|
| The 39th base is stale | before.md | read it | levels 11/10; two amendments; 10Y under 5.0 | re-base, chain → 0 |
| 10Y par over HENRY's 5.0 line on two closes | HENRY close packet; Treasury par CSV | read; PROME's own fetch 16:20 ET | 5.10 [11/12], 5.15 [11/13]; 2Y 4.88, 30Y 5.47 | central, channel 2, kill-on-sight |
| 30Y auction clean; refunding ended without a composition failure | BOND 11/12 packet | read (figures) | indirect 68.11 vs 63.89; dealers 11.39 | central, channel 2 |
| S&P printed under 7,500 and closed above it | HENRY PPI and close packets; fetch_prices.txt | read | low 7,499.40 about 10:22 ET; close 7,561.67 | central, channel 5, kill-on-sight |
| The fall narrowed to chips | HENRY close packet; fetch_prices.txt | read | SMH −2.99%, NVDA −2.01%, QQQ −1.20%, RSP +0.20% | central, channel 5 |
| HY at 320 reset the >320 run | LIQUID 11/13 packet; GATES row GATE-HY-REKILL | read | 320 / 1,314 [11/12]; 0 of 3 after eight observations | central, channel 3, thresholds |
| Nvidia's chief executive resigned, no reason stated | VULCAN 11/12 packets | read (figures) | 8-K Item 5.02 [11/12]; results 11/17 | central, channel 6 |
| Yen touched 160, no close above, no action established | SAM 11/12 packet | read (figures) | high 160.044; close 159.873 | central, channel 4 |
| Oil rose on claims, not barrels | BRENT and FALCON 11/13 packets | read | Jan Brent 95.82 [11/12]; claims CLAIM ONLY | central, channels 1 and 7 |
| HYG ×4 lapsed unfired; QQQ card met its trigger and failed its price | TERRY part-two packet | read | REG-T-04 never fired; $6.23 vs $4.90 | thresholds |
| Oil held its premium on 11/13; positioning gate not gradeable | BRENT part-two packet; GATES row GATE-BRENT-COT-35B | read | settle proxy 95.79 vs 95.82; M1−M3 +4.99; CFTC release 11/16 | channel 1, thresholds |
| Mag-7 slot 10 below yellow | VULCAN 11/13 packet | read | 32.60% [holdings 11/12], breadth +1.72pp | channel 6 |

## Invariants
1. No owner threshold, operator, instrument, consequence, score, frozen prediction or restriction changes. X1 CLOSED/DON'T-SIZE, energy STAND DOWN, Kernel INACTIVE persist.
2. No invented settlement, count, owner grade or trade. Official observations, vendor bars, owner grades and unpublished owner maps stay distinct.
3. The generated book line is pasted whole; no positions or dispositions inferred; no expiry reminders.
4. Full prior bytes preserved in the archive; cold file untouched; every repo pointer resolves after installation.
5. Hot under 70% of 32,550 B; eight channel paragraphs ≤600 B.
6. Kill-on-sight carries the 39th base's still-binding items and its amendments' adds, plus this cut's. Items removed are named below.

## Declared before the plan read
- Removed from kill-on-sight as overtaken or date-bound (they stay binding for their dates in the archive): "December +28.2 bp is a settlement" · "VIX closed above 20" · "HY widened on CPI" · "the oil fall means supply returned" (replaced by "the oil rise means barrels were lost") · "SoftBank rose 13.88% on the results". Amendment 1's "SoftBank has 22.7% leverage" item is carried at 22.5%, the figure Amendment 2 put in its place. "CoreWeave raised its FY2026 capex guide to $37–39B" was Amendment 1 text, not a kill item; the kill item on the guide is carried.
- Dropped from the channels, each staying in the archive with its date: the 11/10 December-meeting pricing and Waller detail (kept in one kill item), the 3Y and 10Y auction figures, TSMC October revenue, the SoftBank results detail beyond the leverage range and the CDS print, the 11/10 oil-fall detail, China's clocks (ZHAO, carried by pointer), Nebius's guide, Trinity Capital's $179.0M, the OCPI index, SoftBank's missing Q2 transcript, the third-carrier line, the 30Y bid-to-cover, SAM's speed row, the 11/6-week distillate build.
- HENRY's close walls are not quoted: HENRY did not publish them under its no-new-level rule; the memo carries the flip, the sign and "walls not published".
- VIX at the 11/13 close is HENRY's 19.03 (vendor bar one minute after the index close); the dashboard cell reads 19.07 and `fetch_prices.txt` 19.36; FRED is unposted. The memo names HENRY's figure in channel 5 and the dashboard's in the table.
- The dashboard's 10Y cell is 5.10 [11/12]; Treasury's 11/13 par (5.15) is named beside it.
- Brent 11/13 is BRENT's settle proxy 95.79 (its 14:28 ET vendor window), not an exchange settle; the vendor's 96.19 at 16:18 ET is a post-settle last and sits in the dashboard table with that label. BRENT's positioning gate could not be graded: the CFTC report as-of 11/10 is delayed to Mon 11/16, so the memo carries the 11/3 vintage and the new review date.
- Not re-read for this base: see `sources.md`. Carried owner lines keep their observation dates.

## Review and disposition
reads: 2 of 2 — **plan read** returned 16:28 ET (Sonnet coldreader; ledger copied to `PROME/reports/2026-11-13_heartbeat-rebase/plan-read.md`): 37 of 44 clean, **1 ❌ · 6 ⚠️**. Kill-on-sight diff against before.md and both amendments: no undeclared removal. Invariants 1 to 6 pass. **❌ fixed before install (one clause):** the central judgment quoted HENRY's unpublished QQQ 680 put wall; it now reads "walls not published". **One ⚠️ fixed as a date error, not as residue:** the central judgment dated the Nvidia resignation 11/12; the 8-K is 11/12 and the board accepted it 11/11 (VULCAN's packet), and the sentence now says both. Installed 16:29 ET after those two edits: archive byte-exact (`cmp`), candidate byte-exact, cold file untouched.

**Residue declared, not fixed (2026-11-13, plan read):** ⚠️ VIX3M/VIX appears at three vintages across the evidence (1.078 HENRY, 1.073 TERRY's first read, 1.069 from `fetch_prices.txt`); the memo carries HENRY's and the plan declared only the VIX level spread · ⚠️ USD/JPY is 159.75 in channel 4 and 159.76 in the dashboard table, two pulls a minute apart · ⚠️ the kill item "3Y and 10Y soft indirects" has no dated figure left in the body (the figures are in the archive) · ⚠️ the near-term calendar's Cass, NEXUS, TIC, RED and custody-release dates were not confirmed by the reader in `state/CALENDAR.md` (not contradicted; weekdays right) · ⚠️ invariant 1 could be misread against the VX-BND-18 red-leg text, which is BOND's own WQ-682 A change relayed, not a PROME change.

**Result read** returned 16:31 ET (Sonnet coldreader; ledger `PROME/reports/2026-11-13_heartbeat-rebase/result-read.md`): **0 ❌ · 4 ⚠️**; install and archive byte-exact, the committed HEARTBEAT still the prior text at the read, cold file unchanged (last committed 2026-10-28), 31 of 31 pointers resolve, book line identical, every dashboard cell matches, eight channels at or under 600 B, 26 figures traced by the reader's own selection with no wrong sign, date, unit or owner; both post-read edits read clean and left no old wording live. No HEARTBEAT edit was made after this read. **Residue declared, not fixed:** ⚠️ Thresholds counts "330 [11/11]" toward the HYG ×5 void clock (2 of 5) while channel 3 and a kill item say the 11/11 row is not an observation under LIQUID's closure rule; both are true (TERRY's void rule counts closes, LIQUID's run counts observations) but the memo does not say so · ⚠️ which VIX and USD/JPY figure is "the close" is not stated · ⚠️ "HENRY's pre-open map 11/16" in Missing links is PROME's expectation; HENRY's packet says open interest arrives with Monday's chain and offers the walls "for a normal wake" · ⚠️ "September revised to +1.4" lacks its unit and prior value (+1.3 → +1.4, per cent m/m). Reads spent; no third read authorized. Any further edit to HEARTBEAT needs an independent read or a new base. Recorded 2026-11-13 16:31 ET.
