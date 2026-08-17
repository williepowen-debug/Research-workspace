# STE / Controlled-Language Ideas — Fleet Adaptation Assessment

**Date:** 2026-07-31 · **Requested by:** Will (YT transcript, https://www.youtube.com/watch?v=uJblcC4lKYw — ASD-STE100 applied to AI writing) · **Author:** DAEDALUS · **Status:** 🗄 **EXECUTED SAME DAY — both recommendations SHIPPED 2026-07-31 (Will-approved) and are now fleet canon**: `BLUEPRINTS/STATE_VOCABULARY.md` + `BLUEPRINTS/STRICT_TEXT.md`, cited by root CLAUDE.md § Output Canon. *(Corrected 2026-08-17, self-audit F22 — this line still read "ASSESSMENT ONLY — nothing built or wired," inverting the record for any fresh reader.)* Historical assessment below unchanged.

---

## 1. What the video claims (compressed, with his own numbers)

| Claim | Evidence he presents |
|---|---|
| Word blacklists ("no em-dashes / no delve") barely reduce slop | 4.36 → 4.21 violations/100w on Claude (−3%); the model routes around a blacklist |
| A checkable *system* works | Orwell's 6 rules −43%; ASD-STE100 distilled skill −74% (Claude); −50% on GPT (where the ban-list also worked −40% — the 3% was a Claude curve, not a law) |
| The rules that matter are machine-checkable | His linter counts sentence length, passive voice, phrasal verbs, marketing adjectives, semicolons; Boeing has shipped a 350-rule STE checker since ~1990 |
| STE's core moves | One word = one meaning (kills synonym rotation) · no stacked hedge-verbs · verbs not nominalizations · no marketing adjectives · hard sentence caps (20/25 words) · semicolon banned |
| Two modes | STRICT for procedures/error messages (wrong reading has a cost); FLAVORED for normal prose |
| Honest caveats | Fixes FORM not substance ("a linter can turn a hollow paragraph into a clean, confident hollow paragraph") · keep away from anything needing a voice · full compliance needs human judgment; only the mechanical subset is scriptable |

Method note: his own epistemics are fleet-grade — he ran the test nobody ran, base-rated the instrument on two models, and reported the result that weakened his headline (GPT ban-list −40%). The transcript is auto-generated and mangled ("slope" = slop, "cloudy" = Claude, "normalization" = nominalization).

## 2. Where the fleet already stands (don't rebuild what exists)

The fleet is **already on the right side of his central thesis** — system over blacklist:

- **Output Canon** (root CLAUDE.md, single home): *Tables > prose. Numbers > narrative ("$477.3B (+26% YoY)", not "grew significantly"). Source + date every claim — no naked numbers.* That is a checkable system, and "no naked numbers" already kills the worst finance-flavored slop (vague magnitude words).
- **Mechanism culture**: the fleet's whole arc (PAT-035/044/074, prome_gate, ledger_staleness, consumer_check) is "give the system a check it can be run against, not a discipline to remember" — his exact conclusion.
- **Prediction discipline** already outlaws hedging where it costs: a prediction must carry LEVEL + INSTRUMENT + WINDOW + confidence; a hedge-stacked claim can't be graded ([[finding_confidence_priced_against_thesis_not_letter]]).

So the import is NOT "adopt a writing system" — we have one. The import is two *specific* STE mechanisms we lack, plus one honest ranking caveat (§5).

## 3. Adaptation candidates, ranked by fleet incident history

### A. Controlled STATE-VOCABULARY registry (STE's dictionary idea, pointed at our real disease) — RECOMMEND

**The one-word-one-meaning rule has already bitten us, repeatedly, at the state-token level — not the prose level.** Measured today: **10 distinct tokens in live use for "this surface is no longer live"** — FROZEN (388 files) · SUPERSEDED (237) · RETIRED (195) · DEAD (155) · ARCHIVED (44) · DO NOT CITE (18) · OBSOLETE (16) · NOT CURRENT (12) · NOT MAINTAINED (11) · DEPRECATED (1).

Incident history (this is synonym rotation causing *enforcement failures*, not style complaints):
- **PAT-035** (7/4): `ledger_staleness.py` recognized only literal `FROZEN`; CARL's `⛔ RETIRED` and MARCO's `⚠️ NOT CURRENT` would have false-flagged. Fix = widen the recognizer.
- **PAT-059** (7/22): recognizer widened AGAIN (v3) after 18 false-FROZENs — the vocabulary kept drifting faster than the recognizer.
- The same class exists for *live*-state tokens (ARMED / FIRED / TRIGGERED / LIVE / OPEN) and resolution tokens (RESOLVED / GRADED / CLOSED / VOID / FAILED) — currently un-inventoried.

**What:** a small registry (one table, DAEDALUS-owned, in `BLUEPRINTS/` — canonical token per lifecycle state + the accepted-legacy variants each enforcer must recognize). New surfaces MUST use canonical tokens (blueprint + REGISTRATION_CHECKLIST line); existing files are grandfathered — the recognizer already handles them, we stop the *growth*.
**Why:** every new variant is a future recognizer widening or a silent false-negative. STE's insight applies exactly: where a machine reads the word, the word is an interface (PAT-069: parsed format = interface).
**Effort:** small — one grep inventory sweep + one table + 2 blueprint lines. **EV:** kills a defect class with n≥3 at spec time rather than recognizer time. **First step:** full token inventory (dead/live/resolution classes), draft registry, Will approves before any enforcer cites it.

### B. STRICT-mode rules for cost-bearing text — RECOMMEND (small, mostly consolidation)

His strict/flavored split maps cleanly onto a surface classification we already implicitly have:

| Surface class | Wrong reading costs | Mode |
|---|---|---|
| Script output/error messages · gate & threshold specs · PREDICTIONS rows · packet ACTION lines | Money, misexecution, ungradeable claims | STRICT |
| Thesis docs, research prose, audit narratives | Reader time only | FLAVORED (Output Canon as-is) |
| Will-facing synthesis (Telegram, dashboards) | — | VOICE — explicitly exempt, per the video's own caveat |

The fleet-specific argument for STRICT on packets is stronger than his aerospace analogy: **our packet readers are LLM sessions with limited context** — the modern version of his stressed non-native mechanic. We have the incident class already: [[finding_backstop_redelivery_is_a_paraphrase_not_a_copy]] (paraphrase drift corrupts instructions), [[finding_triage_summary_compression_inversion]] (compression inverted a meaning). A packet's ACTION lines in strict form (one instruction per sentence, active voice, named actor, no stacked modals, numbers with unit+source+date) is cheap and directly reduces misexecution.

**What:** a ~10-line STRICT ruleset (his "tiny ruleset gets 90%" option — NOT the 900-word dictionary) added to the blueprints' output sections + packet template. Much of it is restating existing canon in checkable form; the genuinely new lines are: one instruction per sentence in ACTION blocks · no stacked modal/hedge verbs on any claim carrying a number · verbs not nominalizations in instructions.
**Effort:** small. **EV:** moderate — misexecution reduction is real but the incident base rate is lower than class A's. **First step:** draft the 10 lines, Will reviews.

### C. Advisory slop-linter — DO NOT BUILD NOW

A `violations/100w` linter for fleet surfaces is buildable in an afternoon, and I recommend against it today, for three reasons from our own record:

1. **A mechanized style screen is a false-positive generator aimed at the best-documented agents** — the exact failure mode I logged 7/30 on the compound-gate screen ([[finding_deliberate_and_unnoticed_asymmetry_look_identical]]): from the condition alone, deliberate density and sloppy density look identical. STATUS files are *deliberately* dense (line caps push long, em-dash-heavy sentences); a sentence-length rule would flag the fleet's most disciplined surfaces first. PAT-031 already deferred line-level strictness once for precisely this FP shape.
2. **New enforcers need owners** (PAT-071). `scripts/` is unowned pending Will's 8/2 ruling; shipping another unowned checker into it recreates the FORGE class.
3. **Base-rate before anyone reads it** ([[finding_base_rate_the_instrument_before_its_event_table]]) — his own data shows the instrument is model- and surface-sensitive.

If A and B land and prose quality still bothers Will, revisit as an advisory, surface-scoped check with an owner — never a gate.

## 4. What NOT to adopt (explicit, so nobody adapts too far)

- **The 900-word dictionary / word whitelist** — wrong domain; finance vocabulary is the content, not the noise.
- **Sentence caps on STATUS/thesis files** — fights the 200–250 line caps, which force density; unwinding that trades a real constraint for a cosmetic one.
- **Anything on Will-facing synthesis voice** — his own caveat; also root canon (readable > terse).
- **Style enforcement as a gate anywhere** — advisory forever; see §3C.

## 5. The honest ranking caveat

His sharpest line applies to us with full force: **this fixes form, not substance.** Every costly fleet defect of the last month — stale mirrors, unowned surfaces, gates that can't fire, checks whose PASS means nothing (PAT-068..074) — would have sailed straight through a perfect prose linter. Class A is worth doing because it's *not actually a style rule* — it's an interface-vocabulary rule with three incidents behind it. Class B is cheap consolidation. Neither displaces the standing queue (TERRY S1 enforcer fix, `scripts/` ownership, Falsification Sweep 8/1, Production Review 8/5).

## 6. Proposal summary (What / Why / Effort / EV / First step)

| # | What | Why | Effort | EV | First step |
|---|---|---|---|---|---|
| A | State-vocabulary registry in BLUEPRINTS + checklist line | n≥3 enforcement failures from token drift; 10 dead-state variants live today | ~1 session | High — kills class at spec time | Token inventory sweep → registry draft → Will approves |
| B | 10-line STRICT ruleset for cost-bearing text (packets' ACTION lines, script messages, gate specs) | LLM readers misexecute paraphrase/hedge; 2 banked incident classes | ~half session | Moderate | Draft the 10 lines → Will reviews |
| C | Slop-linter | — | — | Negative today (FP generator, unowned enforcer) | Not now; revisit after A+B if wanted |

**Nothing here is built without Will's word.** If approved, A and B are blueprint-maintenance work and ride my existing blueprint-maintenance block; neither touches another agent's files.
