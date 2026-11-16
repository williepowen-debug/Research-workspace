# WQ-689 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "689",
  "queue_terms_sha256": "1819faaddb3a452867a69d8bb3eb173a5eff2b08920cf92ee07dd6eb5029d88e",
  "choices": [
    {
      "id": "A",
      "label": "Keep everything as is",
      "meaning": "S5 stays a core channel with its 'partly independent' label; the missed test is noted in VULCAN's record.",
      "consequence": "No change to how the fleet reads S5. The label keeps a claim that its own quarter-long test did not support."
    },
    {
      "id": "B",
      "label": "Relabel only",
      "meaning": "S5 keeps its score of 4 and its core status, but its independence label changes from 'partly independent' to 'independence unsupported this quarter', so it is read together with the capex channel (S1) rather than as a separate alarm. VULCAN registers a successor test on the same letter, nothing widened, for the window to 2027-02-15.",
      "consequence": "The label matches the evidence. No score, band or trigger moves. If the successor test hits, the label can be restored on Will's word."
    },
    {
      "id": "C",
      "label": "Demote S5 to tier-2",
      "meaning": "S5 leaves the core channels.",
      "consequence": "A larger change than the evidence requires on VULCAN's reading: the score of 4 rests on two fired events (the Firmus withdrawal and Volta), not on the claim that missed."
    }
  ],
  "recommended_choice_id": "B",
  "context": "VULCAN tracks AI-infrastructure stress in channels. S5, the financing channel, was promoted to core on August 3 on one claim: financing terms can tighten while AI capital spending is still rising, so S5 can warn on its own clock. VULCAN registered a test of that claim (VULCAN-13) for August 21 to November 15. On November 16 VULCAN graded it MISS: capex was not cut, and no qualifying new case appeared on any of the three legs as written (a regulator-mandated collateral rule outside Wisconsin, a like-for-like repricing of 50 basis points or more, a covenant or structure tightening against the same borrower's own predecessor). The test's registered consequence is this question to Will.",
  "conditions": [
    "Nothing changes until Will rules; no score moves under any option without his word.",
    "The closest case was not counted: IREN's newer GPU loan put the parent fully on the hook (full parent guaranty, parent debt restriction, cross-default) where the older Microsoft-backed loan had limited parent guarantees. VULCAN excluded it because it is a different borrower and credit, the same exclusion it applied twice before. A reader could reasonably count it, which would turn the MISS into a HIT.",
    "The grade was made one day late (no session ran November 14 or 15).",
    "No money, position, card or other desk's rule is touched.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
