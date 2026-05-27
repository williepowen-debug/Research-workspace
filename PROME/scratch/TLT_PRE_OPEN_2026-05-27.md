# TLT Pre-Open Packet — Wed 2026-05-27
**Created:** 2026-05-26 ~17:30 ET (pre-cabled by CC-Prome)
**To be filled:** Wed 2026-05-27 ~8:45-9:30 ET (next CC-Prome session)
**Output for:** Will (broker decision)
**Source rail:** `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md`
**Position in scope:** **3 × TLT Jun 18 $85P** (cost basis $0.82, $246 total)
**Out of scope but on same thesis:** 2 × Sep 30 $85P + 2 × Oct 16 $82P — held, no action

---

## What this packet does

Read live tape against the C1-C5 conditional rail and produce a single plain-English read for Will: **execute today**, **C2 session-1 banked (wait)**, **hold all 3 (substance break)**, or **no fire (do nothing)**.

This is also the **first scan of the WILL_APPROVED 6/18 cluster monitor** — fold that read into the same packet (Step 5).

---

## Step 1 — Pull live tape (Prome, ~8:45 ET)

```bash
python3 FORGE/tools/market-data/dashboard.py
```

**Known issue:** earlier this session, `fetch.py price` errored with `ModuleNotFoundError: No module named 'yfinance'`. If `dashboard.py` hits the same, fall back to `python3 -m pip install yfinance` in `.venv/` first, then retry. If still broken, ask Will for the dashboard URL or pull via web before bothering him with the morning read.

**Fill in:**

| Series | Tue 5/26 close | Wed 5/27 pre-open / live | As-of | Used for |
|---|---:|---:|---|---|
| TLT spot | $85.10 | _____ | _____ | C1, C2, C3 |
| HY OAS | 274 [5/25] | _____ | _____ | C5, R2, R4 |
| VIX | 16.92 | _____ | _____ | R1, R11 vol-spike context |
| KRE | $70.24 | _____ | _____ | R3 cluster trigger |
| WAL | $79.56 | _____ | _____ | A4/A5 position trigger |
| EGBN | (not pulled) | _____ | _____ | A2 position trigger |
| 10Y yield | 4.57% [5/21] | _____ | _____ | Substance context |

---

## Step 2 — Evaluate the TLT rail (Prome)

| Trigger | Condition | Tue close read | Wed read | Verdict |
|---|---|---|---|---|
| **C1** | TLT close ≥ **$85.50** single | $85.10 → did not fire | _____ | _____ |
| **C2** | TLT close ≥ **$85.20** × 2 consec | $85.10 → did NOT bank as session 1 | _____ | Wed close ≥ $85.20 banks session 1 |
| **C3** | TLT close **< $82** | $85.10 → safe (+$3.10) | _____ | _____ |
| **C4** | 2026-06-06 EOD with no other trigger | n/a today | n/a today | 10 days runway from Wed |
| **C5** | HY OAS ≥ 290 sustained OR R11 vol-spike (5/28-6/02 window) | HY OAS 274 (-16bp); R11 clock starts 5/28 | _____ | _____ |

---

## Step 3 — Plain-English readout (Prome → Will)

**Pick the branch that fires; copy-paste the message to Will.**

### Branch A — Nothing fires (TLT closes $82.00 - $85.19)

> **TLT Wed 5/27 read: no trigger fired.**
> TLT closed $___. No C1/C2 session-1 / no C3 / no C5. Runway to C4 backstop: 9 calendar days. C2 path remains alive — Thu close ≥ $85.20 banks as session 1.
> **Action: none today.** I'll repeat read Thu pre-open.

### Branch B — C1 fires (TLT close ≥ $85.50, single session)

> **🟢 TLT C1 FIRED — execute today.**
> TLT closed $___ ≥ $85.50. Single-close trigger fired. Tape says Jun $85P will only decay from here.
> **Place orders today PM or Thu open** (full broker orders below). Net cash ~flat to -$50.
> After fills: I update FORGE/STATUS, action card → COMPLETED, log to TRADE_DECISIONS.

### Branch C — C2 session 1 banked (TLT close ≥ $85.20, first session)

> **🟡 TLT C2 session 1 banked.**
> TLT closed $___ ≥ $85.20. First of 2 sessions banked. **No broker action today.**
> If Thu 5/28 also closes ≥ $85.20 → C2 fires → execute Thu PM or Fri open. If Thu drops below $85.20 → session reset, C2 path restarts.

### Branch D — C3 fires (TLT close < $82)

> **🔴 TLT C3 FIRED — HOLD ALL 3, DO NOT SELL.**
> TLT closed $___ < $82. Puts paying off — thesis activating; roll into expiry week with more exposure, not less.
> **Action: none at broker.** I prepare a fresh decision packet (likely "extend into expiry" or "add Sep/Oct exposure").

### Branch E — C5 fires (substance break)

> **🔴 TLT C5 FIRED — HOLD ALL 3, substance regime break.**
> [If HY OAS]: HY OAS hit ___ ≥ 290 sustained. [If R11]: vol-spike pathway fired in 5/28-6/02 window.
> Thesis activating — DO NOT sell into substance break.
> **Action: none at broker.** I prepare a fresh decision packet to re-evaluate sizing (likely +exposure, not the 2/1 trim).

---

## Step 4 — Broker-ready orders (only used if Branch B fires, or eventually Branch A→C4)

**Place as 2 separate limit orders for cleaner fills:**

### Order 1 — Close out all Jun
- **Sell-to-close 3 × TLT Jun 18, 2026 $85.00 Put**
- Limit: at mid or better
- Expected mid (pull from chain at run time): ~$_____ /contract
- Expected cash in: ~$_____ to $_____ total
- Order type: limit; day or GTC

### Order 2 — Open Sep roll
- **Buy-to-open 1 × TLT Sep 19, 2026 $85.00 Put** *(monthly, NOT Sep 30 quarterly — cleaner basis)*
- Limit: at mid or better
- Expected mid (pull from chain at run time): ~$_____ /contract
- Expected cash out: ~$_____ to $_____ total
- Order type: limit; day or GTC

### Expected net economics
- **Net cash: ~flat to -$50** (a thesis re-positioning trade, not a gain-lock)
- Final stack after fills: 1 × Sep 19 $85P + 2 × Sep 30 $85P + 2 × Oct 16 $82P = **5 contracts** on rate-bear duration

### Forbidden actions (per action card)
- No partial split beyond 2/1 (e.g. trim 1 / hold 2) unless C5 fires
- No revenge-adds if Jun expires worthless
- No re-entering Jun expiry after closing it

---

## Step 5 — 6/18 cluster monitor (first scan of WILL_APPROVED rail)

| Trigger | Threshold | Wed read | Status |
|---|---:|---:|---|
| **R1** VIX ≥ 22 (×2 sessions) | 22 | _____ | _____ |
| **R2** HY OAS ≥ 290 (×2 sessions) | 290 | _____ | _____ |
| **R3** KRE break $63 close | 63 | _____ | _____ |
| **R4** HY OAS ≥ 320 single | 320 | _____ | _____ |
| **A2** EGBN <$26 + (R3 OR Schedule O / Call Report disclosure) | 26 | _____ | _____ |
| **A4/A5** WAL break $73 close | 73 | _____ | _____ |

**If nothing fires:** log a single-line "no fire" entry to the cluster monitor (one-line in SCRATCH or a thin monitor log — TBD on first-run shape).

**If anything fires:** spawn the named domain agent (BROCK for credit, REGINALD for banks) for roll-target validation → fresh Will-approval packet.

---

## Step 6 — Telegram-ready output for Will

Combine TLT branch + cluster scan into one short message:

```
TLT Wed 5/27 pre-open read
Tape: TLT $___ / HY OAS ___ / VIX ___ / KRE ___ / WAL ___
TLT rail: [Branch A/B/C/D/E verdict in 1 line]
[If execute: 2 orders with limits]
6/18 cluster: [N triggers fired / "no fire"]
```

---

## Post-execution file updates (only if Branch B fires)

After Will reports fills:

1. `FORGE/STATUS.md` — TLT position table: remove 3 × Jun 18 $85P; add 1 × Sep 19 $85P with fill-price basis
2. `PROME/TRADE_DECISIONS.md` — append fills + outcome to existing 5/22 entry; state `BROKER_PENDING` → `FILLED` → `POSITION_UPDATED`
3. `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` — header state `BROKER_PENDING` → `COMPLETED`; record fill prices
4. `PROME/ACTIVE_DECISIONS.md` — remove TLT row (terminal)
5. `AGENTS/HENRY/STATUS.md` — flag execution-closed (or HENRY does on next boot via his outbox reply already on file)
6. `PROME/SCRATCH.md` — note close-out

---

## After-action notes for future pre-open packets

If this template structure works well Wed AM:
- Canonize as `PROME/templates/PRE_OPEN_PACKET.md` (reusable shell)
- Add to BOOT.md as a step when a `BROKER_PENDING` action card has a same-day broker window
- v_next: extend the template to cover multi-position pre-open reads (not just single-rail TLT)

If it's clunky, capture friction in `feedback_*` memory entry and iterate before reusing.
