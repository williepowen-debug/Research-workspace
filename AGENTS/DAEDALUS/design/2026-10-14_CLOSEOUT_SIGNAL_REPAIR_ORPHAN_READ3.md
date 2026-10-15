# Closeout signal repair — ORPHAN READ 3: Fix 4 r2 (owner-tree rule + `|| true`), WQ-229 fresh-context reader

**Reader:** fresh-context independent reader (Claude Code subagent, claude-opus-5-5), spawned by DAEDALUS. **Date:** 2026-10-14 (ET; runs 23:00–23:13). **Mode:** read plus drills in one scratch clone. No live stage, commit, stash or reset. Live commands were read-only: `git show/log/diff/ls-tree`, and the candidate and HEAD scripts run with `GIT_OPTIONAL_LOCKS=0`. **The only live write is this file.**
**Read first:** acceptance Fix 4 and its amendment table (`…_ACCEPTANCE.md`, working-tree copy); read 1 (`…_INDEPENDENT_READ.md`, F4-a…f); delta read (`…_DELTA_READ.md`, D4-1…D4-5 and its Not-checked list).
**Property tested (from the spawn brief):** a never-sent packet I authored must always print `[likely YOURS]`, and the script must always exit 0 with output. A recipient filing my committed packet inside its own tree should print `[already committed — not yours now]`.

## Clone base and files under review

| Item | Value |
|---|---|
| Clone | `/tmp/claude-1000/orphan-read3/clone` (`--shared --no-checkout`, then `checkout HEAD`; the local git user is set in the clone only) |
| Base | `33d1a6c84`. Live HEAD was `89f7d59e4` at spawn and `3e4ea6cda` at the end (PROME, OTTO). `git diff --stat` over both ranges on `scripts/orphan_check.sh`, `AGENTS/DAEDALUS/design/` and `daedalus_gate.py` is **empty**. |
| Candidate r2 | `…/scratchpad/step1/orphan_check_r2.sh`, sha256 **`05ac8b6d00793046172e2638b48a3f65e2abb8f82b1dd10d68887e8d9680ac77`**, mode 755. Before **every** run it is re-copied to `orphan-read3/run/` and sha-verified (`tools/lib.sh` `run1` exits 99 on mismatch). It runs from outside the clone, so no reset can swap it in and it adds no status noise. sha re-checked at the end: unchanged. |
| HEAD | `scripts/orphan_check.sh`, sha256 `e9cd6a58b014…` (100755 in the index), extracted and sha-verified on every run |
| r1 (delta-read candidate) | `step1/orphan_check.sh`, sha256[:12] `fbb66c09b949`. Used only to prove that the crash states reproduce. |
| Diff r1→r2 (`diff`) | New `owner_of()`, which returns `PROME/`, `AGENTS/<X>/` or the first path component. DELETED now holds `owner\|basename`, with `committed` wrapped in `if…fi` and `\|\| true` added. The R arm adds `owner_of(src) = owner_of(dst)`. The `??`/`A` arm matches `owner\|basename`. The header comment is amended. |
| Probe (**not a candidate**) | `orphan-read3/run/probe_content.sh`, sha256[:12] `9905bea1659c`: r2 plus a 3-line content-identity rule (see R3-7) |
| Harness | `orphan-read3/tools/lib.sh`. Every scenario first runs `reset --hard <base>` and `clean -fdq`, then asserts a clean status. Scripts resolve `grep` to `/usr/bin/grep`, GNU grep 3.11; the interactive ugrep shell function is not inherited. |

## Population facts (live, read-only)

| # | Command | Result |
|---|---|---|
| P1 | `git ls-tree` inbox layout | Every desk tree has `inbox/` (top), `inbox/WALTER/` (WALTER's routing lane) and `inbox/processed/`. WALTER also has `inbox/DEWEY/` and `inbox/WILL/`; **`inbox/WILL/` is gitignored** (its own `.gitignore` is `*`). Senders write to the top level and recipients file into `processed/`. |
| P2 | Same basename twice inside **one** owner tree (packet-pattern names at HEAD) | **2 of 6,133** (both in REGINALD, both `from-BOND`). 0 for `_from-DAEDALUS_`. |
| P3 | Filing history over 60 days (`git log -M --diff-filter=R`, sources under an inbox) | 6,132 renames. **6,128 are R100** (content-identical), 6,122 keep the basename, **6,118 do both**, and 6,128 stay in the same owner tree. Pure deletions of top-level inbox packets: 78, mostly the "delete side / old-path removals" of plain-mv filings. |
| P4 | AGENTS dirs with tracked files but **no** tracked `inbox/` | ATHENA, CATO, SENTRY (`_archive` aside). Per ROSTER these are reading/knowledge, manual-only SPECIAL and dormant. |

## Scenario results (all ME=DAEDALUS unless noted; W = `AGENTS/WALTER`, P = `2026-10-14_from-DAEDALUS_x.md`)

Each row runs r2 and HEAD on the same state. **Every r2 run exited 0 with non-empty output.** That is about 70 runs over 53 distinct states, plus 8 locale variants and 5 live desks, including the 5,001-entry and 2,712-entry statuses.

### A — delta read's crash cases (D4-1)

| ID | State (porcelain) | r2 | HEAD | r1 (`fbb66c09b949`) | Verdict |
|---|---|---|---|---|---|
| A1 (N4-1b) | `AD W/inbox/P` · `?? PROME/inbox/P` | rc 0, both YOURS | rc 0, both YOURS | **rc 128, 0 lines** | ✅ |
| A2 (N4-4) | `AD W/notes.md` (another desk) · `?? PROME/inbox/P` | rc 0, P YOURS, notes `[not yours]` | same | **rc 128, 0 lines** | ✅ |
| A2b | `AD W/notes.md` alone | rc 0, `[not yours]` | same | — | ✅ |
| A3 (N4-4b) | `RD W/STATUS.md -> W/STATUS2.md` · `?? PROME/inbox/P` | rc 0, YOURS | same | **rc 128, 0 lines** | ✅ |
| A4 (N4-3a) | `D  "AGENTS/BARON/…/ARCHIVED prompts/bill_pulte_fhfa.md"` · `?? PROME/inbox/P` | rc 0, YOURS. The spaced path prints intact (quoted). | rc 0. Path printed as `prompts/bill_pulte_fhfa.md"` | **rc 128, 0 lines** | ✅ |
| A5 | `AD W/inbox/P` alone (my own packet, staged then deleted) | YOURS | YOURS | — | ✅ |
| A6 | `MD W/inbox/P` (committed) · `?? PROME/inbox/y` | y YOURS; P `[already committed]` | both YOURS | — | ✅ |
| A-loc | A2 and A5 under `LC_ALL` = C, POSIX, C.UTF-8 and en_US.UTF-8 (not installed, adds a setlocale warning line) | rc 0, labels identical | — | — | ✅ order-independent now |

### B — delta read's same-name and filing cases (D4-2, D4-3) and the ACs

| ID | State | r2 | HEAD | Verdict |
|---|---|---|---|---|
| B1 (N4-2) | committed `W/inbox/P`; W plain-mvs it to `processed/`; my **new** P at `PROME/inbox/P` | **PROME P YOURS**; both W halves `[already committed]` | all 3 YOURS | ✅ D4-2 closed |
| B2 (N4-2b) | W plain `rm` (or `git rm`, B2g); my new PROME P | PROME P YOURS; W deletion `[already committed]` | both YOURS | ✅ |
| B3 (E3) | W `git rm`; my **staged** PROME P. Git pairs these as `R  W/inbox/P -> PROME/inbox/P` | YOURS (cross-tree) | YOURS | ✅ |
| B4 (N4-7) | my `git mv` of the delivered P from W to PROME | YOURS | YOURS | ✅ D4-3 closed |
| B5 (N4-7b) | my plain `mv` of the delivered P from W to PROME | PROME P YOURS; the W deletion half is `[already committed]` | both YOURS | ⚠️ minor: the packet itself fires |
| B6 (author drill, AC4.1/4.2) | W `git mv` filing; untracked new `p2` in `W/inbox/` | p2 YOURS; `processed/P` `[already committed]` | both YOURS | ✅ |
| B7 | W plain-mv filing (`␠D` + `??`), nothing else | both `[already committed]` | both YOURS (the original false alarm) | ✅ |
| C1b′ / C2d | W `git mv` filing, plus my **new** P at `W/inbox/DEWEY/P` or at the original path | new P **YOURS** | YOURS | ✅ `R` entries never feed DELETED, so the dominant filing method (P3) cannot hide a new packet |
| B8 (ME=PROME) | NEXUS files two PROME packets (one by git mv, one by plain mv); a new `z` to NEXUS; an untracked `PROME/inbox/w` | z YOURS; the 3 filing paths `[already committed]`; `PROME/` filtered | all YOURS | ✅ |
| B9 (ME=NEXUS, name arm) | `␠M AGENTS/AEOLUS/NEXUS_BRIEF.md` · `?? AGENTS/AEOLUS/NEXUS_note.md` | note YOURS; BRIEF `[already committed]` | both YOURS | ✅ |
| B10 | clean tree; separately, only own-dir and `scripts/` lane changes | clean line, unchanged text | same | ✅ AC4.3 |
| F4-b | `?? W/inbox/…_from-DAEDALUS_bundle/` | YOURS | YOURS | ✅ still closed |
| C11 (unmerged; delta read's Not-checked) | `DU …_dm.md` · `UD …_md.md` · `AA W/inbox/P` | rc 0; DU and AA YOURS; UD (present in HEAD) `[already committed]` | all YOURS | ✅ |
| C9a | unborn HEAD (`git init`): `AD` plus `??` packets | rc 0, both YOURS | — | ✅ |
| C9c | run from a subdirectory cwd (`AGENTS/DAEDALUS`) | rc 0, YOURS | — | ✅ |
| Live | read-only parity for DAEDALUS, PROME, OTTO, NEXUS, WALTER (live tree: 1 `␠M`) | rc 0, label sets identical to HEAD | — | ✅ |

### C — new counterexamples

| ID | State | r2 | HEAD | Verdict |
|---|---|---|---|---|
| **C2** | W **`git rm`** of my delivered P (staged `D␠`), then I write a **new** P (different content) at the **same path**. Porcelain shows `D␠ W/inbox/P` and `?? W/inbox/P`. | One line: `[already committed — not yours now] W/inbox/P` plus **"do NOT commit"** (both entries share a dst; `sort -u` folds them) | YOURS | ❌ dangerous direction, regression |
| C2b / C2c | same resend, but W used plain `rm`, or plain `mv` to `processed/` (the path becomes `␠M`) | YOURS (C2c also over-warns on W's filed copy) | YOURS | ✅ safe |
| **C3** | W `git rm` of my **older** packet A (staged) while my **new**, ≥50 %-similar packet B in the same tree is **staged, not yet committed**. Git pairs them: `R  W/inbox/A -> W/inbox/B` | B `[already committed]` plus "do NOT commit" | YOURS | ❌ dangerous direction, regression |
| **C3b** | as C3, but A is **another sender's** packet (`2026-10-12_from-RED_challenge.md`) with similar boilerplate | B `[already committed]` | YOURS | ❌ same mechanism; the deleted file need not be mine |
| **C12b** | W **plain** `rm` of the similar file (unstaged) while my B is **intent-to-add** (`git add -N`). Pairs as `␠R A -> B` | B `[already committed]` | YOURS | ❌ same mechanism (rare: needs `-N`) |
| C3c / C3d (bounds) | C3b with B untracked, or with B staged but W's rm unstaged | B YOURS | YOURS | ✅ pairing needs **both** sides in the index (or i-t-a) |
| **C1′** | W plain-mvs my P to `processed/`; I write a **new** P (different content) to `W/inbox/DEWEY/P`, same tree, other folder | all 3 `[already committed]` | all YOURS | ⚠️ dangerous direction; this is the residue the delta read named. P1 and P2 make it rare: senders write to the top level, and the same basename twice in one tree occurs 2 in 6,133. |
| C7 (ME=PROME) | C1′ with PROME's packet in `AGENTS/NEXUS/inbox/WALTER/` | `[already committed]` | YOURS | ⚠️ = C1′ |
| C1 (`WILL/`) | as C1′, but into `W/inbox/WILL/` | the new file never appears in status (gitignored), in **both** versions | — | ⚠️ pre-existing, outside the script's view |
| C5a / b / e | `git mv` filing, or plain-mv filing, of a delivered packet whose name contains a space or `"` (porcelain quotes it) | YOURS (over-warn). `committed()` never matches a quoted path, and quoted paths never enter DELETED. | YOURS, but displayed mangled (`b_from-…md"`) | ⚠️ safe; display improved |
| C5c | untracked packets with ` -> `, `\|`, `é` or a newline in the name | all YOURS. ` -> ` still displays as `b_from-DAEDALUS_x.md"` (E1) | same | ⚠️ safe, pre-existing |
| C5d | `git mv` filing of a committed name containing `\|` | YOURS (over-warn), displayed as `q_from-DAEDALUS_x.md\|AGENTS/WALTER/inbox/processed/p\|q_…` | YOURS, clean display | ⚠️ safe; a minor display regression (the `\|` field separator) |
| C12a / C12c | `.R` filing (plain mv plus `add -N` on dst); `core.quotePath=false` with `é` (plain-mv filing plus a new PROME copy) | C12a `[already committed]`; C12c: filing delivered, PROME copy YOURS | YOURS | ✅ |
| C6a / b / c (LANE2) | DAEDALUS git-mvs or plain-mvs a committed `scripts/` file into `W/inbox`; lookalikes `scriptsX/` and `AGENTS/DAEDALUSX/`; ME=RED sees `scripts/` | YOURS; lookalikes are not own (correct); RED → `scripts/orphan_check.sh` `[not yours]` | same | ✅ |
| C7b (ME=PROME) | a desk `git mv`s PROME's packet into `PROME/inbox/` | clean line. The rename is filtered on its dst; the staged source deletion in the desk tree is unreported (N4-6). | same | ⚠️ pre-existing; not an unsent packet |
| C7c (ME=WALTER) | `_to-HANS_…WALTER` name: one filed by `git mv`, one new | new YOURS; filed `[already committed]` | both YOURS | ✅ |
| C8a | 5,000 untracked files in `AGENTS/HENRY/inbox/` plus my PROME P (5,001 entries) | rc 0, P YOURS. **20.1 s** | rc 0, **0.10 s** | ⚠️ perf |
| C8b | PROME plain-mvs all 1,356 `processed/` packets to `PROME/archive/` (2,712 entries; DELETED ≈ 112 KB) | rc 0. 274 `[already committed]` (137 D + 137 `??`), **0 flipped**. 18.8 s | — | ✅ / ⚠️ perf |
| C10a | my packet inside a **new untracked subdir** (`?? W/inbox/urgent/`) | `[not yours]` plus "do NOT commit" | same | ❌ **pre-existing** (D4-4/N4-8), not a regression |
| C10b | `status.showUntrackedFiles=no` in config | false clean line | same | ⚠️ pre-existing |

### `owner_of` unit table (sourced alone under `set -euo pipefail`; every call rc 0)

| Input | Owner | Input | Owner |
|---|---|---|---|
| `PROME/inbox/x.md`, `PROME/inbox/WALTER/x.md`, `PROME`, `PROME/` | `PROME/` | `AGENTS/WALTER/inbox/x.md`, `AGENTS/WALTER/` | `AGENTS/WALTER/` |
| `AGENTS/WALTER` (no trailing path), `AGENTS`, `AGENTS/` | `AGENTS/` | `memory/auto/x.md` | `memory/` |
| `top_from-DAEDALUS_x.md` | `top_from-DAEDALUS_x.md/` | `"AGENTS/WALTER/inbox/a b.md"` / `"PROME/inbox/a b.md"` | `"AGENTS/` / `"PROME/` (collapsed, but harmless: quoted paths never enter DELETED, see C5) |
| `AGENTS//x.md` | `AGENTS//` | `-n`, `AGENTS/-e/x.md` | `-n/`, `AGENTS/-e/` (no echo-option capture) |

## Findings

### Delta-read findings re-checked

| ID | Verdict | Evidence |
|---|---|---|
| D4-1 crash (rc 128, empty output) | ✅ **closed** | A1–A4 reproduce rc 128 with 0 lines on r1, and give rc 0 with YOURS on r2. Both `if committed; then …; fi` (the loop now always ends 0) and `\|\| true` guard it. The result no longer depends on order (A-loc). Unmerged states, unborn HEAD, `.R` entries and 5k/2.7k-entry statuses all give rc 0. |
| D4-2 basename coincidence across trees | ✅ **closed** for cross-tree | B1, B2, B2g, B3 → YOURS. Residue: same-tree cases (R3-3, and R3-1/R3-2 below). |
| D4-3 my own re-route of a delivered packet | ✅ closed | B4 → YOURS. B5's deletion half reads delivered, but the packet itself fires. |
| D4-4 new untracked subdir | ❌ **unchanged, pre-existing** | C10a. Not a regression; see R3-6. |
| D4-5 mode / stale comment | ✅ mode / ⚠️ comment | The candidate is now 755, matching HEAD's 100755. The header's "Paths containing spaces mangle in the awk $NF split" (lines 45–46) is stale: r2 no longer splits on `$NF`, and spaced names are now intact but always YOURS. |
| F4-e label text | ⚠️ unchanged | AC4.1 (working-tree acceptance doc) still specifies `[delivered — recipient's change]`; the code prints `[already committed — not yours now]`. |

### New findings

| ID | Verdict | Finding | Repair (smallest) |
|---|---|---|---|
| **R3-1** | ❌ (rare) | **A staged deletion at the same path hides a same-path resend (C2).** `D␠ path` + `?? path` → the `??` basename matches DELETED in the same tree → "do NOT commit" on new, never-sent content. HEAD: YOURS. This needs a recipient's **`git rm`** (staged, not plain `rm` or `git mv`) of my delivered packet, my same-name resend to the same path, and my closeout before the recipient commits. | A `??`/`A` entry whose content differs from the deleted committed blob is new work → MINE (R3-7) |
| **R3-2** | ❌ (rare) | **Git's rename pairing launders my staged packet into a "filing" (C3, C3b, C12b).** Porcelain pairs any staged deletion in the same tree with my staged (or `-N`) packet once they are ≥50 % similar. The R arm then checks owner and committed-src only. The deleted file **need not be mine** (C3b, a RED packet). HEAD: YOURS. Bounds (C3c, C3d): it needs both sides in the shared index, i.e. my packet staged but uncommitted at closeout (a failed `git add && git commit`) plus another session's staged deletion of a templated look-alike in the same tree. | R arm: require the index blob of dst to equal `HEAD:src` (a true filing is R100: 6,128 of 6,132, P3) |
| **R3-3** | ⚠️ (known) | **Same-tree, same-basename plain-mv residue (C1′, C7).** As named in the delta read's Not-checked list. A `git mv` filing does not trigger it (C1b′, C2d). Rare by P1 and P2. | Closed by the same content check (R3-7) |
| R3-4 | ⚠️ safe | Over-warnings, all toward YOURS: quoted names are never classed delivered (C5a/b/e); cross-tree filings by a recipient read YOURS; `\|` in a renamed name and ` -> ` in any name mangle the **display** (C5c/d), but the YOURS label holds. B5's deletion half is the only `[already committed]` on my own action, and its packet fires. | — (accept) |
| R3-5 | ⚠️ minor | **Speed: about 4 ms per entry**, from per-entry `echo \| grep` and `owner_of` forks. 5,001 entries → 20.1 s (HEAD 0.10 s); 2,712 → 18.8 s. The gate's `sh()` timeout is 180 s, so C1 turns UNKNOWN (rc None) only above roughly 45k entries, and fails loud rather than silent. The live tree had 1 to 43 entries today. | Optional: one `grep`/`awk` pass for the pattern and own-filter |
| R3-6 | ❌/⚠️ **pre-existing** (HEAD identical) | A packet in a new untracked directory → `[not yours]` + "do NOT commit" (C10a). This includes a first packet into ATHENA, CATO or SENTRY, whose `inbox/` holds no tracked file (P4). `status.showUntrackedFiles=no` gives a false clean (C10b). Gitignored dirs such as `W/inbox/WILL/` are invisible (C1). If `git status` itself fails, `\|\| true` prints the clean line (by reading, not run). | `git status --porcelain=v1 --untracked-files=all` closes C10a and C10b, as a separate change |
| **R3-7** | probe ✅ | **A content-identity rule closes R3-1, R3-2 and R3-3 without losing a true filing.** It is three lines on r2 (`probe_content.sh` `9905bea1659c`): DELETED stores `owner\|base\|HEAD-blob`; `??`/`A` matches on `git hash-object` of dst (falling back to the index blob); R requires `:dst` = `HEAD:src`. Probe runs, all rc 0: B6, B7, B8, B9, C2r (`git rm --cached`, same content) and C12a → filings still `[already committed]`. **C1′, C2, C3 and C12b → YOURS.** A1, A3 → YOURS; B10 → clean line. C2 then prints the path twice, once YOURS and once delivered (YOURS fires). Content-changed filings (14 of 6,132, P3) fall to YOURS, the safe side. Residue: a byte-identical, same-name copy in the same tree still reads delivered, but its bytes are already in that tree's HEAD. | — (this is the repair) |

## Direction judgement (question 3)

| Direction | Cases | Assessment |
|---|---|---|
| Over-warning (YOURS on someone else's or a delivered change) | R3-4, B5, C2c | **Safe**, as the brief defines it |
| "do NOT commit" on a never-sent packet, **new in r2** | R3-1 (C2), R3-2 (C3/C3b/C12b), R3-3 (C1′/C7) | **Dangerous**. Each needs a same-tree coincidence in the shared index: a staged `git rm`, my staged-but-uncommitted packet, or a same-basename write outside the inbox top level. None was observed in the population (P2, P3). HEAD said YOURS in all of them. |
| "do NOT commit" on a never-sent packet, pre-existing | R3-6 (C10a) | Dangerous, but HEAD is identical; not a regression |
| Silence or a crash | — | **None found**: rc 0 with output in every r2 run (53 states, about 70 runs) |

## Verdict

| Fix | Verdict | Basis |
|---|---|---|
| **4** `orphan_check.sh` r2 (`05ac8b6d…`) | **ACCEPT-WITH-RESIDUE**, and the residue is **not** all safe-direction | Both delta-read ❌s are closed: D4-1 is reproduced on r1 and gone on r2, and D4-2 holds cross-tree. AC4.2 and AC4.3 hold, and the original false alarm (B7, B9) is gone. The always-exit-0-with-output half of the property held in every state I ran. The always-YOURS half fails in three **rare, same-tree** states that HEAD handled correctly (R3-1, R3-2, R3-3). **Recommended before install:** take the R3-7 content-identity rule (3 lines, probed above) and re-run `tools/lib.sh` groups A, B and C on it. If the property is held absolute ("ALWAYS"), r2 as-is is REJECT until R3-7 lands. Records: align AC4.1's label (F4-e), refresh the stale header line (D4-5), and treat `--untracked-files=all` (R3-6) as its own change. |

## Not checked

- R3-7 is a scratch probe, not a reviewed candidate. I ran it on 13 states only (B6, B7, B8, B9, B10, C1′, C2, C2r, C3, C12a, C12b, A1, A3), not on C8 or the C5 quoted set.
- A full gate closeout (`daedalus_gate.py closeout`) with r2 installed was not run. C1's consumer was read instead (gate lines 241–251: rc≠0 → UNKNOWN, a `likely YOURS` line → DUE, otherwise CLEAN) and follows from the labels above.
- Status entries for `T` (typechange), `C` (copies under `status.renames=copies`), submodules and symlinked dirs.
- A real concurrent-session race (two processes mutating the shared index during the run); only static states were tested.
- en_US.UTF-8 collation (the locale is not installed; it only added a warning line) and non-GNU grep.
- The `git status` failure path (corrupt index, dubious ownership), which was assessed by reading only.
- Companion records (EVOLUTION entry, CHECKS.tsv `orphan_check` row, gate spec §8) and Fix 1, 2 and 3: out of scope.
