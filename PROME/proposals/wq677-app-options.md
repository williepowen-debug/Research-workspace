# WQ-677 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "677",
  "queue_terms_sha256": "bac590ee82ec0d54501e02b188fdcd16aa3197490d23d6bf475243aff32733cb",
  "choices": [
    {
      "id": "A",
      "label": "Approve the card as written",
      "meaning": "TERRY's card IDEA-NVDA-CEOGAP-NOV12 is approved exactly as written: one Nvidia Jan-15-2027 call spread, $10 wide, debit at most $4.00, enterable only on 11/18, 11/19 or 11/20 and only if all three entry conditions hold that day.",
      "consequence": "An entry still needs the 11/17 results to pass TERRY's test of VULCAN's written statement (outlook given and not lower, no cut stated), Nvidia below $163.60, a down day for Nvidia and a broker debit of $4.00 or less. The order is yours to place; nothing is executed by the app or by any desk. A fill would be against the closed X1 sizing gate, by your choice."
    },
    {
      "id": "B",
      "label": "Decide when it fires",
      "meaning": "The card stays NOT-FIRED and NOT approved. If its entry conditions are met on 11/18, 11/19 or 11/20, TERRY brings it back to you that day for a yes or no.",
      "consequence": "One more round trip on the day, with the results, the price and whatever is then known about why Huang left. If you are not reachable that day the entry is missed; the card expires at the 11/20 close."
    },
    {
      "id": "C",
      "label": "Decline the card",
      "meaning": "No Nvidia rebound card. TERRY records it as declined and does not bring it back.",
      "consequence": "No capital at risk. A new card would need a new finding."
    },
    {
      "id": "D",
      "label": "I'll say",
      "meaning": "You say in chat what you want changed or done.",
      "consequence": "PROME records your words; nothing is approved until you say it."
    }
  ],
  "recommended_choice_id": "B",
  "context": "Nvidia's 8-K (Item 5.02, accepted 2026-11-12 08:52 ET) says Jensen Huang resigned as President, CEO and director effective immediately; CFO Colette Kress is interim CEO; no reason is stated. Nvidia was about 11.7% lower before the open ($153.47, vendor quote 09:13 ET) after falling 28.6% over the prior 65 sessions. TERRY proposes no short (a put now is a chase) and one rebound card to be entered only after the 11/17 results: buy one Nvidia Jan-15-2027 call spread, $10 wide, paying at most $4.00, so the most it can lose is $400 plus fees. It can be entered only on 11/18, 11/19 or 11/20 and only if the results pass TERRY's test of VULCAN's written statement of what the 11/17 release and CFO commentary say (a next-quarter revenue outlook is given with its midpoint at or above this quarter's actual revenue, no data-center cut is stated, and no order cut, deferral, slowdown or customer change is stated; a withheld or lower outlook, or any stated cut, voids the card), Nvidia is below $163.60 and Nvidia is down on the day. Take profit at a spread bid of $7.00; exit if Nvidia closes below the 11/12 session low. TERRY's own odds that the entry conditions are ever met: 0.15, subjective (lowered from 0.20 when the first condition was reworded).",
  "conditions": [
    "The cause of the resignation is not stated by Nvidia. A legal, regulatory or export liability surfacing after a fill is the tail this card does not survive cheaply; the loss is capped at the debit, at most $400 plus fees. The card is void before entry on any such disclosure.",
    "Passing the results test means no cut was STATED in the release and CFO commentary, not that there was no damage. VULCAN states what the documents say and grades nothing; TERRY applies the test.",
    "The stock was already falling hard before the news, so the overreaction read may be wrong, and no desk owns that view: the overreaction read is TERRY's own.",
    "This is the same bet as the unapproved QQQ Dec-18 670/680 call card (a tech rebound), not a second independent one.",
    "The X1 sizing gate is CLOSED (don't size). A fill would be against it; that is Will's choice per card and is never pre-approved.",
    "Root rule #5: Will approves; TERRY never executes; the order is Will's. Every app answer needs Will's confirming word in PROME's chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
