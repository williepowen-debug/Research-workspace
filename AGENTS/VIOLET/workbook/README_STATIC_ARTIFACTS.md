# Static derived artifacts — read this before "freezing" anything here

**Created 2026-08-20** in response to DAEDALUS PR#4 ACTION 3, which flagged that VIOLET's 2026-07-22 record calls two CSVs FROZEN while **no FROZEN banner or record exists in-tree**, and offered the choice *"banner them or correct the record."*

## The record is what was wrong. Correcting it.

| File | What it is | Read by |
|---|---|---|
| `DIET_COILED_SPRING.csv` | Backtest output — the 19-yr DIET/STRICT coiled-spring episode set behind the L1 canonical base-rate table (KB-VIO-067/079) | `diet_coiled_spring.py`, `two_anchor_ladder.py`, `sustain_run_query.py` |
| `FEB2018_VOLMAGEDDON_M1M2.csv` | Backtest output — the Feb-2018 M1:M2 term-structure analog study | `feb2018_m1m2.py` |

**These are STATIC DERIVED ARTIFACTS, not ledgers — and that is a different category from FROZEN.**

- The data-hygiene FROZEN rule (root `CLAUDE.md` § Data Hygiene) exists for **ledgers that silently drift behind STATUS** — live surfaces whose rows rot as the tape moves. Its banner says *"not maintained; STATUS is canonical, do not cite rows as current."*
- **Neither of these is that.** They are **immutable outputs of a dated computation over a fixed historical window.** They are *supposed* never to change. Their rows are not claims about today and were never going to be. **An artifact that is static by construction cannot rot, so FROZEN is the wrong label** — it would imply abandonment of something that is instead complete.

## ⚠️ Do NOT prepend a text banner to these files

**Four live scripts parse them as CSV.** A banner line ahead of the header breaks every one of them. **This is the failure mode where the hygiene fix causes the outage** — checked before acting rather than after (`grep -rln` over `scripts/`, 2026-08-20).

**If a future sweep flags these as stale by mtime or age: that is a false positive, and this file is the answer.** They are dated computations; their date is their identity. To refresh the science, **re-run the generating script and let it rewrite the file** — do not hand-edit rows, and do not banner them.
