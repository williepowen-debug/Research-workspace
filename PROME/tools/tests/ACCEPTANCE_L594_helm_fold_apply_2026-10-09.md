# ACCEPTANCE — L594 / WQ-372 Helm-fold patch APPLY (owner integration), 2026-10-09

**Written BEFORE the edit:** 2026-10-09 20:37 ET (PROME `prome-1e`, desktop, Fri evening). **Class: PROCESS — this apply is the session's ONE process change (WQ-299 R1); no due domain/position row PROME can advance exists tonight (Isaias wakes wait on NHC's landfall statement; the FORGE reconcile waits on Will's capture).** Authority: WQ-372 RULED (Will 2026-10-02 19:14 ET, *"for 1 - approved go with your recs"*); DOCKET L594 APPLY-READY 10/8 (DAEDALUS recheck `AGENTS/DAEDALUS/runs/2026-10-08_L594_RECHECK.md`, COMPATIBLE-AT-HEAD at 45b320134); build record `AGENTS/DAEDALUS/runs/2026-10-03_HELM_FOLD.md`; independent result read `AGENTS/DAEDALUS/runs/2026-10-03_HELM_FOLD_READER_REPORTS.md` (8 plan treatments APPLIED, residues R1–R3, no blocking defect). Patch: `AGENTS/DAEDALUS/builds/helm_fold_2026-10-03/helm-fold.patch` (3 files: fleet_dashboard.py · will_handbook.py · tests/test_helm_fleet_fold.py; 216+/24−), UNCHANGED since the 10/3 read.

## What the defect is, in its own terms
Fleet-Ops is retired as a published page (WQ-372) but its two unique panels (agent-freshness table · gate chips) still live only there; the Helm, the page Will reads, lacks them. The fix is a reviewed patch that shares Fleet-Ops' row builder with the Helm. The risk of the APPLY is not the code (read 10/3) but the ENVIRONMENT: HEAD has moved (now 09639faaf), the Standard gate grew, state files feed the closeout gate.

## Acceptance conditions (each verified at the artifact, not asserted)
| ID | Condition | How |
|---|---|---|
| A1 | Preconditions at apply time: live sha256 of both tools == target_hashes 'before'; new test path ABSENT; `git apply --check` clean at HEAD 09639faaf | sha256sum · ls · git apply --check |
| A2 | Post-apply sha256 of all three files == target_hashes 'after' (the applied code IS the read code; nothing else changed) | sha256sum · `git status --short` shows exactly the 3 paths |
| A3 | The four test files pass in the owner tree (60/60, same files as the 10/3 record); any state file a test writes is restored from HEAD and named here | unittest · git status · git checkout -- <state file> |
| A4 | Helm `--no-feed` render rc 0: page < 250,000 B (measure.py), `id='fleet-ops'` panel present with the accurate-source label, gate chips show LIVE n · FIRED-UNEXECUTED 0 matching `PROME/GATES.tsv` (19 rows: 18 LIVE + 1 RESOLVED tonight); docket.html byte-identical to the pre-apply render; the four state files (`PROME/state/brief_snapshot.json` · `PROME/state/brief_changes.jsonl` · `PROME/tools/dashboard_state.json` · `PROME/tools/dashboard_build.json`) byte-identical before/after the render | measure.py · grep · cmp · sha256sum |
| A5 | Fleet-Ops `--no-snapshot` preview builds rc 0 with the retirement header line; its row/gate counts equal the Helm panel's on the same inputs | fleet_dashboard.py --no-snapshot -o <scratch> · grep |
| A6 | Standard closeout gate (`prome_gate.py closeout --tier standard`) passes on the full owner environment — RUN AT TONIGHT'S CLOSEOUT (it requires the ARGUS review and builds the dashboard receipt); not claimed before then | closeout verdict block |
| A7 | Post-apply RESULT READ by an independent Opus reader (read-only; devises ≥1 counterexample of its own; ledger to the scratchpad, copied to PROME/reports/) — ❌ fixed only; ⚠️ declared below; the two-correction stop applies per file | reader ledger |
| A8 | Hosted-page verification: NOT performed tonight — WQ-382 (b) RULED B (Will 18:41 ET 10/9): the Helm republishes only on Will's word or at a spine audit. The spine audit is due Sat 10/10; the hosted leg rides it or Will's word. Named here as DEFERRED, not waived | this file + L594 state cell |

## Neighbours (WQ-229 five categories — considered, not performed where N/A)
- **Ordinary:** A3/A4 — the render and tests on tonight's real data (not the frozen 10/3 snapshot).
- **Overlap:** will_handbook.py was edited by PROME on 10/3 (the size split, fd9339821) AFTER the patch's source head 6a7f4ae49 — A1's hash match proves the patch already incorporates that head (DAEDALUS rebased on it 10/3 18:20); no PENDING edit exists (tree clean at boot).
- **Wrong owner:** the patch is DAEDALUS-authored on PROME-owned tools; PROME applies and commits (owner of `PROME/tools/`). DAEDALUS does not commit. N/A beyond that.
- **Missing information:** the literal "last self-commit" field is NOT what the donor supplies (R2) — the panel shows own-surface committed non-inbox activity regardless of author, labelled so. PROME ACCEPTS that documented interpretation for the apply (an attribution source is a separate commission); the label must stay visible on the page (checked in A4).
- **Concurrent activity:** ListAgents 20:1x ET = no other Claude session; `ps` = no Codex process; tree clean. The dashboard state files are PROME's; no desk writes them.

## Results (2026-10-09 20:51 ET, prome-1e) — completion note in WQ-229's four states
| ID | Result |
|---|---|
| A1 | ✅ PASS — live sha256 d30da110… / dbed950b… = 'before'; new test ABSENT; `git apply --check` clean at HEAD 09639faaf |
| A2 | ✅ PASS — post-apply sha256 772a3676… / ba72f099… / b33deb87… = 'after'; `git status` showed exactly the 3 paths (plus this file) among PROME's |
| A3 | ✅ PASS — `Ran 60 tests … OK` in the owner tree; `PROME/tools/dashboard_build.json` was written by test_desk_attention and RESTORED from HEAD (sha256 4927b316… verified before and after) |
| A4 | ⚠️ PARTIAL — render rc 0; `id='fleet-ops'` present; chips LIVE 18 · FIRED-UNEXECUTED 0 = GATES.tsv (19 rows, 18 LIVE, 1 RESOLVED); freshness table 34 desks = ROSTER active count; accurate-source label present; docket.html IDENTICAL (cmp); all four state files byte-identical (sha256 -c). **❌ SIZE LEG FAILED: page 250,621 B vs the 250,000 B target (measure.py).** The fold's own delta is +2,000 B (before 248,621 B → after 250,621 B; the 10/3 frozen validation measured +1,997 B); the page had grown +37,596 B since 10/3 on data alone, leaving 1,379 B of room. Recorded as FAILED, not re-ruled here: the 250,000 B figure is DAEDALUS build-acceptance H5 from PROME's 10/3 spec, enforced by no tool (reader searched will_handbook.py, CLOSEOUT.md, prome_gate.py). Disposition: the apply SHIPS with this leg failed and disclosed; the size fix (move depth into docket.html per the split pattern) or a re-rule of the target goes to DOCKET L602 (Helm size, PROME-owned) at the next process slot. |
| A5 | ✅ PASS — Fleet-Ops `--no-snapshot` preview rc 0; header carries "RETIRED as a published page 2026-10-02 (WQ-372)"; 43 `<tr` rows incl. header/gate rows; state files unchanged after the preview |
| A6 | ⏳ PENDING — runs at tonight's Standard closeout (requires the ARGUS review); not claimed here |
| A7 | ✅ DONE — read 1 (independent Opus reader, read-only, own counterexample): **21/29 ✅ · 7 ⚠️ · 1 ❌ · verdict SHIP-WITH-RESIDUE**; ledger `PROME/reports/2026-10-09_L594_helm-fold-apply_read_1.md`. The one ❌ is A4's size leg above. No code edit after the read (the fix for a size ❌ is not in the patch). |
| A8 | ⏸ DEFERRED — hosted Helm NOT republished tonight (WQ-382 (b) RULED B 18:41 ET: Will's word or a spine audit; the spine audit is due Sat 10/10) |

**Completion note:** IMPLEMENTED (patch applied, hashes match) · TESTED (60/60 in the owner tree; reader re-ran 23 in isolation) · INDEPENDENTLY VERIFIED (read 1, SHIP-WITH-RESIDUE, counterexample run) · **STILL UNRESOLVED: A4 size leg (❌, L602) · A6 (closeout) · A8 (deferred by ruling) · the CLOSEOUT.md rewiring (separate slot, one edit with L665).** Process-change count this session after this apply: ONE (this), class PROCESS.

## Declared residue (from read 1; ⚠️ are declared, not fixed — WQ-178)
- **Reader #22** — freshness classes render as the raw tokens `crit / elev / watch / ok` where the operator surface wants plain words (a label pass, Helm-side; L602 slot or the CLOSEOUT rewiring slot).
- **Reader #23** — a FIRED-UNEXECUTED line inside the new panel is named and escaped but NOT red-styled: the existing CSS rule applies only inside `.board`. Cosmetic; the board's own fired strip still styles.
- **Reader #26** — the Helm's manual still describes Fleet-Ops as one of Will's two pages (WQ-372 retired it); a manual-text fix for the CLOSEOUT/L665 rewiring slot.
- **Reader #27** — the 34-row freshness table sits ABOVE "Broker actions" in Your desk; placement is a product call, not a defect — flagged for Will's eye at the next Helm publish.
- **Reader #29 + counterexample** — the panel's parser (`fleet_dashboard.parse_gates`) and the board's parser (`will_handbook.parse_gate_rows`) can DISAGREE SILENTLY: a condition cell beginning with `"` makes the board's csv reader swallow two rows (16 LIVE / 17 rows) while the panel reads 18 / 19, with no alert; a LIVE-led row whose text names an unexecuted leg counts 0 fired on BOTH (lead-token trust) while grep finds 1. Both behaviours PRE-DATE the patch (the board's parser is unchanged); the panel fails CLOSED on a glued em-dash or an illegal token (alert + "unavailable") where the board keeps counting. Class: the L450 buried-token family, GATES edition — register at the next process slot, never hand-fix tonight.
- **Reader #4** — the reader itself ran only the two isolated test files (23 tests) by instruction; the other 37 (desk-attention · L339 receipt) were run by PROME in the owner tree (A3) and the receipt file restored — PROME's run, not independently re-run.
- **Reader #16** — a carried comment in `collect_fleet_rows` says staleness is in BUSINESS days while the function's own note and code use CALENDAR days (moved verbatim from the donor, not introduced); a one-word comment fix for the L602 slot.
- Standing from the 10/3 read: R1 (999-day parked sentinel) · R2 (activity ≠ authorship; PROME accepts the documented interpretation) · R3 (donor footer wording).
- CLOSEOUT.md re-wiring (symmetry row + step 11: drop the Fleet-Ops publication) is a SEPARATE process slot per L594's own text — to be done in ONE edit with L665's step-11 change (WQ-382 (b)), never tonight.

## Reads
- read 1 (post-apply result, Opus, read-only, own counterexample): 2026-10-09 20:51 ET — 21/29 ✅ · 7 ⚠️ · 1 ❌ (A4 size) — SHIP-WITH-RESIDUE. Ledger: `PROME/reports/2026-10-09_L594_helm-fold-apply_read_1.md`. No further read owed unless a code edit follows (none did).
