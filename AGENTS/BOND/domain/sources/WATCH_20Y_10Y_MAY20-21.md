# BOND — Watch Card: 20Y (5/20) + 10Y (5/21) Reopenings

**Owner:** BOND
**Written:** 2026-05-19 15:47 ET (T-21h to Leg 1 takedown)
**Window:** 5/20 13:00 ET (20Y reopening) → 5/21 13:00 ET (10Y 9Y8M reopening)
**State going in:** 🟡→🟠 long-end leg active. BND-07 Day 2 (10Y 4.59 🔴 sustained, 30Y 5.12 🔴 4th session above 5). JPY through 159, Brent through $111, VIX 17.99 — public credit asleep (HY OAS 283).
**Live position rail:** TLT puts — hold; conditional add on Leg 1 confirmation; aggressive add on two-tail print across both legs.

> ⚠️ **Refresh snapshot at 12:55 ET 5/20 before Leg 1 takedown.** Section 1 values are 5/19 close marks — re-pull live before timestamping the auction-window snapshot.

---

## 1. Pre-Auction Snapshot

**Snapshot timestamp:** _to be set at 5/20 12:55 ET, immediately before 1pm takedown._
**Pre-write reference values (5/19 close, for staleness check at 12:55 ET):**

| Field | 5/19 Close | 5/20 12:55 ET (fill at refresh) | Δ |
|---|---:|---:|---:|
| 10Y yield | 4.59% | — | — |
| 20Y WI yield | _pull from TreasuryDirect/Bloomberg WI quote_ | — | — |
| 30Y yield | 5.12% | — | — |
| TLT mark | $83.01 | — | — |
| USD/JPY | 159+ (confirm spot) | — | — |
| Brent | $111+ (confirm spot) | — | — |
| VIX | 17.99 | — | — |
| SOFR–IORB | -12bps | — | — |

**Dealer-position context (last 20Y reopening, Apr 22):**
BTC **2.68** | tail (not provided in our last log; treat as on-screen) | indirect **59.6%** | direct **20.2%** | dealer **8.6%**.
Apr 22 dealer 8.6% is the **baseline take** — Leg 1 verdicts read against this, not against the long-run average.

**Context note:** 5/20 takedown lands with 10Y already 🔴 sustained (BND-07 Day 2) and macro co-pressure live (JPY 159+, Brent $111+). A tail is partly over-determined by macro; the **mix and dealer take** are the load-bearing reads, not the tail alone (see §5).

---

## 2. Leg 1 — 5/20 20Y Reopening: Verdict Matrix

**Auction:** $13B (assumed reopening size; confirm at announcement). Takedown 1:00pm ET 5/20.

| Print Pattern | BTC | Tail | Indirect | Dealer | Verdict | BOND State | Position Action (TLT puts) |
|---|---:|---:|---:|---:|---|---|---|
| **Clean** | ≥2.60 | ≤+1.0bp | ≥58% | ≤10% | Term-premium-only repricing | 🟡→🟡 (hold) | **Hold.** Ride trend; let 10Y 5-session trigger play out. No add. |
| **Soft but functional** | 2.50–2.60 | +1.0 to +2.0bp | 55–58% | 10–13% | Yellow duration fatigue continuing | 🟡 (hold) | **Hold.** No add. Wait for 5/21 read. |
| **Demand-hole watch** | <2.50 | +2.0bp or worse | <55% | 13–17% | Demand thinning; dealers absorbing | 🟠 (escalate) | **Add-conditional armed.** Scope a 4/5 delta layer pending 5/21. |
| **Dealer-absorption flag** | any | any | <55% | **mid-teens (13–17%)** w/ weak indirect | "Dealers catching what foreigners won't" | 🟠 (escalate) | **Add-conditional armed.** Same layer scope. Flag ZHAO. |
| **Failed** | <2.40 | >+3.0bp | <52% | >17% | Demand hole confirmed | 🔴 (fire) | **Aggressive add same day.** Don't wait for 5/21. |

**Tie-breaker:** if two cells fire (e.g., BTC 2.55 but dealer 14% and indirect 54%) → take the worse of the two reads. Mix > headline BTC.

**Reference: Apr 22 20Y reopening was BTC 2.68 / indirect 59.6% / dealer 8.6% — center of "clean" band. Any drift toward soft/demand-hole vs that baseline is the signal.**

---

## 3. Leg 2 — 5/21 10Y Reopening (9Y8M): Escalation Gate

**Auction:** 10Y reopening, 9Y8M effective. Takedown 1:00pm ET 5/21.
**Context going in:** This is the 5th consecutive 10Y print to watch for a tail. May 12 10Y stopped +0.4bp (4th consecutive tail).

| Print Pattern (combined with Leg 1) | Verdict | BOND State Move | Composite Long-End Vector | Position Action |
|---|---|---|---|---|
| Leg 1 clean + Leg 2 clean | Term-premium-only confirmed | 🟡 hold | 4 → 4 | Hold TLT puts; no escalation. |
| Leg 1 clean + Leg 2 single-tail | Thesis firming; 10Y stress specific | 🟡→🟠 watch | 4 → 4 | Hold; **conviction reinforced, no add unless 5-session 10Y trigger trips.** |
| Leg 1 soft/demand-hole + Leg 2 clean | Mixed; 20Y specifically thin | 🟠 | 4 → 4 | Hold + scoped add layer ready but not pulled. |
| Leg 1 soft + Leg 2 single-tail | Thesis firming both points | 🟠 | 4 → 4.5 | **Add-conditional executes** — pull the 4/5 delta layer. |
| **Two tails in 24h (both legs tail, any size)** | **BND-07 graduates: "thesis firming" → "thesis fired"** | **🟠 → 🔴** | **4 → 5** | **Aggressive add.** Same-day. Signal PROME. |
| Either leg failed (matrix red row in §2 or equivalent on 10Y) | Demand hole confirmed | 🔴 | 5 | Aggressive add; SOFR-IORB watch live. |

**Gate definition — "two tails in 24h":** any positive tail (stop yield > WI yield at 1pm) on both 5/20 20Y and 5/21 10Y, regardless of size. Two non-zero tails on consecutive long-end reopenings in a 24-hour window is itself the signal — size scales urgency, not the verdict.

---

## 4. Decision Rails & Cross-Agent Signal Flags

### 4a. Position-Delta Map (TLT puts)

| Posture Label | Concrete Posture | Triggered By |
|---|---|---|
| **Hold** | Current TLT put position, no change | Leg 1 clean + Leg 2 clean / single-tail |
| **Add-conditional** | **TLT $83P Aug 15 × 2, budget ~$500-600 (accept up to ~$1,000 on marks). Execute morning of 5/20 IF Leg 1 prints orange (§2 rows 3-4).** Fills the Jul-Aug mid-tenor gap in Will's current TLT ladder (Jun 18 $85P × 3 near-dated; Sep 30 $85P × 2 + Oct 16 $82P × 2 long-dated). $83 strike = near-ATM (TLT $82.99 at 5/19 close); real delta if Leg 2 fires without paying for deep ITM. If 5/21 also weak → layer carries with conviction; if 5/21 clean → layer remains as paid-for option on second-derivative break. | Leg 1 soft or demand-hole watch (§2 rows 2–4) |
| **Aggressive-add** | **Execute add-conditional layer (TLT $83P Aug 15 × 2) same-day off this card without waiting for live [Approve], per Will's pre-approval. Plus additional Will-sized layer (sizing TBD; remaining budget headroom — see proposal below).** Pull forward any planned roll. | Leg 1 failed (§2 row 5) OR two tails in 24h (§3 row 5) |
| **Kill** | Close TLT puts | 10Y back below 4.15 AND 5/20 20Y prints clean AND 30Y back below 5 for 3 sessions |

**Pre-approval scope: Aggressive-add posture only. Conditional-add and Hold still require Will-side decision-making cadence.**

All position deltas other than Aggressive-add are **proposals to Will**, not auto-execute. Aggressive-add fires same-day off this card per Will's pre-approval (5/19 relay); BOND/Prome notifies Will and executes.

### 4b. Cross-Agent Signal Flags (NOT actions — Prome routes)

| Trigger | Route To | Signal |
|---|---|---|
| SOFR-IORB lifts from -12bps toward 0 / positive on weak auction print | **LIQUID** | Auction stress transmitting to funding — escalate term-premium read to plumbing read |
| Indirect <55% on either leg | **ZHAO** | Foreign demand hole; reconcile against TIC and recent reserve-manager behavior |
| HY OAS lifts off 283 toward 300 during/after the auction window | **HENRY** | Credit-equity lead activating concurrent with duration break — rare combination, high signal |
| Two tails in 24h (§3 row 5) OR either leg failed | **PROME** | Composite long-end vector 4→5; BOND state 🟠→🔴; escalate to Will-facing synthesis layer |
| Brent or JPY breaks +1σ of current path during 5/20-5/21 | **HAWK / BRENT (Brent) or PROME (JPY)** | Macro co-pressure over-determining the tail — flag for context, not a separate BOND action |

**Discipline note:** BOND identifies; Prome routes. No outbox writes during this watch unless explicitly tasked.

---

## 5. Macro Co-Pressure Box (load-bearing this window)

JPY through 159 and Brent through $111 mean the **5/20 and 5/21 prints land into a tape that is independently inflationary and duration-hostile.** This changes how we read tails:

| Macro Condition Going Into Print | Tail Interpretation |
|---|---|
| JPY 159+ stable, Brent $111+ stable | Tail is **informative** — auction-specific demand read is clean |
| JPY breaking further (160+) or Brent breaking further ($114+) **during the auction window** | Tail is **partly over-determined** by macro — discount the size of the tail by ~30–50%, but the **mix** (indirect %, dealer %) remains clean signal |
| Both JPY and Brent stable | Tail is **fully informative** — read at face value |
| Both JPY and Brent breaking | A tail is **expected** — only a **clean print** is meaningful (i.e., resilience under macro pressure is the signal) |

**Key:** Macro co-pressure can over-determine **tail size** but cannot over-determine **demand mix**. Indirect % and dealer % stay informative regardless of JPY/Brent path. When in doubt, read the mix.

**Pre-print check:** at 12:55 ET 5/20 and again at 12:55 ET 5/21, log JPY and Brent spot in §1 snapshot. If either breaks more than 1% between snapshot and 1pm takedown, note it in the post-print writeup.

---

## 5.5. Morning-of Tasks (5/20)

- **Pre-1pm chain pull** — query live TLT Aug 15 option chain via `FORGE/tools/market-data/`. Report bid/ask for $83P, $82P, $84P. Hand to Will with delta/IV context.
- **Pre-1pm tape refresh** — fill §1 snapshot table at 12:55 ET. Flag any overnight deltas in JPY, Brent, 10Y.
- **Note:** HYG legacy (8 × $75P Jun 18, ~$245 total mark, down 77%) on watch — bystander signal only, no action. Watch HYG mark if Wed two-tail prints; could be a loud bystander signal if transmission catalyzes.

---

## 6. Post-Print Logging Plan

After each leg's 1pm result hits the screen:

| File | Update | Trigger |
|---|---|---|
| `workbook/KB.tsv` | One row per auction: date, tenor, size, BTC, high yield, indirect, direct, dealer, tail, with Source `[CONF TreasuryDirect <date>]` | Both legs, regardless of verdict |
| `workbook/VX.tsv` | Long-end/duration vector score: hold at 4 (clean / single-tail) or push to 5 (two-tail / failed). Note prior state, new state, trigger row from §3. | Both legs |
| `workbook/PREDICTIONS.tsv` | BND-07 status: "in motion Day 2" → either "Day 3 / still firming" (clean) or **"FIRED"** (two-tail / failed) | After 5/21 close |
| `STATUS.md` | Dashboard refresh (10Y, 20Y, 30Y, TLT, SOFR-IORB, HY OAS); Convergence Matrix long-end row; Latest Auction Read append; Bottom Line | Both legs, evening of each |
| `TRADE.md` | TLT puts row — update Current Posture, Conviction, and Hold/Add/Kill Rules to reflect new state | Both legs, evening of each |
| `WATCH_20Y_10Y_MAY20-21.md` (this file) | Append a "Result" section after each leg with: actual print, verdict cell triggered, action taken, cross-agent flags raised | Both legs |

**Archival:** once both legs are logged and STATUS.md/TRADE.md reflect the read, move this file to `domain/sources/auctions_20260520/` as the durable record.

---

## Open Scope Questions for Will — RESOLVED 5/19 PM (Prome relay)

1. **Add-conditional sizing:** ✅ **LOCKED.** TLT $83P Aug 15 × 2, budget ~$500-600 (accept up to ~$1,000 on marks). Fills Jul-Aug mid-tenor gap in TLT ladder; $83 = near-ATM at 5/19 close.
2. **Aggressive-add window:** ✅ **PRE-APPROVED for same-day execution.** If Leg 1 prints failed (BTC <2.40 / tail >+3bp / indirect <52% / dealer >17%) OR two tails in 24h on 5/21 → BOND/Prome notifies Will and executes per posture without waiting for live [Approve]. Pre-approval scope is **aggressive-add only**; conditional-add and Hold still require Will-side cadence.
3. **HYG $75P Jun (legacy 8 contracts, down 77%, ~$245 mark):** ✅ **Let it ride.** No add, no roll, no cut. Watch HYG mark if Wed two-tail prints — bystander signal if transmission catalyzes.

## Open Now (post-resolution)

- **Aggressive-add additional-layer sizing:** the aggressive-add posture is the conditional layer (TLT $83P Aug 15 × 2) **plus** an additional Will-sized layer. Sizing not yet locked. **BOND default proposal:** **match the add-conditional layer = +2 more contracts of TLT $83P Aug 15 (total = 4 contracts, ~$1,000-1,200 budget at 5/19 marks).** Rationale: same strike/tenor keeps the layer easy to manage; doubling preserves convexity without overextending budget headroom. Will can override (e.g., shift second layer to $82P or $84P, or scale to ×4 for double the layer).
