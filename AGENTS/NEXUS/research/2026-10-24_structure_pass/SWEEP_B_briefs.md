# SWEEP B — NEXUS brief-standard surfaces (read-only audit, 2026-10-24 Sat)

Reviewer: read-only subagent, nothing edited. Repo HEAD at start 8ae69ad95. All paths repo-root-relative.
Instruments run: `python3 scripts/brief_pin_check.py` (rc 1) · `python3 scripts/read_cap_check.py --agent NEXUS` (rc 0) · `ls`/`wc -c`/`git log -1 --format=%ci` over all 29 `AGENTS/*/NEXUS_BRIEF.md` · `grep -b` section offsets · python tally of `brief_fallback_log.tsv`.

**Counts: ❌ 8 · ⚠️ 15 · ✅ 11**

---

## ❌ BROKEN / WRONG

| # | Finding | Evidence (path · date) |
|---|---|---|
| ❌1 | **The schema body never took in R3 amendments 1–3, yet the template says the schema wins.** Schema §2/§3 still has: tensions *optional*, no "Recent thesis pivot" line, the forward section named **WATCH**, NEXT DECISION "What would change my view". The template applies all three, and its header says the schema is "CANONICAL — wins over this template on any disagreement". So the canonical file overrules the correct one. | `templates/NEXUS_BRIEF_SCHEMA.md` §2 ("Cross-agent tensions known to me: <optional …>"; "## WATCH (next 2-4 weeks)"), §3.2 ("is optional but high-value"), §3.5, §4.3 table · versus cold decision rows 11/12/13 in `archive/2026-08-28_BRIEF_SCHEMA_decision-log_and_review-history.md` L26–28 ("REQUIRED (not optional)", "WATCH → FORWARD CATALYSTS rename") · template amendments 1–3. |
| ❌2 | **The schema says the §4.4 pin-token ruling "stays HOT and live", but it exists only in the cold file.** Hot §4.4 has no canonical token, no "a pointer is not a pin" rule and no `STATUS commit: NONE (reason)`. Effect on disk: only **3 of 29** briefs use the canonical token (BROCK, LABOR, OTTO), and pins that point instead of giving a hash are still in use: ORACLE "see `git log -1 -- …`", SHADE "same commit as this fold", CORAL "rides the same commit" (the CORAL claim is false at git: brief c81370260 23:01:24, STATUS fab5ea780 23:03:02). | Schema L294 "The §4.4 companion-defect ruling stays HOT and live" · ruling text only at cold archive L69–89 (§8 "RULED … Canonical token: `STATUS commit: \`<hash>\``") · header greps 2026-10-24. |
| ❌3 | **The map's `order` table says "Read the state HERE", but it shows the 2026-09-07 measurement.** The ★10/23 layer itself says the 10/19 cold measurement governs. Disk on 10/24: **A12 15 · pre-A12 6 · n/a 8 (29)**; the table shows 4 / 13 / 9 (26). It leaves out YURI, CYPHER and GIBBS. It still shows SAM as A12, but SAM went back to the old order (VIEW L5, CROSS-DOMAIN L25, brief 10/20). It still shows VIOLET and OSPREY as having no CROSS-DOMAIN, but both are now A12. HENRY has moved from pre-A12 to n/a. | `BRIEFS_MAP.md` §"`order` CONFORMANCE" ("Measured 2026-09-07 ~13:5x ET") · ★10/23 line "A12 order not re-measured this pass (the 10/19 measurement … stands)" · `archive/BRIEFS_MAP_COLD_2026-10-23.md` L17 · `grep -b` offsets 10/24. |
| ❌4 | **The template's worked example (SAM) breaks amendment 12.** It is the reference brief the template sends writers to, and it puts VIEW and CALIBRATION above CROSS-DOMAIN. | `templates/NEXUS_BRIEF_TEMPLATE.md` L5 "Worked example … AGENTS/SAM/NEXUS_BRIEF.md" · SAM brief `## VIEW` byte 228, `## CROSS-DOMAIN` byte 3,751 (commit b613efeef 2026-10-20). |
| ❌5 | **The map calls YURI "Tier-2". ROSTER puts YURI in ACTIVE**, and the map restating tier membership is something the charter forbids. | `BRIEFS_MAP.md` ★9/29 "YURI … **Tier-2: read when the Russian-decision domain is live**" · `PROME/ROSTER.md` L37 "ACTIVE (34) … 33→34 at the 2026-09-19 YURI seat, WQ-267"; YURI absent from TIER-2 (7) L120–130. |
| ❌6 | **NEXUS's own instrument has words run together (glued), which breaks root Output Canon.** | `brief_fallback_log.tsv` 2026-10-19 rows: "FULL:3fresh-contextgpt-6.1-sol readers,all extant briefs includingHAWK", "5STATUScommitsbehind;10/16S2/funding delivered at owner,rawSTATUSconsumed", "rawSTATUS named rows plus committed9db84090f …". |
| ❌7 | **The LIQUID streak is miscounted.** The 10/23 row and the map say "6th consecutive pass". The log's own numbering (10/01 "3rd pass", 10/08 "4th consecutive") makes 10/14 the 5th, 10/19 the 6th and **10/23 the 7th**. | `brief_fallback_log.tsv` rows 10/01, 10/08, 10/23 · `BRIEFS_MAP.md` ★10/23 "6th consecutive pass" and "six consecutive passes (8/23 → 10/23)". |
| ❌8 | **The map's Legend overrides the schema and charter on trigger (a).** Legend 🟡 PIN-STALE says "NOT a (a) trigger if content is fresh". Schema §4.4 and charter BOOT 6 say "(a) is mechanical / always fires". This override exists only in the map. | `BRIEFS_MAP.md` §Legend · schema §4.4 "**(a) is mechanical / always fires.**" · `CLAUDE.md` BOOT 6 "Trigger (a) is mechanical / always fires". |

## ⚠️ STALE / INCOMPLETE / OWED

| # | Finding | Evidence |
|---|---|---|
| ⚠️1 | **Amendment 9 (COMPACT) has no spec in the hot schema.** The header names it, but the form is defined only in cold decision row 19 and §7. The template carries one comment line and no skeleton. **8 briefs have no `## CROSS-DOMAIN`:** AEOLUS, BOND, HENRY, LIQUID, MIDAS, ORACLE, SHADE, WAL. Three of those (HENRY, LIQUID, BOND) are core credit/rates chain desks, not the "utility/single-seam (WATT/MIDAS/AEOLUS/VULCAN)" class amendment 9 blessed. LIQUID's sections ("Current judgment / Counterevidence and limits / Existing next tests") match neither variant. No map cell tracks FORM (full vs compact vs neither); `n/a` hides it. | Schema L6 vs cold L34/L48 · LIQUID brief L11/21/29 · HENRY 2,171 B with no `##` sections · BOND has a single `#` header. |
| ⚠️2 | **The A12 rollout trigger (§4.1-R part 1, "reorder at next re-pin") is not firing.** BROCK, CORAL, MARCO, RED and ZHAO are still pre-A12 after many folds since 9/07, and SAM went back to the old order. Every pre-A12 CROSS-DOMAIN offset is ≤ 15,823 B (MARCO), far below the 54,250 B cap, so §4.1-R part 3 owes no packet. By the schema's own definition, though, A12 has been "RATIFIED-NOT-ROLLED-OUT" for 53 days. | Offsets 10/24: BROCK 5,276 · CORAL 8,309 · MARCO 15,823 · RED 7,713 · SAM 3,751 · ZHAO 13,310. |
| ⚠️3 | **Pin coverage is lower than "UNPINNED 4" suggests.** A hash appears in the header of **12 of 29 (41%)**. Another 13 pass as OK-SAME-COMMIT without any hash. That is valid for amendment 11, but it is not pin coverage. | Header scan with the checker's own `PIN_RE`: hash = BROCK CARL CYPHER FALCON GIBBS LABOR MARCO OTTO REGINALD SAM VULCAN WAL; no hash = AEOLUS BOND BRENT CORAL HAWK HENRY HOMER LIQUID MIDAS ORACLE OSPREY RED SHADE VIOLET WATT YURI ZHAO. |
| ⚠️4 | **Rollup #5 left out the pin coverage + class figure that #4 made a standing requirement.** It is owed in #6. | `brief_health.md` #4 §3 "every future rollup reports PIN COVERAGE + CLASS beside the brief-gap count" · #5 gives only a partial caveat. |
| ⚠️5 | **Briefs stale against STATUS (>1 commit or >7 days):** **BROCK** is 5 STATUS commits and 8 days behind (brief 10/15 16:59, STATUS 10/23 17:05, STALE-PIN). **LIQUID** is 4 commits behind (brief 10/21 22:18, STATUS commits 10/22 19:41, 10/23 22:06, 10/23 22:27 and **10/24 12:34**). That is a late mover after NEXUS's 10/23 pass: the fallback row cites HEAD c121a9eec, and HEAD is now 0423042e9. BOND and CORAL are 1 commit behind (within tolerance). | `git log` 10/24 · pin check output. |
| ⚠️6 | **Readings to watch in rollup #6.** `uncertainty` has **0 rows in the log's whole life** (6/07 → 10/23). `convergence` fell from 7 (#5 window) to 1 after digest readers took over. Direct owner-artifact reads are not logged (charter read-2 ⚠️18/⚠️71): on 10/23 NEXUS read 8 owners directly (LIQUID BOND BROCK HENRY RED REGINALD TERRY PROME) and logged 3. A 0 `brief-gap` may be structural, not a sign of health. | `brief_fallback_log.tsv` · `BRIEFS_MAP.md` ★10/23 read method. |
| ⚠️7 | **The agent token on digest rows has drifted:** FLEET ×4, ALL ×1 (10/19), DIGEST ×1 (10/23). Any tally keyed on the agent column has to normalise these. | `brief_fallback_log.tsv`. |
| ⚠️8 | **The schema is at 32,443 B = 99.7% of the 32,550 B budget.** Fixing ❌1, ❌2 or ⚠️1 will push it over, so it needs a cold rotation first. Candidates: §5 historical proposal, §4.2 pilot text, the §4.1-R "state at adoption" paragraph. Nobody reads it whole today (READS.tsv L502: REGINALD `scoped`), so this is not a current breach. | `wc -c` · `PROME/registry/READS.tsv` L502. |
| ⚠️9 | **A stale open item:** "VIOLET and OSPREY carry `## VIEW` with no `## CROSS-DOMAIN` … owed to a later pass". It is still printed in the schema and the map, but both briefs now carry CROSS-DOMAIN first. | Schema L160 · map `order` block · VIOLET CD 637 < VIEW 3,270; OSPREY CD 10,513 < VIEW 15,854. |
| ⚠️10 | **Pointers inside the schema have gone stale.** §4.5 says "see the §6 strike below", but §6 is cold. The cold archive's header still says "Bytes: 20,074 / crc32 3f13bf74", but the file is 24,252 B (crc 0xe49961e2) since the §A12 append; the header describes only the 8/28 payload and is not labelled that way. | Schema §4.5 · archive L3. |
| ⚠️11 | **The template's stamp uses the banned form** "As of: YYYY-MM-DD ~HH:MM ET". The charter Stamp rule bans `~HH:Mx` on graded records, and schema §2 uses "HH:MM". The template also omits the fail-loud `STATUS commit: NONE (reason)` and the "a pointer is not a pin" line, which is the gap behind ❌2. | Template L60 · `CLAUDE.md` §Stamp rule. |
| ⚠️12 | **Live rules that exist only in the map or brief_health:** (i) Legend MISSING → "log cause=stale", which the 9/29 WALTER row applied "per legend", while the charter defines `stale` only as trigger (a). (ii) The 10/8 PM schema-owner ruling "UNPINNED/pointer pins = §4.1 conformance gap owed at next fold" (now cold-map L27 + ★9/29 carry line). (iii) The A11 read-time carve-out "same-day pin behind HEAD = A11 case, not stale" (`brief_health.md` #4 §5.3). (iv) The Legend PIN-STALE override (❌8). All of these belong in schema §4.4 or the charter BOOT 6. Check whether §4.6's cap treats that as a repair or an amendment. | Paths as cited. |
| ⚠️13 | **A history line in the map reads as live and is wrong now:** "Remaining brief-less: WALTER, OZK, **SHADE** (by design)", but SHADE has had a brief since 8/03. Its dormant list includes CRUISE and FERT (both ACTIVE per ROSTER L109–110) and ATHENA (ARCHIVE SOURCE, L151). | `BRIEFS_MAP.md` ★CENSUS block (7/31 vintage) · ROSTER. |
| ⚠️14 | **The map writes counts and times in forms its own rules ban.** ★10/23 writes "census on disk = 29" and "28 briefs" despite KILL-2 ("the file carries the command, not the number"); this is acceptable as a dated observation, but it is the pattern KILL-2 retired. It also carries `~x` stamps ("21:2x ET") that the Stamp rule bans. | `BRIEFS_MAP.md` ★10/23. |
| ⚠️15 | **Digest-reader count was below the charter once:** BOOT 6 says three readers, but the 10/08 pass ran two. | Charter BOOT 6 · log row 2026-10-08 "two fresh-context Opus digest readers". |

## ✅ WORKING

| # | Finding | Evidence |
|---|---|---|
| ✅1 | **The cap statement agrees across surfaces.** The schema header "LOCKED (R3 + amendments 7, 9, 10, 11, 12) · AMENDMENT CAP IN FORCE (12 of 12)" matches the charter's `templates/` row ("12 of 12 (❌77, verified at the schema header 9/29)"), and the map contradicts neither. Amendments 7 (Expected-by column, §2), 10 and 11 (§4.1, with the SELF-RULED block), 12 (§2 order + §4.1) and the §4.6 cap are all written in the hot body. | Schema L1, L6, §2, §4.1, §4.6 · `CLAUDE.md` WHAT YOU OWN. |
| ✅2 | **The rollup cadence is being kept.** #5 shipped 9/29. #6 is on **DOCKET L555 2026-10-27** (a Tuesday, riding the L554 wake) and is mirrored in NEXUS STATUS L101 and LAST_COMPLETION ("9a not due (L555 10/27)"). That is a 28-day cadence, not yet due. | `PROME/DOCKET.tsv` physical L555 · `brief_health.md` #5. |
| ✅3 | **No brief is over budget or cap.** The largest is BRENT at 23,010 B (70.7%), then ZHAO 22,585, MARCO 22,213, OSPREY 21,495. These match the map's ★10/23 to the byte. | `wc -c` 10/24. |
| ✅4 | **The census matches.** 29 briefs on disk equals the map's ★10/23 figure. CYPHER (9,067 B, pin b562466d3) and GIBBS (3,605 B, pin 6d1d9df51) match. | `ls` 10/24. |
| ✅5 | **The pin check runs and blocks correctly** (rc 1 on BROCK STALE-PIN). Its output is identical to the map's 10/23 transcription: OK-PINNED 11 · OK-SAME-COMMIT 13 · STALE-PIN 1 · UNPINNED 4 (BOND CORAL LIQUID WATT). | Run 10/24. |
| ✅6 | **Every pointer checked exists:** `research/2026-10-23_full_pass/DIGEST_R1–3.md` + `RECORD.md`, the BOND pre-cap snapshot, the schema cold archive, the BRENT 6/07 fallback spec, `DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md`, `AGENTS/SELF_RULINGS.tsv`, both scripts and the SAM brief. | `test -e`. |
| ✅7 | **Rollup #5's arithmetic matches the log:** 17 non-digest rows after 8/28 = stale 9 · convergence 7 · brief-gap 1. | Python tally. |
| ✅8 | **The template's order and token follow the schema:** CROSS-DOMAIN first (A12), the amendment list matches the ratified set, the 32,550 B budget language is right, and it uses the canonical `STATUS commit: <short-hash>`. | Template. |
| ✅9 | **The log is well-formed:** 88 lines, 0 malformed rows, LF line endings, and its header defines the cause set including `digest`. | `cat -A`. |
| ✅10 | **The 10/8 PM strike of the A10 timestamp sentence held at the owners.** No "commit timestamp" text remains in the CARL, FALCON, LABOR, MARCO, OTTO or ZHAO briefs. | grep 10/24. |
| ✅11 | **BOOT 6 is being followed in practice:** HAWK was left out on 10/23 (no cross-war question), the 10/19 model override was recorded, the digest row was logged, and the load-bearing owners were read directly. | Map ★10/23 · log. |

---

## Rollup #6 input (Q2): cause mix, window = rows dated AFTER 2026-09-29 (10/01 → 10/23)

Passes in window: 10/01 (×2: digest + Will-asked direct), 10/08, 10/14, 10/19 (FULL + FILE AUDIT + four-item), 10/23. Digest rows (6) are excluded from rates.

| Desk | stale | convergence | uncertainty | brief-gap | Read per 9a |
|---|---:|---:|---:|---:|---|
| LIQUID | **7** | 0 | 0 | 0 | 🔴 chronic freshness: stale in every dated pass (10/01, 10/08, 10/14, 10/19 ×3, 10/23); 7th consecutive pass incl. 9/17 and 9/29 |
| BROCK | **4** | 1 | 0 | 0 | 🔴 freshness: stale-or-drilled in every pass; STALE-PIN 10/24 |
| BOND | 1 | 0 | 0 | 0 | freshness (desk dark since 10/20) |
| CORAL | 1 | 0 | 0 | 0 | freshness (10/08) |
| MIDAS | 1 | 0 | 0 | 0 | freshness (10/08) |
| RED | 1 | 0 | 0 | 0 | freshness (10/01) |
| YURI | 1 | 0 | 0 | 0 | freshness (10/08) |
| **Total (17)** | **16** | **1** | **0** | **0** | brief-gap rate **0/17**. LIQUID + BROCK = 11/16 stale (69%) |
| digest rows | — | — | — | — | 6 (FLEET 4 · ALL 1 · DIGEST 1) |

Inclusive of the 9/29 rows (already counted in #5): n=36 → stale 23 · convergence 6 · digest 7 · brief-gap 0 · uncertainty 0.
**Required alongside the brief-gap count (rollup #4 standing rule), measured 10/24:** pin coverage (hash in header) 12/29 = 41% · A11-satisfied (OK-PINNED + OK-SAME-COMMIT) 24/29 · STALE-PIN 1 (BROCK) · UNPINNED 4 · canonical token 3/29.
Read: under 9a's rules, the two high-`stale` owners (LIQUID, BROCK) get a freshness-discipline flag, not a brief-quality verdict. No fix-or-drop conversation is warranted (brief-gap 0). Before calling the standard healthy, though, see ⚠️6: the instrument may no longer be able to emit `brief-gap` or `convergence`.

## Verdict
- **Works:** the cadence (#6 docketed for 10/27), the size budgets (no brief over 71%), the census (29 = 29) and the pin tool (output reproducible to the map's transcription).
- **Does not:** the canonical schema body is behind its own ratified amendments (R3 amendments 1–3, the §4.4 token ruling, and the amendment 9 COMPACT form all live only in cold files), and the template defers to it. The hot `order` table is 7 weeks stale and its worked example (SAM) has gone back to the old order.
- **Most valuable change:** a non-amendment repair of the hot schema. First rotate §5 and the pilot text cold to get under budget. Then write into §2/§3 the R3 amendments 1–3 as already ratified, and into §4.4 the canonical token / "pointer is not a pin" / `NONE (reason)` rule plus the A11 read-time carve-out, and drop the Legend override. Separately, replace the map's 9/07 `order` table with the regenerating command's current output, adding a FORM column (full / compact / neither).
