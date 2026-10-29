# H5: residual-flag patch for the CREED case ledger (proposed, not applied)

**Input:** `AGENTS/CREED/cases/CASE_NOTES.md` § "Residual flags after the 2026-09-29 correction pass" (lines 1086–1178). It holds 88 bullets across 44 cases. `flag_no` runs 1–88 in bullet order.
**Output:** `H5_case_patch.tsv` (92 rows, 10 columns). The build script `build_patch.py` sits beside it. It reads every `current_value` from the live files rather than typing it, so each one was byte-exact at build time (2026-10-28).
**Method:** repo evidence only. No web lookups. Every figure is taken as found; nothing new was derived except two checks of existing ratios, which are named in their rows.

## Counts (one primary action per flag)

| Action | Flags | Rows |
|---|---|---|
| RELABEL | 30 | 30 |
| CANNOT-FIX | 22 | 22 |
| FIX | 16 | 17 |
| OBSOLETE *(not one of the four requested actions; added because these flags are already settled, see below)* | 14 | 14 |
| VOCAB | 6 | 9 |
| **Total** | **88** | **92** |

Four flags take more than one row:
- **41:** a FIX to the trigger plus a README definition.
- **56:** a README edit plus the 028 trigger row.
- **85:** a latest_status vocab edit, an event_type vocab edit, and the 054 status_as_of FIX.
- **60:** carries its own 029 trigger row and depends on flag 56's README edit.

## Flags that are obsolete (14): already fixed by later passes, or no ledger cell carries the problem

| Flag | Case | Why there is nothing to do |
|---|---|---|
| 5 | 003 | special_servicer filled 2026-10-01 (Midland) |
| 6 | 004 | event bases already DERIVED / carrying |
| 9 | 005 | value_marks rewritten 10-21 to the county-record receiver sale |
| 15 | 007 | "identity INFERRED" exists only in the seed-verbatim block |
| 31 | 016 | property_type filled 10-21 from a named source |
| 35 | 018 | the under-secured inference is in no cell |
| 49 | 024 | the $330M sale FAILED; row is now REO (2026-09-30) |
| 50 | 024 | already labelled DERIVED |
| 59 | 029 | already DERIVED; the Atrium model values are in no cell |
| 63 | 032 | the $780M basis and the appraisal date are already labelled on the events |
| 67 | 033 | HOMER answered 10/15 (declined the case) |
| 81 | 049 | already UNRECONCILED |
| 83 | 051 | no cell imports the "severity" label |
| 88 | 055 | already UNKNOWN |

Partly obsolete as well:
- **Flag 34** (034 implied_loss_pct): the relabel half is already applied. Only the remittance read is still owed.
- **Flag 51** (025, $56.2M): no ledger cell holds the figure.

## Flags that were wrong or have moved on

- **Flag 2 (001 loss) is now settled at primary.** KB-CREED-046's 2026-10-28 segment and `research/2026-10-28_3000_POST_OAK_10D_LOSSES.md` add up the three trust 10-Ds:
  - Total realized loss **$64,782,869.38 = 86.86%** of the $74,579,200.28 balance at the loss. This reproduces the CRE News $64.8M.
  - The CASES row still says "~$64.5M pro-rata ESTIMATE". The patch replaces that cell.
  - ⚠️ CASE_EVENTS row 318 has an **uncommitted edit in the working tree right now**, so the patch does not touch it.
- **Flag 1 (001 HCAD ~$45M):** the row's "interim appraisal $45M [X/Nightingale]" may be the same $45M as the video's Harris County figure, which would make it a tax-assessor value. That is a possible basis error in an existing mark. Only the HCAD record can settle it.
- **Flag 28 (014 holder):** "hearing outcome not in files" is out of date. KB-WAL-227 shows that FDIC, as receiver for Nano, appeared as creditor-successor at the 9/29 hearing (Doc 100, filed 10/02). This is docket evidence only, not proof of title.
- **Flag 23 (023):** the "$148M basis not stated" flag can be closed at SECONDARY tier.
  - REGINALD's archived STATUS (`STATUS_pre_prune_2026-02-27.md:1026`) reads "-71% from $148M (2018 purchase) | Foreclosure, Bay Area office".
  - That gives the $148M basis and property_type OFFICE.
  - The $42.25M stays basis-UNKNOWN.
- **Flag 84 (053):** the dispute is between unlike measures.
  - Will's workbook v4 gives $306M as the 2018 purchase price.
  - ML-REG-074's "~70-80%" carries no price or benchmark.
  - So 87% and ~70-80% are not competing readings of one figure.
- **Flag 19 (009), new conflict:** `AGENTS/OZK/research/threads/2026-10-28_SEVERITY_COMPS_2026_SWEEP.md:97` says BofA Plaza DTLA "sold out of foreclosure to a 601West affiliate, Jan-2026". The ledger records a 2026-06-16 receivership sale (CREFC). This is not a residual flag, but CREED should see it.
- **Flags 36 and 88, verifier inconsistency:** 019 ("100% vacant since completion") was given a stated-cause trigger, while 025 ("vacant since delivery") and 055 ("never occupied") were set to UNKNOWN on the same kind of evidence. Whatever LEASE_UP_FAILURE rule CREED adopts must apply to all three.
- **Stale line citations:** the verifier's line numbers for `AGENTS/OZK/workbook/KB.tsv` and `AGENTS/REGINALD/workbook/KB.tsv` have shifted (e.g. ML-REG-074 is now line 85, not 76; KB-OZK-094 is now line 101, not 98). The patch cites KB ids alongside line numbers.

## Proposed vocabulary edits (README, for CREED/Will to rule)

1. **`latest_status` + RECEIVERSHIP** (flag 85). Affects 054 and 151, which was forced to FORECLOSURE on 10/21 for this gap.
2. **`latest_status` FORECLOSURE split into in-process vs + FORECLOSED (completed, taker unknown)** (flag 82). Affects 050; 002 should be re-checked too.
3. **`event_type` + RECEIVER_APPOINTED** (flag 85). Affects 009, 011, 054 and 151, whose receivership events are currently typed OTHER.
4. **`trigger` + LEASE_UP_FAILURE** (flag 36), **+ EQUITY_PARTNER_EXIT** (flag 56, for 028 and 029), and **a written MATURITY_DEFAULT definition** (flag 41, which turns 020 to UNKNOWN).
5. **`property_type`: a MIXED_USE definition** (flag 27, for 014).

⚠️ Flags 36, 41 and 56 all edit README line 43, and flags 82 and 85 both edit line 45. Each row's `current_value` is the original line. Apply them one after another, or merge them into one edit per line. A fail-closed applier will reject the second edit on a line otherwise.

## CANNOT-FIX: the external primaries named (22)

| Document needed | Flags |
|---|---|
| HCAD record | 1 |
| Miami-Dade foreclosure complaint / assignment | 8, 10 |
| CMBS trust or Trepp loan record | 11 (Lafayette) |
| The 2025 Bisnow article itself (only a search listing was seen) | 24 (Gateway property type) |
| Atrium PDF pp.45-49 *(already archived in the repo, unread here)* | 12 |
| Foreclosure docket | 16 (AMA Plaza) |
| LA Superior receivership order | 19 |
| PACER petition, 8:26-bk-10925 | 33 |
| Cook County deed | 38 |
| OZK management comments / OZK desk | 40, 53 |
| Baltimore land records | 42 |
| OZK 8-K | 43 |
| Contra Costa County deed | 46 |
| Atrium p.54 / OZK Q4-24 figure | 51 |
| Trust 10-D / Trepp | 64, 65 (Aon) |
| COMM 2015-CR22 10-D | 68, 70 |
| TreppWire Hard Maturities | 74 |
| Suffolk County registry / auction notice | 80 |

The September 2026 Trepp delinquency and special-servicing PDFs (`AGENTS/WALTER/research/2026-10-16_finish/`) were searched for 043, 044 and 045 and did not help.
