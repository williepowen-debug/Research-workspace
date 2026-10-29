# LIQUID — due-row grades, 2026-10-29 (Thu, 00:05–00:30 ET, PROME `prome-92` Tier-1 wake under WQ-184)

Markets closed. Every figure carries its observation date and basis. No threshold, grade operator or band is changed here. Evidence files in this folder: `first_published_ICE_2026-10-29.txt` (FRED `output_type=4` pulls, 00:11 ET), `xccc_2026-10-28.json` (BondBloxx XCCC page, 00:13 ET). The 079 FIRE-band census is `../2026-10-29_079-fire-bands/`.

## 1. Credit — FRED ICE first-published, observation 10/27 (bp)

| Series | 10/23 | 10/26 | 10/27 |
|---|---|---|---|
| HY `BAMLH0A0HYM2` | 338 | 330 | **318** |
| IG `BAMLC0A0CM` | 91 | 90 | 88 |
| BB | 206 | 198 | 187 |
| B | 343 | 336 | 322 |
| CCC | 1,356 | 1,345 | 1,321 |

Derived 10/27: HY−IG 230 · CCC−BB 1,134 · CCC−B 999. All tiers tightened 10/26 and 10/27; no BB/CCC co-widening (the L818 10/27 publication check: nothing to confirm).

## 2. HY >320 sustained (WQ-444 letter, KILL_MEMO row 60) — RUN ENDED

First-published run: 325 / 323 / 331 / 329 / 333 / 327 / 340 / 338 / **330** [10/14 → 10/26] = **9 consecutive cells > 320.0**; **318 [10/27] ≤ 320.0 ⇒ reset to 0-of-3.** The 10/19 MET was non-latching; no fire, no route owed by the letter on a reset. An INFO note goes to WALTER because the 10/19 MET was signalled to ALL. X1 HY half (> 280 sustained): still met (318 > 280); X1 stays CLOSED / DON'T-SIZE (BROCK's half). REG-T-04 (REGINALD's > 350 ×3): own witness 0 of 3, max 340 [10/22].

## 3. Gate grades (letters unchanged)

| Gate | Grade | Basis |
|---|---|---|
| GATE-HY-REKILL | NOT FIRED 0-of-2 | 318 [10/27], 58bp above 260 |
| GATE-LIQ-072 | QUIET / NOT FIRED (price legs) | IG 88 not > 94; basis 230 not < 180 [10/27]; event legs carried from 10/26 |
| GATE-LIQ-069 | 🟠 2-of-2 FIRED unchanged (L2 + L5), no re-count | **L1 NOT FIRED:** BB 187 [10/27] ≤ 220 (33bp under; CCC 5-session −6bp = flat). **L4 NOT FIRED 10/26–10/28:** worst raw close 10/26 NBIS −3.45%; 10/27 all four names +7.9% to +11.2%; 10/28 all up (+4.5% to +7.3%) — equity half fails on every session, so the 10/28 HY cell (pub ~10/29 16:15 ET) is moot for L4. **L2 still above both line sets:** DTCC CRWV 5Y (2031-12-20) 10/27 1,007–1,026bp, 10/28 983 / 945 (capped) clean, 1,003 / 965 dirty — down ~80–100bp from ~1,083–1,100 [10/20], still far above > 550 / > 666.5 (model-derived, not ISDA-certified). **L3** NO_INSTRUMENT. **L5** no new agency action searched tonight (carried 10/22). `scripts/gate069_legs.py` rc 0; `scripts/crwv_cds_grade.py` rc 0. |
| GATE-LIQ-076 | 🟠 existing episode MET (10/22 grade); **current 14-day window 10/15→10/28 reads 1-of-3 (W3 only)** | W2's two weeks (G5L10 −1,462 [10/7], −1,717 [10/14]) are dated by as-of Wednesday, and 10/14 falls outside a window anchored at the 10/28 W3 cell. W3 MET on the yfinance witness 10/26–10/28 (MOVE 94.55 / VIX 16.91 [10/28]); VIOLET's close governs. W1 NOT MET as-of 10/20 (net −2,373,040). **No re-arm** (W3 met every gradeable session since 9/23) ⇒ no second write-up. **Waits on:** W2 as-of 10/21 (NY Fed PD, Thu 10/29 ~16:15 ET) and W1 as-of 10/27 (CFTC TFF, Fri 10/30 ~15:30 ET). |
| GATE-LIQ-079 | NOT ARMED | SOFR99 − IORB (NY Fed primary, IORB 3.90): 10/26 **+11**, 10/27 **+14**bp; no ≥ +30 day. Rising for six sessions (+5 [10/19] → +14 [10/27]) into month-end; 10/28–11/3 are calendar-excluded and break any run. SOFR 3.95 / EFFR 3.88 [10/27]; repo-op take-up $0.004–0.005B 10/26–10/28 (NY Fed); RRP $0.18–0.23B. FOMC 10/28 held 3.75–4.00 (WALTER SIG-W-20261029-001; FRED IORB 3.90 dated 10/29), so the date-matched ceiling is unchanged. FIRE legs: band PROPOSAL delivered tonight (L261), still UNGRADEABLE until Will rules. |

## 4. Rated-CCC composition (WQ-516 A I1, DOCKET L829) — refreshed

BondBloxx XCCC page, retrieved 2026-10-29 00:13 ET (HTTP 200): holdings as-of **10/28**, 178 securities (~158 issuers by name), sector breakdown as-of **10/27** (issuer taxonomy). **AI builders 0.0%** (name screen for CoreWeave, Applied Digital, TeraWulf, Cipher, IREN, Core Scientific, Nebius, Lambda, Crusoe, Hut 8, data-center issuers: 0 holdings) · **Technology 7.81%** (issuer bucket; software not separable without per-issuer classification — DEWEY's 10/22 "software ~6%" is a different, hand-classified basis) · **Communications 16.98%** (≈ DEWEY's cable/telecom/media 16.5%) · **everything else 75.21%** (by difference). Top issuers [10/27]: CSC Holdings 2.13%, Garda World 2.09%, athenahealth 2.07%, CHS 1.99%, Gray Media 1.98%, Ardonagh 1.80%, Altice France 1.74%. ⚠️ Basis change from the 10/22 seed: issuer sector taxonomy, not DEWEY's buckets; the two are not differenced.

## 5. LIQ-04 (10/30 source reconciliation)

No qualifying PitchBook LCD monthly-average BSL new-issue AAA figure obtained; access gap unchanged since the 10/19 reconciliation. Secondary indication only: WALTER SIG-W-20261027-070 relays CRE Daily — September US CLO issuance $41.1B, AAA ~122bp (newsletter-attributed, basis unverified) — below the 150 letter line. Forecast-as-made unchanged.

## 6. Inbox drain (27 items, every sender)

Logged in `board_log.tsv` (rows 2026-10-29); moved with `git mv` to `inbox/processed/` and `inbox/WALTER/processed/`. Acted: WALTER 10/26-012 (Brazil stop-loss testimony kept separate from measured forced liquidation; no LIQUID funding grade), 10/27-025 (data-center cohort widening: newsletter method unverified; read against own CRWV CDS, which tightened 10/20→10/28), 10/27-029 (Broadcom/Anthropic $63B: committed, not funded; supplier residual support), 10/27-040 (JetBlue issuer liquidity $2.2B incl. $600M undrawn; $250M Q4 financing not received; bond identity still a gap), ISHM 10/26 boundary (reply: no broader free HY history than FRED's rolling ~3 years). Everything else noted or info-only.
