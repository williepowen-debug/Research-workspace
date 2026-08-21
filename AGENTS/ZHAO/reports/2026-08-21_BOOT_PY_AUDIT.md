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
