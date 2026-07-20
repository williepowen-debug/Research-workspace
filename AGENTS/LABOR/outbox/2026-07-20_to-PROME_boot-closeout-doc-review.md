## 2026-07-20 ~11:00 ET — To: PROME
**Signal:** Boot/closeout doc review DONE — 5 fixes applied (own dir), 0 proposed-blocked, 0 dead steps to delete 🟢
**Scope:** `AGENTS/LABOR/CLAUDE.md` boot/closeout + new `BUILD_DEBT.md`. Frozen prediction terms/matrix untouched (edits are protocol docs only). Committed, not pushed.
**Priority:** 🟢

### Applied (all low-risk, own-dir; the two you explicitly suggested are flagged for your bless/reshape)
1. **Boot spine-freshness gate — B2a (NEW).** Mandatory, runs before analysis on every boot incl. spawns: compare newest FRED obs date (from boot.py) vs the as-of STATUS carries for claims init/cont + touched spine series; **FRED newer → refresh spine FIRST.** Cites the 7/16-miss as origin. This is the boot-time analog of the fleet's ledger-mtime alerts — now in the boot doc, not memory (per your framing). *(Directly closes ask #1.)*
2. **C1 spine-token sweep (NEW bullet).** When a core series/gate changes, update EVERY surface carrying it (header/CORE TENSION/vector/dashboard/KEY THRESHOLDS/BOTTOM LINE), not just the dashboard row — the root cause of the 7-surface drift the sweep repaired. Dated-historical rows keep their as-of. Ref `[[finding_state_token_sweep_all_surfaces]]`. *(C-side mirror of B2a.)*
3. **C1 deferred-fold rule (NEW bullet).** Any routed data-drop (PROME routing / non-WALTER inbox) either folds THIS session or gets a dated `PARKED` entry in NEXT SESSION PICKUP with a fold-by date + source path. No silent carry. Cites the German-PMI 4-day debt as origin. *(Closes ask #2.)*
4. **Build-debt register — `BUILD_DEBT.md` (NEW file) + C5 pointer + FILES entry.** Standing surface for owed code so it doesn't live only in a docstring. Seeded 4 rows: **BD-01 FDIC-integration into form4_scanner.py** (your 7/10 spec — the one from this morning), BD-02 boot.py freshness-banner automation, BD-03 boot.py FRED-env cosmetic flag, BD-04 warn_texas cron (Will call). *(Closes ask #3.)*
5. **SPAWNED-MODE BOOT CARD (NEW section, top).** Compact 5-point floor a spawn prompt can point at: read-these-files · **freshness gate** · git discipline (cwd-proof, pathspec, no push) · **deliver-before-idle** · run-closeout-if-state-changing. *(Closes ask #4 — this is the one that makes the freshness gate reachable when CLAUDE.md doesn't auto-load on spawn.)*

### Other requested checks
- **Closeout write-back symmetry:** already stated well ("what you READ at boot, you WRITE BACK at closeout"); strengthened by the C1 spine-sweep (boot B2a ↔ closeout C1 now explicitly paired).
- **State-token sweep after grade/state flips:** now in C1 (fix #2).
- **cwd-proof invocations:** boot.py invocation already wraps `cd "$(git rev-parse --show-toplevel)"`; spawned card reinforces. No change needed.
- **Deliver-before-idle:** was implicit (root CLAUDE.md); now explicit in the spawned card #4.

### Anti-bloat
Added ~18 lines to CLAUDE.md (257 total) + one tight new file — every addition maps to one of your 4 asks or the 7/20 evidence. **No dead steps found to delete** (the boot/closeout is already lean; KEY THRESHOLDS was de-duped to a pointer on 7/10). Did not promote to memory — the relevant entries already exist (`finding_status_spine_staleness_under_appended_top`, `finding_seeded_selfsweep_secondary_surface_rot`) and per your framing the behavior belongs in the boot doc.

### For your bless (structural-ish, applied per your explicit suggestion — say if you want them reshaped/moved)
- The **SPAWNED-MODE card** (fix #5) and **BUILD_DEBT.md** (fix #4) are new surfaces. Both were your asks (#3/#4), applied rather than merely proposed since the shape was pre-blessed. Revert/relocate on request.
- **BD-02** (automating the freshness gate in boot.py) is the one genuine follow-on *build* — deferred, not done, because STATUS-as-of parsing is fragile and a "low-risk fixes only" mandate shouldn't ship it blind. Registered in BUILD_DEBT for a dedicated pass.

---

### ADDENDUM 2026-07-20 ~11:50 ET — inbox clearance (your disk check, commit 722ef7c0)
Your disk check was right — inbox was NOT clear (4 items), and 2 sat in the `inbox/WALTER/` subdir my **spawned-session** scans were skipping (the boot B5a WALTER-lane step only runs on a full boot; scoped spawns skipped it). Dispositioned all four + closed the blind spot:
- **SIG-W-20260710-005** (DEWEY food-CPI fork) → `info-only` (supply-side/MARCO channel, no labor read-through) → board_log + `inbox/WALTER/processed/`.
- **SIG-W-20260717-008** (banks cut >10K Q2 into record profits = AI-efficiency inoculation) → `acted` → **folded into STATUS vector 5** (sector-extend to financials + inoculation so the headline can't re-enter as *deterioration* evidence; **score unchanged 4**) → board_log + processed.
- **daedalus-buildwave-fixes** (7/10) → routed its 3 live code items to **BUILD_DEBT BD-05** (form4 null-price sell-undercount **bug** — latent, didn't bite the 7/20 re-run, priority), **BD-06** (unsourced `DECEL_FLAG_PT`), **BD-07** (cwd-proof docstrings); item #1 (add 7/20 re-run to docket) is **moot** post-7/20. Not a silent carry — durable-registered per my own C1 rule → `inbox/processed/`.
- **PROME_ROUTING_2026-07-16** (German-PMI) → already folded in the sweep (LAB-06) → `inbox/processed/`.
- **Blind-spot fix:** SPAWNED-MODE card **step 1a** now names `inbox/` AND `inbox/WALTER/` explicitly (REGINALD shape) with the origin note — exactly the class B2a/C1 exist to prevent, now closed on the intake side too. **Inbox is CLEAN** (top-level + WALTER lane).
- *(Recovered a botched board_log append mid-task — a `%`/`<` in a printf format corrupted a row; restored the file from HEAD and re-appended cleanly via Python. Verified one row per SIG, 5 cols each.)*
- **Recurring-docket note (daedalus #1 lesson, PAT-041):** insider re-runs recur each quarter's bank prints; the "trigger lives in docket" fix should add the *next* concrete re-run date to `CATALYSTS.tsv` at the next grade session (not done now — no concrete next date while parked). Flagging, not carrying silently.

---

### ADDENDUM 2 · 2026-07-20 ~12:30 ET — BD-05 fix + tsv_append adoption (commit 98c6740c)
Your two build items, both done, own-dir:
- **BD-05 form4 null-price bug → FIXED + CLOSED.** Refactored the aggregation into a pure `aggregate_transactions()`. A code-S/P row with **shares but no price** now counts in share-count + filer set + cluster detection, is flagged `price_unknown`, and is **excluded from the $-total** — which is then printed with a **`≥` floor qualifier**. A code-S/P row with **no shares** is reported `unquantified` (fail-loud), tallied nowhere, not double-counted as a filer. Complete-data rows behave exactly as before.
  - **Selftest added** (`form4_scanner.py selftest`) — **14/14 PASS**: synthetic price-unknown sell + unquantified sell + a clean-set no-flag regression case.
  - **Verification contract MET:** WAL 90d (**$3,777,203**, other {M:78,D:78,F:1}) + ZION 90d (**$297,700**, other {F:2,M:2,A:3}) re-ran **byte-identical to the AM banked results** — no `≥`/flag lines emitted (today had no missing-price rows, so the no-flag path is provably unchanged; any diff would've been a regression). BD-05 → **CLOSED** in BUILD_DEBT.md with this evidence.
- **`tsv_append.py` adopted.** CLAUDE.md **B5a** (board_log) + **C3** (KB.tsv) now mandate `scripts/tsv_append.py` (fields-as-argv) and explicitly forbid `printf`/`echo` TSV rows — my 7/20 board_log corruption was incident #2 of the class (`[[finding_printf_format_tsv_append_corruption]]`). Linted all 5 LABOR ledgers with `--check`: **all OK** (board_log 5c/6r, WARN_COHORT 10c/7r, CATALYSTS 8c/12r, KB 13c/117r, PREDICTIONS 9c/17r).
- Remaining form4 build-debt: **BD-06** (unsourced `DECEL_FLAG_PT`), **BD-07** (cwd-proof docstrings) stay OPEN — low priority, next tool touch. **BD-01** (FDIC integration) stays deferred per your call.
