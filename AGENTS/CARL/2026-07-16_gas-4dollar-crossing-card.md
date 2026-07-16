# 🟠 CROSSING CARD — Gas National Avg $4.00 (expected ~Sat-Sun 7/19-20)

**Pre-staged by:** CARL · **2026-07-16 ~10:50 ET** · **For:** weekend-PROME (fleet runs light 7/19-20)
**Purpose:** so weekend-PROME just **confirms a number**, not reconstructs context. This is a **pre-registered CARL call** (CRL-26) — the crossing grades me.

---

## 1. DATA SOURCE + EXACT CHECK
- **Metric:** AAA national average, Regular unleaded (the canonical behavioral-breakpoint series).
- **How to check (30 sec):** from repo root —
  `.venv/bin/python3 AGENTS/CARL/scripts/gas_tracker.py` → read the **"Regular:"** line (it prints "Below $4.00" vs a threshold flag + auto-appends `scripts/data/GAS_TRACKER.tsv`). Or eyeball `gasprices.aaa.com` (national avg, top of page).
- **Current:** **$3.943** (my live pull, 7/16 09:36 ET). **Gap to $4.00 = $0.057.**
- **Momentum:** $3.797 (7/6 wk-ago) → $3.872 (AAA 7/13) → **$3.943 (7/16)** = ~$0.017-0.02/day; Rockies +16¢/wk (biggest region). FRED weekly GASREGW $3.855 (as of 7/13, +7.8¢ WoW) confirms direction. At current pace → **touches $4.00 ~7/19-20 (3-4 days).**
- **Driver:** Hormuz-closed regime — Brent ~$85-86 live (vs ~$70 pre-shock), RBOB wholesale $3.15 feeding the pump on the 17-18d lag.

## 2. WHAT THE CROSSING MEANS (when it prints)
- **First $4.00 national activation THIS CYCLE** (the behavioral breakpoint). The May $4.564 AAA peak was a brief spike-and-revert; this is a fresh **sustained** approach on a supply-shock regime.
- **It lands INSIDE the July CPI reference month** (July calendar month; print rel ~Aug 12). So the crossing = July energy CPI flips from **June's −5.7% MoM → sharply positive** → **July headline goes deflationary→HOT** (my June-trough/July-reload frame).
- **Feeds these rows:**
  - **CRL-26** (this crossing — pre-registered today; the crossing resolves it).
  - **CRL-01** (gas pass-through / behavioral breakpoint) — the pass-through mechanism firing.
  - **V5 Gas-Squeeze vector (currently 3):** **sustained >$4.00 is the re-arm trigger (3→4)** — but that's a **Will-decision**, not auto (held at 3 since 7/10).
  - **V12 Stagflation (5):** July-CPI-hot re-loads the inflation leg (validates the "no relief" read).
  - **NOT CRL-08** ($4.50, 28% OPEN): $4.00 is a waypoint, does NOT resolve CRL-08 — still ~$0.56 away, needs a wholesale re-spike.

## 3. WHAT TO DO ON CROSSING (write-backs + cross-flags)
- **STATUS.md** Gas Pump row → update value + stamp "**$4.00 CROSSED [date]**" (first this cycle); flip status note to behavioral-breakpoint-ACTIVE.
- **PREDICTIONS.tsv CRL-26** → resolve CONFIRMED with date + level.
- **KB row** (next ID after 334) → the crossing datum.
- **NEXUS_BRIEF** → re-stamp + note $4.00 active (July-reload confirmed).
- **Cross-flag HENRY** (July-CPI-hot frame — energy flip feeds his July-CPI/vol read) + **BRENT/HAWK** (pump confirms crude transmission; already own the Brent side). If it ever approaches $4.50 → the CRL-08 SENDING row fires to BRENT/HAWK/PROME.
- **V5 3→4** = flag to **Will** on a *sustained* >$4.00 (≥~2wk or Will-confirm) — do NOT auto-execute the vector bump.

## 4. INVALIDATION (before crossing)
- **Retreat below $3.85 before touching $4.00 → the ~7/19-20 call is a timing MISS** (wholesale rolled over again, à la the 7/10 RBOB −7.33% reversal). $3.85 is ~$0.09 under current $3.943 = a real reversal, not noise.
- **Discriminator:** a dip to $3.88-3.92 = pause/noise, **call intact**; **sustained <$3.85 = wholesale reversal, call broken** (re-arm needs RBOB back >$3.20 sustained). Weekend-PROME: only treat as invalidated if it drops **under $3.85**, else the call stands.

## 5. HOW TO GRADE ME (one line — pre-registered)
> **CRL-26 (pre-reg 7/16, level $3.943):** AAA national Regular crosses **$4.00 by Sun 7/20**. **CONFIRMED** if AAA national ≥$4.00 any day 7/17-7/20. **MISS** if it retreats <$3.85 before touching $4.00, OR fails to reach $4.00 by 7/20 close. Confidence **70%** (momentum favors it; the tail risk is a fresh intraday wholesale rollover — the 7/10 precedent is real).

---
*Weekend-PROME: the whole task is "read the AAA Regular number." ≥$4.00 → resolve CONFIRMED per §3. <$3.85 → invalidated per §4. In between → still pending, no action.*
