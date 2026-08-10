# VIX-vs-HY Decoupling Test Battery (Tests A/B/C)

**Registered:** 2026-08-10, financial-conditions forum (`FORUM/2026-08-10_financial-conditions/`). **Will-ruled 2026-08-10 in-session, forum FINAL §5 item 5: REGISTERED, act on none yet.** DOCKET rows set by PROME: Test B grades **8/24**, Test C closes **8/26**, Test A first read **~9/1**.

**Purpose:** the forum's independence question — is HENRY's twin soft-kill VIX leg and HY leg (and by extension my own GATE-HY-REKILL, confirmed the same kill as HENRY's HY leg per the forum's kill-correlation map) one risk-on factor measured twice, or genuinely distinct? HENRY's daily-change correlation (ρ≈+0.52 full-sample, current-regime ~0.34, effective signals ~1.3-1.5) rules out "one tick measured twice" but cannot rule out a common slow-moving factor. These three tests are the discrimination battery, registered as frozen spec text — no threshold moved, no gate created, nothing fires from these tests alone.

**Provenance:** designed by LIQUID (`03_LIQUID_falsifiers.md` §c), Test A's numeric bands added by HENRY (`01_HENRY_falsifiers.md` §2c), Test C's NO-DATA branch added by HENRY (`01_HENRY_falsifiers.md` §4e). Co-attributed per the forum's own concur/dissent correction (`04_synthesis/03_LIQUID_concur-dissent.md` §2).

---

## Test A — structural, DXY-residual (LIQUID design, HENRY numeric bands)

**Status: REGISTERED, UNDER-POWERED. First read ~2026-09-01. Do not act before then.**

- **Series:** 20-trading-session (≈1 calendar month) rolling change in (a) HY OAS [`BAMLH0A0HYM2`], (b) VIX close, (c) DXY [`DX-Y.NYB`].
- **Method:** regress ΔHY(20d) on ΔDXY(20d) and separately regress ΔVIX(20d) on ΔDXY(20d); take the residuals of each; compute corr(residual-HY, residual-VIX).
- **Window:** expanding sample from GATE-HY-REKILL's registration (2026-06-26) forward. As of 2026-08-10: ~9 non-overlapping 20-day windows. Minimum 12 before drawing a conclusion (~3 more weeks).
- **Read (HENRY's numeric bands, adopted):**
  - Residual correlation **< 0.15** ⇒ the dollar/funding-conditions axis (DXY) is carrying most of the shared slow-moving component; HY-vs-VIX becomes substantially more independent once conditioned on it. LIQUID's own EndGame DXY read gains relevance as the shared-factor explanation.
  - Residual correlation **≥ 0.45** ⇒ the common factor is broader than dollar conditions (a pure risk-appetite factor with no clean single proxy); HENRY's ~1.3-1.5 effective-signals read is close to a ceiling on how independent these legs can ever be shown to be.
  - Between 0.15 and 0.45 ⇒ partial explanation, no clean call.
- **Why DXY:** already LIQUID's registered EndGame negative control (soft/falling = benign; squeeze UP through 102-103 = the one config treating HY and VIX as jointly downstream of a dollar-funding shock) — reuses an instrument this bloc already has a shared read on.

## Test B — tactical, 10-session fresh-extreme race (LIQUID, fully spec'd)

**Status: LIVE, running. Window 2026-08-11 through 2026-08-24. Grades 8/24 (DOCKET).**

- **HY leg:** does HY OAS (`BAMLH0A0HYM2`) print a close **≤265** at any point in the window? (Halfway from the 8/7 print of 270 to the GATE-HY-REKILL 260 kill line.)
- **VIX leg:** does VIX (close basis, per HENRY's applied precedent) print **≤14.77** at any point in the window? (Matching or exceeding the 8/7 intraday low — a genuine fresh cycle extension, not a repeat close near 14.90.)
- **Decoupling-toward-credit:** HY leg fires, VIX leg does not ⇒ credit-specific driver running independent of the vol regime.
- **Decoupling-toward-vol:** VIX leg fires, HY leg does not (HY stalls ≥267 or reverses) ⇒ vol-specific, not credit-led.
- **Same-factor:** both fire in the same window, or neither fires ⇒ consistent with HENRY's ρ measurement, no discrimination achieved.
- No further design work needed — mechanical grade at window close.

## Test C — opportunistic, AI-credit leg on the 8/12 CPI natural experiment (LIQUID design, HENRY NO-DATA branch)

**Status: REGISTERED, instrument not yet named. Window 2026-08-11 through 2026-08-26. Closes 8/26 (DOCKET).**

- Extends HENRY's and VIOLET's VIX-vs-blended-HY common-shock discriminator (8/12 CPI) with a third leg on the idiosyncratic AI-credit channel this forum surfaced (CRWV DDTL repricing, ORCL fallen-angel/off-balance-sheet exposure).
- **Spec:** any qualifying AI-infra credit print (new issue, syndication, CDS mark, rating action) landing in the window. Moves **with** blended HY/VIX ⇒ common-factor evidence, migration thesis weakens. Stays flat or **diverges** ⇒ migration confirmed into a genuinely separate channel.
- **Mandatory NO-DATA branch (HENRY's addition, adopted):** if NO qualifying print occurs in the window, the result is recorded as **NO-DATA** — explicitly NOT a null and explicitly NOT evidence of decoupling. An empty window must not silently read as "the AI-credit channel didn't move," which would let the migration thesis collect free evidence from an absence.
- **Instrument TBD:** no dated, scheduled print exists as of registration (CRWV's next filing-verifiable moment is an undated Q2 10-Q). Name the instrument when one qualifies inside the window.

---

## Cross-reference

- HY-REKILL joint-read pre-registration (T11, same forum) → `KILL_MEMO_HY_OAS_260.md` § Migration joint-read.
- Same-kill counting rule (H-2) → `KILL_MEMO_HY_OAS_260.md` § Same-kill note.
- T6 (30Y benign-bucket test, BOND's instrument, LIQUID co-spec) → STATUS.md § EndGame monitor.
- Full forum record: `FORUM/2026-08-10_financial-conditions/` — desk-state `03_LIQUID`, cross-read `03_LIQUID`, falsifiers `03_LIQUID`, synthesis `01_HENRY` + `03_LIQUID` concur/dissent.
