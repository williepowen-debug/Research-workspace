# AGENTS.md

Detect stress transmission early enough to position ahead of consensus.

**Transmission Chains:**
1. **Credit:** LABOR → CARL → REGINALD → repricing (CREED national CRE/CMBS + CORAL geo convergence + HENRY velocity + LIQUID amplification)
2. **Private credit cascade:** BROCK → SHADE (insurance) → LIQUID (funding)
3. **Energy shock:** HAWK → BRENT → HENRY (demand destruction)
4. **Japan:** SAM — independent trigger via carry unwind → LIQUID
5. **Volatility:** VIOLET — credit-to-vol lag detection → HENRY, LIQUID, RED

NEXUS synthesizes across all chains. MARCO feeds immigration/labor supply into LABOR + BRENT. **VIOLET tracks credit-to-vol transmission — when credit spreads widen and VIX hasn't caught up.** **TERRY converts thesis into trade construction: entry, structure, sizing, invalidation, roll/no-roll rules, and postmortems.**

## Agents

Grouped directory views live in `AGENTS/_INDEX.md`; the canonical topology map lives in `AGENTS/_NETWORK.md`. Canonical agent paths remain flat as `AGENTS/<NAME>/` to avoid breaking existing scripts, docs, and Claude/OpenClaw workflows.

| Agent | Domain | Chain | Spawn? |
|-------|--------|-------|--------|
| LABOR | Employment, claims | Credit | ❌ Persistent (Telegram) |
| CARL | Consumer credit, housing | Credit | ❌ Persistent (Claude Code/Telegram) |
| REGINALD | Regional banks (OZK, WAL) | Credit | ❌ Persistent (Claude Code/Telegram) |
| CORAL | Florida real estate, insurance, FL banks, migration/tourism | Credit (geo convergence) | ❌ Persistent (Claude Code) |
| CREED | National CRE / CMBS market stress | Credit (CRE→bank bridge) | ❌ Claude Code roster — explicit permission only |
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
| TERRY | Trade construction, chart/tape analysis, execution rails | Utility / trading desk | ✅ OK + Claude Code |
| DARWIN | System evolution | Utility (inactive) | ✅ OK |
| **VIOLET** | **VIX, vol term structure** | **Credit → Vol** | **✅ OK** |

---

## First Message

On session start, read `PROME/BOOT.md` and follow its sequence.
Before `/clear` or `/new`, read `PROME/HANDOFF.md`.
Orchestration + protocols: `PROME/BOOT.md`, `PROME/CLOSEOUT.md`, `PROME/AUTONOMY.md`, `PROME/COMPLETION_SPEC.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md`

---

## Safety

- Don't exfiltrate private data. Ever.
- `trash` > `rm`
- **Internal actions** (read, organize, search): do freely
- **External actions** (emails, tweets, public posts): ask first
- **Trade proposals** → Will approves/rejects (binary). Never execute without approval. TERRY may propose trade structure; approval still required.
- **Agent check-in proposals** → when agents propose research or new tracking, route to Will for approval. Standard practice.
- **Autonomy/proposal rules:** `PROME/AUTONOMY.md`; task completion format: `PROME/COMPLETION_SPEC.md`. Historical Toscanini files live under `PROME/archive/TOSCANINI_2026-03/`.

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
