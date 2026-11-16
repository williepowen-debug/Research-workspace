# WQ-691 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "691",
  "queue_terms_sha256": "0b9a5a133eb3d835c34fd35e3d0d973c21f45413a5fc1c7afdf1df681948655f",
  "choices": [
    {
      "id": "A",
      "label": "A downgrade candidate needs a full 4",
      "meaning": "CORAL amends its band wording between tests so that any score from 2 up to but below 4 of 6 holds the Florida thesis at orange and names which criteria were met or half met.",
      "consequence": "Closes the gap. A score of 3.5 holds orange; you would still see it, because CORAL names every criterion met or half met."
    },
    {
      "id": "B",
      "label": "Leave the bands as written",
      "meaning": "No amendment. A score of 3.5 stays outside the written bands.",
      "consequence": "Nothing changes today. If a test ever scores 3.5, the reading would be ruled on that day, after the score is known."
    },
    {
      "id": "C",
      "label": "Round a half up",
      "meaning": "A score of 3.5 is read in the 4-or-more band: a candidate to move from orange to yellow, brought to you.",
      "consequence": "A 3.5 would come to you as a downgrade candidate. Nothing moves without your word either way; this is more generous to the 'thesis is wrong' side."
    }
  ],
  "recommended_choice_id": "A",
  "context": "CORAL's Florida stress thesis carries six pre-registered tests of whether the thesis is wrong, with half points allowed. Its bands read: 4 or more met, a candidate to move from orange to yellow, brought to Will; 2 to 3 met, hold orange and name which; below 2, orange holds unqualified (amended by Will on November 16, row 690). A score of 3.5 falls between the top two bands. No test has scored 3.5; the August and November tests both scored 1.5. Unlike the gap closed in row 690, this one sits on the line that decides whether a downgrade is brought to Will. The next test is February 16, 2027.",
  "conditions": [
    "No colour, gate, threshold or trade changes today under any option.",
    "CORAL raised the gap on November 16 after encoding row 690 and proposed no answer; the recommendation is PROME's.",
    "A change to a desk's pre-registered band is Will's decision; CORAL applied nothing.",
    "The reason to rule now: a band set after a score exists is no longer pre-registered.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
