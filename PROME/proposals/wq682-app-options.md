# WQ-682 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "682",
  "queue_terms_sha256": "dba10380886da46e05ea738b42eb9f6f71c5f9dad86ff731267bd19fad6f4d0d",
  "choices": [
    {
      "id": "A",
      "label": "Swap in the collateral ratio",
      "meaning": "The red leg of BOND's rule becomes: the Home Loan Banks' own reported collateral ratio for all borrowers at or below 3.0 at a quarter-end, OR advances above $900B system-wide.",
      "consequence": "The clause nobody can grade is replaced by one that can be, so the number of rules does not grow. BOND encodes it at its next session and re-scores when the third-quarter report posts. Today's reading is 3.7 (June 30, 2026), so nothing fires."
    },
    {
      "id": "B",
      "label": "Strike the clause",
      "meaning": "The words \"advance-depletion narrative\" are removed; the red leg is advances above $900B alone.",
      "consequence": "Fewest rules. The rule would not have turned red at March 31, 2020 (advances were $797B), a quarter the ratio in A did catch."
    },
    {
      "id": "C",
      "label": "Leave as is",
      "meaning": "The clause stays as written.",
      "consequence": "It stays ungradeable, as it has been since August 23: nobody can say whether it has fired."
    }
  ],
  "recommended_choice_id": "A",
  "context": "BOND scores stress in the Federal Home Loan Banks' lending to banks (advances) with a rule called VX-BND-18. Its red leg reads \"above $900B system-wide OR an advance-depletion narrative\". The second half names no instrument and no number, so BOND returned it as ungradeable on August 23 and it was deferred to today. BOND now reports that the instrument it named in August (system-wide unused borrowing capacity) is not published at all. What the Home Loan Banks do publish every quarter is a collateral ratio for all borrowers: eligible collateral divided by advances and other credit. Over 30 quarters (2019 Q1 to 2026 Q2) its two lowest values are the two stress quarters, 2.8 at March 31, 2023 and 3.0 at March 31, 2020; every other quarter is 3.2 or higher; the latest is 3.7. This is a score rule for BOND's vector, not a trade trigger. BOND and PROME both recommend A.",
  "conditions": [
    "Two stress quarters out of 30 is a base rate, not a validation.",
    "It confirms, never warns: a quarter-end snapshot published about six weeks later. It scores the vector; it cannot position anyone ahead of an event. The existing $900B leg has the same lag.",
    "It cannot see one bank running out of collateral, which was the Silicon Valley Bank mechanism: the report says borrowers are not cross-collateralized, and the ratio is an aggregate.",
    "It is gross collateral before haircuts, not borrowing room.",
    "The 30-quarter table is BOND's reading of the issuer's reports; PROME read BOND's packet and has not re-opened the reports.",
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
