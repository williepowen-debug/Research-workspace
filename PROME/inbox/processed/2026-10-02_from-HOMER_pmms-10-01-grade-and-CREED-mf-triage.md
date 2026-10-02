# HOMER → PROME: PMMS 10/01 graded, CREED MF relay triaged, GATE-HOMER-THESIS-KILL unmoved

**Date:** 2026-10-02 (Fri) ~14:1x ET
**Spawn:** Tier-2 bounded single session under Will's in-session authorization ("okay lets open up the rest of the agents you mentioned spawning earlier"), above PROME's ordinary 4-cap.
**Spawner:** prome-96 (DESKTOP).
**Scope:** PMMS 10/01 grade against pre-registration + CREED multifamily relay (SIG-W-20261001-029) + GATE-HOMER-THESIS-KILL leg check. No new direction; no trade; $0 spend.

---

## ① PMMS 10/01 = 7.28% ⇒ PRE-REGISTERED HOLD STATE FIRED

**Instrument:** Freddie Mac PMMS 30-year fixed, week of 2026-10-01.
**Observed:** 7.28% (15Y 6.60%). +25bps WoW; +57bps over 4 weeks; +73bps YoY. Highest 30Y since 2023-11-22 (7.29%).
**Pre-registration (`AGENTS/HOMER/reports/2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md`):** HOLD ≥7.05% · SOFTEN 7.01–7.04% · LIFT ≤7.00%.
**Grade:** 7.28 ≥ 7.05 ⇒ **HOLD**. 🔴 RED, second consecutive print above 7.0%, +28bps through the line, no uncrossed rung above. The 9/24 "3bps is less than one week's move" caveat is **retired** per the pre-registration.

**Primary verification (two sources):**
- freddiemac.com/pmms, WebFetch 2026-10-02: page year-stamped "October 1, 2026", text "The 30-year fixed-rate mortgage averaged 7.28% as of October 1, 2026, up from last week when it averaged 7.03%."
- FRED DGS10 pull 2026-10-02 (fredgraph.csv id=DGS10): 9/30 = 5.29% (Wed 10Y close, inside PMMS survey window).

**Residual diagnostic (pre-registration §3.1):** PMMS − (Wed 9/30 10Y + 1.92–1.94 four-week spread) = 7.28 − [7.21, 7.23] = **+5 to +7bps**, inside the 10bp line. The spread widened +7bps (192→199bps) and the 10Y rose +18bps (5.11→5.29); the +25bps WoW decomposes to ~+18bps Treasury + ~+7bps spread. **Not "all Treasury" like the four prior weeks, but still inside the regime** — the residual against the four-week spread range is within one normal week.

**Method-change caveat (ships with any "largest since 2022" statement):** WALTER's SIG-W-20261001-025 and the FT headline cite 2022-10-13 (+26bps) as the comparator. Freddie switched the PMMS method on 2022-11-17 (lender survey → Loan Product Advisor applications). Under the current LPA method, **+25bps is the series-high weekly rise** — a stronger and more honest sentence than "largest since 2022."

**Year check:** page reads 10/01/2026. ✓ (LESSONS §1–2; the year-trap on this desk is at n=4.)

---

## ② GATE-HOMER-THESIS-KILL — no leg moved toward kill; fired count 0/5 holds

Per `AGENTS/HOMER/thesis/THESIS.md` §C (FROZEN 2026-09-29):

| Leg | Kill criterion | Current state | Fired count | Direction this spawn |
|---|---|---|---|---|
| **C1 Residential conversion** (CORE) | FC sales YoY ≤0% AND FC inventory YoY ≤0%, 3 prints | Aug: sales +11.7%, inventory +41% | **0/3** | no new print |
| **C2 CMBS** (CORE) | Trepp MF DQ <6.00%, 3 prints | Aug 7.69% | **0/3** | Sept Trepp DQ ~10/01 **owed next session** |
| **C2 GSE** (CORE) | max(Freddie, Fannie) <0.50%, 3 prints | Freddie 0.64%, Fannie 0.57% (Aug) | **0/3** | no new print |
| **A1 FHA-bottom inflow** | FHA SA QoQ ↓ ×2 AND cure YoY > −15% | FHA 11.79% (Q2, 1 of 2 QoQ decline); cure −28% YoY | **½ of first conjunct** | no new print; MBA NDS Q3 mid-Nov decides |
| **A2 Rate amplifier** | PMMS ≤6.50% ×4 weekly | **PMMS 7.28%, 78bps ABOVE kill line**, 4-week direction UP | **0/4** | ⇑ moves AWAY from kill — direction of A2 confirmed |
| **A3 Builder distress** | NAHB HMI ≥40, 3 prints | Sep 32 | **0/3** | no new print |

**LITERAL FIRED-COUNT: 0 of 5 legs. 🔴 holds.** PMMS +25bps supports the A2 claim (rates block the refi/sale exit) and is directionally consistent with the C1 conversion signal (higher rates keep stress from curing on its own). It does not move any leg toward its kill. **Formal grade date 2026-11-20 unchanged.**

---

## ③ CREED multifamily relay (SIG-W-20261001-029, 8 items) — triage

**Items that TRAVEL to HOMER's book (logged to `workbook/MULTIFAMILY.tsv`):**
- **Item 2 — Trepp 2025 MF NOI medians:** NOI +1.8%, insurance pass-through decelerated from +10.9% (2024) to +2.7% (2025), revenue +2.8%, opex +3.7%. 2021-25 cumulative insurance +57.9%. CREED-PRIMARY-read (excerpt). **Material:** eases the acute C2 realization read at the margin (insurance was the biggest 2024 operating-cost driver); does NOT touch the realized-marks row (BANC, Arbor REO, S2) which is C2's load-bearing line. **Miami 33.9% NOI is CORAL's figure, not HOMER's.**
- **Item 3 — CRED iQ MF coupon gap +65bp (vs office +172bp):** MF refi gap exists but less than half of office; CRED iQ MF distress 7.5% on a $5.01B 10-month maturity tail (agent-read). Context for C2's maturity-exposure read. Does not grade a HOMER band and does NOT replace the retired $160B/$270B wall or MBA's 13% share.
- **Item 5 — CRE CLO 28% distress, 2021-22 vintage ONLY:** important TX-syndicator-exposure proxy. **The 28% is the newsletter's; the vintage scope is CREED's agent catch (E1). Carry the vintage scope every time.** ★ This is a THIRD independent instrument naming the TX 2021-22 syndicator cohort HOMER already tracks (TX auction pipeline + Trepp July MF driver + Arbor REO already named).

**Noted but NOT promoted:**
- **Item 1 — Lurin/Venetos FBI probe + involuntary Ch.7:** logged to `STATE_HSG.tsv` as sponsor-level context. **Does NOT change the current TX August auction row** — this is a personal/sponsor event, not an additional property-level filing. HOMER already carries Lurin as one of ≥6 named syndicators there. **Upgrade path:** Northern District of Texas bankruptcy-court docket read would move it from SECONDARY (Unicus Substack) to PRIMARY; owed if Lurin becomes decision-material.

**Context-only, NOT posted to ledger:**
- **Item 4** student-housing 2029-30 maturities (SECONDARY, future), **item 6** Blackstone $90M unnamed (SECONDARY), **item 7** Boulder Creek WA $500K/unit (outside priority states, buyer-appetite datapoint), **item 8** MF-only starts −22.5% MoM (newsletter unverified split; HOMER already carries the Census total of 1,275K −2.6%, not significant).

---

## ④ RESIDUE + SKIPPED CONTROLS (bounded spawn, reported explicitly per CLAUDE.md §Session Process Controls)

**Not pulled this spawn** (bounded scope; next full session owns them):
- **FMHPI Aug** (due 9/30) — docket row open
- **Trepp Sept DQ** (~10/01) — docket row open, ⛔ **mat-adj kill still armed** for the 3rd consecutive absence; first row next session
- **MBA weekly apps** (next release 10/08) — not due today
- **MND daily** — not re-pulled; the BASIS TRAP row's MND figure (7.50 Mon 9/28) is held, not refreshed
- **Fitch primary for the UWM Class A** — carried stale from the 9/29 secondary-only grade
- **D2–D4 thesis defect-register owed research** (Fannie/Freddie MF DQ 2022–24, MBA FHA SA history, NAHB HMI table) — owed before the 11/20 formal grade; not advanced

**Controls not run** (bounded spawn, SKIPPED, not completed):
- ARGUS blind closeout audit — not spawned
- CATO cold read of this PMMS grade — not spawned (the grade matches the pre-registration with no judgment call)
- Full LESSONS re-read — only §1–17 scanned (hot index first page)
- Consumer check for superseded figures — none superseded this spawn (I replaced my OWN 9/24 PMMS figure, which is a self-only vintage change)

**No new direction opened. No trade proposed. $0 spend. No Will-gated surface edited.**

---

## COMPLETION

- **STATUS:** DONE
- **CHANGED:** 7 paths — `AGENTS/HOMER/STATUS.md` (BOTTOM LINE + PMMS row + spread row + BASIS TRAP row + CATALYSTS row + DATA VINTAGE), `workbook/RATES.tsv` (header + PMMS 10/01 row), `workbook/MULTIFAMILY.tsv` (CREED items 2/3/5), `workbook/STATE_HSG.tsv` (Lurin/Venetos context), `docket/CATALYSTS.tsv` (PMMS row closed, next 10/08), `board_log.tsv` (3 WALTER signals consumed), `inbox/WALTER/processed/` (3 git-mv'd signals); plus this packet in `PROME/inbox/`.
- **RESULT:** PMMS 10/01 7.28% graded HOLD per pre-registration (RED, 2nd print above 7.0%); A2 kill count 0/4 unchanged, 78bps above kill line; thesis kill rail 0/5 holds, 🔴 unchanged; CREED MF relay items 2/3/5 logged, item 1 noted but TX auction row not upgraded.
- **GAPS:** Trepp Sept DQ (mat-adj kill armed) not pulled; FMHPI Aug not pulled; Fitch primary for UWM still owed from 9/29.
- **WILL_NEEDS:** none from this spawn — PMMS state did not change (still RED), and A2 moved AWAY from kill, which is directionally supportive of HOMER's thesis and needs no decision.
- **FOLLOW-UP:** next HOMER session first row = Trepp Sept DQ (~10/01, 3rd consecutive mat-adj absence = dated kill executes if absent); then FMHPI Aug; then CARL 3c handle ack by 10/05 → build by 10/09.

— HOMER
