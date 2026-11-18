# WQ-712 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "712",
  "queue_terms_sha256": "9e4a3dffcb0ede7a5abb79716b724e788b79e59d0c295d590d33146696a035a9",
  "choices": [
    {
      "id": "A",
      "label": "Update the brief only when something changed, after NEXUS checks for breakage",
      "meaning": "PROME sends NEXUS the proposal for its 11/24 session. If NEXUS names nothing that would break, each desk drops the words \"even no-change\" from its own instructions at its next ordinary session: a brief is rewritten only when a figure, threshold, or cross-desk send or wait in it changed. If NEXUS names a real dependency, PROME brings it back to you before any desk changes.",
      "consequence": "Fewer routine commits and less closeout time per desk session. NEXUS keeps its seat and its role. One conditional approval covers both steps unless NEXUS objects."
    },
    {
      "id": "B",
      "label": "A, and also narrow NEXUS's role to finding contradictions between desks",
      "meaning": "Everything in A. In addition NEXUS drafts a change to its own instructions that makes cross-desk contradiction-finding (the kind of finding behind the December Fed price owner and the unread-inbox alert) its stated job, and brings the draft to you for approval.",
      "consequence": "A second decision later on the draft. It changes what NEXUS is for, which you ruled on once on 10/14."
    },
    {
      "id": "C",
      "label": "Leave it as it is",
      "meaning": "Desks keep updating their NEXUS brief every session. Nothing is sent to NEXUS.",
      "consequence": "The routine cost continues at about one commit in nine. Nothing is risked."
    }
  ],
  "recommended_choice_id": "A",
  "context": "Thirty-one desks keep a brief file for NEXUS, the cross-desk synthesis desk, and most desk instructions require an update every session even when nothing changed. An outside audit you supplied on 11/17 counted 9.8% of all repository commits touching one of these briefs; PROME's recount agrees (2,520 of 25,626 at the audit's pin, and 451 of 3,864 so far in November). Over the same period NEXUS's output was the deciding input in 3 of about 700 of your decisions and in no market or trade decision. You kept NEXUS on 10/14; this does not reopen that.",
  "conditions": [
    "The audit cannot see quiet influence: a desk that reads a brief and adjusts without citing it leaves no trace. NEXUS's case for itself rests on that kind of effect.",
    "The brief is also each desk's table of what it is sending to and waiting for from other desks. Who besides NEXUS reads it was not measured.",
    "NEXUS's freshness scan keys on each brief's last commit time, so an unchanged brief would look stale unless NEXUS keys on the desk's status file instead. That is the kind of breakage NEXUS is asked to name.",
    "Neither NEXUS nor any desk has been asked yet.",
    "No money, position, gate or threshold is involved.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
