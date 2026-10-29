# SURFACES currency sweep: reader report, 2026-10-28

**Reader:** read-only subagent for DAEDALUS · **Subject:** `AGENTS/DAEDALUS/SURFACES.tsv` (10,967 B, 13 data rows, header comment lines 2-4) · **Budget / cap used:** 32,550 B / 54,250 B · **Writes:** this file only. No tracked file edited, nothing staged.
**Method:** each claim was re-measured with `wc -c`, `git log -1 --format='%h %ad' --date=short -- <path>`, `grep -n`/`grep -c`, `git show --stat`, and read-only tool runs (`check_memory_length.sh`, `validate_all.py --only B3`, `reads_check.py --fleet`, `ledger_staleness.py --trade --all`). Receipts are inline.

---

## (a) Summary

| # | Row (SURFACES.tsv line) | Verdict | Stale cells | Headline |
|---|---|---|---|---|
| 1 | FORGE/ (:5) | **STALE** | Enforcing_mechanism, State, Notes | `position_agreement_check.py` has **0** FORGE references and scans `AGENTS/*/` only, so it does not reach FORGE/. The Gap cell is still true: `ledger_staleness.py` also has 0. The Notes vintage is replaced by the 10/22 ANVIL reconcile. |
| 2 | BOARD/ (:6) | **STALE** (minor) | Owner_provenance, Enforcing_mechanism, Notes | The INDEX matches disk (1,811 = 1,811). The quoted "WALTER owns all writes" no longer appears in WALTER's charter. The last commit is 10/28, not 9/24. |
| 3 | memory/auto/ (:7) | **STALE** | Gap | INDEX_COLD.md is now **46,655 B = 143.3 %** of budget / 86.0 % of cap (was 40,119 B / 123 %). MEMORY.md is 18,194 B = 71.1 %. |
| 4 | HEARTBEAT.md (:8) | **STALE — 🔴 mechanism blind** | Enforcing_mechanism, State, Gap, Notes | `check_heartbeat_chain()` moved to :1060 and **counts 0 against the live file's declared chain of 1**. The 35th-base format (10/26) defeats both of its regexes. |
| 5 | CLAUDE.md (root) (:9) | **STALE** | Enforcing_mechanism (line cite), Notes | `prome_gate.py:1407-1409` now holds calendar code. The `--mirror-map` prompt survives only as hint text at :1800. 23,257 B = 71.5 %. |
| 6 | AGENTS.md (:10) | **STALE** | Gap, Notes | `AGENTS.md:27-41` carries a hand-kept transmission-chain route table (declared at `_NETWORK.md:230`), so "no copy to drift" is false. 5,756 B. |
| 7 | MESSAGING/ (:11) | **STALE** (resolvable) | Gap, Notes | The allowlist was UNVERIFIED and is now verified: `config.yaml:6-7` BRENT/SAM match both desks' charters. The last commit is 2026-10-05, not 9/01. |
| 8 | SIGNALS/ (:12) | **STALE** (Notes) + token defect | State token, Notes | The banner is present at `README.md:3`. `DEAD-FROZEN-BANNERED` is in neither the file header nor STATE_VOCABULARY. AGENTS/SIGNALS.md's last row is now 2026-10-21, not 9/03. |
| 9 | scripts/ (:13) | **STALE** | Owner_provenance, Gap | "packet 004a9f91" resolves to no git object. Resolvable ACK: `0c37a3655`. Since 10/20 there have been 22 commits to scripts/, 11 of them by CATO (a desktop agent launcher). No CHECKS.tsv row covers them. |
| 10 | PROME/WILL_QUEUE.md (:14) | **STALE** (cites/counts) | Enforcing_mechanism (line), Gap, Notes | `check_will_queue` moved :641 → :850. B3 today: 22 rows, PASS. File is 147,468 B (declared summary/scoped only). Last commit 2026-10-28. |
| 11 | FORGE/timing/ (:15) | **CURRENT** | — | Banner present at `FORGE/timing/README.md:1`. Last commit 2026-08-30 (67a36afa4). Root Key Directories row at `CLAUDE.md:66`. |
| 12 | KERNEL/ (:16) | **STALE** (minor) | Enforcing_mechanism (count), Gap (a) | 10 dated activations, all revoked or expired (computed). `def test_` count is 220 (cell: 212). WQ-150 has no live carrier: absent from SCRATCH/STATUS/HANDOFF. |
| 13 | PROME/registry/READS.tsv (:17) | **STALE** | Gap | Today: 18 desks declared, 17 attested, **3 fresh** (CYPHER, FLG, ISHM), 14 stale, 1 not attested (OZK), 28 undeclared (reads_check rc=1). |
| — | Header comments (:3, :4) | **STALE** | — | `:3` cites `render_directory.py :120-124`; the guard is now at **:296-305**. `:4` defines 5 tokens, but rows use 7 distinct tokens, 5 of which are undefined there. See row 8 and §(b) header. |

**Totals:** 1 CURRENT · 12 STALE (1 of them 🔴, a blind mechanism).

---

## (b) Per-row detail

### Header comment lines (not data rows)

| Item | Cell claim | Measured | Verdict | Proposed |
|---|---|---|---|---|
| `:3` guard cite | `render_directory.py` co-registration guard (:120-124) | :120-124 is `counts`/`WF_NOT_APPLICABLE` code. The guard is at `render_directory.py:296-305` ("every FLEET_MAP agent absent from ROSTER tables MUST be handled" → `die(...)`) | STALE | "…co-registration guard (render_directory.py:296-305)…" |
| `:4` State vocabulary | ENFORCED · SCHEDULED · UNMECHANIZED · DEAD-UNBANNERED · UNASSIGNED | Tokens in use across the 13 rows: ENFORCED (4), PARTIAL (3), UNMECHANIZED (2), OWNED (1), ENFORCED-advisory (1), FROZEN-DECLARED (1), DEAD-FROZEN-BANNERED (1). **5 of the 7 are undefined in `:4`.** `grep -c` in `BLUEPRINTS/STATE_VOCABULARY.md`: ENFORCED 0, PARTIAL 0, UNMECHANIZED 0, FROZEN-DECLARED 0, DEAD-FROZEN-BANNERED 0, OWNED 1, SCHEDULED 6 | STALE | Extend `:4` to define every token used (PARTIAL, OWNED, ENFORCED-advisory, FROZEN-DECLARED, DEAD-FROZEN-BANNERED), or re-token rows to the defined set. The charter's STRICT-text bullet names "SURFACES" state cells as canonical-token surfaces, so this is self-owned debt. |

### Row 1: FORGE/ (:5)

| Cell | Cell value (short) | Measured now | Verdict |
|---|---|---|---|
| Owner_provenance | Will ruled 2026-07-30 ~12:25 ET (FORGE-audit S1) | Corroborated by root `CLAUDE.md:30` ("owner: PROME") and `:87` (PROME commits `FORGE/`). The 7/30 ruling text was not re-located (see §d) | CURRENT (by corroboration) |
| Enforcing_mechanism | `position_agreement_check.py --all` (PROME/BOOT.md:67) + ANVIL + PROME closeout | `grep -c FORGE scripts/position_agreement_check.py` → **0**. It scans `AGENTS/*/STATUS.md` + TRADE globs (`:36`, `:115`) and **does not reach FORGE/**. Invocation moved: `PROME/BOOT.md:76` now runs it inside `prome_gate.py boot` (BLOCKING). ANVIL = `.claude/agents/anvil.md` (`PROME/ROSTER.md:164`), manually spawned. `grep -n FORGE PROME/tools/prome_gate.py` → only :536 (regex) and :1063 (docstring), so there is no FORGE check | **STALE (misattributed)** |
| State | PARTIAL | No automated mechanism reaches FORGE/STATUS.md. The only reach is a manually spawned ANVIL reconcile per broker capture (last: 2026-10-22) | Propose **UNMECHANIZED** (owner exists; the reconcile is human-triggered) |
| Gap | `ledger_staleness.py` has 0 FORGE refs; path-teach owed by DAEDALUS | `grep -c FORGE scripts/ledger_staleness.py` → **0**. 8b1012baf (2026-10-22) changed rule 11 (single-word col cap 48) and SELF_FLAG_RE only. `TRADE_GLOBS` (`:573`) = TRADE.md / trade/TRADE.md / TRADE_BOOK.md / POSITIONS.md under agent dirs. `--trade --all` today: "27 agent(s) graded … 16 matched NO trade surface", no FORGE line | **CURRENT** |
| Notes | Header Updated 2026-09-20 (WQ-272, 68c688a57), 9/16 capture, 9/10 marks, "NO BROKER EXPORT EXISTS" | FORGE/STATUS.md header now: "2026-10-22 (Thu) — RECONCILE BY ANVIL to Will's Fidelity positions…pasted 11:01 ET", 25/25 rows tie $39,876.06, Robinhood unverified since 9/29. Last commit **ec5a7058b 2026-10-22** | **STALE** |

**Proposed cells**
- Enforcing_mechanism: "ANVIL reconcile per broker capture (manual PROME-directed spawn) + PROME closeout. No script reads FORGE/: position_agreement_check.py and ledger_staleness.py --trade both scan AGENTS/*/ only (0 FORGE references each)."
- State: `UNMECHANIZED`
- Gap: "ledger_staleness.py and position_agreement_check.py have 0 FORGE references, so FORGE/STATUS.md is outside every automated check; path-teach owed by DAEDALUS (scripts/ grant)."
- Notes: "Reconcile vintage lives in the FORGE/STATUS.md header only (root rule). Last reconcile 2026-10-22 (ec5a7058b, ANVIL, Fidelity capture); Robinhood rows unverified since 9/29. PORTFOLIO.md FROZEN Feb-2026."

### Row 2: BOARD/ (:6)

| Cell | Measured now | Verdict |
|---|---|---|
| Owner_provenance | `grep -n "owns all writes" AGENTS/WALTER/CLAUDE.md` → **no match**. Ownership is now carried at `AGENTS/WALTER/CLAUDE.md:81` (every dispatch writes `BOARD SIG-W-*` + `gen_board_index.py --write`) and `:102` (scope: WALTER/BOARD/…). Earliest BOARD/INDEX.md commit: 34d521d5c 2026-04-15 | STALE (quote) |
| Enforcing_mechanism | `walter_doctor.py` (168,063 B): `check_board_reconcile` :238 · `check_board_log_path_divergence` :934 · `check_delivery_claim_vs_git` :1138 · `check_log_reconcile` :1389 · `check_restated_set_drift` :1706 · `check_cluster_review_overdue` :1882. All are registered in the check table at :2955-2978. The doctor is invoked at `AGENTS/WALTER/CLAUDE.md:38` (boot step 0.5). The "(20 references)" figure cannot be reproduced: `grep -c -i board` = 120 | CURRENT (functions); STALE ("20 references") |
| State | ENFORCED | CURRENT |
| Gap | `gen_board_index.py` present (19,510 B); rowset sha256 stamp present at `BOARD/INDEX.md:3` | CURRENT |
| Notes | INDEX header `signals=1811`; `ls BOARD/SIG-W-*.md \| wc -l` = **1811**, so they agree (cell: 1042). Last BOARD commit **58ad6f5f7 2026-10-28** (cell: 6b153a52f 2026-09-24) | STALE |

**Proposed:** Owner_provenance: "AGENTS/WALTER/CLAUDE.md:81 (every dispatch writes BOARD/SIG-W-* and regenerates INDEX.md) and :102 (WALTER scope includes BOARD/); relocated from AGENTS/WALTER/signals/ 2026-04-14." Enforcing_mechanism: drop "(20 references)" and name the six check functions with the registry span :2955-2978. Notes: "INDEX header signals=1811 = 1,811 SIG-W-*.md on disk (2026-10-28). PAT-071 counter-example: outside AGENTS/ and healthy because the owner's mechanism reaches it."

### Row 3: memory/auto/ (:7)

| Item | Cell | Measured | Verdict |
|---|---|---|---|
| INDEX_COLD.md | 40,119 B = 123 % | **46,655 B = 143.3 % of budget, 86.0 % of cap**; last commit 022a98267 2026-10-15 (PROME) | STALE |
| INDEX_COLD_EMBEDDED.md | 16,692 B | 16,773 B = 51.5 % | STALE (small) |
| MEMORY.md | 19,110 B = 74 % | **18,194 B = 71.1 %** of 25,600. `check_memory_length.sh`: "24 lines (12% of 200), 18194 bytes (71% of 25600)", rc=0 | STALE |
| Whole-read exposure | "over budget for a whole read" | `grep INDEX_COLD PROME/registry/READS.tsv` → **0 rows**. No desk declares a whole read, so this is a size flag, not a declared read-cap breach | Clarify |
| Mechanism | `memory_index_check.py --strict --slug` at root step 1d | `scripts/memory_index_check.py` present; root `CLAUDE.md:81` (carve-out ③) and `:96` (step 1d) | CURRENT |
| Owner_provenance | carve-out ③ | `CLAUDE.md:81` | CURRENT |

**Proposed Gap:** "memory/auto/INDEX_COLD.md is 46,655 B = 143 % of the 32,550 B budget and 86 % of the 54,250 B cap (no READS.tsv whole-read declaration), so it is PROME's to rotate before it reaches the cap. MEMORY.md 18,194 B = 71 % of its 25,600 B boot cap."

### Row 4: HEARTBEAT.md (:8) 🔴

| Item | Cell | Measured | Verdict |
|---|---|---|---|
| Function location | `check_heartbeat_chain()` (:125-140) in Enforcing_mechanism; (:851) in Notes | `def check_heartbeat_chain` at **`PROME/tools/prome_gate.py:1060`**; called at :1930 (boot) and :2011 (closeout) | MOVED |
| Mechanism works? | "ENFORCED … run every PROME boot" | Applying the function's own regexes (`prome_gate.py` counted = `^>\s*(?:#{1,6}\s*\|\*\*)?AMENDMENT\s*#\d+`, declared = `^\*\*Amendments append.*?Chain:\s*(\d+)`) to the live file gives **counted 0, declared None**. The file self-declares "**Amendment chain: 1.**" (`HEARTBEAT.md:2`) and carries one `**Amendment 1 —` block (`:8`). History over the last 8 HEARTBEAT commits: the counted value matched the self-declared chain on every 34th-base version (bf02b4c81 → 83e9572de, chains 0-4). **From 6a3e1e364 (2026-10-26, 35th base) the block style changed to `**Amendment N —` (no `>`, no `AMENDMENT #`), and counted = 0.** The declared-chain cross-check (the 8/04 fail-loud repair) has matched **nothing** on any of those 8 versions, because the header no longer uses the "Amendments append … Chain:" form. Net: the check prints a PASS at any chain length. This is the same failure the function's own docstring (:1067-1071) records from 8/04 | **BLIND (🔴)** |
| State | ENFORCED | — | Propose **PARTIAL**: rule is prose-only in effect until the regex is repaired; the owner's check exists but cannot see the current format |
| Bytes | 24,349 B = 74.8 % | **16,567 B = 50.9 % of budget, 30.5 % of cap** | STALE |
| Base/chain | base 2026-09-22, twentieth re-base, chain 1 | **Base 2026-10-26, THIRTY-FIFTH base, chain 1** (`HEARTBEAT.md:2`) | STALE |
| Last commit | e215d1a06 2026-09-23 | **ef7b600c2 2026-10-27** (PROME) | STALE |
| Owner | PROME | READS.tsv:115 `READ PROME HEARTBEAT.md whole PROME:BOOT.md-5` | CURRENT |

**Proposed:** Enforcing_mechanism: "PROME/tools/prome_gate.py check_heartbeat_chain() (:1060; called :1930 boot, :2011 closeout; ADVISE, warn at 4)." State: `PARTIAL`. Gap: "check_heartbeat_chain is BLIND to the 35th-base format: its regexes require '> **AMENDMENT #N' blocks and an 'Amendments append … Chain: N' header, so the live file (one '**Amendment 1 —' block, 'Amendment chain: 1') counts 0 with no declared cross-check, and it passes at any chain length. Owner: PROME." Notes: "16,567 B = 51 % of budget / 31 % of cap; 35th base 2026-10-26, chain 1; last commit 2026-10-27 (ef7b600c2)."

### Row 5: CLAUDE.md (root) (:9)

| Item | Cell | Measured | Verdict |
|---|---|---|---|
| Mechanism | `consumer_check.py --mirror-map`, MANUAL advisory at PROME closeout (prome_gate.py:1407-1409) | `prome_gate.py:1405-1412` is now calendar-coverage and `check_memory_length` code. The only `--mirror-map` mention in prome_gate is hint text at **:1800**, inside `check_consumer_declared` (:1775). It runs only when a `--superseded` pair is declared, and it is never invoked as `--mirror-map`. `consumer_check.py` still parses the heading `### Canonical → Mirrors map` (:499, :503), which is present at `PROME/SYSTEM.md:50` | MOVED (weaker: hint-only) |
| State | PARTIAL | Still apt | CURRENT |
| Bytes | 24,236 B = 74 % / 45 % | **23,257 B = 71.5 % of budget, 42.9 % of cap** | STALE |
| Last commit | (not in cell) | 3d0f802a0 2026-10-24 (carve-out ⑤) | info |

**Proposed:** Enforcing_mechanism: "scripts/consumer_check.py --mirror-map (parses PROME/SYSTEM.md:50 'Canonical → Mirrors map'); prome_gate.py:1800 names it only as a hint inside check_consumer_declared, when a superseded figure is declared, so a run is manual." Notes: "Auto-loads into every session: 23,257 B = 71 % of budget / 43 % of cap; highest blast radius of any listed surface."

### Row 6: AGENTS.md (:10)

| Item | Cell | Measured | Verdict |
|---|---|---|---|
| Pointer lines | AGENTS.md:22/:27 point to ROSTER | ROSTER pointer at **`AGENTS.md:20`** and `:25` ("roster wins") | MOVED |
| Gap | "no copy to drift" | **`AGENTS.md:27-41` = a 12-row "Transmission chains" route table.** It is declared owned by AGENTS.md at `AGENTS/_NETWORK.md:230` ("`AGENTS.md` owns the compact transmission-chain table"), while root `CLAUDE.md` says topology is canonical at `_NETWORK.md` and "_NETWORK.md wins". No mechanism compares the two. `grep` for an enforcer in scripts/, PROME/tools/ and DAEDALUS/scripts → none. Most recent co-edit: 72cb4bcf4 2026-10-23 (WQ-507, ISHM route) touched both files in one commit | **STALE** |
| Bytes | 4,938 B (9 % of cap) | **5,756 B = 17.7 % of budget, 10.6 % of cap**; last commit 72cb4bcf4 2026-10-23 | STALE |
| State | UNMECHANIZED | Still apt | CURRENT |

**Proposed Gap:** "AGENTS.md:27-41 carries the compact transmission-chain table (owned there per _NETWORK.md:230) alongside the canonical topology in AGENTS/_NETWORK.md; nothing checks that the two agree (WQ-507 updated both by hand in one commit, 72cb4bcf4)." Notes: "5,756 B (11 % of cap). The roster table is retired (WQ-128); AGENTS.md:20/:25 point to PROME/ROSTER.md."

### Row 7: MESSAGING/ (:11)

| Item | Measured | Verdict |
|---|---|---|
| Allowlist | `MESSAGING/config.yaml:6-7` = BRENT, SAM. `AGENTS/BRENT/CLAUDE.md:205-209` and `AGENTS/SAM/CLAUDE.md:287-291` both process top-level `inbox/MSG-*.md` via `MESSAGING/tools/validate.py`, so the allowlist matches both desks' instructions | UNVERIFIED → **VERIFIED** |
| Tests | `MESSAGING/tests/test_msg.py`, `test_validate.py` present | CURRENT |
| env_doctor | `scripts/env_doctor.py:143-148` = PyYAML dependency only | CURRENT |
| Last commit | **88417ced3 2026-10-05** (WQ-385 runtime compatibility). Cell: 0430ca45f 2026-09-01 | STALE |

**Proposed Gap:** "No conformance reader for CROSS_SESSION_MESSAGING.md; MESSAGING/tests exercise the DM v1 tool, not rule conformance. Allowlist (config.yaml:6-7 BRENT, SAM) matches both desks' charters as of 2026-10-28." Notes: "Last commit 2026-10-05 (88417ced3, WQ-385); scripts/env_doctor.py checks only its PyYAML dependency."

### Row 8: SIGNALS/ (:12)

| Item | Measured | Verdict |
|---|---|---|
| Banner | `SIGNALS/README.md:3` "FROZEN 2026-08-11 — dead surface, do not cite as current" | CURRENT |
| WALTER tombstone | `AGENTS/WALTER/CLAUDE.md:53` step 7c lists `SIGNALS/inbound.md` as a retired feed | CURRENT |
| Residue | `SIGNALS/` holds README.md, archive/, briefings/, feeds.yml, inbound.md, seen.json; last commit 77404c56b 2026-08-29 | CURRENT |
| State token | `DEAD-FROZEN-BANNERED` is undefined in header `:4` and in STATE_VOCABULARY.md (0 hits) | DEFECT (self-owned) |
| Notes: AGENTS/SIGNALS.md | Cell: "last row 2026-09-03". Last rows dated **2026-10-21**; last commit 3747997c4 2026-10-22 (LIQUID) | STALE |

**Proposed:** State: a defined token (e.g. add `DEAD-FROZEN-BANNERED` to `:4`, or use `FROZEN-DECLARED`, which row 11 already uses). Notes: "…Not AGENTS/SIGNALS.md: that live cross-agent ledger (carve-out ②, last row 2026-10-21) has no row in this register (candidate C6)."

### Row 9: scripts/ (:13)

| Item | Measured | Verdict |
|---|---|---|
| Owner_provenance "packet 004a9f91" | `git rev-parse --verify -q 004a9f91` → none, and no file outside DAEDALUS's own SURFACES copies cites it. A resolvable record exists: **0c37a3655 2026-07-31** "DAEDALUS -> PROME: scripts/ grant ACK". The grant is restated at `AGENTS/DAEDALUS/CLAUDE.md:93` | STALE (dead pointer) |
| Mechanism | `AGENTS/DAEDALUS/CHECKS.tsv` present: 56 non-comment data rows (last edit 10/23). `validate_all.py --list` A1-A9 = 9 selftest legs (corrections_boot_check, docket_view, orch_log, claim_check, memory_index_check, consumer_check, ledger_staleness, memory_citation_census, read_cap_check) | CURRENT |
| Gap | Cell covers only the 10/20 cleanup. **Since 2026-10-20 there have been 22 commits touching scripts/: CATO 11, PROME 5, WALTER 4, DAEDALUS 2.** New files include `scripts/agents.py`, `agents_gui.py`, `agents_gui.ps1`, `install_agents.py`, `agents.json`, `AGENT_LAUNCHER.md`, `assets/agent-launcher.*`, `tests/test_agents_launcher.py`, `tests/probe_agents_gui.py`, `githooks/pre-commit`, `orch_time.py`. `grep -c -i "launcher\|agents.json" CHECKS.tsv` → 0. Last scripts/ commit 08398d421 2026-10-27 (CATO) | **STALE** |
| Evidence files | `runs/2026-10-20_ORGANIZATION_CLEANUP.md` present | CURRENT |

**Proposed:** Owner_provenance: "Will-ruled 2026-07-31 ~14:45 ET via PROME; DAEDALUS ACK 0c37a3655; charter AGENTS/DAEDALUS/CLAUDE.md:93. PROME retains PROME/tools/." Gap: "Since 2026-10-20, 22 commits by four authors touched scripts/ (CATO's desktop agent launcher, PROME's pre-commit hook, WALTER's orch_log repairs); none of the launcher files has a CHECKS.tsv row or an ownership decision. No whole shared-tool revalidation claimed."

### Row 10: PROME/WILL_QUEUE.md (:14)

| Item | Measured | Verdict |
|---|---|---|
| `check_will_queue` | `def` at **`prome_gate.py:850`** (cell :641); called at :1923 (boot) and :2005 (closeout) | MOVED |
| validate_all B3 | `python3 scripts/validate_all.py --only B3` (2026-10-28): "✅ B3 WILL_QUEUE.md typing [PASS, structural] **22** queue row(s), 7 cols, ids unique" (cell: 19 rows 9/24) | STALE (count) |
| Size | **147,468 B = 453 % of budget, 272 % of cap.** READS.tsv:118-119 declare PROME reads it `summary` (via prome_gate) and `scoped`; DAEDALUS `scoped` (:306). No whole read is declared, so this is not a read-cap breach | info (new) |
| Last commit | **01b5f92f9 2026-10-28** (cell: 57eb7e0a3 9/24) | STALE |
| Born | 090b28389 2026-07-30 present | CURRENT |

**Proposed Gap:** "none open: prome_gate.py check_will_queue (:850, advisory, both modes) plus validate_all.py leg B3 (22 rows PASS 2026-10-28). File is 147,468 B (2.7× cap) and declared summary/scoped only (READS.tsv:118-119)." Notes: "Operator-facing open-items ledger, single live copy; last commit 2026-10-28 (01b5f92f9)."

### Row 11: FORGE/timing/ (:15)

| Item | Measured | Verdict |
|---|---|---|
| Banner | `FORGE/timing/README.md:1` "FROZEN 2026-08-09 … do not cite as current" | CURRENT |
| Root row | `CLAUDE.md:66` "FROZEN research corpus (bannered 2026-08-09)" | CURRENT |
| Last commit | 67a36afa4 2026-08-30 (matches the cited pending-clause clear) | CURRENT |
| ledger_staleness | 0 FORGE refs (see row 1) | CURRENT |

No change proposed. Optionally add "(re-verified 2026-10-28)" to Last_reviewed only.

### Row 12: KERNEL/ (:16)

| Item | Measured | Verdict |
|---|---|---|
| Activation | `KERNEL/README.md:3` "NO ACTIVATION CURRENTLY LIVE". `:5` lists ten dated activation docs. Python check of all 10 `GATE_C_*ACTIVATION*_20*.json`: every one has `revoked_at` set and `window_end` ≤ 2026-09-02T17:00Z, so **0 LIVE** | CURRENT |
| Tools | `KERNEL/tools/git_policy_check.py`, `live_shadow.py`, `audit.py`; `KERNEL/policies/custody-policy.json:5-9` substitutes → `writer_id: RED`, registered_by WILL | CURRENT |
| Test count | Cell "212-test suite". `grep -c "def test_" KERNEL/tests/*.py` sum = **220** (methodology may differ from the original count; not run) | STALE (likely) |
| Provenance commits | 9bbf9c041 (2026-08-25 Gate A), a284c86bd (2026-08-30 root batch) both resolve | CURRENT |
| Gap (a) WQ-150 | Root ④ at `CLAUDE.md:82` keys on activation-file legs (text last changed a284c86bd). WQ-150 is not in `PROME/SCRATCH.md`, `STATUS.md`, `HANDOFF.md`, `DOCKET.tsv` or `WILL_QUEUE.md`. Last carriers: `PROME/HEARTBEAT_COLD.md:158` ("Owed by PROME: the WQ-150 root-④ edit … execute by ~9/8") and `PROME/archive/SCRATCH_ROTATED_2026-09-29_prome-e6c.md:10` ("Carried, not dated") | STALE (now **no live carrier**) |
| Last commit | becfe3516 2026-09-17 | CURRENT |

**Proposed Gap:** "(a) WQ-150 root-④ completion is UNVERIFIED and has no live carrier: last seen in archive/SCRATCH_ROTATED_2026-09-29 'Carried, not dated' and HEARTBEAT_COLD.md:158; (b) between sittings, shadow/events immutability rests on carve-out prose alone." Enforcing_mechanism: "…+ KERNEL/tests (220 test functions by grep, 2026-10-28)…"

### Row 13: PROME/registry/READS.tsv (:17)

| Item | Cell | Measured (2026-10-28) | Verdict |
|---|---|---|---|
| Signed/attested | "11 signed desks, 10 eligible" (10/20 pin) | `reads_check.py --fleet` (rc=1): "553 row(s) · **18** desk(s) with declarations · **17** validly ATTESTED · **28** desk(s) with NO declaration". Per-desk manifests: **fresh 3** (CYPHER 10/23, FLG 10/23, ISHM 10/26); **STALE 14** (AEOLUS, BOND, BROCK, CREED, DAEDALUS 10/09, FERT 10/26, HANS, NEXUS, PROME 10/20, RED 9/14, REGINALD, WAL, WALTER, YURI); **NOT ATTESTED 1** (OZK). File: 17 ATTESTATION · 100 BASIS · 436 READ rows | STALE |
| Roster | "live roster39 vs ruled37" | `PROME/ROSTER.md:37` header "ACTIVE (34)", with a vintage-snapshot warning at `:40`. reads_check counts 18 + 28 = 46 desks known. The 39/37 basis was not re-derived (see §d) | UNVERIFIED |
| Mechanism | reads_check + read_cap_check consumes | `PROME/tools/reads_check.py` runs. `scripts/read_cap_check.py:317` documents READS.tsv consumption | CURRENT |
| Size / last commit | — | 164,177 B; b18a87a3d 2026-10-26 | info |
| Evidence pin | `builds/l748_time_2026-10-20/RESULT.md` | present under `AGENTS/DAEDALUS/` | CURRENT |
| DAEDALUS's own attestation | — | **STALE (dated 2026-10-09)**: self-owned | flag |

**Proposed Gap:** "2026-10-28 reads_check --fleet: 18 desks declared, 17 attested, only 3 fresh (CYPHER, FLG, ISHM); 14 stale incl. DAEDALUS and PROME; OZK unattested; 28 desks undeclared. No freshness certification. Roster count reconciliation still owed by the declaration owner."

---

## (c) Candidate NEW rows (not added)

Scope test: load-bearing, shared, and outside every `AGENTS/<NAME>/`. Two items live under `AGENTS/` but in no agent directory (`AGENTS/*.md|tsv`); they qualify on the register's own definition (`SURFACES.tsv:2`).

| # | Surface | Size / last commit | Owner (source) | Enforcing mechanism | Suggested State | One-line gap |
|---|---|---|---|---|---|---|
| C1 | `docs/GIT_WORKTREE_PROCEDURES.md` | 3,185 B / c5286bf6d 2026-10-19 | PROME, Will-gated (root `CLAUDE.md` § Git Protocol "Before committing … read and execute … in full"; root shared doc per Scope note `:87`) | None found (grep across scripts/, PROME/tools/, DAEDALUS/scripts → 0) | UNMECHANIZED | Mandatory read before every fleet commit, with no check that it exists, stays aligned with root, or keeps its named sections. |
| C2 | `docs/CANON_PROVENANCE.md` | 19,826 B / 50504bc48 2026-09-18 | PROME, Will-gated (root `CLAUDE.md` header) | Self-described "parity test (REVIEW §5 test 3)" on `root-anchor:` phrases; `grep -rl "root-anchor"` in scripts/, PROME/tools/, DAEDALUS/scripts → **0** | UNMECHANIZED | The anchor-parity test it names has no runnable implementation found; 4 root edits since 9/18 (latest 3d0f802a0 10/24) went unchecked against it. |
| C3 | `USER.md` | 8,458 B / 463c3e457 2026-10-20 | PROME (Will-facing; operator rules incl. ⚖️ blocks cited by root Output Canon `CLAUDE.md:58`) | Referenced by read_cap_check / reads_check / spawn_list (path only) | UNMECHANIZED | Whole-read at many boots (DAEDALUS charter; READS rows) with no consistency check against root Output Canon. |
| C4 | `AGENTS/_NETWORK.md` | 12,924 B / 72cb4bcf4 2026-10-23 | PROME (root: canonical topology; "_NETWORK.md wins") | None found | UNMECHANIZED | Canonical topology with a hand-kept sibling table in AGENTS.md:27-41 and no agreement check (pairs with row 6). |
| C5 | `AGENTS/_INDEX.md` | 8,383 B / 5846500b5 2026-10-23 | `_NETWORK.md:231` ("owns grouped directory navigation"); committer PROME | `AGENTS/DAEDALUS/scripts/regen_patterns_hot.py` mentions the path only | UNMECHANIZED | Hand-maintained desk list (e.g. CYPHER row :62) can drift from PROME/ROSTER.md; no diff check. |
| C6 | `AGENTS/SIGNALS.md` | 12,792 B / 3747997c4 2026-10-22 | Shared; author-commits-own-row (root carve-out ②) | `PROME/tools/spawn_list.py` reads it | ENFORCED-advisory (to verify) | Live cross-agent log already flagged in row 8 Notes as having no row. |
| C7 | `AGENTS/SELF_RULINGS.tsv` | 13,068 B / ec166d1ae 2026-09-19 | Shared; ruling agent appends, carve-out ② (header :2); PROME reads at boot | `scripts/tsv_append.py` (append form); `spawn_list.py` reads | UNMECHANIZED (verify) | No row since 9/19 (40 d). Either the delegation tier is unused or rows are being skipped; the header calls an unrecorded ruling a violation. |
| C8 | `AGENTS/VOCABULARIES.tsv` | 7,074 B / cb861d3fb 2026-10-23 | Unstated in file; "Read by all agents at spawn when writing to KB.tsv" (header :3) | None found | UNASSIGNED | Header "Last updated: 2026-03-08" vs a 10/23 commit; no named owner; overlaps BLUEPRINTS/STATE_VOCABULARY.md. |
| C9 | `FORUM/` (README + standing buckets `banks/`, `orchestration/`, `keeper/`) | README 6,780 B / 3d0f802a0 2026-10-24 | Per-post authors (root carve-out ⑤, WQ-486 A, 10/24); README/charters/rulings "stay with their existing owners" | `scripts/firetime_check.py:119` includes FORUM/ in artifact roots (citation resolution only) | UNMECHANIZED | New commit carve-out (⑤, 10/24) with no register row; no check that commits stay within `<stamp>_<YOU>_<slug>.md`. |
| C10 | `PROME/registry/corrections_receipts.tsv` | 18,004 B / d116e8951 2026-10-28 | PROME (file); receipts written via `corrections_boot_check.py --receipt` | `scripts/corrections_boot_check.py`, `prome_gate.py` | ENFORCED (verify) | Shared R1 receipt ledger feeding every desk's boot step 5b; outside AGENTS-scoped checks. |
| C11 | `PROME/registry/WQ_LEDGER.tsv` (+ `.crc`) | **1,991,473 B** / 01b5f92f9 2026-10-28 | PROME | `PROME/tools/wq_ledger.py`, `done_rows_check.py`, `decision_deck.py`; `WQ_LEDGER.crc` (16 B) integrity stamp | ENFORCED (verify) | 1.99 MB append ledger, 36.7× cap; growth/rotation policy not seen. Programmatic-only reads assumed. |
| C12 | `README.md` (root) | 16,645 B / 30e2be225 2026-10-18 | Unstated (root shared doc ⇒ PROME, Will-gated per `:87`) | None found | UNMECHANIZED | Public-facing description of the operation (the repo was once found public: WQ-17); no check on what it discloses. |
| C13 | `KERNELS.md` (root) | 7,093 B / 10d8bb990 2026-08-29 | Root shared doc ⇒ PROME, Will-gated; header says "no live levels…" | None found | UNMECHANIZED | Low: on-demand, last reshaped WQ-129; its "no live levels" rule is prose-only. |
| C14 | `memory/*.md` daily notes (217 files) + `memory/archive/` | latest `memory/2026-10-27.md` | PROME in practice (≥95 of the October `memory/2*.md` commits are PROME's); root Key Directories row | None | UNMECHANIZED | Not covered by carve-out ③ (memory/auto/ only); no retirement/rotation rule seen. |

Checked and **not** proposed: `.github/` does not exist (`git ls-files .github` → 0; the feeds workflow was removed 8/29 per row 8). `exports/` (2 files, 2026-06-21), `AUDITS/` (8 files, 2026-08-25), `reviews/` (19 files, 2026-09-15), `archive/` (73 files, 2026-08-29) and `sources/` (0 tracked) are quiet history stores, so they are low priority unless something live cites them. `PROME/registry/WQ_EXPLAINERS.tsv` (228,146 B, 10/19) and `UNREACHABLE_MEASUREMENTS.tsv` (3,836 B, 10/26) are PROME-internal; fold them into a C11 row if wanted. `AGENTS/_CREDIT.md`, `_ENERGY.md`, `_FUNDING_MACRO.md`, `_PRIVATE_CREDIT.md` and `_SYNTHESIS_OPS.md` (1.4-3.9 KB; group pages) could be one grouped row with C5.

---

## (d) Not read / coverage limits

| Item | Why not verified |
|---|---|
| FORGE 7/30 ~12:25 ET ruling text | Not re-located in PROME archives. Ownership corroborated via root `CLAUDE.md:30/:87` only. |
| HEARTBEAT "5 prose copies" of the re-base rule | Not enumerated. |
| Whether PROME's gate log since 10/26 actually printed `chain at 0 amendment(s)` | `PROME` gate run directories not read. The blind result is derived by applying the function's exact regexes to the file at each commit, not from a gate receipt. `prome_gate.py` was not executed (its boot mode advances BOARD state). |
| KERNEL "212-test suite" | Count method unknown. 220 is a `def test_` grep sum, and the suite was not run. |
| KERNEL "first live refusal… C7 D2" and C-series reviewer gate | Not re-read. |
| READS "live roster39 vs ruled37" | Not re-derived. `ROSTER.md:37` says ACTIVE (34) as a vintage snapshot, and the full roster method command was not run. |
| `walter_doctor.py` behaviour | Functions located and registry wiring confirmed, but the doctor was not run (WALTER's instrument). |
| `CHECKS.tsv` per-row wiring | Only row count (56) and launcher absence checked; row content not re-verified. |
| FORGE/timing "nothing cites the corpus as current" | No fleet-wide citation scan run. |
| WQ-150 final disposition | Searched live PROME surfaces and named archives only. It may have been closed in an archive I did not grep (`PROME/archive/` has 10+ hits; only 3 were read). |
| Dirty tree at read time | `git status` showed DAEDALUS-session changes (`runs/GATE_LOG.tsv`, `scorecards/SCORECARD.tsv`, inbox renames). None of the measured surfaces were dirty (`git status --porcelain` on the 13 surfaces → empty). |

---

## (e) Routing candidates (ranked; need an owner other than DAEDALUS)

| Rank | Sev | Owner | Item | Evidence |
|---|---|---|---|---|
| 1 | 🔴 | PROME | `check_heartbeat_chain` is blind to the 35th-base HEARTBEAT format: counted 0 vs declared chain 1, and the header cross-check never matches, so it passes at any chain length (repeat of the 8/04 v1 failure in its own docstring). | `PROME/tools/prome_gate.py:1090-1093` (regexes), `:1060`; `HEARTBEAT.md:2`, `:8`; format change at 6a3e1e364 (2026-10-26) |
| 2 | 🟠 | PROME | `memory/auto/INDEX_COLD.md` at 46,655 B = 143 % of budget / 86 % of cap and growing (+6,536 B since 9/24). Rotate before the cap. | `wc -c memory/auto/INDEX_COLD.md`; last commit 022a98267 2026-10-15 |
| 3 | 🟠 | PROME | WQ-150 (root carve-out ④ re-key) has no live carrier; completion is unverified. | `PROME/HEARTBEAT_COLD.md:158`; `PROME/archive/SCRATCH_ROTATED_2026-09-29_prome-e6c.md:10`; `CLAUDE.md:82` |
| 4 | 🟠 | PROME (+ Will for root) | AGENTS.md:27-41 route table vs AGENTS/_NETWORK.md, with no agreement check. Root rule says "do not reconstruct routes … in any other mirror", while `_NETWORK.md:230` assigns the compact table to AGENTS.md. The ownership texts conflict. | `AGENTS.md:27-41`; `AGENTS/_NETWORK.md:230`; root `CLAUDE.md` transmission-chain paragraph |
| 5 | 🟠 | PROME / Will (scripts/ ownership) | CATO added a desktop agent launcher (11 commits, ~11 files) under DAEDALUS-owned `scripts/` with no CHECKS.tsv row; decide ownership or relocation. *(DAEDALUS acts on the register side; the authorship decision is not DAEDALUS's.)* | `git log --since=2026-10-20 -- scripts/`; `scripts/agents*.py`, `scripts/install_agents.py` |
| 6 | 🟡 | 14 desks (via PROME, declaration owner) | READS attestations stale for 14 desks (incl. PROME 10/20), OZK unattested, 28 undeclared. | `reads_check.py --fleet` rc=1 output |
| 7 | 🟡 | PROME | `docs/CANON_PROVENANCE.md` names an anchor-parity test with no runnable implementation found. | `docs/CANON_PROVENANCE.md:3`; grep `root-anchor` → 0 in scripts/PROME tools |
| 8 | 🟡 | PROME | `AGENTS/SELF_RULINGS.tsv`: no row since 2026-09-19. Confirm the delegation tier is idle rather than unrecorded. | `git log -1 -- AGENTS/SELF_RULINGS.tsv` → ec166d1ae 2026-09-19 |
| 9 | 🟡 | unassigned → PROME to name | `AGENTS/VOCABULARIES.tsv` has no owner and a header date (2026-03-08) that disagrees with its last commit (2026-10-23). | `AGENTS/VOCABULARIES.tsv:3`; cb861d3fb |

**Self-owned (DAEDALUS, for the record, not routed):** FORGE path-teach in `ledger_staleness.py` (row 1 Gap, still 0 refs); SURFACES header `:3` line cite and `:4` token set; DAEDALUS's own READS attestation STALE (2026-10-09); the `004a9f91` dead pointer.
