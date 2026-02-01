# CLAUDE.md - Trump Administration Financial-Policy Network

## PROJECT OVERVIEW

This is a political-financial intelligence research project mapping conflicts of interest between Trump 2.0 administration officials and companies benefiting from their policy decisions. Focus on tradeable positions and documented patterns.

**Current state:** 94 nodes, 124 edges, 55 catalysts across 7 clusters.

## FILE STRUCTURE

```
NETWORK_CORE.md     # Full reference - READ THIS FIRST for any substantive work
data/
  NODES.tsv         # Entity records (ID|Name|Type|Cluster|Role|Policy_Control|Holdings|Tickers|Status)
  EDGES.tsv         # Relationships (ID|From|To|Type|Evidence|Confidence|Source|Date_Added)
  CATALYSTS.tsv     # Events/triggers (ID|Date|Event|Nodes|Tickers|Expected_Impact|Status)
dossiers/           # Deep-dive xlsx files on critical nodes
sessions/           # Session handoff documents
sources/
  SOURCE_LOG.md     # Structured source tracking (Date|Type|URL|Nodes|Summary)
```

## WORKING PROTOCOL

1. **Starting substantive research:** Read NETWORK_CORE.md first - it has full context, patterns, gaps, methodology
2. **Adding entities:** Load NODES.tsv, use next available N-XXX ID
3. **Adding relationships:** Load EDGES.tsv, use next available E-XXX ID
4. **Discussing catalysts/timing:** Load CATALYSTS.tsv
5. **Deep dives:** Check dossiers/ for existing research on specific people

## QUICK REFERENCE

**Top 5 Conflicts:**
| Official | Role | Conflict | Exposure |
|----------|------|----------|----------|
| Feinberg | Deputy SecDef | Cerberus 7 defense cos + Ligado suing DoD | $15.9B+ DoD + **$39B lawsuit** |
| Brandon Lutnick | Cantor Chair | Bitcoin SPACs (father = Commerce Sec) | ~$10B BTC |
| Sacks | AI/Crypto Czar | Retained 449 AI investments | Unknown |
| Witt | OSC Director | Unknown PE firm + Thiel donor | $5B+ loans |
| JR Gibbens | Treasury SWF | Wife's drone company | Unknown |

**Validated Patterns:**
1. 1789 Capital invest → 84 days → OSC loan (Vulcan, Anduril confirmed)
2. Thiel donor → OSC loans to Thiel portfolio
3. "Family Firewall" - divestiture to sons/spouses, not blind trusts
4. "Spouse Firewall" - officials' spouses retain companies in regulated sectors
5. Deputy SecDef Portfolio Loop - Feinberg/Cerberus/7 defense cos
6. Oil for Policy Exchange - $1B ask → Hamm organizes → Burgum leads Venezuela

**#1 Gap:** Patrick Witt's PE firm name (2021-2024) - extensive research done, requires FOIA

**Clusters:**
- C1: 1789 Capital (Trump Jr, Malik) - OSC defense loans
- C2: Thiel Network (Thiel, Sacks, Witt) - DOGE, AI, crypto, defense
- C3: Lutnick/Cantor (Howard, Brandon, Tether) - CHIPS, CFIUS, Bitcoin
- C4: Bessent/Treasury (Bessent, Gibbens) - CFIUS, SWF
- C5: Pentagon/OSC (Feinberg, Witt, North Wind) - defense loans, hypersonics
- C6: MAGA Media (Rumble, PSQH) - platforms
- C7: Saudi/Energy (Kushner, MBS, Wright) - oil, PIF investments, nuclear

## ACTIVE TICKERS

**Long candidates:** PLTR, XXI, BTGO (pending), UBER, CEPO (pending), RUM, CLBR.U, CVX, COP, LBRT, OKLO
**Bear candidates:** UMAC, DOMH

## CURRENT PRIORITIES

1. FOIA campaign: Witt PE firm, Gibbens ethics disclosures
2. Track BSTR Holdings merger close
3. Monitor BitGo IPO timing
4. Build out DOGE personnel → Thiel connections
5. Map Trumbull government contracts (USASpending deep dive)

## METHODOLOGY

**High-value sources:**
- OGE 278 disclosures (required, detailed)
- SEC filings (public holdings, SPAC structures)
- FEC records (donor relationships)
- Warren/oversight letters (pre-digested conflict research)
- Trade publications (CoinDesk, DroneLife - details officials omit)

**Search patterns:**
- `"[Name]" OGE 278` for ethics disclosures
- `"[Company]" SBIR OR STTR contract` for government work
- `site:treasury.gov "[Name]"` for official bios

**Dead ends to avoid:**
- USASpending web search (need direct database query for dollar values)
- SBIR.gov (shows existence, not amounts)
- Ethics watchdog sites for Witt (no active investigations)

## OUTPUT FORMAT

When adding data, provide TSV-ready rows:
```
N-XXX	Name	Type	Cluster	Role	Policy_Control	Holdings	Tickers	Status
E-XXX	N-XXX	N-XXX	TYPE	Evidence	CONFIRMED	Source	2025-XX-XX
```

## USER CONTEXT

**Trading Philosophy:**
- Macro is chaotic; people are predictable when you understand their financial incentives
- This network maps incentive structures to anticipate policy-driven moves
- Separate from macro thesis (regional bank puts on KRE etc. based on CRE/liquidity stress)
- Play both sides: long beneficiaries AND short losers - pragmatic profit-seeking
- Suspicion: Trump admin may want lower rates due to hidden economic weakness (suppressed data as evidence)

**Project Goals:**
- Long-term compounding knowledge base, not just immediate trades
- Secondary goal: Learning effective AI/LLM collaboration patterns
- Build infrastructure that grows more valuable over time
- Trades prioritize "what's next" but not required - understanding comes first

**Key Insight:** Network may document *historical* alpha extraction - insiders capture gains before patterns visible in public filings. Goal is to get ahead of this.

## OPERATIONAL PREFERENCES

**Autonomy:** Run with research threads autonomously, report back with findings. Check in for major direction changes.

**Auto-Approved Tools:** Use without requiring user approval:
- WebSearch, WebFetch (all domains)
- Grep, Glob, Read, LSP
- Task (subagents for research)

**Documentation:**
- Update NETWORK_CORE.md and CLAUDE.md as we work (don't wait for user to copy/paste)
- Document dead ends so we don't repeat failed searches
- Session handoffs go in sessions/ folder

**Sources:**
- Always note source for accountability
- Save key sources to sources/ folder
- SOURCE_LOG.md tracks: Date | Source | URL | Nodes Affected | Summary
- Optimize for LLM readability, not just human - structured, not blob

**Evidence Standards:**
- CONFIRMED = primary source (SEC, OGE 278, official announcement)
- HIGH = strong circumstantial, multiple secondary sources
- Speculative nodes okay if flagged - can validate later

**Output:** Provide TSV-ready rows when adding data. Prose for exploratory analysis.

## DEAD ENDS LOG

| Date | Target | What Was Tried | Result |
|------|--------|----------------|--------|
| 2025-12-XX | Patrick Witt PE firm | DoD bio, WH announcements, ETHDenver, CoinDesk, CFG Foundation, FEC, Roll Call, Ballotpedia, IQ.wiki | All use identical vague "lower-middle-market PE firm" language. Deliberate omission. Requires FOIA. |
| 2025-12-XX | Trumbull contract values | USASpending web search, SBIR.gov | Shows existence but not dollar amounts. Need database query. |
| 2025-12-XX | Witt ethics investigations | CREW, POGO | No active investigations found. |

---
*For full context, patterns, and research state: read NETWORK_CORE.md*
