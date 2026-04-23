# OZK — Dashboard

**Updated:** 2026-04-23 | **Price:** $48.23 (+1.49% AM) | **TBV:** $47.15 | **P/TBV:** 1.02×
**Thesis:** RESERVOIR v1.3 | **Conviction:** 🔴🔴 HIGH | **KB:** 185 rows / 17 groups
**Next hard catalyst:** IQHQ RaDD maturity Aug 2026 — weighted EL $140M on $555M funded

---

## Positions

*Broker state confirmed by Will 2026-04-23. Total: 11 contracts across 4 lines.*

| Strike | Expiry | Contracts | Wave | Notes |
|--------|--------|-----------|------|-------|
| $42.5P | May 15 | 2 | Originally Wave 1 (Apr earnings — passed) | 🔴 **ROLL PENDING** → Jan27 $42.5P × 2 (~$510 debit). Hard deadline ~May 8. See `THREAD3_ROLL_MATH.md`. |
| **$47.5P** | May 15 | 2 | Near-money · separate from Wave 1 | ~$0.73 OTM at $48.23. 22 DTE. Covers May 1-10 Call Report window (MI3 / NDFI reveal). Rationale to reconfirm. |
| $42.5P | Aug 21 | 3 | 2-3: IQHQ maturity | +2 added ~early April (thesis-add, not Thread 3 execution). Hold. |
| $45P   | Aug 21 | 4 | 2-3: IQHQ maturity | Hold. |

**Thread 3 roll:** May $42.5P × 2 → Jan27 $42.5P × 2. Extends duration past IQHQ Aug maturity + Q3 recognition tempo. **Hard deadline ~May 8** (May premium decays fast). Position state above still shows the May $42.5P open — roll has NOT executed. See `THREAD3_ROLL_MATH.md` for chain quotes (may need refresh).

---

## Q1 2026 Snapshot

*Resolved Apr 21. Full synthesis → `Q1_2026_ANALYSIS.md`*

| Metric | Q1 26 | Trend | Note |
|---|---|---|---|
| EPS | $1.44 | Miss -1.4% vs $1.46 | — |
| Past due loans | **$465M (1.41%)** | 🔴 Doubled QoQ from $207M / 0.64% | Leading indicator — firing |
| Classified + criticized | $1,215M | 🔴 +23% QoQ from $984M | — |
| NCO (ann.) | **0.57%** | In-line with ~50bps FY guide | Deceleration from Q4 25's 1.18% — see Invalidation §2 |
| Provision | $41.9M | vs $45.3M NCO | ACL modest drawdown |
| ACL | $628.5M (1.26%) | — | Coverage 1.35× past-due |
| CET1 | 11.64% | Capital buffer intact | — |
| TBV/share | $47.15 | +11% YoY | Buybacks at $45.51 avg (accretive) |

**3 new substandard credits:** 2 Seattle U District (Office $76M + Life Sci $50M, signed LOI for recap) + 1 Boston Life Sci $169M (matured Dec 18 2025 — sponsor ID TODO #1)
**2 new foreclosed:** Chicago Life Sci $50M · Santa Monica Office $45M (**15% leased**, $5M charge-off on transfer)
**Near-zero-equity LTVs:** Boston Office 95% · Seattle Pioneer 100% · Wauwatosa Hotel 103%

Detail on all 11 tracked problem credits ($719M) → `SEVEN_CREDIT_DEEP_DIVE.md`.

---

## Signal Dashboard

| Signal | Current | Watch Level | Fires |
|---|---|---|---|
| OZK price | $48.23 | <$45 / <$40 | Thesis execution bands |
| Past-due loans | $465M / 1.41% | >$550M or >2.0% next Q | Recognition tempo accelerating |
| NCO (ann.) | 0.57% | >80bps mid-year | Full CRE cycle engagement |
| **NCO kill line** | — | **≤55bps through Q3** | **Invalidation §2 trigger** |
| RaDD leased % | 3.3% (JCVI 50K of 1.5M SF) | Any signing >100K SF | Scenario A probability up |
| IQHQ specific reserve | Not broken out Q1 | Any positive Q2 | Scenario B firing early |
| Sub notes reprice | Oct 1 2026 | Pre-reprice refi announcement | +$12.8M/yr · Tier 2 -20% |

**Cross-feed (ref only, not OZK-specific):** KRE $69.90 · HY OAS 294bps (Apr 8, stale) · Brent $102.66 (🔴 +8.5% since Apr 22 — stagflation re-heating)

---

## Catalyst Calendar (OZK-specific)

*Forward-looking only. Full cross-bank calendar → `../CALENDAR.md`.*

| Date | Event | Thesis Impact |
|---|---|---|
| **~May 1-10** | Q1 Call Report (FFIEC) | MI3 37.6% baseline; classified/criticized detail; specific reserves on problem credits |
| **May 8** | **Thread 3 roll hard deadline** | May $42.5P decays after |
| May 12 | WAL Investor Day (cross-read) | Possible WAL IQHQ exposure (TODO #3) |
| May 15 | $42.5P May expiry | Position expires if not rolled |
| **May-Jun** | Bluerock Q1 NAV marks (IQHQ PIK $246M) | Further markdown → Scenario B probability up |
| **Early Jun** | Aimco v. IQHQ motion-to-dismiss response | Denial → Bluerock PIK terms in discovery (bearish) |
| **Jun 18** | AOCI capital rewrite comment period closes | Cat III/IV bomb intact |
| **Mid-late Jul** | OZK Q2 2026 earnings | Dress rehearsal for Aug IQHQ resolution |
| **Aug 2026** | **IQHQ RaDD maturity** ⚠️ (corrected from Aug 2028) | 4-scenario tree. See `IQHQ_PLAYBOOK.md` |
| **Oct 1, 2026** | $350M sub notes reprice (2.75% → SOFR+209) | +$12.8M/yr interest · Tier 2 -20% for 12mo |

---

## Open Decisions

1. **May $42.5P × 2 — Thread 3 roll** (pending). → Jan27 $42.5P × 2, ~$510 debit. `THREAD3_ROLL_MATH.md`. Deadline ~May 8.
2. **May $47.5P × 2 — manage to expiry** (new item). 22 DTE, ~$0.73 OTM. Original rationale (Apr earnings) expired; current implicit rationale is May 1-10 Call Report window. Decide by ~May 8: hold through CR print, roll, or close.
3. **Boston Life Sci $169M sponsor ID** — 2 candidates (US2 vs Leggat McCall). `TODO.md` #1.
4. **Bluerock as secondary short** — gated on May-Jun NAV mark. `TODO.md` #2.

Full research backlog → `TODO.md`.

---

## Navigation

**Cold boot → `INDEX.md`** · **Thesis → `THESIS.md` (v1.3)** · **Q1 earnings → `Q1_2026_ANALYSIS.md`** · **IQHQ scenarios → `IQHQ_PLAYBOOK.md`** · **Seven credits → `SEVEN_CREDIT_DEEP_DIVE.md`** · **Roll math → `THREAD3_ROLL_MATH.md`** · **Research backlog → `TODO.md`** · **KB navigator → `workbook/KB_INDEX.md`**
