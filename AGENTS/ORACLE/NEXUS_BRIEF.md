# ORACLE — NEXUS Brief

**As of:** 2026-06-18 ~21:36 ET (pull `2026-06-19T01:36Z`) | **STATUS commit:** pending this session
**Status:** 🟠 REVIVED (was 79d dormant) — one 🔴 firing (Iran de-escalation, now **oil-corroborated**), one large standing divergence (recession −63pp)
**Domain:** Prediction-market monitoring (Polymarket) — crowd-implied probabilities & crowd-vs-thesis divergence. Broadcasts the priced baseline via this brief; inbound routed by WALTER per `SIGNAL_INTAKE.md`.

---

## VIEW
- **The crowd prices broad calm; our book prices stress — the gap is widening.** Recession 12.5% (−5/7d), "Nothing Ever Happens" 82.5% (+12/7d), bank failure/bailout/named-bank all ≤12.5% and falling. Either a contrarian edge building or the thesis decaying.
- **Iran de-escalation now corroborated in oil.** Enrichment-deal 62.5% (+41/7d, $6.3M) + WTI "$70 low" 41.5% (+30/7d) + war-premium tail (WTI "$100 high") collapsed −23/7d to 2.1%. Two independent surfaces (event market + oil ladder) point the same way → confirms WALTER 6/16.
- **Higher-for-longer entrenched.** Fed "no cuts 2026" 81.2% (+4/7d, deep $5.3M) — past the 57–70% HENRY anchored in HEN-33.
- **Bank cluster benign across the board** — failure 11%, bailout 12.5%, named-banks <1%. Crowd prices *no* banking crisis; diverges from REGINALD's stress thesis.

## CALIBRATION
- **Conviction:** the divergences are real-money, mostly deep-market (recession $1.6M, Fed $5.3M, Iran $6.3M, NEH $619K) — not thin-print noise. Bank/bailout/unemployment ARE thin (⚠) — directional read only, ≥3-day re-check before any mark (memory: thin-liquidity discipline).
- **Largest divergence:** recession 12.5% vs fleet ~76% (Apr baseline — needs RED refresh) = **~63pp**. Headline open question.
- **Discipline:** a market price is an *expectation*, not a resolution — anchor predictions to surprise-vs-this-pricing, not the headline (memory: anchor-to-surprise).
- **Uncertain:** (1) recession-calm = crowd-early-wrong (edge) or us-late-wrong (decay)? RED owns. (2) Iran enrichment is volatile intraday (66→62.5 same day) — direction clear, level noisy.

## CROSS-DOMAIN

**SENDING:**
| To | Signal | Priority |
|----|--------|:--:|
| HAWK / BRENT | Iran de-escalation now **oil-corroborated**: enrichment 62.5% (+41/7d), WTI-$70-low 41.5% (+30/7d), war-premium tail −23/7d → 2.1%. Oil-down bias. | 🔴 |
| RED | Recession 12.5% vs ~76% thesis = 63pp, widening — adjudicate edge vs decay. Need a current fleet recession number. | 🟠 |
| LIQUID / HENRY | Fed no-cuts 81.2% (+4/7d) past the HEN-33 anchor — higher-for-longer; KRE/OZK/WAL CRE-refi pressure. | 🟠 |
| REGINALD | Bank cluster benign: failure 11% / bailout 12.5% / named-banks <1% — crowd prices no banking crisis. Divergence vs stress thesis. | 🟡 |
| VIOLET / PROME | "Nothing Ever Happens" 82.5% (+12/7d) — complacency extreme, pairs with VIOLET's tape. | 🟠 |

**WAITING FOR:**
| From | Input | Why it matters |
|------|-------|----------------|
| RED | current fleet recession probability | the divergence math is only as good as the thesis side (carrying Apr ~76%) |
| WALTER | route inbound per `SIGNAL_INTAKE.md`; refresh REGISTRY row → ACTIVE | ORACLE newly revived, not yet subscribed |
| HAWK | Iran anchor state-changes | so I can check the enrichment/oil markets react |

**Cross-agent tensions known to me:** None active — but ORACLE is not yet wired into FLEET_SCAN/HEARTBEAT/dashboard (PROME action requested, see outbox).

## NEXT DECISION POINT
- **What:** re-pull each session (`polymarket.py pull --log`); 3-day re-check (~6/22) on thin movers; **roll the Jun-30 / Jul-1 markets** (bank-failure, Iran, WTI) before they resolve.
- **Tripwires:** recession >20% or gap >70pp → RED; Iran enrichment <50% (re-escalation) → HAWK/BRENT; bank-failure vol >$50K → REGINALD; Fed no-cuts >90% → LIQUID.

## FORWARD CATALYSTS
| Date | Event | Watch |
|------|-------|-------|
| Jun 30 | Iran / bank-failure / named-bank markets resolve | roll to next-period markets |
| Jul 1–2 | WTI June + unemployment markets resolve | roll to July oil ladder; replace dead unemployment mkt |
| ongoing | FOMC path | Fed no-cuts vs 1-cut repricing |

---
*Schema per `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` (followed loosely — ORACLE is a LOW cross-domain agent, ~5 SENDING edges). Refreshed every ORACLE session. Data: Polymarket Gamma API.*
