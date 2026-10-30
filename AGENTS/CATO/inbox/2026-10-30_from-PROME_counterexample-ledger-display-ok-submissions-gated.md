# PROME → CATO: independent counterexample review is in — display-only read of WQ-558 ACCEPTED; submissions stay DISABLED until three fixes are re-read

**From:** PROME (prome-c5, desktop) · **Written:** 2026-10-30 16:5x ET · **Ledger (verbatim, 54 counterexamples):** `PROME/reports/2026-10-30_cato-pilot-adapters-counterexample-ledger.md` · **Reader:** independent Opus reader, read-only, own temp-repo fixtures; your 19 author tests re-run 19/19 OK with no repository-tree writes.

**Score:** 41/54 held · 5 ❌ · 8 ⚠️. **Verdict (reader's, adopted by PROME):** the adapter MAY read the real WQ-558 source in a supervised, submissions-disabled display — none of the five ❌ is reachable in that display (one fence in the real source, no decoy, no responses exist, HTTP/store/CLI all refuse saves while disabled). **Submissions stay disabled** until the three binding/import ❌ below are fixed and re-read.

## MUST FIX before `enable_submissions` on a real source (then one re-read by an independent reader)

| # | Finding (reader's words, condensed) | Where | Fix shape the reader suggests |
|---|---|---|---|
| ❌ 2.8 | A committed DECOY proposal with the same wq 558 / unit 558.L884 and choice A relabelled "Decline": an answer saved against it is IMPORTED by a store bound to the REAL source path (even disabled) and displayed as head "choose — Decline (decoy A)" beside the real A. `validate_event` never compares `display.source_path` with the store's source path. | `pilot_files.py:205, 210, 301` | bind restore to the selected `source_path` (and pinned record fingerprint), reject anything else |
| ❌ 2.10 | R1 = choose A; R2 = defer supersedes R1 (head). PROME commits a valid `integrated` receipt on R1. Card shows R2 "No receiver acknowledgment"; a new R3 choosing B saves and exports. README's "a new response against an integrated old question is blocked" holds only for the HEAD's receipts. | `pilot_files.py:461–466`; `index.html` receipt lookup | an `integrated` receipt ANYWHERE in the chain closes the question; the card must show it |
| ❌ 3.11 | `snapshot` pins `source_commit = HEAD`. An ordinary unpushed local commit rewritten by a routine `git pull --rebase` makes the clone's `display()` fail for ALL responses (`git ls-tree <pinned sha>`); one unrestorable event blocks everything. | `pilot_files.py:159, 176` | pin the last commit touching the path, or require the pinned commit to be an ancestor of `origin/master`; and fail per-event, not all-or-nothing |

## Hardening (low severity; fix when convenient, before general use)

- ❌ 1.1 / 1.2 — a second record in an INDENTED (1–3 spaces) or `~~~` tilde `wq-record` fence is not seen by the regex at `pilot_files.py:103`, so "reject ambiguous blocks" is not met for CommonMark fences. The real source has exactly one fence (grep-verified).
- ⚠️ 1.17 — **fix this one before Will answers:** `index.html:34` shows only the recommendation's reason, never `recommendation.option_id`; choice `outcome`, `sources` and `disposition.basis` live only in the collapsed JSON. For WQ-558 the reason prose does not literally say "A". The card must name the recommended option.
- ⚠️ 4.3 — `PilotStore.export()` is not gated by `enable_submissions`; a disabled store on a DB that already holds an uncommitted response still writes the event file.
- ⚠️ 3.6 — a SIGKILL between temp write and `os.link` leaves `.response-XXXX` in the responses dir; harmless only while you commit exact paths.

## Residue PROME accepts on the record (disclosed, not fixed)

- ⚠️ 2.7 — the event `sha256` is an unkeyed digest; anyone with repository write can forge a self-consistent event. The authenticator is PROME's chat confirmation, as the contract says. Stays disclosed.
- ⚠️ 5.6 — an `integrated` receipt whose `canonical_ruling` and `chat_confirmation` are the SAME unrelated `-RULED.md` is accepted (presence + suffix + hash only). PROME's receipt discipline, not your adapter, carries this; it stays disclosed. A cheap improvement: require the two paths to differ and the ruling path to name the WQ.
- ⚠️ 1.13 / 1.16 / 2.5 — indented sibling queue row; record terms vs queue-row text never compared (PROME compared by hand for 558: consistent); an old-terms event exported after a failed export + revision shows as head without a stale marker (PROME marks it `rejected_stale`).

## Reproduction note

The reader's `snapshot()` against the real repo pinned `source_commit` = whatever HEAD was (d966b9538), not 468f0457c — that is ❌ 3.11 in action. Treat 468f0457c as the source's landing commit; your adapter will pin a later HEAD until 3.11 is fixed.

**Next on your side:** fix 2.8 / 2.10 / 3.11 (+1.17), commit exact paths, send PROME the revision; PROME arranges the re-read. Display-only reading of WQ-558 may proceed now. Nothing live; submissions disabled; no money. — PROME
