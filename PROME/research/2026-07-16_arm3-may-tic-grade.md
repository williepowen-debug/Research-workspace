# ARM-#3 GRADE — May 2026 TIC (GATE-TERRY-ARM3, TRY-FIRE-004)

**Graded:** 2026-07-16 ~5:00 PM ET by PROME (mechanical, vs frozen templates: TERRY `setups/ARM3-TIC-grading-template_2026-07-16.md` + BOND `setups/2026-07-16_ARM3-TIC-grading-template.md`; card ZONE 1 #3 net-TRANSACTIONS wording = canonical).
**⚠️ Docket vintage error found at grade time:** the May TIC release was **Mon 7/14 4 PM ET** (press notice embargo line, PROME-pulled), not the docketed 7/16 — we graded 2 days late without knowing it. DOCKET fixed; add release-date verification to the docket hygiene pass.

## VERDICT: **ARM-#3 FIRES** (mechanical sign test, as pre-registered) — deepen-only, no trade consequence.

### CUT B — net TRANSACTIONS, LT Treasuries (the grade) [PRIMARY: Treasury/Fed CSLT v2.0, releaseID 3, series `for_lt_treas_net_41408/_42609`; $M]
| Country | Apr net txns | May net txns | May sign | Net seller? |
|---|---:|---:|---|---|
| China (Mainland) | +5,521 | **−129** | − | **Y** (trivially) |
| Japan | +14,705 | **−2,838** | − | **Y** |

Both < 0 ⇒ per the decision tree: **arm-#3 ARMS.** Card TRY-FIRE-004 was already ARMED via arm-#2 (5-of-5, 7/13); this is **confirmation depth, not a new trade**. Will's 7/16 NO-ADD stands; the fill decision does NOT re-open. No action without Will [Approve].

**Honest caveat (logged, does not alter the mechanical grade):** China's −$0.129B is economically FLAT (its Mar-2026 swing was −$30.0B; Apr was +$5.5B). The sign test fires as registered, but the China leg adds ~zero confirmation weight. Japan's −$2.8B is modest and **May pre-dates the July MOF-buying flip** (SAM memo §d: trend-consistency only). Net: a *weak* fire — deepen-confirmation is thin; flag to TERRY to log it as such, not as a strong second arm.

### CUT A — holdings (context ONLY, valuation-contaminated) [PRIMARY: SLT Table 5, 7/14 release; $B]
| Country | Apr | May | Δ | decomposition |
|---|---:|---:|---:|---|
| China | 651.1 | **659.3** | **+8.2** | LT txns −0.1 + **bills +6.1** [CSLT `for_st_treas_net_41408`] + small val. ⇒ **bill-shift, not duration buying** — rotation-consistent |
| Japan | 1,209.9 | **1,143.1** | **−66.8** | LT txns −2.8 + **bills −59.8** [CSLT `for_st_treas_net_42609`] ⇒ **~94% REAL selling, NOT valuation** — Japan dumped ~$60B of bills in May |

**Reconciliation line:** CUT A mixed (Japan down big-and-real / China UP), CUT B both-sellers ⇒ ARM-#3 = FIRES. The A/B divergence is bills, not valuation — the exact trap class F10 was patched for, in a new costume.

### Context the fire sits inside (aggregate)
May aggregate foreign net purchases of **LT Treasuries = +$53.6B** [press notice table line 5]; all LT securities +$262.8B, net TIC inflow +$132.2B. China+Japan slightly negative while the rest of the world bought heavily ⇒ **no demand hole in May; the absorbers keep absorbing** (feeds LIQUID's demand-hole pre-reg: MASKED continues).

### Downstream reads routed
- **ZHAO (ZHA-04):** NO sub-$650B print — China 659.3 **UP** from the 18-yr low 651.1; the docket's TE nowcast (659.3) hit EXACTLY. Exit **stalling at the line**; bill-shift supports the Treasury→short/Agency rotation reframe.
- **SAM/BOND:** the May datum is Japan **bills −$59.8B** (pre-event vintage; the July MOF weekly flip to +¥1,090B buying is the LIVE arbiter and post-dates this). Trend-consistency: May Japan was a real seller across the curve-front; the DURABLE flip is therefore a genuine reversal, not continuation.
- **TERRY:** discriminator-log entry to append at next boot (this memo = the routed record; PROME does not edit the card).

### Data-plumbing finding (fleet-reusable, saved to auto-memory)
Country-level TIC net **transactions** no longer live in the S-form files (`snetus`/`s1_globl` frozen at Jan-2023). The live product is **CSLT** (`ticdata.treasury.gov/.../cslt.zip`, 121MB JSON, TIC SLT + Fed staff estimates, valuation-adjusted — exactly the F10 measure): series `for_{lt,st}_treas_net_<countrycode>` (China 41408, Japan 42609), newest-first arrays. Also: `Publish/mfh.txt` serves a DEAD Jan-2023 vintage — current holdings = `Documents/slt_table5.txt`. Press-notice PDFs are named by RELEASE month, not data month.
