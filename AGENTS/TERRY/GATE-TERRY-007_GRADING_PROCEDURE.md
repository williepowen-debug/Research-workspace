# GATE-TERRY-007 — 4:15PM GRADING PROCEDURE (MECHANICAL, EXECUTION-ONLY)

**Built:** 2026-08-20 Thu ~09:2x ET by TERRY, at PROME's tasking, for a **FRESH session at ~4:15PM.**
**Card:** `setups/FLOW-TRIGGER_duration-TLT-put.md` (`TRY-FIRE-004`, 25× TLT Sep-30 77P)
**Gate:** `GATE-TERRY-007` — `PROME/GATES.tsv`, registered 2026-08-19.

> ⛔ **THIS FILE DECIDES NOTHING AND GRADES NOTHING.** It is the checklist so the 4:15 session executes rather than re-derives. **Rulings B and C are Will's, encoded verbatim 8/19 — this procedure may not reinterpret them.** If the data disagrees with this file, **the data wins and the card's ZONE-1/F9 text wins over this file.**

---

## 0. Pre-flight (30 seconds)

- [ ] `date` — copy the wall clock; **never hand-write a time or weekday.**
- [ ] Confirm it is **after ~4:15PM ET** — FRED DGS10 publishes then. Before that, **STOP**; a missing row is not a `<4.50` row.
- [ ] Read the card's **ZONE 1 / F9** text and the RULING B/C block. This file is a convenience, not the authority.

## 1. The ONLY instrument

**FRED `DGS10` official closes. Nothing else.**

```bash
curl -s "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10&cosd=2026-08-06" \
  -H "User-Agent: Mozilla/5.0 (research; williepowen@gmail.com)"
```

- ⚠️ **`^TNX` IS COUNT-NEUTRAL.** It neither counts nor resets. Drift is routine and expected (8/19: ^TNX 4.65–4.67 intraday vs DGS10 4.72 official [8/17]). **Do not let a ^TNX print near 4.50 start or reset anything.**
- ⚠️ **Official governs retroactively over provisionals** (card's 7/10 co-ratification riders).
- ⚠️ **Holidays neither count nor reset** — a missing date is a non-day, not a non-qualifying day.
- ⚠️ **Published 2 decimal places.** `4.50` is NOT `<4.50`. The test is **strictly less than 4.50**, so 4.50 itself does **not** qualify. 4.49 does.

## 2. State as of this file's build (2026-08-20 ~09:0x ET)

| date | DGS10 | `<4.50`? |
|---|---|---|
| 2026-08-13 | 4.63 | no |
| 2026-08-14 | 4.68 | no |
| 2026-08-17 | 4.72 | no |
| **2026-08-18** | **4.71** | **no** |
| **2026-08-19** | **NOT YET PUBLISHED** | pending — publishes ~4:15PM **today** |

> ✍️ **DISCLOSURE, so the 4:15 session is not misled about its own novelty:** the 8/18 row **was already published and was observed by TERRY at the 8/20 boot pull.** It is recorded here as **DATA**. **No grade was written to the card, to `GATES.tsv`, or to any ledger** — the graded record remains the 4:15 session's to make. ⚠️ **PROME's tasking said "8/18+8/19 officials publish ~4:15PM 8/20"; that is wrong for 8/18, which was already out.** Only **8/19** is pending.

**Consecutive-close counter: `0`.** Nothing has qualified. No count has started.

## 3. The two rulings, as encoded (do not reinterpret)

- **RULING B** — a **single** official DGS10 close `<4.50` ⇒ **RESET the arm-#2 consecutive-close counter to zero.** It does **NOT** kill arm-#2, does **NOT** lapse the card, does **NOT** exit the filled position. *(Ruled COLD, before any qualifying print.)*
- **RULING C** — **FIVE consecutive** official DGS10 closes `<4.50` ⇒ **EXIT 004.** TERRY **builds the exit proposal → Will [Approve]. Never self-executed.**
- **One close resets; five exit.** Symmetric with arm-#2's arming (5 consecutive ≥4.50).

## 4. Decision table — read the pending 8/19 value, then act

| 8/19 official DGS10 | counter after | action |
|---|---|---|
| **≥ 4.50** (incl. exactly 4.50) | **0** | ✅ **NOTHING.** Record the observation on the card. No proposal, no gate change, `$0` moved. |
| **< 4.50** | **1** | Record **count = 1 of 5**. ⚠️ **This is NOT an exit and NOT a kill** — RULING B/C. Note the next 4 sessions matter. No proposal. |
| **absent / holiday** | unchanged | Non-day. Neither counts nor resets. Re-check next publication. |

**Reaching 5 is the ONLY state that produces a proposal**, and even then the output is a **proposal for Will**, never an execution.

## 5. Moot-risk — pre-registered, so it is not re-litigated at 4:15

**41 DTE at 8/20; $212.50 at risk.** Decay may beat the count: five consecutive closes cannot complete before ~5 business days, and the position expires 9/30. **If expiry beats the count, the correct read is `NO-VERDICT` — a non-event is never scored as a miss.** (Registered with the gate on 8/19.)

## 6. Write-back if and only if something changed

- [ ] Card: append the observation to the RULING B/C block (dated, with the FRED value).
- [ ] If the counter moved off 0 → say so plainly and state the count as `N of 5`.
- [ ] `PROME/GATES.tsv` is **PROME's file** — packet PROME, **do not edit it.**
- [ ] `python3 AGENTS/TERRY/scripts/ledger_sweep.py` must exit 0 before closeout.

---
*Nothing in this file moves money, moves a threshold, or grades anything. TERRY proposes only; Will approves.*
