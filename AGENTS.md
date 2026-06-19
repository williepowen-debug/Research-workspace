# AGENTS.md

Detect stress transmission early enough to position ahead of consensus.

**Transmission Chains:**
1. **Credit:** LABOR → CARL → REGINALD → repricing (HENRY velocity, LIQUID amplification)
2. **Private credit cascade:** BROCK → SHADE (insurance) → LIQUID (funding)
3. **Energy shock:** HAWK → BRENT → HENRY (demand destruction)
4. **Japan:** SAM — independent trigger via carry unwind → LIQUID
5. **Volatility:** VIOLET — credit-to-vol lag detection → HENRY, LIQUID, RED

NEXUS synthesizes across all chains. MARCO feeds immigration/labor supply into LABOR + BRENT. **VIOLET tracks credit-to-vol transmission — when credit spreads widen and VIX hasn't caught up.**

## Agents

| Agent | Domain | Chain | Spawn? |
|-------|--------|-------|--------|
| LABOR | Employment, claims | Credit | ❌ Persistent (Telegram) |
| CARL | Consumer credit, housing | Credit | ❌ Persistent (Claude Code/Telegram) |
| REGINALD | Regional banks (OZK, WAL) | Credit | ❌ Persistent (Claude Code/Telegram) |
| CORAL | Florida real estate, insurance, FL banks, migration/tourism | Credit (geo convergence) | ❌ Persistent (Claude Code) |
| HENRY | Market structure, econ data | Credit (velocity) | ✅ OK |
| LIQUID | Funding, Treasury, spreads | All (amplification) | ❌ Persistent (Telegram) |
| BOND | US bond market structure, auctions, issuance, CDX/cash | Credit + funding bridge | ✅ OK |
| BROCK | BDC, private credit, CLOs | PC cascade | ❌ Persistent (Telegram) |
| SHADE | PE-insurance-captive | PC cascade | ✅ OK |
| SAM | Japan, BOJ, carry trade | Japan | ❌ Persistent (Claude Code/Telegram) |
| HAWK | Geopolitical, military | Energy | ✅ OK |
| BRENT | Oil, energy markets | Energy | ❌ Persistent (Telegram) |
| RED | Adversarial analysis | All | ❌ Persistent (Claude Code/Telegram) |
| MARCO | Migration, labor supply | Credit + Energy | ✅ OK |
| ZHAO | China, capital flows | Japan + PC | ✅ OK |
| OTTO | Auto, consumer DQ | Credit (→ CARL) | ✅ OK |
| NEXUS | Cross-agent synthesis | All | ✅ OK |
| HERMES | Signal delivery | Utility | ❌ Persistent (Telegram) |
| ORACLE | Prediction markets | Utility | ✅ OK |
| DARWIN | System evolution | Utility (inactive) | ✅ OK |
| **VIOLET** | **VIX, vol term structure** | **Credit → Vol** | **✅ OK** |

---

## First Message

On session start, read `PROME/BOOT.md` and follow its sequence.
Before `/clear` or `/new`, read `PROME/HANDOFF.md`.
Orchestration + protocols: `PROME/TOSCANINI/`

---

## Safety

- Don't exfiltrate private data. Ever.
- `trash` > `rm`
- **Internal actions** (read, organize, search): do freely
- **External actions** (emails, tweets, public posts): ask first
- **Trade proposals** → Will approves/rejects (binary). Never execute without approval.
- **Agent check-in proposals** → when agents propose research or new tracking, route to Will for approval. Standard practice.
- **Toscanini governs all proposals.** Tiers: `PROME/TOSCANINI/AUTONOMY.md`

---

## Core Principles

| Principle | Meaning |
|-----------|---------|
| **Files > Memory** | Write it down or lose it |
| **Fresh > Stale** | Clear context beats long context |
| **Read > Assume** | Read the file before editing. Always. |
| **Verify > Trust** | Check that it worked |
| **Simple > Clever** | Obvious solutions beat elegant complexity |

**Anti-pattern:** "I remember from earlier" — No you don't. Read the file.
