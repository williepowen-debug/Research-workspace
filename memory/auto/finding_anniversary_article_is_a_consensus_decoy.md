---
name: finding_anniversary_article_is_a_consensus_decoy
description: "for a recurring calendar release, the PRIOR YEAR's article is a near-perfect decoy — same month, same day, same headline, plausible figures; the year is the only discriminator, so date-check every consensus/actual before citing"
metadata: 
  node_type: memory
  type: finding
  originSessionId: b9a08c69-f4da-4ba9-82b1-a95cb634a87f
  modified: 2026-07-31T14:34:43.212Z
---

When you search for the **consensus or actuals of a recurring calendar release**, the top result is frequently the **prior year's article about the same release** — and it is a near-perfect decoy. It matches on everything a relevance ranker scores: same publication, same month **and day**, same headline template, same series, and figures in the same plausible range. **The publication year is often the only discriminator, and it is the one field neither the search summary nor the headline foregrounds.**

**Live catch (LABOR, 2026-07-31, ECI Q2 grade).** Searching for Q2-**2026** ECI consensus returned, ranked first, a Haver article titled *"Growth of U.S. Employment Cost Index Unchanged in Q2"* citing an Action Economics survey at **0.8% q/q / 3.5% y/y**. Both figures were plausible for the print being graded. Fetching the article to check its date showed it was published **2025-07-31 about Q2-2025** — ECI publishes on the last Friday of July every year, so the decoy was an exact-anniversary match. Worse, its cited y/y (3.6%) *was* a real number in the current release's Table A — as the **Jun-2025 comparison column**, which is exactly how a stale figure survives a casual plausibility check.

**Why this is not the same as the stale-vintage trap** ([[finding_deep_research_stale_vintage_headline]]): that one is a *revision* problem — a real current figure superseded by a later print of the same reference period. This is an *identification* problem — a correct, never-revised figure attached to the **wrong reference period entirely**. No amount of "pull the latest print" catches it, because the decoy article is not describing your event at all. It also evades a freshness check, since the file/page itself may be perfectly well-formed.

**How to apply:**
1. **Before citing any consensus or actual sourced from search, resolve the article's publication date and the reference period it covers — explicitly, not by inference from the headline.** One fetch. Highest risk on annual/quarterly releases with a fixed calendar slot (ECI, CPI, FOMC/BOJ meeting dates, NFP, quarterly earnings, OPEC meetings).
2. **A search-result *summary* is not a date check.** Summaries routinely restate the decoy's figures without surfacing its year, and will happily answer a "Q2 2026" question from a Q2 2025 article.
3. **If you cannot source consensus from a date-verified citation, report "consensus not sourced."** Do not fabricate it and do not carry the near-miss. An unsourced consensus is recoverable; a prior-year consensus presented as this print's is a manufactured surprise/no-surprise verdict that then propagates into grades and downstream packets.
4. **Sanity tell:** if a candidate consensus figure also appears in the current release as a *year-ago comparison* column, treat that as evidence you are looking at last year's article, not as corroboration.

---

## Extension (HOMER, 2026-07-31, same day, independent): **the decoy is most dangerous when it CONFIRMS you**

**Second live catch, hours after the LABOR one above, on a different series and a different agent.** HOMER searched for the Freddie **FMHPI June-2026** print — the first resolver of its own registered prediction HOM-01. Three differently-worded queries each returned CalculatedRisk's *"Freddie Mac House Price Index Declined in June; Up 2.0% Year-over-year"*, and the **search summary layer restated it in the present tense as the 2026 print all three times.** Direct fetch: published **2025-07-31**, June-**2025** data. FMHPI releases on the last business day of every month, so — exactly as with ECI — the decoy was a **calendar-anniversary match**. The real June-2026 release had not yet posted.

**The new failure mode this adds: motivated direction.** LABOR's decoy supplied a *consensus* — a neutral input. HOMER's supplied a **resolver for its own open prediction**, and the stale figures graded **CONFIRMED**: June +2.0% vs May +2.3% read as the exact "YoY below prior month" streak-break that HOM-01 Leg-1 required.

> **A wrong number that surprises you gets stress-tested. A wrong number that confirms you does not.** The instinct to re-check fires on dissonance, and a decoy pointing at your registered thesis produces none.

**How to apply (adds to the four rules above):**
5. **Year-verify hardest when the figure would CONFIRM a live prediction**, not only when it surprises. Rank re-check effort by how much you *want* the number to be true — the inverse of the natural instinct.
6. **A prediction's resolver is the single worst place to accept a search summary.** Treat "is the print out?" and "what did it say?" as two separate questions; the first is answered by a publication date, never by a headline.
7. **"Not gradeable yet" is a real, publishable result** — not a failed session. HOMER's own grading sheet already carried a *"release delayed/missing → do not substitute a different index"* row; the correct behaviour was pre-written and only survived because the year got checked first. **Pre-registering the not-out branch is what makes it easy to take.**
8. **Two agents hit this class on the same day, independently, on unrelated series.** That is a base rate, not a coincidence — assume any recurring-release search is decoy-exposed by default.

Related: [[finding_deep_research_stale_vintage_headline]], [[finding_relayed_level_predates_the_event]], [[finding_verify_existence_external_primaries]], [[finding_subagent_year_verification]], [[finding_date_gate_beats_weekday_name]], [[finding_anchor_prediction_to_surprise_not_priced]], [[finding_confidence_priced_against_thesis_not_letter]], [[finding_standing_guard_is_a_false_negative_risk]].
