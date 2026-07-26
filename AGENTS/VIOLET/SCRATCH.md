# VIOLET SCRATCH — July 25, 2026 (Saturday boot, Will-directed sit-rep)

> **⚡ 7/25 — INTERIM GRADE FILED (KB-VIO-125): crack-candidate ALIVE into FOMC, and the gamma gate is MET.** Settle-path correction: 7/22 was the local LOW (16.64), 7/23 the spike day — **high 20.31 broke the >20 crack leg INTRADAY and was REJECTED to 18.70** (vol sold into the spike, HENRY reconcile); 18.58 [7/24]. Independent channels ESCALATED while the surface faded: **CCC 9.91/disp 8.25 [7/23] fresh episode highs** (confirm-1 ~met), **MOVE 80.08 [7/24, web-verified] new high** (confirm-3 MET), **OVX 3.66/p98.1 deepened**; **COT unwound** (net +10,189→+3,098, pct3y 92.9 — confirm-2 FAILED, the one independent softener); JPY calm but IV/RV 3.04× into BOJ. **HENRY: dealers SHORT-GAMMA 5-of-6 corroborated** (flip ~7,496 pinned, SPX −88pts below, put wall 7,300-7,400 just below — NOT breached; don't say "doubled"). **The registered gate on a non-duplicative pre-FOMC expression is MET; surfaced as a LIVE operator decision** (counterweight: cheap_tail DORMANT 2/4 — mid-range prices, not the floor). No position.

## NEXT SESSION (priority-ordered)

1. **🔴 FOMC Wed 7/29 (2 td) — final KB-VIO-123 grade due by Stale_By 7/30.** Watch the legs on SETTLE basis: VIX>20 settle-and-hold · inversion <1.0 settle · VVIX→120 · fresh credit past CCC 10.0/disp 8.3 · MOVE trajectory. Catalyst stack: FOMC 7/29 + MSFT/META 7/29 + AMZN 7/30 + BOJ 7/30-31 + month-end 7/31, inside buyback blackout, with dealers short gamma. **If Will pursues the surfaced expression decision: defined-risk VIX call spreads only (004 owns the rates-vol leg — no double-count), event-boxed, PROME→TERRY→Will [Approve].**
2. **🔴 Score KB-VIO-127 (Karsan call) by Fri 7/31 close** — HIT = VIX ≥23 touch OR >20 settle-and-hold by 7/31. Base case: miss. Score it either way; it's a registered external-source calibration datum.
3. **🟠 Grade KB-VIO-126 falsification hook after earnings week** — if correlations ROSE and single-stock vol FELL through 7/29-8/1, the benign 3FR base case won; log it against the coiled read honestly.
4. **🟠 COT report-date 7/28, release Fri 7/31 3:30** — did the lev-money unwind continue through FOMC? (7/21 print graded this session: partial unwind, between-branches.)
5. **🟠 VULCAN-09 (VULCAN owns, consume the verdict):** ≥2 of MSFT/META/AMZN falling on capex RAISES 7/29-30 = returns-case repricing confirmed as the live Path-B driver.
6. **🟣 POST-FOMC: refresh BOTH Will-facing Artifacts (SAME URLs)** — edit repo sources in `artifacts/`, republish with `url=`:
   1. Cheat-sheet → `url=https://claude.ai/code/artifact/c2129279-b677-4093-be68-ccdbe0df76b3` (snapshot strip only).
   2. Operating Picture → `url=https://claude.ai/code/artifact/8eb52313-be4e-49a3-8555-e5cc23b44c60` (LIVE STATE band only).
7. **🟡 Carried:** VIX9D (still not separately pulled) · broad equity put/call · HY/BB ladder · VIX6M settle backfill for 7/23-7/24 rows (blank — yfinance ^VIX6M daily lag; fill when the history catches up).

## WHAT I DID THIS SESSION

1. **Booted Saturday** (origin in sync 0/0, MARCO residue untouched; boot.py all-green 18.2s; both staleness guards quiet). Data through 7/24 close.
2. **Consumed the 7/23-eve counterparty answers** (SCRATCH-3 discipline — read before re-asking): **HENRY delivered 4 packets** — gamma chain (UNAVAILABLE → SUPERSEDES → CORRECTION-authoritative: short-gamma 5-of-6, flip ~7,496, −$45B/1%, two retractions honored) + vol-surface reconcile (VIX 20.31 intraday break REJECTED; SKEW faded 2 sessions while VIX rose = tail monetization). **BOND** NEXUS_BRIEF gave MOVE ~80 [7/23] + policy-path mechanism (belly-led real curve, Sept-hike odds 52→80%). **LIQUID silent** (brief stale 7/18) — answered the freshness question from FRED directly: CCC 9.91/disp 8.25 = FRESH episode highs.
3. **Web-verified MOVE 80.08 [7/24 close]** (Yahoo) — WALTER's relayed 76.82 was stale/intraday; BOND's ~80 and the web print reconcile.
4. **Graded COT 7/21 report** (rel 7/24): net +10,189→+3,098, pct3y 99.4→92.9 — confirm-2 FAILED, fade line unmet, between-branches. Logged in KB-VIO-125.
5. **Filed KB-VIO-125** — interim KB-VIO-123 grade (against the LOCKED tree, no re-derivation): confirm 1~met + 3 met (independent), 2 failed; shared legs fade-side but above fade lines; gamma gate MET → live operator decision surfaced.
6. **Processed WALTER inbox (4)**: SIG-004 (COT de-risk, superseded by live print — noted), SIG-006 (Karsan → **KB-VIO-127** scored call, resolves 7/31), SIG-014 (carry crowding — noted, jpy_vol context), SIG-015 (3Fourteen correlations → **KB-VIO-126**, VIX-is-arithmetic mechanism + earnings-week falsification hook). board_log +4, files → processed/.
7. **Consumed + cleared older inbox**: VULCAN 7/22 (Path-B trigger reshaped to returns-case repricing; VULCAN-09 watch), DEWEY 7/20 (CTA cushion direction-yes/level-no; **$464bn do-not-propagate → CALENDAR corrected**), DAEDALUS 7/22 (KOSPI amplifier formalized **CANARY_MAP Tier-2 VIOLET-owned**; write-back packet sent to DAEDALUS inbox under the carve-out — **PAT-032 closed**, both items).
8. **Fixed a real data bug**: backfill.py's holiday guard (^VIX3M-required) was silently dropping REAL trading days whenever Yahoo's ^VIX3M daily history lagged — it ate 7/20-7/24. Relaxed to any-companion (^VIX3M/^VVIX/^SKEW). **VX_DAILY repaired**: 7/20 (18.65), 7/22 (16.64 — the local low the intraday sessions never saw), 7/23 superseded TICK→SETTLE (18.70/20.60/1.1016), 7/24 appended (18.58/20.51/1.1039). MAINTENANCE entry filed.
9. **Write-backs:** STATUS full 7/25 refresh · KB-VIO-125/126/127 · board_log +4 · CANARY_MAP (KOSPI Tier-2 + stamp) · CALENDAR ($464bn fix + semis-IV line) · this SCRATCH · NEXUS_BRIEF · FLOW row (DAEDALUS send) · MAINTENANCE (backfill guard).

## CARRY-FORWARD

- **Regime one-liner:** LOW_VOL 18.58 post-rejection (20.31 intraday break sold back 7/23). Independent stress at new highs (credit fresh 9.91/8.25, MOVE 80.08, OVX p98.1); COT partially unwound; dealers SHORT gamma (confirmed); igniter VIX>23 never touched. Crack-candidate alive, unconfirmed, into the densest catalyst window of the episode (FOMC 7/29 + megacaps + BOJ + month-end). No position; live operator decision pending on a pre-FOMC defined-risk expression.
- **Biggest open loop:** does the short-gamma amplifier finally meet a catalyst it can't absorb? Every prior absorption this cycle happened under LONG-gamma dealers — that mechanism is inverted now. The GEX-absorption base rate may not transfer.
- **Narrative correction to carry:** the 7/23 session's "front-end re-firmed 7/22-7/23" framing was TICK-based and wrong in shape — 7/22 settled at the episode-fade low 16.64; the move was a one-day spike-and-reject on 7/23. Settle basis governs (KB-VIO-092 family).
- **Two mechanical VIX suppressors now named:** KB-VIO-108 (hedge composition) + KB-VIO-126 (record-low correlations). Headline VIX needs decomposition before it does evidentiary work. Candidate thesis-pass item.
- **Data caveats:** weekend values = 7/24 settles; credit T-1 [7/23]; COT 7/21 report; VIX6M blank 7/23-7/24 (Yahoo lag); MOVE next print Monday.
- **Gates:** GATE-VIO-116 re-open FIRED (fold-into-004, live 30× TLT Sep-30 77P). HENRY gamma gate MET. KB-VIO-123 final grade due 7/30.

## OPEN HYPOTHESES (flagged, NOT actionable until backtested)

- **Absorption-regime dependency on dealer gamma sign:** the 0/5 catalyst-absorption streak all occurred under long/positive dealer gamma; 7/29 is the first catalyst of the episode under confirmed short gamma. If it absorbs anyway, the GEX-suppression hypothesis needs a new mechanism; if it doesn't, the base rate was gamma-conditional all along. Either outcome is informative — pre-registered here.
- **VVIX-leads (carried, n=2):** VVIX >100 crossings preceded both VIX pushes (7/17, 7/23); VVIX held 100.73 through Friday's fade while VIX gave back — third instance forming?
- **Divergence-closure direction (carried, n=1 + counter):** 7/21's divergence closed front-end-UP (7/23)… then re-opened Friday. The "closure direction predicts follow-through" hypothesis now has a messy counter-instance; may not survive.
- **COT-leads (carried):** the +10.2K→+3.1K unwind into the 7/21-7/22 fade — sophisticated positioning de-risked BEFORE the 7/23 spike-reject. If VIX breaks >20 settled next week with lev-money already flat, the "extreme-long was the vol-supply cushion" read gains an instance.

---

*Last updated: 2026-07-25 ~15:20 ET (Saturday sit-rep boot + full write-back). Complete: counterparty answers consumed (HENRY short-gamma gate MET, BOND MOVE ~80, LIQUID answered via FRED direct); MOVE 80.08 verified; COT 7/21 graded (partial unwind); KB-VIO-125/126/127 filed; inbox fully cleared (11 files → processed); CANARY_MAP KOSPI Tier-2; backfill guard bug fixed + VX_DAILY repaired; PAT-032 closed. Top next: FOMC 7/29 final grade + operator decision on pre-FOMC expression + Karsan score 7/31. No position. Prior: 2026-07-23 ~12:15 ET.*
