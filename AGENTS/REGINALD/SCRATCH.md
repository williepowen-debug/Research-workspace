# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

*(7/17 section pruned 2026-08-10 — >3wk, per the lesson-14 discipline this time (same-session promote-or-delete, no unpromoted control-notes left behind): **the one live note — WALTER's BB/B sub-index gap on REG-T-03/04 — was PROMOTED to `registry/NOTES.md` §REG-T-03/04** before deletion; the other three (tripwire decomp design lesson, CFG beta-vs-substance, Brent overtaken) were already canon in ROADMAP/brief/STATUS. 7/10 section pruned 7/30 — its "two-clock header silences its own nag" note became MEMORY lesson 14 after sitting unpromoted 20 days.)*

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*

---

## 2026-07-25 (Sat) — loose residue from the 3-leg session + the review exchange

*Task ledger is NOT here — it's `MEMORY.md` §NEXT SESSION (Mon 7/27 build / Tue 7/28 SBCF grade), per this file's own contract.*

### Tooling gotchas hit this session (all cost real minutes)
- **`.venv` path from an agent-launch cwd:** `cd AGENTS/REGINALD && .venv/bin/python3` silently doesn't exist. Always the absolute form `/home/willi/Research-workspace/.venv/bin/python3`, or `cd "$(git rev-parse --show-toplevel)"` first. Bit me twice in one session.
- **Catastrophic regex backtracking killed a grep (2-min timeout, exit 143):** the alternation-plus-quantifier form `(EGBN|WAL|...)[^|]{0,60}(CRE|IPRE)[^|]{0,40}[0-9]{2,3}(\.[0-9])?%` hangs on the matrix's long table rows. **Fix: grep the bare literal, then eyeball** — don't build a clever one-liner against a wide-table markdown file.
- **`sed 's/<[^>]*>//g'` collapses EDGAR tables to unusable single lines.** For any filing where the numbers live in a table, pre-convert cell/row closers to newlines first: `perl -0pe 's{</(td|th|p|div|tr|br|li|h[1-6])>}{\n}gi'`. EGBN's EX-99.1 stripped to **17 lines** the naive way vs usable with the perl pass. This is now the default recipe for any 8-K pull.
- **8-K exhibit shapes vary a lot and it changes what's scoreable:** AMTB publishes a **full by-class nonaccrual + past-due-accruing table in the 8-K** (so it scored fully, no 10-Q needed); BKU gives a criticized-by-segment table but no leading bucket; SSB gives nonaccrual + NCO only; EGBN uniquely **discloses 30-89 past due in the release**. Worth knowing per-name before promising a metric at print time.
- **Amusing, immaterial:** EGBN's filed EX-99.2 deck (`final-2q2026egbnearnings.htm`) contains an unredacted internal editing note — *"Date should be Earnings Release Date, not call date Do we change QR?"* Filed to EDGAR as-is. No analytical content; noted only because it's a reminder that filed decks are human artifacts.

### Arithmetic worth keeping (so I don't re-derive it)
- **EGBN ACL cross-check, two independent routes agreeing:** 1.83% × $6,622M loans = **$121.2M**; 109.01% × $111.1M NPL = **$121.1M**. Q1 check: 114.29% × $128.8M = $147.2M = the frame's §0b figure. Use this pattern to sanity-check any derived ACL before citing it.
- **CCC/HY ratio, computed not eyeballed** (the tripwire's whole content): 7/17 3.5714 · **7/20 3.6320 · 7/21 3.6357 · 7/22 3.6604** · 7/23 3.5776. Three consecutive >3.6 = fire #2. Fire #1 (7/9-13) was 3.607/3.606/3.613 — *marginal*; fire #2 was not. **This is the calculation the boot.py counter must reproduce.**
- **AMTB SFR nonaccrual RATE** (the denominator catch): 1.72% (12/25) → 1.63% (3/26) → **1.60% (6/30/26)**, on a book $1,515.2M → $1,680.8M → $1,954.2M. Dollars +320% YoY, rate *falling*. Keep the rate, not the dollars.

### Observations on the review exchange (not tasks — behavioural notes)
- **Publishing reasoning rather than a conclusion is what made my error catchable.** I asserted a definitional-basis mismatch on the matrix's 547%; PROME built an escalation on it; both were wrong; the whole thing resolved in ~6 hours *because the basis I was claiming was stated and therefore falsifiable.* PROME's line is the keeper: **"a stated basis is falsifiable; an unstated one isn't."**
- **I nearly corrected a correct claim.** My first blast-radius grep surfaced `.claude/worktrees/` and `archive/` paths, which made PROME's "external consumers" look overstated. Re-running excluding worktrees confirmed PROME was right (WALTER STATUS + CROSS_REFS, DAEDALUS profile + PATTERNS + REGINALD_CARD, live DEWEY PROMPT-19). **Lesson: when a grep result makes a reviewer look wrong, check whether the grep is scoping worktrees/archive before you type the correction.**
- **The one thing I added that neither reviewer had:** the matrix header-vs-column mismatch is **systematic across the whole table, not an EGBN quirk** — WAL sits at 474% on the same ÷Tier-1 column under the same SR 07-1 header. PROME's instinct about systematic error was directionally right, for a different reason than either of us proposed, and bounded ~10-20%.
- **Reviewers left one sequencing ambiguity that mattered:** DAEDALUS "grade SBCF first then mechanisms, same session" vs PROME "build Monday before Tuesday's print." Irreconcilable as stated because **SBCF doesn't print until Tue 7/28**. Resolved in MEMORY. Worth noting that two careful reviewers can both be right about intent and jointly produce an impossible plan — check the calendar against the plan, always.
- **Three failures this session were the same shape:** a control that covers the case I anticipated rather than the case that occurred (tripwire caught late twice · derived-surface rot caught externally twice · closeout inbox re-scan covers mid-session but not post-close landings). That shape — not any individual miss — is what Monday is for.

### Half-thought, not pursued
- **EGBN and AMTB both cleared problem credits via SALES rather than cure this quarter** (EGBN: *"collateral liquidations and sales of loans"*; AMTB: *"primarily attributable to loan sales"*). Sales usually clear at a discount, so "classified down" via disposition is a *realized* de-risking, not credits healing. If several names in a cohort are simultaneously selling rather than curing, that's a statement about **who's buying** — a distressed-bid depth question I have no instrument for. Possible investigation: is there a bid for small-bank CRE paper right now, and at what level? Would bear on whether the "de-risking" reads across the cohort holds if the bid thins. Not started; parked here rather than in ROADMAP because I can't yet name a data source.
