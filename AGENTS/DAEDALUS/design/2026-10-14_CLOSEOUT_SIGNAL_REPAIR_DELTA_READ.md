# Closeout signal repair — DELTA READ of the Fix 1 + Fix 4 repair (WQ-229 fresh-context reader)

**Reader:** fresh-context independent reader (Claude Code subagent, claude-opus-5-5), spawned by DAEDALUS · **Date:** 2026-10-14 (ET; runs 22:40–22:55) · **Mode:** read + drill in scratch clones only. No live-repo stage, commit, stash or reset. Live-repo commands were read-only (`git show`/`git log`/`git diff`; `orphan_check.sh` with `GIT_OPTIONAL_LOCKS=0`). The only live write is this file.
**Read first:** `design/2026-10-14_CLOSEOUT_SIGNAL_REPAIR_ACCEPTANCE.md` (Fix 1, Fix 4) and `design/2026-10-14_CLOSEOUT_SIGNAL_REPAIR_INDEPENDENT_READ.md` (F1-a…d, F4-a…f, CE1–CE8, CE-A…D).

## Clone base and files under review

| Item | Value |
|---|---|
| Clone base | `4877ac1c3` (live HEAD at spawn). Live HEAD moved to `c7361651a` during the read (OTTO/NEXUS/WALTER/RED commits). `git diff --stat 4877ac1c3 c7361651a` over the 3 files, `EVOLUTION.md` and the acceptance doc is empty. |
| Clones | `/tmp/claude-1000/delta-reader/clone` (Fix 1 drills, cumulative, plus a gate run) · `iso` (isolated AC sequence and an in-range bad byte) · `iso2` (out-of-range bad byte plus a gate run) · `c4` (Fix 4 drills plus a gate run) |
| Candidates (sha256[:12]) | `complete_check.py` **ecf4be4af892** · `daedalus_gate.py` **80d03dfc1ae9** · `orphan_check.sh` **fbb66c09b949**, from `…/scratchpad/step1/`. Re-verified before **every** run: `tools/install.sh` does copy + sha check for the clone runs, and `tools/oc.sh` refuses on a sha mismatch and runs the candidate from scratch, so a clone reset cannot swap the script in. |
| HEAD versions | `e944d6db0719` / `b280a9108858` / `e9cd6a58b014`. The live working tree equals HEAD for all three (the first versions are not installed). |
| Diff | complete_check: leg (ii) gains `late_entry()` (canonical token, then the first hex-bounded ≥9-hex hash within 120 chars, which must be a prefix of the commit). Gate: `"RECORDED LATE"` added to the `finding_lines` keys. orphan_check: classify-by-state rewrite (porcelain `XY\|src\|dst`; rename / delete / basename-of-deletion / name-arm rules). The candidate's file mode is 100644 against HEAD's 100755 (see D4-5). |
| Receipts | `DAEDALUS_GATE_DIR=/tmp/claude-1000/delta-reader/rcpt{,2,4}`. The shared default `/tmp/claude-1000/daedalus-gate` was not written: its newest file is 21:55 ET, before my first run at 22:42. |

## Commands run (results)

| # | Command (clone unless noted) | Result |
|---|---|---|
| 1 | `daedalus_gate.py --selftest` (candidate) | **RC=0**: `SELFTEST PASS — A1 A3 A4 A5 A8 A12` and `CANDIDATE SELFTEST: 66 passed, 0 failed` |
| 2 | `complete_check.py` (today's range): candidate vs HEAD | candidate RC=0, `📝 PAIRING RECORDED LATE: commit 47bd8f55d … EVOLUTION.md:11`. HEAD RC=1, `⏰ PAIRING: commit 47bd8f55d`. |
| 3 | The new regex over every token in `HEAD:EVOLUTION.md` | 6 tokens. Lines 11→`47bd8f55d`, 34→`0cc007f28`, 41→`fcdcf9254`: all correct, and line 41 binds the standards commit, not the later entry commit `36e8d638f` named after it. Lines 9, 27, 70 are headings with no hash, so they excuse nothing. |
| 4 | Real `closeout --no-superseded --no-memory --rule-declared none` | RC=2 (C0 UNKNOWN; C3, C7 DUE). **C8 CLEAN and displays the 📝 line**, which is also in the receipt's `findings`. |
| 5 | `finding_lines` HEAD vs candidate over all 11 step logs of run 4 | Only difference: +1 📝 line at C8. `findings` is consumed only for display and receipt (gate lines 720/722). Classes and rc are untouched. |
| 6 | Isolated AC sequence (`iso`, one standards commit) | S0 none RC=1 ⏰ · S1 hash-only RC=1 ⏰ · S2 uncommitted canonical RC=1 ⏰ · **S3 committed canonical RC=0 📝** · S4 later commit removes it RC=1 ⏰ · uppercase hash RC=1 ⏰ |
| 7 | `tools/f1.sh` prior CE1–CE8 (fresh standards commit each) | **All ⏰.** CE1 (late for OTHER, HASH unrelated), CE2 VIOLATED, CE3 TEMPLATE, CE4 LATER, CE5 hash inside a longer hex run, CE6 lowercase, CE7 7-char, CE8 hash on the line above |
| 8 | `tools/f1.sh` new N1–N10 | see D1-1…D1-5 and D1-✅ |
| 9 | Non-UTF-8 byte in committed EVOLUTION: `iso` (in range) and `iso2` (via a `PROME:` commit, out of range) | In range: both versions traceback, RC=1. **Out of range: candidate traceback RC=1; HEAD completes normally.** Gate on `iso2`: **C8 BLOCKING** with no finding line (D1-4). |
| 10 | Fix 4 prior drills, candidate vs HEAD (`tools/oc.sh`) | clean tree → clean line. Author drill: git-mv filing → `[already committed]`, untracked → YOURS. CE-A, CE-B, CE-C, CE-D → **YOURS** (all closed) |
| 11 | Fix 4 new N4-1 … E3 | see D4-1…D4-5 and D4-✅ |
| 12 | `bash -x` on the AD state; order probe; patched `\|\| true` probe | The trace ends at `git cat-file -e HEAD:AGENTS/WALTER/notes.md` → `DELETED=` → exit **128**. Adding a staged `M.` entry (which sorts after `AD`) → rc 0. Patched copy on the AD state → rc 0 and YOURS restored. |
| 13 | Gate closeout in `c4` on the AD state; bare `bash scripts/orphan_check.sh DAEDALUS` | Gate: **C1 UNKNOWN `orphan_check rc 128`**, packet not named. Bare: **no output at all, rc=128.** |
| 14 | Repo population (live, read-only) | **250** packet basenames at HEAD live in >1 dir (max 37 copies). 30 of these are `_from-DAEDALUS_`. `47bd8f55d` today wrote `2026-10-14_from-DAEDALUS_brief-pin-wiring.md` into **12** inboxes. Per-desk `NEXUS_BRIEF.md` is committed only by its owning desk (0 NEXUS-subject commits since 07-15). 44 tracked paths contain a space. |
| 15 | Live read-only parity (`GIT_OPTIONAL_LOCKS=0`) for DAEDALUS, PROME, OTTO and NEXUS | Labels identical to HEAD, rc 0. The live tree had 39 ` M` + 4 `??` and no staged entries. |
| 16 | Same-owner probe (scratch only, `orphan_probe_owner.sh`; not a candidate) | see the D4-2 repair column |

## Findings

### Prior findings re-checked

| ID | Verdict | Evidence |
|---|---|---|
| F1-a | ✅ closed | CE2–CE5 → ⏰ (cmd 7). `LATE\b` and the hex-bounded hash hold. |
| F1-b | ✅ closed for CE1 | A late line for OTHER that mentions HASH later no longer excuses HASH. Residue: D1-2. |
| F1-c | ✅ closed | C8 shows 📝, the one-line display diff appears only at C8, and the class is unchanged (cmds 4–5). |
| F1-d | ⚠️ unchanged (safe direction) | CE6–CE8 still ⏰. The required form is stated only in the code comment. **AC1.1 still says "in either order, ≤40 chars apart"**, which is stale against the code. |
| F4-a / F4-b / F4-c | ✅ closed | CE-A, CE-B, CE-C → `[likely YOURS]` (cmd 10). |
| F4-d | ✅ resolved toward YOURS | ` M` of a packet-pattern file → YOURS. As a result, AC4.1's "an uncommitted change to a delivered path → delivered" now holds only for rename, delete and the name arm. The AC text needs amending. |
| F4-e | ⚠️ unchanged | The code prints `[already committed — not yours now]`; AC4.1 specifies `[delivered — recipient's change]`. |
| F4-f | ✅ improved | A spaced untracked packet is now YOURS (as a quoted path), where HEAD printed `[not yours] b.md"`. ` -> ` inside a name still mangles in both versions (E1). |

### New findings

| ID | Fix | Verdict | Finding | Evidence | Repair (smallest) |
|---|---|---|---|---|---|
| D1-1 | 1 | ⚠️ | **Token prose is negation-blind.** Each of these excuses the commit with 📝: N1 `NOT a PAIRING, LATE record for HASH; that commit still owes its own entry` · N2 `Open: PAIRING, LATE entry still owed for HASH` (within AC1.1's letter, but against its intent: the change record is still missing) · N4b `complete_check accepts PAIRING, LATE …; example from today's drill: HASH`. The direction is dangerous. Each needs the uppercase token typed into DAEDALUS's own committed EVOLUTION, followed by a real unpaired in-range commit (default range = today). Live corpus: 6 tokens, all genuine. | cmd 8 | One template rule in EVOLUTION: the late entry is `**PAIRING, LATE:** <hash> …`, and the token never appears in negated, pending or rule-describing prose. |
| D1-2 | 1 | ⚠️ | **The first hash after the token is not necessarily the subject.** N3b: `PAIRING, LATE — after OTHER's READ_CAP edit, the commit actually missing its entry is HASH`, where OTHER = `5f16b6c1b` is a real unpaired in-range commit. Result: **OTHER 📝 (false excuse)**, HASH ⏰. N3a is the mirror image. Mitigation: the 📝 line names the EVOLUTION line and is now visible at C8. | cmd 8 | Require the hash to be the first token after `PAIRING, LATE:` / `PAIRING RECORDED LATE:` (allow only `` ` ``, `*` and spaces between). This also kills D1-5. |
| D1-3 | 1 | ⚠️ | **`endpos` truncation.** `hexhash.search(line, m.end(), m.end()+120)` treats offset 120 as end-of-string, so a >40-hex run that straddles it matches its visible prefix. N7a (FULL+`abcdef0123` at offset 111) → 📝. The same run at offset 5 (N7b) → ⏰. Contrived: it needs a commit hash glued to more hex. | cmd 8 | Search without `endpos` and test `h.start() - m.end() <= 120`. |
| D1-4 | 1 | ⚠️ | **New crash path (regression vs HEAD).** `subprocess.run([... "HEAD:…EVOLUTION.md"], text=True)` decodes strictly. One committed non-UTF-8 byte anywhere in EVOLUTION.md (even from another desk's commit, outside the range) → traceback, RC=1 → **gate C8 BLOCKING with no finding line**. HEAD's only EVOLUTION read uses `errors="replace"` and completes. This fails closed, so nothing is hidden, but it breaks complete_check's own §9 contract (a crash should be rc 2 CANNOT-CERTIFY). | cmd 9 | Add `errors="replace"` to that `subprocess.run`, or try/except → print CANNOT-CERTIFY and exit 2. |
| D1-5 | 1 | ⚠️ (safe) | **Numeric shadowing.** `[0-9a-f]{9,40}` also matches decimals. N6 `PAIRING, LATE (rotated block crc32 1151981870): HASH` → ⏰ (crc32s are routinely cited in this repo). A 32-hex asset id first (N5b) → ⏰. These are false BLOCKINGs, never false excuses. | cmd 8 | As D1-2 |
| D1-✅ | 1 | ✅ | AC1.1, AC1.2 and AC1.3 hold; removal re-surfaces the miss (S4); CE1–CE5 are closed. A commit URL with the full hash (N5) and the heading form (N9) excuse as intended. Two tokens on one line (N4) each bind their own first hash. An uppercase hash → ⏰. Legs (iii)–(v) are untouched. The gate's +1 key changes only C8's display. | cmds 2–8 | — |
| D4-1 | 4 | ❌ | **`set -e` crash: rc 128, empty output, capable case silenced.** Lines 93–94 read `DELETED=$(… committed "$dst" && echo … done \| sort -u)` with **no `\|\| true`**. If the last sorted entry is a `*D*` whose dst is not in HEAD, `git cat-file -e` returns 128, pipefail carries it out of the substitution, and `set -e` exits. Reached by: `AD` (staged, then deleted). N4-1b is my own staged packet moved with plain `mv`; **N4-4 is another desk's unrelated file**. Also reached by `RD` (N4-4b) and a staged `D.` of a spaced path (N4-3a; 44 tracked paths have spaces). Under `C.UTF-8`, staged XY codes sort after `.M` and `??`, so such an entry is last whenever no `M.`/`R.` entry exists (cmd 12). **Bare root-1b run: nothing printed, rc 128, fleet-wide, and any desk can create the state in the shared index.** DAEDALUS gate: C1 UNKNOWN with the packet unnamed. HEAD in all 4 cases: rc 0 + `[likely YOURS]`. Violates AC4.3 and AC4.2. | cmds 11–13 | `… done \| sort -u \|\| true)`. Probed: rc 0, YOURS restored. |
| D4-2 | 4 | ❌ | **Basename coincidence still hides never-sent packets** (the residue of the F4-a repair). A committed deletion with the same basename *anywhere* flips my untracked or added packet to `[already committed — not yours now]` + "do NOT commit". N4-2: WALTER files my delivered copy with plain `mv`, and my new same-name copy to `PROME/inbox/` is untracked → all three labelled delivered. N4-2b: the recipient deletes its copy. E3: my staged `A.` vs the recipient's `git rm`. **This is realistic:** same-name broadcast is routine (250 multi-dir basenames; today's 12-inbox `brief-pin-wiring`). A staggered broadcast plus one recipient filing by plain `mv` is exactly this state. Violates AC4.2. | cmds 11, 14 | Count a delete/rename as a delivery only **within one owner tree** (`AGENTS/<X>/` or `PROME/`): a recipient files inside its own tree. Probe (cmd 16): N4-2, E3 and N4-7 → YOURS. Author drill, plain-mv filing and PROME-packet filing → delivered. AD state → rc 0. |
| D4-3 | 4 | ⚠️ | **My own re-route of a DELIVERED packet** (N4-7: `git mv` WALTER→PROME; N4-7b: plain `mv`) → "not yours now / do NOT commit". State alone cannot tell me from a recipient. | cmd 11 | The same-owner rule (D4-2) returns YOURS for cross-owner moves (probed). |
| D4-4 | 4 | ⚠️ pre-existing | Unchanged from HEAD. N4-8: my packet inside a **new untracked subdir** (`?? AGENTS/WALTER/inbox/urgent/`) → `[not yours]` + do NOT commit. N4-6: a rename **into** my own dir leaves the source deletion outside my dir staged while the check prints clean. E1: ` -> ` inside a filename mangles. The new comment's claim "untracked dirs … stay [likely YOURS]" holds only when the dir name itself matches the pattern. | cmd 11 | `-uall` for N4-8 (a separate change) |
| D4-5 | 4 | ⚠️ minor | The candidate file mode is 100644 (HEAD 100755). Installing by `cp` onto the existing path keeps 755 (verified in the clone: content-only ` M`); `mv` or `install` would flip it. All callers use `bash …`. The header line "Paths containing spaces mangle in the awk $NF split" is now stale. | diff | Install by `cp`, and refresh that comment line. |
| D4-✅ | 4 | ✅ | N4-1 (plain `mv` of my untracked packet between inboxes) → YOURS. N4-1c (staged, then `git mv`) → YOURS. `AM` → YOURS. PROME as ME: `PROME/` filtered, new packet YOURS, NEXUS-filed PROME packet delivered. Name arm: FALCON's `NEXUS_BRIEF.md` edit → delivered and NEXUS's new `NEXUS_` file → YOURS, and the population confirms desks own their briefs. `\|` in a name → YOURS. A spaced untracked packet → YOURS. The clean line is unchanged. Live parity holds on 4 desks. Gate C1 still keys only on `likely YOURS`. | cmds 10, 11, 14, 15 | — |

## Per-fix verdict

| Fix | Verdict | Basis |
|---|---|---|
| **1** complete_check RECORDED-LATE (+ gate key) | **ACCEPT-WITH-RESIDUE** | The prior ❌s (F1-a, F1-b) and ⚠️ F1-c are closed; the AC sequence and the live 47bd8f55d case hold. Every remaining false-excuse path (D1-1…D1-3) needs the deliberately typed uppercase token, followed by a real unpaired in-range commit, in DAEDALUS's own committed EVOLUTION.md. Every excuse prints a 📝 line naming that EVOLUTION line, now visible at C8. **Before install:** take the one-token D1-4 (`errors="replace"`) ride-along. **Records:** state the canonical form (D1-1, D1-2) in the EVOLUTION template, and amend AC1.1's "either order, ≤40 chars" text. |
| **4** orphan_check classify-by-state | **REJECT as repaired** | F4-a, F4-b and F4-c are closed, but there are two new ❌. **D4-1:** a crash (rc 128, empty output) reachable from any desk's shared-index state, which silences the capable case fleet-wide; the fix is one token. **D4-2:** basename coincidence violates AC4.2, and same-name broadcasts are routine. Both repairs were probed in scratch (same-owner rule + `\|\| true`). Likely ACCEPT after both, plus a re-run of this battery (`tools/oc.sh` cases in this file). Also align AC4.1's label and its ` M` clause (F4-d, F4-e). |

## Not checked

- Fix 2 and Fix 3: out of scope. The candidate gate is HEAD plus one key, and no ack code is present.
- The prior reader's exact CE texts were not stored (its `f1.sh` takes templates as arguments). I reconstructed CE1–CE5 from the wording of its findings table and CE6–CE8 from F1-d.
- The same-owner probe is a scratch experiment, not a reviewed candidate. Its own residue: a same-basename resend into the **same** recipient's tree, while that recipient files or deletes its earlier copy, would still read delivered.
- Unmerged states (`UU`/`DU`/`DD`), `.R` intent-to-add renames, C-quoted non-ASCII names, `core.quotePath=false`.
- Locales other than C.UTF-8. Collation decides which entry sorts last; not run.
- Companion records (EVOLUTION entry, CHECKS.tsv row, gate spec §8, charter step 9): not read.
- A live gate closeout: not run, because it would append to the live `runs/GATE_LOG.tsv`. Clone runs only.
- `closeout --candidate` end-to-end, and the midnight rollover of complete_check's default range.
