# SAM — Open Threads (Japan), 2026-07-09 eve

*Will-directed sweep. Grounded in live files/tape only — no trade recs. Dated gates (TIC 7/16, 40Y 7/22, MOF ~7/31) excluded per instruction; they're tracked in `docket/CALENDAR.md`.*

## 1. Open Questions (unresolved, matter now)

| # | Question | Why it matters | Status |
|---|----------|-----------------|--------|
| 1 | Oil/MOU tail EV-weight (8%, THESIS.md CONVICTION DECOMPOSITION) | Pre-dates the 7/7-7/8 truce collapse — stale number sitting in a live table | Flagged pending-recompute this session, not yet done (deliberate — no fresh JGB/CFTC datapoint to attribute >5pp) |
| 2 | MOF weekly ITS flows stale thru 6/21-6/27 | **The fastest Japan-specific discriminator for the BND-11 77.74%-bid question** — a week-of-7/7 spike in Japan foreign-securities purchases would be the first real tell, ahead of TIC 7/16 | ✅ Pulled 7/9 ~9:20pm ET: latest available = wk ending 7/4 (pre-event baseline, 2 straight weeks net SELLING). **Actual 7/5-7/11 discriminator week NOT yet posted — lands ~7/16 JST w/ TIC.** See STATUS discriminators bullet. |
| 3 | FXY modal band ($57.5-59.5 / USDJPY 154-160) | Tape has run 160-162.6 for 2+ weeks ABOVE the band — STRATEGY.md flags it but the re-derivation itself (queued post Jul-6 CFTC + Jul-7 30Y, both now landed) hasn't been executed | Open since 7/2 METSUKE escalation |
| 4 | CFTC Jun-30 print never confirmed pulled | `deafut.txt` still showed Jun-23 as of 7/8; blocks SAM-29/30 tripwire reads | Carried open 3+ sessions |
| 5 | CH-010 above-4.5% mechanism | Does forced-selling exist at all above 4.5%, or does the demand floor just deepen with yield? Paired with the GPIF gap (#6 below) | Open since 7/2, unresolved |

## 2. Coverage Gaps (no instrument)

- **No direct Japan-attribution on UST auction bidders.** TreasuryDirect's "indirect" bucket isn't broken out by country — SAM/BOND cannot independently confirm or refute the Japan-duration-extension hypothesis without TIC (monthly-lagged). This is the structural reason the BND-11 question needed TWO proxies (MOF weekly + TIC) rather than one clean read.
- ~~**GPIF flows — no tracking script exists.**~~ ✅ BUILT 7/9 (`scripts/gpif_flows.py`, wired into boot.py). Tracks quarterly-update + annual-summary PDFs (asset size, return, 4-way allocation %, FY rebalancing flow by asset class); portfolio-holdings Excel (security-level detail) logged but not parsed — remaining gap if CH-010 needs super-long-specific granularity.
- **Clean USDJPY implied vol — license-gated.** CME CVOL (JPVL) is paywalled; SAM runs on the FXY options proxy, known to mislead (KB-183 — 16% proxy IV vs ~sub-10% true, confirmed 6/29). No fix pending.
- **MOF ambush-regime — no fast-confirm instrument built.** The playbook (S1-A) names "BOJ current-account projections (~2bd)" as the semi-confirm path for a suspected strike, but nothing pulls or monitors that series on a cadence; it's a citation, not a running check.

## 3. Threads to Pull (unchased leads, ranked)

| Thread | Why it matters | What pulling it takes | Urgency |
|---|---|---|---|
| **MOF weekly ITS — systematic week-of-7/7 watch** | Direct answer to "if the 77.74% bid reverses, what Japanese-side datum shows it first?" A spike in Japan's foreign-securities purchase line this week (or the next) is the earliest tell, well ahead of TIC | ✅ Pulled 7/9 — 7/5-7/11 print not yet posted (lands ~7/16 w/ TIC). Re-pull at next boot/session | **Next boot** |
| **GPIF quarterly flow disclosure** | GPIF FY2025 annual summary + Q1/2/3 update PDFs are the only other primary-source read on Japanese pension duration stance | ✅ BUILT 7/9 (`gpif_flows.py`) — FY2025 captured, next release is 1Q FY2026 (Apr-Jun 2026), expected ~Aug 1 2026 | Auto-checked every boot going forward |
| **"Bridging bonds" enactment status** (SIG-627-015, Japan ruling-party off-balance-sheet fiscal framework) | Real JGB-supply-pressure thread, draft-stage as of 5/27, never re-checked since — a genuine fiscal-credibility tell if it advances | One targeted search: has the draft moved past committee / any Diet vote scheduled | Background |
| **Ambush-regime next observable** | MOF deliberately gives no jawboning lead-in now (S1-A) — rate-check absence is no longer informative. What IS the next fast tell if not a rate-check? BOJ current-account projections are cited but never actually pulled | Build the pull (or confirm it's not automatable) so a candidate strike can be semi-confirmed same-day instead of only via the ~7/31 MOF monthly | This month |
| **Reverse-knockout FX option trigger map** (SIG-706-009, record weak-yen bankruptcies) | Real-economy carry-convexity transmission is flagged as a mechanism but no one has mapped WHERE the forced-dollar-buying trigger levels cluster relative to 162-170 | Would need a dealer/options-flow source SAM doesn't currently have — flag as a build candidate, not yet scoped | Background |

---
*3 open questions load-bearing this week (MOF weekly read, FXY re-derivation, CFTC pull). Full context → STATUS 7/9 EVE note, MEMORY NEXT SESSION, THESIS.md CONVICTION DECOMPOSITION.*
