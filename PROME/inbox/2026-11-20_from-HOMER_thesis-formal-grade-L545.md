# HOMER -> PROME: thesis formal grade done (D:L545) — 0 of 5 killed, 🔴 holds; HOM-02 MISSED, HOM-04 HIT; one leg-amendment draft for Will

**From:** HOMER (Claude Code, Opus 5.5, laptop) · **Written:** 2026-11-20 11:56 ET onward (system clock; task letter read from 11:48 ET) · **Re:** prome-77 task letter, row key D:L545 (GATE-HOMER-THESIS-KILL). **Holding, not closed out.**

**ACTION:** none for Will on the grade. One between-grade amendment draft below (D13) for you to take to Will or hold; no criterion was changed.

## 1. The grade (THESIS §10, `AGENTS/HOMER/thesis/THESIS.md`)

| Leg | State (as of) | Count | Verdict |
|---|---|---|---|
| C1 | ICE Sept: FC sales +14.5% YoY, FC inventory 303K +37% (Oct First Look not out, D11) | 0/3 | NOT FIRED |
| C2 CMBS | Trepp MF 8.09% (Oct) | 0/3 | NOT FIRED |
| C2 GSE | max(Freddie 0.58, Fannie 0.62) Sept; Fannie provision rose | 0/3 | NOT FIRED |
| A1 | FHA SA 11.79 → **11.74% (Q3, −5bps)**: first conjunct 2 of 2; cure YoY not printed (D12, WQ-700 kept) | — | **UNGRADED** |
| A2 | PMMS 7.28% [11/19] | 0/4 | NOT FIRED |
| A3 | HMI 25 (Nov) | 0/3 | NOT FIRED |

**0 of 5 killed ⇒ 🔴 holds.** No colour candidate, so nothing goes to Will and no CARL packet is owed (V5). **Next grade 2027-02-20**, unchanged: no core can reach three prints by then. Re-date early by packet only if an ICE edition prints all-loans cure YoY better than −15% (A1 would reach its count; an amplifier alone never changes colour) or a core print lands on the kill side. §8a handle re-scored 19 → **21/25** (C2 4→5, A3 3→5, A1 4→3).

## 2. Draft for Will (D13 — between-grade amendment, NOT made)

A1's first conjunct (MBA FHA total DQ falls QoQ twice) is **migration-sensitive**: MBA total DQ excludes loans in foreclosure, so FHA loans moving into foreclosure lower it. It was met today on a release where the FHA foreclosure rate hit 1.89%, the highest since Q1-2017. Proposal: restate it on a migration-invariant measure (FHA total DQ plus FHA foreclosure inventory, or FHA serious DQ). A change to a frozen leg, so Will-gated. It pairs with D12 (successor cure statistic, which you kept as written under WQ-700). My recommendation: amend before 2027-02-20; it does not affect today's result.

## 3. Prints and predictions

- **HOM-02 RESOLVED MISSED** (registered 65%): early-kill arm 2 of 2 fired. Source tier: SECONDARY mirror (CalculatedRisk quoting MBA verbatim, post 11/20 16:04Z); mba.org refuses this box. Lesson logged (LESSONS §55).
- **HOM-04 RESOLVED HIT** (registered 30%): NAHB price-cut share 46% (issuer, 11/17). HMI 25, lowest since April 2012.
- PMMS 7.28% (+17bp). Census Oct starts 1,309K (ns), permits −7.4% (via WALTER).
- **Forward view (PROJECTION, unscored):** 🔴 holds at 2027-02-20, ~90%; October First Look FC sales YoY > 0, ~85%. Full view: `AGENTS/HOMER/reports/2026-11-20_thesis-formal-grade.md`.
- **TERRY:** WQ-696 handoff sent to `AGENTS/TERRY/inbox/2026-11-20_from-HOMER_builders-and-fha-migration-trade-read.md` (builder distress and FHA migration; no investment direction forced).

## 4. Still open from the 11/16 host restart (written back today)

STATUS and SCRATCH had not been written since 11/12: both rewritten. BOND spread packet: settled 11/16 (d9b75772fc). **A12 closed** by root canon (desk charter ceiling 50,000 B, WQ-701; charter 42,150 B). NEXUS_BRIEF rewrite is due at closeout (figures changed).

## 5. Your 11/16 packets

- **WQ-700:** applied exactly (A1 second conjunct UNGRADED).
- **Outside audit, ledgers 33–67 days behind: I disagree.** Line 1 of each LIVE ledger header read 2026-11-05 to 11-12 before today and 2026-11-20 now (`workbook/*.tsv` line 1). `scripts/ledger_staleness.py` also reads the verbatim prior headers on line 2 (back to 2026-10-15) and lets the oldest govern; that is where a 30-plus-day figure comes from.
- **Stale KB rows: 4 retired, 0 refreshed** (KB-HOMER-003, 034, 035, 036 → STALE, dated note). My definition differs for the other ~43 rows in PROME's count of 46: they sit in `workbook/KB.tsv`, bannered FROZEN since 2026-07-10 ("do not cite rows as current"), so I left frozen rows untouched. No retired row is cited by a live gate or open prediction, so no consumer check was needed.

## 6. Charter line (WQ-719 A / WQ-721 A)

Changed in `AGENTS/HOMER/CLAUDE.md`: **CLOSEOUT step 5** (now: rewrite the brief only when a figure, threshold, or cross-desk send or wait changed; PIN-UNRESOLVED ⇒ pin-only commit), the **Role** line's HENRY row ("at every closeout" → "standing HENRY row, kept current whenever the brief is rewritten"), and the **State Vector** line ("write-back at every closeout" → "when its content changed"). Residue grep clean.

## COMPLETION — HOMER — 2026-11-20
STATUS: ✅ DONE
CHANGED: AGENTS/HOMER/thesis/THESIS.md, thesis/PREDICTIONS.tsv, STATUS.md, SCRATCH.md, CLAUDE.md, LESSONS.md, LESSONS_COLD_2.md, docket/CATALYSTS.tsv, registry/THRESHOLDS.tsv, registry/corrections_receipts.tsv, workbook/{PIPELINE,BUILDER,RATES,PRICING,KB_LIVE}.tsv, board_log.tsv, reports/2026-11-20_thesis-formal-grade.md, archive/STATUS_rotated_2026-11-20.md, inbox → processed (9); AGENTS/TERRY/inbox packet; this packet
RESULT: Thesis kill rail graded 0 of 5 legs killed, 🔴 holds, next grade 2027-02-20; handle 19 → 21/25. HOM-02 MISSED (FHA SA 11.74%, second QoQ fall, while the FHA foreclosure rate hit 1.89%, a 9-year high); HOM-04 HIT (46% of builders cutting; HMI 25). Inbox 9/9 drained, 4 stale KB rows retired, 2 corrections receipted.
GAPS: MBA primary unreachable (mba.org 403, site-wide) — graded on a verbatim mirror. ICE October First Look and GSE October monthlies not out (C1 and C2-GSE graded on September, D11). Not checked: Redfin Oct gap, NAR pending Oct, Miami Oct condo, C.A.R., ATTOM Q3.
WILL_NEEDS: None for the grade. D13 (amend A1's first conjunct to a migration-invariant measure) is Will's if PROME takes it up.
FOLLOW-UP: Closeout on PROME's ask (NEXUS_BRIEF rewrite due). ICE First Look Oct ~11/23–30; Trepp Nov ~12/01–05 (HOM-05).
