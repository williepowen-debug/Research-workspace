# NEXUS — Mode-A profile refresh, READER REPORT (2026-09-03)

**Reader:** DAEDALUS Mode-A subagent (read-only) · **Written:** 2026-09-03 ~21:15 ET (`date` = Thu Sep 3 21:14 EDT 2026) · **Tree state at read:** `git status --porcelain -- AGENTS/NEXUS/` = clean; HEAD `658e6cd3b` (local, DAEDALUS's own unpushed commit); `origin/master` = `c101dc953`; NEXUS's last commit `1c54b76e1` (9/3 20:06) **is on origin** (`git branch -r --contains 1c54b76e1` → `origin/master`).
**Subject vintage:** the existing profile `profiles/NEXUS.md` (body 8/17, STALE banner 9/1) was read first; its §1–§7 structure is followed below. FLEET_MAP row re-cut 2026-09-01 (L4 H, DEMOTED from L5) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md:30` + `_READER_REPORTS.md:21` read for the PR#5 findings.
**Method note:** every byte figure is `wc -c` on the working tree at read time; every crc32 below was RE-COMPUTED (`zlib.crc32`, read-only python one-liners) rather than trusted. No script that writes was run; `read_cap_check.py` was NOT executed — its perimeter logic was read (`scripts/read_cap_check.py:55-197`) and applied by hand.

---

## 0. Headline (what changed since the profile body and the 9/1 demotion)

| Fact | Evidence |
|---|---|
| NEXUS is **not dark** — two live sessions since the 9/1 demotion: 9/2 systems review (`58eca316c` 20:48, `35ebf7054` 20:57, `bb0c37591`, `e28f1170d`) and 9/3 dark-owner drain (`1c54b76e1` 20:06). | `git log --since=2026-08-17 -- AGENTS/NEXUS` (49 commits; 16 self-`NEXUS`-prefixed, 33 inbound) |
| **STATUS.md 32,508 B** — under the 32,550 B budget by **42 B** (99.9% of budget). Split landed 9/2 in `58eca316c` (46,471 → 32,526), re-cut 9/2 `35ebf7054` (→ 32,376) after PROME's obligation diff found two DELETED obligations, +132 B on 9/3. | `wc -c`; `git show 09994e545:…STATUS.md \| wc -c` = 46,471; `LAST_COMPLETION.md` receipts table |
| **PREDICTIONS_MONITOR.md 21,624 B** (66.4% of budget) — split 9/3 (`1c54b76e1`) from 59,146 B (source vintage `c2dbc635a`, crc32 3831447128 — **re-computed and matches**). Cold half `PREDICTIONS_COLD.md` 48,029 B, 12 blocks. | `wc -c`; `git show c2dbc635a:…PREDICTIONS_MONITOR.md \| python3 zlib.crc32` → bytes 59146 crc32 3831447128 |
| **All 25 crc32 stamps in both cold files VERIFIED** (13/13 `STATUS_COLD.md`, 12/12 `PREDICTIONS_COLD.md`) — the "verbatim" claim holds byte-for-byte. | §3a table below |
| **`Last full matrix review: 2026-09-02`** (`STATUS.md:4`) — after 8/28, as the re-promote condition requires. | quoted in §3c |
| **29-item obligation ledger** for the PREDICTIONS split exists as a file (`research/2026-09-03_predictions_monitor_split_obligation_ledger.md`, 8,746 B): 15 live re-homed HOT · 14 discharged · 0 deleted · 2 surfaced. The STATUS split's obligation diff (15 items) lives **only in commit message `35ebf7054`** — no NEXUS-side file. | §3b |
| My own independent trace of the pre-split STATUS obligations: **31 items traced; 3 dated catalysts from the pre-split docket's UNSWEPT row are found on NO NEXUS surface** (Iran waiver 8/21 · OPEX 8/21 · Affirm FQ4 ~8/25-28). | §3b table |
| 🔴 **`CONFIRMED.md:18` still reads "the POLICY-PATH LABEL is CONTESTED"** while `STATUS.md:31` (M-03) and `:152` say **"C-36 RULED 9/1, label SPLIT"** — a STATE change that did not reach the trophy-case surface; `CONFIRMED.md` last commit `cc36ea8c0` 2026-08-12. This is the exact defect the charter's own closeout 9b was written for (`CLAUDE.md:74-77`, which names C-36 as its founding case). | §6 D-1 |

---

## 1. FILE ANATOMY — measured 2026-09-03 (`wc -c` files, `du -sb` dirs)

### 1a. Top-level files

| File | Bytes | Lines | Last commit | What it is |
|---|---:|---:|---|---|
| `CLAUDE.md` | 52,632 | 343 | `1c54b76e1` 9/3 | Charter: IDENTITY · CONTRACT · BOOT 1–7a / LIVE-EVENT / EXECUTE 8–9 / CLOSEOUT 9–16 (with 9a/9b/9c) · 5 frameworks · Disciplines A–J · WHAT YOU READ/OWN · CROSS-AGENT SIGNALS · OUTPUT RULES · WHEN TO RUN · ANTI-PATTERNS. Auto-injected at launch, not a Read-tool read (161.7% of the read budget — see §1b note). |
| `STATUS.md` | **32,508** | 170 | `1c54b76e1` 9/3 | Hot board: header (Updated 9/3, Last full matrix review 9/2, READ-CAP CURED line, SLATE line) · prob split 20/47/33 · matrix M-01…M-11 (`:24-38`) · antecedent map R1–R11 (`:43-63`) · transmission chain (`:66-75`) · tensions T-01…T-24 (`:78-93`) · threshold proximity (`:96-127`) · catalyst docket (`:129-137`) · narrative gap (`:140-147`) · CONFIRMED pointer (`:150`) · BOTTOM LINE (`:156`) · LAST RUN (`:164`). |
| `STATUS_COLD.md` | 59,469 | 279 | `58eca316c` 9/2 | Cold companion of STATUS: §A–§G (8/17–8/28 vintage, 7 blocks, 17,924 B) + ADDENDUM §H1–§H6 (9/02 per-row evidence detail). Header `:3` says ON DEMAND, never at boot. |
| `PREDICTIONS_MONITOR.md` | **21,624** | 63 | `1c54b76e1` 9/3 | Hot ledger: purpose/restructure header (`:2-4`) · **LIVE OBLIGATIONS table L1–L7** (`:6-20`) · discipline rubric + status taxonomy (`:22-40`) · ACTIVE table 9 rows PRED-24/30/37/38/40/41/43/45/48 (`:45-57`) · COLD index (`:61`). |
| `PREDICTIONS_COLD.md` | 48,029 | 198 | `1c54b76e1` 9/3 | Cold companion: §P1/§P2 (pass-log preamble, orphan note) · §C1/§C2/§C3 (confirmed / resolved / past-trigger) · §G0–§G4 (7/10–7/31 gate adjudications) · §F falsified log · §E closed E-phase. 12 crc32 blocks. |
| `templates/NEXUS_BRIEF_SCHEMA.md` | 28,971 | 277 | `58eca316c` 9/2 | The fleet brief schema NEXUS owns (R3 + amendments 7, 9, 10, 11, **12**; **§4.6 AMENDMENT CAP 12 of 12** ratified 9/1). §6-7 split to `archive/` 8/28 (`:272`). |
| `templates/NEXUS_BRIEF_TEMPLATE.md` | 9,787 | — | `5e8b4617c` 6/7 | Rollout template. Unchanged since 6/7 — pre-dates amendments 9–12 (see §6 D-9). |
| `BRIEFS_MAP.md` | 29,595 | 87 | `f74f656fb` 8/28 | Fleet brief census/freshness index; consulted at BOOT 6. Header `:3` "Updated: 2026-08-07" while body carries a ★8/28 delta (§6 D-4). |
| `board_log.tsv` | 31,260 | 69 (68 rows) | `1c54b76e1` 9/3 | WALTER-lane + root-inbox consumption log (v0.2 header). Last 7 rows 9/3 in the 7/31 ISO-offset format. |
| `brief_fallback_log.tsv` | 7,181 | 47 | `de28799f7` 8/28 | Append-only brief→STATUS fallback instrumentation; last row 8/28 (BROCK, `stale`). |
| `brief_health.md` | 7,661 | — | `d6bcc4ec2` 8/28 | Rollup #4 home (closeout 9a alternate home) — carries the pin-coverage retraction. Rollup #5 owed (`STATUS.md:168`). |
| `SIGNALS.md` | 9,393 | 33 | `58eca316c` 9/2 | Live unresolved queue (S-26082801, S-26060701); forward-only. |
| `CONFIRMED.md` | 7,216 | 27 | `cc36ea8c0` **8/12** | Trophy case C-01…C-36. **Stale on C-36** (§6 D-1). |
| `LAST_COMPLETION.md` | 10,714 | — | `1c54b76e1` 9/3 | Session handoff (documented SCRATCH divergence). Carries the receipts table + 9c read-or-defer list + NEXT BOOT OWES (a)–(j). |
| `BRIEFING_2026-08-29_SYSTEMS_REVIEW.md` | 12,401 | — | `f7f5adc6a` 8/28 | Input pack for the 9/2 systems review — **consumed** (slate delivered 9/2); retirement-eligible after the WQ-163 items 3/4/⑤ ruling (~9/10). |

### 1b. Directories

| Dir | Bytes (`du -sb`) | Files | What it is |
|---|---:|---:|---|
| `inbox/` | 536,814 | 136 | **root: 1 file** (`2026-09-03_from-PROME_WQ-163-item6-RULED-your-C2-window-pin-STANDS.md`, 511 B, committed `40b48812a` 20:38 — arrived 32 min AFTER NEXUS's 20:06 closeout; not dwell debt) · `WALTER/` 57 files all in `WALTER/processed/` (root 0) · `processed/` 78 files. |
| `archive/` | 140,698 | 7 | 4 pre-June syntheses + `2026-05-21_revival_audit_draft.md` + 8/28 STATUS prose rotation (22,920 B) + 8/28 schema decision-log split (22,693 B). |
| `research/` | 120,079 | 11 | Pre-registrations + resolutions: 8/12 split falsifier RESOLUTION, 8/28 successor falsifier RESOLUTION, **9/2 T-12 admission-gate prereg**, **9/3 obligation ledger**. |
| `outbox/` | 53,859 | 11 | 1 root (`2026-09-02_to-PROME_self-audit-slate-drain-and-split.md`, 9,085 B) + `delivered/` 10 (last 7/22). Charter `:262`: legacy lane, empty-by-design since carve-out ①. |
| `proposals/` | 39,963 | 1 | `2026-09-02_self-audit-improvement-slate.md` — the DOCKET L206 slate (11 items; WQ-163). |
| `templates/` | 38,758 | 2 | (above) |
| `signals_archive/` | 32,048 | 7 | Consumed signals + the 7/10–7/16 gate block + the 6/27–7/24 pass log (both still referenced by `PREDICTIONS_COLD.md:92-97`). |
| `recon/` | 24,430 | 3 | 6/6 self-audit, C-ID index (still pointed to by `CONFIRMED.md:4`), E-phase prereg. |
| **Total `AGENTS/NEXUS`** | **1,316,332** | — | |

**Absent (searched):** `registry/` — `ls AGENTS/NEXUS/registry` → no such dir. `scripts/corrections_boot_check.py:171` (`new = not rcpt_path.exists()`) creates the receipts file on first receipt, so absence = no correction has ever named NEXUS; not a defect. `SCRATCH.md` absent by documented design (`CLAUDE.md:250`). `NEXUS_BRIEF.md` absent by design (NEXUS consumes briefs; `d6bcc4ec2` message).

### 1c. BOOT READS (from `CLAUDE.md` §BOOT `:30-49` + §WHAT YOU READ `:223-235`), sized against the 32,550 B budget

| Boot step | File | Verb in charter | Bytes | % of budget | read_cap_check counts it? | Grade |
|---|---|---|---:|---:|---|---|
| BOOT 1 (`:31`) | `STATUS.md` | "Read" | 32,508 | **99.9%** | yes (universal) | ✅ under budget · **🟡 ≥75% rotate tier** (24,412 B) · 42 B headroom |
| BOOT 2 (`:32`) | `CONFIRMED.md` | "Read" | 7,216 | 22.2% | yes | ✅ |
| BOOT 3 (`:33`) | `PREDICTIONS_MONITOR.md` | "read … in full (a WHOLE boot read — READ_CAP rule 16)" | 21,624 | 66.4% | yes (since 9/3 reword) | ✅ under the 70% rotate-to target |
| BOOT 5 (`:35`) | `SIGNALS.md` | "Read" | 9,393 | 28.9% | yes | ✅ |
| BOOT 6 (`:36`) | `BRIEFS_MAP.md` | "**Consult** … first — it is the authoritative, live index" | 29,595 | **90.9%** | **NO** — `consult` is not in `READ_VERB_RE` (`read_cap_check.py:62-64`) and IS in `SCOPE_MARKERS` (`:75`) | ✅ under budget but **🟡 rotate tier and INVISIBLE to the instrument** (§6 D-5, §8 Q2) |
| BOOT 6 (`:36`, "per `templates/NEXUS_BRIEF_SCHEMA.md` §4.4") | `NEXUS_BRIEF_SCHEMA.md` | section reference | 28,971 | 89.0% | yes (NEXUS receipt: "SCHEMA 53% of cap") — an over-count by the tool's own one-directional bias | ✅ under budget · 🟡 rotate tier |
| BOOT 4 (`:34`) | `inbox/` | "Scan" | dir | — | n/a | not a file |
| §WHAT YOU READ `:229` | `memory/auto/` (recent) | "Scan since last run" | dir | — | n/a | outside boot section |
| (auto-injected) | `CLAUDE.md` | harness load, not a Read | 52,632 | 161.7% | not the cap's object | ⚠️ see §8 Q3 |

**Instrument-scoped whole-read total (the 5 files NEXUS's own receipt names): 99,712 B.** +`BRIEFS_MAP` = 129,307 B. +charter = 181,939 B. **Not over budget on any single boot-mandated file; one file (STATUS) is 42 B from breach; two more (BRIEFS_MAP, SCHEMA) sit in the ≥75% rotate tier.** `STATUS_COLD.md` (59,469 B) and `PREDICTIONS_COLD.md` (48,029 B) are **not named as reads anywhere in the boot section** — `grep -n "STATUS_COLD\|PREDICTIONS_COLD" CLAUDE.md` → `:33` (says "never boot-read"), `:235`, `:249` (WHAT YOU READ/OWN, "on demand only"). Rule-17 off-path branch holds.

---

## 2. WHAT CHANGED since 2026-08-17 (`git log --since=2026-08-17 --format='%h %ad %s' --date=short -- AGENTS/NEXUS` → 49 commits, 76 files; 16 self / 33 inbound by subject prefix)

**New files that did not exist on 8/17** (`git diff --name-status --diff-filter=A 687b1dd74..HEAD -- AGENTS/NEXUS`, inbox excluded; 54 inbox adds separately):
`STATUS_COLD.md` · `PREDICTIONS_COLD.md` · `brief_health.md` · `BRIEFING_2026-08-29_SYSTEMS_REVIEW.md` · `archive/2026-08-28_STATUS_prose_rotation.md` · `archive/2026-08-28_BRIEF_SCHEMA_decision-log_and_review-history.md` · `proposals/2026-09-02_self-audit-improvement-slate.md` · `outbox/2026-09-02_to-PROME_self-audit-slate-drain-and-split.md` · `research/2026-08-28_successor_falsifier_RESOLUTION.md` · `research/2026-09-02_t12_respec_admission_gate_prereg.md` · `research/2026-09-03_predictions_monitor_split_obligation_ledger.md`. One rename: the 8/17 PROME commission packet → `inbox/processed/`.

**The 10 most structurally important changes:**

| # | Commit | Date | What |
|---|---|---|---|
| 1 | `1c54b76e1` | 9/3 | **PREDICTIONS_MONITOR hot/cold split + 29-item obligation ledger** (WQ-163 item 1 cure): 59,146 → 21,624 B hot; `PREDICTIONS_COLD.md` (12 crc32 blocks); LIVE OBLIGATIONS header L1–L7 invented as the hot file's obligation register; charter BOOT 3 verb reconciled to "whole read" (rule 16); `PREDICTIONS_COLD.md` added to §WHAT YOU OWN; ANALYSIS-vs-SIGNAL route clause added to §CROSS-AGENT SIGNALS; C#2 window PINNED 8/28→9/10 (L1a). |
| 2 | `58eca316c` | 9/2 | **STATUS hot/cold split #1** (46,471 → 32,526 B; 13 crc32 blocks → `STATUS_COLD.md`) + **full matrix review dated 9/02** + slate delivered (DOCKET L206, 11 items) + T-12 admission gate pre-registered at n=503 + amendment 12 encoded + **§4.6 amendment CAP** (schema stops at 12) + WQ-105 discharged. |
| 3 | `35ebf7054` | 9/2 | **Split re-cut after PROME's obligation diff**: two live obligations (gamma-flip refresh owed; OTTO 10-D panel legs owed to Will) had been DELETED from both files, one (RED FT-01 guard) pushed cold — all three restored HOT; STATUS → 32,376 B. Encodes the rule "a split is audited by OBLIGATION, not bytes" (now READ_CAP rule 18). |
| 4 | `d6bcc4ec2` | 8/28 | STATUS prose rotation 61,022 → 46,033 B (7 blocks, crc-stamped, → `archive/`); `brief_health.md` created with rollup #4 and the **pin-coverage RETRACTION** (rollups #1–#3's "zero brief-gap" claim withdrawn as evidence of health); 8/29 briefing pack written. |
| 5 | `895290f47` | 8/28 | **Schema hot/cold split** 42,103 → 22,909 B (§6–7 decision log + review history → `archive/`, crc32 3f13bf74); STATUS residual deliberately NOT improvised — escalated to the slate. |
| 6 | `f7f5adc6a` | 8/28 | Closeout stamp recording that the read-cap became ROOT CANON that day ⇒ STATUS 46,033 B is a **BREACH**, carried openly (the line PR#5 demoted on). |
| 7 | `fd7b82c8c` | 8/28 | **R1 corrections boot line inserted as step 7a** by NEXUS's own hand (DAEDALUS idle-target skip) — `CLAUDE.md:49`. |
| 8 | `de28799f7` / `09994e545` | 8/28 | Successor falsifier GRADED BRANCH C (NO-VERDICT, EARNED, FINAL) + closeout check battery recorded; `5447497cc` drained the WALTER lane (9 signals). |
| 9 | `c95a2c293` (PROME) · `213ef8963` (DAEDALUS) | 9/2 | The ruling chain NEXUS executed: DAEDALUS adjudicated PREDICTIONS_MONITOR a whole boot read (against its own 8/28 correction; READ_CAP rules 16/17); PROME packeted the Will ruling ("Approve 163 item 1 as adjudicated"). |
| 10 | `40b48812a` (PROME) | 9/3 20:38 | WQ-163 ⑥ RULED — **C#2 window pin STANDS** (Will "163 - yes"); packet in `inbox/` root, unprocessed (post-closeout). |

Not structural but load-bearing inbound: `cdbb04865` OTTO 26→30 panel supersession · `2ed23c7c0` CARL PREDICTIONS table moved to `PREDICTIONS_MIRROR.md` (NEXUS re-pointed 9/2) · `940a09c86` DAEDALUS PR#5 demotion packet · `0f0b44852` PROME WQ batch (WQ-105 amendment 12 + CAP).

---

## 3. THE RE-PROMOTE CONDITION, graded at the artifact

FLEET_MAP `Next_upgrade` (re-cut 9/1): *"RE-PROMOTE L5 when, in one session: read-cap breach CURED — 'cured' = the split LANDED AND the obligation ledger RE-HOMED (WQ-163 item 1 …) verified by DAEDALUS AT THE ARTIFACT, never by the byte count alone — + a full matrix review dated after 8/28. Then §7 AUTHORITY label → Conf H."*

### 3a. Leg (a) — split LANDED: STATUS.md under 32,550 B with a cold half whose header says what it holds and how it was split

| Check | Result | Evidence |
|---|---|---|
| `STATUS.md` < 32,550 B | **32,508 B — YES, by 42 B** | `wc -c AGENTS/NEXUS/STATUS.md` |
| `STATUS_COLD.md` exists | YES, 59,469 B, 279 lines, created `58eca316c` 9/2 | `wc -c`; `git log -- STATUS_COLD.md` (1 commit) |
| Header says what it holds | **`STATUS_COLD.md:3`:** *"**Created:** 2026-09-02 (read-cap hot/cold split) · **Owner:** NEXUS · **Read:** ON DEMAND, never at boot."* — `:5`: *"Everything below was moved out of `STATUS.md` **VERBATIM**, byte-for-byte, with a `crc32` per block, on 2026-09-02 to bring `STATUS.md` under the **32,550 B** read-cap budget …"* — `:7`: *"**What is here:** historical narrative whose live conclusions are carried forward in `STATUS.md`, plus per-pass methodology artifacts … and the NOT-CONFIRMING threshold rows … **What is NOT here:** any live convergence row, tension, breached/proximate threshold, forward docket row, the probability split, or the narrative gap — those stayed hot."* | quoted |
| crc per block, date, source-line addresses | Every §-block header carries `Moved verbatim 2026-09-02 · N B · crc32 xxxxxxxx` + the pre-split STATUS line range. **All 13 re-computed: VERIFIED** — §A 54cc553b/6,516 · §B 7a0670f1/1,464 · §C 965196cb/4,261 · §D 0011d5a2/1,013 · §E f26c61ee/1,197 · §F de547e70/1,942 · §G 9e3ab437/1,531 · §H1 a2b9b97a/13,193 · §H2 f27296d1/4,510 · §H3 8917fefc/2,614 · §H4 09c884bf/4,437 · §H5 6dec3689/7,403 · §H6 1f38b29a/4,951. | python `zlib.crc32` sliding-window match, this read |
| Hot side names the cold file at each split point | YES — `STATUS.md:20` (`📦 COLD → STATUS_COLD.md — §A-§G 8/28; §H1-§H6 = 9/02`), `:26` (§H1, 13,193 B, crc32 a2b9b97a — matches), `:45`, `:66`, `:78`, `:96`, `:126`, `:129`, `:140`, `:166` | `grep -n STATUS_COLD STATUS.md` |
| Same-commit measurement (rule 17) | `58eca316c` message states 46,471 → 32,526 B and `read_cap_check --agent NEXUS = READ-CAP 0`; `35ebf7054` states 32,376 B; 9/3 `LAST_COMPLETION.md` receipts table states 32,508 B with 42 B headroom. | commit messages |

**Leg (a) verdict: MET.** Caveat that DAEDALUS should carry: 32,508 B is **above the fleet's ≥75% rotate trigger** (24,412 B) and far above the <70% rotate-to target (22,785 B) named in `read_cap_check.py:49-50` and the DAEDALUS byte-tier convention; `read_cap_check` grades this 🟡 but returns rc=0. `LAST_COMPLETION.md` says it in NEXUS's own words: *"the next session that adds a cell must cut first."*

### 3b. Leg (b) — obligation ledger RE-HOMED

**(i) PREDICTIONS_MONITOR split (the WQ-163 item 1 object).** Ledger file: `research/2026-09-03_predictions_monitor_split_obligation_ledger.md` (8,746 B). Table §A enumerates **29 items O1–O29** with pre-split location, state re-checked 9/03, and new home. Tally (`ledger §A` last row): **15 live → HOT** (O1, O1a, O2, O3, O7–O10, O14, O15, O17, O19–O25) · **14 discharged with evidence named → COLD** · **0 deleted** · **2 SURFACED** (O1a: C#2 window start never pinned → pinned; O25: PRED-45 re-mark missed 9/02). Spot-verified at the artifact: L1–L7 present at `PREDICTIONS_MONITOR.md:8-20`; PRED-24/30/37/38/40/41/43/45/48 rows present at `:48-57` (9 ACTIVE rows; the header says 9); O16 orphan `PROME/PREDICTIONS_MONITOR.md` — I confirm absent (`ls PROME/` shows no such file); `PREDICTIONS_COLD.md:5` states "Zero live obligations were left in a cold block (verified by the ledger, not by bytes)". **Counts: 29 before / 29 accounted after / 0 not found.** ✅

**(ii) STATUS split (9/2).** No NEXUS-side ledger FILE exists — searched `grep -rln "obligation diff\|obligation ledger\|15 obligations" AGENTS/NEXUS/` → hits only in `STATUS.md` (the ⭐ line), `board_log.tsv`, and PROME's 9/2 packet; the 15-item list lives in commit message `35ebf7054` ("Remaining 12 of 15 obligations: hot, or discharged with the discharge visible on a boot-read surface"). PROME's packet (`inbox/processed/2026-09-02_from-PROME_WQ-163-item1-…md` §3) declares the STATUS cure *"verified genuine and discharged"*. So I ran my own trace: every obligation-bearing line in the pre-split STATUS (`git show 09994e545:AGENTS/NEXUS/STATUS.md`, 46,471 B — identical bytes to `58eca316c~1`) matched on owed/refresh/STALE/watch/due/backstop/re-mark/queued/pending/must/guard, then each item grepped in hot `STATUS.md`, `STATUS_COLD.md`, `PREDICTIONS_MONITOR.md`, `PREDICTIONS_COLD.md`:

| # | Pre-split obligation (line in 09994e545 STATUS) | Where it lives now | Verdict |
|---|---|---|---|
| 1 | Full matrix review owed at ≥8/29 (`:4`) | `STATUS.md:4` "Last full matrix review: 2026-09-02" | DISCHARGED, visible hot |
| 2 | QCEW attribution OPEN until NFP 9/4 (`:11`) | `STATUS.md:130-133` docket 9/4 NFP; `STATUS_COLD.md` §B | HOT |
| 3 | LAB-08 unresolved, FINAL Feb-2027 (`:11`) | `STATUS_COLD.md` §B only (2 hits); hot 0 | 🟡 COLD-ONLY — LABOR-owned dated resolver; not a NEXUS action |
| 4 | TRY-FIRE-004 25× TLT Sep-30 77P (`:15`) | `STATUS.md:14` | HOT |
| 5 | Sept-odds STALE 8/12, ORACLE dark (`:42`) | `STATUS.md:47` R1 "Sept-odds 0.31→0.48 [8/28]" | DISCHARGED by refresh |
| 6 | Kalshi downgrade board un-refreshed (`:42`) | `STATUS_COLD.md:46,208` (§C 8/17 detail, §H4 9/02 full T-23 text); hot T-23 `:90` carries "BOND OWNS IT" without the Kalshi board | 🟡 COLD-ONLY — BOND-owned (T-23 accepted 8/15) |
| 7 | China domestic demand watch, arbiter 8/31 PMI (`:51`) | `STATUS.md:59` R11 PROMOTED | DISCHARGED → promoted |
| 8 | CARL kill-rule → Will A/B/C ~9/30 (`:66`) | `STATUS.md:71` chain + `PREDICTIONS_MONITOR.md:13` L2 | HOT (two homes, consistent) |
| 9 | OTTO 8/17 10-D panel legs owed to Will BEFORE (`:66`) | `STATUS.md:71` "OWED TO WILL, restored 9/02 after my own split dropped it" | HOT (restored) |
| 10 | T-10 → 9/11 CPI (`:80`) | `STATUS.md:85` | HOT |
| 11 | T-20 PortWatch control ~8/20 (`:83`) | `STATUS.md:88` (re-spec 9/5-9/8) + `PREDICTIONS_MONITOR.md:14` L3 | HOT, superseded form |
| 12 | T-23 BOND owns, no threshold (`:86`) | `STATUS.md:90` | HOT |
| 13 | Gas $4.00 CARL V5 (`:100`) | `STATUS.md:105` `[STALE]` | HOT, stale-marked |
| 14 | Hormuz throughput — do not cite until control (`:101`) | `STATUS.md:107` POSITIVE-DETECTOR-ONLY | HOT, superseded form |
| 15 | Gamma flip — refresh owed by owner (`:102`) | `STATUS.md:108` `[STALE 8/6, 28 days]` "restored 9/02" | HOT (restored after PROME diff) |
| 16 | MIDAS WQ row 51 must be ruled before 8/28 (`:103`) | `STATUS.md:106` MIDAS-06 TERMINAL 8/31, verified Kernel 9/2 | DISCHARGED, visible hot |
| 17 | TTF >€50 `[STALE 7/31]` (`:104`) | `STATUS.md:110` | HOT, stale-marked |
| 18 | RED-FT-09 owner refresh due (`:111`) | `STATUS.md:117` `[STALE 21 sessions]` | HOT, stale-marked |
| 19 | BROCK HY<270 re-eval FIRED, owed to BROCK, packeted (`:112`) | hot 0 hits on "270"/"re-eval"; `STATUS_COLD.md:102` (§G 8/28 LAST RUN); BROCK's answer 8/28 in `inbox/processed/2026-08-28_from-BROCK_270-re-eval-RUN-…md` | 🟡 DISCHARGED, but the discharge is visible only in inbox/processed, not on a boot-read surface (the 35ebf7054 standard) |
| 20 | BOND T6 hard close 8/29 (`:113`) | `STATUS.md:118` GRADED NO-VERDICT 2026-08-30 | DISCHARGED, visible hot |
| 21 | Docket 8/18→8/27 "FIRED BUT UNSWEPT" (`:135`) — 10 named catalysts | `STATUS.md:131` replaced by "8/18→09-02 SWEPT AND CLOSED — 13 owner-graded outcomes consumed, each into its matrix row" (outcomes NOT enumerated) | see 21a–21j |
| 21a | 8/19 FOMC minutes (T7) | `STATUS.md:31` M-03 "8/19 minutes, 3 HIKE dissents, DGS2 moved ZERO" | HOT (relabelled) |
| 21b | 8/20 20Y JGB auction (T-24) | `STATUS.md:92` T-24 "8/20 20Y AMBIGUOUS ⇒ NO-VERDICT" | HOT |
| 21c | 8/20 PortWatch known-positive control | `STATUS.md:35,88` FAILED at both desks | HOT |
| 21d | 8/21 Jackson Hole | `STATUS.md:131` (date corrected: 8/27-29) | HOT |
| 21e | **8/21 Iran waiver** | **0 hits** in STATUS / STATUS_COLD / PREDICTIONS_MONITOR / PREDICTIONS_COLD | 🔴 **NOT FOUND** |
| 21f | **8/21 OPEX** | **0 hits** (all four surfaces) | 🔴 **NOT FOUND** |
| 21g | 8/24 OSPREY durability | `STATUS_COLD.md:48` (§C R9 8/17 detail) only; hot carries OSPREY Channel-3 `[STALE 8/15]` + "Owner dark since 8/20" (`:120`) | 🟡 stale-marked by proxy (owner dark) |
| 21h | ~8/25-28 GSE July monthlies | `STATUS_COLD.md:201` (§H4 T-15 full text "GSE-MF mod-suppression") only | 🟡 COLD-ONLY — HOMER/REGINALD-owned |
| 21i | **Affirm FQ4** | **0 hits** (all four surfaces) | 🔴 **NOT FOUND** |
| 21j | FAL-04 window close | `STATUS.md:124` NOT CONFIRMING "FAL-04 crude legs" | HOT |
| 22 | 9/11 non-renewable second evaluation (`:138`) | `STATUS.md:84,134` + `PREDICTIONS_MONITOR.md:8-9` L1/L1a | HOT |
| 23 | C-36 CONTESTED guard / C-35 grading caveat (`:162`) | `STATUS.md:152` (C-36 now "RULED 9/1 — SPLIT"; C-35 "do not grade on transit counts") | HOT — **but `CONFIRMED.md:18` not updated (§6 D-1)** |
| 24 | R9 Russia/Ukraine unswept (`:171`, implicit) | `STATUS.md:49` `[STALE 2026-08-17]` | HOT, stale-marked |
| 25 | RED FT-01 demotion guard (`:8` region) | `STATUS.md:109` "guard restored 9/02" | HOT (restored) |
| 26 | Fallback rollup #5 owed (`:181`) | `STATUS.md:168` "fallback rollup #5 not run" + `LAST_COMPLETION.md` (i) | HOT |
| 27 | STATUS 46,033 B BREACH carried openly (`:3`) | `STATUS.md:6` "READ-CAP CURED, both surfaces" | DISCHARGED |
| 28 | "harvest gate unchanged" (TRY-FIRE-004, `:15`) | 0 hits hot/cold; hot `:14` carries GATE-TERRY-ROLL70 FILLED 9/2 instead | 🟡 dropped — TERRY-owned; `LAST_COMPLETION.md` 9c defers TERRY STATUS |

**Counts (my trace): 31 obligation items traced (28 + the docket row's 10 sub-items counted as 3 found-hot + 7 listed) → found HOT or discharged-visible-hot: 23 · cold-only / by-proxy (owner-owned, not NEXUS actions): 6 (#3, #6, #19, #21g, #21h, #28) · NOT FOUND on any NEXUS surface: 3 (#21e Iran waiver, #21f OPEX, #21i Affirm FQ4).** The three not-found items are dated events inside a docket row the split REPLACED with a summary ("13 owner-graded outcomes consumed") rather than moving verbatim — the summary does not enumerate the 13, so whether these three were among them cannot be certified from NEXUS's files. They are owner-side events (FALCON/HAWK · HENRY · OTTO), not NEXUS-owed actions, which is why PROME's obligation diff (scoped to owed actions/watches) would not have caught them.

**Leg (b) verdict:** PREDICTIONS_MONITOR (the WQ-163 item 1 object) — **MET** (29/29 accounted, ledger in a file, 12/12 crc verified, zero live obligations cold). STATUS — **MET at the ruling's letter** (PROME discharged it 9/2; all NEXUS-OWED actions found hot) with **CANNOT-CERTIFY on 3 owner-side dated events** that have no trace on any NEXUS surface. Combined: **MET, with the three named residues carried as a packet to NEXUS** (not a re-grade trigger — they are not NEXUS-owed actions and the rule-18 class is "enumerate"; the fix is one enumerating line in `STATUS_COLD.md` §H or a "not swept" mark).

### 3c. Leg (c) — full matrix review dated after 8/28

**`STATUS.md:4`:** *"**Last full matrix review:** **2026-09-02.** ⚠️ **9/03 = drain + DELTA-ANNOTATION, NOT a re-sweep:** 17 owner surfaces committed after the 9/02 close (…) — read-or-defer list in `LAST_COMPLETION.md`; rows not annotated here inherit 9/02."* Corroborated: every matrix row `Last updated` is 9/02 or an honestly-held older date (M-01/M-04 2026-08-12, `:30,:33`); `58eca316c` message enumerates the per-row moves (M-03 −4, M-05 +3, M-06 −5, M-07 +3, M-09 +4, M-10 −2, M-11 +3). Also `PREDICTIONS_MONITOR.md:15` (L5) self-records that the 9/02 review **missed PRED-45's queued re-mark** — a scoped defect of the completeness claim, owed ≤9/11. **Verdict: MET** (9/02 > 8/28; the review is real, dated, and self-audited).

### 3d. WQ-163 open items (context, not a leg)
Items 3 · 4 · ⑤ with Will by 9/10 (`PROME/WILL_QUEUE.md:3,26`); item ⑥ (C#2 window pin) RULED 9/3 20:38 STANDS (`inbox/…item6…md`). The ~9/11 second-C grade + admission gate is the next dated NEXUS obligation (`PREDICTIONS_MONITOR.md:8-9`).

---

## 4. PREDICTIONS_MONITOR.md — the 9/2 "whole boot read" ruling

| Check | Result |
|---|---|
| Size / % of 32,550 B budget | **21,624 B = 66.4%** (below the 70% rotate-to target; 40% of the 54,250 B cap) |
| Charter verbs reconciled? | YES — `CLAUDE.md:33` "read `PREDICTIONS_MONITOR.md` in full (a WHOLE boot read — READ_CAP rule 16 …)"; `:235` "Whole read at boot (BOOT step 3; READ_CAP rule 16). `PREDICTIONS_COLD.md` on demand only." The 8/28 "scan"/"Full at boot" contradiction (`58eca316c` message) is gone. |
| `PREDICTIONS_COLD.md` exists | YES — 48,029 B, 198 lines, 12 § blocks, **12/12 crc32 re-computed and VERIFIED** (P1 89d58827/9,307 · P2 8642d034/449 · C1 9623b105/2,170 · C2 ac99a9b7/4,557 · C3 993e1b18/8,613 · G0 c836c9af/465 · G1 ca709389/3,128 · G2 a3d0c4a2/3,241 · G3 bdc1a8d6/4,421 · G4 f6a281e5/7,241 · F a20de91c/587 · E 25c97323/536) |
| Its header | **`PREDICTIONS_COLD.md:2-3`:** *"**Created:** 2026-09-03 (WQ-163 item 1 cure — `PREDICTIONS_MONITOR.md` hot/cold split) · **Owner:** NEXUS · **Read:** ON DEMAND, never at boot. ⛔ **THIS FILE IS NOT A BOOT READ.** … Everything below was moved out of it **VERBATIM**, byte-for-byte, with a `crc32` per block (zlib.crc32 over the block's UTF-8 bytes, no trailing newline), on 2026-09-03 … Source vintage = the file at commit `c2dbc635a` (59,146 B, whole-file crc32 3831447128 per `PROME/tools/measure.py`)."* — `:5`: *"**What is here:** resolved rows, closed archives, the stacked pass-log header, and the 7/10→7/31 cross-agent gate-adjudication record. **What is NOT here:** any live prediction row, any owed action or watch … **Zero live obligations were left in a cold block**."* |
| Source-vintage claim | **Re-computed: `git show c2dbc635a:…PREDICTIONS_MONITOR.md` = 59,146 B, crc32 3831447128 — matches.** (`c2dbc635a` is a WALTER commit of 9/3; the file was unchanged from `35ebf7054` to there.) |
| Hot file structure | LIVE OBLIGATIONS L1–L7 (`:6-20`) · rubric (`:22-40`) · ACTIVE 9 rows (`:45-57`) · COLD index (`:61-63`). `wc -l` = 63. |

**Verdict: under budget, ruling executed, cold companion crc-clean.** Residue: L5/L6 (PRED-45 + PRED-43 re-marks) are self-declared owed ≤9/11.

---

## 5. DO-NOT-TOUCH quirks — re-verified

| Profile §5 quirk (8/17 body) | Status today | Evidence |
|---|---|---|
| `LAST_COMPLETION.md` IS the session handoff, not `SCRATCH.md` — don't add a SCRATCH | **PRESENT** | `CLAUDE.md:250` ("Intentional divergence from fleet `SCRATCH.md` standard … do not re-flag"); `:94` closeout 15 writes it; boot reads it implicitly via `STATUS.md:165` pointer. `ls` → no SCRATCH.md. |
| Convergence matrix + PREDICTIONS_MONITOR are CORE OUTPUT — do not DARWIN-strip | **PRESENT** | `CLAUDE.md:22` CONTRACT PRODUCES; `BLUEPRINTS/utility-agent.md:5` names NEXUS utility. Unchanged. |
| `templates/` ownership by design; per-agent `NEXUS_BRIEF.md` are INPUTS | **PRESENT, strengthened** | `CLAUDE.md:20` (naming warning), `:255` (§WHAT YOU OWN); schema now carries **§4.6 AMENDMENT CAP** (`NEXUS_BRIEF_SCHEMA.md:1,218`): a 13th change = RE-SPEC SITTING, Will-gated. **New editor hazard:** any schema edit that adds an amendment breaches the cap. |
| `brief_fallback_log.tsv` cause-tagging — only `brief-gap` is a defect | **PRESENT** | `CLAUDE.md:43,70-74`. **Amended by `brief_health.md` rollup #4 (8/28):** every rollup must now report PIN COVERAGE + CLASS beside any brief-gap count; rollups #1–#3's "zero brief-gap" is RETRACTED as evidence of health. |
| `board_log.tsv` create-on-first-use; absence not a bug | **GONE as stated** (struck at PR#4) — file EXISTS, 68 rows, last 7 on 9/3; `CLAUDE.md:46-47` still carries the create-on-first-use clause as a fallback | `wc -l board_log.tsv` = 69; `tail -3` rows `2026-09-03T20:0x-04:00 … INBOX_ROOT`. **Note:** root-inbox items are ALSO logged here with `source=INBOX_ROOT` (rows at `:67-69`) — a convention extension beyond the v0.2 spec's `INBOX_WALTER`. |
| `BRIEFS_MAP.md` two-layer structure (top ★ delta supersedes per-agent table) | **PRESENT, now four layers** (★8/28 > ★8/7 > ★8/3 > ★7/31 deltas above a 6/16-vintage table) | `BRIEFS_MAP.md:3,6-12`. Any fix must reconcile all layers; see §6 D-4. |
| 7/3 DAEDALUS-applied handles (CONTRACT block, labeled BOTTOM LINE, boot-7 cwd-note) sourced from NEXUS's own content | **PRESENT** | `CLAUDE.md:18-24` CONTRACT; `STATUS.md:156` `## BOTTOM LINE`; `CLAUDE.md:45` cwd-proof note. Closeout-16 cwd verify now ALSO present (`:99`) — PR#5 marked RESOLVED. |

**New load-bearing quirks an editor could break (added this read):**

| Quirk | Where | Why load-bearing |
|---|---|---|
| **42 B of STATUS headroom.** Any addition to `STATUS.md` without a same-size cut breaches root canon. | `STATUS.md` = 32,508 B; `LAST_COMPLETION.md` "STATUS byte cost" para | The next writer (NEXUS itself, or a DAEDALUS/PROME edit) must cut first. |
| **crc32-stamped verbatim blocks in both cold files** — 25 blocks, each `crc32` over the block bytes with no trailing newline. Editing a cold block (even a typo) invalidates its stamp. | `STATUS_COLD.md` §A–§H6; `PREDICTIONS_COLD.md` §P1–§E | Verbatim-ness is the split's integrity proof; the fleet convention is rotation-never-editing. |
| **Hot/cold pointer pairs are bidirectional** — hot names cold section + byte count + crc at each split point (`STATUS.md:26` "§H1 (13,193 B, crc32 a2b9b97a)"); cold names the pre-split hot line range. | `STATUS.md:20,26,45,66,78,96,126,129,140,166` | A re-cut of a cold block must update the hot pointer's byte/crc figures. |
| **LIVE OBLIGATIONS table (L1–L7) = the obligation register of the hot ledger**; rule `PREDICTIONS_MONITOR.md:6` "each has ONE home" and `:4`/ledger O15: pass narratives go COLD at write time, never stack in the header. | `PREDICTIONS_MONITOR.md:6-20` | A closeout that writes a pass narrative into the header re-creates the 59 KB failure. |
| **C#2 evaluation window is PINNED and Will-ruled to STAND** — FRED daily cells 2026-08-28 → 2026-09-10 inclusive, grade at first boot on/after 9/11. | `PREDICTIONS_MONITOR.md:9` (L1a); `inbox/2026-09-03_from-PROME_WQ-163-item6…md` | Moving the window start after the ruling is a re-spec, not a pin. |
| **NON-RENEWABLE clause armed, C #1 of 2** — a second C forces the T-12 re-spec through the pre-registered ADMISSION GATE (`research/2026-09-02_t12_respec_admission_gate_prereg.md`: no spread-LEVEL spec admissible under 21 sessions). | `STATUS.md:14-18,84`; `PREDICTIONS_MONITOR.md:8` | The gate is frozen; do not "help" by proposing a level-based successor. |
| **Discipline I has no FIELD on STATUS** — the 9/2 Kharg own-goal (9 cells, 21 days) is recorded as a discipline that "runs only when remembered" (`58eca316c` message; slate item 5). | `CLAUDE.md:202-210` | An editor adding a state row without a lifted-check field re-creates it. |
| **Route rule: raw signals → WALTER's inbox, never direct** (ANALYSIS-vs-SIGNAL clause added 9/3). | `CLAUDE.md` §CROSS-AGENT SIGNALS (`:271-293`) | Routing around WALTER is a fleet violation (root CLAUDE.md Direct Messaging). |
| **Inbox root items are logged to `board_log.tsv` with `source=INBOX_ROOT` before `git mv`** (9/3 practice). | `board_log.tsv:67-69` | A drain that moves root items without a log row breaks the desk's consumption receipt. |
| **`BRIEFING_2026-08-29_SYSTEMS_REVIEW.md` is CONSUMED** (slate delivered 9/2) but still carries "READ THIS FIRST" in its title line. | `BRIEFING…md:1` | A fresh session could re-read it as live instruction. (§6 D-8) |

---

## 6. DEFECTS (flag, never fix)

| ID | Sev | File:line | Defect | Suggested fix |
|---|---|---|---|---|
| D-1 | 🔴 silent-failure | `CONFIRMED.md:18` | C-36 row says **"the POLICY-PATH LABEL is CONTESTED"** (7/31 vintage; file last committed `cc36ea8c0` 2026-08-12) while `STATUS.md:31` M-03 says "BOND → **C-36 RULED 9/1, label SPLIT**" and `STATUS.md:152` "C-36: OWNER-RULED 9/1 — the label is now a SPLIT; cite the split and the guard-rail verbatim." A STATE change (label) reached STATUS and not the trophy case — the exact case closeout **9b** (`CLAUDE.md:74-77`) was written for, and its worked example IS C-36. `LAST_COMPLETION.md` 9/3 says "CONFIRMED.md (no state change)" — true for 9/3, false for the 9/2 session that consumed the ruling. | NEXUS packet: update C-36 row to SPLIT with the 9/1 BOND ruling cite; re-run 9b from the CHANGE (58eca316c's M-03 edit), not from the files. |
| D-2 | 🟠 | `STATUS.md` (32,508 B) | **42 B headroom** — 99.9% of budget, above the ≥75% rotate trigger (`read_cap_check.py:49`, DAEDALUS byte-tier). rc=0 masks it (grade 🟡 prints, exit 0). The next cell forces a cut mid-session — the "correction pass is unreviewed work" failure the desk itself named 8/28. | Rotate to <70% (22,785 B) as a deliberate pass: candidates = NOT-CONFIRMING one-line index (`:124`), resolved docket row `:131`, CONFIRMED pointer `:150-152` (→ CONFIRMED.md), LAST RUN 9/02 block `:166-168` (→ LAST_COMPLETION). Or PROME/DAEDALUS rule that the 75% tier is advisory for boards. |
| D-3 | 🟠 | `STATUS.md:131` vs pre-split `:135` | The 8/18→8/27 "FIRED BUT UNSWEPT" docket row (10 named catalysts) was replaced by "SWEPT AND CLOSED — 13 owner-graded outcomes consumed" without enumerating the 13. Three of the ten named catalysts have **zero hits on any NEXUS surface**: Iran waiver 8/21 · OPEX 8/21 · Affirm FQ4 (`grep -c` = 0 in STATUS, STATUS_COLD, PREDICTIONS_MONITOR, PREDICTIONS_COLD). The original row text is in neither cold file (it was not one of the 13 crc blocks). | One line in `STATUS_COLD.md` §H (or `LAST_COMPLETION.md`) enumerating the 13 outcomes, and "NOT SWEPT" marks for any of the three not among them. |
| D-4 | 🟡 | `BRIEFS_MAP.md:3` | Header **"Updated: 2026-08-07 Fri"** while the body's top delta is ★8/28 and the last commit is `f74f656fb` 8/28 — a header older than its body (the inverse of the header-edit anti-pattern; a freshness scan keyed on the header reads it 21 days staler than it is). Also `:59`: "WATT / MIDAS / AEOLUS (+ VULCAN) run a compact variant" — VULCAN executed the revert to FULL variant 9/3 (`inbox/processed/2026-09-03_from-VULCAN_amendment-9-revert-EXECUTED…md`); `LAST_COMPLETION.md` already flags this as owed (j). | Bump `:3` to the ★8/28 date on the next touch; strike VULCAN from `:59`. |
| D-5 | 🟡 | `CLAUDE.md:36` / `read_cap_check.py:62-75` | `BRIEFS_MAP.md` (29,595 B, 90.9% of budget) is "Consult[ed] … first — the authoritative, live index" at BOOT 6, but the verb `consult` is not a read verb and IS a scope marker, so the file is **invisible to `read_cap_check`** — the same shape as the 8/28 PREDICTIONS_MONITOR under-count (a perimeter defined by a VERB). It is under budget today, so no breach; but it grows with every delta layer (four now) and nothing measures it. | NEXUS: say in `:36` whether BRIEFS_MAP is read whole (then it is a rule-16 whole read) or only its ★ top block (then say "top block only"). DAEDALUS: READS.tsv row. |
| D-6 | 🟡 | `STATUS_COLD.md:108` | Trailer *"End of cold companion. Total moved verbatim: 17,924 B across 7 blocks."* now sits mid-file above ADDENDUM §H (`:113`, six more blocks, 37,108 B). A reader stopping at "End of" misses §H1–§H6. | Move the trailer to EOF and restate the totals (13 blocks). |
| D-7 | 🟡 | `CLAUDE.md` (no §7) | **§7 AUTHORITY & SAFETY label absent** — `grep -n -i authority CLAUDE.md` → only `:49` (prose inside boot 7a). The blueprint (`utility-agent.md:35`) requires the section "only if it has cross-fleet write power … or state the read-only boundary explicitly." NEXUS DOES hold a cross-fleet write power: it owns the schema that governs 26 desks' briefs and rules on amendments (`:255`; schema §4.6 CAP; 8/28 ruling on VULCAN/HOMER at `NEXUS_BRIEF_SCHEMA.md:213`). The read-only boundary exists in prose (`:12` "You do NOT generate original research. You do NOT own any domain."; `:266-269`) but the schema-ruling authority and its guards (Will-gated at ≥13; amendments route through NEXUS) are scattered. This is the FLEET_MAP's named Conf-H gate. | One `## AUTHORITY & SAFETY` block: (i) read/synthesize-only on domain content; (ii) schema authority — what NEXUS may rule alone (defect repair, zero-text) vs Will-gated (amendments, cap); (iii) never edits another desk's brief. |
| D-8 | 🟡 | `BRIEFING_2026-08-29_SYSTEMS_REVIEW.md:1` | Title still "🔴 READ THIS FIRST" though the review it fed was delivered 9/2 (`proposals/…slate.md`). No banner marks it consumed. | Add a one-line CONSUMED banner pointing at the slate; retirement-eligible >60d per root Data Hygiene once WQ-163 3/4/⑤ close. |
| D-9 | 🟡 | `templates/NEXUS_BRIEF_TEMPLATE.md` | Last commit `5e8b4617c` 2026-06-07 — pre-dates amendments 9–12, including amendment 12's **section ORDER change** (CROSS-DOMAIN first, `NEXUS_BRIEF_SCHEMA.md:157`). The template a new desk copies still has the pre-12 order unless verified otherwise (I did not diff the template body against schema §2 — flag, not finding). | NEXUS: confirm the template's section order matches schema §2 post-amendment-12; if not, a zero-text re-order under the CAP's "defect repair" clause. |
| D-10 | 🟡 (correction to a DAEDALUS cell) | `FLEET_MAP.tsv` NEXUS Gaps cell | The cell says *"`## VIEW` body ~57 items with no numeric cap (NEXUS_BRIEF_SCHEMA.md:30/34 soft-trim only)."* The schema DOES state a numeric bound: `NEXUS_BRIEF_SCHEMA.md:65` "<3-5 bullets …>" and `:107` "3-5 bullets, declarative claims." The real gap is ENFORCEMENT — `:213` "THE 100-LINE CEILING IS ON THE WRONG AXIS AND IS NOT ENFORCED … a line/byte-axis re-spec is now RE-SPEC-SITTING work under §4.6." | Re-word the cell: "VIEW bound 3-5 bullets stated (:65/:107), unenforced; any enforcement = §4.6 re-spec sitting." |

Carried, not new (already self-recorded by NEXUS): PRED-45 + PRED-43 re-marks owed ≤9/11 (`PREDICTIONS_MONITOR.md:15-16`) · R9 owner sweep · fallback rollup #5 · 14 deferred owner surfaces (`LAST_COMPLETION.md` 9c list).

---

## 7. MATURITY READ — Utility class, per leg

| Leg | Requirement | Verdict | Evidence |
|---|---|---|---|
| L0 | Skeleton: dir + CLAUDE.md | **MET** | `AGENTS/NEXUS/CLAUDE.md` 343 lines, 52,632 B |
| L1 | STATUS + labeled BOTTOM LINE | **MET** | `STATUS.md:156` `## BOTTOM LINE` (3 paragraphs, dated 9/03 content); header `:3` Updated 2026-09-03 |
| L2 | Structured record accruing, valid schema | **MET** | `board_log.tsv` 68 rows, v0.2 header, last 7 rows 9/3 in the 7/31 ISO-offset format (`:67-69`); `brief_fallback_log.tsv` 47 lines, cause-tagged; `PREDICTIONS_MONITOR.md` ACTIVE 9 rows + L1–L7 + rubric; `PREDICTIONS_COLD.md` 12 crc blocks; `CONFIRMED.md` C-01…C-36 |
| L3 | Role rubric applied consistently | **MET** | Disciplines cited in live rows, not just documented: Disc-A `STATUS.md:33` (M-05 "threshold fired, mechanism did not — capped at ↑3"), Disc-H `:34` (M-07), `:113` (HY<260 four desks one line), Disc-J `:15` (split move written as evidence re-weigh), Disc-D `:144`, Disc-G `:85` (T-10 WALTER leg decomposed), Disc-F `:43` antecedent re-run; frameworks 1–5 each have a live section |
| L4 | Output consumed by others | **MET** | PROME consumed the 9/3 delivery (`PROME/inbox/processed/2026-09-03_from-NEXUS_drain-7of7…md`; `40b48812a` "Your 9/3 delivery (b9a214bba) consumed"); WQ-163 (`PROME/WILL_QUEUE.md:26`) is a Will-queue row built on NEXUS's slate; VULCAN executed NEXUS's amendment-9 revert release (`inbox/processed/2026-09-03_from-VULCAN_…EXECUTED…md`); RED answered slate item 4 on invitation (`inbox/processed/2026-09-02_from-RED_…slate-item-4-answered.md`); CARL re-pointed on NEXUS's read (`2ed23c7c0` "NEXUS + DAEDALUS riders discharged") |
| L5 | Clean closeouts · zero YEYOU flags (waivable) · CURRENT | **MET on currency and read-cap; ONE closeout defect open** | Current: STATUS 9/3 (`:3`), matrix review 9/2 (`:4`), 1-day gap; inbox root 0 dwell (the single item post-dates closeout); WALTER lane 0. Clean closeout 9/3: receipts table in `LAST_COMPLETION.md`, `1c54b76e1` on origin, tree clean, obligation ledger in a file, crc 25/25 verified. **Not clean:** D-1 — the 9/2 session moved C-36's STATE and did not propagate it to `CONFIRMED.md` (closeout 9b, `CLAUDE.md:74`). YEYOU: no feed exists (DAEDALUS charter box) — waivable. |

**Recommendation: RE-PROMOTE to L5, Conf M (not H).**
**The single deciding fact:** the re-promote condition as Will-ruled (WQ-163 item 1, 9/2 22:24) is **complete at the artifact** — both boot ledgers are under budget (32,508 B / 21,624 B), both splits are verbatim (25/25 crc32 re-computed), the obligation ledger for the ruled object exists as a file with 29/29 items accounted and 0 deleted, and the full matrix review is dated 9/02. Conf M rather than H because of D-1 (a 9b cross-surface STATE miss on the charter's own founding example) and the 42 B headroom (D-2) — both are single-session fixes, and together with the §7 AUTHORITY label (D-7) they are the Conf-H gate. **If DAEDALUS reads a 9b miss as disqualifying "clean closeouts," the alternative is HOLD L4 with D-1 as the named leg** — I do not recommend that: the miss is one row, two days old, on a file whose last consumer-facing change was a ruling NEXUS correctly carried on the board it owns; the ruled condition was the read-cap cure and it is cured.

---

## 8. OPEN QUESTIONS (phrased for DAEDALUS to ask the owner)

| # | Question | Ask whom |
|---|---|---|
| Q1 | The 8/18→8/27 docket row's 13 "owner-graded outcomes consumed" (`STATUS.md:131`) are not enumerated anywhere. Were Iran waiver (8/21), OPEX (8/21) and Affirm FQ4 among them, and if not, where is their "not swept" mark? (Zero hits on all four NEXUS surfaces.) | NEXUS |
| Q2 | Is `BRIEFS_MAP.md` (29,595 B, 90.9% of budget) read WHOLE at BOOT 6, or only its ★ top block? The charter says "Consult … first — the authoritative, live index" (`CLAUDE.md:36`); `read_cap_check` cannot see it under either reading. | NEXUS (perimeter) → DAEDALUS READS.tsv |
| Q3 | `CLAUDE.md` is 52,632 B (161.7% of the read budget) and grows ~1.7 KB per session (`LAST_COMPLETION.md` receipts: 50,948 → 52,632). It is auto-injected, not a Read-tool read — is the read cap's object the Read tool only, or does the boot-context total matter? (NEXUS itself raised "a per-surface budget with no total" in `35ebf7054`.) | DAEDALUS (READ_CAP canon) |
| Q4 | Does the ≥75% rotate tier (`read_cap_check.py:49`) BIND a hot board like `STATUS.md` (32,508 B = 99.9%) or is it advisory? `read_cap_check` prints 🟡 and exits 0; NEXUS treats budget-minus-1 as compliant. | DAEDALUS / PROME |
| Q5 | PROME's 9/2 obligation diff of the STATUS split (15 items, `35ebf7054`) — does a PROME-side artifact list the 15, or does the list exist only in the commit message? A ledger that lives in `git log` is not a file a boot reads. | PROME |
| Q6 | Is the C-36 SPLIT label's non-propagation to `CONFIRMED.md` (D-1) a 9b miss NEXUS will fix at its next boot, or does NEXUS read "cite the split and the guard-rail verbatim" (`STATUS.md:152`) as the trophy case's authoritative form? | NEXUS |
| Q7 | Does `NEXUS_BRIEF_TEMPLATE.md` (last commit 6/7) match schema §2's post-amendment-12 order? (Flagged, not diffed — D-9.) | NEXUS |
| Q8 | The §7 AUTHORITY block: does NEXUS agree its schema-ruling power (8/28 §4.5 ruling on VULCAN/HOMER; §4.6 CAP) is a cross-fleet write power that the blueprint's §7 exists for — or does it hold that every ruling is Will-gated via PROME and the block would restate that? | NEXUS → DAEDALUS |

---

*Read-only. Nothing in `AGENTS/NEXUS/` was touched. This file is the only write.*
