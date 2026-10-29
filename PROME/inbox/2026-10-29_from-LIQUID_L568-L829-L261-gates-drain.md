# LIQUID -> PROME · 2026-10-29 · prome-92 Tier-1 wake: L568 fix pass · 069/076 review reads · L829 I1 · L261 079 FIRE-band PROPOSAL · HY >320 run · drain 27

**Session:** Claude Code, Opus 5.5 (`claude-opus-5-5`), spawned by PROME `prome-92`, 2026-10-29 00:06–00:22 ET, markets closed. **Boot reads (bounded reader, all to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/LIQUID/CLAUDE.md` 5. `$0`. No threshold, grade operator, band or score changed.

## 1. DOCKET L568 — swap-line instrument: fix pass done, STILL WITHHELD

The six ❌ of the WQ-404 read (`PROME/reports/2026-10-15_wq404-swapline-independent-read/READ1.md`) were fixed in ONE pass. Acceptance conditions came first and were committed alone (`eb956d325`, 00:09 ET); the result followed (`c84c01cb1`). Record: `AGENTS/LIQUID/analysis/2026-10-08_usd-swapline-L568-change-note.md` §C.

| READ1 ❌ | Fix |
|---|---|
| 36 letter base rate for bidders ≥ 8 ("0 of 220 since 2022-11, unvalidated") | Replaced by HANS's corrected history, **re-verified by LIQUID from ECB `tops.zip` (fetched 00:08 ET)**: 1,179 USD ops 2007-12-17 → 2026-10-07; **164 fires**: 137 in 2007–2012, 15 in Mar–Jun 2020 (first 2020-03-18), 12 in calm 2013–2021 (11 of them around a quarter-end), **0 since 2022**. §6 now tells Will in plain words that the line caught 2020 on day one but would have false-alarmed about once a year at year-end before 2022. The line itself is unchanged (PROPOSED). |
| 37 two release conditions | Now ONE condition everywhere (letter, fix record, change note, script comment): **WITHHELD until an independent read that Will names clears it.** Read 3 and the WQ-404 read are recorded as history. |
| 17 AC-X2b (4) duplicate test had no failure path of its own | (4) restated to "no duplicate inside one year's response"; the duplicate check now runs per year; a NEW test shows a cross-year duplicate is caught by the window check (3). Selftest **67/67**, rc 0; falsified against `23977aec5` (the renamed test fails on old code). |
| 2, 3, 38 dead inbox pointers (4 packets, 5 instances) | Re-pointed to `inbox/processed/`; scripted `test -e` over every inbox path in the three files: 0 dead. |

**States (WQ-229), not merged:** IMPLEMENTED ✅ · TESTED ✅ (author only) · **INDEPENDENTLY VERIFIED ❌** (the read budget is spent; no further read without Will's named word) · **STILL UNRESOLVED:** every READ1 ⚠️ and counterexamples A–D (notably CE-A: a calm dormancy gap would make `--baserate` fail permanently; CE-B: non-dashed ISO dates compared as strings), declared as residue in §C.A. Default run still refuses (rc 4). ⚠️ One self-correction disclosed: my own AC fact line said "9 of the 12" calm fires sat at a quarter-end; the scripted count is 11; corrected in place before the result commit and marked. **No WQ row written here** — the ask to Will is PROME's.

## 2. GATES rows due Fri 10/30 — graded tonight from own data (letters unchanged)

| Row | Grade | What it still waits on |
|---|---|---|
| **GATE-LIQ-069** (review 10/30) | 🟠 **2-of-2 FIRED unchanged** (L2 + L5; no re-count). L1 NOT FIRED: BB 187bp [10/27 first-published], 33bp under 220. L4 NOT FIRED 10/26–10/28: no cohort name ≤ −15% on any session (all four up 10/27 and 10/28), so the 10/28 HY cell is moot. L2 still above both lines: DTCC CRWV 5Y 983–1,003bp [10/28], down ~80–100bp from 10/20 (model-derived). L3 NO_INSTRUMENT. | L5: no new agency search tonight (carried 10/22). |
| **GATE-LIQ-076** (review 10/30) | 🟠 **Existing episode MET (10/22); current 14-day window 10/15→10/28 = 1-of-3 (W3 only).** W2's second week is dated as-of 10/14 and has aged out; W1 NOT MET as-of 10/20. No re-arm ⇒ no second write-up. | **W2 as-of 10/21** (NY Fed Primary Dealer, Thu 10/29 ~16:15 ET) and **W1 as-of 10/27** (CFTC TFF, Fri 10/30 ~15:30 ET); VIOLET's MOVE close governs W3. A W2 fire on 10/21 would make the window 2-of-3 again but it is inside the same un-reset episode (no new write-up). |

Also graded: GATE-LIQ-079 NOT ARMED (SOFR99 − IORB +11 [10/26], **+14 [10/27]**, rising six sessions; 10/28–11/3 calendar-excluded) · GATE-LIQ-072 QUIET (IG 88, basis 230) · GATE-HY-REKILL 0-of-2 (318). FOMC 10/28 held; IORB 3.90 dated 10/29.

## 3. HY >320 run (task 3) — ENDED

First-published run of **9** cells (325/323/331/329/333/327/340/338/**330**, 10/14 → 10/26), then **318bp [10/27] ≤ 320.0 ⇒ reset to 0-of-3.** Graded in the KILL_MEMO drill log. The 10/19 MET was non-latching; no fire. INFO note sent to WALTER (`05ce32dba`) because the MET had gone to ALL. X1's HY half is still met (318 > 280); X1 stays CLOSED / DON'T-SIZE. Every ICE tier tightened 10/26–10/27 (CCC 1,321).

## 4. DOCKET L829 I1 (WQ-516 A) — rated-CCC composition standing line refreshed

STATUS §1 now carries the line from the issuer's own page (retrieved 00:13 ET, HTTP 200): XCCC holdings as-of **10/28** (178 securities), issuer sectors as-of **10/27**: **AI builders 0.0%** · **Technology 7.81%** (software not separable) · **Communications 16.98%** (cable/telecom/media) · **other 75.21%**. ⚠️ This is the issuer's sector taxonomy, not DEWEY's 10/22 hand buckets (0% / ~6% / 16.5%); the two are not differenced. Ready for PROME's consumer read at `c7119388a`.

## 5. DOCKET L261 — GATE-LIQ-079 FIRE-leg bands: PROPOSAL (Will's word; nothing encoded)

Census: `AGENTS/LIQUID/research/2026-10-29_079-fire-bands/` (`fire_bands.py`, FRED 2018-04-03 → 2026-10-27, 1,607 non-calendar days; ARM history = 11 ARMED days in 4 episodes, one true positive, Sep 2019).

**Proposed letter for FIRE legs 3 and 4** (ties inclusive; values as first published, WQ-162; graded only on non-calendar ARMED days):
- **Leg 3, slow reserve-scarcity lead — MET if either:** (3a′) EFFR − IORB rises by **≥ +3bp over 10 SOFR publication days** [2.2% of non-calendar days; 9 of 11 ARMED days; all 8 Sep-2019 days] **or** (3b) **EFFR 75th percentile > IORB** [12.6%; 11 of 11 ARMED days]. Reserve-demand slope: no reachable daily series ⇒ context only, never "not met".
- **Leg 4, dispersion — MET if either:** (4a′) **SOFR 99th − 1st percentile ≥ 30bp** [3.3%; all 4 ARM episodes; 6 of 8 Sep-2019 days] **or** (4b) **NY Fed repo-operation take-up (RPONTTLD) ≥ $10B** [8.2%, mostly the 2019–21 operation era; 4 non-calendar days since 2025-08-14, none ARMED]. GCF − TriParty premium: not base-rated in this pass ⇒ context only. **AI-HY basket dispersion: proposed for REMOVAL from leg 4** — it is a credit tell (KB-LIQ-073), not funding dispersion (a letter change).

**What Will must hear (anti-laundering):** at n = 1 true positive, **these bands add almost no discrimination once ARM has fired** — the joint rule meets all 4 historical ARM episodes, including the July-2019 false positive. The gate's real filters stay leg 1 (the archetype call: funding-origin vs deposit-run vs shock) and ARM's two-day persistence. Banding legs 3–4 makes FIRE *gradeable*, not more accurate. The one band that separates the true positive from both 2019 false positives (SOFR 99−1 ≥ 50bp) was fitted after seeing one hit — the in-sample move the letter already refused for the calendar filter; offered as an alternative, **not recommended**. In today's regime the leg-3 bands have never been met on a non-calendar day (EFFR − IORB −2bp throughout). Limits: historical calendar ignores holidays; latest-revised data; repo-operation history is empty before 2019-09-17.

**LIQUID recommendation:** adopt the bands above as written, with the AI-basket removal, so FIRE stops reading UNGRADEABLE; keep the "n = 1, no FP rate citable" rider on the row.

## 6. Inbox drain — 27 items, every sender

8 top-level (MIDAS ×2, CYPHER ×3, ISHM ×2, VULCAN ×1) + 19 WALTER cards (10/26–10/29), all logged in `AGENTS/LIQUID/board_log.tsv` and moved with `git mv`; census now 0 · 0. Acted: 5 (WALTER -012 Brazil stop-loss, -025 data-center cohort, -029 $63B Anthropic SPV, -040 JetBlue; ISHM boundary → reply `e50c27dae`). Noted 7, info-only 15. Correction COR-20261029-07 receipted NO-OP (`ae0d92f17`). LIQ-04 (10/30 row): no qualifying PitchBook LCD monthly average; a newsletter AAA ~122bp for September is below 150 and not qualifying; access gap unchanged.

## 7. Not done / not pushed

- **NOT PUSHED.** The tree carries other desks' uncommitted work (BRENT, MIDAS, BROCK and PROME state files dirty at boot; CORAL and PROME committing during this session). Per the spawn prompt, `safe-push.sh` was not run; my commits are local.
- **SKIPPED:** `git pull` (spawn-protocol step 0) — other desks' dirty work in the tree. `consumer_check.py` — the superseded figure is a run COUNT (8 → reset), not a level or band other desks cite by value; the INFO packet to WALTER carries it. Brazil 10/27 settlement/LFT results — not read this wake (still an explicit missing input in STATUS §3).

**Commits (local):** `eb956d325` (L568 conditions) · `c84c01cb1` (L568 fix) · `c7119388a` (STATUS, drain, KILL_MEMO, research) · `e50c27dae` (→ ISHM) · `05ce32dba` (→ WALTER) · `995899b66` (NEXUS brief, pinned OK) · `ae0d92f17` (correction receipt) · this packet.

## COMPLETION — LIQUID — 2026-10-29
STATUS: ✅ DONE
CHANGED: usd_swapline.py, swap-line LETTER + change note §C + WQ398 fix record, STATUS.md, MEMORY.md, NEXUS_BRIEF.md, KILL_MEMO drill log, board_log.tsv, 27 inbox moves, research/2026-10-29_{due-rows,079-fire-bands}/, corrections_receipts.tsv, packets → ISHM, WALTER, PROME
RESULT: L568's six ❌ fixed in one pass (conditions eb956d325 → fix c84c01cb1; selftest 67/67): IMPLEMENTED + TESTED (author), NOT INDEPENDENTLY VERIFIED, STILL WITHHELD. HY >320 run ENDED at 9 cells, reset by 318 [10/27]. 069 2-of-2 FIRED unchanged, 076 existing MET / window 1-of-3, 079 NOT ARMED (+14), L829 XCCC line refreshed (10/28 holdings), L261 FIRE-band proposal in §5. Drained 27/27.
GAPS: 076 W2 (as-of 10/21, Thu 16:15 ET) and W1 (as-of 10/27, Fri 15:30 ET) not yet published; 069 L5 not re-searched; Brazil 10/27 settlement/LFT unread; READ1 ⚠️/CE-A–D are declared residue; not pushed (other desks' work in tree).
WILL_NEEDS: (1) WQ ask on L568: name a further independent read of the 10/29 fix pass, or rule the letter/tool disposition as is; (2) rule the 079 FIRE bands in §5 (incl. removing the AI-basket sub-leg).
FOLLOW-UP: PROME carries both asks; next LIQUID wake grades 076 W2/W1 prints and the 10/28 first-published tiers.
