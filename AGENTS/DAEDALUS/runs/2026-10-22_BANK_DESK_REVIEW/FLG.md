# FLG — Organization & Process Review (read-only, for DAEDALUS)

**Written:** 2026-10-22 11:24 EDT Thursday (from `date`) · **Reviewer:** read-only design reviewer · **Subject state:** FLG live (PROME catch-up); FLG's last commit `76c0982ef` 11:17 ET, on origin/master; FLG tree clean (`git status --porcelain -- AGENTS/FLG` empty).

## Verdict

FLG is a young desk whose **analytical core is strong**, and stronger than its L3 grade suggests. It has a self-built PRIMARY flow ledger (13 filings, identity ties 13/13). It base-rates its own triggers and retracts on the record. Its **Q3 pre-print frame is frozen**, and I verified the hash: sha256 `cb686b26…b2f` matches both the working tree and HEAD. The frame's source-basis table and its 11 rules for what not to infer from silence are at least as good as OZK's card.

**Nothing has to be built from scratch before 06:00 ET tomorrow.** One small item can only be written before the print: a pre-stated **earnings-surprise threshold**, plus a mapping to TERRY's open FLG candidate (#1).

The weaknesses are about organization, not analysis:
- **(a) Contradictions with ruled canon.** FLG-01's 75%→50% re-mark exists only in narrative. Under WQ-112 a narrative re-mark does not score.
- **(b) Stale old-regime text on surfaces other desks pull.** THESIS v1.0 body, the EXIT_PROTOCOL justification, KB header, and STATUS "ZERO registered gates" all still describe superseded states.
- **(c) A charter Git line that restates the non-ff recovery without the dirty-path overlap check.** This is risky on today's shared, dirty tree.
- **(d) An L4 trade leg that fails on the letter.** TRADE.md says "no position" but gives no re-arm condition, and it does not know that TERRY holds an FLG candidate.

There are **no 🔴 findings.**

## Findings

| # | Sev | Dim | Finding (specific, with numbers) | Evidence | V/I | Fix owner | Suggested fix |
|---|---|---|---|---|---|---|---|
| 1 | 🟠 ⏰ **before 06:00 ET 10/23** | H / E | **The earnings-surprise route has no pre-stated trigger magnitude, and nothing on FLG's surfaces links to TERRY's open FLG candidate.** The charter route (`Earnings/guidance surprise (direction + magnitude vs the release) → TERRY, PROME 🟠`) has no threshold. The frame addendum only says "record direction + magnitude" against consensus EPS ~$0.07 and revenue ~$545M (aggregator-grade). TERRY's 10/12 shortlist holds **"1 — FLG downside, WATCH; not ready"** (Jan-2029 12P, ~$380 risk), but no FLG file mentions it. TERRY's shortlist also recorded FLG's CALENDAR as "latest owner 10/1". Friday's packet decision therefore rests on judgment after the print. | `AGENTS/FLG/CLAUDE.md:164`; `reports/2026-10-21_Q3-2026_PREPRINT_FRAME.md:117`; `AGENTS/TERRY/research/2026-10-12_new-trade-shortlist.md:9,26`; `grep -rl TERRY/research AGENTS/FLG` → none | Verified (absence) | Desk | **Before 06:00 ET**, write a **separate dated pre-print annotation file**; the frame says "No edit after this line". It should state: (i) the surprise threshold, e.g. EPS ≥$0.02 vs $0.07, or FY26 provision guide outside $90–140M; (ii) which A–F readings packet TERRY, and that they go as NOT-FIRED context only (Will 10/20 "trade ideas loosened"). Commit it before the release; if it is missed, the window is gone. |
| 2 | 🟡 | H | **No adversarial disambiguation pass** (blueprint §5 print contract, item 2). Two examples: (a) A-row 3 "ACL down again (<$869M) with NAL ≥$2,700M → For" and A-row 5 "Q3 provision <$37M, guidance unchanged → Neutral-to-against the mechanism" **can fire together** on a plausible quarter, with opposite arrows. (b) Item B leaves a **dead band of $2,500–2,800M NAL** with no reading, and a modest decline lands there. Opposite arrows on two legs may be intended, but no rule says how they combine. | Frame `:29-33`, `:41-42` | Inferred (that the co-fire matters) | Desk | Optional before the print: one dated co-fire note, in the same annotation file as #1, saying they grade separately by leg and do not combine. Otherwise record the co-fire explicitly in the post-print file. |
| 3 | 🟡 | H | **The 06:00 wake depends on a session existing.** DOCKET L522 says "FLG grades in its open window if live at 06:00 ET, else PROME directs the grade". I saw no scheduled mechanism. The cost is low: the frame is frozen, so a late read loses no integrity, only timing for the TERRY route. | `PROME/DOCKET.tsv:522` | Inferred | PROME / Will | Confirm who opens the 10/23 session. If it is later than 08:00, the call transcript replaces the live call in the frame's step 4. |
| 4 | 🟠 | D | **FLG-01's confidence re-mark does not count under ruled canon.** STATUS presents "75% → 50% (amended)". The machine `Confidence` cell still reads **`75% PROVISIONAL`**; the 50% exists only in Notes. WQ-112 (Will, 9/01): "a re-mark is valid only when it lands in the machine field with its date — a narrative-only re-mark is not a mark and does not score." As written, FLG-01 grades at 75%, the confidence the desk itself disowned. | `workbook/PREDICTIONS.tsv` FLG-01 col 4 vs col 11; `STATUS.md:127,131`; `FORGE/PREDICTION_DISCIPLINE.md:36,43` | Verified | Desk | Write the dated re-mark into the field, e.g. `50% [2026-10-2x] (was 75% [2026-08-28]) PROVISIONAL`. This is allowed pre-resolution (WQ-161 ② explicitly preserves WQ-112 re-marks). Resolve_By 2027-03-15, so it is not urgent, but it costs one cell. |
| 5 | 🟠 | A | **The charter restates the non-ff recovery and drops root's safety check.** CLAUDE.md:206 says "non-ff → `git pull --rebase --autostash`, re-push, never force". It omits root step 3's required **dirty-path overlap check**, which exists because "the autostash stashes the whole dirty tree, other agents' work included". Today PROME has 9 modified or staged paths in the shared tree (session-start git status). A FLG closeout that follows line 206 literally would stash PROME's live work. This also violates blueprint §8: "Git = cite-don't-restate". | `AGENTS/FLG/CLAUDE.md:206`; root `CLAUDE.md` §Git Protocol step 3 | Verified | Desk (charter edit; permission + idle) | Replace the recipe with a citation: "non-ff → root §Git Protocol session-end step 3 (overlap check first)". |
| 6 | 🟠 | A / C | **"Zero registered gates" is false on two hot surfaces.** CLAUDE.md:104 says "Nothing is registered today" and STATUS.md:119 says "Registered gates: still ZERO, and still deliberately". In fact **GATE-FLG-T08 was registered 2026-08-28** (PROME `c9214c78d`) and fired 10/1; it is now terminal and archived from GATES.tsv. FLG's own CALENDAR row cites it. A reader of STATUS learns the opposite of the record. | `git log -S'GATE-FLG-T08' -- PROME/GATES.tsv` → `c9214c78d 2026-08-28 … GATE-FLG-T08 registered`; `CALENDAR.md` 10-01 row | Verified | Desk | Change to: "1 registered (GATE-FLG-T08, 8/28, FIRED 10/1, terminal); 0 live". Also retire the charter's build-time sentence (blueprint §6b.3: role tense, not state tense). |
| 7 | 🟠 | C / D | **Old-regime text survives on the thesis of record, which consumers pull** (blueprint §7 C4 "grep own tree for the old regime by name"). See the stale-text list below the table. TERRY read THESIS.md whole on 10/12. **THESIS.md is 32,422 B = 99.6% of the 32,550 B budget**; it is not a boot read, but any growth crosses the budget. | grep output in Coverage; `THESIS.md:63,224,226`; `workbook/EXIT_PROTOCOL.md:203,219`; `STATUS.md:88` | Verified | Desk | Run the C4 grep for `top gap`, `~12-month`, `pending REGINALD`, `Q2-seasonal` and fix each hit in place, as amendments per the version-log practice. Move closed-question narrative (Q1–Q2d, ~125 lines) to a cold file, so THESIS keeps headroom for the Q3 amendment. |
| 8 | 🟡 | D | **The kill rail confirms in one direction only, and has for 63 days.** The "Falsifies the stance" row of the bidirectional flip has been ⛔ UNSET since 8/20. The `Kill rail re-derived:` stamp is 2026-08-28 (55 d), and 10/21 corrections deliberately did not bump it. The reason is well argued: K-3 requirement 3 assumes one regime, and FLG has a 2024Q2 regime break. But that is a **framework question no one has ruled on**: does a repair-detecting kill on a post-break window, n=4 halves, pass? It was routed to REGINALD, not to DAEDALUS or Will. | `EXIT_PROTOCOL.md:3,218`; `STATUS.md:96` | Verified | DAEDALUS (blueprint §4 requirement-3 under regime breaks) + desk | DAEDALUS rules on whether "requirement 3 on the post-break window" is acceptable. The desk re-tests once the Q3 10-Q adds a half (n=5), or files a Will-gated "falsify-leg waived with reason". |
| 9 | 🟡 | E / L4 | **The trade surface fails L4 reading A on the letter, and its cohort section is stale.** Details are in the trade-surface list below the table. **No expiry-nagging content: complies with Will's 10/20 ruling.** | `TRADE.md:1-31`; `OPERATIONS.md` MATURITY LADDER L4 reading A | Verified | Desk | Add one re-arm line, e.g. "FLG hands TERRY a construction input when [named frame readings / FLG-02 HIT] — NOT-FIRED context allowed per Will 10/20". Cite TERRY's candidate. Replace the cohort paragraph with a pointer to `FORGE/STATUS.md`. Use the `root rule #N` form. This is the cheapest path to the L4 trade leg. |
| 10 | 🟡 | C | **STATUS shape and carried items.** Details are in the STATUS list below the table. Size is fine: 168 lines, 22,364 B (69%). The BOTTOM LINE is current, but its heading is undated. | `STATUS.md:7,11-54,56-115,119,150,166` | Verified | Desk | Rewrite rather than prepend: fold the three session blocks into one current-judgment section, rotate the 8/28 narrative per the charter's verbatim-crc procedure, fix `Level`, strike ②, and give ① a date and dependency (#11). |
| 11 | 🟡 | D | **A Call Report dependency is not recorded on any FLG surface.** T-01 (Q3 Call Report ingest ~11/14) and owed item ① (the CDR pull) need FFIEC CDR access. The **CDR JWT expires 11/05** (DOCKET L180; WILL_QUEUE row 31 = Will's regen). REGINALD's MI3 cohort run that produces FLG's MIRROR cells is due 11/07. FLG has no row noting either. | `grep -i 'jwt' AGENTS/FLG/{STATUS.md,CALENDAR.md,workbook/TRIGGERS.tsv}` → 0 hits; `PROME/DOCKET.tsv:180` | Verified (absence) | Desk (record) / Will (regen) | Add the dependency to T-01's notes and to the CALENDAR 11/05 row. |
| 12 | 🟡 | D | **The MATURITY_WALL cadence is probably too slow.** Its `Cadence: SCHEDULED next_due=2027-03-01` header says "the 10-K carries the fullest version", but the ledger's 6/30/26 rows come from the **Q2 10-Q**. So the Q3 10-Q (~11/06) likely carries a 9/30 table. The quiet declaration hides that update from the staleness tool for ~4 months. T-10 (Next_Check 2027-03-08) is the same. No 3/31 rows exist, so whether every 10-Q carries the table is unverified. | `workbook/MATURITY_WALL.tsv:1-2` + rows (as_of 2025-12-31, 2026-06-30) | Inferred | Desk | Re-declare next_due = the Q3 10-Q date (~11/06–11/09), or state on the header why 10-Q rows are not tracked. |
| 13 | 🟡 | A / B | **The FILES table omits 9 live surfaces, and the flow ledger's parser has no documented home.** Omitted: NONACCRUAL_FLOW, MATURITY_WALL, RGB_GUIDELINES, CALENDAR, reports/, scripts/extract_filings.py, registry/, board_log.tsv, inbox/WALTER/. `extract_filings.py` produced the PRIMARY flow ledger and its next use is the Q3 10-Q (~11/06). It has no docstring, usage or provenance. No boot or charter line names it; the only reference is `sources/NONACCRUAL_ROLLFORWARD_EXTRACTS_2026-08-28.md:3`. It exits 0 and prints `null` on a missed table. The 13/13 identity check that "caught two real parser defects" is not in the script. | `CLAUDE.md:212-224`; `scripts/extract_filings.py` (whole) | Verified | Desk | Add FILES rows in role tense. Give the script a usage docstring and an identity-tie assertion with exit codes 0, 1 and 2 (CHECK_STANDARD §3/§9). Name it in the T-02 row as the 10-Q ingest step (blueprint §8 "durable cadence home"). |
| 14 | 🟡 | A | **The charter lags newer root canon.** Details are in the charter list below the table. **No dead references:** no YEYOU, Helm, `AGENTS/PROME/` or live `FORGE/PORTFOLIO.md`. Partly fleet-wide: OZK and FERT charters also lack COMPLETION_SPEC. | `CLAUDE.md:13,30,198`; `PROME/COMPLETION_SPEC.md:10`; `TRADE.md:4,28,29` | Verified | Desk (fleet pattern → DAEDALUS sweep) | Add the explicit-read line to the card. Replace line 30's partial list with "root §Git Protocol session-end 1–3 (incl. 1c-bis/1d/1e)". Align to 32,550 B or cite READ_CAP. |
| 15 | 🟡 | B | **The boot-read manifest declares nothing for FLG.** **Zero FLG rows in `PROME/registry/READS.tsv`**, so `read_cap_check` rc 0 is "clean within what the scan found, NOT a clean bill". It is fleet-wide: OZK, WAL and FERT also have 0, and only 12 readers are declared. `boot.py` at the desk root rather than `scripts/` does **not** matter: it self-locates, follows the FERT/WATT pattern, I verified it read-only, and it ran rc 0 with clean output on every leg. | `read_cap_check.py --agent FLG` output; READS reader histogram | Verified | PROME / DAEDALUS | Declare FLG's 3 boot reads (CLAUDE, STATUS, TRIGGERS) plus an ATTESTATION row when the fleet declaration pass reaches the bank specialists. |
| 16 | 🟡 | F | **Inbound packets waited up to 20 days, and two declared outbound routes have never carried a packet.** Five top-level inbox packets dated 10/01–10/16 were processed only on 10/21 (`b8465b7cd`). They included REGINALD's 10/7 RED-band packet (14 d) and DAEDALUS's 10/8 sweep (13 d). An event-driven desk has no wake for an inbound ASK between prints. **FLG→LIQUID and FLG→TERRY (_NETWORK:74-75) have never carried a packet** (0 `from-FLG` files in either inbox). TERRY pulls instead, and the conditional LIQUID route has not fired. REGINALD consumes FLG's output (5 packets processed; REGINALD STATUS cites the FLG ladder). NEXUS reads FLG STATUS whole. | `git show --stat b8465b7cd -- AGENTS/FLG/inbox`; `find AGENTS/{LIQUID,TERRY}/inbox -iname '*from-FLG*'` → none | Verified | PROME (inbound-ASK wake rule for EVENT-DRIVEN desks) / desk | PROME: a packet carrying an ASK to an EVENT-DRIVEN desk gets a DOCKET row with a date. Desk: once #1 lands, the TERRY edge becomes live; otherwise annotate _NETWORK that TERRY consumes by pull. |
| 17 | 🟡 | G | **Stale headers and a stale trigger row.** (a) KB.tsv header line 3 still says "Every row below is a MIRROR … NOT an FLG primary pull". It has been false since 8/28's A1 rows: the header-contradicts-body defect PREDICTIONS.tsv's own header records. (b) T-07's instrument cell says "REGINALD market.py", but STATUS:152 names `vx_ladder_check.py`. T-07 is a price backup on a ladder that has sat at terminal RED since 10/7, and it keeps being re-dated. Price is not a thesis input (frame rule 9). | `workbook/KB.tsv:3`; `TRIGGERS.tsv` T-07 | Verified | Desk | Fix the KB header. Mark T-07 as stood down (STOOD-DOWN, at terminal band; REGINALD owns VX-REG-6.03), or state what it still wakes for. |
| 18 | 🟡 | (DAEDALUS) | **DAEDALUS's own view of FLG is stale.** The FLEET_MAP row says "No owner STATUS update after October 1"; it has been superseded by the 10/21 and 10/22 sessions, the frozen frame and the 10/22 PROME packet. The profile carries a STALE banner, and its refresh date (11/06 first grade) still stands. | `grep -P '^FLG\t' FLEET_MAP.tsv`; `profiles/FLG.md:3` | Verified | DAEDALUS | Refresh the Gaps cell at the next row touch. Keep L3: the resolving leg is NOT-ADJUDICATED until FLG-02/03 grade (≤11/20). |

### Detail for #7: stale old-regime text

1. THESIS:63 says "Stage 2 remains the weak link and is now the top research gap". The same file at :204 says it was CLOSED 8/28.
2. THESIS:224 says "~12-month DSCR fuse … Stage 2 remains open". The fuse was corrected to ~21 months (KB-052), and EXIT_PROTOCOL:203 claims the fix was made everywhere ("all corrected").
3. THESIS:226 says the falsify leg is "UNSET pending REGINALD's cohort base rate". That candidate was retired 8/28.
4. EXIT_PROTOCOL:219 justifies the H1-vs-H1 rule as "formation is Q2-seasonal (KB-037)". That was refuted by KB-045 (STATUS:88). The rule survives; its stated reason does not.

### Detail for #9: trade surface

- Reading A passes only if the surface feeds proposals, or is declared flat or frozen **with an explicit re-arm condition**. TRADE.md says "NO POSITION … this desk proposes none at the Q3 print" and gives **no re-arm condition**.
- It does not mention TERRY's 10/12 FLG candidate (see #1).
- The "Cohort context" section uses **8/14 FORGE marks** and an **8/20 price of $13.49**. The header says "LIVE — state as of 2026-10-21", which is a fresh header over a stale body.
- Robinhood absence has been unverified for 22+ days.
- Citations use "root Critical Rule 4/5" and "Root rule 6 … rule 7", not the canonical `root rule #N`.

### Detail for #10: STATUS shape and carried items

- **Header says `Level: L1`**; FLEET_MAP has L3.
- **Three session logs (10/22, 10/21, 10/01) are stacked above "START HERE"**, the current-judgment section. Blueprint R3 requires the spine to be rewritten, not prepended.
- "START HERE" and "SECOND PASS" are undated 8/28-vintage narrative, about 60 of 168 lines. "NYC just froze the rents … effective October 2026" is still written in the future tense.
- Owed item **② "numeric comparator for K-4" is DONE**: EXIT_PROTOCOL K-4 says "Comparator set 2026-08-28, KB-FLG-051", and it was committed in `2c1b48b7f`.
- Owed item **① FFIEC CDR pull** has been carried 55 d with no date or trigger.

### Detail for #14: charter currency

1. The SPAWNED-MODE card (:13) reads only FLG CLAUDE, STATUS and TRIGGERS. COMPLETION_SPEC:10 requires explicit reads of root CLAUDE.md, AGENTS.md and USER.md (runtime amendment 10/05). PROME's spawn brief covers this; the card does not.
2. Closeout (:30) lists commit, orphan, consumer and push only, and omits 1c-bis, 1d and 1e. The desk in fact ran the ledger nudge and claim_check on 10/22 (STATUS:27), so practice is ahead of the charter.
3. The STATUS budget is "≤32,000 B / 24,000 B" (:198); canon is 32,550 B.
4. Will's 10/20 rulings are not reflected. They are relevant to FLG as an evidence feeder for NOT-FIRED trade ideas.

## What's working well

- **Pre-print discipline.** The frame was written 10/21 and frozen with a verified sha256. A table settles which source can give which number (release vs 10-Q vs Call Report) before any number is read. Its 11 rules on what not to infer from silence are explicit, the 8-K exhibit-index step is there, and release figures are barred from grading FLG-02/03. DOCKET L522 carries the frame's hash.
- **Primary-sourced ledgers with two-clock headers.** Quarterly ledgers are declared quiet (WQ-147) rather than left to rot. NONACCRUAL_FLOW is an identity-checked 13-filing series.
- **Prediction hygiene otherwise sound.** Resolve_By dates are hard dates with a buffer (PAT-115), each row names its instrument, if-falsified actions are present, and the desk refused to VOID a disowned call.
- **Clean checks.** `boot.py` is read-only, its rc contract held when I ran it, and all four legs printed explicit clean lines. `claim_check` weekday found 5 files clean; corrections rc 0 with 2 receipts; read_cap rc 0; ledger_staleness rc 0.
- **Inbox now drained,** with a board_log for WALTER signals.
- **Strong self-correction record:** K-3's six dead candidates, the fuse correction and the SHARE-vs-dollars catch.
- **Clutter is minimal** (58 files). The sibling surfaces FLG lacks — MEMORY, INDEX, WEAKNESSES, SCENARIOS, REGINALD_CHANNEL, LESSONS, POSITIONS — are **local forms, not blueprint gaps**: blueprint mentions are 0 for all but MEMORY.md and POSITIONS, which appear only incidentally. NEXUS_BRIEF (§6) is covered by NEXUS's declared whole-read of STATUS; OZK also lacks one. PREDICTIONS_ARCHIVE is N/A until a row resolves.

## Coverage

**Read whole:**
- `AGENTS/FLG/CLAUDE.md` 1–229
- `STATUS.md` 1–169
- `reports/2026-10-21_Q3-2026_PREPRINT_FRAME.md` 1–125, plus sha256 of working tree and HEAD
- `TRADE.md`
- `boot.py`
- `scripts/extract_filings.py`
- `inbox/PROTOCOL.md`
- `registry/corrections_receipts.tsv`
- `board_log.tsv` (lines cut at 250 chars)
- `CALENDAR.md` (lines cut at 500 chars)

**Read partially:**
- `THESIS.md` 1–66 and 192–end. **Not read:** 67–191 (Q1–Q2d bodies, headings only).
- `workbook/EXIT_PROTOCOL.md` 3–7, 16–24, 41–46, 163–170, 209–248, plus a heading grep. **Not read:** 25–40, 47–162, 171–208 except grep hits at 203 and 219.
- Workbook TSV `#` headers for 6 ledgers (cut at 400 chars).
- PREDICTIONS rows (cut at 700 chars) plus FLG-01 Confidence and Notes in full.
- TRIGGERS columns 1–6 (cut at 400 chars) plus T-13 in full and T-07 columns 3, 4, 6.
- MATURITY_WALL columns 1–6, all rows.
- KB.tsv header (3 lines), last 3 rows (cut at 200 chars), and a column-count check (79 rows × 13 columns).
- `sources/NONACCRUAL_ROLLFORWARD_EXTRACTS_2026-08-28.md` 1–12.
- Inbox and outbox listings, plus the `b8465b7cd` inbox stat.

**Not read at all:**
- MI3_FLG, NONACCRUAL_FLOW and RGB_GUIDELINES data rows
- The three 9/27 reports
- `archive/` contents
- Processed packet bodies

**Fleet and context material:**
- Root `CLAUDE.md` (session context).
- `USER.md` 43–47 only.
- `DAEDALUS/OPERATIONS.md` 39–59.
- `BLUEPRINTS/market-agent.md` 27–160, with long bullets cut at 700–900 chars, so some §3/§5/§8 bullet tails are unread.
- `profiles/FLG.md` 1–60 (cut at 400 chars).
- FLEET_MAP rows for FLG, OZK and WAL.
- `_NETWORK.md` grep plus lines 60–80.
- Greps of READS.tsv, GATES.tsv and DOCKET (L180 and L522 in full).
- `PROME/COMPLETION_SPEC.md` (grep).
- `FORGE/PREDICTION_DISCIPLINE.md` lines 36 and 43.
- OZK and WAL top-level listings; the first 1,500 B of `OZK/workbook/Q3_2026_SCORING_CARD.md` and `WAL/Q3_PRINT_GRADING_FRAME_2026-09-24.md`.
- Grep of TERRY's 10/12 shortlist.
- REGINALD and NEXUS STATUS lines matching "FLG".

**Commands run (all read-only):**
- `python3 AGENTS/FLG/boot.py` → rc 0. I first confirmed `ledger_staleness.py` writes only inside its tempdir self-test.
- `scripts/read_cap_check.py --agent FLG` → rc 0
- `scripts/ledger_staleness.py FLG` → rc 0
- `scripts/corrections_boot_check.py FLG` → rc 0, no receipt flags
- `scripts/claim_check.py --check weekday` on STATUS, CALENDAR, TRIGGERS, the frame and TRADE → 5 clean
- `git log`, `git show --stat`, `git log -S`, `sha256sum`

**Not checked:**
- Whether PROME has landed FLG's 17 WATCH_FOR phrases in `newsweep_config.py` (outside this tree).
- Whether any scheduled mechanism opens a session at 06:00 ET.
- Whether the Q3 10-Q will carry a maturity table.
