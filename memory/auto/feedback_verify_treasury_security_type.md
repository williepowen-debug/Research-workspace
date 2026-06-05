---
name: verify-treasury-security-type
description: "Treasury's \"term\" field collapses TIPS and nominal notes under the same label (e.g., \"10-Year\"); always verify securityType / CUSIP family before scheduling matrix tests or auction-event-conditional rules"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a696a8de-98a8-4d0a-9f0b-22aca634910d
---

When scheduling any decision rule, matrix test, or agent work around a Treasury auction event, **verify the underlying security type before locking the calendar.** Treasury's announced-auction data uses a "term" field (e.g., `"10-Year"`) that collapses **TIPS and nominal notes** under the same label. The TreasuryDirect API and the announcement schedule both show this collapse — only the `securityType` field (`"Note"` vs `"TIPS-Note"`) and the CUSIP family distinguish them:

- Nominal 10-Year Note family: **`91282CQ*`** (e.g., `91282CQQ7` = 5/12/26 new issue)
- 10-Year TIPS family: **`91282CP*`** (e.g., `91282CPU9` = 5/21/26 reopening, actually "9-Year 8-Month TIPS")

The auction press-release PDF header is authoritative — it spells out "9-Year 8-Month TIPS" vs "10-Year Note" explicitly.

**Why:** *Caught 5/21/26 in real time. I built a matrix-Q4 conditional rule around BOND's "1pm 10Y reopening today" assuming nominal — Treasury's schedule confirmed `"Term: 10-Year"`. The underlying security was actually a TIPS reopening (CUSIP 91282CPU9, "9-Year 8-Month TIPS"). BOND's matrix v1/v2 thresholds (BTC <2.30, dealer >12%, indirect <55%) are calibrated on nominal note demand statistics and are not comparable to TIPS bidder dynamics. The whole pre-auction briefing and dual-grade-format ask was misdirected. The matrix Q4 deferral became a real reschedule (to ~June 10-12 next nominal 10Y reopening) and BOND's careful pre-auction baseline + sentiment-context-lens work had to be repurposed for the wrong test. A web search result earlier in the day had actually correctly identified the security as TIPS, but I dismissed it because the structured Treasury data field said "10-Year" — should have trusted the spelled-out description over the term-classification field.*

**How to apply:**

1. **Whenever scheduling agent work or decision rules around a Treasury auction date:** before locking the calendar, run:
   ```
   curl -s "https://www.treasurydirect.gov/TA_WS/securities/announced?format=json" \
     | python3 -c "<filter by date>; print(term, cusip, securityType)"
   ```
   and verify `securityType` is `"Note"` (or `"Bill"`, `"Bond"`, `"FRN"`) — NOT `"TIPS-Note"` — for nominal threshold-matrix use.

2. **CUSIP family as quick distinguishing tell:** `91282CQ*` = nominal note (recent vintage); `91282CP*` = TIPS family (recent vintage); `912810U*` = bonds (30Y/20Y). When a CUSIP doesn't match the family you expect for the term-class, that's the red flag.

3. **Authoritative source = the press-release PDF header.** Once an auction prints, the PDF at `https://www.treasurydirect.gov/instit/annceresult/press/preanre/YYYY/R_YYYYMMDD_N.pdf` spells out the security type in plain English in its first table header (e.g., "9-Year 8-Month TIPS" vs "10-Year Note"). Confirm against this before propagating any matrix-grade framing.

4. **If you have any uncertainty:** ask the domain agent (BOND) to verify the security type before you commit to the framing in any cross-agent brief. Better to ask once than to misdirect a full pre-auction cycle.

5. **When briefing domain agents about an upcoming auction:** include the CUSIP and explicitly say "nominal note" or "TIPS reopening" — never just "10-Year reopening" without security-type qualifier. The qualifier is cheap; the misframing is expensive.

**Cross-references:** [[verify-counts-before-propagating]] — same family of error (stating a fact across files without verifying ground truth first). [[behavior-language-over-hash-pinning]] — relatedly, "10-Year reopening today" is a behavior reference that decays when the underlying security changes; security-type qualifier makes the reference durable.
