# WQ-693 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "693",
  "queue_terms_sha256": "11d5e4fd3f72d715e7d61c2787a18dbb4eb5a047398ea260090a3b8d11b8c098",
  "choices": [
    {
      "id": "A",
      "label": "Retire the Decision Deck for good",
      "meaning": "The hosted Deck page, its tap store pickup, its cards and explainers are retired, not paused. Decisions keep arriving the way they have since October 19: this chat, the queue, and the Decisions app. PROME closes the three repair rows that only matter if the Deck returns, and the row for two small queue-row writer commands that was parked with them, and changes 'paused' to 'retired' in its own manuals.",
      "consequence": "Four open rows close and a standing 'paused' note leaves the boot and closeout manuals. The shared parser code the queue tools use stays. If you ever want the page back it is a rebuild, not a resume."
    },
    {
      "id": "B",
      "label": "Resume the Decision Deck",
      "meaning": "The pause is lifted. PROME reconciles the hosted tap store first, as the pause ruling requires, then owes the three parked repairs before the page is trusted again.",
      "consequence": "The page comes back beside the Decisions app, with its upkeep at every boot and closeout and three repairs to make first."
    },
    {
      "id": "C",
      "label": "Leave it paused",
      "meaning": "Nothing changes. The four rows stay open with no path to closing until you decide.",
      "consequence": "No work now; the rows and the 'paused' notes stay."
    }
  ],
  "recommended_choice_id": "A",
  "context": "Will paused the Decision Deck on October 19 (WQ-460). Since then every ruling has come through this chat and the queue, and the Decisions app built by CATO has been live since October 31. Four obligation rows wait on the Deck's return: a ledger truncation that shows on the Deck's decided view, a pickup that only runs at boot, a layout residue, and two small commands for writing queue rows. None can close while the Deck is merely paused.",
  "conditions": [
    "The pause ruling says taps made on the hosted page and never read stay UNKNOWN. The last verified pickup was October 9. If you tapped anything on the old page after that and never said it in chat, retiring leaves it unread: tell PROME before choosing A.",
    "Retiring the page does not touch the Decisions app, the queue, or the parser code the queue view and the ledger use.",
    "Option A's manual edits are wording only (paused becomes retired) in PROME's own manuals and the four skill copies; no rule's meaning changes. They get one blind read before commit.",
    "The two queue-row writer commands (DOCKET line 734) would be dropped, not built: queue rows stay hand-written and checked by the ledger sync, as they were today.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
