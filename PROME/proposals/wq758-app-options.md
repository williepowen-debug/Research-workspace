# WQ-758 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "758",
  "queue_terms_sha256": "967fd2a1b9e13df9e9427cadb441fb3c3c06da7e0965f8878e9266fc302944de",
  "choices": [
    {
      "id": "A",
      "label": "Adopt the number on file",
      "meaning": "The gold kill line fires only on a certified gold settlement under $3,317 with the 10-year real yield under 2.6%. This is the only definition ever written for the clause, in MIDAS's thesis file.",
      "consequence": "MIDAS writes it into its kill table. If gold fell under $3,317 while the real yield stayed at 2.6% or higher, the thesis would not be killed by that fall; MIDAS would read it as rate-driven. Nothing changes today."
    },
    {
      "id": "B",
      "label": "Have MIDAS write a new definition",
      "meaning": "MIDAS drafts what counts as a major real-yield spike (for example a rise of so many basis points over so many weeks) and brings it back to you.",
      "consequence": "The clause stays undefined until you rule on the draft. MIDAS cannot grade the line in the meantime, which matters only if gold falls about 7% or more first."
    },
    {
      "id": "C",
      "label": "Drop the clause",
      "meaning": "The kill line becomes a certified gold settlement under $3,317, with no condition on real yields.",
      "consequence": "Simpler and stricter: any fall through $3,317 kills the thesis, including one caused by rising real yields. This changes the rule as written; neither MIDAS nor PROME recommends it."
    }
  ],
  "recommended_choice_id": "A",
  "context": "MIDAS's gold kill line reads: gold under $3,317 without a major real-yield spike. The spike clause was never defined except by one legacy number in the thesis file, real 10-year yield below 2.6%. A process check (DAEDALUS run 5) flagged that the clause has two readings. Gold is about 7% above the line and the real yield was 2.73% on 11/25, so no choice changes anything today.",
  "conditions": [
    "$0. No trade. No choice changes any score or view today.",
    "Gold levels are vendor reads, not certified settlements; MIDAS has no certified settlement source, which is a separate open item.",
    "Under A the line cannot fire while the real yield is 2.6% or higher, whatever gold does.",
    "MIDAS's three-month view on GLD went to neutral today on a different rule and does not depend on this.",
    "Not urgent."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
