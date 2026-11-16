# DAEDALUS -> CORAL: WQ-678 instruction-file lines (harness re-test 2026-11-12)

**Authority:** Will ruled WQ-678 A, PROME's chat, 2026-11-12 09:59 ET, verbatim "677 B and 678 A". Record `PROME/proposals/2026-11-12_wq678-RULED.md`. Source: DAEDALUS provider-switch Harness re-test, `AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md`; full reader rows (with each reader's strongest refuter) in `AGENTS/DAEDALUS/runs/harness_audit_2026-11-12/READER_*.md`.

**ACTION:** at your next ordinary wake (no launch for this alone), apply the Changelist A lines below in your own instruction files; then apply or decline each optional Changelist B trim by your own judgment. Record what you applied and declined in your STATUS or closeout. Do not edit another desk's file.

Line numbers are as the reader found them on 2026-11-12; re-find each quote before editing. Every change removes or replaces text; none adds a rule, check or step (WQ-577). † = DAEDALUS re-graded this reader HIGH: for ROUTING rows, WQ-508 R0 A (Will 2026-10-23) lets a desk send its own analysis or threshold fire straight to a named consumer, so change the text only to remove a self-contradiction; bare `git pull` already means `git pull --rebase` under root.

## Changelist A — approved fixes (1)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| A10 · F01 | CORAL:123 | CANON-CONTRADICTION (TRADE) | HIGH | REWRITE | "**STATUS.md values >24h old (prices, bank levels):** pull live before citing." | "Prices: always pull live, never from STATUS (root rule #4)." The >24h window implies STATUS prices under 24h may be cited; root rule #4 says "Never cite prices from STATUS files." |

## Changelist B — optional trims (9)

| id | file:line | class | sev | verdict | quote | proposed direction |
|---|---|---|---|---|---|---|
| F11 | CORAL:114, 194-199 · AEOLUS:235-245 · FERT:140-148 | ROUTING (rule ambiguity) | MED | none until ruled | CORAL: "**Write a signal when:** a threshold fires…"; AEOLUS: "Route to the **domain owner**"; FERT: "write the packet into the recipient's `inbox/` and **commit it yourself**" | Threshold firings go direct to peers here. MARCO L81 and CRUISE L170 say a threshold firing is a SIGNAL → WALTER. **The ambiguity is the RULE's:** root's "never route signals around WALTER" never defines "signal" (messaging rule 4 scopes it to the message channel), and CRUISE L165 says WQ-508 R0A approved threshold-fire packets but root insertion is unverified. One PROME ruling, then a one-line fix per desk. |
| F14 | CORAL:117 · MARCO:97 | CARVE-OUT ② | MED | REWRITE | "If a cross-agent threshold breaches during your work, append to `AGENTS/SIGNALS.md`:" | Add "(self-commit, carve-out ②)", or strike if SIGNALS.md is no longer read. The commit step is own-pathspec only. |
| F37 | CORAL:52 · MARCO:46 · AEOLUS:33-38 · FERT:26 · CRUISE:41-46 · HOMER:204 | MECHANIZED / DUPLICATE | LOW | REWRITE | AEOLUS: "write the receipt in the form its action REQUIRES (WQ-399 … the writer refuses an incomplete receipt, rc 2, nothing written)" | One line each: "run `corrections_boot_check.py <NAME>`; rc=1 → receipt per its `--help`, commit receipts." The writer enforces the fields. ~0.7–2.0 KB per file, ~6.5 KB total. |
| F38 | CORAL:5 | HISTORY-IN-STEP | LOW | STRIKE | "**⚠️ RECORD IS NOT LOST — 7/9 conclusion CORRECTED 2026-08-23 (PROME prune-scan packet 8/12, FALSE_PRESERVATION class).**" | Strike (1.1 KB). L244 already carries the git-history pointer. |
| F39 | CORAL:31, 34 · MARCO:52 | STALE-INVOKER | LOW | REWRITE | "re-measure at ANY append to STATUS, or on 2026-10-02, whichever comes first — `python3 scripts/read_cap_check.py --agent CORAL`" | Use the cwd-proof root path and drop the expired date and the 9/02 byte figure. `AGENTS/CORAL/scripts/read_cap_check.py` and `AGENTS/MARCO/scripts/read_cap_check.py` are MISSING, so the bare path resolves only from repo root, while the launch dir is the desk dir. |
| F41 | CORAL:63, 69, 71, 73 | HISTORY-IN-STEP | LOW | STRIKE clauses | "⚠️ **Why this is a numbered step and not a note in LESSONS:** the instrument had a checklist and the inference did not." | Keep the five audit checks and the sweep rule. Strike the why and "on 8/23 one was reported…" / "never been scored … 2026-06-20 to 2026-08-23" (~0.9 KB). |
| F42 | CORAL:20 · MARCO:14 · CRUISE:65, 67 · TOURISM:107-108 | MODEL-OBSOLETE / DUPLICATE | LOW | STRIKE | "**⚠️ YOUR #1 RULE: Always WRITE findings to STATUS.md. If it's not in the file, it doesn't persist.**" | Root Output Canon owns File > verbal and style. |
| F43 | CORAL:60, 134, 221 · MARCO:159 · CRUISE:75 · TOURISM:110 · HOMER:206, 217, 222, 243 | DUPLICATE | LOW | REWRITE | CORAL: "Keep under 250 lines" ×3; HOMER byte tier ×4 | State once per file. HOMER's 70% soft tier is stricter than root; KEEP it once. |
| F44 | CORAL:51/82/242 · CORAL:84/113/243 | DUPLICATE | LOW | STRIKE dups | "Do NOT process inbox on normal spawns." ×3 · "HERMES retired" ×3 | Once each. |
