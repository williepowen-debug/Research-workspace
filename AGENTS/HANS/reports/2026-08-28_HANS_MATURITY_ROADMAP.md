# HANS — maturity roadmap
**Written 2026-08-28** on Will's direction: *"Eventually I want this desk to catch up to more mature agents and be able to provide helpful knowledge to the group as a whole."*
**Baseline:** the measured comparison in `2026-08-28_HANS_vs_SAM_ZHAO_regional_desk_comparison.md`. Phase 0 was executed the same day.

---

## THE TWO GOALS ARE DIFFERENT AND THE SECOND IS THE HARDER ONE

**"Catch up" is an infrastructure problem — largely solved today.** **"Provide helpful knowledge to the group" is an OUTPUT problem, and it is not solved by having more ledgers.** A desk can be fully instrumented and still supply nothing anyone uses. **The measurable test is not what HANS holds; it is what other desks CONSUME.** Today's evidence: 13 packets delivered, **1 confirmed consumed** (HENRY, in `processed/`). That ratio is the real scoreboard.

---

## WHAT HANS UNIQUELY HOLDS — the honest inventory

**These five are the reason the desk exists. Nobody else in the fleet carries them:**
| # | Holding | Who needs it | State |
|---|---|---|---|
| 1 | **German Mfg PMI → US ISM ~2-month lead** | HENRY (thesis-critical) | ✅ live · ⚠️ the capex-vs-demand-regime question is **untested** |
| 2 | **ECB / BoE / Fed policy divergence** | BOND, LIQUID, MARCO | ✅ live — 3 hiking-bias CBs off one energy shock |
| 3 | **EU energy → European macro cost transmission** (BRENT owns oil price, HAWK the theatre) | HENRY, BRENT, LIQUID | ✅ live, 2 fires open |
| 4 | **Euro-area bank ↔ private-credit seam** | LIQUID, REGINALD, BROCK | 🆕 **Will-ruled mine 8/28** · 🔴 **not yet read at primary** |
| 5 | **UK gilts / BoE / LDI** | BOND, LIQUID | 🆕 taken 8/18–8/28 · 🔴 **no daily feed** |

⚠️ **#1 is the crown jewel and it has an untested assumption inside it.** A capex/fiscal-driven PMI is a weaker ISM lead than a demand-driven one, and **this desk has never tested whether the lead holds across those regimes.** Fixing that is worth more to the fleet than any new ledger.

---

## PHASE 0 — INFRASTRUCTURE ✅ DONE 2026-08-28
`boot.py` (7 sections, SPAWN step 0) · `fetch_eu.py` (ECB Data Portal, keyless: daily AAA 10Y + per-country spreads) · `KB.tsv` (34 facts, 33 with `Stale_By`, enforced at boot) · **0 fossil vectors** (was 28) · registry 14 rows + fire ledger · `KILL_TREE` 13 entries · 1 pre-registration.

## PHASE 1 — CLOSE THE FEED AND CREDIBILITY GAPS *(next 2–3 sessions)*
| Item | Blocker | Note |
|---|---|---|
| **Read ECB FSR May-2026 at primary** | none — **mine to do** | 🔴 **First obligation of the newly-ruled lane.** Until done, LIQUID's no-onward-routing constraint binds. **Owning a lane does not retroactively verify what was surfaced in it.** |
| **AGSI+ storage feed** | 🔑 **free API key** | 5-minute signup at `agsi.gie.eu/account` → `AGSI_API_KEY` in `FORGE/tools/market-data/.env`. Then `HANS-T-08` is automated |
| **UK gilt daily** | no free source found | FRED is monthly + ~2mo lagged. **Stays manual and named**; revisit only if the UK leg proves load-bearing |
| **Unfreeze `VX-HANS-6.02`** (UK pension funding) | none | PPF 7800 Index is **public and monthly** — a Stage-1 metric for `FLOW-HANS-5` sitting frozen for no good reason |

## PHASE 2 — BECOME CONSUMED, NOT JUST CORRECT *(the actual goal)*
1. **Test the PMI→ISM lead across capex- vs demand-driven regimes.** The single highest-value analytical piece this desk could produce for the fleet. Result goes to HENRY either way — *including if it shows the lead is weaker than advertised.*
2. **Publish a standing `NEXUS_BRIEF.md`** — SAM and ZHAO both have one; HANS does not. It is how a desk's state becomes readable **without spawning it.**
3. **Grade `HNS-05` on both axes** (binary *and* §3b tactical-vs-regime). Pre-committed; reporting only the binary is the named failure.
4. **Track consumption, not dispatch.** Standing check: `find AGENTS/<RECIPIENT> -iname "*HANS*"` → is it in `processed/`? **A packet in `inbox/` is not knowledge transferred.**

## PHASE 3 — MATURITY MARKERS *(dated, falsifiable — not aspirations)*
| Marker | Target | Why this one |
|---|---|---|
| Predictions **resolved and graded** | **≥6 by 2026-12-31** | Book is 4 graded / 5 open. First is ECB **9/10** |
| **Turn-calls** in the book | **≥2 of every 5** | Direct answer to the 8/28 finding that hits were all continuations |
| Packets **confirmed consumed** | **≥5 in `processed/`** | The output test, not the dispatch test |
| Boot run **before** each session's work | **100%** | The 6.5-month BoE defect is impossible if this holds |
| KB facts past `Stale_By` at any boot | **0** | Expiry enforced, not decorative |
| Fossil vectors | **0, sustained** | Regression guard on today's cleanup |

---

## WHAT WOULD MAKE THIS DESK NOT WORTH MATURING — stated so it can be tested
**`EUROPE_MACRO` has carried ONE routed signal since the code shipped 8/18.** If, by **2026-11-30**, the routing table still shows ~1 inbound signal a month **and** fewer than 3 packets have been consumed downstream, **the honest read is that this is an EVENT-DRIVEN desk that should be spawned at catalysts, not a standing one** — and I should say so rather than manufacture tempo. **Manufactured cadence against thin flow is theatre, and it is the failure mode a desk in "catch-up" mode is most likely to commit.**
