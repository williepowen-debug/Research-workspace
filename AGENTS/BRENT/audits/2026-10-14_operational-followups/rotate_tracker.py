"""One-shot tracker rotation: preserve the before-image and operative clauses."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
BRENT = HERE.parents[1]
ARCHIVE = BRENT / 'archive/2026-10-14_operational-followups'
original = (ARCHIVE / 'TRACKER.md').read_text()
target = BRENT / 'demand_destruction/TRACKER.md'
assert target.read_text() == original, 'Concurrent tracker change: inspect rather than overwrite'
retained = []
def section(name, start, end):
    lo = original.index(start)
    hi = original.index(end, lo)
    text = original[lo:hi]
    retained.append({'name': name, 'start_utf8': len(original[:lo].encode()),
                     'bytes': len(text.encode()), 'sha256': hashlib.sha256(text.encode()).hexdigest()})
    return text

live = section('standing rules and all eleven alert lines', '> ### ⛔ STANDING RULES FOR ROUTINES', '**⚖️⚖️ 8/12 Wed')
old_gas = next(line for line in live.splitlines() if line.startswith('> | 4 |'))
new_gas = '> | 4 | **GASREGW > $4.00** | **$4.331/gal**, October12 observation [CONF EIA October14 posting, direct primary read] | Above existing line; −$0.023 WoW versus October5. BRT29 historically FAILED; no new BRT31 grade. |'
live = live.replace(old_gas, new_gas)
cushing = section('existing single-print reactivation letter', '**⑤ RE-ACTIVATION — REGISTERED', '**⑥ ⚠️ NOTIFICATION')
basis = section('existing instrument-basis canon', '**④ THE CANON, RULED PER SURFACE', '**⑤ ⛔ AND I FOUND')
capture = section('existing daily-bar capture restriction', '**⑤b ⛔⛔⛔ ADDENDUM', '**⑥ ✅ THE PROMPT')
premium = section('observational premium definition and revisit letter', '**⑥ ✅ THE PROMPT', '**⑦ ★★ WHAT THE NEW SERIES')
zero = section('zero-AIS inference restriction', '> ⇒ ★ **A ZERO IN AN AIS-DERIVED', '> ✅ **WHAT SURVIVES')
log = original[original.index('## WEEKLY DATA LOG'):original.index('## MONITORING SCHEDULE')]
table = [line for line in log.splitlines() if line.startswith('|')]
kept_rows = [line for line in table[2:] if line.startswith('| **Oct 5**')]
assert len(kept_rows) == 1
meta = json.loads((ARCHIVE / 'manifest.json').read_text())['files']['demand_destruction/TRACKER.md']
receipt = f"[Verbatim before-image](../{meta['before_image']}): {meta['bytes']} UTF-8 bytes, crc32 `{meta['crc32']}`; payload rule whole file. [Manifest](../archive/2026-10-14_operational-followups/manifest.json)."
intro = '''# DEMAND DESTRUCTION TRACKER

> # 📟 **REGISTERED ALERT LINES — THIS BLOCK IS READ AT RUN TIME BY THE FOUR CLOUD ROUTINES. IT IS THE SINGLE POINT OF TRUTH FOR WHAT THEY WATCH.**
> **October14 operational follow-up — SCOPED-PARTIAL:** line4 now uses direct EIA October12 gasoline, postedOctober14. Fresh utilization API returns92.7% forOctober2; present but12d old versus unchanged10d observation budget, not a missing series. Lines1–3/5–6 retain October7release/weekOctober2 values; line8 retains savedCOT#9, current raw fetch403; lines9–11 retain October7 captures. No new paired/settlement/holding/BRT31grade. Do not read a document edit as a new observation. [Evidence](../audits/2026-10-14_operational-followups/REPORT.md).
> **Next existing releases:** WPSR ThursdayOctober15noonEDT/weekOctober9; COT#10 FridayOctober16~15:30ET/asofOctober13. Existing saved routine prompts are verified; live scheduler configuration/normal-run acceptance remain UNVERIFIED. See SCHEDULED_RUNS.md and the existing CATO handoff.

'''
out = intro + live + '\n## Operative letters retained from dated adjudications\n\n'
out += 'The original dated reasoning is archived. These excerpts preserve existing restrictions; their old measurements are historical. Current grades belong to their canonical owners.\n\n'
out += cushing + '\n' + basis + '\n' + capture + '\n' + premium + '\n'
out += '### AIS coverage restriction\n\n' + zero
out += '\n`KILL-LEG2-TRANSIT` is retired; the old August NOT-FALSIFIED label is history, not a current test. Denominator/never-blend convention: [HORMUZ_TRANSIT_BASELINE](../domain/HORMUZ_TRANSIT_BASELINE.md). AIS corroborates, never fires alone under BG02; no single-vendor hub diagnostic substitutes into that rule.\n\n'
out += '## WEEKLY DATA LOG\n\nAll original weekly rows are preserved in the before-image below; the original table header remains here for future routine appends. Newer saved core evidence is October7/weekOctober2, and the latest scheduled routine is [FridayOctober9](data/friday_2026-10-09.md); the alert table above carries the reconciled state. No missing weekly row or run was fabricated.\n\n'
out += '\n'.join(table[:2]) + '\n\n'
out += '## Historical alerts, models and prior weekly rows\n\n' + receipt + '\n\n'
out += 'The March/July PathB tables, timing model, NOPI scorecard and old all-three-triggers/exit-all-longs instruction are historical. Current phase interpretation: [THESIS](../thesis/THESIS.md); demand grading: [BRT31note](../thesis/prediction_notes/BRT-31.md); action/holding authority: [TRADE](../TRADE.md). No archived rule is reactivated by a link.\n\n'
out += '## MONITORING SCHEDULE\n\nExisting actual routine mirror and installation gaps: [SCHEDULED_RUNS](../SCHEDULED_RUNS.md). Dated releases: [CATALYSTS](../docket/CATALYSTS.tsv); holiday exceptions govern over a generic Wednesday label. No new schedule or monitor created.\n\n'
out += '## CROSS-AGENT ROUTING\n\nCanonical topology: [network](../../_NETWORK.md). BRENT supplies dated energy facts and limits; consumer/inflation/credit conclusions remain with their owners. A signal or an archived PathB combination does not authorize a trade.\n\n'
out += '## KEY REFERENCES\n\n[Current composite](DEMAND_COMPOSITE.md), [THESIS](../thesis/THESIS.md), [registered tests](../workbook/REGISTRY.tsv), [TRADE decision paths](../TRADE.md). [TRANSITION_MATRIX](TRANSITION_MATRIX.md), [MATRIX_REVIEW](MATRIX_REVIEW.md), [HOARDING](HOARDING.md), [ANALOGS](ANALOGS.md) and [HAMILTON](HAMILTON.md) retain their historical research dates. Frozen KB/VX/FLOW are not current observations.\n'
assert len(out.encode()) < 32550
for index in range(1, 12):
    before = next(line for line in original.splitlines() if line.startswith(f'> | {index} |'))
    after = next(line for line in out.splitlines() if line.startswith(f'> | {index} |'))
    assert after == (new_gas if index == 4 else before)
target.write_text(out)
(HERE / 'tracker-retained-blocks.json').write_text(json.dumps({'retained_exact_slices': retained, 'changed_live_line': {'before': old_gas, 'after': new_gas}, 'before_bytes': len(original.encode()), 'after_bytes': len(out.encode())}, indent=2)+'\n')
print('Tracker:', len(original.encode()), '->', len(out.encode()), 'UTF-8 bytes; all eleven lines retained, only line4 observation changed')
