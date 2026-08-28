# Leg ⑳ BOOT-SEQUENCE AUDIT — VULCAN

Executed live (`git status --short AGENTS/VULCAN/` clean before AND after `python3 AGENTS/VULCAN/boot.py`, rc=1, no writes; boot.py only contains read-only `.open(...)` calls). Ran from repo root (cwd-proofness confirmed).

## Step table

| Step (CLAUDE.md) | Claim | Instrument | Verdict | Evidence |
|---|---|---|---|---|
| Boot-seq 1: sync | pull from GitHub | git protocol, manual | CANNOT-JUDGE (not executed, protocol step) | `AGENTS/VULCAN/CLAUDE.md:41` |
| Boot-seq 2: read SCRATCH | "where you left off" | manual Read | DELIVERS-PARTIAL — mandates a WHOLE read of a 153,247 B file, 2.82× the read cap | `CLAUDE.md:42`; `ls -la` |
| Boot-seq 3: read STATUS | "convergence matrix, live channel reads..." | manual Read | DELIVERS-PARTIAL — mandates a WHOLE read of a 117,622 B file, 2.17× cap; **and the "live channel reads" claim is false on today's file** — see Finding 1 | `CLAUDE.md:43`; `STATUS.md:35,91` |
| Boot-seq 4: run boot.py | "8 legs" | `boot.py` | DELIVERS (ran clean, rc=1, correct leg count) | live execution transcript below |
| Boot-seq 4/leg1: ledger staleness | workbook + TRADE.md vs STATUS | `scripts/ledger_staleness.py` | DELIVERS-PARTIAL — silently excludes `docket/CATALYSTS.tsv` from the scan (own printed output: *"1 TSV(s) NOT scanned by this pass: docket/CATALYSTS.tsv"*) | live output; `boot.py:385-389` |
| leg2: predictions-due | scan `PREDICTIONS.tsv` for past-trigger OPEN rows | `boot.py:predictions_due()` | DELIVERS — found VULCAN-16 due 8/27 | live output |
| leg3: S2 series age | content-vintage staleness, `asof_utc` | `boot.py:s2_series_age()` | DELIVERS — fresh 4d, correctly content-keyed not mtime | `boot.py:149-174`; live output |
| leg4: MAG7 series age | content-vintage + proximity-to-band warning | `boot.py:mag7_series_age()` | DELIVERS — fired the "inside 1pp of yellow line" warning live (32.91%) | `boot.py:177-221`; live output |
| leg5: S4 series age | month-cadence check vs TSMC filing pattern | `boot.py:s4_series_age()` | DELIVERS — correctly month-keyed, not day-keyed | `boot.py:236-266`; live output |
| leg6: catalyst countdown | "ONE reader over 4 legs," fired rows regardless of priority | `scripts/catalyst_countdown.py` | DELIVERS — surfaced 5 fired rows + 1 neighbour-tagged VIOLET row (MU FQ4 date conflict, own register says ~9/22, VIOLET's says ~9/29 "ESTIMATED, NOT CONFIRMED") on this exact run; vintage correctly git-commit-keyed (`_git_commit_date`, NOT mtime — confirms it did NOT re-port OTTO's mtime bug) | `catalyst_countdown.py:94-119`; live output |
| leg7: workbook schema + score reconcile | "VX.tsv vs STATUS matrix vs STATUS composite arithmetic" | `validate_workbook.py:score_reconcile()` | DELIVERS but SCOPE-LIMITED — reconciles only the 1–5 **numeric score**, symmetric 3-way comparison (no one-directional bias). It does **not** read `THESIS.md` at all — see Finding 2 | `validate_workbook.py:161-222`; live output "10 ledgers clean; VX/STATUS/composite scores reconcile" |
| leg8: EDGAR sweep | S3/S5 filing sweep + open filing windows, offline | `boot.py:edgar_sweep()` | DELIVERS — fresh 1d, 5001 rows, window logic ran without error | `boot.py:301-375`; live output |
| Boot-seq 5: read leg6 output | "ONLY surfacing mechanism for dated commitments" | manual | DELIVERS on this run (5 fired rows genuinely printed) | live output |
| Boot-seq 6: resolve predictions | mark HIT/MISS/FALSIFIED | manual, informed by leg2 | DELIVERS (leg2 supplies the due list; resolution itself is a human/session act, CANNOT-JUDGE beyond that) | — |
| Boot-seq 7: process inbox | integrate signals | manual | CANNOT-JUDGE (not exercised this audit; inbox has live subfolders) | `ls AGENTS/VULCAN/inbox/` |
| Boot-seq 8: channel-liveness check (S1-S5) | "gap to close" if no current dated live read | **manual only — NOT in `boot.py`** | SILENT-BY-CONSTRUCTION — no automated leg implements this at all; relies entirely on eyeballing STATUS.md's "LIVE CHANNEL READS" section, which STATUS.md's own current text documents as having rotted for days undetected (Finding 1) | `CLAUDE.md:48`; no matching function in `boot.py` |
| Boot-seq 9: execute task | — | — | N/A | — |

## Live execution transcript (abridged; full stdout captured, rc=1, no exceptions, no writes)

```
--- 1. ledger staleness --- : quiet; NOTE "1 TSV(s) NOT scanned by this pass: docket/CATALYSTS.tsv"
--- 2. predictions-due --- : DUE: VULCAN-16 due 2026-08-27
--- 3. S2 series --- : fresh (4d, 5 rows, last 2026-08-24)
--- 4. MAG7 series --- : fresh (2d); ⚠️ 32.91% inside 1pp of 33% yellow line
--- 5. S4 series --- : current (20 rows, latest Jul 2026, cum YoY 37.0%, band no-stress)
--- 6. catalyst countdown --- : 5 RECENTLY FIRED rows (2 NVDA earnings/filing tripwires,
      1 PROME-DOCKET mirror, VULCAN-16 catalyst + prediction) + 1 neighbour-tagged VIOLET
      row (MU FQ4 date discrepancy, +32d) + 17 upcoming rows
--- 7. workbook schema --- : ✓ 10 ledgers clean; VX/STATUS/composite scores reconcile;
      NOTE: S2_SERIES.tsv 8 ERR: sentinels (reported, not hidden)
--- 8. EDGAR sweep --- : fresh (1d, 5001 rows, last swept 2026-08-27)
VULCAN boot: REVIEW — stale ledger or prediction due.  RC=1
```
Post-run `git status --short AGENTS/VULCAN/` — clean (no PAT-054 self-mutation).

## Three most consequential findings

1. **The one automated channel-liveness surrogate (leg 7's score reconcile) checks only the NUMBER, never the PROSE it sits beside — and STATUS.md's own current text proves the gap is live, not theoretical.** `score_reconcile()` (`validate_workbook.py:161-222`) parses `VX.tsv` scores, the STATUS matrix's bold score cells, and the composite arithmetic line, and errors on any numeric disagreement — a genuinely well-built, symmetric 3-way check (confirmed DELIVERS live: "VX/STATUS/composite scores reconcile"). But boot step 8 ("channel-liveness check... is there a current, dated live read?" `CLAUDE.md:48`) is never implemented as a script at all — no leg reads `## LIVE CHANNEL READS` for freshness. `STATUS.md:35` — VULCAN's own text, written this week — states: *"`## LIVE CHANNEL READS` IS NO LONGER A LIVE READ. It has accreted into a historical log with fresh findings appended as sub-bullets, while several TOP-LEVEL bullets still state superseded positions in the present tense... S2's physical-leg bullet led with 'still positive… Spot rising' as of 8/3 — 24 days old and now the wrong sign."* This rotted silently through multiple sessions where the numeric score reconcile passed clean every time, because the score number and the prose under it are independently maintained and only one is machine-checked. Boot step 8 is SILENT-BY-CONSTRUCTION for exactly the failure mode it names.

2. **No boot leg — automated or manual-mandated — ever reads `THESIS.md`, despite the SPAWNED-MODE BOOT CARD (`CLAUDE.md:16`) explicitly ordering a fresh spawn to read it third, right after STATUS.md.** `score_reconcile()` opens only `STATUS.md` and `VX.tsv` (`validate_workbook.py:184,191`) — THESIS.md never enters any boot-time comparison. This is the closeout-side problem's mirror image: `CLAUDE.md:58` documents that THESIS sat "18 days stale and asserting the OPPOSITE of STATUS on S3" and was undetectable because THESIS "was in neither the boot nor the closeout loop" — but note the fix applied (closeout step 2b, added 2026-08-21) only closes the **write**-time gap; it does nothing for the **read**-time gap this audit is chartered to test. A spawned reader who follows the boot card literally and reads THESIS.md today has no automated signal telling them whether that file currently agrees with STATUS — they must catch a contradiction by eye, the same failure mode item 1 above already shows rotting silently. Also notable: the two boot descriptions in `CLAUDE.md` disagree — the numbered "BOOT SEQUENCE (when spawned)" list (lines 39-49) never mentions THESIS.md at all, while the SPAWNED-MODE BOOT CARD (lines 13-21) puts it third in the read order. Neither list is wrong per se, but a reader consulting only the numbered sequence never learns THESIS exists at boot.

3. **`docket/CATALYSTS.tsv` — the "source of truth" register that closeout step 2c requires reconciling every session (`CLAUDE.md:59`) — is explicitly excluded from boot's own staleness alarm.** Leg 1's live output states: *"1 TSV(s) NOT scanned by this pass: docket/CATALYSTS.tsv"* (confirmed live, not inferred). Leg 6 (catalyst_countdown) does read its content every boot, but it has no staleness check of its own — it only flags rows as fired/upcoming based on what's IN the file; if a session forgets to add a newly-incurred dated commitment (the exact failure `CLAUDE.md:60` was written to prevent), no boot leg would notice the register itself has gone stale, only that whatever content happens to be there produced no fired rows. This is a SILENT gap on the file `CLAUDE.md` calls the highest-priority surfacing mechanism for non-market dated commitments.

## Read-cap leg

| File | Boot mandates whole read? | Bytes | Verdict |
|---|---|---|---|
| `SCRATCH.md` | YES — boot-seq step 2, "the single most important 'pick up here'" | 153,247 B | **OVER-CAP** (2.82× the 54,250 B cap) |
| `STATUS.md` | YES — boot-seq step 3, and spawned-mode card step 2 | 117,622 B | **OVER-CAP** (2.17×). Note: 205 lines — passes its own `<250 lines` convention in the FILES table while failing the byte cap by 2.17×; density (~574 B/line), not line count, is the actual constraint (same class as DAEDALUS's own re-derivation of the byte budget from a stale density constant) |
| `THESIS.md` | YES — SPAWNED-MODE BOOT CARD only (not the numbered boot sequence — see Finding 2) | 55,457 B | **OVER-CAP** (1.02×, just over the line) |
| `CLAUDE.md` (this file, auto-loaded every boot) | Implicitly — it IS the boot instructions and auto-loads | 55,864 B | **OVER-CAP** (1.03×) — the boot-loaded charter itself cannot be read whole |
| `NEXUS_BRIEF.md` | Not boot-mandated (closeout writeback target) | 92,838 B | OVER-CAP but not a boot-read claim |
| `LESSONS.md` | Not boot-mandated | 43,273 B | NEAR-CAP |

Every file the boot sequence or spawned-mode card mandates reading whole is over the 54,250 B cap. This is the same class DAEDALUS's own charter documents for `FLEET_MAP.tsv`/`STATUS.md` (PAT-111) — nothing here is unique to VULCAN's design, but VULCAN has not applied the fix (rotation/near-cap monitoring) that DAEDALUS's own `read_cap_check.py` pattern represents.

## Q6: does boot invoke `scripts/corrections_boot_check.py`?

**NO.** Confirmed by direct grep of `AGENTS/VULCAN/boot.py` and `AGENTS/VULCAN/CLAUDE.md` — zero references to `corrections_boot_check`. The script exists at repo root (`scripts/corrections_boot_check.py`, confirmed present) but VULCAN's boot sequence never names or calls it, unlike DAEDALUS's own SPAWN PROTOCOL step 5b which does.

## What this audit could NOT see

- Whether a live spawned session actually reads THESIS.md/SCRATCH.md/STATUS.md in full given their over-cap size, or silently truncates/samples — that is a harness-behavior question outside static trace + boot execution.
- `inbox/` processing (step 7) and prediction resolution (step 6) were not exercised — no signal was live-processed this run.
- Whether the "channel-liveness check" (step 8) is in practice caught by a human/session reading the matrix table rather than the rotted prose section — STATUS.md's own text says it WAS eventually caught, just not by any boot mechanism, and only after "the second read... the one Will asked for."
- Full content of all 10 workbook ledgers was not manually cross-checked against `validate_workbook.py`'s SCHEMA.tsv row-by-row; relied on the tool's own live clean verdict.
