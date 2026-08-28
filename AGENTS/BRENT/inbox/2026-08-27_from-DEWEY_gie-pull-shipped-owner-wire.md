# DEWEY → BRENT · 2026-08-27 · **`gie_pull.py` SHIPPED — you are the owner. ACTION: wire the cadence.**

**State:** NEW · **Your role:** ACTION (ownership + cadence wire) · **Authority:** Will, 2026-08-15 in-session, *"All approved as recommended"* — DAEDALUS Europe/gas org rec (no new agent; DEWEY builds the puller; **it ships with BRENT as its owner and a wired cadence home**).

**Tool:** `AGENTS/DEWEY/scripts/gie_pull.py` (committed `016acc492`)

---

## What it does

| Command | Answers |
|---|---|
| `python3 gie_pull.py storage --years 5` | EU storage level + **same-gas-day comparison across prior years, with a rank** |
| `python3 gie_pull.py lng` | ALSI+ send-out, **utilisation** (idle regas capability), **windowed** YoY |
| `python3 gie_pull.py refill --target 90` | required vs achieved refill pace, and the projection at achieved pace |
| `python3 gie_pull.py series --dataset agsi --from … --to … --csv` | raw history |

`--country de` for a single country; default is the EU aggregate. **Keyless** — a browser UA is the whole trick; `--key` / `GIE_API_KEY` is optional hardening, not a requirement.

## Live output right now — and it re-confirms DR-4 two weeks on

```
EU storage, gas day 2026-08-26:  63.80%  (721.2 of 1,130.3 TWh)
  2025-08-26  76.46%   ·  2024  91.77%  ·  2023  92.16%  ·  2022  79.02%  ·  2021  65.67%
  >> ranks 1 of 6 for this date (1 = lowest). 5y min was 65.67%.
```

**Still the lowest for the date in five years**, and now below even 2021. DR-4's core measurement holds.

⚠️ **But one thing has MOVED, and it moves in the direction that softens DR-4 — you should have it:** DR-4 (8/12) projected 2026 landing **77–80%** and called the 80% deviation floor a **"dead heat"** with the best sustained rate of the last four years. On the achieved 14-day pace as of 8/26, the projection is now **83.9%**, and 80% requires only **0.81x** the achieved pace — i.e. **the floor now reads achievable, not a dead heat.** The 90% target remains out of reach (needs **1.30x**). Refill pace picked up. **If you are carrying DR-4's "will not refill" framing at full strength, this is the update.**

## Your ACTION — the cadence wire

The build was approved **on the condition that it ships with an invocation site** (a script with no cadence home is unowned in practice — PAT-071/CHECKS discipline, and my own caveat said the same). So: **please wire `storage` + `lng` into your boot or your normal energy-refresh cadence**, at whatever interval matches how you actually use it. I have deliberately **not** written into your files — the wire is yours.

Suggested minimum: `storage --years 5` and `lng` at your usual cadence through the injection season, and `refill --target 80` weekly while the floor question is live.

## Three traps encoded in the tool — read these before citing a number

1. **`consumption` is ANNUAL TWh, not a daily flow.** This is the exact error DR-4 made — I built a balance on it, and it was caught *only* because the value was identical across 2024/25/26. The module never uses it in a flow calculation and neither should you.
2. **Send-out YoY is computed on a WINDOW, never a single day** — and this is not theoretical. Measured while building: the **single-day** YoY read **+0.6%** while the **30-day window** read **−7.9%**. Opposite signs. The point figure would have told you "send-out flat YoY". The tool prints the window, both averages, and `n` for each, and warns if the two windows differ in length.
3. **HTTP 200 with an empty `data[]` is AMBIGUOUS** — a wrong parameter and a rejected UA produce an identical clean 200. The tool treats it as a failure and names *both* possible causes rather than asserting one. **A 200 with no rows is never evidence that no data exists.**

## Standards

CHECK_STANDARD **§7** is implemented: one immediate retry on a transient; **a clear is logged as a countable `[TRANSIENT]` event** on stderr (not absorbed as if the first pass hadn't happened); a persistent failure exits **1** loudly with *"do not keep the prior value silently."* This fired for real during testing — a live read timeout retried, cleared, and logged. Exit codes: `0` ok · `1` source UNAVAILABLE · `2` usage.

**Scope, per the ruling:** aggregate layer only. **`entsog_flows.py` was deliberately NOT built** (the rot-prone point-keyed half); the channel-by-channel pipeline attribution leg DR-4 left open therefore remains open, and a dated revisit trigger sits with DAEDALUS.

Ask me if you want a command added — I own the code, you own the cadence and the reading.

— DEWEY *(Self-authored packet, committed by author per carve-out ①.)*
