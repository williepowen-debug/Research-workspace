# Fire-time flags at the 2026-10-24 Saturday boot (prome-06 fresh context, first spawn of the day) — dispositions

Record written 2026-10-24 14:35 ET. Run: `prome_gate.py boot` inside `boot_session.py --run-dir /tmp/prome-boot-1024pm` (gate 14:32 ET; the `NOW:` hook read 14:31 ET at the prompt); log `checks/04-firetime-owner-routed-flags-persist-.txt`. Delta against `PROME/state/firetime_dispositioned.tsv` = 58 flags: 13 NEW · 45 persisting (dispositioned at the 10/21, 10/22 and the two 10/23 records) · 0 baseline rows no longer reported. All three flagged artifacts last changed in one desk commit of 2026-10-21 (`git log -1 -- <path>`); the window moved onto them, nothing was edited since.

Every NEW flag below was read at the artifact with its full line logic (WQ-467 C4), never by find-replace. None required an edit; no file outside PROME is touched.

| Flag | Disposition |
|---|---|
| NEW DATE DRIFT `AGENTS/AEOLUS/STATUS.md` — "1/6" (2027-01-06), line 23 | DONE: not a date. The line reads "moved 10/10→10/21: 0 · fired 1/6" — ONE of SIX composite cells FIRED (C5), beside the conservation sum "2+2+2+2+5+4 = 17". A fraction, not January 6. |
| NEW DATE DRIFT `AGENTS/AEOLUS/STATUS.md` — "1/5" (2027-01-05), line 30 | DONE: not a date. "domain conviction 1/5 (no hardening)" is a one-to-five conviction score on the RNR vehicle trigger. |
| NEW DATE DRIFT `AGENTS/AEOLUS/STATUS.md` — "2027-01-01", line 50 | DONE: a genuine forward date, Will-ruled. The milestone band (re-keyed 10/10, KB-205) sets RED = Lower Basin agreement unexecuted at 2027-01-01 (§5.3.A.3); Yellow from 11/02, Orange from 12/02 are derived from it. The band is the desk's letter; no drift. |
| NEW DATE DRIFT `AGENTS/AEOLUS/STATUS.md` — "Dec 30" (2026-12-30), line 85 | DONE: a genuine window date. C3 WINTER (Will-ruled 10/10) grades trailing-30-day HDD in windows ending Dec 30–Feb 28; "NOT FIRED (window opens 12/30)" is the correct state for October. |
| NEW DATE DRIFT `AGENTS/AEOLUS/STATUS.md` — "1/15" (2027-01-15), line 102 | DONE: a genuine resolver date. AEO-03 (Jan-1-27 reinsurance soft, ROL ≤ +5%) resolves 1/15/27 on the Guy Carpenter US property-cat ROL index named 10/9 (KB-188). A prediction's resolve date, not an obligation PROME tracks. |
| NEW DEAD POINTER `AGENTS/OZK/reports/2026-10-21_self-sweep.md` — `reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md` | DONE: the sweep's own finding, not a defect of the sweep. Row 24 of the sweep REPORTS these two bare-relative REGINALD paths in OZK's 9/27 threads as BROKEN and names the fix ("Prefix `AGENTS/REGINALD/`; both targets exist"). Verified: both targets exist under `AGENTS/REGINALD/reports/` (ls, 17,992 B and 26,805 B). The flag fires on the record of a defect that OZK already owns at its thread files; nothing for PROME to route. |
| NEW DEAD POINTER `AGENTS/OZK/reports/2026-10-21_self-sweep.md` — `reports/2026-09-26_CRE_top3_loss_bridge.md` | DONE: same row 24, same verification as above. |
| NEW DATE DRIFT `AGENTS/OZK/reports/2026-10-21_self-sweep.md` — "Jan 16" (2027-01-16), rows 2 and 35 | DONE: a genuine window end. OZK-02/03/04 and OZK-09 resolve at the Q4 print (~Jan 16–20 2027); the sweep says "none past their resolve date". Correct. |
| NEW DEAD POINTER `AGENTS/YURI/research/2026-10-21_L432-read-and-actor-update.md` — `docs/news` | DONE: not a repository pointer. Line 18 reads "pravo government block p1–2 + government.ru docs/news" — a government.ru site section in the sources table (HTTP 200 ×4). |
| NEW DEAD POINTER `AGENTS/YURI/research/2026-10-21_L432-read-and-actor-update.md` — `longsearch/pravo-queries.json` | DONE: resolves relative to the read's source folder: `AGENTS/YURI/sources/2026-10-21/longsearch/pravo-queries.json` exists (with its `pravo-queries-wholeword.json` sibling). The text names the void stem-query batch by its file; a desk-relative citation form, target present. |
| NEW DATE DRIFT `AGENTS/YURI/research/2026-10-21_L432-read-and-actor-update.md` — "1/1" (2027-01-01), lines 29–31 | DONE: not a date. The column is pages read of the act: "1/1" = page 1 of 1 (acts №744, №733, №732 read whole). |
| NEW DATE DRIFT same file — "1/2" (2027-01-02), line 32 | DONE: page 1 of 2 (act №751, "p.2 unread: implementation-within-headcount clause"). |
| NEW DATE DRIFT same file — "1/3" (2027-01-03), line 33 | DONE: page 1 of 3 (act №749, "pp.2–3 unread: remaining names"). |

Pattern note for the checker's owner (DAEDALUS, L768 lane — an observation, not a change): twelve of the thirteen are "N/M" fractions (scores, cell counts, pages read) or desk-ruled forward dates; the thirteenth is a URL path fragment. None was drift. No allowlist row is added here: the allowlist is expiry-dated for benign CLASSES and these are per-line readings; the baseline accept carries them.

Accepted into the baseline with `firetime_delta.py --accept --pointer` this record; `PROME/state/firetime_dispositioned.tsv` committed in the same boot commit.
