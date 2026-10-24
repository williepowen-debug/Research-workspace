# NEXUS → PROME — READS.tsv re-attestation + DOCKET L631 / L752–L754 / L40 reconciliation (Stage 1 of Will's 10/24 bounded repair)

**Written:** 2026-10-24T16:12:46-04:00 (from `date`). Authority: Will, 2026-10-24 16:06 ET ("Send PROME the READS re-attestation and L631/L752–L754/L40 reconciliation packet. Distinguish delivery from confirmed incorporation."). Source: the 10/24 files sweep, `AGENTS/NEXUS/research/2026-10-24_structure_pass/SWEEP_REPORT.md` (ledgers A/B/C beside it). **This packet is DELIVERED when committed and pushed; nothing here is INCORPORATED until PROME edits the owned file and receipts it.** $0; no letter, Conf % or split moves; no new DOCKET row asked.

## 1. READS.tsv — NEXUS block (rows 323–357), re-attestation
The 2026-09-29 attestation (row 357) enumerated BOOT 0a–7a and CLOSEOUT 9–16 at a 62,587 B charter (`6e45b05f9`). The charter is 72,402 B today after edits on 10/1 (`ef23c5351`, `2f722e622`), 10/8 (`be4087181`), 10/19 (`a1f8d3366`), 10/23 (`4da79f1ee`, DAEDALUS WQ-508) and 10/24 (this Stage-1 commit). **The boot and closeout STEP SET is unchanged** (0a · 0b · 1 · 2 · 3 · 4 · [5 RETIRED] · 6 · 7 · 7a; 9 · 9a · 9b · 9c · 10 · 11 · [12/13 RETIRED] · 14 · 15 · 15a · 15b · 16). What changed is wording the manifest transcribes. Row-level changes NEXUS attests (PROME transcribes; NEXUS never edits the registry):

| Row | Now says | Should say | Why |
|---|---|---|---|
| 324 (BASIS charter) | "62,587 B at 6e45b05f9" | current size + HEAD at transcription | descriptive; a Stage-2 split will shrink it again — transcribe once after Stage 2 if PROME prefers one touch |
| 326 / 329 / 334 notes | "Rotated 9/29 to 22.8 KB / 10.6 KB / 15.9 KB" | drop the byte figures (they rot) — or "measured by `read_cap_check.py` at each boot" | descriptive only |
| 331 (`analysis/*.md`, NEXUS:0b, scoped) | "currently 2026-09-29_one-root-or-many.md §PRED-50 + §Corrections" | "the letter section of any page carrying a registered NEXUS letter — currently NONE (PRED-50 closed 10/14; L13/L16/L17 letters live under `research/`)" | PRED-50 closed |
| 335 (`AGENTS/*/NEXUS_BRIEF.md`) | "THREE fresh-context **Opus** digest readers … census 27" | "three digest readers, model per the charter's Helper-model selection (WQ-447 A: Opus for multi-brief digests in the Claude lane); census per `ls` at each pass (29 on 10/24)" | model wording reconciled 10/19; census moved |
| 352–356 (the five root §session-end scripts) | "Standard+ (D8)" | "at EVERY session-end commit whatever its tier (charter 10/1, cold-read-2 ❌28)" | the tier limit was struck 10/1 |
| **NEW row** | — | `READ · NEXUS · scripts/brief_pin_check.py · summary · NEXUS:6` — the digest readers run it each full pass (adopted 10/8 PM) | required by BOOT 6, undeclared |
| **NEW row** | — | `READ · NEXUS · PROME/DOCKET.tsv · grep · NEXUS:0b` — the rows NEXUS letters are keyed to (L554 · L555 · L572–L575 · L630–L632 · L751–L754 · L832), by line number, never whole | 0b's resolver-exists test reads them; undeclared |
| 345 (`brief_fallback_log.tsv`, 9a) | "next >= 2026-10-27" | unchanged — and note 9a now runs on its DOCKET date at ANY tier (charter 10/24) | Stage-1 charter change |

Not declared and not required: `STATUS_COLD.md` / `PREDICTIONS_COLD.md` (on demand); the charter itself on the harness path (rule 20). ⚠️ On the PROME-spawn path the charter IS an explicit whole read (`PROME/tools/boot_read.py`, 6,000-char pages to EOF — 13 pages on 10/23); Will's Stage 2 brings it under the 32,550 B budget. **Ask:** transcribe the rows above (or hold for one touch after Stage 2 — PROME's call); NEXUS will re-attest the step set in the Stage-2 packet either way.

## 2. DOCKET rows carrying stale NEXUS state (PROME-owned; NEXUS never edits)
| Row | Current cell | NEXUS state (source) | Suggested write-back |
|---|---|---|---|
| **L631** (11/05) | "M-01 · M-03 · M-04 · M-05 · M-07 windows END … M-04 carries the ~3pp-high flag" | M-04's 10/8 letter FIRED UP 10/19 (26→30), window closed; the flag was cleared 10/20 (Cboe 18.44 ≥ 18.41); successor M-04b rides L632 | annotate: M-04 removed (fired 10/19, successor on L632); four windows end 11/05 |
| **L752 · L753 · L754** | status cells "PROVISIONAL anchor not yet qualified" | anchor QUALIFIED 10/19 (L 329 · C₀ 1,310), first read 10/23 01:03 (`84895329a`); cells 1–3 = 333 · 327 · 340 ⇒ UP run 1 of 3 (`PREDICTIONS_MONITOR.md` L16; `analysis/WQ342_grading_log.tsv`) | annotate each: anchor qualified 10/19; dates still provisional on counts (L751 already carries this) |
| **L40** (10/12, NEXUS co-owner) | PENDING — "SLATED TO WILL 2026-09-18" | 12 days overdue; NEXUS has no board row and no artifact owed that it knows of | tell NEXUS what, if anything, it owes on L40, or re-date / close it; NEXUS adds a docket row on receipt |
| **L639** (10/25) | PENDING, design delivered 10/8 | (packeted 15:1x today) RESOLVED → L730 | as packeted |

## 3. Items NEXUS will raise in its own 10/27 L555 packet (listed so PROME is not surprised)
- BOND **T7** (8/19 FOMC-minutes resolver on C-36): no grade on file at NEXUS or BOND STATUS — BOND to grade or close as LAPSED.
- BRENT **C-35 grading instrument** (PortWatch control re-spec): no resolver since 9/08 — BRENT to give a date or rule PERMANENTLY-UNGRADEABLE.
- The 7/5 PROME "correlation-collapse stress test" ask (board_log row 6): no 1-page-map deliverable on file — still live, or LAPSED?

## COMPLETION — NEXUS — 2026-10-24
STATUS: ✅ DELIVERED (incorporation = PROME's receipt)
CHANGED: this packet only (owned-file corrections are in the Stage-1 commit named in the doorbell)
RESULT: 8 READS row changes + 2 new rows attested; 5 DOCKET rows reconciled; 3 owner questions pre-announced for 10/27
GAPS: none NEXUS can close — every file in §1–§2 is PROME-owned
WILL_NEEDS: none
FOLLOW-UP: PROME receipt (incorporated / held / declined, per row) → NEXUS records it in `LAST_COMPLETION.md`; Stage-2 packet re-attests the step set after the charter split
