# WP1 — TALOS Report: CARL Sub-Agent CLAUDE.md Fixes (2026-07-10)

**Agent:** TALOS (editor, under DAEDALUS) · **Scope:** `AGENTS/CARL/sub_agents/{STUE,HOMER,DOC,GIG,POLLY,POP}/CLAUDE.md` ONLY · **Driver:** `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md`
**Fence honored:** only the six CLAUDE.md files touched. No STATUS.md, no workbook TSV, no CARL top-level, no PHAN/META. No git commands run (DAEDALUS commits the batch).
**Method:** Read every target file + verified every audit claim against disk (`ls`, TSV row counts, `state_vectors/` contents) BEFORE editing. Row counts = non-empty data rows excl. header.

---

## Per-file changelist

### STUE
| Fix-class | Line(s) (orig) | Before → After |
|---|---|---|
| SV ghost path | 110 | `**Location:** ../SHARED/state_vectors/incoming/...` → `**Channel:** write to own `state_vectors/`, `SV-STUE-YYYY-MM-DD-NN.md`, CARL reads at harvest` + provenance comment; `**Filename:**` line kept |
| Threshold header | 67 | `| Metric | Current | ...` → `| Metric | Current (build-vintage snapshot) | ...` |
| Threshold note | after 74 | added `> Live values live in STATUS.md's dashboard — ... snapshot column is NOT current ...` |
| Key Files dirs | 90-94 | added `research/`, `domain/`, `state_vectors/` (all exist on disk, were undocumented) |

### HOMER
| Fix-class | Line(s) (orig) | Before → After |
|---|---|---|
| SV ghost path | 135 | `../SHARED/...` → canonical `state_vectors/` channel + provenance comment; `**Filename:**` kept |
| Threshold header | 73 | `Current` → `Current (build-vintage snapshot)` |
| Threshold note | after 85 | added snapshot note |
| Key Files dirs/files | 107-119 | added `KB.tsv` (canonical, exists, was omitted from workbook enum) + `state_vectors/` dir (exists) |
| Wrong count | 181 | `workbook/KB.tsv, 45 entries` → `65 entries` (verified: 65 data rows) |

### DOC
| Fix-class | Line(s) (orig) | Before → After |
|---|---|---|
| SV ghost path | 131 | `../SHARED/...` → canonical `state_vectors/` channel + provenance comment; `**Filename:**` kept |
| Threshold header | 65 | `Current` → `Current (build-vintage snapshot)` |
| Threshold note | after 74 | added snapshot note |
| Wrong count | 100 | `VX.tsv ... (12 vectors)` → `(18 vectors)` (verified 18 data rows, none superseded) |
| Wrong count | 102 | `FLOW.tsv ... (5 flows)` → `(7 flows)` (verified 7) |
| Key Files dirs | 106-113 | added `state_vectors/` (exists); `sources/` annotated "created on demand; not present"; `archive/` (4 named files) annotated "deleted in 2026-06 public-prep prune, commit 1cb18fbc" (files gone from disk) |

### GIG
| Fix-class | Line(s) (orig) | Before → After |
|---|---|---|
| SV ghost path | 120 | `../SHARED/...` → canonical `state_vectors/` channel + `(Prior SVs live in outbox/)` + provenance comment; `**Filename:**` kept |
| Threshold header | 63 | `Current` → `Current (build-vintage snapshot)` |
| Threshold note | after 70 | added snapshot note |
| Wrong count | 97 | `VX.tsv ... (18 vectors)` → `(17 vectors)` (verified 17; audit-confirmed) |
| Wrong count | 98 | `ML.tsv ... (13 entries)` → `(18 entries)` (verified 18; audit-confirmed) |
| Wrong count | 173 | `(18 vectors, 5 CRITICAL)` → `(17 vectors, 6 CRITICAL)` (VX status col: 6 CRITICAL) |
| Key Files dir | 101-103 | added `outbox/` (exists, holds SV-GIG-*.md); `sources/` + named file already correct, untouched |

### POLLY
| Fix-class | Line(s) (orig) | Before → After |
|---|---|---|
| SV ghost path | 127 | `../SHARED/...` → canonical `state_vectors/` channel + provenance comment; `**Filename:**` kept |
| Threshold header | 57 | `Current` → `Current (build-vintage snapshot)` |
| Threshold note | after 69 | added snapshot note |
| Key Files dirs | 101-108 | `sources/` annotated "created on demand; not present"; `archive/` (4 named legacy files) annotated "deleted in 2026-06 public-prep prune, commit 1cb18fbc" (none exist on disk) |

### POP
| Fix-class | Line(s) (orig) | Before → After |
|---|---|---|
| SV ghost path | 133 | `../SHARED/...` → canonical `state_vectors/` channel + provenance comment; `**Filename:**` kept |
| Threshold header | 63 | `Current` → `Current (build-vintage snapshot)` |
| Threshold note | after 74 | added snapshot note |
| Key Files path fix | 106-113 | `sources/ (research deep dives go here)` → `domain/sources/` with the 2 real files (`INVISIBLE_INCOME_DEEP_DIVE.md`, `SB_BANK_PIPELINE_DEEP_DIVE.md` — exist there); `archive/` (4 named files) annotated "deleted in 2026-06 public-prep prune, commit 1cb18fbc" |

---

## VERIFIED (re-read each edited region after editing)

- **Ghost path eradicated:** `grep -rn "SHARED/state_vectors"` across all six → **0 hits**. All 6 carry the `<!-- SV channel corrected 2026-07-10 -->` provenance comment.
- **Threshold fix uniform:** all 6 files have header `Current (build-vintage snapshot)` and exactly 1 snapshot-note line each, placed directly below the table before the next `##` header.
- **Count fixes (each independently re-counted, header excluded):** GIG VX=17, GIG ML=18, GIG CRITICAL=6 (status col tally); DOC VX=18, DOC FLOW=7; HOMER KB=65. No superseded/retired rows masked any count (checked DOC VX status col — all live; GIG VX status col — 1 BREACHED/6 CRITICAL/5 ELEVATED/1 INFO/4 NORMAL = 17).
- **Dir annotations match disk:** verified via `ls` — STUE has research/domain/state_vectors (added); HOMER has state_vectors + workbook/KB.tsv (added); DOC/POLLY have NO sources/ or archive/ (annotated, not silently deleted); POP has domain/sources/ with both named files (path corrected from top-level `sources/`); GIG has outbox/ with SV-GIG files (added).
- **`state_vectors/` confirmed as the real channel:** STUE (2 SVs), HOMER (1 SV + corrected/), DOC (3 SVs) all hold live SV files — validates the canonical-channel text for the three that already use it.
- Key Files code-blocks re-read post-edit (DOC, POP, STUE SV block shown) — render cleanly, no broken fences.

## SKIPPED / NOT-AS-DESCRIBED (no forced fixes)

- **POLLY VX count (13), POLLY FLOW (5), POP VX (17), POP FLOW (5), GIG FLOW (6), GIG PREDICTIONS (8):** re-counted, all **already correct** — left untouched.
- **GIG `sources/` + baseline file (lines 101-103, 184):** exist on disk exactly as documented — **not a defect**, left as-is (only added the undocumented `outbox/`).
- **PHAN / META:** out of scope — not touched.
- **Prune-provenance (commit `1cb18fbc`):** annotated per the audit's stated provenance; I did **not** run `git log` to independently confirm the SHA (task barred git commands). The annotation is sourced to the audit, and the four named files' absence from disk was directly verified by `ls`.
- **GIG SV go-forward channel:** GIG currently delivers SVs to `outbox/` (not `state_vectors/`). Per fix-#1's explicit "apply to all six" + canonical `state_vectors/` text, I set the go-forward channel to `state_vectors/` uniformly and flagged the existing `outbox/` SVs inline (`(Prior SVs live in outbox/)`) rather than silently diverging — surfaced here for DAEDALUS/CARL awareness (this is a genuine practice-vs-canon delta, not a doc typo).
- **CARL-lane items left untouched as instructed:** all `KB-CARL-*` / `VX-CARL-*` cross-ref IDs, VX-CARL-SL-01..07 ranges, frozen VX.tsv references, HOMER's "40 housing entries delegated (Apr 13)" historical migration fact (only the stale *current* count 45→65 was fixed). No predictions resolved, no data values changed beyond the mechanical row-counts.

---

**BOTTOM LINE:** All 6 files fixed, all 4 fix-classes applied, every audit claim verified against disk before editing. Ghost SV path gone fleet-of-six-wide; threshold tables now self-label as build-vintage snapshots; 6 wrong counts corrected (GIG ×3, DOC ×2, HOMER ×1); directory blocks reconciled to disk (adds for existing-undocumented, annotations for pruned/on-demand, path fix for POP). One practice-vs-canon delta surfaced (GIG outbox vs state_vectors). Ready for DAEDALUS batch commit.
