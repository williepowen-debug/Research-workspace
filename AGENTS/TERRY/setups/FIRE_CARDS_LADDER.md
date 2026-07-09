# FIRE CARDS — Ladder & Comparison

**Updated:** 2026-07-09 (TRY-FIRE-004 added, NO-ARM recorded) · **Owner:** TERRY · **Status:** all **PROPOSE-ONLY**, **$500 max-loss/card**, **0 fired live**.
Living index of the staged fire cards. Standing rule (Will 6/26): fresh capital deploys ONLY on a fired trigger — never pre-position. Update this doc when a card is added/fired/invalidated.

**The cards:**
- `PRICE-TRIGGER_HY280_regional-put.md` — TRY-FIRE-001
- `PRINT-TRIGGER_WAL-EGBN-build.md` — TRY-FIRE-002
- `PRINT-TRIGGER_monoline-COF-SYF-ALLY.md` — TRY-FIRE-003
- `FLOW-TRIGGER_duration-TLT-put.md` — TRY-FIRE-004 (duration/TLT puts, flow/velocity-discriminator-gated — spec routed by PROME 7/6, ID-corrected 7/8, card built + 7/9 arm-check NO-ARM recorded this session)

---

## Comparison

| | **TRY-FIRE-001** | **TRY-FIRE-002** | **TRY-FIRE-003** |
|---|---|---|---|
| **Target** | KRE (regional ETF) | WAL / EGBN (single-name regional) | COF / SYF / ALLY (monoline) |
| **Trigger class** | **PRICE** | **PRINT** (regional) | **PRINT** (consumer) |
| **Fires when** | HY OAS **≥280 sustained** (from ~276) | grades path **(c)** WAL ex-fraud NCO >55bps + life-sci charge-off, OR path **(a)** ≥2 specific builds {CFG/OZK/EGBN/WAL} | grades path **(m)** un-mask: ≥2 monolines (or 1 strong-single ≥2 tells) |
| **Catalyst date** | Any time (price-driven, not dated) | EGBN ~Jul 22 / WAL ~Jul 30 | SYF/ALLY ~Jul 21 / COF ~Jul 21–23 |
| **What grades it** | Live HY OAS + CCC-HY ratio | `grade_print.py` paths a/b/c | `grade_print.py` path m (`--book-direction`/`--nco-guide`/`--dq-formation`) |
| **Vehicle** | KRE puts, **3–6mo**, 8–12% OTM | WAL/EGBN puts, **post-print** Sep/Jan-27, 8–12% OTM | firing monoline puts, **post-print** Sep/Oct/Jan-27, 8–12% OTM |
| **Why this vehicle** | Level/path trigger → **ETF beta** is the clean read | Single-name credit substance → single-name put | Single-name un-maskable consumer → single-name put |
| **Invalidation** | HY round-trips <270 sustained | grade = release / collective-only / $99M cures | clean masked headline, OR already gapped (no under-reaction) |
| **Existing book overlap** | ⚠️ KRE Dec/Sep/Aug ladder (check net-new) | ⚠️ Sep WAL put ladder (check net-new) | None — net-new (verify) |
| **Thesis owner** | REGINALD + NEXUS | REGINALD / CARL | CARL + REGINALD grid |

---

## July print calendar (from `grade_config.json`)

```
Jul 16    CFG, OZK         -> feed path (a) regional tally
Jul 21    SYF, ALLY, ZION  -> monolines (path m) + ZION (path b AOCI trap)
~Jul 21-23 COF             -> monoline bridge (card path m + commercial)
Jul 22    EGBN             -> cleanest path (a) regional
Jul 30    WAL              -> path (c) standalone + path (a) build-defer
```

---

## How they ladder — and the link between them

- **By trigger type:** FIRE-001 is the **price** rail (fires any day LIQUID's X1 conjunction hits); 002 and 003 are **print** rails, date-bound to the July earnings window.
- **By sequence within the prints:** the **monolines (003) print ~Jul 21, ahead of the WAL/EGBN expression names (002, Jul 22–30)** — the un-maskable consumer tell reads *first*.
- **The gate link (load-bearing):** the monoline print is also the **gate** on the regional card. Monoline **BREAK** (003 path-m fires) → raises EGBN/WAL build odds (002 more likely to grade). Monoline **BEAT** → fades path (a) before the regionals print. So 003 is also the **leading indicator that tilts whether 002 fires.**

**Net:** three expressions, one credit thesis, laddered so the earliest/cleanest read (monolines) informs the later/heavier one (regionals), with the price rail (HY280) underneath as the regime-level catch-all.

> Caveat per owners (6/25–26): trade-READY ≠ high-conviction. REGINALD grades realized synchronized NCO as a **2027** event (Q2 path = reserve-build, ~25–35%); LIQUID is pre-trigger (HY ~276, in no-man's-land). Don't pre-position into green banks — let the print/level grade, then express.

---

## TRY-FIRE-004 (separate rail — duration, not credit)

**Target:** TLT puts · **Trigger class:** **FLOW/VELOCITY** (explicitly not PRICE-level) · **Thesis owner:** BOND/LIQUID/SAM+ZHAO · **Confidence:** LOW/contingent.
Arms on ANY ONE of 3 discriminators (BND-11 acute 7/9 reopen / VX-BND-05 10Y-sustain 5-closes≥4.50 / soft TIC 7/16) — never the bare 30Y-level poke. Full spec + discriminator log → `FLOW-TRIGGER_duration-TLT-put.md`.
**2026-07-09 state:** arm-#1 (BND-11) **NO-ARM, HIGH confidence** — every leg failed (indirect 77.74%, dealer 10.05%, BTC 2.44, foreign demand surged; BOND grades the level as oil/term-premium, not demand-hole). arm-#2 (10Y 5-close sustain) is the **live watch**: 2-of-5 entering today, 10Y ~4.53 intraday — today's 4PM close, if ≥4.50, makes 3-of-5. arm-#3 (TIC) unchanged, pending 7/16.
