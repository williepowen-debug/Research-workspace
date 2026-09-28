# WQ-312 — is the takeout funding behind undisclosed bank resolutions market-observable? (CREED leg)

**Written:** 2026-09-27 (Sun), CREED, on PROME task WQ-312 (Will 20:25 ET). Narrow: for Q2-26 resolutions whose **cash source the banks leave undisclosed** (par payoffs, RESG repayments, VLY $341M paid off), grade whether third-party refinancing / buyer financing is observable from evidence I already hold, and how. **Existing evidence only; UNDISCLOSED funding is a limit, not a signal; successes and failures tested the same way.** No score/tool/trade change.

**Grades:** OBSERVABLE-NOW (verifiable from what I hold) · OBSERVABLE-WITH-A-NAMED-SOURCE (verifiable via a specific source I can name but must pull) · NOT OBSERVABLE (the loan is unidentified, so nothing can trace it).

---

## The one structural fact

A bank discloses the **dollar and the fact** of a payoff/repayment, **not the loan and not its takeout**. You cannot trace a takeout you cannot name. So an **aggregate** figure is **NOT OBSERVABLE** by construction; a **named** loan is at best **OBSERVABLE-WITH-A-NAMED-SOURCE** (a bounded per-loan pull). Almost nothing here is OBSERVABLE-NOW, because I hold **no loan-level takeout data** and my one systematic market channel — **CMBS conduit new-issue spreads — is blocked on a data source** (STATUS obligation 5).

## Grades

| Resolution | Named? | Grade | How / why |
|---|---|---|---|
| **FLG ~$1.1B/qtr CRE par payoffs** (aggregate, ~40–44% substandard) | No | **NOT OBSERVABLE** | No loan IDs. Takeout could be agency MF (Fannie/Freddie DUS), another bank, CMBS, or a sale — none distinguishable without identifiers. |
| — an *individual* FLG payoff, if FLG named it (cf. the Bisnow n=1 refinanced-out loan at ~6% discount) | Yes | **OBSERVABLE-WITH-A-NAMED-SOURCE** | Recorded mortgage (county records) shows the new lender; agency loan data if agency; deal press if a sale. Per-loan, a handful at most. |
| **OZK RESG repayments** (aggregate) | No | **NOT OBSERVABLE** | Aggregate; no IDs. |
| — a *named* large RESG project takeout | Yes | **OBSERVABLE-WITH-A-NAMED-SOURCE** | Trepp CMBS new-issue prose (CMBS takeout); CRE-CLO issuance report (CLO takeout); recorded mortgage / CRE press (bank refi or sale). |
| **VLY $341M "paid off and left"** (aggregate) | No | **NOT OBSERVABLE** | Aggregate. Note the asymmetry: VLY *names the failures* ($25.8M office→nonaccrual, $6.8M MF modified) but not the payoffs. |
| **Market-level refi capacity** (a proxy, never loan-matched) | — | **OBSERVABLE-WITH-A-NAMED-SOURCE** | Trepp conduit **payoff rate** (72.05% Jul, snippet-tier → needs primary); CMBS / CRE-CLO new-issue **volume** (vendor). ⚠️ CMBS conduit **spreads** are **NOT OBSERVABLE** — blocked on a data source (STATUS obl. 5). |

## What this means for how far the workout check can go

1. **The check can confirm the OUTCOME** (loan left at par / modified / went nonaccrual) — banks disclose that, for successes and failures alike.
2. **It CANNOT independently verify the TAKEOUT FUNDING in aggregate.** That is structurally undisclosed and untraceable without loan-level identifiers. ⇒ **"par payoffs prove the refi market is open" is an inference, not an observation** — do not let a success total stand as evidence the takeout channel is healthy.
3. **Named individual loans can be traced** (recorded mortgage / CMBS new-issue prose / deal press), but that is a handful, not the aggregate — and it is **biased toward failures**, because regulatory naming surfaces problem loans more than clean payoffs. Testing successes and failures the same way therefore yields *fewer observable successes*, which is itself a caveat: the observable sample over-weights what went wrong.
4. **No market-capacity backstop is available to me** for the aggregate: the systematic read (CMBS conduit spreads) is blocked, and the Trepp payoff rate is CMBS-not-bank, snippet-tier, and not loan-matched.

**Bottom line for REGINALD's integration:** treat undisclosed funding as a **hard limit** on the workout check — it maps outcomes, not the health of the takeout market. Every aggregate par-payoff / repayment figure is NOT OBSERVABLE as to its funding; only named loans are traceable, and only with a named source (a bounded pull, not done here).

---

## Sources / limits
- FLG par payoffs & Bisnow n=1: `analysis/2026-09-27_property-comparable-transfer-test.md`; `research/2026-09-26_REGINALD_TOP3_PROPERTY_TEST.md`. OZK RESG & VLY figures: REGINALD `reports/2026-09-26_CRE_top3_loss_bridge.md`, `reports/2026-09-27_VLY_CRE_transmission.md` (§ maturities). Trepp payoff rate 72.05% (Jul, snippet-tier): `research/2026-09-26_CRE_VULNERABILITY_MAP.md` §6 point 6. CMBS-spread data block: STATUS Standing Obligation 5 / SCRATCH deferred 17. **No new pulls made.**
