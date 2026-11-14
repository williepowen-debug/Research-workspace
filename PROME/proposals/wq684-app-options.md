# WQ-684 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "684",
  "queue_terms_sha256": "8d9dd5b5a9a02e6a53481dfc41924eb5db89a6793e0523dcae9432e8845ae941",
  "choices": [
    {
      "id": "A",
      "label": "Title skim in WALTER's intake step",
      "meaning": "At each news batch WALTER reads the titles of the ordinary headlines as well as the alerts and review items, and makes a card only for a title that touches a held position, a live gate or a watched theme.",
      "consequence": "Catches any kind of story, not just kinds already named. Costs 5 to 10 minutes a batch on WALTER's estimate. WALTER edits its own intake step and PROME verifies. PROME checks on December 14 and drops the step without asking again if no card came from it."
    },
    {
      "id": "B",
      "label": "Add alert words to the collector",
      "meaning": "PROME adds free classifier terms for broad outages and bank-operations stories in the news collector, so those headlines arrive flagged as alerts.",
      "consequence": "No new step for WALTER. It catches only the kinds of story that are named: terms written after the Microsoft miss would not have caught the Ares remark."
    },
    {
      "id": "C",
      "label": "Accept the gap",
      "meaning": "Nothing changes; ordinary headlines stay unread.",
      "consequence": "No added cost and no new step. A story that the collector does not flag is found only if a bookmark, a desk or Will raises it."
    }
  ],
  "recommended_choice_id": "A",
  "context": "The news collector sorts each headline into alert, review item or ordinary. WALTER's intake step lists only alerts and review items, so ordinary headlines are marked as seen without being read. Twice in three days a story that mattered sat there: an Ares chief executive's remark on GPU values reached the board 13 days late (found November 11), and seven headlines on the November 12 Microsoft outage, American Banker's among them, were marked unread on November 13 until Will asked about the outage. The November 13 batch held 179 ordinary headlines. WALTER raised the question and adopted none of the options; it keeps routing meanwhile.",
  "conditions": [
    "A is a new standing step. Will's October 31 word asks for a concrete recurring miss and his word before one is added; this is two misses in three days.",
    "Titles only: a story whose title does not show why it matters still slips under A.",
    "A and B both work only when a WALTER session runs; nothing is read while no window is open.",
    "The 5 to 10 minutes is WALTER's estimate, not measured.",
    "No money, position, card, gate or other desk's rule is touched.",
    "The follow-up card on the Microsoft outage itself is a separate item that WALTER holds for Will's go; this decision does not route it.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
