# CHECK STANDARD — how a standing check earns trust (fleet build standard)

**Owner:** DAEDALUS · **Created:** 2026-08-11 (Will-approved 8/9 via PROME governance batch — mechanism 3 of the 7/31 governance rulings; §1 generalizes the `scripts/firetime_allowlist.tsv` precedent) · **Scope:** binds NEW standing checks at build time and existing `scripts/` checks at next material edit. Companion registries: `STRICT_TEXT.md` (output text) · `STATE_VOCABULARY.md` (state tokens) · `CHECKS.tsv` (the per-check register this standard is enforced through).

A standing check is only as trustworthy as its quiet runs. Every rule below exists because a specific fleet check violated it and the violation was measured — sources cited per rule.

---

## 1. Known-false-positive suppression = an expiry-dated REGISTER, never a pattern widening

Every standing check with recurring known-benign flags gets a register file (the `firetime_allowlist.tsv` form):

| Register row carries | Why |
|---|---|
| `artifact · flagged-token · expiry · date-added · reason-with-verification-evidence` | A future reader must be able to re-verify without archaeology |

- **Expired rows RE-FLAG themselves.** A clean quiet run therefore means *genuinely clean*, and the register doubles as a standing alarm. No permanent suppressions, by design.
- **Suppression-by-regex/pattern is FORBIDDEN** (PAT-035 enforcer-blindness: the next *genuine* instance hides behind the same pattern). Registration is per-instance and dated.
- **Registration ≠ suppression of a class:** a row that names a checker DEFECT (e.g. URL-as-path, fixed 8/11) carries "retire this row when the fix lands" — and the fix-shipper retires it (6 rows retired 8/11 on exactly this contract).
- **A malformed register row suppresses NOTHING and says so** — a broken allowlist must never hide flags (fail-loud, `load_allowlist` precedent).
- The cheapest edit that silences a flag must never damage correct text: **if the only way to clear a flag is to make a right row less right, the CHECK is defective** — fix the check, register the instance meanwhile (RED ML-RED-143, the two-day-range class).
- Riders that cite this pattern when built: HENRY leg-(g) child · `PUBLISHED.tsv` concept-matching known-FP handling (LABOR BD-09, ruled 7/31).

## 2. A check states its own PERIMETER in its output

`✓ CLEAN` over an unstated scope certifies nothing (finding_verification_zero_is_ambiguous; SAM's PyYAML outage printed CLEAN on a box where DM v1 could not run — ruled 8/7). Output names what was checked AND the known not-checked ("checked: market-data deps, 6 keys · NOT checked: messaging, agent-local"). A null result states what it searched.

## 3. No guard ships unverified (PAT-074, adopted 8/3)

Before a check leaves the author's desk: **(a)** its intended flag line was *watched printing* on a real capable case, and **(b)** its clean line was watched on a clean case. `py_compile` and `rc=0` are not evidence. Four instances in five days of guards certifying health they never checked preceded this rule; first use caught the fifth.

## 4. Truncation announces itself

Any output cap — display (`[:N]` lists) or **scan-scope** (checking only the most recent K values) — prints "`(+N more)`" / "`N older value(s) NOT scanned`". A capped list with no suffix tells its reader "that's all of them" (PROME 8/8: WILL_QUEUE reported 4 roll-off rows when there were 14; consumer_check's `keep[:5]` was silently narrowing its own scan). Scope-caps are the worse subclass: they change *what the check certifies*, not just what it shows.

## 5. On-FAIL, name the owner and the next move

A flag nobody can act on is alert fatigue. Each failure line carries (or the check's header names) the owning surface and the fix path ("restore recipe: MACHINE_LOCAL.md, the row naming the key"). Never a hardcoded pointer that fits only the first key it was written for (env_doctor "FRED row" defect, fixed 8/11). `CHECKS.tsv` gains a per-check on-FAIL column at the next register pass (PAT-084).

## 6. Failure-direction is chosen, and stated

Every discriminator biases somewhere. State which way: a missed URL is noise, a missed real dead pointer is a fire-path break ⇒ bias toward flagging (firetime URL guard skips ONLY when no repo entry of that name exists). A guard against a known FP class is a standing false-negative risk (finding_standing_guard_is_a_false_negative_risk) — which is why §1 forbids pattern-suppression and why an FP-class fix narrows the check instead of widening the skip.

## 7. Transient sources get ONE retry, and a cleared transient is still an EVENT (adopted 2026-08-15, PROME-routed off BRENT's 8/13 review; n=3 measured)

Any fetcher feeding a **graded or boot-read surface** must, on a first-pass failure (HTTP 5xx, timeout, `None`-shaped empty response): **retry once immediately** before either recording the source unavailable or silently keeping the prior value. Then:

- **Clears on retry** → use the fresh value AND **log the transient as an event** (a dated line in the fetcher's output or its owner's ledger — the class stays countable; it is never absorbed as if the first pass hadn't happened).
- **Persists through retry** → record `UNAVAILABLE` **loudly** (a printed flag naming the series, per §2/§5) — never a silent keep-prior. A retry-free consumer sees a *silent gap rather than an error*: the row just doesn't update, no rc fires, and downstream freshness checks read the stale value as the newest. Transient-and-self-healing is the worst shape precisely because nothing fails.

Measured instances (why n=3 earned a rule): 2026-08-13 BRENT — four FRED rows (`BAMLH0A0HYM2` ×3, `DHHNGSP`) threw 500/timeout on first pass, probed clean on immediate retry · 2026-08-12 PROME — `yfinance` `NoneType` ×3 + one FRED timeout, all cleared on retry · the `BZZ26` episodes (BRENT, prior sessions). This is the network-layer sibling of the mtime/staleness classes: the defect is invisible at the surface that inherits it. BRENT deliberately did NOT build a desk-local wrapper ("that fixes one desk and leaves the pattern live everywhere") — the rule is fleet-level by construction. Binds new fetchers at build time and existing ones at next material edit, per this standard's scope line.

## 8. A fetch tool's fallback must be visible in its default output, its artifact, and its exit code — RATIFIED (Will, 2026-08-17 verbatim "Ratify §8" — ruling record `AGENTS/DAEDALUS/inbox/processed/2026-08-17_from-PROME_WILL-RULING-check-standard-s8-RATIFIED.md`, committed same-hour `2efa4f2f0`; encoded PROVISIONAL earlier the same day off the SFG sweep, marker struck on the ruling)

Any tool that pulls external data and has a designed fallback (cache, last-known, prior-close, empty-dict, walk-back) must make the fallback **visually distinguishable from fresh success at every layer a consumer reads**:

1. **Default line carries served vintage + source-mode** — `✅ <thing> OK (LIVE 2026-08-17)` vs `⚠️ <thing> CACHED (2026-06, no live pull)`. A warning that exists only on stderr, in a docstring, or under `--verbose` does not count: 9 fleet wrappers delete stderr on rc==0, and non-verbose is the boot default. (Exemplars: `ofr_stfm.py` `[Final→…, then Preliminary]` · `chain_fetch.py` `(as-of <ORIGINAL pull time> (cached))`.)
2. **Any file the tool writes carries the same stamp** — 3 of the sweep's 16 hits overwrote their artifact with the degraded result, so the stale state outlived the run. (Exemplar: `h2a_pull.py` stamps `via=wayback | snap=<ts>` into the artifact header.)
3. **A distinct nonzero rc for "served, but not fresh"** — rc=0 was doing no work in 5 of 6 reader-3 CLASS-HITs. (Exemplar: `cot_gold.py` rc=3 stale-vintage WAIT.)
4. **A fetch failure must never render as a data verdict** (the INVERTED form — the sweep's most dangerous): "no results found", "status quo", or a sentinel-driven signal (`999.0x put-heavy` from a missing column) manufactured from an unreachable source. Distinguish CANNOT-REACH from GENUINELY-EMPTY before printing a negative (`finding_unfetched_is_not_unavailable`, `finding_count_what_published_before_reading_the_verdict`).
5. **Wrapper corollary (the layer above):** boot/wrapper scripts relay stdout AND stderr unconditionally and derive their summary verdict from **marker-present, never rc alone** — the 2026-08-16 WATT/VULCAN/MIDAS/FERT `run_alert()` contract, verified by execution (FERT live run: ⚠️ surfaced verbatim, verdict flipped to REVIEW rc=1). A wrapper whose ✅ keys on rc will print green beside the loud text it just relayed. **Vocabulary discipline (2026-08-17, WATT first-live-use — the guard's own inversion): ⚠️ is reserved for STATE-DEPENDENT degradation (something is worse than last run and needs attention); a STANDING caveat or by-design wall prints `NOTE:` and must NOT trip the marker verdict.** WATT wired this contract and its first run went REVIEW off three permanent ⚠️ lines its own fix had just added — all true, none actionable — converting silent-fallback-green into PERMANENT-RED, the same failure inverted. Fix the vocabulary, never weaken the guard: the first agent to add a standing caveat after adopting rule 5 will hit this.

Scope note: §7's retry rule handles the *transient* half; this section handles the *designed-degradation* half. Both exist because "nothing failed" and "nothing fresh was pulled" are different facts.

## 9. A shared check's exit code must be able to disagree with clean — RATIFIED (Will, 2026-08-17 EVE verbatim "approve" — ruling record `PROME/proposals/2026-08-17_eve-approve-batch-RULED-heartbeat-tag4-daedalus-consumer-batch-ask1.md` item 3, committed `ccf10de89`; verified at the artifact before this encode)

**Canon (ruling wording, verbatim):** *"A shared check's exit code must be able to disagree with clean — 0 clean · 1 findings · 2 cannot-certify; a consumer's verdict keys on rc-1-or-marker, never rc-0-as-proof-of-clean."*

- **Producer half:** an "alert, not a gate" always-0 contract is a standing silent-fallback-green exposure — every rc-keyed consumer renders ✅ OK over real findings, and the safe-to-wire rationale ("wiring it can't break a boot") optimizes the wrong failure direction. `2` (cannot-certify: misconfiguration, scope not covered, usage) dominates `1` when both occur. Origin case: `scripts/ledger_staleness.py`, whose MISCONFIGURED path *also* exited 0 — the defect was wider than its own flag said (record: `AGENTS/DAEDALUS/upgrades/LEDGER_STALENESS_RC_CONTRACT_2026-08-17.md`, PAT-110).
- **Consumer half:** verdict = rc-1 OR marker-present (§8 rule 5 keeps the marker channel authoritative; rc agrees with it, never substitutes for it); rc-2 = the check cannot certify its scope — treat as leg failure, never assume quiet. rc-0 alone is never proof of clean.
- **Contract-change discipline:** revising a shared check's rc contract means editing the producer AND every rc-keyed consumer in ONE batch — a producer-only ship re-creates the 8/16 marker-contract regression class (a stale finding rendering as boot FAILURE on every wired desk). Survey consumers BEFORE changing the contract.
- Scope: binds new shared checks at build and existing ones at next material edit, per this standard's scope line. §8 rule 3 is the fetch-tool instance of the same principle; this section is the general shared-check form.
