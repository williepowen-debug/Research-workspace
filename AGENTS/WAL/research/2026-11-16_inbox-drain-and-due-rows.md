# WAL — inbox drain, due rows, read cap (2026-11-16)

**Assignment:** PROME prome-6f wake on Will's word in PROME's chat 2026-11-16 13:45 ET (items 1–5). Runtime: Claude Code, Opus 5.5 (`claude-opus-5-5`), desktop checkout; session ID not exposed (UNKNOWN). Git: no pull and no push (GitHub name lookups failing today, per PROME); HEAD was 2 commits ahead of the last fetch at boot; foreign dirty paths (`PROME/state/ORCH_INFLIGHT.md`, `PROME/state/ORCH_LOG.tsv`) left untouched.

**Live price (root rule #4):** WAL **$73.22 (−2.10%)**, KRE $71.90 (−1.15%), vendor quote via `scripts/boot.py` at 14:02 ET 11/16, intraday not a close. Spot is **4.41% below** v2.5 EV $76.60. Boot checks: corrections rc 0; SEC: no issuer filing since 11/11; FFIEC Q3 already carried; FINRA latest settlement 10/30 (already logged); KB expiry 98 of 195 ACTIVE rows past Stale_By at boot (not judged today); predictions-due silent at boot (no open row existed).

## 1. Inbox — every packet's disposition (8 loose packets; WALTER lane empty)

| Packet | Disposition | What it changed |
|---|---|---|
| 2026-11-11 DEWEY 003R full-population refresh | noted → **KB-296** | Logged the Q3 population read with its required caveats (United Fidelity = 69.1% of the $1–10B band's noncurrent increase; WAL's $10–100B band trigger OFF quarter on quarter). Changed no score: WAL's own broadening test is its frozen DP2 |
| 2026-11-11 DEWEY 003R placement continuation | noted → folded into **KB-296** | Changed nothing beyond KB-296; comparator-date and denominator rule recorded there for any future citation |
| 2026-11-11 DEWEY 003R six-bank partial | info-only (report's own action: "retain as information") | Nothing |
| 2026-11-11 DEWEY L517 Plaza pre-read | noted → **KB-295** | H1–H11 read-sheet: no move. Records the 11/17 final cash-collateral hearing and the lease-rejection motion |
| 2026-11-11 DEWEY Plaza marketing and document limits | noted → **KB-295** | Adds the broker's 31% occupancy representation; H7/H8/H11 still unread. No move |
| 2026-11-12 DEWEY L517 no opposition | noted → **KB-295** | No objection by the 11/3 deadline; consistent with the October stipulation, not a value signal. No move |
| 2026-11-16 DEWEY L517 pre-check | noted → **KB-295** | Docket unchanged since #127 (11/11). No move; next observable is the 11/17 result |
| 2026-11-12 DAEDALUS WQ-678 harness lines | **acted (partly)** | Changelist A: none for WAL. Changelist B (10 optional trims): **applied C13** (stale "v2.4" in three charter rows dropped) and **C20** (stale "awaiting the 10-Q" parenthetical dropped). **Declined C14–C19, C21, C22** today: DOCKET L810 asks for this charter's size fix as a VERBATIM hot/cold split with no rewording, which was done (below); C21 rewrites a routing line, and under L810's class C4 a charter change that moves a route goes to Will; the rest reword history-in-step text that the split already took out of the boot-read path or that git history preserves. Re-offerable at a later ordinary wake |

All eight moved to `inbox/processed/` with `git mv`. Nothing in the inbox is a trade finding (every DEWEY action block says no price, recovery or timing fact for TERRY).

## 2. Due rows (graded by this desk's own written rules; nothing pre-graded)

| Row | Due | Done today |
|---|---|---|
| Forward Q4 predictions (`Q3_10Q_RESCORE_RULE_2026-10-22.md`: register after WAL-01 closes, each with a dated Resolve_By and anchor type; STATUS carrier "by Sun 11/15") | 11/15, **one day overdue** | **Registered WAL-03 to WAL-07** in `workbook/PREDICTIONS.tsv`, all OPEN: Q4 NCO > 40bps (20%); hotel franchise finance nonaccrual > $0 at 12/31 (35%); OREO properties > 27 at 12/31 (50%); Q4 "deposit costs" line > Q3 $165.4M (55%, the issuer-basis ECR line the 11/11 rate read asked for); $99M credit charge-off or specific reserve disclosed by the FY2026 10-K (25%). Resolve_By 2027-01-31 (expected event, re-pin on announcement) or 2027-03-01 (10-K statutory). These are registrations, not grades |
| OZK pointer behind KB-228 (STATUS carrier "~Thu 11/5", overdue) | ~11/5 | Re-read OZK STATUS (commit 151a4af402, 11/11): Q3 10-Q graded 11/7, RaDD pass on its own tables, no reserve or readvance. KB-228 stands; Stale_By extended to 2027-01-31 with that reason. No OZK figure mirrored |
| DOCKET L810 charter hot/cold split (WAL leg) | next launch brief (this one) | Done: see § 4 |
| DOCKET L517 Plaza Continental (WAL consumes) | re-dated by PROME to 11/18 | **Not due; not pre-graded.** Today's consumption is the inbox drain above |
| DOCKET L515 (FDIC Nano disposition, 2027-06-25), L518 (Makhijani trial, 2027-01-12) | not due | Not graded |
| KB-294 Basel III disclosure (review 11/25) | not due | Not retried |

## 3. Who is paying to extend — logging only

Lines live in `research/2026-11-16_who-pays-to-extend.md` (8 credits). Pointer in STATUS. Moves no score, band, gate or trigger.

## 4. Read cap (`scripts/read_cap_check.py --agent WAL`)

| Surface | Before | After | How |
|---|---|---|---|
| `CLAUDE.md` (charter) | 26,842 B, 82% | 20,510 B, 63% | DOC OWNERSHIP and FILES sections moved verbatim to `CHARTER_REFERENCE.md` (sha256 e47b54e6…428b), pointers left. C13/C20 and the PREDICTIONS list were edited just before the move, recorded in that file's header |
| `STATUS.md` | 27,644 B, 85% | 20,072 B, 62% | "LATEST (10/28)" table moved verbatim to `archive/STATUS_rotation_2026-11-16.md` (sha256 900d082f…a557) |
| `MEMORY.md` | 25,274 B, 78% | 5,143 B, 16% | Prior session notes (11/4 and earlier) moved verbatim to `archive/MEMORY_rotation_2026-11-16.md` |

Re-run after the moves: `READ-CAP-RESULT rc=0 … rotation_due=0` (all three under the 70% stop).

## Closeout checks

- REGINALD channel: nothing new since WAL's 11/11 ACK of the 11/05 entry; no new entry written (no new info, correction or threshold firing for REGINALD).
- Drift check: 0 named-field issues (the loose-inbox issue cleared). 4 "new identities" are coincidental token matches, not revived claims: today's −2.10% day change on STATUS lines 9 and 58 collides with a retired 8/23 "−2.10% required move" token; an 11/11 NII "+2.6%" (KB-288 and the rate read) collides with a retired 8/23 "+2.6%" buffer token. The reviewed-identity baseline was not edited.
- Claim check (weekday): one flag, `workbook/PREDICTIONS.tsv:3` "Wed 10/22" (10/22/2026 was a Thursday) inside a dated historical header line; left as written, recorded here.
- Consumer check: no published figure superseded today, so not run. Orphan check: no WAL-authored orphan; CREED's dirty files are not mine and were not touched.
- Not changed, with reason: THESIS/CHANGELOG/WEAKNESSES/SCENARIOS (no thesis move; registering predictions is not a re-mark), POSITIONS (no broker data), MARKET_TRACKER (last snapshot 11/10 is inside its 10-day window; FINRA 11/14 settlement not yet published).

## 5. Context (no action)

Chase login outage confirmed by the bank (CYPHER, CYB-INC-072, relayed by PROME, not verified here): nothing in it names Western Alliance. No WAL action.

## Trade read

**No material finding for TERRY today.** The price move (−2.1% on the day, 4.4% under EV) is within the 20-day realized volatility of 33.4% (10/30–11/10 tracker), and no new WAL fact explains it. No direction is argued.
