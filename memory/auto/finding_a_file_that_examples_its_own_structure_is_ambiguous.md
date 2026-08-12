---
name: finding_a_file_that_examples_its_own_structure_is_ambiguous
description: "When a file contains an EXAMPLE of its own structure — a template block quoting its real section headings — the example is indistinguishable from the structure to every string-matching tool, and scripted edits silently write into the example"
metadata:
  type: finding
---

**A file that contains an example of its own structure is ambiguous to every tool that matches on strings.** The example and the real thing are the same bytes. Anchored edits hit whichever comes first — and the example almost always comes first, because examples go at the top.

## The instance

**RED, 2026-08-12.** `SCRATCH.md` — a session handoff — opened with a `<!-- TEMPLATE -->` comment listing its own section headings verbatim: `## CHANGES SINCE`, `## WHAT I DID`, `## OPEN THREADS`, and so on. The live body used those identical strings.

Every scripted insert anchored on a heading (`s.replace("## OPEN THREADS\n", ...)`, first occurrence) matched **the commented copy**. Three collisions in one working day. Two were caught by inspecting heading line-numbers afterward. **The third was committed and pushed** — two carry-forward handoff threads written *inside* an HTML comment: present in the file, rendering as nothing, and due to be read at the next boot as a handoff that silently omitted them.

## Why it survives every check

This is the property that makes it worth a memory rather than a bug report:

- A **content grep** confirms the text is there. It is there.
- **Schema / lint / format checks** pass — the file is well-formed.
- **Freshness and staleness checks** pass — the file was just written.
- **Rendered output** shows nothing, and nobody diffs rendered output.

So the defect reports as *healthy* on every axis anyone measures, and the only symptom is content quietly not existing for its reader.

## Three fixes, weakest to strongest

1. **Anchor on the last occurrence.** Fixes the caller, not the file. Every future caller has to remember, and callers are often scripts written in a hurry.
2. **Verify placement by offset after each insert** — assert *which* occurrence you hit, not that the string is present. Better, but it is a check, so it only fires if someone runs it.
3. **Remove the ambiguity.** Stop the example quoting the real thing. Strip the structural markers from the template (list section *names*, not `## headings`), and leave an explicit do-not-restore note with the incident recorded.

**Take (3).** *A check that must be remembered is the same class of failure as the bug it detects.*

## Verify functionally, not by inspection

After fixing, do not eyeball it. Assert the properties:

- every structural anchor now matches **exactly once** (it matched twice before);
- a **simulated naive first-occurrence insert** — the exact failure mode — lands in the body, tested by checking the insertion index falls outside the comment delimiters;
- the example block contains **zero** live structural markers, so the ambiguity cannot silently regrow when someone later "tidies" the template.

## Where else this lives

Anywhere a file demonstrates its own format: a README showing its own config syntax, a schema file with an example row that parsers may read as data, a docs page whose sample code blocks contain the very markers a build step scans for, a commit-message template quoting real trailer keys. **Ask: if a tool searched this file for a structural marker, could it land on the illustration instead of the thing?**

Related: [[finding_dead_path_regrows_unless_senders_repointed]] — the same regrow shape, where a convention re-creates what was removed · [[finding_silent_blank_evades_review]] · [[finding_verification_zero_is_ambiguous]] — a check reporting clean is ambiguous the same way · [[finding_mechanize_the_cap_not_the_ritual]] — prefer a mechanism over a remembered step.
