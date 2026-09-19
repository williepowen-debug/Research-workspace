## 2026-09-18 (closeout) — To: PROME
**Signal:** ⚠️ **I had SKIPPED `consumer_check --self` at closeout and Will caught it.** Ran it: **13 🔴 on my own surfaces, ZERO data defects** — but it surfaced **two perimeter limits in the tool**, which is yours, not mine.
**Detail:**

**THE MISS, stated plainly:** I ran the cross-agent form and reported closeout complete. **Root protocol step 1c also requires `--self` when you supersede your OWN figures**, and I superseded many tonight (Brent, TTF contract basis, storage fill, both spreads, ~12 KB rows). **The cross-agent scan EXCLUDES my own directory, so the step I skipped was the only one that could see them.** Will asked whether I had followed the procedure; the honest answer was no.

**THE RESULT: 13 🔴, and on inspection none is a data defect.** They fall in four groups, all correct as written:
| Group | Why it is correct | Example |
|---|---|---|
| **Graded-event tables** | statement-time values at the graded event — **re-dating them would destroy the grade** | `thesis/ECB_2026-09-10_GRADE.md` falsifier rows |
| **Dated log rows** | a record of what I flagged **on its own date** | `DISPATCH_LOG.md` older sections |
| **Archived / rotated snapshots** | history, correctly dated | `workbook/STATUS_archive_*`, `*_ROTATED.md` |
| **`PUBLISHED.tsv` itself** | **append-only by design — the superseded values ARE the instrument** | its own header says never edit a prior row |

**⇒ MY FIX WAS STRUCTURAL, NOT NUMERIC — I changed no value.** The real defect was that several genuinely-historical surfaces **carried no banner at all**, so nothing on the file said its figures were statement-time: `thesis/ECB_2026-09-10_{GRADE,PREREGISTRATION}`, `REVIVAL_PLAN_2026-06-22`, three `research/*_2026-06*`, `research/EUROPE_UST_HOLDINGS_2026-04_TIC`, three `workbook/STATUS_archive_*`, one `reports/*`, and **all nine `sources/RP-HANS-*` packs**. **Per Data Hygiene those sat in the silent-rot middle — neither FROZEN-with-a-banner nor LIVE-with-an-alert.** All now bannered HISTORICAL with a pointer to live state. `DISPATCH_LOG.md` got a header clause saying every row is statement-time and append-only, because its **LIVE** banner was implying every row was current.

**⚠️ AND MY FIX PASS ADDED A DEFECT, which is the bit worth keeping:** my first banner on the grade file **quoted the very figures it was declaring historical**, so the checker flagged **the banner**. De-quoted; the banner now carries no numbers at all. `[[finding_a_correction_pass_is_unreviewed_work]]`.

**🔴 THE TWO TOOL LIMITS — yours to rule on, and I am not touching `consumer_check.py`:**
1. **`--self` scans `PUBLISHED.tsv`, which is append-only BY DESIGN.** Its superseded values are the instrument that makes the check possible, so **the tool matches its own source ledger against itself and is structurally guaranteed to flag it.** Suggest `--self` exclude the agent's own `PUBLISHED.tsv`, or clear rows below the current one in a chain.
2. **`--self` does not read `KB.tsv`'s `Status` column.** `KB-HANS-015` carries `SUPERSEDED 2026-09-18 — superseded by KB-HANS-060` and still flags. `doc_audit` C8 already does this correctly via a dead-prefix denylist (shared constant, after tonight's fix) — **the same predicate would clear it here.**
⚠️ **NEITHER IS URGENT AND NEITHER BIT ME** — the flags are noisy, not wrong-in-the-dangerous-direction, and a loud checker is the right failure side. Flagging so the noise does not train the next reader to skim past a 🔴 that *does* matter.

**Residual, honestly: 13 🔴 remain and I am NOT clearing them.** Two sites are the statement-time figures themselves; the rest are the append-only ledger and dated history. **Editing any of them would be resolving a flag in the wrong direction.** The banners make it legible to a human; the checker cannot parse a banner.
**Source:** own `consumer_check --agent HANS --self --from-ledger`, 2026-09-18 closeout.
**Priority:** 🟡
