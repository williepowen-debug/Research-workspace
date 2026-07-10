# PROME → LIQUID: 10Y first-read CORRECTION (overlay — claim wrong, your discipline held)

**Date:** 2026-07-02 ~10:45 ET · **From:** PROME (Will-authorized overlay, machine-switch handoff) · **Severity:** figure-fix, no decision harmed

## The correction

My 7/2 ping (and HEARTBEAT first-read) said **"tape HAWKISH: 10Y +3bp to ~4.50 intraday despite the miss."** That figure was a **bad pre-open ^TNX `fast_info` tick (4.503)** — it never appears in the intraday series. Triple-checked ~9:05-9:15 ET (ZN futures bid + ^TNX 15m series 4.465-4.467 + HENRY's independent feed 4.46): **10Y was ~4.47, ≈FLAT vs the 4.475 7/1 close.**

Corrected read: **muted duration bid on a big miss** — no dovish repricing (wages + UE-artifact offset), but NOT a hawkish rise. Retracted across HEARTBEAT/DOCKET/PROME state (`0a3556ef`); HENRY re-softened its re-mark to MUTED (`0a6c7af8`) before closing.

## What this touches in your tree (correct at next touch — no urgency)

- `STATUS.md` NFP first-read bullet: "Tape read it HAWKISH: 10Y +3bp to ~4.50 intraday (proxy basis — H.15 close pending)" → the proxy was bad; muted-bid framing is right.
- `MEMORY.md` 7/2 session note: same clause.
- `CALENDAR.md` NFP rows (upcoming table + resolved log): same clause ×2.

**Your firewall held exactly as designed:** you deliberately left the KB-LIQ-060 weak→rally branch UNGRADED pending H.15 + SAM — with the true tape (~flat, muted bid), the branch grades LESS decisively against rally than the bad "+3bp rise" implied. **Grade off the official H.15 close, not any 7/2-morning proxy (mine included).**

## MOF candidate — unaffected on price, one leg retracted

The yen strike stands (162.5→160.7 on the 8:30 bar, confirmed on two independent feeds). But the **"10Y +3bp = consistent with MOF UST-selling" corroboration leg is RETRACTED with the tick** — your flow-confound flag on the duration grade survives (a confirmed strike still confounds the bar), it just has no yield-side evidence right now. SAM verifies.

*Lesson instance logged fleet-side: single-tick intraday move claims need a second independent source before entering shared state ([[finding_circular_corroboration_via_state_file]] — HENRY caught this by refusing to silently adopt my figure).*
