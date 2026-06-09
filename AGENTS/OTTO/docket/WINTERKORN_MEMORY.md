# WINTERKORN — Memory (state)

State file for `WINTERKORN.md` (OTTO docket steward). Read this right after the spec.

**Inaugural state — no prior runs.** First spawn will populate `## LAST RUN`. Seeded sections below give the sub-agent enough bootstrap context to make its first run productive without ambiguity.

---

## CHANGES SINCE LAST RUN

*(none — inaugural)*

Sub-agent should populate this at run start by reading STATUS / THESIS / CHANGELOG / PREDICTIONS and noting what's moved since the prior `## LAST RUN` timestamp.

---

## LAST RUN

*(none — inaugural. First run, populate format:)*

```
### YYYY-MM-DD — [trigger: weekly Tue / T-3 pre-hearing / post-miss audit]
- Pruned: [list]
- Added: [list]
- Refreshed: [list]
- Modeled-date revisions: [list]
- Pre-fire verification: [N scanned; revisions; halts-on-ambiguity]
- Baseline audit: [fired? what was checked; delta proposed]
- Notes: [any observation worth carrying forward; goes to NEXT RUN HINTS too]
```

---

## PENDING

OTTO-side decisions / actions queued from prior runs. WINTERKORN adds new items; OTTO clears resolved-by-OTTO ones. WINTERKORN never removes its own entries — that's OTTO's job.

*(empty at seed)*

Future format:
```
### YYYY-MM-DD — [category: SCOPE / DATE-ESCALATION / STATUS-SYNC / PREDICTIONS-SYNC / CALENDAR-AMBIGUITY]
- [one-line description + source + suggested resolution]
```

---

## STANDING MONITORS

Recurring watches WINTERKORN should re-verify every run regardless of pre-fire window. These are the rows where source-of-truth is known to drift / be blocked.

### Per-case dockets (verify weekly during active hearing cycles)
- **First Brands docket (S.D. Tex., Judge Lopez)** — Highest-activity case. Hearing calendar revises frequently; UST motions + DS denials cascade. Re-verify all First Brands rows every run. Sources: Kroll (auth-gated → news mirrors), Law360, Octus, CreditSights, Trucks-Parts-Service.
- **Tricolor Ch.7 docket (Verita, Judge Burns)** — Verita cert-verification failure is known and recurring; primary source routinely blocks. Fallback sources: Bloomberg Law, Green Street News, Auto Finance News. Halt-on-ambiguity if all secondary sources are silent.
- **Tricolor SDNY criminal (Chu/Goodgame, Judge Liman)** — Selective scope: trial date Oct 19 2026 + cooperator motions only. Re-verify Oct 19 monthly until ~T-30; then weekly.
- **Carvana derivative / discovery (DE Chancery)** — Verify production milestone dates from StockTitan / PRNewswire / direct Chancery filings.

### Recurring releases (monthly cadence; verify forward two)
- **Fitch Auto ABS Index** — Most recent print Jan 2026 (60+ DQ 6.90%, recovery 32.64%, ANL 9.81%). Next ~Feb 2026 print due (then monthly). Source: Fitch direct + Auto Finance News.
- **NY Fed HDC (Quarterly)** — Q1 2026 released May 12. Q2 2026 due ~Aug. Source: newyorkfed.org.
- **S&P / KBRA / Moody's ABS surveillance** — Monthly + on-event. Watch for ECNL revisions, CreditWatch placements, downgrade waves.

### Bank-earnings cycle (named-banks subset only)
- Q2 2026 earnings cycle opens ~Jul 15 (JPM, WFC, C lead). Named-banks: **JPM, 5-3, BCS, Regions, MTB, OBK**. Source: SEC EDGAR + IR calendars.

### ABS pricing windows (modeled rows)
- **EART Q3 2026** — Exeter Q3 issuance typically Sep. Modeled date; revise within 7d via SEC EDGAR FWP.
- **Bridgecrest** — Carvana-related; quarterly. Watch for related-party pricing dynamics.
- **GCAR / smaller stressed shelves (CPS, Flagship, Lendbuzz, SAFCO)** — Watch for shelf-halt signal (OTTO-07).

### TRADE.md position expiries
- ⚠ TRADE.md is **rehab-pending** (stale since pre-CVNA 5:1 split May 7). Position expiries pulled from TRADE.md should be flagged with skepticism. Cross-verify with FORGE if possible. Pause adding position-expiry rows until TRADE.md rehab is complete.

---

## CALIBRATION

**OTTO-owned section. WINTERKORN reads but never writes here.** OTTO records:
1. **Declined release classes** — what OTTO decided isn't worth tracking under the current thesis lens (with date + reason). WINTERKORN excludes these from baseline-audit proposals.
2. **Accepted-as-proposed examples** — patterns WINTERKORN should keep proposing.
3. **Calibration notes** — anything OTTO wants future-WINTERKORN to know about scope decisions.

### Declined release classes
*(empty at seed)*

Format:
```
- [YYYY-MM-DD] [class name] — [reason]
```

### Calibration notes
*(empty at seed)*

---

## NEXT RUN HINTS

Notes from the most recent run for the next-WINTERKORN to read first. Captures one-off context that doesn't fit in STANDING MONITORS but matters for the next sync.

### Bootstrap hints (2026-06-09, inaugural)

**🔴🔴 IMMEDIATE: Jun 12 First Brands UST hearing is T-3 from inaugural spawn.**
The First Brands `Jun 12` row in CATALYSTS.tsv is the canonical pre-fire verification target. **If your first run is before Jun 12:** verify the §1112(b) UST convert-or-dismiss hearing is still 10am CT Friday Jun 12 (per Law360 #2482099 / Octus); halt-on-ambiguity if source is unclear. **If your first run is after Jun 12:** sweep the hearing outcome from STATUS / CHANGELOG; prune the Jun 12 row (or mark `— FIRED` for 1-week retention).

**Jun 17 Tricolor creditor meeting + Jun 17 First Brands plan-confirmation** — both T-8 from inaugural. Tricolor row already flagged as ⚠️ AT RISK / likely SLIP (no distribution-plan found May-Jun per STATUS). Verify both via the relevant docket; both are likely to revise.

**Carvana Jun 12 discovery production 2** — DE Chancery; check StockTitan / PRNewswire for any updated production schedule.

### Standing context (durable)

- **Pre-fire date verification is the load-bearing job step.** OTTO's Jun-8 catch (First Brands Jun-17 → Jun-12) is the canonical failure mode this sub-agent exists to prevent.
- **Verita Global cert issue is known and recurring.** Halt-on-ambiguity convention applies to all Tricolor Ch.7 docket fetches.
- **First Brands is the highest-activity case.** Re-verify weekly.
- **TRADE.md is rehab-pending.** Skip position-expiry additions until rehab is done.
- **Spawn cadence:** weekly Tue + on-demand T-3 pre-hearing. Outside that cadence, spawn cost > value.
