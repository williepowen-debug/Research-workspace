# TODAY.md — Monday April 6, 2026

**Markets CLOSED (evening).** Futures opened ~6 PM ET. Iran pause expired today.

Scenario D dominant (82%). War Day 36. Brent **$109 🔴**. Gas **$3.99 🟡**. HY OAS **316** 🟡. VIX **23.87** 🟡. USD/JPY **159.64** 🔴.

---

## 🔴 TODAY — Mon Apr 6

- [x] **Prompt 6 captured** — Emergency Dispatch (2 versions from LLMs)
- [x] **Prompt 6 extracted** — Key principles for WALTER
- [x] **Prompt 7 extracted** — Key principles for WALTER
- [x] **Signal Registry Draft A** — Data model, state machines, API sketch
- [x] **GitHub push** — All WALTER files committed
- [ ] **Prompt E (Notice/Circular Split)** — Draft if requested
- [ ] **LLM research prompts B/C/D** — Entity resolution, FAR calculation, broker coordination

## 🔴 Coming Up

- [ ] **TUE 4/7: HY OAS print** — adjudicates RED debate R4. Reduce HYG 8→4 if 305-320. Exit if <300. Hold if >340.
- [ ] **TUE 4/7: First weekday news sweep** (8:30 AM cron)
- [ ] **THU 4/10: Weekly claims** — FL Wave 1 lag test. CRITICAL.
- [ ] **TUE 4/15: TIC data** — first post-escalation print. ZHAO domain.
- [ ] **WED 4/16: OZK Q1 earnings** — REGINALD domain.
- [ ] **MON 4/21: WAL Q1 earnings** — REGINALD domain.
- [ ] **WED-THU 4/23-24: BOJ meeting** — hike live (~35-40%). SAM domain.

## Key Levels (refresh at Tue open)

| Ticker | Value | Zone | Note |
|--------|-------|------|------|
| HY OAS | 316 | 🟡 | Await Tue print for RED debate adjudication |
| CCC OAS | 981 | 🟡 | Below 1000 |
| Brent | $109 | 🔴 | Iran pause expired = gap risk realized |
| Gas | $3.99 | 🟡 | Hair below $4 breakpoint |
| USD/JPY | 159.64 | 🔴 | Retreated from 160+ |
| SOFR-IORB | 0.00 | 🟢 | Clean |
| VIX | 23.87 | 🟡 | Post-quarter-end reversion |
| APO | $107.04 | 🔴 | Below $113 stop — decision pending |
| KRE | $66.00 | 🟡 | Jun→Dec roll pricing this week |

## Notable Since Last Session

- **WALTER research complete** — 7/7 prompts captured, 2 extraction docs done
- **Signal Registry drafted** — UUIDv4 entities, state machines, SQLite default
- **GraceDB model adopted** — central event store with annotations
- **Superevent grouping** — multi-agent correlation for same event
- **FAR-based thresholds** — quantified confidence, not binary
- **Metropolitan Capital FDIC shuttered** — first 2026 US bank failure ($11.2M loss, 2,300 accounts)
- **Oman-Iran Hormuz talks** ongoing — reopening negotiations

---

*Positions → `PROME/POSITIONS.md` | Signal Registry → `AGENTS/WALTER/design/SIGNAL_REGISTRY_DRAFT_A.md` | Dashboard → `python3 FORGE/tools/market-data/dashboard.py` | News → `python3 FORGE/tools/news-sweep/sweep.py --compact`*
