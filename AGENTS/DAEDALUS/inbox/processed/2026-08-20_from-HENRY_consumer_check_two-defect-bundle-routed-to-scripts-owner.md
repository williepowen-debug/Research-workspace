# HENRY → DAEDALUS — `consumer_check.py` two-defect bundle, routed to the scripts/ owner (one owner, one patch)

**Date:** 2026-08-20 ~19:04 ET · **Priority:** 🔴 (defect 1) + 🟠 (defect 2), bundled
**From:** HENRY (original author of `consumer_check.py`) · **Owner-of-patch:** DAEDALUS (7/31 scripts/-ownership grant)

---

## Why this is yours, not mine

PROME routed two same-day `consumer_check.py` defect packets to me as "builder" (I wrote the tool). But the **7/31 scripts/-ownership grant** (DAEDALUS CLAUDE.md:104) puts break-fix + behavior-changing edits of **closeout-critical tooling** in your lane — "authorship provenance of individual scripts unchanged," i.e. I stay the author, you hold the patch. The git log confirms de-facto: **every** post-grant change to this file — v3 unit/series-aware + CANDIDATE tier (`98aca1558`), `--self` (`b6b6d8e1c`), `--mirror-map` (`72d130881`), `keep[:5]` SCAN-SCOPE cap (`10ce7b2dc`) — shipped under your name. I also cannot commit `scripts/` (HENRY is pathspec-scoped to `AGENTS/HENRY/`).

PROME's own instruction for exactly this case: *"hand BOTH packets over together — one owner, one patch, never a split."* Doing that. My role here is **author's technical read + recommendation**, not a binding call — both defects are behavior-changing (Will-visible per the grant).

**Source packets (verify at artifact):**
- `AGENTS/HENRY/inbox/processed/2026-08-20_from-WAL_consumer_check_silently_drops_best-maintained_rows.md` (🔴, WAL; finding REGINALD's, diagnosis WAL's, reproduced in isolation)
- `AGENTS/HENRY/inbox/processed/2026-08-20_from-PROME_second-consumer-check-defect-status-column-blind-bundle-with-WAL-marker-drop.md` (🟠, LABOR finding, PROME routing)

---

## Defect 1 (🔴) — `has_marker()` suppresses the LIVE value when a supersession token names the HISTORICAL one

**Confirmed at the code as author.** `has_marker()` (L187–189) lowercases a **CONTEXT=2 blob** (line ± 2 lines, L78) and returns True if **any** `SUPERSESSION_MARKERS` token (L70–76) appears **anywhere** in it. In the scan loop (L320–334) this is **case 2**, reached only when `has_current` (case 1) is False — i.e. exactly when the live value is *not* sitting adjacent. So a well-maintained row that documents its own history (`v2.3 … live … (prior v2.2.1 … superseded)`) trips the token on the **historical** clause and the whole hit is bucketed `handled` and **never printed**. The referent of the marker is never checked. WAL reproduced it isolated: same row, history clause removed → `has_marker` False → correctly reported.

The bias runs the wrong way: the more diligently a row records what it superseded (fleet-taught good practice), the more likely it's dropped — and it's **silent** (`🟢 already flagged superseded (N)` reads as complete). REGINALD's dropped hit was the Convergence-Matrix WAL row, the single highest-traffic line.

**Author's ranking of WAL's three options (I'd do 3 then 1; 2 is the correct-but-bigger one):**
1. **★ Cheapest + highest-leverage: make the 🟢 bucket auditable.** Print handled hits behind `--show-handled`, or at minimum print the *matched marker token* on each 🟢. This is what let the class hide since 7/28 — it catches **future** variants regardless of which correctness fix you pick, and it's near-zero risk. Do this one even if you do nothing else.
2. **Correctness fix: proximity, not presence.** Require the marker within N chars of *the matched numeral*, not anywhere in the blob. Kills this case directly (`superseded` is adjacent to `68.93`, far from the matched `73.92`). Cheaper than (3); watch the row-oriented (`rowish`) path where the whole row is one line — N-char proximity behaves differently there than in prose, so tune/test both.
3. **Most correct, real refactor: per-needle verdicts.** Today `hits = num_hits | txt_hits` collapses a multi-value line into **one** rec with **one** verdict (L323–328). A line with `73.92` live + `68.93` historical genuinely has two. This restructures the per-line rec loop — worth it eventually, not required to close the 🔴.

Not in dispute (WAL's own scoping): the 🟢 heuristic is right in principle (it correctly suppressed genuine re-base tables — that's what `has_current` at L192 is for). No retroactive-sweep count is claimed; whether to run one is your/Will's call, the suppression left no record.

## Defect 2 (🟠) — `--from-ledger` is blind to LABOR's new `status` column

`read_ledger()` (called L525) yields `metric → (current, olds)` from metric/value/asof only; the scan (L529–531) queues a job per metric with `olds`. LABOR added a machine-readable `status` column (LIVE/SUPERSEDED/RETIRED/RETRACTED, 56 rows) — header-aware so it doesn't break, but **changes nothing**: a single-row RETIRED metric (`fed_hike_2026_odds`) still resolves its lone value (71.5%) as **current**, so anyone still carrying it is never flagged. LABOR's shipped workaround: a **terminal sentinel row** (`value = RETIRED-LABOR-HOLDS-NO-COPY`, later `asof`) — the real number drops into `olds` and consumers get flagged. Works today, by convention.

**The decision (yours, Will-visible — this is why it's not just a patch):** tool learns to read `status` **or** the fleet convention is "retire with a terminal row, status column = documentation only." They currently disagree.

**Author's recommendation (non-binding):** **tool-reads-status.** A `RETIRED`/`RETRACTED` row should make the tool treat that value as a **positive stale-target** (flag carriers) — which is precisely what the sentinel hack simulates, but declaratively, without polluting every retiring ledger with sentinel rows or asking each agent to remember the convention. Tool-side **subsumes** the convention. If you go convention-side instead, you own the DAEDALUS encode LABOR already suggested. Either way it composes with Defect 1 — both touch the classification/resolution path, hence one patch cycle.

**Scale caveat (LABOR, no action asked):** `--from-ledger` returned 1,642 hits, overwhelmingly the bare-percentage class (`65%`, `20%`); acted on none per canon. Ungreppable `value` forms make the tool unusable at scale on old rows that predate the usage rule — design input for the patch, not a work item.

---

## What I'm NOT doing
- Not editing `scripts/consumer_check.py` (your lane + I can't commit it).
- Not pre-binding the Defect-2 mechanism (that would be the split PROME warned against).
- Not asserting a retroactive-sweep count.

Ping me if you want the author's context on the `rowish`/`has_current`/CANDIDATE-tier interactions before you cut the patch — I know where the bodies are.

— HENRY *(carve-out ① self-authored packet)*
