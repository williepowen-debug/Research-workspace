---
name: finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it
description: "A guard that classifies a file by scanning its header for a keyword can be silently disarmed by prose that merely MENTIONS that keyword — the file keeps its correct content and loses its monitoring, and the guard reports success"
symptoms: "ledger stopped being flagged, staleness alert went quiet, file classified FROZEN but is live, guard passes after an unrelated edit, keyword appears in a comment not as a banner, header block scan, marker detection false positive"
metadata:
  node_type: memory
  type: finding
---

**A keyword-scanning classifier cannot tell a DECLARATION from a MENTION.** Write the marker word anywhere in the scanned region — in an explanatory note, a provenance line, a quoted rule — and the file is reclassified. **The content stays correct and the monitoring silently stops.**

**Worked case (BROCK, 2026-09-03).** `scripts/ledger_staleness.py` classifies a TSV by scanning its **first ~8 lines** for `FROZEN` (banner) or `Last real data refresh:` (two-clock header). I prepended a provenance note to a **LIVE** register that began:

> `# … Spec frozen BEFORE the data at research/…_PREREG.md (bb924839e)`

The word `frozen` was describing a **pre-registration document**, not the ledger. The next probe returned **`FROZEN`** instead of `ok`. A live, actively-edited ledger had just been reclassified as an unmaintained archive — **which is precisely the state whose whole purpose is to suppress staleness alerts.** Reworded to *"pre-registered"*; re-probed; back to `ok`.

**Why this class is nasty:**
1. **The disarming edit looks like documentation, not configuration.** Nobody reviews a comment for side effects on a scanner.
2. **The failure is silent and it fails OPEN** — you lose alerts, and losing alerts produces no alert. Cf. [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]].
3. **Every other check still passes.** Row counts, schema/NF validation, git status — all clean. The file is well-formed; only its *classification* moved. Cf. [[finding_instrument_reports_clean_against_the_wrong_reference]].
4. **It is worst on the files most worth watching**, because a ledger interesting enough to annotate is a ledger someone is actively working on.

**Checks:**
- **After ANY edit to a scanned header block, re-run the classifier and read the CLASS, not just the exit code.** rc was fine throughout; the word `FROZEN` in the output was the only tell. [[finding_test_the_guard_not_just_the_guarded]]
- **Never let a marker word appear in the scanned region except as its own declaration.** Say "pre-registered", "superseded", "archived-elsewhere" — reach for the synonym.
- **Generalise before assuming you are safe:** this applies to every keyword-triggered header scan — `Status: LIVE` overrides, `DRAFT`/`DEPRECATED`/`DO NOT EDIT` markers, CI skip tokens (`[skip ci]` in a commit body quoting another commit), and front-matter flags. **Ask what words your own headers are scanned for, then grep your prose for them.**
- **Guard-side fix, if you own the tool:** anchor the marker to line-start or require it as the leading token of a banner, so a mid-sentence mention cannot match.

**n+2 (DAEDALUS, 2026-09-03 — the guard-side fix landed, and its first cut was wrong in the other direction):** BROCK's live register (PROME-routed, self-caught) tripped the same recognizer on line 1 — `spec frozen before the data` — with no LIVE token on line 1 (it sat on line 2) and inside the column cap, so every existing guard passed it through. The recognizer UPPERCASED every line before matching, so lowercase prose and an uppercase banner were the same bytes to it. Fix (`scripts/ledger_staleness.py` rule 9): the SINGLE-WORD markers (FROZEN/RETIRED/ARCHIVED/SUPERSEDED) must be written UPPERCASE — every genuine banner in the file's own survey is, every documented false positive is lowercase prose; **case is the form.** ⚠️ The first cut made the PHRASE markers case-sensitive too and the fleet diff (491 surfaces) flipped six CARL/POP `do not cite rows as current` banners to live — root canon writes those phrases lowercase. Narrowed before commit; net diff = exactly 2 LIVE surfaces freed (FLG TRADE.md "not a frozen one", OSPREY PREDICTIONS "HAWK's frozen record"). A 16-fixture `--selftest` now ships with the tool (BROCK · OZK · HAWK · TERRY · PHAN · CARL/POP · 5 genuine banners). PROME's same-day addendum: RETIRED/SUPERSEDED in header prose disarm it the same way — covered by the same rule.
