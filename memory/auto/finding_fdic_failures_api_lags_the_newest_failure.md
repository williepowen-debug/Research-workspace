---
name: finding_fdic_failures_api_lags_the_newest_failure
description: "The FDIC failures API lags the most-recent bank failure by roughly a week, and the HTML Failed Bank List under-reports if you read one page — no naive read of either source returns the true 2026 count"
metadata:
  node_type: memory
  type: reference
symptoms: "FDIC API returns fewer bank failures than actually happened; BankFind missing the newest failure; bank failure count disagrees with the newswire; failed bank list shows only 2 for the year; api.fdic.gov/banks/failures FAILYR filter looks wrong; banks.data.fdic.gov returns Moved Permanently; resolving a bank-failure prediction market off the FDIC list"
---

**Measured 2026-08-28 (WALTER, own pulls, with controls).** Ground truth for 2026 YTD was **5** bank failures. Neither FDIC surface returns 5 on a naive read:

| source | returns | why |
|---|---|---|
| `https://api.fdic.gov/banks/failures?filters=FAILYR:2026` | **4** | **Tioga-Franklin Savings Bank (Philadelphia, closed 2026-08-21) was ABSENT seven days after closure.** The API lags the newest failure. |
| FDIC HTML **Failed Bank List**, single fetch | **2** | The list is **paginated**; one fetch sees page 1. |
| Newswire / FDIC press releases | **5** | American Banker, Banking Dive, ABA Banking Journal all call Tioga-Franklin "the fifth bank to fail this year." |

**Controls run:** `FAILYR:2025` → 2 (plausible); unfiltered → 4,117 back to 1934. **The index is populated and the filter works** — this is a *recency lag*, not an empty index.

⚠️ **`banks.data.fdic.gov/api/failures` is DEAD** — it returns **HTTP 301** with a plain-text body `Moved Permanently. Redirecting to https://api.fdic.gov/banks/failures…`. A client that does not follow redirects gets that string, and a JSON parser raises `JSONDecodeError` on it. **Use `api.fdic.gov/banks/failures` and follow redirects.**

**How to apply.** For a *complete* current-year failure count, use **the HTML list AND page through it**, or the API **plus** the newest FDIC press releases. For anything resolving on the official list — including prediction markets that name the "Failed Bank List" as their resolution source — **the API view can be a week behind, so a YES can be true and unresolvable for days.**

🔑 **The failure mode is a clean-looking false negative in the reassuring direction.** The query succeeds, returns valid JSON, and undercounts. Nothing in the response says the newest row is missing — so a desk checking "has another bank failed?" gets "no" with no error to notice. `[[finding_verification_zero_is_ambiguous]]` · `[[finding_instrument_reports_clean_against_the_wrong_reference]]`

⚠️ **Provenance worth keeping, because the first version of this finding was wrong.** It began as a peer's report that the API returned `total:0` with the index "not populated." That did **not** reproduce — the observed value was 4 — and the peer retracted it on discovering it could not re-derive the command behind it. **A finding relayed as prose without its command is a rumour with a number in it** (`[[finding_loadbearing_number_must_be_reproducible]]`). The lag above is the part that survived an independent run.

Related: [[finding_fdic_securities_filings_api]] — a *different* FDIC API (`securitiesfilings.fdicconnect.fdic.gov`, filings/Form 4), same agency, do not confuse them. [[finding_edgar_403_user_agent_header]] — gov-data API family.
