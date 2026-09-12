# HEARTBEAT — FIFTEENTH re-base, 2026-09-12 (Sat, markets CLOSED) · plan, receipts and DECLARED RESIDUE

**Owner:** PROME. **Purpose:** the WQ-178 declared-residue block for the fifteenth re-base, plus the receipts a reader should recompute rather than trust.

---

## 1. What the re-base did

| | |
|---|---|
| Base | 14th (2026-09-11) + Amendments #1 and #2 → **15th (2026-09-12), chain 0** |
| Hot file | **28,490 B (87.5% of the 32,550 B budget) → 22,782 B (69.99%)** at close of the re-base |
| Amendments | ROTATED VERBATIM → `PROME/HEARTBEAT_COLD.md` **§A14** (entry-crc32 3012472809, 1,451 B) · **§A15** (1121796424, 3,138 B) |
| Channel long-forms | written to cold **§1.4 · §2.4 · §3.3 · §8.2** (first pass) and **§4.2 · §5.4 · §6.2 · §7.3** (second pass, the ≤600 B re-cut) |
| Retired claims | six settled entries dropped to `PROME/archive/HEARTBEAT_RETIRED_CLAIMS_LEDGER.md` with a dated 2026-09-12 section; the hot cell remains the binding set |
| Dashboard | all eight channel headlines rewritten to render WHOLE at `fleet_dashboard.py`'s `headline[:60]` slice — **verified in the built HTML** (longest 60), not asserted |

**Nothing load-bearing was lost.** Token-diff of the pre-re-base file against (hot + the new cold sections + the retired-claims ledger) left 24 absent tokens; every one was checked: 13 are 9/11 INTRADAY prices from the old §Skip tape block (correctly dropped — a 9/12 file carries no 9/11 tape), 1 is BOND's 30Y-R dealer figure on BOND's own surface, and the other 10 are short-form identifiers whose full forms live in `GATES.tsv` / `DOCKET.tsv` / COLD (verified individually).

## 2. Receipts — recompute, never trust

```
sed -n '/^# HEARTBEAT\.md$/,$p' PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-09-12.md | head -c -1
  → 28,490 B · crc32 2053291015 · byte-identical to `git show 303267de8:HEARTBEAT.md`
```

⛔ **This receipt was wrong twice before it was right, and the failure mode is worth more than the figure.**

1. First form: *crc32 **632502878** over `tail -n +9`*. The crc reproduced under **no** variant (spine audit #13 swept offsets 1–19 × {raw, stripped, appended} — zero hits), **and** the offset excluded the `# HEARTBEAT.md` title and the whole `**Base:**` header — the two lines that say *which* re-base is being preserved. The file was also **untracked in git**.
2. Second form: `tail -n +7`, correct when written. **Writing the correction lengthened the banner above it, which moved line 7 and broke the receipt inside the very edit that was fixing it.** A cold read minutes later computed the then-correct offset as `+11`; by the time that report arrived, `+11` was wrong too.
3. Third form, the one above: **anchored to a delimiter, not a line number.** Re-verified after the banner edit that broke the previous two. Measured for the record — `+7` → 29,383 B, `+9` → 29,311 B, `+11` → 29,205 B, all wrong; the delimiter form → 28,490 B, exact.

**Rule this earns: a receipt keyed to a line NUMBER is invalidated by editing the lines above it, while the thing it certifies has not changed. Anchor to content, and prefer a git object — it authenticates the bytes independently of whoever wrote the banner.**

Other receipts written at this re-base, all recomputed and matching: §A14 `3012472809` · §A15 `1121796424` · `PROME/archive/ACTIVE_DECISIONS_STAMP_PRIORS_2026-09-12.md` block `4268380213`.

## 3. Reads performed (WQ-178 budget)

- **PLAN read:** not taken as a separate pass — the re-base plan was the pre-existing STATUS/SCRATCH row naming the three stale claims, the COT grade and the buyback context, itself corrected by ARGUS earlier the same day.
- **RESULT read 1:** `coldreader`, blind, against 22,635 B — 47 claims, **3 ❌**, 12 ⚠️.
- **RESULT read 2:** same reader, against 23,119 B after the BND-22 material landed — 49 claims, **4 ❌**, 13 ⚠️.
- **❌ fixed (4):** the snapshot receipt (above) · FT-11 stated "applied once" in one cell and "ACTIVATED but never APPLIED" in another — RED's own words are the latter · the kill-set entry *"BND-22 is OPEN"* killed the word rather than the claim, so a reader applying it literally had to strike the true sentence beside it · the CRMT bridge ordinal.
- ⚠️ **A ⚠️ that was fixed anyway because it sat OUTSIDE the file under budget and was a live position quantity:** the reader flagged HEARTBEAT's `77P ×20` against DOCKET L74/L267 titles reading `×25`. **The hot file is right and the registered rows were stale** — `FORGE/STATUS.md` carries the arithmetic receipt (*"77P $231.26 = 20/25 × $289.08 ✓"*) and 5 contracts were sold on 9/10. Both rows annotated; the original size is left visible as history.

## 4. DECLARED RESIDUE — ⚠️ carried, NOT fixed

Each of these was raised by the blind cold reader, verified as a real observation, and deliberately left. **None changes a level, a fire path, a gate state or a position.** They are listed so they do not disappear under "the re-base is done."

1. **"The 004 add line is THROUGH" is asserted flat in the one-liner, §2 and the dashboard**, while §2's own body says the add-line-vs-`≥2.50 sustained` wording is *outcome-determining* and unresolved. The headline records MET what the body calls unsettled. ⛔ Left because the flat statement is the one a reader must not miss and the hedge is one clause away in the same channel; **the disagreement is named at DOCKET L356 and is TERRY's and BOND's to settle, not PROME's to pre-empt with softer wording.**
2. **BG-02 is still carried with a 9/17→9/25 gradeable window on a floor the retired-claims cell kills as unsound** (0.8 mb/d directional vendor spread vs a 0.7 floor). "Repair pre-registered strictly restrictive" names no author, no approval and does not say which text the 9/17 grade uses. ⛔ BRENT's, and WQ-234 is exactly this question in front of Will.
3. **"1.748× cover" has an unstated basis** — it is offered ÷ the $6.0B **cap**; offered ÷ **accepted** is 2.02×. The "weakest of n=26, prior min 3.22×" comparison is therefore uncheckable from the hot file. ⛔ The figure and the n=26 comparison are BOND's (`e6f3dd133`); PROME relays, and re-deriving the basis is BOND's call.
4. **"COT-35B CLEARED" reads as a gate state** while `GATES.tsv` says the row is **LIVE** with `review_by` 9/18. It means "the owed grade landed", not "the gate is closed."
5. **"LIQ-069 ARMED 1-of-2"** against a row whose condition is *"re-arm, ANY ONE of 5 legs"* — the denominator 2 is undefined in the hot file. (All its dates reconcile.)
6. **An ellipsis in the kill-set inverts its own meaning:** *"the 9/10 Treasury cells are unpublished"* [⛔ **all four are**; the 9/11 cells were **not**] — the verb is omitted, so the quoted DEAD claim supplies "unpublished"; only §2 and the dashboard let a reader recover "published".
7. **Un-glossed identifiers and scores used as if known:** 20/47/33 · 29/75 · "composite 14/20" · "BAND B, 0 of 5 axes" · 1A/1B/2A · "HEN-44 CONFIRM by 1bp" (threshold never stated) · HEN-46 (no level) · CRL-30 · LIQ-072 (appears nowhere else in the file) · FAL-05 "@55%" · "OVX/VIX 3.41 (p96.6)" (window and basis unstated) · and **"RISK_RULES #14"** — ✅ **FIXED, and chasing it found a real defect underneath.** Root sanctions only "root rule #N" and "Non-Negotiable #N", with an explicit ⚠️ that the two lists do not line up. Following the number showed **it resolves to nothing: `AGENTS/TERRY/RISK_RULES.md:74` cites `(#14)` while its own `## Non-Negotiables` list runs 1–13.** PROME had been relaying a dangling citation faithfully — *the relay was correct and the pointer was still dead.* Both PROME sites (`HEARTBEAT.md` §Book state, `ACTIVE_DECISIONS.md`) now cite `RISK_RULES.md` §"Breaking root rule #6", which resolves; **TERRY's own file was NOT edited** — the finding is appended to the same-day TERRY packet. The substance (a day-colour gate is a MOMENT property; the 9/10 read expired with its session) is not in doubt and the VLO grade is unchanged.
8. **A named contributor with no content:** the header lists DAEDALUS in the 9/12 six-desk wave; `grep -c DAEDALUS HEARTBEAT.md` → 1, the header itself. Its output landed in DOCKET and the tools, not in a channel — but a stranger cannot tell whether a channel is missing or the name is vestigial.
9. **The file's only source-less figure:** "~$6.2T of US options expire ON 9/18" — no source, no as-of, no owner, against the file's own *"Source + date every claim"* discipline.
10. **"decay monotone in tenor" contradicts the levels printed beside it:** VIX9D 17.70 < VIX 17.84 < VIX6M 21.17 — the LEVELS rise with tenor; only the percentage CHANGES decay. The basis is unstated, and the "EVENT bid, not a regime re-rate" conclusion rests entirely on it.
11. **A breakeven built from figures the file itself supersedes:** SAM's "$108 shock … ≈ Brent $309 at ¥154" against the dashboard's own "Brent BZX26 $107.63 [9/10 settle]" and "USD/JPY 153.57 [9/10]" — in a file whose kill-set retires a "$108.45 [9/10]" Brent print as an overnight `BZ=F` value. The $309 is not derived from the file's own levels.
12. **The hot file does not flag that DOCKET L74/L267 titles read `×25`** for the TLT 77P leg while it carries `×20`. ✅ **Half-addressed:** both rows were annotated at this pass with the live count and the `FORGE/STATUS.md` receipt, so the rows now self-correct; the hot file still does not say the titles are stale.
13. **§1–§3 run 1,100–1,200 B against the §C ruled target of ≤600 B per channel** — they carry the day's decisive grades and were not cut to the target.
14. **The hot file closed at ~73% of budget, over the <70% stop line it had cleared at 22,782 B.** The overage is the snapshot-receipt correction, the BND-22 material and the ❌ fixes — all load-bearing, all arriving after the re-base closed. The 75% rotation line (24,412 B) is not tripped.

**Fixed rather than carried, because it was a one-token pointer defect the reader found in the index I had just trimmed:** the cold-section list had dropped **§K.1** while §KERNEL still pointed "→ cold §K + §K.1". Restored; both now agree and §K.1 exists at `HEARTBEAT_COLD.md:156`.

**Independently re-verified by the cold reader after the fix, not by PROME:** `sed -n '/^# HEARTBEAT\.md$/,$p' PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-09-12.md | head -c -1` → **28,490 B / crc32 2053291015**, byte-identical to the git object, *"and it is also edit-stable above the delimiter, which the line-offset form was not."* **Pointers: 42/42 resolve, none dead.**

## 5. ARGUS pass — findings taken, and what they say about this session's own error rate

ARGUS audited the pending candidate against baseline `6a016ec31`, 72 claims, and the candidate moved twice under it. **Eight ❌, all PROME's, all fixed.** The ones worth carrying forward as pattern rather than as line-items:

- **Four different byte figures for ONE file** appeared across `STATUS.md`, `SCRATCH.md` and `HANDOFF.md` during the pass — 22,635 · 22,782 · 71.5% · 69.99% — **each true at the moment it was written and none current when read.** The file kept growing as load-bearing fixes landed, and every surface recorded the number at its own moment and then stopped. All four now read one measured figure with the rotate-line distance stated. ⚠️ **This is the same defect as the crc receipt, in a different unit: a figure a reader can recompute does not belong in prose** (`PROME/CLAUDE.md` § Session Process Controls, "No live measurements in prose") — and this pass wrote five of them anyway, in the middle of fixing one.
- **A stale figure on the TOP line of the next boot's action list manufactures work.** `SCRATCH.md` ★ NEXT and `STATUS.md` both still called the `ACTIVE_DECISIONS` rotation OWED at 76.4% after the pass's own stamp-chain rotation had taken it to **73.6%, under the 75% line**. Both now say the rotation is a CHOICE and that a recorded decision NOT to rotate closes the item.
- **A Will-facing dashboard chip was lost silently by prose compression.** Shortening the §Stress-dashboard cell to `claims 206K / 1,774K` removed the literal `Cont claims` that `fleet_dashboard.py:385` keys on, so `Cont Claims` fell out of `dashboard_state.json` while the number survived in the sentence. Restored. **A full section diff then confirmed nothing else went: levels 11→11 · channels 8→8 · gates 20→20 · fleet 33→33 · split 35 · docket 78→81 (the three rows registered today).**
- **A kill-on-sight guard was rotated out while the thing it guards is a LIVE instruction.** *"ENERGY $6,209 / duration-short $1,220"* went to the ledger as settled history — but §Book state still says to size any add against that sleeve, so the retired denominator was a live hazard, not history. Back in the hot cell.
- **The breach list named 3 of 8 channels; all 8 breach** the ruled ≤600 B (§4 628 B smallest, §2 1,729 B largest). Naming the worst three read as naming the set.
- **Hand-fixing the named rows was not fixing the class.** A cold reader named `DOCKET` L74 and L267 as carrying a stale `×25` for the TLT 77P leg; both were annotated. ARGUS then found **L255 — a LIVE 2026-09-30 disposition row instructing HOLD to expiry on "TLT $77P ×25"** — which the named-row sweep never reached, and pointed out that L74's annotation sat *behind* the stale token, so a truncated render still showed ×25. Fixed as a class: every row asserting the count now carries **`×20 [was ×25; 5 SOLD 9/10 — receipt FORGE/STATUS.md: "77P $231.26 = 20/25 × $289.08 ✓"]` in the title cell.** `[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]`
- ⛔ **`DOCKET` L212 was deliberately NOT changed and the reason is recorded here rather than left as an omission:** its `×25` sits inside a dated capture of the 2026-08-17 state (*"DFII10 2.44 [8/17] is 6bp from the 2.50 add-gate — 004 (TLT Sep-30 77P ×25)"*). The position **was** ×25 on 8/17. Correcting it would corrupt a correct historical record — the path-class rule `consumer_check.py` encodes as *"a DATED RECORD is not a STALE CLAIM."*
- **The snapshot receipt failed a THIRD time, inside the sentence explaining the first two.** The corrected banner said the title and `**Base:**` were "lines 7 and 8 of THIS file"; the correction above them had grown and they were at 11 and 12 when ARGUS read it. No line number appears in that banner now. **Three "correct" offsets in one session (+7, +9, +11), each invalidated by an edit above it, while the delimiter form survived every one** — independently re-verified by both reviewers against the git object.

**Reviewer disagreement worth recording:** ARGUS's first pass raised a ❌ that the WQ-165 blind read had not run; it **withdrew that finding on re-verification** once the cold-read report existed. Recorded because a withdrawn finding is evidence the reviewer re-checked rather than re-asserted.

### ARGUS's later passes — the two that changed an action, and two withdrawals

- **A LIVE sizing instruction was denominated in RETIRED figures, and restoring the hot guard was not the fix.** `PROME/ACTIVE_DECISIONS.md:38` reads *"size any duration-short or oil-long add against the SLEEVE total"* and named **$6,209 / $1,220 [9/9 closes]** — the pair `HEARTBEAT.md` retired on 9/11 in favour of the 9/10 CLOSE marks, and the pair whose kill-on-sight guard this very re-base rotated out of the hot cell as settled history. 🔑 **The guard and the instruction lived in different files, which is exactly how a rotation strands one.** Re-based to **$6,007.06 / $1,105.14**, all three retired pairs kill-on-sight in the same cell, and a line telling the reader to refresh at `FORGE/STATUS.md` first. ⚠️ The first version of this fix pushed `ACTIVE_DECISIONS` back **over 75%**; it was compressed and the rationale moved here — `[[finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag]]`.
- **I measured an artifact AFTER editing it and wrote the result up as its before-state.** The stamp-rotation banner claimed the `Updated:` line *"had accreted 11 `Prior:` entries / 2,872 B"*. The true pre-edit figures are **10 / 2,394 B** — the 11th `Prior:` and the extra 478 B were my own rotation stamp, already prepended when I measured. Banner corrected and now carries the reproducible form (`git show 303267de8:PROME/ACTIVE_DECISIONS.md | sed -n '2p'`). ⚠️ **Same family as the crc receipt and the four byte figures: this pass generated three separate wrong measurements while its subject was a wrong measurement.**
- **Two withdrawals, recorded because a reviewer that withdraws is one whose remaining findings mean something.** ARGUS raised "no blind cold-reader verification artifact exists for this re-base" and "HANDBOOK still routes BOND to the ~2.53 nowcast"; both were re-checked against the moved candidate and voided — the read had run and the rewrite had landed, its pass simply predated both artifacts. ⚠️ Sequencing lesson kept: **a report that lands after the audit makes a present control look missing.**
- **Two pre-existing instrument defects found while confirming this re-base broke nothing — registered, NOT fixed** (DOCKET **L359**, **L360**), per the operator's instruction to record rather than open another improvement session:
  - `fleet_dashboard.py` `TICKER_TILE_MAP` has **two patterns that have never produced a tile and fail silently**. `SOFR-IORB` cannot match because `HEARTBEAT.md` writes a **Unicode minus** (`SOFR\u2212IORB`) — PROME verified this independently of the reporter rather than taking it on report. `Brent` matches and still reaches no tile. Both predate the re-base, checked at baseline. **The class is the item: a map entry that matches nothing is indistinguishable from a datum that is absent.**
  - **The ARGUS scope was computed on a non-quiescent tree twice, and `HEAD` moved mid-audit** (303267de8 → c73ad9733, `will_brief.py` auto-persist) — so the closeout's own HANDOFF write was invisible to the perimeter that authorises the audit. **A tool advancing HEAD on its own defeats the recorded-baseline design the auditor's independence rests on.** Dated to the 9/19 sitting because it is an input to the ARGUS trial grade (L333); repairing the instrument under audit on the night it reports would be PROME re-tuning what it is fenced from. Mitigation tonight: the scope was re-run immediately before the commit.

**Review:** at the next re-base, or at any amendment that touches an affected cell.
