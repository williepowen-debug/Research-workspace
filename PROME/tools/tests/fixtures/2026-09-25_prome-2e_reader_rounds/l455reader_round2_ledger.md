# L455 independent read — ROUND 2 (the one allowed third read)
**Reader:** l455reader (Opus, did not write the fix). Read-only against the repo; throwaway repos `cx1…cx14/` and probes under this scratchpad. Diff read: `git diff -- PROME/tools/spawn_list.py PROME/tools/desk_activity.py` (uncommitted, correction 2) + the test file + `ACCEPTANCE_…L455.md` § Reader round 1.

## NOT VERIFIED — ❌ 2 · ⚠️ 5 · ✅ 9

The round-1 ❌1–3 and ⚠️2–3 are **fixed as reported**: every round-1 counterexample now reads correctly, and the population is unchanged (3,884 / LOST 0 / GAINED 383 / REJECTED 5, same five SHAs).

**But the ❌1 fix as written is NARROWER than the rule I validated.** Probe-4 said: if the ONLY home evidence is packets into the desk's own inbox, then NOT its own. The installed code says: if EVERY path is a packet into its own inbox, then NOT its own (`all(...)`, `spawn_list.py:145`). So as soon as the delivering commit touches one more path of any other kind, the packet-into-own-inbox falls through the loop's `continue` and the commit is attributed. That kind of path is a packet into a second desk, a `memory/auto/` file, or a `scripts/` file.

Separately, a lane packet two levels deep inside the desk's own inbox is not a `_PACKET` match, so it counts as home evidence.

Four new false-ACTIVE counterexamples: CX8, CX9, CX10, CX12. All are **latent**: 0 instances in the 3,886-commit no-merges population since 9/1, and 0 two-level lane paths in the whole repo.

**A population-neutral fix exists (probe-5, 0 disagreements over 3,886 commits × 46 desks).** But `spawn_list.py` is CLOSED for the session under the two-correction stop. So these go to declared residue plus a next-session row, unless Will says otherwise.

**WQ-229 states:** IMPLEMENTED ✅ · TESTED ✅ (22/22) · INDEPENDENTLY VERIFIED ❌ · STILL UNRESOLVED: ❌R2-1, ❌R2-2 below; ⚠️R5 and ⚠️4–6 as declared; ⚠️ new below.

---

## ❌ Findings

### ❌R2-1 — an own-inbox packet plus ANY other non-refuting path is attributed to the recipient (CX8 · CX9 · CX12)
- **Claim:** The "only own-inbox packets ⇒ False" guard uses `all()` over ALL paths, not over the HOME paths. A delivery into desk X's inbox under a subject naming X is credited to X whenever the same commit also carries any path the loop `continue`s past or treats as un-homed:
  - a second packet into another desk (PROME's multi-recipient send)
  - `memory/auto/`
  - `_SHARED_LOGS`
  - `scripts/`

  This is round-1 ❌1 surviving in a wider shape. It contradicts the record's own wording: "mail INTO the desk's own inbox is the SENDER's act".
- **Artifact:** `PROME/tools/spawn_list.py:143-146` (`if any(p.startswith(home) and not _PACKET.match(p) …): return True` then `if paths and all(_PACKET.match(p) and p.startswith(home) for p in paths): return False`), then the loop `:147-153`, where `_PACKET.match(p)` ⇒ `continue` for the own-inbox packet.
- **Verification command:** `cd /home/willi/Research-workspace && python3 - <<EOF … exec(cx.py helpers) …` (throwaway repos `cx8`, `cx9`, `cx12`; each has a `HAWK: baseline` own commit first):
  - CX8, PROME: `HAWK and BROCK re-grade packets (PROME L420/L433)` → `AGENTS/HAWK/inbox/…from-PROME_a.md` + `AGENTS/BROCK/inbox/…from-PROME_b.md`
  - CX9, MIDAS: `HAWK L433 packet + lesson filed (MIDAS)` → `AGENTS/HAWK/inbox/…from-MIDAS_r.md` + `memory/auto/finding_x.md`
  - CX12, DAEDALUS: `HAWK check repaired and notified (DAEDALUS)` → `AGENTS/HAWK/inbox/…from-DAEDALUS_r.md` + `scripts/claim_check.py`
- **Observed:**
  - `last_self_commit(HAWK)` = `d536835` / `5eb6f75` / `602d49a`, the delivering commit each time.
  - `desk_activity.last_commit` agrees: `d53683503` / `5eb6f75d0` / `602d49ab4`.
  - **False ACTIVE ×3** → a due HAWK row is silently NOT spawned.
  - CX8 is the most realistic shape: PROME sends to several desks in one commit with a recipient-led subject.
  - Population: 0 instances (probe-5 agrees with the installed rule on all 3,886 commits, so no live commit takes this path).
- **Proposed change (probe-5):** Define own-home evidence as `p.startswith(home) and (not p.startswith(home+"inbox/") or p.startswith(home+"inbox/processed/"))`. If any path is own-home evidence ⇒ True. If any home path remains (it can only be inbound mail) ⇒ False. Otherwise fall through to the existing loop. Result: population disagreements with the installed rule = **0** / 3,886 commits × 46 desks; CX8/CX9/CX12/CX10 → False; WALTER 0542eff05 shape → True; AEOLUS `processed/` drain → True. Add CX8 and CX9 as fixtures. The existing `test_reader_cx1…` covers only the two-path and one-path shapes, which is why it passed.

### ❌R2-2 — a packet in a TWO-level lane of the desk's own inbox counts as home evidence (CX10)
- **Claim:** `_PACKET` admits one lane level (`(/[^/]+)?`). `AGENTS/HAWK/inbox/WALTER/urgent/SIG-970.md` is therefore "a home path that is not a packet", which is own-home evidence, so the delivering commit is credited to HAWK. In round 1, ⚠️4 (lane depth) failed toward DARK because the lane was in ANOTHER desk's inbox. In the desk's OWN inbox the same regex gap fails toward **ACTIVE**, so the declared residue ⚠️4 is mis-labelled as DARK-only.
- **Artifact:** `PROME/tools/spawn_list.py:106` (`_PACKET`), `:143`; `ACCEPTANCE_…L455.md` § Reader round 1 residue "⚠️4 … fails toward DARK".
- **Verification command:** throwaway `cx10`: `HAWK: baseline` → `AGENTS/HAWK/STATUS.md`; WALTER: `HAWK SIG-970 routed (WALTER)` → `AGENTS/HAWK/inbox/WALTER/urgent/SIG-970.md`. Real-repo check: `git ls-files | grep -E '^AGENTS/[^/]+/inbox/[^/]+/[^/]+/' | grep -v processed` and `git log --since=2026-09-01 --format= --name-only | grep -E '^AGENTS/[^/]+/inbox/[^/]+/[^/]+/' | grep -v /processed/`.
- **Observed:**
  - `last_self_commit(HAWK) = ('2026-09-25','05919c7')`; desk_activity agrees with `05919c753`. **False ACTIVE.**
  - Real repo: 0 two-level lane paths in the tree, and 0 committed since 9/1. Latent.
- **Proposed change:** The probe-5 home-evidence rule above closes it, because it tests the `inbox/` prefix, not `_PACKET`. Correct residue ⚠️4's direction in the record: "DARK in another desk's inbox; ACTIVE in its own".

---

## ⚠️ Findings

### ⚠️R2-1 — "any quoted path ⇒ False" also refuses an ordinary own commit (CX11), so condition 1 fails toward DARK
- **Artifact:** `spawn_list.py:139-140` (the quoted check runs BEFORE the home-evidence check).
- **Command:** throwaway `cx11`: `BROCK closeout 2026-09-25` → `AGENTS/BROCK/STATUS.md` + `AGENTS/BROCK/notes/café_crème.md`.
- **Observed:**
  - `last_self_commit(BROCK) = ('2026-09-25','8974fef')`, which is the older `BROCK: baseline`. The closeout is lost. False DARK (visible direction, so condition 9 is respected).
  - Quoted paths in the ENTIRE history: `git log --format= --name-only | grep -c '^"'` = **0**.
- **Proposed change:** Move the quoted-path refusal to after the own-home-evidence test, as probe-5 does. CX11 → True, CX3 stays False, population disagreements 0. Or add `-c core.quotePath=false` to both log calls and keep the refusal for the residual (tab / newline / `"`) cases. Declare it if the file stays closed.

### ⚠️R2-2 — `attributed`'s docstring now contradicts the code
- **Artifact:** `spawn_list.py:120-131`. It still says "any path under the desk's home ⇒ its own" and "only packets / memory/auto/ / un-homed paths / no paths at all ⇒ its own". Since correction 2, own-inbox packets are NOT home evidence and a quoted path refuses.
- **Command:** `sed -n 120,146p PROME/tools/spawn_list.py`
- **Observed:** Two docstring bullets are false against the code at `:139-146`. A future editor reading the docstring as the contract would re-introduce round-1 ❌1.
- **Proposed change:** Rewrite the bullets with the next substantive fix; do not spend a correction on it alone. Declare it in the residue.

### ⚠️R2-3 — `test_merge_commits_are_never_attributed` mutates the shared class fixture
- **Artifact:** `test_spawn_list_desk_commit_attribution_L455.py:174-182` (checkout / commit / merge on `cls.repo` inside a test method).
- **Command:** code read. unittest runs methods alphabetically, so `test_overlap_*`, `test_prome_*`, `test_reader_*`, `test_sibling_*`, `test_strong_*` and `test_wrong_owner_*` run after the extra OTTO commits land.
- **Observed:** It passes today (22/22) because no later test asserts OTTO's newest commit. Any future OTTO assertion placed after `m…` alphabetically becomes order-dependent.
- **Proposed change:** Build the merge in its own throwaway repo in `setUp`, or in a separate TestCase. Low priority.

### ⚠️R2-4 — carried: R5 (PROME `processed/` move inside a desk's inbox, CX2) · ⚠️4 lane depth (re-labelled by ❌R2-2) · ⚠️5 lazy import · ⚠️6 registry
- **Artifact:** `ACCEPTANCE_…L455.md` § Reader round 1 declared residue.
- **Command:** re-ran `cx2`.
- **Observed:** CX2 is still attributed to BOND (`362898c`), as declared. The ⚠️5 and ⚠️6 text matches my round-1 findings.
- **Proposed change:** Only ⚠️4's direction wording needs correcting (see ❌R2-2).

### ⚠️R2-5 — probe-5 is a validated rule, not validated code
- **Artifact:** this ledger's probe-5 (heredoc in session).
- **Command:** population diff against the installed rule, plus the 9 named cases.
- **Observed:** 0 disagreements / 3,886 commits × 46 desks. Probe-4 also scored 0 in round 1 and was then transcribed as a narrower `all()` (that is ❌R2-1).
- **Proposed change:** Whoever implements it next session pastes probe-5 verbatim and adds CX8/CX9/CX10/CX11 as fixtures BEFORE the edit (WQ-229: acceptance first). A fourth reader is then needed, since this sitting's third read is spent.

---

## ✅ Findings

| # | Claim | Artifact | Command | Observed | Change |
|---|---|---|---|---|---|
| ✅1 | Suites green | test file; spawn_list; fail_closed; presence | `python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_spawn_list_desk_commit_attribution_L455.py` · `grep -c 'def test_'` · `--selftest` · `test_spawn_list_fail_closed.py` · `--cadence-selftest` · `test_presence_reader_contract.py` · `python3 -m unittest PROME/tests/test_presence_activity.py` | `Ran 22 … OK`, grep = **22** · 11/11 · 15/15 · PASS · PASS · `Ran 12 … OK` | none |
| ✅2 | Round-1 CX1 fixed | `:143-146` | re-ran `cx1` | HAWK stays at baseline `fbdf364` after both the MIDAS delivery and the PROME packet-only commit (the two-path and one-path shapes) | none |
| ✅3 | Round-1 CX3 fixed | `:139-140` | re-ran `cx3` | `last_self_commit(ZHAO) = None`, desk_activity `None` | see ⚠️R2-1 |
| ✅4 | Round-1 CX4 + CX7 fixed | `:105-106` | re-ran `cx4`, `cx7` | YURI `None` / `None` for both | none |
| ✅5 | Round-1 CX5 (merge) fixed in BOTH readers | `spawn_list.py:175`, `desk_activity.py:102` (`--no-merges`) | re-ran `cx5` | TERRY `None` / `None` | none |
| ✅6 | Condition 7 population | `:132-153` | `python3 <SP>/c7.py` | commits **3,884**, LOST **0**, GAINED **383**, REJECTED **5**: `c1405c40e` `2e38b1f24` `873e7d82c` `900afe854` `f4a509844` | none |
| ✅7 | Window + `--no-merges` + `--until` | `:175-178` | `win.py` (patched to `--no-merges`): 46 desks × 4 vintages, n=40 vs unlimited vs old reader; plus live `Liveness(None)` over 46 desks | flags **0**; no `!ERR`. Live sample: YURI `f0688f6ee`, BROCK `61cedd4ec`, RED `82b7ef9b9`, DAEDALUS `9b87c0909`, HAWK `ceb01e1e6` | none |
| ✅8 | The lead's suggested edges that hold | `:143` | `cx13`: `git mv AGENTS/HAWK/inbox/p.md → AGENTS/HAWK/research/p.md`, loose subject. `cx14a`: `AGENTS/HAWK/.claude/settings.json`. `cx14b`: `.claude/skills/…` + `PROME/.claude/skills/…` under a HAWK subject | cx13 → attributed (`604b492`; the rename prints only the new home path, and filing your own mail is your own act). cx14a → attributed (a desk's own `.claude/` is home). cx14b → NOT attributed (HAWK stays at `3b83466`). Correct in all three | none |
| ✅9 | Sibling parity held on all 14 counterexample repos | `desk_activity.py:96-109` | every `show()` above | identical verdicts in every case, including the ❌ ones (both readers are wrong together; the parity itself holds) | none |
