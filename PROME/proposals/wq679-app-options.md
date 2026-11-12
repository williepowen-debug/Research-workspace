# WQ-679 — explicit decision card

Question, options, context and conditions are decision terms. Queue Notes are operational; put changed conditions here or in the question, not only in Notes.

```decisions-options
{
  "schema_version": "decisions-options/3",
  "wq_id": "679",
  "queue_terms_sha256": "fd50501e74c1c845fdd25e72c7922c7b1fee5a53464853dc38600aea1fa515d0",
  "choices": [
    {
      "id": "A",
      "label": "Apply both sets",
      "meaning": "The 11 root-file trims (root CLAUDE.md 5, AGENTS.md 3, docs/GIT_WORKTREE_PROCEDURES.md 3) and the 8 charter trims PROME accepts are approved.",
      "consequence": "PROME drafts each change in a ruling record, has it read blind before the edit and again after, and commits. Root CLAUDE.md changes go in as one transplant. The 7 charter trims PROME declines stay as they are."
    },
    {
      "id": "B",
      "label": "Root files only",
      "meaning": "The 11 root-file trims are approved. PROME's charter is left as it is.",
      "consequence": "The charter keeps about 5 KB of history that every PROME boot reads, and its line 20 keeps wording looser than root's."
    },
    {
      "id": "C",
      "label": "Charter only",
      "meaning": "The 8 charter trims are approved. The root files are left as they are.",
      "consequence": "Root keeps the duplicates, provenance tags and the fixed message-file path."
    },
    {
      "id": "D",
      "label": "Hold",
      "meaning": "Nothing is applied. The list stays on file.",
      "consequence": "No file changes. Nothing breaks; these are trims, not contradictions."
    }
  ],
  "recommended_choice_id": "A",
  "context": "DAEDALUS's instruction-file re-test (WQ-678, which you ruled A on 2026-11-12) also listed small trims in files only you can open for editing. Root files, 11 rows, all rated LOW: in root CLAUDE.md a duplicate of TERRY's rule-6 test becomes a pointer, rule 1 loses the Claude-only tool name (the rule number is kept), three provenance tags leave a file that says it holds rules only, the Direct Messaging bullet is shortened to its rule, and the frozen-portfolio note is stated once; in AGENTS.md a restated-roles line, a retired-table note and a duplicate potash line go; in docs/GIT_WORKTREE_PROCEDURES.md the pre-commit check moves ahead of the commit commands, 'a message file you own' replaces the fixed /tmp/msg.txt that two sessions can overwrite, and provenance tags go. PROME's charter, 8 of the 15 rows offered: line 20's dirty-tree wording becomes a pointer to root (root has no 'with Will approval' escape for stashing another desk's work), the header's stamp chain becomes one line, and six history strikes (resolved docket notes, the lapsed-freeze header, provenance asides, the body of the suspended process ceiling, which stays on file in its own ruling record). PROME declines the other 7 as owner, including the rewrite of the review-budget paragraph, where compressing risks changing a rule. Source: PROME/inbox/processed/2026-11-12_from-DAEDALUS_WQ678-PROME-rows.md.",
  "conditions": [
    "Every change removes or replaces text; none adds a rule.",
    "The charter's line 20 change is stricter than today's text, not looser.",
    "The readers judged text only; no session behaviour was tested.",
    "The saving is the readers' estimate, not measured: about 5 KB of every-boot reading in the charter, under 2 KB in the root files.",
    "Every app answer needs Will's confirming word in chat."
  ],
  "confirmation": {
    "mode": "chat",
    "scope": "other",
    "reason": "Matching PROME-chat confirmation remains required under the installed fallback."
  }
}
```
