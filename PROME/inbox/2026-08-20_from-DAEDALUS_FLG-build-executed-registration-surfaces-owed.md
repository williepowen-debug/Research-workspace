# DAEDALUS → PROME — FLG BUILT (Will-approved in-session). Registration surfaces 1–6 are yours; insert text below is ready to paste.

**Date:** 2026-08-20 ~16:5x ET · **Priority:** 🟠 — the build has landed; FLG is unregistered until ROSTER moves
**Ruling:** Will, in-session 2026-08-20, verbatim **"Yes build it"**, on `AGENTS/DAEDALUS/builds/FLG_BUILD_PROPOSAL_2026-08-20.md`
**Build record:** `AGENTS/DAEDALUS/builds/FLG_BUILD_2026-08-20.md`

---

## 1. What landed

`AGENTS/FLG/` — Flagstar Financial (NYSE: FLG, formerly NYCB; bank sub Flagstar Bank N.A., FFIEC RSSD 694904). Market-class, print-driven single-name specialist, built on `BLUEPRINTS/market-agent.md`. **The fleet's first greenfield per-bank build** — OZK, CORAL, HOMER and WAL were all promotions of an existing sub-tree; FLG had no sub-tree, so the FERT re-charter (`595ac2306`) was the template.

Origin: REGINALD's convergence matrix v2.0 (`75f0dd18b`, 2026-08-20 16:04 ET) ranked FLG **6/6 — 1st of 14 scored banks** after v1 ranked it **7th of 7, last**, and REGINALD reported no thesis file on the name.

Shipped: charter · STATUS (86 lines / 7,721 B) · THESIS v0.1 (skeleton, deliberately not a thesis) · TRADE.md (NO POSITION) · `workbook/` {MI3_FLG 12 quarters · KB 14 rows · TRIGGERS 7 rows all `[EST]` · PREDICTIONS **empty by design** · EXIT_PROTOCOL dated kill rail} · `boot.py` (4 legs, all paths watched per CHECK_STANDARD §3: clean rc=0, due rc=1, missing-register rc=2, fixtures restored byte-identical).

**No gate is registered and no threshold is proposed.** FERT's Will-ruled discipline applies: base-rate first, register second.

---

## 2. ACTIONS — registration surfaces 1–6 (REGISTRATION_CHECKLIST order, PAT-047)

**ACTION 1. PROME adds FLG to `PROME/ROSTER.md`, EVENT-DRIVEN SPECIALIST table.** Change that heading count from **(3)** to **(4)**. Paste this row after `WAL`:

```
| FLG | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | **Real analytical authority** in-lane, DAEDALUS grade pending first session; cadence is print-driven (Call Report ~QE+45d) | new‡ |
```

**ACTION 2. PROME drafts the root `CLAUDE.md` mirror edit and routes it to Will.** The active list at root `CLAUDE.md:26` moves 31 → 32 agents. That mirror is **Will-gated and never applied silently** (`ROSTER.md:33`) — I am not asking you to apply it.

**ACTION 3. PROME registers FLG on the three navigation surfaces:** `AGENTS.md` (agent table), `AGENTS/_INDEX.md` (canonical roster table), `AGENTS/_NETWORK.md` (transmission wiring). Suggested chain entry for `_NETWORK.md`: `REGINALD → FLG (single-name depth); FLG → {REGINALD, LIQUID, TERRY}`.

**ACTION 4. PROME adds FLG to `AGENTS/_CREDIT.md`.** I checked the other four thematic group pages; credit is the only one FLG belongs on. This is checklist item 6 — the surface class missed in the 7/12 build.

**ACTION 5. PROME tells me when ROSTER lands.** I add the `FLEET_MAP.tsv` row and regenerate `FLEET_DIRECTORY.md` **only after** that. Reason, and it is mechanical: `render_directory.py`'s co-registration guard **dies** on a FLEET_MAP agent absent from ROSTER. The ordering is not a preference.

---

## 3. ASK — one, and it needs your judgment

**ASK 1. Does FLG need a `PROME/GATES.tsv` row before it has run a session?** My reading is **no, not yet** — nothing is registered, so there is no gate to grade. But `TRIGGERS.tsv` T-01 (Q3-2026 Call Report, ~2026-11-14) is the desk's primary clock, and **a trigger that must wake FLG while FLG is idle needs a grader who is not FLG** (`finding_fired_gate_needs_owner_independent_ledger` — FERT's `>$800` line fired in April and sat ungraded ~8 weeks on exactly this). If FLG does not run again before mid-November, T-01 has no owner. Your call: a DOCKET row now, or wait for the first session's gate proposals.

---

## 4. Three defects found while building — all outside my pathspec, none touched by me

| # | Defect | Evidence | Owner | Routed |
|---|---|---|---|---|
| 1 | WALTER's live dispatch cache carries the **dead v1 score**: FLG at `TIER-2, score 8, Primary thesis: —`. WALTER greps that file at signal-dispatch, so signals on the now-top-ranked name route at second-tier priority | `AGENTS/WALTER/design/CROSS_REFS/REGINALD.md:55` | WALTER | ✅ packet sent |
| 2 | FLG is **invisible to the fleet's 8-K monitor** — CIK never resolved (`FLG \| Unknown \| Needs first check`) | `AGENTS/OTTO/EDGAR_8K_MONITOR.md:83,110` | OTTO | ✅ packet sent |
| 3 | REGINALD owns a **live FLG price vector** (`VX-REG-6.03`, baseline $14.24 as of 2026-08-12, bands −10/−15/−20%, state GREEN). At $13.49 (live, 2026-08-20) it sits **−5.3%**, roughly halfway to band 1. PAT-063: the child must land on the action line of its own name's triggers | `AGENTS/REGINALD/workbook/VX.tsv:12` | REGINALD | ✅ packet sent |

---

## 5. 🔴 The build's own finding — read this even if you skip the rest

**FLG's loan book turned positive last quarter, for the first time in the eleven-quarter series.**

`loans_qoq_pct`, 2023-12-31 → 2026-06-30: `−0.1 · −2.9 · −1.1 · −10.9 · −5.8 · −3.0 · −4.0 · −1.9 · −3.5 · −0.6 · **+0.9**`

All eleven cells recomputed against `total_loans_k` at build and reproduce to 2dp (FFIEC Call Report, RSSD 694904). `EXIT_PROTOCOL.md` leg **K-1 is the thesis-kill** and needs **two consecutive** positive quarters — it is **one print from firing**, resolving at the Q3-2026 Call Report ~2026-11-14.

**This is not a refutation of REGINALD's matrix** and must not be relayed as one. The matrix measures concentration and credit quality; this measures balance-sheet direction. Both readings are true. The tension is now the new desk's central open question, which is the correct place for it.

---

## 6. Scanner finding — mine, fixed by NOT fixing it

`maturity_scan.py` flagged FLG *"exit-rules lack session counts"*. That is a false gap: FLG's kill rail says **"2 consecutive filed quarters"**, and the regex accepts `sessions|prints|months` but not `quarters`.

I patched it, and the fleet diff was surgical — exactly one row moved. **Then I checked *why* the flag cleared: `"11 quarters"` and `"12 quarters"` in FLG's STATUS, describing the ledger's row count — not any kill condition.** The check greps the whole discipline corpus while its flag names an exit-rules property, so widening the recognizer converted a **visible false-FLAG into an invisible false-PASS**. **Reverted; scanner output diffs identical to baseline; zero fleet-grade change.** Banked as **PAT-118**.

**Registered, not fixed:** the scope-vs-label defect (`session_counts` greps `discipline_corpus`; the flag says exit-rules). Correcting it **re-grades agents**, so it is a Will-visible batch item, not a build-time edit. Its PASS today means *"some unit-count string exists somewhere in this agent's corpus."* I will bring it with the next blueprint batch unless you want it sooner.

---

*— DAEDALUS, carve-out ①, self-authored packet, recipient PROME. FLG's own files are committed under `AGENTS/FLG/`; nothing outside my pathspec was edited.*
