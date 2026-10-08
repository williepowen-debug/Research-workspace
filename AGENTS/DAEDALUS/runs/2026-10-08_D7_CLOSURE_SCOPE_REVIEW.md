# D7 — `corrections_boot_check.py --closure` scope and acceptance review (DAEDALUS, 2026-10-08 15:06 EDT from `date`)

**Owed:** the scope review missed on 10/05 (STATUS carried list). **Authority:** Will APPROVED D7 at the 9/17 P4 sitting, "sequenced AFTER D3+D4" (`runs/2026-09-17_P4_SITTING_RULING_PACKAGE.md` l.19); contract §5 (l.156–171), fixtures §4 D9 + §6. D3 and D4 are both ruled, so the build is unblocked on paper. **This review asks one question: would the contract, built today, produce a useful verdict on the live register?**

## 1. Rulings since 9/17 the contract must absorb

| Ruling | Effect on D7 |
|---|---|
| WQ-254 D4(a), 9/24 | A passed cap/DEAD-AT-CAP never discharges a named target. Leg 3 ("latest receipt per agent,id") must treat DEAD-AT-CAP as status only. No contract change; add a fixture. |
| WQ-286 ④, 10/02 | RETIRED named rows still need a receipt. Leg 3 must not skip RETIRED. Add a fixture. |
| WQ-393, 10/08 (today) | Rows are written at publish; `targets` = corrected ∪ correcting recipients; `--write-compliance` exists. D7 can trust row existence and target sets from 10/08 forward. Older rows may still carry short targets: `--write-compliance --since` finds them. |

## 2. Gating finding — legs 4, 4b and 6 have almost no input to read

Measured 2026-10-08 15:06 EDT over all 30 receipt files (`AGENTS/*/registry/corrections_receipts.tsv` + PROME's), 108 rows:

| Field the contract reads | Rows carrying it | Ruled |
|---|---:|---|
| `artifact=` (legs 4, 4b) | **5 of 108**; post-9/17 APPLIED: **1 of 23** | D3, 9/17 |
| `scope=` (leg 4, NO-OP) | 5 of 108 | D3, 9/17 |
| `validation_ref` (leg 6) | **0 of 108** | D2, 9/17 |
| `review=` (leg 3, DEFERRED) | 0 of 2 DEFERRED | contract §5 |

**Cause (read at code):** `cmd_receipt` in `scripts/corrections_boot_check.py` writes `receipt_date · correction_id · action · note` and takes only `--action` and a free `--note`. It never asks for `artifact=`, `scope=` or `validation_ref`. The ruled fields have no write path except remembering to type them into prose. This is the same adoption failure L210 found in the register's write leg (fixed today by WQ-393), one hop downstream.

**Consequence:** built to contract today, `--closure` returns **1 OPEN on essentially every row** (leg 6 absent ⇒ OPEN; leg 4 post-word APPLIED without `artifact=` ⇒ OPEN). A tool that flags everything ranks nothing. That is not a defect in the contract. The contract is right, and its inputs were never produced.

## 3. Recommendation — fix the writer first, then build D7

| Step | What | Owner | Gate |
|---|---|---|---|
| ① | `--receipt` gains `--artifact <path#key>`, `--scope <text>`, `--validation-ref <path#key\|NONE>`. **APPLIED requires `--artifact` and `--validation-ref`; NO-OP requires `--scope`; DEFERRED requires `--review YYYY-MM-DD`.** A missing field is rc 2 with the remedy printed, and nothing is written. The values are stored as `key=value` tokens in `note`; no new column, the receipt header is unchanged. | DAEDALUS (`scripts/` grant) | **Behaviour change on a fleet boot tool: every desk's receipt command changes. Will-visible batch, not autonomous.** |
| ② | Selftest legs for ①: each action missing its field ⇒ rc 2, file unchanged. Each complete ⇒ row written with the tokens. Old 4-field rows still parse. | DAEDALUS | with ① |
| ③ | Existing 108 rows: no backfill. D7 prints them as `PRE-WORD` (contract §5 leg 4 already has this class). | — | none |
| ④ | Build `--closure` to the 9/17 contract, plus the D4(a)/WQ-286 fixtures above, plus a `PRE-WORD` count line, then an independent reader with its own counterexamples. | DAEDALUS | approved (D7) |
| ⑤ | WALTER's prune consumes `--closure` output (contract sequence). | WALTER | after ④ |

**Not done here:** ① and ④ are not built. ① is held for Will's word because it changes what every desk types. The 9/17 contract text is not edited; this review is its scope record.
