# If a government attributes a cyberattack to a state, can cyber insurers deny claims? State-backed exclusions, attribution and the size of the channel
**Date:** 2026-10-22 (research 21:35–21:45 ET) | **Mode:** Thesis | **Confidence:** High on clause mechanics (read from the Lloyd's Market Association clause PDFs and the Lloyd's bulletin); Medium on precedents (news-sourced rulings); Low on market adoption (no survey found)
**Commission:** Will-directed in the DEWEY session, 21:33 ET (Will's pick #3). No REQ. Tests CYPHER FLOW `FL-CYP-18` (government attribution → state-attack/war exclusions invoked → insured recoveries contested; UNTESTED). Live referent: Microsoft's 21 Oct vendor attribution of the ConnectWise Cloud Backup compromise to China-aligned Storm-0940 (no government attribution as of 22 Oct).

## Key Finding
**Government attribution alone would NOT let most cyber insurers deny claims, because most of the market's exclusions need more than attribution.**
- **Lloyd's has required state-backed cyber exclusions since 31 Mar 2023** (Bulletin Y5381). Three of the four model clauses (LMA5565A–5567A) exclude a non-war state attack **only if it makes a state an "impacted state"**, meaning a "major detrimental impact" on its functioning via an essential service, explicitly including "financial institutions and associated financial market infrastructure", or on its security or defence.
- **Only Clause 1 (LMA5564A) excludes every state cyber operation**, including data copying or removal. Under that clause, attribution alone decides the claim.
- **Attribution is evidence, not a trigger.** The 2023 wording says the parties "will consider such objectively reasonable evidence", which "may include" a government attribution. The insurer keeps the burden of proof.
- **The 2021 "no loss shall be paid" pending-attribution freeze was withdrawn** in the 2023 versions.
- **Outside Lloyd's**, many policies still carry old war wording ("identical or close to the NMA464", Simmons & Simmons, Mar 2026). *Merck v. Ace* (NJ App. Div., 1 May 2023) held that wording "does not apply unless there is some military action".
- **No reported case of an insurer invoking the new state-backed exclusions** was found for 2023 to Oct 2026.
- **Channel size:** US cyber direct premiums ≈ **$9.46B (2025)**, loss ratio 53 (NAIC). Global ≈ $15–16B (Munich Re, as reported).
- **For ConnectWise/Storm-0940:** even if a government endorses Microsoft's attribution, the exclusion bites under Clauses 2–4 only if the incident disrupted US finance at a *national* level. Microsoft reports no successful authentication in the spray and names no victims. **The channel is real for a NotPetya-scale event, and marginal for this one.**

## Evidence

### 1. Clause mechanics (LMA PDFs, read by the helper; PRIMARY)

| Clause | Excludes (beyond war) | Attribution | Pending period | Insured's systems outside the impacted state |
|---|---|---|---|---|
| LMA5564A (Clause 1, Jan 2023) | **All** state cyber operations, incl. "copy, remove" of data | "Objectively reasonable evidence… may include formal or official attribution by the government of the state in which the computer system… is physically located" | None | n/a |
| LMA5565A (Clause 2) | Operations in war or its "immediate preparation", or that make a state an impacted state; **other state operations capped at a sub-limit** (blank = no cover) | Same | None | Not in the excerpts read |
| LMA5566A (Clause 3) | Same as Clause 2, without the sub-limit carve-back | Same | None | Not in the excerpts read |
| LMA5567A (Clause 4) | Same as Clause 3 | Same | None | **Cover given back** for the insured's systems outside the impacted state |
| "B" versions | Same exclusions; **no attribution paragraph** | — | — | Need Lloyd's prior agreement (DAC Beachcroft, INSTITUTIONAL) |
| Original 2021 LMA5564–5567 (withdrawn) | Similar; Clause 4 named retaliatory operations between China, France, Germany, Japan, Russia, UK and USA | Government of the system's location = "primary but not exclusive" factor | **"It is agreed that during this period no loss shall be paid"** | Clause 4: "bystanding cyber asset" carve-back |

- **Lloyd's Bulletin Y5381** (dated 17 Aug 2022 in the PDF; law firms say 16 Aug): from 31 Mar 2023, standalone cyber policies must exclude state-backed attacks that "significantly impair the ability of a state to function", state whether systems outside the affected state are covered, and set out "a robust basis… [for] attribution". PRIMARY (Lloyd's Y5381 bulletin PDF on assets.lloyds.com, helper read; exact URL not captured). *The bulletin's text and its embedded link name different model-clause references (LMA21-043-PD vs -042-PD); carried, not resolved.*
- **Bulletin Y5433 (June 2024):** extended the rule to multi-line policies with a cyber section and introduced seven clause "Types"; Type 7 is barred from 1 Jul 2024. INSTITUTIONAL (DAC Beachcroft summary; the bulletin itself was not opened).

### 2. Precedents

| Case | Wording | Outcome | Basis |
|---|---|---|---|
| *Merck v. Ace American* (NJ) | Property "Hostile/Warlike Action" exclusion; NotPetya, ~$1.4B loss, $699.5M disputed | Trial court Jan 2022; **App. Div. 1 May 2023:** exclusion "does not apply unless there is some military action". Settled ~8 Jan 2024, terms confidential | NEWS ([Claims Journal](https://amp.claimsjournal.com/news/east/2023/05/04/316786.htm)); settlement not confirmed from a court filing |
| *Mondelez v. Zurich* (IL) | War exclusion; >$100M | Settled during the jury trial, late Oct/early Nov 2022; no ruling | NEWS |
| 2024–26 | — | **No case on the new state-backed clauses found** | INSTITUTIONAL ([Simmons & Simmons, 26 Mar 2026](https://www.simmons-simmons.com/)) |

### 3. Has anyone invoked it?
None found for 2023 to 22 Oct 2026, including after Volt Typhoon and Salt Typhoon. SEARCH-NOT-FOUND. Simmons & Simmons expects insurers to advance response costs under reservation of rights, which means disputes may be private rather than absent.

### 4. Attribution timing (how long the "pending" window lasts)

| Event | Government attribution | Lag |
|---|---|---|
| NotPetya (Jun 2017) | US/UK → Russian military, Feb 2018 | ~7.5–8 months |
| SolarWinds (Dec 2020) | "Likely Russian", Jan 2021; formal US/UK → SVR with sanctions, 15 Apr 2021 | ~3 weeks provisional / ~4 months formal |
| Microsoft Exchange / Hafnium (Mar 2021) | US/EU/UK/NATO → China's Ministry of State Security, 19 Jul 2021 | ~4.5 months |
| Salt Typhoon (Sep–Oct 2024) | FBI/CISA "affiliated with" China, Oct 2024; joint statement 13 Nov 2024 | ~1–2 months |
| ConnectWise / Storm-0940 (Oct 2026) | Microsoft only (vendor), 21 Oct 2026 | pending |

All timing rows are NEWS, helper-sourced. The destructive events were the slow ones.

### 5. Channel size
- US cyber premiums 2025 ≈ **$9.46B**, +3.5% year on year; loss ratio 53 (2024: 48.7). PRIMARY (NAIC 2026 cybersecurity insurance market resource-center page on content.naic.org, helper read; exact URL not captured; PDF not downloaded). A 2024 split ($9.14B total vs $7.075B US insurers only) was seen in summaries and not verified.
- Global ≈ $15.3B (2024), ~$16.3–16.4B (2025 forecast), Munich Re as reported (NEWS; not on the Munich Re page opened).
- **Share of policies with state-backed vs old war wording: no survey figure found.** Marsh (2022): "Attribution… should not automatically trigger an exclusion" (INSTITUTIONAL).

### 6. CYPHER FLOW `FL-CYP-18` read
The mechanism exists in policy wording but has **0 observed invocations in 3.5 years**. Suggest it stays UNTESTED, re-phrased to the actual condition: "government attribution **plus impacted-state-scale disruption** (Clauses 2–4) **or** a Clause-1 policy". On that test, the ConnectWise/Storm-0940 case fails the scale leg.

## Counter-Evidence
- **For a bigger channel:** Clause 1 policies (all state operations, including data theft) would turn a government attribution of a data-theft campaign directly into denials, and their market share is unknown. Merck binds only New Jersey and never reached its supreme court. Insurers may reserve rights quietly, which would keep disputes invisible. The financial-market-infrastructure language in "essential service" means a large bank or payments disruption *could* qualify as an impacted-state event.
- **For a smaller one:** the burden stays on insurers. The freeze clause was withdrawn. Old war wording loses after Merck. There have been 0 reported invocations, and markets have so far preferred to settle (Mondelez, Merck).

## Source Quality Assessment
Strong: the LMA clause texts and Y5381 (primaries). Medium: precedents (news) and NAIC (resource page, not the PDF). Weak: adoption shares (none), the Y5433 mapping, and the global premium (relayed).

## References
- LMA clause PDFs (LMA5564A/B, 5565A, 5566A, 5567A/B; 2021 LMA5564/5567): lmalloyds.com `/wp-content/uploads/2025/09/<id>-1.pdf`
- Lloyd's Y5381: Market Bulletin PDF on assets.lloyds.com (exact URL not captured)
- DAC Beachcroft, 30 Jan 2023 and 10 Jun 2024: https://www.dacbeachcroft.com/
- Simmons & Simmons, 26 Mar 2026: https://www.simmons-simmons.com/
- Marsh, 21 Aug 2022: https://www.marsh.com/
- Claims Journal (Merck): https://amp.claimsjournal.com/news/east/2023/05/04/316786.htm
- NAIC 2026 cybersecurity insurance market resource-center page: content.naic.org (exact URL not captured)
- Microsoft Storm-0940: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/

## Process Report
**Searches run:** one helper (33 tool calls, 14 searches, DATA-RETURN, no repo writes); clause PDFs extracted to scratch.
**Data gaps:** adoption shares, Lloyd's share of the cyber market, the Y5433 text, whether in-force policies still carry the 2021 freeze wording, the Merck settlement filing, Volt Typhoon timing.
**Source frustrations:** the NAIC PDF was too large for WebFetch.
**Confidence in findings:** High on the mechanics, Low on how much of the market each clause covers.
**If I had more time/tools:** broker data (Marsh/Aon) on clause adoption; the SHADE desk's own insurer filings for wording.
**Suggestions:** SHADE could ask which clause its watched insurers file (state filings / SERFF for US admitted cyber forms).
