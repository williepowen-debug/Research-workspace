# Codex cross-vendor red-team — Friday decision-rail specs (2026-07-09, pre-verdict)

**Reviewer:** OpenAI Codex (2nd run of the cross-vendor lane). **Scope:** GATE-BRENT-SUSTAIN + TRY-FIRE-004 specifications — the rail graded Fri 7/10 post-close (first capital-deploying gate in weeks). Read-only; spec attack, not market opinion.
**PROME verification:** F1/F2/F5 confirmed against the live files; F9 confirmed non-biting-today (streak unbroken → both semantics agree). One process note: this agent initially idled WITHOUT delivering (first delivery-contract violation of the day — from the lane that doesn't read our playbook); delivered on chase. Bake an explicit "your final message must contain the full findings" line into future Codex prompts.
**Disposition (Will-approved same evening):** F1-F4/F7/F8 → BRENT spec-ratification addendum (Opus spawn, 7/9 PM, pre-registered before Friday tape). F5/F6/F9/F10 → TERRY card patch (Sonnet spawn, same evening; card stays ALIVE re-scoped to the inflation/term-premium channel per Will). F11 → folded into BRENT addendum (boundary directions). PROME fixes its own GATES.tsv "close basis per RED" row (recommendation had been recorded as ratified) once BRENT's addendum lands.

## Findings (severity-ranked; full text in the session record)

- **F1 🔴 — round-trip <$74 basis (intraday vs close) unratified.** BRENT memo silent; RED memo only recommended close-basis; GATES.tsv/SCRATCH recorded it as decided. Verdict-flipping on a $75.02-close-after-$73.90-wick tape. → BRENT ratifies settlement basis.
- **F2 🔴 — CONFIRM/DENY not jointly exhaustive.** DENY required round-trip AND sanctions walk-back (<48h) — un-triggerable while the 7/17 wind-down keeps sanctions nominally in force → the most-likely bearish path (slow bleed, no walk-back) returned NO verdict. → DENY redefined as complement of CONFIRM.
- **F3 🟠 — "Fri close" named no contract/settlement print** (ICE front-month settles ~14:30 ET; grading was scheduled "post-US-close" against spot fetches). → graded print named.
- **F4 🟠 — leg observability:** sanctions leg = near-automatic pass (freebie); war-risk + transit legs lag with possibly no fresh Friday print; no stale-leg rule; BRENT self-grades its own gate. → freshness rule: no-fresh-print = non-countable; freebie leg dispositioned explicitly.
- **F5 🟠 — TRY-FIRE-004 kill-line written card-global, applied arm-local — and the "clean 7/9 print" disarm literally FIRED today** (77.74% indirect). Substantive half: the card's demand-hole thesis leg died with BOND's grade while arm-#2 rides the surviving oil/term-premium channel. → invalidations scoped per-arm; thesis re-scoped two-channel; Will ratified keep-alive.
- **F6 🟡 — arm/disarm not mutually exclusive, no precedence/latch rule.** → disarm-dominates + latch added.
- **F7 🟡 — ">$75 both sessions" had no Thursday grading step.** → Thursday leg graded in BRENT's addendum (7/9 settlement ≈ $75.89 = PASS, PROME pull; BRENT ratifying from own source).
- **F8 🟡 — two legs lack numeric thresholds** (transits "drop" to what; P&I observable unnamed). → thresholds added in addendum.
- **F9 🟡 — arm-#2 run-vs-count drift** ("5 consecutive" card vs "N-of-5" ledger/BOND STATUS). Non-biting while the streak is unbroken. → card pins consecutive-run + reset; BOND co-ratifies in Friday packet (VX-BND-05 is BOND's framework).
- **F10 🟢 — arm-#3 "TIC holdings down" fires on valuation, not flow** (yield-up month marks holdings down with zero selling). → respecified as TIC net transactions, comparison month named.
- **F11 🟢 — boundary edges** (exactly $75.00 fails a strict ">"; dealer "18–20%" range). → pinned in addendum.

## Lane verdict (2nd run)
RED's same-vendor red-team had pre-flagged 3 of these (basis, leg-lag, level-necessary-not-sufficient) — but **F2 (undefined middle) and F5 (self-contradicting card, disarm already fired) were new**, missed by two same-vendor passes. The cross-vendor lane's second run paid for itself on the highest-stakes artifact in the book, the night before it graded. Pattern to keep: red-team the rail BEFORE the verdict session, fixes pre-registered before the tape exists.
