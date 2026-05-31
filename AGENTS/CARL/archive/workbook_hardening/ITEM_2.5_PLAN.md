# Item #2.5 — KB→VX Reference Integrity Plan

**Created:** 2026-05-02 (planning session, no mutations yet)
**Status:** READY TO EXECUTE — Session 1 first
**Source artifact:** `workbook/AUDIT_2026-05-02.md` Item #2.5 entry, this session's planning conversation, and external agent feedback in `User Input/Two responses.md`

This document is self-contained. A fresh CARL session should be able to execute Session 1 without re-reading the planning conversation.

---

## Live state (verified 2026-05-02)

**Re-validate this number first** by running the enumeration script in §Appendix A. Original SCRATCH said "43 dangling refs" but a SUPERSEDED-format-only scan undercounted. Comprehensive scan shows:

| Metric | Count |
|---|---|
| Distinct dangling VX IDs in KB.tsv | **43** |
| Total dangling KB→VX edges | **59** |
| KB rows affected | ~50 (some rows reference >1 dangling ID) |

### Four naming generations co-existing in KB.Vectors col

| Generation | Pattern | Example | Dangling count |
|---|---|---|---|
| Decimal-legacy | `VX-CARL-N.NN` | `VX-CARL-1.10` | 1 ID, 2 edges |
| Fragment | `VX-CARL-N` | `VX-CARL-5` | 1 ID, 1 edge |
| Standard | `VX-CARL-FAMILY-NN` | `VX-CARL-MTG-01` | 34 IDs, 47 edges |
| Multitoken | `VX-CARL-FAMILY-DOMAIN` | `VX-CARL-ABS-AUTO-ALLY` | 7 IDs, 9 edges |

**Side-finds folded into this work:**
- `VX-CARL-MACRO-05` appears **twice** in VX.tsv (duplicate row — one needs renumbering)
- `SCHEMA.tsv` description for `Delegated_To` says "Status should typically be SUPERSEDED" but Item #2a actually preserved Status=ACTIVE for delegated rows. Description is wrong, needs edit.

---

## Methodology rule (codify before execution)

**Lesson from Item #2d:** Cluster-pattern matching ("these are both about oil") is unreliable for SUPERSEDED-by-pointer dispositions. Verification revealed only 7 of 22 initial SUPERSEDED candidates actually carried forward the load-bearing content; 14 were downgraded to STALE.

**The same risk applies to VX consolidation:**

> **Before any CREATE that bundles >1 KB row, AND before any REDIRECT, verify that the proposed Green/Yellow/Red threshold bands actually apply to all rows being bundled or redirected.** If they don't — split into separate vectors, or REMOVE the ref. Topical adjacency is not vector identity.

**Worked example of failure mode:**
- KB-154 (plasma donations) is a *lower-cohort behavioral signal*
- KB-111 (JPM retail equity flow) is an *upper-cohort positioning signal*
- They are both "K-shape" topically, but no single Green/Yellow/Red threshold measures both
- Bundling them under one VX-CARL-K-01 vector would produce an umbrella-with-no-shared-threshold, same problem as the SUPERSEDED-by-pointer failures

**Add to CARL CLAUDE.md** as a standing rule under "OUTPUT RULES" or new "WORKBOOK DISCIPLINE" section before Session 1 begins.

**Threshold-uncertainty flagging (Agent B):** Any threshold band drafted under uncertainty should be marked `[FLAG: uncertain — Will to review]` in the Notes column. Don't bury judgment calls in clean-looking structure.

---

## Pre-disposition framework (rough — to be firmed in Session 1)

Disposition actions:

| Action | Meaning | Touches |
|---|---|---|
| CREATE | Add new VX row to VX.tsv | VX.tsv (append) |
| REDIRECT | Swap KB.Vectors VX ID for an existing one | KB.tsv (in-place edit) |
| REMOVE | Blank the bad ref from KB.Vectors (preserve other refs, preserve Status) | KB.tsv (in-place edit) |
| VX_DEDUPE | Renumber the duplicate MACRO-05 row | VX.tsv (in-place edit) + any affected KB refs |

**Rough first-pass disposition expectations** (subject to verify-by-reading-target):

### Likely CREATE (~7 rows, possibly more after multitoken review)
- **K-01** — K-shape lower-cohort framework (KB-154/155/156/157 + KWLTH-01/KB-091)
- **WEALTH-01** — Upper-decile wealth/positioning, V14 (KB-237 + KSHAPE-01/KB-111 if threshold fits)
- **DSL-01** — Diesel divergence (KB-253, current open thread per ROADMAP)
- **AG-01** — Farm bankruptcies / food CPI loading (KB-251)
- **FL-01** — FL multi-vector composite (KB-113; possibly absorbs STATE-FL/KB-249)
- **CC-01** — CC 90+ DQ stress anchor (KB-096/155/243; CRL-05 metric)
- **SAV-01** — Savings rate, live STATUS metric at 4.0% (KB-098)

### Likely REDIRECT (only after verify-by-reading-target)
- **KSHAPE-01 (KB-111)** → WEALTH-01 (NOT K-01) — upper-K positioning, not lower-K behavior
- **KWLTH-01 (KB-091)** → K-01 — Reuters K-shape narrative is framework-level
- **FERT-01 (KB-101)** → FOOD-01 only if threshold fits

### Likely REMOVE (KB row stands without VX linkage)
- All decimal-legacy + fragment: VX-CARL-1.10, VX-CARL-5
- HSG-06..11 (10 KB rows): early-Feb pre-taxonomy housing snapshots
- MTG-01/016/020/021/022 (7 KB rows): entire MTG family doesn't exist; legacy
- FHA-01/03 (3 KB rows), DQ-01/02 (2), CREDIT-01, DEMO-01, STRESS-01, LAB-01, RETAIL-01 (KB-094 STALE), 401K-01 (KB-009 CONFIRMED)
- **RV-01, FF-01, AUTO-01** (moved here from REDIRECT after agent pushback): topical adjacency only

### Multitoken category — verify before disposing (~7 IDs)
- ABS-AUTO-ALLY (KB-105), ABS-AUTO-CACC (KB-106), ABS-AUTO-SPREAD (KB-153) — current and ACTIVE; CREATE new VX rows or fold into ABS-* family (already 17 rows). Decide based on whether ABS family schema admits subprime-auto naming.
- AUTO-CVNA (KB-027/152), CVNA-GT (KB-107) — Carvana-specific; fold into AUTO-MIX-* if covered, else CREATE
- LABOR-ICE-01 (KB-103/104) — likely REMOVE (LABOR domain, not CARL VX scope)
- STATE-FL (KB-249) — likely fold into FL-01 CREATE

---

## Session 1 — Verification & Disposition Firming (~60 min)

**Goal:** Produce a complete, reviewable dispositions artifact at `workbook/ITEM_2.5_DISPOSITIONS.md`. **ZERO mutations to TSVs.** Pure planning output.

### Step 1.0 — Codify methodology rule (~5 min)
Edit `AGENTS/CARL/CLAUDE.md` to add the verify-by-reading-target rule (text in §Methodology rule above) under appropriate section. Commit separately or fold into Session 2 commit.

### Step 1.1 — Re-validate the live count (~5 min)
Run the enumeration script in §Appendix A. Confirm 43 IDs / 59 edges. If different from this plan, update plan and proceed.

### Step 1.2 — Verify-by-reading on all 43 dangling IDs (~25 min)
For each dangling VX ID:
1. List the KB row IDs that reference it
2. Read each KB row's Date, Status, Fact (first 200 chars), Notes, full Vectors col
3. Decide disposition per row (not per VX ID — same VX ID may produce different actions for different KB rows referencing it)
4. Apply the methodology rule: if proposing CREATE bundling, can a single threshold measure all bundled rows? If proposing REDIRECT, does the target's threshold structure measure THIS row's claim?

### Step 1.3 — Draft CREATE specs (~20 min)
For each confirmed CREATE row, draft the full 11-col VX schema:
- ID, Name, Current_Value, Status, Green, Yellow, Red, Frequency, Source, Last_Refreshed, Notes

For Current_Value, pull from STATUS.md where the metric is tracked (CC 90+ DQ, savings rate, etc.).

For Green/Yellow/Red bands:
- If a clear historical threshold exists (GFC peak for CC, V8/V14 boundaries for K-01/WEALTH-01), use it
- If uncertain, mark `[FLAG: uncertain — Will to review]` in Notes
- Cite the source reasoning for each band in Notes

### Step 1.4 — Architectural fold-in scoping (~5 min)
- Confirm MACRO-05 duplicate fix logic (which row gets renumbered, where do KB refs to it currently point)
- Confirm SCHEMA.tsv Delegated_To description edit (1-line text fix)
- Confirm whether any of the 7+ CREATEs lands in POP-domain territory (probably AG-01 — flag with `Delegated_To=POP` in Notes per the Item #2d precedent for KB-169/251)

### Step 1.5 — Write the disposition artifact (~10 min)
Output `workbook/ITEM_2.5_DISPOSITIONS.md` with:
- Verified count + breakdown by naming generation
- Per-VX-ID disposition table: VX-ID | KB rows | disposition | reasoning | verified-by-reading? Y/N
- 7+ CREATE row drafts (full VX schema, ready to paste)
- 3 architectural items (MACRO-05, SCHEMA description, POP defer note)
- Open questions for Will (any thresholds flagged uncertain)
- Estimated mutation counts for Session 2

**Session 1 deliverable:** Single review-ready MD file. Nothing in TSVs touched.

**Approval gate:** Will reviews `ITEM_2.5_DISPOSITIONS.md`. Pushes back or approves to execute. **Do not proceed to Session 2 without approval.**

---

## Session 2 — Execute & Validate (~45 min)

**Pre-step:** Read `ITEM_2.5_DISPOSITIONS.md` cold. Confirm it's the approved version.

### Step 2.1 — Build mutation script (~20 min)
`/tmp/fix_kb_2.5.py` modeled on `/tmp/fix_kb_2d.py`. DISPOSITIONS dict drives 4 action types:
- `CREATE_VX`: append rows to VX.tsv (full 11-col schema from Session 1 doc)
- `REDIRECT_REF`: swap VX ID in KB.Vectors col (preserve other refs, preserve Status)
- `REMOVE_REF`: blank just the bad VX ref token (preserve other refs, preserve Status, preserve commas/structure)
- `VX_DEDUPE`: renumber the duplicate MACRO-05 row, update any KB refs to it

**Backup before run:**
- `/tmp/VX.tsv.bak_2.5_{epoch}`
- `/tmp/KB.tsv.bak_2.5_{epoch}`

**Bug to watch for:** Item #2d had a Python list-by-reference bug that propagated a Stale_By blank from one row to a copied row. Use deep copy or fresh row assembly per mutation.

### Step 2.2 — Apply (~5 min)
- Run script
- Verify expected mutation counts match Session 1 plan
- Spot-check 5 KB rows + new VX rows visually

### Step 2.3 — Verification (~5 min)
- Re-run dangling-ref enumeration (§Appendix A) → expect **0 dangling**
- Re-run audit_kb.py (or equivalent) → no new violations
- Confirm KB row count unchanged at 260, VX row count = 110 + N (CREATE count)
- Confirm MACRO-05 dedupe: only one row with that ID

### Step 2.4 — Architectural fold-ins (~10 min)
- Edit `SCHEMA.tsv` `Delegated_To` description (preserve-Status logic; 1-line text fix)
- MACRO-05 dedupe applied via S2.1 script
- Add KB→VX integrity check spec to validator backlog (prep for Item #3, no implementation yet)

### Step 2.5 — Document & commit (~5 min)
- `workbook/AUDIT_2026-05-02.md`: add Item #2.5 resolution log entry (per-disposition breakdown + final state)
- `ROADMAP.md`: move Item #2.5 from OPEN THREADS → RECENTLY RESOLVED
- `SCRATCH.md`: rewrite for next session per template
- Single commit: `CARL: workbook hardening Item #2.5 — VX reference integrity (N CREATE + M REDIRECT + K REMOVE + dedupe)`

**Session 2 deliverable:** Clean dangling-ref check (0 dangling). Workbook integrity restored.

---

## Risks & mitigations

1. **S1 surprise count growth.** If verify-by-reading surfaces a 5th naming generation or load-bearing rows that change disposition mix significantly, table grows.
   *Mitigation:* time-box S1 at 75 min hard. If blown, escalate to Will, pause, don't push through.

2. **Threshold uncertainty on CREATE rows.** WEALTH-01 (V14) and FL-01 (composite) don't have crisp single-source thresholds.
   *Mitigation:* flag uncertain ones in Notes per Agent B's rule. Do not paper over.

3. **POP-domain CREATE leak.** AG-01 (farm bankruptcies) feels POP-domain. POP doesn't have a KB.tsv yet.
   *Mitigation:* AG-01 stays in CARL VX with `Delegated_To=POP` flagged in Notes. No physical move attempted (matches Item #2d precedent for KB-169/251).

4. **Session boundary error.** If Session 1 disposition doc is approved but then Will changes mind during Session 2 execution, mid-execution rollback is messy.
   *Mitigation:* approval-gate is firm. If Will pushes back during S2, abort apply, revert from backup, reset.

---

## Files involved

| File | S1 reads | S1 writes | S2 reads | S2 writes |
|---|---|---|---|---|
| `workbook/KB.tsv` | ✓ | — | ✓ | ✓ (mutate) |
| `workbook/VX.tsv` | ✓ | — | ✓ | ✓ (append + dedupe) |
| `workbook/SCHEMA.tsv` | ✓ | — | ✓ | ✓ (description fix) |
| `workbook/AUDIT_2026-05-02.md` | ✓ | — | ✓ | ✓ (log entry) |
| `workbook/ITEM_2.5_PLAN.md` (this file) | ✓ | — | ✓ | — |
| `workbook/ITEM_2.5_DISPOSITIONS.md` | — | ✓ (create) | ✓ | — |
| `STATUS.md` | ✓ (for Current_Value) | — | — | — |
| `CLAUDE.md` (CARL) | ✓ | ✓ (methodology rule) | — | — |
| `ROADMAP.md` | — | — | ✓ | ✓ (move thread) |
| `SCRATCH.md` | — | — | ✓ | ✓ (rewrite) |

---

## Open architectural questions (deferred — DO NOT resolve in 2.5)

These are real, but they're not blocking 2.5. Acknowledge them in the AUDIT log Item #2.5 entry but defer to a future session:

1. **POP needs a KB.tsv** if physical-move-to-sub-agent becomes the canonical pattern. Currently uses ML.tsv with different schema. Affects KB-169, KB-251, possibly future AG-01 delegation.
2. **44 existing HOMER-delegated rows** weren't physically moved in Item #2d — only the new KB-202 was migrated. Migration backlog if physical-move becomes canonical.

These were flagged by external agents (`User Input/Two responses.md`) and are correctly deferred per Agent B's framing.

---

## Appendix A — Dangling-ref enumeration script

Run as starting point of both Session 1 (validate) and Session 2 (post-apply verification).

```python
import csv, re
from collections import defaultdict

vx_ids = set()
with open('workbook/VX.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        if row and row[0].startswith('VX-CARL-'):
            vx_ids.add(row[0])

dangling = defaultdict(list)
all_refs = defaultdict(list)
kb_total = 0

with open('workbook/KB.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    header = next(reader)
    vec_idx = header.index('Vectors')
    id_idx = header.index('ID')
    status_idx = header.index('Status')
    for row in reader:
        if not row or not row[id_idx].startswith('KB-CARL-'):
            continue
        kb_total += 1
        if len(row) <= vec_idx: continue
        # Split on whitespace/commas; check each token starts with VX-CARL-
        tokens = re.split(r'[\s,]+', row[vec_idx])
        for tok in tokens:
            tok = tok.strip().rstrip('.').rstrip(',')
            if tok.startswith('VX-CARL-'):
                all_refs[tok].append(row[id_idx])
                if tok not in vx_ids:
                    dangling[tok].append((row[id_idx], row[status_idx]))

# Categorize
buckets = {'DECIMAL': [], 'STANDARD': [], 'MULTITOKEN': [], 'OTHER': []}
for vx_id in dangling:
    suffix = vx_id.replace('VX-CARL-', '')
    if re.match(r'^\d+\.\d+$', suffix):
        buckets['DECIMAL'].append(vx_id)
    elif re.match(r'^[A-Z0-9_]+-\d+$', suffix):
        buckets['STANDARD'].append(vx_id)
    elif re.match(r'^[A-Z0-9_]+(-[A-Z0-9_]+)+$', suffix):
        buckets['MULTITOKEN'].append(vx_id)
    else:
        buckets['OTHER'].append(vx_id)

print(f"Dangling IDs: {len(dangling)} | Edges: {sum(len(v) for v in dangling.values())}")
for bn, ids in buckets.items():
    if ids:
        edges = sum(len(dangling[i]) for i in ids)
        print(f"\n{bn}: {len(ids)} IDs / {edges} edges")
        for vx in sorted(ids):
            kbs = ', '.join(sorted(set(r[0].replace('KB-CARL-', '') for r in dangling[vx])))
            print(f"  {vx} [{len(dangling[vx])}]: {kbs}")
```

**Expected Session 1 output:** 43 dangling IDs / 59 edges (1 DECIMAL + 1 OTHER + 34 STANDARD + 7 MULTITOKEN).
**Expected Session 2 post-apply output:** 0 dangling IDs / 0 edges.

---

## Appendix B — Agent feedback summary

External multi-agent peer review (`User Input/Two responses.md`) caught material errors in the original plan draft:

| Catch | Adopted? | Reason |
|---|---|---|
| Count was 43/59 not 47/34 (which itself was wrong) | ✓ | My regex missed multitoken + decimal patterns |
| K-01 collapse risks topical-umbrella failure | ✓ | KB-154 plasma vs KB-111 retail flows can't share threshold |
| 3 REDIRECTs (RV-01, FF-01, AUTO-01) flagged as topical-adjacency | ✓ | Likely become REMOVE after verify-by-reading |
| 3 missed ABS-AUTO refs (KB-105/106/153) | ✓ | These are the multitoken pattern |
| MACRO-05 duplicate in VX.tsv | ✓ | Folded into S2 dedupe step |
| SAV-01 should be 7th CREATE | ✓ | KB-098 is live STATUS metric |
| Methodology rule belongs in CLAUDE.md | ✓ | Added as S1 step 1.0 |
| Threshold-uncertainty flagging in Notes | ✓ | Added as S1 step 1.3 rule |
| REMOVE caveat (check load-bearing dependence) | ✓ | Folded into per-row verify in S1.2 |
| Sub-vector nesting (K-01.RETAIL / K-01.WEALTH) | ✗ | VX schema is flat ID-Name-Value; two separate vectors with cross-refs in Notes is cleaner |

Agent feedback file is at `User Input/Two responses.md`. Read for full context if S1 surfaces unexpected questions.
