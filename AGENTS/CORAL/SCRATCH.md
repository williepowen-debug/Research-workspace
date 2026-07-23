# CORAL SCRATCH — 2026-07-22 EVE (~10PM ET, PROME-spawned scoped session: BKU Q2 grade)

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (7/21 EVE full refresh)

Narrow PROME-scoped evening session: grade **BKU Q2 (leg 2 of the FL-bank synchronization test)** on the frozen 7/21 pre-registered 4-axis frame. **VERDICT: BENIGN — 1-of-4 axes deteriorating (bar ≥3) → BKU does NOT count; sync count stays 0-of-≥2.** Zero threshold moves; graded as-written.

- **Axes:** (a) NCO 11bps vs 61bps Q1 = BENIGN · (b) provision $15.1M vs $25.1M Q1, no named FL-RE reserve = BENIGN · (c) ACL 0.87%→0.91% (+4bps, outside ±1bp band) = DETERIORATING mechanical (context: build into improving asset quality, ACL/NPL 75.9%→97.1%) · (d) NPLs −19% QoQ/−40% YoY + criticized CRE −14% QoQ = BENIGN.
- **Tape-vs-fundamentals DISAGREE (context, not grade):** BKU −4.43% to $45.94 — ugliest cohort reaction this week — on EPS $0.97 miss (cons ~$1.00–1.03) + revenue miss + expense creep; credit was the strongest part of the print.
- **Primary:** Q2 8-K ex-99.1, EDGAR acc. 0001504008-26-000076, pulled + parsed directly (curl + UA header; WebFetch 403s on EDGAR).
- Three independent FL surfaces now benign in 48h: CCBG credit (7/21) + FL June labor (7/21) + BKU credit (7/22). **Rail NOT met, unchanged; no state change without PROME/Will.**

## WHAT I DID THIS SESSION

- Boot: CLAUDE + STATUS + FL_BANK_WATCHLIST (frozen frame). No git pull needed (PROME packet; 3 other live sessions on box — touch-nothing-outside-own-dir discipline).
- Pulled BKU 8-K ex-99.1 from EDGAR (primary), extracted credit tables, graded mechanically.
- **Files:** FL_BANK_WATCHLIST (row 2 graded + sync-count line + live-window line), STATUS (new 7/22 block + signal line + bank-exposure headline + BKU row [px $45.94 7/22] + open-Q1 + FEEDS-TO), CALENDAR (BKU ✅), KB ML-CORAL-047 (9-col validated), outbox `2026-07-22_to-PROME_bku-fl-sync-leg2-grade.md`, SCRATCH (this), NEXUS_BRIEF (refresh).
- Commit local only — **NO push** per PROME packet (3 live agent sessions on box).

## NEXT SESSION (mechanical, in order)

1. **7/23: GATE DAY cluster grade** — VLY (BMO) + SSB/AMTB/USCB (AMC) per pre-registered spec (`FL_Forward_Log.md` + `CLUSTER_FL_BANK_LEG.md`). First day the ≥2 bar could mathematically fire; with CCBG+BKU benign it needs ≥2 deteriorating among the remaining 5 names. USCB condo-assoc book = purest read; transcript-mine VLY + BPOP calls for HOA/association color.
2. **⚠️ Parcl MSI sustain check — STILL PENDING (not in tonight's scope):** fresh pull ≥7/22; ≥5 FL metros still >6.0 → FIRE 🟠→🔴 supply-side leg. The one item that can move a leg to 🔴 immediately.
3. **7/28–29:** SBCF grade (nonaccrual 3rd-rise tell) · Ocala June UR (BLS 7/29) · Amendment-3 hearing (pre-reg ML-CORAL-042).
4. **New from tonight:** BKU 10-Q check on the unattributed "higher specific reserves" ACL component (which segment?) — de minimis unless it names FL-RE.
5. Carried: Bertha dissipation confirm · SIRS 12/31/26 statute verify · One Alliance Demotech FSR · CCBG $0.2M-vs-$0.9M provision conflict (ex99.1 re-pull) · HO-premium 3-figure reconcile · FL Realtors county-PDF cash-share build.

## OPEN THREADS

- **Bank-transmission gate: NOT met, 0-of-≥2** — 7/23 + 7/28 decide the week. Pre-registrations frozen, do not re-fit.
- **MSI tripwire: ARMED, sustain check overdue-pending (item 2 above).**
- EGBN 7/22 AMC printed, not read (context-only, non-FL — excluded from count by construction).
- HO premium level / metro condo months-supply / Sep-Oct Citizens takeout dates / RESEARCH-INTAKE query amendment — all carried unchanged from 7/21.

## MAIL STATE

- `inbox/` (root): 0 pending at 7/21 closeout; NOT re-scanned tonight (narrow one-off spawn — per protocol step 8/9 exemption). `inbox/WALTER/`: 0 pending as of 7/21.
- `outbox/`: NEW `2026-07-22_to-PROME_bku-fl-sync-leg2-grade.md` (PROME spawned this session and receives the report directly; file left in outbox root per task packet). Prior: 7/21 PROME muni-credit memo still in root (in-flight).
- 3 other agent sessions LIVE on this box tonight — committed pathspec-only, no push, no pull.
