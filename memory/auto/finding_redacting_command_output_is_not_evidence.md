---
name: finding_redacting_command_output_is_not_evidence
description: A command written to HIDE a value cannot tell you about that value — its output looks identical whether the value exists or is empty; test by a property that survives redaction (length/checksum/exit code)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 743a2106-2e23-427c-bdeb-f3448c5b87b6
  modified: 2026-08-13T17:29:19.221Z
---

**HOMER, 2026-08-13.** Diagnosing a FRED fetch failure, ran `grep -oE 'FRED[A-Z_]*=' .env` to avoid printing a secret. It output `FRED_API_KEY=`. Read that as *"present but EMPTY"*, wrote it into a report, and **asked the operator to register a new API key.** The key was present, 32 chars, and the sanctioned tool path worked the whole time. PROME caught it within the hour.

**The mechanism:** the pattern **ends at the `=` and excludes the value by construction.** It prints **identically** whether the value is a 32-char secret or nothing. **The redaction was deliberate and correct — then its output was treated as evidence about the very thing it was designed to hide.**

**Why:** a secret-safe command *feels* like a careful act, so its output inherits the credibility of the caution that produced it. The care went into not-leaking; none went into whether the result could answer the question.

**How to apply:** **Never infer a value from a command written to exclude that value.** To test presence/absence without disclosure, measure a property that **survives redaction**: length (`awk -F= '/^KEY=/{print length($2)}'`), a checksum, or an **exit code from the real consumer** — best of all, just run the tool and see if it works. **Tell:** you are about to claim something about *the content of X* using output you deliberately made *not contain X*.

**Two second-order lessons, both load-bearing:**
- **This reached an ASK with an external cost** (register an account). **Any claim that triggers a spend, a signup, or an escalation to another agent deserves one confirming check by an independent method BEFORE it is sent.**
- ⚠️ **The correction's stated CAUSE was also wrong.** PROME's reconstruction — "you read the wrong `.env`" — was plausible and false; the right directory had been used. **Accepting a correction is not the same as accepting its explanation. Verify the mechanism, or the real trap stays live and unrecorded.**

**Sibling failure the same day, same root:** an unsanctioned scrape (`fredgraph.csv`) that is bot-blocked **fails as a SILENT TIMEOUT, not a 403** — indistinguishable from an outage, and it produced two false "FRED is blocked" escalations in two days (HOMER 8/13, NEXUS 8/12). **Check the sanctioned path before escalating an outage.** See [[finding_blocked_mirror_is_not_an_unreachable_primary]], [[finding_unfetched_is_not_unavailable]], [[finding_verification_zero_is_ambiguous]].
