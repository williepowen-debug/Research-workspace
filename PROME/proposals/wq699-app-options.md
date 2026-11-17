# WQ-699 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "699",
  "queue_terms_sha256": "3595dd97c77147f6977087e09b3c53ede29c532f8b8db375a75f45c1a6d8a29d",
  "choices": [
    {
      "id": "A",
      "label": "Switch to the matched basis",
      "meaning": "BOND changes one definition on two surfaces, its mortgage-spread watch (VX-BND-17) and the start-up watcher that feeds it: the weekly mortgage survey is paired with the last Treasury close before the Thursday it is published, not with that Thursday's close. PROME verifies the edit at BOND's files.",
      "consequence": "The watch stops firing on a mismatch of weeks. On this basis it would not have left its 180 to 230 band at all in 2026, including on November 5. The cost: it reacts one week late to a sharp Treasury move that happens on a Thursday."
    },
    {
      "id": "B",
      "label": "Leave it as it is",
      "meaning": "No change. The watch keeps pairing the survey with the same Thursday's Treasury close.",
      "consequence": "The watch keeps comparing two different weeks, and BOND and HOMER keep quoting different figures for the same spread (201 against 213 on November 12). Both 2026 breaks of the band, October 22 and November 5, came from this pairing."
    }
  ],
  "recommended_choice_id": "A",
  "context": "BOND, the Treasury desk, watches the gap between the 30-year fixed mortgage rate (Freddie Mac's weekly survey) and the 10-year Treasury yield as one sign of mortgage-market stress; the normal band is 180 to 230 basis points. HOMER, the housing desk, measures the same gap on a different pairing of dates. On November 16 the two desks reconciled: HOMER's pairing is right, the gap is about 213, and BOND withdrew its 201. BOND's backtest of 97 weeks found that both 2026 readings outside the band came from its own pairing. BOND did not apply the change itself because it moves what fires on a watcher you approved on September 28.",
  "conditions": [
    "The band (180 to 230), the thresholds and the scope of the watch do not change.",
    "The score is 1 on both bases today; nothing moves at the switch, and the November 5 and November 12 records stand as written.",
    "BOND's backtest used Treasury's own file while the watcher reads FRED's series; they matched on the two dates checked, not on every date.",
    "PROME has read BOND's packet and has not re-run the backtest.",
    "No trade implication: BOND calls this a correction to a measurement, not a market finding.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
