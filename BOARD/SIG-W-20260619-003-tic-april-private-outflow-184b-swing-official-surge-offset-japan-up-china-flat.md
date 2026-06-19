---
signal_id: SIG-W-20260619-003
dispatched: 2026-06-19T16:07:00Z
origin: Will Telegram intake (6-image batch, msgs 2401+2402, 2026-06-19 ~15:58 UTC = ~11:58 AM ET)
source: LiveSquawk @LiveSquawk + First Squawk @FirstSquawk (X, 2026-06-18 4:01-4:03 PM ET) relaying the April 2026 US Treasury TIC release
signal_type: threshold-crossed
domain: UST_FOREIGN
cluster: FED_FRAMEWORK
cluster_secondary: ASIA_CHINA
signal_role: cluster_mediating
narrative_channel: n/a (US Treasury official data release — outside the Iran-cluster narrative-channel enum)
precedence: PRIORITY
to: BOND
info: [LIQUID, HENRY, RED]
confidence: 0.88
verify_verdict: SKIP-VERIFY (official US Treasury TIC release; core figures cross-confirmed by two independent squawk relays — $26.1B total + $103.1B LT match exactly)
verify_method: none (market-fact, official-data, two-source-concordant); BOND to anchor on the TIC primary + Fed custody, not the squawk text
combine_note: two images same data (LiveSquawk + First Squawk) → one signal per same-theme combine rule
---

# TIC April: headline inflows collapse to $26.1B on a ~$184B private-sector swing-to-outflow; official sector + long-term offset

## Substance (SKIP-VERIFY 0.88 — official Treasury data, two-source-concordant)

April 2026 US Treasury TIC release (out 6/18):
- **Total net TIC flows $26.1B**, down from ~$150.7B prior (LiveSquawk) / "$149.3B March" (First Squawk — minor revision/rounding between relays; core figure $26.1B identical).
- **Driver = private-sector swing to a $23.1B OUTFLOW from a $160.6B inflow the prior month** — a **~$184B month-over-month swing** in private capital.
- **Offset by:** net **long-term** TIC inflows **rising to $103.1B** (prev $81.3B) + **official-sector inflows surging to $49.2B** — "foreign demand for long-term US assets remained strong... helping offset weaker private capital."
- **Holders:** **Japan increased UST holdings to $1.210T**; **UK raised to $938B**; **China little changed at $651B.**

## Why it matters — mediates "buyer-base narrowing (bear)" vs "official-sector still bidding (offset)"

**BOND (action) — UST market structure / buyer-base:** this is the April data point on BOND's "expensive, not broken" thesis. **cluster_mediating both ways:** (bear) the headline collapse + the private-sector flip to net outflow is the buyer-base-narrowing / rollover-fragility thread (compounds SIG-W-20260606-002 UST<1yr $8.3T record + SIG-W-20260522-007 TIC March −$139B); (offset) **official-sector inflows surged $49.2B + long-term inflows rose** — the foreign-official bid did NOT vanish in April, and long-term demand strengthened, which is the counter to a clean "foreigners exiting USTs" read. BOND to fold into the June-refunding-cleared / re-armable-at-FOMC frame.

**Notable cross-read — Japan UST UP in April despite yen weakness:** Japan *added* to $1.210T in April even as USD/JPY ran toward the intervention zone. April PRE-DATES the June stress (BOJ hike 6/16 to 1.00%, USD/JPY 161 6/18) — so this is NOT yet intervention-driven UST selling; it's a baseline data point that the intervention-selling channel had not yet activated as of April. Flag for SAM's intervention-watch as a "not-yet-firing" datum (do not over-read April into the June setup).

**LIQUID (info) — funding/flows:** foreign-bid composition feeds term-premium / UST funding conditions.

**HENRY (info) — rates/macro:** UST demand composition is a rates-structure input.

**RED (info) — auto-cc (cluster_mediating):** steelman which dominates — the private-outflow buyer-base-narrowing (bear) or the official-sector+long-term offset (benign). One-month flow data, volatile; needs the May print for trend (2nd-print discipline).

## Source framing (precision caveat)

Official Treasury data relayed by two squawks; the $26.1B total and $103.1B long-term figures match across both relays. The "$150.7B vs $149.3B prior" discrepancy is a minor revision/rounding between the two relays, not a data conflict. BOND should anchor on the TIC primary table.

## AIGs / cross-refs

- BOARD: SIG-W-20260522-007 (TIC March −$139B largest monthly decline since Sep'22), SIG-W-20260606-002 (UST<1yr $8.3T record / foreign-CB share declining), SIG-W-20260522-010 (Turkey UST 89% liquidation), SIG-W-20260606-001 (CB gold net buying)
- BOND STATUS 6/15 (June refunding cleared; "expensive not broken"; re-armable at FOMC)

## Provenance

- Intake: Telegram 6-image batch msgs 2401+2402, 2026-06-19 ~15:58 UTC
- Pipeline: BOARD-grep novel (last TIC signal = March, SIG-W-20260522-007) + two-image same-data combine → SKIP-VERIFY (official Treasury release, two-source-concordant) → dispatch
