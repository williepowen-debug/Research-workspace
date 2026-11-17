# Weekly scorecard — November 7–13, delivered November 16

COMPLETE, three days late (owed Friday 2026-11-13; rendered 2026-11-16 about 21:00 ET on PROME prome-c4's 20:56 ET message relaying Will's word). Unchanged v1.3 renderer; 27/27 selftests pass; production render rc 0. Fixed source commit `916e683f5dbfa517e3aab361fe310b52946bad35`, detached shared-object clone, sparse `*.md/*.tsv/*.py`, full Git history, inputs clean. `scorecards/2026-11-13_inputs.json` pins the basis and output hashes. All ten previous series rows conserved; exactly one row appended (base file identical to the pinned commit before the append).

| Measure | Result |
|---|---:|
| Sourced docket dispositions | 92; another 2 lack source references; 68 tombstones date NOT-SEEN |
| Terminal forecast entries | 16: 8 HIT, 1 MISS, 1 NO-VERDICT, 4 RESOLVED-UNTYPED, 2 UNMAPPED (HEN-57, HEN-58 `RESOLVED-HIT`) |
| Recorded brief-defect catches / published corrections | 7 / 11; different populations, no efficiency ratio |
| Recorded ruling stamps (instrument) | **0 — INSTRUMENT MISS, see below**; Will-minutes not measured |
| Commits / author-days / logged touches | 1,389 / 11 / 170 |
| Zero-capital affirmative touches | 170 / 170 |
| PROME-only-path commits | 482 / 1,389 |

⚠️ **Column 5 (rulings) and column 7 (decision yield) are wrong this week, and the cause is the instrument.** WILL_QUEUE rows now record a ruling in the second cell as `Done YYYY-MM-DD HH:MM ET — RULED X`; the v1.3 parser reads only `RULED YYYY-MM-DD` inline or the title form with the date leading the second cell, so it reads none of them. A hand grep of the same pinned file finds 35 rows marked Done inside the window with a RULED verb (rows 645 and 650 to 683; 649 MOOT excluded); 4 are C9 class receipts fired without an ask (672, 675, 680, 683), leaving about 31 Will rulings. That is a hand count, not an instrument cell, and the series row keeps the instrument's 0 so the series stays one method. The previous week's 20 stamps may also be an undercount; not re-checked here. Repair is an existing-tool fix in DAEDALUS's lane (teach the parser the `Done <date> — RULED` form, selftest both forms); not done in this delivery.

Cutoff: rendered against the 11/16 committed snapshot with the 11/7–11/13 event-date filters unchanged, so later-entered dispositions can appear and compacted or unstamped items can be missed. Activity counts are not evidence of improvement or decline. WQ-656 B (CRL-15 ungradeable, no Brier) does not touch this instrument: the scorecard counts terminal tokens and computes no Brier.

REVIEW: not-required — scheduled execution of the existing method, no scoring rule or code change; the column-5 miss is disclosed, not repaired. Last actual run November 16; next Friday obligation November 20.
