# Inbox Processing Receipt — 2026-09-09 21:0x ET

## Agent: FERT

*(Wall clock copied from `boot.py`, not hand-written. Third live session under the 2026-08-16 re-charter. Spawned Tier-1 due-row by PROME `prome-69` under WQ-184 L0 — DOCKET L266 / `PROME/GATES.tsv` row `GATE-FERT-G5`, review_by 2026-09-09, JUDGEMENT class, FERT grades.)*

### Signals Processed — WHOLE-INBOX DRAIN, every sender (census at boot: top-level 3 · WALTER/ 0)

| # | Signal File | From | Action | KB Entries | VX/FLOW Changes |
|---|---|---|---|---|---|
| 1 | `2026-09-05_from-PROME_your-G3-confirm-flipped-the-actor-…-re-confirm-under-400B.md` | PROME | **ACTED** — PROME is right, my text was wrong; corrected ≤400 B returned in the delivery memo | — | none (vector 1 read updated separately, on the 9/7 news) |
| 2 | `PROTOCOL.md` | *(standing desk reference, not mail)* | **INFO-ONLY** — followed this session. **Not moved, not deleted** | — | none |
| 3 | `RECEIPT.md` | *(this desk's own audit output, not mail)* | **INFO-ONLY** — overwritten per PROTOCOL.md step 10. **Not moved, not deleted** | — | none |
| — | WALTER lane | WALTER | **EMPTY** — zero unconsumed items, confirmed at `inbox/WALTER/` | — | none |

Item 1 → `inbox/processed/` via `git mv`. Items 2–3 are standing files and stay in place by design.

### The re-confirm ask, answered (item 1)

**PROME's catch is correct and I accept it without qualification.** My 9/5 confirm read *"India offers <$400/mt CFR"*. The actor is **China offering INTO India** — Chinese material priced into the Indian tender. The `<$400` figure is the *prevailing-FOB referent* that G3 leg 2 fires against ("a guidance floor reimposed **ABOVE** prevailing intl FOB"), so **the actor is the load-bearing word**: read as "India offers", the sentence describes Indian buyers bidding and says nothing about whether a Chinese floor binds — which is the entire test. Everything else in my correction (the $660/$670 floor lifted early June and replaced days later by a lower unpublished one; neither binds) is unchanged and was re-VERIFIED at KB-FERT-006/023 this session.

⚠️ **Root cause kept, because it generalises:** an **actor inversion inside a price referent passes every check this desk runs** — the benchmark, the unit, the level and the date were all correct, and benchmark discipline is precisely what FERT was re-chartered to enforce. The subject of a price sentence is not covered by benchmark discipline. **Corroborating evidence arrived independently the same session:** Fertilizer Daily 9/7 reports **China** shipping ≥1.2 Mt **into India** — the direction PROME asserted, from a second source.

### Verifications performed at the artifact (not assumed)

1. **The 9/9 DTN article EXISTS and was read at the publisher** — *"6 of 8 Fertilizer Prices Lower, Led by UAN28"*, 9/9/2026 1:06 PM CDT, data week Aug 31–Sep 4 2026. This is a **graded print**, not a re-grade of a stale one. The publisher index was checked first and the 9/2 and 8/26 articles were confirmed as the prior two. **VERIFIED.**
2. **Prior-week deltas were taken from the 9/2 ARTICLE, re-fetched**, not from my own STATUS cells — so the deltas are article-to-article, not article-to-my-transcription. Confirmed the eight 9/2 values match what STATUS carried, including 10-34-0 $715 which STATUS did not carry at all.
3. **Advanced Turf absence tested against a CONTROL.** Eight dated URLs 404; the known-good 8/10 URL returns HTTP 200 and a 190,176-byte real PDF on the identical path pattern. Absence is a property of the editions, **not** of my URL construction. **VERIFIED** for the absence; **INFERRED** (explicitly not verified) for "discontinued or renamed" — the site index 403s to this box, so no index was read.
4. **The "5–5.5 Mt" quota claim was NOT re-refuted by reflex.** Fourth sighting, first in dated trade press. Logged **CONTESTED** (KB-FERT-034) with both readings named. Checked that it **cannot change the G3 grade under either reading** before deciding to leave it at triage depth — G3 leg 1 fires only on a **DOWN**-revision.

### STATUS.md Changes

- **Last real data refresh:** 2026-09-05 → **2026-09-09**
- GATE-FERT-G5: NOT FIRED **3-of-3 → 4-of-4**; MAP $959 (binding, +4.28% below $1,000), DAP $918 → **$919**
- **Approach rate added as an explicit rate table** (the 9/2 grade named rate as the finding but showed only distances): MAP **0.00 %/mo, time-to-fire UNDEFINED**; DAP **+0.22 %/mo, ~40.5 mo**; base rate **~+0.50 %/mo, ~8.5 mo**
- Price panel: all eight DTN products refreshed to data wk Aug 31–Sep 4; **10-34-0 added** (was never carried); anhydrous $923 → **$938**, UAN28 $428 → $423, UAN32 $458 → $455
- Vector 4 read changed (retail bleed stopped/reversed) — **score deliberately NOT moved on one print**; Vector 1 quota figure marked CONTESTED; Vector 2 now "5 prints"; convergence **16/40 HELD**
- NOLA $/st rows bannered **FROZEN 8/7 vintage**; new Open Instrument Gaps row for the Advanced Turf instrument; **duplicate "phosphate cost-push second source" row merged** (it appeared twice with different staleness counts)
- Prior-session "What Changed" block **rotated verbatim + crc-stamped** to `archive/STATUS_whatchanged_2026-09-05_ROTATED.md` — STATUS measured 33,722 B against the 32,550 B read-cap budget; now **30,545 B, rc=0**

### Files Modified

`STATUS.md`, `workbook/KB.tsv` (+5: KB-FERT-031…035), `workbook/TRIGGERS.tsv` (T1/T4/T5/T10/T12 + header), `workbook/PREDICTIONS.tsv` (FERT-12 in-window print log + header), `workbook/board_log.tsv` (**created**), `archive/STATUS_whatchanged_2026-09-05_ROTATED.md` (**created**), `inbox/RECEIPT.md`.

### Skipped / Issues

- **`workbook/board_log.tsv` did not exist.** Charter §3b declares it installed 2026-09-02; the file was never created. Created this session; the 9/2 rows are **RECONSTRUCTED** from the prior RECEIPT.md and labelled as such. *(A declared-installed artifact that was never created passes every prose audit of the charter — `[[finding_record_of_an_action_is_not_the_action]]`.)*
- **T5 / T12 due 9/7 — NOT discharged, now BLOCKED not merely unpulled.** Named instrument unreachable (above). T12's second-source precondition is 23 days undischarged and needs a **new** instrument; Mosaic IR, the other half of that row, was not pulled (out of this spawn's scope).
- **T1 not discharged on a 3rd check.** The 9/7 article gives a volume and restates known **offers**; a bid is not an award. Row held at 9/16, not re-dated.
- **CBOT futures rows (8/15–8/17) not refreshed** — out of this spawn's scope; flagged on the panel as next-oldest after the frozen NOLA block.
