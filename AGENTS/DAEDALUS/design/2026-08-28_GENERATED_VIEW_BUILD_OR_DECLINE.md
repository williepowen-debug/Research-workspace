# ⑱ GENERATED VIEW OVER OWNER SURFACES — BUILD-OR-DECLINE (decided at the 8/28 wiring sweep, per Will 8/22 "approve on the waiting decision")

**Owner:** DAEDALUS · **Date:** 2026-08-28 · **Origin:** RAV residual concerns items 1 + 5 (`PROME/codex/2026-08-22_RAV_residual-concerns.md` rows 1/4/5) → PROME fold packet `inbox/2026-08-22b` → WILL_QUEUE row 89. **Scope guards honored:** no second store · labels canonical at surfaces, map derived (`render_directory.py` model) · CHECK_STANDARD §12 base-rate-before-wiring.

## Decision: **DECLINE-WITH-TRIGGERS** (both halves), re-open on measured conditions — not on a date

The fold bought a date so RAV's residual ("depends on the generated-view discipline existing later") stops being open-ended. The date arrived; the base rate was measured; **a map built today would be a map of almost nothing**, which is PAT-088 (a declared inventory is empty until its source surfaces carry the rows) and PAT-113 (a regenerated surface with no wired source dies at the next regeneration).

| Half | What it would join | Base rate measured 2026-08-28 | Verdict | Re-open trigger (pre-registered, measurable by one command) |
|---|---|---|---|---|
| **(1) Single-place-to-SEE-corrections view** (RAV item 5 rider; Forum-6 index-not-store) | `AGENTS/WALTER/registry/CORRECTIONS.tsv` (R1 register) + per-desk `registry/corrections_receipts.tsv` | Register = **2 rows**; receipts files exist at **3 of 37** desks (CREED, RED, WALTER); R1 boot leg wired at **1/37** (batch changelist in front of Will today) | **DECLINE for now** — the register IS the single place; a view over 2 rows is decoration | Build when `CORRECTIONS.tsv` ≥ **20 rows** OR R1 receipt coverage ≥ **80%** (the 9/26 withdrawal-test threshold) — whichever first; `python3 scripts/corrections_boot_check.py --coverage` is the instrument |
| **(2) Generated authority map** (RAV item 1; PAT-124 discoverability; hand-map PRE-DECLINED) | Class 1-ext role labels (`CANONICAL` / `DERIVED` / `SCRATCH` / `HISTORICAL`) declared in surface headers | **16 of 1,641** shared (non-`AGENTS/`) `.md` surfaces carry a role label in their first 6 lines = **1%** | **DECLINE** — a join over 1% is a map of 16 files, and the 99% would read as "unlabeled", which a reader will take as "no authority" (the PAT-129 perimeter-launder shape) | Build when ≥ **25%** of shared surfaces carry a label (grep given below), OR when a second consumer beyond RAV asks for it. Labels accrue conform-on-touch (Class 1-ext is forward-only by ruling); no batch-labeling sweep is proposed — that would be the hand-map by another name |

**The measuring command for trigger (2), so the next reader re-runs it rather than trusts this number:**
```
python3 - <<'EOF'
import glob,re; lab=re.compile(r'\b(CANONICAL|DERIVED|GENERATED|SCRATCH|HISTORICAL)\b'); n=h=0
for p in glob.glob("**/*.md",recursive=True):
    if p.startswith(("AGENTS/","memory/",".venv","FORGE/_archive","FORGE/timing")) or "/archive/" in p or "/_archive/" in p: continue
    n+=1; h+= bool(lab.search("".join(open(p,errors="replace").readlines()[:6])))
print(f"{h}/{n} = {100*h/n:.0f}% labeled")
EOF
```

## What the decline does NOT do
- It does not withdraw Class 1-ext (the labels stay the ruled forward-only convention; `render_directory.py` remains the worked DERIVED-map example).
- It does not re-open RAV's declined ledger — the R1 register is the store; this only says the VIEW over it is premature.
- It leaves RAV item 4's concern answered in the form it asked for: "later" now has two measurable conditions instead of a date.

**Return:** PROME registers this at WILL_QUEUE row 89 as DECIDED-DECLINE-WITH-TRIGGERS; Will's word closes or overrides it. — DAEDALUS
