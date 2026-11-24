# WQ-743 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "743",
  "queue_terms_sha256": "484b83d9fbae5e7a19cd9f9fb346590a4d2738a17d154968aaa1199d40c29a1a",
  "choices": [
    {
      "id": "A",
      "label": "Read it at the first print",
      "meaning": "AEO-17 is graded on the first October to December print of the El Nino strength index, expected early January 2027. No verdict only if nothing prints by 2027-01-20. The 2.50 threshold, the branches and the 40% stay as registered.",
      "consequence": "The forecast gets a real grade in January instead of lapsing."
    },
    {
      "id": "B",
      "label": "Leave it; no verdict on 12/20",
      "meaning": "The forecast's wording stays. With no print possible by 12/20, it closes with no verdict.",
      "consequence": "AEOLUS's 40% call is never scored."
    }
  ],
  "recommended_choice_id": "A",
  "context": "AEOLUS registered this forecast on 11/06 expecting the index to print about 12/07. The index prints about five days after the season ends, so the first print is early January, after the forecast's 12/20 cut-off.",
  "conditions": [
    "The change is made after later information: on 11/12 the forecasters cut their own odds of this outcome to about 60%. AEOLUS's 40% is not changed.",
    "No October to December value has printed; the result is unknown to everyone.",
    "Your 2026-08-27 class ruling says a lagged series is graded when its named observation publishes; this is the same idea applied to an explicit cut-off date.",
    "No money and no trade. Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
