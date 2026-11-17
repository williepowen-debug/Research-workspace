# WQ-701 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "701",
  "queue_terms_sha256": "272cb88b483e6c221830b822a5d501ef3be8d0de3d3ecac9b73e61c63a6345df",
  "choices": [
    {
      "id": "A",
      "label": "Apply all eight",
      "meaning": "Everything in the proposal as PROME drafted it: the 50,000-byte ceiling for desk instruction files (A2), the follow-through line on the existing closeout check (B), the one-time rule sweep after 11/24 (C), the cheaper trim path (D), the shared-tools line with one citation form (E), the precedence line (F), the blocked-sites rule (G) and deleting root's leftover git pull sentence (H2). The two skill copies stay as they are (H3).",
      "consequence": "Root rules gain four passages and lose one sentence, about 1.3 KB net. Four desks trim their instruction files at their next sessions. Your 11/11 and 11/16 words against new review cycles are lifted for the one sweep."
    },
    {
      "id": "B",
      "label": "Apply the core set",
      "meaning": "A2, B, D, G and H2 only: the 50,000-byte ceiling, the follow-through line, the cheaper trim path, the blocked-sites rule, and deleting the leftover sentence. No precedence line, no shared-tools line, no rule sweep for now.",
      "consequence": "Root gains two passages and loses one sentence. The items left out are the ones where the review found no actual conflict or overreach; they can be brought back later."
    },
    {
      "id": "C",
      "label": "Choose by letter",
      "meaning": "You name the letters in chat (A1, A2 or A3 for the ceiling; B through H2 for the rest) and PROME applies exactly those.",
      "consequence": "Nothing beyond the letters you name is applied."
    },
    {
      "id": "D",
      "label": "Apply nothing further",
      "meaning": "The eight start-up lines already fixed stay fixed. No root rule, number or review limit changes.",
      "consequence": "Twelve desk instruction files stay over the fleet read cap under DAEDALUS's exemption, and LABOR's and OSPREY's can still be cut off on a single explicit read."
    }
  ],
  "recommended_choice_id": "B",
  "context": "An outside read-only review of the fleet's rules found that rules a script enforces are followed and rules that rely on memory are not, that twelve desk instruction files are over the 32,550-byte read cap through an exemption a desk wrote for itself, and that trimming rules costs far more paperwork than the text removed. PROME checked its main claims at the files: most hold; one is wrong (the two skill copies cannot drift unnoticed, the boot gate compares them) and one is out of date (rulings have had dated follow-through rows since 11/16). You asked PROME at 22:01 ET on 11/16 to fix the eight items. The one that needed no choice is done. The others change what a root rule says, set a number, or change PROME's own review limits, so the exact text is in the proposal for your word.",
  "conditions": [
    "The 50,000-byte figure is PROME's choice of margin under the roughly 54,250-byte point where one read cuts off; it is not a measured threshold.",
    "The cheaper trim path lowers PROME's own review requirement for edits that only delete or move text; it is yours to grant.",
    "Root rule text gets one blind read before it is applied and one after.",
    "The review's three companion passes and its BRENT and CFTC example were not checked by PROME.",
    "The rule sweep is a review cycle; it runs only if you lift your 11/11 and 11/16 words for it.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
