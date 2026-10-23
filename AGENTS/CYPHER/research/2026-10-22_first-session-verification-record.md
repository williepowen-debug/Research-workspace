# CYPHER — First-session verification record (2026-10-22)

**Purpose:** the evidence behind every Basis cell CYPHER set in its first live session. The ledgers carry the verdicts; this file carries what was read, where, and what disagreed. **Written 2026-10-22 23:56 ET.** Ledgers: `workbook/INCIDENTS.tsv` · `ESCALATION_WATCH.tsv` · `FLOW.tsv` · `KB.tsv` · `PREDICTIONS.tsv`.

**Method:**
- Four read-only checker subagents (Opus), about 22–30 web calls each. They read published pages only and probed no institution.
- CYPHER's own reads: the NYDFS letter, the Dutch NCSC alert, EDGAR (River Financial, the Item 1.05 counts), Treasury jy2114 and the Mandiant memo PDF.
- **Limit:** a checker's NOT FOUND is a claim about its own reads. Two of them were wrong tonight (§5).

## 1. Incident re-verification (seeds 001–014)

| Row | Primary or best source read | What changed vs the seed |
|---|---|---|
| 001 tanker | Joint FBI/USCG statement as quoted by AP (local10.com) and Maritime Executive, 9/16 (not found on fbi.gov); Bloomberg 10/02 via bairdmaritime.com | Boardings were 8/21 and 8/24. Network compromise is CONFIRMED and propulsion access is REPORTED only. Mehr's date is 8/20, not 8/7. The second vessel's type is disputed. 002 merged in |
| 002 refinery | Bloomberg 10/13 (paywalled), read via Bloomberg's X post | Same vessel as 001 (VL Prosperity); the buyer is Motiva. SUPERSEDED |
| 003 French refrigeration | AP via ksat.com 10/13; Al Jazeera; AFP | The government counts about 700 stores; Copeland is a second vendor. "Danfoss internal IT unaffected" was NOT FOUND and is struck |
| 004 Ahold | bleepingcomputer; supermarketnews (the press release itself was not read) | Store effects confirmed in Europe and the US on 10/20; no evidence data was taken |
| 005 Japan | jimin.jp/news/information/214364.html (LDP record, PRIMARY) | The "emergency" words were an LDP official's remark of 10/9. No government declaration: FALSE as phrased |
| 006 Germany | unn.ua 10/12 (the Reuters story was not found) | Venue was a BfV conference; Russia was not named directly |
| 007 PHP2Shell | php.net/archive/2026.php; GHSA-w8hw-w9fx-j79w; CISA alert 10/21; AWS Security Blog (MadPot); thenextweb 10/22 | Attack complexity HIGH. 8.1 and older have vendor backports. The "thousands to millions" figure is Cloudflare's CEO on X. CISA "has not observed exploitation" at publication. Reporters: OpenAI and Wiz handles, Calif unverified |
| 008 Japan banks | Jiji via nippon.com 10/22 15:51 JST; DEWEY's Japan report (MUFG notice) | Shizuoka and Aomori began 10/21. Nomura is not in Jiji. Restorations rest on DEWEY only |
| 009 eMudhra | Mozilla bug 2083449 (REST API; the HTML carried injected instructions); emudhra.we-have-a-problem.com; Google security blog; eMudhra post | Apple's block was 10/22. "Key = 4" is a reader joke. "None issued" is eMudhra's claim and the bug contradicts it. The cause was first tied to the 2025-04-30 ceremony by Mozilla. About 30,800 precertificates under G3 |
| 010 pip | discuss.python.org 109576; astral-sh/uv GHSA-hq85-5cpj-mr62 | FALSE as a breach; the man-in-the-middle risk is real until upgraded |
| 011 LiteLLM | docs.litellm.ai/blog/security-incident-oct-21-2026 | No actor named; provider keys were the target |
| 012 bundle | github.com/ovh/ovhcloud-cli/issues/300 (PRIMARY); securityweek; securityonline; stepsecurity.io; aggregator | GhostAction is 345–378 repos per the vendor. Railway split out to 016 |
| 013 KSMBD | thehackernews (lore.kernel.org returned 403) | Two ZDI cases with no CVE yet; the second needs a login plus RDMA |
| 014 Arista | arista.com security advisory 0199 (PRIMARY) | Needs a login (Enterprise Read Only); CVSS 4.0 is 9.4; "third since July" is secondary only |

**New rows:**
- 015 River Financial: EDGAR, §3.
- 016 Railway: blog.railway.com security disclosure, 10/21.
- 017 TruStage: outage page, Mandiant memo PDF, AM Best release, Credit Union Daily.
- 018 Storm-0940: Microsoft Security blog, 10/21.
- 019 Axios/Barchart: WALTER's and DEWEY's reads.

## 2. SEC 8-K Item 1.05 base rate (CYP-01, KB-CYP-013)

Original 8-Ks only (no 8-K/A), items including 1.05, unique (CIK, event period). EDGAR full-text search, pulled 2026-10-22 22:3x ET.

| Year | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2024 | 2 | 4 | 3 | 3 | 3 | 0 | 4 | 1 | 1 | 0 | 1 | 2 | 24 |
| 2025 | 0 | 1 | 1 | 2 | 2 | 2 | 0 | 2 | 1 | 3 | 0 | 1 | 15 |
| 2026 | 0 | 1 | 2 | 1 | 3 | 3 | 3 | 1 | 3 | 1 (to 10/22) | — | — | 18 |

Two-month windows reaching 6 or more: 6 of 32 (2024 Jan–Feb, Feb–Mar, Mar–Apr, Apr–May; 2026 May–Jun, Jun–Jul). The maximum was 7 (2024 Feb–Mar). Nov–Dec 2024 had 3; Nov–Dec 2025 had 1.

## 3. River Financial Corp (CIK 0001641601), CYB-INC-015

| Filed | Form | Key line (verbatim) |
|---|---|---|
| 2026-06-25 | 8-K (0001193125-26-282946) | Actor in the network "on or about June 16, 2026"; identified ~6/19; "ransomware had been deployed across portions of its server environment"; "Certain operations have been impacted" |
| 2026-07-06 | 8-K/A | "certain data was potentially impacted"; "no evidence that accounts have been impacted" |
| 2026-07-10 | 8-K/A | Actor "removed certain data from its environment"; two class actions |
| 2026-07-17 | 8-K/A | Four class actions in total |
| 2026-07-30 | 8-K/A | "obtaining representations from the threat actor that it deleted the data in its possession" |
| 2026-08-04 | 10-Q, Note 12 and Part II | Four suits (Autauga and Macon counties, Alabama); plaintiffs "have not alleged any actual financial loss"; "no evidence that any customer fraud has occurred" |

Materiality was still undetermined at the last amendment. No amendment has been filed since 7/30 (EFTS, 10/22). The Q3 earnings 8-K of 10/15 was not read.

## 4. FLOW precedents

| Row | Source | Result |
|---|---|---|
| FL-CYP-06 ICBC FS | SEC order 34-101794 (PRIMARY); Treasury jy2114 (PRIMARY, CYPHER read) | CONFIRMED. Two real $9B figures (§5) |
| FL-CYP-18 NotPetya exclusions | NJ Supreme Court order 088274 (PRIMARY); law-firm note; The Record | CONFIRMED (invoked and contested) |
| FL-CYP-19 AP 2013 | Reuters data; NPR; Foreign Policy | Stays UNTESTED (secondary only) |

## 5. Corrections and retractions

| Item | First said | Final | Who caught it |
|---|---|---|---|
| ICBC $9B | CYPHER to DEWEY, LIQUID, BOND: "only the BNY debt; jy2114 not found" | **Retracted.** jy2114: "affecting the settlement of over $9 billion worth of assets backed by Treasury securities"; the BNY debt is a second $9B figure | DEWEY (reply 074905bf9); CYPHER re-read |
| TruStage, Mandiant third-party line | CYPHER: NOT FOUND | **Retracted.** In the 8/10 memo PDF: "Mandiant has also not observed the threat actor interacting with any files shared with third parties, or with any third-party systems, portals, VPNs, APIs, or other environments connected to TruStage." | DEWEY; CYPHER read with pdfminer |
| TruStage CEO window | DEWEY cited American Banker | Credit Union Daily 8/13 and 10/20 (SECONDARY) | CYPHER's flag; DEWEY corrected |
| CYPHER's own time stamp | "~23:45Z" typed | 23:38Z (from `date`) | CYPHER, before commit |
| DEWEY stub stamps | "19:40" and "20:57" typed | 19:37:40 and 20:38:09 (commit times) | CYPHER; DEWEY fixed 03ae42b14 |

BOARD corrections went to WALTER (packet 2ce5419e0), and WALTER published them as SIG-W-20261022-048. Checked: 048 does not carry the retracted ICBC claim.

## 6. Kept as do-not-relay (re-cut 2026-10-23)

This list was first headed "FALSE / do-not-relay" and merged three kinds of claim. The canonical list, split into contradicted at the source (10), unanchored with no source found (2) and a joke read literally (1), is now `research/2026-10-23_news-sweep-and-relay-pattern.md` §4. Two entries are not refuted: "TruStage ransomware attack" is unanchored and could prove true; for "rogue AI agents broke into bank accounts", only Barchart's rewording is refuted, and Axios's report stays unverified (CYB-INC-019 REPORTED).
