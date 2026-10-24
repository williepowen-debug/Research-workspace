# Fire-time flags at the 2026-10-23 22:2x ET boot (prome-06 fresh context, laptop) — dispositions

Run: `prome_gate.py boot` inside `boot_session.py --run-dir /tmp/prome-boot-20261023-222622-fable` (gate 22:26 ET); log `checks/04-firetime-owner-routed-flags-persist-.txt`. Delta against `PROME/state/firetime_dispositioned.tsv` = 45 flags: 2 NEW · 43 persisting (dispositioned at the 10/21, 10/22 and 10/23 evening records) · 1 baseline row no longer reported.

| Flag | Disposition |
|---|---|
| NEW DATE DRIFT `PROME/WILL_QUEUE.md` — "Jan-15" (2027-01-15), row 513 | DONE (verified at the artifact, full logic re-read of the row): "HYG Jan-15 77/74P ×4" names the OPTION EXPIRY of the approved NOT-FIRED card, not an obligation date. 2027-01-15 is the third Friday of January 2027 (standard monthly expiry; `date` arithmetic), and TERRY's card writes it in full as "HYG Jan-15-2027" (`AGENTS/TERRY/setups/CREDIT_hyg-jan15-77-74P_or_htgc-16P_REG-T-04_2026-10-23.md` line 35). No docket row is implied: the card's registered window end is DOCKET L830 (11/13), its own time stop is Fri 2027-01-08 on the card, and Will manages his own expiries (`USER.md` § No expiry nagging). The checker's nearest row (MAKHIJANI trial 1/15/2027) is a coincidence of date, not a reference. Row text unchanged. |
| NEW DATE DRIFT `PROME/proposals/2026-10-23_wq513-516-RULED.md` — "Jan-15" (2027-01-15) | DONE: the same expiry in the ruling record's verbatim approval text (leg (a)); a ruling record is a frozen letter and is not edited. Same verification as above. |
| 1 baseline row no longer reported | DONE: pruned with `firetime_delta.py --prune` (its disposition is "done: pruned"). |

Accepted into the baseline with `firetime_delta.py --accept --pointer` this record; `PROME/state/firetime_dispositioned.tsv` committed in the same boot commit.
