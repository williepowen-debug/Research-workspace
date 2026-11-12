# WQ-678 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "678",
  "queue_terms_sha256": "7682dca0c9f3d8873f7103680a6bbb9dd0a9fe671b6c60222d2227ea50439083",
  "choices": [
    {
      "id": "A",
      "label": "Apply the 18 fixes; send the trims as optional packets",
      "meaning": "Changelist A (18 verified contradictions) is approved: each desk applies its own lines by packet, PROME applies the six in its own files, DAEDALUS applies its own. Changelist B (about 550 trims) goes out as one packet per desk; each owner applies or declines.",
      "consequence": "No desk is launched for this alone; each applies its lines at its next ordinary wake. The USER.md line 50 item still needs your own word: strike or keep. PROME's charter line 39 changes (force-push moves from ask-first to never)."
    },
    {
      "id": "B",
      "label": "Apply the 18 fixes only",
      "meaning": "Changelist A is approved as in choice A. Changelist B (the trims) is not sent.",
      "consequence": "The contradictions are fixed; the estimated boot-reading saving from the trims is not pursued. The USER.md line 50 item still needs your own word."
    },
    {
      "id": "C",
      "label": "Hold",
      "meaning": "Nothing is applied now. The record stays on file.",
      "consequence": "The 18 contradictions stay in the instruction files until you say otherwise."
    },
    {
      "id": "D",
      "label": "I'll say",
      "meaning": "You say in chat what you want changed or done.",
      "consequence": "PROME records your words; nothing is applied until you say it."
    }
  ],
  "recommended_choice_id": "A",
  "context": "You asked DAEDALUS at 09:07 ET on 2026-11-12 to re-test the desks' instruction files after its switch from Codex to Claude. Nine independent readers read 74 files whole and logged 599 items. DAEDALUS re-checked the 47 rated serious and kept 18 as real contradictions with the root rules or your own instructions (Changelist A): for example four desks' push-failure shorthand skips the root safety check, one desk's commit line would sweep other desks' rows, PROME's charter lists force-push as ask-first where root says never, PROME's playbook says desk spawns run on Sonnet where you ruled Opus, two desks name PROME rather than TERRY for trade construction, and several name Claude-only tools as the only route. The other roughly 550 items (Changelist B) are trims: history inside steps, duplicates of root, dead pointers; the readers estimate about 300 KB of boot reading saved, by eye, not measured. Nothing has been edited. Record: AGENTS/DAEDALUS/runs/2026-11-12_HARNESS_RETEST.md.",
  "conditions": [
    "Every change removes or replaces text; none adds a rule.",
    "Six of the 18 are in PROME's own files; the charter line is a change to PROME's own charter and needs Will's word; PROME applies each under its usual two-read review.",
    "USER.md line 50 against line 52 (sell-or-roll rail on cards) is Will's own file: he says strike or keep; no choice here decides it.",
    "The readers judged text only; no session behaviour was tested. The trims are owner judgment and a desk may decline any, so the 300 KB estimate is a ceiling.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
