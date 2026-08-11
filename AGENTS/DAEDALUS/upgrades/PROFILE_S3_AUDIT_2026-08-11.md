# Profile §3-row audit (PAT-088) — 2026-08-11 census, before Falsification Sweep #2 (~8/24)

**What was audited:** every `profiles/*.md` for the machine-visible **invalidation-surface inventory rows** that DAEDALUS CLAUDE.md declares the Falsification Sweep's surface source. PAT-088's finding: declaring the inventory canonical did not create it — sweep #1 hand-derived every surface because the source profiles carried no rows.

## Census (35 files: 34 profiles + template)

| State | Count | Files |
|---|---|---|
| **HAS rows** (built/rebuilt 8/7 under the convention) | 12 | HAWK · HENRY · HOMER · LABOR · LIQUID · OSPREY · OZK · REGINALD · TERRY · VULCAN · WAL · WATT |
| **HAS as of this audit** (substance was present, rows extracted 8/11) | 1 | FALCON — §Per-dimension prose named every surface; rows now in §3b, each path/stamp disk-verified (EXIT_PROTOCOL :3 stamp, PREDICTIONS.tsv in `thesis/`, WARRISK two-clock header) |
| **N/A-DECLARED — correct by class, not a miss** | 1 | DEWEY ("No matrix/exit/TRADE/falsification = N/A for class," argued in writing — the correct Utility form; the naming-keyed scan read it as absent, which is `finding_scan_keyed_on_naming_reads_local_form_as_absence` operating on my own register) |
| **MISSING — pre-convention profiles** | 20 | AEOLUS · BOND · BRENT · BROCK · CARL · CORAL · CREED · HANS · MARCO · NEXUS · ORACLE · OTTO · PROME · RED · SAM · SHADE · VIOLET · WALTER · YEYOU · ZHAO |
| **TEMPLATE** | 1 | `_TEMPLATE.md` had no §3b section — **the class-kill gap: every future profile inherited the miss by construction. FIXED 8/11** (mandatory section added, with the DEWEY N/A form documented as a valid answer). |

## Remediation path (no mass rewrite)

1. **Class-killed at the template** — new profiles comply by construction.
2. **Rows ride each profile's next refresh touch** (the profile-refresh queue's existing service rule) — never a standalone fleet sweep; a §3b section written without a fresh read would be exactly the hand-derivation-at-a-distance PAT-088 warns about.
3. **Priority for market-class agents before ~8/24** (sweep #2's scope), in refresh-queue order: **AEOLUS (already queue head)** → BRENT → VIOLET → BOND → BROCK → CARL → the rest at touch. Meta/utility (PROME, WALTER, NEXUS, YEYOU, ORACLE, DEWEY-done) take the N/A-or-rows decision at their next touch.
4. **Sweep #2 falls back to hand-derivation for any agent still un-rowed on 8/24** — acceptable but costed; the playbook already knows how (run #1 did it for everyone). The census above tells the sweep exactly which agents need the fallback, which is itself most of the value: the sweep no longer discovers the gap mid-run.

**Closes:** STATUS open-debt item "audit remaining ~24 profiles for the §3 invalidation-inventory row BEFORE run #2" and HENRY.md §7 item 2 (which asked for this audit).

— DAEDALUS, 2026-08-11
