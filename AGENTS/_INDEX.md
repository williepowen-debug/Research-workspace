# AGENTS Index

**Purpose:** Human-friendly organization layer for the flat `AGENTS/<NAME>/` directory.

**Important:** Canonical agent paths remain flat. Do **not** move active agent folders without a migration pass; many docs, scripts, and Claude Code workflows reference `AGENTS/<NAME>/...` directly.

Canonical topology / transmission map: [`_NETWORK.md`](./_NETWORK.md).

## Quick groups

| Group | File | What it covers |
|---|---|---|
| Credit / Consumer / Banks | [`_CREDIT.md`](./_CREDIT.md) | Labor, consumer credit, housing, banks, Florida, REIT/CRE |
| Private Credit / Insurance | [`_PRIVATE_CREDIT.md`](./_PRIVATE_CREDIT.md) | BDCs, CLOs, PE-insurance wrappers |
| Energy / Geopolitics / Commodities | [`_ENERGY.md`](./_ENERGY.md) | Military shocks, oil, climate→economy, fertilizer, cruise/tourism, policy/geopolitical vectors |
| Funding / Macro / Market Structure | [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md) | Treasury plumbing, rates, Japan/China/Europe, FX, econ tape |
| Synthesis / Trading / Operations | [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md) | Cross-agent synthesis, adversarial review, trade construction, delivery, research ops |

## Canonical roster (live)

Active + Tier-2 agents and meta-agents with live folders. Full verified classification + evidence → [`../PROME/ROSTER.md`](../PROME/ROSTER.md).

> **This table groups by SUBJECT (Credit / Energy / Funding / Synthesis) — that is a different axis from RESPONSIBILITY CLASS.** As of the **2026-08-05 Phase 1 taxonomy pass**, `PROME/ROSTER.md` splits the live roster into five descriptive classes — **ORGANIZING / SERVICE · REVIEW / QC · DOMAIN ACTIVE · PROVISIONAL ACTIVE · EVENT-DRIVEN SPECIALIST** — and **owns that assignment.** Read it there; do not infer responsibility class from the group column here, and **do not mirror the per-agent class into this table** (a duplicated high-churn field rots independently — the failure this pass exists to fix). Labels are **descriptive only**: they change no routing, boot priority, grading or read obligation. Neither `PROVISIONAL ACTIVE` nor `EVENT-DRIVEN SPECIALIST` is a demotion.
>
> *Historical note: this table previously described its members as "Active + Tier-2 **domain owners**," carrying the same flattening the Phase 1 pass corrected in ROSTER — several rows here (NEXUS, WALTER, RED) are organizing/service or review lanes rather than uniform domain owners. (TERRY and ORACLE were listed in this parenthetical until 8/6 — removed, Will-directed review: the same Phase 1 pass rules both **DOMAIN ACTIVE**, TERRY explicitly overriding the preflight's service bucket.)*

| Agent | Canonical path | Primary group |
|---|---|---|
| AEOLUS | [`AEOLUS/`](./AEOLUS/) | Energy / Commodities (climate→economy; cross-links Credit, Funding/Macro) |
| BOND | [`BOND/`](./BOND/) | Funding / Macro |
| BRENT | [`BRENT/`](./BRENT/) | Energy / Geopolitics |
| BROCK | [`BROCK/`](./BROCK/) | Private Credit |
| CARL | [`CARL/`](./CARL/) | Credit |
| CORAL | [`CORAL/`](./CORAL/) | Credit |
| CREED | [`CREED/`](./CREED/) | Credit · Tier-2 (explicit-permission spawn) |
| DAEDALUS | [`DAEDALUS/`](./DAEDALUS/) | Meta — fleet architect (on-demand) |
| DEWEY | [`DEWEY/`](./DEWEY/) | Synthesis / Ops · Tier-2 |
| HANS | [`HANS/`](./HANS/) | Funding / Macro · Tier-2 |
| FALCON | [`FALCON/`](./FALCON/) | Energy / Geopolitics (Iran-Gulf war theater; ←HAWK split 7/12) |
| FERT | [`FERT/`](./FERT/) | Energy / Commodities (fertilizer supply/price/policy → food-CPI → CF; nitrogen + phosphate; potash TRIAGE-ONLY per FERT `CLAUDE.md` §POTASH; re-chartered EVENT-DRIVEN 2026-08-16, ←archive-source) |
| HAWK | [`HAWK/`](./HAWK/) | Energy / Geopolitics (cross-war synthesis + dormant book) |
| HENRY | [`HENRY/`](./HENRY/) | Funding / Macro |
| HOMER | [`HOMER/`](./HOMER/) | Credit (housing asset market; ←CARL promotion 7/12) |
| LABOR | [`LABOR/`](./LABOR/) | Credit |
| LIQUID | [`LIQUID/`](./LIQUID/) | Funding / Macro |
| MARCO | [`MARCO/`](./MARCO/) | Energy / Geopolitics / Credit bridge |
| MIDAS | [`MIDAS/`](./MIDAS/) | Energy / Commodities (metals: monetary gold/silver + industrial copper/PGM) |
| NEXUS | [`NEXUS/`](./NEXUS/) | Synthesis / Ops |
| ORACLE | [`ORACLE/`](./ORACLE/) | Synthesis / Ops |
| OSPREY | [`OSPREY/`](./OSPREY/) | Energy / Geopolitics (Russia-Ukraine war theater; ←HAWK split 7/12) |
| OTTO | [`OTTO/`](./OTTO/) | Credit · Tier-2 |
| RED | [`RED/`](./RED/) | Synthesis / Ops |
| REGINALD | [`REGINALD/`](./REGINALD/) | Credit |
| SAM | [`SAM/`](./SAM/) | Funding / Macro |
| SHADE | [`SHADE/`](./SHADE/) | Private Credit |
| TERRY | [`TERRY/`](./TERRY/) | Synthesis / Ops |
| VIOLET | [`VIOLET/`](./VIOLET/) | Synthesis / Ops |
| VULCAN | [`VULCAN/`](./VULCAN/) | Funding / Macro (AI-capex concentration / market structure; systemic) |
| WAL | [`WAL/`](./WAL/) | Credit (Western Alliance single-name specialist — thesis v2.3, frozen-frame print grading, FRAUD/ litigation arc; promoted from REGINALD 2026-07-25) |
| FLG | [`FLG/`](./FLG/) | Credit (Flagstar Financial single-name specialist — NYC rent-regulated multifamily/CRE concentration, formerly NYCB; first greenfield build 2026-08-20, off REGINALD matrix v2.0) |
| OZK | [`OZK/`](./OZK/) | Credit (Bank OZK single-name specialist — revived 2026-07-18 on its Q2 gate exactly as pre-registered; ROSTER flipped 7/22; this row moved from Dormant 7/25 registration sweep) |
| WALTER | [`WALTER/`](./WALTER/) | Synthesis / Ops |
| WATT | [`WATT/`](./WATT/) | Energy / Commodities (power/grid: PJM stress → price → cost) |
| RAV | [`RAV/`](./RAV/) | Meta — deep factual/analytical reviewer + bounded repair (Codex, Will-driven) |
| YEYOU | [`YEYOU/`](./YEYOU/) | Meta — repo-wide reviewer (manual/branch) |
| ZHAO | [`ZHAO/`](./ZHAO/) | Funding / Macro (China — UST demand / capital flows / Korea; reactivated 2026-07-05) |

*PROME runs from root [`../PROME/`](../PROME/); the historical `AGENTS/PROME/` tree is archived under [`../PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/`](../PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/).*

## Dormant / archive-source folders — present, do not launch without cause

| Folder | Tier | Note |
|---|---|---|
| [`SENTRY/`](./SENTRY/) | dormant | Cross-domain signal pipeline; human-idle since 6/02 |
| [`BARON/`](./BARON/) | dormant | Trump financial-policy network; dormant since 5/08 |
| [`CRUISE/`](./CRUISE/) | ACTIVE / EVENT-DRIVEN | Cruise-sector event specialist — CCL vehicle, BRENT fuel-cost transmission (re-classed 2026-08-21, `PROME/ROSTER.md` ‡‡) |
| [`ATHENA/`](./ATHENA/) | archive-source | Reading / knowledge companion — do not launch |

## Retired → `AGENTS/_archive/`

BUFFER · DOC · EARNINGS · FOREX · DARWIN — scaffolded-but-never-launched or superseded; moved out of the live tree 2026-06-27. **HERMES** folder removed (mail-carrier deprecated by the messaging overhaul). **REITS** (REIT tape → [`CREED/`](./CREED/)) and **TRADES** (→ [`TERRY/`](./TERRY/)) folders were pruned in the 2026-06 public-prep cleanup.

## Maintenance rule

When adding a new agent:
1. Create the canonical folder as `AGENTS/<NAME>/`.
2. Add it to this roster.
3. Add it to exactly one primary group file, plus cross-links if it bridges domains.
4. Update `PROME/ROSTER.md` (verified classification) if it is an operational agent, not just an experimental/workbook folder; add it to the `AGENTS.md` chain table and `_NETWORK.md` only if it joins a named transmission chain.
