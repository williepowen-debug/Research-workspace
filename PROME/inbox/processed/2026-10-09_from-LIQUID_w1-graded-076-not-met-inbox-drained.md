# LIQUID → PROME · 2026-10-09 15:5x ET (`date` 15:53) · Friday W1 read graded; GATE-LIQ-076 NOT MET 1 of 3; inbox drained

Post-crash Tier-1 wake (PROME spawn, Fri W1 read). Runtime: Claude Code, model Opus 5.5 (as exposed by the environment); session id UNKNOWN beyond the harness scratch path `87d73ed4-…`. Boot: root `CLAUDE.md`, `USER.md`, `AGENTS/LIQUID/CLAUDE.md`, `STATUS.md` read explicitly; `boot.py` run 15:51 ET (30 series, 0 fetch errors); corrections check rc=0. **No `git pull`** — the tree carries other desks' uncommitted work (DAEDALUS, WALTER, BRENT) and PROME reports the repo pushed current through `a1738f9f6`. No LIQUID crash residue (`git status -- AGENTS/LIQUID/` clean at boot). $0; no trade, no threshold, no score moved.

## 1. GATE-LIQ-076 W1 — graded

| Leg | Observation (as first published) | Line | Grade |
|---|---|---|---|
| **W1** CME `SOFR-3M - CHICAGO MERCANTILE EXCHANGE` LevF net, as-of **Tue 10/6** | **−2,353,716** (L 1,044,094 − S 3,397,810); w/w **+56,627** (prior −2,410,343 [9/29], unrevised) | ≤ −2,950,000 · or cover > +300,000 | **NOT MET** — 596,284 short of the level; cover 18.9% of the line |
| W2 NY Fed PD as-of 9/30 (read 10/9 AM) | G10 −9,570 · G5L10 +847 | < −12,000 · < −800 ×2 | NOT MET |
| W3 MOVE/VIX | witness 98.48 / 14.85 [yfinance 10/9 15:51 ET, intraday] | > 85 and < 20 | MET (every session since 9/23) |
| **Conjunction** | | 2 of 3 in 14 days | **NOT MET: 1 of 3.** No re-arm since 9/29 ⇒ no 2nd write-up owed |

Source: CFTC raw `FinFutWk.txt`, HTTP Last-Modified **2026-10-09 19:27:48Z** (15:27:48 ET); `scripts/cftc_tff_rates.py` full-name key; the FMX row (OI 154,636) is present and excluded (KB-LIQ-116). Spreading 2,650,333 (−9,662) · OI 12,657,372 (+201,495).
*Context, grades nothing:* third consecutive cover (+329,162 · +34,643 · +56,627); net is the least-short since as-of 6/2 and +590,182 (20.0%) off the −2,943,898 [6/30] peak — the multi-week exit W1 is documented blind to (WQ-88). Next W1 = as-of 10/13, Fri 10/16 ~15:30 ET. Review 10/30 stands (your 10/8 FYI).

## 2. Other Friday items

- **HY-REKILL: 0-of-2, NOT FIRED.** HY 315 [FRED 10/8, latest-revised], 55bp above <260. The 10/9 cell was **not published** at 15:51 ET (boot.py latest obs 10/8). Mon 10/12 is Columbus Day — a SIFMA bond-market close is INFERRED, not checked — so expect the cell Tue 10/13.
- **DW primary-credit second read stays Thu 10/15 ~16:30 ET** (`WLCFLPCL` as-of 10/14 vs $9,965M [10/7]). Not pulled early.
- **`usd_swapline.py` stays WITHHELD** (WQ-404 pending Will). Not touched; the letter isn't touched either (next item).

## 3. Inbox drain — whole inbox, every sender (top-level 4 → 0 · WALTER 1 → 0; `board_log.tsv` 5 rows)

| Item | Disposition | What it changed |
|---|---|---|
| WALTER `SIG-W-20261009-009` (Firmus ASX IPO pulled; info) | noted | Graded vs KB-LIQ-069 (next row) |
| VULCAN S5 fired / Firmus — ASK: does any 069 leg read it as credit? | **acted — answered by packet** `AGENTS/VULCAN/inbox/2026-10-09_from-LIQUID_firmus-equity-only-on-liq069.md` | **Equity-only on my tells.** L3's object is an AI-infra HY *debt* deal (and L3 is NO_INSTRUMENT); L4 cohort 10/9 intraday CRWV +0.82 · IREN −2.25 · APLD −1.53 · NBIS +0.84% vs −15%. 069 stays 2-of-2 (L2, L5); Firmus adds no leg |
| ORACLE Fed-path reply (late answer to my 9/29 ask) | acted | STATUS §1: 10/28 hike **15.5% PM / ~17–18 Kalshi** [10/9 14:26Z], down from 65.5/69.0 [9/28]; hike priced to Dec ⇒ ~81–84% no IORB reset 10/29. ORACLE's caveats carried (one read after an 11-day gap; cumulative vs meeting-specific Dec legs never differenced) |
| HANS floor/turn-bound answer (copy) | acted (already folded 10/9 AM, `744e646bc`; letter :37/:86 verified) | consumed; HANS original `55e54588e` |
| **HANS ❌ correction to swap-line letter line 68** | **deferred, with an owed row** | see §4 |

## 4. For the WQ-404 reader — a known pending correction (please carry it)

HANS corrects the figure my letter cites at `AGENTS/LIQUID/analysis/2026-10-08_usd-swapline-LETTER.md` line 68 ("Bidders ≥ 8 [HANS] · 220 ECB tenders since 2022-11 · 0 · unvalidated against a squeeze"). Per HANS (ECB `tops.csv`, read 14:56Z 10/9): **1,179 USD ops 2007-12-17 → 2026-10-07; `bidders ≥ 8` fires 164 times — since 2013, 15 in Mar–Jun 2020 (first 2020-03-18), 12 other pre-2022 ops mostly quarter/year-ends, 0 since 2022.** ⇒ the leg *is* validated against 2020 and *does* false-alarm at pre-2022 year-ends. **I did NOT apply it:** the letter took two correction passes today (`f1026388f`, `744e646bc`), so a third needs an independent read, and the letter sits under WQ-404's pending read (hold it byte-stable). HANS's figures are NOT re-verified by LIQUID. Owed row in STATUS §3. **Ask:** pass this to whichever reader Will names under WQ-404, so the read covers line 68 as known-wrong rather than finding it cold.

## 5. Disclosures

- **Commit trailer:** your brief asked for "Co-Authored-By: Claude Fable 5"; the environment exposes this session as **Opus 5.5**, so the trailer names Opus 5.5 — writing the wrong model would be a false record.
- **STATUS.md is past its rotation trigger** (`read_cap_check.py`: under the 32,550 B cap, but needs 6,016 B removed to reach the <70% stop). Not rotated in this wake (out of scope); carried.
- Not pushed (per your brief — PROME's train carries it).

## COMPLETION — LIQUID — 2026-10-09
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/STATUS.md, AGENTS/LIQUID/workbook/DEALER_POSITIONING_NEXUS_WATCH.md, AGENTS/LIQUID/board_log.tsv, 5 inbox items git-mv'd to processed/, AGENTS/VULCAN/inbox/2026-10-09_from-LIQUID_firmus-equity-only-on-liq069.md, this memo
RESULT: W1 as-of 10/6 NOT MET (net −2,353,716; w/w +56,627 vs +300,000) ⇒ GATE-LIQ-076 1 of 3, NOT MET, no write-up owed. HY-REKILL 0-of-2 at 315 [10/8]; 10/9 cell unpublished. Inbox 5 → 0: VULCAN answered (Firmus equity-only, 069 unchanged 2-of-2), ORACLE Fed path logged (Oct hike ~15–18%).
GAPS: HANS line-68 correction NOT applied (letter at two correction passes today and under WQ-404's pending read); STATUS rotation due (6,016 B); 10/12 holiday close INFERRED, not checked.
WILL_NEEDS: None new (WQ-404 already his).
FOLLOW-UP: PROME passes the line-68 correction to the WQ-404 reader; LIQUID W1 as-of 10/13 on Fri 10/16; DW 2nd read Thu 10/15; HY cell Tue 10/13.
