# LIQUID -> PROME: CoreWeave 5Y from the 11/27 DTCC full file, and the H.4.1 as-of 11/25 (D:L1302 evening part)

**Written:** 2026-11-27 20:35 ET (`date`). LIQUID ran on Claude Code, model Opus 5.5 (claude-opus-5-5), spawned by PROME prome-80 (context c369a3d5) on the laptop. Runtime gaps: SendMessage is a deferred tool and is tried at the end.
**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages (the harness also injected it), `AGENTS.md` 1, `USER.md` 3, `AGENTS/LIQUID/CLAUDE.md` 4, `AGENTS/LIQUID/STATUS.md` 4. **SKIPPED:** spawn step 0, `git pull --rebase`. The tree carried another desk's uncommitted PROME files at start, so under the spawn rules I did not pull. `boot.py --quick` ran and found nothing new: its 11/26 credit row is the holiday carry.

## 0. In plain words

The full-day DTCC swap file for Friday 11/27 is out (read 20:26 ET). **No CoreWeave credit-default-swap trade of any maturity was done on 11/27, and none on 11/26.** So there is still no fresh 5-year price for TERRY's card. Re-reading all the files from 11/20 on, I found that my grader missed some CoreWeave rows: they are labelled only by a bond code, not by name. Two of the three trades behind my "1,359 at the 11/24 close" have since been cancelled as errors. **The last valid 5-year price is 1,371 bp (1,326 clean), traded at 16:07 ET on Monday 11/24.** That is 12 bp higher than I reported. It is still well above the card's 1,200 bp line, and it is still three sessions old for a Monday 11/30 entry. The Fed's weekly balance sheet (as of Wednesday 11/25) shows no funding strain. The emergency repo facility, foreign official repo and other credit are all essentially zero, and discount-window borrowing is flat at $8.9B. Foreign official custody holdings of Treasuries were flat, so there is still no sign that Japan sold Treasuries to fund intervention. Bank reserves fell $73B on the Wednesday to $2.93T. That was mostly the Treasury's cash account and holiday currency demand, and reserves are still $129B above the $2.8T line. **Nothing here changes my assessment.** GATE-LIQ-079 is not armed. One small new item: secondary credit, the Fed lending window for banks that do not qualify for primary credit, showed $50M on Wednesday, up from zero. It is tiny, and it is REGINALD's to watch.

## 1. Task 1: CoreWeave 5-year CDS (WQ-745)

**WQ-745 one-liner:** latest valid CoreWeave 5Y (Dec-2031) **1,371 dirty / 1,326 clean, traded 11/24 at 16:07 ET ($2M)**; for an 11/30 entry it is **three sessions old by my count (11/25, 11/27, 11/30)**; **above** the card's 1,200 bp line (+171 dirty, +126 clean). TERRY counts sessions and owns the card. Packet: `AGENTS/TERRY/inbox/2026-11-27_from-LIQUID_crwv-5y-1127-full-file.md`.

| File (DTCC PPD SEC cumulative credits) | Rows | CoreWeave rows executed that day | Valid 5Y Dec-2031 executed that day | Note |
|---|---|---|---|---|
| 11/27, read 20:26 ET (HTTP 200, 54,869 B; byte-identical at 20:31 and 20:35 ET, §5) | **755** (events to 22:21:52Z = 17:21 ET) | **0** | **none** | Three CoreWeave rows, all about 11/24 trades (below) |
| 11/26 (holiday) | 453 | 0 | none | |
| 11/25 | 2,102 | 4Y ×2, 5Y odd lot (EROR), 2Y (EROR) | **none** | 4Y Dec-2030 1,429 / 1,379 (13:20Z) and 1,415 / 1,366 (17:22Z, nonstandard flag blank): **not the card's instrument** |
| 11/24 | 1,225 | 5Y, 4Y, Jun-2031, 3Y | yes | below |

**11/24 Dec-2031 5Y prints, with cancels matched by Original Dissemination Identifier across the 11/24, 11/25 and 11/27 files** (dirty / clean, `crwv_cds_grade.py` conversion):

| Exec (ET) | ID | Notional | Level | State now |
|---|---|---|---|---|
| 10:10 | 6524799176 | $0.5M | 1,309 / 1,267 | live (odd lot) |
| 10:23 | 6525032503 | $2M | 1,359 / 1,314 | live (nonstandard-term flag blank) |
| 15:12 | 6529626509 | $3M | 1,359 / 1,314 | **EROR** 6549685864 (11/25 file) |
| 16:01 | 6551078065 (11/25 file) | $3M | 1,359 / 1,314 | **EROR** 6600557547 (11/27 file) |
| 16:07 | 6530428445 → CORR 6530495066 | $2M | **1,371 / 1,326** | live (named only by ISIN US21873SAC26) |
| 16:07 | 6530626814 → EROR 6600891984, re-report 6600891988 (11/27 file) | $2M | 1,371 / 1,326 | live as re-reported |

- **Nonstandard tenors (not the card's instrument):** Jun-2031 1,269 / 1,226 (exec 16:49 ET 11/24, reported 11/25); the 15:30Z Jun-2031 1,330 / 1,286 was EROR'd and re-reported. 4Y Dec-2030 on 11/24: 1,259 to 1,284 dirty.
- **Defect found (KB-LIQ-168):** `crwv_cds_grade.py` matches by name only and applies cancels file by file. It missed the ISIN-named 16:07 ET prints and the later-file EROR rows, which is how 1,359 came to stand as "the 11/24 close". Tonight's read used `AGENTS/LIQUID/research/2026-11-27_crwv-5y-1127-file/crwv_xfile.py`, which keeps the grader's conversion but matches by name, by RED 239FAV* or by ISIN US21873S*, and applies cancels across all the files. The grader fix is owed (STATUS §3). Because the grader is a GATE-LIQ-069 L2 input, the fix owes an independent read. GATE-LIQ-069 L2 stays FIRED; this is a fact update, not a re-grade.
- ⚠️ The conversion is a flat-hazard approximation (4% flat rate, 40% recovery), not the ISDA model. The dirty column is the headline (KB-LIQ-163).

## 2. Task 2: H.4.1 as-of Wed 11/25 (released Fri 11/27; `federalreserve.gov/releases/h41/20261127/` HTTP 200 at 20:28 ET; the `/20261125/` path 404)

Figures are in $ millions. The comparison is the 11/19 release (as-of 11/18). Week averages and Wednesday levels are shown separately.

| Leg | Week avg 11/25 | Chg vs wk 11/18 | Wed 11/25 | Wed 11/18 |
|---|---|---|---|---|
| Reserve balances | 2,963,667 | −15,989 | **2,928,659** | 3,001,790 (−73,131) |
| ON RRP "Others" | 366 | +68 | 300 | 331 |
| Foreign official RRP pool | 319,666 | −4,458 | 326,828 | 316,712 (+10,116) |
| Repo, "Others" (SRF) | 1 | −14 | 0 | 0 |
| Repo, foreign official (FIMA) | 3 | +3 | 1 | 1 |
| Primary credit | 8,810 | −556 | 8,886 | 9,055 |
| Secondary credit | 11 | +11 | **50** | 0 |
| Other credit extensions | 0 | 0 | 0 | 0 |
| Central bank liquidity swaps | 145 | −1 | 145 | 146 |
| TGA | 902,038 | −14,575 | 923,563 | 892,310 (+31,253) |
| Custody, marketable Treasuries | 2,539,928 | +2,555 | 2,543,541 | 2,544,011 (−470) |
| Custody, total | 2,808,325 | +1,712 | 2,811,444 | 2,813,231 |

- **Wednesday reserve fall, −$73.1B:** Reserve Bank credit −$9.6B (securities −$8.0B). Absorbing factors +$63.6B: TGA +$31.3B, currency +$14.6B (the pre-Thanksgiving draw), foreign RRP pool +$10.1B, other deposits +$4.4B. This is a calendar and Treasury-cash move, not a funding signal. Reserves are above the $2.8T line by $129B on the Wednesday basis and $164B on the average.
- **Japan-intervention legs:** no Treasury sale and no FIMA borrowing visible. Custody is all foreign official accounts, not Japan alone (BOND owns custody; SAM owns the yen call). The MOF monthly total (about 11/30) remains the direct read.
- **What it changes:** nothing in my assessment. Financing constraint NOT SHOWN; GATE-LIQ-079 NOT ARMED (SOFR99−IORB +13 [11/25]; the gate is SOFR-keyed, and H.4.1 does not grade it). Secondary credit of $50M is too small to matter on its own. I logged it in STATUS §1 only. It is information for REGINALD, which owns individual banks, and PROME routes it if wanted.

## 3. Inbox (census before: top-level 1, WALTER 9 → after: 0 and 0)

| Item | Disposition | Note |
|---|---|---|
| SIG-W-20261127-006, -013, -014 | info-only | cyber cluster; US data; no plumbing channel |
| -007 | noted | item 8 SOFR−IORB +5 matches §1 |
| -008 | acted | TERRY's fresh CoreWeave 5Y is answered by §1. The "CCC past 1,200" basis is UNKNOWN, so FRED ICE CCC 1,417 [11/25] stands. Semafor (banks marketing AI loans via SRT) added to the KB-LIQ-153 combination row |
| -010 (correction COR-20261127-02) | acted, **APPLIED** | It touches my SoftBank line. Every DTCC SoftBank print is the **yen** contract. USD 5Y is 516 to 535 [11/26 relays]. My yen-curve "5Y INFERRED 560 to 600" is withdrawn as a USD read. The yen 5Y printed 562 / 555 at 05:30Z 11/26 (¥50M) |
| -012 | noted | CoreWeave notes 73.9 to 79.2, YTW about 17% [11/25, vendor] and $11.0B of 2027 principal added to KB-LIQ-153; no score moved |
| -015 (COR-03), -016 (COR-04) | info-only, **NO-OP** receipts | no LIQUID claim touched |
| PROME `gate069-since-independent-read-UNRESOLVED` | deferred, encoded in STATUS §3 | Repair findings 1 to 3 and decide 4 to 7 at the next session that may edit the script (12/02 at the latest). Not edited tonight. Until it is re-read, no grade rests on `--since` output alone |

`corrections_boot_check.py LIQUID` returns rc 0 after the three receipts.

## 4. Changed

`AGENTS/LIQUID/MEMORY.md` (session blocks) · `NEXUS_BRIEF.md` (CoreWeave and H.4.1 fold, its own commit) · `AGENTS/LIQUID/STATUS.md` (header; §1 CoreWeave, SoftBank, funding with H.4.1, Japan; §2 069 L2 fact; §3 the 069 owed row, the `--since` row, the Japan row and the grader-fix row; §6 KB range) · `workbook/KB.tsv` (KB-LIQ-168 new; KB-LIQ-153 combination members added 11/27) · `board_log.tsv` (10 rows) · `registry/corrections_receipts.tsv` (3) · `research/2026-11-27_crwv-5y-1127-file/` (two scripts, OUTPUT.txt) · 10 inbox `git mv`s · TERRY packet.

## 5. GAPS

- The SoftBank 3.5Y Jun-2030 print of 11/25 recomputes tonight at 576 clean / 583 dirty, against 555 / 548 quoted at midday. The difference is unreconciled; it may be a capped-notional handling difference. It is not load-bearing for WQ-745.
- The `crwv_cds_grade.py` fix is not done tonight: it is a gate input and owes an independent read.
- No 11/27 FRED credit cells are posted yet (about 11/30), so no gate was graded, as briefed.
- DTCC retries: the 11/27 file was posted at the first check (20:25:51 ET), so the UNPOSTED branch never applied. It was byte-identical at 20:31 and 20:34:59 ET (HTTP 200, 54,869 B). A later restatement inside the file cannot be ruled out; the 11/30 read re-applies any later-file cancels.

## COMPLETION — LIQUID — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/STATUS.md, AGENTS/LIQUID/MEMORY.md, AGENTS/LIQUID/NEXUS_BRIEF.md (fold, second commit), AGENTS/LIQUID/workbook/KB.tsv, AGENTS/LIQUID/board_log.tsv, AGENTS/LIQUID/registry/corrections_receipts.tsv, AGENTS/LIQUID/research/2026-11-27_crwv-5y-1127-file/{crwv_xfile.py,softbank_rows.py,OUTPUT.txt}, 10 inbox git mvs, AGENTS/TERRY/inbox/2026-11-27_from-LIQUID_crwv-5y-1127-full-file.md, this memo
RESULT: DTCC 11/27 full file (755 rows) has 0 CoreWeave trades; latest valid 5Y revised to 1,371 dirty / 1,326 clean at 16:07 ET 11/24 (two $3M 1,359 prints errored; grader missed ISIN-named rows, KB-LIQ-168), 3 sessions old for 11/30, above 1,200. H.4.1 as-of 11/25: reserves Wed $2,928.7B (−$73.1B, TGA and currency), SRF/FIMA nil, primary credit $8.9B, custody Treasuries flat; assessment unchanged, 079 not armed. Inbox 10 → 0; 3 correction receipts.
GAPS: crwv_cds_grade.py fix owed (gate input, needs independent read); SoftBank 3.5Y 576 vs 555 unreconciled; 11/27 FRED cells not posted (no grades, as briefed); git pull skipped (other desk's dirty files at start).
WILL_NEEDS: None.
FOLLOW-UP: 12/02 wake: 069/076 reviews, gate069 `--since` repair (findings 1-3) and the crwv grader fix, each to an independent read; 11/30 DTCC slices/full file for a fresh CoreWeave 5Y; secondary credit $50M is information for REGINALD if PROME routes it.
