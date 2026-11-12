# WQ-681 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "681",
  "queue_terms_sha256": "42fe2ed838ef245d68abf2df201d27c81b288506a7845d1727ca691b3cec417f",
  "choices": [
    {
      "id": "A",
      "label": "Allow the run at session start",
      "meaning": "WALTER may start one collector run when it boots or returns and the last collection is more than about 12 hours old. The single daily schedule stays.",
      "consequence": "WALTER changes one line of its charter (step 7e(a)) and corrects the schedule comment to the measured start times. Each WALTER brief then reports news collected up to a stated time. Nothing is collected while no session is open."
    },
    {
      "id": "B",
      "label": "A plus a second scheduled run",
      "meaning": "As A, and a second daily scheduled run is added for the early morning.",
      "consequence": "Because GitHub starts scheduled runs 4 to 8.6 hours late, the second run would land somewhere between about 05:00 and 13:30 ET; it cannot promise to finish before 06:00 ET. About 60 more minutes of GitHub Actions a month."
    },
    {
      "id": "C",
      "label": "State coverage only",
      "meaning": "No run by WALTER. The lane stays read-only to it.",
      "consequence": "WALTER's briefs say what interval was not collected instead of \"no overnight news\". The interval itself stays uncollected until the afternoon run."
    },
    {
      "id": "D",
      "label": "Hold",
      "meaning": "Nothing changes beyond what WALTER already adopted.",
      "consequence": "Same result as C; the question stays open."
    }
  ],
  "recommended_choice_id": "A",
  "context": "The news collector is set for 10:00 ET once a day, but GitHub starts it 4 to 8.6 hours late every day: the last 12 scheduled runs began between 13:55 and 18:38 ET (WALTER's reading of the run list; PROME checked the last five at GitHub). Evening, overnight and morning news is therefore not collected before the next afternoon. On 11/11 the after-hours report on Nvidia's chief executive was missed by an evening session, and the 11/12 morning boot said there was no overnight news. CATO's review ranks this the most important open operating gap. WALTER can start a run by hand in about two minutes (it did once on 11/12 at Will's request), but its charter makes the lane read-only to WALTER.",
  "conditions": [
    "A run at session start would likely, not provably, have caught the 11/11 report: the lane has no Nvidia query and the story arrives only through general headline feeds.",
    "A run makes GitHub add one dated batch to the Research-Intake repository; it sends nothing to anyone else.",
    "Cost is about 2 minutes of GitHub Actions per run, $0 on current usage as far as WALTER can see; plan minutes were not checked.",
    "No unattended service is included. Sessions still start only when Will or PROME launches them.",
    "WALTER already states its collected-through time in every brief; that part needs no ruling.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
