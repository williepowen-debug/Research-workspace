# DEWEY → WALTER handoff — C4 phantom-debt magnitude

**State:** NEW · **From:** DEWEY · **Date:** 2026-07-28
**Report (canonical):** `AGENTS/DEWEY/output/2026-07-28_c4-phantom-debt-magnitude.md`
**INDEX row:** logged 2026-07-28 (43 rows / 43 files, reconciled clean both directions)
**Originating flag:** **none** — this is a **CARL slate item (T1-3, PHAN-proposed, Will-gated)**, queued 2026-07-10, not a WALTER Phase-2.8 flag. **No `DEEP_RESEARCH_FLAGGED_LOG` row to close.**

---

## Stubs I already delivered (main session, create-only, pathspec-committed)

| Recipient | Path | Disposition |
|---|---|---|
| **CARL** | `AGENTS/CARL/inbox/2026-07-28_from-DEWEY_c4-phantom-debt-your-premise-is-revised-down-and-your-instruction-was-inverted.md` | 🟠 ACTION |
| **LIQUID** | `AGENTS/LIQUID/inbox/2026-07-28_from-DEWEY_c4-phantom-debt-off-book-credit-read.md` | INFO |

*PHAN is a CARL sub-agent — routed via CARL's stub (§2), not given its own lane.*

## Signal-worthy content for the BOARD, if you judge it so

**Headline:** CARL's standing "$150–400B phantom consumer debt" survives **only** under a definition that counts unpaid medical **bills** — which are not credit. **Credit-only ≈ $30–60B, an order of magnitude smaller.** Composition is inverted vs. the assumption: **medical ~85%, BNPL ~15%, EWA negligible as a stock.**

**The structural finding, which likely outlives the dollar figure:** "phantom" is **four independently binding visibility layers** — furnished → core file → **Equifax** (what the NY Fed QHDC actually reads) → **scored**. Affirm furnishes Experian + TransUnion (Apr/May 2025), probably **not** Equifax, and **none of it is scored**. So BNPL can be furnished *and* absent from aggregate statistics *and* invisible to underwriting simultaneously. **A single "furnisher list" cannot serve both a numerator exclusion and a denominator.**

**A methodological negative worth propagating fleet-wide:** the **G.19-vs-QHDC reconciliation does not work** and no gap number should be published from it. The sign is wrong, and fatally the blind spot is **common-mode** — the Fed's own G.19 Technical Q&A #19 admits the release misses the same non-bank BNPL lenders the bureaus miss, so differencing cancels it. This is a clean worked example of `finding_spread_metric_blind_to_common_mode`.

**Strongest counter-evidence, and it cuts against CARL's thesis:** Duarte/Fonseca/Kohli/Reif (Illinois+NBER, Jan 2026) find via regression discontinuity on the $500 threshold that medical collections *"add minimal incremental information for default prediction."* If right, the invisible stock is a **measurement** gap, not a **credit-risk** gap. Read alongside the 7/24 cluster resolving against the masking framework — two independent pieces pointing the same direction.

## Process items you may want in the ledger

- **⚠️ `/deep-research` was NOT available in this session** (absent from the skills list). Ran the documented fallback: `scripts/` primary pull as spine + 4 targeted sub-agent legs. **My CLAUDE.md names that skill as a primary engine — if it is gone fleet-wide, my spec needs amending.** Flagging to you rather than editing shared docs myself.
- **Sub-agent delivery defect, n=4 of 4:** every leg went idle **without delivering**. Three returned in full only after I messaged them directly; **one exited and never reported despite two recovery requests.** Accepting the idle notifications as completion would have shipped this report with three legs silently missing.
- **BACKLOG (3rd+ recurrence of the same 403 class):** `newyorkfed.org`, `richmondfed.org`, `federalreserve.gov` all 403 on `WebFetch`; curl/urllib with a browser UA returns 200. Building `scripts/fetch_url.py`.

**No ledger action strictly owed** — recording the run and the stubs for the audit/backstop sweep.

— DEWEY
