# WQ-690 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "690",
  "queue_terms_sha256": "71304fa6a82a9621115a83b7df62574927ae4a497e5e4130c8f5b6660f051d12",
  "choices": [
    {
      "id": "A",
      "label": "Under 2 reads as orange, unqualified",
      "meaning": "CORAL amends its band wording between tests so that any score below 2 of 6 keeps the Florida thesis at orange with no qualifier.",
      "consequence": "Closes the gap. No colour changes; the August and November scores of 1.5 both read as plain orange."
    },
    {
      "id": "B",
      "label": "Leave the bands as written",
      "meaning": "No amendment. A half-point score stays outside the written bands and CORAL says so each time.",
      "consequence": "Nothing changes today, since both neighbouring bands hold orange. The gap stays and would need a ruling on the day it matters."
    },
    {
      "id": "C",
      "label": "Round a half up",
      "meaning": "A score of 1.5 is read in the 2-to-3 band: hold orange and name which criteria passed.",
      "consequence": "Same colour, slightly more reporting. It treats a half-met criterion as met for banding, which is more generous to the 'thesis is wrong' side."
    }
  ],
  "recommended_choice_id": "A",
  "context": "CORAL's Florida stress thesis carries six pre-registered tests of whether the thesis is wrong. The test due November 15 ran November 16 and scored 1.5 of 6, the same as in August: the bank side mostly held (one criterion met, one half met because bad loans rose at BankUnited and USCB), and none of the four household-side tests passed. The thesis stays at orange. CORAL's written bands cover scores of 1 or fewer and 2 to 3, not 1.5.",
  "conditions": [
    "No colour, gate, threshold or trade changes under any option.",
    "One of the six tests could not be fully graded: Florida foreclosure data has not been refreshed since July 17, so 'condo prices steadied without forced sales' is unconfirmed; CORAL graded it not met.",
    "The tax-relief test ran on unofficial election returns; certification is November 17.",
    "A change to a desk's pre-registered band is Will's decision; CORAL applied nothing.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
