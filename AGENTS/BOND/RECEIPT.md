# BOND — Run Receipt

**Session:** 2026-08-21 (Fri) ~11:30 → ~12:xx ET · **Session 2 of the day.** · **Trigger:** Will — "boot up" · a VULCAN cross-session correction landed at boot and set the session's shape.
**Disposition:** 🔵 **SESSION STILL OPEN — this receipt was stamped PREMATURELY.** Will's instruction was *"boot up"*; I treated a peer correction as the session's work and ran the closeout tail before being tasked. **Shipping the fix fast was right — the false CCC clause was live on two other desks while I was looking at it. Declaring the session over was a separate act I bundled in without noticing.** Re-stamp at the real close. *(Work recorded below is complete and pushed:)* — **peer correction accepted in full; it then surfaced a larger error of my own, which was corrected, propagated-out and confirmed applied at both receiving desks.** Position **UNCHANGED** (TLT puts HOLD, no add). Composite **12/35**. **No thesis-level change.**

---

## 1. Boot

| Step | Result |
|---|---|
| `git pull` | Already up to date |
| `docket_check.py` | **rc=0** — 4/4 upcoming coupon auctions docketed (8/25 2Y · 8/26 1Y11M + 5Y · 8/27 7Y), CUSIP-keyed |
| `boot_recompute.py` | **rc=0** — no unguarded drift on the boot-unread surfaces (`TRADE.md` / `monitors/` / `NEXUS_BRIEF`) |
| PREDICTIONS DUE-scan | **`BND-15` only OPEN**, in-window through 8/29 — **nothing DUE** |
| WALTER lane | 0 |
| General inbox | 5 present, all deferred from session 1 (general inbox = a separate task) |
| Levels re-confirmed | 30Y **5.19** / 10Y **4.65** / 2Y **4.19** / DFII10 **2.35** [all 8/19] · HY **275** / CCC **1035** / IG **82** [all 8/20] · add-gate **15bp** · run **32 consecutive ≥5.00, 48 days in 2026** |

## 2. The correction received — accepted in full (`KB-BND-159`)

VULCAN: *"two independent pulls of ONE source is not a cross-check."* **Correct, and the framing was mine.** Session 1's `RECEIPT`/`SCRATCH` recorded that VULCAN *"independently pulled HY OAS 275bp [8/20], matching this refresh exactly."* **Both pulls hit `FRED BAMLH0A0HYM2`.**

- **What the agreement DOES validate** — kept, because it is normally invisible: the **FETCH** on both sides (no transcription slip, no stale cache, no mis-keyed series).
- **What it CANNOT do:** corroborate the **VALUE**. *Agreement between two readers of one source is a property of the readers, not of the number.*
- **Fixed on both surfaces; it never reached the 9/3 deliverable — caught one surface early.**
- ⇒ **STANDING RULE ADOPTED:** a BOND surface reporting agreement with another desk **names the series both sides pulled.** *(VULCAN adopted the same rule at its desk.)*

## 3. ⚠️ What that surfaced — my own error, larger (`KB-BND-162`, n=6)

Re-pulling the primary to verify a *different* figure exposed a false clause published in session 1: *"16 prior obs ≥1035, **every one of them April-2025**."*

| | count | dates |
|---|---|---|
| Apr-2025 | 12 | 2025-04-04 → 2025-04-22 |
| Oct-2023 | 2 | 10/30, 10/31 |
| Nov-2023 | 1 | 11/01 |
| Aug-2024 | 1 | 08/05 |

**Four episodes across three years — 12 of 16, not 16 of 16.** *(`BAMLH0A3HYC` · session closes · 2023-08-22→2026-08-20 · n=787 · cache-busted.)*

- **UNAFFECTED:** fresh 2026 high · not a series high · max 1137 (2025-04-07) · count 16 · all four declared parameters.
- ⚠️ **DIRECTION RUNS AGAINST ME** — four episodes is a **more ordinary** level than a single tariff-shock touch, so the correction **weakens** the escalation read. `VX-BND-11` holds at 3; 1100 is the registered line and nothing fired.
- **METHOD:** I declared four parameters and **computed the count**, then attached an **uncomputed adjective about that set's internal composition**. **Where the 16 observations SIT is a second computation wearing the first one's parameters.**
- **Also corrected:** *"IG flat in a 3bp band"* → `BAMLC0A0CM` **0.78 → 0.82 over 12 closes, a 4bp band drifting WIDER**. Replaced with a better-constructed contrast: **HY index DEAD FLAT 2.75→2.75 [8/05→8/20] while its own CCC tail ran +12bp** — same family, same provider, no denominator mismatch.

**Propagation + fix:** 8 live surfaces here · PROME's HEARTBEAT §3 tag · VULCAN's STATUS (adopted verbatim with attribution). Fixed **by PATTERN**, ⚠️ **and the first pattern had a hole** — bold markers hid `STATUS.md:8`, caught only by the residual re-scan. **The pattern pass is not the check; the residual scan is.** `KB-BND-155` → **CORRECTED**, Fact intact as the record (`KB-BND-139` precedent).

## 4. Reciprocal finding sent — fan-out is not replication (`KB-BND-161`)

VULCAN's *unreached-by-three* CDS record **verified at LIQUID's artifacts and checks out** — but it bundles two claims of different strength: **① ABSENCE is genuinely three-desk strong** (each failure to reach is an independent attempt against its own toolkit); **② LEVEL is not** — all three desks hold the 7/27 prints from **ONE WALTER dispatch** (`SIG-W-20260728-008`; `-002` additionally to LIQUID/VULCAN). **Three inboxes, one source.** VULCAN split it into two permanent lines. **Kept off Will's HELD US-sovereign-CDS item** — different reference entity.

## 5. CRWV filed RELAYED-PENDING-VERIFICATION (`KB-BND-160`)

VULCAN offered the **filing, not the figure** (CRWV Q2 10-Q, acc `0001769628-26-000366`, Note 16). **5.0→5.5 in three months, both recourse-guaranteed = +100bp; DDTL 4.0 non-recourse ⇒ Mar→Aug NOT quotable as +325bp.** **BOND has not pulled it and asserts nothing.** **Perimeter: neocloud, private/bank-syndicated ⇒ enters neither side of the hyperscaler long-dated public IG issuance share.**

## 6. Files written

`STATUS.md` (249 ln, at cap — 2 corrections inline, no lines added) · `SCRATCH.md` (rewritten) · `RECEIPT.md` · `workbook/KB.tsv` (+159/160/161/162; `-155` → CORRECTED) · `workbook/VX.tsv` · `docket/CATALYSTS.tsv` · `TRADE.md` · `NEXUS_BRIEF.md` · `monitors/CREDIT_PRIMARY_MARKET.md` · `MEMORY.md` (2 durable learnings) · auto-memory ×2 **extended, no new slugs** (`finding_crosscheck_with_free_parameter_validates_nothing` — same-primary case + fan-out corollary; `finding_verified_figures_do_not_verify_the_shape_claim` — third form, routed there by PROME).
**THESIS/CHANGELOG NOT bumped** — no new channel, no conviction shift, no threshold breach, no prediction resolution. Both corrections moved a **characterisation**, not a score.

## 7. Checks

`docket_check` **rc=0** · `boot_recompute` **rc=0** · `closeout_check` **rc=0 clean, 0 findings across both checks** · unavailability sweep clean (no undated claim) · mirror check clean (`BND-15` the only OPEN row and STATUS agrees; THESIS header `v1.1.6` consistent after session 1's fix; CATALYSTS ↔ docket agree) · TSV field-counts verified **whole-file** (13/13) · ledger nudge **N/A** (commit set includes STATUS **and** KB/VX/CATALYSTS).

## 8. Mail state

**In:** 5 deferred, unchanged (DAEDALUS · LABOR · REGINALD · VIOLET · PROME hyperscaler allocation ~9/3). WALTER lane empty.
**Out:** 1 packet → **VULCAN**, committed `496f2893d`, doorbelled, **confirmed applied in-session** (VULCAN `KB-108`). ✅ **DELIVERY VERIFIED BY CONTENT AT THE RECIPIENT, not by filename** — VULCAN consumed it and `git mv`'d it to `AGENTS/VULCAN/inbox/processed/` in `5bd99247b`, whose commit message quotes this packet's findings verbatim (the four-episode breakdown, the composition-adjective diagnosis, the IG substitute, the attribution caveat). **That is the strongest delivery evidence this desk has recorded** — it clears both the *"did it arrive?" ≠ "do they know?"* gap and the naming-convention false-orphan trap in one check.
**Cross-session:** VULCAN ×2 (correction in → accepted in full; reply out → applied both ways, no open items). PROME ×2 (ack in; CCC correction out → **HEARTBEAT §3 carried the false clause, corrected `b2f5ecdd1`, ~20 min exposure; PROME confirms nothing false reached Will**).

**One line:** *a peer told me my cross-check wasn't one, and checking that sent me back to the primary, where the thing I found wrong was mine and bigger — and it ran against my own thesis.*
