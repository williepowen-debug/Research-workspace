---
name: finding_frozen_fixture_control_is_blind_to_resolution_faults
description: "A positive control that re-parses a FROZEN local artifact validates the parser and nothing upstream of it. When the fault is in how the input is CHOSEN or FETCHED, the control passes while the pipeline is broken — and its PASS is worse than no control, because it certifies the run and stops the operator looking."
symptoms:
  - "positive control PASS but every live row came back empty or n/d"
  - "control passes on a frozen fixture while real fetches return the wrong document"
  - "scraper silently started parsing a wrapper/index page instead of the data document"
  - "upstream API changed its file listing and the checks never noticed"
  - "all fields missing but status says OK-PARTIAL"
metadata:
  node_type: memory
  type: finding
  modified: 2026-08-27T20:30:00.000Z
---

**2026-08-27, OTTO.** A 10-D scraper feeding a registered cross-agent instrument ran and printed
**`POSITIVE CONTROL … PASS ✓`**. In the same run **every one of nine deals returned all-blank metrics**,
and the ledger upsert **overwrote four good historical rows with empty ones.**

The control was doing exactly what it was written to do: re-parse a **frozen, locally-pinned exhibit**
and assert a known value. The parser was fine. **The fault was one layer upstream** — the data source's
directory-listing endpoint had begun returning an **incomplete file list** that omitted the exhibit, the
resolver's filename heuristic matched nothing, and a **silent fallback** selected the wrapper document,
which contains no data table. The control could not see any of that, because **its input never travels
that path.**

**Why this is worse than having no control.** A missing control leaves an operator uncertain, and
uncertainty prompts a look. A **passing** control converts a destroyed run into a certified one. The
run's own summary line read as success, and the only thing that surfaced the problem was noticing that
the printed metric columns were empty.

**The generalisable shape.** A control validates the **stage it exercises** and creates confidence about
the **whole pipeline**. Pipelines have at least three separable stages —

1. **Selection / resolution** — *which* artifact am I about to read? (URL built, endpoint queried, file
   chosen from a listing, ticker mapped to an ID)
2. **Retrieval** — did I actually get it? (status, auth, redirect, truncation, cache)
3. **Interpretation** — did I read it correctly? (parse, units, schema)

**A frozen-fixture control exercises only stage 3.** Stages 1 and 2 are precisely where an upstream
provider's silent change lands, and they are the stages whose failures **look like empty data rather than
like errors**.

**How to apply:**

1. **Ask what your control's input path is.** If the fixture is local, pinned, or cached, the control is
   a **parser** test. Say so in its label — `PARSER CONTROL: PASS` claims far less than
   `POSITIVE CONTROL: PASS`, and the honest label is what stops the false certification.
2. **Add a live-path control alongside it.** Fetch one known artifact **through the real resolution and
   retrieval path** and assert a known value. It costs one request and covers stages 1-2.
3. **Treat "all fields missing" as a FAILURE status, never a partial one.** A record that resolves none
   of its headline metrics is a pipeline failure wearing a data costume. Give it its own loud state and
   **refuse to let it write.**
4. **Never let a failed read supersede a good stored value.** Last-write-wins silently assumes the newest
   write is the better one; a failed parse also wins. Guard the write, not just the read.
5. **Kill silent fallbacks in resolution code.** "Couldn't find the right file, so take the first
   plausible one" is the mechanism that turns an upstream change into wrong data instead of an exception.
   **Raise.** Substituting a different artifact is the failure, not the recovery.
6. **When a provider is the upstream, assume its listing/discovery surface can change independently of
   its content surface.** Here the exhibit was still served at its URL with a 200 — only the *listing*
   stopped mentioning it. Content reachable + index incomplete is a real and silent combination.

Sibling of [[finding_instrument_reports_clean_against_the_wrong_reference]] (there the referent was
wrong; here the referent is right but *unreachable by the path under test*) and of
[[finding_test_the_guard_not_just_the_guarded]]. Also the tooling limb of
[[finding_adoption_is_not_validation]]: the control had been consumed, trusted and consistent for weeks,
and had never once been asked what it could not see.
