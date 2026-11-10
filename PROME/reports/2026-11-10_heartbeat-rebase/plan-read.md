COLDREADER · PROME/reports/2026-11-10_heartbeat-rebase/candidate.md · 17,475 B (measure.py, wc -c; 87 lines) · 46 claims (PLAN READ)
SCORE: 36/46 ✅ · 9 ⚠️ · 1 ❌

## Ledger: claim -> evidence -> result -> note
(candidate line numbers; evidence abbreviations: HEN-ow = HENRY overnight-hike-repricing-waller; HEN-cl = HENRY close-read; HEN-cpi = HENRY cpi-grade; HEN-1500; HEN-qqq; VIO; BND; LIQ; TER; BRT; SAM1/SAM2; BRK1/BRK2; NEX; CARL; RED; FERT; ZH1/ZH2; WALT; GATES = PROME/GATES.tsv; WQ = PROME/WILL_QUEUE.md)

| # | Claim (line) | Evidence | Result | Note |
|---|---|---|---|---|
| 1 | Core CPI +0.3% (+0.296%), headline +0.4%, each 0.1 over consensus, third straight 0.3 core; BLS page unread (L6) | HEN-cpi | ✅ | HENRY: "both 0.1 over consensus, third straight 0.3 core"; "release page itself is unread" |
| 2 | Waller London speech 04:00 ET backed Dec hike, 50 bp "should be considered" if core ~0.3+ (L6) | HEN-ow | ✅ | primary text read by HENRY and verified by SAM2 |
| 3 | December pricing 82% -> 99% "in that minute" (L6, L78) | HEN-ow, HEN-1500 | ⚠️ | HENRY's RESULT line says the same, but his tick data: 95.975 -> 95.950 in the 04:00 minute, 95.945 (=99%) by 04:15; 99% is the 08:25 read. See W3 |
| 4 | Dec ended +28.2 bp, more than one full hike, vendor last trade 16:01 ET not settlement (L6, L10, L78) | HEN-cl | ✅ | |
| 5 | Par 2Y 4.73 (+17), 10Y 4.98, 30Y 5.35 [11/10]; front-led bear flattener (L6, L10) | HEN-cl, BND | ✅ | 11/9 par 4.56/4.88/5.26 |
| 6 | 2s10s 25 bp from 32 (L10) | HEN-cl | ✅ | arithmetic checked |
| 7 | HEN-62 RESOLVED-HIT; 2Y RED (>4.60); 10Y 2 bp under red (L10) | HEN-cl | ✅ | "no band moved" - candidate says "on HENRY's bands", ok |
| 8 | 3Y 11/9 indirect 55.48 vs 57.44; 10Y 61.23 vs 65.05; I' FIRE second in two sessions; dealers 9.77%; auction health holds at 3; no composition failure, no score moved (L6, L10, L78) | BND, LIQ | ✅ | but see W4 (omitted ruling tension) |
| 9 | S&P 7,520.93 (-0.38%); VIX 19.46 (<20 on the print), LOW_VOL holds; VIX3M/VIX 1.061; intraday high 21.43; History unposted (L6, L16) | HEN-cl, VIO, dashboard | ✅ | |
| 10 | SPY +1.99% from Friday's close | sources.md (749.92; 735.29 from 38th base) | ✅ | 749.92/735.29 = +1.99% |
| 11 | NVDA -5.47%, $168.89, single-name second day (L6, L16) | HEN-cl, HEN-cpi, sources | ✅ | second-day label from the 11:10 read |
| 12 | HY 334 [11/9] from 348 [11/5]; 342 [11/6]; CCC 1,311; IG 91 (L6, L12) | LIQ, BND, dashboard | ✅ | |
| 13 | Tier rule STALLS; >320 run MET 8 obs; REG-T-04 0 of 3; rekill 0 of 2; funding eased fifth day (L6, L12, L60) | LIQ §2 | ✅ | |
| 14 | Veterans Day not a session for counts; fix 398a946b9a owner-tested only (L12) | LIQ §1 | ✅ | |
| 15 | HYG fall today a rates move, not measured spread move; 11/10 HY cell publishes 11/11 (L6) | TER §3 | ✅ | TERRY's read is 11:41 ET intraday |
| 16 | Brent settled 92.57 [11/9] from 98.32 [11/6] (-5.85%); low 89.15 08:40 ET; BZF27 91.98 [11/10 vendor] (L6, L8) | BRT, dashboard | ✅ | settle is "EST wire relay" in BRENT's basis column; candidate drops the label (W6) |
| 17 | Qatar interim terms unconfirmed and denied; Trump "highly unlikely"; no barrels returned; Dated Brent $107.03 [11/3] (L6, L8, L78) | BRT | ✅ | BRENT lists JPM/GS surplus calls and Aramco OSP as third driver, omitted (minor) |
| 18 | Boundary #1 (>=$120 x3) not met, "about $29 away" (L8) | BRT | ⚠️ | BRENT's $29 is vs 91.48 at the 14:28 window; candidate pairs it with 91.98 (120-91.98 = 28.02). See W7 |
| 19 | EIA STEO: Q4 balance 0.69 draw -> 1.47 build, supply, consumption unchanged; OPEC spare 0.01 mb/d through Mar 2027; one agency (L8) | BRT | ✅ | |
| 20 | BRT-33 OPEN, 2 of 3 valid sessions (L8) | BRT | ✅ | |
| 21 | SOFR99-IORB +6 bp [11/9]; LIQ-079 NOT ARMED (L10, L62) | LIQ §2 | ✅ | dashboard shows SOFR-IORB -2 (different series, labelled) |
| 22 | MOVE 92.43; dashboard table values: HY/CCC, Brent, 10Y 4.88/SOFR 3.88, USD/JPY 158.76, KRE/OZK/WAL, APO/ARES, TLT/BIZD/ARCC, FSK/OBDC, claims, gas, Cushing (L27-40) | dashboard.txt | ✅ | every cell matches dashboard.txt; stamp 16:35:10 ET = 21:35:10 UTC |
| 23 | USD/JPY high 158.845 [11/10 11:30 ET]; approach to 160 is the live risk; MOF acted before (L14) | SAM2 | ✅ | |
| 24 | BOJ Dec 76% [Totan 11/10], from 52% [11/6]; equivalents not probabilities (L14) | SAM2 | ✅ | 76% read is pre-Waller per SAM |
| 25 | Life insurers net bought Y62.3B foreign bonds Oct, first since May (L14) | SAM2 | ✅ | sector aggregate, not UST-specific (omitted; minor) |
| 26 | SoftBank reported LTV 15.9% [9/30]; SAM roll 22.5% at Arm $183.26; 25% ceiling near Arm $145; finance chief named no asset sale (secondary transcript) (L6, L14, L78) | SAM1, SAM2 | ✅ | caveats omitted: W5 |
| 27 | Gamma: S&P above 7,500, ~1.5% under ~7,635 flip, map not re-run; QQQ/NDX NEGATIVE 11:19 ET, spot under main strike (L16, L50) | HEN-cl, HEN-qqq | ✅ | |
| 28 | HEN-57 NOT FIRED; HEN-63 0.70 open; HEN-58 PPI ladder 11/13 (L16, L65) | HEN-cpi, HEN-1500, HEN-cl | ✅ | |
| 29 | VULCAN 15/25, no letter; TSMC Oct revenue and CoreWeave Q3 (17:00 ET) ungraded; Nvidia announced own investigation 11/8 (AP) (L18) | VULCAN STATUS head | ✅ | "TSMC ... tonight" (L6): VULCAN says TSMC October 6-K 11/10; time of release not evidenced (W9) |
| 30 | NEXUS PRED-38 MISS; smaller filers ~11/16 unread (L18) | NEX | ✅ | |
| 31 | IREN $6B of $15B uncommitted; Microsoft cut not a default on Blue Owl-held loan (BROCK reading, not a lawyer's) (L18) | BRK2, carried | ✅ | |
| 32 | Car-Mart eleventh bridge to Thu 11/12 (L12) | BRK1 | ✅ | |
| 33 | Card flow into 90+ 6.87% [Q3], down from 6.97; 90+ dollars rose (L12, L55) | CARL, NEX, RED | ✅ | |
| 34 | Hormuz B1/C14/D85 HELD, 7 ships lost (FALCON, cutoff 11/9); weekly review 11/11 (L20) | FALCON STATUS | ✅ | |
| 35 | China: every 11/10 clock re-suspended; next cluster Jan 9-11, 2027; 11/27 clock covers graphite and "is not addressed" (L20) | ZH1, ZH2 | ⚠️ | graphite scope ✅; "not addressed" = no extension on MOFCOM list at 11:19 ET (ZHAO), could be read as "nobody addressed it" (W8) |
| 36 | REGINALD Q3 Call Reports (n=14, no skill; L180 BROADER weak) carried; MIDAS 13/20, Oct 30 UNEXPLAINED-DOWN carried (L20, L22) | before.md Amendment 2 / sources.md "carried, not re-read" | ✅ | disclosed as carried |
| 37 | GLD $369.36 (-2.68%) [11/10 vendor], MIDAS not graded (L6, L22) | fetch.py price GLD (re-run by me: -2.68%, as-of 2026-11-10) | ✅ | -2.68% not in sources.md; traced by re-running the tool |
| 38 | FERT: NASS corn 179.6, no fertilizer cause; Oct food at home +0.4% led by beef and snacks, cereals flat; closes on three clean months (WQ-665 B, WQ-666 A) (L22) | FERT, WQ rows 77-78 | ✅ | WQ-666 also requires "no USDA ERS outlook revised up citing input costs" - omitted (minor, in W8) |
| 39 | HYG x5 FIRED on HY 348 [11/5] vs >344, UNFILLED; entry any session through 12/4 at <=$0.60, up-day condition waived this card only (WQ-663 B); HYG x4 NOT FIRED 0 of 3; pair needs Will's word; ORCL NOT FIRED; UNG x5 ended 11/7 (L61) | GATES row 32, TER | ✅ | caveats omitted: W10 |
| 40 | 069 L1 and L4 NOT FIRED on 11/9 session, L4 ungradeable 11/11-11/12; 076 1 of 3, review 11/13; 069/079 review 11/12 (L60) | LIQ §2; GATES review col | ❌ | the 069 gate state "2-of-2 FIRED" dropped. See E1 |
| 41 | GATE-BRK-R2 review 11/16 then 12/7, leg (a) latched WQ-563 A; GATE-FALCON-001 review 11/11 (L63-64) | GATES | ✅ | |
| 42 | Near-term calendar (L67) | LIQ, BRK1, BRK2, DOCKET L811 (Skydance 11/11), RED, FERT | ✅ | Nebius / Athene 11/12 and IEA mid-Nov carried; not in CALENDAR.md grep (UNKNOWN, carried from before.md) |
| 43 | Book line (L70) | `will_brief.py --book-line` re-run | ✅ | byte-identical to candidate L70 |
| 44 | c4022901e8 ANVIL reconcile: Fidelity ties $44,607.15; Robinhood $440.86 "derived and does not tie"; Will declined 8/8 export (WQ-548) (L72) | FORGE/STATUS.md L5, L97; WQ row 71 | ⚠️ | WQ-548 decline ✅; Fidelity tie ✅; FORGE says Robinhood $440.86 is the displayed account value, "NOTHING TIES TO THE CENT", the DERIVED items are $533.90 prior close and line values. "$440.86 is derived" is loose (W11) |
| 45 | Refresh gate passed 16:14 ET, /tmp run directory (L58) | /tmp/prome-boot-a874f4d9/refresh-v07d04x6/gate.txt mtime 16:14:46, PASS | ✅ | |
| 46 | Kernel INACTIVE; invariants: hot under 70% of 32,550 B; channels <=600 B (L75, L84) | measure.py: 17,475 B = 53.7%; channel lengths (C locale, bytes) 524/598/559/587/568/588/580/509 | ✅ | channel 2 at 598 B is 2 B under the cap; ok |

## Invariant checks
1. No threshold/operator/instrument/consequence change: ONE ❌ (E1, 069 fired state silently dropped) and one ⚠️ (W2, QQQ-card T1 FIRED record dropped). X1 CLOSED/DON'T-SIZE, energy STAND DOWN, Kernel INACTIVE persist (L6, L75, L87). HYG consequence wording unchanged except the declared WQ-663 B waiver (matches GATES).
2. No invented settlement/count/grade: ok; 11/9 Brent "settled" is an EST wire relay (W6).
3. Book line pasted whole: ✅ (byte-identical to tool output); no expiry reminders: ✅.
4. Pointers: all candidate paths resolve except the expected archive snapshot (see POINTERS). Plan "Review and disposition" section is EMPTY today; candidate L2 points to it for "declared review residue" (W12).
5. Hot <70%: 17,475 B (53.7%) ✅; channels <=600 B ✅.
6. Kill-on-sight: full diff run. Every item in before.md's body list and Amendments 1-3 "adds" is either in the candidate or named in the plan's declared removals. Verified item by item: no undeclared kill-on-sight removal found. Two kept items whose supporting channel text was dropped: "the ban runs through year-end (January 31, 2027)" (Russia diesel-ban date declared dropped from channels; L78 keeps the kill with no source in the hot file) - W13.

## Ranked findings

### ❌ E1. GATE-LIQ-069 fired state dropped from Thresholds
- Candidate L60: "069 L1 and L4 NOT FIRED on the 11/9 session, L4 ungradeable 11/11 to 11/12; 076 1 of 3, review November 13; 069/079 review November 12 (LIQUID 11/9; GATES governs)."
- before.md L66: "069 2-of-2 FIRED; 076 1 of 3, review November 13; 069/079 review November 12."
- GATES.tsv GATE-LIQ-069 state cell: "LIVE — owner 2-of-2 FIRED unchanged at the 11/6 owner grade: L4 FIRED on the 11/5 session ... fired-leg count unchanged, no new consequence; L1 NOT FIRED ..."
- Why: "NOT FIRED" on a session leg replaces "2-of-2 FIRED" for the gate. A stranger reads 069 as quiet; the gate's fired count (and its consequence "re-run cohort discriminator + flag NEXUS") is not carried. Not named in the plan's declared removals (the plan only declares kill-on-sight/channel/missing-link/book removals). Fix is one clause: "069 owner 2-of-2 FIRED unchanged; 11/9 session L1 and L4 NOT FIRED".

### ⚠️ W2. QQQ-card T1 FIRED (Oct 23) record dropped from Thresholds; held-VLO RESOLVED line dropped; undeclared
- before.md L71: "QQQ-card T1 FIRED October 23 stands as a record; HEN-57 core CPI 0.4+ (November 10), HEN-58 PPI ladder (November 13); NEXUS L554 Tuesday." and L70: "held-VLO gate RESOLVED November 5 on Will's sale of the original share."
- Candidate L65: "HEN-57 NOT FIRED; HEN-62 RESOLVED-HIT; HEN-58 PPI ladder November 13; ..." and L64: "BRENT boundary #1 not met; GATE-FALCON-001 review November 11."
- Plan declared removals contain neither. The T1 FIRED is a fired state of a card (TERRY L? "QQQ $671.83, NOT FIRED, not approved" is a different reading of the QQQ card). Declare or restore.

### ⚠️ W3. "82% to 99% in that minute" outruns HENRY's own tick data
- Candidate L6: "December pricing went from 82% to 99% in that minute (HENRY)"; L78: "Waller's 04:00 ET speech moved it 82% to 99% before the print".
- HEN-ow: "ZQZ26 sat at 95.975 ... then 95.970 -> 95.950 in the 04:00 ET minute ... and 95.945 by 04:15"; HEN-1500 table: 11/9 15:00 = 82%, "11/10 08:25 ET (after Waller, before CPI)" = 99% (95.945). So 99% is the 08:25 level; the one-minute move ends about 95.950 (about 96% on HENRY's 2.8-points-per-tick scale). HENRY's COMPLETION line does say "82% -> 99% pre-print jump happened in the single 04:00 ET minute", so attribution to HENRY is faithful; the stranger-safe wording is "82% to 99% between Waller's 04:00 ET release and the print".
- Also HENRY: "UNKNOWN: positioning or leak story (none found, search not exhaustive)"; candidate states cause without that limit (kill-on-sight L78 is fine).

### ⚠️ W4. BOND's open ruling question not carried
- Candidate L10: "I' FIRE, the second in two sessions ... auction health holds at 3 (BOND)".
- BND §1: "A known reading tension ... VX-BND-01's Threshold_Red text (8/27 ruling) reads I' as sufficient alone. Practice since 9/15 ... treats a bare I' fire as the marker under the WQ-157 pairing ... If Will wants two consecutive refunding I' fires to move the score, the ruling is his."
- A "who owns the call" caveat that could change a score; CLAUDE.md anti-laundering lists "who owns the call". Not in candidate. (Hot file is not Will-facing prose, but the next brief draws from it.)

### ⚠️ W5. SoftBank under-ceiling claim drops two caveats that could change the reading
- Candidate L14: "SAM's roll 22.5% at Arm $183.26; the 25% ceiling is reached near Arm $145; the finance chief named no asset sale (secondary transcript)"; L6: "under its own 25% ceiling".
- SAM1: "Not in any of these numbers: ABB $5.4B, 'Q3 onwards' - If closed debt-funded at cost, about +1.2 points (rough)"; "Gotō on 25% / asset sales: Not read ... Known-unknown"; "SoftBank's own pro forma ... Excludes the $10B October tranche ... with it, 22.4% at $186.30". SAM2: Goto said LTV "should be higher than 15.9%".
- 22.5% + about 1.2 = 23.7%, still under 25 but the headroom the candidate shows (Arm 26% above the ceiling price) is not the headroom after ABB.

### ⚠️ W6. 11/9 Brent "settled" without its basis
- Candidate L8: "settled $92.57 [11/9] from $98.32 [11/6], −5.85%"; L6 same. before.md L14 carried "settled $98.32 [11/6, wire, EST]".
- BRT: "BZF27 settled 92.57 on 11/9 ... Basis: EST wire relay and vendor bars"; plan L34: "Brent 11/10 settle unread; the vendor bar is carried."
- Invariant 2 (official vs vendor stay distinct): the label "EST wire" was dropped from both settles.

### ⚠️ W7. "$29 away" paired with the wrong price
- Candidate L8: "Brent January BZF27 $91.98 [11/10, vendor] ... Boundary #1 (≥$120 ×3) not met, about $29 away."
- BRT: "About $29 away at the 11/10 window (+31%)" where the window price was 91.4819; 120 - 91.98 = 28.02.
- Two prices on one line; the distance belongs to the 14:28 ET window price, not the cited $91.98.

### ⚠️ W8. 11/27 China clock "not addressed" and FERT end-window rider
- Candidate L20: "the 11/27 clock covers graphite and is not addressed (ZHAO)".
- ZH2: "No extension was on the list at 11:19 ET"; "The row omits graphite" (the ROW omitted it, not a document). A stranger can read "not addressed" as "no one has addressed graphite", or as "not extended"; and "WQ-666 A three clean months" (L22) omits "with no USDA ERS outlook revised up citing input costs" (WQ row 77).

### ⚠️ W9. "TSMC's October revenue report tonight" (L6)
- Candidate L6: "CoreWeave and TSMC's October revenue report tonight and are ungraded at this cut."
- VULCAN STATUS head: "11/10 TSMC October 6-K and CoreWeave Q3 (5:00 PM ET) NOT graded at this close". Only CoreWeave's 17:00 ET is timed; TSMC's release time is not in the evidence (L18 and L51 correctly say CoreWeave only).

### ⚠️ W10. HYG x5: rule #6 break and TERRY's added-risk caveat not carried
- Candidate L61: "the up-day entry condition is waived on this card only (WQ-663 B); any session through December 4 at ≤$0.60, read off the broker; the order is Will's hand."
- GATES row 32: "TERRY card f9c8c0bda6, root rule #6 break written with figures before any fill"; TER §3: "a hawkish Fed gives this spread a second way to pay that the card did not underwrite. Construction rule #23: no add on a rates-driven gain." CLAUDE.md: breaking root rule #6 only with the measurement written on the card before the fill.
- A reader of the hot file alone sees a waiver without the condition on its use.

### ⚠️ W11. Robinhood "$440.86 is derived and does not tie"
- Candidate L72: "Robinhood $440.86 is derived and does not tie".
- FORGE/STATUS L97: "Account value $440.86 ... so $533.90 at the prior close (DERIVED)"; "NOTHING TIES TO THE CENT (D-98)"; "Σ DERIVED line values $416.75 leaves $24.11 unshown".
- $440.86 is the displayed value; derived are the line values and prior close. Loose, not wrong in direction.

### ⚠️ W12. Pointer to content not yet written
- Candidate L2: "Plan, verification and declared review residue: PROME/plans/2026-11-10_heartbeat-39th-rebase-PLAN.md"; L84: "Plan/read record above carries declared residue and source limitations."
- Plan file ends at "## Review and disposition" with nothing under it. Must be filled before install, else the pointer is dead at install.

### ⚠️ W13. Kill-on-sight keeps a fact the hot file no longer supports
- Candidate L78: "'the ban runs through year-end' (January 31, 2027)".
- Plan declared: "Dropped from the channels: ... the Russia diesel-ban date ..." ; before.md L14 held "Russia's producer diesel ban runs to January 31, 2027 (№1436)". Kill item stays binding (not an invariant breach) but its antecedent ("the ban") is now undefined in the candidate.

### ⚠️ (own check C5) CHG-RED-045 clause drops its decision owner
- Candidate L55: "CHG-RED-045 to 11/17".
- RED: "Open to 11/17 only for Will's reopen decision"; CARL: "the divergence is not a request; only Will can reopen the 8/16 choice"; CARL ACTION: "carry the §1 divergence below to Will as a fact".
- The candidate states the superseded rule would not-fire? It says (kill list L78) only "ratified rule reads NOT FIRED". The fact that the superseded rule WOULD read FIRED and that Will owns the reopen call through 11/17 is absent. (Counted within the W numbering as part of "who owns the call"; listed here as the tenth ⚠️ in the SCORE.)

## Checks I devised beyond the brief
- C1. Re-ran `FORGE/tools/market-data/fetch.py price GLD` (as-of 2026-11-10, -2.68%) to trace a figure sources.md does not support; re-ran `will_brief.py --book-line` and diffed it against L70: identical.
- C2. Arithmetic recomputation: 749.92/735.29 = +1.99%; 4.98-4.73 and 4.88-4.56 give 25 and 32 bp; 92.57/98.32 = -5.85%; 28.2/25 = 1.128 (13%); (7,635-7,520.93)/7,520.93 = 1.52%; 120-91.98 = 28.02 (vs the "$29" in L8, W7); 22.5% + 1.2 = 23.7% (W5).
- C3. Byte-level channel cap in C locale (awk length): channels 524/598/559/587/568/588/580/509 B; channel 2 is 2 B under the 600 cap; total 17,475 B = 53.7% of 32,550.
- C4. Weekday check for every dated weekday in the calendar (Tue 11/10, Wed 11/11, Thu 11/12, Fri 13, Mon 16, Tue 17): consistent with the 38th base's Friday 11/6.
- C5. GATES.tsv review_by column for 069/079 (11/12), 076 (11/13), FALCON-001 (11/11), BRK-R2 (11/16), HYG follow-01 (12/4): all match the candidate.
- C6. Refresh-gate claim traced to /tmp/prome-boot-a874f4d9/refresh-v07d04x6/gate.txt (mtime 16:14:46 ET, PASS).
- C7. Direction test on each "NOT FIRED / FIRED" state against owner packets: only 069 reads differently (E1). WQ-663/665/666/548 rows verified verbatim in WILL_QUEUE.md.

POINTERS: 33/34 resolve; dead: PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-11-10.md (expected until install). Tested: 15 AGENTS/*/STATUS.md, PROME/{GATES.tsv, DOCKET.tsv, WILL_QUEUE.md, HEARTBEAT_COLD.md, SCRATCH.md, state/CALENDAR.md, themes/ellison/, tools/measure.py, tools/will_brief.py, plans/...PLAN.md}, FORGE/STATUS.md, USER.md, dashboard.txt, sources.md, and all 23 packet files named in sources.md under PROME/inbox/processed/ (23 of 23 resolve; the three "..._" shorthand entries in sources.md expand to existing files). Not resolvable by file: "DOCKET L247" (a bare line reference carried from the 38th base; DOCKET.tsv line 247 is a KERNEL row, consistent with the Kernel line); commit c4022901e8 exists as a commit.
ONE-LINE VERDICT: Mostly yes, with one fix first: the central judgment, channels 1-8, the dashboard table and the kill-on-sight list all trace to the owner packets, but the Thresholds line drops GATE-LIQ-069's "2-of-2 FIRED" (E1) and the plan's review-residue section is empty (W12); fix those two and declare or restore the dropped QQQ-card T1 record (W2) before install.
