# WQ-756 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "756",
  "queue_terms_sha256": "0b822c46670ab509c26ea7ae9044ede15b66a91450f19d416107f1201a69f7f9",
  "choices": [
    {
      "id": "A",
      "label": "Count dividends in this case",
      "meaning": "When fund shares are down and manager shares are up, the leg is MET only if the funds are also down after counting dividends; otherwise NOT MET. The other cases keep the raw-close basis.",
      "consequence": "Today's reading is NOT MET (funds +1.22% with dividends). SHADE writes the sentence into its trigger. No past reading is regraded."
    },
    {
      "id": "B",
      "label": "Met on raw closes",
      "meaning": "Funds down while managers are up counts as the funds leading down, on raw closes as the rule is written.",
      "consequence": "Today's reading is MET and the trigger fires, arming SHADE's deep read of insurer filings. Research only, $0. The leg will tend to fire in any long window because payouts lower raw closes."
    },
    {
      "id": "C",
      "label": "Not met unless both fall",
      "meaning": "The leg needs both groups down with the funds down more. Funds down while managers are up is NOT MET.",
      "consequence": "Today's reading is NOT MET. The trigger cannot fire while manager shares are rising, even if fund shares fall hard."
    },
    {
      "id": "D",
      "label": "Leave it ungraded",
      "meaning": "No change. This case stays outside the rule and gets no grade.",
      "consequence": "The trigger stays silent whenever funds fall and managers rise; SHADE reports the figures and stops, as today."
    }
  ],
  "recommended_choice_id": "A",
  "context": "T-SHADE-01 arms SHADE's deep read of insurer statutory filings. It needs the high-yield spread above 280 bp for five sessions (met) and the private-credit funds ARCC, FSK, OBDC and BIZD leading their managers APO and ARES down. From 9/24 to the 11/25 close the funds are down 0.37% on raw closes and the managers are up 5.67%; with dividends the funds are up 1.22%. The rule does not cover funds down while managers are up, so SHADE gave no grade.",
  "conditions": [
    "Research consequence only: no trade, no sizing, $0. The X1 sizing gate is separate and stays closed.",
    "SHADE read Athene's Q3 statutory statement today without the trigger, so nothing waits on this.",
    "Figures are SHADE's, read from its closes file; PROME did not recompute them.",
    "No past reading is regraded under any choice.",
    "Not urgent."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
