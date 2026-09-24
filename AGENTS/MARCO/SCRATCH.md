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

### s30b — Will: "refresh the five July-31 vector rows" (all done)
| Row | Mark | Read |
|---|---|---|
| `GTR-01` Canada FL travel-search | BREACHED → **CRITICAL** | Aug −23.1% vs 2024; June's −43.8% was the only 2026 month past −40%. Two pulls agree within ~1pp |
| `3.02` FL–Snowbelt price spread | CRITICAL → **ELEVATED (borderline)** | +4.93pp vs 5.0 line; 9 of 12 basket variants under. **7/31 baskets were never recorded** → declared in `baselines/vx302_baskets.tsv` (forced rebase, −0.29pp on Jun). Narrowing is the robust part |
| `TX-02` Austin | BREACHED (held, duration 43 mo) | Aug −4.73% YoY, decelerating; rate leg now ELEVATED. Zillow revised LEVELS between vintages |
| `FL-03` FL days-on-market | NORMAL (held) | 81 = +9.5% vs baseline, 0.5pp from ELEVATED; YoY −6.9% |
| `CA-01` CA FAIR Plan | CRITICAL (held) | no new publication (still June); next ~mid-Nov (est.) |
- No desk carries any of these marks (grep) → no packets. New VX staleness floor 2026-08-11.

### s30c — Will: "refresh the four August-11 rows too" (all done)
| Row | Mark | Read |
|---|---|---|
| `1.03` intl visitor spending | CRITICAL → NORMAL → **ELEVATED (low), s30d** | BEA Travel exports Jan–Jul **−0.58%** (annualised −$1.25B); May–Jul up. The carried 2025 **−$8.3B never reproduced** (BEA 2025 +$1.28B). Trailing-12 window would read low ELEVATED |
| `3.01` FL household premium | BREACHED → **ELEVATED** | Matched basis 2.95x (Insurance.com 9/15). No source reaches >4x; the row's own cell said 2.4x |
| `SDL-01` foreign-born LF | BREACHED → UNRULED → **ELEVATED (Will-ruled, YoY basis)** | Aug YoY −379K (ELEVATED) / 2-yr −1,189K (CRITICAL). BREACHED = retracted-2.2M residue. **Will to rule the basis** |
| `SFE-03` Citizens | NORMAL band (held) | **PIF 266,231 @8/31, −4.3% MoM — depopulation resumed**; exposure **$74.8B** (carried $295.1B was Jun-2025). CORAL packeted; 10/1 chase closed |
- Three of four marks did not follow from their own data — same class as the 8/21 band audit. FLOW-REG-01 / FLOW-IMG-01 mark annotations corrected. VX floor now 2026-08-21.

### s30d — Will: "do item 2" = full band audit of all 36 live VX rows
- Method: 3 blind Opus readers (12 rows each, mark-vs-value, no desk context) → MARCO verified every flag at the row/primary before editing. Readers' files: job scratch `audit_g{0,1,2}_result.md`.
- **Re-graded:** `APT-01` ELEVATED→**CRITICAL** (declared 2-yr stack basis; still carried 3 withdrawn claims in its current read; duplicates `1.04`) · `CA-02` CRITICAL→**UNSCORED** · `1.03` NORMAL→**ELEVATED** (12-month-actual rule, consistent with EMG-01).
- **Confirmed on fresh data:** `2.01` BREACHED — TRAC June 2026 ICE arrests ≥39,563 vs FY24 avg 9,453/mo (≥4.19x).
- **Refreshed:** `2.03` Aug (NORMAL, 0.03pp margin) · Census V2025 → `3.04` (−56.5% was cross-vintage; −37.0%; **CORAL packeted**), `TX-04` (label fix, +67,299), `SBMD-01` (−482,326; AZ/NV carried figures didn't reproduce).
- **Text/label:** `2.08` single mark; `H2A-01` names its OR-leg; `NV-01` marked CARRIED; `SFE-03` band token; `CA-01` judgment-graded; `3.02`/`1.01`/`2.08` band-cell residue.
- **Open (MAINTENANCE T2-I):** merge `APT-01`/`1.04`; `H2A-02` lead-time p25 leg unreported; `CA-01` surge leg needs a number; `FL-01` level-vs-growth basis.

### Housekeeping
- **Archived** (`git mv` → `archive/`, created on purpose): `NOTES.md`, `OPEN_THREADS_2026-07-09.md`, `RP-MARCO-MBS_BASELINE.md`, `workbook/ML_BACKUP_20260418.tsv`, `workbook/VX_HISTORY.tsv`.
- **TRADE.md FROZEN** (canonical banner; IBOC premise died with Channel 4 LOW). **COUPLINGS** (both BRENT edges a month stale — crude → `ENR-02` consumer; freight edge → Resolved). **RESEARCH_STATUS**, **DEFERRED** (4 TOURISM entries closed-lapsed), **MAINTENANCE** (T1-F/T2-C/T3-B closed; T2-E partial; new T2-G voter-reg tool, T2-H VX tail), **FINDINGS**, **EXPECTED_SIGNALS** ES-06 (withdrew "on track"), **CLAUDE.md** (dead "CONFIRMED FINDINGS" pointer; condo 7.8mo; Canada −26.63%), **MEMORY** (BLS API supersedes the WebFetch workaround), MAR-24 cell text.
- STATUS: stale column labels, spring-vintage H-2A row, dead "READ FIRST" pointer, key-date order, MAR-12 added (was missing), LFPR item updated with Aug; **rotated 81% → <70% of read cap** (→ `_archive/STATUS_unresolved_rotated_s30_20260924.md`, `_archive/STATUS_s29_header_20260924.md`).

## NEXT SESSION
1. 🟠 **LVCVA August (~9/30)**.
2. 🔴 **Banxico AUGUST (Oct 1)**: SDL-01 re-spec print 2 of 2. Co-run the state-of-origin map. *(Citizens PIF chase closed 9/24 — pulled the 8/31 primary.)*
3. 🔴 **Wed 10/14: `ENR-02` leg 1** (verify the Oct CPI date for leg 2).
4. 🟠 **~Oct 15:** StatCan Sep (`ID-01`) · NTTO Sep · BTS July.
5. 🟡 **~Oct 20 (est.):** BLS state Sep — confirm `VX-2.06` on revised Aug.
6. 🟠 **~Oct 28: MIA September report** (MIA-2-consecutive trigger).
7. ✅ SDL-01 ruled (YoY → ELEVATED). 🟡 **MAINTENANCE T2-G:** cycle-matched voter-reg column. VX floor now 8/11 (1.03 / 3.01 / SDL-01 / SFE-03). Watch `3.02` and `FL-03` — both sit within 0.5pp of a band line.
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
**Inbox 2 UNPROCESSED** (LABOR 9/17 · ZHAO 9/18), not an inbox spawn. **WALTER lane:** `SIG-W-20260924-017` (grocery correction) arrived mid-session → logged **info-only** in `board_log.tsv` (MARCO never carried the claim). Moved to `processed/` after WALTER committed its delivery (`24c290efa`).
**Sent:** CARL (correction — voter-reg counter-signal was election cycle) · CORAL ×2 (Citizens 8/31 PIF 266,231 + FYI 3.01 re-grade; FL intl-migration −56.5% was cross-vintage → −37.0%).

## PUSH STATE
Session 30: see the closeout commit and the `safe-push.sh` receipt line.
