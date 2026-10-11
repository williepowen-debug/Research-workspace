# FHLB research hub (REGINALD)

*Built 2026-10-10 (Sat ~20:3x ET) on Will's direction: "consolidate it all into one centralized area. Even if we just copy the data/files over there." Owner: REGINALD. **Re-check this map at any append, or on 2026-11-07 (the Q3 Call Report run), whichever is first.***

**Start here.** Everything the fleet has on the Federal Home Loan Banks (FHLBs) is either IN this folder or listed below with its path. Two kinds of file live here:

- **Canonical (edit here):** `reports/`, `verification/`, `data/KEY_PRIMARY_TABLES.md`, `sources/SOURCES.md`, this README.
- **Copies (never edit here):** `copies/` and `data/DESK_ROWS_SNAPSHOT_2026-10-10.md`. Each copy opens with a 2-line banner naming its source path, commit and crc32; `copies/MANIFEST.tsv` lists all 25. Their figures are as of each source's own date. To refresh a copy, re-copy the source; to fix a figure, fix the SOURCE.

## The questions

| # | Question | Where it stands (2026-10-10; re-check) | Read |
|---|---|---|---|
| Q1 | **Is FHLB borrowing a sign of regional-bank stress?** (`REG-T-06`: advances >$700B ×3 quarters = "EARLY-CRISIS") | **No, as currently measured.** The H1-2026 rise (+$136.2B) was commercial banks (+$121.4B), about half of it four very large banks; credit unions and savings institutions shrank (−$13.7B); 106 mid/small SEC filers +$2.3B. Q3 likely FELL (nowcast ≈ $770B). As lettered the alarm fires ~10/29 anyway → **WQ-414 (Will, due 10/24).** | `reports/…_Q2_composition…` · `reports/…_Q3_nowcast…` · `verification/…` §Key primary figure |
| Q2 | **What is inside the total?** | By borrower type at 6/30/26: commercial banks 56.4% · insurers 24.9% · credit unions 9.1% · savings institutions 8.2%. Insurer dollars are a record ($202.8B) but their share fell from 27.0% at Q1. | `verification/…` · `data/KEY_PRIMARY_TABLES.md` |
| Q3 | **The insurer channel (Athene, Delaware Life) and its bank links** | Real, owned by **SHADE** (insurers) / **BROCK** (private credit). Losses in an insurer failure land mainly on policyholders and guaranty funds; the FHLB's protection there rests on **state** law and holding the collateral, not the federal §10(e) lien. Bank links are small and named: Citizens $450M revolver to Delaware Life (status after YE2025 unknown) · Truist and Fifth Third paused Delaware Life sales · WAL = 13% of FHLB San Francisco's book (YE2025). | `verification/…` ledgers B and C · `data/KEY_PRIMARY_TABLES.md` |
| Q4 | **Is the 2023 lifeline tighter for a weak bank?** | **Unknown (inference only).** FHFA AB 2024-03 (active) tells FHLBanks to lend on the member's condition, not just collateral; the FHLBanks' own Council calls it "procyclical". **No public evidence** of an actual pullback; FHFA-OIG calls member credit risk "abated" for FY2026. | `verification/…` ledger C (R1–R3) |
| Q5 | **Where did September's small-bank borrowing come from?** | Small banks' borrowings +$32.9B in 3 weeks to 9/30 (H.8), but FHLB system debt rose only +$6.2B in September ⇒ mostly NOT FHLB, or FHLB-funded from its own liquidity. Open. | `reports/…_Q3_nowcast…` §4 · STATUS H.8 row |

## Folder map

| Path | What |
|---|---|
| `reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md` | **Canonical.** Who borrowed in H1 (district XBRL, named members, borrower-side breadth), the 2020–26 base rate of the >$700B letter. *Moved here 2026-10-10; a forwarding stub sits at the old `AGENTS/REGINALD/reports/` path.* |
| `reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md` | **Canonical.** Q3 advances nowcast from Office of Finance debt (≈ $770B, ±2 sd $728–813B), H.8 vs FHLB gap. *Moved; stub at old path.* |
| `verification/2026-10-10_external_report_verification.md` | Claim-by-claim check of Will's external draft: bottom line + three ledgers (EDGAR, Delaware Life, regulatory/system). |
| `data/KEY_PRIMARY_TABLES.md` | District top-borrower tables (Des Moines, Indianapolis, San Francisco, Chicago), Athene and Delaware Life borrowing room. |
| `data/DESK_ROWS_SNAPSHOT_2026-10-10.md` | COPY: every FHLB row in THRESHOLDS · VX · KB · FLOW · PREDICTIONS · registry NOTES, verbatim, with re-extract commands. |
| `sources/SOURCES.md` | Every primary document: URL or SEC accession, date, local file. |
| `sources/*.pdf` | 17 PDFs (Office of Finance CFRs, GAO, FHFA, FHFA-OIG, Council letter, Iowa code). **Local-only (gitignored here)**; re-download on another machine from SOURCES.md. |
| `sources/FHLB_Risk_Research_Report_Reconciled.docx` (+ `_TEXT.md`) | Will's external draft. **A lead list, not a source** (see verification). |
| `copies/REGINALD/` | 14 copies of desk material: Feb-2026 haircut research and monitoring design, Feb readings, CFG Q1 "FHLB flipped", the frozen FHLB-dependency scoring proposal, the PNC/Pittsburgh attribution (8/23), the WQ-318 per-bank funding baseline + script, BOND's two FHLB packets, my WQ-414 packets to PROME, my 10/10 signal + amendment. |
| `copies/fleet/` | 11 copies from other desks: OTTO (WAL FHLB & liquidity) · OZK (pledged loans) · SHADE (Athene funding mix; BROCK→SHADE Delaware Life packet) · BROCK→HAWK (5/1) · BOND (rotated catalyst rows) · FORGE (PE-insurer cascade, frozen corpus; T-bill/repo) · RED (KRE bull case) · WAL (stale earnings prep) · CORAL (Seacoast funding). |
| `copies/MANIFEST.tsv` | Source path, commit, crc32, bytes and a one-line note per copy. |

## Live surfaces that stay where they are (tools and boot checks read them there)

| Surface | Holds |
|---|---|
| `STATUS.md` §THRESHOLD STATUS: FHLB row, small-bank borrowings row | **the live level** (one source of truth; never restate it here) |
| `registry/THRESHOLDS.tsv` `REG-T-06`, `REG-T-08` · `registry/NOTES.md` | the alarm letters |
| `workbook/VX.tsv` `VX-REG-7.01` (live) · `7.02` / `7.03` (**STALE since 2026-02**) | tracking vectors |
| `workbook/KB.tsv` (17 FHLB rows, ML-REG-009 … 186) | knowledge base |
| `CALENDAR.md` (~10/29 Q3 figure row; weekly funding row) · `ROADMAP.md` (`REG-T-06` thread) | dates and threads |

## Next dates

| Date | What |
|---|---|
| Thu 10/15 · Fri 10/16 | Fed H.4.1 (discount window) · H.8 (small-bank borrowings, week of 10/7): Q5 |
| **Sat 10/24** | **WQ-414 due: Will re-letters `REG-T-06` or not** |
| ~Thu 10/29 (estimate) | Office of Finance Q3 combined advances; grade against the ≈ $770B nowcast (a miss >$40B ⇒ check FHLBank liquidity drawdown) |
| early–mid Nov | FHLBank Q3 10-Qs (top-borrower tables); Athene Q3 10-Q; OF monthly debt file for October |
| 2026-11-05 · 11-07 | FFIEC token expiry (Will) · Q3 Call Report run (per-bank FHLB advances) |

## Known bad figures in older material (do not cite)

- **"FHLB at $480B" (Feb–Apr 2026)**, in `copies/fleet/RED__KRE_BULL_CASE.md` (Pillar 10) and this desk's April WALTER liaison notes. The Office of Finance shows **$694.0B at 3/31/25 and $676.7B at 12/31/25**. The $480B basis is unknown. RED owns its file.
- **The external draft's** San Francisco JPMorgan >10% claim (that was YE2024), "$14.7B credit unions" (matches MBS investments), the Council of FHLBanks quote (fabricated), "Indianapolis most insurer-heavy" (Des Moines is), insurer membership 7.7% (9.7–9.9%), commercial-bank share ~48% (56.4%). Detail → `verification/`.
- `VX-REG-7.02` haircuts and `7.03` pledging: STALE since 2026-02; haircut schedules are not public.

## Not copied: incidental mentions

On 2026-10-10, **138 files in this desk** and **340 elsewhere in the fleet** (excluding `AGENTS/_archive/`) mention the FHLB. Most are one-line references inside bank notes, status rotations or routing logs; they were indexed by command, not copied. List them with (from the repo root):

```
grep -rli 'FHLB\|Federal Home Loan' --include=*.md --include=*.tsv --include=*.py AGENTS PROME FORGE | grep -v 'AGENTS/REGINALD/research/FHLB/'
```

Copy any of them in on request; add a row to `copies/MANIFEST.tsv` with the same banner format.

## Who owns what next door

SHADE: insurer lenders (Athene, Delaware Life; `T-SHADE-01`) · BROCK: private credit and the APO Dec-18 $95P vehicle question · LIQUID: funding plumbing (SOFR−IORB, discount window) · BOND: the curve; its FHLB vectors were shelved 8/18 · WAL / OZK / FLG desks: each bank's own FHLB use.
