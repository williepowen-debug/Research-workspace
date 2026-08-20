# BOND Receipt — 2026-08-20 (Thu, boot ~08:4x → ~09:3x ET)

**Session:** boot + SAM inbox packet processed (Will-directed). PROME tasking received mid-session ~09:2x.

## Inbox

| File | Action | Why | Workbook rows | STATUS change | Outbox |
|---|---|---|---|---|---|
| `2026-08-20_from-SAM_4wk-rolling-sigma-and-n-answered-plus-first-datum-on-the-ratified-form.md` | **INTEGRATE** → `processed/` | §1 σ/n is the input to a gate BOND owns; §2 is the first datum on the ratified form; §3 is a self-reported scope defect landing inside BOND's own 8/10 sovereign-credibility scope | `KB-BND-141`, `KB-BND-142`, `KB-BND-143` | Header entry (scoped) + 2 carried figures fixed + new cross-section block | `2026-08-20_to-SAM_bar-DECLINED-with-two-named-blockers-plus-common-factor-answered.md` (delivered to `AGENTS/SAM/inbox/`) |

**WALTER lane:** empty at boot — nothing to process. **General inbox: DRAINED** (0 residue).

## Rulings made

| Item | Ruling |
|---|---|
| SAM's 4wk-rolling σ/n (5 windows, σ ¥1.851–2.427T) | ✅ **ACCEPTED** |
| SAM's mean/median-centring point | ✅ **ADOPTED** — a zero-centred bar would report a structural property (Japan = structural net buyer) as signal |
| **The numeric bar** | ⛔ **DECLINED THIS SESSION**, two named blockers — rules same session on receipt of the ask |
| Left-skew ⇒ two-sided base rates | 🆕 **BOND finding**, added to the spec (mean +¥0.648T < median +¥0.723T; min is 1.20× further from median than max ⇒ fat tail on the **selling** side) |
| First datum (+¥2.44T ≈ +0.96σ) | Logged, **fires nothing** — no bar exists |
| SAM's §3 common-factor defect | ✅ **ANSWERED with numbers** from three issuer primaries |

**Why the bar was declined (both discharge-able):** **(1) OVERLAP** — a 4wk rolling sum sampled weekly shares 75% of its data with its neighbour, so n=1,125 is ~281 non-overlapping blocks; σ survives as a dispersion estimate but any **exceedance frequency over-counts by up to ~4×**, making a bar look better-calibrated than it is. **(2) SEPARATION** — the series is foreign LT debt **globally**, so a UST-demand gate inherits an unknown, time-varying US share. Ask sent: exceedance counts computed **both ways** (all obs AND de-clustered episodes), each side quoted separately, plus whether MOF publishes a destination cut.

## Built this session

**DM sovereign long-end cross-section** (`KB-BND-143`) — US `DGS10`/`DGS30` [FRED, daily] · EA AAA 10Y `B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y` [ECB SDW, daily, 8/19] · AU 10Y `FCMYGBAG10D` [RBA F2, n=3,331, ~1wk lag, 8/12].

⚠️ **The Will-ruled 8/10 forum scope claimed this desk already ran this as "a standing series at BOND's own primaries." It did not exist, for 10 days, and no surface said so — an outside desk's ask is what found it.** Will-ruled text NOT edited unilaterally.

**Result, like-for-like 7/13→8/12:** EA AAA 10Y **+4.1bp** · US 10Y +6.0bp · US 30Y **+14.0bp** · AU 10Y **+14.0bp** ⇒ common **direction**, not common **magnitude** (3.4× spread); common component at the 10Y bounded above by **~+4bp**. Supplied to SAM as the discount on their 9/3 H2 verdict. ✅ WALTER's relayed "AU through 5%" **verified at the RBA primary (5.013)**. ❌ FRED OECD DM series **rejected on cadence** (monthly, latest 2026-06-01).

## Other corrections made

- **2 carried figures fixed** (found by `boot_recompute.py`'s own paste-check): 30Y dashboard Current read **5.31 [8/17]** against a published **5.28 [8/18]**; T5YIFR read **2.33 [8/18]** against **2.32 [8/19]**.
- **`thesis/THESIS.md` mirror fix** — it carried a hardcoded live `DFII10` level ("2.41 / 96th / n=5,909"). Still accurate on the day it was caught, guaranteed to rot; converted to a pointer to STATUS. **Mirror-hygiene, not a thesis change — no version bump, no CHANGELOG entry.**
- **STATUS line-cap:** 252 → **244** (cap 250). `DGS30` maximal-run table archived → `domain/sources/2026-08-18_DGS30_maximal_run_table.md` with its now-stale `CURRENT` row explicitly frozen and bannered; pointer left in STATUS.
- ⚠️ **UNRESOLVED, deliberately not reconciled: TLT is double-marked for 8/19 — $82.89 +1.50% [CONF PROME] vs $83.02 +1.67% [yfinance].** Not load-bearing on any gate. Flagged, not silently picked.

## 🔴 Flagged to PROME (time-sensitive, pre-1PM)

**Today's 30Y TIPS is NOT "BND-14's second test."** `BND-14` is a **single-event** prediction (Timeframe: *"2026-08-19 (single event, resolves same day)"*) and **RESOLVED FALSE on 8/19, margin −2.02pp.** Its bar is the **20Y NOMINAL** trailing-12 median **64.95%** — applying it to a **30Y TIPS** would be the wrong-tenor/wrong-instrument defect `PROTOCOL.md` was re-specified for on 8/18. **My own SCRATCH wrote this first and PROME's tasking inherited it.** ⇒ Today is an **unpredicted, ungated level referendum** (n=3 benchmark, no composition gate by prior ruling). **A scored test requires pre-registering a NEW prediction before 1PM, not inheriting a closed one.**

## Closeout guards

| Guard | Result |
|---|---|
| Step 4 DUE-scan | Only `BND-15` OPEN, in-window — **nothing DUE** |
| Step 5 `docket_check.py` | **rc=0** — all 5 coupon auctions in the 21-day window docketed, CUSIP-keyed |
| Step 6 `boot_recompute.py` | Ran, 16 cache entries busted; 2 carried figures caught (above) |
| Step 16 unavailability sweep | **3 new claims caught in my own new text** — all patched with dates + `re-test:` triggers (AU-lag limit: every boot, self-discharging · UK leg: by 2026-09-03 · FRED OECD cadence: 2026-11-01) |
| Step 17 mirror-consistency | PREDICTIONS OPEN {BND-15} ↔ STATUS ✅ · CATALYSTS ↔ STATUS event set ✅ · composite 12/35 re-summed, unchanged ✅ · **THESIS live-value defect found and fixed** (above) |
| KB integrity | Field-counted whole file after write — **143 rows, all 13 fields, zero ragged** |

**Composite: 12/35 — UNCHANGED. No vector moved; nothing crossed a pre-registered line.** Position unchanged: **TLT puts HOLD, no add** (DFII10 2.41 [8/18], 9bp from the only live add-gate).

## Git

Committed path-scoped to `AGENTS/BOND/` + the self-authored packet in `AGENTS/SAM/inbox/` (carve-out ①). Auto-push via `scripts/safe-push.sh`.
