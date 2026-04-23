# OZK Domain Audit — March 25, 2026
**Auditor:** Reginald Subagent | **Audit date:** 2026-03-25 | **Earnings:** April 16 (22 days)
**Scope:** Full domain review — architecture, KB quality, thesis coherence, staleness, gaps, earnings readiness

---

## 1. Architecture Assessment

### Folder Structure

The domain has grown organically into a mature, well-differentiated structure. Core files are present and clearly scoped. The separation of concerns (THESIS = narrative, KB = data, STATUS = live dashboard, INDEX = cold-boot) is sound and consistently observed.

**Present and accounted for:**
- ✅ Core: INDEX, STATUS, THESIS, SCENARIOS, WEAKNESSES, EARNINGS_PREP, EXTERNAL_PROMPTS
- ✅ Deep dives: research/ (12 files, all populated)
- ✅ Geography: GEOGRAPHY/ (EXPOSURE_MAP, FL_PARADOX/, REGULATORY_DISTRICTS, STATUS)
- ✅ Life Sciences: LIFE_SCI/ (FINDINGS, STATUS, README)
- ✅ Workbook: KB.tsv + KB_INDEX.md
- ✅ Archive: 5 superseded files cleanly retired

**Undocumented folders — potential orphans:**

| Folder | Files | Referenced in INDEX? | Status |
|--------|-------|---------------------|--------|
| `INSIDERS/` | DEPARTURES.md, README.md, SELLING.md, STATUS.md, TIMELINE.md | ❌ NOT in INDEX.md | Orphan risk |
| `MARKET/` | CONTEXT.md, README.md, snapshots/, STATUS.md, TRADE_LOG.md | ❌ NOT in INDEX.md | Orphan risk |
| `PRIVATE_CREDIT/` | COUNTERPARTY_WATCH.md, NDFI_EXPOSURE.md, README.md, STATUS.md, TRANSMISSION.md | ❌ NOT in INDEX.md | Orphan risk |

Three entire sub-folders — INSIDERS/, MARKET/, and PRIVATE_CREDIT/ — exist and appear non-trivial (5 files each with README and STATUS) but are completely absent from INDEX.md. On a cold boot, an agent would never find them. These either need to be indexed or explicitly marked as deprecated.

PRIVATE_CREDIT/ is especially concerning: it covers NDFI exposure and counterparty watch (Affinius, Blue Owl) — directly thesis-relevant. The NDFI_SHADOW_CRE_ANALYSIS.md in research/ overlaps significantly. Unclear which is authoritative.

**Naming inconsistencies:**
- `INSIDERS/` folder vs `INSIDER` KB group vs `research/INSIDER_ACTIVITY_COMPILED.md` — three parallel structures covering the same domain
- `LIFE_SCI/` folder vs `LIFE_SCI` KB group — fine, but LIFE_SCI/FINDINGS.md and the LIFE_SCI KB group cover overlapping ground without a clear primary
- INDEX.md's "File Map" is stale: workbook section still references "136-row" KB, "16-group" KB_INDEX, which is wrong (159 rows, 17 groups per KB_INDEX.md; the exec count shows 16 distinct group tags in KB.tsv — discrepancy addressed below)

**Row count inconsistency — INDEX.md is not self-consistent:**
- INDEX.md header: "KB at 136 rows" (last session note, clearly stale)
- INDEX.md boot table: "146-row" (also stale)
- STATUS.md header: "141 rows, 16 groups"
- KB_INDEX.md: "159 rows, 17 groups" (claims 17 but only 16 distinct group tags exist in KB.tsv)
- Actual KB.tsv: 159 data rows (160 lines - 1 header)

**Verdict:** The discrepancy isn't data corruption — it's that INDEX.md and STATUS.md weren't updated after the last session's KB growth (from 141 to 159 rows via Prompts 16 and 20). The domain grew 13% in the final session without a cleanup pass on the navigation files. KB_INDEX.md is the most current. INDEX.md urgently needs its row counts corrected.

**Dead/redundant files:**
- `research/README.md` — presumably exists but not mentioned anywhere; likely empty scaffolding
- The "GAP" KB group (rows 056-060, 6 entries) points to `GAP_ANALYSIS_REPORT.md` — but this file is in `archive/` and not directly accessible per INDEX.md. Cold-boot agent following KB_INDEX would hit a dead link.

---

## 2. KB Quality

**Distribution (actual counts from KB.tsv):**

| Group | Count | Assessment |
|-------|-------|------------|
| LIFE_SCI | 21 | ✅ Well-populated — largest group, justified given $3.1B exposure |
| MATURITY_WALL | 20 | ✅ Core thesis mechanism, appropriately large |
| BULL_COUNTER | 17 | ✅ Good — adversarial coverage is a strength |
| GEOGRAPHY | 13 | ✅ Strong — 58 MSAs mapped |
| CRE_CONCENTRATION | 12 | ✅ Sufficient |
| FL_PARADOX | 12 | ✅ 4-model convergence, thesis-stabilizing |
| DISTRESSED_LOANS | 9 | 🟡 Thin given the named loan count (IQHQ + 6 others). Should be ~12-15 |
| MGMT_CREDIBILITY | 9 | ✅ Adequate |
| EXTEND_PRETEND | 8 | ✅ Core mechanism well-covered |
| SHADOW_CRE | 7 | ✅ Sufficient for the argument |
| ACL_THINNING | 7 | 🟡 Core thesis layer but thinnest of the three waves relative to importance |
| GAP | 6 | ⚠️ Points to archived file — group may be vestigial |
| CAPITAL_LIQUIDITY | 6 | ✅ Adequate — C3 rebuttal handles the depth |
| PEER_COMP | 4 | 🔴 Critically thin — only 4 rows for the most persuasive single data point (5.4x NCO) |
| MEMO_ITEM_3 | 4 | 🟡 Thin for a novel metric that's a significant thesis differentiator |
| INSIDER | 4 | 🟡 Thin but newly added (Prompt 16); adequate for sentiment signal |
| **TOTAL** | **159** | **16 distinct groups (KB_INDEX.md claims 17 — one group missing or mislabeled)** |

**Group count discrepancy:** KB_INDEX.md header says 17 groups, but the actual KB.tsv contains only 16 distinct group tags. The navigator itself lists 16 groups across its tables. This is a documentation error in the header — someone incremented a counter without adding a group.

**Source quality:**
- Tier A (primary filings — FDIC API, FFIEC Call Report, 10-K): ~45% of rows. Strong.
- Tier B (multi-LLM synthesis with source citation): ~40% of rows. Reliable for structural claims; weaker for point-in-time prices.
- Tier C (single-model, secondary): ~15% of rows. Flagged with ⚠️ in THESIS.md where they appear.

**Known unverified rows (explicitly flagged in THESIS.md):**
- KB-OZK-061: $13.8B 2022 origination total — "UNVERIFIED from primary data." This is the maturity wall's foundational assumption. Critical gap.
- KB-OZK-028: IQHQ 97% vacancy — "⚠️ Oct 2024, may be stale"
- KB-OZK-062: DBRS "63% of CCC-C pool" — "⚠️ UNSOURCED"

**Duplicates:** No exact duplicates detected from structure, but SHADOW_CRE and MEMO_ITEM_3 overlap significantly (MI3 is a subset of shadow CRE). Rows 018-020 (MEMO_ITEM_3) could be absorbed into SHADOW_CRE or vice versa. The split serves pedagogical clarity in KB_INDEX but creates maintenance overhead.

**Status field usage:** 157 rows ACTIVE, 2 CORRECTED, 0 STALE. The Stale_By dates (mostly 2026-04-30) are future-dated — meaning the stale tracking system hasn't been triggered yet. This is structurally correct but creates a false sense of cleanliness: several rows contain April 2024 data (e.g., KB-028 vacancy) that is substantively stale even without the status flag.

---

## 3. Thesis Coherence

### Three-Wave Framework

The framework is internally consistent and well-documented. The causal chain (interest reserve depletion → maturity wall → noncurrent step-up → forced provision catch-up → EPS compression → multiple re-rating) is mechanically sound and supported by primary data.

**Wave 1 (Now → Apr 16): KB support — STRONG**
- Charge-off acceleration: KB-003 (FY 1.18%), Q4 NCO $98.3M (8x YoY)
- Reserve melting: KB-001/002 (ACL collapsed $56.6M in Q4 while noncurrent doubled)
- Named catalysts live: Sterling Bay Lincoln Yards seized (KB-094), Pacific Center sold (KB-095)
- Extend-and-pretend mechanism: KB-096 through KB-104 (590 mods, 98% gap, 59% re-default)
- ✅ Evidence density is high for Wave 1. The weakest element is the exact Q1 charge-off estimate for the $265M SVP loan sale.

**Wave 2 (Q2 2026, NY pipeline): KB support — MODERATE**
- NY district 30-89 delinquency: 0.41% (KB referenced in EARNINGS_PREP, confirmed via FDIC QBP)
- NY pipeline concentration in "other nonfarm nonresidential" stated but not directly enumerated at loan level
- **Gap:** No named NY loans in DISTRESSED_LOANS group. The NY pipeline conversion risk is regional/aggregate, not loan-specific. This is the thesis's most abstract wave — no named borrower, no specific maturity date. Analytically sound but would be harder to prove right at Apr 16.

**Wave 3 (IQHQ, ~Aug 2028): KB support — STRONG on diagnosis, WEAK on timing**
- RaDD capital stack analysis is the domain's best work: KB-137 through KB-141, plus LIFE_SCI/STATUS.md (21 KB rows, $1.23B total debt, 15% PIK mezz accruing $76M phantom)
- The extension to Aug 2028 explicitly moved this outside the current options window. WEAKNESSES.md correctly identifies this (C5). THESIS.md notes it. But SCENARIOS.md was drafted when maturity was Aug 2026 — language may still imply a near-term catalyst
- ✅ IQHQ is correctly repositioned as "background risk + worst-case anchor" rather than Q2 catalyst. EARNINGS_PREP.md handles this appropriately.

**MI3 Discovery (Memo Item 3 / Hidden CRE):**
- This is the domain's most differentiated insight — not in Temple 8, not in sellside
- KB-018 through KB-020 + KB-087 support it, plus research/C1_RECLASSIFICATION_REBUTTAL.md
- The logical chain (C&I grew 153%, ~46% of construction decline migrated to C&I, CEO confirmed reclassification mechanic) is solid
- **Gap:** Competitor comparison is thin. Only one peer (Metropolitan, failed) has a Memo Item 3 ratio cited. Prompt #8 (Metropolitan failure comparison) would directly strengthen this.

**Logical gaps:**
1. **The $13.8B origination figure is load-bearing and unverified.** If 2022 origination was $10B or $8B, the maturity wall is meaningfully smaller. Prompt #18 exists for this but is in "Nice to Have."
2. **No direct evidence linking interest reserve depletion to specific loan-level defaults.** The mechanism is modeled (KB-088/089/090) but the chain from "reserves exhausted" → "sponsor can't pay" → "NPA classification" is inferential, not documented.
3. **Affinius/Blue Owl exit counterparty risk** (mentioned in SCENARIOS.md as mispricing factor #7) has no KB rows and no research file. PRIVATE_CREDIT/ likely covers this but is orphaned from the navigation system. Prompt #9 (Affinius bonds) remains undone.

---

## 4. Staleness

### Most Urgently Stale (Must Refresh Before Apr 16)

| Item | Current State | Staleness Risk | Action |
|------|--------------|----------------|--------|
| **Short interest** | "14-15%, undated" | Could be materially higher or lower. Squeeze risk calc depends on it. | Run Prompt #5 now (30 min). FINRA REGSHO or Ortex. |
| **Stock price in SCENARIOS.md** | "$42-44 STALE — now ~$49" | Scenario targets, EV table, put EV calculations all use wrong anchor price. Options analysis numbers are wrong. | Recalculate EV table and put EV with $49 current price before Apr 16. |
| **Jefferies Q1 (WAL read-through)** | 3x deferred, not pulled | This is a confirmed peer read-through, 22 days from earnings. Deferred too long. | Pull immediately — 30 min max. |
| **IQHQ vacancy (KB-028)** | Oct 2024 sourced, marked stale | LIFE_SCI/STATUS.md says "3.3% leased" (Jan 2025 via Prompt 15) so the old 97% vacant is now superseded, but KB-028 itself isn't marked CORRECTED | Mark KB-028 status SUPERSEDED, link to KB-137 |
| **8-K EDGAR monitoring** | CIK 0001569650 — "not set up" per STATUS.md | Any pre-announcement in next 22 days could materially affect position | Set up alert immediately — this is zero-cost risk management |
| **SVP loan sale Q1 impact** | "$265M sold to SVP Jan 2026, loss unknown" | The Q1 charge-off impact of this sale is the single biggest unknown for April 16 earnings | Research immediately — SVP is Strategic Value Partners, check any press releases or FDIC data |

### Stale But Manageable

| Item | Current State | Note |
|------|--------------|-------|
| DBRS "63% of CCC-C" claim (KB-062) | UNSOURCED | Nice to verify but not load-bearing |
| $13.8B 2022 origination (KB-061) | UNVERIFIED | Prompt #18 exists but classified "nice to have" — should be Medium Priority |
| Bioterra ($202M) status | "Vacant, facing distress" | No KB row update since initial entry. Any development? |
| IQHQ capital stack detail | Jan 2025 HR Ratings cited | KB-139 says source is secondary — HR Ratings full report not pulled |

---

## 5. Research Gaps

### Remaining Prompts (#8, #9, #10, #13, #19) — Priority Assessment

| Prompt | Topic | Current Priority | Audit Assessment | Earnings Relevance |
|--------|-------|-----------------|-----------------|-------------------|
| **#8** | Metropolitan failure comparison | Medium | ✅ RIGHT PRIORITY — Memo Item 3 is thesis differentiator; direct failure analog strengthens it significantly | High — MI3 is an Apr 16 earnings call question angle |
| **#9** | Affinius bonds | Medium | ✅ RIGHT PRIORITY — Affinius is OZK's most frequent co-lender. If bonds at 81¢ / Oct 2026 deadline fail, construction maturity wall worsens mechanically. Zero KB rows currently. | High — exit counterparty risk |
| **#10** | Sell-side consensus | Medium | 🟡 LOWER PRIORITY THAN MARKED — useful context but doesn't change thesis. Citi Sell is already known. | Low — nice context |
| **#13** | Peer 2022 vintage comparison | Medium | ✅ RIGHT PRIORITY — either confirms systemic maturity wall (strengthens macro framing) or confirms OZK is an outlier (strengthens idiosyncratic bad underwriting argument). Win either way. | High — directly addresses Apr 16 management "one-off" defense |
| **#19** | Metro market conditions by MSA | Medium | 🟡 PARTIALLY COVERED — Prompt 20 (life sci) already covers SD, Boston, Bay Area. Prompt 5/Geography covers FL. What's genuinely missing is office-specific conditions in NY, Chicago, Atlanta, Seattle. | Medium — background |

**Prompts #8 and #13 should be elevated to HIGH PRIORITY.** They directly address the two lines of defense management will use on Apr 16: "Metropolitan is nothing like us" (#8 tests this) and "our 2022 vintage is unique, not a peer phenomenon" (#13 tests this).

**Missing research not in any prompt:**
1. **SVP loan sale charge-off** — the $265M Pacific Center sold to Strategic Value Partners in Jan 2026. Was this at par (as management claims)? Any press release, FDIC data, or SVP filing could indicate actual loss. This is a Q1 specific charge-off unknown with direct Apr 16 impact.
2. **Buyback non-use** — Prompt #12 exists as "nice to have" but a bank that authorized a $200M buyback and used $460K is an extraordinary signal. Should be medium priority given earnings proximity.
3. **SCENARIOS.md price refresh** — not a research prompt but an analytical task. The entire scenario framework is anchored to a $42-44 price that's now $49. All put EV calculations are wrong.
4. **Options implied move** — Prompt #14 exists and is "nice to have" but with May puts 22 days from earnings, knowing the implied move and current IV is operationally important for position management.

---

## 6. Earnings Readiness

**EARNINGS_PREP.md overall rating: 🟡 GOOD BUT INCOMPLETE**

### Strengths
- Pre-earnings confirmed developments are solid (Lincoln Yards seizure, SVP sale)
- "What to Watch" list is comprehensive and well-prioritized — the 5 primary items are the right items
- Peer comparison framework (the 6-metric table) is ready to deploy
- RC-N noncurrent breakdown by loan type is the strongest pre-call data point — 75.2% in "other nonfarm nonresidential" is a devastating opener
- Red flags / green flags framing is useful for real-time call monitoring

### Missing / Weak
1. **No Q1 charge-off estimate range.** The prep document watches for whether charges accelerate or decelerate but gives no analytical estimate of what Q1 should be. Without a base estimate, any number is hard to contextualize in real time. At minimum: "Expected Q1 NCOs: $70-100M based on SVP sale + ongoing maturity wall, vs Q4's $98.3M gross."
2. **The SCENARIOS.md price mismatch flows into EARNINGS_PREP.** The put EV tables in SCENARIOS.md are anchored to $42-44. EARNINGS_PREP.md discusses positions but doesn't update the scenario math for the current $49 price. At $49, the Bear scenario ($30-37) is 25-33% down vs the $42-44 anchor's 10-15%. The put structure looks better at $49, not worse — but this hasn't been recalculated.
3. **No decision framework for position management on Apr 16.** The doc says what to watch but not what to do. What's the trigger to add? To trim? If the call is a "nothing burger" (no major charge-offs, management says things are fine), does the thesis still hold with the May puts at 22 days? This is the operational gap.
4. **Peer earnings timing is listed (ZION ~Apr 20, WAL ~Apr 21) but no peer watchlist.** What specific data points from WAL's call are most relevant to OZK's thesis? WAL has NY CRE exposure and a weak ACL coverage (~90% per KB-136). It's a natural read-through.
5. **Short interest is explicitly marked as undated** in both STATUS.md and EARNINGS_PREP.md's checklist. This remains undone three days from the audit window. Days-to-cover is directly relevant to position sizing guidance.

---

## 7. Recommendations — Top 5 Priorities Before Apr 16

### Priority 1: Fix SCENARIOS.md and EARNINGS_PREP.md with current price ($49)
**Why urgent:** All put EV calculations, scenario probability tables, and position sizing guidance are anchored to a price that's $7 wrong. The thesis case is actually stronger at $49 (more downside in bear case, higher intrinsic value if it breaks) but this hasn't been articulated. Operationally, a trader managing puts on Apr 16 needs correct numbers. This is a 2-hour analytical task, not a research task.

### Priority 2: Pull short interest (now — 30 minutes)
**Why urgent:** Status.md has flagged this as "MUST DO this week" three consecutive sessions. It keeps being deferred. Short interest affects position sizing, squeeze risk, and days-to-cover. At 14-15% SI undated, the squeeze risk calculation could be significantly wrong. The May puts (22 days to earnings) are particularly sensitive to squeeze dynamics. FINRA REGSHO is free and takes 10 minutes.

### Priority 3: Run Prompts #8 (Metropolitan) and #13 (Peer 2022 vintage) before Apr 10
**Why urgent:** These are the two analytical pillars that would be most persuasive to a skeptic on the Apr 16 call. If management characterizes Q1 charge-offs as "idiosyncratic" or "one-off," the peer vintage comparison (#13) is the immediate rebuttal. If they dismiss the Memo Item 3 concern, the Metropolitan failure comparison (#8) is the immediate counter. These aren't background research — they're live call ammunition. Six days is enough time.

### Priority 4: Set up EDGAR 8-K monitoring for CIK 0001569650
**Why urgent:** This is listed in every STATUS.md "MUST DO" and never gets done. A forced pre-announcement before Apr 16 (loan impairment disclosure, material event) would be the highest-value signal possible. Missing it because no alert was configured would be inexcusable. This takes 15 minutes on EDGAR email alert.

### Priority 5: Index INSIDERS/, MARKET/, and PRIVATE_CREDIT/ folders into INDEX.md
**Why urgent:** Three non-trivial folder trees exist completely outside the navigation system. PRIVATE_CREDIT/ covers Affinius and NDFI counterparties — directly relevant to the Affinius/Blue Owl exit risk discussed in SCENARIOS.md. On any cold boot, a future agent would work without this context. The TRADE_LOG.md in MARKET/ likely contains position history that doesn't appear in STATUS.md. Index these folders or explicitly deprecate them. Either action takes 30 minutes.

---

## Additional Flags

**Weak claim to watch:** The "95% of original 2021-2022 reserves mathematically exhausted" claim (KB-088/089) is modeled, not empirically verified. It's presented with high confidence in THESIS.md but it's an ANALYTICAL/ESTIMATE row, not EMPIRICAL. If OZK's Q1 call shows no construction deterioration and mentions "interest reserves remain adequate," this claim will be challenged. The model should be stress-tested against alternative assumptions (e.g., higher sponsor top-up rates).

**Temple 8 correction is handled well but creates risk:** THESIS.md explicitly corrects Temple 8's "ACL inversion" (-2bps) claim as a denominator error. This is intellectually rigorous. But it also means the domain's headline number (ACL 1.26% per OZK's own basis) is less dramatic than Temple 8's claimed 1.16%. If someone encounters Temple 8 first and then reads the domain files, the correction could create confusion about which numbers to use. A single "Canonical Numbers vs Temple 8 Claims" reconciliation table in EARNINGS_PREP.md would address this.

**Bull case probability may be understated:** SCENARIOS.md has Bull at 15%. At $49 (well above the $41 TBV), the market is implying the stock has embedded bull optionality the thesis is discounting. Wave 1 (Apr 16) needs to deliver a clear negative signal or the stock could grind higher. If Q1 charge-offs come in light (hypothetically $50-60M), the market may read it as "the worst is over." This outcome isn't fully stress-tested in the scenario analysis.

---

*Audit conducted: 2026-03-25 | Files read: 12 core + 3 supplementary | Next audit: post-Apr 16 earnings*
