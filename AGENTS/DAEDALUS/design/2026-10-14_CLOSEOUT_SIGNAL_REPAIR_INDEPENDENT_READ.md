# Closeout signal repair — INDEPENDENT READ (WQ-229 fresh-context reader)

**Reader:** fresh-context independent reader (Claude Code subagent, claude-opus-5-5), spawned by DAEDALUS · **Date:** 2026-10-14 (local ET, finished ~22:35 ET) · **Mode:** read + drill in scratch clones only. No live-repo stage, commit, stash or reset. Live-repo commands were read-only: `git diff` / `git status` / `orphan_check.sh` run with `GIT_OPTIONAL_LOCKS=0`.
**Acceptance read first:** `design/2026-10-14_CLOSEOUT_SIGNAL_REPAIR_ACCEPTANCE.md` (5,579 B, Fix 1–4, AC1.1…AC4.3).

## Clone base and files under review

| Item | Value |
|---|---|
| Clone base | `859c1d125` (live HEAD at spawn). Live HEAD later advanced to `d4628cb3c` from other desks' commits; none of them touch the four files. |
| Clones | `/tmp/claude-1000/reader/clone` (changed files), `/tmp/claude-1000/reader/pristine` (HEAD versions, for before/after), `/tmp/claude-1000/reader/c4` (Fix 4 drills) |
| Files copied from the live working tree (sha256[:12]; re-verified identical to live at 22:29 ET) | `complete_check.py` bd63e1a94ed0 · `daedalus_gate.py` cdcc4f33bb04 · `profile_clock_check.py` c870cca5ace6 · `scripts/orphan_check.sh` 4b176c110e56 |
| Gate receipts | All my gate runs used `DAEDALUS_GATE_DIR=/tmp/claude-1000/reader/rcpt`. The shared default `/tmp/claude-1000/daedalus-gate` was not written: its newest file is 21:55 ET, before my first run. |

**Read in full or in relevant ranges:** the four diffs. Whole `complete_check.py`. `daedalus_gate.py` §registries (boot_registry, closeout_registry), `child_step`/`read_cap_step`/`finding_lines`, `run()`, the new ack code and selftest. Whole `profile_clock_check.py` `vintage_of`/`main`. Whole `orphan_check.sh`. The output formats of each ack-able child: `sweeps_due.py` profile relay, `profile_clock_check.py` print block, `docket_owed.py` assess(), `claim_check.py` flag/print, `consumer_check.py` stale print, `check_memory_length.sh`, `read_cap_check.py` tier labels.

## Commands run (results)

| # | Command (clone unless noted) | Result |
|---|---|---|
| 1 | `daedalus_gate.py --selftest` (changed) | RC=0 · legacy `SELFTEST PASS` · `CANDIDATE SELFTEST: 66 passed, 0 failed` · `ACK SELFTEST PASS` (12/12 ✓) |
| 2 | same on pristine HEAD | RC=0 · legacy PASS · candidate 66/0, so the existing selftests are unchanged |
| 3 | `complete_check.py` (today range) | RC=0 · `📝 PAIRING RECORDED LATE: commit 47bd8f55d … EVOLUTION.md:11`. The author's live case reproduces. |
| 4 | real `daedalus_gate.py closeout --no-superseded --no-memory --rule-declared none` | RC=2 · C0 UNKNOWN, C3 DUE, C7 DUE · `VERDICT — NEW this run: C0 UNKNOWN, C3 DUE, C7 DUE`. Matches the author's state. |
| 5 | Fix 1 drill S0–S4 (one standards commit `7153baa2c`) | S0 no entry RC=1 ⏰ · S1 hash-only RC=1 ⏰ · S2 uncommitted late entry RC=1 ⏰ · S3 committed late entry RC=0 📝 · S4 a later commit removes the entry → RC=1 ⏰ (re-surfaces; no silent re-hide) |
| 6 | Fix 1 CE1–CE8 (`tools/f1.sh`; fresh standards commit each) | CE1–CE5 **excused (📝)** · CE6–CE8 still ⏰ (see F1-a/b/d) |
| 7 | `finding_lines()` over complete_check output | 6 📝 lines in child stdout → **0 kept** in gate display and receipt |
| 8 | Fix 2 E2E drills via harness `tools/gh.py`: real registry steps, real children, chosen `today` | C5, C9, C1, C0 hidden-new cases all print `NEW this run: none` + 📌 CARRIED (F2-a/b) |
| 9 | Author's Fix 2 drill: acks C0/C3/C7 → run | `NEW this run: none`, 3 × 📌. Reproduced. Positive control: new CANNOT-EVALUATE agent → `C0 UNKNOWN` NEW ✓ |
| 10 | In-process ack edge cases (15 probes) | See F2-c…F2-j and the ✅ rows |
| 11 | Real closeout with one `\xff` byte in `GATE_ACKS.tsv` | **Traceback `UnicodeDecodeError`, RC=1, receipts 11→11 (none written)** (F2-c) |
| 12 | `daedalus_gate.py verify-receipt <new receipt>` | `✅ VALID … IDENTITY ONLY`, RC=0; new keys `new`, `ack_problems`, step `fp` do not break it |
| 13 | `profile_clock_check.py --as-of 2026-10-14 --profiles <live profiles/>`: pristine vs changed | both rc=2; `diff` **IDENTICAL** over 38 profiles |
| 14 | `scripts/tests/test_profile_clock_check.py` | `Ran 12 tests … OK` |
| 15 | `vintage_of()` old vs new on 12 synthetic headers | see F3-a |
| 16 | Fix 4 drills in `c4` (author drill + CE-A…CE-F), each also run against the HEAD script | see F4 rows; every run RC=0 (bare rc read) |
| 17 | Live, read-only: `orphan_check.sh DAEDALUS` old vs new (+ NEXUS, FALCON) | identical labels. Live tree had no DAEDALUS-pattern entry at 22:2x ET, so the 10/14 FALCON case is reproduced only as a drill. |

## Findings

| ID | Fix | Verdict | Finding | Evidence | Repair (smallest) |
|---|---|---|---|---|---|
| F1-a | 1 | ❌ | **The excuse matcher is not anchored.** `late_words` is case-sensitive *substring* `PAIRING.{0,40}LATE`, so LATE matches inside **VIOLATED, TEMPLATE, LATER, RELATED, TRANSLATE**. `c[:9] in l` is a substring, so the hash matches inside any longer hex string. Excused, with no late record: CE2 `HASH VIOLATED PAIRING rule ii; owner to fix next session` · CE3 `HASH touched the PAIRING block of CLAUDE_TEMPLATE` (CLAUDE_TEMPLATE occurs 7× in EVOLUTION+archive) · CE4 `` `git show HASH` … PAIRING diff; decide LATER `` · CE5 `PAIRING LATE drill: blob sha256 ffffHASHeeee…`. This relaxes a gate, so a false excuse fails in the dangerous direction. | cmd 6 | `\bPAIRING\b\W{0,5}(?:RECORDED\s+)?LATE\b` and `(?<![0-9a-f])h(?![0-9a-f])` |
| F1-b | 1 | ❌ | **The excuse is not bound to the commit.** Any committed line that carries this hash *anywhere* plus the words excuses it, including a late entry for a **different** commit that cites this one as unrelated (CE1: `PAIRING RECORDED LATE for 0123abcde — …; HASH is the unrelated READ_CAP typo fix` → HASH excused). EVOLUTION lines are whole paragraphs (47 non-empty lines, median 430 chars, max 1,789), and 2 already carry ≥2 hashes. | cmd 6 | Require the hash within ~N chars after the LATE token (the live entry has it 33 chars later), or a canonical per-commit token `PAIRING-LATE: <hash>` |
| F1-c | 1 | ⚠️ | **AC1.4 holds only at complete_check's own stdout.** Under the gate (C8, the surface closeout reads), `finding_lines` keeps **0 of 6** `📝` lines. RECORDED-LATE lives only in `logs/<stamp>_C8.txt`, so the miss is invisible to the closeout reader. | cmd 7, cmd 4 (C8 shows no 📝) | Add `"RECORDED LATE"` to `finding_lines` keys (display only; CLEAN steps are never ack-able) |
| F1-d | 1 | ⚠️ | Fails safe but noisy: a genuine late entry is **not** recognised in lowercase (`pairing, late:`), with a 7-char hash, or with the hash on the line above the words (CE6/CE7/CE8 → still ⏰, so a false BLOCKING persists). A late entry rotated to the archive also re-surfaces the miss (same direction; only matters inside the range, default = today). | cmd 6 | State the exact required form in the EVOLUTION template |
| F1-✅ | 1 | ✅ | AC1.1 (committed late entry → 📝, not a finding), AC1.2 (hash-only → finding), AC1.3 (uncommitted entry → finding). `HEAD` is the right basis: a later commit that **removes** the entry re-surfaces the miss (S4 RC=1), so nothing re-hides silently. Legs (iii)–(v) untouched in the diff. | cmd 5 | — |
| F2-a | 2 | ❌ | **Digit normalisation plus a *set* of lines hides new problems** wherever numbers are identity rather than age (this is the most important question). **C9:** the signal *is* a date. An ack written on 10/14 for `'Last Updated' is 2026-10-13, not 2026-10-14` CARRIES 10/15's fresh failure `is 2026-10-14, not 2026-10-15` (a different session's miss). **C1:** packet names carry dates and WQ ids. After acking `2026-10-14_from-DAEDALUS_WQ-385-reply.md` and delivering it, a NEW never-sent `2026-10-15_from-DAEDALUS_WQ-434-reply.md` prints `NEW: none` + 📌, so the packet would be orphaned silently. In-process: `PAT-101/WQ-385/L285` ≡ `PAT-180/WQ-434/L658`; 1 line ≡ 2 lines that differ only in digits (set collapse; this is the B5 recurring-DOCKET-row mechanism). | cmd 8 (C9, C1 E2E), cmd 10 #13–14 | Normalise only age/size tokens (`\b\d+d\b`, `age \d+`, `\d[\d,]* B`, `\d+%`); keep dates, line numbers and ids; hash a sorted **list** (multiset), not a set |
| F2-b | 2 | ❌ | **The fingerprint covers the *display subset*, not the findings.** `finding_lines` drops the lines that name *what* is wrong for two ack-able steps. **C5:** claim_check's per-flag `path:line` / message lines carry no key marker, so the fingerprint is the constant `1f67545653a34f1f` for **any** weekday flags. E2E: acked 1 flag in STATUS.md, fixed it, planted 3 different flags in `PROME/WILL_QUEUE.md` → `NEW: none` + 📌 C5. **C0/B1:** profile `ALERT <AGENT>` lines follow a non-key line and are never captured (15 live ALERTs are already absent from the gate display). E2E: acked C0, made HANS stale (`ALERT HANS … 101d > 45d`) → `NEW: none` + 📌 C0. | cmd 8 (C5, C0 E2E) | Fingerprint the child's flagged-item lines (or full log minus the volatile walk-list), not `finding_lines` |
| F2-c | 2 | ❌ | **An unreadable register breaks the rc contract (AC2.1/AC2.5).** `load_acks` reads the file outside its `try`. One non-UTF-8 byte (or a directory or permission error at that path) makes the gate crash **after** all children ran: Python traceback, **RC=1** (the contract reads that as BLOCKING; the correct rc for this run was 2), **no receipt, no GATE_LOG row**. "Malformed rows are named, never ignored" holds per row but not per file. | cmd 11 | Wrap the read in try/except → `ack_problems`; never let presentation code change rc |
| F2-d | 2 | ⚠️ | Per-session obligations can be acked: C9 (above) and the UNDECLARED UNKNOWNs of C2/C4/C10, whose reason is a fixed string. An ack carries every later session's failure to declare for up to 21 days (probe #11: C4 UNDECLARED ack on 10/14 → CARRIED on 10/20). | cmd 10 #11 | `ack` refuses C9 and UNDECLARED results |
| F2-e | 2 | ⚠️ | The 21-day cap can be bypassed by hand: `load_acks` never checks `added ≤ today`. A row `added 2026-11-01 / expires 2026-11-20`, read on 10/14, is valid and CARRIED (37 days out, still CARRIED on 11/20). | cmd 10 #8 | Reject `added > today` |
| F2-f | 2 | ⚠️ | The match ignores class: a row written while a step was DUE carries the same step as ADVISORY when the fingerprint is equal (probe #10). Theoretical today, because per-class reason strings differ. | cmd 10 #10 | Store the class in the row and match it |
| F2-g | 2 | ⚠️ | `ack --owner` with a TAB returns rc 0 `✍️ ACK written` but writes an 8-field row, which the next run names as ignored. `--reason` is validated; `--owner` is not. | cmd 10 #15 | Validate owner like reason |
| F2-h | 2 | ⚠️ | The register is read from the **working tree**, so an uncommitted ack is effective. This is the opposite of Fix 1's committed-only principle. Not required by AC2.2, but worth a deliberate ruling. | code read | Read `HEAD:` or state the choice |
| F2-i | 2 | ⚠️ | `ack` takes the newest `*_<mode>.json` from the **shared default** receipt dir (`/tmp/claude-1000/daedalus-gate`, not per tree), with no check of the receipt's `head`/root. A newer receipt from another clone, worktree or candidate run is acknowledged as "what was seen". Content matching bounds the harm. | code read | Check `receipt.head == HEAD` and the root |
| F2-j | 2 | ⚠️ | AC2.5 says the receipt gains `carried` *per step*. In fact the key appears only on carried steps (non-carried steps have `fp` and optionally `ack_note`). Cosmetic. | cmd 12 key dump | — |
| F2-✅ | 2 | ✅ | On the normal path, classes, rc, receipt and GATE_LOG are unchanged: rc is computed before `apply_acks`, legacy and candidate selftests are identical to pristine, verify-receipt is VALID, and the GATE_LOG row code is untouched. BLOCKING is never carried (`ack` refuses it, the matcher ignores it). Probes behave as AC2.4 says: mode mismatch → NEW · duplicate rows → CARRIED · expired + live duplicate → CARRIED (live) · expiry == today → CARRIED · expiry = added+21 accepted · +22 named + ignored · expired → NEW + named. Reordered lines are stable (sorted). The author's C0/C3/C7 drill reproduces, and the positive control (new CANNOT agent) goes NEW. | cmds 1, 2, 9, 10, 12 | — |
| F3-a | 3 | ⚠️ | The new **in-Body-segment** `WHOLE refresh <date>` path skips the delta/partial guard that the primary path applies, and has no negation or plan guard. These certify a past date as body vintage (old → new): `WHOLE refresh 2026-10-08 planned (not yet done)` · `… DEFERRED to Q4` · `no WHOLE refresh 2026-10-08 — skipped` · `… (partial — §3 only)` · `(mirrors VULCAN's WHOLE refresh 2026-10-08)`, all 09-05 → **10-08**. No live profile has such wording (cmd 13 identical). A future-dated planned refresh fails loud (AC3.2) until the date passes, then silently certifies. The standalone-segment path has the same pre-existing class (`Full refresh 2026-10-08 planned` was already read). | cmd 15 | Apply the existing `(delta|partial)` test to each `whole` match; refuse when trailing words say planned/deferred/skipped/no |
| F3-b | 3 | ⚠️ | `Body: A, §3 refreshed B, WHOLE refresh C` still raises `section refresh lacks explicit whole-body vintage` (the ambiguity check fires before WHOLE is considered). A safe-direction false alarm. | cmd 15 | — |
| F3-✅ | 3 | ✅ | AC3.1 (both forms read C), AC3.2 (a future WHOLE date → `age < 0` → CANNOT-EVALUATE), AC3.3 (byte-identical output over all 38 live profiles, rc 2 both), 12/12 unit tests. | cmds 13–15 | — |
| F4-a | 4 | ❌ | **Reused basename hides a never-committed packet (AC4.2 violated).** PROME filed `2026-10-14_from-DAEDALUS_drill1.md` to `PROME/inbox/processed/` (committed). DAEDALUS then writes a **new** packet with the same name to `PROME/inbox/` (untracked `??`). Result: `[already committed — not yours now]` + "do NOT commit". The HEAD version says `[likely YOURS]`. Cause: the basename arm (`ls-tree … | grep -F "/${base}"`; also unanchored at the end). | cmd 16 CE-A | Delivered-by-basename only when the same status also shows a ` D` of a committed path with that basename (the plain-`mv` pair) |
| F4-b | 4 | ❌ | **An untracked directory matching the pattern is labelled delivered (AC4.2 violated).** `?? AGENTS/WALTER/inbox/2026-10-14_from-DAEDALUS_bundle/` gives `base=""`, so `grep -F "/"` matches every tracked path → `[already committed]`. HEAD version: `[likely YOURS]`. | cmd 16 CE-B | Treat a trailing `/` as not delivered (or `git status -uall`) |
| F4-c | 4 | ❌ | **My own move is read as the recipient's.** A committed `AGENTS/DAEDALUS/outbox/…_from-DAEDALUS_x.md`, `git mv`'d into `PROME/inbox/` and not committed (porcelain `R  src -> dst`): src is in HEAD → `[already committed — not yours now]`, so the recipient never receives it and the guidance says do NOT commit. HEAD version: `[likely YOURS]`. | cmd 16 CE-C | A rename whose src is under `HOME_DIR`/`LANE2` is never "delivered" |
| F4-d | 4 | ⚠️ | My **own** unsent edit (addendum or correction) to my delivered packet (` M PROME/inbox/…_from-DAEDALUS_x.md`) is now told "do NOT commit". This is by AC4.1 design (state cannot tell author from recipient), but the guidance is absolute; the HEAD version said `[likely YOURS]`. Needs an explicit ruling: if delivered packets are never edited, say so in the guidance. | cmd 16 CE-D | Soften: "if YOU edited it, send a new packet" |
| F4-e | 4 | ⚠️ | The label differs from AC4.1: it prints `[already committed — not yours now]`, while AC4.1 specifies `[delivered — recipient's change]`. Grep-able consumers need one string. | diff | Align the AC or the code |
| F4-f | 4 | ⚠️ | Pre-existing and unchanged: names with a space or `" -> "` mangle to `[not yours] packet.md"`, and non-ASCII names stay C-quoted. Behaviour is identical to HEAD (documented edge); exit 0 in all. `|` and `$(id)` in names classify correctly. | cmd 16 CE-F | — |
| F4-✅ | 4 | ✅ | Author drill (git-mv filed → delivered; untracked → YOURS); staged-new `A` → YOURS; recipient plain `mv` (` D` + `??`) → both delivered; PROME as ME (home `PROME/` filtered, own packet YOURS, filed packet delivered); clean line unchanged; **exit 0 in every run** (bare rc). `pipefail`: the `grep -q` SIGPIPE was correctly removed in `delivered()`; the remaining `echo | grep -qiE` sits in an `if` with a sub-buffer write and cannot SIGPIPE. Gate C1 still keys on `likely YOURS` only. | cmds 16–17 | — |

## Per-step judgment: can a digit-only or uncaptured change be a NEW problem that an ack hides?

| Step | Ack-able classes | Verdict | Why |
|---|---|---|---|
| C0 / B1 sweeps_due | DUE, UNKNOWN | ❌ | Profile ALERT lines are never fingerprinted (F2-b, E2E). Named `⏰ DUE:`, SELF-ROW and CANNOT lines are safe. |
| C1 orphan_check | DUE, UNKNOWN | ❌ | Dates and WQ ids in packet names, plus set collapse (F2-a, E2E). |
| C2 consumer_check | DUE, UNKNOWN | ⚠️ | Stale hits are captured (`path:line` + text); collapse only when the citing text is identical after digit removal. UNDECLARED is ack-able (F2-d). Not run E2E. |
| C3 ledger nudge | DUE, UNKNOWN | ✅ | Ledger names carry identity; only behind-counts are normalised (an age tick). |
| C4 memory | DUE, UNKNOWN | ✅ / ⚠️ | rc1→rc2 changes the context wording (`WARNING…at/over` → `CRITICAL…at/over the boot-load cap`), so it goes NEW. UNDECLARED is ack-able (F2-d). |
| C5 claim_check | ADVISORY, UNKNOWN | ❌ | The flagged items are never fingerprinted; constant fingerprint (F2-b, E2E). |
| C6 PATTERNS conservation | UNKNOWN (parse fail only) | ✅ | Fixed message. |
| C7 / B4 read_cap | DUE, UNKNOWN (+ B4 ADVISORY) | ✅ | Per-path lines carry the tier label (🟡/🟠/🔴); a new path or tier change goes NEW. Growth within a tier is carried, by design. |
| C8 complete_check | UNKNOWN | ✅ | CANNOT-CERTIFY text names its cause. |
| C9 STATUS stamp | DUE | ❌ | The date is the whole signal (F2-a, E2E). |
| C10 rule-declared | (DECL) | ✅ | Not ack-able. UNDECLARED → UNKNOWN is ack-able (F2-d). |
| B0 git state | UNKNOWN (fetch fail) | ⚠️ | ahead/behind and dirty counts normalised; `⛔ do NOT pull` appears only when dirty > 0, so 0→N breaks the fingerprint but N→M does not. |
| B2 corrections | UNKNOWN | ✅ | rc1 is BLOCKING (never carried). |
| B5 docket_owed | DUE | ⚠️ | Rows differing only in `L<n>`/date with identical role and catalyst text collapse (mechanism shown in-process, #14). Not run against a real recurring row. |

## Overall verdict per fix

| Fix | Verdict | Basis |
|---|---|---|
| **1** complete_check RECORDED-LATE | **REJECT as shipped** → ACCEPT after F1-a + F1-b (two regex/binding lines) | The ACs pass literally and the basis is right (HEAD, with removal re-surfacing), but five demonstrated false-excuse paths relax a gate in the dangerous direction. F1-c (gate never shows 📝) should ride along. |
| **2** NEW vs CARRIED | **REJECT as shipped** | Classes and rc are unchanged on the normal path (✅), but four ack-able steps (C0/B1, C1, C5, C9) let a demonstrably new problem print `NEW this run: none` (F2-a, F2-b). One bad byte in the register breaks the rc contract and loses the receipt (F2-c). AC2.3's promise ("any added, removed or changed finding line breaks it") is false for these steps. |
| **3** WHOLE refresh | **ACCEPT-WITH-RESIDUE** | ACs and live parity proven. Residue F3-a: planned, deferred, negated or partial wording in the Body segment certifies; no live profile is affected. |
| **4** orphan_check delivered | **REJECT as shipped** | Three demonstrated regressions where a never-sent packet is now labelled `[already committed — not yours now]` with "do NOT commit" (F4-a, F4-b, F4-c; the HEAD version said `[likely YOURS]` in all three). This is the capable case AC4.2 says must still fire. |

## Not checked

- A real 9-char prefix collision between two commits: not constructible (36-bit). F1-a's substring-in-longer-hex case is the reachable variant.
- C2 consumer_check and B5 docket_owed ack drills end-to-end (output-format read plus an in-process mechanism only). B0 fetch-failure ack.
- `closeout --candidate` with a `GATE_ACKS.tsv` present, end-to-end (candidate selftests only).
- Cross-machine git merge of `GATE_ACKS.tsv` (conflict markers are valid UTF-8 and would be named per row; not run).
- The author's companion records now being edited in the live tree (EVOLUTION entry, gate spec §8, charter step 9, CHECKS.tsv row): not read.
- A real closeout on the live repo (not run, because it would append to the live `runs/GATE_LOG.tsv`).
- Midnight/timezone rollover of complete_check's default "today" range. My Fix 1 drills used `--since 2026-10-14`.
- Consumers of gate receipts beyond a repo grep (only `AGENTS/CATO/runs/2026-09-18_1102_system-review-probe.py`, historical).
