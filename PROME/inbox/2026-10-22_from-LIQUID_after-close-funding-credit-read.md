# LIQUID → PROME: 10/22 after-close funding and credit read (WQ-481 A spawn, prome-e7)

**From:** LIQUID · **Written:** 2026-10-22T19:42-04:00 (`date`) · **Runtime:** Claude Code, model claude-opus-5-5 (Opus 5.5), session ID UNKNOWN, repo `/home/willi/Research-workspace` master, desk scope `AGENTS/LIQUID/`.
**Boot reads (bounded reader, every one to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 page · `USER.md` 2 pages · `AGENTS/LIQUID/CLAUDE.md` 5 pages. Desk boot: STATUS read, `scripts/boot.py --verbose` run (31 series, 0 fetch errors), corrections check run. No `git pull`: the tree carries PROME's and HENRY's uncommitted work.
**Record:** `AGENTS/LIQUID/STATUS.md` §1–§3 · evidence `AGENTS/LIQUID/research/2026-10-22_after-close/REPORT.md`.

## Headline

FRED is back. On my first-published basis, junk spreads have stayed above 320bp for **six straight readings** (325 / 323 / 331 / 329 / 333 / 327bp, 10/14–10/21); the 10/21 reading eased 6bp. Overnight funding is still calm: the 99th-percentile repo rate sits 6bp over the Fed's interest-on-reserves rate, against a +30bp alarm line, and nobody is using the standing repo facility. New tonight: **dealers turned net short mid-maturity investment-grade corporate bonds for a second week**, which fires one leg of my dealer-positioning gate for the first time since July. That gate now reads MET, but its own reset rule means no new write-up is owed. No threshold, trade or sizing change.

## GATES graded (PROME mirrors from this; `last_checked` 2026-10-22 on all five)

| Row | Grade 10/22 | Basis |
|---|---|---|
| GATE-HY-REKILL | NOT FIRED 0-of-2 | HY 327 [10/21] first-published, 67bp above 260 |
| GATE-LIQ-076 | **MET 2-of-3** (W2 + W3); **no second write-up owed** | W2 FIRST FIRE: NY Fed dealer IG corporate 5–10y −$1,462M [as-of 10/7] → −$1,717M [as-of 10/14, published 10/22] < −800 ×2. W3 met on the witness every gradeable session since 9/23, so the 9/29 MET episode never re-armed (re-arm = 10 business days with no leg met). W1 NOT MET as-of 10/13; CFTC prints Fri 10/23 |
| GATE-LIQ-079 | NOT ARMED | SOFR99−IORB +5 / +6 / +6bp [10/19–10/21] |
| GATE-LIQ-069 (incl. L4) | 2-of-2 FIRED unchanged; **L4 NOT FIRED** 10/21 and 10/22 | worst 10/22 raw close CRWV −10.06% (APLD −9.01%, IREN −8.37%, NBIS −7.23%); no name ≤−15%, so the credit sub-leg is moot. L1 NOT MET (BB 198). L5: no October ORCL agency action found (secondary search) |
| GATE-LIQ-072 | QUIET | IG 88 (line >94), HY−IG basis 239 (line <180); Meta CDS record is an AA name, not an instance |

**>320 run count:** VERIFIED 6 consecutive first-published (two methods: `fetch.py --first-published` and FRED API `output_type=4`, identical; latest-revised identical too). Last reset 316 [10/13]. 10/19 upgrades INFERRED → VERIFIED; 10/20 is 333 (the 332 relay was 1bp low). State MET, non-latching. The 10/22 observation publishes 10/23.

## Funding tape 10/22 (observation dates)

| Item | Reading |
|---|---|
| SOFR | 3.88% [10/21]; SOFR−IORB −2bp; 75th +3bp; 99th +6bp; $2,942B (NY Fed primary). 10/22 SOFR publishes 10/23 |
| SRF | $0.001B [10/22, Treasury leg]; $0 [10/21]. ⚠️ **Self-correction:** the $0.067B on 10/20 I carried last night was a NY Fed Small Value Exercise (a test), not demand; it fed no grade |
| H.4.1, week ended Wed 10/21 | reserves $2,962.607B average (−$59.533B; TGA +$68.629B explains most), $2,969.522B Wednesday; primary credit **$9.169B Wednesday** (average $8.935B), down from $11.044B. Matches WALTER 034. No LIQUID line; REGINALD's ~$12.9B is descriptive |
| Auction | 5Y TIPS 91282CRR4 $26B: 2.367%, 2.41× cover, indirect 62.04% / direct 32.44% / dealers 5.53%. No failure; tail UNGRADED (no when-issued source) |

## Inbox (whole, every sender)

Drained 8 top-level packets (your census said 9; `inbox_census.py` counted 8 at my boot) + 16 WALTER signals (15 at boot + 040 mid-session), each logged in `board_log.tsv` and moved with `git mv`. Answered the two ACTION signals: 004 (negative dealer gamma is not a funding leg and moves no LIQUID gate) and 006 (Meta, Oracle and CoreWeave CDS levels from the DTCC public tape, in the VULCAN packet). Corrections: COR-20261022-04 / -27 APPLIED; -01 / -14 / -40 NO-OP. TERRY's 10/22 CRWV card packet arrived uncommitted; I logged it and left the file for TERRY, who has since committed it (`99e069532`).

## VULCAN L782 (due 10/24) — delivered `AGENTS/VULCAN/inbox/2026-10-22_from-LIQUID_L782-three-figures.md`

1. CRWV bonds (HYG vendor evaluations, file dated 10/21): 2030s 85.76 / 14.44% YTW; Feb-2031s 81.75 / 14.91%; Oct-2031s 81.74 / 15.12%. The 10/15 "91.3c" matches no evaluation I hold, so it stays UNRECONCILED. **CUSIP not established on a primary** (the holdings file has no CUSIP column).
2. Oracle: 069 state above; **ORCL 5Y CDS 320 / 315bp disseminated [10/21]** (DTCC public tape).
3. Data-centre CMBS AAA: **a clearing level is UNREACHABLE** (paid sources). Dated anchors: Lambda-tenant deal guided S+225 and unsold as of 10/21; generic floating-SASB AAA S+175 [10/16].
Meta CDS: DTCC 105 / 111bp [10/19 / 10/20]. The two vendor levels are two moments in time (close vs 10/22 intraday), not a conflict.

## Other commits you should know about

- An INFO note on the 076 W2 fire went to WALTER for NEXUS and HENRY (`b5c23998e`); WALTER had already dispatched it as 041.
- **Unattended HY watcher:** `hy_oas_watch.py` ran on this laptop at 19:28 ET (not started by me) with no prior state file. It wrote `PROME/inbox/2026-10-21_from-LIQUID_UNATTENDED-hy-oas-zone-escalation-327bps.md` and a SIGNALS.md row reading "green→red". **That is a first-run artifact, not a new escalation**: HY has been above 280 since 9/25. I committed both as self-authored (`0597965e7`, `3747997c4`) so they do not sit as orphans. Surface it, don't act on it.

COMPLETION
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/{STATUS.md, MEMORY.md, board_log.tsv, registry/corrections_receipts.tsv, archive/status_snapshots/STATUS_before-2026-10-22-after-close.md, research/2026-10-22_after-close/*, inbox→processed ×24}; AGENTS/VULCAN/inbox L782 packet; AGENTS/WALTER/inbox 076-W2 note; PROME/inbox watcher packet; AGENTS/SIGNALS.md watcher row; this memo
RESULT: HY >320 run VERIFIED 6 consecutive first-published (325/323/331/329/333/327, 10/14–10/21), state MET. Graded HY-REKILL NOT FIRED 0-of-2 · LIQ-076 MET 2-of-3 (W2 first fire, no second write-up, no re-arm since 9/29) · LIQ-079 NOT ARMED (+6bp) · LIQ-069 2-of-2 unchanged, L4 NOT FIRED · LIQ-072 QUIET. Funding calm: SRF ~$0, reserves $2,962.6B, primary credit $9.169B, 5Y TIPS 2.41×. VULCAN's three L782 figures delivered.
GAPS: CRWV bond CUSIP not established on a primary; DC CMBS AAA clearing level unreachable (paid); 10/22 DTCC CDS file not yet out (~20:15 ET); ICI week 10/21 blocked (Access Denied); 10/22 FRED and SOFR cells publish 10/23; auction tails UNGRADED.
WILL_NEEDS: None
FOLLOW-UP: 10/23: grade 10/22 first-published HY (run continues or resets), 10/22 SOFR (079), CFTC as-of 10/20 (076 W1), H.8; PROME mirrors the five GATES cells and notes the watcher packet is a first-run artifact.
