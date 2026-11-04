# ACCEPTANCE CONDITIONS — L557 residual futures evening-bar repairs

**Written before code edits:** 2026-11-04 10:30 ET, PROME on Kimi Code CLI. **Owner:** PROME / FORGE market-data tools. **Source:** DOCKET L557 and CATO's 2026-09-29 independent review EB1–EB3. **Class:** consequential repair to a shared market-data instrument and Will-facing dashboard.

**Review boundary:** the initial implementation ran under Will's no-agent instruction. His later bounded catch-up approval expressly directed independent reviews; a read-only reviewer completed the initial review and re-review, with no owner agents or research threads.

## Conditions

**EB1-A — invalid and stale timestamps never become a clean evening label.** Boolean, zero, negative, unparseable and unusable `regularMarketTime` values classify `unverified`; price is retained and change withheld. A last trade before the bar date qualifies as `evening-next-session` only when it is at/after 17:00 ET and the bar date is the next registered session after the last-trade date. A preceding daytime or too-old stamp is `unverified`, not evening.

**EB1-B — stale marks survive in both renderers.** A stale day row keeps `⚠stale`. A genuinely classified evening row loses the stale mark only when its bar is dated today or is the already-relabelled next trade date after today; stale evening rows retain the mark. Zero/boolean/too-old cases are visibly `unverified` in both renderers. Genuine adjacent-session evening cases retain their evening label and withheld change.

**EB2 — quote and chart must describe one coherent price observation.** `price_fetch` compares the displayed `fast_info.lastPrice` with `history_metadata.regularMarketPrice` before classifying a futures row. Missing, boolean, nonnumeric, nonfinite or mismatched chart prices classify `unverified` and withhold change. Matching values use a floating-point tolerance of `1e-9` only; this is a vendor coherence check, not proof that two coincidentally equal prints share a timestamp. The existing metadata-symbol identity guard remains in force. Equity, index and FX rows remain unchanged.

**EB3 — the session cutoff is always evaluated in ET.** Convert the epoch to `America/New_York` before comparing the 17:00 close and deriving the last-trade date. An 18:30 ET instant remains evening when the vendor timezone is `America/Los_Angeles`. Existing timezone fallback and unverified behavior remain intact.

**W1 — reason text names the actual failure.** A newer-than-expected prior bar is a prior-bar gap, not a missing prior bar; the dashboard uses the generic `⚠prior-bar gap, Δ withheld`. A non-session-date row no longer reuses the evening-span change reason. The older L462 acceptance text uses the actual CLI stamp form `MM-DD⚠eve→MM-DD`.

**REGRESSION — existing behavior stays intact.** Ordinary futures day rows keep price/change; genuine same-day and already-relabelled evening rows keep their labels with change withheld; equity after-hours rows are untouched; pre-L462 cache rows remain loud. Existing L409, contract-identity, contract-probe and L462 tests pass. The live dashboard still runs after the edit.

## Neighbours considered

- **Ordinary:** matching quote/chart prices on a day bar preserve the existing day result and change.
- **Overlap:** same-day 16:59:59 versus 17:00:00 ET, previous-day evening under the next trade date, stale evening bars, and pre-fix cache rows are covered.
- **Wrong owner:** code changes are limited to PROME-owned `FORGE/tools/market-data/`; tests and acceptance live under `PROME/tools/tests/`. No owner grade, gate, threshold or desk file changes.
- **Missing information:** absent/invalid timestamp, absent/invalid chart price, unresolved timezone and absent bar date fail loud with price retained and change withheld.
- **Concurrent activity:** no live owner is writing these paths in the available record; Git remains shared, so only exact pathspecs are committed. No cache wipe or external message occurs.

## Completion note

**IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · L557 RESOLVED.** The quote/chart join, ET normalization, adjacent-session bound, stale marks and reason-text repairs are in `fetch.py` / `dashboard.py`. Initial author runs passed 67 checks; the final independent re-review passed 69 checks (31 L462 · 10 L409 · 22 contract-repair · 6 contract-probe).

A real dashboard pull completed at 2026-11-04 10:39 ET. December Brent printed `$117.70 [10/30] ⚠stale ⚠prior-bar gap, Δ withheld`, preserving the stale price while withholding the unsupported change. No live evening session was occurring; new evening and failure behavior is fixture-tested.

The first independent review returned NOT ACCEPTED on a stale day-gap CLI mark and an infinite-epoch exception. PROME fixed both and added regressions; the same reviewer reran its counterexamples and returned ACCEPT, with no remaining scoped defect. Full evidence and failed results: `PROME/reports/2026-11-04_L557-independent-review.md`.
