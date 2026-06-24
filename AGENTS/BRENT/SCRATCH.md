# BRENT SCRATCH — Wed Jun 24, 2026 (EIA wk-6/19 data pull — ROUTING BOUNDARY #3 FIRED)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable. Supersedes the Jun-22 SCRATCH.

**Session arc:** Booted Wed Jun 24 (continuation from prior context that hit the summary wall mid-rebase). The EIA WPSR for week ending Jun 19 was pulled, filed, and committed. The pre-registered ROUTING BOUNDARY #3 (Cushing sub-20M) has now FIRED. A rebase conflict was resolved (upstream fe44ae3a vs my f97f55f) and the commit pushed to origin (109fd804). PushNotification sent to Will.

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **Fri Jun 27 AM — Baker Hughes rig count (BH Jun 27)** — watch oil rig direction (trough 407, threshold 457 = +50 from trough). BRT-26 slow-response frame still intact.
2. 🔴 **Fri Jun 27 (or Sat Jun 28) — CFTC COT (Jun 23 data)** — this is the SECOND post-MOU forced-liquidation read (Jun 16 data was first, last week); critical for Trigger #3 re-arm and XLE stub decision. ~3:30pm ET Fri.
3. 🟠 **Trigger #2 datapoint #3 CONFIRM** — the Jun 19 gasoline product supplied 4-wk YoY was NOT indexed in EIA tables at run time (WGFUPUS2 series showed only through Jun 12). Pull `https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=wgfupus2&f=W` when indexed (typically updates 2-4h after 10:30am release). Need a single-week Kbpd value to compute the 4-wk YoY and confirm magnitude vs the −5% threshold.
4. 🟠 **Refinery utilization Jun 19** — WPULEUS3 was also not indexed at run time. Pull from EIA WPSR dashboard or series once available.
5. 🟡 **NEXUS_BRIEF outbox routing** — Cushing breach is now live. Confirm NEXUS picks up the SENDING row at next boot (should auto-route to LIQUID/HENRY/RED via NEXUS_BRIEF updates this session).

## CHANGES SINCE LAST SESSION (Jun 22 → Jun 24)
- **EIA Jun 24 (wk-6/19) CONFIRMED:**
  - **🚨 Cushing 18.957M (−1.077M WoW) — BELOW 20M OPERATIONAL FLOOR. ROUTING BOUNDARY #3 ACTIVE.**
  - Commercial crude 412.134M (−6.088M, beat est −4.5M by 1.6M) — ~7% below 5yr avg
  - SPR 331.191M (−9.109M) — 40+ yr low (lowest since ~1983); no throttle; 6th+ consecutive cycle-max draw
  - Total crude incl SPR −15.197M WoW (2nd consecutive cycle-max week)
  - Gasoline stocks 216.299M (+2.099M), ~6% below 5yr avg
  - Distillate 106.116M (+3.016M), ~10% below 5yr avg
  - Production 13,819 Kbpd (+119K est); imports 5,570 Kbpd (~−150K est)
  - Retail gas ~$4.048/gal (Jun 22 AAA/FRED) — near $4 behavioral threshold; was $3.99 Jun 18
- **Trigger #2 datapoint #3 PENDING** — WGFUPUS2 not indexed for wk-6/19 at run time; est ~−1.5 to −2.0% [EST] based on trend; −5% threshold still far (0/3 on 3-wk clock)
- **Refinery util Jun 19 PENDING** — Jun 12 CONF 96.7%
- **Git:** session committed + pushed (109fd804); prior rebase conflict resolved

## WHAT I DID THIS SESSION
- **Pulled EIA WPSR wk-6/19** via EIA table1.csv + table4.csv [CONF]; cross-validated via TradingEconomics, Investing.com, OilPrice.com, AAA/FRED
- **Created `data/eia_2026-06-24.md`** (158 lines; full data file)
- **Updated `demand_destruction/TRACKER.md`**: alert block (Routing Boundary #3 + crude draw alert); header (Jun 24 / War Day ~117); Cushing tier-1 row (18.957M BREACHED); Trigger #2 row (datapoint #3 PENDING); new weekly log row (Jun 19 wk end)
- **Resolved rebase conflict** (`git checkout --theirs` flow; prior session used `--ours` which took the upstream version; re-applied edits manually before `git rebase --continue`)
- **Pushed** to origin master (109fd804)
- **PushNotification sent** to Will: Routing Boundary #3 active

## NEXT SESSION (dated, future-verifiable)
1. **Fri Jun 27** — Baker Hughes rig count + CFTC COT (Jun 23 data, first TRUE post-MOU liq read); XLE stub decision gate
2. **Fri Jun 27 (or check asap)** — Pull WGFUPUS2 and WPULEUS3 for Jun 19 week to complete the PENDING EIA cells in TRACKER.md (Trigger #2 datapoint #3 + util Jun 19)
3. **Wed Jul 1** — EIA WPSR (wk-6/26); watch Cushing trajectory at sub-20M pace (~18M next week if −1M/wk continues)
4. **~early Jul (Jul 3 modeled)** — SPR re-auth decision; 172M tranche authorization exhausted; DOE re-auth required to continue draws
5. **Fri Jul 8** — EIA STEO (July); first post-deal price-path revision

## OPEN THREADS / WATCHES
- 🔴 **Routing Boundary #3 NOW ACTIVE** — LIQUID (WTI basis/dislocation), HENRY (physical price distortion = inflation input), RED (systemic signal) alerted via NEXUS_BRIEF
- 🔴 **Trigger #2 datapoint #3 PENDING** — gasoline 4-wk YoY for wk-6/19 not yet indexed; confirm when WGFUPUS2 updates
- 🔴 **Physical/price divergence at cycle maximum** — Cushing below 20M operational floor while Brent pricing PATH A normalization at $78–82; snap-back potential is highest of the cycle if Lebanon re-escalates into record-short positioning
- 🟠 **Cushing trajectory** — at ~1M/wk draw pace, falls to ~18M next week; WTI delivery dislocation risk escalating
- 🟠 **SPR re-auth (early July)** — 172M authorization fully withdrawn ~early Jul; DOE needs new authorization to continue ~9M/wk pace; runway to §6241 252.4M floor = ~8-9 weeks if no throttle
- 🟠 **CFTC COT Jun 16 (first post-MOU liq read)** — Jun 26 CFTC release; critical for Trigger #3 re-arm; record-short ICE Brent MM net
- 🟡 **Refinery util Jun 19 PENDING** — need WPULEUS3 Jun 19 value; Jun 12 was 96.7% (util >95% since Jun 5 keeps BRT-12 crack-squeeze channel active)
- 🟡 **LIQUID HY-Energy-OAS pull** — owed, DEFERRED per Will Jun 20

## POSITION DECISIONS PENDING
- **XLE $65C Sep 30** — HOLD on a short leash through Jun 26/27 (Will Jun 20 hold; v4.2 hold-not-lapse). Routing Boundary #3 firing = physical squeeze deepening = kinetic-tail stub more justified NOT less. Reassess after Jun 27 COT (first post-MOU liq print) + early-July SPR re-auth.
- **No new flat-price longs** — de-escalation confirmed + contango + crowded short = wrong regime to add length either way.

## MAIL STATE (one line per signal)
- **Inbox/WALTER:** no new signals this session; lane CLEAR from Jun-22 SCRATCH
- **Outbox:** no new acute outbox; Routing Boundary #3 routing handled via NEXUS_BRIEF SENDING (not outbox, per outbox-restraint guidance)

## WORKBOOK HEALTH
- TRACKER.md updated (Jun 24 EIA data + Boundary #3 alert); data/eia_2026-06-24.md created
- NEXUS_BRIEF updated (this session); SCRATCH written (this session)
- THESIS unchanged (no new phase transition; conviction unchanged from v4.2)
- PREDICTIONS: no resolutions this session; BRT-28 (Cushing <20M) was the pre-registered Boundary #3 — **FIRED** (validate against PREDICTIONS.tsv and resolve if open)
- **GIT:** session pushed to origin/master (109fd804). Clean.
