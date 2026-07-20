# PROME → TERRY: broker export LANDED + reconciled — Monday spine unblocked — 2026-07-20 ~8:45 AM ET

**Will-authorized (in-session).** This note updates your 7/19 packet (`2026-07-19_from-PROME_tlt-put-live-entry-read.md`) with this morning's fresh state. That packet remains the task spec; this is the delta.

## 1. The fillability gate is CLEARED
Will delivered the fresh broker export this morning (screenshots, ~8:27 AM ET pre-market). **PROME reconciled the FORGE mirror 7/16→7/20 — read `FORGE/STATUS.md` (commit `b7c26f21`) as your book input.** Rule #4 still applies at fill-time (live re-mark before any proposal goes to Will), but the export input your packet was gated on now exists.

Key book facts for your reads:
- **Core duration-short book UNCHANGED:** TBT 14 sh + TLT $85P Sep-30 ×2 (mark $1.78, TLT $84.52 = strike slightly ITM) + $82P Oct-16 ×2 ($0.79). Cash $23,530.77 — **no fills over the gap; NO-ADD held; the $500 is still banked.**
- **NEW Robinhood entries (Will direct):** WAL $77.5P Aug-21 ×1 (nearest-money bank put, survives the 7/21 print) · USO $128C 7/22 ×1 · QQQ $696P **expires TODAY** (ITM at QQQ ~$695.3 pre-market — Will's day-trade lane, not yours, but it's in the book). **§9 concentration math should use these** — the WAL 77.5P and USO 128C both deepen the "Mideast-hot / bank-print" thesis stack.
- All Jul-17 expiry dust (both accounts) died as recorded, incl. your triaged USO 120C/127C.

## 2. Day-color: today may QUALIFY — adjudicate first
Pre-market ~8:35 AM: **TLT +0.37% GREEN · equities red** (WAL −2.0%, KRE −1.6%, QQQ −1.5%) · USO +3.9% on Brent ~$88.3. That is the BOND-ruled clean-entry signature (arm-LIT + TLT-green = yields pulling back, not chasing). Your packet's task order stands: **(a) rule the rule-#6 day-color question** (BOND inversion memo 7/18 — formalize it on the card), **(b) live-chain re-mark the TLT Sep-18 74/75/76/77P ladder**, **(c) is-Monday-qualifying**, **(d) go/no-go proposal → Will [Approve]**. Pre-market color is indicative only — re-check at your read time; regular session opens 9:30.

## 3. Also owed today (from your inbox/queue, unchanged)
- **Kharg merged-semantics confirm** — GATE-TERRY-006 went LIVE 7/18 on the corroborator-anchored merged condition; FALCON's confirm note is staged in its outbox for you. Verify vs your TRY-FIRE-006 card wording; ack to PROME outbox.
- **HBAN stub → dust-rider** — Will ruled EXIT-THESIS 7/18; retire the stub per the REGINALD brief (×2 Oct-16 16P rides as dust).
- **Paper-book boot step 5b** — Phase-1 went live 7/19 (`ae739980`, seed PB-0001); your boot wiring should pick it up. Two non-blocking nits from PROME are in your inbox (venv-for-live-marks · entry_basis wording).

## 4. Deliver-before-idle
Findings + the go/no-go proposal → your outbox to PROME **and** state written to your own dir + committed (pathspec, own dir only) before you idle. PROME is live in a parallel window; REGINALD/FALCON/LABOR spawning now — FALCON owns anything Kharg-corroborator-fresh you might need (ask via outbox, don't self-source).

— PROME
