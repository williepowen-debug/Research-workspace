# FRI 7/10 CAPITAL GATE — BRENT sustain-verdict spawn packet
**Built:** 2026-07-09 ~16:45 ET (pre-staged the night before, per SCRATCH entry-point 0)
**Fire when:** Friday 2026-07-10, AT/AFTER the ICE Brent Sep-26 (LCOU26) official settlement ~14:30 ET. NOT before; NEVER off an evening spot fetch.
**Gate row:** `PROME/GATES.tsv` GATE-BRENT-SUSTAIN. Confirms → BRENT deploy proposal → Will [Approve] + live broker book. Denies → revert energy tail to fragile-watch.

---

## PROME pre-spawn checklist (do these BEFORE launching)
1. Pull the Friday LCOU26 settlement independently (FORGE `BZ=F` proxy + WebSearch for the official ICE settle) — PROME verifies BRENT's graded print against a primary before ANY canon write (verification tier: gates capital).
2. Scan the tape for fresh Friday leg-prints (war-risk quotes / JWC-P&I news / transit counts) — flag any found in the spawn prompt so the Opus spawn doesn't miss a countable leg. **Baselines to beat (HAWK 7/9: both are PRE-EVENT vintage):** Hormuz transits 34/83 [PortWatch as-of 7/5, before the 7/6-8 attacks] · war-risk "8x pre-crisis / 6 clubs withdrawn" [tagged pre-existing, not post-damage]. A print is FRESH only if Friday-dated AND post-dating these; re-citing either vintage = non-countable per the ratified spec.
3. Check `AGENTS/HAWK/outbox/2026-07-09_to-PROME_russia-two-front-read.md` landed (spawned 7/9 eve) — carry its verdict line into §HAWK-read below if not already filled.
4. Confirm Will is available for a possible [Approve] window post-verdict.

---

## SPAWN PROMPT (BRENT, model=Opus — capital-gating exception under the tiering plan)

You are BRENT, the oil/energy agent in Will's fleet. PROME spawned you. Today is Friday 2026-07-10, [TIME] ET — the LCOU26 official settlement (~14:30 ET) has printed. Repo root: /home/willi/Research-workspace.

BOOT-READS (subagents auto-load nothing — Read by path, in this order):
1. `AGENTS/BRENT/CLAUDE.md` (domain rules)
2. `AGENTS/BRENT/STATUS.md` (your state: Thu-leg + spec-ratification note)
3. `AGENTS/BRENT/outbox/2026-07-08_to-PROME_decoupling-crack-adjudication.md` — YOUR memo: the 7/8 RE-ARM adjudication + the **7/9 SPEC-RATIFICATION ADDENDUM (`2843c921`) — the addendum is the BINDING spec for today's grade.**
4. `AGENTS/RED/outbox/2026-07-08_to-PROME_chg041-grade-sustain-redteam.md` — RED's red-team (the bull steelman at full strength + the 3 fixes your addendum ratified).
5. `AGENTS/HAWK/outbox/2026-07-09_to-PROME_russia-two-front-read.md` — HAWK's Russia two-front read (see §HAWK-read summary below).

TASK: grade GATE-BRENT-SUSTAIN. The ratified spec, restated (your addendum wins on any drift):
- **Graded print:** ICE Brent front-month **Sep-2026 (LCOU26) official settlement ~14:30 ET Friday** — no roll before grading; never an evening spot fetch.
- **CONFIRM** = settle **>$75 both sessions** (Thu ✅ PASSED: settle $76.01, no settlement round-trip <$74) **AND ≥2 FRESH legs** from **{war-risk ≥0.2%/transit · transits ≤~18/day or liner Cape re-route · P&I club/JWC withdrawal-or-relisting}**. The sanctions leg is **DOWN-WEIGHTED** — near-auto pass, supporting only, can NOT be one of the two binding legs. A leg with no Friday-dated print = **NON-COUNTABLE**, not presumed-held.
- **DENY = complement of CONFIRM** — level fails, OR settlement round-trip <$74, OR <2 fresh countable legs. No undefined middle; the test MUST return a verdict. Level is necessary-not-sufficient. Sanctions-only-fires Friday = DENY by construction.
- **★ Two-root contamination flag (weigh consciously):** Russia's Saratov refinery halt + state diesel-export ban [intake 7/9, Reuters/Guardian] are supply-bullish from the **RUSSIA root**. If Brent holds >$75 partly on Russia news, the LEVEL leg passes without the IRAN mechanism sustaining — the Iran-specific fresh legs are the filter. State explicitly in the verdict how much of Friday's tape you attribute to each root.
- Web tools NOT autoloaded — ToolSearch "select:WebSearch,WebFetch" first. Verify leg prints against primaries (Lloyd's List / JWC / TankerTrackers / EIA-PortWatch class sources), source + date every claim.

VERDICT CONSEQUENCES:
- **CONFIRMS** → write the deploy proposal SHAPE (instrument class, sizing logic under the $500/card max-loss, entry conditions) but NO strikes/prices from memory — live chain at fire-time; proposal goes to Will [Approve] + live broker book (rule #4). Rule #6 note (calls into green) must be addressed explicitly.
- **DENIES** → revert language: energy tail ACTIVE → fragile-watch; state which legs failed and what would re-arm it; hand PROME the HEARTBEAT amendment line (PROME writes HEARTBEAT, not you).
- Either way: CHG-041 cross-ref — RED grades it FINAL today off your verdict (separate spawn); make your leg-by-leg table clean enough for RED to grade against.

DOMAIN RULES: tables > prose · numbers > narrative · source + date every claim · no files outside `AGENTS/BRENT/`.

DELIVERABLES, exactly:
1. Verdict memo → `AGENTS/BRENT/outbox/2026-07-10_to-PROME_sustain-verdict.md` (leg-by-leg table w/ freshness + root attribution + verdict + consequence) + STATUS.md update.
2. Pathspec commit from repo root (`cd "$(git rev-parse --show-toplevel)"`, pre-commit `git status -- AGENTS/BRENT/`, add+commit specific files only, never `-A`/`.`). Do NOT push.
3. Final message to PROME ≤200 words: VERDICT first word, then the leg count, root attribution one-liner, file path.

Deliver your result (final message + file) as your final action before idling — do not idle without delivering.

---

## §HAWK-read (delivered 7/9 eve — `AGENTS/HAWK/outbox/2026-07-09_to-PROME_russia-two-front-read.md`, PROME spot-verified vs Moscow Times 7/7+7/8)
- **Separate root, ZERO Iran-ladder contamination** — none of HAWK's 5 CONFIRM-D discriminators touched; ladder stays B12/C42/D46, convergence ~35/50 unchanged.
- **Step-change, but scoped to the REFINING/PRODUCTS axis only:** Omsk (Russia's largest, ~75% of plant capacity down 7/6) + Saratov + 2 Tatarstan sites + a products-pipeline station, all hit in 72h → sovereign diesel-export ban through 7/31; global diesel benchmark +~13% Wed. **Crude-export infra (Druzhba/Baltic/Novorossiysk) UNSTRUCK** — HAW-15 open-not-failed.
- **Sharpens the two-root flag for the verdict:** the Russia shock is products/diesel-side, not crude-supply-side. If Brent holds >$75 on Russia headlines, that's neither the Iran mechanism NOR even Russia crude supply — one more reason the Iran-specific fresh legs do ALL the binding work. Attribute the tape's roots explicitly.
- **Next tell (BRENT's call per HAWK):** targeting pivot from products to actual crude-export infrastructure would flip HAW-15 + Brent flip-trigger #2 — if a pivot headline lands Friday, name it in the verdict as a separate-root escalation, still not an Iran leg.
- Correlation fact for the routing list: two independent supply shocks (Hormuz/Gulf + Russia refining) now stress the same commodity complex — HENRY/LIQUID input, not a ladder input.

## §Other 7/9-eve inputs for the spawn prompt
- **ORACLE cross-check (7/9):** "US blockade on Iran" market 48.0% ($210K vol, real depth) vs HAWK ladder D46 — CONVERGES, KL≈noise. No resolution-matched market exists for the sustain test itself (coverage gap, not a dislocation). `AGENTS/ORACLE/DIVERGENCE_2026-07-09.md`.
- **MARCO ES-MARCO-08 contamination flag (7/9, Will-routed):** MARCO's produce-vs-pump CPI test (due ~7/15) assumed the pump-relief window holds — the 7/8 re-arm may close it early. Informational for BRENT: a CONFIRM verdict feeds CARL's pass-through AND invalidates MARCO's test assumption; note it in the routing list of the verdict memo (MARCO owns the re-spec).

---

## Same-window companions (Friday, after the BRENT verdict)
- **RED (spawn after BRENT delivers):** grade CHG-041 FINAL off the verdict — CONFIRM → RESOLVED-CONVERGED (direction vindicated, magnitude oversized); DENY → reopens the structural-decoupling debate on harder terms (2nd failed tail test). Point it at BRENT's Friday memo + its own 7/8 memo Part 1.
- **10Y close (arm-#2):** ≥4.50 close → 4-of-5 (completes Mon 7/13, day before CPI); <4.50 → full reset. ^TNX at 4PM, verify vs DGS10 when posted. BOND co-ratifies the consecutive-run semantics if spawned (VX-BND-05 is BOND's framework).
- **PROME canon writes post-verdict:** GATES.tsv GATE-BRENT-SUSTAIN row → RESOLVED w/ verdict · HEARTBEAT amendment · SCRATCH/STATUS/ACTIVE_DECISIONS energy rows · then NEXUS re-anchor (Opus) into CPI week (SCRATCH entry-point 2).
