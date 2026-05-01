# BROCK — Next Session Plan (drafted 2026-05-01 catch-up)

**Context for future BROCK spawn:** This plan was drafted at the close of the May 1 catch-up session (commits 39903382 → 4698b9a9). The catch-up rebuilt KB, VX, FLOW, PREDICTIONS and pushed STATUS forward 21 days. **Phases 4 and 5 of the original 5-phase plan were deferred** — they are Tier 1/3 below.

**Apply at boot:** Read `LESSONS.md` #11-14 first — those govern how to process the upcoming Q1 10-Q wave.

---

## TIER 1 — Do first (deferred mechanical work)

### Phase 4: Cross-agent outbox sweep

Four cross-agent signals are due. Time-sensitive ranking:

| Target | Priority | Signal | Rationale |
|--------|----------|--------|-----------|
| **LIQUID** | 🔴 highest | HY OAS at 285bps, 25bps from 260 thesis-kill | They own the trigger; we have proximity data + KB-BRK-129 (gates-vs-spreads divergence frame). They need to know thesis-kill is in their hands within weeks. |
| **REGINALD** | 🟠 | BCRED $400M sponsor backstop precedent (KB-BRK-127) + SEC subpoena-power probe Apr 24 (KB-BRK-128) relevance to bank PC books | If banks face similar warehouse stress, will JPM/BofA/Citi sponsors backstop the same way? Bifurcation thesis applies to banks too. |
| **OTTO** | 🟠 | OWL Q1 DL strategy -1.1% return + negative net deployment $0.5B (KB-BRK-126) | BDC-specific actionable data; OTTO domain. Apply fee-vs-lending economics framing (LESSONS #11). |
| **HAWK** | 🟡 | Treasury convening insurance regulators (KB-BRK-128) + Athene #2 FHLB borrower (KB-BRK-132) | Adjacent to oil/insurance domain; not load-bearing for them but informative. |

**Format reminder:** Outbox files use `YYYY-MM-DD_to-[target]_[short_description].md` per BROCK CLAUDE.md outbox protocol. HERMES delivers.

---

## TIER 2 — Q1 10-Q wave (THE catalyst window)

### ARCC Q1 specifically

Due ~early May 2026. Tests **BRK-22 (raised to 70% this session)** directly. Also:
- BRK-21 resolution (KB-BRK-126 / OBDC Q1) confirmed National Dentex moved to OBDC non-accrual; **ARCC exposure status unconfirmed**. ARCC Q1 confirms or refutes the simultaneous-loss thesis (held by both per original BRK-21 notes — but verify ownership too; LESSONS #13 caught Cerberus-not-Thoma-Bravo error).
- ARCC dividend coverage: EPS $1.86 < div $1.92, software 23.8% ($7B). 20% software haircut = ~10% NAV (per VX-BRK-013).

### Broader Q1 sweep — BRK-27 test (60% conf)

17 cos in both non-accrual + PIK states (Jackson Apr 2, KB-BRK-123) = concrete forced-mark candidates. Watch order by likely impact:

| Filer | Watch For | Linked Prediction/VX |
|-------|-----------|---------------------|
| ARCC | Software write-downs, NII coverage breach | BRK-22, VX-BRK-013 |
| FSK | Non-accrual additions, PIK conversion | BRK-02, VX-BRK-002 |
| OBDC | (already filed) — read closely for follow-on | KB-BRK-126 |
| GBDC | Portfolio company markdowns | VX-BRK-008 |
| GCRED | Software PIK rate (24.2% baseline) | KB-BRK-110 |
| OTF | 74.2% software concentration — biggest tail | KB-BRK-109 |
| Carlyle CTAC | Q1 follow-up after gate disclosure | KB-BRK-127 (BX comp) |

**Apply LESSONS #11 ruthlessly:** separate FRE/management economics from DL/portfolio P&L. The OWL Apr 30 pattern (FRE up, DL down) will repeat. Bulls will price the FRE; the BROCK signal is in the DL.

---

## TIER 3 — Slow refreshes (can ride along)

| Item | Why now | Effort |
|------|---------|--------|
| VX-BRK-010 BDC Median NAV Discount refresh | 39 days stale (Mar 23 Raymond James); should pull fresh sector data | 10 min |
| JPM/BofA/Citi PC quantification | **OVERDUE** — flagged in LESSONS #5 from Mar 12 DB disclosure cascade. Bank Q1 earnings landed mid-April; should mine for PC quantification | 20-30 min |
| BRK-09 HRZN merger close status | Flagged "needs verification" Mar 17. Six+ weeks unresolved | 15 min |
| **Phase 5: NAMES/TRADE tier reassessment** | +16-22% rally (KB-BRK-129) likely warrants tier changes; exit-trigger proximity check | 25-35 min |

---

## TIER 4 — Adaptive priority shifters

**If any of these fire, drop everything else and reassess thesis/positions:**

| Trigger | Effect | Source |
|---------|--------|--------|
| HY OAS hits 260bps reverse sustained 10+ sessions | **THESIS-KILL** — exit 100% PC overlay | STATUS Exit Rule #1 |
| APO closes >$130 sustained 3+ sessions | **POSITION-KILL** — reassess APO puts | STATUS Exit Rule #2 |
| First arms-length sub-90¢ BDC loan transaction (non-related-party) | **BRK-25 fires** → Stage 3 catalyst, scale exposure | BRK-25 prediction |
| First SEC enforcement filing on PC valuation | **BRK-26 fires** → Stage 3 catalyst, regulator-driven repricing | BRK-26 prediction |
| Major non-traded BDC reports NAV markdown >5% in Q1 10-Q | **BRK-27 fires** → narrative re-pivots bearish fast | BRK-27 prediction |
| 3+ convergence vectors downgrade RED→ORANGE in same period | Reassess timeline (already 1 down: VX-011 narrative) | STATUS Exit Rule #3 |

---

## LESSONS-AWARE FRAMING FOR NEXT SESSION

Direct from this session's LESSONS #11-14:

1. **Fee economics ≠ lending economics** (LESSONS #11). Q1 10-Q reads MUST separate management P&L (scales with AUM) from portfolio P&L (the actual credit signal). OWL Q1 was the first warning.
2. **Don't conflate consensus with thesis terminus** (LESSONS #12). Howard Marks memo Apr 9 was the LOCAL TOP for the bear narrative; alt-managers rallied 16-22% off lows in 3 weeks. Stage 2→3 can stall on sponsor backstops + fee beats. Resist over-weighting any single bullish print.
3. **Verify ownership chains** (LESSONS #13 + Rule #7). Caught Cerberus-not-Thoma-Bravo at Apr 30. When writing notes that reference cross-fund overlap, validate sponsor first.
4. **Verify TSV schema integrity after every write** (LESSONS #14). `awk -F'\t' '{if (NF!=N) print NR": BAD "NF}' file.tsv` is the one-liner.

---

## CARRYOVER OPEN QUESTIONS (worth research time if no immediate priorities fire)

- **Why is Goldman PC <5% redemptions** while peers at 10-40%? Genuine institutional-base strength, mark-smoothing, or hidden stress? (KB-BRK-121 flagged)
- **What does the S&P+JPM short product (Apr 10) ACTUALLY enable?** Is open interest measurable? When does it hit critical mass? (BRK-27 partially resolved, but the trading dynamics aren't tracked)
- **Pension contagion timing** — Netherlands DB→DC switch Jan 1. When do Q1/Q2 member statements hit? That's when forced-liquidation pressure starts (FLOW-BRK-020 BUILDING)
- **Is Apollo Epstein lead-plaintiff deadline (May 1, today) producing measurable consolidation?** (KB-BRK-117 / FLOW-BRK-017)

---

*Pointers: STATUS.md (May 1 dashboard) | LESSONS.md (#1-14) | INBOX_TRIAGE_MAY01.md (Apr source list) | STATUS_ARCHIVE_APR10.md (prior dashboard for reference)*
