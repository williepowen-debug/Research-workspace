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

*(7/25 section pruned 2026-08-13 — 19d, promote-or-delete per lesson-14: the **perl EDGAR-table recipe** and the **regex-backtracking gotcha** → MEMORY §Findings; **"a stated basis is falsifiable, an unstated one isn't"** and the **control-covers-the-anticipated-case shape** → MEMORY lessons (the shape got two fresh instances today); the **EGBN two-route ACL cross-check** → MEMORY §Findings; the **small-bank-CRE-bid half-thought** → ROADMAP backlog; CCC/HY fire-#2 arithmetic DELETED as superseded by the full FRED series pulled 8/13. 7/17 section pruned 2026-08-10 — >3wk, per the lesson-14 discipline this time (same-session promote-or-delete, no unpromoted control-notes left behind): **the one live note — WALTER's BB/B sub-index gap on REG-T-03/04 — was PROMOTED to `registry/NOTES.md` §REG-T-03/04** before deletion; the other three (tripwire decomp design lesson, CFG beta-vs-substance, Brent overtaken) were already canon in ROADMAP/brief/STATUS. 7/10 section pruned 7/30 — its "two-clock header silences its own nag" note became MEMORY lesson 14 after sitting unpromoted 20 days.)*

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

## 2026-08-13 (Thu) — residue from a six-pass day

*Task ledger is NOT here — `MEMORY.md` §NEXT SESSION, per this file's own contract.*

### Tooling worth keeping
- **FFIEC `RetrieveFacsimile` accepts `facsimileFormat: PDF` and `XBRL`, not just `SDF`** — and the PDF is the *independent verification path*, because FFIEC lays the numbers out itself and your MDRM parser never touches them. Decode: base64 inside a JSON string → `pdfminer.extract_text`. This is how the OZK cells were hand-read.
- **FDIC BankFind is a genuinely independent cross-check and it exposes memo item 3.** `api.fdic.gov/banks/financials?filters=CERT:<cert>` — ⚠️ `banks.data.fdic.gov` **301-redirects**, so use `-L` or the new host. Field map found: `LNCOMRE` = `RCON2746`, `LNCI` = item 4, `LNRECONS` = construction (1.a.1+1.a.2), `LNREMULT` = 1.d. **Different agency, different pipeline — this is what closes the gap a same-source re-render cannot.**
- **`git check-ignore -v <path>` on BOTH the old and new path** is the two-second version of today's `git mv` finding. Ran it both ways on the sub-agent move and it settled the question instantly.

### Arithmetic worth keeping (so I don't re-derive it)
- **OZK RC-C decomposition Q2-25 → Q2-26, the one that killed hypothesis (c):** item 4 **+$2,273,530K** · 1.a.2 construction **−$1,931,379K** · 1.d multifamily **−$1,790,714K** · item 9 **+$98,409K** · total loans **−$444,084K** · MI3 **−$771,824K**. The secured book *shrinking* is what refutes "collateral got perfected."
- **Step-detector base rate:** 17/154 QoQ transitions = **11.0%**, 7 of 14 banks, 9 up / 8 down. Largest three: WAL +$582M (24Q1), WAL +$438M (24Q4), OZK −$432M (25Q3).

### Behavioural — parked here on purpose, not tasks
- **Twice today the correction came from someone else asking a question I could have asked myself.** NEXUS asked whether my fire-count matched the raw series (it didn't). Will asked whether OZK's collapse was a tool malfunction (it wasn't — but the question surfaced the grid defect and the step). **Both were cheap questions about my own instrument that I had not asked.** No rule fixes this; noting the shape.
- **The base rate arrived AFTER the alarm, twice in one day** — the up-cap "5 of 8 grew faster than their book" and the OZK step. Both dissolved on base-rating. The pattern is that I notice a *pattern* and reach for a *mechanism* before asking *how often does this happen anyway*.

### Half-thought, not pursued
- **Is there a bid for small-bank CRE paper, and at what level?** *(Carried from 7/25 and still unnamed after 19 days — now promoted to ROADMAP's investigations backlog with the data-source gap stated explicitly, because a note that cannot name its instrument is exactly what rots here.)*
