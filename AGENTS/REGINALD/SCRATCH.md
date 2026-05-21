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

## 2026-05-01 PM — Wave 1 chunks 3-6 + Q1 CR sweep [PRUNED 2026-05-11; durable bits already in MEMORY/LESSONS]

**WAL Q1 transcript line-numbers (kept — useful for future quoting):**
- L22: opening — "decisive actions taken on two previously disclosed fraud-related credits"
- L28: LAM — "fully charged off the remaining $126.4 million balance of the loan to a fund of Leucadia Asset Management" + "we will not provide further commentary"
- L34: Cantor — "$29.6 million specific reserve... validated by current as-is appraisal values" + "$26 million" charged + recovery sources (UHNW springing guarantees, mortgage fraud policy)
- L106: leading-vs-lagging — "criticized assets were largely stable... special mention loans increased $78 million quarter-over-quarter, the change was not thematic"
- L154: revised guide — "core net charge-off guidance of 25-35 basis points... at or slightly above the midpoint of this range"

**Open backlog item:**
- "Juris banking" line — mentioned multiple times in WAL transcript as the "real surprise driver." Need KB row capturing what Juris banking actually IS. Research add: what business / counterparty / how does it monetize? (Investor Day May 12 may surface.)

---

## 2026-05-08 PM — May 8 Friday session [PRUNED 2026-05-11; durable bits in MEMORY findings]

Detail in MEMORY.md LAST SESSION (May 8 PM) one-line recap + commit history `d5d08d56` / `486aea0b` / `325dc8de` / `0d876199`.

---

---

## 2026-05-11 PM — Investor Day prep + tape break [PRUNED 2026-05-17; integrated to MEMORY LAST SESSION + Q&A overreach lesson durable in MEMORY Feedback]

Detail in MEMORY.md prior-session 1-line recap + LESSONS.md falsifier-status pattern.

---

## 2026-05-10/11 PM — WALTER LIAISON converged + V2.1 ship [PRUNED 2026-05-17; durable patterns in MEMORY References + LESSONS]

Detail in MEMORY.md References LIAISON entry + LESSONS.md 2 methodology entries.

---

## 2026-05-15 / 17 — Investor Day FINDINGS + SSB ladder [PRUNED 2026-05-21; durable bits in MEMORY LAST SESSION (May 15-17 1-liner) + WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md]

**Still-open research items not yet addressed elsewhere:**
- Investor Day **Slide 89 NDFI peer chart**: WAL labeled "moderate" with chart text "13% 12% 12% 11%..." — partial answer from 10-Q: NDFI 25.2% of HFI ($14.93B); Business+PE = 7.9% ties to Slide 24's "7% Ex-Mtg Credit cohort median." The 13% chart number likely uses a different denominator (Ex-Mtg basis but including PE funds in numerator?). PDF deck would resolve. Low priority.
- Investor Day **Slide 113 stress test 5.3% total loan loss rate** assumes 2026 severely-adverse with CET1 stressed to 9.0% — already EXCEEDS v2.2 Bear-fast scenario assumptions. Mgmt pre-positioning "we can absorb worse than bears model" narrative. **SCENARIOS.md cross-check open.**
- Slide 68 Mortgage Warehouse "Zero credit losses since 2010" — 10-Q silent on Atlas SP / non-bank counterparty; consistent with deck. CARL Apr 14 research already established WAL not direct to FHA-stressed servicers. Item closable.

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
