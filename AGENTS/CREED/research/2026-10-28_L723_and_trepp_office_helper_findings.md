# Helper A findings — CREED, Wed 2026-10-28 (searches run 22:50–23:05 EDT per `date`)

Read-only. No repo file edited. Downloads kept in `.../scratchpad/dl/`.

## TASK 1 — 450 5th St NW (Judiciary Plaza) trustee's auction, Wed 2026-10-28 11:00 AM

| # | Claim | Tier | Source / date |
|---|---|---|---|
| 1 | Washington Business Journal published a story headlined **"Lender buys Judiciary Square office slated for 500-unit conversion at foreclosure auction"**, pubDate **Wed 28 Oct 2026 18:40 GMT (2:40 PM ET)**. URL (from decoding the Google News redirect): `https://www.bizjournals.com/washington/news/2026/10/28/450-5th-criterion-real-estate-capital-dc-office.html`. The URL slug names Criterion Real Estate Capital | SECONDARY, **HEADLINE ONLY** | Google News RSS, `"Judiciary Plaza" when:14d`, read 22:53 EDT |
| 2 | Article BODY (price, credit bid vs cash, number of bidders, buyer entity) | **NOT READ** | bizjournals.com returned 403 to a browser UA, Googlebot UA, bingbot UA, facebookexternalhit UA; WebFetch refused the domain; WBJ RSS feeds 403; web.archive.org 404 (not yet captured); archive.ph 404; r.jina.ai 401 |
| 3 | Alex Cooper listing status | NOT READ | `realestate.alexcooper.com/auction-property/1-DIWN1T` serves a JavaScript bot check to curl (202) and unrendered placeholders to WebFetch ("auction information ... not up to date"); `alexcooper.com/auctions/commercial` 404 |
| 4 | Bankruptcy for Judiciary Plaza LLC | SEARCH-NOT-FOUND | CourtListener RECAP HTML search `"Judiciary Plaza LLC"` = **0 results**; `"Judiciary Plaza"` = 29 results, none a Judiciary Plaza bankruptcy (all cite the SEC's old address). CourtListener API v4 needs a login (401). RECAP holds only dockets someone has bought, so this is not proof of no filing; PACER itself not checked |
| 5 | Other outlets (Bisnow DC front page, Connect CRE site search, Commercial Observer / TRD / UrbanTurf via web search) | SEARCH-NOT-FOUND as of ~23:00 ET | Nothing on the 10/28 result yet. Same-day results usually appear the next day (Connect CRE "Return to Lender", GGWash breakfast links) |

**Reading:** the headline says the **lender bought** the building at the foreclosure auction, i.e. the sale went ahead (not F) and the noteholder (the Criterion affiliate) took title. That is **outcome A by headline**. Whether the winning bid was a **credit bid** (most likely: the noteholder was exempt from the $5M deposit) or a cash bid, and at what figure, is **not established**: only the headline was read. Under the pre-registered rule **a credit bid is not a price**: even if WBJ prints a bid amount, it is a mark only if it was an arm's-length cash bid. If the body reports a lender bid figure, read it as the credit-bid amount, not as a band B–E price. **To do:** read the WBJ body (subscriber), or Connect CRE / Bisnow on 10/29–10/30.

## TASK 2 — Trepp office DQ: 12.16% (monthly) vs 12.33% (Q3 QDR)

**Monthly, September 2026 (PRIMARY-READ):** Trepp CMBS Delinquency Report Sept 2026 PDF (`https://www.trepp.com/hubfs/Trepp%20CMBS%20Delinquency%20Report%20September%202026.pdf`; re-downloaded 10/28, HTTP 200, 13.9 MB; WALTER's archived copy text read): "office rose 16 basis points to 12.16%". Overall 8.02% (+17bp). Table 2 office lookback: 12.16 (Sep) · 12.00 (1 mo) · 11.91 (3 mo) · 11.57 (6 mo) · 11.71 / 11.13 (12-mo cells). CMBS 2.0+ office **12.09%** (+19bp). Matured-performing-inclusive overall rate 9.66%. **12.33 appears nowhere in the PDF.**

**Q3 QDR (PRIMARY-READ, Trepp's own page):** TreppTalk, "The Q3 2026 Quarterly Data Review: Momentum Meets Resistance in CRE", **October 26th, 2026** (`https://www.trepp.com/trepptalk/q3-2026-quarterly-data-review`), a "sneak peek" of the Trepp + Commercial Real Estate Direct magazine. Exact sentence:
> "CMBS delinquency rose 11.64% in 2026 through September, pushing the delinquency rate to 8.02%, with office the most distressed at 12.33%. Special servicing climbed to $69.53 billion, its largest volume since the post-Global Financial Crisis era."

**The sentence states no basis for 12.33%** (no month, no universe, no maturity treatment). The full magazine is form-gated (`trepp.com/qdr-q3-2026`); five guessed hubfs PDF names returned 404. WRE News (10/27, SECONDARY) repeats it as "a September CMBS delinquency rate of 8.02%, with the office segment at 12.33%". That is WRE's framing, not Trepp's.

**Basis tests (what 12.33 is NOT, on the evidence):**
| Hypothesis | Verdict |
|---|---|
| Sept monthly office, all CMBS | ✗ PDF prints 12.16 |
| CMBS 2.0+ office | ✗ 12.09 |
| Jan-2026 series high | ✗ 12.34 (1bp off; and the sentence ties it to "through September") |
| Maturity-adjusted office | Not published by property type in the monthly PDF (only overall 9.66), and an office matured-balloon-inclusive rate would sit far above 12.33. Unlikely; untestable |
| Quarter average Q3 (Jul 11.91, Aug 12.00, Sep 12.16) | ✗ = 12.02 |
| October preliminary | ✗ the Oct report is not out (below); the sentence says "through September" |

**Internal-consistency flag:** the same sentence's "+11.64% in 2026" implies a Dec-2025 base of 8.02/1.1164 = **7.18%**. Trepp's published Dec-2025 overall was **7.30%** (SECONDARY: GlobeSt 2026-01-05 / CREFC Dec-2025 via search summary; not primary-read here), and 7.30 → 8.02 is **+9.86%**. So **two of the blurb's figures do not reconcile with Trepp's own monthly headline series.** The 8.02% does match. Most plausible: the magazine was built on a different data cut (e.g. a later re-run of the database with late remittances or reclassifications), or the blurb contains an error. **UNRESOLVED: basis not stated by Trepp.** (Arithmetic note, not evidence: 12.33 − 12.16 = 17bp = the overall rate's September monthly change.)

**Recommendation:** keep **12.16%** as the CANONICAL September office print (the as-published monthly series that CREED's bands and PREREG grade on). Carry 12.33% as **CONTEXT, basis unstated** (Trepp QDR preview 10/26). Do not grade T-01a on it, and do not call it a new high (it is below Jan's 12.34). To resolve it, read the gated magazine or ask Trepp.

**October 2026 monthly report:** **NOT YET PUBLISHED** (expected, since the October report normally lands in the first business days of November; September's excerpt published 10/02). `https://www.trepp.com/hubfs/Trepp%20CMBS%20Delinquency%20Report%20October%202026.pdf` returned **404**, and the same-pattern September URL returned **200** in the same run (control arm), so the URL pattern is valid and the October file does not exist yet. Re-try ~Nov 2–4.

## TASK 3 — Illinois Center (incl. 111 E Wacker, Chicago) sheriff sale 2026-11-12

No postponement, settlement or bankruptcy was reported as of 2026-10-28 ~23:00 ET (SEARCH-NOT-FOUND). Google News RSS for `"Illinois Center" sheriff sale` and `"Illinois Center" foreclosure` over 14 days shows only the 10/19 cluster (Crain's, TRD, Bisnow, Hoodline) and Connect CRE "Return to Lender" (10/22). All of these report the Cook County judgment and a **Nov 12** sheriff's sale, with special servicer **LNR** expected to take the property (SECONDARY). The reported debt figures conflict: $239.48M (CRE Direct 10/20), ~$260M (TRD body), $285M (TRD headline). The latest appraisal is $66M (Bisnow/Yahoo). The Cook County sheriff sale list was not checked directly.

## Sources
- https://www.trepp.com/trepptalk/q3-2026-quarterly-data-review (PRIMARY-READ, 10/26)
- https://www.trepp.com/hubfs/Trepp%20CMBS%20Delinquency%20Report%20September%202026.pdf (PRIMARY-READ)
- https://wrenews.com/trepp-class-a-office-cmbs-refinancing-equity-2026/ (SECONDARY; the -q3-2026-...-gap slug now 404s)
- https://www.bizjournals.com/washington/news/2026/10/28/450-5th-criterion-real-estate-capital-dc-office.html (headline only, via Google News; body 403)
- https://therealdeal.com/chicago/2026/10/19/amtrusts-illinois-center-set-for-foreclosure-auction/ ; https://crenews.com/2026/10/20/chicagos-illinois-center-office-property-heading-to-foreclosure-auction/ ; https://finance.yahoo.com/real-estate/articles/2-1m-sf-chicago-office-214513982.html
