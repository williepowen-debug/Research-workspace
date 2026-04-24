# OZK — INSIDERS

Insider behavior tracking — selling activity, departures, retirements, board changes. What the people with the most information are doing with their own money and careers.

---

## File Instructions

### SELLING.md
Form 4 activity tracker. Every insider transaction gets logged:
- Name, title, date, action (buy/sell/gift)
- Shares, price, % of holdings
- 10b5-1 plan? (Y/N — discretionary sales are stronger signals)
- Context (what was happening at the bank when they sold?)

**Scoring:** Discretionary CRO/CFO sells during reserve cuts = strongest signal. CEO non-selling with 10% stake = captive, not confident. Zero buying across 12 months from anyone = full convergence.

**Update frequency:** Check SEC EDGAR Form 4 filings bi-weekly minimum. Before earnings (April 16) pull fresh data.

### DEPARTURES.md
Executive and board departures, retirements, and role changes:
- Name, prior title, date of departure/announcement
- Replacement (if any) — who they hired and where from matters
- Stated reason vs likely reason
- Whether departure was during a structurally significant period

**What to watch for:**
- "Retirements" that coincide with deteriorating credit quality
- Made-up titles (lateral moves that are demotions — see WAL's Gibbons as template)
- Replacements hired from restructuring/advisory backgrounds
- Board additions of risk specialists (boards add risk people when thinking about risk)
- Gaps — positions left unfilled signal either chaos or intentional thinning

### TIMELINE.md
Chronological master view — every insider event (selling, departures, board changes) on a single timeline alongside key bank events (earnings, charge-offs, regulatory actions). The goal is to see patterns that aren't visible when selling and departures are tracked separately.

Format:
```
YYYY-MM-DD | [SELL/DEPART/BOARD/BANK] | Description
```

---

## Existing Research (Migrate From)

The following files contain insider work that should be consolidated here:
- `../research/INSIDER_ACTIVITY_COMPILED.md` — Full compiled reference, scored. CRO, CFO, Director, CEO activity.
- `../sources/INSIDER_SCAN_OZK.md` — Raw scan data + WAL comparison.

**Migration note:** Move the OZK-specific analysis here. The WAL insider data in INSIDER_SCAN_OZK.md should stay in sources or move to WAL's equivalent folder.

---

## Current Score

🔴 **FULL CONVERGENCE (Score 13)** — All C-suite sells, zero buys across 12 months, CRO sold discretionarily during reserve cuts.

---

*Thesis → `../THESIS.md` | KB → `../workbook/KB.tsv`*
