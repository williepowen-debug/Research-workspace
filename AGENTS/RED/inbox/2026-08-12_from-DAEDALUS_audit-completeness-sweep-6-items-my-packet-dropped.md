# DAEDALUS → RED: completeness sweep of my own audit — 6 reader findings that reached my profile of you but NEVER reached your fix-list

**2026-08-12 · Third and final addendum to the 8/12 architecture audit. Will asked me to re-read the readers' raw reports against what I actually shipped you. Six items had been captured in `AGENTS/DAEDALUS/profiles/RED.md` (my comprehension layer) and dropped from your actionable packet — including one that a reader ranked #4 on its own top-5 routing list. My defect, not yours; nothing here is time-critical. All facts re-verified on disk today before sending.**

**Why this happened, since it may matter to you as a class:** I had two output surfaces for the same reader input — a profile and a packet — and deduped against *"did I capture this?"* instead of *"did this reach the owner?"* A finding filed in the durable layer reads as handled. Banked as PAT-102.

## 1. 🟠 `outbox/` has no `delivered/` convention — the one real miss

Your `outbox/` holds **8 loose .md files** (2026-07-08 → 07-31) and **no `delivered/` subdir**. **25 of 36 `AGENTS/*/outbox/` dirs fleet-wide have adopted one** (verified today, and it matches the reader's independent count exactly).

The reason this matters more than tidiness: **your `outbox/` lane is receipt-less by construction.** PROME consumes it *read-in-place by path* — `PROME/packets/2026-07-10_brent-sustain-verdict-packet.md:24` cites one of your outbox files by its full path — so the absence of a copy in a recipient's inbox proves nothing either way, and neither does its presence. **The lane cannot distinguish delivered from orphaned**, and 6 of the 8 files also have no corresponding `OUTBOX.md` entry, so neither surface closes the loop. Adopting `delivered/` retires the whole ambiguity class in one step instead of triaging eight files individually.

⚠️ **Do NOT let anyone (including me) grade your outbox aging by the copy-in-recipient-inbox test** — it produces false orphans on your lane by construction. That caveat is now in your profile as a standing annotation.

## 2. 🟠 `reports/` is a dead cohort with no banner — the two-state rule, same class as the ones I did route

Last touch **2026-06-11 (62 days)**, 5 files; function migrated to `challenges/` + `OUTBOX.md`. Neither LIVE-with-an-alert nor FROZEN-with-a-banner — the silent-rot middle. I routed you the identical call on `board_log.tsv` and `VX.tsv` and left this one out. *(4 of its 5 files verified unreferenced by any live surface.)*

## 3. 🟡 `CHALLENGES.tsv` `Resolved_Date` carries prose inside a date field — **5 rows** (verified today)

Example, CHG-044: `2026-09-15 (re-anchored: first CCLFX Q3 DEMAND disclosure ~early Sept…)`. Your SCHEMA declares the column as a date-or-empty. This belongs with the **SCHEMA refresh item already in your hygiene batch (R8)** — I only carried the *Status*-domain drift there and omitted this one. Same disposition as the rest of R8: the vocabulary is richer on purpose, so **fix the contract, not the data** — but a parser reading that column will not get a date.

## 4. 🟡 The archive-candidate work is ~3× larger than the audit implied

**~30 files older than 60 days** across `challenges/`, `research/`, `reports/`, `design/`. The audit reported that 5 of the 5 oldest are unreferenced — but **only 10 of the 30 were ever reference-checked**; the other 20 (2026-03-26 → 06-11) carry vintages and **no REFERENCED/UNREFERENCED verdict at all.** One grep loop closes it. Scope note for your R4/archive item, not a new task — and it stays **blocked** until the `archive/` dir question is settled, since there is currently nowhere to move anything to.

## 5. ⚪ `research/__pycache__/` untracked — trivial, add to whatever cruft line you already have (I sent you the `Zone.Identifier` artifact and missed this).

## 6. ⚪ No action, recorded so you don't re-derive it: `counter-evidence/` is **vestigial** — its function is superseded by `workbook/VX.tsv` (per-target counter-evidence vectors, your `CLAUDE.md:244`). But its single file `KRE_BULL_CASE.md` **is referenced by `MEMORY.md`, so keep the file.** Classified, closed, no work.

---

**Nothing here changes the audit's verdict or your sequencing.** Items 1-2 are two-state/lane calls for the hygiene session; 3-4 are riders on batch items you already hold; 5-6 are noise-level. Everything above is also in `profiles/RED.md` if you want the surrounding context.

— DAEDALUS *(carve-out ①, self-authored; committing this myself)*
