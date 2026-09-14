# ACCEPTANCE CONDITIONS — `fetch.py` contract identity (WALTER's named ask, 2026-09-14)

**Written BEFORE any edit to `FORGE/tools/market-data/fetch.py`** (WQ-229 repair-completion discipline).
**Owner:** PROME (FORGE is PROME-standard). **Raiser:** WALTER, packet `2026-09-14_from-WALTER_fetch-py-reports-no-contract-month…`. **Reproduced at the artifact 19:2x** — `fetch.py price HOX26` → `ERROR 'currentTradingPeriod'`, exit 3; `HOX26.NYM` → `$4.77`.

⚠️ **These are the properties the repair must hold, in the defect's own terms — not a restatement of the symptom.** *"Report the contract month"* is too narrow; it does not say what happens when the vendor will not supply one, which is the case that matters most here.

## The conditions

1. **A dated contract symbol does not die on an opaque error.** Either it resolves, or it fails with a message naming the working form.
2. **Every futures price carries its contract identity, or an explicit UNKNOWN with the reason.** ⛔ Never a blank, never a guess, never a plausible default.
3. **Identity comes from vendor data, never inferred from the symbol string alone.** A symbol-parse succeeds on `HOX26` and is useless on `HO=F` — the continuous ticker is the whole defect.
4. **A continuous ticker resolves to the dated contract it is currently tracking.** Identity on a dated symbol is nearly trivial; identity on `HO=F` is the ask.
5. **The negative control holds: different months must return different values.** (L386's mandatory half.) An identity claim that cannot survive this is withheld, because a price match alone cannot separate *same contract* from *resolver collapsed onto one series*.
6. **Non-futures are unaffected** — equities, indices, FX keep current behaviour and output shape.
7. **The rendered table stays a parser contract** (PAT-069). Identity is additive.
8. **Both known-failing methods are named in the code** so nobody re-derives them: `shortName` truncates; price identity alone cannot separate same-contract from fallback.

## Neighbours CONSIDERED (WQ-229 — one line each, N/A justified)

- **Ordinary** — `CL=F`, `HO=F`, `RB=F`, `BZ=F` continuous; the main path. **TEST.**
- **Overlap** — the response cache (`_cache_get`) holds pre-fix entries with no identity field; a stale hit must not render as *identity absent from the vendor*. **TEST.**
- **Wrong owner** — N/A: `fetch.py` is PROME's under the FORGE grant, no other desk edits it; consumers read its output, which conditions 6–7 fence.
- **Missing information** — a ticker for which the vendor supplies no month (**Brent — measured, see below**). Must degrade to explicit UNKNOWN, never crash, never fabricate. **TEST.**
- **Concurrent activity** — WALTER is live (`walter-d9`) and stated it is flagging, not editing; `git status -- FORGE/` clean at 19:2x. Low risk, re-checked before commit.

## Measured before writing any code — and one of these changes the ask

| Symbol | Price | `shortName` | Identity? |
|---|---:|---|---|
| `CL=F` | 101.99 | `Crude Oil Oct 26` | ✅ **October** |
| `HO=F` | 4.7714 | `Heating Oil Nov 26` | ✅ **November** |
| `RB=F` | 3.1685 | `RBOB Gasoline Nov 26` | ✅ November |
| `NG=F` | 2.883 | `Natural Gas Oct 26` | ✅ October |
| `GC=F` | 4335.4 | `Gold Dec 26` | ✅ December |
| `ZC=F` | 534.0 | `Corn Futures,Dec-2026` | ✅ December — ⚠️ **a second, different format** |
| **`BZ=F`** | **106.36** | **`Brent Crude Oil Last Day Financ`** | ⛔ **NONE — truncated at 30 chars and the MONTH is what got cut** |

⇒ **`CL=F` is October while `HO=F` and `RB=F` are November — the desync, directly visible.** That is the finding the tool has been unable to state.

**Negative control — PASSES, and it is what licenses the dated form:**
`CLV26.NYM` 101.99 · `CLX26.NYM` 97.52 · `CLZ26.NYM` 92.80 — three months, three prices.
`HOV26.NYM` 4.985 · `HOX26.NYM` 4.7714 · `HOZ26.NYM` 4.551.
`BZX26.NYM` 106.36 · `BZZ26.NYM` 101.35 · `BZF27.NYM` 97.01.
⇒ `.NYM` symbols resolve **distinct** contracts; they are not collapsing onto the continuous series.

### 🔴 Two corrections to the ask as filed, both measured

1. ⛔ **There is NO `expireDate` field on this vendor path.** WALTER's *"emit `expireDate` at minimum"* **cannot be implemented as written** — the field does not exist in `history_metadata` for any symbol tested. What exists is the **name**, which carries the month for every energy contract **except Brent**.
2. ⛔ **Brent has NO month identity available at all.** `shortName` truncates identically for every Brent month, and `longName` (`Brent Crude Oil Last Day Financial Futures`) carries no month either. ⇒ For `BZ=F` the honest output is **UNKNOWN with a named reason**, not a guess. A price-match against dated symbols *is* informative here **because the negative control above rules out fallback** — but it costs extra network calls, so it belongs behind an explicit command, not in every pull.

## Out of scope, named so it does not creep

- ⛔ **No threshold or letter re-specced.** `HEN-46`/`HEN-F1` are HENRY's and are settling with Will (WQ-252).
- ⛔ **No spread guard inside `fetch.py`** — it does not compute spreads; consumers do. A fail-closed *spread* emitter is a real idea and belongs where the differential is built. Recorded, not built here.
- ⛔ **PROME adjudicates no desk's grade.**

## 🔴 INDEPENDENT REVIEW, 2026-09-14 19:2x — **THREE BLOCKING DEFECTS, ALL CONFIRMED BY PROME AT THE VENDOR, ALL FIXED**

A read-only reviewer was given the diff and these conditions and told to devise its own counterexamples rather than re-run mine. It returned **NOT YET FIXED**. Every finding was verified independently before fixing — none taken on the reviewer's word.

**❌1 — `contract_probe()` did not exist.** The header comment stated *"`contract_probe()` below runs that control and refuses to answer without it."* **There was no such function anywhere in the repo.** Condition 5 had been satisfied **by hand, in the markdown table above**, and nothing in the shipped tool re-ran it. ⛔ **A fabricated assurance sitting in the exact place a reader checks whether the control is mechanized** — `[[finding_record_of_an_action_is_not_the_action]]`, committed inside the file whose purpose was to mechanize a control. **FIXED by writing the function, not by deleting the sentence** — the mechanized control is the valuable half. The false sentence is left in place with its correction beside it, so the failure is legible rather than erased.

**❌2 — a live futures ticker rendered SILENT.** `contract_identity` short-circuited on `instrumentType != "FUTURE"`, and the renderer decided renderability from the resulting basis. **`CT=F` (Cotton) returns `instrumentType='ALTSYMBOL'` with a null `shortName` from this vendor right now** — confirmed by PROME's own sweep — so it printed with **no contract line at all, indistinguishable from an equity.** ⛔ This **passed the letter of condition 6 while defeating condition 2**, which is the condition that matters, and the code's own comment said silence *"would read as 'no roll hazard here' — the failure this exists to stop."* **FIXED:** renderability now comes from the ticker or the vendor's own type, never from parse success; `CT=F` renders `UNKNOWN (vendor-supplied-no-name (instrumentType='ALTSYMBOL'))`.

**❌3 — a live network failure was rendered as a CACHE problem with an inert remedy.** The `except Exception` path set only `asof`/`prev_asof`, leaving the contract keys **absent**, which the renderer reported as *"cached before 2026-09-14 — re-pull."* On a **fresh** pull the cause is false and the remedy does nothing; the reader concludes stale-cache artifact and uses the price. ⛔ The two facts my own comment insisted *"must not render alike"* **did**, and the cache branch won. **FIXED:** every live path now sets `contract_basis`, so an absent key means exactly one thing.

⚠️ **The reviewer's report truncated mid-❌3; the remainder — any further ❌/⚠️, its SOUND section, and the clean negatives on the month-regex and retry-visibility angles — is REQUESTED AND NOT YET RECEIVED.** Until it arrives the review is **incomplete**, not passed.

## Verification after the fixes

- **❌2 counterexample:** `CT=F` UNKNOWN-with-reason · `CL=F` Oct 2026 · `AAPL` no contract line (condition 6 held).
- **❌3:** live failure → `UNKNOWN (metadata-unavailable:JSONDecodeError)`; genuine pre-fix cache entry → `UNRESOLVED (entry cached before…)`. **Different facts, different renders.**
- **❌1:** `contract_probe('BZ')` → **IDENTIFIED, `BZ=F` is tracking `BZX26.NYM` (November)**, control `passed-distinct-prices` (106.36 / 101.28 / 97.01). **This is the answer Brent could not have from the name.**
- ★ **Two INDEPENDENT methods cross-validated, no shared input:** name-derived vs price+control — `CL=F` `Oct 2026` ↔ `CLV26.NYM`; `HO=F` `Nov 2026` ↔ `HOX26.NYM`. Agreement of two unrelated routes, not one route checked twice.

## 🔴 REVIEW ROUND 2, 19:3x — **TWO MORE BLOCKING, ONE WARNING. All confirmed by PROME before fixing.**

**❌4 — my "never cache a failure" fix covered ONLY my own reproduction.** The guard fired only when **every** ticker in the basket errored (`all(...)`) — i.e. the single-symbol case, `price HOX26`, and nothing else. **Every production caller is a basket** (`dashboard.py`; the `prices`/`all`/`snapshot` commands pass `list(ALL_PRICES.keys())`), so one bad ticker among thirty still cached its error for the full TTL. ⛔ **I fixed the row I had reproduced instead of the class — having cited `[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]` in this same file, in this same session, for a different repair.** **FIXED:** errored entries are stripped per-ticker; the good ones cache.

**❌5 — the month regex could emit a CONFIDENT WRONG MONTH.** `re.search` + first-match-wins + `[a-z]*` after the month token meant **`"Gasoline Octane 87 Dec 26"` → `('Oct 2087', 'vendor-shortName')`** — `Oct`+`ane`, then `87`; the real `Dec 26` later in the string never reached. A wrong month carrying a basis that reads as **fully sourced** is strictly worse than UNKNOWN, and it is the precise Nov-vs-Oct leg error this repair exists to prevent. ⚠️ **The reviewer was straight about its evidence: no live vendor name triggers it — mechanism unguarded, trigger unobserved.** That is a reason to fix it, not a defence. **FIXED at the mechanism, not the output:** the regex now matches only real month tokens (abbreviated or full) ending on a word boundary, so `Octane` cannot match at all. A plausibility bound (now−1 … now+10) and an ambiguity refusal are kept as defence in depth — ⚠️ **filtering an output would not have been enough: `"Gasoline Octane 26"` has no competing real month and no filter could save it.**

**⚠️6 — condition 1 held for only half of what it said, and missed an asset class.** `_BARE_DATED_RE` was anchored `[A-Z]`, so CME FX roots that lead with a digit (`6E`, `6J`, `6B`, `6A`, `6C`) never reached the retry and `6EZ26` still died on the opaque KeyError. **And condition 1's second limb — *"or it fails with a message naming the working form"* — had no implementation at all.** **FIXED:** both.

⚠️ **One finding I did NOT accept as stated, and the disagreement produced a better fix.** The reviewer proposed refusing whenever the name yields more than one candidate. My implementation resolves when exactly one candidate is plausibly dated — so `"Gasoline Octane 87 Dec 26"` now returns **`Dec 2026`**, which is the *correct* answer, rather than UNKNOWN. **My own test expectation was the thing that was wrong, not the code** — but chasing it surfaced the deeper fix above.

**One defect neither of us raised, found by my own regression:** `"Crude Oil October 26"` returned **`October 2026`** while `"Crude Oil Oct 26"` returned `Oct 2026` — **the same contract labelled two ways depending on vendor phrasing, which defeats the string comparison the field exists to support.** Labels are now normalised to the 3-letter form.

**Round-2 verification:** 18/18 name cases pass, including all 14 live vendor names, both reviewer counterexamples, and the two I added. Mixed-basket caching keeps good entries and strips errors; all-error and empty baskets cache nothing. `6EZ26`/`6JZ26` now gated; `--no-cache`/`AAPL` still rejected.

## Completion states — never merged

- **IMPLEMENTED:** ✅ yes, including the three review fixes.
- **TESTED (author's own):** ✅ all eight conditions, plus the reviewer's two counterexamples and the cross-validation above.
- **INDEPENDENTLY VERIFIED:** ⛔ **NO.** Across two rounds a reader found **five blocking defects and one warning**; none of the fixes has been re-reviewed, and the report is still incomplete (⚠️7 onward outstanding). **Passing my own tests establishes implemented, never verified** — `[[finding_adoption_is_not_validation]]`. ⚠️ **Round 2 is the argument for that rule: every round-1 fix was written carefully and round 2 still found two blocking defects in the same file, one of them INSIDE a round-1 fix.**
- **STILL UNRESOLVED:** the remainder of the review · re-review of the three fixes · `contract_probe` is unexercised on a root where the control should FAIL (no such case found live, so the refusal branches are reasoned-but-unobserved) · the fail-closed **spread** guard, which belongs in consumers and is not built.
