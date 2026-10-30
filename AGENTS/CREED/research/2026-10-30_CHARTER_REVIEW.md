# CREED charter review — 2026-10-30 (Will: "look at instruction file … anything old, superseded, redundant, duplicated")

**File:** `AGENTS/CREED/CLAUDE.md`, 40,535 B = 124.5% of the 32,550 B read budget (DAEDALUS item 8). **✅ EXECUTED 2026-10-30 evening (Will-ruled, all three choices yes, with conditions): 40,535 → 25,448 B; line map at `archive/CHARTER_HISTORY_2026-10-30.md`.** Findings below as written before the edit.
**Constraint found:** `PROME/registry/READS.tsv:401-405` and the read-cap manifest cite boot steps by number (`CREED:6.3`…`6.7`, `closeout-6`, `closeout-8b`). **A cleanup must keep step numbers stable** (or PROME re-points them in the same change).

## A. Wrong today (fix regardless of any slimming)

| # | Line | What it says | Truth |
|---|---|---|---|
| A1 | 16 Mission "Own" | "multifamily stress outside Florida-specific CORAL scope" | MF **scoring** is HOMER's since 7/27; CREED keeps the MF data pull (opportunistic) and, since Will 10/28, **named MF cases** in `cases/` |
| A2 | Mission | no mention of the **case ledger** (`cases/`, Will-directed 9/29) — a standing CREED function | missing |
| A3 | 74 trap #8 | "`creed_selfcheck` is blind to this by construction — check 1 is file-level" | false since today's fix (line-scoped); the *unit* blindness it means is still true for non-trigger prose |
| A4 | 92 boot 4c | "Live finding: T-06 and T-06b carry numeric bands with NO metric vector … never counted" | resolved: T-06b → `VX-5.03` (counted, n=2/12), T-06 → `VX-5.01 [QUALITATIVE-VALUE]` |
| A5 | 54 Route Matrix | "CREED reports inbox dispositions; PROME `git mv`s" | CREED files its own processed items (10/28, 10/30) |
| A6 | 111 Workbook | LEDGER_GLOB = "`workbook/*.tsv registry/*.tsv`" | file also carries `cases/*.tsv` |
| A7 | 50 Route Matrix | pension route "(PROME to reflect)" | done: `AGENTS/_NETWORK.md:97-98` |
| A8 | 136 S5 block | "CREED's own MF-row citation is itself SECONDARY (… via Connect CRE)" | Trepp is PRIMARY-READ since 8/20 (the argument's premise ② no longer holds; the kill decision stands) |
| A9 | 60 traps preamble | "Full versions stay in `SCRATCH.md`" | inverted: SCRATCH's copies are the short ones and say *"THAT copy [CLAUDE.md] is the one that matters"* |
| A10 | 180 | lists a deleted file (`inbox/2026-02-24_signals.md`, removed 6/28) | dead reference |
| A11 | 198 | "the June 2026 source packs are trail" | the packs are June and July |

## B. Duplicated (same rule in 2–3 places inside this file, or verbatim elsewhere)

| # | Where | Duplicate of |
|---|---|---|
| B1 | §Current Rails (202-214) | boot step 6 sub-list (94-101) — same five files, same on-demand note, said twice |
| B2 | §Working Hypothesis (218-227) | `thesis/THESIS.md` §Current State Classification, row text verbatim |
| B3 | Archive move history (93, 169, 233) | three copies of "REGINALD moved it 8/13, `a7bae0d06`, refs not updated until 10/22" |
| B4 | S8a recompute rule (100, 209) | twice, plus the REIT-module history twice |
| B5 | S5/HOMER ownership (26, 46, 130, 132-140) | four places; the standing rule is one sentence |
| B6 | Git pathspec rule (163, 237) + "do not execute trades" (33, 236) | each twice here, and in root CLAUDE.md |
| B7 | §Current Stale-State Warning (187-198) + line 5 | the Feb-2026 legacy-data warning, twice |
| B8 | Canonical-truth ordering (126) | also README, SCRATCH, STATUS — keep here (rule home), fine |

## C. History inside rules (the root "Rules only" model says reasons live elsewhere)

~14 KB of the file is dated narrative: who found what, which session, what the line said before. Largest blocks:
- **S5 courier-kill block** (132-140, ~2.6 KB) — an 8/13 decision record; the live rule is one line.
- **Boot 4c blockquotes** (87-92, ~2.3 KB) — why the scan was built, fixture history, the stale A4 finding. Live rules: run it; TRIPPED = go grade; LEG k/n meaning; read the unscannable register; DUE ≠ fire.
- **Closeout 8b blockquotes** (159-161, ~1.3 KB) — why the self-check exists.
- **Trap #5** (~2.4 KB) — the $160B MF-wall retirement story; the rules are four lines.
- **Trap #7** instances ①–③ (~1.6 KB) and **trap #3** dated widenings (~1.3 KB).
- **Trap preamble** promotion history (~1 KB); 🆕 markers from August on traps 6–8 and step 4c.
- Parenthetical "(changed/re-pointed/added on <date> because …)" on boot steps 0, 4, 6.1, 6.2, 7, 7b and closeout 2, 3, 8, 8c; CARL feed line 26.

## D. Judgment calls for Will (not just tidying)

1. **Three boot reads that look done:** `research/INBOX_TRIAGE_2026-06-21.md` (a June inbox, triaged and promoted into THESIS), `archive/LEGACY_PULL_FORWARD_2026-06-21.md` (legacy mechanisms) and `thesis/CHANGELOG.md` are read whole every boot (READS rows 402-405). Demoting them to on-demand saves boot reading, the way the REFRESH pack was demoted 9/30. Needs PROME to update READS rows.
2. **Trap #2's example** carries ARI's $2.2B / BVPS $12.05 (4/24) — ARI is now liquidating (delist 11/6). The principle stays; the example could become dated history.
3. **Where the moved history goes:** proposal = verbatim, crc-stamped, to `archive/CHARTER_HISTORY_2026-10-30.md` (same method as today's rotations), and the reasons index in `MAINTENANCE.md`.

## Estimate
Fix A + remove B duplicates + move C history verbatim → roughly **22–25 KB (68–77% of budget)**, with every rule, trap and step number kept. Traps stay always-loaded, compressed to rule + one-line instance.
