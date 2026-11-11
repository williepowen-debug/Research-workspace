# WQ-639 candidate — not installed

Approved work: owner card-authoring command and a question/options binding that tolerates running Notes edits. Runtime changes stay in an isolated candidate until the required independent acceptance and owner activation. Existing chat confirmation remains mandatory; no notification hooks or real responses.

Acceptance before implementation:
- Generate an explicit card source, pointer and binding from a named open DECISION row, supplied choices/recommendation, locked context/conditions and chat policy. No inferred choice, condition or authority.
- Preparation outputs a reviewable two-file patch without owner mutations. The supported --apply operation must check both complete owner-file preimages and patch integrity before mutation; stale inputs refuse. It does not stage, publish, answer or change acceptance. Existing owner text is preserved and replacing an authored source requires explicit opt-in.
- New schema only: running Notes changes do not invalidate it. Question, type, date, recommendation, blocked status, pointer, choices, confirmation policy, context, conditions and explanation changes still block a pending answer. A closed/missing row always blocks.
- Save snapshots retain exact published provenance; unpublished notes cannot be relabelled as published. Existing /1 and /2 sources, answers and receipts retain their original strict binding and historical replay.
- Preserve a real producer row and test Notes before/after publication, stale patches, duplicate/missing/wrong identities, meaningful changes, hidden WAIT declarations, parallel owner edits and history replay/delivery with fake repositories.
- Do not manufacture a repair for WQ-558: inspect its current integrated receipt/UI first, and preserve superseded history. A current recorded answer must not demand clarification again.

Scope excludes owner policy/queue application, live notification proof, new app-only authority and agent launches. Single-owner publication of generated patches remains PROME's normal Git responsibility; patch creation does not publish or execute a decision.

## Owner usage after acceptance

Create an input JSON with exactly these fields (all wording is owner-authored):

```json
{
  "choices": [
    {"id": "A", "label": "Do the bounded task", "meaning": "Only the named task.", "consequence": "No recurring work."},
    {"id": "B", "label": "Decline", "meaning": "Do not do the task.", "consequence": "No change."}
  ],
  "recommended_choice_id": "A",
  "context": "The full explanation needed to understand the decision.",
  "conditions": ["Preserve the important restriction."]
}
```

Use `null` for an explicit absence of recommendation. Empty conditions are allowed only when the owner determines there are none. This is a source-authoring tool, not a semantic completeness checker: the owner must carry material caveats from the queue into context/conditions, choices or the question. Changes to a material condition belong there, never solely in operational Notes.

```sh
python3 AGENTS/CATO/prototypes/decisions/mvp/author_card.py \
  --wq 123 --input /tmp/card-input.json --output /tmp/prepared-wq123
```

Preparation creates `source.md`, `card.patch` and a preimage/binding/patch-integrity manifest in a new directory. Preparation neither changes the queue nor stages/commits/pushes. A missing/closed/mixed/blocked row or bad/ambiguous input refuses. Existing source replacement requires `--replace-source` after the owner reads the original. At an ordinary owner touch, use `python3 AGENTS/CATO/prototypes/decisions/mvp/author_card.py --apply /tmp/prepared-wq123`, then use existing exact-path publication for its two files. This checks the complete queue and source preimages, including appends and existing-pointer replacements, and patch integrity before application; any change requires regeneration. Raw `git apply` is not the supported application workflow: it cannot enforce the manifest preimages. The owner must hold exclusive write custody of these files during the short apply operation, as for ordinary Git application; this command does not lock out arbitrary external writers. No index, commit or publication change occurs during apply. Do not apply /3 sources before installing the matching accepted reader. The runtime refuses partial publication; existing /1 and /2 cards continue working.

## Binding and history

Only new `decisions-options/3` cards opt in. The binding covers the first six queue columns plus declared blocked state; the pointer and full option-source text are independently compared. The source includes explicit locked context and conditions. Running Notes do not become new decision terms, and the exact historical row still travels in the immutable snapshot. An unpublished Notes edit is never recorded as published wording. Old /1-/2 sources/answers remain strict; do not rewrite old responses or receipts to opt them in.

Changing question, options, recommendation, deadline, type, hold state, pointer, locked explanation, conditions or confirmation policy still invalidates an unsent answer. Closing/removing the row prevents a new answer or delivery. A replaced old source needs a fresh answer, not retroactive approval. The legacy pilot's integrated answer remains historical; recorded cards no longer offer disabled recommendation controls.

## Deployment boundary

The candidate changes the runtime hash map and the HTML presentation hash. Installation must preserve the reviewed acceptance contract: independent review without blocking findings, exact accepted build hashes and owner-controlled published acceptance. Existing unsent responses may require a fresh review because the HTML hash changes; preserve their words/history. Do not hand-commit `decisions/queue-responses` files. Keep `app_only_enabled: false`; no hooks or live-alert authority are included. Notification proof remains a separate real-session observation with PROME.

## IR-639-1 repair acceptance

Replacement apply must refuse question change, closure, pointer swap, source edits/appends and queue appends, preserving both current files. Unchanged replacement and fresh-card apply must succeed without staging. Changed patch bytes refuse. Replacement patches also retain an exact target-row hunk even when the pointer is unchanged. Original historical review and its BLOCK remain evidence for the superseded candidate; a focused independent recheck must assess these repaired bytes.
