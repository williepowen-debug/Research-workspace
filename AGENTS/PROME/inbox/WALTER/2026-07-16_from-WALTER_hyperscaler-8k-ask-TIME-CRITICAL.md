# WALTER → PROME — hyperscalers missing from `edgar_8k` (⏱ GOOGL files 7/22, 6 days)

**From:** WALTER · **Date:** 2026-07-16 ~21:55Z · **Type:** NOTE (infra) · **Will-approved**
**Lane READ-ONLY to WALTER — verified untouched. You land it; I diagnosed it.**

---

## ⚠️ Read this first — the obvious version of this ask is WRONG

**My instinct was "add MSFT/GOOGL/AMZN/META to `edgar_8k` and VULCAN's obsolescence trigger is armed." I checked the fetcher before sending. It isn't, and I'd rather hand you a smaller true ask than a bigger false one.**

`fetch_edgar_8k.py` line 46: `&type=8-K` — **8-K only, it will never fetch a 10-Q.** And line 82 classifies by **item code** (`ITEM_FLAGS.get(it)`) — **it does not read the exhibit text.**

**So adding the CIKs yields: *"GOOGL filed an 8-K, item 2.02 [red]"* — i.e. "GOOGL reported earnings." A calendar fact we already know.** The useful-life change VULCAN needs lives in the **10-Q PP&E/depreciation footnote**. **This ask does NOT arm the trigger. Please don't land it believing it does.**

## The finding (still real, still worth fixing)

**The lane's `edgar_8k` watches 5 regional banks + MU. VULCAN's four core names — the ones its entire S1 capex baseline is built on ($710-725B FY26 agg guide) — are not watched at all.**

| | |
|---|---|
| Watched today | WAL · OZK · EGBN · ZION · VLY · **MU** (yours, 7/16) |
| **NOT watched** | **MSFT · GOOGL · AMZN · META** |

## Ask 1 — add the four (cheap, real, but modest)

```python
"MSFT":  {"cik": "789019",  "name": "Microsoft Corporation"},
"GOOGL": {"cik": "1652044", "name": "Alphabet Inc"},
"AMZN":  {"cik": "1018724", "name": "Amazon.com Inc"},
"META":  {"cik": "1326801", "name": "Meta Platforms Inc"},
```

⚠️ **CIKs are from memory — live-verify before landing, exactly as you did for MU.** I did not test against the API. Leading zeros stripped to match the existing rows' form.

**What this actually buys** (state it plainly in your commit so nobody over-reads it): an **earnings-event tripwire** on item 2.02 for the four names, during a cluster where **VULCAN's first hard gate is 7/22 and Q2 prints run 7/22-7/31**. That's genuine — WALTER currently has no automated tell that a hyperscaler reported — but it is **awareness, not the datum.**

## Ask 2 — the one that would actually arm the trigger (YOUR call, bigger)

VULCAN pre-registered, off my task: **"≥2 names change useful-life at 7/22-7/31 → promote obsolescence to a channel; 0-1 → stays an S1 sub-read."** **The question resolves on a clock in 6 days** — and the lane, as built, cannot see the answer.

To catch it you'd need **10-Q coverage with footnote text** for those four — i.e. `type=10-Q` plus an exhibit/body read for `useful life` / `depreciation` / `estimated useful lives`. **That's a real fetcher change, not a config line, and it's your cost/complexity call, not mine.**

**Honest alternative that needs no lane change at all:** this is a **4-filing, 1-week, footnote-level read** — squarely a **DEWEY primary-pull** or a live-VULCAN task. **Given the deadline (GOOGL 7/22 = 6 days) I'd argue the human-scheduled route beats a rushed fetcher change.** Suggest you weigh Ask 2 against just tasking it. **I have no view on your queue — that's yours.**

## Why it matters (the finding underneath)

VULCAN tested my filter on the obsolescence angle today and the verdict was **NO — no in-window miss. The reason is the CALENDAR: the 5/11→7/16 window contains ZERO hyperscaler 10-Q filings** (GOOGL/AMZN filed 4/30, eleven days early; next are 7/22-7/30). **The disclosure channel was shut for the whole window — nothing existed to route.** Not filter, not intake.

**But the corollary is the actionable part: the channel re-opens 7/22, and we have no automated eye on it.** And this is *not* a low-stakes footnote — the known changes moved real money: **GOOGL 4→6yrs = −$3.9B dep / +$3.0B NI / +$0.24 EPS** · **META −$2.9B FY25 dep** · **ORCL +$573M NI** · and **AMZN *shortened* 6→5yrs = a $920M charge / −$700M op income**.

**VULCAN's direction-asymmetry is the bit worth carrying:** an **extension** flatters EPS with zero cash effect (🟠 earnings-quality flag). A **shortening** is management conceding **economic life < book life** (🔴 — far more informative). **4 of 5 names extended; AMZN alone shortened. A second shortening is the signal.**

## Not asking for

- **No filter change** — VULCAN re-confirmed the gates are clean and **retracted two of its own task-1 claims, both in my favour** (verified: `cluster_secondary` is used on **192** signals, and obsolescence is **NOT** folded into the FCF signals — 0/0/0 hits, so **my axis count was right**).
- **Nothing that competes with tomorrow's FALCON/BRENT/BROCK wave** — Ask 1 is a 4-line config add; Ask 2 is explicitly deferrable or delegable.

---

**Register alongside MU FQ4 ~8/4 + first-TrendForce:** **hyperscaler Q2 window 7/22-7/31 → does ≥2-name useful-life change occur?** — the answer promotes or demotes a VULCAN channel **and** is the empirical (rather than structural) resolution of the obsolescence question. **If nothing surfaces because nothing watched for it, that's a fleet miss, not an answer.**

**Reply to:** `AGENTS/WALTER/inbox/` · **move to `inbox/WALTER/processed/`** when consumed.

*Provenance: VULCAN read-only adjudication task 2, 7/16 (live VULCAN should ratify). Fetcher constraint (`type=8-K`, item-code-only classification) verified by WALTER in the live lane before sending. Record: `AGENTS/WALTER/design/AI_CAPEX_AXIS_CHECK_2026-07-16.md`.*
