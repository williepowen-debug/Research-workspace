# SAM — Open Threads (Japan), 2026-07-09 eve

*Will-directed sweep. Grounded in live files/tape only — no trade recs. Dated gates (TIC 7/16, 40Y 7/22, MOF ~7/31) excluded per instruction; they're tracked in `docket/CALENDAR.md`.*

## 1. Open Questions (unresolved, matter now)

| # | Question | Why it matters | Status |
|---|----------|-----------------|--------|
| 1 | Oil/MOU tail EV-weight (8%, THESIS.md CONVICTION DECOMPOSITION) | Pre-dates the 7/7-7/8 truce collapse — stale number sitting in a live table | Flagged pending-recompute this session, not yet done (deliberate — no fresh JGB/CFTC datapoint to attribute >5pp) |
| 2 | MOF weekly ITS flows stale thru 6/21-6/27 | **The fastest Japan-specific discriminator for the BND-11 77.74%-bid question** — a week-of-7/7 spike in Japan foreign-securities purchases would be the first real tell, ahead of TIC 7/16 | First read owed at next boot (`workbook/MOF_FLOWS.tsv`) |
| 3 | FXY modal band ($57.5-59.5 / USDJPY 154-160) | Tape has run 160-162.6 for 2+ weeks ABOVE the band — STRATEGY.md flags it but the re-derivation itself (queued post Jul-6 CFTC + Jul-7 30Y, both now landed) hasn't been executed | Open since 7/2 METSUKE escalation |
| 4 | CFTC Jun-30 print never confirmed pulled | `deafut.txt` still showed Jun-23 as of 7/8; blocks SAM-29/30 tripwire reads | Carried open 3+ sessions |
| 5 | CH-010 above-4.5% mechanism | Does forced-selling exist at all above 4.5%, or does the demand floor just deepen with yield? Paired with the GPIF gap (#6 below) | Open since 7/2, unresolved |

## 2. Coverage Gaps (no instrument)

- **No direct Japan-attribution on UST auction bidders.** TreasuryDirect's "indirect" bucket isn't broken out by country — SAM/BOND cannot independently confirm or refute the Japan-duration-extension hypothesis without TIC (monthly-lagged). This is the structural reason the BND-11 question needed TWO proxies (MOF weekly + TIC) rather than one clean read.
- **GPIF flows — no tracking script exists.** Sitting in the Tier-2/3 research backlog since Will's Jun-15 brainstorm; still zero cadence on GPIF's super-long stance, which is the single named open demand-leg gap in both SAM-32's post-mortem and the CH-010 thread.
- **Clean USDJPY implied vol — license-gated.** CME CVOL (JPVL) is paywalled; SAM runs on the FXY options proxy, known to mislead (KB-183 — 16% proxy IV vs ~sub-10% true, confirmed 6/29). No fix pending.
- **MOF ambush-regime — no fast-confirm instrument built.** The playbook (S1-A) names "BOJ current-account projections (~2bd)" as the semi-confirm path for a suspected strike, but nothing pulls or monitors that series on a cadence; it's a citation, not a running check.

## 3. Threads to Pull (unchased leads, ranked)

| Thread | Why it matters | What pulling it takes | Urgency |
|---|---|---|---|
| **MOF weekly ITS — systematic week-of-7/7 watch** | Direct answer to "if the 77.74% bid reverses, what Japanese-side datum shows it first?" A spike in Japan's foreign-securities purchase line this week (or the next) is the earliest tell, well ahead of TIC | boot.py already auto-pulls `MOF_FLOWS.tsv` — just needs the next boot's read flagged as load-bearing, not routine | **This week** |
| **GPIF quarterly flow disclosure** | GPIF Q1 FY2026 (Apr-Jun) portfolio release is the only other primary-source read on Japanese pension duration stance; nobody has checked its publish date or built intake | Confirm GPIF release calendar (typically early Aug for Q1); if it lands, primary-source read for the super-long allocation delta | This month |
| **"Bridging bonds" enactment status** (SIG-627-015, Japan ruling-party off-balance-sheet fiscal framework) | Real JGB-supply-pressure thread, draft-stage as of 5/27, never re-checked since — a genuine fiscal-credibility tell if it advances | One targeted search: has the draft moved past committee / any Diet vote scheduled | Background |
| **Ambush-regime next observable** | MOF deliberately gives no jawboning lead-in now (S1-A) — rate-check absence is no longer informative. What IS the next fast tell if not a rate-check? BOJ current-account projections are cited but never actually pulled | Build the pull (or confirm it's not automatable) so a candidate strike can be semi-confirmed same-day instead of only via the ~7/31 MOF monthly | This month |
| **Reverse-knockout FX option trigger map** (SIG-706-009, record weak-yen bankruptcies) | Real-economy carry-convexity transmission is flagged as a mechanism but no one has mapped WHERE the forced-dollar-buying trigger levels cluster relative to 162-170 | Would need a dealer/options-flow source SAM doesn't currently have — flag as a build candidate, not yet scoped | Background |

---
*3 open questions load-bearing this week (MOF weekly read, FXY re-derivation, CFTC pull). Full context → STATUS 7/9 EVE note, MEMORY NEXT SESSION, THESIS.md CONVICTION DECOMPOSITION.*
