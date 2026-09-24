# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** session 30 — opened **2026-09-24 ~15:05 ET** (Thu), Will-directed "boot up, read through your files, sweep for stale or old info"; closed ~16:xx ET. Same-day follow-on to s29.

## CHANGES SINCE (session 29 → 30) — same day
- Nothing new published for MARCO's docket. Boot clean: WALTER lane empty, corrections rc 0, fetchers current, drift clean. Local 1 ahead of origin, nothing incoming; CARL's two data TSVs dirty in the tree (not ours — left alone).

## WHAT I DID (session 30) — stale sweep, no thesis version move
### Data rows refreshed on primaries (the 4 VX rows >60d)
| Row | Was | Now | Consequence |
|---|---|---|---|
| `REM-02` Central America remittances | 7/2, IDB secondary, Q1 +9.1% | **Jan–Jul +7.2% YoY, Jul +3.7%** (Banguat/BCR/BCH own files); NORMAL, Honduras alone ELEVATED | **MAR-12 35→8%** (Sep–Dec must avg −16.4%); carried Q1 was 2.3pp low. Docket row 2027-01-31 added |
| `EMG-01` IRS expatriates | 7/2, NORMAL on 2025's 4,889 | **H1-26 3,243 (+38.5%); trailing-4Q 5,790 ⇒ ELEVATED** | "+102% YoY" was QoQ — fixed in THESIS/FINDINGS/VX |
| `2.06` construction wage gap | 7/25 NORMAL | **Aug prelim +2.43pp ⇒ ELEVATED**, first crossing in 20 mo | Vector only (THESIS v3.0 bars Channel-1 reopen). Confirm ~10/20 (est.) |
| `FL-01` FL L&H wages | 7/25 | Aug $23.96 vs US $23.74; still Amendment-2 artifact; $15 step 9/30 | none |
- StatCan Q2 BOP (carried "unpulled" since late Aug): Canadians' US travel spend **C$6,513M, +1.2% YoY / −13.5% 2-yr**; the carried Q1 "+$1.3B travel" was total services — TIMELINE corrected. `KB-CAN-48`.
- **Voter-reg "counter-signal" re-based:** +35.6% YoY is midterm-vs-off-year; vs 2022 **−21.0%**. Now "not a direction tell either way." STATUS, ES-06, NEXUS fixed; **CARL packeted** (it carries it in `handoff_RED/COUNTER_LOG.md`).
- Helpers: 2 Opus subagents (remittances; IRS + StatCan). Load-bearing figures re-verified at source by me (Guatemala Aug in the xlsx; StatCan vector via WDS; FR Q2 doc via API — FR name count NOT re-counted).

### Housekeeping
- **Archived** (`git mv` → `archive/`, created on purpose): `NOTES.md`, `OPEN_THREADS_2026-07-09.md`, `RP-MARCO-MBS_BASELINE.md`, `workbook/ML_BACKUP_20260418.tsv`, `workbook/VX_HISTORY.tsv`.
- **TRADE.md FROZEN** (canonical banner; IBOC premise died with Channel 4 LOW). **COUPLINGS** (both BRENT edges a month stale — crude → `ENR-02` consumer; freight edge → Resolved). **RESEARCH_STATUS**, **DEFERRED** (4 TOURISM entries closed-lapsed), **MAINTENANCE** (T1-F/T2-C/T3-B closed; T2-E partial; new T2-G voter-reg tool, T2-H VX tail), **FINDINGS**, **EXPECTED_SIGNALS** ES-06 (withdrew "on track"), **CLAUDE.md** (dead "CONFIRMED FINDINGS" pointer; condo 7.8mo; Canada −26.63%), **MEMORY** (BLS API supersedes the WebFetch workaround), MAR-24 cell text.
- STATUS: stale column labels, spring-vintage H-2A row, dead "READ FIRST" pointer, key-date order, MAR-12 added (was missing), LFPR item updated with Aug; **rotated 81% → <70% of read cap** (→ `_archive/STATUS_unresolved_rotated_s30_20260924.md`, `_archive/STATUS_s29_header_20260924.md`).

## NEXT SESSION
1. 🟠 **LVCVA August (~9/30)**.
2. 🔴 **Banxico AUGUST (Oct 1)**: SDL-01 re-spec print 2 of 2. Co-run the state-of-origin map. Chase CORAL on Citizens PIF.
3. 🔴 **Wed 10/14: `ENR-02` leg 1** (verify the Oct CPI date for leg 2).
4. 🟠 **~Oct 15:** StatCan Sep (`ID-01`) · NTTO Sep · BTS July.
5. 🟡 **~Oct 20 (est.):** BLS state Sep — confirm `VX-2.06` on revised Aug.
6. 🟠 **~Oct 28: MIA September report** (MIA-2-consecutive trigger).
7. 🟡 **MAINTENANCE T2-H:** VX tail rows 3.02 / CA-01 / FL-03 / GTR-01 / TX-02 (7/31). **T2-G:** cycle-matched voter-reg column.
8. 🟡 **Inbox (only if Will asks):** LABOR 9/17 · ZHAO 9/18.
9. **Do NOT hunt a fifth Channel-1 transmission instrument** — and do not read `2.06` ELEVATED as one.

## OPEN THREADS
| Item | Status |
|------|--------|
| 🔴 FL-$ hole | DEWEY `MARCO-DR-1` = PROME L466, needed-by 11/16; retraction fallback |
| 🟠 MIA Aug −5.69%: demand or capacity? | Sep report ~10/28 |
| 🟠 SDL-01 re-spec 1 of 2 | August ~Oct 1 |
| 🟡 `2.06` ELEVATED (prelim) | ~10/20 |
| 🟡 MAR-12 at 8% | resolver ~late Jan 2027 |
| ⚠️ Read budgets | STATUS <70% after rotation; MEMORY 74% (351 B to trigger) — next MEMORY addition rotates first |

## Mail state
**Inbox 2 UNPROCESSED** (LABOR 9/17 · ZHAO 9/18), not an inbox spawn. **WALTER lane:** `SIG-W-20260924-017` (grocery correction) arrived mid-session → logged **info-only** in `board_log.tsv` (MARCO never carried the claim). ⚠️ **File left in `inbox/WALTER/`** — WALTER had not yet committed its delivery, so a `git mv` would break WALTER's sweep commit. **Next boot: `git mv` it to `processed/`** (it is already in board_log, so the drain's not-yet-logged filter will skip it — do it by hand).
**Sent:** CARL (correction — voter-reg counter-signal was election cycle).

## PUSH STATE
Session 30: see the closeout commit and the `safe-push.sh` receipt line.
