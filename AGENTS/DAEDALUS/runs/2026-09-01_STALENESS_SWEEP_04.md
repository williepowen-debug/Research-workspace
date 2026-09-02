# Fleet Staleness Sweep — RUN #4 — 2026-09-01 21:01 ET

**Owner:** DAEDALUS · **Cadence:** 21d · **Prior run:** 2026-08-11 (#3) · **This run:** ON CADENCE (21d, +0d) — the L5 cadence leg that failed three times before held. · **Playbook:** `sweeps/STALENESS_SWEEP.md` · **Registry:** `sweeps/REGISTRY.tsv`

## 0. Verdict in one line
15 flags at 10 desks. Read at the artifact they split **4 REAL · 8 HELD-HONESTLY · 3 DECLARED-IN-THE-WRONG-FORM**. Zero dormant freezes qualify (every flagged owner committed within 11 days). The durable finding is about the instrument: it cannot make that split, and four desks have independently invented the header field that would let it (§8 M2).

## 1. Perimeter — stated before the verdict
| Pass | Command (repo root, `.venv/bin/python3 scripts/ledger_staleness.py …`) | Result |
|---|---|---|
| default | `--all --quiet` (30d vs own STATUS) | 10 desks / 15 surfaces, rc=1 |
| trade | `--trade --all --quiet` | **0 flags across 23 graded**; 16 desks matched NO trade surface and are **named** (ATHENA CORAL CREED DAEDALUS FALCON HANS HENRY HOMER LIQUID NEXUS OSPREY RED SENTRY SHADE WALTER YEYOU). Run #3's registered item "`--trade` fail-loud / report-unmatched" is **SHIPPED** (perimeter line, `e23aeb51b` 2026-08-22) — CLOSED. |
| strict | `--all --strict --quiet` | 26 flags, all exempt-class (§3) |
| writes | `--all --writes --quiet` (bar 12) | 16 ledgers / 12 desks ≥12 STATUS-writes behind (§3) |
| abs-floor | `--all --abs-floor --quiet` (90d) | 1 fire: RED VX.tsv ABS 92d (§3) |
| read-cap | `AGENTS/DAEDALUS/scripts/read_cap_check.py --all` | 19 over budget, **0 mandated** — within the heuristic perimeter only (§6) |

Every pass prints per-desk perimeter lines (e.g. CARL 52 scanned + 9 TSVs NOT scanned; MARCO 7 scanned + 19 NOT — `baselines/`). **NOT-scanned TSVs are outside this verdict.**

**Dark census** (last self-authored commit, `git log`): every flagged owner ≤11d — CRUISE 8/21 (oldest), OSPREY 8/23, all others ≤8/28; FALCON/REGINALD/TERRY/WALTER/BRENT/MIDAS/RED 9/1. Pre-approval leg (b) fails for all ⇒ **0 freezes**. Fleet-wide, only CRUISE (11d), YEYOU (12d) and OSPREY (9d) exceed a week; DEWEY/RAV have no STATUS.md (invisible to every STATUS-relative check — carried from run #3).

## 2. Default-pass flags, classified at the artifact
| Desk · surface | Δ | What the header says | Class | Disposition |
|---|---|---|---|---|
| CARL `thesis/PREDICTIONS.tsv` | +34d · **28 STATUS-writes** | no header, no banner (81 KB) | **REAL** | packet → CARL |
| CARL `sub_agents/PHAN/workbook/COCKROACH.tsv` | +49d | two-clock, APPEND-ON-EVENT; hygiene clock **2026-08-15** (STATUS 8/27) | HELD, hygiene clock one session behind | packet → CARL (same packet) |
| CARL `…/PHAN/workbook/REGULATORY.tsv` | +49d | same | HELD | same |
| CRUISE `workbook/FLOW.tsv` | +43d | no header, no banner; FL-CRU-02 "7/2 DE-ESCALATED", FL-CRU-01 "Brent $71 TAILWIND" vs FALCON STATUS 9/1 adjudicating GATE 1/2 on live mine claims | **REAL — PAT-062 (stale AND directionally flattering)**; desk has **0** `ledger_staleness` wiring (born 7/2, after the 7/4 rollout; dark 7/3→8/14) | packet → CRUISE |
| FALCON `workbook/FLOW.tsv` | +33d · 14w | migration note only, no clock; rows self-annotate `[STALE Apr20 figs]` | **REAL** — staleness written IN-ROW where the tool reads HEADERS | packet → FALCON |
| FALCON `workbook/WARRISK.tsv` | +41d | two-clock; `Last re-pull ATTEMPTED: 2026-08-20 — NO NEWER PRIMARY`; clock deliberately not advanced | HELD (exemplar) | none |
| FLG `MATURITY_WALL.tsv` / `MI3_FLG.tsv` / `NONACCRUAL_FLOW.tsv` | +60d ×3 | "EXPECTED-STALE BY CONSTRUCTION", quarterly, `Next: 2026-11-14 / 11-06 / 2027-03-01` | **DECLARED, wrong form** — the tool's `# Cadence: SCHEDULED next_due=` token is parsed by `--nudge` only, and FLG's `Next:` spelling by no mode | packet → FLG (one-line conform) + M1 |
| MARCO `workbook/VX.tsv` | +52d | two-clock, dated to the OLDEST live vector, tail being worked (gap closed 7mo→7wk since 8/21) | HELD | none |
| OSPREY `workbook/WARRISK.tsv` | +30d | two-clock; 4th empty canvass logged 8/20 | HELD | none |
| OTTO `workbook/SHELF_ACTIVITY.tsv` | +34d · 21w | single-row probe log 2026-07-25, no header; **named in neither CLAUDE.md nor STATUS.md**; OTTO `boot.py` wires `ledger_staleness` ⇒ alarm has printed at every OTTO boot since ~8/24, unactioned | **REAL — PAT-095 n+1** (alarm ≠ ask) | packet → OTTO (the named ask) |
| OZK `thesis/PREDICTIONS.tsv` | +40d | two-clock; `Last reviewed: 2026-08-28`, no confidence moved since 7/23; header documents the 8/28 rule-8 fix | HELD | none |
| RED `workbook/VX.tsv` | +88d · ABS 92d | two-clock, alert deliberately LIT while 9/17 vectors CARRIED-not-measured (S33) | HELD (RED's own open item) | none new |

**Already-routed check:** none of the four REAL surfaces has been packeted before (grep of `outbox/`, `inbox/processed/`, owners' inboxes: 0 prior packets naming them). Owner inbox depth at dispatch: CARL **26 unprocessed** (10 staleness-related) · CRUISE 3 · FALCON 0 · FLG 1 · OTTO 3. CARL's depth is flagged to PROME; a 27th packet into that inbox is the run #3 MARCO shape one notch earlier.

## 3. Candidate passes
- **strict (26):** `SCHEMA.tsv` ×14 (static by design — exemption correct) · `VX_HISTORY.tsv` ×4 (HANS +196d, MARCO +202d, OTTO +208d, ZHAO +189d) · archives ×4 (BROCK KB_ARCHIVE +155d / PREDICTIONS_ARCHIVE +50d, MARCO ML_BACKUP +126d, SAM FLOW_ARCHIVE +91d = run #3's named pair; SAM live 8/28 — owner's call, not re-routed). **No defect.**
- **writes (16 ledgers ≥12 STATUS-writes behind, 12 desks):** SAM GPIF_FLOWS **30w** · CARL thesis/PREDICTIONS 28w · REGINALD MI3_COHORT 24w, NDFI_COHORT 20w, ACL_ROLLFORWARD 18w, RUNWAY 18w, FLOW 14w · BRENT INCIDENTS 21w, LESSONS_INDEX 13w · OTTO SHELF_ACTIVITY 21w · HOMER MULTIFAMILY 20w · LIQUID PREDICTIONS 20w · HENRY PUBLISHED 16w · **DAEDALUS SURFACES 15w (mine — serviced at the Production Review this session)** · FALCON FLOW 14w · VULCAN S4_SERIES 14w · BOND FLOW 13w · SAM TRADE_BALANCE 13w · AEOLUS SERIES 12w. Playbook §3b: CANDIDATES for the owner to confirm cadence — carried in the PROME rollup, no per-owner packet on the writes read alone (4 overlap §2).
- **abs-floor (90d):** RED VX.tsv only. First live fire of the PAT-092 counter fleet-wide — and it fired on the one ledger whose owner is deliberately holding the alert lit. The counter works; it added nothing this run.

## 4. Class-10 assertion-row leg (§3c) — first base-rate measurement
- **Scope:** 49 coordination-ledger-class files (`AGENTS/*/docket/*.tsv`, `board/BOARD_LOG.tsv`, `registry/*.tsv`, `*QUEUE*`, PROME DOCKET/WILL_QUEUE). **Token set:** OWED · PENDING · NEVER-DELIVERED · UNDELIVERED · AWAITING · CARRIED. ⚠️ Naming-keyed (PAT-078): the count is a **LOWER BOUND** on standing-state rows.
- **Fleet excl. PROME:** 30 line-matches → **13 standing-state rows** after removing catalyst/fire rows (Class 3 / fire-ledger, out of scope by the leg's own text). **PROME DOCKET.tsv: 138 line-matches — PROME-lane, not graded here.**
- **Grade (a) completion-artifact path/pattern · (b) expiry-or-resolver date:** **both 0/13 · one 8/13 · neither 5/13.** The five carrying neither: REGINALD `board/BOARD_LOG.tsv` `BACKFILL-PENDING` ×3 (SIG-W-20260509-003/004/017, standing since 2026-05-09 = **115d**) · CREED `registry/THRESHOLDS.tsv:18` "AWAITING REGINALD (dark since 8/13)" (REGINALD is live 9/1 — a named ask can land now) · HOMER `docket/CATALYSTS.tsv:33` "PENDING CARL RULING — no date; chase at CARL's next boot" (self-aware).
- **Verdict for the leg:** volume (13 rows, 5 bare) does **not** justify a script enforcer; the class stays a sweep leg + conform-on-touch. Re-measure at run #5; if the bare count grows while the token set is unchanged, that is the evidence line.

## 5. Doc-retirement queue (rides this sweep — registered 8/17)
- Own-dir census (`upgrades/ builds/ design/`, last commit >60d): **1 file** — `upgrades/HANDLE_SWEEP_independence-action.md` (2026-07-03). Referenced by `BLUEPRINTS/market-agent.md:42` (a live protocol doc travels it) ⇒ **NOT eligible** (clause ②: nav refs don't count; blueprint refs do).
- 7 files cross 60d by 9/16 (DEWEY_DRAFTS_REVIEW, WP2_KORE_REPORT, BATCH_01_handles, BATCH_03_net-new, BRENT_CARD, VIOLET_LIQUID_FIRMING, + the above), each with 1–5 refs — first real sweep at the registered ~9/16 date. **0 moves this run.**

## 6. Read-cap leg
`read_cap_check.py --all`: 19 over budget, 0 mandated. **Stated within the heuristic perimeter** — PROME's 8/31 packets show this instrument sees 1 of 6 PROME boot reads and is blind to cross-agent mandated reads by construction; the READS.tsv consumer half is next on this session's board. `CLAUDE.md` (mine) at 32,443 B = **99.7 % of budget** — any charter edit this session must be net-neutral or trim first. CARL `thesis/PREDICTIONS.tsv` 81,390 B = 250 % — discovery, named in the CARL packet.

## 7. Self-scope (PAT-050)
outbox flat files: **0** · `SURFACES.tsv` 15 STATUS-writes behind → Production Review this session · FLEET_MAP self-row scored 8/28 (4d) · REGISTRY row updated this run · `runs/` gains this record.

## 8. Mechanism findings → two proposals (Will-gated; PAT-035 additive, default mode byte-identical, §3 both paths at ship)
**M1 — `--all` honors the declared-quiet vocabulary.** `# Cadence: EVENT-DRIVEN` / `SCHEDULED next_due=YYYY-MM-DD` / `EXEMPT-BY-CHARTER` is parsed by `--nudge` only. The fleet sweep prints a declared-quiet ledger as a bare stale line, so FLG's three correctly-declared quarterly series cost a human read every run. *Effort:* ~20 lines, reuse the nudge parser. *EV:* 3 of 15 flags self-classify; every future SCHEDULED ledger stops costing a read.

**M2 — canonize the ATTENTION clock.** Four desks invented the same third header field in four spellings: `Last re-pull ATTEMPTED:` (FALCON, OSPREY) · `Last hygiene/no-event check:` (CARL) · `Last reviewed:` (OZK) · RED in prose. Each exists to say "the data clock is old ON PURPOSE and someone looked on <date>" — the exact state PAT-044 forbids laundering into the data clock. Proposal: one canonical key (`# Last attention: YYYY-MM-DD`, STATE_VOCABULARY + the PAT-044 header canon), and `ledger_staleness` prints `held (attention Nd)` when attention ≤ threshold, `stale AND unattended` when attention > threshold or absent. Data clock untouched. *EV:* today's 15 would have split 4/8/3 **without a human read** — this is the difference between a sweep that needs an hour of judgment and one that reads itself. *First step:* Will's word on the key name; then a 6-case capable suite (both spellings ×2 desks, absent, stale-attention).

**Design lesson (PAT-011 extended, not minted):** when four desks converge on the same field in four spellings, the vocabulary is late, not the desks. Convergent independent invention is a canonization trigger.

## 9. Dispositions
- **Freezes:** 0 (pre-approval unused; nothing qualified).
- **Packets (carve-out ①):** CRUISE · FALCON · OTTO · CARL · FLG (owner freeze-or-refresh, each one file) + PROME rollup (writes candidates, Class-10 base rate, M1/M2, CARL inbox depth, REGINALD/CREED bare rows). Recipients dark at dispatch except PROME ⇒ messaging rule 6b, PROME doorbelled.
- **Patterns:** PAT-011 n+1 (convergent invention = vocabulary latency) · PAT-095 n+1 (OTTO SHELF_ACTIVITY alarm printed ~8 boots unactioned).
- **Registered items closed:** `--trade` fail-loud (run #3) — SHIPPED, verified in this run's output.

## 10. NOT done, stated
- Root canon 1c-bis nudge line spot-check (§3b): present — PASS. Whether desks RUN it is not measured here.
- No owner file edited. Content-drift read (PAT-062) performed for CRUISE only; FALCON FLOW rows self-annotate STALE and were not re-read against the tape.
- PROME DOCKET Class-10 rows (138 matches) not graded — PROME-lane.
- Confirm-reads (did the owner consume?) for run #3's packets (ORACLE, CARL 4b, MARCO) not run — MARCO's VX header (8/21) shows uptake at the artifact; the other two are unverified.
