---
name: webfetch-pdf-saves-despite-parse-error
description: "WebFetch returns 'cannot parse binary/encoded streams' on PDFs but STILL SAVES the file to disk and prints the path — the parse error is NOT a dead end. Ignore it, take the path, extract locally with pdfminer; use `pdftotext -layout` for TABLES because pdfminer interleaves columns, and foot-check every extracted table. Nearly cost a 4-agent study every one of its government-PDF primaries."
metadata:
  node_type: memory
  type: finding
---

2026-07-24, WALTER's 4-agent FHA/VA stress-test. Every load-bearing primary in the study was a large government PDF (HUD FY2025 MMI Annual Report 3.3MB, the ITDC actuarial review 18.5MB, five Agency Financial Reports, an enrolled bill). **WebFetch failed to parse all of them**, returning `cannot parse binary/encoded streams`.

**That error is not a failure. WebFetch still writes the file to disk and prints the local path.** One agent noticed, and it was the difference between a dead study and a complete one:

1. Call WebFetch on the PDF URL. **Ignore the parse error. Take the path it prints.**
2. Extract locally: `.venv/bin/python3 -c "from pdfminer.high_level import extract_text; print(extract_text('<path>'))"`
3. **For TABLES use `pdftotext -layout -f <first> -l <last> <path> -`.** pdfminer interleaves columns and silently scrambles financial tables.
4. **Foot-check every extracted table.** The one scrambled table in that run was caught only because its totals did not add up.

Via this route the agents recovered full text of every primary — 327K and 389K characters from the two biggest — and did local `grep` on them, which produced findings unreachable any other way (e.g. "redefault" appears exactly ONCE in a 381,721-character actuarial review; an enrolled bill's §702 text at line 5958).

**Why it matters beyond PDFs:** the failure is silent and self-confirming. An agent reads "cannot parse," concludes the source is unreachable, and reports a *negative* — "could not verify at primary" — that is indistinguishable from a genuine absence. On a study whose entire purpose was auditing whether a widely-cited number holds up, that would have manufactured false gaps and left a weak citation standing.

**Related access notes from the same run:** EDGAR and many `.gov` hosts 403 without a browser User-Agent (`[[finding_edgar_403_user_agent_header]]`) — curl with a UA often works where WebFetch does not. `hudoig.gov` is Cloudflare-walled but only partially (older PDFs at direct paths still fetch). `hud.gov/sites/dfiles/CFO/documents/afr20XX.pdf` 404s for prior years while `archives.hud.gov/reports/afr/afrXXXX.pdf` works. Prefer an **enrolled bill on govinfo.gov** over a committee section-by-section summary when verifying statutory text.

**How to apply:** put the extract-locally recipe in the spawn prompt for any research task expected to hit government or filing PDFs, rather than trusting each agent to discover it. And treat any agent's "unreachable at primary" on a PDF host as provisional until the local-extraction path has been tried.

Related: [[finding_edgar_403_user_agent_header]] · [[finding_fail_loud_on_incomplete_data]] · [[finding_discovery_tool_wrong_slice_false_zero]] · [[feedback_subagent_web_tools_not_autoloaded]] · [[finding_loadbearing_number_must_be_reproducible]]
