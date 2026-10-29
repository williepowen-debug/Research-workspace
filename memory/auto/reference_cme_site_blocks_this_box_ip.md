---
name: reference-cme-site-blocks-this-box-ip
description: "cmegroup.com returns HTTP 403 with an explicit 'IP address is blocked due to suspected web scraping' terms-of-use message to Will's box (first seen 2026-10-28 23:49 ET). CME settlement bulletins and the settlements JSON are unavailable from here; do not try to evade the block."
symptoms: "CME bulletin PDF download is a 602-byte JSON; pdfminer 'No /Root object'; Section61 fetch 403; CmeWS settlements endpoint 403; source (1) settlement missing for every date"
metadata:
  type: reference
---

**Fact (BRENT, 2026-10-28 23:49 ET, two independent desks hit it the same hour):** every `cmegroup.com` request from this machine (daily-bulletin PDFs and `CmeWS` settlements JSON) returns HTTP 403 with a JSON body: "This IP address is blocked due to suspected web scraping activity ... strictly prohibited by CME Group's website Data Terms of Use ... contact gcc@cmegroup.com." Saved body: `AGENTS/BRENT/research/2026-10-28_eia-oct28/cme-block-response-2026-10-28T2349.json`.

**Why it matters:** WQ-420 source (1) and every other "CME official settlement" step fail here. The October 23 bulletin was readable on 10/26, so the block started between then and 10/28.

**How to apply:** do not rotate user agents, proxies or headers to get around it (terms of use). Use the letter's fallbacks: vendor daily rows accepted against the settlement-window proxy, wire-reported settles labelled EST, or Will's broker. Unblocking is Will's/PROME's call (contact CME GCC or use a licensed feed). Related: [[finding_negative_reachability_is_a_claim_about_your_request]] — this one IS a real refusal, and its message says so.
