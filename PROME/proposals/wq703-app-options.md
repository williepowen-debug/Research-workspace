# WQ-703 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "703",
  "queue_terms_sha256": "da971064d708760fd5f7562e85bec15934f5acccaf59f5e380bb3c3d7019f368",
  "choices": [
    {
      "id": "A",
      "label": "My word covers the list PROME reads back",
      "meaning": "When you tell PROME to start desks on work, it reads back in chat each desk and what it will be asked to do, then launches exactly that list, whether or not a dated row is due. The read-back is saved in the launch log. The word lasts for that sitting only.",
      "consequence": "The rule matches what you already do. The due-rows-only limit on your own word goes away; PROME's own launches without your word keep their existing limits."
    },
    {
      "id": "B",
      "label": "Keep it to rows already due",
      "meaning": "Your blanket word covers only desks whose dated row is due. Anything else PROME brings to you as a proposal, and you say yes to that list.",
      "consequence": "A tighter rule and one more exchange each time you ask for work that has no due row, as on 11/16."
    },
    {
      "id": "C",
      "label": "Only the words launch or wake count",
      "meaning": "A blanket launch word must use the word launch or wake. General phrases such as start working on these are treated as a request for a proposal.",
      "consequence": "Least ambiguity about what you meant, most back-and-forth."
    }
  ],
  "recommended_choice_id": "A",
  "context": "On 11/10 you ruled (WQ-661 A) that when you give a blanket word to launch desks, PROME first lists each desk and its due row in chat, limits the launch to rows already due, and the word lasts for that boot only. Since then your words have been wider than that rule. On 11/16 at 13:45 ET you said: Id like to go back to your findings and start working on these, and PROME started four desks that had no due row. An outside audit on 11/16 asked that the term be defined and that you say whether such a phrase counts and whether it may reach past due rows.",
  "conditions": [
    "Choice A changes one sentence of PROME's own charter; it gets one blind read before and one after.",
    "Laptop memory still limits how many desks run at once.",
    "PROME's launches without your word keep their existing tiers and limits under every choice.",
    "The audit also cites 11/8; PROME checked only the 11/16 instance.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
