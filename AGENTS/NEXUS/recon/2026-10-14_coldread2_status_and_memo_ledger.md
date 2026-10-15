COLDREADER (read 2, scoped) · A = AGENTS/NEXUS/STATUS.md (focus lines only, uncommitted tree) + B = PROME/inbox/2026-10-14_from-NEXUS_catch-up-reanchor-S1-C1-committed-M06-letter-DEFECTIVE-PRED50-closed.md (whole) · 22,761 + 8,780 B · 88 claims
SCORE: 67/88 ✅ · 20 ⚠️ · 1 ❌

❌ 76 B §4 L42 "**RED:** live tonight. FT-08 (core 3-month 3.2 ≥ 3.0) and FT-10 (SKEW 3 of 4) grades are uncommitted at my read." contradicts B §5 L59 "`RED-FT-08` FIRED — core 3-mo 3.247%, net-bear 60 → 63 [RED S52 `b79c04c9a`]", A L85 "**FIRED — RED S52 `b79c04c9a` 10/14 20:23: net-bear 60 → 63.**" and A L52 "ONE CPI print — RED graded". `git show b79c04c9a`: 2026-10-14 20:23:57, "FT-08 fired … FT-10 3 of 4 pending … official 10/14 Cboe bar absent at 20:23 ET". This is read 1's ❌69 surviving in B: the pass record §G L58 still says "RED live, FT-08 / FT-10 grades uncommitted at this pass", and §4 was copied from it. FIX: "RED: committed `b79c04c9a` 20:23:57. FT-08 FIRED (net-bear 60 → 63). FT-10 at 3 of 4, waiting on the 10/14 Cboe bar (RED grades it on publication)."

⚠️ 82 B §5 L65 "In the tails, yes; in the center, no … The center is IG, funding, breakevens, index vol under 18 and the long end, and all of it held." This sits under "What tonight's inputs say", but the center cells are pre-CPI: L61 has IG 83 and HY 316 with no date and "funding SOFR−IORB −1 [10/13]"; A L11 says "Credit/rates = FRED obs 10/13". Only breakevens [FRED 10/14], VIX [10/14c] and the long end [BOND 13:59] are post-CPI. "Index vol … held" is also stronger than A L105 "Index vol rising off the floor" and L110 "a VIX only now lifting" (15.27 → 16.87). And L67 lists "the 4th SKEW close" as a line the CENTER has to cross, after L65 defined skew as a tail. The table supports "tails yes"; it does not show the center holding through CPI. FIX: "center: no post-CPI move where measured (breakevens 2.35 [10/14], long end retraced [BOND 13:59], VIX up 15.27 → 16.87 but under 18); IG / HY / funding are 10/13 cells, unread for CPI day". Move SKEW out of the center's nearest lines.
⚠️ 57 A L128 "bottom-tier widening the AI-disruption mechanism failed to explain (VULCAN; LIQUID neutral)". The hatches are dropped here, against A L9 "⚠️ Hatches open: equities stand in for credit; a lagged catch-up is untested" and VULCAN L59 "Lagged-equity catch-up | **Not excluded** | UNKNOWN". This is the only summary line that lost them; the bottom line L143 keeps "equity proxy, lag untested". FIX: append "(on an equity proxy; lag untested)".
⚠️ 36 A L52 C1 "ONE CPI print — RED graded, ORACLE · MARCO · CARL owe". Late mover: `23ee5bdf7` 2026-10-14 20:37:31 "MARCO: s32 catch-up — … ENR-02 leg 1 passed", and MARCO STATUS L87 "✅ read 10/14 | … CPI Sep (ENR-02 leg 1, F&V)". Also unconsumed: `inbox/WALTER/SIG-W-20261014-023.md` (00:38Z = 20:38 ET, RED FT-08 update). Closeout 9c applies. FIX: "RED · MARCO graded; ORACLE · CARL owe", and consume -023 or defer it in writing.
⚠️ 49 A L85 "Oil→core leg (CHG-028) NOT MET … Composition → 11/10." This drops RED's consequence. RED packet (processed): "NOT MET …, so REALIZED is foreclosed for 11/10". RED commit: "REALIZED foreclosed at 11/10". WALTER -023: the "'still needs November 10' [line] is now incomplete". FIX: "Composition → 11/10 (REALIZED already foreclosed, RED)".
⚠️ 33 A L50 "gasoline carried over half the HEADLINE". The compression removed the base: the only headline figure left on the board is A L21 "headline 3.7% y/y". RED's packet says "over half the monthly increase", and HEARTBEAT #3 says "+0.6% m/m … gasoline +9.1% m/m = over half the headline". NEW (introduced by the rewrite). FIX: "gasoline (+9.1% m/m) carried over half of the +0.6% m/m headline".
⚠️ 81 B §5 L60 "the 10/14 bar is unpublished" omits A L23 "delayed print 157.30 is provisional", which is ≥150 and therefore points at an FT-10 fire. If FT-10 fires tomorrow, this is a "you didn't tell me" item. FIX: add "(a delayed 157.30, RED provisional, would qualify)".
⚠️ 64 B L6 "BRENT confirmed on 10/9 that no settle source exists". The scope is widened: pass record §D quotes BRENT "NO SETTLE SOURCE AVAILABLE TO BRENT", and B L23 drops "TO BRENT" (Disc-I). FIX: "no settle source is available to BRENT".
⚠️ 10 DOCKET L558 is dated 2026-10-16 (DOCKET.tsv). A L8 says "dated 10/16", but A L120 and B §2 L24 run it Mon 10/19, and B asks only for a "consumer note", not a re-date. A 10/16 wake will fire with nothing planned. FIX: ask PROME to re-date L558 to 10/19.
⚠️ 3 Two different "four state changes". A L3 lists "PRED-50 · WQ-341 · M-06 · RaDD"; B L6 says "Four state changes: (1) S1 … (2) M-06 … (3) PRED-50 … (4) VULCAN". RaDD (extended; loss recognition UNKNOWN) appears nowhere in B, which PROME is to carry to Will. Note that PROME registered WQ-425 "OZK put timing" at 20:37 (`305cce45f`). FIX: one five-item list in both files.
⚠️ 61 Two priors for the Oct-28 +25bp odds. A M-03 L22 has "≈36% … vs 15.5 / 18.0 [ORACLE 10/9]"; A T-26 L73 and B caveat 3 have "~22% → ~36%". The ORACLE pair is still unlabeled (read-1 ⚠️30), and pass record §G says "ORACLE FOMC forward row contradicts its 10/9 line". FIX: label the ORACLE pair, and say 22% is BOND's prior bar.
⚠️ 78 B §5 L54 "Cell 11 … made a five-run impossible before cell 15". This is read-1 ⚠️73's wording surviving in B: it implies a run could complete AT cell 15. A L7 and B §2 L24 are correct. FIX: "broke the last five-run that could complete by cell 15".
⚠️ 9 A L7 and B L59 "(RED 60/40)" sit beside "net-bear 60 → 63". The RED packet defines it as "RED weights that 60/40 for 'no spiral'". FIX: "(RED: 60/40 no-spiral)".
⚠️ 80 B L62 "VIX 16.87 · VVIX 97.25 (14:38) [10/14, your dashboard]". VVIX is VIOLET's 14:38 figure (HEARTBEAT #3: "VIOLET 15:10 ET … VIX 17.08 … VVIX 97.25 at 14:38 ET"), so a close and a 14:38 snapshot share one label. TLT 78.89, BAC NCOs, IG 83 and HY 316 carry no date or source in the B table.
⚠️ 71 B L23 and L77 use bare "L630", "L558", "L554 / L630 / L558 / L553" (DOCKET rows) next to "L15" (a PREDICTIONS_MONITOR row) in the same cell. The charter rule says "PROME docket rows are ALWAYS written `DOCKET L<n>`".
⚠️ 17 · 26 · 35 · 44 · 68 · 85 (low; full text below)
POINTERS: 48/48 resolve; dead: none.
ONE-LINE VERDICT: A, yes: all four read-1 ❌ are fixed everywhere in A with no reversal. The residue is one dropped hatch (L128), one compression that lost the CPI base (L50), and two late movers (MARCO, WALTER -023). B, not yet: §4 still says RED's FT-08 grade is uncommitted while §5 cites the commit. §5's "center held" leans on pre-CPI 10/13 cells. Caveats 1–4 do survive intact.

---

## Check answers (spawner's 1–4)

(1) Were read 1's four ❌ fixed? In A, yes, with no rephrased reversal.
- VULCAN: A L9 "3 of 4 on 9/29, CABO z −1.8 read as issuer-specific; 4 of 4 on 10/7". This matches VULCAN L6/L34/L56.
- LIQUID: A L9/L44/L74/L143 "neither shows nor refutes". "Repriced by quality" is now LIQUID's own words (LIQUID L75: "The whole ladder repriced by quality"). "quality repricing", "returned against" and "both reads" are absent from both files.
- RaDD: A L62/L143 carry "loss recognition UNKNOWN". "benignly" and "de-risk" are absent. M-05's "Secondary cause RESOLVED" keeps its caveats in the same cell.
- FT-08: A L85/L7/L72/L143 say FIRED with the commit.
- In B, ❌1–3 are fixed (§3 L29–37). ❌4 SURVIVES at B L42 (❌76).
- Near-residue: A L128 drops the hatch (⚠️57), and B L54 keeps read-1 ⚠️73's wording (⚠️78).

(2) New errors from the compression:
- ⚠️33: CPI m/m base lost.
- ⚠️49: "REALIZED foreclosed" not carried.
- ⚠️36: late movers.
- ⚠️82: headline stronger than its cells.
- Restored correctly: M-06 frozen letter; M-10 "never two votes"; M-11 "never sum" / "0.1¢"; T-29 Aramco; T-30 "No registered threshold"; LIQ-076 review 10/30; the C1 10Y guard; the DOCKET prefixes in A; the L554 re-date note; the BOND kill marked one-shot; the L13 row moved to NOT CONFIRMING "DEAD".
- FLG "T-08 · RGB freeze" was legitimately dropped: GATES header "10/09 terminal pass: 1 row (GATE-FLG-T08) → archive".
- LIQ-07 "final 10/16" is now owner-sourced (LIQUID STATUS L12: "final read October16 after funding publication").

(3) B §5:
- Mostly dated and sourced; the exceptions are ⚠️80.
- "Tails yes": supported (SKEW 3 of 4, CCC window high, QQQ −1.97%).
- "Center no / all of it held": only partly supported (⚠️82).
- Caveats 1–4: all four survive in B, and each has a home in A (L8 · L9/L143 · L40/L22 "not certified" · L17/L25).
- Caveat 2's "tonight" re-dates 10/9 reads (⚠️85).

(4) Cross-line figure checks:
- No hard figure contradiction between A and B, other than ❌76 and the two priors in ⚠️61.
- Arithmetic re-checked: CCC +38 / B +9 / BB +2 / IG +1 since 10/7; CCC−IG 1,184 vs 1,147; VIX 1.13 to 18; HY 4bp; T10YIE 5bp; IG 11bp; FT-08 3.247%.

## Full ledger

| # | Where | Claim | V | Note |
|---|---|---|---|---|
| 1 | A3 | 10/14 Wed 20:23; 5 dark days; 853 commits | ✅ | B L6 10/9 18:43 → 10/14 20:11 |
| 2 | A3 | No letter fired; no Conf % moved; split HELD | ✅ | |
| 3 | A3/B6 | State-change lists | ⚠️ | See above |
| 4 | A3 | "WQ-341 mechanism leg FAILED (VULCAN; LIQUID neutral)" | ✅ | |
| 5 | A4/A15 | One delta list 10/1 · 10/8 · 10/9 · 10/14 | ✅ | Read-1 ⚠️7 fixed |
| 6 | A6 | 20/47/33, re-dated 10/08, HELD | ✅ | |
| 7 | A7 | L13 letter; cells 1–12 (12 values counted) | ✅ | |
| 8 | A7 | "Only cells 13–15 remain … C#1" | ✅ | |
| 9 | A7/B59 | "(RED 60/40)" | ⚠️ | See above |
| 10 | A8/A120/B24 | DOCKET L558 dated 10/16, run 10/19 | ⚠️ | See above |
| 11 | A9 | PRED-50 CLOSED, §C6 | ✅ | §C6 L326 "all 27 logged cells unchanged" |
| 12 | A9 | VULCAN 3 of 4 / CABO z −1.8 / 4 of 4 | ✅ | VULCAN L6, L34 |
| 13 | A9 | LIQUID neither/nor; "repriced by quality" | ✅ | LIQUID L75, L79 |
| 14 | A9 | Hatches; Root B CANDIDATE UNSUPPORTED; eff-N 1+1 | ✅ | |
| 15 | A11 | Positions → FORGE (vintage in its header) | ✅ | Read-1 ⚠️18 fixed |
| 16 | A11 | TLT 82P CLOSED 10/12 | ✅ | |
| 17 | A11 | TBT "WQ-357's 10/14 clock — no decision recorded at my read" | ⚠️ | Honest, but has no docket or next-boot line. HEARTBEAT #3 also has no outcome. Add "(d) WQ-357 outcome" to next-boot |
| 18 | A11 | WQ-360 LAPSED 10/14 | ✅ | HEARTBEAT #3 "LAPSED 15:00 ET today unapproved" |
| 19 | A11 | [10/14c] = PROME dashboard close (HEARTBEAT #3) | ✅ | |
| 20 | A11 | BZZ26 LTD Fri 10/30, corrected from 10/29 | ✅ | Declared |
| 21 | M-04 | VIXCLS, SKEW 3 of 4, 157.30 provisional, HENRY gamma, letter | ✅ | Anchor L 15.41 still unprinted (minor) |
| 22 | M-05 | RaDD extended with in-cell caveats; FLG/WAL/OZK/KRE | ✅ | OZK/WAL/KRE = HEARTBEAT dashboard |
| 23 | M-06 | DEFECTIVE; frozen letter shape restored; 10/19 | ✅ | |
| 24 | M-06 | Sinking (type unconfirmed); loss count; Dhahran/Shedgum; IEA Sept / Middle East | ✅ | Read-1 ⚠️35/36/37 fixed |
| 25 | M-07 | IG 83 · 83* · 83; funding; LIQ-079 | ✅ | Read-1 ⚠️40 fixed |
| 26 | M-07 | BAC "$1.349B vs $1.412B Q2" | ⚠️ | "Q2" is not in the pass record (§E: "NCOs $1.349B vs $1.412B (0.44% vs 0.47%)"). Label is unsourced |
| 27 | M-08 | Letter; B 317; CCC 1,267; CCC−BB; "+38 vs B +9 · BB +2 · IG +1" | ✅ | Read-1 ⚠️43 fixed |
| 28 | M-10 | Rides L11; "never two votes"; ZHAO interval | ✅ | |
| 29 | M-11 | DOCKET L673; perimeters; never sum; 0.1¢; letter | ✅ | |
| 30 | R1 | Proxy ~36% not certified; T10YIE/T5YIFR [10/14]; HENRY dark | ✅ | Pass record §C 10/14 column |
| 31 | R3 | B +7 on 10/13; LIQ-07 final 10/16; BRK-31 | ✅ | LIQUID STATUS L12, L47 |
| 32 | R4 | Two faces; Root B wording | ✅ | |
| 33 | R5 | "over half the HEADLINE" | ⚠️ | NEW, see above |
| 34 | R5 | Core non-energy, shelter +0.4, oil→core NOT MET, T10YIE < 2.40 | ✅ | RED ask 2 applied |
| 35 | R7 | "breadth −3.44pp" | ⚠️ | Series unnamed (read-1 ⚠️58, not fixed). FIX: "RSP−SPY 63d" |
| 36 | C1 | "MARCO … owe" | ⚠️ | Late mover, see above |
| 37 | C1 | 10Y guard restored; SKEW once; C2/C3 | ✅ | |
| 38 | Chain | LABOR→CARL | ✅ | |
| 39 | Chain | CARL→REGINALD | ✅ | |
| 40 | Chain | REGINALD→repricing; RaDD caveat; "3 of 14" | ✅ | REGINALD STATUS L20 (standing claim) |
| 41 | A64 | Chain verdict; CFG 10/16 → WAL 10/19 → OZK 10/20 | ✅ | |
| 42 | T-01 | Bear/tape lists; headline = real wages, one datum | ✅ | RED ask 3 applied; no "tanker" |
| 43 | T-26 | Two windows; TP −5.1 / RN +1.4 | ✅ | Pass record §E; read-1 ⚠️64 fixed |
| 44 | T-26 | "BOND's 10/14 ACM read decides" | ⚠️ | No due date; not in docket or next-boot. FIX: date it, or "(BOND, due <date>)" |
| 45 | T-27 | | ✅ | |
| 46 | T-30 | $9.965B; No registered threshold; Thu 10/15 ~16:30 | ✅ | LIQUID STATUS L48 |
| 47 | T-10…29 | Pointer row; DOCKET prefix; Aramco | ✅ | |
| 48 | FT-08 | FIRED `b79c04c9a` 20:23; airfares 1.159 vs 2.35 | ✅ | |
| 49 | FT-08 | "Composition → 11/10" | ⚠️ | See above |
| 50 | BOND kill | MET 10/1 one-shot; 9/30 $52.885B below | ✅ | |
| 51 | Breached rest | LIQ-07, HENRY trio, HY, CCC/B, FLG/OZK, owners | ✅ | |
| 52 | Proximate | All distances | ✅ | |
| 53 | Not conf. | HY 56bp; L13 DEAD; LIQ-076 review 10/30 | ✅ | |
| 54 | Cluster | Verdict | ✅ | |
| 55 | Docket | All rows and dates | ✅ | DOCKET L555/572–575/631/632 dates match |
| 56 | Narrative | Consensus | ✅ | |
| 57 | Narrative | "failed to explain" | ⚠️ | See above |
| 58 | Narrative | Counter-signal; CCC−IG 1,184 vs 1,147 | ✅ | |
| 59 | A143 | Bottom line | ✅ | All four fixes present |
| 60 | A145 | Next boot owes | ✅ | FT-08 removed (WQ-357 item: see 17) |
| 61 | M-03/T-26/B74 | Two priors | ⚠️ | See above |
| 62 | B3 | Header, pointers, commit-date stamp | ✅ | |
| 63 | B6 | Dark window; L554 missed | ✅ | |
| 64 | B6 | "no settle source exists" | ⚠️ | See above |
| 65 | B §1 | `f87e66c1f`; part list; "one day after 10/13" | ✅ | DESIGN L4; DOCKET L639 = 10/13 |
| 66 | B §2 | L554 RESOLVED-late → Tue 10/20 | ✅ | |
| 67 | B §2 | L630 BRENT quote; EIA ~8-day lag, 8–15% | ✅ | Pass record §D |
| 68 | B §2 | "L630 grades nothing unless I re-spec or withdraw" | ⚠️ | A withdrawal does not make it grade. FIX: "unless re-spec'd; a withdrawal retires it" |
| 69 | B §2 | L558/GATES row 19, C#1 by arithmetic | ✅ | GATES.tsv line 19 = GATE-NEXUS-T12S-DFII10 |
| 70 | B §2 | L553 / L571 | ✅ | |
| 71 | B23/B77 | Bare L-numbers | ⚠️ | See above. B L77 ACTION also omits DOCKET L639 (S1), which A L118 lists as consumed |
| 72 | B §3 | VULCAN | ✅ | |
| 73 | B §3 | LIQUID | ✅ | |
| 74 | B §3 | Two caveats; no non-root | ✅ | VULCAN L48 (9/15→9/28) |
| 75 | B §4 | HENRY · FALCON · WATT · brief hygiene | ✅ | Pass record §G |
| 76 | B §4 | RED "uncommitted" | ❌ | See above |
| 77 | B §5 | Number and basis; 8/3 history | ✅ | |
| 78 | B §5 | "impossible before cell 15" | ⚠️ | See above |
| 79 | B §5 | FT-08, SKEW, T10YIE, CCC, sinking, long-end rows | ✅ | |
| 80 | B §5 | VVIX source; undated cells | ⚠️ | See above |
| 81 | B §5 | "10/14 bar is unpublished" (157.30 dropped) | ⚠️ | See above |
| 82 | B §5 | "tails yes / center no … all of it held" | ⚠️ | See above |
| 83 | B §5 | CCC−IG; nearest lines 4 / 5 / 11bp | ✅ | |
| 84 | B | Caveat 1 | ✅ | |
| 85 | B | Caveat 2 "lost its support tonight" | ⚠️ | The reads are dated 10/9 (A T-27 "(10/9 …)"); "tonight" is when NEXUS consumed them. FIX: "lost its support (10/9 reads, consumed tonight)" |
| 86 | B | Caveat 3 | ✅ | ORACLE prior: see 61 |
| 87 | B | Caveat 4 | ✅ | |
| 88 | B77 | ACTION / ASK none of Will | ✅ | |

POINTERS: 48 tested, all resolve.
- Files (14): STATUS_COLD, pass record, PREDICTIONS_COLD, FORGE/STATUS, HEARTBEAT, analysis/one-root-or-many, disc-J letters, CONFIRMED, LAST_COMPLETION, S1 DESIGN, BRIEFS_MAP, GATES.tsv, DOCKET.tsv, STATUS.
- Commits (4): a16831e82, b79c04c9a, f87e66c1f, c032d9106.
- DOCKET rows (16): L553, 554, 555, 558, 571–575, 586, 630–632, 639, 651, 673.
- Anchors (14): §H4/12/16/20, §C6, pass record §C/§D/§E, S1 §7/§10, ★10/14, GATES row 19 (by file line), HEARTBEAT #3.

Read-only: no repository file touched.
