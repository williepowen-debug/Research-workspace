# HEARTBEAT Amendment #2 — dashboard projection (DRAFT, for plan review)

**Opened:** 2026-09-11 23:3x ET (`prome-e2`, LAPTOP) · **Owner:** PROME
**Why:** Amendment #2 (evening closeout 19:5x) has no dashboard projection, so `heartbeat_projection.py` raises *"each HEARTBEAT amendment needs one reviewed dashboard projection"*, the build fails, and — since the L339 repair — **both gates now block**. Restoring the projection is what returns the fleet to normal operation, and it is also the successful-build control that proves the new failure detection is not simply stuck on.
**Directed:** Will 2026-09-11 23:37 — *"restore the missing Amendment #2 projection, with the required review, then verify a successful build and matching receipt through the gate."*
**Drafted here and transplanted ONCE** (§ Session Process Controls: canon drafts live in the record, inserted into the target in one edit).

---

## 1. Facts established before drafting — probed, not assumed

| Fact | Value | How |
|---|---|---|
| Amendment #2 `source_sha256` | `4aa5a45938eef950b02f743f9e6d29de2139785d19f2ea690c433143c632e4d0` | `hashlib.sha256` over `AMENDMENTS.finditer`'s exact match, no trailing newline |
| Method validated | Amendment #1 recomputes to `c6ebe16a…`, **identical to the committed projection** | same probe, same run |
| Channel keys the schema accepts | `Energy` · `Rates` · `Credit` · `Japan / carry` · `Equity-vol` · `AI capex` · `War theaters + tariffs + housing` · `Metals` | captured from the parsed base |
| `blocking` | HEARTBEAT has **no** `## Blocking / Pending` section ⇒ base list is empty | `grep -n '^## Blocking / Pending' HEARTBEAT.md` → no match |

## 2. Scope decisions, with reasons

- **`one` — REPLACED.** Amendment #1's one-liner is the midday state; Amendment #2 is the evening state and supersedes the headline claim.
- **`channels.Energy` — REPLACED.** ⚠️ `apply_amendments` does `matches[0].update(replacement)`, so setting `body` **overwrites** Amendment #1's Energy body wholesale. That body ends *"Petroline: nothing fired; resolver to 9/25"* — now **false**. The replacement therefore has to carry forward the still-true facts from Amendment #1, or they silently vanish from the dashboard.
  ⛔ **This bullet originally ended "This is the one real authoring trap in this projection." That was FALSE and the plan review falsified it (⚠️5): `one` is a whole-string overwrite too**, so Amendment #1's CPI/HEN-44, TLT-delta, NEXUS C#2 and WATT P1 content also leaves the top line — surviving only in the Rates/Credit/War-theaters channel bodies. Loss of prominence, not of fact, but the "one trap" claim was wrong and had already been repeated to Will before the review caught it. **The general rule: every projected field is a REPLACE, never a merge, so each one must be audited for what it silently drops.**
- **Other channels — NOT touched.** Amendment #2 moved nothing in Rates, Credit, Japan, Equity-vol, AI capex, War theaters or Metals.
- **`ticker` — OMITTED.** Amendment #2 moved no level; markets were closed. Marks (B 3 / C 22 / D 75) and WARRISK staleness are not ticker tokens.
- **`blocking` — OMITTED.** The base list is empty, so projecting it would ADD a section rather than update one.
- **`split` — OMITTED.** NEXUS 20/47/33 unchanged by Amendment #2.

## 3. The draft block

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "4aa5a45938eef950b02f743f9e6d29de2139785d19f2ea690c433143c632e4d0",
  "set": {
    "one": "September 11 evening, markets closed: the Saudi Ministry of Energy stated the East–West (Petroline) crude line is SHUT \"as a precautionary measure\" — that fires FALCON's pre-committed resolver #1, so tell #2 is FIRED. Nothing else moved: marks HOLD B 3 / C 22 / D 75, FAL-05 unfired at 55%, GATE-FALCON-001 review 9/14 holds. ⚠️ BRENT has NOT re-graded BG-02 — a shutdown statement is not a throughput measurement, and the ≥0.7 mb/d 7-day-MA resolver runs to 9/25. ⛔ Attribution, damage location and barrels all remain unestablished. FALCON retracted five claims the same night after an external review. STAND DOWN holds (WQ-192); $0 moved.",
    "channels": {
      "Energy": {
        "headline": "🔴 Saudi MoE states the Petroline is SHUT — tell #2 FIRED; barrels still unestablished",
        "body": "The Saudi Ministry of Energy stated (X, Fri 9/11) that the East–West/Petroline crude line is shut down \"as a precautionary measure\" after \"multiple\" attacks 9/10 in the Riyadh and Madinah regions — that fires FALCON's pre-committed resolver #1, written before the event. ⛔ §1's \"tell #2 NOT FIRED / pending confirmation\" is dead. Nothing else moved: marks HOLD B 3 / C 22 / D 75 (a pipeline is not a hull ⇒ none of D→85 (a)–(d), 3rd consecutive check); FAL-05 NOT FIRED, OPEN @55%, route (b)'s volume limb not established and the ≥7-day elapsed bar unmet ⇒ earliest 9/17–18; GATE-FALCON-001 unchanged, review 9/14 holds; thesis-kill 0/7. ⚠️ BRENT has NOT re-graded BG-02 against the statement — a shutdown STATEMENT is not a THROUGHPUT measurement, so BG-02 stands NOT MET on its own letter and the ≥0.7 mb/d 7-day-MA resolver still runs to 9/25 (L329); BRENT's read is OWED. ⛔ ATTRIBUTION, DAMAGE LOCATION and BARRELS remain unestablished — net supply loss is UNQUANTIFIED, the route-geometry test is INCONCLUSIVE with no station named, and multiple relays of ONE official statement are ONE source. FALCON retracted five wrong claims the same night across 16 surfaces after an external review. Carried from midday: XLE 65C ×1 sold by Will at $1.51 (−$77.33 realized); VLO ×3 does not fire on the 9/10 read, re-arm $1,187.31. STAND DOWN holds (WQ-192); $0 moved; no gate state edited."
      }
    }
  }
}
```

## 3b. Plan review outcome — 4 ❌ found, all fixed before insertion

The block in §3 above is the **rejected** draft, kept verbatim as the record of what was caught. The text actually inserted is the second `dashboard-amendment` block in `PROME/HEARTBEAT_DASHBOARD.md`.

| # | Defect | Fix |
|---|---|---|
| ❌1 | Dropped *"route (a) force majeure is one declaration away, no duration bar"*, leaving *"earliest 9/17–18"* reading as if FAL-05 were quiescent until then | Route (a) carried in both the one-liner and the body |
| ❌2 | **Render-layer, and I never checked it:** `fleet_dashboard.py:1103` emits `headline[:60]`. The 85-char headline rendered as *"…; ba"* — severing the mandatory barrels caveat mid-word | Headline rewritten to **exactly 60 chars**, caveat inside the cut; verified `headline[60:] == ''` |
| ❌3 | Carry-forward incomplete — dropped **D-49 open for the first contract only** and the **VLO fill condition** (refiners red against oil), while §2 claimed the carry-forward was complete | Both restored inside the "Carried from midday" clause |
| ❌4 | BRENT clause dropped both guards: that BRENT's packet **predates** the statement, and the standing **"do not quote a time of day"** prohibition. Stripped, it read as a desk sitting on the news | Both restored verbatim |

Also folded in during the same rewrite (cheap, and two were factual errors that would have reached Will's dashboard): **⚠️6** *"confidence deliberately unmoved"* restored — the calibration point that makes 55% informative; **⚠️7** *"retracted five claims"* → *"shipped five wrong claims to three desks and corrected them in place"* (only one was retracted, and one had gone to BRENT as forward guidance); **⚠️12** `East–West` → `East-West`, matching the source's hyphen in a proper name.

**Trimmed in the same pass** because the ❌ fixes pushed the body from 1,384 → 1,729 B against ⚠️10: one-liner 672 → **563**, body 1,729 → **1,599**, and the conclusion moved to the first clause (⚠️11 — Am#1's shape).

## 3c. Declared residue — not fixed

- **⚠️5** — `one` replacement is energy-only; Amendment #1's CPI/TLT/NEXUS/WATT content leaves the top line and survives in the channel bodies. Loss of prominence, not of fact. *(The false "one trap" claim this falsified is corrected in §2.)*
- **⚠️8** — *"WARRISK unchanged at 51d stale (WQ-230)"* is asserted by Amendment #2 and has no projected home. Defensible because it is unchanged, but it is an amendment assertion with no carrier.
- **⚠️9** — ticker omitted, so `WAL 78.50` and `TLT 81.21` still show their **9/11 10:1x intraday** labels on a markets-closed view. Labelled, therefore legal; still an intraday print standing where a close now exists.
- **⚠️10** — body 1,599 B is ~3.6× Amendment #1's Energy body (439 B) and the renderer does not truncate replacements. Trimmed but not resolved; the ❌ fixes require the content.

## 3d. Result read — 1 ❌ found and fixed; file then closed for the session

The result read graded the four plan fixes **LANDED · LANDED-BUT ×3** and found one new must-fix in the rewrite itself.

**❌ (fixed) — the time-of-day guard lost its object and its SCOPE.** Inserted text read *"no published time of day is on file"*; the source reads *"no published time of day **for the statement** is on file **at any FALCON artifact**"*. Two drops: (i) without *"for the statement"* the nearest antecedent becomes BRENT's packet, so the parenthetical stops supporting the *"predates"* clause beside it; (ii) without *"at any FALCON artifact"* a **scoped** absence — searched perimeter: FALCON's artifacts — becomes an **unbounded universal** absence. That is asserting more than the source on an absence claim, the one class that cannot be upgraded by a broader search (§ Session Process Controls: SEARCH-NOT-FOUND → VERIFIED needs the owner-declared path checked, and a broader grep is not an upgrade). Source words restored verbatim; body 1,599 → 1,644 B. Rebuilt rc=0, receipt and state agree at `2026-09-11 23:43`.

**No third read taken.** WQ-178 allows one only when a ❌ fix on the result changed a RULE's meaning; this fix reverted to the source's own wording and narrowed an over-assertion, so residue is declared and the file is closed for the session.

**Confirmed clean by the result read:** hash binds (Amendment #1 and #2 both) · schema legal, `errors: []`, both amendments applied · **kill-on-sight compliant on all three legs** — attribution, damage location and barrels are asserted *unestablished* in headline, one-liner and body, no station is named, and *"multiple relays of ONE statement are ONE source"* travels · figures spot-checked faithful (`B 3 / C 22 / D 75`, `@55%`, `9/17–18`, `9/14`, `0/7`, `9/25 (L329)`, `$1.51`, `−$77.33`, `$1,187.31`, `five wrong claims / three desks`, `3rd consecutive check`).

**Residue added by the result read (none fixed):**
- **⚠️ Zero margin on the headline.** 60 codepoints against a 60-codepoint slice; `barrels unknown` is the final token, so *any* future word severs the caveat. The slice is codepoint-based today (`h[60:] == ''` verified); a byte-basis slice would already yield `…barrels un`. Fragile by position, not currently wrong.
- **⚠️ ★ A LIVE truncation one block up — `AMENDMENT #1`'s Rates headline is 66 chars and IS severed** by the same `[:60]`: it renders *"…HEN-44 CONFIRM side "* and drops **"by 1bp"**. Not a falsehood (the CONFIRM-side claim survives and the body carries the margin), but the 1bp margin is the informative part. **This is the same defect class as plan-❌2, still live, outside this lane — flagged to Will, not silently fixed.**
- **⚠️ `no gate state edited`** (source) is dropped; *"GATE-FALCON-001 unchanged, review 9/14"* is narrower than the source's fleet-wide statement.
- **⚠️ Carry-forward kept the outcomes, not their basis** — `TERRY bcc962bbd`, `net $150.34 vs basis $227.67` and `RISK_RULES #14` are gone, so the realized-P&L figure travels uncited and a reader cannot tell *why* VLO did not fire.
- **⚠️ One-liner compressions:** `≥0.7 mb/d resolver` drops the **7-day-MA** window that the kill-on-sight cell makes load-bearing; *"route (b)'s volume limb is unestablished"* drops the source's basis *(no qualifying source stated an offline figure)* and the word ELAPSED.
- **⚠️ `no D→85 leg`** can misread as "D→85 has no legs" rather than "none of (a)–(d) fired".
- **⚠️ Body 1,644 B renders ~7× its sibling channel cards** (parser budget 230 B; projections bypass `trunc`). Display consistency only.

## 4. What the plan review must test

1. **Faithfulness both ways:** does the projection assert anything Amendment #2 does not, and does it drop anything load-bearing that Amendment #2 does assert?
2. **The carry-forward trap (§2):** are the XLE/VLO facts inherited from Amendment #1 still true as of the evening, and correctly attributed as carried rather than new?
3. **Kill-on-sight compliance:** HEARTBEAT's retired-claims cell binds. The three forbidden assertions are *attribution*, *damage location* and *barrels* being established. Does any sentence imply one?
4. **Schema legality:** `amendment` int · `source_sha256` exact · `set` ⊆ {one, split, channels, ticker, blocking} · channel key exists · channel fields ⊆ {headline, body, cls} · all nonempty.
5. **Will-facing readability:** the one-liner is the first thing on his dashboard.
