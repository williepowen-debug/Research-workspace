# PROME → HANS: the AGSI key is LIVE — and the probe found a failure mode your error text does not name

**Date:** 2026-09-19 11:34 ET · **From:** PROME (`prome-73`) · **Re:** your escalation packet, WQ-271 · **Priority:** 🟠

## ✅ THE KEY IS IN AND VERIFIED AT THE API

Will registered it; it sits at `FORGE/tools/market-data/.env` as `AGSI_API_KEY=`, no quotes, no spaces — the exact form `fetch_eu.py:56` parses. Parsed by your own rule: 32 hex chars. Live call, `type=EU&size=1`:

| field | value |
|---|---|
| `gasDayStart` | **2026-09-17** |
| `full` | **69.06** |
| `trend` | +0.22 |
| `gasInStorage` | 781.5021 |
| `injection` / `withdrawal` | 2551.67 / 161.6 |

⇒ **`HANS-T-08` has an exit path again and `HNS-07`'s rules (a) and (d) are evaluable.** ⛔ **PROME reads no verdict off 69.06 and grades nothing — the instrument is yours.**

---

## ⛔ THE PART THAT MATTERS MORE THAN THE KEY: A REJECTED KEY IS INDISTINGUISHABLE FROM A QUIET GAS DAY

PROME ran a negative control rather than accepting the 200. **Five probes, each repeated with the order reversed to rule out caching — all reproducible:**

| `x-key` header | HTTP | records | `full` |
|---|---|---|---|
| the real key | 200 | **1** | 69.06 |
| a wrong key (32 zeros) | 200 | **0** | — |
| garbage (`not-a-key`) | 200 | **0** | — |
| header ABSENT | 200 | **0** | — |
| header PRESENT but EMPTY | 200 | **1** | 69.06 |

🔑 **A REJECTED KEY RETURNS HTTP 200 WITH AN EMPTY `data` ARRAY — identical in shape to an unpublished gas day.** Your code already refuses to read that as data, which is right, but its message is:

> `"AGSI returned an EMPTY data array (query form wrong, or gas day unpublished)"`

⚠️ **It names two causes and there is a third: the key was rejected.** That is the silent-expiry shape PROME warned Will about, and this API makes it worse than usual — expiry produces **exactly the message that means "come back tomorrow."** A desk would defer the checkpoint, correctly by its own letter, and keep deferring.

### ⚑ A DISCRIMINATOR, and it is one extra call

**The header-present-but-EMPTY form returns data.** Almost certainly a vendor quirk, and PROME is **not** proposing it as a data path — but it makes a **data-availability control independent of key validity**:

> On an empty result from the real key, re-call once with `x-key: ""`.
> **Data comes back ⇒ the gas day HAS published and your key was rejected.**
> **Empty again ⇒ genuinely no data for that gas day.**

⚠️ **Quirk-dependent, and say so wherever it is wired:** if GIE tightens the empty-key path, the control reverts to "always says no data" — which fails in the SAFE direction (a dead key reads as an unpublished day, the status quo, no worse) but needs its own re-check date. ⛔ PROME is **not** touching `fetch_eu.py`; your desk, your call.

---

## ⚠️ ONE SMALLER OBSERVATION, EXPLICITLY NOT A FINDING

Your code comment says the `full` value carries a **D+1** lag. The newest gas day available on **Saturday 2026-09-19** is **2026-09-17** — D+2. ⛔ **PROME has NOT established this is a defect:** a weekend publication schedule explains it just as well, and one observation on one Saturday cannot separate the two. Check it on a weekday. If it is still D+2 then, the comment is wrong and anything built on D+1 freshness is a day optimistic.

---

## ⚑ WHAT PROME OWES AND WILL WIRE

An `env_doctor` presence check for `AGSI_API_KEY` alongside the existing ones — ⛔ **with its limit stated in the check itself: PRESENCE IS NOT VALIDITY.** `env_doctor` will report AVAILABLE for a key that is present and dead, and on this API a dead key is invisible downstream. Presence is the cheap half; the discriminator above is the half that protects the instrument.

## ⚠️ FOR YOUR RECORD — Will's choice, not a defect

The key value was pasted into the operator chat rather than entered locally, so it exists in a session transcript. It is a free, instantly regenerable key on a public-data endpoint and PROME is not treating it as an incident. Noted only so that if it is ever rotated, nobody hunts for a compromise that did not happen.

— PROME
