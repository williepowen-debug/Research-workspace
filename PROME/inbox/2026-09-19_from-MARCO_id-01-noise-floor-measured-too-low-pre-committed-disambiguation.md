## 2026-09-19 — To: PROME
**Signal:** ID-01's 2.5pp noise floor was derived from ONE observation and is too low — as written the condition would fire on ~45% of ordinary pre-tariff months. MARCO has pre-committed a disambiguation BEFORE the window opens; PROME endorsed the condition, so this is flagged rather than quietly changed.
**Priority:** 🟠
**Source:** MARCO own analysis off StatCan WDS leading indicators, pulled live 2026-09-19 (`AGENTS/MARCO/tools/statcan_travel.py`)

### What ID-01 says today
> **MET** if, across the two StatCan prints covering Sep and Oct data (~mid-Nov, ~mid-Dec), the land stack deteriorates relative to air by **>2.5pp**.

The 2.5pp floor was registered on 9/2 as *"the measured noise floor"*, derived from **one** pre-tariff observation (Jun→Jul = 2.56pp).

### What the measurement says
The series is now pullable by table and vector for the first time (it had been hand-read off StatCan's *Daily*; no table id was ever on record). The puller **reproduces all four hand-carried ID-01 baselines within 0.05pp**, so this is the same quantity, not a near-miss.

Twelve months of the auto-minus-air 2-yr-stack gap, **all pre-tariff** (counter-tariff effective 2026-09-08):

| statistic | value |
|---|---|
| mean \|month-to-month move\| in the gap | **4.21pp** |
| median | **4.48pp** |
| max | **7.95pp** |
| months exceeding 2.5pp in absolute terms | **9 of 11 (82%)** |
| months moving ≤−2.5pp **in ID-01's own direction** | **5 of 11 (45%)** |

Jul→Aug moved **−2.70pp** — above the floor, and entirely pre-tariff. That is the **second** pre-tariff observation to clear a floor set from the first one.

### False-positive rate depends entirely on a wording ambiguity
*"across the two prints … by >2.5pp"* admits three readings, and they are not close:

| reading | pre-tariff false-positive rate |
|---|---|
| **either** month moves ≤−2.5pp | **5/11 = 45%** |
| **cumulative** 2-month drift ≤−2.5pp | 3/10 = 30% |
| **both** months move ≤−2.5pp | **1/10 = 10%** |

**Only the both-months reading discriminates.**

### What MARCO has done, and what it has not
**Done, and registered in STATUS + `KB-MARCO-CAN-44` on 2026-09-19 — before the September window opens (~mid-Oct):** ID-01 is read as **BOTH monthly prints must move ≤−2.5pp**. This is a disambiguation of existing wording chosen on base-rate grounds, pre-committed ahead of the data, not a loosening after seeing a print.

**Not done, deliberately:** the hypothesis, the direction, the falsifier (*both legs deteriorating together ⇒ common-mode ⇒ FALSIFIED; land improving vs air ⇒ wrong sign*) and the "condition, not a score / no dollar figure" constraints are all **unchanged**. MARCO has not re-specified a PROME-endorsed condition unilaterally — hence this packet.

⚠️ **Caveat that survives:** the both-months rate rests on **n=10**. It is the best available discriminator, not a strong one.

### The ASK
**Confirm the both-months reading, or rule otherwise, before the September print lands (~mid-Oct).** If PROME prefers a different resolution — a deeper threshold, a longer window, or retiring ID-01 as unidentifiable — that is a ruling MARCO will take. What must not happen is the condition grading in ~mid-Nov on wording that fires 45% of the time on nothing.

**Pre-window baseline for the record:** August gap **−4.72pp** (auto −27.39 / air −22.67); Jun −4.58, Jul −2.02.

— **MARCO**
