# GATE BASIS SWEEP 02 — STRANGER B record (2026-10-08)

Started: Thu Oct 8 16:14 EDT 2026 (`date`). Grader: stranger, letter-only. Read perimeter: PROME/GATES.tsv header + 8 assigned rows; each row's definition_surface section (whole); each file named in the row's `source` column; public data.

Columns used: col 4 `condition`, col 8 `source`, col 11 `definition_surface` (header line 2 of GATES.tsv).

## §0 Verdicts

| Gate | Verdict | The one blocking (or most load-bearing) question |
|---|---|---|
| GATE-BRENT-COT-35B | **GRADED — JOINT NOT-SPENT** (as-of 9/29: shorts 129,436 ≥ 118,326; OI-share 6.8901% > 4.909%) | "Resolving vintage = FIRST PRINT" — a stranger fetching later cannot prove the row read is the first print (re-issue ledger out of reach). |
| GATE-FERT-G5 | **GRADED — NOT FIRED** (DTN 10/7: MAP $974, DAP $934) | Is the observation national, and is it DAP **OR** MAP? The pointed-to "full letter" says only "DAP/MAP > $1,000/ton"; the tie/geography clauses exist only in the summary cell. |
| GATE-CORAL-MSI-01 | **CANNOT-GRADE from the letter** ("owner-side canonical text = AGENTS/CORAL/STATUS.md OQ §A" — a STATUS.md, outside the perimeter). Summary cell alone → provisional: neither rule fires, leg stays 🟠 (10/8 stamp: Tampa 7.17 · Punta Gorda 6.42 · North Port 6.32 · Cape Coral 5.91 · Lakeland 6.12) | Which Parcl pages/series, and what counts as a "reading" when pages update daily (verdict depends on the grader's pull cadence)? |
| GATE-TERRY-ROLL70-EXIT | **GRADED — NOT FIRED, 0-of-3** (10/7 close $74.35; 10/8 $75.50 provisional) | Consecutiveness/reset clause (d) is "PENDING REGINALD CONCURRENCE" on the letter's face; "guard section" names no heading. |
| GATE-BRK-R2 | **GRADED — (a) FIRED** on North Haven PIF LLC (43.8%, 9/18 SC TO-I/A) and OCIC (~30%, 10/2 8-K), both reproduced at EDGAR; **no new fire since 10/2; (b) NOT FIRED** | Does the gate re-fire per vehicle / per extra quarter, and does P1's membership RULE (which OTIC appears to meet) or its named LIST govern? |
| GATE-NEXUS-T12S-DFII10 | **GRADED (provisional, Treasury early copy) — NO BRANCH COMPLETED** through cell 10 (L = 2.85; edges 2.95/2.75; longest UP run 1); window open, 5 cells left | FRED governs "as first published" and FRED/ALFRED were unreachable; is a Treasury-only cell "published"? |
| GATE-TERRY-VLO-HELD-01 | **GRADED — A NOT FIRED, no notice** (10/8 ③ ESTIMATE ≈ $113.56–113.58); **B1 NOT FIRED**; B2 no 8-K | VWAP of which price over which bars — and my pull had no `expireDate`, which by the letter's identity rule would make the observation UNKNOWN. |
| GATE-HOMER-THESIS-KILL | **GRADED (interim) — no leg at kill count ⇒ 🔴 holds**; A1 unverified (MBA 403) | C1 "FC pre-sale inventory YoY": inventory COUNT or pre-sale RATE? |

No gate was judged NOT A PUBLISHED-SERIES GATE: all eight resolve on published observations, though CORAL (letter in STATUS), BRK-R2 (population judgment), VLO B1/B2 (scope judgment) and HOMER (HALF rule, cure-rate line) carry judgment calls inside them.


---
## §1.1 GATE-BRENT-COT-35B — GRADED: JOINT NOT-SPENT (as-of 2026-09-29 print)

**Letter location.** GATES col 4 says "Letter -> REGISTRY.tsv COT-FUEL-35B". definition_surface = `AGENTS/BRENT/workbook/REGISTRY.tsv COT-FUEL-35B` + the 8/14 register card. Read: REGISTRY.tsv row `COT-FUEL-35B` (whole row — it is at **file line 156**, not "row 123" as the definition_surface cell says) and the whole card `AGENTS/BRENT/setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md`. Source column also names `PROME/proposals/2026-08-12_rule-batch-RULED.md (35b)` (read whole) and `AGENTS/BRENT/STATUS.md rows 13-14` (**NOT read** — STATUS.md is outside my permitted perimeter; recorded as a limit, §3).

**Grading attempt (verbatim).** `date` 2026-10-08 16:15 EDT. `curl -A "Mozilla/5.0" https://www.cftc.gov/dea/newcot/f_disagg.txt` → 456,793 B; every row report_date 2026-09-29 (277 rows). Row `"WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE",260929,2026-09-29,067651,...`: field 8 (Open_Interest_All) = **1,878,576**; field 15 (M_Money_Positions_Short_All) = **129,436** (fields counted 1-indexed on comma split, name = field 1; this reproduces the card's stated 8/4 check method). OI-share = 129,436 ÷ 1,878,576 × 100 = **6.8901%**.
- Leg A: 129,436 ≥ 118,326 ⇒ **NOT-SPENT** (11,110 contracts above the NOT-SPENT floor).
- Leg B: 6.8901% > 4.909% ⇒ **NOT-SPENT** (letter gives only the SPENT side "≤4.909%"; I read the complement as NOT-SPENT — Leg B has no deadband).
- Both agree ⇒ **JOINT NOT-SPENT** ⇒ consequence: base-case sizing within cap. No print for as-of 2026-10-06 exists yet (posts Fri 10/9), so this is the latest gradeable vintage.

**Questions / guesses.**
1. **Field numbering basis** is not in the GATES cell or the registry row ("field 15 ÷ field 8") — 0- or 1-indexed? The card says "1-indexed"; I took that. A stranger with only the registry row has to guess; the guess is checkable only because field 15 lands on a plausible MM-short column.
2. **"Resolving vintage = FIRST PRINT carrying the as-of report_date."** I fetched 6 days after release. I cannot prove what I read is the first print rather than a re-issue — there is no first-print archive I can reach; the registry names a re-issue ledger (`workbook/COT_VINTAGES.tsv`) that is outside my perimeter. Grade is conditional on "no re-issue since 10/2".
3. **Leg B tie convention / precision**: "≤ 4.909%" — compared at full float precision or rounded to 3 dp? Undefined. Irrelevant today (6.89%), decisive on a ~4.909 print.
4. **Leg B NOT-SPENT side** is never stated; only "≤4.909% … GATING". I inferred ">4.909% = NOT-SPENT". The GATES cell's "'GATING' and 'BOTH agree or NO-VERDICT' are ONE rule" helps, but a literal reader could also read GATING as "Leg B is a precondition for SPENT only", in which case a Leg-B miss + Leg-A NOT-SPENT could be either NOT-SPENT or NO-VERDICT. Here both read NOT-SPENT, so no difference.
5. **Leg A rounding**: bands quoted as integers derived from a .5 base (registry shows round-half-up); shorts are integers so ties at the .5 are impossible — clean.
6. **4.909% provenance disagreement between surfaces**: the GATES cell says "⚠ NOT re-reproduced since 8/13; BRENT owes the reproduction"; the registry row (the letter) says "✅ REPRODUCED 2026-09-18 … = 4.9086%". The GATES summary is stale relative to its own pointed-to letter. I did not re-reproduce (not decisive today).
7. **Base 122,904.5 vs card's 122,904**: the card (a definition_surface) still tables the truncated 122,904; the registry row explains the .5. A reader of the card alone gets a base that does not reproduce the bar. Levels themselves agree on both surfaces.
8. **Source pointer `2026-08-12_rule-batch-RULED.md (35b)` resolves to NOTHING**: that file has rows 27, 32b, 33b, 36b, 40–48 — no row 35b. The ruling the card cites is actually in an inbox packet (`inbox/processed/2026-08-12_from-PROME_35b-successor-RULED…`) not named in the source column. Dangling citation.
9. **"REVERT: re-read every print, never a latch"** — clear. **"median_unit … bar -1.0, deadband ±0.5"** — clear given the registry.
10. Registry row says Socrata lags ("Grade off the RAW file, never Socrata") — I used the raw file; consistent.

---
## §1.2 GATE-FERT-G5 — GRADED: NOT FIRED (DTN article 2026-10-07, data "last week of September 2026")

**Letter location.** GATES col 4 says "FULL LETTER + base-rate table → definition_surface (registry letter archived 8/22)". definition_surface = `AGENTS/FERT/workbook/TRIGGERS.tsv (T4)` + `PROME/inbox/processed/2026-08-17_from-FERT_gate-proposals-base-rated-plus-three-asks.md`. Source adds `AGENTS/FERT/workbook/EXIT_PROTOCOL.md`. All three read whole (TRIGGERS: header + T4 row whole).

**What the pointed-to "full letter" actually says.** The packet §2 table row G5: "DTN retail **DAP/MAP > $1,000/ton** | DTN Progressive Farmer weekly article | … ✅ PROPOSE". That is the ENTIRE letter at the definition_surface. TRIGGERS T4 is a wake register row (cadence, instrument, consumption log) and carries no threshold text. EXIT_PROTOCOL.md §0 supplies "Print = one published observation … DTN = weekly article" and a missing-print rule, but does not mention G5's $1,000 level at all. **The geography clause and the tie clause ("strictly > $1,000 at DTN's whole-dollar precision — a $1,000 print does NOT fire") exist ONLY in the GATES summary cell** (marked "CLARIFIED 2026-10-01 … FERT's text verbatim"), i.e. the summary is MORE complete than the letter it points to. The "registry letter archived 8/22" is not in my perimeter and is not named by path.

**Grading attempt (verbatim).** `date` 2026-10-08 16:15 EDT. `curl -A "Mozilla/5.0 …" https://www.dtnpf.com/agriculture/web/ag/crops` → found slug `/article/2026/10/07/uan32-leads-fertilizer-prices-higher`; fetched it (184,282 B, first-party). Article "UAN32 Leads Fertilizer Prices Higher", DTN Retail Fertilizer Trends, 10/7/2026 4:50 AM CDT, Russ Quinn: "average retail price … tracked by DTN for the last week of September 2026 … DAP had an average price of **$934/ton**, MAP **$974/ton**". Test: DAP 934 > 1000? no. MAP 974 > 1000? no. ⇒ **NOT FIRED.** No newer DTN retail article exists on the crops index as of 16:15 ET 10/8 (next expected Wed 10/14). MAP is $26 (2.67%) below the line.

**Questions / guesses.**
1. **AND vs OR.** Definition surface says "DAP/MAP" (slash). GATES cell says "DAP OR MAP". I graded OR (both are under, so no difference today), but the letter-of-record is ambiguous between "either" and "both".
2. **Geography.** The article never uses the words "US national average"; it says "average retail price … tracked by DTN". I accepted it as the clarified "national average as printed", but a stranger cannot confirm from the article that this is national (DTN surveys ~300 retailers; the article does not state scope).
3. **Observation date.** Is the observation dated by the article date (10/7) or its data week ("last week of September")? Unstated. Matters for any "as-of" bookkeeping, not for today's verdict.
4. **One print fires, or persistence?** Neither the letter nor the cell states a count. I read one print > $1,000 as FIRE (no "sustained"); EXIT_PROTOCOL §0 says "sustained" is never used without a count, consistent with a single-print gate, but this is inference.
5. **Revision / re-statement**: DTN occasionally restates prior-week averages; no vintage rule (first print vs latest) is stated. Not decisive today.
6. **Is the gate a one-shot or re-armable?** Consequence "FERT adjudication … packet to PROME" — after a fire, does it re-arm? Unstated.
7. "Whole-dollar precision" tie rule is clear (from the cell only).
8. The "registration CONTEXT" Pink Sheet $/mt figures are explicitly not the instrument — clear, no confusion created.

---
## §1.3 GATE-CORAL-MSI-01 — CANNOT-GRADE from the letter (letter lives in a STATUS.md); summary cell alone gradeable → provisional "neither rule fires, leg stays 🟠"

**Letter location.** definition_surface = `AGENTS/CORAL/STATUS.md (owner-side canonical letter; this row is summary+pointer per PAT-006)`; the condition cell also says "owner-side canonical text = AGENTS/CORAL/STATUS.md OQ §A". Source = `AGENTS/CORAL/STATUS.md §5` + `PROME/inbox/processed/2026-08-23_to-PROME_MSI-leg-has-no-registered-stand-down-WILL-RULING-NEEDED.md`. **The canonical letter is in a STATUS.md, which my perimeter forbids — NOT read.** Read: the 8/23 packet (whole). The packet is the stand-down REQUEST (proposed "breadth <5-of-5 >6.0 on TWO consecutive readings ≥10 days apart ⇒ 🔴→🟠"); it is NOT the amended 9/28 letter, and it differs from it (packet: breadth-based stand-down; amended cell: SAME-metro < 5.90 stand-down, band 5.90–6.00). So the only non-STATUS surface I can reach carries a superseded rule.

**Blocking element:** "owner-side canonical text = AGENTS/CORAL/STATUS.md OQ §A" — the letter is housed in a surface a stranger is barred from (and that, by its nature, rotates).

**Provisional grade from the GATES summary cell alone (verbatim attempt).** `date` 2026-10-08 16:16 EDT. Fetched `https://parcllabs.com/research/markets/fl/{tampa,punta-gorda,north-port,cape-coral,lakeland}/metro` (URL slugs GUESSED by me — the letter names no URL/ID; all redirected to www.parcllabs.com, HTTP 200). Each page: `Updated: 10/8/2026` (ONE stamp across all five ⇒ a valid READING per the cell). Page titles: Tampa **7.17** · Punta Gorda **6.42** · North Port **6.32** · Cape Coral **5.91** · Lakeland **6.12**.
- Re-fire test (all five > 6.00): 4 of 5; Cape Coral 5.91 ≤ 6.00 ⇒ NOT qualifying ⇒ "a FAILING reading resets to zero" ⇒ re-fire pair 0 of 2.
- Stand-down test: only meaningful from 🔴; state cell says leg is 🟠 since 9/13 ⇒ N/A. (No metro < 5.90 anyway; Cape Coral is in the 5.90–6.00 policy buffer.)
- ⇒ **Neither rule fires; leg stays 🟠.** This is the same page stamp as the owner's 10/8 reading quoted in last_checked, so per the cell "a repeat pull on the same stamp = the same reading" — I reproduced it, I did not add a reading.

**Questions / guesses.**
1. **Which pages / which identifiers?** "one pull of all five pages" — no URL, Parcl market id, or MSA code given. Parcl's own homepage lists FL markets as "Fort Myers", "Sarasota", "Lakeland", "Tampa" (MSA ids 2899822, 2900192, 2900041, …) and has NO "Cape Coral", "North Port" or "Punta Gorda" entries there; I found those only by guessing slugs. Are "Cape Coral" = Parcl "Fort Myers" (Cape Coral–Fort Myers MSA) and "North Port" = "Sarasota" (North Port–Sarasota–Bradenton MSA)? Possibly the same geographies under two names, possibly not. I did not check whether the Fort Myers/Sarasota map entries carry the same values.
2. **Which MSI series?** Parcl publishes a headline MSI plus sub-indices (single family, new construction, price bands — the national map shows 5.78 / 6.04 / 4.90). The letter says "Parcl Motivated Seller Index (0–10)" without property type. I used the page-title headline number.
3. **Precision**: "to the hundredth" — I used the 2-dp title value; whether a hidden 3rd decimal exists (and whether 6.004 is "> 6.00") is not addressed.
4. **What is a "reading" when the page updates daily?** Parcl says "updated daily". The cell defines a reading by page stamp, so any day can produce a reading. Then "two consecutive readings with stamps ≥10 days apart" + "an intervening qualifying reading preserves the FIRST qualifying reading's clock" + "a FAILING reading resets" means **the verdict depends on how often the grader pulls**: a daily puller can see a failing day that a weekly puller never sees. The cadence ("weekly", per review_by) is in the review cell, not the letter. Unresolved.
5. **Starting state** is not in the letter; I had to take 🟠 from the state cell to know which rule applies.
6. **Storm rule S1–S4** (state cell: "pre-registered 10/8 … CORAL STATUS OQ §A") changes how readings 10/10–10/23 are graded ("graded as written + FLAGGED"), but its text is only in STATUS.md. A stranger grading next week could not apply it. Today (≤10/9) = normal per the cell's paraphrase.
7. The packet (8/23) proposed "<5-of-5 breadth" stand-down; the cell's amended letter uses "SAME metro <5.90". Two different rules on reachable surfaces; I followed the cell (later-dated, Will-ruled 9/28 per its text) — but that is me choosing between texts.
8. "10 days apart": calendar days, stamp-to-stamp, inclusive? Unstated (e.g., 10/8 → 10/18 = 10 days: qualifies with "≥").

---
## §1.4 GATE-TERRY-ROLL70-EXIT — GRADED: NOT FIRED, run 0-of-3 through the 10/7 settled close (10/8 close $75.50 provisional)

**Letter location.** GATES cell: "FULL LETTER → definition_surface (ROLL70 card, guard section) — this cell is summary + pointer only". definition_surface = `AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md`. **There is no section titled "guard" in the card.** Headings are §0–§11 plus dated OWNER TOUCH blocks. Candidates: §5c table row ① ("Guard — REG-T-02 EXIT ≥ $81.90 ×3 official closes") and §6 Risk/scoring bullet "Invalidation" (which carries the BASIS clauses (a)–(d), written 2026-09-24). I read §5c, §6/6a, §7 and the 9/24 + 9/28 OWNER TOUCH/RECORD blocks whole, and grade on §6 "Invalidation" as the only text with a basis. Source also names `AGENTS/REGINALD/registry/NOTES.md §REG-T-02 STATE RULING` — **there are TWO subsections with that title (2026-09-01 and 2026-08-20)**; I read the whole `REG-T-02` section (both rulings + both EXIT GRADE blocks). And `PROME/proposals/2026-09-01_wq-batch-RULED.md` row 143 (read: "guard = REG-T-02 EXIT (WAL ≥81.90 ×3 closes ⇒ close the roll)").

**Letter as I read it (§6 Invalidation):** WAL ≥ $81.90 on 3 consecutive official closes; (a) value = WAL regular-session close, UNADJUSTED, per share; (b) $81.90 exactly qualifies; (c) a close counts only once its daily-bar volume is unchanged across two pulls from two different tools after 16:00 ET; (d) **"⏳ PENDING REGINALD CONCURRENCE … until REGINALD answers, (d) is TERRY's proposed letter, not a joint one"**: consecutive regular sessions, holiday skipped, any settled close < $81.90 resets to 0, missing vendor bar ≠ holiday (labelled substitute or UNKNOWN; UNKNOWN does not advance and the run cannot complete through it).

**Grading attempt (verbatim).** `date` 2026-10-08 16:18:02 EDT. `curl https://query1.finance.yahoo.com/v8/finance/chart/WAL?range=1mo&interval=1d`: closes 9/30 75.10 · 10/1 75.70 · 10/2 76.38 · 10/5 76.02 · 10/6 76.09 · 10/7 **74.35** (vol 1,480,000) · 10/8 **75.50** (vol 1,387,161). Second pull 16:18:12 from `query2.finance.yahoo.com` (same vendor, different host): identical closes and volumes; `adjclose` = `close` for these dates (no dividend in window). stooq.com returned a JavaScript proof-of-work wall (no data). Every close in the month is < $81.90 (max 79.66 on 9/9). ⇒ The most recent settled close (10/7, $74.35) is non-qualifying ⇒ **run 0-of-3; NOT FIRED.** 10/8 $75.50 is $6.40 below the line; whether it is "settled" under (c) is unproven (see Q3) but cannot change the verdict.

**Questions / guesses.**
1. **"guard section" does not exist as a heading.** I had to choose which part of a 52.9 KB card is the letter. The §5c row ① and the 9/28 RECORD say only "≥$81.90 × 3 consecutive closes"; only §6 carries the basis.
2. **Clause (d) — consecutiveness/reset — is, on the letter's own face, NOT settled** ("PENDING REGINALD CONCURRENCE"; nothing later in the card records the concurrence). The GATES cell asserts "a close <81.90 resets the count" as if settled. So the reset rule I applied is a *proposed* rule per the letter. REGINALD's own NOTES (8/20 ruling) does use "3 consecutive daily closes" with the 6/26·6/29·6/30 run, which is consistent, but it does not state the reset or missing-bar rule.
3. **Clause (c) "two different tools"**: is query1 vs query2 Yahoo two tools? Is Yahoo + yfinance two tools (same upstream)? How far apart must the pulls be? Vendor consolidated volume is often static for minutes and revised later (late prints) — two identical pulls 10 s apart prove little. Unresolvable from the letter.
4. **"OFFICIAL close" (GATES cell) vs "regular-session close" from a vendor daily bar (letter (a))**: NYSE's official closing price and a vendor bar can differ. The letter picks the vendor bar via REGINALD's method; the GATES cell word "OFFICIAL" suggests the exchange figure. Which one wins at a 1-cent tie?
5. **Precision / tie at float**: Yahoo returns floats (e.g. 76.37999725…). 9/14 reads **79.18** on today's Yahoo vs **79.19** recorded on the card for the same session. A close at 81.895 rounded one vendor up and another down would split the tie rule (b). No rounding convention stated.
6. **Vendor coverage**: the letter says 9/22's bar was MISSING for WAL; today's Yahoo chart HAS a 9/22 bar (77.75). So "missing bar" is a property of the pull date/tool, not the session — the letter's UNKNOWN branch is reader-dependent.
7. **Life of the guard**: the gate dies "with the position" / at 12/4 time stop; position truth is off-repo (card: "current holdings unverified"). A stranger cannot confirm the guard is still live; I assumed it is.
8. Two REGINALD subsections share the title "STATE RULING" — the source pointer is ambiguous.

---
## §1.5 GATE-BRK-R2 — GRADED: leg (a) FIRED (North Haven PIF LLC Q3-26 prelim 43.8%; OCIC Q3-26 prelim ~30%), both reproduced at primary; NO new fire since 10/2; leg (b) NOT FIRED (no in-window FINAL yet)

**Letter location.** GATES cell: "Letter → PC_REDEMPTION_REGISTER.tsv". definition_surface = `AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv (header + gate_status column)`. Read: all 30 `#` header lines whole (incl. population record P1–P12, FIRE RECORDs #1–#2, OTIC data row) + the column header + the gate_status column for all 11 rows. Source = `AGENTS/BROCK/research/2026-09-03_WQ158_OUT_OF_SAMPLE_RESULTS.md` (read whole; it is the evidence for the levels, it predates the 25% ruling and recommends retiring "<20%").

**Letter as I read it.** Per vehicle in the P1 population (six named CIKs): (a) ≥3 CONSECUTIVE strictly-sub-100% issuer-stated satisfaction quarters (P8); a prelim ≤94.0% counts immediately, >94.0% waits for the final (P7); reset on a full quarter, an unmeasurable/inferred quarter, or no offer (P9). (b) single quarter Σaccepted÷Σsubmitted strictly < 25.00%, FINAL filing only (P6), pricing date on/after 2026-09-03.

**Grading attempt (verbatim).** `date` 2026-10-08 16:19 EDT. EDGAR `data.sec.gov/submissions/CIK{…}.json` for the six P1 CIKs, filings dated ≥ 2026-09-25: BCRED 8-K 9/30 (items 5.07, 8.01 — not a tender result) · OCIC 8-K 10/2 (7.01, 9.01) + 13G/A 10/7 · North Haven LLC 8-K 9/29 (5.02) · ADS 424B3 10/1 (scanned: no tender/proration text) · Monroe none · CCLFX none. No SC TO-I/A since 9/18.
- North Haven LLC SC TO-I/A acc 0001193125-26-395654 (filed 9/18): "the Company accepted for purchase approximately **43.8%** of the Units … validly tendered … on a pro rated basis"; offer expired 9/14, units repurchased at NAV as of 9/30/2026. Q1 47.8 / Q2 41.6 per register ⇒ 3 consecutive sub-100% ⇒ **(a) FIRES** (43.8 ≤ 94.0 ⇒ counts on the prelim). (b): 43.8 > 25 and prelim ⇒ no.
- OCIC 8-K acc 0001193125-26-411315 Ex. 99.1/99.2: "OCIC will fulfill its 5% tender offer on a pro rata basis, approximately **30%** of total shares tendered"; footnote: Q1'26 "22.8% of each shareholder's tender request", Q2'26 "26.6%". ⇒ 3 consecutive sub-100% ⇒ **(a) FIRES**. (b): ~30 > 25, prelim ⇒ no.
- No other vehicle has a new issuer-stated figure ⇒ **no new fire today.** BCRED at 2 (next ~12/3 per header); OCIC Q3 FINAL (for (b)) not yet filed.

**Questions / guesses.**
1. **Does the gate re-fire?** "ONE vehicle shows …" reads like a single escalation; the register treats each vehicle as a separate fire ("SECOND VEHICLE to fire"). And does a 4th consecutive sub-100% quarter at an already-fired vehicle fire again, or is that vehicle spent? Unstated. Today's grade is unaffected but the next BCRED print (its 3rd) and NH's Q4 print (its 4th) depend on it.
2. **Population: rule vs list.** P1 defines membership by three criteria AND names six vehicles "as of 2026-09-18". OTIC (Blue Owl Technology Income Corp., CIK 0001869453) appears to satisfy all three criteria (SEC registrant, periodic tender, issuer-stated figure "approximately 13% of total shares tendered") yet is "TRACKED ONLY — NOT COUNTED" by the owner's recommendation, with "Population change = Will's word" pending. A stranger applying P1's criteria literally would count OTIC and (if its Q1/Q2 were issuer-stated sub-100%) fire (a) on it and possibly (b) at its final. I did NOT count it, but that is following the owner's note over the stated criterion.
3. **"Quarter" identity**: the issuer's own quarter label (OCIC "Q3'26", window closed 9/30) vs pricing-date quarter (NH Q3 priced at 9/30 NAV, offer expired 9/14). Consistent today, but unstated.
4. **"Issuer-stated" with "approximately"**: OCIC "approximately 30%" and NH "approximately 43.8%" — an approximate figure qualifies under P6/P7? I assumed yes (both far from 94% and 25%).
5. **Precision "as filed"**: register carries OCIC Q1 **22.82%**; the 10/2 issuer letter states **22.8%**. Two issuer figures at different precision for the same quarter — which is "as filed"? (Out-of-window for (b) either way.)
6. **(b) window**: "repurchase pricing date ON/AFTER 2026-09-03" — NH's pricing NAV date is 9/30 (in window), but the offer expired 9/14. If an offer expired before 9/3 but priced after, is it in window? Unstated beyond "pricing date".
7. **Feeder look-through**: OCIC's letter excludes feeder-fund shareholders; P4 excludes the feeders as vehicles. Satisfaction at the main registrant only — consistent, but I inferred it.
8. GATES summary cell carries a correct one-line letter but omits P6–P9 (vintage, buffer, strictness, reset); the summary alone would have left the prelim-vs-final question open (I would not have known the 94.0% buffer).

---
## §1.6 GATE-NEXUS-T12S-DFII10 — GRADED (provisionally, on the Treasury early copy; FRED unreachable): NO BRANCH COMPLETED through cell 10 (10/8); window OPEN, 5 cells remain

**Letter location.** GATES cell: "FULL LETTER → definition_surface §2 (frozen) — this cell is summary + pointer". definition_surface = `AGENTS/NEXUS/research/2026-09-24_t12_successor_DFII10_letter.md`; source names the same file (§1 · §2 · §4) + a PROME packet + a RULED proposal row. Read the letter file whole (§2 is the letter). Did NOT read the PROME packet or RULED row (named in source; not needed — the letter is self-contained; listed in §3 as unread-by-choice).

**Grading attempt (verbatim).** `date` 2026-10-08 16:20–16:23 EDT. FRED `fredgraph.csv?id=DFII10` and ALFRED: **failed** (HTTP/2 INTERNAL_ERROR; HTTP/1.1 retry timed out at 60 s; `/data/DFII10.txt` same). US Treasury `daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve` → 200, `10 YR` column:
anchor **L = 2.85 [9/24]** ⇒ UP edge ≥ **2.95**, DOWN edge ≤ **2.75**.

| cell | date | 10 YR | ≥2.95? | ≤2.75? |
|---|---|---|---|---|
| 1 | 9/25 | 2.83 | – | – |
| 2 | 9/28 | 2.90 | – | – |
| 3 | 9/29 | 2.91 | – | – |
| 4 | 9/30 | 2.93 | – | – |
| 5 | 10/1 | 2.88 | – | – |
| 6 | 10/2 | 2.92 | – | – |
| 7 | 10/5 | 2.95 | ✔ (tie, ≥) | – |
| 8 | 10/6 | 2.91 | – | – |
| 9 | 10/7 | 2.92 | – | – |
| 10 | 10/8 | 2.87 | – | – |

Longest UP run = 1 (cell 7); DOWN run = 0. ⇒ **Neither branch has completed; not C yet** (C requires the 15th cell). Remaining cells 11–15 (expected 10/9, 10/13, 10/14, 10/15, 10/16 if 10/12 Columbus Day is a non-publication day): **UP can still complete only if all five are ≥ 2.95; DOWN only if all five are ≤ 2.75; otherwise C #1 ⇒ one re-anchored window at L₂ = cell 15.** My grade matches the GATES state cell (cells 1–8 NEITHER; 9 = 2.92).

**Questions / guesses.**
1. **FRED governs, and I could not reach FRED or ALFRED** — so "each cell as first published" at FRED is unverified for every cell, including the anchor L. My grade is on the "same-basis early copy". A 1bp FRED/Treasury difference at 2.95 (cell 7) or at the anchor would move edges; none is decisive today.
2. **Is a Treasury-only cell "published"?** The 10/8 cell is on Treasury today and (typically) on FRED tomorrow. "A cell not yet published is not an observation" — published WHERE? If only FRED publication counts, today's count is 9 cells, not 10. I counted 10 using the early-copy permission; either way no run completes.
3. **"First published" vs current FRED**: if FRED revises a cell (rare for DFII10), first-published governs — requires ALFRED vintages, which a stranger needs and could not get today.
4. **Tie convention**: "≥ L + 0.10" with L and cells at 2-dp → exact decimal ties (2.95). I treated 2.95 as meeting the UP edge. Float arithmetic (2.85+0.10) happened to give 2.95 exactly in Python here, but the letter does not say to compare in basis points / integers.
5. **Holidays**: "bond-market holidays" — SIFMA calendar? Treasury? 10/12 (Columbus Day) assumed non-publication; the letter counts cells, so this only shifts calendar dates.
6. **Regime caveat** in the GATES cell ("his word re-cuts this cell only if he meant the literal string") — a pending interpretive question about whether the LITERAL "≥2.50 on five published sessions" is the letter. If it is, it was met at registration and would grade FIRED. The letter itself (§1.2) rejects that reading; I graded the banded §2.
7. Disc-A mechanism test applies only at a fire — not exercised.

---
## §1.7 GATE-TERRY-VLO-HELD-01 — GRADED: leg A NOT FIRED, no notice (10/8 settlement-window ESTIMATE ≈ $113.56–$113.58); B1 NOT FIRED; B2 no Valero 8-K (IR/executive remarks not checked)

**Letter location.** definition_surface = `AGENTS/TERRY/setups/VLO-SHARE_management-proposal_2026-09-28.md` (no section named in that column; its header says "Letter = § 2 (A) + § 3 (B) + § 5 as written" and "Exact letter: § 2-bis" for the amendment). Source names § 2 (A) · § 3 (B) · § 5 · ⚖️ ASK + `PROME/WILL_QUEUE.md WQ-330` + BRENT `NOTE.md` + `PROME/proposals/2026-10-07_VLO-december-management-RULED.md`. Read: card header, §2, §2-bis, §3, §5, §6, ⚖️ ASK whole. Did NOT read WILL_QUEUE.md (shared queue; the card quotes the ruling), BRENT NOTE.md (declares itself "observables, no thresholds"), or the RULED proposal beyond its heading list (the card's §2-bis claims to quote its "Approved amendment" verbatim — I did not verify the quote against the source; §3).

**Grading attempt (verbatim).** `date` 2026-10-08 16:23:47 EDT.
- ① CME settlement: `cmegroup.com` settlements endpoints → **HTTP 403** (both URLs tried). Unavailable.
- ② vendor daily row 10/8: Yahoo `HOX26.NYM` 4.8425 (vol 46,876), `CLX26.NYM` 90.70 (vol 298,439) ⇒ 4.8425×42 − 90.70 = **$112.69** — a last-trade close (pulled 16:2x ET, after 14:30) and **$0.87 away from ③ ⇒ REJECTED** (outside $0.15). Note the 10/7 rows carry the SAME volume as 10/6 (HOX26 41,943; CLX26 265,937) — the duplicated-volume defect the letter names, reproduced.
- ③ 14:28–14:30 ET one-minute VWAP from Yahoo 1-min chart (bars stamped 14:28, 14:29, 14:30 ET): HOX26 4.88246 (typical) / 4.88123 (close); CLX26 91.4841 / 91.4538 ⇒ crack **$113.579 (typical-price VWAP)** / **$113.558 (close VWAP)**; using only bars 14:28–14:29: $113.580 / $113.560. ESTIMATE, single vendor.
- Leg A: ≈ $113.56 is not < $95 and not < $90.16, and far outside ±$0.15 of $90.16 ⇒ **NOT FIRED, no notice.** Governing pair = November (10/8 ≤ 10/14) ✔.
- B1: whitehouse.gov/presidential-actions/ listing (16:24 ET): October items = Columbus Day 2026, **Emergency Tax Relief on Diesel Fuel (Oct 5)**, National Energy Dominance Month 2026 (Oct 7), National Manufacturing Day 2026. Diesel tax-relief text contains no "export" (and excise-tax suspension is expressly NOT B1); Energy Dominance proclamation mentions exports only as LNG achievements. Federal Register API full-text since 9/15 for "diesel export" / "distillate export" / "petroleum product exports" / "export of refined petroleum": hits are OFAC Venezuela general licenses (9/30), SAFE vehicles rule, unrelated. ⇒ **B1 NOT FIRED.**
- B2: Valero (CIK 1035002) EDGAR since 9/20: Form 4 (9/21), 3/A (10/6) — no 8-K. Valero IR press releases and "named executive" remarks NOT checked ⇒ B2 = no filing-primary evidence; not exhaustively graded.

**Questions / guesses.**
1. **VWAP definition**: "one-minute volume-weighted settlement-window proxy" — VWAP of what price per bar (close? typical (H+L+C)/3?) The card's own 10/7 grade quotes BOTH ($105.79 typical / $105.82 close). Which governs at a ±$0.15 boundary? Unstated; spread here ~$0.02.
2. **Which bars are "14:28–14:30"?** Bars stamped 14:28/14:29/14:30 (the 14:30 bar runs 14:30:00–14:30:59, after the CME 14:30 settle) or only 14:28–14:29? The card's grades say "3 bars per leg", implying the 14:30 bar is included — I note it, the letter doesn't say.
3. **Contract identity "on each pull"**: the card's method is `expireDate` on both legs. My Yahoo chart pull returned `expireDate: None` for both. I relied on the explicit symbols HOX26/CLX26. If expireDate is the required proof, the letter says a missing identity ⇒ UNKNOWN — i.e. a stranger with my tool would have to grade **UNKNOWN**, not NOT FIRED. I took symbol = identity.
4. **Tie / precision**: "strictly below $90.16" — compared at what rounding of HO×42 (HO quotes to 4 dp; ×42 gives 4 dp)? Not stated.
5. **"Accepted only within $0.15 of (3)" — at what time is ② pulled?** The daily row read after 14:30 is a last trade (letter: reject provisional rows), but "finalized" is never defined beyond duplicated volume. My 10/8 row has fresh volume yet is a post-settle last trade — is that "provisional"? It fails the $0.15 test anyway.
6. **B1 scope edge**: OFAC Venezuela Sanctions Regulations general licenses (Federal Register 2026-09-30) concern licensing exports (incl. diluents/diesel) to ONE country under an IEEPA programme. B1 lists "an IEEPA national-emergency declaration with that operative text, or a Commerce/BIS licensing rule" and requires a "signed presidential action". An OFAC (Treasury) GL is neither presidential nor Commerce/BIS — I ruled it out, but the letter never says whether a destination-specific sanctions licence counts as "licenses US distillate/diesel exports".
7. **B2 evidence surface**: "on the record (press release, 8-K, or a named executive)" — a named executive in an interview/earnings call is not systematically searchable; a stranger can only check EDGAR + IR.
8. **Notice ±$0.15 band**: the §2 missing-data table cites "same band the gate letter uses at $95", but the §2-bis approved letter states the ±$0.15 UNKNOWN band only at $90.16. Is a ③-only reading of $95.05 a notice or UNKNOWN? Two texts disagree.
9. **Grader identity**: "TERRY (grades at its touches)" — the letter's consequence is a TERRY rec; does a stranger's grade count for anything? (Out of scope; noted.)

---
## §1.8 GATE-HOMER-THESIS-KILL — GRADED (interim, not a formal-grade date): NO LEG at its kill count ⇒ "Anything else" ⇒ 🔴 holds; A1 not independently verified

**Letter location.** definition_surface = `AGENTS/HOMER/thesis/THESIS.md (owner-side canonical letter; frozen §3 legs + §4 rule)`; the GATES cell says "this row is summary+pointer (PAT-006)". Read THESIS.md header + §3 (all five legs) + §4 whole. Source also names `AGENTS/HOMER/docket/CATALYSTS.tsv` row 'THESIS KILL RAIL — formal grade' and a PROME inbox packet — NOT read (the letter is self-contained; listed in §3).

**What "grade as of today" means here.** Formal grades are 2026-11-20 and 2027-02-20; "Earlier only if any leg reaches its kill count." So today's gradeable question is: has any leg reached its kill count? I tested every leg I could reach.

**Grading attempt (verbatim).** `date` 2026-10-08 16:25–16:27 EDT.
- **C1** (ICE First Look FC sales YoY ≤0% AND FC pre-sale inventory YoY ≤0%, 3 consecutive monthly prints): `mortgagetech.ice.com/resources/data-reports/first-look-at-august-2026-mortgage-data` (released 2026-09-28): FC sales "up 12% year over year"; active FC inventory "up 89,000, or 41%, year over year"; pre-sale inventory rate 0.54%. Latest print fails both conditions ⇒ run 0 ⇒ **not killed** (Sept First Look not yet out, ~10/23–28).
- **C2 CMBS channel** (Trepp CMBS MF DQ < 6.00%, 3 consecutive): `trepp.com/trepptalk/cmbs-delinquency-report-sept-2026`: "Multifamily rose 35 basis points to **8.04%**" ⇒ run 0 ⇒ channel alive ⇒ leg C2 cannot be killed (LEG KILL needs both channels) regardless of the GSE channel, which I did not pull.
- **A1** (MBA NDS FHA SA DQ falls QoQ 2 consecutive quarters AND ICE Mortgage Monitor serious-DQ cure-rate condition): `mba.org` → **403**; CalculatedRisk search returned only historical posts. **UNVERIFIED.** No new NDS since 9/29 (Q3 ~mid-Nov), so A1's state cannot have changed since the owner's 9/29 grade — but I cannot confirm that grade.
- **A2** (Freddie PMMS 30-yr ≤ 6.50% on 4 consecutive weekly prints): `freddiemac.com/pmms/docs/PMMS_history.csv`: 9/24 7.03 · 10/1 **7.28** · 10/8 **7.40** ⇒ run 0 ⇒ **not killed**.
- **A3** (NAHB/Wells Fargo HMI ≥ 40 on 3 consecutive monthly prints): NAHB `t2-national-hmi-history-202609.xls`: 2026 Jan 37 · Feb 37 · Mar 38 · Apr 34 · May 37 · Jun 36 · Jul 34 · Aug 35 · **Sep 32** ⇒ run 0 ⇒ **not killed**.
- ⇒ Cores: 0 killed; amplifiers: A2, A3 not killed, A1 unverified (≤1 possible, so "≥2 of 3 amplifiers" impossible) ⇒ **§4 row "Anything else": 🔴 holds.** No early formal grade is triggered.

**Questions / guesses.**
1. **C1 "FC pre-sale inventory YoY"** — ICE publishes BOTH an inventory COUNT (active foreclosure inventory, +41% YoY) and a pre-sale inventory RATE (0.54% of active loans). The letter says "FC pre-sale inventory YoY"; the GATES summary says "foreclosure-inventory YoY". Count YoY and rate YoY can differ in sign near zero. I used the count; unresolved.
2. **Precision**: First Look prose rounds ("up 12%"); the letter's own text quotes "+11.7%" (a table figure). Which number grades "≤ 0%" at the boundary — prose or table? (Matters only at ~0%.)
3. **Pre-registration prints**: do "3 consecutive monthly prints" include prints before 2026-09-29? Unstated. Not decisive today.
4. **C2 GSE channel definitions**: letter = "the higher of Freddie MF DQ and Fannie MF **serious** DQ"; GATES summary = "max(Freddie, Fannie MF DQ)" — the summary drops "serious". Freddie's MF DQ measure (60+? 90+?) is not defined; the two are different measures being max'd. Source documents (Freddie/Fannie monthly volume summaries) not named.
5. **Fannie provision pairing** ("same quarter's Fannie MF credit provision"; if it rose, grade HALF) mixes a monthly series with a quarterly one: which quarter pairs with a mid-quarter month? Undefined.
6. **A1 cure-rate leg**: "serious-DQ cure rate YoY better than −15% (above the Cure Rates Yellow line)" — "Cure Rates Yellow line" is not defined anywhere I may read; "better than −15%" sign convention (is −10% better? presumably yes) is inferred. ICE Mortgage Monitor is a PDF; series location unnamed.
7. **"LEG KILL = both channels killed at the same grade"** — at a formal grade only, or whenever both counts are simultaneously complete? Interacts with "EARLIER if any leg reaches its kill count": does an early formal grade happen when ONE CHANNEL completes, or only a whole leg?
8. **Amplifier context data disagree with NAHB's own table**: the letter lists HMI "Feb 36" (2026, "search summaries"); NAHB's table says 37. Not kill-deciding; shows the letter's context figures are not primary.
9. **Dead-instrument rule** (>45 days without a print ⇒ UNGRADED): Trepp/ICE/PMMS/NAHB all printed within 45 days; MBA NDS is quarterly (~90 days between prints) — by the letter's own 45-day rule, is A1's NDS leg perpetually "dead" between prints? The instrument-health line for A1 gives no 45-day rule, but §4's UNGRADED clause is general. Unclear.

---
## §2 Summary-cell-alone findings (would the GATES `condition` cell alone have been gradeable?)

| Gate | Summary cell alone gradeable today? | What the summary lacks or gets wrong vs the letter / pointer finding |
|---|---|---|
| BRENT-COT-35B | **YES** — names file, market, code, fields 15 ÷ 8, all Leg-A bands, Leg-B level, agreement rule, vintage | Field index base (0/1) unstated. Cell says 4.909% "NOT re-reproduced since 8/13"; the letter (registry row) says REPRODUCED 2026-09-18 — summary is stale vs its own letter. definition_surface cites "row 123" (row is now file line 156). Source pointer "2026-08-12_rule-batch-RULED.md (35b)" resolves to no row (that file has no 35b). |
| FERT-G5 | **YES** — and it is MORE complete than the letter | Cell says "FULL LETTER … → definition_surface", but the definition_surface carries only "DTN retail DAP/MAP > $1,000/ton"; geography + strict-tie clauses exist only in the cell. Letter's "DAP/MAP" (slash) vs cell's "DAP OR MAP". "Registry letter archived 8/22" — no path given. |
| CORAL-MSI-01 | **YES, provisionally** (I graded from it) | Cell declares the canonical letter is in `AGENTS/CORAL/STATUS.md` (a rotating state file, out of a stranger's reach here). No URLs/market ids, no MSI sub-series, no pull cadence; storm rule S1–S4 referenced only in the state cell, text only in STATUS. The one reachable non-STATUS source (8/23 packet) carries a SUPERSEDED stand-down rule. |
| TERRY-ROLL70-EXIT | **YES for today** (all closes ≫ $6 below) | Pointer "ROLL70 card, guard section" matches no heading. Cell asserts the reset rule as settled; the letter marks clause (d) "PENDING REGINALD CONCURRENCE". Cell lacks the unadjusted basis, the ≥ tie, the settled-bar rule and the missing-bar rule — all decisive near $81.90. "OFFICIAL close" (cell) vs vendor regular-session bar (letter). |
| BRK-R2 | **PARTLY** — legs (a)/(b) and the prospective window are there | Missing the population (P1, six CIKs), the prelim-vs-final vintage (P6), the 94.0% prelim buffer (P7), strictness (P8) and the reset rule (P9). A summary-only grader could not decide whether a preliminary figure counts, or which vehicles (OTIC? ASIF? Fund A?) are in. |
| NEXUS-T12S-DFII10 | **YES** — instrument, anchor date, ±0.10, 5-run, 15-cell window, one re-anchor | Omits "each cell as first published", the Treasury early-copy permission and "FRED governs on a difference". Carries an open interpretive question (literal "≥2.50 on five sessions" vs the band) that could flip the verdict to "fired at registration" if Will's word is read literally. |
| TERRY-VLO-HELD-01 | **YES** — the cell is near-verbatim letter | Neither cell nor letter defines the VWAP price (typical vs close) or the exact bars; identity-check method (expireDate) is in the card's operational text only. Notice-line ±$0.15 band: card §2 says it applies at $95, the approved §2-bis letter states it only at $90.16. |
| HOMER-THESIS-KILL | **YES at leg level** | Drops "pre-sale" (C1 inventory) and "serious" (Fannie MF DQ); omits the HALF rule (Fannie provision pairing), the amplifier "intensity note" row, the dead-instrument/UNGRADED rule, and the cure-rate definition. |

---
## §3 Limits — data and text I could not reach, and perimeter choices

**Data unreachable (16:14–16:27 EDT 2026-10-08):**
- FRED and ALFRED (`fredgraph.csv`, `alfredgraph.csv`, `/data/DFII10.txt`): HTTP/2 INTERNAL_ERROR, HTTP/1.1 60 s timeouts ⇒ NEXUS graded on the Treasury early copy only; "first-published" unverifiable.
- CME settlements (`cmegroup.com`): HTTP 403 ⇒ VLO leg A source ① unavailable; graded on source ③ (ESTIMATE).
- MBA (`mba.org`): HTTP 403; CalculatedRisk search gave only historical posts ⇒ HOMER A1 unverified.
- stooq: JavaScript proof-of-work wall ⇒ no second-vendor WAL close; both WAL pulls were Yahoo (query1/query2).
- CFTC first-print vintage: only the current `f_disagg.txt` is reachable; whether the 9/29 row is the FIRST print cannot be proven (no first-print archive).
- Parcl: metro URLs/IDs not given by the letter; slugs guessed (`/research/markets/fl/<metro>/metro`). Fort Myers / Sarasota map entries not compared.
- Not pulled (judged non-decisive): Freddie/Fannie MF DQ (HOMER C2 GSE channel — CMBS channel alive makes the leg unkillable today), Valero IR press releases / executive remarks (VLO B2), NH/OCIC final SC TO-I/A (not yet filed).

**Repository text NOT read, by rule:**
- Any `STATUS.md`: BRENT `STATUS.md rows 13-14` (named in BRENT's source column) and **CORAL `STATUS.md` (CORAL's definition_surface and canonical letter)** — the latter is why CORAL is CANNOT-GRADE from the letter.
- `PROME/GATES_README.md`: the GATES header says its rules are to be read "as if they still sat in this header". My perimeter said "the GATES.tsv header" only, so I did NOT read it; any default tie/consecutiveness/vintage rule it holds was unavailable to me — another place where a stranger's perimeter and the letter's perimeter differ.

**Repository text in-perimeter but NOT read, by choice (letter was self-contained):** `PROME/WILL_QUEUE.md` WQ-330; BRENT `research/2026-09-28_vlo-thesis-observables/NOTE.md`; body of `PROME/proposals/2026-10-07_VLO-december-management-RULED.md` (only its headings — so the card's "verbatim" quote of the amendment is unverified by me); NEXUS's PROME packet `2026-09-24_from-NEXUS_wq261…` and RULED row 261; HOMER `docket/CATALYSTS.tsv` row and its PROME packet; FERT TRIGGERS rows other than T4.

**Wall-clock receipts:** start 16:14:27 · BRENT 16:15:00 · DTN 16:15:42 · Parcl 16:16:39 · WAL 16:18:02/16:18:12 · EDGAR 16:19:11 · DFII10 16:20:25–16:23:07 · VLO 16:23:47–16:24:35 · HOMER 16:25:33–16:26:16 (all `date`, EDT).
