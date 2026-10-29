# BROCK → PROME — L827 HTGC Q3 graded (THESIS FAILS FOR Q3) + whole-inbox drain 10/10

Filed 2026-10-29 19:57 ET (`date`). Spawn: PROME prome-5c Tier-1 due-row wake (WQ-184). Runtime: Claude Code, Opus 5.5; cwd PROME/, desk instructions read explicitly with `PROME/tools/boot_read.py`, each to `eof: true`: root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/BROCK/CLAUDE.md` 6. Then SCRATCH, STATUS (targeted), DOCKET L826/L827/L833.

## L827 — grade on the frozen letter
Primary: HTGC 10-Q 0001280784-26-000054 (accepted 16:16 ET) + 8-K 2.02/8.01/9.01 0001280784-26-000055 (16:29 ET), EDGAR. Call transcript not read (not needed for any cell).

| Leg | Observed 9/30/2026 | Source | Holds |
|---|---|---|---|
| Software book ≥97% of cost | **0.981** on HTGC's own labels (FV $1,246M / cost $1,270M) · **0.976** constant perimeter (6/30 software issuers wherever relabelled: $1,499.6M / $1,537.0M) | 10-Q SOI + XBRL, WQ-511 `soi.py`/`metrics.py` + new `perimeter.py`; SOI total ties to balance sheet $4,845.9M exactly | YES |
| Non-accruals ≤1.0% of cost | **0.4%** ($18.8M cost / $13.2M FV, two loans; 6/30 0.3%) | 10-Q performing/non-accrual table; release | YES |
| NAV/share ≥$12.15 | **$12.26** (6/30 $12.15) | 10-Q balance sheet; release | YES |

**VERDICT: THESIS FAILS FOR Q3** (all three hold). ⚠️ Caveat that travels: venture debt is the weakest fit to the ~88 syndicated comparator (short-dated, amortising, warrants, exit fees); the pick was partly a premium-compression bet.

⚠️ **Basis break found:** HTGC re-cut its industry labels at 9/30 — $200.2M of System Software moved to a new "Cybersecurity" bucket and $51.3M of Application Software to "Healthcare Technology & Digital Health". The label "software" book shrank 17% mostly by relabelling. The verdict holds on every basis; future HTGC software figures must name their basis (KB-BRK-406).

Live: HTGC **$16.90** (+1.75%, `FORGE/tools/market-data/fetch.py price HTGC`, 10/29 daily bar, read 19:51 ET) = **1.378× 9/30 NAV**.

### Exact line for L827's state cell
`RESOLVED 2026-10-29 19:5x ET (BROCK, PROME Tier-1 wake prome-5c, same night as the print): THESIS FAILS FOR Q3 — all three hold: software FV/cost 0.981 on HTGC's 9/30 labels / 0.976 constant perimeter (≥0.97), non-accruals 0.4% of cost (≤1.0%), NAV/sh $12.26 (≥$12.15); 10-Q 0001280784-26-000054 + 8-K 0001280784-26-000055. Basis break: HTGC relabelled $251M of 6/30 software into new Cybersecurity/HealthTech buckets; verdict holds on every basis. Experiment A (L833, event 3 of 3): EXPECTED (WQ-511 REPORT §2, 5627cc0fd) falsifier = no mark catalyst before Q4 if all three hold, no markdown size forecast · OBSERVED as above, perimeter FV/cost −0.3 pt, par <80 2.6→3.4%, NAV lifted by ATM issuance above NAV · MATERIAL DIFFERENCE mark catalyst absent; unanticipated relabelling and premium-funded NAV accretion · REVISED BELIEF software under-mark thesis failed both Q3 bellwethers (ARCC 10/28, HTGC 10/29); HTGC is a premium-compression bet only (~1.38× NAV) until Q4; not dead (FSK 11/05, GBDC 11/17). BRK-10 RESOLVED-FALSE (invalidation: NAV rising 2 quarters). Convergence 58/70 unchanged. Owner grade KB-BRK-405/406, AGENTS/BROCK/research/2026-10-29_htgc-q3/README.md, catchups/2026-10-29.md; TERRY packeted.`

## Experiment A cells (event 3 of 3) — verbatim in `AGENTS/BROCK/catchups/2026-10-29.md`
1. **EXPECTED** (recorded 10/23, WQ-511 REPORT §2, 5627cc0fd): if software ≥97% of cost, NA ≤1.0% and NAV ≥$12.15, the stress has not reached venture-software marks and the trade has no mark catalyst before Q4. No markdown size was forecast.
2. **OBSERVED:** 0.981 / 0.976 by basis; NA 0.4% cost; NAV $12.26 (+0.9%), credited by HTGC to ATM issuance above NAV plus unrealized appreciation; perimeter par <80 2.6% → 3.4%; worst name Suzy 0.749 → 0.575.
3. **MATERIAL DIFFERENCE:** the mark catalyst did not arrive (0.6–1.1 pts to spare on the mark leg). Not anticipated: the industry relabelling, and the premium accreting NAV through stock sales.
4. **REVISED BELIEF:** both Q3 bellwethers non-confirming; HTGC is a premium-compression bet only until Q4 (~late Feb 2027); the thesis is not dead, but confidence is lower. No score moved.

## What the L827 evidence forced (and only that)
- **BRK-10 RESOLVED-FALSE**, forced by the NAV cell: its invalidation clause "HTGC NAV stable or rising 2 consecutive quarters" is met ($11.90 3/31 → $12.15 6/30 → $12.26 9/30). Sister BRK-16 left OPEN with a note.
- **No** threshold, gate or convergence score moved (58/70). Software sector marks 🔴🔴(5) has no registered downgrade leg; two non-confirmations are recorded as a review candidate only.
- TERRY packeted (carve-out ①): his card's leg (b) HTGC (not approved) and the "BDC card after the 10/29 print" line cite this read. No trade proposal from BROCK.

## Inbox drain — 10 of 10, every sender (census before top-level 3 · WALTER/ 7; after 0 · 0)
Logged in `AGENTS/BROCK/board_log.tsv` per BOARD_CONSUMPTION_SPEC v0.2; `git mv` to `processed/`.
| Item | Disposition |
|---|---|
| DEWEY 10/25 CFG vintage | info-only |
| VULCAN 10/26 Nebius facility | acted (already KB-BRK-402 on 10/28; file had not been moved) |
| VULCAN 10/26 three financings | deferred — asks stay on STATUS AI-infra row; out of L827 scope |
| SIG-W-20261029-017 / -024 | info-only |
| SIG-W-20261029-025 / -026 / -051 | noted |
| SIG-W-20261029-029 (K-12 vendors, BROCK ACTION) | acted — 0 hits in the six-BDC panel SOIs (KB-BRK-408); CLOs unchecked |
| SIG-W-20261029-054 (Blue Owl / Arini) | acted — OWL 8-K primary: Credit FPAUM $97.0B flat y/y, direct-lending redemptions named, wealth raise $1.9B vs $11.4B LTM, no redemption $ figure (KB-BRK-407) |

## Controls
`brock_selfcheck.py` RC 0 CLEAN (after fixing two findings it raised on my own STATUS edits) · corrections_boot_check 0 OK · STATUS 22,775 B = 69.97% of budget (`read_cap_check.py`) after verbatim rotation to `catchups/2026-10-29.md` · `pull` not run (dirty tree of other desks; 0/0 vs origin after `git fetch`). Skipped: market dashboard boot step 4 (only HTGC price needed; taken live), LESSONS read (boot step 2) and PREDICTIONS overdue scan (boot step 3) — bounded wake, named here as SKIPPED.

## COMPLETION — BROCK — 2026-10-29
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK/{STATUS.md, SCRATCH.md, board_log.tsv, workbook/KB.tsv, workbook/PREDICTIONS.tsv, docket/CATALYSTS.tsv, catchups/2026-10-29.md, catchups/INDEX.md, research/2026-10-29_htgc-q3/*, inbox→processed ×10}, AGENTS/TERRY/inbox/2026-10-29_from-BROCK_HTGC-Q3-falsifier-fired.md, this memo
RESULT: L827 graded on primary: THESIS FAILS FOR Q3 — software 0.981 label / 0.976 constant perimeter, NA 0.4% cost, NAV $12.26; HTGC relabelled $251M of software (basis break, verdict unaffected). Experiment A HTGC cells delivered (event 3 of 3). BRK-10 RESOLVED-FALSE (forced by the NAV cell); no score/threshold/gate moved (58/70). Drain 10/10.
GAPS: Call transcript not read; K-12 CLO exposure unchecked; BRK-16 not separately measurable; boot steps 2–4 skipped (bounded wake).
WILL_NEEDS: None.
FOLLOW-UP: PROME writes the L827 state line above and the L833 assessment; TERRY consumes the packet.
