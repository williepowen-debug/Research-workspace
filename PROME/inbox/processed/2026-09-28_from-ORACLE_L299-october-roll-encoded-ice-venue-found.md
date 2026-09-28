# ORACLE → PROME · 2026-09-28 09:5x ET · DOCKET L299 settled: the October roll is encoded, and the October leg turned out to sit on a different venue

Spawn `prome-7f`, Tier-1 follow-up (WQ-260). ORACLE commit `279b7aec1`. All reads are ORACLE's own, taken at the venue or the contract on 2026-09-28, 13:45–13:50Z.

## L299 — the three items

| # | Item | Result | Evidence |
|---|---|---|---|
| ① | Re-pin the October $110 market | **PINNED.** `will-wti-reach-110-in-october-2026`, Polymarket id **4936102**, created 2026-09-25T04:02Z, ends 2026-11-01T03:59Z. Mid **25.5%** (bid 25 / ask 26, last 31). Vol **$224**, liq **$3.3K** ⇒ ⚠️ **THIN** (under the $5K bar): no mark on one print. The whole October event is $19.9K. The "v5 dies at 10/01" branch is moot. | Gamma `markets?slug=` 13:45Z; `polymarket.py search "WTI October 2026"` |
| ② | Month-roll rule, named first | **Stays v5.** The roll opens a new REGIME **segment**, `v5-oct26-icewti110`, and is never differenced against September. The Sept exit (1.4%) vs the Oct entry (25.5%) is days-to-touch, not a repricing. **Not my call: Will's record answers it.** Record row 260 reads verbatim: *"L299's 9/28 October-roll + Active-Month disclosure runs on v5"* (VERIFIED at `PROME/proposals/2026-09-24_wq-batch-282-254-261-260-276-RULED.md` L12). Standing rule, now written in the tool: a month roll opens a segment, and a change of meaning opens a version, which is Will's. | tool L125–L128, `watchlist.tsv` v5-Oct banner |
| ③ | Active-Month switch, checked at the contract | **Nov26 → Dec26 at the open of the session dated Thu 10/15, i.e. 8:00 PM ET on Wed 2026-10-14.** ICE Nov26 LTD is **Mon 2026-10-19** and Dec26 LTD is 11/19, read from the ice.com expiry table (VERIFIED). The market's own rule makes the next contract Active from the third-to-last session, and no US holiday falls 10/13–10/19. **The DOCKET's "~10/16" was INFERRED from the CME rule (CLX26 LTD 10/20): wrong venue, and one session late.** At today's curve the switch is a **~$3.95 downward level step** (CLX26 $94.19 / CLZ26 $90.24, fetch.py 9/28). That step lowers the odds of reaching $110 without any change in risk. | `ice.com/products/213/WTI-Crude-Futures/expiry` (HTTP 200, 9/28) |

**Rows:** the last Sept-segment row is **+75.1pp** @ 13:48Z (supply 1.4%). The first Oct-segment row is **+51.0pp** @ 13:49Z (76.5 − 25.5), and the tool flags it THIN.

## ⛔ New finding: the October market resolves on a different venue

I read the resolution texts at Gamma on 9/28. **September resolves on CME CL** (Pyth "WTI", 6 PM ET sessions, CME's last-trading-day rule). **October resolves on ICE Futures Europe WTI** (Pyth **"CLL"**, 8 PM ET sessions, ICE's rule, which is one US business day earlier). ICE WTI cash-settles against NYMEX, so the price question is the same. The session window and the roll date are not. The September Active-Month date (the 9/18 session) **stands**, because September was CME.

Will ruled WQ-260 on a CME-based premise ("same disclosures as v4"). A resolution-venue change is arguably a change of meaning, and under my own rule that is Will's call. **ORACLE rec: stays v5, disclosed.** Either answer only relabels a string: the segment string already keeps the rows non-comparable, and no arithmetic changes.

## v5 threshold PROPOSAL (not encoded; Will's word needed)

| Band | Proposed | Basis |
|---|---|---|
| Arming | Only after the Oct $110 leg clears **$5K liq on 3 consecutive reads** | Today it is $3.3K. ORACLE's thin rule |
| Alert | Oct $110 **≥ 40%**, sustained ≥ 3 reads, with no read spanning 10/14 20:00 ET | Entry 25.5% with spot $94.19: $110 is +16.8% away, about a 45% implied vol touch. 40% means spot near ~$100, or a vol regime shift |
| Critical | **≥ 60%** sustained ≥ 3 reads, **or** the leg resolves YES | Mirrors the v3/v4 sustained-read shape (v3 Alert: >45% sustained ≥3) |

It is recorded in the VX-ORC-04 Alert cell as UNSET plus this proposal. I encode it only on Will's word.

## Movers at 13:48Z (charter rule: >10pp in 48h goes to PROME for triage; each is one read and none is re-graded)

- **US–Iran next senior meeting:** by **10/31 75.5** (9/27: 50.0; $52.5K vol / $27.1K liq). By 9/30 66.5 (38.0; ⚠️ $4.2K liq). By 12/31 84.5 (77.5). Under the charter this >20pp shift goes to HAWK/BRENT. **Not routed by me**; your triage. HAWK owns why it moved.
- **Fed Oct hike:** Kalshi `KXFED-26OCT >4.00` **69.0** (63.0; OI 33.6K) vs PM **65.5** (Δ7d +16.0; $391.7K liq). The VX-ORC-08 Alert (>66%) is crossed **on Kalshi only**: the venues split on one read. PM Dec-specific hike **79.0** (Δ1d +10.5).
- Thin, not marked: BOJ Oct top leg PM −11.5 ($1.3K liq) / Kalshi −9 (→ SAM) · FL Cat-4 −14.5 ($1.0K liq).

## Inbox drain, 4/4 (logged in `board_log.tsv`, moved to `processed/`)

- **CATO NB5 receipt:** relabelled as asked. §3 of `analysis/2026-09-27_bank-failure-markets.md` now reads "Depth has been falling all year" → "Lifetime volume per contract instance has fallen across 2026", with an explicit not-depth note, and "deepest" → "largest lifetime volume". The same relabel is in KB-ORC-101. No re-pull. (a) The regulator's release time stays unverified, and no lead or lag is claimed.
- SIG-W-20260927-004 / -005 / -006 (Nano Banc): noted. ORACLE never carried the WAL-link, $108M or ~$260M figures (grep), so COR-20260927-05 and -06 are receipted **NO-OP**. Corrections check: rc=0.

## COMPLETION — ORACLE — 2026-09-28
STATUS: ✅ DONE
CHANGED: ORACLE watchlist.tsv, tools/disruption_supply_spread.py, workbook/{DISRUPTION_SUPPLY_SPREAD,VX,KB,ODDS_LOG,KALSHI_ODDS_LOG}.tsv, STATUS, SCRATCH, NEXUS_BRIEF, MAINTENANCE, board_log.tsv, analysis/2026-09-27_bank-failure-markets.md, registry/corrections_receipts.tsv, 4 inbox→processed; this memo
RESULT: L299 settled. ① Oct $110 pinned (id 4936102, 25.5%, liq $3.3K ⚠️ THIN). ② Stays v5 per WQ-260 record row 260; new segment v5-oct26-icewti110, first row +51.0pp (never vs Sept +75.1). ③ Active Month Nov→Dec at 8:00 PM ET Wed 10/14 (ICE Nov26 LTD 10/19, VERIFIED). The docket's ~10/16 came from the CME rule. FOUND: October resolves on ICE WTI (CLL); September was CME. Inbox 4/4 drained; CATO NB5 relabel done.
GAPS: STATUS was a partial update (oil and movers re-read; other alerts carry their 9/27 basis, labelled). history/movers/coverage not run (coverage due ~10/01). Pre-existing mixed CRLF/LF in DISRUPTION_SUPPLY_SPREAD.tsv logged, not fixed.
WILL_NEEDS: (a) Does the CME→ICE resolution-venue change keep the October leg as v5? ORACLE rec: yes, disclosed; either answer only relabels a string. (b) v5 thresholds as proposed above (arm after 3 reads ≥$5K liq; Alert ≥40%, Critical ≥60% or YES, each sustained 3 reads). ORACLE rec: approve.
FOLLOW-UP: PROME: correct L299's "~10/16" to 10/14 20:00 ET (ICE) · triage the Iran-meeting +25.5pp (10/31 leg) for HAWK/BRENT · ORACLE: re-read the Oct leg on 3 separate days; Oct→Nov roll ~11/01 under the same segment rule.
