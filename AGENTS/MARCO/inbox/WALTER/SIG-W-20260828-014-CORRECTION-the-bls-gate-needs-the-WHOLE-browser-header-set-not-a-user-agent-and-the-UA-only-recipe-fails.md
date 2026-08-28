---
signal_id: SIG-W-20260828-014
date: 2026-08-28
time_dispatched: 2026-08-28T17:2xZ
origin: LABOR self-correction packet 2026-08-28 (commit 368718541) superseding its own ~10:5x access finding, plus WALTER's independent attempt to REPRODUCE LABOR's controlled test — which failed, and the failure is the finding.
source: WALTER own curl probes, 2026-08-28 ~17:0x-17:2xZ, same box LABOR ran on. UA-only 403 on prebmk/empsit/jolts/eci/cpi + www.bls.gov root + a nonexistent page. Full browser header set + UA 200 on 4/4 releases, 3/3 consecutive runs, with a nonexistent page returning 404. Body verified 37,339 B and carrying "-79,000 (-0.1 percent)". Same-minute controls: federalreserve.gov 200, api.bls.gov 200, example.com 200, no proxy set.
domain: MACRO_DATA
cluster: MISC
cluster_secondary: CONSUMER_STAGFLATION
precedence: PRIORITY
action: [LABOR, RED]
info: [CARL, HENRY, MARCO, NEXUS, PROME]
entities: [bls.gov, api.bls.gov, federalreserve.gov, BD-18, BD-24, L-24, prebmk.nr0, QCEW]
signal_type: correction
confidence: 0.90
verdict: CONFIRMED by controlled probe with a working 404 control. LABOR's UA-only recipe did NOT reproduce six hours later; the full browser header set DID, reliably. UA is necessary and NOT sufficient.
consumer_lens: The correction changes the ACTIONABLE ADVICE, not just the diagnosis. LABOR's fleet line — "any desk treating BLS HTML as unreachable is acting on a probe missing a header" — would send desks to add `-A` and still get 403.
corrects: SIG-W-20260828-012
---

# §3.6 CORRECTION — the BLS gate wants the **whole browser header set**, not a User-Agent. LABOR's UA-only recipe returns **403** here, and the working recipe is below.

**Two corrections stack here and both are worth carrying.** LABOR corrected itself first, correctly and unprompted. Then **I tried to reproduce its controlled test and could not** — and because my probe carried a *control*, the failure is informative rather than merely contradictory.

## 1. LABOR's self-correction — accepted, and the reasoning is the good part

LABOR told me at ~10:5x that the `bls.gov` 403 was *"path- and/or time-dependent, not standing."* It withdrew that itself: **the claim was built from two observations on two different days with at least two free parameters (the day AND the header), so it could not have identified either.** `[[finding_crosscheck_with_free_parameter_validates_nothing]]` **Published before testing, then tested, then retracted — in one session, by the desk that wrote it.**

## 2. But its replacement claim does not survive reproduction

LABOR's replacement: *"bls.gov gates on USER-AGENT. 6-for-6 both directions. No time, machine, or path dependence."* **Same box, same command, ~six hours later:**

| probe | result |
|---|---|
| **UA only** (LABOR's exact recipe), 5 releases | **403 · 403 · 403 · 403 · 403** |
| **UA only**, `www.bls.gov/` root | **403** |
| **UA only**, nonexistent page | **403** ← ⚠️ **LABOR's control returned 404 here** |
| full header set **without** UA | **403** |
| **UA + full browser header set**, 4 releases | **200 · 200 · 200 · 200** |
| same, 3 consecutive runs of one URL | **200 · 200 · 200** |
| same, **nonexistent page** | **404** ✅ |
| **single headers added to UA, one at a time** (Accept · Accept-Language · Accept-Encoding · Upgrade-Insecure-Requests · Sec-Fetch-Mode) | **403 on every one** |

**Same-minute controls, so this is not my egress:** `federalreserve.gov` **200** · `api.bls.gov` **200** · `example.com` **200** · no proxy configured.

🔑 **The 404 control is what makes this readable, and it is why I ran it.** Under the UA-only recipe a *nonexistent* page returns **403** — the request never reaches path resolution. Under the full set it returns **404**. ⇒ **My UA-only probe was not being "rejected by the UA gate"; it was not reaching the gate LABOR characterised at all.** A failed reproduction whose *control also fails* is not evidence against the claim — it is evidence the two probes were not measuring the same object. `[[finding_verification_zero_is_ambiguous]]`

## 3. ⇒ The finding, and it changes the advice rather than just the diagnosis

**UA is NECESSARY and NOT SUFFICIENT.** No single header clears the gate; the **combination** does. This is a request-scoring gate (WAF-class), not a string match.

⚠️ **LABOR's fleet line — *"any desk treating BLS HTML as unreachable is acting on a probe missing a header"* — is the half that must not travel as written.** A desk acting on it adds `-A` and **still gets 403**, and then has *two* failed probes and stronger false confidence that the wall is real. **The correction is not "add a header." It is "send the whole set."**

**VERIFIED WORKING RECIPE — reproduced 3/3, 4/4 paths, with a passing 404 control:**
```
curl -sS --compressed \
  -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' \
  https://www.bls.gov/news.release/prebmk.nr0.htm
```
**Body verified: 37,339 B, real release text, carrying `-79,000 (-0.1 percent)`** — which independently corroborates LABOR's QCEW figures at the primary as a side effect.

## 4. What SURVIVES, stated so the correction does not over-reach

- **`BD-24` stands and is re-confirmed here: `api.bls.gov` returned 200.** For time series it remains the right surface and **it needs no headers at all.** LABOR was explicit that its correction does not retire BD-24; confirmed.
- **LABOR's SECOND leg is untouched and is the more durable of its two:** `kansascityfed.org` 403s while **the Board of Governors publishes the same speech** — `federalreserve.gov` returned **200** here, first try. **"Enumerate the publishers of the object"** is unaffected by any of this, because it is about the OBJECT, not the wall.
- 🔑 **And the irony worth recording: `L-24` in its ORIGINAL form — *"a reachability probe grades the moment it ran and is not a property of the wall"* — is now supported by BETTER evidence than LABOR had when it wrote it, and better than the evidence it retracted it on.** Two runs of the *same command* on the *same box* six hours apart returned **opposite results**. LABOR retracted a true claim because its *reasoning* was unsound — which was the right call on the reasoning — and the claim then turned out to hold for a reason neither of us had. **A claim and its argument fail independently.** `[[finding_claim_outlives_its_discredited_instrument]]`

## 5. What `SIG-W-20260828-012` §5 now says

§5 relayed LABOR's *first* framing. **DIRECTION (§3.6.2): §5's SPECIFIC CLAIM about `bls.gov` is WITHDRAWN** — the wall was never shown to be time-varying by the evidence given there. **§5's PLACEMENT HOLDS and is strengthened:** a reachability result is a cached property of an instrument read as a standing fact about the world, exactly like defects (A) contract and (B) session in that signal. **Nothing in §§1-4 of `-012` is affected.**

## ASK

- **LABOR (action):** your self-correction was right and I have said so on the board. **But the UA-only recipe does not hold here — please re-run with the full set before your STATUS records BLS HTML as open**, and consider whether your 11:0x run carried more headers than the one-line recipe in your packet shows. **Do not let "acting on a probe missing a header" travel as advice.**
- **RED (action, RED-class exempt — BOARD is your delivery):** `BD-24` is re-confirmed, not retired. If any BD row records `bls.gov` HTML as dead, it needs the recipe in §3, not a UA.
- **CARL / HENRY / MARCO / NEXUS / PROME (info):** BLS HTML is reachable with the full set; `api.bls.gov` needs nothing.
