# Helm split — independent CATO review

**October 3, 2026. Assessment:** keep the split, with a bounded owner correction for two independently reproduced medium-severity defects. Ordinary rendering preserves the selected records and substantially reduces the main page. But the two files read separate source snapshots (HS1), and a recovered docket-read error can restore the large page while reporting OK (HS2). Hosted navigation and fresh-session republishing remain unverified here.

## Scope and authority

Will explicitly asked CATO to check the delivered split after being told the episode reached its review ceiling. This is that named additional review, not a reset or authorization for further automatic rounds. Pin: `1b1d39deca707dba3b8458e06de1eb5230135804`; implementation `bece2cfba`; pre-edit acceptance `0c8c76239`. Inspected the renderer diff, acceptance/tests, closeout manual/runner changes, declared residue and publication ledger. CATO did not author the implementation.

PROME and WALTER are active in Will's windows. The tree was clean at the pin. Tests and renders ran in a git-archive extraction under `/tmp/cato-helm-review-gwx8g9sf`, including the neighboring test's known state write and the real feed writer. No owner code, tracked state, hosted page, permission or operational ledger changed. No agents launched or messages sent. CATO writes only this review, evidence and continuity.

## Verified ordinary behavior

- Six split tests plus ten desk-attention tests passed with `python3 -W error::ResourceWarning -m unittest tests.test_helm_size_split tests.test_desk_attention -v` in the isolated copy. The neighboring test wrote that copy's dashboard build file, not the live tree.
- Independently checked all 79 selected rows: page links and supporting-document IDs match; each row's own record preserves its escaped title, owner, state, completion terms and evidence. This is a per-record check, stronger than finding the text somewhere in the document.
- Compared legacy `desk_attention.render` with the actual pre-split module on the same sources: byte-identical. The author's legacy test compares the new implementation with itself; this separate comparison supplies old/new evidence.
- A real full render in the isolated copy called the feed updater once with `write=True`; dry runs used `write=False`. This verifies call behavior, not fleet-wide feed concurrency.
- Acceptance preceded implementation. CLOSEOUT steps 7/11 and runner 0b now describe the supporting file and listing prerequisite.

Same-source measurements at the pin, using `PROME/tools/measure.py` on generated files; longest lines were extracted to files and measured with the same instrument:

| Output | Bytes | Longest line, bytes |
|---|---:|---:|
| Pre-split renderer | 425,543 | 54,877 |
| Split main page | 205,265 | 6,131 |
| Supporting docket | 250,616 | 7,886 |

The new main page is approximately 48.2% of the old page. This reproduces the reduction, not the historical 419,929 → 205,457 pair from earlier builds. Total generated payload is larger; the intended saving is the mandatory main-page read. Demonstrated next-session benefit remains pending.

## Findings

### HS1 — medium: a single build can produce a link with no record

**Evidence:** `PROME/tools/desk_attention.py:256` reads pending work for the supporting file; `:315` independently reads it for the page. `PROME/tools/will_handbook.py:786–788` invokes those stages consecutively. One output writer does not make the input snapshot consistent.

**Reproduction:** the independent probe appended a valid pending PROME row to the isolated DOCKET after `write_docket` completed, before the attention render. The page linked `docket.html#L603`, but the supporting document had no `L603`. The full run returned 0, printed `handbook: OK`, and recorded no alerts. A separate injected newly pending row reproduces the same failure. This is a boundary counterexample, not evidence that today's hosted artifact is broken.

**Consequence:** a source change during rendering can make the two files disagree; a date boundary can likewise change membership between their separate date reads. The acceptance's concurrent-activity N/A rationale and unconditional no-dangling-link claim are too strong.

**Owner correction:** PROME should read/select the docket once with one date basis and pass those rows to both outputs, or detect source changes and discard/retry both outputs together. Checking only filename existence is insufficient.

**Closure:** source appends and pending/resolved transitions at the boundary cannot produce mismatched targets or records; retain ordinary and legacy behavior. No implementation by CATO.

### HS2 — medium: a supporting-read failure can return the large fallback as OK

**Evidence:** `will_handbook.py:726–727` returns None on errors returned by `render_docket_page`, without recording them. Its comment assumes the second read will reproduce the same error.

**Reproduction:** inject a ValueError on the first pending-work read and valid rows on the second. The full run returns 0 with no alerts and prints `handbook: OK … (no docket file — page in legacy form)`. The result is a 425,583-byte page, reintroducing the expensive read. A supporting-document-specific returned error has the same outcome. The fallback suffix is visible, but the failure reason and REVIEW status are lost. This differs from existing W2, where a stale supporting file survives failure.

**Owner correction:** preserve supporting-build errors through `alert('docket', …)` or equivalent. A legacy fallback may remain, but should carry its error and return REVIEW. Sharing the input snapshot also removes the two-read recovery ambiguity.

**Closure:** a first-read failure followed by recovery, and a supporting-render-only error, both remain visible with nonzero REVIEW status; ordinary success is unchanged. No implementation by CATO.

## Limits and recommendation

- **P4 pending:** no publication attempted. At the next fresh Standard closeout, view only the small page, list supporting files, republish the pair and record the outcome at existing L602.
- **Hosted navigation unverified:** the ledger records Helm v57 and docket.html in the hosted listing. Presence does not prove a relative link opens the right record. No authenticated Claude Artifact tool is available here; CATO checked local output and the receipt, not the live site. The next owner check should open a representative hosted record and its return link.
- Existing W1–W8 and read-3 W-a–W-d remain declared: line length depends on future data; stale supporting files can survive fallback publication; repository-relative source links are not established hosted links. No broad repair of these items was undertaken.
- The hosted listing records index.html at 206,009 B, separately from the earlier build figures. CATO did not infer a new discrepancy from differently labelled builds.
- The separate HEARTBEAT test defect and over-claimed log subject were read as recorded limitations, not independently repaired or fully re-audited.

**Recommendation:** preserve the size split; return HS1/HS2 to PROME as one bounded correction, then grade existing hosted-link/P4 conditions. No additional recurring review tier. This assignment ends with evidence and advice; implementation, sends and the broader backlog assessment remain unassigned.

## Reproduction and delivery

`probe.py` and `probe-results.jsonl` preserve the independent checks. Run only in a throwaway extraction of the pin containing PROME, FORGE, HEARTBEAT and the source files named by FORGE's management registry, with a `.cato-isolated-review` marker. Command: `python3 -B probe.py <isolated-root> <temporary-output-directory>`. The probe deliberately writes its source copy and feed state and refuses an ordinary checkout. Its assertions describe the defects at this pin and should fail after correction; convert them to positive regression expectations in the owner's suite.

Closeout checks: intended inputs verified readable before checking. Weekday check passed on exactly `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, `AGENTS/CATO/CONTINUITY.md`, and this report. Direct startup measurements: CATO AGENTS 6,465 B, CHARTER 9,921 B, CONTINUITY 7,476 B; root CLAUDE 24,199 B, USER 4,626 B, AGENTS 4,991 B — all below 32,550 B. Generic `read_cap_check.py --agent CATO` remains **CANNOT-EVALUATE**, rc 2, because it assumes a local CLAUDE.md; not counted as a pass. Orphan advisory clean; `git diff --check` clean. No ledger-nudge, auto-memory or consumer-figure change condition was triggered. Only the four exact CATO paths in this delivery are authorized for commit. The commit/push receipt is delivered in-session without another commit solely to record its hash.
