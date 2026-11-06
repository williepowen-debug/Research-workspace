# WQ-599 decision brief — PREVIEW, not installed

**Status:** preview under Will's 2026-11-06 11:08 ET instruction. No pointer is in the queue row, so the app does not read this yet. It approves nothing and changes no answer-confirmation rule. ⚠️ WQ-599 was RULED C at 10:59 ET, before this was prepared: this is a sample of the format only, showing the question as it stood, and must render as closed and not answerable. Its row hash is null because the row left OPEN.

```decisions-brief
{
  "schema_version": "decisions-brief/1",
  "wq_id": 599,
  "queue_row_sha256": null,
  "prepared_at": "2026-11-06 11:10 ET",
  "stale_after": "2026-11-07",
  "question": "The agents' trades failed the scale test you set on August 8. Should the fleet shrink because of it?",
  "what_changes": "The test asked for 10 closed trades that agents proposed and you approved. The count is 5, so the rule you registered calls for a shrink proposal rather than another improvement list. Today 41 desks can run. TERRY's draft keeps 2 always running, puts 20 on call and 19 to sleep, keeps all their files, and can be reversed on your word. It would spend less, though how much is unmeasured, and sleeping desks stop watching their areas.",
  "recommendation": {
    "status": "NONE_YET",
    "text": "No recommendation yet. Unresolved: whether too many desks is why the count is low. RED's judgement puts that at about a quarter, behind you running capital yourself and trigger rules holding entries back. The saving could be up to 46.4%, or under 7.7%."
  },
  "conditions": [
    "Florida desks CORAL and MARCO would go to sleep, though Florida is a top priority for you.",
    "ORACLE, the independent check using prediction-market odds, would go to sleep. Who launches it and reads its alerts is already unowned.",
    "Triggers with no date need a named watcher, or they can fire with nobody reading them.",
    "Five trades says little about research value. RED says the proposal is not ready to adopt as written. PROME would stay running and helps grade this, so it has a conflict."
  ],
  "supporting": [
    {
      "label": "TERRY's draft v4",
      "path": "AGENTS/TERRY/research/2026-11-07_op-scale/DRAFT_SHRINK_PROPOSAL.md"
    },
    {
      "label": "The recount and rulings",
      "path": "PROME/reports/2026-11-05_op-scale-recount.md"
    },
    {
      "label": "RED's final read",
      "path": "AGENTS/RED/reports/2026-11-05_S59_OP_SCALE_ADVERSARIAL_READ.md"
    }
  ]
}
```

```decisions-options
{
  "schema_version": "decisions-options/1",
  "wq_id": 599,
  "queue_row_sha256": null,
  "choices": [
    {
      "id": "A",
      "label": "Accept as drafted",
      "meaning": "2 always running, 20 on call, 19 asleep, with TERRY on call and named watchers.",
      "consequence": "PROME and TERRY carry out the change. Files stay, and it can be reversed on your word."
    },
    {
      "id": "B",
      "label": "Accept with changes",
      "meaning": "You name the changes, for example keeping Florida or ORACLE awake.",
      "consequence": "TERRY redrafts and it comes back to you."
    },
    {
      "id": "C",
      "label": "Decline",
      "meaning": "The fleet stays as it is.",
      "consequence": "The test is still recorded as not met, and nothing changes."
    }
  ]
}
```
