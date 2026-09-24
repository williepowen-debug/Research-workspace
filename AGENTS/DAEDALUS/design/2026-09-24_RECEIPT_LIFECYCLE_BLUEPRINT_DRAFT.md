# Receipt lifecycle + binary sidecar: BLUEPRINT (DRAFT, not an encode)

**Status:** DRAFT by a DAEDALUS drafting subagent, 2026-09-24. DAEDALUS reviews and owns what ships. **Commission:** DOCKET L263 (row dated 2026-09-18, now **6 days past**), from WQ-171 ③. **Route:** DAEDALUS → PROME → Will. Nothing here is ruled.
**Ruled (verbatim, `PROME/proposals/2026-09-03_wq171-172-RULED.md`):** Will 2026-09-03 21:54 ET, *"Approve WQ-171 ① and ② and WQ-172 with your recs."* ① = Git Protocol 4d, subject ≤100 chars (`60994163d`). ② = KERNEL status surfaces records-derived (`04b761a86`). ③ = *"DAEDALUS blueprint, obligation-audited (READ_CAP rule 18), proposal back to Will, after `validate_all` types the ledgers; Codex's do-not list binds"*: **no history rewrite · no AGENTS reorg · no KERNEL expansion · no new validators before the ledgers are typed** (audit record `:30`). Codex also (`:79`): *"Do not add another state ledger … Consolidate the existing ones."*
**Precondition:** `validate_all.py` v1 landed `4dd2816b2` (9/10). Its header: *"types the three PROME decision ledgers"* (B1 DOCKET · B2 GATES · B3 WILL_QUEUE). ⚠️ **So the precondition is MET for PROME ledgers only.** No desk ledger is typed (`board_log`, `corrections_receipts`, `.consumed.tsv`). Anything added here must be born typed, as a validate_all leg.

| | |
|---|---|
| **What** | (i) A consumed per-recipient copy leaves HEAD once a **typed receipt row** exists AND the **rule-18 obligation audit** balances. The audit is done by the recipient at filing; the prune comes later and is mechanical. (ii) New source binaries stay out of the repo; a sidecar row (locator · sha256 · date · extracted-text path · extractor) goes in instead. |
| **Why** | 6,661 consumed copies = **39.6% of tracked paths**, 5.4% of bytes, ~99 landings a day, 0 deletions in 30 days. Binaries: **+97.8 MB in 30 days** (§1). |
| **Effort** | One validate_all leg + an extension to WALTER's §5.1 ledger (WALTER concurrence) + a binary check. About 1 DAEDALUS session + 1 WALTER touch. The backlog is the expensive part (⚖️ D3). |
| **Expected value** | Path count stops growing linearly. A filed ASK must say where its duty went, and today nobody checks that. `.git` stops gaining ~98 MB a month in new binaries. |
| **First step** | Will rules D1–D5. Then a DAEDALUS → WALTER packet with the column spec. |

## 0. Prior-art line (CHECK_STANDARD §13)

**Symptom searched:** "consumed copy kept forever" / "receipt says consumed, ask not done" / "binary in repo" / "processed/ prune". Searched `MEMORY.md` + `INDEX_COLD*.md` + `PATTERNS_HOT.md` + `PATTERNS.tsv`: bare rc=0, positive control 272 `finding_` hits. **Not novel. It is shaped around:** `finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit` · `finding_record_of_an_action_is_not_the_action` · `finding_live_claim_in_a_closed_container_is_invisible` · `finding_external_consumer_check_before_restructure` · `finding_grep_respects_gitignore_so_ignored_zones_are_invisible` · PAT-044 · PAT-102 · **PAT-154** (a guard reading `processed/` from the tree should read history; pruning forces that branch).

| Existing | Does | Why it is not this |
|---|---|---|
| `board_log.tsv` (WALTER §5; 32 files, 1,984,171 B) | Recipient row per consumed WALTER signal: `timestamp_read · signal_id · disposition · source · notes` | WALTER lane only (2,717/6,661). No commit, no result pointer, no obligation field. §1 defines *consumed* as **moved to `processed/`**, so pruning amends WALTER's definition. |
| `processed/.consumed.tsv` (§5.1 v0.19; **1 instance**, 108 lines) | Per-dir `consumed_date · file · consumer · note`. Separates FILED from CONSUMED; `walter_doctor filed_vs_consumed` reads it | Records *who* consumed, with no obligation or prune leg. **The closest form: §2 extends it rather than minting a ledger.** |
| `corrections_receipts.tsv` (25 desks) + `corrections_boot_check.py` | Receipt lifecycle for corrections, with a tested §9 rc contract | One class, keyed to WALTER's register. The model for the **checker contract**. |
| STATE_VOCABULARY Class 11 / Class 10 | Ladder `ROUTED→DELIVERED→CONSUMED→ENCODE-CONFIRMED→CLOSED-VERIFIED`, with *"nothing resolved below ENCODE-CONFIRMED"* / standing rows name artifact + expiry | Vocabulary, not a record. §3 mechanizes the Class 11 sentence; Class 10 is where re-homed duties land. |
| **2026-06-30** `2ce49f188` + `c819a955c` | PROME deleted **818 + 42** processed/delivered copies and kept the `.gitkeep`s: *"Per Will: keep the concept, periodically clear the churn. Recoverable from history."* | **Came before rule 18 (9/2)**: no audit, and one desk sweeping 30+ others' mail (§5.1's FILED≠CONSUMED case). Precedent for *pruning*, not for *how*. |
| `.gitignore` REGINALD/WAL/SHADE globs | PDFs local-only, extracted `.md` kept | A sidecar with no locator and no sha256: the other machine can't tell whether it has the file or whether its copy matches. |

## 1. Measurement (2026-09-24, every figure run by this drafter)

| Quantity | Value | Basis |
|---|---|---|
| Tracked paths | 16,826 | `git ls-files` |
| …in `inbox/**/processed/` | **6,661** (6,597 `.md`, 62 `.gitkeep`), **38** desks incl. PROME | regex over ls-files |
| …bytes | **25,356,411 B** = 5.4% of 473,377,324 B | `du -cb` over list |
| Largest | PROME 816 (5.08 MB) · HENRY 490 · LIQUID 384 · BRENT 369 · REGINALD 298 · WALTER 290 · DAEDALUS 271 | |
| Landings into inbox `processed/`, 30 d (08-25→09-24) | **2,963** (135 born there; rest rename-dest) · new inbox arrivals 2,916 | `git log -M --name-status` |
| Deleted from `processed/` | **0** in 30 d · 889 all-time, 860 of them on 2026-06-30 | `--diff-filter=D -M` |
| vs Codex 9/3 anchor | 5,061 → 6,661, about +1,600 in 21 d | cross-instrument, see R6 |
| Cited by path from live tracked files | **444** distinct (427 resolve), cited from 222 files. DOCKET 56 · GATES 8 · WILL_QUEUE 9 | `git grep`; control 2,396 files mention `processed/` |
| ASK-shaped copies | WALTER lane **1,133/2,695** · direct **2,741/3,902** (broad pattern) | heuristic, R1 |
| Sender `outbox/**/delivered/` | 305 files, 1,492,508 B | out of scope |
| Binaries on HEAD | PDF 72 / **186.1 MB** · DOCX 19 / 32.6 · XLSX 25 / 12.7 · XLS 8 / 9.0 · PNG 22 / 3.0 · JPG 10 / 0.8 · HTML 103 / 40.7 MB | |
| Binaries added 30 d | **171 files, 97,755,231 B** (86.1 MB non-HTML). SAM 87 · BRENT 51 · HAWK 12 · CARL 10 | current HEAD sizes |
| `.git` | 494 MB (Codex 9/3: ~378 MB) | `du -sh` |

**Headline:** consumed copies are a **path-count** problem: 40% of paths, 5% of bytes, nothing pruned since June. Binaries are the **byte** problem: one month of new non-HTML binaries = **3.4×** every consumed copy in the repo. Neither pruning shrinks the clone, because history keeps everything and rewriting it is forbidden. **(i) buys a leaner, greppable HEAD plus a forced obligation audit. (ii) stops future `.git` growth.**

## 2. Receipt row schema

**Where (rec, ⚖️ D1): extend `processed/.consumed.tsv`**, one per `processed/` dir. Reasons: Codex's "consolidate"; a reader following a dead cite lands in the directory holding its receipt; and `walter_doctor` already reads the file (§5.1 grammar (b)). The existing four columns stay first, so the 106 legacy rows still parse.

| # | Column | Type / rule |
|---|---|---|
| 1–4 | `consumed_date · file · consumer · note` | existing. `consumer` ≠ dir owner ⇒ FILED (§5.1) |
| 5 | `signal_id` | `SIG-W-…` or packet stem; joins `board_log`, `CORRECTIONS.tsv`, DOCKET |
| 6 | `received_commit` | sha that put the file at its **original inbox path** on origin. This is the retrieval handle. **Key = `file`+`received_commit`** |
| 7 | `state` | Class 11: `CONSUMED` \| `ENCODE-CONFIRMED` (never `CLOSED-VERIFIED`; that is the sender's rung) |
| 8 | `result` | `path[#anchor]` \| sha \| `NONE` (legal only if `asks_found`=0) |
| 9 | `asks_found` | int, ≥ the scanner's count unless col 4 says why |
| 10 | `asks_discharged` | int: done at `result`, or declined **by reply packet** (its path in `result`) |
| 11 | `obligations_rehomed` | `;`-list `path:anchor` (each a Class-10 row: artifact + expiry) \| `NONE` |
| 12 | `copy` | `HEAD` \| `PRUNED`, flipped **in the same commit as the `git rm`** |

**Balance (fail-closed):** `asks_found = asks_discharged + count(obligations_rehomed)`, or the row is not prune-eligible.

## 3. Rule-18 obligation audit: REQUIRED, done at FILING and not at prune

A copy in `processed/` is **already off every boot path** (rule 17's off-path branch). Any ASK still live inside it went invisible when it was filed (`finding_live_claim_in_a_closed_container_is_invisible`); pruning only removes its last greppable home. **So the audit runs in the filing commit, while the recipient still has the packet in context.** The receipt row IS the audit output: `asks_found` is rule 18's BEFORE list, and `discharged` + `rehomed` is the AFTER list.

- **Who:** the recipient, i.e. the `processed/` dir owner. Never the sender, PROME, or a sweep (§5.1's TERRY case: a WALTER session filed six TERRY items).
- **Instrument:** `--scan <file>` prints each ASK-pattern line with its line number; the recipient attests. **The scanner count is a FLOOR, not the truth.**
- **Fail-closed:** an unbalanced row ⇒ the copy stays on HEAD indefinitely. Scanner hits > `asks_found` with no reason ⇒ rc 1. An ASK-bearing copy may sit at `CONSUMED`, but **may not leave HEAD** until it is `ENCODE-CONFIRMED` or every ask is re-homed.
- **Re-home targets:** the desk's STATUS owed register, CALENDAR, a DOCKET/GATES row via PROME, or a reply packet. Each is a path the check resolves.

## 4. What leaves HEAD, when, by whom, and how to get it back

**Eligible when ALL hold:** a typed, balanced receipt · `consumed_date` ≥ **30 days** ago (⚖️ D2) · the receipt row already on origin · the path **cited by no live tracked file** (today this excludes 427, including every DOCKET/GATES/WQ artifact cell; `firetime_check.py:244` reads the processed twin's TEXT) · not the artifact of a pending dated event (Data Hygiene clause ①) · not a ruling record (e.g. the CHECK_STANDARD §8 cite).

**Who:** the recipient, under an **inverse of carve-out ①** (⚖️ D4): explicit-path `git rm` of copies in your own `processed/`, with subject token `prune:<AGENT>`, flipping col 12 in the same commit. Never `-r`, never a dir pathspec; `.gitkeep` stays.

**Retrieval (full clone only; see R3):**
```
git show <received_commit>:AGENTS/<X>/inbox/[WALTER/]<file>          # from the receipt, one step
git log --all --full-history --diff-filter=D --format='%h %ad %s' -- 'AGENTS/<X>/inbox/processed/<file>'
git show <prune_sha>^:AGENTS/<X>/inbox/processed/<file>              # from a dead cite
```

## 5. Binary sidecar (future intake only; nothing on HEAD moves)

`AGENTS/<X>/sources/SIDECARS.tsv`: `source_id · locator` (public URL or off-repo store key, ⚖️ D5) `· sha256` (exact retrieved bytes; either box verifies a re-fetch) `· bytes · retrieval_date` (UTC) `· extracted_text_path` (**must exist on HEAD**; what agents read) `· extractor` (tool==version) `· sensitivity` (`PUBLIC`\|`PRIVATE`; PRIVATE never goes to a shared store). The binary is `.gitignore`d by extension under `sources/`; the sidecar row is committed. On a serial two-box setup the sha256 is load-bearing: a gitignored file lives on one machine, and grep there skips it silently.

## 6. Enforcement sketch (spec only)

**validate_all leg B4** + owner modes in `scripts/handoff_receipt_check.py`: `--agent X` · `--scan <file>` · `--prune-plan X` (read-only; never runs `git rm`) · `--selftest`. §10: DAEDALUS's own 271 copies IN scope. §11 reader: the recipient at closeout + validate_all.

| rc (§9) | Meaning |
|---|---|
| **0** | Every copy past grace has a typed, balanced receipt. Every `PRUNED` file is absent on HEAD **and** resolvable via `received_commit`. Prints its perimeter (*"N dirs, M copies, K receipts read"*), never a bare "clean". |
| **1** | No receipt past grace · unbalanced · scanner > `asks_found` unexplained · **silent prune** (file gone, no `PRUNED` row) · `PRUNED` but still on HEAD · pruned path still cited live · `prune:<AGENT>` ≠ dir owner · new binary without a sidecar. Every instance printed, count first. |
| **2** | Header missing or unparseable · 0 rows from a non-empty file (§14) · git cannot answer history or origin (never read as absent) · unknown agent · shallow clone. |

**§3 plan:** a capable fixture (balanced, one un-rehomed ASK) must give rc 1; a clean fixture must give rc 0 with its perimeter; an empty ledger must give rc 2. **§9 consumer survey BEFORE build:** `walter_doctor` (twin logic ~L1146–1230 already accepts deletion when the original path reached origin) · `firetime_check.py` (handled by the cite exclusion) · `PROME/tools/{inbox_census,agent_freshness,fleet_dashboard,argus_scope,commit_check}.py`, `scripts/{consumer_check,ledger_staleness}.py` (all EXCLUDE `processed/`). Surveyed by grep only; R2.

## 7. Neighbours (WQ-229 five)

| Case | Behaviour |
|---|---|
| **Ordinary** | File + receipt in one commit → after 30 d, `--prune-plan` → recipient `git rm` + flip. |
| **Overlap: board_log** | A WALTER item gets a `board_log` row (unchanged) **and** a receipt, joined on `signal_id`. Different questions: *how I met it* vs *where its duty went*. Merging them is WALTER's call. |
| **Overlap: corrections** | `result` = the `corrections_receipts` line, so the duty is discharged by pointer and never duplicated. `DEFERRED`/`CONTESTED` ⇒ unbalanced ⇒ stays. |
| **Overlap: sender `delivered/`** | A second full copy (305). Out of scope; noted so that a pruned recipient copy is never read as "the only copy gone". |
| **Wrong owner** | `consumer` or `prune:` token ≠ dir owner ⇒ FILED / rc 1. PROME's 6/30 form is not repeatable here. |
| **Missing info** | Legacy 4-column rows, or no `received_commit` ⇒ never eligible, and not an error. |
| **Concurrent** | *Consumed on desktop, pruned on laptop:* eligibility needs the receipt **on origin**, and closeout pushes before a switch, so the laptop prunes only what the desktop published. *Two sessions on one box:* an explicit-path `git rm` meets another session's autostash rebase only through the dirty-path overlap check. *Re-delivery after prune:* a new key, so a new row. |

## 8. Risks

1. **CONSUMED over an undone ASK.** This is `finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit`: a `result` that resolves passes every presence check whether or not the work landed. The check proves the pointer resolves, **never that the ask was done. A balanced row is a declaration, not a verification**; only `ENCODE-CONFIRMED` or the sender's `CLOSED-VERIFIED` says more.
2. **The scanner floor becomes the ceiling.** Desks attest exactly the scanner count, and duties outside the pattern vanish at prune while the audit stays green (PAT-154).
3. **Burden gets gamed.** ~97 arrivals a day fleet-wide, so if the rows are costly, `asks_found=0` becomes the default answer. That is why D3 waits for a base rate.
4. **A cite added after the prune** hits a dead path. rc 1 flags it; nothing prevents it.
5. **WALTER's definition of *consumed*** changes without WALTER if D1 bypasses the concurrence.

## 9. Decisions for Will (⚖️, DAEDALUS rec first)

⚖️ **D1: Receipt home.** **Rec: extend `processed/.consumed.tsv`** (WALTER §5.1; concurrence packet first). Alt: a new per-desk `registry/handoff_receipts.tsv`, which would be a fourth receipt ledger and runs against "consolidate".

⚖️ **D2: Grace before a copy leaves HEAD.** **Rec: 30 days after `consumed_date`.** Alt: 60 days (the Data Hygiene clock).

⚖️ **D3: Backlog: 6,661 copies, ≈3,874 ASK-shaped by heuristic, none ever audited.** **Rec: forward-only for 60 days, then decide on the base rate** of forward receipts that needed a re-home (§12). Alt A: prune no-ASK backlog copies on scanner-zero plus a positive control (an absence claim over a heuristic). Alt B: repeat the 6/30 wholesale clear, which rule 18 now forbids without an audit.

⚖️ **D4: Root Git Protocol gains the carve-out ① inverse** (recipient `git rm`s its own processed copies, explicit path, `prune:<AGENT>`). **Rec: approve, forward-only.** Root text is Will-gated.

⚖️ **D5: Binary store.** **Rec: public URL + sha256 as the floor; one off-repo store for sources with no stable URL.** Which store (OneDrive / RESEARCH-INTAKE / other) is a spend choice and **yours** (PROME flagged it 9/3).

**The most important is D3:** it decides whether this is a small forward mechanism or a 6,661-file audit.

## 10. Declared residue

| # | Not verified | Consequence |
|---|---|---|
| R1 | ASK counts are grep heuristics. The direct-lane pattern over-counts, and both may miss duties. | Hand-audit a sample (~50) before any backlog number is used. |
| R2 | No consumer was *executed* against a pruned fixture. | Run the survey, don't read it, before build. |
| R3 | Whether both boxes hold full (non-shallow) clones. | Retrieval fails on a shallow clone; rc 2 detects it, doesn't fix it. |
| R4 | Whether any store (OneDrive…) is reachable from both boxes. | D5 is priced blind. |
| R5 | Whether WALTER accepts columns on §5.1. | D1's rec depends on it; the alt is ready. |
| R6 | Bytes = working-tree `du` over ls-files, not blob sizes. 30-d binary bytes use current sizes. 5,061→6,661 crosses instruments. | Magnitudes sound; exact figures indicative. |
| R7 | The 427 live-cited copies are not split by whether the citing doc is itself live. | The ineligible set may be smaller. |
