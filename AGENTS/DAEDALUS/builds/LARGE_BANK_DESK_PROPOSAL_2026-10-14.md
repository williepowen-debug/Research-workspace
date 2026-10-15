# BUILD PROPOSAL — a large-bank desk (working name GIBBS, from "G-SIB")

**Author:** DAEDALUS · **Date:** 2026-10-14 20:37 ET · **Status:** 🟡 PROPOSED — Will-gated, nothing scaffolded, no ROSTER row
**Requested by:** Will via REGINALD, 2026-10-10 11:32–11:42 ET (verbatim in `inbox/2026-10-10_from-REGINALD_large-bank-desk-proposal-inputs.md`: *"Maybe a separate agent that tracks them - REGINALD is already has its hands full"*). That note directed a proposal, not a build.
**Job:** #1 Build · **Blueprint:** `BLUEPRINTS/market-agent.md` · **Precedents:** FLG (mechanism-scoped bank desk, 8/20), CREED (Tier-2 event-driven)
**Evidence:** `builds/2026-10-14_LARGE_BANK_PRIMARY_CHECK.md` (primary-source check, 10/14; tags `[P]` primary · `[S]` secondary · `[M]` unverified)

⚠️ **Late:** this sat 4 days in DAEDALUS's inbox unread. The "build before the first prints" option is gone: 7 of the 16 in-scope firms reported 10/13–10/14. The filings persist, so a retrospective Q3 read is still possible.

---

## RECOMMENDATION IN ONE LINE

**Build it as a Tier-2, event-driven market desk scoped to one question: does stress showing up in regional banks also show up at the largest banks, and is their lending to non-bank finance transmitting it? Use a named list of 16 US firms that matches the Fed's top three supervisory categories, not a "$250B" line.**

---

## 1. WHAT

| Element | Proposal |
|---|---|
| **Question (mechanism, not "watch the banks")** | Regional stress → is it industry-wide or regional-only? And: the large-lender channel to non-bank financials (NDFI) and private credit — is it tightening, reserving, or naming counterparties? |
| **Perimeter** | **Named list frozen at charter, re-cut each quarter** — the 16 US top-tier firms in Fed Categories I–III at 6/30/2026 `[P]`:<br>**Cat I (8 GSIBs):** JPM · BAC · C · WFC · GS · MS · BK · STT<br>**Cat II:** AXP (since Q2-26, per its 10-Q) · NTRS ($179B — Category II on cross-border activity)<br>**Cat III:** USB · COF · PNC · TFC · SCHW · FITB (moving from IV to III from Q3-26, per its 10-Q) |
| **Explicit exclusions (register, with re-look condition)** | Foreign-bank US holding companies (TD, BMO, Barclays US, UBS Americas, RBC US, DB USA): no standalone earnings, and their FR Y-9C source is blocked to automated access today. HANS keeps the European parents. Re-look if a reachable data route appears. |
| **Boundary names needing an owner call before they print** | **HBAN** ($284.0B at 6/30, Category IV, in REGINALD's 14-bank cohort; likely crosses into III on Q3 data `[X]`) — prints 10/22. **FITB** ($300.2B, transitioning) — prints 10/19. Recommendation: FITB → new desk; HBAN stays REGINALD's until its category changes, then a named hand-off. |
| **Per-print read (the hand-off REGINALD asked for)** | Four items, each tagged *industry-wide or regional-only?*: ① deposit costs and interest-free deposit trend ② CRE and office reserves and charge-offs ③ NDFI / private-credit exposure, commentary and reserves ④ net-interest-income guidance. Context for REGINALD — **ungraded, no thresholds** at build. |
| **Regime watch** | Stress test and capital buffer (June), the 3/19/2026 capital re-proposal (AOCI counted in capital for Cat III/IV) — REGINALD's calendar row moves here or stays (owner call), and the reported plan to re-index the tailoring thresholds to GDP (Reuters 9/25 `[S]`; **not proposed** as of 10/13 `[P]`). |
| **Cadence** | Tier-2, event-driven (CREED precedent): quarterly prints, June stress test, regulatory events. Not daily. |
| **Ship at build** | `CLAUDE.md` charter (blueprint §1–§8), `STATUS.md` + BOTTOM LINE, `workbook/KB.tsv`, `workbook/PREDICTIONS.tsv` (empty, Class-3 enum + `Resolve_By`), `PERIMETER.tsv` (the 16, with as-of and category source), dated falsification surface day 1 (L3 requirement), minimal `boot.py` |
| **Not at build (PAT-048)** | No new scraper. Reuse REGINALD's proven SEC EDGAR route; add the SEC XBRL frames endpoint and the Fed Large Commercial Banks release, both reached today `[P]` |

## 2. WHY

| Reason | Evidence |
|---|---|
| **No desk owns large-bank fundamentals today** | Fleet grep: BROCK covers JPM/WFC/C only through its private-credit question (BRK-31); REGINALD holds a one-quarter bank-level sample and uses them as price comparators; CARL reads COF/AXP card credit. **Nobody covers BK, STT, SCHW, GS or MS as subjects** (primary check §5) |
| **REGINALD cannot tell industry-wide from regional without a comparison group** | REGINALD packet: the September leg of the regional selloff was led by the largest banks (ρ −0.72 return vs size across its 14 names, n=14, statistical not causal) |
| **The private-credit channel runs through the large lenders** | BROCK 10/02: the one named bank facility to a private-credit vehicle that tightened is JPMorgan's FSK revolver (KB-BRK-314) |
| **Capacity** | REGINALD: 12 bank prints 10/16–10/27 plus the 11/07 Call Report run; Will 10/10: "REGINALD is already has its hands full" |

**What the primary check corrected in REGINALD's draft** (all `[P]` except as noted):
- "$250B total assets" is **not** the Category III line. Category III is ≥$250B **average** assets **or** ≥$100B plus ≥$75B in one of three risk measures (12 CFR 252.5(d)); averages are four quarters of quarterly-average balances (252.2), not period-end.
- The draft list of 10 **missed BK and STT (two of the eight GSIBs), SCHW, AXP, FITB and HBAN.**
- Northern Trust is Category II at $179B; four foreign-bank holding companies are Category III below $250B.

## 3. EFFORT

| Step | Who | Size |
|---|---|---|
| Charter + scaffold from the market-agent blueprint | DAEDALUS | one session |
| Registration (ROSTER row, AGENTS.md, _INDEX, _NETWORK, 5 group pages, FLEET_MAP/directory) per `builds/REGISTRATION_CHECKLIST.md` | PROME (ROSTER) + DAEDALUS | one pass |
| WALTER routing lane (phrase list for the 16 names + the four items) | WALTER | one packet |
| HBAN / FITB owner call; AOCI calendar row home | REGINALD + new desk; Will only if they disagree | one exchange |
| First live session: retrospective read of the 7–12 already-printed firms, then live for FITB 10/19 · COF 10/20 · NTRS 10/21 · HBAN 10/22 · AXP 10/23 | new desk (PROME spawn) | one session per print cluster |

Ongoing cost: one more Tier-2 desk drawing on Will's usage limits, mostly in the two weeks after each quarter-end.

## 4. EXPECTED VALUE

- REGINALD gets the comparison group it says it lacks, before its own 12 prints finish (10/27).
- The private-credit chain (BROCK → SHADE → LIQUID/REGINALD) gains a reader at the lenders, where reserve builds and named counterparties first appear.
- The fleet gains coverage of the custody and brokerage deposit base (BK, STT, NTRS, SCHW), which nobody reads today.
- Honest limit: this is evidence infrastructure, not a trade idea. Any position stays TERRY's card and Will's approval.

## 5. DECISIONS FOR WILL (PROME registers the WILL_QUEUE row before presenting)

| # | Decision | Recommendation |
|---|---|---|
| 1 | Build the desk? | **Yes**, Tier-2 event-driven |
| 2 | Perimeter | **The named list of 16** (Fed Categories I–III, US top-tier), re-cut quarterly; foreign-bank holding companies excluded with a re-look condition |
| 3 | Timing | **This week**, so it is live for the 10/19–10/23 prints; read the earlier prints retrospectively |
| 4 | Name | **GIBBS** (from "G-SIB"; the fleet uses short human names). Alternatives: ATLAS, MORGAN |

## 6. FIRST STEP

On Will's yes: DAEDALUS drafts the charter and `PERIMETER.tsv` in one session; PROME adds the ROSTER row; REGINALD and the new desk settle HBAN and FITB before FITB prints Mon 10/19.

## 7. Caveats that travel with this proposal

- ⚠️ **No Fed holding-company data (FR Y-9C) was reachable** — the FFIEC site returned a CAPTCHA to every automated request. US totals come from SEC 10-Q/8-K filings `[P]` and match the FFIEC figures quoted by Wikipedia to $1B. Foreign-bank holding-company totals are secondary only. This is a data wall the desk will hit too; Will may be able to download Y-9C data by hand if it matters.
- ⚠️ Categories rest on the Fed's June 2026 stress-test table plus each firm's own 10-Q; the underlying risk measures (FR Y-15) were not checked. Categories move quarterly (AXP and FITB already did this year).
- ⚠️ The tailoring thresholds may be re-indexed (reported, not proposed). A named list avoids silent perimeter drift if that happens.
- Schwab's 10/15 earnings date is a calendar estimate `[S]`; several other dates came from issuer releases seen through mirrors.
- Process disclosure: the primary-check helper reached SEC EDGAR with the User-Agent already in REGINALD's scripts, which carries Will's contact email, as SEC requires. No other service received it.
