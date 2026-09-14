---
signal_id: SIG-W-20260914-008
date: 2026-09-14
timestamp: 2026-09-14T17:52:03Z
time_dispatched: 2026-09-14T17:52:03Z
source: WALTER
origin: "Will desktop drop-zone inbox/WILL/IMG_2381.PNG + IMG_2378.PNG (batch BM-20260914-02 items 1 and 4) — @KobeissiLetter X post 10:23 ET 2026-09-14 and @nytimes X post 11:09 ET 2026-09-14, same underlying event. The 10Y leg was already carried in SIG-W-20260914-003; the MORTGAGE leg is new and conflicts with our own lane figure."
domain: HOUSING
cluster: CONSUMER_STAGFLATION
precedence: PRIORITY
action: ["HOMER"]
info: ["CORAL", "REGINALD", "CARL", "BOND", "MARCO", "LIQUID", "RED", "TERRY", "PROME"]
entities: ["MORTGAGE30US", "Freddie-Mac-PMMS", "Mortgage-News-Daily", "US-10Y-Treasury", "Kobeissi-Letter", "New-York-Times"]
confidence: 0.55
confidence_language: the-10Y-leg-is-CONFIRMED-at-a-tier-1-primary; the-MORTGAGE-claim-is-an-aggregator-assertion-that-CONFLICTS-with-our-own-most-recent-print-and-is-NOT-resolved-here
signal_type: data-conflict
resources: 1
safety_net: clear
word_count: 420
verdict: "TWO SCREENSHOTS, ONE EVENT, AND ONE GENUINELY NEW LEG. The 10Y breaching 5.00pct is CONFIRMED at the NYT and was already carried as tape context in SIG-W-20260914-003 -- the NYT copy upgrades its sourcing and it is annotated there, not re-dispatched. THE NEW AND UNRESOLVED CLAIM IS KOBEISSI'S 'US mortgage rates are back above 7pct'. OUR OWN MOST RECENT FIGURE IS MORTGAGE30US 6.76pct, carried orange in the RESEARCH-INTAKE lane. Those are not necessarily in conflict and that is the entire point: MORTGAGE30US is Freddie Mac's PMMS, a WEEKLY survey printing Thursdays, while the daily trade series move with the 10Y and can sit well above a lagging weekly print. WALTER holds no daily mortgage series and did NOT derive a proxy. HOMER owns the series question; this is routed so the number does not travel with no basis attached."
---

# "Mortgage rates back above 7%" against our own 6.76% print — name the series before anyone carries either

## The two screenshots are one event, and it is already ours

**@nytimes, 11:09 ET 9/14:** *"The 10-year Treasury yield… breached 5% for the first time in years, capping a long stretch of turmoil in the bond market that has pushed up borrowing costs for companies and consumers."*
**@KobeissiLetter, 10:23 ET 9/14:** same event, with a TradingView chart reading **C 5.004%, +0.250 (+5.26%)**, O 4.764 / H 5.004 / L 4.732.

✅ **The 10Y leg was ALREADY DISPATCHED today** in `SIG-W-20260914-003` as tape context (*"10Y at/near 5.00%, highest since October 2023"*). **The NYT copy upgrades the sourcing from an aggregator to a tier-1 primary, so it is ANNOTATED ADDITIVELY on `-003` rather than re-dispatched.** ⚠️ **The Kobeissi chart candle shows a +0.250 move — do NOT read that as a single-session change without establishing the candle's interval; it is not stated on the screenshot and I did not resolve it.**

## 🔴 The new leg, and it disagrees with our own board

**Kobeissi: *"US mortgage rates are back above 7%."***
**Our own most recent figure: `MORTGAGE30US` 6.76%, carried ORANGE in the RESEARCH-INTAKE lane.**

⛔ **DO NOT RESOLVE THIS BY PICKING THE ONE YOU LIKE. They may both be correct, and the reason is the basis:**

| Series | What it is | Cadence |
|---|---|---|
| **`MORTGAGE30US`** | Freddie Mac **PMMS survey** | **WEEKLY, prints Thursday** |
| Daily trade series (e.g. Mortgage News Daily) | lender rate sheets | **DAILY** |

🔑 **With the 10Y going ~4.77 [9/3] → 4.95 [9/10] → ~5.00 [9/14], a DAILY series can sit above 7% while a WEEKLY survey still reads 6.76% from its last Thursday print. That is a LAG, not a contradiction — and reporting either number without naming its series manufactures a disagreement that does not exist.**

📌 This is `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` with the sign flipped: **an apparent CONFLICT between two readings that are both fine once you name the instrument.** Same shape as this morning's `RED-FT-08`-vs-sell-side-consensus item.

⛔ **WALTER holds NO daily mortgage series and did NOT build a proxy.** I am not grading which is right.

## Requested action

- **HOMER** — **housing is yours and so is this call.** Three things only you can settle: **(a) which series is Kobeissi quoting**, and is >7% true on it today; **(b) when does `MORTGAGE30US` next print** and what does the 10Y move imply for it; **(c) is there a level on either series that matters to your thesis**, or is this just the mechanical pass-through of a 5% 10Y? ⚠️ **If you carry a mortgage number anywhere downstream, carry its series name with it** — that is the whole reason this is a dispatch and not a log line.
- **CORAL** on `info:` — **Florida is a top-priority geography and a >7% mortgage rate bears on FL housing and affordability**, which is already a live thread in your enrollment/migration work.
- **REGINALD · CARL** on `info:` — bank mortgage books and consumer borrowing cost respectively.

⛔ **NOT ASSERTED:** that mortgage rates are above 7%; that they are not; the Kobeissi candle interval. **ESTABLISHED:** the 10Y breached 5.00% (NYT), and our own lane's most recent mortgage figure is 6.76% on a weekly survey basis.
