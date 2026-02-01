# CLAUDE.md - Trump Financial-Policy Network

## WHAT THIS IS

Political-financial intelligence project mapping conflicts of interest between Trump 2.0 officials and companies benefiting from their policy decisions. Focus on tradeable positions and documented patterns.

**Network State (approximate):** ~290 nodes | ~522 edges | ~142 catalysts | 10 clusters (C1-C7 + C10 Housing + C11 SFR/BTR + C12 Clean Beneficiaries) + SCOTUS overlay + DOGE layer
*See TSV files for exact counts*

---

## FILES

```
C:/Projects/TRUMP-NETWORK/
├── CLAUDE.md              # This file - read first every session
├── RESEARCH_STATUS.md     # Research status index - READ SECOND (prevents re-investigating closed threads)
├── handoffs/              # Handoff notes - read latest for recent context
│   ├── TRUMP-NETWORK_NNN_HANDOFF.md  # 3-digit session numbering
│   └── archived/          # Consolidated older handoffs
├── data/
│   ├── NODES.tsv          # Entities (ID|Name|Type|Cluster|Role|Policy_Control|Holdings|Tickers|Status)
│   ├── EDGES.tsv          # Relationships (ID|From|To|Type|Evidence|Confidence|Source|Date)
│   └── CATALYSTS.tsv      # Events/triggers (ID|Date|Event|Nodes|Tickers|Impact|Status)
├── dossiers/              # Deep-dive files on critical nodes
├── sources/SOURCE_LOG.md  # Source tracking
└── research/
    ├── prompts/           # Research prompts for external LLM - AUTO-GENERATE when new threads emerge
    └── results/           # User uploads external research here for analysis
```

---

## VALIDATED PATTERNS

These are the core insights. Each confirmed with multiple examples.

| Pattern | Mechanism | Examples |
|---------|-----------|----------|
| **84-Day OSC Loop** | 1789 invests → ~84-102 days → OSC loan; **SECTOR-SPECIFIC**: only works for rare earths/critical minerals, NOT defense tech or energy | Vulcan Elements (Aug→Nov 2025 = 84d); Base Power = NEGATIVE (no OSC by Day 95, residential ineligible) |
| **Reverse Signal** | DoD contract awards → THEN 1789 invests (de-risking strategy); opposite of OSC Loop causality | Firehawk: USAF Aug→1789 Sep; PsiQuantum: AFRL Apr→1789 Sep; Cerebras: DARPA Apr→1789 Sep |
| **Thiel Donor Loop** | Thiel donates to candidate → candidate runs OSC → OSC loans to Thiel portfolio | Witt ← Thiel; Anduril loan |
| **Family Firewall** | Official "divests" to sons/spouse, not blind trust | Lutnick → sons hold Tether 5%, ~$10B BTC |
| **Spouse Firewall** | Spouse retains company in regulated sector | Gibbens wife runs Trumbull (drones) |
| **Deputy SecDef Loop** | Feinberg → Cerberus → 7 defense cos → $15.9B DoD + $39B lawsuit | Ligado suing DoD; Feinberg profits |
| **Oil for Policy** | $1B ask → donations → cabinet picks → policy payoff | Hamm $1M → Burgum Interior → Venezuela |
| **Hedge Fund Pipeline** | Write investment thesis at fund → join govt → implement policy | Miran at Hudson Bay → CEA → tariffs |
| **Pre-Confirmation Pipeline** | Pitch deal before confirmation → execute after | Gelsinger → Lutnick → xLight $150M |
| **Dark Money Pipeline** | Paid op-eds from lobbyists → dark money board seats → regulatory appointment → implement donors' wish list | Zeldin: CGCN $98K → AFPI → EPA → Endangerment Finding repeal |
| **Write the Playbook** | Write policy chapter at Heritage → get appointed → implement own chapter | Vought (OMB), Carr (FCC), Burke (Ed), Szabo (EPA) |
| **Regulator-Regulated Loop** | Found consulting firm for industry → take equity in clients → get appointed to regulate them → approve their deals | Atkins: Patomak → Securitize board → SEC Chair → approves Securitize SPAC |
| **DOGE Capture Loop** | Private actor → SGE appointment (no divestiture) → root access to agency systems → cut competitors → award contracts to own companies | Musk → DOGE → SpaceX $6.7B; cuts traditional contractors |
| **Dual Access Network** | Pay $500K for transactional access (Exec Branch Club) + join elite salon (Dialog) for ideological consensus | Chamath, Sacks in BOTH networks |
| **Three-Layer Capture** | Dialog (ideology) → Executive Branch Club (transactions) → DOGE (operations) | Consensus → deals → implementation |
| **Access Marketplace** | $500K membership → Cabinet face time → policy discussions shielded → regulatory favoritism | Exec Branch Club MBS afterparty with FTC Chair, Ag Sec |
| **Starve Incumbents, Feed Insurgents** | Policy restricts legacy players (buybacks, regulations) → benefits network-connected insurgents | Defense EO squeezes primes (2.4:1 buyback/capex ratio) → Thiel/1789 defense tech benefits |
| **Quid Pro Quo Reversal** | Major donor faces ADVERSE policy despite contributions (unusual - tests hypothesis limits) | Schwarzman $45M to Trump → housing ban targets his SFR portfolio; watch for carve-outs |
| **Ethics Demolition** | Fire Chief Ethics Officer → Fire General Counsel → Fire ethics team → Create impunity for conflicts | Pulte: Fired Fannie ethics team Oct 2025 (~12 staff + CEO Libby + GC McCoy); then endorsed policy benefiting family co |
| **Policy-Profiteer (Direct)** | Family member of regulated company appointed to regulate it → publicly endorses policy benefiting family | Pulte (grandson of PHM founder, >$5M income) → FHFA Director → endorsed housing ban Jan 9 → PHM primary beneficiary |
| **Shadow Advisor** | Hold multiple senior positions without Senate confirmation → escape scrutiny/recusal requirements → approve conflicts | Witt: OSC Acting Dir + Crypto Council Exec Dir + Deputy USD(R&E) — all without confirmation; controls $200B+ |
| **Coordinated Omission** | Every official bio uses identical vague language to hide employment → suggests deliberate coordination | Witt: Every bio says "lower-middle-market PE firm" — no firm named anywhere; EcoFusion Solutions found on LinkedIn but zero public records |
| **Capital Redirection Scheme** | Ban sector A → institutional capital redirects to sector B where official has ties | Turner: Ban SFR investors → capital flows to multifamily (JPI, his $651K employer) |
| **Donor Enrichment Pipeline** | Donors fund candidate → candidate runs program → donors profit from program | Turner: Ziklag donors funded Turner → Turner ran OZ → Ziklag members profited from OZ tax benefits |
| **Ideology as Financial Cover** | Religious/nationalist rhetoric provides moral cover for pro-wealthy policies | Turner: Christian nationalist framing (WallBuilders/Prestonwood) disguises developer enrichment |
| **Personnel Exclusion** | Exclude legacy industry insiders from admin → enables adverse policy against that industry | Trump 2.0 Pentagon: zero Boeing/Raytheon/LMT execs (vs Trump 1.0 Esper+Shanahan); enables Starve Incumbents |
| **Dual Investment Strategy** | Same fund operates two distinct strategies by sector: (A) Pre-government capital for minerals, (B) Post-government de-risking for defense tech | 1789: Pre-OSC Pipeline (Vulcan→OSC loan); Proven Contractor (Firehawk, PsiQuantum, Cerebras = invest after DoD contracts) |
| **Expand-Then-Restrict** | Restart paused financing program → expand volume with network-connected players → restrict to BTR-eligible only → locks out portfolio buyers while preserving builder revenue | Housing ban: GSE SFR financing paused (Biden) → restart under Pulte → restrict to BTR only → INVH forced from portfolio buying to BTR (PHM partner) → PHM revenue preserved |
| **Clean Cover** | Include non-network-connected companies in policy benefits → use them for political theater/propaganda → legitimizes network enrichment as "merit-based reform" | Hegseth "Arsenal of Freedom" tour: Rocket Lab (Khosla-backed, anti-Trump donor) showcased as model Jan 9 2026 → provides cover for Anduril/SpaceX (network-connected) benefiting from same policy |

---

## CLUSTERS

| ID | Name | Key Figures | Domain | Primary Exposure |
|----|------|-------------|--------|------------------|
| C1 | 1789 Capital | Trump Jr, Malik, Buskirk, Masters | OSC defense loans | CLBR.U, UMAC, DOMH |
| C2 | Thiel Network + SEC | Thiel, Sacks, Witt, **Atkins, Luckey, Stephens** | DOGE, AI, crypto, SEC, defense tech | PLTR, BTGO, CEPT/SECZ |
| C3 | Lutnick/Cantor | Howard, Brandon, Tether, **Securitize** | Bitcoin, CHIPS, tokenization | XXI, CEPO, RUM, SECZ |
| C4 | Bessent/Treasury + P2025 | Bessent, Gibbens, Miran, **Vought, Navarro** | CFIUS, SWF, tariffs, OMB | - |
| C5 | Pentagon/Cerberus | Feinberg, Witt, **Homan, Miller** | Defense, OSC, border | Ligado $39B lawsuit |
| C6 | MAGA Media | Rumble, PSQH, **Carr (FCC)** | Platforms, telecom | RUM, PSQH |
| C7 | EPA/Energy | Kushner, MBS, Wright, Burgum, **Zeldin, Dunn** | Oil, PIF, nuclear, EPA | CVX, COP, LBRT, OKLO |
| C10 | Housing Policy | **Pulte (FHFA), Turner (HUD), Moreno, Vance** | GSE financing, housing regulation | - |
| C11 | SFR/BTR Transition | **Schwarzman, Rowan**, Pretium, INVH, AMH | SFR landlords (THESIS REVISED: AMH=BTR winner, INVH=BTR pivot via PHM) | INVH, AMH, BX, APO |
| C12 | Clean Beneficiaries | **Rocket Lab, Peter Beck, Khosla Ventures** | Defense/space insurgents WITHOUT network ties | **RKLB** (Tier 2 beneficiary - same policy tailwind, no conflict baggage) |

---

## TOP CONFLICTS (by dollar exposure)

| Official | Role | Conflict | Exposure |
|----------|------|----------|----------|
| Feinberg | Deputy SecDef | Cerberus 7 defense cos + Ligado suing DoD; divested to adult children trusts (Family Firewall) | $15.9B + **$39B lawsuit** |
| **Atkins** | SEC Chairman | $6M crypto (Securitize, Anchorage, Off the Chain); Patomak clients; FTX advisor; must approve Securitize SPAC (Brandon Lutnick) | **$327M net worth** |
| Brandon Lutnick | Cantor Chair | Bitcoin SPACs + Securitize SPAC (father = Commerce Sec) | ~$10B BTC + SECZ |
| Sacks | AI/Crypto Czar | Retained 449 AI investments; BitGo 7.8%; "dream team" with Atkins | Unknown |
| Kushner | Affinity Partners | $2B from Saudi PIF; zero returns; $87M fees | $55B EA deal pending |
| Miran | CEA + Fed | Wrote tariff policy at Hudson Bay; implemented it | $30B fund benefited |
| **Zeldin** | EPA Administrator | $98K CGCN op-eds; AFPI chair (Tim Dunn); Qatar consulting; implementing Dunn's wish list | Career funded by regulated |
| **Vought** | OMB Director | Project 2025 architect; wrote 350 draft EOs; coordinates DOGE; "shadow president" | Ideological, not financial |
| **Schwarzman** | NOT in govt | $45M+ Trump donor → faces ADVERSE housing ban policy (Quid Pro Quo Reversal pattern) | 55K homes via Tricon |
| **Pulte** | FHFA Director | **EXTREME**: Grandson of PHM founder; >$5M income 2024; endorsed housing ban on Fox Jan 9; FIRED entire Fannie ethics team Oct 2025; Palantir holdings + Fannie contracted Palantir; GAO investigation Dec 2025; Ethics Demolition + Policy-Profiteer patterns | **~$1.5B family stake PHM** |
| **Turner** | HUD Secretary | COORDINATOR: JPI $651K salary; attended Ziklag donor conference June 2019 while running OZ; Jeff Sandefer $115K donor; coordinates housing ban with Pulte; Capital Redirection benefits JPI | ~$883K 2024 income |

---

## RESEARCH STATUS

**See `RESEARCH_STATUS.md` for current status of all research threads.**

| Category | What It Means |
|----------|---------------|
| EXHAUSTED | OSINT exhausted - do not re-investigate without new external lead |
| COMPLETE | Fully documented - monitor for news only |
| ACTIVE | Watching for specific triggers |
| GAPS | Known unknowns that could be researched |

**Before suggesting any research direction, CHECK RESEARCH_STATUS.md first.**

---

## TICKERS

**Long candidates:** PLTR, XXI, CVX, COP, LBRT, OKLO, RUM, VLD, **CEPT**, **RKLB**
**Pending:** BTGO (IPO), CEPO (merger), CLBR.U (target TBD), **SECZ (Securitize post-SPAC)**
**Bear candidates:** UMAC, DOMH
**DOGE winners:** PLTR (+$10B Army deal), SpaceX (private, $6.7B), Anduril (private, $842M)
**Defense EO losers:** LMT, RTX, NOC, GD (-4-6% Jan 7); BA (also targeted)
**Defense insurgent (Tier 2 - Clean Cover):** RKLB ($1.3B+ SDA backlog, Golden Dome SHIELD, no network conflict)
**Housing BTR ecosystem (THESIS REVISED):** PHM, INVH, AMH - all LONG (7,500-home PHM-INVH partnership; AMH 95.7% BTR model; "ban" transforms sector, doesn't destroy it)
**Housing PE exposed:** BX, APO (Schwarzman/Rowan portfolios - portfolio buyers without BTR pivot)

*VLD (Velo3D): Defense 3D printing, Anduril/SpaceX supplier, NDAA beneficiary, Playground portfolio*
*CEPT (Cantor Equity Partners II): Brandon Lutnick SPAC; merging with Securitize → SECZ; Atkins conflict*
*SECZ (Securitize): $1.25B tokenization platform; BlackRock-backed; Atkins had board seat + options*
*PLTR (Palantir): Thiel network; $10B Army Enterprise Agreement Jul 2025; DOGE era beneficiary*
*RKLB (Rocket Lab): Clean Cover beneficiary; $1.3B+ SDA backlog; on Golden Dome SHIELD roster; Khosla-backed (anti-Trump donor); Hegseth showcased Jan 9 2026*
*INVH/AMH: SFR REITs directly targeted by Trump housing ban; watch for carve-outs*
*BX/APO: PE firms with SFR exposure; Schwarzman/Rowan are major Trump donors facing adverse policy*

---

## USER CONTEXT

**Trading philosophy:**
- Macro is chaotic; people are predictable via financial incentives
- Play both sides: long beneficiaries AND short losers
- Separate from macro thesis (KRE puts based on CRE/liquidity)
- Suspects Trump admin wants lower rates due to hidden economic weakness

**Project goals:**
- Long-term compounding knowledge base
- Understanding first, trades second
- Learning AI/LLM collaboration patterns

**Key insight:** Network may document *historical* alpha extraction - insiders capture gains before patterns visible in public filings. Goal is to get ahead.

---

## OPERATIONAL PREFERENCES

**Autonomy:** Run research threads autonomously. Report back with findings. Check in for major direction changes.

**Low-profile requirement:**
- Do NOT file FOIA requests or take actions that create paper trails
- Prefer passive monitoring over active outreach
- Research via public sources only (OSINT)
- If a thread requires FOIA to unlock, mark it DORMANT and move on

**Auto-approved tools:** WebSearch, WebFetch, Task, Bash(git *), Bash(dir *), Bash(type *)

**Documentation:**
- Update TSV files as we work (don't batch)
- Session handoffs: focus on deltas, decisions, and system changes (not full history)
- Document dead ends immediately in RESEARCH_STATUS.md
- Always note sources

**Output format for new data:**
```
N-XXX	Name	Type	Cluster	Role	Policy_Control	Holdings	Tickers	Status
E-XXX	N-From	N-To	TYPE	Evidence	CONFIRMED	Source	2026-XX-XX
```

**Evidence standards:**
- CONFIRMED = primary source (SEC, OGE 278, official announcement)
- HIGH = strong circumstantial, multiple secondary sources
- Speculative okay if flagged

---

## METHODOLOGY

**High-value sources:**
- OGE 278 disclosures (required, detailed)
- SEC filings (holdings, SPAC structures)
- Warren/oversight letters (pre-digested conflict research)
- Trade publications (details officials omit)

**Search patterns:**
- `"[Name]" OGE 278` for ethics disclosures
- `"[Company]" SBIR OR STTR contract` for government work
- `site:treasury.gov "[Name]"` for official bios

**What works:**
- Follow the money and family relationships
- Warren letters are roadmaps
- Anomalies that don't make surface sense often reveal the biggest patterns

**Pattern analysis principles:**
- **Negative controls matter:** When research clears someone (e.g., Rathje), document it - this validates the hypothesis by contrast and redirects focus to the actual node (e.g., Witt)
- **Patterns have variants:** A pattern may work in multiple directions (e.g., 84-Day Loop has Forward and Reverse variants). When discovered, update the pattern description, don't create separate patterns
- **Test predictions:** When a pattern predicts something (e.g., Hadrian OSC loan by Oct 15), track whether it occurs. Misses are as informative as hits

---

## EXTERNAL RESEARCH WORKFLOW

**Purpose:** Preserve context/tokens in main session by offloading deep research to external LLM.

**Folder Structure:**
- `research/prompts/` - Claude writes research prompts here
- `research/results/` - User uploads external research results here

**AUTO-GENERATE PROMPTS when:**
1. New policy announcement with network implications (like EOs, regulations)
2. New thread emerges that requires deep dive (company history, personnel background)
3. Breaking news on existing network nodes
4. User identifies anomaly worth investigating
5. Gap identified that would benefit from comprehensive external research

**Prompt Template:**
```markdown
# Research Prompt: [Topic]

**Date Created:** YYYY-MM-DD
**Priority:** HIGH/MEDIUM/LOW
**Status:** PENDING/IN_PROGRESS/COMPLETE
**Network Relevance:** [Which clusters/nodes this relates to]

---

[Research question and specific angles to cover]

## OUTPUT FORMAT
Structured sections with specific facts, dollar amounts, dates, names.
Cite sources. Save to: research/results/[filename].md
```

**Workflow:**
1. Claude identifies research need → writes prompt to `research/prompts/`
2. User runs prompt in external LLM
3. User saves results to `research/results/`
4. User notifies Claude → Claude analyzes and integrates into network
5. Claude updates prompt status to COMPLETE

**When analyzing results:**
- Extract new nodes/edges for TSV files
- Identify new patterns or pattern confirmations
- Flag tradeable implications
- Note any new gaps requiring follow-up prompts

---

## BOOT SEQUENCE

1. Read this file (CLAUDE.md)
2. **Read RESEARCH_STATUS.md** - CHECK EXHAUSTED SECTION BEFORE SUGGESTING ANY RESEARCH
3. Read latest session handoff in `handoffs/` (TRUMP-NETWORK_NNN_HANDOFF.md)
4. Check `research/results/` for new uploads to analyze
5. Check `research/prompts/` for pending prompts (update status if user completed)
6. Load TSV files on-demand when working

**CRITICAL:** Do not suggest re-investigating topics marked EXHAUSTED in RESEARCH_STATUS.md. These have been thoroughly researched and require non-OSINT methods (FOIA, leaks, news) to unlock.

**Proactive behavior:** When new threads or policy developments emerge during session, AUTO-GENERATE research prompts to `research/prompts/` without waiting for user to ask. Notify user that prompt is ready for external research.

**Deep history:** For full session history pre-Jan 8 2026, see `handoffs/archived/TRUMP-NETWORK_001-007_CONSOLIDATED.md`

---

## LESSONS LEARNED

Operational insights from past research to avoid repeating mistakes.

**Research Disambiguation:**
- **EcoFusion ≠ PE firm:** Witt had TWO separate roles - PE firm MD (~2021-23) and EcoFusion CEO (2023-24). Don't conflate them.
- **Name collisions are common:** "Witt" returned Arkansas billionaire W.R. Stephens Jr. Always verify target identity early.
- **Negative results are valuable:** ReElement being RULED OUT as 1789 connection validates the 84-Day Loop by providing a control case.

**Pattern Recognition:**
- **Coordinated language = coordinated omission:** When every bio uses identical vague phrasing, it's deliberate.
- **Check both Forward and Reverse patterns:** 84-Day Loop works both ways (invest→contract AND contract→invest).
- **Warren letters are roadmaps:** Her oversight letters often pre-digest the most valuable conflict research.

**System Management:**
- **Check RESEARCH_STATUS.md before suggesting research:** Prevents re-investigating closed threads.
- **Update status files as you work:** Don't batch updates - drift causes confusion.
- **Mark threads DORMANT, not failed:** If OSINT is exhausted but FOIA could unlock, it's dormant pending external exposure.

---

*For questions about Claude Code itself, use Task tool with subagent_type='claude-code-guide'*
