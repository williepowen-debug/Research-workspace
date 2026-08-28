# HANS vs SAM vs ZHAO — regional-desk compare/contrast
**Author:** HANS · **Date:** 2026-08-28 · **Commissioned by:** Will, in-session ("HANS is a bit on the lighter side vs some of our other agents")
**Method:** direct measurement of the three trees at `origin/master` — file inventories, `git log` authorship counts, ledger row counts, `read_cap_check.py`, and reads of each charter. No estimates; every figure below is counted.

---

## BOTTOM LINE

**Will's read is correct, but the deficit is narrower and more fixable than "lighter" suggests.** HANS is not uniformly behind — it is **catastrophically behind on one axis and level-or-ahead on another.**

| | The finding |
|---|---|
| 🔴 **Where HANS is genuinely behind** | **Data infrastructure. HANS has ZERO ingestion scripts, no knowledge base, no time-series ledgers, and no boot script.** SAM has 20 pull scripts; ZHAO has 2 plus a staleness guard. **This is not a depth difference, it is an absence of mechanism** — and it is the direct, demonstrable cause of the 6.5-month staleness found on this desk today. |
| 🟢 **Where HANS is level or ahead** | **Governance instruments.** HANS is the **only one of the three with a standalone threshold registry + fire ledger + scannability classification**, and the **only one of the three that passes the read-cap budget.** SAM carries 6 boot reads over budget, 4 over the cap itself. |
| ⚠️ **The uncomfortable one** | **HANS carries MORE vectors than ZHAO and maintains FEWER.** 67 vs 39 — but **28 of mine are Jan–Mar vintage and ZERO of ZHAO's are.** I have been measuring breadth I cannot maintain. |

---

## 1. THE MEASUREMENTS

### Activity and output
| Metric | **HANS** | **SAM** | **ZHAO** |
|---|---:|---:|---:|
| Own-authored commits, all time | **31** | **442** | **77** |
| Commits, last 30 days | **19** | **180** | **31** |
| — *of which today (2026-08-28)* | ***19*** | — | — |
| Inbox files (lifetime traffic) | 16 | **173** | 53 |
| Outbox files | 16 | **32** | 11 |

⚠️ **Read the HANS column honestly: 19 of 31 lifetime commits are from today.** Before this session the desk had **~12 commits since February.** SAM commits more in a fortnight than HANS has in six months.

### Instruments and ledgers
| Instrument | **HANS** | **SAM** | **ZHAO** |
|---|---|---|---|
| **Ingestion scripts** | 🔴 **0** | ✅ **20** (one per series) | ✅ **2** |
| **`boot.py`** | 🔴 **none** | ✅ yes | ✅ yes (with staleness guard) |
| **`KB.tsv` knowledge base** | 🔴 **does not exist** | ✅ 167 rows / 168 KB | ✅ 128 rows / 106 KB |
| **Time-series ledgers** | 🔴 **none** | ✅ USDJPY 1,383 · MOF_FLOWS 1,130 · FXY_OPTIONS 193 · JGB_YIELDS 101 · RATE_DIFF 98 | 🟡 none (VX snapshots only) |
| Prediction book | 9 | **70** | 15 |
| Vector ledger | 67 | 15 | 39 |
| **Threshold registry + fire ledger** | ✅ **14 rows + 5 fires, only desk of the three** | 🟡 embedded in scripts/KB | 🟡 embedded in KB |
| Falsification surface | ✅ `KILL_TREE.md` (13 entries, built today) | ✅ **`thesis/` — 17 files incl. pre-registrations** | 🔴 **none** |
| **Read-cap compliance** | ✅ **PASS (only desk of three)** | 🔴 6 reads over budget, 4 over cap | 🟡 STATUS at 88% of cap |

---

## 2. 🔴 THE REAL DEFICIT: HANS HAS NO DATA INFRASTRUCTURE

**This is the whole finding, and it is causal rather than cosmetic.**

SAM does not know USD/JPY because a session looked it up. **SAM knows USD/JPY because `usdjpy.py` runs and appends to a 1,383-row ledger.** Same for JGB yields, BOJ OIS, CFTC positioning, MOF flows, CPI, trade balance, cross-currency basis — **20 series, each with its own puller, each landing in a ledger that grows.**

**HANS has no equivalent of any of it.** Every number on this desk arrives by hand, from a web search, into a snapshot cell that is then correct exactly until it isn't — with **nothing that notices when it stops being true.**

### What that cost, measured today
| Defect found 2026-08-28 | Duration undetected |
|---|---|
| BoE Bank Rate carried at 4.50% (actual **3.75%**) | **6.5 months** |
| TTF vector carrying `17.5` under a fresh 7/16 stamp | ~6 weeks, survived a domain sweep |
| 28 of 67 vectors on Jan–Mar vintage | **5–7 months** |
| Whole desk frame wrong (energy-crisis → long-end) | **43 days dark** |

**None of these are analytical failures. Every one is a missing-mechanism failure**, and SAM's architecture makes the entire class impossible: a script that runs cannot forget.

### 🔑 THE SHARPEST FACT IN THIS REPORT
**ZHAO's `boot.py` docstring, verbatim:**
> *"FLAGS ANY TRACKED FIGURE THAT HAS GONE STALE, so a **2.5-month drift** like the one found on 2026-07-04 surfaces at boot instead of never."*

**ZHAO had my exact failure, at half the magnitude, seven weeks earlier — and built the fix.** I had a **6.5-month** drift and found it **by hand**, in a session Will had to spawn. ⇒ **The remedy already exists in this fleet, is 2 scripts wide, and I did not adopt it.** That is the finding I would most want acted on.

---

## 3. 🟢 WHERE HANS IS LEVEL OR AHEAD — stated because a fair comparison has to

**This is not defensiveness; both items are measured and both cut against the "lighter = worse" reading.**

1. **HANS is the only one of the three with a standalone threshold registry.** `registry/THRESHOLDS.tsv` (14 rows) + `HANS_T_FIRED_LOG.tsv` (5 fires, 4 open) + a README carrying a **scannability classification** — 6 auto-gradable, 7 needing a human or calendar, 1 explicitly **uninstrumented and marked as un-fireable so the gap stays countable.** SAM and ZHAO keep thresholds inside scripts and KB rows, which works but is not separately auditable.
2. **HANS is the only one of the three that passes the read-cap budget** (root P1 ruling, 32,550 B). STATUS at 27,552 B / 51% of cap. **SAM has 6 boot-mandated reads over budget and 4 over the cap itself; ZHAO's STATUS sits at 88% of cap.** ⚠️ **Being small is currently protecting HANS from a debt both larger desks now have to pay** — so *"grow like SAM"* is the wrong instruction taken literally.

---

## 4. ⚠️ THE FINDING I LIKE LEAST — breadth I cannot maintain

| | HANS | ZHAO |
|---|---:|---:|
| Vectors carried | **67** | 39 |
| Refreshed in August | 27 | 4 |
| **Still Jan–Mar vintage** | **28 (42%)** | **0** |

**ZHAO carries fewer vectors and no fossils. HANS carries 71% more vectors, 42% of which are 5–7 months dead.** A larger ledger read as coverage; it was **inventory**. ⇒ **The fix is not only "add scripts" — it is also "retire or freeze what cannot be maintained."** A 67-row book where 28 rows are fiction is worse than a 39-row book that is true, because the dead rows make the coverage look better than it is.

---

## 5. WHAT SAM HAS THAT IS WORTH COPYING — AND WHAT IS NOT

**Worth copying (highest value first):**
1. **Per-series ingestion scripts** — the whole deficit above.
2. **`boot.py` with a staleness guard** — ZHAO's is the right size to copy; SAM's is the mature form.
3. **`KB.tsv`** — and its **schema is the instrument, not the file**: `ID · Date · Group · Entity · Fact · Source · Conf · **Epistemic** · Status · **Stale_By** · **DerivedFrom** · Vectors · Notes`. **`Stale_By` is a built-in expiry; `Epistemic` separates measured from inferred; `DerivedFrom` gives provenance chains.** My `ML.tsv` (426 rows) is a flat log with **none of those fields** — it cannot expire, cannot flag an inference, cannot show what a claim rests on.
4. **Pre-registration documents** (`thesis/*_PREREGISTRATION.md`) — SAM writes the hypothesis, the rival hypotheses and the discriminating signature **before** the event. My prediction rows are one line; SAM's are a document. Given today's finding that my book is mostly momentum continuations, **this is the discipline that would fix it.**

**NOT worth copying:**
- **SAM's boot-read weight.** 6 reads over budget, 4 over the cap. **SAM is paying read-cap debt that HANS does not have.** Copy the *instruments*, not the *volume*.
- **SAM's 442-commit cadence** is a function of Japan being a live, fast, position-bearing thesis. **`EUROPE_MACRO` currently carries one routed signal since the code shipped 8/18** — the flow does not justify that tempo, and manufacturing it would be theatre.

---

## 6. RECOMMENDATION — ranked by value ÷ cost

| # | Action | Cost | Why first |
|---|---|---|---|
| **1** | **`scripts/boot.py`** — port ZHAO's shape: live pull (TTF, Bund, gilt 10Y/30Y, EUR/USD, DXY) + **key-figure age** + catalyst countdown + open predictions + VX staleness | **~1 session** | **Kills the entire defect class that produced today's session.** Highest value in the report by a wide margin. |
| **2** | **Retire or freeze the 28 fossil vectors** | ~half session | Makes the ledger true. Must precede automation or the script will faithfully monitor fiction. |
| **3** | **`workbook/KB.tsv` on ZHAO's schema** | ~1 session | Gives claims an expiry (`Stale_By`) and an epistemic class. Seed from the ~40 live facts in STATUS, **not** by migrating 426 stale `ML.tsv` rows. |
| **4** | **3–5 ingestion scripts** for the daily-scannable registry rows (`T-05` Bund · `T-06`/`T-13` gilts · `T-07` TTF · `T-08` storage gap · `T-11` EUR/USD) | ~1–2 sessions | Turns 6 auto-gradable registry rows from *aspiration* into *mechanism*. |
| **5** | **One pre-registration** on the next real event (**ECB Sept 10**, `HNS-05`) | ~1 hour | Directly answers the "book is all continuations" self-challenge. |

⚠️ **Sequencing matters and #2 must not slip behind #1.** Automating a ledger that is 42% fiction produces a script that reports confidently on dead rows — **the exact defect I logged four times today, rebuilt in code.**

---

## 7. HONEST LIMITS OF THIS REPORT

- **I am the subject.** A self-assessment naming a mostly-fixable deficit and two areas of advantage is the flattering shape; **weight it accordingly and check the counted figures, which are reproducible.**
- **I did not read SAM's or ZHAO's charters in full** — 33 KB and 29 KB respectively. Structure and ledgers were measured; **judgement quality was not assessed and is not claimed.**
- **Commit counts measure output, not value.** SAM's 442 reflects a live position-bearing thesis; a desk with genuinely less to say *should* commit less. **The damning number is not 31 commits — it is 28 fossil vectors and 0 scripts.**
- **No comparison was made to the other regional desks** (BRENT, HAWK, MARCO, CORAL, AEOLUS). Scope was Will's: SAM and ZHAO.
