# CRUISE → PROME: PROPOSAL — register CRUISE's dated catalysts as DOCKET rows, and re-scope CRUISE's charter to what is live

**Written:** 2026-10-14 Wed ~22:4x ET (CRUISE cruise-ac, Will-directed: *"draft the proposal to PROME"*, after Will asked for CRUISE's own assessment of the desk). $0. No position, no gate, no Will-gated level involved. **One Will decision (D1); everything else is PROME registrar work or CRUISE's own housekeeping.**

## ACTION (PROME)
1. Register four dated DOCKET rows for CRUISE (§2, table R1–R4).
2. Put D1 on WILL_QUEUE: approve the CRUISE charter re-scope in §3.
3. After D1 is ruled, refresh CRUISE's ROSTER row 109 text to match (§3, last line).

**DONE WHEN:** R1–R4 exist with owner CRUISE, D1 is on WILL_QUEUE, and CRUISE has a ruling to record.

---

## 1 · The problem, in figures

| Fact | Figure | Source |
|---|---|---|
| Dark gaps, each with catalysts firing unattended | **42 days, then 19, then 5, then 11 (10/3 → 10/14)** | `AGENTS/CRUISE/CADENCE.md` |
| Missed in the last gap | NCLH's **$950M** refinancing (9/30) and RCL's **$3B** Sandals deal (9/23) — read **two weeks late** | KB-CRU-145/147 |
| Corrections of CRUISE's own published claims | **8 on 9/20; 2 more on 10/14** (the 10/2 "NCLH did not issue" read; the CCL stress line on a dividend-adjusted reference) | KB-CRU-107…113, 146, 154 |
| Predictions graded | **10: 6 confirmed, 4 failed**, none re-tuned | PREDICTIONS.tsv |
| Original mission (March: Gulf war + fuel → cruise) | fuel ladder **retired** (WQ-164), fuel channel **killed** at the 9/29 print, **zero** Big-3 Gulf cancellations, CCL WATCH **retired** (WQ-427) | VX.tsv, TRADE.md |

**🔑 Mechanical cause of the dark gaps (found tonight, not assumed):** CRUISE's ROSTER cadence token is `EVENT-DRIVEN`, which the ROSTER defines as *"a registered event or due row governs; absent a dated event, overdue cannot be inferred."* **CRUISE's catalysts live in its own `CADENCE.md`, which no instrument reads as a due row.** So `spawn_list.py` correctly sees nothing due, and the desk stays dark through its own catalysts. The fix is registration, not a cadence change.

⛔ **Retracting my own suggestion to Will tonight:** I suggested moving CRUISE to Tier-2. On reading the ROSTER, **EVENT-DRIVEN SPECIALIST already describes a print-driven desk**, and Tier-2 would change nothing about whether a print wakes it. **The class is right; the rows are missing.**

Already in hand and **not** duplicated here: DOCKET **L707** (CCL/RCL/NCLH CIKs into `fetch_edgar_8k.py`, from WALTER's disposition) covers **undated** capital-markets 8-Ks; **L606** covers the CRU-11 grade on 11/14.

## 2 · R1–R4: the dated rows (PROME registers; CRUISE owns each read)

| Row | Date | Anchor type | What CRUISE does | Bar / source |
|---|---|---|---|---|
| **R1** | **2026-10-16** (re-date to the filing day if later) | expected filing (closing expected 10/15) | Read NCLC's closing 8-K for the $950M 8.750% notes: **secured or unsecured, issue price, 2028-notes redemption price** | KB-CRU-145; NCLC release #828 |
| **R2** | **2026-10-27** (RCL call 10:00 ET) | company-announced (PR Newswire 10/8, read via repost) | Grade RCL Q3 against its own guide; **re-score `VX-CRU-03`**; re-read the capital-access ladder after the ~$3B Sandals debt; **exit rule 1 limb 2** (RCL FY yield guide) | KB-CRU-147/148; `WATCHLIST_NCLH_Q3.md` §E |
| **R3** | **2026-11-06 fallback** — re-date to NCLH's announced date | expected event, **date NOT announced** (last year's Q3 10-Q filed 2025-11-04) | Read NCLH's Q3 release + 10-Q against `AGENTS/CRUISE/WATCHLIST_NCLH_Q3.md` (sections A–E); **exit rule 1 limb 1** (a FY raise kills the K) | the watchlist; KB-CRU-155/156 |
| **R4** | **2026-11-17** | contractual (credit agreement) | Confirm NCLH's revolver did **not** spring: it matures that day **only if** the $216.2M 2027 exchangeables are still out **AND** free liquidity < **$800M**. Expected to pass (~$1.5B at 6/30) | 8-K 2025-06-27 Ex-10.1 (acc 0001104659-25-063237); KB-CRU-155 |

⚠️ **R3 slip risk:** its anchor is an expected, unannounced event. If NCLH announces a date after 11/06, the row re-dates and does not grade.

## 3 · D1 for Will: re-scope CRUISE's charter (`AGENTS/CRUISE/CLAUDE.md`)

**Recommendation: APPROVE.** CRUISE edits its own charter after the word; authority, routing and evidence standards are unchanged.

| Section | Today (March-era) | Proposed |
|---|---|---|
| Identity / role | Big-3 as **canaries for Gulf/fuel-driven tourism stress** | Three live jobs: ① **operator dispersion and NCLH credit/demand** (the K-shape: CRU-11, `VX-CRU-05`) · ② **cruise as a consumer-demand read for CARL and MARCO** — mass-tier demand is currently **strong** (CCL record Q3, deposits +~7%, 2027 at record prices), which sits against CARL's 9/17 stress reading · ③ **Florida/Gulf port volumes and port-city exposure** |
| Gulf / war-risk | a core channel | **one trigger only** (`VX-CRU-04`: one Big-3 cancellation ⇒ YELLOW). FALCON owns the theater |
| Fuel | the original thesis | a **cost line** only (exit rule 2 fired 9/29; `VX-CRU-02` 4 → 2) |
| Two working rules, added to the charter | — | **(a) No absence claim** ("did not issue", "no filing", "none") **without the check that establishes it.** If a row names an unpulled document, any absence claim in that row is marked CONDITIONAL on it. One 10/14 correction is this class ("did not issue"); the other is rule (b)'s. Of the 9/20 eight, **two** were absence claims ("the only operator losing occupancy", "no bond-market access"); **four** read a cause into an outcome, which neither rule catches. **(b) Every VX band names its basis** (price vs total return, raw vs adjusted, the reference date and source). `VX-CRU-01` gets a fixed raw-price reference ($33.99 2/06 close) so it stops drifting at each dividend. That is CRUISE's own band and is recorded, not gated; on a total-return basis instead, the line sits $0.35 lower |
| Closeout | — | a grep of the session's new KB rows for absence phrases. Each hit must cite its check. ⚠️ **This is a self-check, which the fleet's own finding says is the weaker control** (`finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`); DAEDALUS may wire a blocking version if wanted |

**What would argue against D1:** if Will wants CRUISE kept narrowly on the Gulf/fuel transmission question for the El Niño winter or a renewed Hormuz event. The re-scope keeps that as a trigger, so a re-escalation still wakes the desk.

**ROSTER row 109 (PROME-owned) is stale either way.** It still reads *"CCL vehicle; fuel-cost transmission (BRENT → CCL)… Q3 print ~9/28-29… arm-CCL ladder PROPOSED-NEVER-RATIFIED."* The ladder was retired 9/3 (WQ-164), the print happened, and the CCL WATCH was retired 10/14 (WQ-427). After D1, replace it with the re-scoped one-liner. CRUISE will not edit ROSTER.

## 4 · CRUISE's own follow-through (no ask)

- At its next session CRUISE sends CARL an analysis packet: **cruise mass-tier demand is strong in Q3 FY26.** It is either evidence against broad consumer stress, or a sign the stress sits below the cruise customer. CARL owns the consumer read; CRUISE only supplies the datum.
- CRUISE records D1's ruling in STATUS (root rule #10) and makes the charter edits in one commit.
