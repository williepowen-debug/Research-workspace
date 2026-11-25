# TRADE IDEA — CRWV Feb-19-2027 40/30 put spread — AI-infrastructure financing stress, entered on a relief rally
**Date:** 2026-11-24 (written 23:4x EST from `date`)
**Setup ID:** `IDEA-CRWV-AIFIN-NOV24`
**Thesis owner:** LIQUID (AI-infrastructure financing is the credit channel that is actually working: `PROME/inbox/processed/2026-11-24_from-LIQUID_D-L1252-issuance-freeze-read.md`; packet `inbox/processed/2026-11-24_from-LIQUID_D-L1252-issuance-read-for-reread.md`). VULCAN owns CoreWeave and AI capex. HENRY: two clocks (`AGENTS/HENRY/research/2026-11-24_credit-equity-read/READ.md`). TERRY owns only the construction.
**Terry verdict:** CONDITIONAL — **NOT-FIRED, NOT approved.** Proposed to Will via PROME under D:L1252. TERRY lean: approve as NOT-FIRED, low conviction (§8).
**Confidence in trade structure:** Medium-Low.
**Data freshness:** ⚠️ All figures are after the 11/24 close. Spot is the 11/24 regular close (vendor, `fetch.py`, read 23:3x EST). The chain is the vendor screen (`chain_fetch.py`, fetched about 23:40 EST; last option trades 15:19–15:59 ET): **screening marks, not fill prices** (durable finding 5b). **Re-price on the broker chain in the session before any order** (root rule #4). Position truth: FORGE mirror 11/18 shows no CRWV line; later changes `[POSITION_STATE_UNKNOWN]`.

## 0. Hard caveats
- [x] Live price checked: CRWV $42.60 −11.85% [11/24 close]
- [x] Option chain checked, screening only (after hours)
- [x] Position truth: `[POSITION_STATE_UNKNOWN]` after the 11/18 capture
- [ ] **Catalyst dates:** CoreWeave's next earnings date is **NOT VERIFIED**. The vendor shows only the past report (11/10). It must be read from CoreWeave IR or an 8-K before any entry (RISK_RULES § Option-Specific). If it falls before 2/19, either exit by the time stop or write the print-hold on the card in those words (construction rule #18 (c)). Nvidia's 10-Q is due about 12/04 (12/09 with a 12b-25; VULCAN's arithmetic, not an IR date).
- [x] Thesis owner current: LIQUID 11/24 23:22 ET
- **$500 default:** inside, $326.30 at the limit. **X1 sizing gate CLOSED (DON'T-SIZE, `PROME/STATUS.md` § Restrictions):** entry needs Will's explicit X1 choice on this card. Nothing is pre-approved.
- **Book overlap:** with the approved `IDEA-HYG-FOLLOW-NOV05` (fill UNKNOWN), the two together risk up to **$632.80**, 1.27× the default if they are counted as one idea (§6a). That is Will's choice.
- ⛔ `IDEA-NVDA-CEOGAP-NOV12` stays DEAD. This card does not revive it: different name, different direction.

## 1. One-line setup
Own a capped bet that the financing squeeze on AI-infrastructure borrowers gets worse at its epicentre. Enter only on a green-day relief rally while CoreWeave's credit still prices distress. Never chase the selloff.

## 2. Preconditions
- **Thesis precondition:** LIQUID's read stands: refusals are concentrated in AI-infrastructure and the weakest credits (UST Global pulled 11/16; ING's data-centre loan auction short of bids 11/20; an Oracle data-centre loan piece sold mid-80s; Nebius swapped a HY bond for a one-year loan). GATE-LIQ-069 has 3 legs fired (L4 on 11/20). CoreWeave 5Y CDS is about **1,314 bp [11/24, DTCC via LIQUID's converter]**, up from 1,078 [11/18], its highest in LIQUID's record. LIQUID's odds (unscored): about 45% that a neocloud or data-centre borrower restructures or misses a financing deadline within 1 to 3 months.
- **Tape precondition (trigger T1, both legs):** (a) CRWV completes a regular-session close **≥ $48.00** on a **green** session (a relief rally; 11/23 closed at $48.33); AND (b) LIQUID's latest CoreWeave 5Y CDS read, dated no more than 2 sessions before the entry, is **≥ 1,200 bp**.
- **Catalyst precondition:** CoreWeave's earnings date has been read from IR (see §0).
- **Do NOT trade if:** CoreWeave's planned roughly $4B IG loan launches and prices (LIQUID's unknown: the financing door reopens at the epicentre); LIQUID's CDS read is under 1,000 bp; or the broker debit is above $3.25.

## 3. Chart / tape read (vendor closes, 11/24)
| Item | Read |
|---|---|
| Current price | CRWV **$42.60** (−11.85%), 61.2M sh. Last 5 closes 47.83 · 44.91 · 39.51 · 48.33 · 42.60 |
| Trend | Down hard: $91.72 [10/6] → $42.60, −53.6%. 60-bar high $99.83, low $39.51 [11/20] (60 of 60 bars) |
| Peers, 10/6 → 11/24 | NBIS 249.87 → 87.31 (−65%) · IREN 41.28 → 12.95 (−69%) · APLD 25.34 → 12.22 (−52%) · ORCL 144.24 → 109.50 (−24%) · SMH −32.5% since its peak (HENRY) |
| Breadth (HENRY) | RSP $213.96 +0.54%, flat since 9/21 while HY is +97 bp. KRE +0.32%, IWM +0.53%. The fall is the chip and AI complex, not the market |
| Vol | Realised (60 bars, vendor closes): 10-day 197%, 20-day 160%, 60-day 115%. Implied (screen): Feb-19 40P 109%, 30P 119%; Jan-15 115–127%. **Implied sits below 10- and 20-day realised** and near 60-day |
| Liquidity | Feb-19 40P 7.35/7.50, OI 10,185 · 30P 3.35/3.45, OI 5,776 (vendor). Jan-15 30P OI 106,840. Penny-wide to 15-cent markets at the close |

## 4. Entry
- **Trigger:** T1 (a) and (b) above, any session through **Fri 2026-12-11** (covers LIQUID's freeze-test week 11/30–12/4, Nvidia's 10-Q around 12/04, and the FOMC on 12/9).
- **Order:** one complex order, never legged, limit **≤ $3.25** net debit (32.5% of width). Today the screen mid is $4.03, so the cap blocks entry now. That is deliberate: no chase.
- **Do not chase:** above $3.25, or on a red CRWV session.
- **If missed:** the card lapses at the 12/11 close. A later entry is a new card.
- ⚠️ **Construction rule #15:** leg (a) opens on a rally, which means the market has priced LESS of this thesis that day. The gate firing is **not** evidence the thesis is working. Leg (b), CDS still ≥ 1,200 bp, is the only thesis-information leg.

## 5. Structure
| Item | Figure |
|---|---|
| Legs | CRWV **Feb-19-2027 40P / 30P**, ×1 |
| Screen 11/24 (spot $42.60) | 40P 7.35/7.50 · 30P 3.35/3.45 ⇒ mid $4.03, outer $4.15 |
| Model at the trigger (Black-Scholes, IV 109/119% from the screen, 4% rate; not a broker Greek) | spot $48 → about $3.02–3.12; spot $46 → about $3.31–3.40 |
| **Max loss** | **$326.30** at the $3.25 limit ($325 + $1.30 fees at $0.65 per contract per side) |
| Max gain | about $672.40 at CRWV ≤ $30 on 2/19 ($675 less exit fees) |
| Breakeven | **$36.75** at the limit: −23.4% from a $48 entry, −13.7% from today's $42.60 |
| DTE | 87 at 11/24 |

**Alternatives considered:**
- **Jan-15 40/30:** mid $3.58 today, model about $2.49 at $48. Cheaper, but 52 days is shorter than LIQUID's 1-to-3-month horizon (construction rule #16).
- **Outright 40P:** about $7.43; pays the full 109% vol with no wing sold.
- **NBIS, IREN, APLD:** smaller names, wider markets, already down 52–69%.
- **ORCL:** the October put-spread card lapsed unfired on 11/20. Oracle is a tenant and a lender at once, so it is a less pure expression.
- **A lender leg (OWL, $9.12 +0.55%):** no named loss and no BROCK or LIQUID direction. No card.
- **Short shares:** undefined loss on a name that rallied +22% in one session (11/23).

**Why this expression:** it sits at the epicentre of the working channel. It has the deepest options book among the neoclouds. The spread sells the richer 30P wing. Feb-19 covers the 1-to-3-month horizon.

## 6. Risk / scoring
### 6a. EFFECTIVE-N
| Field | Entry |
|---|---|
| N_claimed | 3: CoreWeave CDS, the AI-infrastructure deal refusals, GATE-LIQ-069 equity legs |
| Shared antecedent | AI-infrastructure financing appetite. One event, CoreWeave's $4B loan clearing (or a clean Nvidia 10-Q with an AI rally), would hit all three |
| **N_eff** | **1, sized as one view, ×1** |
| Book overlap | Approved HYG ×5 (fill UNKNOWN). The shared antecedent is the AI-led credit move, but **the falsifiers differ**. The HYG card dies on broad HY at or under 330 for 5 closes (LIQUID: about 30% by 12/11), and this card can still pay in that case if the squeeze stays at the epicentre. This card dies on the epicentre's financing reopening, while HYG can still pay on a non-AI broad freeze (LIQUID about 20%). Correlated, not identical: **count them as about 1.5 views, and as one view against the $500 default if Will prefers**: $632.80 together |

- **Risk unit:** $326.30 max loss = 1.3R (1R ≡ $250, cap 2R = $500).
- **Edge:** no positive expectancy shown and no probability of profit stated. The one measured point in its favour: implied vol (109–119%) is below 10- and 20-day realised (197%, 160%), so on that measure the convexity is not overpriced. Against it: the equity has already fallen 54% and the CDS is already at its record.
- **Invalidation (after entry):** LIQUID's CoreWeave 5Y CDS under 1,000 bp; or CoreWeave's $4B loan prices; or a CRWV close ≥ $60.00. Sell at the bid.
- **Gap/event risk:** Nvidia 10-Q around 12/04 (clean ⇒ AI rally; NT 10-Q or Item 4.02 ⇒ gap down). FOMC 12/9 (HEN-63 hike 0.70). Optimum grace about 12/16 (not a CoreWeave event). CoreWeave earnings date UNVERIFIED. Single-name gaps run both ways at 160–200% realised vol.
- **Liquidity:** acceptable on the screen. Thanksgiving week is thin (11/26 closed, 11/27 short); prefer no entry on 11/27.
- **Execution block:** T1 both legs · CoreWeave IR date read · Will's approval AND his X1 choice on this card · broker debit ≤ $3.25 · green CRWV session.

## 7. Target / management (written before any fill)
- **Harvest (durable finding 9):** sell at a broker bid **≥ $6.00** (60% of width). That is +$272.40 net at a $3.25 entry with fees both ways.
- **Partial:** none; ×1.
- **Roll rule:** none pre-registered (Non-Negotiable #6).
- **Time stop:** sell by the close **Fri 2027-02-05**, or the session before CoreWeave's earnings if they fall earlier (once the date is IR-verified).
- **Review cadence:** at each LIQUID CDS read and at each CRWV green session while the card is unfilled. After a fill, at each LIQUID read.

## 8. Why not / counter-trade
- **The obvious trade is already done.** CRWV is −54% and the CDS is at its record. Buying protection after the crash pays for a move the market has already made. The rally-entry trigger is the only defence.
- **Short-covering rallies are violent:** +22.3% on 11/23. One clean Nvidia 10-Q or a CoreWeave financing headline could send it past the $60 kill.
- **HENRY's base case is range (about 50%).** In a range a debit spread bleeds.
- **LIQUID's 45% is for any neocloud or data-centre borrower, not CoreWeave itself.** CoreWeave's own odds are lower and unestimated.
- **Most of LIQUID's deal facts are relays.** Weekly HY volume is UNMEASURED.
- **TERRY's lean:** approve as NOT-FIRED, low conviction. It is the one expression that isolates the channel LIQUID measures as working rather than broad HY. It costs at most $326.30 and refuses to chase. If Will wants no AI-equity exposure beyond his HYG approval, declining is equally sound.

## 8b. Trigger forecast (WQ-493 A)
- **Trigger event:** CRWV completes a regular-session close ≥ $48.00 on a green session while LIQUID's latest CoreWeave 5Y CDS read (≤ 2 sessions old) is ≥ 1,200 bp.
- **Deadline:** Fri 2026-12-11, 16:00 ET close.
- **Resolution basis:** vendor daily bars re-pulled after 16:15 ET (`fetch.py`) for the close and colour; LIQUID's committed CDS read (DTCC via LIQUID's converter) for leg (b).
- **Probability:** **0.40, subjective (TERRY).** The price leg alone is likely at 160–200% realised vol (it closed at $48.33 on 11/23). The joint leg is harder, because a rally to $48 usually comes with tighter CDS. Grades the trigger only, not the trade. `CALIBRATION.tsv` CAL-0010.

## 8c. Re-read 2026-11-25 09:4x–09:5x EST (PROME morning wake; no term changed)
- **Every term above stands: no level, operator, instrument or consequence changed.** Still NOT-FIRED, NOT approved, X1 CLOSED.
- **Tape (vendor, intraday, red day):** CRWV **$37.75 −11.40%** (09:47); T1 (a) now needs **+27.2%** to a green $48.00 close. Leg (b): LIQUID's 1,314 bp [11/24] stands (WALTER SIG-W-20261125-013 relays the same figure as a record, secondary); it is too old for an entry after 11/26, so a later entry needs a fresh LIQUID read.
- **Screen:** 40P 9.35/9.40, 30P 4.50/4.70 ⇒ **mid $4.78, outer $4.90**; IV 111.7% / 123.1%. Model at those IVs: $3.25 near CRWV $46, $2.91–3.13 at $48 (70–86 DTE). The cap and the trigger still agree.
- **Earnings date:** still not verifiable (Q4 FY2026 date unannounced). Precedent: Q4 FY2025 reported 2026-02-26, announced 2026-02-05 (CoreWeave IR). If repeated, after the 2/19 expiry and the 2/05 time stop. Read from IR before any entry, as before.
- **Trigger odds:** registered CAL-0010 stays 0.40 (graded as registered). TERRY's current unscored view: **about 0.20**.
- **Evidence today:** no financing-specific evidence (VULCAN: valuation de-rating; SpaceX GPU lease notes priced upsized). Lean unchanged: A, low conviction; B equally sound. Note `research/2026-11-25_morning-tradeability/NOTE.md` §1.

## 9. Decision
- [ ] APPROVE NOT-FIRED: ×1, limit ≤ $3.25, max loss $326.30, on T1 and a green CRWV session by 12/11, **with Will's X1 choice on this card**
- [ ] REJECT
- [ ] REWORK with changes: [what]

**APPROVAL REQUIRED — Will must approve/reject before execution.**
