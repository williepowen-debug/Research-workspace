# CHECK_STANDARD Batch B — DRAFT for Will's gate (unblocks PROME's Batch B; drafted 2026-08-21 eve)

**Status: DRAFT — nothing below is encoded.** One ruling covers all six items (PROME's one-word-instead-of-three rec, my concurrence). On approval: encode into `BLUEPRINTS/CHECK_STANDARD.md` + EVOLUTION same commit; §10/§11-style PROVISIONAL markers where the flow requires ratify-after-first-live-use.

**Provenance discipline:** every ⑤b item below was verified at ZHAO's artifact before drafting (precondition from my own register): counts-keyed verdict at `AGENTS/ZHAO/scripts/boot.py:319-332` · monkeypatched-legs fixture in commit `9f97c7f5f` ("Both branches fixture-tested via monkeypatched legs so the OK path runs without mutating real files") · declared-asymmetry comment at `boot.py:298-301`. WAL rules verified at the source packet + `AGENTS/WAL/MEMORY.md:80` (base rates 54→scoped and 10/23 baseline are WAL's own measurements).

---

## Item 1 — fold into §1 (suppression register): PROXIMITY-NOT-PRESENCE for historical-marker exclusions *(WAL rule 3)*

> A marker that excuses a hit (SUPERSEDED, corrected-in-place sentinel, historical-quote label) excuses it only within a **stated character/line window** of the hit — presence anywhere in the file excuses nothing. *(Measured: consumer_check's presence-anywhere `has_marker` cleared WAL's 🔴 with the marker ~1,100 chars away — the D1 defect, fixed 8/21 `a9a1129e7`; WAL built its own `derived_drift_check` with the windowed form rather than inheriting the bug.)*

## Item 2 — fold into §3 (no guard ships unverified): the MONKEYPATCHED-LEGS fixture form *(ZHAO ⑤b-ii)*

> A named method for §3's clean-case leg: **exercise the OK path by monkeypatching the check's own legs (or pointing it at fixture inputs via override flags), never by mutating real files** to manufacture a clean state. *(Reference: ZHAO `9f97c7f5f` both-branches fixture test; memory_citation_census `--hot-index/--cold-index` overrides, field-exercised by PROME 8/21 eve.)*

## Item 3 — fold into §6 (failure-direction is chosen, and stated): DECLARED ASYMMETRY *(ZHAO ⑤b-iii)*

> When a check deliberately treats two defect classes asymmetrically — one **reports-but-does-not-flip** the verdict (chronic backlog that would pin permanent-red and kill the signal) while the other **flips** (fail-open class: unparseable input) — **the choice is written as a code comment at the site**, so the next reader sees a decision, not an oversight. *(Reference form verbatim at ZHAO `boot.py:298-301`; kin: `finding_deliberate_and_unnoticed_asymmetry_look_identical`.)*

## Item 4 — fold into §8 (as a rule or rule-5 sharpening): GLYPH-VS-COUNT *(ZHAO ⑤b-i)*

> A verdict layer keys on **alert COUNTS the section functions RETURN**, never on scraping its own stdout for glyphs. The fleet's emoji vocabulary double-serves as severity marker and priority marker (STATE_VOCABULARY Class 9 fixes new writes, legacy is grandfathered forever), so a scrape-verdict reads permanent-REVIEW on every clean boot that merely has a 🔴-priority event scheduled — **and permanent-red is silent-green inverted: a verdict that cannot go clean gets ignored exactly like one that cannot go red** (the verify_push law). *(Reference: ZHAO `boot.py:319` `total = sum(v for _, v in legs)`.)*

## Item 5 — NEW § (ship calibration): BASE-RATE BEFORE WIRING; THE SIGNAL IS THE DELTA *(WAL rules 1+2, one section)*

> Before wiring a new check into any boot/closeout step: **run it unscoped and count the hits.** A check that fires on legitimate history ships alert fatigue, and a check nobody reads is worse than no check — scope until the hit population is actionable (present-tense assertions; exclude version-pinned history and frozen calibration records), and **"don't wire it" is a real answer**. Then: **record the swept baseline in the check's own docstring and report the DELTA against it, not the level** — residual hits are known history; a desk copying the check's shape without its baseline degrades it to noise within a week. *(Measured at WAL: 54 unscoped hits → scoped; baseline 10/23 recorded; first run then beat the human sweep that had just finished on the same tree. Kin: `finding_base_rate_the_threshold_before_building_it` — this is its check-side twin.)*

## Item 6 — NEW § (spec completeness): the PRIOR-ART LINE *(memory-retrieval disposition ①, wording as drafted in the answer packet)*

> **Prior-art line (mandatory on new mechanism specs):** any new check, guard, threshold mechanism, or process-fix spec carries one line: the SYMPTOM searched against `MEMORY.md` + `memory/auto/INDEX_COLD.md` + `PATTERNS_HOT.md` (grep the bodies, not just the indexes — cold bodies are dark to injection but fully greppable), with either the slug/PAT cited or the words **"searched, novel."** A spec without the line is incomplete, the same way one without a §3 verification plan is. Scope explicitly EXCLUDES market judgment; the moment is mechanism-design, not closeout (too late) and not ambient (2×-ceremony at 33-agent scale). Enforcement: DAEDALUS checks it at review as §3 is checked now; REGISTRATION_CHECKLIST picks it up for new builds. **Re-open trigger pre-registered (Batch-A record): ≥3 false-"searched, novel" claims in a month revives the declined cross-index.**

---

**What is deliberately NOT in this batch:** the derived-drift check itself (WAL's stays local — don't-build verdict stands until ≥3 desks need the shape; only the RULES canonize) · any Class-8 SCHEDULED token text (8/23-sitting/8/28-sweep lane, one-cloth with the cadence enum) · recurrence instrumentation (waits on the distillation leg's first Production Review run).

— DAEDALUS (drafter; ruling and encode order are Will's)
