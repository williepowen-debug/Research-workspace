# ZHAO docket/

## `CATALYSTS.tsv` — ZHAO's forward dated-event registry (created 2026-08-21)

**Source of truth for ZHAO's dated events. STATUS.md's CALENDAR is the HUMAN MIRROR** — it may summarise, but the **event SET must not diverge**. If they disagree, this file wins and STATUS gets reconciled.

**Schema (8 col, fleet-dominant — LABOR/SAM/BRENT/LIQUID/CARL/RED/BOND form):**
`date · event · what_to_check · threshold_signal · priority · who_cares · notes · date_class`

### ⚠️ `date_class` — LOCALLY DECLARED ENUM. One field, one token.

| token | means |
|---|---|
| `confirmed` | the publisher has announced this exact date |
| `external` | a known publication schedule (e.g. TIC mid-month); day may shift ±2 |
| `estimated` | ZHAO inferred it from a customary window |
| `modeled` | month or quarter known, **day is a placeholder** — re-date when announced |

*Rendered with a `~` prefix for `modeled` (LABOR's convention).*

**Why a declared enum:** the fleet census (2026-08-21) found **8 distinct values, 19 blanks, and a desk-private token** (`sam-internal`) across 13 desks — an uncontrolled vocabulary carrying machine-read load. DAEDALUS ruling: adopt now with a locally-declared enum; fleet STATE_VOCABULARY canon follows at the 8/28 sitting. Dropped `watch`/`pending` deliberately — an un-fired row already means that.

### ⚠️ ONE FIELD, ONE TOKEN — the rule this desk learned the hard way

**Annotations go in `notes`, NEVER inside a machine-read cell.** On 2026-08-21 ZHAO found two live instances of the same defect: a prediction Status reading `OPEN — GRADED 7/16, NOT FIRED` matched no filter and hid the prediction that fired that day; a `Last_Updated` cell reading `2026-07-04 (STALE — HAWK/BRENT own the live number)` made the row **permanently un-stale** — the word STALE in the field is exactly what blinded the staleness checker. **A cell with an annotation in it has stopped being data.**

### ⚠️ `priority` — P-TOKEN carries the meaning; the circle is decoration

**`P1` / `P2` / `P3`**, optionally followed by a coloured circle. **STATE_VOCABULARY Class 9 (marker-role separation), Will-ruled 2026-08-21** — provenance is this desk's own find: §4 was printing 🔴 as a *priority* glyph while 🔴 means *severity* everywhere else, so any marker-scrape would read a healthy high-priority catalyst as an alert, permanently and plausibly.

The ruling is **forward-only** and this file's existing rows were **grandfathered** — they were converted anyway, on 2026-08-21, the same day. ⚠️ **Reason, which generalises: a data file's existing rows are the TEMPLATE for its next row.** Forward-only compliance is defeated by copy-the-neighbour, so on a template-shaped surface the cheap moment to conform is while the author is still holding it.

### Reader

`scripts/catalyst_countdown.py` (invoked by `boot.py` §4). Per DAEDALUS Q1: **one reader over three registries** — this file + `PREDICTIONS.tsv:Resolve_By` + DOCKET rows naming ZHAO. **Never a fourth registry**: the three have different owners and lifecycles, and merging them is an interface break.
