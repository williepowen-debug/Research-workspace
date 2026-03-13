# Deck Project — Agent Prompts

Stored here so we can iterate on the template and track what we sent.

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
