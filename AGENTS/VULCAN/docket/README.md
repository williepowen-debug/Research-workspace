# VULCAN `docket/`

## `CATALYSTS.tsv` — VULCAN's forward dated-event registry (created 2026-08-21)

**Source of truth for VULCAN's dated commitments.** `NEXUS_BRIEF.md`'s `⏱️ THE CLOCK` table
is the **human mirror** — it may summarise, but the **event SET must not diverge**. If they
disagree, this file wins and the CLOCK gets reconciled.

**Schema (8 col — fleet-dominant LIQUID/LABOR/SAM/BRENT/CARL/RED/BOND/ZHAO form):**
`date · event · what_to_check · threshold_signal · priority · who_cares · notes · date_class`

Adopted from **ZHAO's `docket/` build**, the reference implementation under the DAEDALUS
Q1 architecture ruling (packet `de9f1b441`, 2026-08-21). ⚠️ **Not invented here** — VULCAN
asked DAEDALUS the schema question *before* building and was told a canonical form had
landed that morning. Conformance is on a **ruling**, not a guess; the 2026-08-28 fleet
canonization sweep therefore **ratifies** this desk rather than migrating it.

### ⚠️ `date_class` — LOCALLY DECLARED ENUM. One field, one token.

| token | means |
|---|---|
| `confirmed` | the publisher has announced this exact date |
| `external` | a known publication schedule (e.g. TSMC's ~10th-of-month 6-K); day may shift ±2 |
| `estimated` | VULCAN inferred it from a customary window |
| `modeled` | month or quarter known, **day is a placeholder** — re-date when announced |

*Rendered with a `~` prefix for `modeled` (LABOR's convention).*

**Annotations go in `notes`, NEVER inside a machine-read cell** (ZHAO's rule, learned the
hard way: a Status cell reading `OPEN — GRADED 7/16, NOT FIRED` matched no filter and hid
the prediction that fired that day).

### ⚠️ `priority` — the **P-token** carries the meaning; a circle is decoration

`P1` / `P2` / `P3`. **STATE_VOCABULARY Class 9 (marker-role separation), Will-ruled
2026-08-21:** a coloured circle means *severity* everywhere else in the fleet, so using one
as a *priority* glyph makes any marker-scrape read a healthy high-priority row as an alert.
This file was built **after** the ruling and conforms **from row 1** — PROME's template-
surface rider: *a data file's existing rows are the template for its next row.*

### Why this file exists

`boot.py`'s only date leg read `workbook/PREDICTIONS.tsv`, which **by design** holds only
`VULCAN-NN` **market forecasts**. Every other dated commitment — a filing tripwire, a
self-grade owed, a docket resolver, a maturing guarantee — was surfaced by **nothing**.
Measured 2026-08-21: **10 dated commitments, 7 with no surfacing mechanism at all**, one of
which (the **9/11 self-grade**) existed in exactly one place: a line of prose in `SCRATCH.md`.

### Reader

`scripts/catalyst_countdown.py`, invoked by `boot.py` **leg 6**. Per the DAEDALUS ruling:
**ONE reader over the existing registries, never a fourth registry** — they have different
owners and lifecycles (`PREDICTIONS` rows are letter-frozen graded artifacts; `PROME/DOCKET`
is the coordinator's cross-agent surface; this file is VULCAN's forward calendar). Merging
them would break every consumer *and* you would still need the reader. **The measured defect
was never surface-count — it was INVOCATION.**

The reader covers four legs:
1. this file · 2. `workbook/PREDICTIONS.tsv:resolve_date` (OPEN rows) · 3. `PROME/DOCKET.tsv`
rows VULCAN **owns** · 4. **neighbours' registries naming VULCAN** — see below.

### 🔑 Leg 4 — the transport gap, and why the fix is consumer-side

VIOLET's `CATALYSTS.tsv` carries an `agent_domain` column; LIQUID's carries `who_cares`.
Both **name other desks**. **DAEDALUS 2026-08-21: they are LOCAL ANNOTATION — no transport
exists.** *"It reads as addressed and isn't"* (PAT-063 class).

**What that cost this desk, measured the day leg 4 was written:**
- **NVDA Q2 FY27 earnings 2026-08-26**, primary-verified at NVIDIA's own IR release, sitting
  in VIOLET's file tagged `VULCAN/VIOLET/HENRY` **since 8/18** — while VULCAN carried
  *"8/31 NVDA 10-Q"* as its S1 tripwire. **The capex guide lands at the CALL**, five days
  earlier than the date this desk held.
- **MU FQ4 ~9/29** flagged by VIOLET as **"ESTIMATED, NOT CONFIRMED"**, while **three**
  VULCAN predictions resolved against it as though it were settled.

The fix needs **no publisher cooperation, no new convention and no fleet rollout**: each
desk greps its own name out of its neighbours' files. ⚠️ **STRICTLY READ-ONLY on other
agents' trees** (PAT-054) — it reports; the human decides what to register.
⚠️ **Coverage matching is BY DATE ONLY and therefore COARSE** — a neighbour row on a date
already carried counts as covered even if it is a different event. It **under-reports**.
Stated rather than silently tuned: a coarse check that says so beats a precise-looking one
that doesn't.

⚠️ **This finding is n=2 rows, ONE publisher, ONE consumer.** That is not a demonstrated
fleet class, and it was **not** offered as one. The falsifying test — *across all catalyst/
calendar files, count rows naming a non-owner desk, then check whether that desk carries the
date* — is **registered for the 2026-08-28 sweep** (row in this file). If most desks DO carry
them, this is VULCAN's filing gap and the finding is retracted.

### Maintenance

Reconcile at **every closeout** alongside `NEXUS_BRIEF.md`'s CLOCK, or this becomes the next
out-of-loop surface — the exact failure that put `THESIS.md` 18 days into asserting the
opposite of `STATUS.md`. **When you ADD a surface, put it in a loop the same session.**
