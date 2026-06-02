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

## 2026-06-02 — Boot + file-tree catch-up [pruned 4 stale sections >2wk: 5/1, 5/8, 5/10-11, 5/11; collapsed 5/15-17 to open items]

**Things noticed during the catch-up (factual hygiene session — no analysis pursued):**
- CALENDAR + STATUS PREDICTIONS sections were both stale at REG-24 60% / REG-25 55% — never synced to the 5/21 v2.2 ratchet (canonical PREDICTIONS.tsv was already 70%/75%). Synced both. Lesson echo: a thesis-version bump touches more files than the headline four; sweep PREDICTIONS *consumers* (STATUS, CALENDAR) not just the canonical tsv.
- Credit bifurcation is the one signal that didn't fade with the risk-on tape: CCC OAS 946 [6/1] vs HY 272, ratio 3.22x→3.48x. Recorded in STATUS macro-read; Will reviewed and chose to keep in STATUS (no separate tripwire / ROADMAP item this session). If it keeps widening, candidate for a CCC/ratio early-warning trigger to supplement the lagging HY>320 tripwire.

**Carried-forward open research threads (orphaned from pruned sections — promote to ROADMAP investigations on next research pass):**
- **"Juris banking"** (from WAL Q1 transcript, 5/1) — named multiple times as the "real surprise driver." Still no KB row capturing what it actually IS (business / counterparty / monetization). Research add.
- **Investor Day Slide 113 stress test** (from 5/15-17) — 5.3% total loan loss rate under 2026 severely-adverse, CET1 stressed to 9.0% — *exceeds* v2.2 Bear-fast assumptions. Mgmt pre-positioning "we can absorb worse than bears model." Open SCENARIOS.md cross-check (analysis pass, not this session).
- **Investor Day Slide 89 NDFI peer chart** (from 5/15-17) — "13% 12% 12% 11%" chart text vs 10-Q's 25.2%-of-HFI / 7.9% Business+PE. Likely different denominator. PDF deck would resolve. Low priority.

---

## 2026-05-21 — 10-Q drill + V2.2 ship [PRUNED at closeout; durable bits in MEMORY LAST SESSION + WAL/CHANGELOG]

**Things noticed but didn't dig into:**
- WAL 10-Q does NOT contain the Investor Day Slide 89 NDFI peer chart referenced in 5/15 SCRATCH — that was a deck-specific comparator and doesn't surface in 10-Q narrative. Slide 89 ground-truth still requires PDF deck read.
- $13M non-performing senior lien loan purchased in Q1 + "plans to acquire additional non-performing senior lien loans as appropriate" — WAL is making a deliberate strategy of senior-lien acquisition to defend LAM collateral. Worth tracking as a sub-vector of V2 recovery — if WAL keeps buying senior liens, it's defensive (good for net recovery) AND signals they're not confident in standard workout. KB candidate.
- $60M LOI subsequent event (different substandard credit at carrying value) — positive but isolated; suggests not all problem credits will need to be written down at distressed marks. Worth Q2 print reconciliation: did the LOI close? At what price relative to carrying value?
- Active litigation against **Jefferies Financial Group** (parent) in NY Supreme Court Mar 2026 — material escalation from "complaint against LAM subsidiary." Discovery process could surface NEW Leucadia-platform info; worth periodic docket checks. **NY Sup Ct PACER-equivalent search would be a useful one-off.**

**One-liners cached:**

```bash
# WAL 10-Q drill recipe (verified 5/21):
curl -s -A "REGINALD research willie@research.local" -o wal-20260331.htm "https://www.sec.gov/Archives/edgar/data/1212545/000162828026033054/wal-20260331.htm"
.venv/bin/python3 -c "import re; t=re.sub(r'<[^>]+>',' ',open('wal-20260331.htm').read()); t=re.sub(r'\s+',' ',t); open('wal-20260331_text.txt','w').write(t)"
# Result: 5.3MB raw → 339KB stripped — consistent with MEMORY findings 10x XBRL inflation

# Search patterns that worked:
grep -oiE "(Schedule O|Table 16|large credit)" wal-20260331_text.txt   # 0 hits — not 10-Q items
grep -oiE "(Leucadia|Jefferies|Cantor)" wal-20260331_text.txt          # 3+9+9 hits — V2 inventory CLEAN
.venv/bin/python3 -c "import re; text=open('wal-20260331_text.txt').read(); [print(text[max(0,m.start()-100):m.end()+300]) for m in re.finditer(r'days past due', text, re.IGNORECASE)]"
```

**Open externality:**
- WAL Investor Day Q&A transcript still not located (downgraded priority post-v2.2; 10-Q B1 fire is the bigger trigger). Could escalate v2.2 → v2.3 if B1-from-Q&A surfaces.
- Cross-bank life-science pattern: WAL $99M + OZK IQHQ. Watching for #3.

---

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
