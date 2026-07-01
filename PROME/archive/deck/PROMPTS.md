# Deck Project — Agent Prompts

Stored here so we can iterate on the template and track what we sent.

**Prompt evolution:**
- V1 (CARL/REGINALD): Base template. Worked well but outputs were paragraph-shaped, not slide-shaped.
- V2 (BROCK/LIQUID): Added "quote-ready slide sentence" requirement. Customized difficulty framing per domain.

---

## REGINALD (Spawned 2026-03-13)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, doesn't read call reports).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, BANK_EXPOSURE_MATRIX.md, domain/NDFI_HIDDEN_CRE_HYPOTHESIS.md, domain/INSIDER_BEHAVIOR_SCAN.md, domain/sources/ (especially the OZK thesis, FDIC QBP, Hidden CRE analysis, WAL research, Apollo interconnection), and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

Focus areas that matter most for this deck:
- **Memo Item 3 / hidden CRE discovery** — this is our most original work. Explain it like you're proving it to a skeptic.
- **OZK and WAL specifics** — balance sheet details, insider selling, the things that make someone say "wait, really?"
- **The 2007 parallel** — why this is a slow grind, not SVB-style
- **FDIC/industry-level data** — anything showing this is systemic, not just one or two bad banks
- **KW bondholder revolt** — if it's a useful precedent for "how these things start"
- **Deutsche Bank $30B private credit disclosure** — interconnection risk

For each item, provide:
1. **The finding** (one sentence, plain English — no jargon someone's wife wouldn't understand)
2. **Why it matters** (2-3 sentences connecting it to the thesis)
3. **The source** (specific filing, data series, or document — we need to be able to say "look it up yourself")
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Rank by persuasive power to a smart outsider, not by how important it is to our trading. The question is: "what would make someone who thinks the market is fine stop and reconsider?"

Write output to `AGENTS/REGINALD/DECK_EVIDENCE.md`.

---

## CARL (Spawned 2026-03-13)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, doesn't read call reports).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, domain/ATHENE_DEPOSIT_MAP.md, domain/sources/CVNA_FRAUD_WATCH.md, archived STATUS files, and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

Focus areas that matter most for this deck:
- **Consumer delinquency data** — credit cards 90+ at 12.70%, subprime auto 60+ at 7.1% ALL-TIME RECORD, student loans 16.3%. These are numbers that hit people in the gut because they know someone struggling.
- **The savings rate** — 3.6% matching 2008. This is the "buffer is gone" proof.
- **Goeasy collapse** — the Canadian canary. -57%, dividend suspended, NCO mid-teens. Leads US by 1-2 quarters.
- **SoFi CNL trigger** — first ever. Stress climbing UP the quality stack, not just subprime.
- **K-shape convergence** — both rich and poor moving down now. FHA DQ 11.52% vs conventional 2.89%.
- **Gas price behavioral breakpoint** — $4/gallon as the moment consumers change behavior. Currently $3.40-3.75 and rising.
- **The fertilizer → food CPI chain** — this is the "it gets worse in Q3-Q4" story
- **Repossessions at 3M (+76% above GFC peak)** — visceral, relatable number

For each item, provide:
1. **The finding** (one sentence, plain English — something that would make someone at a dinner party put down their fork)
2. **Why it matters** (2-3 sentences connecting it to the broader thesis)
3. **The source** (specific data series, filing, or publication — credibility matters)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Rank by persuasive power to a smart outsider. Consumer data is inherently relatable — lean into that. The person reading this should think "this is happening to people I know."

Write output to `AGENTS/CARL/DECK_EVIDENCE.md`.

---

## BROCK (Spawned 2026-03-13)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, doesn't follow private credit markets).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md, domain/sources/ (especially the Eisman/Gober transcript analysis, Eisman Ep49 analysis, FDIC NDFI exposure data, Iran financial targets piece, BDC cash coverage methodology), EXPECTED_SIGNALS.md, and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

Focus areas that matter most for this deck:
- **The fund gate cascade** — 4 gates in 6 days. This is the "bank run in slow motion" story for private credit. Name the funds, name the dates.
- **Athene / APO structure** — the insurance-as-leverage-vehicle story. $442B, 48% illiquid, the Kuvari captive stuffing. Eisman and Gober are publicly short — explain why in plain English.
- **BDC pricing collapse** — average 78¢ on the dollar, FSK at 51¢, PSEC at 44¢. The market is already saying these assets aren't worth what the books claim.
- **PIK loans doubling** — 6.4%, 40% of borrowers negative free cash flow. Explain what PIK means for a non-specialist: "they can't pay interest so the lender pretends they did."
- **The bank interconnection** — $4.2T NDFI exposure, Atlas SP double default, JPM and MS restricting warehouse lines, WFC at $59.7B (double the next largest). This is how private credit stress reaches the banking system.
- **PIMCO calling it a "crisis of bad underwriting"** — when the biggest bond manager in the world uses that language publicly, it matters.
- **Software collateral markdowns** — JPM marked down, Vista/Thoma Bravo named. 40% of sponsor-backed loans.

For each item, provide:
1. **The finding** (one sentence, plain English — make it land for someone who's never heard of a BDC)
2. **Why it matters** (2-3 sentences connecting it to the broader thesis)
3. **The source** (specific report, filing, or named quote — this audience will include someone who works in finance and will want to verify)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Also include one **quote-ready slide sentence** per finding — a single line we could put directly on a slide without editing.

Rank by persuasive power to a smart outsider. Private credit is an unfamiliar world for most people — your job is to make them understand why $1.7 trillion in opaque loans is their problem too.

Write output to `AGENTS/BROCK/DECK_EVIDENCE.md`.

---

## LIQUID (Spawned 2026-03-13)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, doesn't follow Treasury plumbing).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, CREDIT_THRESHOLDS.md, INBOX.md, domain/sources/ (especially the insurance Level 3 CRE transmission piece, archived STATUS), and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

Focus areas that matter most for this deck:
- **The Fed trap in plain English** — GDP 0.7% + Core PCE 3.1% = stagflation. They can't cut (inflation), they can't hike (recession). Explain why this is worse than either problem alone.
- **HY OAS at the threshold** — 317-320bps, our trigger for "credit transmission confirmed." Explain what a spread is and why this number matters, simply.
- **Treasury auction deterioration** — 10Y below-average demand, 20Y "disastrous tail," 30Y clearing at 4.87%. The pattern: buyers exist but demand higher and higher yields. What that means for mortgage rates, bank funding costs, everything.
- **RRP at zero** — $0.278B, essentially no buffer. Explain what this means: the financial system's shock absorber is empty heading into quarter-end.
- **The demand hole** — foreign buyers (Japan, China, Gulf states) reducing Treasury purchases. ZHAO's four-anchor framework: $40-72B/mo in combined selling. Who buys if they don't?
- **The TSMC inflation channel** — Hormuz → Qatar LNG → Taiwan power → chip supply → tech goods inflation → Core PCE +24-36bps → Fed cuts eliminated. This is the chain that welds the rate-cut door shut.
- **Bear steepening** — 10Y surging while front end stays anchored. What this signals about market expectations.

For each item, provide:
1. **The finding** (one sentence, plain English — Treasury market plumbing is the hardest thing to explain simply, so really work at this)
2. **Why it matters** (2-3 sentences — always connect back to "and that's why rates stay high / the Fed is stuck / your mortgage rate isn't coming down")
3. **The source** (auction results, FRED series, specific data)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Also include one **quote-ready slide sentence** per finding — a single line we could put directly on a slide without editing.

Rank by persuasive power to a smart outsider. Your domain is the hardest to make accessible — bonds, funding markets, repo plumbing. The audience needs to walk away understanding one thing: **the normal rescue mechanisms (rate cuts, cheap money, government borrowing) are all broken at the same time.** Make that visceral.

Write output to `AGENTS/LIQUID/DECK_EVIDENCE.md`.

---

## HENRY (Spawned 2026-03-13)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, doesn't track GDP revisions or vol regimes daily).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, CONVERGENCE_REPORT.md, EXIT_RULES_REVIEW.md, domain/BEIGE_BOOK_MAR4_2026.md, domain/ECON_CALENDAR.md, domain/REFERENCE_TABLES.md, domain/sources/ (NFP synthesis, Lighthouse Macro framework), and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

Focus areas that matter most for this deck:
- **The Hamilton demand destruction framework** — NOPI at 47 log points, GDP drag of -3.0 to -4.9pp, peak impact Q1 2027. This is the intellectual backbone of our timing. Explain it so someone who's never heard of Hamilton or NOPI understands why oil shocks destroy economies on a predictable schedule.
- **GDP 0.7% + the earnings repricing math** — street expects 12-14% EPS growth built on ~2.5% GDP. Actual GDP is 0.7% pre-shock. Walk through the arithmetic: what happens to S&P earnings when GDP is negative? The 1973-74 template.
- **NFP -92K** — first negative payroll this cycle. Dec revised to -17K. What this means for the "jobs are fine" narrative.
- **The VIX regime shift** — why vol is suppressed now but coiled. The FOMC 0-cut dots as the mechanical trigger for VIX 35→55. Make this accessible.
- **The stagflation confirmation** — GDP 0.7% + Core PCE 3.1% as the definitive data point. Both mandates failing simultaneously.
- **The Beige Book** — what the Fed's own regional contacts are saying about real economic conditions.
- **Consumer spending revised down** — 2.4% → 2.0%. The last pillar cracking.

For each item, provide:
1. **The finding** (one sentence, plain English)
2. **Why it matters** (2-3 sentences — always connect back to "this is why the market is mispriced / this is what happens next")
3. **The source** (specific data release, academic paper, filing)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Also include one **quote-ready slide sentence** per finding — a single line we could put directly on a slide without editing.

Include a **glossary** section (2-3 sentences each) defining: NOPI, stagflation, bear market, VIX, EPS. The audience is smart but may not know these terms cold.

Rank by persuasive power to a smart outsider. Your domain is the macro picture — the "so what does all this add up to?" Your evidence should make someone understand that the economy is already weaker than the market is pricing, and an oil shock is about to make it dramatically worse on a knowable timeline.

Write output to `AGENTS/HENRY/DECK_EVIDENCE.md`.

---

## SAM (Spawned 2026-03-13)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, has probably heard "carry trade" but couldn't explain it).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, INBOX.md, RESEARCH_STATUS.md, CHECKIN_MAR6.md, domain/sources/RP-SAM-4_JAPAN_LIFE_INSURER_STRESS.md, and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

Focus areas that matter most for this deck:
- **The carry trade unwind in plain English** — Japan kept rates at zero for decades, so global investors borrowed yen cheap and invested elsewhere. Now Japan is raising rates. Explain why unwinding this is like pulling a thread that unravels global markets. Make it visceral, not academic.
- **USD/JPY at 159.50 — intervention zone** — MoF rate checks triggered at this exact level in January. What intervention means and why it would accelerate the unwind.
- **The repatriation data** — ¥3.07T net selling in February ($19.4B), banks selling ¥3.14T (5x more than life insurers). FY-end March 31 = T-18 days. The acceleration question.
- **BOJ hawkish pivot** — Reuters 4-source report that Iran war may SPEED UP hikes, not delay them. The regime shift from "cushioning growth" to "fighting inflation." Hawkish hold probability doubled to 30%.
- **Life insurer stress** — J-ICS regulatory change forcing repatriation. The structural (not cyclical) reason Japan keeps selling foreign bonds.
- **The TIC data watch** — March 15 Japan UST holdings. Why this is the hard confirmation of the demand hole.
- **How Japan connects to everything else** — Japan is the largest foreign holder of US Treasuries. When they sell, US rates rise. When US rates rise, bank balance sheets deteriorate, mortgages stay expensive, and the Fed trap tightens. Make this connection explicit.

For each item, provide:
1. **The finding** (one sentence, plain English — Japan macro is intimidating to most people, so really simplify)
2. **Why it matters** (2-3 sentences — always connect back to "and this is why it affects YOUR interest rates / YOUR stock portfolio")
3. **The source** (MoF data, Reuters, BOJ statements, TIC)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Also include one **quote-ready slide sentence** per finding — a single line we could put directly on a slide without editing.

Include a **glossary** section (2-3 sentences each) defining: carry trade, intervention, repatriation, BOJ, fiscal year-end. The audience is smart but Japan macro is a foreign language to most Americans.

Rank by persuasive power to a smart outsider. Japan is the "nobody's watching but it matters enormously" story. Your evidence should make someone understand that the world's largest creditor nation is pulling its money home — and that's a problem for everyone who has a mortgage, a 401k, or a savings account.

Write output to `AGENTS/SAM/DECK_EVIDENCE.md`.

---

## MARCO (Spawned 2026-03-13) — V3 (less directive)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows what a put is, follows news but doesn't track immigration policy or labor supply data).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, EXPECTED_SIGNALS.md, RESEARCH_STATUS.md, CHECKIN_MAR6.md, MARCO_SKELETON.md, RP-MARCO-MBS_BASELINE.md, domain/sources/, and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

You decide what's most important. Read everything, then rank by what would be most persuasive to a smart outsider. Your domain is the most *human* part of the thesis — real people, real jobs, real grocery bills. The audience should walk away thinking "this isn't abstract — this is happening to people right now."

For each item, provide:
1. **The finding** (one sentence, plain English — these are kitchen-table issues, make them land that way)
2. **Why it matters** (2-3 sentences — connect to the broader thesis: consumer stress, inflation, economic slowdown)
3. **The source** (specific data, government reports, news outlets)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Also include one **quote-ready slide sentence** per finding — a single line we could put directly on a slide without editing.

Write output to `AGENTS/MARCO/DECK_EVIDENCE.md`.

---

## BRENT (Spawned 2026-03-13) — V3 (less directive)

**Project: Thesis Deck — Evidence Assembly**

We're building a shareable slide deck to explain and defend our portfolio thesis. Audience: finance-literate but not deep in macro (knows oil prices matter, doesn't follow tanker rates or OPEC+ dynamics).

Your job: read through your **entire domain** — STATUS.md, TRADE.md, MEMORY.md, domain/ECON_CALENDAR.md, domain/REFERENCE_TABLES.md, and any other files in your directory — and assemble a ranked list of your **10 most significant findings or pieces of evidence**.

You decide what's most important. Read everything, then rank by what would be most persuasive to a smart outsider. Energy is the most intuitive part of the thesis — everyone pays for gas. Your job is to make them understand the scale and duration of what's happening, and why the cascading consequences reach far beyond the gas pump.

For each item, provide:
1. **The finding** (one sentence, plain English — everyone understands gas prices, build from there)
2. **Why it matters** (2-3 sentences — always connect to the portfolio: why this means rates stay high, banks stay stressed, consumer breaks)
3. **The source** (EIA, AAA, Reuters, specific military confirmations)
4. **Strength rating** (🔴 smoking gun / 🟠 strong signal / 🟡 supporting evidence)

Also include one **quote-ready slide sentence** per finding — a single line we could put directly on a slide without editing.

Also include a brief **"Why can't they just fix it?"** section — address the obvious objections a skeptic would raise. Keep answers to 1-2 sentences each.

Write output to `AGENTS/BRENT/DECK_EVIDENCE.md`.

---

## HAWK (Spawned 2026-03-13) — V3

**Project: Thesis Deck — Evidence Assembly**

[Geopolitics/military → economic consequences. 10 findings ranked. Connect military/diplomatic actions to economic outcomes people can feel. Sources: DoD, Lloyd's, shipping data. Write to AGENTS/HAWK/DECK_EVIDENCE.md]

---

## ZHAO (Spawned 2026-03-13) — V3

**Project: Thesis Deck — Evidence Assembly**

[Capital flows / UST demand hole. 10 findings ranked. Make invisible flows concrete: who's selling, how much, why rates stay high. Includes "The Demand Hole" summary section. Sources: TIC, MOF Japan, PBOC. Write to AGENTS/ZHAO/DECK_EVIDENCE.md]
