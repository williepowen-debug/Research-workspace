# L530 open leg — read_cap_check OWNER-DIRECTED NOTICE (isolated patch, 2026-10-08)

**State: IMPLEMENTED + TESTED. NOT INDEPENDENTLY VERIFIED. REVIEW: required** (it changes a gate's output contract: new report section, two new machine-line keys, one new opt-in flag). No reader has seen it.
**Not committed to `scripts/`.** DAEDALUS holds a standing Will-ruled 2026-07-31 grant over repo-root `scripts/`, but PROME's 2026-10-08 wake brief routes every `scripts/` change through a proposal + patch + packet, so this is a patch for PROME to apply, not a commit. Acceptance conditions (written first): `ACCEPTANCE.md`.

## What it does
READ_CAP rule 15 counts a cross-agent whole read in the READER's perimeter and promises the OWNER a notice. Before this patch the breach printed only in the reader's run: `--agent WALTER` showed HANS's THRESHOLDS.tsv at 103% of budget (WALTER:6b) and went rc 1, while `--agent HANS` never named the file, although HANS is the only desk that can rotate it.
- `foreign_reads()` scans READS.tsv through the existing `load_reads()`. CLASS rows are expanded with `_class_members()`, a helper factored out of `declared_reads()`, so both functions expand a glob the same way. Each file is graded with the existing `grade()`.
- In `--agent X`, a file X also reads itself is annotated in X's own row (`· ALSO read whole by WALTER:6b`). All other files appear once each in a new section: `OWNER-DIRECTED NOTICE` with path, bytes, % of budget, band and the foreign `reader:step`s.
- If nothing qualifies, an explicit clean line prints. A manifest that cannot be read at notice time prints `UNKNOWN` and never prints the clean line. A missing foreign file prints `DOES NOT EXIST — the reader's manifest defect`.
- READS.tsv has no `owner` column today. Owner is therefore the desk whose home contains the path. If someone populates an `owner` column that disagrees with the path, the patch prints `OWNER/PATH DISAGREE` and assigns the row to neither desk. `AGENTS/X/sub_agents/<S>/` belongs to S, not X.
- Machine line: `owner_notices=<n|UNKNOWN> owner_notices_over_budget=<n|UNKNOWN>` are added before `charter_bytes`, which stays last. Results with assessed=0 carry 0. **X's own counts and rc are unchanged by default.**
- `--owner-notice-blocking` (opt-in, `--agent` only) sets rc ≥1 when a foreign-read file of X is 🟠/🔴, and rc 2 when the notice is UNKNOWN. The output labels it **a CANON QUESTION for PROME/Will, NOT adopted**, because it would move rule 15's verdict onto the owner.

## Test receipts (scratch `git archive HEAD` at a3e8af6fa; never the live tree)
| Check | Before | After |
|---|---|---|
| `--selftest` | 112/112 rc 0 | **125/125 rc 0** (+13 legs N1–N8, `EXPECTED_LEGS` 112→125 in the same edit) |
| New legs on UNPATCHED code (legs-only variant) | **114/125, rc 1 — 11 of 13 new legs FAIL** | — |
| `test_read_cap_catchup_20261003.py` (`python3 -B -m unittest`) | 29 OK | 29 OK |
| `--fleet` output | rc 1 | rc 1, **byte-identical** |
| prome_gate `summarize_read_cap` on `--agent PROME --require-manifest --charter-mode explicit` | rc 0, parses | rc 0, parses, same verdict |

The two new legs that also pass on unpatched code are non-regression or negative legs, and they cannot fail where the feature is absent: N1's "owner rc unchanged" and N5's "sub-agent subtree not shown".

Live desks (scratch copy of HEAD; default mode):
| Desk | rc before | rc after | Machine line, before vs after | Notice |
|---|---|---|---|---|
| HANS | 0 | 0 | identical apart from the new keys | `owner_notices=2 owner_notices_over_budget=1` |
| CREED | 0 | 0 | identical apart from the new keys | clean line; 3 own rows annotated (STATUS←NEXUS:6, THRESHOLDS/FIRED_LOG←WALTER:6b) |
| WALTER | 1 | 1 | identical apart from the new keys | clean line. The only body diff is the size of `scripts/read_cap_check.py` itself, which WALTER declares as `summary` |
| DAEDALUS | 0 | 0 | identical apart from the new keys | clean line; STATUS annotated ←NEXUS:6 |

HANS after the patch:
```
  ✉️  OWNER-DIRECTED NOTICE [HANS] (READ_CAP rule 15): 2 file(s) under AGENTS/HANS/ that OTHER desks' declared boot reads load WHOLE — counted in THOSE readers' perimeters, NOT in this desk's totals or rc. …
     🟠 AGENTS/HANS/registry/THRESHOLDS.tsv   33,544 B   103% of budget  over budget (readable, no headroom)  ← read whole by WALTER:6b
     ✅ AGENTS/HANS/registry/HANS_T_FIRED_LOG.tsv   13,463 B    41% of budget  under 75% of budget  ← read whole by WALTER:6b
```

## Apply (PROME)
1. Precondition: `sha256sum scripts/read_cap_check.py` = `before` in `target_hashes.json` (b5fbd2fd…). If it differs, stop; do not three-way merge.
2. `git apply AGENTS/DAEDALUS/builds/readcap_owner_notice_2026-10-08/owner-notice.patch`, then confirm the result equals the `after` hash (ecd31652…).
3. `python3 scripts/read_cap_check.py --selftest` (expect 125/125) and `python3 -B -m unittest discover -s AGENTS/DAEDALUS/tests -p test_read_cap_catchup_20261003.py`.
4. `python3 scripts/read_cap_check.py --agent HANS`. Expect the THRESHOLDS notice line, rc 0. Then run the boot gate's read-cap leg unchanged.
5. Update DAEDALUS `CHECKS.tsv` (read_cap_check row) after the patch lands. That edit is DAEDALUS's.

## Residue (declared, not fixed)
- R1: the notice prints only for desks whose own perimeter was assessed. The early rc-2 returns (manifest unavailable, unattested, `--require-manifest` on an undeclared desk, heuristic CANNOT-EVALUATE) skip it, and their assessed=0 machine line carries 0, which that contract defines as an unearned count.
- R2: `--fleet` is deliberately unchanged. It computes the notice but neither prints nor totals it.
- R3: rule 15 says READS.tsv carries `reader` and `owner` as separate fields. The live header has no `owner` column, so that canon sentence is false today and is a READ_CAP text fix for DAEDALUS. The patch derives the owner from the path.
- R4: the whole-perimeter "every path on a multi-path boot line" leg of L530 stays PARTIAL, as previously adopted. This patch closes only the owner-measurement leg, and only as a notice; whether the owner's rc should be bound is the canon question in A9.
- R5: today's live evidence beyond HANS: NEXUS reads ZHAO/BROCK `NEXUS_BRIEF.md` whole at 39,556 B and 34,568 B (122% and 106% of budget). Under this patch both owners would see them in their own runs.

## Independent result read — 2026-10-08 (added after the read; the patch is byte-unchanged)
Fresh-context Opus reader, 23 own counterexample legs + an independent re-implementation (72 owner/file pairs, 0 missing) + before/after on 51 desks: **ACCEPT-WITH-RESIDUE, ❌ 0 · ⚠️ 8 · ✅ 14** — `INDEPENDENT_READ_2026-10-08.md`. No gate or consumer changes verdict.
**Do NOT apply before W1 and W2 are fixed** (both latent today, both cheap; DAEDALUS owes the fix + a result read, next touch 10/9): **W1** a foreign whole read under `AGENTS/X/sub_agents/<S>/` where S has no CLAUDE.md is shown nowhere and X's clean line is FALSE (MARCO has four such charterless sub-agent dirs today, 0 rows) — exclude a sub-agent dir only when it resolves as a desk home; **W2** a foreign `whole` row naming a directory prints "DOES NOT EXIST" — test `exists`, not `isfile`. Declared residue: W3 own-CLASS collapsed member hides the annotation (<70% only) · W4 TERRY `boot.py:300` row regex would read notice rows as TERRY boot surfaces (0 today; TERRY packet or a distinct leading token) · **W5 HANS's own closeout runner prints only `tail[-1][:78]`, so even after apply HANS sees THRESHOLDS only by running `--agent HANS` — the notice is pull-only; gate surfacing is a separate change** · W6 row classification re-implemented (root of W2) · W7 the opt-in blocking flag makes prome_gate's summary raise "rc contradicts" (fails closed) — adoption needs a consumer change, add to the canon question · W8 the WALTER receipt above also gains an ALSO-annotation and the clean line. State: IMPLEMENTED · TESTED · INDEPENDENTLY READ (ACCEPT-WITH-RESIDUE) · NOT READY TO APPLY until W1/W2.

## v2 — W1/W2 fixed (2026-10-08 afternoon, DAEDALUS)
`owner-notice.patch` is now **v2** (v1 kept byte-for-byte as `owner-notice_v1.patch`). Same base hash `b5fbd2fd…` (live `scripts/read_cap_check.py`, last commit 39178712a); result hash `e7f511e1…` (`target_hashes.json`). Delta vs v1, code only in `foreign_reads`:
- **W1:** `under_home` excludes `sub_agents/<S>/` only when `S/CLAUDE.md` exists (desk_home's own test). A charterless S, or a file directly in `sub_agents/`, stays with the parent.
- **W2:** a foreign concrete row naming a directory is skipped (not cap-bearing; the reader's run shows it); "missing" now means `not os.path.exists`.
- **Tests:** N5 fixture now gives S a CLAUDE.md (the chartered case). New **N9** (charterless sub-agent file read whole → noticed, no clean line) and **N10** (directory row → no DOES NOT EXIST). `EXPECTED_LEGS` 125 → 127.
**Watched:** v2 selftest 127/127 ✅. The same tests with only the two code fixes reverted fail exactly N9 and N10 (125/127), so both tests can fail. Live before/after on 43 FLEET_DIRECTORY desks: rc identical 43/43. Owners with an over-budget foreign read are BROCK (NEXUS_BRIEF 106%) and ZHAO (NEXUS_BRIEF 122%), both read by NEXUS:6; both were packeted today (`AGENTS/{BROCK,ZHAO}/inbox/2026-10-08_from-DAEDALUS_NEXUS_BRIEF-over-read-budget.md`). HANS = 0 over: HANS rotated THRESHOLDS 103% → 68% today, ae7bf8d27.
**State:** IMPLEMENTED · TESTED · v1 INDEPENDENTLY READ · v2 delta INDEPENDENTLY READ (below). W3–W8 remain declared residue, unchanged.

## v2 delta result read — 2026-10-08 (patch byte-unchanged since the read)
Fresh-context Opus reader, 16 own fixtures run on v1 and v2 + selftest + 51-desk live comparison: **ACCEPT-WITH-RESIDUE, ❌ 0 · ⚠️ 3 · ✅ 17**. **W1 FIXED · W2 FIXED.** `--fleet` byte-identical unpatched/v1/v2; live rc identical on 51 desks. Ledger `INDEPENDENT_READ_V2_2026-10-08.md`.
Declared residue (not fixed, so the artifact stays byte-stable under its read):
- **X1** (latent, inherited from v1): the sub-agent test is "CLAUDE.md present", not "desk_home resolves here". Three layouts would still hide a foreign read: a top-level desk with the sub-agent's name, one name under two parents, chartered-in-chartered. 0 exist today. The reader's resolver-based variant passes 127/127. Fix at the next touch, with its own read.
- **X2** (cosmetic, cannot occur in a committed tree): FIFO and trailing-slash rows disagree between owner and reader runs.
- **X3** (text): the selftest pass line still says "N1–N8".
**READY TO APPLY (PROME's slot):** `owner-notice.patch` (v2) onto live base `b5fbd2fd…` gives result `e7f511e1…`. Notice-only default; the opt-in blocking flag stays a canon question (A9/W7).
