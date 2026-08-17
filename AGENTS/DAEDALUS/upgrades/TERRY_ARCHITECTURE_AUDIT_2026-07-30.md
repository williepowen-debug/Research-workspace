# TERRY — ARCHITECTURE AUDIT (structure / file system / wiring)

> 🗄 **DATED AUDIT/WORK RECORD (last content 2026-07-30; bannered 2026-08-17, self-audit F5).** Findings were routed at write time; this doc is history, not a live queue. Closure state of individual findings lives with the owning agents.

**Author:** DAEDALUS · **Date:** 2026-07-30 PM · **Directed by:** Will · **Method:** read-only, solo (no fan-out — session rules). TERRY **LIVE** (last commit 16:26, `PAPER_BOOK.tsv` uncommitted) ⇒ every fix packet-routed, **nothing edited**.
**Scope:** structure, file anatomy, wiring, enforcement reachability. **NOT** trade judgment, thesis, or card quality — not my lane.
**Prior comprehension:** `profiles/TERRY.md` (7/22) · `upgrades/TERRY_CARD.md` · FLEET_MAP row (Utility **L4** Conf H, last scored 7/22).

---

## VERDICT

**TERRY is one of the better-built agents in the fleet, and its defect mass is almost entirely OMISSION rather than rot.** Everything documented is accurate and current; the problem is what the documentation does not mention — **7 of 12 directories, 3 of 10 scripts, and both mail lanes are absent from the FILES table.** Nothing is broken in the sense of failing; several things are unreachable in the sense of never being looked at.

**The single most important finding is against MY instrument, not TERRY's files:** the fleet staleness enforcer **structurally cannot see TERRY's three live ledgers**, and it reports a benign-looking line instead of failing loud. TERRY is the **only** agent in the fleet in that state, and its ledgers are the ones that gate live capital.

**Health check first, because it is most of the file:** `boot.py` runs **rc=0** with a real health card · `ledger_sweep.py` is a genuine anti-drift enforcer and ran **clean** ("all surfaces agree, no naked superseded values") · `setups/` + `INDEX.md` + `_archive/` is the **best card-registry lifecycle in the fleet** · `inbox/processed/` discipline is strong (74 filed) · the STATUS banner convention was **fixed today** off the RAV review (append-below → rewrite-in-place, the exact defect class I found in PROME two days ago) · dual card templates, RISK_RULES/RISK_SCORING rubrics, and a POSTMORTEMS file carrying a **re-graded** root cause with a withdrawn finding. This is a desk that audits itself.

---

## FINDINGS

| # | Sev | Finding | Owner |
|---|---|---|---|
| **S1** | 🔴 | TERRY's 3 live ledgers are invisible to the fleet staleness enforcer, which passes silently | **DAEDALUS** (mine) |
| **S2** | 🟠 | `outbox/` has no `delivered/` lifecycle — 14 packets top-level, oldest 33 days | TERRY |
| **S3** | 🟠 | BOOT has no general-inbox step; an unprocessed WALTER IMMEDIATE from today is sitting in the lane | TERRY |
| **S4** | 🟡 | 7 of 12 directories absent from the FILES table — incl. a **second undocumented ledger** | TERRY |
| **S5** | 🟡 | 3 empty scaffold dirs, 2 of which are traps (`postmortems/`, `workbook/`) | TERRY |
| **S6** | 🟡 | 3 undocumented scripts, 2 load-bearing (43KB of the toolchain) | TERRY |
| **S7** | 🟢 | BOTTOM LINE contradicts itself — closes an event in ¶1, calls it "pre-staged" in the last line | TERRY |
| **S8** | 🟢 | README 13d stale vs a directory that gained 5 subdirs | TERRY |

---

### S1 🔴 — THE ENFORCER CANNOT REACH TERRY'S LEDGERS, AND SAYS SOMETHING REASSURING INSTEAD

```
$ python3 scripts/ledger_staleness.py TERRY
[TERRY] no workbook ledgers found
```

**That line is false in substance.** TERRY has three live TSV ledgers, all written **today**:

| Ledger | Rows | Role |
|---|---|---|
| `SETUPS.tsv` | 8 | the structured setup tracker — 13 columns incl. `verdict`, `will_decision`, `status` |
| `PAPER_BOOK.tsv` | 34 | the Phase-1 shadow book |
| `SIGNALS.tsv` | 15 | inbound signal ledger |

**Mechanism:** `ledger_staleness.py:243` defaults to `--glob 'workbook/*.tsv'` and `:241` enumerates *"every `AGENTS/*/` **with a workbook/**."* TERRY **has** a `workbook/` directory — containing **only `.gitkeep`**. So it is enumerated, finds nothing, prints the benign line at `:209`, and **passes**. Had `workbook/` not existed, TERRY would have been skipped just as silently.

**Blast radius measured, not assumed: TERRY is the ONLY agent in the fleet that hits this line** (`--all`, 1 of N). That is not reassuring — it means the enforcer's blind spot lands on exactly one agent, and it is **the one whose ledgers gate live capital.**

**This is a false negative in my own instrument.** Every Fleet Staleness Sweep since the mechanism shipped has reported TERRY clean **by never looking at it**. It is:
- **n=5 of the glob-scoping class in four days** — FLEET_MAP 7/28 · `walter_doctor._registry_rows` 7/29 · `ledger_staleness.py`/FORGE 7/30 AM · YEYOU `boot.py` 7/30 PM · **this**. PAT-071's family, and this instance is *the same script* as the FORGE one, failing a second way.
- **the `finding_silent_blank_evades_review` / PAT-060 shape**: a report of *"nothing found"* is indistinguishable from *"nothing to find."* A check whose null output is ambiguous cannot falsify.
- **owned by nobody.** `ledger_staleness.py` lives in `scripts/`, which `SURFACES.tsv` records as **having no named owner** — the gap I flagged this morning as the next ownership ruling. This is its first concrete cost.

**Proposed fix (mine to build, needs a word on the shared-script edit):**
1. **Fail loud, don't pass quiet** — if an agent dir has a `workbook/` but zero matching ledgers **and ≥1 top-level `*.tsv`**, emit a 🔴 `LEDGERS-OUTSIDE-GLOB` line naming the files. Generalizes past TERRY.
2. **Per-agent glob override** — the script already supports `--glob`; TERRY's sweep entry should carry `--glob '*.tsv'`. No file moves. *(Moving TERRY's TSVs into `workbook/` is the wrong fix — they are referenced by path across `CLAUDE.md`, `CLOSEOUT.md`, `boot.py`, `ledger_sweep.py` and the card corpus. **Never relocate a file to satisfy a scanner.**)*
3. **`daytrading/LEDGER.tsv` is a fourth ledger** in the same blind spot (S4).

---

### S2 🟠 — `outbox/` has no lifecycle; 14 packets, oldest 33 days

`AGENTS/TERRY/outbox/` holds **14 top-level packets** dated 6/27 → 7/27. There is **no `delivered/` subdirectory** and **no WRITE-BACK step** that moves anything. Several are demonstrably closed loops (`try-fire-004-refire-FILLED`, `wal-q2-print-gate-adjudication`, `hban-retired-kharg-wording-confirmed`).

**Consequence:** the outbox stops answering *"what is outstanding?"* — the only question an outbox exists to answer — and a reader cannot distinguish a packet awaiting reply from one closed three weeks ago.

**Fleet n=3 in three days:** BRENT (my 7/28 audit, same finding) · **VIOLET fixed its own today** (`07b3da51`, 16:32 — its commit message reads *"outbox/ had no lifecycle while 23 fleet agents already had one"*) · TERRY. TERRY is now among the last. Fix is `mkdir outbox/delivered/` + one CLOSEOUT line.

---

### S3 🟠 — BOOT reads the Will drop-zone and nothing else; a live signal is sitting unread

`CLAUDE.md` BOOT is steps 0–13. **None reads `inbox/`.** `boot.py:237` checks exactly one lane:

```
Will drop zone (inbox/WILL/): N file(s) awaiting review
```

`inbox/` (top level) and `inbox/WALTER/` are **not checked by either the prose protocol or the script**. Live right now:

> `inbox/WALTER/SIG-W-20260730-004-drone-us-fsru-damietta-first-med-strike.md` — **IMMEDIATE**, landed today, unprocessed.

The `processed/` discipline is excellent (49 + 25 filed), so this is not sloppiness — **it is a missing protocol step in an agent that otherwise files diligently.** n=2 with BRENT (7/28: *"no general-inbox boot step"*), which makes it a blueprint candidate rather than two coincidences.

---

### S4 🟡 — 7 of 12 directories are undocumented, and one holds a second ledger

| Directory | Files | In FILES table? | Note |
|---|---|---|---|
| `daytrading/` | 5 | ❌ | **A sub-desk**: `JOURNAL.md` · **`LEDGER.tsv`** · `PROFILE.md` · `QQQ_DESK_CARD.md` · `README.md` |
| `grades/` | 3 | ❌ | `ALLY.json` · `SYF.json` · `WAL.json` — machine-readable grade artifacts |
| `inbox/` | 80 | ❌ | the mail lane, incl. WALTER + WILL sub-lanes |
| `outbox/` | 15 | ❌ | see S2 |
| `research/` | 2 | ❌ | + `research/sources/` |
| `postmortems/` | 1 | ❌ | empty — see S5 |
| `workbook/` | 1 | ❌ | empty — the direct cause of S1 |
| `options/sources/` | 2 | partial | parent documented, `sources/` not |

**`daytrading/LEDGER.tsv` is the sharp one** — a fourth ledger, undocumented **and** outside the enforcer's glob (S1). An entire sub-desk with its own journal, profile and ledger exists in a directory the operating spec never names.

This is PAT-073③ (FILES-table drift) in its **omission** form rather than its stale-value form: TERRY's table has no *wrong* rows — the rows it has are accurate. It simply stopped growing while the directory did.

---

### S5 🟡 — three empty scaffold dirs, two of them traps

`charts/` · `postmortems/` · `workbook/` contain **only `.gitkeep`**.

- **`postmortems/` is a trap:** the live artifact is top-level `POSTMORTEMS.md` (142 lines, rewritten today, carrying the re-graded VIXCS root cause). An empty same-named directory is an invitation for a future session to write the next post-mortem into the wrong home and silently fork the record.
- **`workbook/` is not merely empty, it is load-bearing in the wrong direction** — its existence is what makes S1 pass quietly instead of skipping loudly.
- `charts/` is benign (documented, *"saved chart notes/screenshots if generated"*).

**Rule worth stating:** an empty scaffold dir is not free. It either becomes the home for its concept, or it is removed — the middle state creates two homes for one thing, and the enforcement question ("does this agent have ledgers?") gets answered by the *directory*, not the content.

---

### S6 🟡 — 3 undocumented scripts, 43KB of them load-bearing

FILES table documents 7 of 10 scripts. Absent: **`chain_fetch.py` (21KB)** · **`grade_print.py` (22KB)** · `csv_pnl.py` (5.7KB).

`chain_fetch.py` is cited as live-validated tooling in TERRY's own STATUS **and** in my FLEET_MAP notes as part of the L4 evidence — *"tooling live-validated (chain_fetch marks matched proposal)."* **The fleet's record of TERRY's maturity rests partly on a script TERRY's own spec doesn't list.** Related known gap: `grades/*.json` (S4) are presumably `grade_print.py`'s artifacts, and neither end of that pipeline is documented.

---

### S7 🟢 — the BOTTOM LINE contradicts itself in the same section

Opens: *"THE DESK HAS ITS FIRST REALIZED NUMBER, AND IT IS A LOSS: −$111.60 (−38.8%) on TRY-VIOLET-VIXCS"* — the exit **executed**.
Closes (last line): *"**2026-07-29 addendum:** VIXCS's 7/30 mandatory exit is now fully **pre-staged**…"* — pending tense, for an event resolved earlier the same day.

Small, but it is the one place TERRY's otherwise-excellent rewrite-in-place discipline slipped: a dated addendum survived the rewrite that superseded it. Exactly the failure mode the **7/30 banner-convention fix** was adopted to prevent — worth noting *because* the convention is one day old and this is its first residue.

### S8 🟢 — README 13 days stale; two archive conventions

`README.md` (7/17) predates `daytrading/`, `grades/`, `research/`, and the current `options/` build-out. Its `AGENTS/TRADES/` reference is correctly labelled archived/dormant — not dangling. Separately, `archive/` and `setups/_archive/` coexist with different scopes (agent-level vs card-level); defensible, but only one is documented.

---

## WHAT I AM NOT FLAGGING

- **TSVs at top level rather than in `workbook/`** — a deviation from the market-agent convention, but TERRY is **Utility** class and its ledgers are its primary product, not a research substrate. Location is fine; **the enforcer should adapt, not the files** (S1).
- **No `PREDICTIONS.tsv`** — TERRY's prediction surface is the card corpus + `PAPER_BOOK.tsv` + `grades/`. Correct for the class.
- **`STATUS.md` at 221 lines** — within its own cap, and the BOTTOM LINE is present, current, and genuinely informative.
- **The `.cache/` and `__pycache__/` dirs** — correctly gitignored (`AGENTS/TERRY/.gitignore:2`, root `.gitignore:32`), zero tracked files. Clean.

---

## DISPOSITIONS

| # | Fix | Owner | Gate |
|---|---|---|---|
| S1 | fail-loud `LEDGERS-OUTSIDE-GLOB` + per-agent glob override | **DAEDALUS** | shared `scripts/` edit — **needs Will's word**; ties to the unowned-`scripts/` ruling |
| S2 | `outbox/delivered/` + CLOSEOUT move-step | TERRY | packet |
| S3 | general-inbox boot step (prose + `boot.py`) | TERRY | packet · **1 live signal unread** |
| S4 | FILES table += 7 dirs; document `daytrading/LEDGER.tsv` | TERRY | packet |
| S5 | resolve `postmortems/` + `workbook/` (adopt or remove) | TERRY | packet |
| S6 | FILES table += 3 scripts | TERRY | packet |
| S7 | drop the superseded addendum | TERRY | packet |
| S8 | README refresh | TERRY | packet (low) |
| — | blueprint: general-inbox boot step (n=2), outbox lifecycle (n=3), empty-scaffold rule | DAEDALUS | next blueprint block |
| — | FLEET_MAP re-score — row last scored **7/22**, heavy activity since | DAEDALUS | 8/5 Production Review |

**No maturity change proposed today.** L4 stands; none of these findings is an L5 blocker, and the L5 gate on TERRY's row (gate-grader discipline holding a full cycle) is behavioural, not structural.
