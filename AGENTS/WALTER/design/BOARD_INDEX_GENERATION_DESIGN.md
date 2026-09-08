# BOARD/INDEX.md — GENERATE, don't shard. Design note v0.1 (DRAFT, 2026-09-04)

**Owner:** WALTER (BOARD_CONSUMPTION_SPEC owner). **Asked by:** PROME packet 2026-09-03 21:4x (Codex workspace audit §4 "Generate the BOARD index", Will "approved go ahead" on PROME's sequence). **Status:** WQ-174 APPROVED 2026-09-04; cutover IMPLEMENTED in the working tree 2026-09-08 under L273. Commit/push pending PROME serialization. Receipt: `../outbox/2026-09-08_board-index-cutover-receipt.json`. The v0.1 design and historical measurements below are preserved.

## 0. The call in one paragraph

**Generate `BOARD/INDEX.md` in place from signal frontmatter, keep its exact structure (preamble · cluster ToC · `## CLUSTER (N)` sections · `**TOTAL**`), cut each row to a derived compact form.** Do **not** shard by month: every live consumer navigates by cluster or greps by ID/name, none by month, and sharding changes 13 boot surfaces plus the doctor's parser for no reader benefit. A compact in-place regeneration changes **zero readers**, cuts the file **~81%** (1,628,719 B → ~310 KB measured projection), and, more importantly than the bytes, **makes the correction back-marker DERIVED** — which is the failure this desk keeps paying for by hand (11 of 57 correction links had no INDEX back-marker this morning; 4 were mine from yesterday).

## 1. Measurements (2026-09-04, HEAD `ab60c638e`)

| Quantity | Value |
|---|---|
| INDEX size / rows | 1,628,719 B / 880 rows |
| Row bytes: median / p90 / max | 1,178 / 3,560 / 11,107 |
| Largest cluster section (IRAN_HORMUZ, 154 rows) | 316,222 B — **9.7× the 32,550 B read budget for a "drill into your cluster"** |
| Compact projection (id · date · cluster · precedence · action→info · H1 title ≤140 · file) | **308,834 B, avg 350 B/row** |
| Largest cluster section after compaction (est.) | IRAN ~54 KB · BANK_COLLATERAL ~43 KB · CONSUMER_STAGFLATION ~47 KB |
| Rows carrying a lifecycle/correction marker | 46 |
| …of which have NO `status:`/`corrects:` header of their own | 22 → 12 derivable by inverting `corrects:`; **10 are hand-annotation only** (§5 list) |
| Signals with a `status:` header whose INDEX row is UNMARKED | **39 of 46** — the INDEX is *behind the files*, not ahead of them |
| Correction links (`corrects:` → target) / INDEX back-marker absent | 57 / 11 at boot (4 fixed 9/4 by hand; 7 remain, 8/19–8/28) |

**Read:** the bytes are the visible problem; the two marker gaps are the load-bearing one. A hand-maintained derived surface drifts in BOTH directions and nothing measures it. A generator makes it a projection.

## 2. Who reads it, and how (enumerated — the answer to PROME's "human/boot readers are yours")

| Reader | Operation on INDEX.md | Affected by compaction? | Affected by month-shards? |
|---|---|---|---|
| `walter_doctor.py` (board_reconcile, cluster_review_overdue) | parses ToC rows, `^## NAME (N)$`, `**TOTAL**` | **no** | **yes** (sections move) |
| `PROME/tools/board_scan.py` (the §3.5 pull) | **never reads INDEX** — globs `BOARD/SIG-W-*.md` | no | no |
| CARL boot 5 | `grep -oE 'SIG-W-…'` over INDEX vs **`AGENTS/CARL/board/BOARD_LOG.tsv`**; mtime check | no | yes (grep path) |
| RED 1.5 (b1) | reads the cluster ToC (~6 KB) | no | no |
| REGINALD 9b | pull INDEX + SIG files since last ledger row (ID diff) | no | yes |
| FALCON / HAWK / OSPREY (b) | grep rows naming the desk on a word boundary | no | yes (glob) |
| WAL, OZK, MARCO, TERRY, DAEDALUS, AGENTS.md, ROSTER, SYSTEM | reference / pointer only | no | no |
| `staleness_sweep.py` | lexical read of the section preamble | no | no |
| `PROME/tools/reads_check.py` | names INDEX as the canonical "never read whole" example | no | no |
| Human drill ("scan the Cluster overview, then drill into your cluster") | reads ONE `## CLUSTER` section | **yes — this is the read that is 100–316 KB today** | yes |

**Nobody reads it whole.** The only whole-file consumers are greps. ⇒ The 1.6 MB is a cost to git, to audits, and to any session that Reads it by mistake (the boot-step-1 anchor class); the *human* cost is the cluster drill, and compaction fixes that without sharding.

## 3. Frontmatter contract (what the generator needs from each `SIG-W-*.md`)

| Field | Status | Fallback |
|---|---|---|
| `signal_id`, `date`, `cluster`, `precedence` | mandatory (FORMAT_SPEC) | filename for id; **fail closed** on the rest — name the file, exit 1 |
| `action:` / `info:` | v0.8+ | legacy `to:`/`info:` strings |
| `domain` | mandatory | — |
| `confidence` | mandatory | — |
| H1 title (`# …`, first) | body | `verdict:` first sentence, then filename slug |
| `status` + `status_ref` + `status_date` | v0.10, optional | absent → no lifecycle marker |
| `corrects:` on the CORRECTING signal | v0.13, optional | inverted by the generator → back-marker on every target row |
| 🆕 **`corrects_direction:`** on the correcting signal — `HOLDS` / `WEAKENS` / `FLIPS` + one line | **NEW, optional, FORMAT_SPEC v0.20 (landed 9/4 under WQ-174 ②)** | absent → marker reads "CORRECTED → `SIG-ID`" without a direction, flagged by the generator as `DIRECTION-MISSING` |

The **§3.6.2 direction rule** ("HOLDS / WEAKENS / FLIPS") currently lives only in prose banners; the new field gives it a machine home so the INDEX marker can carry it. **This is the one schema change and it is Will-gated** (structural: adds a field the generator reads).

## 4. Cutover — five steps, each with a check

1. **Obligation audit BEFORE (READ_CAP rule 18):** enumerate every INDEX row with a hand annotation that has no frontmatter source (§5 list of 10) and give each a `status:`/`status_ref:` header **first**. Until this is done the generator would DELETE them. The 39 `status:`-header rows with no marker gain one; the 7 remaining absent back-markers appear.
2. **Build `tools/gen_board_index.py`** — deterministic, writes a line-0 banner with the row-set sha (RED's `FALSIFICATION_TRIGGERS_SCAN.tsv` pattern), `--check` mode diffs the derived row set against the live file: ID set, per-cluster counts, marker presence per row. `--write` **would create** `BOARD/INDEX.generated.md` beside the live file. ⚠️ **That file does NOT exist and is not expected to: the soak has run `--check` only, which never writes.** It is the `--write` DEFAULT TARGET, not an artifact — do not read its absence as a missed step. *(Flagged as a dead pointer by PROME's `firetime_check` 2026-09-06; corrected here to describe the path rather than reference it, which is the honest fix — an allowlist entry would have suppressed a true reading.)*
3. **Parity test:** `walter_doctor.py` pointed at the generated file must reconcile (ToC = sections = files = TOTAL) and every ID present in the hand file must be present in the generated one; every marker in the hand file must be present or explicitly listed as "dropped: no source field" (should be zero after step 1).
4. **Swap** (one commit, WALTER-owned): generated file replaces INDEX.md; preamble shrinks to a pointer at BOARD_CONSUMPTION_SPEC §2 (the precedence→delivery table is a mirror and goes); the "Cluster activity detail (archived ToC changelog)" section moves to `design/history/`. Boot step 11 changes from "append a row + update the ToC" to "run the generator" — a WALTER `CLAUDE.md` edit, the old auto-load-cap claim was withdrawn on 9/6 (auto-loaded charters are exempt); keep the executable step concise.
5. **Doctor check `index_generated_fresh`:** regenerate to memory at every doctor run and fail HIGH on drift, so a hand edit to INDEX.md can never silently survive. Closeout gate unchanged otherwise.

**Exemption test after cutover:** unchanged. `board_scan.py` never touched INDEX; CARL's grep still finds every ID; RED's ToC read is the same ToC. The §3.5 warrant ("their own complete whole-INDEX BOARD-diff IS the pull") is about a step the recipient runs, not about the file's size.

## 5. The ten hand-annotated rows a regeneration would lose (rule 18 list — must get a header BEFORE step 2)

`SIG-W-20260627-017` · `SIG-W-20260706-008` · `SIG-W-20260716-004` (the known case: verdict lives ONLY as an INDEX annotation, flagged 8/18) · `SIG-W-20260724-006` · `SIG-W-20260725-002` · `SIG-W-20260727-001` · `SIG-W-20260727-013` · `SIG-W-20260727-016` · `SIG-W-20260727-018` · `SIG-W-20260728-006`.

**✅ HEADER PASS EXECUTED 2026-09-04 (WQ-174 step 1) — 7 headers written, 3 NO-HEADER with reasons:**

| Signal | Disposition |
|---|---|
| `-0706-008` | `PARTIALLY-CORRECTED` 2026-08-17 (PROME at primaries, four defects) **+ banner lifted verbatim from the INDEX row** — the body had no copy |
| `-0716-004` | `PARTIALLY-SUPERSEDED` 2026-07-24 (LIQUID KB-LIQ-087 via PROME) |
| `-0724-006` · `-0727-013` · `-0727-018` · `-0728-006` | `PARTIALLY-CORRECTED` 2026-07-27/28 — each body already carried its CORRECTION banner; only the header was missing |
| `-0727-016` | `PARTIALLY-SUPERSEDED` 2026-07-27 (PROME's narrower claim adopted, ADDENDUM in body) |
| `-0627-017` | **NO HEADER** — the row text is dispatch-time routing guidance ("route the decomposition, not the headline"), present in the body; not a lifecycle state |
| `-0725-002` | **NO HEADER** — regex false hit ("ACTIVELY FALSIFIED" is content about DQ data, not a lifecycle tag) |
| `-0727-001` | **NO HEADER** — the row says another signal's call is superseded; that status already sits on the target `SIG-W-20260725-008` (`status_ref: SIG-W-20260727-001`) |

**✅ SECOND PASS 2026-09-04, found by `gen_board_index.py --check` (the tool's own regex is wider than my audit's):** 5 more headers — `-0901-015` · `-0901-016` (same-session ERRATA, `PARTIALLY-CORRECTED`, ref SELF) · `-0819-014` · `-0819-016` (BRENT packets 8/20–8/21, `PARTIALLY-CORRECTED`) · `-0813-006` (self-correction ~40 min post-dispatch); and 4 more content false positives allow-listed IN THE TOOL with reasons (`-0727-014` · `-0730-008` · `-0815-001` · `-0815-006`). Also **5 legacy signals from the 8/3 sweep carried a non-spec `status_note:` field** (`-0702-002` · `-0723-003` · `-0725-006` · `-0727-019` · `-0728-007`) — text moved verbatim into a body banner, field removed.

**✅ STEP 2 BUILT 2026-09-04 — `tools/gen_board_index.py`:** `--check` PASS (881 IDs identical · per-cluster counts identical · **hand-only markers 0** · 66 derivable markers the live file LACKS would be GAINED) · `--write` → `BOARD/INDEX.generated.md` **452,007 B** (vs 1,628,719 B; the v0.1 estimate of ~309 KB omitted domain, info lists and markers) · doctor-style parity PASS (ToC = sections = rows = TOTAL = files, 12 clusters). **172 legacy signals have no H1**; their titles are seeded ONCE from the live index into `registry/INDEX_LEGACY_TITLES.tsv` (24,818 B, read by the generator, never extended by hand). `DIRECTION-MISSING` is flagged only on corrections dated ≥ 2026-09-04 (the field's ratification), so the 55 pre-field corrections print a plain `CORRECTED → SIG` marker.

⚠️ **Phase-2 flag, measured not estimated:** the compacted IRAN_HORMUZ section is **80,583 B** (CONSUMER_STAGFLATION 68 KB · BANK_COLLATERAL 60 KB) — a cluster drill into any of the top three still exceeds the 54,250 B physical cap. The per-cluster shard option in §6 is therefore not optional for those three; it is the next decision after the swap, not folded into it.

⇒ After these passes every lifecycle/correction marker on the INDEX has a frontmatter source, an inverted `corrects:`, or a named allow-list reason. The generator's `--check` re-derives this at every run and reports zero hand-only markers before the swap. ⚠️ Lesson re-bought during the pass: a `status_note:` field was written and stripped the same minute — it is not in FORMAT_SPEC (MEMORY 9/3 finding 5). The header pass uses exactly the three v0.10 fields.

## 6. Considered and rejected

- **Monthly shards** — readers are cluster-keyed; a month cut breaks every cluster drill and every grep into a glob; 13 boot surfaces change for a benefit only git sees.
- **Per-cluster shard files now** — same reader-change cost; keep as a **phase-2 option** if any compacted cluster section still exceeds the budget (IRAN will, at ~54 KB): the generator can emit `BOARD/index/<CLUSTER>.md` and keep the last 30 days in the root section. Separate decision.
- **Doing nothing about markers and only trimming bytes** — that is the "size remedy that leaves a boast behind" pattern; the marker drift is the defect that costs decisions.

## 7. Asks

- **Will:** approve (a) the generate-in-place direction, (b) the `corrects_direction:` field (FORMAT_SPEC v0.19), (c) WALTER building the generator this week with the step-1 header pass first. Nothing in the live INDEX changes until (c).
- **PROME:** the Codex "spec retains superseded wording inside the live rule" item is **NOT** riding this pass — it is a BOARD_CONSUMPTION_SPEC edit under rule 8 and gets its own packet.
- **Cost:** generator ~150 lines + one doctor check; header pass 10 rows; no spawn.

## 8. Implementation receipt — 2026-09-08

Pre-swap `--check` PASS at 891 IDs, zero hand-only markers. Executed `--write BOARD/INDEX.md --cutover`; this is the live output path. Historical ToC changelog moved byte-for-byte to `history/BOARD_INDEX_TOC_CHANGELOG_PRE_CUTOVER_2026-09-08.md`. Boot step 11 now runs the generator. Existing post-cutover doctor branch and behavioural tests verify actual rendered rows, not only the banner. Further dispatches regenerate this same index. No sharding or reader changes. Commit durability remains pending PROME serialization.
