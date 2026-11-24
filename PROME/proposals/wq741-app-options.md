# WQ-741 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "741",
  "queue_terms_sha256": "eb5920bfad490d7d17df55498ee39bf309c5b45f5407d00f72176d53a7165248",
  "choices": [
    {
      "id": "A",
      "label": "Adopt the river rule, register both forecasts",
      "meaning": "AEOLUS adds 'European low water ended': Kaub daily mean at or above 77 cm on 10 complete days in a row, counted only while a low-water fire is the latest event. It also registers the water-board vote forecast (50%) and the Florida winter rain forecast (75%).",
      "consequence": "The rule would complete about 11/27. The rivers score stays 3 and no trigger moves."
    },
    {
      "id": "B",
      "label": "Adopt the river rule only",
      "meaning": "The rule is added as in A. The two forecasts stay proposed and unregistered.",
      "consequence": "Same as A for the river; nothing is scored on the two forecasts."
    },
    {
      "id": "C",
      "label": "Keep everything proposed",
      "meaning": "Nothing is adopted or registered.",
      "consequence": "The rivers exit stays ungradeable."
    }
  ],
  "recommended_choice_id": "A",
  "context": "AEOLUS's rule for ending the European rivers alarm needs a Rhine freight price that has no free source, so it cannot be graded. It offers a river-only rule in its place, and two forecasts.",
  "conditions": [
    "The rule says the river recovered, not the freight market: a carrier still lists low-water surcharges at Kaub 113 and 145 cm.",
    "Its record is 0 wrong of 3 calls (2003, 2018, 2022), a small sample.",
    "77 cm is the waterway authority's navigation reference; history does not single it out.",
    "The property-insurance exit stays not gradeable; AEOLUS withdrew its replacement.",
    "No money and no trade. Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
