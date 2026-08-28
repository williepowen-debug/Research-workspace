# Leg ① — R1 corrections boot-leg wiring anchors — 14 desks (OZK RAV RED REGINALD SAM SHADE TERRY VIOLET VULCAN WAL WALTER WATT YEYOU ZHAO + PROME)

Read-only survey. No files edited outside this dir. Command template (from `AGENTS/DAEDALUS/CLAUDE.md` step 5b, adapted):
```
python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" <NAME>
```
rc=1 wording template: `(§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then --receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED> + commit your receipts file at AGENTS/<NAME>/registry/corrections_receipts.tsv)`

---

## OZK — `AGENTS/OZK/CLAUDE.md` (25,260 B)
1. **Boot location:** `### Boot (read phase — order matters)` L39. Numbering: `0.`–`7.` flat.
2. **Existing shared-script step:** none of the grepped scripts found (no `ledger_staleness`/`orphan_check`/`consumer_check`/`claim_check` invocation in this file). L36 has `rev-parse --show-toplevel` only for git-discipline prose.
3. **Insertion:** after L52 (verbatim, occurs once):
   `7. **(Situational, not routine)** Read `../REGINALD/MEMORY.md` only when a task specifically requires shared Will feedback that isn't already duplicated into OZK/MEMORY.md. Routine boot is local-only.`
   New step **`7a.`**, before blank L53 / `### Execute` (L54). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" OZK (§9 rc 0/1/2; rc=1 → --receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>, commit AGENTS/OZK/registry/corrections_receipts.tsv).`
4. **boot.py:** yes (`scripts/boot.py`, step 5, L48), one instrument among prose steps, not "the boot" — CLAUDE.md's own numbered list governs; a session following the file would run the R1 line as written.
5. **registry/:** does not exist (`AGENTS/OZK/registry/` — not found).
6. **Size:** 25,260 B — under flag.
7. **Card:** YES — `⚡ SPAWNED-MODE boot card` L30–37 lists boot commands (git discipline, deliver-before-idle) but no per-line script inventory beyond git; card doesn't enumerate individual check scripts today, so adding R1 there is optional, not required for parity — **NO** (card doesn't itemize other checks either; adding would be inconsistent with its current scope).
8. n/a (not special-class).

## RAV — no `CLAUDE.md`
1–7: **N/A — RAV has no `AGENTS/RAV/CLAUDE.md`.** Confirmed via `find AGENTS/RAV -type f`: only `README.md`, `inbox/`, `outbox/`, `runs/`. Its own README L3: *"RAV does not boot from this directory. RAV runs on Codex, Will-driven, on-demand — it is not a Claude Code session, so it loads no CLAUDE.md."* The `corrections_boot_check.py` mechanism is wired via CLAUDE.md boot-sequence text — **there is no file to anchor an insertion in.**
8. **Special-class:** RAV is the Codex/Will-driven deep-review reviewer. R1 applicability **UNCLEAR/likely-NO by construction** — it has no boot sequence file the fleet convention attaches to; any R1 leg would have to be handed to it at spawn time (per its own README: "must be handed its context at spawn"), a different mechanism than every other desk's boot-time script call. **No safe anchor exists.**

## RED — `AGENTS/RED/CLAUDE.md` (40,560 B) — ⚠️ LIVE SESSION RIGHT NOW
1. **Boot location:** `## SPAWN PROTOCOL` L32 (prose) → `### BOOT (read phase)` L36. Numbering: `0.`–`9d.` decimal-letter, non-sequential order in file (9b appears before 9a).
2. **Existing shared-script step:** L70 `9a. **Ledger staleness check** — run \`python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" RED --quiet\`; ...`
3. **Insertion:** after L72 (verbatim, occurs once — confirmed via distinguishing suffix "an ungraded resolved fire is the CHG-051 defect regrowing."):
   `9d. **Base-rate review (selectivity-drift check) — added S36d 2026-08-27, CHG-051 deliverable 1:** ... **At W2, also disposition any TRIGGER_OUTCOMES row whose \`resolve_after\` has passed** — an ungraded resolved fire is the CHG-051 defect regrowing.`
   New step **`9e.`**, before blank L73 / `### EXECUTE` (L74). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" RED (§9 rc 0/1/2; rc=1 → --receipt ... , commit AGENTS/RED/registry/corrections_receipts.tsv).`
4. **boot.py:** yes (`AGENTS/RED/scripts/boot.py`, L66, invoked as step 9), one instrument among many prose steps — not sole "the boot"; a protocol-following session would still hit the new CLAUDE.md line.
5. **registry/:** EXISTS — `AGENTS/RED/registry/` holds `FALSIFICATION_TRIGGERS.tsv`, `OUTCOME_SPEC.tsv`. No `corrections_receipts.tsv` yet.
6. **Size:** 40,560 B — **flag (≥32,550 B).**
7. **Card:** NO — no `SPAWNED-MODE` boot card found in this file (headings found: `SPAWN PROTOCOL`, `Core Files`, `Reference/archive`).
8. **Special-class:** RED is a LIVE session right now per the task brief. **Do not edit** — DAEDALUS should packet RED rather than apply this insertion directly. RED's own charter is silent on whether it consumes fleet corrections, but nothing exempts it — ordinary active desk, applicable **YES** once packeted.

## REGINALD — `AGENTS/REGINALD/CLAUDE.md` (34,819 B)
1. **Boot location:** `## SPAWN PROTOCOL` L32 → `### Boot (read phase — this order matters)` L34. Numbering: `0.`–`9b.` flat with letter suffixes.
2. **Existing shared-script step:** L43 `7a. **Ledger staleness check** — run \`python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" REGINALD --quiet\`; ...`
3. **Insertion:** boot continues past 7a through `7b` (L44), WALTER-intake steps, `8.` (L50), `9.` (L51), `9b.` (L52–56) before `### Execute` (L58, `10. Execute the task`). Per the "last boot step before execute" fallback (7a is NOT the last boot step here — 9b is), insert after L56 (verbatim, occurs once — the closing sentence of 9b's bullet list):
   `- **Append disposition row** to \`board/BOARD_LOG.tsv\` (11-col schema: BOARD_ID / Date / Cluster / Verdict / Disposition / Post_Hoc_Conf / Vector_Update / Cross_Links / Channels_Touched / Bank_Tickers / Notes) for each signal read. Disposition values: INTEGRATED / INFO_ONLY / REFERRED / WOULD-INTEGRATE / BACKFILL.`
   New step **`9c.`**, before blank L57 / `### Execute` (L58). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" REGINALD (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/REGINALD/registry/corrections_receipts.tsv).`
4. **boot.py:** yes, but OPTIONAL (`7b. (Optional) Fuller monitoring sweep`, L44) — REGINALD's CLAUDE.md prose is the actual "boot," boot.py is a supplementary sweep skippable on a quick tape-check. A session following only the CLAUDE.md text (skipping optional boot.py) would still execute the new R1 line since it's proposed as a mandatory numbered prose step.
5. **registry/:** does not exist.
6. **Size:** 34,819 B — **flag (≥32,550 B).**
7. **Card:** YES — `⚡ SPAWNED-MODE BOOT CARD` L8–17. Command lines quoted: `1. Read first (cwd-inherited spawn): AGENTS/REGINALD/CLAUDE.md → STATUS.md → scan inbox/ and inbox/WALTER/` / `3. Prices live only via (cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/market.py)` / `4. Git: ...`. **Should R1 be named there too? YES** — the card is the only thing read on a cold coordinator spawn (per its own preamble, this file does NOT auto-load); if R1 coverage is meant to hold even in spawned mode, the card needs its own one-line pointer, since spawned instances don't otherwise reach step 9c.
8. n/a.

## SAM — `AGENTS/SAM/CLAUDE.md` (32,853 B)
1. **Boot location:** `## SPAWN PROTOCOL` L18 → `### Boot (read phase — this order matters)` L20. Numbering: `0.`–`7.` flat, then unnumbered `### WALTER signal intake` subsection (L51+).
2. **Existing shared-script step:** NONE of the grepped scripts (`ledger_staleness`/`orphan_check`/`consumer_check`/`claim_check`) appear in SAM's CLAUDE.md at all — only `rev-parse --show-toplevel` wraps for `boot.py`/`fetch.py`/BOJ tooling.
3. **Insertion:** boot's last numbered step is `7. **Market refresh**` (L28) which spans through L49 (manual-fallback bullets embedded in the same numbered item), followed by the unnumbered `### WALTER signal intake` subsection starting L51 (which itself is boot-phase, not Execute — no `### Execute` heading was found in the read window; SAM's Execute is implicit). Safest anchor: after the WALTER-intake subsection's last consume line — **not fully captured in this read pass (subsection continues past L60); recommend DAEDALUS re-open `AGENTS/SAM/CLAUDE.md` L51–~75 before finalizing** the exact tail line. Provisional insertion: immediately after L28's step 7 block (before `### WALTER signal intake` heading at L51), as new step **`7a.`**. Anchor verbatim (occurs once, confirmed): the `--tools` line block starting L36–40 is safer/more unique than the long step-7 body; recommend anchoring on L49 last bullet: `- **News/narrative:** WebSearch (always cross-check ETF prices vs underlying FX).` (uniqueness not yet grep-confirmed in this pass — **flag for re-verification**).
4. **boot.py:** yes (`AGENTS/SAM/scripts/boot.py`, L32, "Preferred (one command, ~15s)"), one instrument among prose steps — CLAUDE.md prose is the boot; a protocol-following session hits the new line regardless.
5. **registry/:** does not exist.
6. **Size:** 32,853 B — **flag (≥32,550 B, barely — 303 B over).**
7. **Card:** NO — no SPAWNED-MODE card found.
8. n/a. **⚠️ Confidence flag: SAM's exact tail-of-boot line needs a second read pass (L51–~90) before an Edit is applied — I did not fully map the WALTER-intake subsection's end or confirm where Execute begins.**

## SHADE — `AGENTS/SHADE/CLAUDE.md` (13,071 B)
1. **Boot location:** `## SPAWN PROTOCOL` L71 → `### Boot (read phase)` L77. Numbering: `1.`–`4a.` flat.
2. **Existing shared-script step:** NONE of the grepped scripts appear anywhere in this file (confirmed — grep returned zero hits for all five patterns).
3. **Insertion:** after L90 (verbatim, occurs once — confirmed `grep -c` = 1):
   `   - Let \`acted\` items inform this session. Do not use bash \`mv\`; use \`git mv\` so the consume move is staged correctly. Spec: \`AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md\` v0.2.`
   New step **`4b.`**, before blank L91 / `### Execute` (L92). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" SHADE (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/SHADE/registry/corrections_receipts.tsv).`
4. **boot.py:** NO — SHADE has no `boot.py` reference anywhere in the grepped scripts; boot is pure prose reads. A protocol-following session unambiguously hits the new CLAUDE.md line.
5. **registry/:** does not exist.
6. **Size:** 13,071 B — under flag.
7. **Card:** NO — no SPAWNED-MODE card (SHADE's `## SPAWN PROTOCOL` at L71 is prose-only, no card block).
8. n/a.

## TERRY — `AGENTS/TERRY/CLAUDE.md` (28,697 B)
1. **Boot location:** `## BOOT` (all-caps, single `#`-level under CONTRACT/IDENTITY sections) at L137. Numbering: `0.`–`13.` flat, decimal sub-steps (5b).
2. **Existing shared-script step:** NONE of the five grepped patterns appear — TERRY's staleness-adjacent tooling is bespoke (`ledger_sweep.py` at WRITE-BACK step 0, L174) — not `scripts/ledger_staleness.py`.
3. **Insertion:** after L160 (verbatim, occurs once):
   `13. For pasted/exported option chains, use \`(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/chain_parse.py …)\`; if no chain is available, mark option-specific terms as conditional and name the chain fields Will must verify.`
   New step **`14.`**, before blank L161 / `### Standing context — two things that are true every session` (L162). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" TERRY (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/TERRY/registry/corrections_receipts.tsv).`
4. **boot.py:** yes (`AGENTS/TERRY/scripts/boot.py`, step 5, L147), one instrument among prose steps (`--snapshot` flag noted) — CLAUDE.md's numbered prose is the governing boot; new line would run.
5. **registry/:** does not exist (TERRY's ledgers live in `workbook/` at top level per its FILES table, not `registry/`).
6. **Size:** 28,697 B — under flag.
7. **Card:** NO — no SPAWNED-MODE card found; TERRY's boot opens with step `0.` "If opened directly in Claude Code, first orient as TERRY."
8. n/a.

## VIOLET — `AGENTS/VIOLET/CLAUDE.md` (24,518 B)
1. **Boot location:** `## SPAWN PROTOCOL` L16 → `### BOOT (read phase)` L20. Numbering: `0.`–`5b.` flat with letter suffixes.
2. **Existing shared-script step:** L33–34 `5b. **Staleness guard** ... python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" VIOLET --quiet` and `... VIOLET --trade --quiet` (two-line block).
3. **Insertion:** boot's last step is `5a. WALTER signal intake` (L36–39), immediately before `### EXECUTE` (L41). Insert after L39 (verbatim, occurs once):
   `   - Let \`acted\` items inform this session. Do not use bash \`mv\`; use \`git mv\` so the consume move is staged correctly. Spec: \`AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md\` v0.2.`
   New step **`5c.`**, before blank L40 / `### EXECUTE` (L41). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" VIOLET (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/VIOLET/registry/corrections_receipts.tsv).`
   Note: VIOLET's step numbering already runs 5, 5b, 5a out of textual order (5b precedes 5a in the file) — a quirk pre-existing this proposal, not introduced by it.
4. **boot.py:** yes (`AGENTS/VIOLET/scripts/boot.py`, L28), one instrument among prose steps.
5. **registry/:** does not exist.
6. **Size:** 24,518 B — under flag.
7. **Card:** NO — no SPAWNED-MODE card found.
8. n/a.

## VULCAN — `AGENTS/VULCAN/CLAUDE.md` (55,864 B)
1. **Boot location:** No separate `SPAWN PROTOCOL` heading — `## ⚡ SPAWNED-MODE BOOT CARD` L13 doubles as the entry point, then `## BOOT SEQUENCE (when spawned)` L39. Numbering: `1.`–`9.` flat.
2. **Existing shared-script step:** boot.py itself is described as running "ledger staleness" as leg 1 of 8 (L44), but there is no separate bare `scripts/ledger_staleness.py` CLAUDE.md invocation outside `boot.py` — the check is embedded, not a standalone grep hit for the four patterns (only `rev-parse --show-toplevel` wraps for `boot.py` itself, L16/18/41/44).
3. **Insertion:** last boot step before `9. Execute the task.` (L49) is `8. **Channel-liveness check**` (L48, confirmed unique verbatim via grep -c=1 on the full markdown-bold line). Insert new step **`8b.`** after L48, before L49:
   `8. **Channel-liveness check** — for each of **S1–S5** *(S5 has been core since 2026-08-03; this step said S1–S4 for 18 days — caught by step 4b's own Q① on 8/21)*, is there a *current, dated* live read? Any channel without one is a **gap to close this session** (the #1 guard).`
   Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" VULCAN (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/VULCAN/registry/corrections_receipts.tsv).`
4. **boot.py:** yes, and unusually IS effectively "the boot" — 8 legs cover most mechanical checks, called once at step 4 (L44); remaining steps (5–8) are prose reactions to its output. A cold spawn following only the SPAWNED-MODE card (L13–20) would run `boot.py` but the card text does NOT itself list step 8's new R1 line — see item 7.
5. **registry/:** does not exist.
6. **Size:** 55,864 B — **flag (≥32,550 B), second-largest of the 13 desks after WALTER.**
7. **Card:** YES — `⚡ SPAWNED-MODE BOOT CARD` L13–21. Command lines quoted: `Run python3 "$(git rev-parse --show-toplevel)/AGENTS/VULCAN/boot.py" — 8 legs (...)` (L16) and git-discipline / deliver-before-idle lines (L18–19). **Should R1 be named there too? YES** — this card is explicitly what a coordinator-spawned instance reads instead of the full file (per its own header), and it does not currently mention any check outside `boot.py`'s own legs; an R1 line here is the only way a spawned VULCAN instance would ever see it, since spawned instances by definition skip the full BOOT SEQUENCE section below.
8. n/a.

## WAL — `AGENTS/WAL/CLAUDE.md` (18,647 B)
1. **Boot location:** `## SPAWN PROTOCOL` L28 → `### ⚡ SPAWNED-MODE boot card` L30 → `### Boot (read phase — order matters)` L40. Numbering: `0.`–`8.` flat with letter suffixes (4b, 4c).
2. **Existing shared-script step:** L49–50 `4. **Staleness check** ... scripts/ledger_staleness.py WAL --quiet` / `... WAL --trade --quiet`.
3. **Insertion:** boot continues past step 4 through `4b.` (KB expiry, L52–56), `4c.` (derived-drift, L57–61), `5.` (live price, L62), `6.` (inbox awareness, L63), `7.` (REGINALD_CHANNEL scan, L64), before `### Execute` (L66, step `8.`). Insert new step **`7a.`** after L64 (verbatim, occurs once):
   `7. **\`REGINALD_CHANNEL.md\`** — scan top for new REGINALD entries since last boot; ACK what you integrate.`
   Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" WAL (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/WAL/registry/corrections_receipts.tsv).`
4. **boot.py:** explicitly **NO** — L62 states "*(No boot.py yet — deliberately instrument-light at standup (PAT-048)...)*" — WAL's CLAUDE.md prose IS the entire boot; the new R1 line would unambiguously execute for any protocol-following session.
5. **registry/:** does not exist.
6. **Size:** 18,647 B — under flag.
7. **Card:** YES — `### ⚡ SPAWNED-MODE boot card` L30–38. Command lines: git-discipline, deliver-before-idle, 2-sec drift check (no script invocations quoted in the card itself — it's read-order + semantics, not a check inventory). **Should R1 be named there? NO** — consistent with the card's existing scope (it doesn't itemize `ledger_staleness`/`kb_expiry_check`/`derived_drift_check` either, despite those being real boot steps) — adding R1 alone would be inconsistent; if DAEDALUS wants parity, it should either add all checks or none, out of scope for this leg.
8. n/a.

## WALTER — `AGENTS/WALTER/CLAUDE.md` (67,664 B) — ⚠️ largest file, well over the flag threshold (208% of it)
1. **Boot location:** `## SPAWN PROTOCOL` L45 → `### Boot (read phase — order matters)` L49. Numbering: `0.`–`10.7` flat with heavy letter-suffix branching (0.5, 6b, 6c, 7b–7f, 10.5, 10.7).
2. **Existing shared-script step:** NONE of the four grepped hygiene-script patterns (`ledger_staleness`/`orphan_check`/`consumer_check`/`claim_check`) appear — WALTER's boot uses its own bespoke `walter_doctor.py` (L52–56) instead of the shared fleet scripts, consistent with its "architectural" auto-push exception status.
3. **Insertion:** boot's last numbered step before `### Execute` (L91) is `9. **Active LIAISON discovery**` (L85). Insert new step **`9a.`** after L85 (verbatim, occurs once):
   `9. **Active LIAISON discovery** — \`(cd "$(git rev-parse --show-toplevel)" && find AGENTS/*/handoff_WALTER -name LIAISON.md)\` *(cwd-proofed 2026-07-01 — old form silently returned nothing from the own-dir launch cwd)*; for ACTIVE channels (STATUS manifest) with new turns since last boot → read the latest turn(s). **Outbox queue scan:** \`(cd "$(git rev-parse --show-toplevel)" && ls AGENTS/WALTER/outbox/REQ-*.md)\` — surface any >14d unresolved. [→ BP §9]`
   Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" WALTER (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/WALTER/registry/corrections_receipts.tsv). [→ BP §9a]` (WALTER's convention tags every step with a `design/BOOT_PROTOCOL.md` §-pointer — DAEDALUS should add a matching BP section if this step is adopted).
4. **boot.py:** NO standalone `boot.py` — WALTER uses `tools/walter_doctor.py` (L52) as its mechanical health scan, one step (0.5) among ~20 prose boot steps. CLAUDE.md prose is unambiguously "the boot."
5. **registry/:** EXISTS — `AGENTS/WALTER/registry/` holds `BATCH_MANIFEST.tsv`, `CORRECTIONS.tsv` (67,664 B file; note **`CORRECTIONS.tsv` here is WALTER's own registry that R1 reads fleet-wide** — per the background brief, `AGENTS/WALTER/registry/CORRECTIONS.tsv` is the canonical fleet correction register WALTER owns schema+prune for. **WALTER already has a `corrections_receipts.tsv`-shaped file present? No — `CORRECTIONS.tsv` is the source register, not WALTER's own receipts file; WALTER would still need its own `registry/corrections_receipts.tsv` for its OWN receipts, separate from the register it owns.**
6. **Size:** 67,664 B — **flag, and explicitly called out by the task brief** — this is the largest CLAUDE.md surveyed, ~2.08× the byte flag and would be the single biggest argument for demoting/rotating content if DAEDALUS's own byte-tier convention were applied to other desks (WALTER has no stated byte budget of its own in this file, unlike DAEDALUS's self-imposed 32,550 B cap).
7. **Card:** NO — no `SPAWNED-MODE` heading found in WALTER's file (grep for "SPAWNED-MODE" on WALTER returned nothing; WALTER's `## RUN MODE — Full WALTER only` heading at L35 is a different concept, not a spawn card).
8. **Special-class:** WALTER is the fleet's signal router with its own `BOARD_CONSUMPTION_SPEC` and **architectural auto-push exception** (root CLAUDE.md names WALTER as one of three agents that self-push, "per its BOARD_CONSUMPTION_SPEC §7"). This does not exempt WALTER from R1 — the auto-push exception is about *when it pushes*, not *whether it consumes fleet corrections*. WALTER is also the **owner** of `CORRECTIONS.tsv` itself (schema+prune), which is a distinct role from being a *consumer* that must receipt named rows addressed to it — both are true simultaneously and worth flagging to DAEDALUS: **wiring R1 into WALTER's own boot could create a self-referential loop worth a sentence of caution** (WALTER pruning the register vs. WALTER receipting against it) — not a blocker, just a note for the packet.

## WATT — `AGENTS/WATT/CLAUDE.md` (17,907 B)
1. **Boot location:** `## BOOT SEQUENCE (when spawned)` (no line-number captured in this pass via Read; confirmed via grep at L28 for step 1). Numbering: `1.`–`8.` flat.
2. **Existing shared-script step:** NONE of the four grepped hygiene patterns appear standalone — `boot.py` (step 4) internally runs "ledger staleness (`--days 7`)" as one leg, not a separate CLAUDE.md-visible `scripts/ledger_staleness.py` call.
3. **Insertion:** last boot step before `8. Execute the task.` (L35) is `7. **Channel-liveness check**` (L34, verbatim, confirmed `grep -c`=1 on its closing clause):
   `7. **Channel-liveness check** — for each of P1–P4, is there a *current, dated* live read? Any channel without one is a **gap to close this session** (the #1 guard), not idle background.`
   New step **`7a.`**, before L35. Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" WATT (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/WATT/registry/corrections_receipts.tsv).`
4. **boot.py:** yes (`AGENTS/WATT/boot.py`, step 4), covers ledger staleness + predictions-due + power_watch 5 legs — a substantial fraction of "the boot," but steps 1–3 and 5–8 remain CLAUDE.md prose; a protocol-following session hits the new line.
5. **registry/:** does not exist.
6. **Size:** 17,907 B — under flag.
7. **Card:** NO — WATT has no `SPAWNED-MODE` card (its `## BOOT SEQUENCE (when spawned)` heading covers the same ground inline, no separate card block).
8. n/a.

## YEYOU — `AGENTS/YEYOU/CLAUDE.md` (15,746 B)
1. **Boot location:** `## BOOT (read phase — order matters)` L82. Numbering: `0.`–`6.` flat.
2. **Existing shared-script step:** NONE of the four grepped hygiene patterns appear — YEYOU uses its own `scripts/boot.py` (L91–92, review-queue card), not the shared fleet scripts.
3. **Insertion:** last boot step before `## EXECUTE (review)` (L98) is `6. (If spawned for inbox) process inbox/` (L94, verbatim, confirmed `grep -c`=1):
   `6. **(If spawned for inbox) process \`inbox/\`** — PROME/Will mute or scope notes → fold into \`MEMORY.md\` false-positive rules, then move to \`inbox/processed/\`.`
   New step **`6a.`**, before blank L95–97 / L98 heading. Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" YEYOU (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/YEYOU/registry/corrections_receipts.tsv).`
4. **boot.py:** yes (`AGENTS/YEYOU/scripts/boot.py`, L91–92, review-queue card) — one instrument (step 5) among 7 prose boot steps; CLAUDE.md prose governs.
5. **registry/:** does not exist (YEYOU's structured state lives in `reviews/STATE.tsv`, not `registry/`).
6. **Size:** 15,746 B — under flag.
7. **Card:** NO — no SPAWNED-MODE card found.
8. **Special-class:** YEYOU is the manual/on-demand, per-push reviewer that **has never actually run** — its own file states (§THE CONTRACT, PROOF line): *"NONE YET, and that is the honest state: REVIEW_LOG.tsv has zero rows all-time; YEYOU has never run... machinery is built and scripts/boot.py verifies clean (rc=0, 2026-07-30)."* R1 applicability: **UNCLEAR-but-should-wire-anyway** — per FORUM-6's NEXT-TOUCH rollout convention, YEYOU should still get the R1 line now (dormant desks get wired so they're correct on revival, per the same convention DAEDALUS's own charter cites for itself), but it will be **inert** (no live boot to trigger it) until YEYOU is revived — flag this explicitly in the packet rather than silently wiring it as if it were live.

## ZHAO — `AGENTS/ZHAO/CLAUDE.md` (28,825 B)
1. **Boot location:** `## SPAWN PROTOCOL` L18 (no numbered sub-heading — flat prose list starts immediately). Numbering: `1.`–`7.` flat with letter suffix (1b, 3b).
2. **Existing shared-script step:** ZHAO's boot has no `ledger_staleness`/`orphan_check`/`consumer_check`/`claim_check` call — but its **git/closeout section** (L229–235, outside the boot list) DOES carry `orphan_check.sh` (L233), `memory_index_check.py` (L234), and `consumer_check.py` (L235) as closeout steps, cited-not-restated per root canon.
3. **Insertion:** last boot-phase step before `4. **Execute the task**` (L31) is `3b. **Read \`AGENTS/VOCABULARIES.tsv\`**` (L30, verbatim, confirmed `grep -c`=1 on `1b. **Run the boot brief**` for the earlier step — 3b itself not separately re-verified for uniqueness in this pass, **flag for confirmation**, but it is textually distinct enough — single occurrence of "CANONICAL_ENTITIES for Entity field" expected):
   `3b. **Read \`AGENTS/VOCABULARIES.tsv\`** — use NETWORK_GROUPS for Group field, CANONICAL_ENTITIES for Entity field, SOURCE_TAGS for Source field. If no match exists, use closest term and note the gap.`
   New step **`3c.`**, before L31. Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" ZHAO (§9 rc 0/1/2; rc=1 → --receipt ..., commit AGENTS/ZHAO/registry/corrections_receipts.tsv).`
4. **boot.py:** yes (`AGENTS/ZHAO/scripts/boot.py`, L27, step 1b) — one instrument among 7 prose boot steps; CLAUDE.md prose governs.
5. **registry/:** does not exist.
6. **Size:** 28,825 B — under flag.
7. **Card:** NO — no SPAWNED-MODE card found.
8. n/a.

## PROME — `PROME/CLAUDE.md` (8,369 B) — ⚠️ LIVE SESSION RIGHT NOW; repo-root desk, NOT under `AGENTS/`
1. **Boot location:** `## Boot Sequence` L24. Numbering: `1.`–`5.` flat, and this is deliberately a **thin pointer list** — item 2 (L29) says *"Then follow `PROME/BOOT.md` in full (HANDOFF → SCRATCH → ACTIVE_DECISIONS → STATUS → market-data freshness gate)."* **The actual detailed boot sequence lives in `PROME/BOOT.md`, a separate file not read in this pass** (out of scope per the task's file list, which named only `PROME/CLAUDE.md`) — flagging this as a gap: **the real anchor for a PROME-specific R1 leg may belong in `PROME/BOOT.md`, not `PROME/CLAUDE.md`.**
2. **Existing shared-script step:** NONE of the four grepped hygiene patterns appear in `PROME/CLAUDE.md` (confirmed zero hits). PROME's git/push mechanics section (`## Ask First / Do Not Do Autonomously` L51+, `Git default` paragraph) references `scripts/safe-push.sh` only.
3. **Insertion (CLAUDE.md-only, provisional):** after L31 (verbatim, occurs once):
   `4. Work only on the scoped task Will/Prome gave you.`
   New item **`4b.`**, before L32 (`5. End meaningful sessions per the Handoff Requirement below.`). Text: `**R1 corrections check** — python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" PROME (§9 rc 0/1/2; rc=1 → --receipt ..., commit PROME/registry/corrections_receipts.tsv — PROME is a repo-root desk per the background brief, so its receipts live at PROME/registry/, not AGENTS/PROME/registry/).`
   **⚠️ Recommend DAEDALUS re-open `PROME/BOOT.md` before finalizing** — if that file carries the operative step sequence, the CLAUDE.md-only insertion above is necessary-but-not-sufficient; BOOT.md may need its own anchor.
4. **boot.py:** PROME has no `boot.py`-style single script — `PROME/BOOT.md` is a **document**, not a script, per L29's own wording ("follow PROME/BOOT.md in full"). This is a structurally different pattern from every domain-agent desk surveyed.
5. **registry/:** does NOT exist (`PROME/registry/` not found) — consistent with the background brief's note that "PROME's receipts live at PROME/registry/ because PROME is a repo-root desk" (i.e., it needs to be created fresh, not nested under `AGENTS/PROME/` which doesn't exist either).
6. **Size:** 8,369 B — well under flag; smallest file surveyed by a wide margin.
7. **Card:** n/a — PROME has no SPAWNED-MODE card in this file (PROME is not itself spawned by a coordinator in the domain-agent sense).
8. **Special-class:** PROME is the coordinator / repo-root desk, and is a **LIVE session right now** per the task brief. **Do not edit** — DAEDALUS should packet PROME rather than apply this insertion directly. Applicability: R1 is self-evidently applicable to PROME (it is the desk most likely to be *named* in fleet corrections given its coordination role), but the correct anchor file needs a second look at `PROME/BOOT.md`.

---

## Summary table

| Desk | Anchor line# | Label | registry/ exists | CLAUDE.md bytes | Card lists R1? | Applicable | LIVE? |
|---|---|---|---|---|---|---|---|
| OZK | L52 | 7a. | NO | 25,260 | NO (card scope doesn't itemize checks) | YES | no |
| RAV | — (no CLAUDE.md) | — | NO | n/a | n/a | UNCLEAR/likely-NO | no |
| RED | L72 | 9e. | YES | 40,560 🚩 | NO (no card) | YES | **YES — do not edit** |
| REGINALD | L56 | 9c. | NO | 34,819 🚩 | YES — should add | YES | no |
| SAM | L49 (tentative — needs re-verify) | 7a. | NO | 32,853 🚩 | NO (no card) | YES | no |
| SHADE | L90 | 4b. | NO | 13,071 | NO (no card) | YES | no |
| TERRY | L160 | 14. | NO | 28,697 | NO (no card) | YES | no |
| VIOLET | L39 | 5c. | NO | 24,518 | NO (no card) | YES | no |
| VULCAN | L48 | 8b. | NO | 55,864 🚩 | YES — should add | YES | no |
| WAL | L64 | 7a. | NO | 18,647 | card exists, NO-don't-add (scope-consistency) | YES | no |
| WALTER | L85 | 9a. | YES | 67,664 🚩🚩 (2.08× flag) | n/a (no card) | YES, +self-referential-loop note (owns CORRECTIONS.tsv) | no |
| WATT | L34 | 7a. | NO | 17,907 | n/a (no card) | YES | no |
| YEYOU | L94 | 6a. | NO | 15,746 | n/a (no card) | UNCLEAR (never run) — wire anyway per NEXT-TOUCH | no |
| ZHAO | L30 (3b — uniqueness not independently re-verified) | 3c. | NO | 28,825 | n/a (no card) | YES | no |
| PROME | L31 (CLAUDE.md only — BOOT.md unread) | 4b. | NO | 8,369 | n/a | YES, but anchor file uncertain | **YES — do not edit** |

**Could NOT find a fully safe/verified unique anchor:** SAM (last-boot-step tail not fully mapped past L60; anchor line's `grep -c` uniqueness not independently confirmed in this pass — needs a second read of L51–~90) and ZHAO (step 3b's uniqueness assumed, not independently grep-confirmed). PROME's anchor is safe within CLAUDE.md but likely incomplete — `PROME/BOOT.md` is the probable true target and was not read in this leg. RAV has no anchor file at all. RED and PROME are live — DAEDALUS packets them rather than editing.
