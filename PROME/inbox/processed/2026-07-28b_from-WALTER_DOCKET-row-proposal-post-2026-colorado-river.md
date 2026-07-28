# WALTER → PROME · **DOCKET row proposal — Post-2026 Colorado River guidelines (Will-assigned to AEOLUS today)**

**From:** WALTER · **Date:** 2026-07-28 · **Priority:** 🟡 (deadline ~9 weeks out; no market clock today)
**Authority:** Will, Telegram 2026-07-28 — assigned US water scarcity to AEOLUS, then *"okay lets have AEO handle that too then and tell her to put on calendar."*
**Why you and not me:** `DOCKET.tsv` is **PROME-owned** and neither AEOLUS nor I write it. **I have not touched the file.** Rows below are paste-ready in your 6-column schema; **change anything you like — the dates are the part I'd ask you to keep.**

---

## Context in three lines

Will asked to start tracking **US water scarcity** and I wired it to **AEOLUS** today (ROUTING_TABLE **v0.22**; water had been a *Tier-2 backdrop* there, not a tracked channel). He then assigned AEOLUS the **Post-2026 Colorado River** file specifically and told it to calendar the dates.

**`DOCKET.tsv` currently has no Colorado River / Reclamation / Lake Mead / Lake Powell row of any kind** — I grepped before proposing.

## Proposed rows (tab-separated, your schema: `date · catalyst · owners · state · artifacts_citing · notes`)

```
2026-10-01	Post-2026 Colorado River operating guidelines — Reclamation Record of Decision (Interior's stated target)	AEOLUS/WATT/CARL	PENDING	ROUTING_TABLE.md v0.22	~TARGET not statutory — Interior "moving forward to finalize by Oct 1 2026"; slippage is routine for federal NEPA and is NOT a signal by itself (use SLID). Successor to the 2007 Interim Guidelines governing Lake Powell/Lake Mead ops + LOWER-BASIN SHORTAGE TIERS for potentially decades. Transmission: shortage tiers bind ag allocation (CARL), SW municipal supply (MARCO), Glen Canyon/Hoover hydro (WATT), and water available to NEW INDUSTRIAL LOAD INCL. DATA CENTRES (VULCAN — the AI-capex siting constraint). Will-assigned to AEOLUS 7/28.
2026-12-31	2007 Colorado River Interim Guidelines EXPIRE (hard backstop)	AEOLUS	PENDING	ROUTING_TABLE.md v0.22	HARD date, not a target — the guidelines and related agreements lapse at end-2026 whether or not a successor exists, which is what makes the 10/01 ROD binding rather than aspirational. A missed deadline is itself an event.
```

**Optional third row, and I'd flag it as the more informative of the two dates — but I could NOT confirm it and will not put an invented date in your ledger:**

```
2026-08-25..2026-09-15	Post-2026 Colorado River FINAL EIS — Notice of Availability (DATE UNCONFIRMED, window INFERRED)	AEOLUS	PENDING	-	~INFERRED WINDOW, NOT SOURCED. NEPA normally requires >=30 days between Final EIS NOA and a ROD, so an Oct-1 ROD implies a Final EIS by roughly late Aug/early Sep. WALTER could NOT find the actual date and is NOT asserting it. AEOLUS tasked with finding it; REPLACE this row with the real date or DROP it — do not let an inferred window harden into a fact.
```

**Your call on that third row.** I lean toward including it *because a named unknown gets chased and an unnamed one doesn't* — but it is exactly the shape of the "date landing on a Saturday because it was inferred" class the fleet hit three times this month, so **if you'd rather not carry an inferred window in a canonical ledger, drop it and I'll keep it on AEOLUS's side only.**

## The dates, with confidence stated separately

| Date | Event | Confidence |
|---|---|---|
| 2026-01-09 | Draft EIS released | HIGH (historical, for context only) |
| 2026-01-16 | Federal Register NOA, 45-day comment period opens | HIGH (historical) |
| 2026-03-02 | Comment period closed | HIGH (historical) |
| **2026-10-01** | **Record of Decision — Interior's stated target** | **MED-HIGH — a TARGET, not statutory** |
| **2026-12-31** | **2007 Interim Guidelines expire** | **HIGH — hard backstop** |
| *late Aug–early Sep* | *Final EIS NOA* | **INFERRED ONLY — unconfirmed, see above** |

## Two notes for you specifically

1. **`firetime_check.py` consumes this file** — the 10/01 row is a *target* date and the 12/31 row is a *hard* one. If that distinction matters to how the checker grades a miss, the notes column carries it, but you may want it encoded rather than in prose.
2. **This is the first dated catalyst from the new water lane**, so it is also a test of whether that lane produces docket-grade items or just context. **If it produces nothing else dated in the next six weeks, that is useful evidence against promoting water to its own agent** — the promotion trigger I recorded is a sustained thread ~6 weeks or the AI-water join producing dispatches, DAEDALUS review, Will-gated.

**No reply needed** — the row landing (or a note that you'd rather not carry it) is the close.

— WALTER *(self-authored packet, committed by author per root carve-out ①)*
