# BOND — Run Receipt

**Session:** 2026-07-28 (Tue, ~03:00–04:30 ET) — 5-day-dark boot into a live cluster (7Y auction 1PM today, FOMC decision 2PM tomorrow) → live-event override → Will-tasked **full mail drain, 12 items**. · **Overwritten at closeout.**

**Mail state at close:** general inbox **EMPTY** · WALTER lane **EMPTY** · outbox 2 new.

## Session summary

Booted 5 days dark (last session 7/23) and found **two state changes my own surfaces were blind to** and **one owed deliverable**. Wrote the time-critical artifact first — the 7/27 auction grade off TreasuryDirect primaries plus a **FROZEN 7Y pre-registration**, on disk ~10h before the print — then drained all 12 mail items. Net: **composite 12 → 14/35**, two vector upgrades, a ~25pp correction to the FOMC framing, a 26-day-stale credit row caught, and a specification error conceded as its author.

---

## General inbox (7 → all processed)

| File | Action | Why | Workbook | STATUS change | Outbox |
|---|---|---|---|---|---|
| `2026-07-23_from-HENRY_HEN-42-correction-adopted-joint-falsifier-registered` | **LOG_ONLY / SUPERSEDED** | Close-the-loop; registered my falsifier as JOINT on HEN-42. **Superseded within the week by its own subject** — that falsifier is now adjudicated MIS-SPECIFIED. | KB-089 | — | folded into HENRY reply |
| `2026-07-24_from-DEWEY_p3-china-external-financing-axis` | **LOG_ONLY / DEFER** | Correct and stands; scope set by PROME's 7/27 packet. Date-gated. | — | — | — |
| `2026-07-25_from-PROME_framespec-latent-bug-check` | **INTEGRATE (acted on same session)** | "Pre-register against the source that CARRIES the metric, not the event date." **Applied immediately** — the 7Y pre-reg is tail-free *because* TD publishes no when-issued. Also surfaced a live instance of the bug in my own docket. | VX-BND-09 | ECB row re-marked as an owned miss | — |
| `2026-07-27_from-PROME_batch3-dispatch-P3-reserve-currency` | **DEFER (hard gate)** | Start gate = first boot **on or after 2026-08-03**. Not started; docketed as a literal date. | — | CATALYSTS row | — |
| `2026-07-27_from-PROME_fedwatch-repulled-post-collapse` | **INTEGRATE + UPGRADE** | Conclusion right, reasoning fragile (rests on contested scrapes). Re-derived the same conclusion on FRED primaries. | **KB-091** | FOMC row corrected | → HENRY |
| `2026-07-28_from-HENRY_hen42-falsifier-misspecified-5y-tail` | **INTEGRATE + ROUTE_OUT** | 3 asks answered; conceded the spec defect as author; found an over-retraction on his side. | **KB-089/091/092** | matrix + catalysts | → HENRY |
| `2026-07-28_from-NEXUS_727-auction-split-raw-your-grade-owed` | **INTEGRATE + ROUTE_OUT** | Owed grade delivered off primaries; 3 relayed figures corrected. | **KB-089** | auction rows, VX-01 2→3 | → NEXUS |

## WALTER lane (6 → all processed)

| File | Action | Why |
|---|---|---|
| `SIG-W-20260725-013` basis trade $1.3T→$1.0T | **INTEGRATE — highest-value item in the lane** | Yields a **third hypothesis** for thin-cover-with-intact-composition, orthogonal to both sides of HEN-42. **KB-092** (logged ESTIMATE; LIQUID owns the call). |
| `SIG-W-20260725-016` CPI component vol ~1.45 | **LOG_ONLY** | Dispersion, not level. CARL owns. **Not carried as load-bearing** — per WALTER's own caveat it should be rebuilt from BLS, not cited. **KB-093** |
| `SIG-W-20260727-008` Fed T-bill RMP inoculation | **INTEGRATE-light** | The refutation *is* my surface (30Y >5% throughout the buying). Confirms standing canon: post-QT the Fed buys **bills** ⇒ no coupon/long-end bid. Malpass "IORB 5.4%" flagged stale (IORB 3.65). **KB-093** |
| `SIG-W-20260727-013` July hike is the live risk | **INTEGRATE — load-bearing correction** | Forced the ~25pp FOMC correction. **KB-091** |
| `SIG-W-20260727-016` HY OAS 279 + tranche pull | **INTEGRATE — load-bearing correction** | Forced the credit-staleness catch. **KB-090** |
| `SIG-W-20260727-018` GS/JPM AI-credit baskets 319bp | **INTEGRATE** | Credit market structure (my lane): synthetic/TRS execution ⇒ positioning builds faster than the cash float allows, either direction. **KB-093** |

---

## Files written

- **`analysis/2026-07-28_grade_7-27-2Y-5Y_prereg_7-28-7Y.md`** — NEW. 7/27 grade off TD primaries (n=250) + claim audit + falsifier adjudication + **FROZEN 7Y pre-reg**. Committed `7a18ec13` at ~03:00 ET, **~10h before the 1PM print**.
- **`workbook/KB.tsv`** — +5 rows (**KB-BND-089…093**). CRLF preserved; all rows 13-column-validated post-write.
- **`workbook/VX.tsv`** — 10 rows updated. **Score changes: VX-BND-01 2→3** (auction health, on the pre-registered `BTC<2.3` leg) · **VX-BND-02 1→2** (HY spread, on velocity).
- **`STATUS.md`** — state line, 11 dashboard rows, convergence matrix (**composite 12 → 14/35**), catalyst table, new BOTTOM LINE.
- **`docket/CATALYSTS.tsv`** — 7/27 resolved with the grade; 7/28 7Y added with frozen branches; **FOMC corrected and re-dated to 7/29 alone** (the old `7/28..29` span invited grading on day 1); 8/03 P3 start-gate row; credit recurring row 🟠→🔴; ECB row marked an owned miss.
- **`outbox/2026-07-28_to-HENRY_falsifier-was-mine-and-misspecified-plus-you-over-retracted.md`** — NEW.
- **`outbox/2026-07-28_to-NEXUS_727-grade-delivered-holding-with-a-marker.md`** — NEW.

## Corrections issued this session

| To | Claim | Correction |
|---|---|---|
| **Self** | HY OAS 275 `[CONF FRED, 7/2]` | **279 [7/24]** — carried 26 days. *Plausible-stale*: survived because the value sat between the 263 trough and the truth. |
| **Self** | FOMC "HOLD ~90% priced" (7/16 vintage) | **~65% hold / ~34% hike** — ~25pp error; at that level the *decision* is the event, not the guidance tone. |
| **Self** | Joint HEN-42 falsifier | **Mis-specified by me as its author** — DENY branch anchored on a 2Y tail a term-premium story structurally cannot produce. Non-firing ≠ pass. |
| **Self** | "FRED DGS 7/27 missing = tool artifact" | **Wrong** — verified against the CSV endpoint; FRED genuinely lacks 7/27 DGS/DFII while publishing the derived T10YIE. `fetch.py` was not stale. |
| HENRY | 5Y BTC "lowest in nearly five years" | **~3y10m** (Sept-2022); margin 0.01 |
| HENRY | FedWatch leg retracted entirely | **Over-retracted** — the instrument died, the claim didn't. Re-derived on FRED primaries. |
| NEXUS | "worst BTC since ~Sept 2022 (~5-year low)" | Date right, **label wrong** (~3y10m) |
| NEXUS | "14th consecutive tail" | **Unverifiable by construction** — TD publishes no when-issued. Not carried. |
| NEXUS | MOVE re-mark "names you" | **Not mine** — BOND's row already read 80.08 **[7/23]**, correctly dated. |

## Git

Commit `7a18ec13` (analysis + frozen pre-reg, pre-print). Closeout commit follows: KB/VX/STATUS/CATALYSTS/RECEIPT/SCRATCH + 2 outbox + 12 `git mv`s — all BOND-pathspec from root cwd. Auto-push via `scripts/safe-push.sh`.

## Owed / not done

- **7Y grade** — pre-reg frozen; **print lands 1PM ET today**, grade owed after.
- **BND-01** resolves 7/31 (HY 350 vs 279) → will resolve **FAILED**.
- **FR2004** — now **5 prints owed** (6/24, 7/1, 7/8, 7/15, 7/22); NY Fed API caps pre-2026 in-env. Carried 4 weeks — needs a workaround or a Will/PROME flag rather than another silent roll.
- **P3 Batch-3** — gated to 2026-08-03, docketed.
- **ECB GovC calendar** — verify from the ECB primary before re-docketing.
- **HENRY UST structural-demand corpus** (Mar-vintage) — still deferred.
