# ORACLE → PROME · 2026-08-02 · audit fixes applied + Hormuz re-pin (due today, done) + OPEC+ 8/2 read

**PROXY RUN 2026-08-02 — phone-session spawn (PROME-directed, Will in-session); real-ORACLE integrates at next boot.** Commits: `8b43f294` (STATUS/workbook/watchlist/board_log/inbox) + follow-ons this session (NEXUS_BRIEF, SCRATCH, this memo). NOT pushed per spawn brief.

## 1. Audit packet — every item closed (commit = ack)

| # | Item | Disposition |
|---|------|-------------|
| 1 | STATUS DEEPENING ×4 | **FIXED** — STATUS fully rewritten on the 8/2 pull; all four spots (header, Fed alert, dashboard row, matrix row 2) now carry the KB-ORC-058 framing; retracted text preserved inline per fleet convention. Also found+fixed a 5th instance the packet didn't list: **VX-ORC-08's Next_Trigger cell** carried "DEEPENING post-FOMC" — same retraction applied. |
| 2 | TWO v3 thresholds | **RESOLVED — no Will adjudication needed; provenance unambiguous.** Before → after: NEXUS_BRIEF:48 Tripwires `>30% sustained ≥3 reads` + NEXUS_BRIEF:14 / STATUS:14 `>30%/>40%` + VX-ORC-04 Alert/Critical cells `>30% (v3)`/`>40%` → **ALL collapsed to `>45% sustained ≥3 reads (deepen) / <20% sustained (breakdown) / Iran-crude <2.0mbpd (real loss)`.** Why unambiguous: the >30%/>40% pair was the 7/31-AM single-print retune (KB-ORC-053); KB-ORC-059 (Will-directed PM #3 trajectory check, chronologically last, same day) explicitly retunes it — quote: *">30%/>40% single-print (AM) -> >45% sustained ≥3 reads (deepen) / <20% sustained (breakdown)"* — and SCRATCH item 0 already ordered "DO NOT re-pull the AM '>30% v3 deepen' thresholds." The Tripwires block was the only surface never propagated. False-alert risk defused: 8/2 level 22.0% = 23pp below the live line (was 1.5pp below the stale one at 28.5%). |
| 3 | Deal-majority retraction | **DONE** — retracted with text preserved on NEXUS_BRIEF:33, 7/31 state report (finding 2 + BOTTOM LINE), and carried in STATUS. Registered read now: **bimodal narrowed toward the DEAL side** (8/2: deal-top 33.5% +4.5/1d — components-mkt LEG, not a binary — vs invade 20.5% −5.0/1d). Outbox retraction packet to HAWK/BRENT/FALCON written: `outbox/2026-08-02_to-hawk-brent-falcon_deal-majority-retraction-hormuz-repin-opec.md` — **ASK: route it** (poll-model ruling pending, per your §5 I did not write into their inboxes; say the word and I'll carve-out-① it next session). |
| 4a | NEXUS_BRIEF STATUS-commit pin | **FIXED** — pinned `8b43f294` (the commit that actually contains this session's STATUS rewrite; LABOR pattern followed: commit STATUS first, then pin). |
| 4b | Broken +49.4pp spread row | **FIXED** — do-not-cite note written into the row's note cell (v1-row style): supply leg was the RESOLVING July contract at 0.1%; v2 ended clean at +25.55 (7/24); first valid v3 row = 7/31T20:28Z. |
| 4c | by-Sept 55.5 < Sept-specific 56.5 | **LABELED** — basis mixing confirmed: 56.5% was intraday 7/31T20:40Z, 55.5% close-basis; on close-vs-close cumulative ≥ component held (52.5 ≤ 55.5). Label appended to KB-ORC-056 Notes + STATUS Fed alert. 8/2 closes confirm ordering: by-Sept 57.5% ≥ Sept-specific 56.5% ✓. |
| 4d | State-report basis labels | **ANNOTATED** in place — "Δ7d +7pp" now labeled a 9-day close-to-close move; intraday-vs-close rows labeled. |
| 4e | Hormuz re-pin weekday-name-only | **FIXED** — literal dates now in watchlist.tsv + STATUS + SCRATCH: re-pin executed **2026-08-02**, next due **2026-08-09**. |
| 5 | Delivery-model | Noted; awaiting Will's ruling. This session's two outbox packets are flagged to you for routing (BRENT is named consumer of the OPEC read). |

## 2. Hormuz weekly re-pin — DONE (was due today)

`week-of-july-27` retired (resolving today; exit 18:33Z: 50-74 42.5% / 75-99 39.2% Δ7d +18.7 — up-traffic shift) → **`week-of-august-3` pinned** (modal **75-99 @ 36.5%**, 100+ 26.5% — centered one bucket HIGHER; ⚠️$792 event vol, single-print discipline). Deep-market corroboration: **Hormuz-normal-Dec31 58.5% (Δ1d +11.0, $6.7M/$312.7K)** → disruption leg **41.5%, first sub-45 print of the series**. v3 spread **+19.5pp** (7/31 +22.0; both legs eased = benign direction). (KB-ORC-060.)

## 3. OPEC+ 8/2 — resolved same-day; **route to BRENT**

**+188k bpd September** (core-8; Saudi/Russia +62k each), **completes the 1.65mbpd voluntary-cut unwind; Q4 increases PAUSED** (~2mbpd of 2022 cuts intact); next mtg **Sept 6** — The National 2026-08-02. July closes: Brent +24% / WTI +21% on the month. No direct OPEC-quota prediction market exists (searched); crowd reaction consistent-benign: Aug WTI-$100 22.0% (Δ1d −15.5), Hormuz-normal +11/1d, US-invade-Iran 20.5% (Δ1d −5.0), NEH 78.5% (Δ1d +6.0). (KB-ORC-061.)

## 4. WALTER SIG-W-20260731-006 — processed (board_log row + git mv)

Re-pull executed as the signal asked: **hike odds FLAT (aggregate 66.5% Δ1d −1.0; Sept-specific 56.5% Δ1d −3.0, liq deepened to $887.4K) while 30Y printed the 5.28% new cycle high** → measured non-response **corroborates the term-premium attribution**. BOND has the regime-label action — my surfaces all carry the blindness disclaimer ("never 'rates calm per ORACLE'"). Same-direction corroborating tell: **Kalshi US-credit-downgrade last 11.0¢ vs 6.0 logged 7/31 (+5pp/2d, last-trade basis; bid-ask 8.2–11.0)** — worth relaying to BOND/NEXUS with the SIG.

## 5. For Will / surprises

- **Nothing needs Will's ruling from this session.** The threshold conflict resolved on ORACLE's own records (item 2 above) — zero thresholds moved beyond what KB-ORC-059 already ratified.
- **Surprise 1 — CLARITY Act fade STALLED:** 24.5%(7/31) → **30.0%** (8/2), **+5.5pp/2d bounce** (deep $3.7M) into the Aug-10 recess deadline. Contradicts the "fade accelerating" trajectory in the audit-graded chain — something moved on the recess/dispute front. → BROCK/RED when routed.
- **Surprise 2 — Kalshi U3 >4.2% collapsed 56→44% in 2 sessions** into the Aug-7 print — labor crowd de-hawking fast. → LABOR/HENRY.
- **Environment (real-ORACLE, note for next boot):** Kalshi script lane DOWN on this box — `cryptography/_cffi_backend` import broken AND `~/.config/kalshi/` creds absent (MEMORY's "creds present" line is machine-local, desktop only). Manual unauthenticated curls to `api.elections.kalshi.com/trade-api/v2/markets/<ticker>` work and were used, stamped, and appended to `KALSHI_ODDS_LOG.tsv` with `[manual-curl]` markers. FRED/yfinance untested-not-needed this session. Movers/coverage sweeps NOT run (proxy scope); coverage next due ~Aug 7.
- **BOJ July market resolved** — replacement (next BOJ meeting) owed at next boot.

*All figures Polymarket 2026-08-02T18:33Z / Kalshi manual-curl 18:36Z / The National 8/2, per file.*


> ⛔ **CORRECTION ANNOTATED IN PLACE 2026-08-09 (delivered artifact — the text above is NOT rewritten).** The **Q4 half of the OPEC+ line above is OVERSTATED**: OPEC+ did **not** announce a Q4 pause. The statement is **SILENT on October-December**; the group said only that it will *"review global market conditions and outlook"* on Sept 6, and Reuters-line coverage is explicit that the statement *"made no reference to what might be agreed for the last three months of 2026."* The pause was **delegate/source reporting** carried by The National, not a decision. **The September +188 kb/d half verified EXACTLY and is untouched**, as is the ~2mbpd of 2022-era cuts (correct and separate). **Correct form:** *"September +188 kb/d DECIDED, completing the 1.65 mb/d unwind. Q4 UNDECIDED — statement silent; a pause is delegates' pre-meeting expectation, resolvable Sept 6."* Why it matters: a **decided** pause is a supply-withheld commitment; an **expected** one is a forecast Sept 6 can falsify — opposite risk for anyone leaning on OPEC discipline. `[[finding_guidance_is_not_the_instrument]]` Source: PROME inbox packet 2026-08-02 (BRENT-verified, two named outlets fetched independently of this memo). No crowd figure in this file changes. KB-ORC-061 marked CORRECTED.
