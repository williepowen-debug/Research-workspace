READ-1 · L594 helm-fold APPLY · 29 claims
SCORE: 21/29 ✅ · 7 ⚠️ · 1 ❌
❌ 5 A4 page size — acceptance A4: "page < 250,000 B (measure.py)" vs `measure.py after/helm.html` → "250621 B (wc -c)". Over by 621 B. Attribution: see SIZE below.
⚠️ 4 A3 full set — only the two isolated files were run (by instruction); test_desk_attention (10) + test_dashboard_build_receipt_L339 (27) = 37 of the 60 were NOT run by this reader: UNVERIFIED here.
⚠️ 16 Carried comment in collect_fleet_rows: "# -- fleet rows (active roster, git-computed; staleness in BUSINESS days)" contradicts the same function's own note "own-surface age (non-inbox), CALENDAR days" and the code (round(own) calendar). Moved verbatim, not introduced; the retired page's GLOSSARY (fleet_dashboard.py:871–873 "business days … weekends don't age anyone") is wrong the same way. Code and Helm label are right.
⚠️ 22 Freshness column prints raw class tokens: `label = row["word"] if row["parked"] else (… else row["cls"])` → render shows "crit"/"elev"/"watch"/"ok". The donor maps these to plain words (FLEET_WORD: fresh/quiet/lagging/cold, fleet_dashboard.py:548). On a Will-facing page "crit" for a 15-day-quiet desk (MARCO) reads as "critical"; Output Canon: jargon unpacked or dropped.
⚠️ 23 Fired-gate lines render unstyled: panel emits `<p class='fired'>`, but the only rule is `.board .fired{…crit…}` (will_handbook.py:261) and the `.board` div closes before `#tab-desk` (verified in after/helm.html). A FIRED-UNEXECUTED line would show as plain text, not red. Zero fired tonight, so not visible in the render; CE2 confirms the markup.
⚠️ 26 Helm still advertises Fleet Ops: after/helm.html renders "Fleet Ops is the instrument panel" and "Your pages, two: the Helm … · Fleet Ops (instrument panel). Both regenerate at every PROME closeout" (source PROME/HANDBOOK.md:257, outside the patch). Contradicts the new Fleet-Ops header "RETIRED as a published page 2026-10-02" and CLOSEOUT.md step 11. FLEETOPS_URL (will_handbook.py:45) is now an unused constant. Pre-existing text; this is residue, not a patch defect.
⚠️ 27 Placement: `h.append(fleet_html)` comes before `attention_html`, so a 34-row freshness table is now the FIRST section of "Your desk". It sits above broker-actions at byte 14886 vs fleet-ops at 12789. Root Output Canon: "the decisions that are his stand at the top". No placement rationale found in HELM_FOLD.md / READER_REPORTS (SEARCH-NOT-FOUND).
⚠️ 29 Two gate counters on one page, two parsers: the board (`parse_gate_rows`, csv.reader, default quotechar) and the new panel (`fd.parse_gates`, split on tab). They can disagree silently (CE4: board 16 LIVE vs panel 18 LIVE, no alert). The board parser is the defective one and pre-dates the patch; the fold makes the gap visible but does not detect it.

## Acceptance legs (verified at the artifact)
1 ✅ A2 hashes: sha256 of fleet_dashboard.py ba72f099…, will_handbook.py 772a3676…, tests/test_helm_fleet_fold.py b33deb87… == target_hashes 'after' (3/3). `git apply --check -R helm-fold.patch` clean.
2 ✅ A2 scope: `git diff --stat` = exactly the 2 tracked tools (103+/24−); with the 113-line new test that totals 216+/24−, matching the patch. `git status --short -- PROME/` = those 3 paths plus PROME's own untracked ACCEPTANCE_L594 file. AEOLUS dirt is ignored.
3 ✅ A1 drift: HEAD is now 90a2b365d, not 09639faaf. The two newer commits touch only AGENTS/REGINALD/; `git diff fd9339821 HEAD -- <both tools>` is empty.
4 ⚠️ see above. Isolated run: `python3 -B -m unittest test_helm_fleet_fold.py test_helm_size_split.py` → Ran 23 (14+9), OK. The 4 state files' sha256 and `git status -- PROME/` are unchanged after the run.
5 ❌ see above.
6 ✅ A4 `id='fleet-ops'` appears ×1 in after/helm.html (×0 before).
7 ✅ A4 source label present and true to the code: non-inbox own-surface age, "regardless of author", rounded calendar days, "does not prove the desk ran". None (never committed OR query failed, agent_freshness.py:127) shows as "unavailable / no history".
8 ✅ A4 gate chips "LIVE 18 · FIRED-UNEXECUTED 0" == GATES.tsv: 19 data rows (all NF=12); 18 with col6 ^LIVE; 1 RESOLVED (GATE-TERRY-VLO-SCALE); 0 rows containing FIRED-UNEXECUTED. The board line "18 gates LIVE · none fired" agrees.
9 ✅ A4 freshness rows: 34 == fd.parse_roster() ACTIVE = 34 (ROSTER.md "## ACTIVE"…"## TIER-2"). load_parked(10/9) = {} (none parked).
10 ✅ A4 `cmp before/docket.html after/docket.html` → identical (277,792 B each).
11 ✅ A4 state files: all 4 current hashes == state_before4.sha. Note: state_before.sha (20:37) lists brief_* under PROME/tools/, which does not exist; it is superseded by state_before4.
12 ✅ A5 after/fleet_ops.html: the retirement line appears ×1. Fleet rows 34 == Helm 34, same order, same day values (0 mismatches). LIVE tags 18, fired 0 == Helm.

## Diff claims (stranger read)
13 ✅ parse_gates(diagnostics=None) keeps legacy rows; build() still calls parse_gates(today) with no diagnostics (test_executed_prefix… asserts legacy kind).
14 ✅ Lead-token whitelist LIVE|FIRED-UNEXECUTED|RESOLVED|LAPSED|RETIRED == GATES_README.md:21 STATES == prome_gate.py:67 GATES_STATES. (It is a hand copy; drift is not mechanized.)
15 ✅ Malformed-input diagnostics: header schema, <8 cols, missing/dup ID, unknown lead, no header, no rows. Each makes the panel withhold counts and raise an ALERT ("no all-clear"). Shown by tests and CE3/CE6.
16 ⚠️ see above.
17 ✅ build() refactor is a pure extraction: the body moved into collect_fleet_rows unchanged; A5 equality holds.
18 ✅ Fleet-Ops header "RETIRED as a published page 2026-10-02 (WQ-372) … built for the gate only" matches CLOSEOUT.md:96 step 11 (retired, still builds for L339). The link == HELM_URL ee088d08 (will_handbook.py:47).
19 ✅ `import fleet_dashboard as fd` has no import-time effects (module-level constants only; `__main__` guard at :1452). The CE run left no pycache or tree change.
20 ✅ render_fleet_panels never calls build, write_build_receipt or _persist_state (test_shared_helpers…). State hashes are unchanged.
21 ✅ The 999 sentinel shows as "unavailable / no history" and a parked word is kept (tests; nothing parked tonight, so not seen in the render).
22 ⚠️ / 23 ⚠️ see above.
24 ✅ Hint "LIVE means no unexecuted fired leg; executed legs may exist" == GATES_README STATES ("means 'no fired-and-UNEXECUTED leg', never 'nothing has fired'"). It holds by contract only; see CE1.
25 ✅ "Fired actions remain on the board above": the board div renders before #tab-desk.
26 ⚠️ / 27 ⚠️ see above. (The header link removal itself is ✅: c884f088 appears ×0 in after, ×1 in before.)
28 ✅ render(…, fleet_html="") default is backward compatible. In main() the render_fleet_panels call sits outside a try, but both of its legs catch internally.
29 ⚠️ see above.

## SIZE (task 6)
before/helm.html 248,621 B → after 250,621 B: fold delta +2,000 B exactly. A line diff accounts for all of it: the header line loses 100 B (Fleet Ops link removed), the fleet-ops section adds 2,100 B, and the other changed lines are equal-length timestamps (0 B). On the 10/3 frozen snapshot (validation.json) the delta was 211,025 → 213,022 = +1,997 B, so the fold's own cost is stable.
The pre-apply page grew 211,025 → 248,621 (+37,596 B) in 6 days of data. That left 1,379 B of headroom against a 2,000 B fold. The breach is crossed by the patch's delta, but the cause is pre-existing page growth; at that rate the page passes 250,000 B within days without the fold.
The 250,000 B target comes from DAEDALUS build ACCEPTANCE H5 ("on the same frozen representative snapshot"). It is enforced by no tool: SEARCH-NOT-FOUND in will_handbook.py, CLOSEOUT.md and prome_gate.py. A4 as written is NOT met. It must be recorded FAILED with this attribution, or re-ruled, or the page trimmed; it must never be recorded as passed.

COUNTEREXAMPLE: scratch copies of tonight's GATES.tsv, read via fd.REPO / wh.ROOT patched to a scratch root (script: l594/ce/run_ce.py; roster and fleet rows stubbed); panel vs board vs grep compared.
 CE1 a LIVE-led cell "LIVE — leg 2 FIRED-UNEXECUTED 10/9" → panel FU 0, board fired [], grep 1. Every lead-token consumer, the panel included, trusts the contract; nobody flags the violation.
 CE2 a real FIRED-UNEXECUTED row with <b> in the cell → panel LIVE 17 / FU 1, row named and HTML-escaped; the board agrees. Rendered unstyled (#23).
 CE3 "LIVE—NOT ARMED" (em-dash glued) → panel UNAVAILABLE + ALERT fleet-gates (fails closed); the board still counts 18.
 CE4 a condition cell opening with `"` → panel 18 LIVE / 19 rows (correct); board 16 LIVE / 17 rows (csv swallowed 2 rows), no alert → silent split on one page (#29).
 CE5 CRLF file → identical to baseline (splitlines handles it).
 CE6 "FIRED-EXECUTED" → panel UNAVAILABLE + ALERT; the board counts it as fired.
 Baseline copy → 19 rows / 18 LIVE / 0 FU on both counters.
POINTERS: 15/15 resolve; dead: none. (Acceptance file · patch · target_hashes · L594_RECHECK · HELM_FOLD · READER_REPORTS · GATES.tsv · GATES_README · CLOSEOUT.md:96 · HANDBOOK.md:257 · commits 09639faaf/fd9339821/6a7f4ae49/45b320134 · HELM_URL constant.)
ONE-LINE VERDICT: SHIP-WITH-RESIDUE. The applied code is the reviewed code (hashes, reverse-apply). Rows and gate counts match GATES and ROSTER, docket and state files are unchanged, and bad input fails closed. But A4's size leg FAILS (250,621 ≥ 250,000 B; the fold adds +2,000 B onto a page that grew 37.6 KB since 10/3). It must be recorded failed or re-ruled, not passed. ⚠️ 22/23/26/27/29 are declarable residue.
