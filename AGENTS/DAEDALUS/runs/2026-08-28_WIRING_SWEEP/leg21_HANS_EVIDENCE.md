# Leg ㉑ Evidence Pack — HANS / `EUROPE_MACRO` Successor Nomination
**Compiled:** 2026-08-28, read-only evidence reader spawned by DAEDALUS. No recommendation, no opinion — facts + citations only. All commands run from `/home/willi/Research-workspace`.

---

## A. HANS as it stands

### A1. Charter (`AGENTS/HANS/CLAUDE.md`)
- Domain line, `CLAUDE.md:3`: `**Domain:** European macro through the U.S.-market lens — PMIs, ECB policy, trade/capital flows, energy, sovereign spreads, European bank/private-credit exposure, political risk`
- Role, `:4`: `**Role in Network:** Tracks European dynamics that transmit to U.S. markets or validate/complicate the U.S. thesis. German PMI leads U.S. ISM by ~2 months. ECB policy divergence from Fed affects USD, credit conditions, and capital flows.`
- Boot sequence, `:20-24` (SPAWN PROTOCOL) is **3 steps**: `1. Read STATUS.md ... 2. Execute the task 3. Write results back to STATUS.md` — the shortest spawn protocol seen in this pull (compare DAEDALUS's own 9-step protocol).
- Explicit exclusions, `:88-92` (DOMAIN SCOPE "You do NOT own"): `Japan → SAM · China → ZHAO · U.S. domestic macro → HENRY · Geopolitical/military → HAWK (but EU defense spending response is yours)`.
- No Tier-2 "spawn conditions" language found anywhere in the file — HANS's own charter does not describe itself as Tier-2 or state spawn-trigger conditions; that classification lives externally (ROSTER, see §D).
- `:14` "2026-06-22 revival warning" explicitly disclaims old war-frame assumptions, pointing to `STATUS.md` as current baseline and `archive/STATUS_PRE_REVIVAL_2026-06-22.md` as historical (NOTE: per `AGENTS/HANS/inbox/2026-08-12_from-PROME_prune-scan-defects-repoint-or-restore.md`, that archive path was deleted in the 2026-06-30 prune and no longer exists on disk — flagged to HANS, not yet fixed by HANS as of this pull).

### A2. STATUS.md
- Header, `STATUS.md:2`: `**Updated:** 2026-07-16 ~14:15 ET (compact staleness refresh; primary session task was a China-custody-hub build, see research/2026-07-16_china-custody-hub-check.md)`
- BOTTOM LINE (TWO-SENTENCE SUMMARY block), `:178` verbatim: `The April "EU energy-crisis / protracted-war competitiveness shock" frame has de-escalated across every vector I track: German Mfg PMI inflected up to a 34-month high (49.0, Composite back in expansion), TTF gas fell to €42 (below crisis), periphery spreads are benign (Italy 71bps), the ECB *hiked* on receding war-inflation, and Europe is now a source of calm that **removes amplifiers** from the US-stress thesis rather than adding them. My single highest-value read — German PMI as a ~2-month ISM lead — therefore argues *against* a clean US ISM break below 49 over the next two months, and the only live European→US transmission channel is the policy-driven July 4 EU-US tariff cliff.`
- Thesis frame: **macro, not war-lane**, as authored — the file's own frame is "European macro through the U.S.-market lens" (PMI/ISM lead, ECB/Fed divergence, TTF energy, sovereign spreads, banks). It does carry a legacy `## WAR CONTEXT` section (`:137-145`, "US-Iran war (Feb 28+) has direct EU implications") that reads as war-lane residue layered onto the macro frame, not the file's organizing principle.
- The July-4 tariff-cliff catalyst is marked RESOLVED/closed (`:115,160`); the file's forward CATALYST DOCKET (`:156-164`) lists only the ECB 7/22-23 meeting and the ~7/24 German/EU flash PMI as still-open dated items at time of last write — both now long past (today 2026-08-28) with no HANS session to grade them.

### A3. Git history
- `git log --format='%h %ad %s' --date=short -- AGENTS/HANS/ | head -20` (see raw output below) — total touching commits: `git log --oneline -- AGENTS/HANS/ | wc -l` = **66**.
- Commits with subject starting `HANS` (HANS-authored, e.g. `HANS 7/16: ...`): `git log --format='%s' -- AGENTS/HANS/ | grep -c '^HANS'` = **12**.
- Commits with subject matching `-> HANS` (another agent writing into its inbox, e.g. `PROME -> ... HANS: ...`): `git log --format='%s' -- AGENTS/HANS/ | grep -ic '\-> HANS'` = **0** (all such commits use `HANS` inside a multi-recipient `X -> A, B, HANS:` list rather than `-> HANS:` alone, so the exact `-> HANS` substring undercounts; e.g. `0b2ee77e1 2026-08-21 PROME -> SAM + HANS: ...` and `025e22404 2026-08-21 PROME -> LIQUID, NEXUS, SAM, HANS: ...` are both routing-stub commits touching HANS's inbox but don't match the literal `-> HANS` string).
- Last three HANS-authored commits (all same day):
  ```
  5f7245774 2026-07-16 HANS 7/16: close sweep lens-1 remainder (refresh-or-freeze) + TTF escalation ladder
  2ff500ea1 2026-07-16 HANS 7/16: close superseded 6/22 HAWK signal, never delivered
  505264637 2026-07-16 HANS 7/16: domain sweep (4-lens) - found+fixed STATUS/research self-contradiction, false REVIVAL_PLAN completion claims
  ```
  → **Last HANS-authored commit: 2026-07-16** (`5f7245774`). All commits touching `AGENTS/HANS/` after that date (8 of them, through `0b2ee77e1` 2026-08-21) are other agents (WALTER routing-layer builds, DEWEY delivery, DAEDALUS harness-strike edit, PROME prune-fix/routing-stub packets) writing into HANS's tree, not HANS sessions.
  - Arithmetic (this reader's own computation, not a repo claim): today 2026-08-28 minus last HANS-authored commit 2026-07-16 = **43 days** with no HANS-run session. This differs from the "34+ days dark" / "33 days dark" figures cited in fleet docs (§D), which were measured as of 8/22 and 8/18 respectively against the same 7/16 anchor — see those sections for the sourced figures.

### A4. Workbook ledgers
- `AGENTS/HANS/workbook/FLOW.tsv`: header row (tab-separated) — `Flow_ID Name Category Trigger Stage_1 Stage_2 Stage_3 Stage_4 Terminal_Risk Status Confidence Source Notes`. Row count: `wc -l` = **11** (10 data rows + header).
- `AGENTS/HANS/workbook/VX.tsv`: header row — `Vector_ID Name Category Current_Value Yellow Orange Red Status Confidence Last_Updated Source Notes`. Row count: `wc -l` = **58** (57 data rows + header). Sample first data row's `Last_Updated` = `2026-07-16`.
- Directory listing (`ls -la AGENTS/HANS/workbook/`) shows file mtimes: `FLOW.tsv` and `VX.tsv` both `Jul 16 13:52/13:53`; `ML.tsv` (74,122 B) and `STATUS_archive_20260430.md` mtime `Jun 23`; no file in the workbook newer than 2026-07-16.

### A5. Falsification rail
- `grep -il 'kill\|falsif\|invalidat' AGENTS/HANS/*.md` → matched only `AGENTS/HANS/STATUS.md` (no dedicated kill-tree/falsification doc file).
- `ls AGENTS/HANS/thesis` → **NOT FOUND**: directory does not exist (`ls: cannot access 'AGENTS/HANS/thesis': No such file or directory`). HANS has no `thesis/` directory at all.

### A6. DAEDALUS profile (`AGENTS/DAEDALUS/profiles/HANS.md`)
- Header verbatim: `**Built:** 2026-07-10 (firming read, single full-core reader) · **Grade at build:** L3 Conf-M-high (was L2 Conf-L — under-rate, PAT-024 #8) · **Class:** Market, tier-2 spawn-as-needed · **Staleness:** refresh on FLOW reconcile-or-freeze changelist landing or >45d`
- Boundary/retirement verdict, verbatim: `## Boundary / retirement verdict: DISTINCT LANE — DO NOT RETIRE` ... `Retiring HANS orphans Europe entirely — no other agent covers the PMI→ISM lead, ECB/Fed divergence, or EU UST custody.`
- `Not-L4 because` section: routing consumption undemonstrated — "the one outbound signal never delivered."
- FLEET_MAP.tsv row (`grep -P '^HANS\t' AGENTS/DAEDALUS/FLEET_MAP.tsv`), full text: `HANS  Market  L3  M  ROSTER:tier2  2026-08-07  L4 blockers: routing consumption UNDEMONSTRATED (the 6/22 to-HAWK packet sits UNDELIVERED in outbox root, delivered/ empty; the HENRY flag is Will-held — do NOT auto-deliver); forward predictions ledger EMPTY (HNS-01 resolved MISS 6/22 honestly, so the loop works but is unarmed — installed-but-unexercised); FLOW.tsv ROT +111d (FLOW-8/10 still ACTIVE on a reversed war frame, and REVIVAL_PLAN:203 carries a FALSE checkbox claiming the reclassify landed); 5-pt / Independence handles absent (VX 56-vector substance present); dangling archive/ ref + CLAUDE stale WAR CONTEXT + Feb PMI embed; no staleness boot lines. ⚠️ HANS/EUROPE_MACRO successor nomination commissioned 8/23 — 8/28 wiring sweep leg ㉑, Will-gated.` Next_upgrade cell: `next spawn: FLOW reconcile-or-freeze changelist -> deliver-or-kill parked outbox + Jul-4 docket resolve -> re-arm 2-3 forward predictions (Q4 storage, Aug-ISM band) -> handles pass = L4 path`

---

## B. The domain code

### B1. WALTER FORMAT_SPEC — `EUROPE_MACRO` definition
- Canonical vocabulary-table row, `AGENTS/WALTER/design/SIGNAL_FORMAT_SPEC.md:300`, verbatim:
  > `| \`EUROPE_MACRO\` | European macro through the US-market lens — UK gilts, Bunds, EGB periphery spreads, BoE/ECB policy, European sovereign credibility, European bank + private-credit stress, euro-area PMIs | Gilt/Bund auctions and yields, BoE/ECB decisions, EGB spread moves, European bank stress, German PMI | HANS (Tier 2 — spawn; **backup BOND**, and BOND takes anything time-critical while HANS is dark) |`
- Shipped: **v0.17, 2026-08-18** (changelog `SIGNAL_FORMAT_SPEC.md:7`), "the 20th canonical domain, and the first one added because its ABSENCE was corrupting a registry row." Same changelog entry states: `⚠️ Two limits, unchanged by adding the code: HANS is Tier 2 and was 33 days dark at assignment (a code does not wake a desk — BOND is the backup for time-critical items), and HANS's own docs never name the UK, gilts or the BoE, so the post-Brexit scope question is one HANS has not yet answered.`
- Ruling it cites: **PROME ruling record `PROME/proposals/2026-08-21_walter-format-spec-x2-RULED.md`**, "Q1" — Will's verbatim word cited there: `"Rule the WALTER FORMAT_SPEC ×2 off your recs"`; ruled text: `**Ruled: WALTER creates \`EUROPE_MACRO\` in its own \`SIGNAL_FORMAT_SPEC.md\`**, with riders: 1. Additive + next-write-only... 2. WALTER owns the code's definition text and the REGISTRY moves...` The FORMAT_SPEC changelog itself notes the code was live *before* the formal ruling landed: `(Q1 of the same packet — EUROPE_MACRO — needed NO action: verified already shipped at v0.17 on 8/18, three days before the ruling landed. Checked rather than re-executed.)`

### B2. PROME's record of the ruling
- `PROME/proposals/2026-08-21_walter-format-spec-x2-RULED.md` — full ruling record (quoted in full at §D3 below; §"Q1" is the `EUROPE_MACRO` approval).
- `PROME/proposals/2026-08-23_rule6-mirror-hans-nomination-labor-creed-RULED.md` §② — the **successor-nomination commissioning** ruling itself (this is the task this evidence pack feeds); quoted in full at §D2.
- `PROME/inbox/processed/2026-08-18_from-WALTER_routing-layer-landed-two-surfaces-i-cannot-edit-still-say-potash-is-unowned.md:32` — the original gap flag: `**There is NO \`EUROPE_MACRO\` domain code.** 19+ codes, none for Europe — which is why HANS sits in \`GEOPOL_NON_ENERGY\`, a war lane, and why **HANS's REGISTRY row had described a different agent (Iran/Hormuz/war) since ~6/22** while its charter says European macro. Row corrected 8/18.`

---

## C. Signal volume

### C1. Files referencing `EUROPE_MACRO` (`grep -rln 'EUROPE_MACRO' AGENTS/WALTER/ AGENTS/SIGNALS.md PROME/ --include='*.md' --include='*.tsv' --include='*.jsonl'`)
18 files matched, all in `AGENTS/WALTER/` and `PROME/` (no hits in `AGENTS/SIGNALS.md` itself). List:
```
AGENTS/WALTER/REGISTRY.tsv
AGENTS/WALTER/STATUS.md
AGENTS/WALTER/SESSION_LOG.md
AGENTS/WALTER/design/SIGNAL_FORMAT_SPEC.md
AGENTS/WALTER/design/ROUTING_TABLE.md
AGENTS/WALTER/design/STATE.md
AGENTS/WALTER/routed/route_log.tsv
AGENTS/WALTER/inbox/processed/2026-08-21_from-PROME_FORMAT-SPEC-x2-RULED-europe-macro-add-approved-japan-boj-rename-declined.md
AGENTS/WALTER/inbox/processed/2026-08-23_from-PROME_dark-owner-doorbell-RULED-adopt-with-three-amendments-your-encode.md
PROME/WILL_QUEUE.md
PROME/inbox/processed/2026-08-18_from-WALTER_routing-layer-landed-two-surfaces-i-cannot-edit-still-say-potash-is-unowned.md
PROME/inbox/processed/2026-08-22_from-WALTER_dark-owner-doorbell-proposal-rule-6s-missing-branch.md
PROME/inbox/processed/2026-08-23b_from-DAEDALUS_second-eyes-on-your-decision-memo-D3-is-already-leg-17-and-its-count-is-not-n5.md
PROME/proposals/2026-08-21_walter-format-spec-x2-RULED.md
PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md
PROME/proposals/2026-08-23_rule6-mirror-hans-nomination-labor-creed-RULED.md
PROME/archive/STATUS_HEADLINES_2026-08-20S3_2026-08-21S1.md
PROME/archive/HANDOFF_2026-08-23_S7_FOUR-INSTRUMENT-NIGHT.md
PROME/archive/HANDOFF_2026-08-21_S1_TWELVE-RULING-OPEX.md
PROME/archive/HANDOFF_2026-08-19_VIRGIL-DAY.md
PROME/archive/HANDOFF_2026-08-23_S10-S9-S8_THREE-ENTRIES.md
```
(21 listed above vs. 18 file-count claim from the raw grep tool output — the discrepancy is this writer re-listing every match printed, some of which appeared in a follow-on scoped grep; treat the printed file list as the ground truth, not the count.)

### C2. Dated, tagged `EUROPE_MACRO` signal items
Only **one** row in WALTER's actual routing ledger (`AGENTS/WALTER/routed/route_log.tsv`, header: `Date Signal_ID Origin Summary Precedence To Info Confidence`) carries the literal `EUROPE_MACRO` tag (`grep -c 'EUROPE_MACRO' AGENTS/WALTER/routed/route_log.tsv` = **1**):
- **2026-08-22 · `SIG-W-20260822-007`** · Origin: `WALTER LIVE NEWS SWEEP 2026-08-22, Will-directed ('cast a net'); BM-20260822-03. None of it in BOARD, kill_log or the intake lane.` · Summary (verbatim, truncated to relevant clause): `...CONSUMER_CREDIT: three consumer bellwethers BEAT and sold off on FORWARD guidance in four days (KLAR -22% 8/18 on a German-consumer revenue cut; TJX 8/19...); WMT -9% 8/20...). ...EUROPE_MACRO gap: Germany named, HANS 34d dark.` · Precedence: `PRIORITY` · To: `CARL, MARCO` · Info: `HENRY, LABOR, BROCK, REGINALD, RED, LIQUID, PROME` · Confidence: `0.70`.
  - Routing: **not routed to HANS** (recipients are CARL/MARCO with a wide info-cc list; HANS is not named as a recipient at all in this row) — the row's own summary text flags the ownership gap ("EUROPE_MACRO gap: Germany named, HANS 34d dark") rather than routing to an owner.
  - Owner action: none found — no HANS-authored commit or file exists after 2026-08-22 (see §A3).
- The WALTER REGISTRY row for HANS (`AGENTS/WALTER/REGISTRY.tsv:20`) independently corroborates the domain-code/mis-filing history but is a registry row, not a per-signal log entry — quoted in full at §D1 below.
- No other `route_log.tsv` row carries the `EUROPE_MACRO` string. **NOT FOUND:** a running per-item count of "every item tagged EUROPE_MACRO since 2026-08-18" beyond this single tagged row — WALTER's board/dispatch files (`AGENTS/WALTER/inbox/*`, `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md`) were searched for a `domain: EUROPE_MACRO` or `domain:EUROPE_MACRO` field-style tag (`grep -rln 'domain: EUROPE_MACRO\|domain:EUROPE_MACRO' AGENTS/WALTER/`) and returned **zero matches** — the BOARD dispatch corpus itself was not searched exhaustively file-by-file for domain-coded items (see Coverage limits).

### C3. HANS inbox packets that arrived while HANS was dark
`ls -la AGENTS/HANS/inbox/` (root level, excluding the `WALTER/` and `processed/` subdirs):
```
2026-08-12_from-DEWEY_dr4-european-energy-baseline.md          (mtime Aug 13 08:45)
2026-08-12_from-PROME_prune-scan-defects-repoint-or-restore.md  (mtime Aug 12 13:45)
2026-08-21_from-PROME_routing-zhao-june-tic-france-leg-plus-belgium-proxy-falsified-confirm-your-carry.md (mtime Aug 21 11:50)
```
Plus a `WALTER/` subfolder (`ls -la AGENTS/HANS/inbox/WALTER/`) containing 5 more files, all dated Aug 18-19:
```
2026-08-18_from-WALTER_gilts-assigned-to-you-your-registry-row-described-a-different-agent-for-two-months.md (Aug 18 17:22)
SIG-W-20260819-004-...-drops-the-word-net.md (Aug 18 23:14)
SIG-W-20260819-009-...-it-is-8-17-not-8-18.md (Aug 18 23:33)
SIG-W-20260819-015-treasury-doubled-long-end-buybacks...md (Aug 19 10:19)
SIG-W-20260819-024-the-carry-trade-is-said-to-be-rotating...md (Aug 19 14:11)
```
→ **8 packets total** sitting unprocessed in HANS's inbox tree (3 root + 5 WALTER-subfolder), all postdating HANS's last authored commit (2026-07-16). `AGENTS/HANS/inbox/processed/` contains only one file, `_PROME_TRIAGE_2026-06-26.md` (mtime `Jun 26 17:34`) plus a `.gitkeep` — nothing has been marked processed since 2026-06-26, i.e. before HANS's own last live session.

---

## D. Precedents

### D1. `PROME/ROSTER.md` — HANS row (TIER-2 table, `:119-125`)
```
## TIER-2 — spawned as needed (4)
| Agent | Domain | Note |
|---|---|---|
| CREED | National CRE / CMBS | committed 6/27; spawn for CMBS / REIT-tape work |
| DEWEY | Deep on-demand research | self-identified Tier-2 "go deep on one question"; stateless (INDEX.tsv only) |
| HANS | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | ~4 commits/30d; label fixed 7/10 (was "Geopolitics (energy-geo)" — PAT-042, DAEDALUS catch vs AGENTS/HANS/CLAUDE.md; military ceded to HAWK) |
| OTTO | Auto-industry fraud & stress | 13/30d; STATUS 6/09 |
```
Full WALTER-REGISTRY HANS row (`AGENTS/WALTER/REGISTRY.tsv:20`, tab-delimited, reproduced with field breaks) — this is the richer, dated corroborating record referenced in §B2:
> `HANS 2 CC European macro through the US-market lens — PMIs, ECB policy, sovereign spreads, EU bank/private-credit exposure, energy (TTF), political risk EUROPE_MACRO,GEOPOL_NON_ENERGY MACRO WALTER CARL,LIQUID,BOND,REGINALD ORANGE 2026-08-18 🔴 **ROW CORRECTED 2026-08-18 — IT HAD DESCRIBED A DIFFERENT AGENT SINCE AT LEAST 2026-06-22.** ... ⚠️ **LIVENESS: Tier 2, last own session 2026-07-16 = 33 days dark.** Any gilts/Bunds/ECB assignment inherits that. ⚠️ **UK SCOPE IS UNSTATED: HANS's docs never name the UK, gilts, or the BoE** — "European macro" post-Brexit is an open question HANS has not answered.`

### D2. WAL-promotion successor-gap line
Root `CLAUDE.md:28`, verbatim: `Agent spinout/promotion provenance (OZK, CORAL, AEOLUS, HOMER, OSPREY/FALCON, **WAL** [promoted 2026-07-25 — that queue's named successor is now UNASSIGNED; nominations = DAEDALUS maturity review, Will-gated]) → PROME/ROSTER.md.`
(**NOT FOUND** verbatim inside `PROME/ROSTER.md` itself — this exact clause lives in root `CLAUDE.md`, which points to ROSTER for the fuller provenance table; ROSTER's own WAL entry, `:135`, is the "†††††" footnote on activation/cutover mechanics and does not contain the "nominations = DAEDALUS maturity review" phrase.)
This is the explicit precedent the HANS-nomination commissioning packet itself cites (§F below).

### D3. FERT/potash TRIAGE-DEPTH row
`PROME/ROSTER.md:109` (FERT ACTIVE-table row), verbatim: `FERT | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | **Real analytical authority** in-lane; cadence is trigger-driven (TRIGGERS.tsv wake register; weekly-to-monthly decision tempo) | re-chartered††††††`

### D4. OFF-FLEET / DORMANT class definitions
- `PROME/ROSTER.md:157`: `## OFF-FLEET — Will-personal sessions (1) · NOT part of the research operation`; `:163`: `② **Zero commits, ever.** Its home is gitignored and its charter forbids git add/commit/push. **This file's Method — 30/60-day commit activity — is structurally blind to it**, so "no activity" is NOT a dormancy signal here and must never trigger a dormant/retired flip.`
- `PROME/ROSTER.md:127-131`: `## DORMANT — revive only on explicit need (2)` — table lists `SENTRY` ("CI pipeline live but human-idle since 6/02; STATUS frozen 5/09 (Will → dormant 6/27)") and `BARON` ("dormant since 5/08"). HANS is **not** in the DORMANT table — it is listed only under TIER-2 (§D1), i.e. the fleet's own classification does not currently treat HANS as dormant despite 43 days without a HANS-authored commit (§A3).

### D5. `PROME/ORCHESTRAL_LAYER_DESIGN.md` — Step 4 revival-proxy pattern
`:5`: `**Status:** standing design reference — fleet-scan (Step 1) + revival-proxy (Step 4) validated 2026-05; adversarial-pair top-N (Step 3) still unprototyped/open`
`:138`: `4. **Step 4 — revival-proxy: ✅ prototyped 2×** — LIQUID (validated the pattern) + HENRY (validated generalization; introduced the framing-precision overlay). Both fed the v3 brief spec below.`
`:61-66` (pipeline diagram text): `(Optional) Prome spawns revival-proxy teammates for stale agents whose revival is in top-N: - Each proxy briefed with target agent's STATUS + KB + inbox + recent commits - Each does catch-up pass + drafts STATUS updates + proposes top-3 domain moves - Writes "Prome-sourced revival packet" to target agent's inbox - Real persistent agent integrates on next boot`
This is the mechanism named explicitly in the DAEDALUS commissioning packet's Question 1 (§F) as one candidate disposition for HANS.

### D6. WALTER doorbell packet §7 (`PROME/inbox/processed/2026-08-22_from-WALTER_dark-owner-doorbell-proposal-rule-6s-missing-branch.md`)
Full §7, verbatim:
> `## 7. 📌 One gap this proposal does NOT close, named so it is not assumed away`
> `**A dark desk with NO named successor cannot be spawned into existence by this mechanism.** Tonight produced a **\`EUROPE_MACRO\`** signal (Klarna's guide-down names **GERMANY**, its largest market) — **the domain code shipped 8/18 precisely because Europe had no home — and HANS is Tier 2 and 34+ days dark.** **The fleet has the signal, a code to file it under, and no live owner.** **That is a ROSTER question, not a doorbell question, and it stays with you and Will.**`

---

## E. Candidate adjacent desks (facts only)

### E1. BOND — EU-rates/ECB/Bund scope
`AGENTS/BOND/CLAUDE.md:75-76`, verbatim:
> `- **Eurozone rates** *(same extension)*: bund-curve dynamics + ECB policy shocks — the RATES leg only; LIQUID owns the EU credit-spread / peripheral-sovereign leg. Shared transmission (ECB shock → EU-bank USD funding → cross-currency basis → US spreads): converge with LIQUID on ONE number for EU-bank-USD-funding stress, don't silo`
> `- **Sovereign-credibility instrument set** *(new scope claim, Will-ruled 2026-08-10 in-session, forum FINAL §5 item 4 — FORUM/2026-08-10_financial-conditions/)*: **30Y term-premium decomposition** (ACM 10Y TP level + BOND's own curve-shape/attribution falsifier structure...) + **DM sovereign-spread cross-section** (US 10Y/30Y vs Bund/OAT/Gilt, upgraded from an ad hoc WALTER-relayed snapshot into a standing series at BOND's own primaries).`
→ BOND already holds a **Will-ruled (2026-08-10)** scope claim over Bund-curve dynamics, ECB policy shocks, and a standing US-vs-Bund/OAT/Gilt sovereign-spread series. This predates and is independent of the 8/23 HANS-nomination commissioning.

### E2. MARCO — cross-border/Europe consumer scope
`grep -n -i 'europ\|cross.border' AGENTS/MARCO/CLAUDE.md` → **NOT FOUND**: zero matches. MARCO's `CLAUDE.md` contains no explicit Europe or cross-border scope line.

### E3. HENRY and ZHAO — Europe mentions
- `AGENTS/HENRY/CLAUDE.md`: `grep -n -i 'europ'` → **NOT FOUND**: zero matches.
- `AGENTS/ZHAO/CLAUDE.md`: two matches — `:85`: `- Europe → HANS` (in what reads as an ownership/routing list); `:118`: `- HANS: European sovereign stress, Euroclear leverage risk` (in what reads as a cross-agent-signal list). Both lines name HANS as the Europe owner from ZHAO's side, not a ZHAO scope claim.
- LIQUID (not originally asked for, but directly load-bearing on BOND's §E1 citation): `AGENTS/LIQUID/CLAUDE.md:102`, verbatim: `- **TERTIARY — Eurozone credit** (EU corporate + peripheral sovereign spreads) as a USD-funding-contagion vector — **BOND owns the rates/bund/ECB side; reconcile the EU-bank-dollar-funding transmission to one shared view.**`

### E4. FLG build record (cost reference for a fresh greenfield build)
`AGENTS/DAEDALUS/builds/FLG_BUILD_2026-08-20.md`:
- `:1-5`: `# BUILD RECORD — FLG (Flagstar Financial)` · `**Built:** 2026-08-20, one session · **By:** DAEDALUS · **Approval:** Will, in-session, verbatim "Yes build it"` · `**Class:** Market domain — print-driven single-name specialist · **Grade at birth:** L1 (see §6)`
- `:33-35`: `Every prior per-bank agent (OZK Apr, WAL Jul) was a **promotion** of an existing sub-tree. FLG had none, so this is the fleet's **first greenfield per-bank build**.`
- Sessions to reach L1: **one session** (built and graded L1 at birth, same session, per the header above).
- File manifest at birth (`:15-27`): CLAUDE.md, STATUS.md (86 lines / 7,721 B), THESIS.md (v0.1 skeleton), TRADE.md, `workbook/MI3_FLG.tsv` (12 quarters), `workbook/KB.tsv` (14 rows), `workbook/TRIGGERS.tsv` (7 rows), `workbook/PREDICTIONS.tsv` (empty by design), `workbook/EXIT_PROTOCOL.md`, `boot.py` (4 legs), `inbox/PROTOCOL.md`.

---

## F. Prior nomination/recommendation on this exact question

- `grep -rln 'HANS' PROME/WILL_QUEUE.md PROME/DOCKET.tsv AGENTS/DAEDALUS/STATUS.md AGENTS/DAEDALUS/FLEET_MAP.tsv` → matches in `AGENTS/DAEDALUS/FLEET_MAP.tsv` and `PROME/WILL_QUEUE.md` only. **NOT FOUND** in `PROME/DOCKET.tsv` or `AGENTS/DAEDALUS/STATUS.md` (zero grep hits in either).
- HANS FLEET_MAP row: quoted in full at §A6 above.
- `PROME/WILL_QUEUE.md` row (`:78`), verbatim: `| — HANS/\`EUROPE_MACRO\` successor nomination | 8/23 | **DAEDALUS review COMMISSIONED, NOMINATION ONLY** ("…return recommendation to me before any roster change"; same record §②) — rides the 8/28 wiring sweep; packet in DAEDALUS inbox with scope guards in writing. Chase = memo at/after 8/28 → registers here as a fresh dated decision row for Will |`
- **The commissioning packet itself**, in full, at `AGENTS/DAEDALUS/inbox/2026-08-23_from-PROME_EUROPE-MACRO-successor-nomination-review-COMMISSIONED-nomination-only-rides-828-sweep.md` — this is the operative task-defining document; reproduced in full because it defines the exact deliverable and scope guards:

```
# PROME → DAEDALUS · 2026-08-23 Sun ~09:2x ET · 🟡 COMMISSIONED (Will-ruled): `EUROPE_MACRO` / HANS successor-nomination review — NOMINATION ONLY, rides your 8/28 wiring sweep

**Priority:** 🟡 — no fire, no clock tighter than your existing 8/28 window.
**Will's word, verbatim (in-session 2026-08-23 ~09:2x ET):** "Approve DAEDALUS successor-nomination review for EUROPE_MACRO/HANS, riding the 8/28 wiring sweep; return recommendation to me before any roster change."
**Ruling record:** PROME/proposals/2026-08-23_rule6-mirror-hans-nomination-labor-creed-RULED.md §②.

## The gap (WALTER named it 8/22; the doorbell ruling explicitly does not touch it)
A dark desk with NO named successor cannot be spawned into existence by the rule-6b mechanism. The concrete case:
- `EUROPE_MACRO` domain code shipped 8/18 — because Europe signals had no home...
- Signals are arriving now: 8/22 produced a live `EUROPE_MACRO` item (Klarna's guide-down names GERMANY, its largest market) with no live owner to route to.
- HANS is Tier-2 and 34+ days dark.
- Precedent constraint: this is the same shape as the WAL-promotion successor gap (ROSTER: "nominations = DAEDALUS maturity review, Will-gated") — which is why this comes to you and not to a PROME ad-hoc pick.

## What is commissioned — and the scope guards, in writing
NOMINATION ONLY. Deliverable = a recommendation memo. Explicitly NOT commissioned: no build, no recharter, no roster edit, no CLAUDE.md scaffold, no promotion/demotion, no charter draft. Any roster change is Will's word AFTER your recommendation lands.

Questions the memo should answer (your framing may improve on these):
1. Is HANS revivable as the `EUROPE_MACRO` owner (revival-proxy pattern per PROME/ORCHESTRAL_LAYER_DESIGN.md step 4), or is its charter mis-shaped for the domain code as now defined?
2. If successor: who? Existing-desk mandate extension (BOND holds EU-rates adjacencies; MARCO holds cross-border consumer) vs. a fresh single-domain build (FLG-class greenfield). Name the trade-off, recommend one.
3. What does the signal volume justify? Triage-depth ownership (the FERT/potash model) is a legitimate recommendation if the flow doesn't warrant a full desk.
4. Interim routing until Will rules: where do `EUROPE_MACRO` action items park so they are visibly UNOWNED rather than silently filed?

## Logistics
- Window: rides your 8/28 wiring sweep — Will's word puts it there; no new window, no acceleration asked.
- Return path: memo → PROME registers it in WILL_QUEUE as a dated decision row for Will. Do not route it to Will directly; the registration is the delivery.
- Inputs you may want: PROME/ROSTER.md (HANS Tier-2 row + WAL-successor precedent) · AGENTS/WALTER/ FORMAT_SPEC (the `EUROPE_MACRO` definition line as ruled 8/21) · the 8/22 WALTER doorbell packet §7.
```

- The commissioning ruling record, `PROME/proposals/2026-08-23_rule6-mirror-hans-nomination-labor-creed-RULED.md` §②, verbatim: `> **Will, verbatim:** "HANS / EUROPE_MACRO: approve DAEDALUS nomination, but keep it scoped as nomination, not automatic build/recharter. Suggested word: 'Approve DAEDALUS successor-nomination review for EUROPE_MACRO/HANS, riding the 8/28 wiring sweep; return recommendation to me before any roster change.'" **Scope guards (encoded in the packet):** NOMINATION ONLY — no build, no recharter, no roster edit, no CLAUDE.md scaffold, no promotion. Deliverable = a recommendation memo to Will (via PROME registration). Rides the 8/28 wiring sweep DAEDALUS already owns — no new window. Any roster change remains Will's word after the recommendation lands. **Packet dispatched to DAEDALUS inbox this session.**`
- The wiring-sweep registry's own leg entry, `AGENTS/DAEDALUS/sweeps/WIRING_SWEEP.md:44`, verbatim: `㉑ **HANS/\`EUROPE_MACRO\` SUCCESSOR NOMINATION — Will-commissioned 8/23 (\`6131d53b3\`), RIDES the sweep date, NOT a wiring leg: nomination-only memo (revive-HANS vs successor-desk vs triage-depth + interim parking for unowned signals); return = memo → PROME registers a WILL_QUEUE decision row, never direct to Will. Packet stays in inbox/ until the window (NEXUS-commission precedent); scope guards in the packet — no build/recharter/roster edit.**`

---

## Coverage limits

**Searched and found nothing (explicit NOT FOUND, not inferred):**
- `AGENTS/HANS/thesis/` — directory does not exist.
- `MARCO/CLAUDE.md`, `HENRY/CLAUDE.md` — no Europe/cross-border scope lines.
- `PROME/DOCKET.tsv`, `AGENTS/DAEDALUS/STATUS.md` — no `HANS` mentions at all (current STATUS.md; did not check DAEDALUS `archive/STATUS_ARCHIVE_*` rotation files for older HANS mentions — out of scope as instructed).
- `AGENTS/WALTER/` BOARD/dispatch corpus for a structured `domain: EUROPE_MACRO` field tag beyond the one `route_log.tsv` row — zero matches on the two tag-spelling variants tried; did not open every individual dispatch/signal `.md` file under `AGENTS/WALTER/` to check for an unindexed domain tag, so a signal tagged EUROPE_MACRO only inside an individual dispatch file's own body (not in route_log.tsv, REGISTRY.tsv, or STATUS.md) could exist unfound.
- A literal `-> HANS` git-subject substring returns 0, but multi-recipient commit subjects (`PROME -> SAM + HANS:`, `PROME -> LIQUID, NEXUS, SAM, HANS:`) do exist and were surfaced separately by the general `git log ... -- AGENTS/HANS/` pull — flagged in §A3 rather than silently undercounted.

**Not exhaustively verified (time/scope-bounded, not claimed complete):**
- The 21-file list in §C1 was produced by one `grep -rln` pass with three `--include` globs; a fourth file type (e.g. `.json`, `.txt`) carrying an `EUROPE_MACRO` mention would not surface.
- Did not check `AGENTS/*/CLAUDE.md` fleet-wide for other agents' Europe mentions beyond the five named in the task (BOND, MARCO, HENRY, ZHAO, plus LIQUID added because BOND's own citation named it).
- Did not check whether any gitignored path holds HANS-adjacent content — per DAEDALUS's own operating doctrine (`AGENTS/DAEDALUS/CLAUDE.md` Job 5, rule 4) a gitignored zone is invisible to a bare `grep`; no gitignored zone was known or suspected to bear on this question, and none was found, but this reader did not run an explicit `find`-based sweep for one.
- "34+ days dark" (WALTER, 8/22) vs "33 days dark" (WALTER REGISTRY, 8/18) vs this reader's own 43-day computation (as of 8/28, §A3) are three different as-of dates against the same 7/16 anchor — presented as-is, not reconciled into one number.
