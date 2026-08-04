# TERRY · QQQ LANE

**Created 2026-08-04** at Will's direction: *"I am interested in finding some way to trade QQQ because the volatility and volume seems strong to me. But clearly I am not doing a good job."*

Both halves of that sentence are load-bearing, and this directory exists to serve both — **the instrument is worth specialising in, and the record says the losses are not coming from the analysis.**

---

## ⛔ BOUNDARY CONTRACT — read before adding anything here

This desk has already killed one directory for being a fork waiting to happen (`postmortems/`, removed 7/30 — an empty scaffold beside the live `POSTMORTEMS.md`). **This lane must not become the second.**

| Lives HERE | Lives ELSEWHERE — do not copy it here |
|---|---|
| Durable, **measured** QQQ knowledge (base rates, vol/volume regime, levels that have been tested) | **Trade cards** → `setups/`. Always. No exceptions, no "working copies." |
| Re-runnable analysis scripts | **Day-trade process, journal, P&L roll-up** → `daytrading/` (all instruments) |
| The consolidated QQQ record + failure-mode diagnosis | **Day-desk QQQ rules** → `daytrading/QQQ_DESK_CARD.md` — that card is canonical for intraday |
| The pre-ticket construction rules for this instrument | **Structured setup state** → `SETUPS.tsv` · **ledger** → `TRADE_BOOK.md` |

**The test for anything new: does it state a fact about QQQ that survives across trades?** If it states the state of a *position*, it belongs in a card or a ledger, not here.

⚠️ **Nothing in this directory is a state surface.** `ledger_sweep.py` does not gate it, so a number copied here can rot silently. **Cite the source; do not restate it.**

---

## 📉 THE RECORD — QQQ, 2026-07-20 → 08-04

*Consolidated from `daytrading/JOURNAL.md` (canonical for the day tickets) and `setups/`. Summary, not a ledger — go to the source before acting on any figure.*

| | |
|---|---|
| Day-desk short-dated put tickets | **7**, since 7/20 |
| Realized on those | **≈ −$2,268** |
| The 687P ×3 (closed 8/4 at Will's word) | **≈ −$783 to −$843** `[FILL_PRICE_UNKNOWN]` |
| **Total realized** | **≈ −$3,081** |
| Swing cards built | 2 (`TRY-WILL-QQQ-VFADE`, `TRY-WILL-QQQFADE` parked) — **$0 deployed** |
| **Directional split** | **8 of 8 short** |

### 🔴 The diagnosis, and it is not what it looks like

**The read has been internally consistent and the execution has not.** Five failure modes, and **four of them are the same failure wearing different clothes — a plan that exists and is not executed:**

| # | Failure | Evidence |
|---|---|---|
| **1** | **Direction is a bias, not a read** | 8 of 8 short, into a tape that ran **+10.1% in four sessions** |
| **2** | **Size exceeds the cap before the trade is even wrong** | 687P at **$843 = 3.4R** against a **2R / $500** cap = **1.7× oversized** |
| **3** | **No harvest — winners round-trip** | 687P was **+23.6% at Friday's close**, held through a non-trading gap, died near-worthless |
| **4** | **The hard stop has NEVER been executed** | breached ~10:10 on 8/3, not acted on. **0 for 4 across four reviews.** |
| **5** | **Same-day re-entry after a loss** | **4 of 4.** 7/30: realized −$390, then bought −$1,431 the same session = **3.65× the dead ticket** |

> ★ **#2–#5 are all "the rule was written and not followed."** That means **more analysis will not fix this.** The fix has to be structural — see `PLAYBOOK.md`, whose central move is to stop relying on in-the-moment execution of rules this desk has a 0-for-4 record on.

**What is NOT broken:** the tape-reading. 7/7 puts is a *consistent* read, and the V-fade card's thesis invalidation was **pre-registered and correct** — it named the level that would refute it, and cost **$0** when the level printed. The machinery works. The discretion is what leaks.

---

## 📁 Contents

| File | Purpose |
|---|---|
| `README.md` | This — boundary contract, the record, the diagnosis |
| `RESEARCH.md` | Measured findings: V-recovery base rates, the vol/volume regime, the data-integrity finding. **Dated; re-derive before trading off it.** |
| `PLAYBOOK.md` | What this desk will and will not trade on QQQ, and the pre-ticket gate |
| `scripts/v_episodes.py` | Re-runnable episode analyzer. `--selftest`, `--integrity`, `--json` |

## 🔁 Re-run before quoting anything

```bash
(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/qqq/scripts/v_episodes.py)
(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/qqq/scripts/v_episodes.py --integrity)
```

**Every number in `RESEARCH.md` is a 2026-08-04 snapshot.** The script is the authority; the document is the transcript. If they disagree, **the script is right and the document is stale** — that is the whole reason the script exists.
