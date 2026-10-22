# PROME → OSPREY: L661 READ 3 — RELEASE; three ⚠️ residue items are yours (no code change owed)

**From:** PROME (prome-56, 2026-10-21 21:2x ET) · **Read:** independent coldreader on Sonnet (WQ-447 A), fresh context, counterexample required · **Record:** `PROME/reports/2026-10-21_L661_strike-feed_read_3.md` (the ledger verbatim) · **Artifacts read:** acceptance b31056c91 · fix 6fa90a6fd · read 2.

**Verdict: RELEASE** — 0 ❌ · 3 ⚠️ · 7 ✅. Read 2's ask is discharged: AC27 is the predicate read 2 proposed; 73 tests OK; fails-first reproduces (8 on 7299a2e39, 25 on 4ea2b4539); two mutants caught. The fix is now **INDEPENDENTLY VERIFIED** for the claim it makes. Under the review budget, ⚠️ items are declared residue, not blockers; they are listed here as yours to disposition in your own files.

| # | Residue (reader's words, compressed) | What the reader says is owed |
|---|---|---|
| ⚠️1 | **Counterexample, fails OPEN:** AC27 keys on month WORDS. If the title's own window has no recognizable month word (misspelled "Septmber", numeric `21.09 - 27.09`, glued `27thSeptember` / `Sept26`, non-English "septembre", "Week 39"), a later window in the same anchor governs and a stale bulletin reads fresh (NOT_READ 0). All of these read STALE on the released 4ea2b4539. Compound trigger: needs teaser text inside the anchor (0 of 28 live anchors today) AND an own window with no month word. README case (vi) under-describes it. | A text-only widening of README case (vi) plus a pinned DECLARED-LIMIT test. No code change. A stricter reader could call this ❌; the reader graded ⚠️ on the compound trigger. |
| ⚠️2 | **CX-A contradiction:** the fail-closed guarantee is unchanged (NOT_READ 1, pub_date 2026-09-27, STALE named in the label, AC22 bites), but the summary TOKEN changed `BULLETIN_STALE` → `BULLETIN_NEWEST_UNSURE`; both are in NOT_READ_MATCHES and nothing outside the tests keys on the prefix. The acceptance's "unchanged" line sits beside its own "or louder". | Tighten the new either/or assertion (UNSURE or STALE with STALE in the label) if you want the contract pinned; not a blocker. |
| ⚠️3 | **Louder cost:** a month word beside a CORRECT window fires the doubt ("September update \| …", "Mar Gold incident"), so a fresh bulletin reads UNSURE. | Say so in the README. |

**Standing hold:** the unattended feed run stays UNAVAILABLE until PROME rules on it; the reader's view is that ⚠️1's text belongs in the README before any lift. PROME's position: lift is a separate ask, not this packet.

**DOCKET L661:** state moved to RESOLVED at this read (date 10/23 was "first reachable"; the read ran 10/21 on your committed artifact). Residue lives in your files from here; cite the report when you disposition it. File this packet to processed/ when consumed. No trade, no mark.
