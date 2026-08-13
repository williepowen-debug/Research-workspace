# BRENT → PROME — **P6 VERDICT: KILL.** EU gas storage does not transmit to crude. Feed routed to SAM.

**2026-08-13 ~14:xx ET · Will-approved slate item P6 · `$0` moved · zero thresholds · zero registrations · zero capital · arm stays RETIRED.**

> ## ⚖️ **VERDICT: KILL — no BRENT instrument, no level, no registry row.**
> **EU gas storage transmits to GAS, not crude.** Storage predicts **TTF 2–3× more strongly than crude at every horizon**, and what little crude signal exists **runs through gas prices** — it is TTF with extra steps, and TTF is not mine either. **The prior I stated before looking was KILL, and the data agrees — but it agrees on the numbers, not on my say-so.**

**Artifact: `AGENTS/BRENT/setups/2026-08-13_P6-eu-storage-crude-transmission-PREREG.md` — pre-registration and verdict in ONE file, prereg section unedited.**

## 1. Pre-registered before any data was pulled

**Mechanism named** (gas-to-oil switching — the only channel by which a storage % reaches crude), **instruments named** (AGSI+ fill vs Dated Brent `DCOILBRENTEU`, with `BZ=F` robustness and `TTF=F` as the control), **metric named** (seasonal `DEFICIT` = fill% − same-calendar-day mean of prior years, because raw fill% is ~90% seasonality), and **the verdict rule fixed as numbers**: KEEP ≥0.35 · NO-VERDICT 0.20–0.35 · **KILL <0.20 at every horizon**. I also pre-committed the shared-antecedent guard (Test C) as *"the single biggest way this test can produce a false KEEP."*

## 2. Result — and n removed my escape hatch

**AGSI+ gave 5,702 daily observations back to 2011-01-01** — far more than the "small n, cannot tell" limit I had pre-registered as a possible honest outcome. **n ≈ 4,550 usable; the ≥200 floor is cleared ~23×.** This is a real measurement, not a detection-floor problem.

| h | ρ **Dated Brent** | ρ `BZ=F` | ρ **TTF** | partial (crude \| TTF) |
|---:|---:|---:|---:|---:|
| 5 | **−0.055** | −0.052 | −0.139 | −0.040 |
| 10 | **−0.082** | −0.072 | −0.186 | −0.066 |
| 21 | **−0.104** | −0.115 | −0.211 | −0.091 |
| 42 | **−0.101** | −0.110 | **−0.235** | −0.067 |

**|ρ| vs crude is 0.055–0.104 — below the 0.20 KILL floor at every horizon.** Excluding 2022 (Nord Stream) changes nothing (−0.055/−0.076/−0.071).
✅ **The SIGN is correct** (deeper deficit → higher forward crude), so the mechanism isn't backwards — **it is just far too weak to be an instrument.** Reporting that because it's the half that favours the hypothesis.
✅ **Test B decided it:** storage → TTF is 2–3× stronger than storage → crude at every horizon. **Gas-side channel.**
✅ **Test C:** controlling for TTF shrinks crude's relationship further. **Not independent.**

## 3. ⛔ I tried to REFUTE my own KILL, and one cell cleared the bar. I did not take it.

A full-sample rank correlation would miss a **threshold effect that only exists at extreme deficits** — **which is exactly today's regime** (DEFICIT = **−16.91pp**, near the bottom of a 15-year range). So I cut the tail:

| subsample | h=10 | h=21 | **h=42** |
|---|---:|---:|---:|
| ≤ −8pp | −0.191 | −0.208 | −0.126 |
| **≤ −12pp** | −0.163 | −0.265 | **−0.373 ← clears the 0.35 KEEP bar, TTF ≈ −0.106** |

**On a literal reading that is a KEEP. I am not calling it one, for three reasons — the third is fatal:**
1. **NOT PRE-REGISTERED.** The −8/−12pp cuts are mine, invented *after* seeing the full-sample result — **6 extra tests, 1 cleared.** ⛔ **That is anchor-fitting, and it is exactly what I killed the 35b incumbent band for this week** (`FUEL SPENT` fired on 1 of 8 anchors). **I will not do to myself what I refused to accept from a band.**
2. **EFFECTIVE n IS ~7, NOT 767.** The deepest tail is 767 **overlapping daily rows from SEVEN contiguous episodes** (2015 · 2017 ×2 · 2018 · **2021-05→2022-03, 319d** · 2026-01→03 · **2026-05→08, 75d**). At a 42-day forward window, rows inside an episode are near-duplicates.
3. ⛔ **THE TWO DOMINANT EPISODES ARE THE SHARED-ANTECEDENT CASE MY OWN PREREG NAMED AS THE #1 FALSE-KEEP RISK.** 2021-22 and 2026 are **69% of the tail**, and in both crude rose for reasons with nothing to do with European gas storage — the post-COVID recovery, and the Hormuz cycle. **"Low storage AND rising crude" there is two symptoms of one antecedent.**

**⇒ Documented and routed as an untested hypothesis. Not adopted, not registered, not proposed.**

## 4. Routing — SAM primary, with the whole week attached

**→ `AGENTS/SAM/inbox/2026-08-13_from-BRENT_handing-you-the-EU-gas-storage-feed-tested-and-killed-for-crude.md`**

**Why SAM:** the surviving mechanism is **EU refill competing for the same LNG cargoes Japan buys** — a JKM/import-cost question, and my own charter says *"Japan energy imports / LNG → SAM."* **Explicitly framed as decline-able**, with no ask and no reply owed — I routed on my read of the charter, not by asserting ownership of his desk.

**Everything travels so the recipient re-learns nothing:** the `gie:` probe grammar · **the gate is the User-Agent, not a key, and GIE's error text lies about which** · the **`total==0` fail-loud guard** (HTTP 200 with an empty payload on malformed queries *and* UA denial) · the undocumented-keyless caveat (row 37 = hardening-only) · **the DR-4 binding-rule correction (flexible 1 Oct–1 Dec, NOT 1 Nov)** · the state (59.32%, lowest for the date in 5 years, landing zone 77–80%) · **and my own "TTF €59 FALLING" direction error, in case it propagated to him.**

### ⚠️ ONE THING FOR YOU TO ROUTE — I RESPECTED THE AEOLUS FENCE LITERALLY
I drafted an **AEOLUS cc** (the winter-heating-demand leg is plausibly theirs: Europe enters winter on the thinnest buffer of the modern record, and whether that bites is a heating-degree-day question). **You fenced `AGENTS/AEOLUS/` and I did not write into it** — even though a cc packet is carve-out ①, the fence was stated plainly and **AEOLUS's tree is visibly mid-restructure** (6 modified DOSSIERs, 11 new untracked paths), so the fence was well-placed.
**The drafted packet is parked at `AGENTS/BRENT/outbox/pending_routing/2026-08-13_from-BRENT_cc-EU-gas-storage-feed-routed-to-SAM-winter-demand-leg-is-yours.md`.** **Deliver it when their session closes, or tell me to, or bin it — your call.** ⛔ **`git status` on `AGENTS/AEOLUS/` shows zero writes from me.**

## 5. What this vindicates, and what it does NOT say

✅ **The scoped-down framing was the right call.** The obvious version of P6 builds a storage instrument on my desk. **The kill-or-keep version cost one part-session and returns a clean negative** — and *"don't build it"* is a real answer. `[[finding_base_rate_the_threshold_before_building_it]]`
⛔ **It does NOT say EU storage is unimportant, or that 59.32% isn't alarming.** It says **it is not BRENT's instrument.** DR-5 already showed the same shape from the other side.

## 6. Housekeeping done first, per my own flag — and it found a defect

**`STATUS.md` 248 → 224 lines** before writing anything new. Archived the **CONVERGENCE MATRIX** (7/21 re-score, the oldest live-formatted block, never re-run after 7/21 and superseded by the 7/23 fire / 8/6 escalation / 8/8 ADNOC / 8/13 ADCOP) → `workbook/STATUS_archive_20260813_convergence_matrix_jul21.md`, pointer left behind.
⛔ **AND ARCHIVING SURFACED A LIVE CONTRADICTION NO CHECK WOULD HAVE CAUGHT: the POSITIONS one-liner still read `token longs USO 2sh / STNG 2sh` (7/27 vintage) — it understated the book's largest undefended leg by 17× and asserted a holding that does not exist, while the corrected 8/4 block sat ~100 lines above it on the same surface.** Replaced with a pointer (TRADE.md is canonical; per my own CLAUDE.md, STATUS keeps a pointer only — **the line existing at all was the defect**). **Found by the 250-line cap forcing a read of a region nothing routinely re-reads.**

**Fences honoured:** zero thresholds · zero registrations · zero capital · arm RETIRED · **`AGENTS/AEOLUS/` and WALTER's files untouched** · pathspec commits · not pushed.

— BRENT *(carve-out ①, self-authored packet)*
