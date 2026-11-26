# CARL charter history (moved verbatim from `AGENTS/CARL/CLAUDE.md`)

**Moved:** 2026-11-26 by CARL on Will's word in-session (*"Yes, move history (Recommended)"*, answering whether CARL may move incident history out of its charter verbatim with pointers; PROME C4 class, prome-80). Each span below is the exact text that stood at the pointer `*(→ archive/CHARTER_HISTORY.md Hn)*`; no rule sentence was moved without being kept in the charter. Where a span contained an instruction, that instruction was left in the charter verbatim (marked KEPT IN CHARTER). Before-copy crc32 2591414096 (49,254 B). Clarifying text added beside H4, H5 and H19 after a fresh reader's check (no rule lost; three spots read badly without context); that text is new or restored wording, recorded as KEPT IN CHARTER.

## H1 — SPAWN step 5 (BOARD diff)

Verbatim span:

```text
 *(Paths anchored 2026-07-01 — the old pair mixed root-relative `BOARD/` with CARL-relative `board/`, so it resolved from NO single cwd.)*
```

## H2 — SPAWN step 5b.1

Verbatim span:

```text
 ⚠️ **Stated explicitly because the first wording of this step read as a whole-file Read and put an 11,772 B ledger onto the measured boot path — which would have made a rotation that CUT 11,746 B from STATUS look like a net saving while the boot-read TOTAL barely moved.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
```

## H3 — SPAWN step 5b.2

Verbatim span:

```text
 *(Installed 2026-09-11, KB-CARL-450. Why: WALTER `SIG-W-20260812-006` arrived 8/12 and was filed `INFO_ONLY` on 8/15. CARL's own disposition note said the series slope was "FLATTENING" and cited corroboration — then wrote "CRL-10 UNCHANGED at 62%." The same signal carried the Oct-2025 missing-denominator caveat that is exactly CRL-10's resolvability defect. **Neither reached the row, and CRL-10 was cut 62→8 on 9/11 using the argument that had been sitting in my own note for 27 days.** `INFO_ONLY` means recorded-and-not-acted-on BY DEFINITION, so routing a resolvability hazard there guarantees the outcome — the rubric asked what the signal IS and never whether it touches a REGISTERED INSTRUMENT.)*
```

## H4 — SPAWN step 5b path note

KEPT IN CHARTER beside the pointer: CARL's v0.1 ledger lives one directory down, at `board/BOARD_LOG.tsv`; WALTER's telemetry cannot see it.

Verbatim span:

```text
 CARL's 760-row v0.1 ledger lives one directory down, so for ~3 months CARL read to WALTER's telemetry as a desk that *"keeps no board_log"* and *"cannot be tested at all."* **The work was recorded; the record sat at an address the instrument does not visit.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
```

## H5 — SPAWN step 7.0 (pipe)

KEPT IN CHARTER beside the pointer: The orchestrator has per-script timeouts and cannot hang. Redirect to a file and read that: `... boot.py > /tmp/boot.txt 2>&1`.

Verbatim span:

```text
 *(2026-09-11: CARL ran `boot.py | tail -120`, saw 0 bytes after 12 minutes, declared it HUNG, and reported a two-session failure pattern to Will. It was not hung — unpiped it runs in **25.0s, exit 0, all 7 scripts OK**, slowest 11.0s. The 12-minute run was real and is consistent with FRED latency putting several scripts near their 90s per-script timeouts — which is also what the 9/10 note describes — but the **orchestrator has per-script timeouts and cannot hang.** Redirect to a file and read that: `... boot.py > /tmp/boot.txt 2>&1`. `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — the zero bytes were a property of the PIPELINE, not the program.)*
```

## H7 — SPAWN step 7.0 (wiring)

Verbatim span:

```text
 *(Wired 2026-07-10 per DAEDALUS S3 finding — resolves the consumer_pulse-into-boot thread.)*
```

## H8 — SPAWN step 7c

Verbatim span:

```text
 *(`$10` = Notes explicitly — `$NF` broke when the `Instrument` column was appended 7/24 and silently printed the wrong column; caught 7/31.)*
```

## H9 — SPAWN step 7d

Verbatim span:

```text
 *(Wired 2026-06-27; ABS_BASELINE flagged — CARL already FROZE 5 others, good hygiene. Invocation cwd-proofed 2026-07-01 — the bare root-relative form failed from an own-dir launch cwd.)*
```

## H10 — SPAWN step 7e

Verbatim span:

```text
 *(Wired 2026-08-28, DAEDALUS wiring sweep leg ①, batch Will-approved in-session.)*
```

## H11 — CLOSEOUT step 12

KEPT IN CHARTER beside the pointer: Standard = `MESSAGING/CROSS_SESSION_MESSAGING.md` §2 rule 4 + root `CLAUDE.md` 'never route signals around WALTER'.

Verbatim span:

```text
 *(HERMES retired 2026-06-30; the fleet-wide replacement sentence written then said 'deliver directly' without reconciling WALTER's signal mandate — one template change propagated to ~20 desks, so it read as canon everywhere and as a defect nowhere. Corrected 2026-09-02 on DAEDALUS's fleet census; standard = `MESSAGING/CROSS_SESSION_MESSAGING.md` §2 rule 4 + root `CLAUDE.md` 'never route signals around WALTER'.)*
```

## H12 — CLOSEOUT step 14b

Verbatim span:

```text
 (The fleet's dominant content-stale mechanism is a brief written mid-session while STATUS work continues — refreshing isn't the fix, ordering is.)
```

## H13 — CLOSEOUT step 15 (Check G)

Verbatim span:

```text
 *(G exists because the Brier audit found reading the failure taxonomy at BOOT demonstrably did not stop CRL-24 — the check has to live at registration.)*
```

## H14 — CLOSEOUT step 15 (Checks D, E)

KEPT IN CHARTER beside the pointer: Spec + acceptance test: `scripts/CONSISTENCY_CHECK_SPEC.md` §Phase 4.

Verbatim span:

```text
 *(D and E added 2026-07-24 after two coherence bugs that no single-file review could catch: a downgrade armed against an instrument that doesn't publish the series, and POP-P06 >5% at 50% vs CRL-15 >6.5% at 65%. Spec + acceptance test: `scripts/CONSISTENCY_CHECK_SPEC.md` §Phase 4.)*
```

## H15 — MESSAGING inbox count

Verbatim span:

```text
 *(2026-09-02: boot reported "inbox at 1" and SCRATCH had claimed "INBOX AT ZERO" on 9/1 — both measured on `inbox/*.md` while `inbox/WALTER/` held two PRIORITY signals. Both had in fact been consumed via the BOARD route on 8/15; what was wrong was the COUNT, not the work. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.)*
```

## H16 — FILES table, outbox row

Verbatim span:

```text
 *(Corrected 2026-09-02 — this FILES row carried the retired HERMES 'signals go directly' wording; a table row is where a correction lands last, `[[finding_summary_section_merges_what_the_body_separates]]`.)*
```

## H17 — Doc Ownership, mirror pairs

Verbatim span:

```text
 *(Claim corrected 7/31 — PROME audit found the prior wording asserted machine coverage that does not exist.)*
```

## H18 — WORKBOOK DISCIPLINE

Verbatim span:

```text
 Item #2d (May 2 2026): only 7 of 22 cluster-matched SUPERSEDED candidates actually carried forward the load-bearing content; 14 were downgraded to STALE on verification.
```

## H19 — SPAWN step 7.0 (consistency_check at boot)

KEPT IN CHARTER beside the pointer: boot.py runs consistency_check with `--quiet --warn-only`, surfacing mirror drift, undeclared instruments and cross-ledger monotonicity violations at boot. `--warn-only` exits 0 so a finding renders as a FINDING, not a script FAILURE; a 🔴-prefixed summary line survives collapsed mode. **Closeout runs it WITHOUT `--warn-only`, where exit 1 is the gate.**

Verbatim span:

```text
 *(consistency_check wired in 2026-07-24 with `--quiet --warn-only`: it surfaces mirror drift, undeclared instruments and cross-ledger monotonicity violations **at boot** rather than only at closeout — the two 7/24 coherence bugs were live for hours before anything looked at them. `--warn-only` exits 0 so a finding renders as a FINDING, not a script FAILURE; a 🔴-prefixed summary line survives collapsed mode. **Closeout runs it WITHOUT `--warn-only`, where exit 1 is the gate.**)*
```

## H20 — FILES table, TRADE.md row

KEPT IN CHARTER beside the pointer: The path named here was DELETED by `1cb18fbc3` and is GIT-HISTORY-ONLY. Recover with `git show 1cb18fbc3^:AGENTS/CARL/<path>`.

Verbatim span:

```text
 ⚠️ **[RE-POINTED 2026-08-15 — PROME 6/30 prune-scan, class FALSE_PRESERVATION: the path named here was DELETED by `1cb18fbc3` and is GIT-HISTORY-ONLY. Recover with `git show 1cb18fbc3^:AGENTS/CARL/<path>`. Claim kept because it is a true historical record; the location was the false part.]**
```

## H21 — FILES table, archive/workbook_hardening row

KEPT IN CHARTER beside the pointer: The path named here was DELETED by `1cb18fbc3` and is GIT-HISTORY-ONLY. Recover with `git show 1cb18fbc3^:AGENTS/CARL/<path>`.

Verbatim span:

```text
 ⚠️ **[RE-POINTED 2026-08-15 — PROME 6/30 prune-scan, class DEAD_PATH: the path named here was DELETED by `1cb18fbc3` and is GIT-HISTORY-ONLY. Recover with `git show 1cb18fbc3^:AGENTS/CARL/<path>`. Claim kept because it is a true historical record; the location was the false part.]**
```

## H22 — WORKBOOK DISCIPLINE (worked failure)

Verbatim span:

```text
 (Worked failure: KB-154 plasma donations is a behavioral lower-cohort signal; KB-111 retail flows is an upper-cohort positioning signal — they're both "K-shape" topically, but no single threshold measures both.)
```

## H23 — CLOSEOUT step 15 (hand-verify pairs)

Verbatim span:

```text
 *(Boot-side auto-scan of these pairs = the Phase-3 `scripts/consistency_check.py` enhancement.)*
```

