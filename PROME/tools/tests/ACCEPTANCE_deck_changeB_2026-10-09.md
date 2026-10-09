# ACCEPTANCE — Decision Deck Change B + card-clarity items (Will's 2026-10-09 17:06 ET assignment)
**Written BEFORE any edit** (WQ-229; `decision_deck.py` is under the two-correction stop from L660 episode 1 and the L663 acceptance-first condition — this file is the required acceptance for THIS episode; L663's residue items stay THEIR OWN episode except where an AC below names one).
**Owner:** PROME (`prome-15`). **Authority:** Will 17:06 ET verbatim assignment (pasted, five numbered items, bounded: *"Keep this assignment bounded to those improvements; the remaining brainstorm stays backlog"*) + the ruled Change B spec (`PROME/proposals/2026-10-09_deck-options-and-grouping-RULED.md` §2d amendment + §3) — an R1 second-process-change overrun on Will's explicit word, disclosed at closeout.
**Baseline for the preservation diff:** scratchpad `deckB/baseline_owed.html` built from HEAD 4b6e8856a before any edit (18 option-fragment extract in `baseline_options.json`).

## Acceptance conditions (each testable; the feature's terms, not symptoms)

**AC-B1 — chips render (assignment 1 / Change B).** The Owed panel carries one chip bar above the first group heading: `All` + one KIND chip per category present among non-blocked rows (`Trade` · `Gate` · `Rule` · `Hands` · `Launch` · `Chore`; deterministic map from the queue's Type cell, mapping stated in a code comment) + one DOMAIN chip per distinct declared token in the sidecar's new optional 11th column `domains` (·-separated). Each chip shows its card count. No row text is ever classified by guesswork: a row with no declared domain simply carries no domain chip.

**AC-B2 — filtering is client-side and total-safe.** Tapping a chip hides exactly the cards that match neither the chip nor the pin rule (AC-B3); `All` restores every card; group headings whose visible set is empty hide with their cards; tab/панel behavior unchanged.

**AC-B3 — the ruled pin amendment survives verbatim in substance.** A card that (a) is due today or overdue, OR (b) whose Needed-by/Item text carries an explicit `HH:MM ET` clock, OR (c) whose Type is money-moving (`TRADE` / `[Approve]` / `BROKER`) renders `data-pin="1"` with a visible PINNED marker and **remains visible under EVERY chip, including a viewer's saved one; the chip filters only the rest.** (Ruling: §2d — "pinned at the top under every filter chip, including a saved one".) Pin computation is server-side at build.

**AC-B4 — saved filter per viewer.** The selected chip persists in localStorage (per view key), restored on load, wrapped in try/catch, and a saved chip can never hide a pinned card (the filter function exempts `data-pin` structurally, not by remembering to).

**AC-B5 — short card fronts (assignment 2).** For an explainer card the always-visible front is exactly: title · kind pill · due pill (+PINNED) · **If nothing** · **PROME rec** (as authored — caveats travel inside it verbatim) · the Change-A options list where one exists · the tap controls. `What it is` / `Why it is yours` (+ `If yes`/`If no` on non-options cards) move behind a `<details>` labelled *Background*; the raw-row `<details>` stays. No explainer text is dropped — only moved behind Expand.

**AC-B6 — exact deadlines with timezone (assignment 3).** When the row's Needed-by or Item text carries an explicit `HH:MM ET` clock, the due pill renders it (`due today · 2026-10-09 · 15:45 ET`). Otherwise the pill shows the date alone — **the build never invents a time of day.**

**AC-B7 — tap status pipeline (assignment 4).** The tapstate distinguishes three stages, each with a timestamp: ① *Recorded* (write ack; "awaiting PROME pickup"); ② *Received by PROME* (doc `consumed: true`) — names the pickup stamp when the doc carries one (`picked_up` / `pickup` / `consumed_at`, else "stamp not recorded") and states in the rendered text that **receipt is not execution** — the disposition lands at the next rebuild; ③ *Disposition recorded* — rendered ONLY when the doc carries `disposition` (+optional `disposition_ts`); the page never invents one. Store doc shape for WRITES is unchanged (Change A fields preserved); the new fields are read-optional. BOOT 3b contract note: pickup MAY now also write `disposition`/`disposition_ts`; nothing requires it yet.

**AC-B8 — staleness honesty (assignment 5).** The build stamp carries the `ET` label (header + panelbar), and the Owed panelbar states: figures carry their own observation dates; a freshly built page does not refresh them. The Change-A unit source line (owner path + §) is unchanged.

**AC-B9 — Change A preserved byte-for-byte where it matters.** On the same sources, the post-change build's option labels, texts and consequences are IDENTICAL to `baseline_options.json` (18 fragments); `validate_options`/`parse_options`/`offered_options` are not edited; the tap write document gains NO new written fields.

**AC-B10 — fail-closed paths unchanged.** The blank-deck refusal, the options-mismatch refusal and the full existing selftest still pass; selftest gains: sidecar header accepts 10 or 11 columns (8 retired only if absent live); ≥1 pinned card exists whenever a row is due today/overdue or money-typed; the chip bar renders when ≥1 non-blocked row exists.

**AC-B11 — rendered interactions verified before publish (assignment's verification clause).** `decision_deck_runtime.cjs` gains executable cases: chip filter hides a non-pinned non-matching card and NEVER hides a `data-pin` card (saved-filter restore included); consumed-doc-with-stamp renders stage-②'s "receipt is not execution" text; a `disposition` doc renders stage-③. All runtime cases pass in node against the PRODUCTION scripts.

**AC-B12 — reference page still storeless.** The existing harness case (reference view never opens a store) passes unchanged.

## Neighbours (WQ-229 — considered, one line each)
- **Ordinary:** AC-B1–B12 above.
- **Overlap:** `WQ_EXPLAINERS.tsv` gains an optional 11th column — consumers: `decision_deck.py` (adapts, header-zip already tolerant) and `prome_gate.py` (reads column 0 only — VERIFIED at prome_gate.py:1402 before this file was written). No other code consumer (`grep -rln --include=*.py` over PROME/ scripts/ FORGE/).
- **Wrong owner:** domain chips are PROME-declared convenience labels, never owner classifications — stated in the chip bar's title attribute; a wrong label cannot hide urgent work because pinning is kind/date-based, not domain-based.
- **Missing information:** no declared domain ⇒ no domain chip for that card (visible under All + its kind); no pickup stamp ⇒ "stamp not recorded"; no disposition fields ⇒ stage ③ absent, never invented.
- **Concurrent activity:** old store documents (every live tap) carry none of the new optional fields and must render exactly as today at stages ①/②; the write path is unchanged so a tap from a stale open page stays valid.

## Verification plan (ordered; run before publish)
1. `python3 PROME/tools/decision_deck.py --selftest` (extended) — PASS.
2. `python3 -m pytest PROME/tools/tests/test_decision_deck_split.py -q` — PASS.
3. `node PROME/tools/tests/decision_deck_runtime.cjs < <(extractor)` (extended) — PASS.
4. Build to scratchpad; AC-B9 fragment diff vs baseline — IDENTICAL.
5. Grep assertions: chip bar present; `data-pin` present on every due-today/overdue/money row; ET label on stamp; pinned-exempt filter in JS.
6. Independent Opus cold read (consequential Will-facing surface, WQ-229) — publish only after its ❌ are fixed or dispositioned; three-read ceiling, early stop per WQ-165.
7. Republish Owed (live page read first — this session has not yet touched the artifact), reference untouched (WQ-382 (a)).

## Closing section (2026-10-09 ~17:50 ET, prome-15 — the episode's record)
**State: IMPLEMENTED · TESTED (26 pytest + 33 subtests + the extended node harness + selftest 16 checks) · INDEPENDENTLY VERIFIED (read 3 of 3, coldread-deckB3: 0 ❌ · 10 ⚠️, verdict SHIP; a reproducible rebuild matched the reviewed page byte-for-byte less the stamp).** Episode reads: read 1 (coldread-deckB) 4 ❌ · 14 ⚠️ → all ❌ + 12 ⚠️ fixed; read 2 (coldread-deckB2) verified read-1 closed, found 3 NEW ❌ in the fix pass · 12 ⚠️ → all ❌ + 8 ⚠️ fixed; read 3 verified everything closed, 0 new ❌. Ledgers: session scratchpad `deckB/changeB_read{,2,3}_ledger.md`, quoted in the session transcript. decision_deck.py reached the two-correction stop at pass 2; the budget's final read followed; NO edits after read 3.

**AC re-cuts made during the episode (supersede the text above; read-3 ⚠️5's record):**
- AC-B3/AC-B6: the clock comes from the NEEDED-BY cell ONLY (read-1 ❌1 — Item-text stamps are not deadlines); zone-inclusive capture (ET/EDT/EST) rendered verbatim; an ellipsis marks further clock-like tokens in the cell.
- AC-B5: `If yes`/`If no` stay ON THE FRONT beside the buttons (read-1 ⚠️11); only What-it-is/Why-it-is-yours go behind Background, and ONLY when they carry no caveat marker — a MARKED caveat unfolds the whole card (read-1 ❌2, read-2 ❌1). **The guard is a MARKER set, not semantics** — FORWARD RULE: PROME marks any decision-relevant caveat in a sidecar what/why cell with ⚠️ or the word "caveat" (WQ-401 was marked at source this episode as the first application).
- AC-B1: chip counts cover ALL rows including blocked (blocked cards render under chips).
- AC-B7 clarification (read-3 ⚠️1): `recorded_as` IS the queue-record line — the disposition as PROME recorded it (BOOT 3b field names store-verified 10/9: consumed_at · consumed_by · recorded_as). Once stage ③ renders it, "receipt is not execution" is superseded by the actual record, by design; the caveat line covers only the consumed-without-record state.
- The ruled "at the top" (§2d) is implemented as pinned-first WITHIN each of the three ruled groups (the groups themselves are the ruled render spec's own structure).

**Declared residue (not fixed; read-3 numbering + carried):** r3-⚠️2 no harness case on the consumed_at+recorded_as doc shape · r3-⚠️3 non-ISO string stamps render "Invalid Date ET"; a Timestamp OBJECT reads "stamp not recorded" (latent; the store writes ISO) · r3-⚠️4 the selftest caveat regex is narrower than the render's (both err toward showing; the forward rule is homed HERE, not only in a comment) · r3-⚠️6 the SELFTEST's today is box-local (build/main are ET) · r3-⚠️7 case-variant ordinary domains render as separate chips; collision warnings travel under the `options_warnings` key · r3-⚠️8 the chip-bar/pill titles say "due" meaning due-today/overdue · r3-⚠️9 the chipnote renders only via build()'s pre-pass · r3-⚠️10 the en-CA Intl date-format assumption (fails toward no top-up, server pin unaffected) · carried from reads 1–2: stamp-clocks inside Needed-by cells remain a RULE question for Will (anchoring; today's live pills are correct) · "9:45am–10:30 ET" loses its window start · chip counts read as result size (chipnote discloses) · kind_chip substring brittleness · no pytest for the pinned-first sort (verified at the page by read 3) · the plain-card byte-identity guard is now a content guard (disclosed, wq-1 and wq-2 asserted).

