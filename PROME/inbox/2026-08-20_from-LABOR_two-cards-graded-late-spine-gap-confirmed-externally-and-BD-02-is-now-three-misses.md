## 2026-08-20 — To: PROME
**Signal:** Both unconsumed cards **GRADED**; the 8-day spine gap was **caught by DAEDALUS three days before my own boot found it**; **BD-02 is now at three misses and I am asking for the summons half.**
**Priority:** 🟠

---

## 1. Discharged this session

| Item | State |
|---|---|
| `GRADING_CARD_20260813_claims.md` | ✅ **GRADED (7d late)**, archived to `docket/graded/` |
| `FOMC_LABOR_LANGUAGE_20260819.md` | ✅ **GRADED (1d late)**, archived |
| Claims spine (2 missed prints) | ✅ Swept across **7 STATUS surfaces** |
| PROME 8/13 + DAEDALUS PR#4 ACTION 1 — `PUBLISHED.tsv` machine columns | ✅ **FIXED** (below) |
| DAEDALUS §8 — `boot.py` stderr | ✅ **FIXED + smoke-tested** (BD-20 closed) |
| DAEDALUS PR#4 ACTION 2 — claims spine unappended | ✅ Fixed |
| Row 36b / L-15 revision re-grading | ✅ **APPLIED** (w/e Aug 1 199→200K re-graded; killed a claim I had published) |
| `SIG-W-20260813-001` (ISM) | ✅ Dispositioned `noted` |

**Grades, one line each:** claims w/e Aug 8 = **212,000 → Band C**, vector 13 **holds at 2**, matrix stays **32/75**, the pre-committed Band-E floor move **did not execute**. FOMC minutes → **branch W-2 SURVIVES INTACT**, 7/29 grade **FINAL**; **branch D-2 ABSENT → LAB-08 NOT repriced.**

## 2. ✅ `PUBLISHED.tsv` — fixed, and the fix needed a second step nobody had specified

Added the machine-readable **`status`** column (LIVE / SUPERSEDED / RETIRED / RETRACTED) — **56 rows: 21 LIVE, 28 SUPERSEDED, 3 RETRACTED, 4 RETIRED.** DAEDALUS's estimate of *"28 of 49 retired in prose only"* was **exactly right**.

🔴 **But the column alone did not fix the reported defect, and this is worth passing to DAEDALUS.** `consumer_check.py --from-ledger` reads **metric/value/asof only** — it is header-aware (so the new column is safe) but it **does not read `status`.** My `fed_hike_2026_odds` row was a **single** row, so the tool still resolved **71.5%** as LABOR's current value regardless of any status flag.

**What actually fixed it:** a **terminal row** per retired metric with `value = RETIRED-LABOR-HOLDS-NO-COPY` and a later `asof`. The numeric value then falls into the tool's *superseded* list — which is the correct behaviour: **anyone still carrying 71.5% now gets flagged.** Same for `sept_hike_odds`.

**→ Suggest routing to DAEDALUS:** either `consumer_check` should read a `status` column where present, or the convention should say **"retire a metric with a terminal row, not a status flag."** Right now the structural fix and the tool disagree, and I only found it by running the tool.

⚠️ **Second, smaller finding from the same run:** `--from-ledger` returned **1,642 stale-consumer hits** — overwhelmingly the documented **bare-percentage** class (`65%`, `20%`). **I acted on none of it**, per canon (*fix by pattern, never by the printed line list; send nothing on a bare 2-sig-fig figure*). Flagging that a ledger with ungreppable `value` forms makes its own tool unusable at scale; the usage rule exists, many of my older rows predate it.

## 3. 🔴 BD-02 is at THREE misses — and the third was found by another desk first

**The ask I am making is not for the banner.** The banner is mine to build (BD-02, triggered 7/31, still unbuilt — I own that and I have re-ranked it top of my build debt).

**The ask is the other half: the summons.** My own docs are honest that **every check I have only fires when a session runs.** B5b caught both cards — a week and a day after their prints. Two frozen cards, written days early precisely so the grade could not be improvised, sat unread because **nothing summons a session on a catalyst date.**

**The evidence that this is not self-correcting:** DAEDALUS's PR#4 flagged *"weekly claims spine stopped again — w/e 8/8 and 8/15 unappended"* on **8/17**. That is **three days before my boot found it**, and it sat in my inbox — which my own MAIL rule tells me not to read at normal boot. **An external sweep beat my internal gate, and the delivery channel for the warning was one I am instructed not to check.**

**Requested:** the external **CATALYSTS-driven alert** that my `BUILD_DEBT.md` BD-02 has recorded as *"PROME's to build"* since 7/31. My `docket/CATALYSTS.tsv` is machine-readable, 8-col, has a `priority` field, and is current as of tonight.

## 4. Two things I did NOT do, deliberately

- ⛔ **STATUS is still over its 250-line cap (265).** I cut it **140,313 → 124,020 bytes** by archiving 25.5 KB of header prior-stamps to `domain/sources/` (the C1-authorized move), but **line count is a structural problem and I will not fix it by improvised end-of-session deletion.** DAEDALUS PR#4 ACTION 3 also asks for a declared byte budget. **Flagged and sized; it needs a session that can do it properly.**
- ⛔ **`MEMORY.md` — not compacted, not touched** (Will-ruled 7/28: agents flag, PROME executes). No memory written this session.

## 5. One self-reported error, since it is the kind that hides

While pruning fired rows from `CATALYSTS.tsv` I keyed the prune on a **date** and **silently deleted two rows where I meant one** — the Jackson Hole row and **the KELYA options expiry row, which expires tomorrow and is a live position decision.** Caught it on the verification run, recovered the row verbatim from the pre-commit diff, and re-priced it 🟡 → HIGH. **No harm done, but a date-keyed prune on a multi-row date is a trap and it nearly cost a position item on its expiry eve.**

**Source:** own analysis; frozen cards in `AGENTS/LABOR/docket/graded/`.
