# ANVIL → PROME — D-70 position-mapping follow-through, 2026-10-15

**From:** ANVIL (clerk instance spawned by prome-81; Claude Opus 5.5, Claude Code) · **Written:** 2026-10-15 ~11:1x ET (`date` 11:10:02 EDT at last verify) · **State:** `FORGE/position_management.tsv` edited on disk, NOT committed · **awaiting commit authorization**
**Touched:** `FORGE/position_management.tsv` ONLY. `FORGE/STATUS.md` NOT touched (its D-70 row still reads "UNTOUCHED"; the contract in `FORGE/DASHBOARD.md` does not require a STATUS note, so I left the mirror byte-stable. The next reconcile, or PROME, updates the D-70 row text).
**SendMessage:** not exposed to this instance ⇒ this file + final text, per contract rule 10.

## 0 · Two corrections to the brief (verified at the artifact)
1. **CMG Oct-30 $28P and KRE Nov-27 $67P rows already existed** (HEAD L33 / L32, sourced to the 10/13 transcription, hashes VALID, both rendered MAPPED before my edit). D-70's "no rows for … CMG / KRE 67P" in STATUS was wrong on those two. I refreshed both; I did not duplicate them (the loader refuses a duplicate key).
2. Brief item (c) omits **QQQ Oct-16 $725P** (the round trip), but STATUS's D-70 row names it. I added it as a CLOSED record row (precedent: L34 QQQ 750C 10/13 round trip). **Drop it if you want — it renders nowhere** (closed contracts are not holdings).

## 1 · Verification (all run after the edit)
| Check | Result |
|---|---|
| `fleet_dashboard.py --no-snapshot -o …/anvil_d70_preview.html` | rc=0; **zero "Management evidence changed/missing" lines** (before: 5). `grep -c "Management evidence"` on the HTML = 0 |
| `desk_attention.coverage()` errors | `[]` |
| Holdings mapped | **15 of 20** parsed holdings MAPPED (before: 9 of 20 + 5 withheld). Still UNMAPPED, outside this task: GLD · APD · APO $95P · RH KRE $25P · RH T (see § 4) |
| `positions_from_forge.py --selftest` | rc=0 |
| TSV shape | 39 lines × 15 fields every line; `file` = UTF-8, no CRLF (`grep -c $'\r'` = 0); header unchanged; no row deleted or re-ordered (34 → 38; 4 appended at EOF) |
| Sources | **No mapping row is sourced to `FORGE/STATUS.md` any more** ⇒ future mirror edits no longer withhold mappings by byte change. Every new hash computed from the file's bytes at edit time |
| `measure.py` | 23,364 B · 39 lines · crc32 1502308367 |
| `git diff --stat FORGE/` | `FORGE/position_management.tsv \| 32 ++++++++++++++++++--------------` (1 file, 18 insertions, 14 deletions) |

## 2 · Changes, by row (key = account / ticker / instrument / expiry)
| Row | Change | Fields changed | New source |
|---|---|---|---|
| Fidelity TLT $77P 2026-09-30 | Marked TERMINAL; pointer → rotation 10/01 chunk D (verified there: 10 @ $0.01 + 5 @ $0.02 = $18.80 ⇒ −$154.64 vs $173.44, HOLD rail retired, GATE-TERRY-007 MOOT); Activity rows 9 + 12 = the 9/30 transcription | complete_when · source · sha · checked | `FORGE/_archive/STATUS_ROTATION_2026-10-01.md` |
| Fidelity KRE $60P 2026-09-30 | TERMINAL; rotation 10/01 chunk D (sold 9/30 @ $0.01 ⇒ −$451.48, roll leg 1) | same | same |
| Fidelity WAL $70P 2026-09-18 | TERMINAL; rotation 09/27 § Ticket record (Activity row 5, EXPIRED as of 9/18, −$768.67). ⚠️ The old cell said "rows 4–5" for each; the record gives **row 5 = $70P, row 4 = $67.5P** — I wrote each row's own number | same | `FORGE/_archive/STATUS_ROTATION_2026-09-27.md` |
| Fidelity WAL $67.5P 2026-09-18 | TERMINAL; same record, row 4, −$750.67 | same | same |
| Robinhood WAL $70P 2026-12-18 | Live; source moved to the governing TERRY card (gate, manual harvest, 12/4 time stop, $4.40 GTC CANCELLED 9/28 all on the card); "not in Fidelity captures" note re-pointed at D-83. Gate ID unchanged | complete_when · source · sha · checked | `AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md` |
| Fidelity QQQ $740P 2026-10-15 | **CLOSED**: ×3 sold 10/14 net $3,474.93, DERIVED +$1,882.94, cohort +$2,022.60 incl. prior +$139.66; MGMT-QQQ740P-OCT15 SPENT; card path; TERRY booking 178377533 | review · order UNKNOWN→NOT_APPLICABLE · action · complete_when · source · sha · checked | `PROME/data/2026-10-15_broker-capture-TRANSCRIPTION.md` |
| Fidelity USO $150C 2026-10-14 | **CLOSED**: ×2 sold 10/14 net $760.68, DERIVED +$385.35; card path; TERRY 178377533 | same | same |
| Fidelity HBAN $16P 2026-10-16 | ×2 → **×1** (sale not in visible Activity, D-80); WQ-302 outcome unseen; card path added | review · **fill NOT_APPLICABLE→UNKNOWN** (a sale happened by the qty bridge but no fill row is visible) · complete_when · source · sha · checked | 10/15 transcription |
| Fidelity WAL $65P 2026-12-18 | WQ-429 RULED A (sell ×4 before Mon 10/19 print); ×4 still held, no order in Pending (D-82); card path; fills owed DOCKET L709 | **owner (wording only, see § 3)** · **approval NOT_RECORDED→APPROVED** · **fill FILLED→UNKNOWN** · review · action · complete_when · source · sha · checked | `PROME/proposals/2026-10-14_wq428-430-RULED.md` |
| Fidelity OZK $40P 2026-11-20 | WQ-428 RULED (sell ×4 before Tue 10/20 print); same pattern | same | same |
| Fidelity KRE $67P 2026-11-27 | C5 card due 2026-11-24 (DOCKET L705) as the review date; still no card | review · complete_when · source · sha · checked | `PROME/inbox/processed/2026-10-14_from-TERRY_WQ425-OZK-WAL-cards.md` |
| Fidelity CMG $28P 2026-10-30 | 10/14 sell-1 limit $0.46 VERIFIED CANCELED (not a fill); ×2 held | review · source · sha · checked | 10/15 transcription |
| Fidelity AAPL Stock | 5 → 4 (sold 1 @ $347.02, Processing); DERIVED +$323.38. **Not in your list**; changed because the contract says to reconcile the row an execution touches in the same pass | review · source · sha · checked | 10/15 transcription |
| Fidelity VLO Stock | Pointer only: HELD-01 letter at `PROME/GATES.tsv` + ruling path `PROME/proposals/2026-10-07_VLO-december-management-RULED.md` appended; source (10/13) unchanged and still valid | complete_when · checked | unchanged |
| **NEW** Fidelity QQQ $715P 2026-10-15 | Owner "Will-direct; owner UNKNOWN — no desk, no card (D-77)"; action = the standing sell-or-roll rule (`USER.md` 9/30 19:03 ET), no card/order/approval inferred; ITM handling D-60 | — | 10/15 transcription |
| **NEW** Fidelity QQQ $735C 2026-10-16 | Same shape; bought 10/14 net −$252.66 | — | 10/15 transcription |
| **NEW** Fidelity QQQ $725P 2026-10-16 | CLOSED round trip; basis/realized UNKNOWN (D-80) | — | 10/15 transcription |
| **NEW** Fidelity KRE $60P 2026-12-18 | One row covers both lots (2 + 3 M); C5 card due 2026-12-16 (DOCKET L706); owner cell copied from DOCKET L706; action blank (follow-through, not a broker task) | — | WQ-425 packet |

No threshold, gate ID, consequence or owner **assignment** was changed. No card was invented: the four Will-direct lines say "no card" explicitly.

## 3 · State changes you should check (they are judgment-adjacent)
1. **WAL 65P / OZK 40P approval → APPROVED.** Basis: Will's verbatim "Approve 428, 429 and 430" in the RULED record (10/14 21:32 ET). WQ-429 is recorded there as choice A, "until corrected". If you would rather keep NOT_RECORDED until Will's read-back is confirmed, revert that one cell.
2. **Fill FILLED → UNKNOWN on WAL 65P / OZK 40P.** The old FILLED meant the 10/7 *entry*; next to an approved SELL action it reads as "the sale filled", which the 10:10 capture contradicts (both still ×4). UNKNOWN is the honest state of the action's fill. The same ambiguity sits in older live rows (L30-era convention: USO 150C, KRE 67P and CMG kept FILLED = entry). I left KRE 67P and CMG at FILLED (no approved sale action on them). **Convention question for the contract owner (PROME):** does `fill` describe the action or the entry?
3. **Owner cell wording on WAL 65P / OZK 40P:** "TERRY management unrecorded" was false once the cards existed (24dbebe78). New wording names the same three parties (Will · TERRY card = recommendation · PROME records), in the existing pattern of the QQQ card rows. Revert if you read this as an owner change.
4. **HBAN fill NOT_APPLICABLE → UNKNOWN** (see § 2).

## 4 · Still open, with owner
| Item | Owner |
|---|---|
| CMG $28P and KRE $67P owner cells still say "TERRY construction" while STATUS D-77 says no card/owner exists. I did not change it (owner assignment) | **PROME** decides the wording |
| Unmapped holdings: GLD (20 sh, +3 unseen fill, D-80) · APD · APO $95P (a Will HOLD ruling exists, `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②, so a row could point there) · RH KRE $25P · RH T | **PROME** — outside this task; they surface as "UNRECORDED" as the contract intends |
| TBT row still says "Remaining5 retain October14 decision clock" — the clock has passed with no outcome in the capture (valid hash, so not withheld) | **PROME** / TERRY (WQ-357) |
| STATUS D-70 row text still says "UNTOUCHED … no rows for CMG / KRE 67P" | the next ANVIL reconcile, or PROME (STATUS is 418 B under the cap; a rotation comes first) |
| QQQ 715P expires today and 735C/HBAN tomorrow: the mapping states the standing rule only; the order is Will's | **Will** |

## 5 · Consumer verdict
- No structural change: header and 15-field schema unchanged (the loader refuses a schema change and did not). Consumer = `PROME/tools/desk_attention.py` `coverage()` (via `fleet_dashboard.py`): verified clean above. **No consumer sweep owed.**
- `positions_from_forge.py` does not read this file; selftest rc=0 anyway.

## 6 · Proposed commit (after your word)
```
FORGE: D-70 mapping refresh — 2 closed, HBAN x1, 4 new rows, 5 withheld evidence re-pointed

position_management.tsv only (STATUS.md untouched). Terminal TLT77P/KRE60P Sep-30 ->
rotation 10/01 chunk D; WAL 70P/67.5P Sep-18 -> rotation 09/27 ticket record (rows 5/4);
RH WAL 70P -> TERRY ROLL70 card. QQQ 740P Oct-15 and USO 150C Oct-14 CLOSED (10/14 sales).
HBAN 16P x2->x1. WAL65P/OZK40P -> WQ-428/429 RULED record, cards by path. KRE67P C5 L705.
CMG cancel, AAPL 5->4, VLO ruling path. New: QQQ 715P, 735C (no card, Will-direct),
725P round trip (closed), KRE 60P Dec-18 (C5 L706). No row sources FORGE/STATUS.md now.
fleet_dashboard preview: 0 evidence warnings (was 5); 15/20 holdings mapped.
positions_from_forge selftest rc=0. 39 lines x 15 fields, LF.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
```

**awaiting commit authorization** — on your word: `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/position_management.tsv` from the repo root, hash reported back. No push. Staying available.
