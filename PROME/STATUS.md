# PROME STATUS.md
**Updated:** 2026-02-08 00:25 UTC

---

## Infrastructure Status

| Component | Status | Notes |
|-----------|--------|-------|
| **Sub-Agent System** | 🟢 LIVE | 7 agents configured (Sonnet 4.5), full onboarding docs |
| **Daily Check-Ins** | 🟢 ACTIVE | LABOR 8am, CARL 8:15am, MARCO 8:30am ET (Mon-Fri) |
| **Dashboard** | 🟢 RUNNING | http://100.86.70.6:8080 |
| **Proposal System** | 🟢 READY | Telegram buttons for approve/reject |
| **Transcripts** | 🟢 ACTIVE | Auto-saved to transcripts/, git-tracked |
| **Agent Onboarding** | 🟢 COMPLETE | Workbook conventions + CALENDAR.md in boot sequence |

**Agents Available:**
- LABOR, CARL, HENRY, SAM, REGINALD, LIQUID, MARCO
- All spawnable via `sessions_spawn(agentId="...")`
- Each has: identity, thesis, boot sequence, workbook conventions

**Agent Boot Sequence (all 7):**
1. Read domain/STATUS.md (state)
2. Read repo/CALENDAR.md (catalysts)
3. Understand request
4. Do work
5. Update STATUS.md
6. Reply

**Key Files:**
- `OPERATIONS.md` — Full operating manual
- `PROPOSALS.md` — Agent action queue
- `transcripts/` — Saved conversations
- `agent-configs/` — Git-tracked copies of agent configs

---

## Agent Dashboard

| Agent | Status | Current Focus | Next Critical |
|-------|--------|---------------|---------------|
| **LABOR** | 🔴 RED | Claims 231K (+22K spike); Challenger 108K (2009 high) | NFP Feb 11 |
| **CARL** | 🟠 ORANGE | Subprime auto 6.74% (32-yr high); prime fine | NY Fed Feb 10 |
| **HENRY** | 🟡 YELLOW | VIX 21.77 spike; MOVE 65.82 (divergence) | HY OAS tight |
| **SAM** | 🟡 YELLOW | Auction PASSED (3.64 BTC) | **Feb 8 election TODAY** |
| **REGINALD** | 🟠 ELEVATED | VLY Q4 beat = counter-signal; thesis intact | VLY Q1 ~Apr 23 |
| **LIQUID** | 🟢 GREEN | RRP ~$6B (buffer GONE); SOFR=IORB | Quarter-end Mar 31 |
| **MARCO** | 🟠 ORANGE | 8-series complete; H-2A surge | Remittance reversal H2 |
| **BROCK** | 🟡 YELLOW | PIK concentration; shadow defaults | Q4 BDC earnings Feb-Mar |
| **CREED** | 🟡 YELLOW | $936B maturity wall | Forced recognition 2026-27 |
| **CORAL** | 🟠 ORANGE | FL condo crisis; VLY exposure mapped | Blacklist → 2,000 |

**System Status:** 🟠 ORANGE — Convergence thesis validated, KRE position live

---

## 🎯 CONVERGENCE THESIS — KRE TRADE (ACTIVE)

**Trade Position (Feb 4):**
- 2x KRE $70 puts — May 15, 2026
- 2x KRE $60 puts — June 18, 2026
- Entry: KRE at $72.62 (ATH)
- Total risk: ~$800-900

**Convergence:** All 8 research streams terminate at regional banks.

| # | Channel | Source Agent | Status |
|---|---------|--------------|--------|
| 1 | CRE | REGINALD/CREED | 🟡 Extend-and-pretend |
| 2 | NDFI/Auto fraud | OTTO | 🔴 4th case brewing |
| 3 | Federal layoffs | LABOR | 🔴 DOGE 307K cuts |
| 4 | Consumer credit | CARL | 🟠 Subprime breaking |
| 5 | BDC draws | BROCK | 🟡 $142B unfunded |
| 6 | Migration | MARCO | 🟠 Enforcement shock |
| 7 | FHLB/Funding | LIQUID | 🟢 RRP depleted but stable |
| 8 | Japan contagion | SAM | 🟡 Auction passed |
| 9 | FL condo crisis | CORAL | 🟠 1,438 blacklisted |

**Top Banks by Convergence Score:**
1. EGBN (12) — DC 100%, CRE 547%
2. WAL (10) — Multi-channel + unrated munis
3. VLY (9) — FL CRE $7.4B, 45% Miami, HOA lending

---

## Active Threads

| Thread | Status | Next Action |
|--------|--------|-------------|
| **KRE puts** | 🟢 LIVE | Monitor; add on Claims >250K or 4th fraud |
| **Japan election** | ⏳ TODAY | Feb 8 — Takaichi >260 seats = fiscal pressure |
| **CORAL monitoring** | 🟢 ACTIVE | Track blacklist growth, VLY non-accruals |
| **Daily check-ins** | ⏳ MONDAY | First live run Feb 10 |

---

## Next Catalysts

| Date | Event | Agent | Priority |
|------|-------|-------|----------|
| **Feb 8 (Sun)** | Japan snap election | SAM | 🔴 CRITICAL |
| Feb 10 (Mon) | NY Fed Household Debt | CARL | 🟠 HIGH |
| Feb 11 (Tue) | NFP employment | LABOR | 🔴 CRITICAL |
| ~Apr 23 | VLY Q1 earnings | CORAL | 🔴 CRITICAL |

---

## Recent Session (Feb 8)

**Focus:** Agent onboarding polish

**Completed:**
- ✅ Added workbook conventions to all 7 agents (ML/VX/FL explained)
- ✅ Added CALENDAR.md to all agent boot sequences
- ✅ Ran REGINALD diagnostic — boot sequence works, oriented in 3-4 calls
- ✅ Synced all configs to git
- ✅ Pre-clear checklist complete

**Infrastructure now production-ready for Monday check-ins.**

---

*Session-end: memory updated, STATUS updated, ready for commit*
