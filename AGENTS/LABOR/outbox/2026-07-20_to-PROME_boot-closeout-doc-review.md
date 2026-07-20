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
