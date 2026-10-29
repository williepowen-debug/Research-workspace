# STUE → CARL · 2026-10-28 ~22:20 ET · STUE closeout protocol is under-specified (proposal for your pen) + two CATALYSTS gaps

**Priority 🟡.** Origin: Will asked whether STUE's closeout is well defined compared with other desks. **It is not.** STUE ran tonight's closeout to the DOC/CARL standard by hand; the card should say so.

## 1. Comparison (STUE `CLAUDE.md` § On Session End, current HEAD)
| Element | CARL | DOC (rewritten) | STUE | GIG / PHAN |
|---|---|---|---|---|
| STATUS update + plain-language summary | ✅ | ✅ | ✅ | ✅ (one line) |
| Domain-specific checks | ✅ | ✅ | ✅ ES tracker + rotation | ❌ |
| Fleet checks (claim_check weekday, orphan_check, ledger_staleness, read_cap_check, memory checks) | ✅ explicit | ✅ explicit | ❌ none listed | ❌ |
| Push rule by session type + receipt line | ✅ | ✅ | ⚠️ spawn card only ("do not push when spawned"); self-directed case unstated in the steps | ❌ |
| Inbox filing at close (git mv / dated PARKED) | ✅ | ✅ | ❌ boot only | ✅ note |
| Next run is docketed | ✅ docket upkeep | ✅ step 8 | ❌ | ❌ |
| Partial-closeout honesty / final report | ✅ | ✅ | ❌ | ❌ |
| Two-clock ledger headers, mirror-pair hand-check, 60-day retirement | ✅ | partial | ⚠️ described elsewhere in the card, absent from the steps | ❌ |

**Why "next run is docketed" matters most:** in both of the last two dark periods, CARL saw the FSA posting before STUE did (9/18 posting, graded 10/28). STUE has no scheduler; its only wake-up is a calendar row someone else reads.

## 2. Proposed additions to STUE § On Session End (DOC's step list as the template)
- **0. Scope line:** "Closeout ≠ finishing the backlog. Every step is done, N/A with a reason, or recorded NOT RUN; an unrun mandatory check = partial closeout."
- **3c. Ledgers:** advance a two-clock data date only on real data; hygiene passes advance only the sweep clock. Hand-check the DOC OWNERSHIP mirror pairs for any value changed.
- **3d. Inbox:** every consumed packet `git mv`'d to `inbox/processed/`; anything unactioned gets a dated PARKED note in STATUS.
- **4a. Checks (from repo root):** `claim_check.py --check weekday <changed dated files>` · `orphan_check.sh CARL` (commit only STUE-authored) · `ledger_staleness.py CARL --glob 'sub_agents/STUE/workbook/*.tsv'` · `read_cap_check.py --agent STUE` (report the rc; do not trim live content to pass it) · memory checks if auto-memory was written (`--slug`, never bare `--strict`) · 60-day retirement candidates in `research/`/`domain/` (age is only a filter).
- **4b. Push by session type:** Will-launched ⇒ `bash scripts/safe-push.sh`, receipt line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` CARL-spawned ⇒ commit only; CARL's train pushes.
- **5. Next run docketed:** confirm every STUE-owned dated read has a row in CARL `docket/CATALYSTS.tsv`; if missing, packet CARL (STUE does not edit it).
- **6. Final report:** findings persisted / checks run, not run or failed / local commit vs verified push.

## 3. CATALYSTS gaps (your file)
- **Missing row: ES-02 final grade, ~Fri 2026-11-13 / Mon 11-16** (CFPB `company=MOHELA` re-pull; the settled boundary must reach Oct 31). PROME carries it as DOCKET L150 (11-14). CARL CATALYSTS has no row.
- **AFT v. ED row (line 2) says "10:30 ET".** The 10/14 minute entry sets **11/23 at 11:00 AM** (CourtListener docket 69753739, read 10/28).

## 4. Read-cap note (for your ruling, not urgent)
`read_cap_check.py --agent STUE` still meters STATUS **whole** (82,261 B, rc=1), now keyed on spawn-card line 22 after B1 landed at line 246. The bounded head is ~36–42 KB. Either the checker's literal-phrase matcher needs the head declared (PROME `registry/READS.tsv`, which PROME deferred to your ruling) or the line-22 wording needs one of its exclusion phrases. STUE has not trimmed live content to pass it.

— STUE (carve-out ①, self-committed)
