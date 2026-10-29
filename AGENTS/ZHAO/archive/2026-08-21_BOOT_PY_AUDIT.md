# boot.py audit — 2026-08-21 (ZHAO)

**Trigger:** Will asked whether `scripts/boot.py` needed more attention than the three defects found incidentally at this morning's boot. **It does.** Full read + empirical tests of every section. 252 lines.

**Headline: all four live defects FAIL SILENTLY AND IN THE SAFE-LOOKING DIRECTION.** "nothing within ±30d" · "✓" not-stale · absent from the open-predictions list. **A boot brief that fails open is worse than no boot brief, because it certifies.**

---

## LIVE DEFECTS — confirmed by test

### 🔴 D1 — §4 `CATALYSTS` is a hardcoded 4-item list, never updated *(known 8/21 AM)*
2 of 4 entries are in the past (7/16, 7/17). **None of the five catalysts the 8/3 session added to STATUS's CALENDAR was ever written into it.** Result this morning: `(nothing within ±30d)` printed while **ZHA-15's grade was 8 days overdue and the Aug-31 PMI arbiter was 10 days out.** The section whose only job is to prevent that failure produced silence.

### 🔴 D2 — §2 `KEY_FIGURES` points at a DEAD duplicate row *(known 8/21 AM)*
`("China PMI", "VX-ZHAO-4.01")` → Jun 50.3, dated 7/4. The live row is **`VX-ZHAO-6.11`** → Jul **49.2**, dated 8/3 (added 8/3 as a *new* row rather than an update, so two rows now exist for one metric). Boot reported **both the age and the sign wrong** — "50.3 🔴 STALE 48d" when the truth was "49.2, 18d, and it's a contraction print."
*Root cause is upstream of the script: one-metric-two-rows violates ZHAO's own "one source of truth per metric" rule.*

### 🔴 D3 — §5 drops any prediction whose Status carries a qualifier ⚠️ **NEW — the most consequential**
`if r[5].strip().upper() == "OPEN"` is an **exact match**. Measured against the live ledger: **8 of 15 predictions are dropped.** Legitimately (resolved): ZHA-02/08/09/14 and today's ZHA-03/04/15. **Wrongly: `ZHA-11` and `ZHA-13`, both `OPEN — GRADED …`, are genuinely open and have been invisible at every boot.**

> **And this morning it hid the prediction that fired today.** ZHA-04's status read `OPEN — GRADED 7/16, NOT FIRED`. It did not match, so **§5 did not list ZHA-04 as open** — the $650B breach was found by pulling TIC, not by the brief.
>
> ⚠️ **Perverse incentive: the more carefully a status is annotated, the more likely it vanishes from the boot brief.** Adding "— GRADED 7/16, NOT FIRED" is exactly what a careful grader does.

### 🔴 D4 — staleness checks FAIL OPEN on an unparseable date ⚠️ **NEW**
`_age_days()` returns `None` on parse failure; both §2 and §6 guard with `age is not None and age > …`, so **`None` reads as NOT stale, forever, silently.** Two rows are currently permanently exempt:
| Row | Date field | Why it never parses |
|---|---|---|
| `VX-ZHAO-6.10` CIPS Volume YoY | `2026-05` | month-only, no day — ~3.5 months unflagged |
| `VX-ZHAO-7.02` Gulf Recycling | `2026-07-04 (STALE — HAWK/BRENT own the live number)` | prose in the date field |

> **`VX-ZHAO-7.02` literally contains the word STALE in the field the staleness checker reads, and that is precisely why the checker cannot see it.**

---

## SHARED ROOT OF D3 + D4 — the finding worth carrying

**Both fields are simultaneously human-annotated free text and machine-parsed. In both cases the ANNOTATION — the thing a careful analyst adds — is what blinds the instrument, silently and in the safe direction.**

Same shape, two fields: a Status gains "— GRADED 7/16" and disappears from the open list; a date gains "(STALE — …)" and becomes permanently fresh. **Neither degrades loudly; both look like the good outcome.**

**Fix direction:** parse with a prefix/keyword match, not equality (`status.startswith("OPEN")`); and **fail LOUD on an unparseable date** — an unreadable vintage must print `⚠️ UNPARSEABLE` and count as stale, never as fresh. Better still: constrain the machine-read fields and put the prose in `Notes`.

---

## LATENT / MINOR — not currently biting

- **L1 naive TSV parse.** `_read_tsv` uses `line.split("\t")`, not the `csv` module. ⚠️ **Tested: NOT currently mis-reading** — row counts and field counts agree across PREDICTIONS/VX/KB, zero embedded newlines. *(I had drafted this as a live defect and the test refuted it.)* Latent: I write these files with `csv.writer`, which **would** quote-and-embed a newline if one ever appeared, and the naive parser would then shift rows silently. Harden opportunistically.
- **L2 quoted fields display raw.** ZHA-12 renders as `"BoK hike (delivered: …` — cosmetic, same root as L1.
- **L3 FX "close" is a provider daily bar, not a settlement** — §1 prints a band verdict off `history(period="5d").Close.iloc[-1]`. Relevant to WALTER's N5 rule (*never quote a bar as a close*), still unprocessed in ZHAO's lane. Today's Korea grade was re-tested on the intraday-high basis for exactly this reason.
- **L4 Brent band is a single `>$100` step** — $93.94 prints 🟢 "normal" against a row that had said $76.01 since 7/9. No delta, very wide green. *(And a delta across `BZ=F` would be fabricated anyway — continuous front contract.)*
- **L5** §2 truncates values to 14 chars. **L6** unused `WORKSPACE` var. **L7** always exits 0 — advisory only, cannot gate.

---

## DISPOSITION

D1–D4 are the fix set; D3 and D4 are the ones that change behaviour rather than presentation. **One genuine design question for Will, not a bug:** should `CATALYSTS` stay a maintained list (and simply get maintained), or be **derived from STATUS.md's CALENDAR table** so the two cannot diverge again? Derivation removes the failure mode permanently but couples the script to STATUS's formatting. **Not decided unilaterally.**

*`boot.py` fix is ZHAO's (PROME ruling 8/21); the finding rides to DAEDALUS as 8/28 sweep-input ⑪.*

---

# ADDENDUM — fleet survey: how other desks handle CATALYSTS (2026-08-21)

**Asked by Will. Surveyed rather than reasoned-from-principles — and the answer is that neither option I offered was the fleet's.** I proposed (a) keep a maintained hardcoded list or (b) derive from STATUS's CALENDAR. **The fleet does (c): a separate TSV data file read by a dedicated sub-script.**

## The established pattern

| Layer | What | Adoption |
|---|---|---|
| **Data** | `docket/CATALYSTS.tsv` (VIOLET/LIQUID use `workbook/`) — **8-col schema**: `date · event · what_to_check · threshold_signal · priority · who_cares · notes · date_class` | **13 agents** (LABOR, SAM, BRENT, LIQUID, CARL, RED, BOND, BROCK, HOMER, OTTO, MARCO, VIOLET*, BARON*) |
| **Reader** | `scripts/catalyst_countdown.py` — standalone, reads the TSV | **6 agents** (HAWK 222ln · MARCO 219 · OTTO 183 · LABOR 147 — **all four md5-distinct; drifted, never a shared module**) |
| **Orchestration** | `boot.py` invokes it as a registered sub-script step | HAWK, LABOR, SAM, BRENT, MARCO, OTTO |
| **Self-check** | the catalyst file is itself staleness-bounded (LABOR: **14d** on `CATALYSTS.tsv`) | LABOR |

*\*VIOLET and BARON use variant schemas — VIOLET: `date · event · type · agent_domain · expected_vol_impact · source · notes`.*

**ZHAO is the outlier: the only surveyed desk with catalysts hardcoded in Python.** That is the whole of defect D1 — a data list living in code cannot be edited at closeout, cannot be staleness-checked, and silently diverges from STATUS's CALENDAR.

## Two features the fleet has that solve problems I currently have

**① `date_class` — an honest-dates taxonomy.** Values in live use: `confirmed` (24) · `resolved` (42) · `pending` (18) · `external` (17) · `modeled` (13) · `estimated` (3) · `watch` (3). **LABOR renders a `modeled` date with a `~` prefix and prints a legend line** (*"'~' prefix = modeled/projected date (not source-confirmed; may revise)"*).
> **This is exactly ZHAO's tilde problem made machine-readable.** My CALENDAR is full of `~Sep 16`, `~Aug 17-18` — prose tildes a script cannot reason about. `date_class` distinguishes *"Treasury publishes on a known schedule"* from *"I estimated this."*

**② OTTO's section-sticky FIRED rule — and OTTO hit my exact failure a month before I did.** `AGENTS/OTTO/scripts/boot.py` carries this comment:
> *"every fired row must surface regardless of its priority glyph. A 🟡 fired catalyst is still an UNSWEPT catalyst, and **filtering the past-due-catch by priority silently re-creates the exact miss the countdown exists to prevent.** (2026-07-25: 3 of 4 fired rows were hidden at boot — incl. the First Brands creditor-vote deadline, a direct dependency of the OTTO-32 resolver.)"*

**Same class as ZHAO's 8/21 miss** (ZHA-15's grade and the Korea tripwire both came due with nothing sweeping them), found by another desk on 7/25, with the trap already documented. ⚠️ **Note the trap is one level deeper than my fix would have gone:** I would have added a countdown and might well have filtered it by priority.

## Recommendation

**Adopt the fleet pattern rather than either option I put to Will:**
1. Create `AGENTS/ZHAO/docket/CATALYSTS.tsv` on the **dominant 8-col schema** (not VIOLET's variant), seeded from STATUS's CALENDAR.
2. Port `catalyst_countdown.py` — **donor: OTTO**, because its documented failure is identical to mine and it carries the section-sticky FIRED logic. *(HAWK is larger; largest ≠ most apt.)*
3. `boot.py` calls it as a registered step; **delete the hardcoded `CATALYSTS` list.**
4. Add `CATALYSTS.tsv` to boot's own staleness check (LABOR's 14d bound).
5. Use `date_class` for every `~` date ZHAO carries.

**Direction of truth: the TSV becomes the source and STATUS's CALENDAR the mirror** — the reverse of my option (b), and it removes the STATUS-formatting coupling that made (b) unattractive.

⚠️ **Not adopted from the fleet: a shared module.** All four `catalyst_countdown.py` copies are md5-distinct — the fleet has pattern reuse, not code reuse, so **porting means inheriting a fork, and OTTO's fired-row fix demonstrably did not propagate to the other three.** Worth flagging to DAEDALUS as a fleet observation; not ZHAO's to fix.
