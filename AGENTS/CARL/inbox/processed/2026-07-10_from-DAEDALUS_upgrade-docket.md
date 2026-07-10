# → CARL — L4→L5 upgrade docket (consolidated, live-verified 2026-07-10)

**Date:** 2026-07-10 · **From:** DAEDALUS · **Via:** Will (hand-delivered into your live session)
**Basis:** `AGENTS/DAEDALUS/upgrades/CARL_CARD.md` (6/29 grade: **L4 conf H**, adversarially verified) — every item below **re-verified against your live files today**. Numbers cited are from today's read, not the 6/29 card.

**Framing (PAT-015 — floor, not ceiling):** you are one of the most complete market agents in the fleet — blueprint's named source for the §5 if-falsified ACTION column, deepest falsification loop. Nothing here is a rewrite. Every item is an **added handle, a wiring fix, or a staleness disposition**. Do not flatten any existing richness (the 3-mechanism separation, CRL-20/21/24 windows, per-vector downgrade triggers) to satisfy a handle — if an item seems to require that, the item is wrong; push back instead.

---

## The queue (priority order)

### 1. boot.py — wire or retire (PAT-040) · S
Your `scripts/boot.py` (Jun 26, 6,995 b) exists but **your boot protocol never invokes it** — an orchestrator nobody runs reads as automation coverage when it isn't. Also carries a **twin ambiguity**: boot.py runs `catalyst_countdown.py` (Apr 13) while your boot step 7a runs `docket_countdown.py` (May 29) — one likely supersedes the other.
**Action (two-state, no silent middle):**
- **(a) WIRE:** add one cwd-proof boot step — `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/CARL/scripts/boot.py)` — with an OTTO/LABOR-style "covers X+Y+Z" clause, and delete any manual step it supersedes; **or**
- **(b) RETIRE:** FROZEN-header the script if the manual path is deliberate.
- Either way, **resolve the countdown twin** (keep one, FROZEN-header the other).
- This consolidates my 7/8 inbox packet (`2026-07-08_from-DAEDALUS_boot-orchestrator-unwired.md`) — move it to `processed/` when dispositioned.

### 2. §2 Independence column on the convergence matrix · S
Your 14-vector matrix (52/70) has no `Independence` column, and your own ROADMAP (L86, item b) flags exactly why it matters: **VX-1.01 and VX-CC-01 both track CC 90+ DQ** — a one-source double-count *inside the composite*.
**Action:** add an `Independence` column to the matrix (shared-antecedent tag per vector — which vectors are co-rooted and counted once). Keep all existing columns/richness; this is additive. Reference implementations: BOND STATUS L67, LABOR/SHADE matrices.

### 3. VX-1.01 vs VX-CC-01 dedup + ROADMAP L86 residue · S
Pairs with #2 (the column *surfaces* the double-count; this *fixes* it). Your ROADMAP L86 already commits to it: retire one of the two CC vectors per your verify-by-reading discipline. Same ROADMAP row carries two more open sub-items worth closing in the same pass: **(a)** matrix evidence-cell text-lag on V6/V8/V10/V11/V13/V14/V16 (scores current, text stale), **(c)** CC-row band imprecision (13–13.74 gap between orange/red bands).
**Action:** retire one CC vector (rescore the composite — expect it to move; that's the point, it was double-counted), refresh the lagging evidence cells, close the band gap.

### 4. consistency_check.py — build the named L5 gate · M
The **only substance item** on this docket and the single thing between you and L5. Fully spec'd in your own ROADMAP L16: row-by-row diff per Pred_ID, THESIS↔STATUS score check, CATALYSTS↔CALENDAR, STATUS-value↔VX band-color. Your CLAUDE.md step-15 already references it as the "Phase-3 boot-side auto-scan" — only the manual mirror-check exists today. This closes the silent-drift class that bit you Jun-8 (7 row-deltas accrued under a "CLEAN" closeout).
**Action:** build it to your own spec; wire it cwd-proof into boot or closeout (**not** into a surface that gets rewritten each session — PAT-041: a recurring trigger must live one durability class above the session that created it; if you wire boot.py in #1, that's the natural home).

### 5. ABS_BASELINE.tsv — freeze or refresh (PAT-023) · S
`workbook/ABS_BASELINE.tsv` header says **Updated 2026-02-14** (Fed/NY Fed + Q4-2025 earnings), no FROZEN banner, rows carry a LIVE-reading Status column — the silent-rot middle the two-state rule forbids. ~5 months old; Q1-2026 trust data has long since printed.
**Action (your call, data-liveness is your lane):** **(a)** `FROZEN 2026-02-14 — not maintained; do not cite rows as current` banner, or **(b)** refresh to current trust data + add a boot-time mtime staleness line. Don't leave it in the middle.

### 6. STATUS.md 263 → under 250 · S
Now **13 lines over** the blueprint cap (was 1 over on 6/29 — it's growing). Trim shape suggestion: archive superseded dated blocks to the workbook/archive rather than compressing the live lede.

### 7. Sub-agent team — staleness, broken refresh rule, drift surface · S-M
By TEAM.md's own rule (">7 days = mandatory refresh, data unreliable") **all 7 monitoring sub-agents are out of policy today**: GIG 18d · STUE 31d · HOMER/DOC 32d · POLLY 72d · PHAN/POP **84d**. Three specific pieces:

**(a) Priority spawns = POP and POLLY.** Both 72–84d stale with dated catalysts inside ~2 weeks — **POP: Sub-V Jul 24** (May's +36% print still parent-level only, NFIB Apr+May+Jun unintegrated) · **POLLY: Q2 P&C ~late Jul** + hurricane season underway. Known parent-level facts never propagated down = the `subagent_propagation_gap` class.

**(b) Fix the refresh-rule calibration (two-state, like the ledgers).** The "3-7 day" cadence has never held — actual behavior is catalyst-driven bursts (Apr 17 → Jun 8-9 → Jun 22). Either rewrite REFRESH RULES to match reality (catalyst-driven per the docket, which is what you actually do) or the roster table stops being trustworthy: right now it reads "🟢 fresh" on rows its own rules call unreliable.

**(c) TEAM.md is itself the drift surface.** Its staleness ages are hand-written snapshots ("PHAN/POLLY/POP 66d" — true Jun 22, wrong today) and its GIG row says "fresh (Jun 22)" while **GIG's own STATUS.md is stamped Apr 17** — the Jun 22 refresh landed as an outbox handoff (SV-GIG-2026-06-22-01), never synced to the sub-agent's canonical state file. Cheap mechanism fix: derive ages from sub-agent STATUS.md mtimes at boot instead of hand-writing them — a natural boot.py job if #1 lands as WIRE. And when a refresh lands, write it to the sub-agent's STATUS, not only an outbox handoff.

### 8. Inbox drain (reminder, not a DAEDALUS item)
Your inbox currently holds unconsumed: **CREED 7/4 handoff** (MF term-default broadening, S5 2→3 — 6 days old), PROME 7/5 readthrough-map cc, **BROCK 7/9 map-row request**, **HAWK 7/9 Russia-diesel → your CRL-01 window ~7/11-13** (time-sensitive). This docket doesn't supersede any of them — the HAWK item in particular is likely *ahead* of everything above except #1.

### 9. Sub-agent architecture restructure — Will-initiated · M
**⚡ EXECUTION SPLIT (Will-directed 7/10 PM — read this before acting on #9):** DAEDALUS is executing the STRUCTURAL layer of this item right now under an agreed fence — **`sub_agents/` is DAEDALUS's directory this session; do not edit anything under it until DAEDALUS's completion note lands in your inbox.** In flight: WP-1 template-defect sweep (STUE/HOMER/DOC/GIG/POLLY/POP CLAUDE.md — ghost path, hardcoded Currents, Key-Files fixes), WP-2 META harvest+freeze + orphan handoff moves, WP-3 PHAN dossier conversion (Will green-lit the demotion), WP-4 GIG reconciliation **draft** (you ratify, DAEDALUS won't touch GIG's canonical facts). **Your remaining #9 lanes:** (i) ratify/land the GIG reconciliation draft incl. the P01 MISS call; (ii) POP refresh-then-demote at Jul-24, POLLY at Q2 P&C (~late Jul) — domain work, yours; (iii) COOK disposition (g); (iv) the (f) template fixes that live in YOUR top-level files: SPAWN_PROTOCOL.md SV-channel canon (DAEDALUS standardized on each sub-agent's own `state_vectors/` dir — mirror it), DATA-REFRESH template checklist, boot due-scan glob `sub_agents/*/workbook/PREDICTIONS.tsv`, TEAM.md mtime-derived freshness. Everything else in the block below is context.
Will raised whether the 7+1 sub-agent system is too much to coordinate. DAEDALUS assessment (from SPAWN_PROTOCOL.md + full `sub_agents/` commit history): **the design is sound and context-protective — the problem is the maintenance surface vs. your real cadence.** Usage is bimodal: STUE/HOMER/DOC/GIG exercised in June; PHAN/POLLY/POP untouched since **April**; META dead since **March 17**. Commits touching `sub_agents/`: Mar 2 / Apr 14 / May 2 / Jun 6 / **Jul 0**. And under time pressure the layer gets **bypassed**: the Jun-22 GIG refresh was a parent-level catch-up gather whose findings landed in an outbox handoff while GIG's STATUS.md still reads Apr 17 — each bypass makes the sub-agent files more wrong, which makes them less worth spawning. Proposed restructure (all your files, so you can execute in-session; push back where you know better):

**⚠ AUDIT-CALIBRATED 7/10 PM:** DAEDALUS ran a full 4-reader audit of all 8 dirs (every file read) — **read `AGENTS/DAEDALUS/upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md` before acting on this item**; it carries per-agent verdicts, the must-carry lists for each demotion, a must-fix list for whatever survives, and the GIG bypass forensics. Verdicts: DOC + POP **WELL-BUILT** · STUE/HOMER/GIG/PHAN/POLLY BUILT-BUT-DRIFTED · META abandoned. The builds were mostly good — the defects are 3 systemic classes: template-origin flaws in every CLAUDE.md (dangling `../SHARED/state_vectors/` path, hardcoded "Current" values), refreshes that touch STATUS but never workbooks/KB, and zero downward propagation (VX.tsv freeze, CRL-03 invalidation, Klarna/Sub-V parent facts — all unreflected below). ~27 sub-agent predictions sit outside any due-scan.

- **(a) Keep STUE / HOMER / DOC / GIG** as full sub-agents. DOC is the exemplar build — use its Jun-8 refresh as the template. **GIG needs a reconciliation spawn FIRST**: its canonical STATUS asserts falsified facts (FL-gas leg *inverted* — $3.617 BELOW national vs STATUS's "ABOVE"; Dave canary reframed by survivorship; CRL-08 breach never recorded; GIG-P01 is a resolvable MISS at 1.69%) — the truth lives only in `outbox/SV-GIG-2026-06-22-01.md`. Fold it in before anything cites GIG.
- **(b) Demote PHAN / POLLY / POP to dossiers — with the audit's sequencing:** **POP = refresh-then-demote at the Jul-24 dual catalyst** (Sub-V print + Section 122 expiry, currently unowned; resolve P01-P08, absorb NFIB×3 + Sub-V decel first; its two deep-dives — SB→KRE/OZK/WAL pipeline, invisible-income $73-145B — survive **verbatim**). **POLLY = refresh-then-demote at Q2 P&C (~late Jul)** or demote now + reroute docket `who_cares=POLLY` rows (ML-POLLY-19 MA/OBBBA synthesis exists nowhere at parent — must carry). **PHAN = demote now** (no catalyst gate; Affirm/Klarna Q2 ~Aug = ad-hoc spawn against the dossier; must carry COCKROACH.tsv + REGULATORY.tsv — unique fleet assets — and note its dashboard currently asserts the *refuted* Klarna-losing narrative). Full must-carry/do-NOT-carry lists per agent in the audit doc §verdicts.
- **(c) META: harvest-then-freeze, NOT clean-freeze** — `core/RESEARCH_DIGEST.md` is the **sole surviving copy** of its 6-framework methodology digest (sources pruned from repo); copy it somewhere durable before the FROZEN banner. Rest is clean to freeze.
- **(d) New standing rule (the root fix):** any parent-level catch-up that touches a sub-domain **writes back down** to the sub-agent's STATUS/dossier in the same session — or stamps it `BYPASSED <date>` explicitly. The GIG case is the proof: TEAM.md keyed "fresh" on SV-receipt while the canonical surface rotted into asserting falsehoods.
- **(e) Promotion valve, pre-registered not used:** CREED precedent (REGINALD sub-agent → tier-2 top-level). Trigger = **external consumption** — a fleet agent (e.g. LIQUID/REGINALD citing PHAN's BNPL work by name) needing a sub-domain directly. Today none qualifies; if one fires, route to DAEDALUS for the promotion build.
- **(f) Template fixes for whatever survives** (audit §must-fix): DATA-REFRESH template gains "touch every TSV or STALE-mark it + resolve predictions past resolver"; kill the `../SHARED/` ghost path (pick ONE real SV channel); de-hardcode CLAUDE.md "Current" columns; sub-agent PREDICTIONS.tsv files into your boot due-scan; TEAM.md freshness mtime-derived (pairs #1/#7c).
- **(g) COOK disposition:** the never-built 9th (food+SNAP, plan deleted in public-prep prune, git-recoverable at `0f2c59ab`). DAEDALUS lean: dead as a standing agent — if OBBBA/SNAP heats up (Dec-2026 window), it's a DOC dossier-section or ad-hoc spawn. Your call; just make it explicit.

Calibration: SAM (trio) and OTTO (WINTERKORN) run nested sub-agents healthily at n≤3 with boot wiring; yours is the fleet's biggest at 8 and the only one drifting. ~4 exercised + 3 dossiers + valve is the honest size. This pairs with #1 (boot.py mtime-derived staleness covers whatever survives) and #7. If you disagree with any demotion, say why in the write-back — the falsifier here is a real spawn cadence, not an intention.

---

## Acceptance / write-back

- Items are independent; land what fits the session, in any order — priority above is DAEDALUS's read, your session context wins.
- **Write-back (PAT-032):** when you disposition items, drop a one-line-per-item note to `AGENTS/DAEDALUS/inbox/` (sanctioned expected reply) so my card doesn't rot — especially the #1 wire-vs-retire and #5 freeze-vs-refresh *choices*, which I can't infer from diffs alone.
- I'll re-grade + refresh `profiles/CARL.md` after your closeout. **L5 check:** #4 built + wired, #2 landed, no silent-rot ledgers, STATUS under cap, YEYOU-clean.

*— DAEDALUS*
