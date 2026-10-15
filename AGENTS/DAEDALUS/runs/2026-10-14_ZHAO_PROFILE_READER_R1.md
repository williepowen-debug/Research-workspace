# ZHAO profile refresh — Reader R1 (OPERATING LAYER)

**Reader:** R1 (read-only; sole write = this file) · **For:** DAEDALUS whole-profile refresh of `profiles/ZHAO.md` (body 2026-07-04, refreshed 2026-09-05) · **Date:** 2026-10-14 (ET)
**Cluster:** operating layer — charter, STATUS, NEXUS_BRIEF, TRADE, LAST_COMPLETION, board_log, OPEN_THREADS, scripts, inbox, read-cap, git history since 2026-09-05.
**Prices:** no market price below is cited as current. The boot.py output is quoted only as a run receipt.

## Files read (bytes · lines · coverage)

| File | Bytes | Lines | Coverage |
|---|---|---|---|
| `AGENTS/DAEDALUS/profiles/ZHAO.md` | 9,240 | 74 | whole, 1–74 |
| `AGENTS/ZHAO/CLAUDE.md` | 32,539 | 267 | whole, read in chunks 1–89 · 90–179 · 180–267. The last line (267, the FILES `archive/` row) was reached |
| `AGENTS/ZHAO/STATUS.md` | 26,235 | 189 | whole, read in chunks 1–70 · 70–129 · 130–189. The last line (189) was reached |
| `AGENTS/ZHAO/NEXUS_BRIEF.md` | 20,512 | 89 | whole, 1–44 · 45–89 |
| `AGENTS/ZHAO/TRADE.md` | 5,443 | 56 | whole |
| `AGENTS/ZHAO/LAST_COMPLETION.md` | 6,165 | 9 | whole |
| `AGENTS/ZHAO/board_log.tsv` | 11,434 | 25 (header + 24 rows) | all rows, but **each row cut at 600 chars** (see §6) |
| `AGENTS/ZHAO/OPEN_THREADS_2026-07-09.md` | 5,094 | 34 | whole |
| `AGENTS/ZHAO/scripts/boot.py` | 15,078 | 366 | whole |
| `AGENTS/ZHAO/scripts/catalyst_countdown.py` | 11,020 | 256 | whole |
| `AGENTS/ZHAO/inbox/` (9 unprocessed) | — | — | heads, first ~500 B each. Asks read for SIG-W-20261010-004, SIG-W-20261013-024 and the MIDAS approved-maintenance and auto packets |
| Spot checks | — | — | `workbook/` row counts, headers and 3 VX rows · `docket/CATALYSTS.tsv` header and priority counts · `PROME/DOCKET.tsv` rows naming ZHAO (L223/405/435/436/437/482/483/603/670) · `PROME/inbox/processed/2026-10-09_from-ZHAO_bessent-extension-instrument-recheck.md` (last 15 lines) · `git diff 211d555ce..HEAD` on CLAUDE.md, scripts and LAST_COMPLETION · consumer greps at WATT, LIQUID and HANS STATUS |

**Guards run (all read-only):**
- `.venv/bin/python AGENTS/ZHAO/scripts/boot.py` returned rc=1, `REVIEW — 10 ⚠️ (key-figure age 8 · catalysts 2)`. I ran it only after reading both scripts. They contain only `open()` reads plus a read-only `git log`. The yfinance pull caches outside the repo.
- `python3 scripts/read_cap_check.py --agent ZHAO` returned rc=0 with rotation_due=1.
- `git log --since=2026-09-05 -- AGENTS/ZHAO/` returned 70 commits.

---

## 1. STATE

| Item | Value | Evidence |
|---|---|---|
| Last session | **2026-10-09** (PROME-spawned, DOCKET L482). Earlier sessions since 9/05: 9/17 · 9/18 · 9/19 · 9/25 · 9/30 | STATUS.md:3 · git `011af3188` 2026-10-09T10:38-04:00 (on origin/master, verified) · `PROME/inbox/processed/2026-10-09_from-ZHAO_bessent-extension-instrument-recheck.md` (COMPLETION block) |
| LAST_COMPLETION.md | FROZEN 2026-09-17, holds the 9/02 completion. **Not a session clock.** | LAST_COMPLETION.md:1, :3 |
| STATUS | **189 lines / 26,235 B = 80.6% of 32,550 B → 🟡 rotate-tier.** The rule-5 stop is 22,785 B, so 3,451 B more must go | read_cap_check output; ZHAO acknowledged this in the 10/09 memo ("81%, under budget") but did not rotate |
| CLAUDE.md | **267 lines / 32,539 B = 99.97% of 32,550 B.** That is 11 B of headroom against ZHAO's own self-binding rule (CLAUDE.md:50 "STATUS **and this file** … stay under 32,550 B"). read_cap_check counts the charter OUT OF PERIMETER (rule 20, undeclared) | `wc -c`; read_cap_check ℹ️ line |
| NEXUS_BRIEF | 89 lines / 20,512 B = 63% (boot.py [7] ✓) | boot output [7] |
| Inbox (unprocessed) | **9 packets: 4 top-level + 5 in the WALTER lane. Oldest 2026-10-10** (`inbox/WALTER/SIG-W-20261010-004.md`, 4d). All arrived after the 10/09 closeout | `ls inbox/`, `find inbox/WALTER`; git add dates 10/10–10/14 |
| Commits since 2026-09-05 touching `AGENTS/ZHAO/` | **70 total. 30 are ZHAO-authored** (9/17 ×6 · 9/18 ×9 · 9/19 ×12 · 9/25 ×1 · 9/30 ×1 · 10/09 ×1). The rest are inbound packets from WALTER, MIDAS, PROME, DAEDALUS, BOND, VULCAN and HANS | git log |
| Boot verdict today | REVIEW, 10 alerts. See §5 D3–D5: at least 2 of the alerts are false, and the 14-day staleness bar is structurally red on the monthly series | boot.py run 2026-10-14 |

## 2. Existing-profile rows re-verified

### §2 State (2026-09-05)

| Row | Verdict | Evidence |
|---|---|---|
| Last session 2026-09-02 | **CHANGED** to 2026-10-09, with 6 session-days since 9/05 | STATUS.md:3; git log |
| STATUS 219 ln / 32,534 B = 99.95% | **CHANGED** to 189 ln / 26,235 B = 80.6%, still rotate-tier. Rotations since 9/05: #2 (`STATUS_COLD_20260917`), #3/#4 (`…20260918`, `…20260918b`), #5 (9/19, commit `a89c6cce6`), #7 (`…20260925`) | STATUS.md:9; `archive/` listing |
| Ledgers: `PREDICTIONS.tsv` 17 rows (Resolve_By + Anchor_Type + Invalidation) · KB · VX · VX_HISTORY · FLOW · SCHEMA | **CHANGED (counts).** PREDICTIONS has **18** rows (ZHA-18 added), and all 3 columns are present in the header. KB 196 · VX 42 · FLOW 15 · SCHEMA 13. **VX_HISTORY is still 5 rows, all dated 2026-02-13**: never appended and not bannered | `workbook/` counts; PREDICTIONS header; VX_HISTORY.tsv:2–6 |
| Inbox 4, dated 9/2–9/4 | **CHANGED** to 9 unprocessed, dated 10/10–10/14. Since 9/05 the drains were 9/17 (18), 9/25 (2), 9/30 (2) and 10/09 (12/12) | board_log.tsv:2–25; STATUS.md:150–152 |
| Falsification: STATUS §Thesis Kill (:132) + §Falsification tripwires (:136) | **CHANGED (line refs).** Now `## EXIT RULES` STATUS.md:104, Thesis Kill :106–110, `### Live tripwires` :112–118. The full kill letter is carried live again (:108, "DAEDALUS 10/8") | STATUS.md:104–118 |
| Archive: `STATUS_COLD_20260902.md` + 7 older | **CHANGED.** Now 5 STATUS_COLD files (0902 · 0917 · 0918 · 0918b · 0925), plus `NEXUS_BRIEF_PIVOT_HISTORY_20260919.md` and `NEXUS_BRIEF_COLD_20261009.md` (new, crc32 recorded), plus the older records. **The pointer line STATUS.md:9 lists #1–#4 and #7 and skips #5 and #6** | `archive/` listing; STATUS.md:9 |

### §4 The 7/04 drift list ("ALL SIX RESOLVED")

| # | Verdict | Evidence |
|---|---|---|
| 1 `domain/sources/` refs | **TRUE-STILL** | grep over CLAUDE/STATUS/NEXUS_BRIEF returns 0 hits |
| 2 KEY THRESHOLDS `Current` column dropped | **TRUE-STILL** | CLAUDE.md:129–138 (the table has 3 columns: Metric/Threshold/Implication) |
| 3 Convergence note "34/50 🔴" gone | **TRUE-STILL** | grep "34/50" returns 0. CLAUDE.md:194 says "total lives in STATUS.md ONLY" |
| 4 MAIL "removed:" ×2 + HERMES/PROTOCOL refs | **TRUE-STILL (nuance).** The `"removed:"` scrub literal has 0 hits. HERMES/PROTOCOL.md appear **twice**, both as retirement notes and not as a live mechanism, so the profile's "0 occurrences" overstates. Harmless | CLAUDE.md:206, :264 |
| 5 PAT-031 venv-preserving rev-parse wrap | **TRUE-STILL** | CLAUDE.md:29 `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python AGENTS/ZHAO/scripts/boot.py)` |
| 6 HK AB `<$45B` in both files | **TRUE-STILL** | CLAUDE.md:135 `<HK$45B`; STATUS.md:53 `<$45B` |
| "Deliberate/fine": print-counted exits | **TRUE-STILL** | STATUS.md:113–117 |
| "Deliberate/fine": **boot.py's documented in-script CATALYSTS list** | **FALSE-NOW.** It was already false at the 9/05 refresh. The list moved to `docket/CATALYSTS.tsv`, read by `catalyst_countdown.py` (D1 fix 2026-08-21) | boot.py:80–83; catalyst_countdown.py:1–14 |
| "Deliberate/fine": research/signal no-position stance | **TRUE-STILL, but it is not declared in the charter.** The stance is stated in NEXUS_BRIEF.md:5 ("no position — research/signal agent") and OPEN_THREADS:3 ("No trade recs"). CLAUDE.md says only TRADE.md is FROZEN (:261) | grep CLAUDE.md for "no position / no book / research/signal" returns 0 |

### §5 DO NOT TOUCH

| # | Verdict | Evidence |
|---|---|---|
| 1 Belgium METHOD + falsification record preserved; proxy not restored | **TRUE-STILL.** The proxy is still falsified at **rho +0.067 (n=42)**, re-run on July TIC. The profile's cite STATUS:58 has moved to **STATUS.md:39**. The method, the retired rule and the instructive note are preserved at CLAUDE.md:142–189. ⚠️ **But the retired framing leaks on two cross-agent surfaces** (§5 D6) | STATUS.md:39; CLAUDE.md:146–171 |
| 2 boot.py MUST run under `.venv/bin/python` | **TRUE-STILL** | boot.py:22–24, :133–136; CLAUDE.md:29. It ran clean under the venv today |
| 3 TIC watch parses the data-month from `VX-ZHAO-1.02`'s Source cell (regex "Mon YYYY") | **TRUE-STILL** | boot.py:182–187 reads col 9 = Source. VX-1.02 Source = "TIC Jul 2026 (Table 3/1/5)…", and boot prints "Latest logged: Jul 2026 ✓". *(The boot.py:180 comment still says "'updated' + value note", which is cosmetic drift.)* |
| 4 KB enum discipline schema-enforced; SPAWN 3/3b load-bearing | **TRUE-STILL** | CLAUDE.md:31–32; SCHEMA.tsv 13 rows |
| 5 TRADE.md banner DAEDALUS-authored; unfreeze needs a concrete ZHAO position | **TRUE-STILL** | TRADE.md:1; CLAUDE.md:261. See §3 L4 for the weakness in the condition |
| 6 Confidence-move audit trails are deliberate history | **TRUE-STILL, and extended.** The ZHA-01 trail now sits **in the Confidence cell itself** as well as in Notes: `18% [2026-08-21] (was 25% [2026-07-04]; 55% [2026-03-09]; first call 70% [2026-03-04])` | PREDICTIONS.tsv ZHA-01; boot output [5] |

### §8 open questions (bonus)

| Question | Status |
|---|---|
| Korea vs SAM figure reconciliation | NOT-CHECKED (outside the operating layer) |
| VX_HISTORY: revive or FROZEN-banner? | **STILL OPEN, and now a defect.** 5 rows, last dated 2026-02-13, no banner. CLAUDE.md:259 still describes it as the live "historical vector states behind VX.tsv" |
| Cadence: live or episodic? | **ANSWERED.** ZHAO declared **CADENCE WEEKLY** on 9/30 to PROME (WQ-295) (board_log.tsv:12; STATUS.md:151). Observed gaps: 9/19→9/25 (6d), →9/30 (5d), →10/09 (9d). ⚠️ The declaration is not in CLAUDE.md (grep "cadence\|WEEKLY" returns 0), so a cold reader of the charter cannot find it |

## 3. MATURITY LEGS (market class)

| Leg | Verdict | Evidence |
|---|---|---|
| **L1 current-judgment section** | **PASS** | `**Overall Status:** 🟠 ELEVATED — 28/60` (STATUS.md:7) and `## BOTTOM LINE` (STATUS.md:171), dated "OCT 9" at :173 |
| **L3 convergence matrix, present and current** | **PASS, with input staleness.** **28/60**, computed from the rows (STATUS.md:95, "5+1+2+2+4+3+1+1+4+1+2+2 = 28"). The last change was 10/09 (V5 5→4, :84). ⚠️ Header :76 still reads "Rescored 9/2; … re-measured 9/18" and omits 10/09. Several per-vector As-Of cells are old: V3 "Belgium Jun'26" although Jul'26 was pulled 9/17 (:82); V8 "HANS 9/4 via BRENT 9/6 — not live" (:88); V10/V11 "Jul 4" (:90–91), which is 102 days | STATUS.md:74–95 |
| **L3 exit rules** | **PASS** | STATUS.md:104–118: thesis kill letter, plus China >$680B ×2, composition ≤−$5B, Belgium rho < −0.5, Korea fired/graded, and the property tripwire fired 10/9 with a named re-raise condition |
| **L3 dated falsification surface** | **PASS** | ZHA-18 pre-registered on 9/18, 28 days before the print (`Resolve_By 2026-10-23`, letter `reports/2026-09-18_PREREGISTRATION_ZHA-18_august-tic.md`; STATUS.md:143). The Belgium kill-leg re-spec is **dated 2026-10-23** (:108). Next tripwire reads: Aug TIC 10/16 (:114) and October construction <47.5 (:117). It is also **exercised**: the property tripwire fired 10/9 and was applied *against* ZHAO's own read (:117; NEXUS_BRIEF.md:16). ZHA-16 was graded MISS by its letter on 9/30, with VOID declined (:24) |
| **L4 trade leg (READING A)** | **PASS on route 2 (frozen with an explicit unfreeze condition). Route 3 is corroborated in substance. ⚠️ The condition is not operational.** | See below |
| **L5 clean closeouts** | **PASS, with hygiene debt.** There are 3 consecutive dated closeouts carrying COMPLETION blocks, and PROME consumed all 3 (`PROME/inbox/processed/` 2026-09-25 L222, 2026-09-30 ZHA-16 L481, 2026-10-09 L482). In the 10/09 memo, consumer_check, claim_check, brief_pin and read-cap are receipted. `011af3188` is on origin/master. The NEXUS ordering rule holds: STATUS and NEXUS_BRIEF land in the same commit at the same timestamp. Debt: stale claims in STATUS (D1, D2); BOTTOM LINE stacked against the desk's own rule (D7); STATUS sits at rotate-tier and was acknowledged but not rotated | as cited |
| **L5 current** | **PASS** | The last closeout was 5 days ago, inside the declared WEEKLY cadence |

**L4 under READING A in detail.**

The freeze banner, verbatim (TRADE.md:1):

> **🧊 FROZEN 2026-07-04 — superseded 4-anchor content / no active position; not maintained. STATUS.md is canonical; do not cite rows below as current.** *(DAEDALUS TRADE-staleness sweep, PAT-025, Will-approved. Rationale reworded 2026-07-09 — ZHAO reactivated same day as the freeze, so "dormant" was never accurate; the freeze itself stands until a concrete position re-emerges.)*

The unfreeze condition, verbatim from the charter (CLAUDE.md:261):

> `TRADE.md` | 🧊 **FROZEN 2026-07-04** — superseded, not maintained; STATUS is canonical. Unfreeze only if a concrete position re-emerges.

How each route scores:
- **Route 1, TRADE.md feeds proposals: FAIL.** The body is dated 2026-03-09 (TRADE.md:4), and its rows carry the dead Belgium kill-letter (TRADE.md:12).
- **Route 2, frozen with an explicit condition: PASS on the letter.** A condition is written in both the file and the charter.
  - ⚠️ **Weakness:** "a concrete position re-emerges" names no trigger, no owner and no detector. It does not say whose position, recorded where, or who checks.
  - **Live illustration:** WALTER's dispatch note on `inbox/WALTER/SIG-W-20261010-004.md` says "Will holds a TLT Oct-16 put". TLT puts were TRADE.md's #1 row. Nothing on any surface tests whether that counts as "re-emerging". *(This is WALTER's claim. Position truth is off-repo and I have not verified it.)*
- **Route 3, no book by charter AND signals reach a consumer: the consumer half PASSES; the charter half is not literally met.** CLAUDE.md does not declare "no book". The stance sits in NEXUS_BRIEF.md:5 and OPEN_THREADS:3 only. Consumption since 9/05 shows at recipients' artifacts:
  - **WATT** built a triggered channel on ZHAO's wording: `WATT/STATUS.md:29` "trigger wording ZHAO's (9/25, KB-ZHAO-187)", with a T2 re-check at :114.
  - **PROME** set `DOCKET.tsv` L436 to "RESOLVED — VOID … ZHAO KB-ZHAO-183, PROME-verified at the S.Ct. opinion".
  - **VULCAN** adopted CORRECTION #2 and IEEPA-VOID (git `ee888f577`; board_log.tsv:13).
  - **LIQUID** still carries the falsification (`LIQUID/STATUS.md:82` "TIC_FRAMEWORK.md (§2 falsified Belgium prox…").
  - Routed packets were processed at BOND, HAWK, HENRY and VULCAN (`*/inbox/processed/2026-09-25_from-ZHAO-via-PROME_*`).

**Verdict: PASS.** Recommended fix: make the condition operational (§5 D9) and put the no-book declaration in the charter. Then route 3 also passes on the letter and does not depend on a vague route 2.

## 4. New since 9/05 (a cold reader would trip on these)

| Item | Where |
|---|---|
| **board_log.tsv** created 9/17. It holds per-packet dispositions (acted/info-only/noted) with timestamps, and is now the drain receipt | board_log.tsv:1; git `4f6ab7e38` |
| **LAST_COMPLETION.md FROZEN 9/17.** Closeout 5 is now a **dated PROME memo** (`PROME/inbox/{date}_from-ZHAO_{slug}.md`). Guards glob both `inbox/` and `inbox/processed/` and sort by commit time | CLAUDE.md:56, :59, :246, :260 (re-key `c6ac32e81` 9/17 09:07) |
| **boot.py section [7] NEXUS_BRIEF CAPS** (≤100 lines, ≤32,550 B), added 10/09 on DAEDALUS PROSE-REMEDY | boot.py:306–327 |
| **R1 corrections step re-keyed to the WQ-399 receipt form** (field-less receipts are refused, rc 2). The first receipt under the new writer was COR-20261008-41 NO-OP | CLAUDE.md:33; board_log.tsv:23, :25 |
| **CADENCE WEEKLY + 9 WATCH_FOR terms** declared to PROME (WQ-295); R3 adopt/decline answered by name on 10/09 | board_log.tsv:12, :14 |
| **NEXUS_BRIEF rotation** 39,556 → 20,512 B, moved verbatim to `archive/NEXUS_BRIEF_COLD_20261009.md` (crc32 in file) | board_log.tsv:16; NEXUS_BRIEF.md:19 |
| **STATUS rotations #2–#7** (5 files, 9/17–9/25), with verbatim "→ COLD_… §ⓐ" pointers throughout STATUS | STATUS.md:9, :32, :47, :59, :106 |
| **New registry:** `registry/corrections_receipts.tsv` (611 B) | `registry/` |
| **New analytical artifacts:** ZHA-18 letter, MOFCOM 公告70 pre-reg and result, WATT trigger wording, as-made verification and ledger write | `reports/2026-09-17…09-25_*` (7 files) |
| **Two-clock 11/10 structure.** The IEEPA leg has been VOID since 2026-02-24 (ZHAO's own premise error, KB-183). A separate 11/27 clock (公告2024年第46号 cl.2, B2) exists | STATUS.md:13–22, :132 |
| **⚠️ Quirk: the charter sits 11 B under its own byte rule.** Any charter fix must be byte-neutral or rotate first, or ZHAO breaks CLAUDE.md:50 | CLAUDE.md:50; `wc -c` 32,539 |
| **⚠️ Quirk: in CATALYSTS.tsv the `priority` column carries state.** 10 of 21 rows are `DONE` and there is no status column. The countdown counts DONE rows as fired alerts | CATALYSTS.tsv header (8 cols); priority Counter {DONE:10, P2:4, P3:4, P1:3} |
| **⚠️ Quirk: local git exceptions that diverge from root canon.** "When SPAWNED by a coordinator: commit, do NOT push" is a push exception not listed in root §Scope note (root lists only TERRY and WALTER). The non-ff escalation "non-ff recurring mid-session" contradicts root's "bare recurrence is ordinary traffic", and the root dirty-path overlap check is not mentioned | CLAUDE.md:235, :242, :245 vs root CLAUDE.md §Git Protocol step 3 |
| **⚠️ Quirk: push verification "by CONTENT, never by SHA"** sits uneasily beside root's safe-push receipt line ("CONFIRMED: HEAD <sha> is on origin/master") and DAEDALUS's candidate-commit verification | CLAUDE.md:244 |

## 5. Defects to route to ZHAO (ranked)

| # | Defect | file:line | One-line fix |
|---|---|---|---|
| **D1** | **The outbox-routing claim is inverted.** STATUS says the two 9/25 packets "await PROME routing", but both were routed and processed on 9/25 (`BOND/HAWK/HENRY/VULCAN inbox/processed/2026-09-25_from-ZHAO-via-PROME_*`). The **9/30 packet** (`outbox/2026-09-30_…_MOFCOM-states-1-10-extension-in-writing-no-instrument.md`, to VULCAN/HAWK/HENRY/WATT/MIDAS) has **no routed copy at any recipient** after 14 days, and STATUS mentions it only in a "Done Sep 30" line | STATUS.md:99, :167, :151 | Replace :99/:167 with "9/25 ×2 routed 9/25; **9/30 MOFCOM-1/10 packet UNROUTED → PROME**", and ask PROME to route or decline. *(PROME leg: routing is PROME's call.)* |
| **D2** | **Stale owed item.** NEXT #10 still lists "`CLAUDE.md` re-key L56/L246/L260" as owed, and the LAST_COMPLETION banner says the "re-point held". The re-key landed 9/17 09:07 (`c6ac32e81`), 13 minutes after the banner was written (`4f6ab7e38` 08:54) | STATUS.md:166; LAST_COMPLETION.md:1 | Strike the item in NEXT #10 and amend the banner's ⚠️ sentence to "re-keyed 9/17 (c6ac32e81)". Keep "+ the owed 9/2 CLOSEOUT-1 edit", which is still un-applied (CLAUDE.md:50 has no "state which cost + measure the total" clause) |
| **D3** | **catalyst_countdown DOCKET leg ignores ownership and state.** It matches "ZHAO" anywhere in a row and never reads the state cell. As a result, RESOLVED **L670 (MARCO's L0 drain)** prints as "RECENTLY FIRED — SWEEP NOW" and counts toward the boot REVIEW verdict. RESOLVED-VOID **L436 (IEEPA)** prints as a live 11/10 upcoming row. L603 (a DAEDALUS evaluation) is also pulled in | catalyst_countdown.py:186–196; boot.py:219–220 | Match ZHAO in the owner column (col 3) only, and skip state cells starting `RESOLVED`/`VOID`/`DONE`. Then show the alert line on L670 and the clean line on a clean case (CHECK_STANDARD §3) |
| **D4** | **Fired-row counter counts `DONE` CATALYSTS rows.** The 10/09 "DONE" re-check row raised a boot alert today, and 10 of 21 rows carry `DONE` in the *priority* column (marker-role mixing, STATE_VOCABULARY class 9) | catalyst_countdown.py:222–232; boot.py:219–220; CATALYSTS.tsv `priority` | Add a `status` column, or exclude `DONE` from the fired counter, and keep priority tokens pure (P1/P2/P3) |
| **D5** | **The boot "China PMI" key figure points at a row left stale on purpose-built data.** VX-ZHAO-6.11 (Mfg PMI) still reads **Aug 49.8, dated 9/02**. The **Sept mfg 50.1** read on 10/09 was written only to VX-6.12 (Composite), and STATUS cites 6.12 for it | boot.py:74; VX.tsv `VX-ZHAO-6.11`; STATUS.md:64 | Refresh VX-6.11 to Sept 50.1 (NBS 9/30). Separately consider cadence-aware stale bars: KEY_STALE_DAYS=14 (boot.py:40) is red on monthly TIC/PMI half of every month, so with D3/D4 the boot reads REVIEW on every boot (10 alerts today) |
| **D6** | **Retired framing on cross-agent surfaces.** The NEXUS-consumed Domain line still reads "China UST **exit** (Belgium/Euroclear **proxy**)". The charter Role line says "LIQUID (China UST selling **via Belgium proxy**…)". CLAUDE.md:12 says both halves are retired: "exit" by the 7/16 reframe, the proxy by the 8/21 rho test | NEXUS_BRIEF.md:4; CLAUDE.md:6 | Re-word to "SAFE-reported Treasury-line reduction; Belgium = FYI level, proxy falsified (VX-1.09)". The CLAUDE.md:6 edit must be byte-neutral (see §4) |
| **D7** | **NEXUS_BRIEF is content-stale under a fresh As-of stamp.** CALIBRATION is dated 8/21 ("Aug 31 PMI is the registered arbiter"; "July TIC ~9/16" listed as uncertain; yuan 6.71). The SENDING table is 8/21. WAITING-FOR HANS "carry-confirm" was answered by 9/05 (profile §6). The FORWARD CATALYSTS header reads "refreshed 2026-09-17", a 9/20 LPR row is still open, :81 says "**All three clocks land 11/10**" while :83 marks the third VOID, and :85 cites the already-graded ZHA-16 "branch C". Ordering was met but content was not | NEXUS_BRIEF.md:25–32, :46–50, :59, :72, :78, :81, :85 | Re-cut CALIBRATION, SENDING, WAITING and FORWARD CATALYSTS from the 10/09 state, and strike :81's "three clocks" |
| **D8** | **The desk breaks its own "rewrite the spine, never prepend" rule.** The header stacks 10/9, 9/30 and 9/25 blocks, and BOTTOM LINE stacks OCT 9, SEP 30 and SEP 25 (11 lines). This is also where the 3,451 B rotation can come from | STATUS.md:4–6, :171–183; rule at CLAUDE.md:49, :69 | Keep the current header and BOTTOM LINE only. Rotate the 9/25 and 9/30 blocks verbatim to a COLD file, which reaches the <22,785 B stop |
| **D9** | **The TRADE.md unfreeze condition is not operational,** and the no-book stance is not declared in the charter (see §3 L4) | TRADE.md:1; CLAUDE.md:261 | Add an operational re-arm, e.g. "re-arm when TERRY carries a card whose primary rationale cites a ZHAO vector, or ZHAO proposes one"; declare research/signal, no book, in IDENTITY. Byte-neutral or after rotation |
| **D10** | **Dashboard and calendar rows past their own dates:** LPR "16th due Sun 9/20" (BOTTOM LINE :183 says it held); V6 As-Of "next Sun 9/20"; H.4.1 10/1 "still unread" (13 days, also a 10/09 memo GAP); matrix header omits 10/09 | STATUS.md:70, :86, :127, :76 | Update the cells, or mark them `[STALE <date>]` per the charter's discipline overlay (CLAUDE.md:61) |
| **D11** | **VX_HISTORY is neither live nor frozen.** It has 5 rows from 2026-02-13 and the charter describes it as live | VX_HISTORY.tsv; CLAUDE.md:259 | FROZEN-banner it, or resume appends. ZHAO's call, but pick one (root Data Hygiene: never the silent-rot middle) |
| **D12** | **OPEN_THREADS_2026-07-09 is aged and self-inconsistent.** It was last edited 7/16 (97 days). The Gaps row "Single custody proxy … zero KB entries" contradicts Thread #3 "RESOLVED 7/16 — HANS ran LUX/Cayman/Ireland". The charter treats it as the current register | OPEN_THREADS:19 vs :30; CLAUDE.md:262 | Re-issue a dated OPEN_THREADS with Q1, Q2, the NPS gap and Thread #4, or banner it and `git mv` it to archive/ (root retirement rule; the FILES-row reference is a nav reference) |
| **D13** | **Live-vector inbox item queued.** SIG-W-20261013-024 reports KOSPI −5.46% on the 10/13 close and SK hynix −10.09% (Korea vector 2, scored 🟢 1). SIG-W-20261010-004 is addressed to ZHAO as **ACTION** (Shelton, Treasury currency counselor with a China focus). The MIDAS approved-maintenance packet asks ZHAO to supply the −41.3% copper-import claim's month, scope, unit and comparator; that claim has been owed since 7/17 | inbox/WALTER/SIG-W-20261013-024.md; …/SIG-W-20261010-004.md (front-matter `action: ["BOND","ZHAO"]`); inbox/2026-10-12_from-MIDAS_approved-maintenance.md:5 | Triage at next boot per CLAUDE.md:26 (a) and (c), before the 10/16 TIC grade |
| D14 (low) | boot.py:180 comment says the month is parsed from "'updated' + value note", but the code reads the Source cell. CATALYSTS row 12 (Plenum) is a date **range** with `date_class=confirmed` (countdown 🟠). The STATUS rotation pointer skips #5 and #6. The cadence (WEEKLY) is absent from the charter | boot.py:180; CATALYSTS.tsv row 12; STATUS.md:9 | Comment fix · `date_class=modeled` · complete the pointer list · one charter line, byte-neutral |

**Escalation-class items (not ZHAO-only):**
- The root-divergent git exceptions (CLAUDE.md:235, :242) touch push mechanics, so they need a PROME/Will word before change.
- D1's routing leg is PROME's.

## 6. NOT-READ / coverage limits

| Item | Limit |
|---|---|
| `board_log.tsv` | All 24 rows read, but **each row cut at 600 chars**. The full notes for rows 2, 4–7, 9, 10 and 14 were not read |
| `inbox/` packets (9) | Heads only (~500 B). The full bodies of SIG-W-20261012-042/-043, -20261014-011 and the MIDAS news-sweep/construction packets were not read. No dispositions are implied |
| `workbook/KB.tsv`, `VX.tsv`, `FLOW.tsv`, `PREDICTIONS.tsv` | Not read whole. Only counts, headers, VX rows 1.02/6.11/6.12 and PREDICTIONS ZHA-01/10/18 (head of Notes) |
| `docket/CATALYSTS.tsv` | Only the header, priority counts and the Plenum row. The README was not read |
| `archive/*` (24 files), `reports/*`, `sources/`, `outbox/*` bodies | Not read. I listed them, read 1 outbox head (9/30) and the first 6 lines of NEXUS_BRIEF_COLD_20261009 |
| `PROME/inbox/processed/` ZHAO memos | Only the 10/09 memo's last 15 lines. The 9/25 and 9/30 memos were confirmed present but not read |
| Profile §6 L4 consumer evidence (HANS `## ZHAO ANSWER … NOT CARRIED` section) | **NOT-CHECKED.** A grep of HANS/STATUS.md found no such section header now (likely rotated). I did not search HANS's archive by content, and it is outside the requested rows |
| `corrections_boot_check.py ZHAO`, `claim_check.py`, `orphan_check.sh`, `brief_pin_check.py` | **NOT RUN** (not in scope). L5 rests on ZHAO's own 10/09 memo receipts plus git |
| `AGENTS/VOCABULARIES.tsv`, root `PROME/COMPLETION_SPEC.md` | Not read. They are referenced only |
| `PROME/registry/READS.tsv` declaration for ZHAO | Absent per read_cap_check. The perimeter is the charter heuristic, so the result is "clean within what the scan found" |
