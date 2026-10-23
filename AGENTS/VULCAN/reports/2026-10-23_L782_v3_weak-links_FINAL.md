# L782 v3 FINAL — AI-infrastructure financing: where does the chain break first?

**Written:** 2026-10-23, session start 14:37 ET (stamps from `date`; prices intraday 14:39 ET unless marked close) · **Owner:** VULCAN (DOCKET L782, lead, due 2026-10-24) · **Session:** Will-launched direct boot (Claude Code, Opus 5.5).
**Status: COMPLETE.** Every PENDING cell from v1/v2 is now filled or explicitly date-deferred. LIQUID's owner figures arrived 10/22 ~19:40 ET (packet `inbox/processed/2026-10-22_from-LIQUID_L782-three-figures.md`) [KB-270].
**Supersedes for current use:** `reports/2026-10-22_L782_v2_weak-links.md` (v2, kept as the record; its ranked table, reasoning and sources still apply except the cells changed below). No trade, threshold or score change is made here.

## Bottom line

**Unchanged: the chain breaks from the bottom, at delivery, not at the paying hyperscalers — and the credit market now agrees in numbers.** LIQUID's fund evaluations put CoreWeave's unsecured bonds at 80–86 cents (yields 14.4–15.1%, 10/21), while DEWEY finds the secured compute-SPV notes (Applied Digital, TeraWulf, Cipher) barely moved: the stress sits in unsecured parent debt, not in lease-backed structures [KB-270, KB-274]. Oracle is wide (5-year CDS 315–320bp, about the high-yield index) but has not been cut to junk: no October rating action [KB-270]. The only AI-tenant data-centre bond (Lambda, $301M) failed to sell at a ~50bp premium — an access signal, not a loss. **High-yield widening (+80bp since late summer, HY OAS 340bp 10/22) is mostly broad; the AI leg is ~3bp of the last +24bp** [KB-274]. **S5: no new qualifying event — S5 4, n=2, composite 15/25.** SK hynix's Solidigm IPO halt (10/23) is not scored: no application ever existed [KB-271].

## Changes since v2 (10/22 13:34 ET)

| # | Row | v2 cell | v3 cell | Source / tier |
|---|---|---|---|---|
| 1 | 2 CoreWeave parent | 2031s 79.46c (10/20 · T3); 2032 YTW 15.15% (10/16); **2030s basis conflict PENDING** | **Jun-2030 85.76 / 14.44% · Feb-2031 81.75 / 14.91% · Oct-2031 81.74 / 15.12% · Jul-2032 80.04 / 14.91%** (HYG vendor evaluation as of 10/21 · T2 LIQUID). **91.3c (10/15) UNRECONCILED** — matches no fund evaluation; treat as a different instrument or stale print. Bloomberg 10/20 prints sit 1–3 pts below, consistent with a down-day trade. CUSIP not established on a primary (Reg S ISIN only). Equity **$54.99, −1.10%** (10/23 14:39 ET · T1); 10/22 close **$55.60, −10.06%** | LIQUID [KB-270]; fetch.py |
| 2 | 4 Oracle parent | CDS ~280bp (10/15) / 322bp label (10/19); **LIQ-069 PENDING** | **5Y CDS 320bp / 315bp disseminated (10/21, DTCC · T2 LIQUID); 314bp (10/22, DTCC, PROME theme home).** GATE-LIQ-069 **2-of-2 FIRED, unchanged**; fallen-angel ladder **R1 NOT FIRED** (no October agency action; S&P BBB−, Moody's Baa2 negative, Fitch BBB). Equity **$127.78, +1.78%** (10/23 · T1). Long bonds ~+70–80bp since late summer, about in line with HY (DEWEY) | LIQUID [KB-270]; DEWEY [KB-274]; `PROME/themes/ellison/` |
| 3 | 8 DC CMBS/ABS | current spread **PENDING** | **No dated clearing level reachable** (Trepp/Intex/Bloomberg paid — UNREACHABLE, not absent). Anchors: Lambda SASB AAA guided **S+225 (~9/22) and NOT SOLD as of 10/21**; CREFC generic floating SASB AAA **S+175 (10/16)**; Barclays ~165bp (~9/14 · T3). ⇒ ~50bp DC premium at guidance that did not clear = access signal. **Correction (COR-20261022-27):** v2's "no BDC found" is wrong — Barings BDCs held a BB− class (since exited); private-credit loans ~$0.69B (Ares, Cliffwater); no stress in the KBRA/DBRS perimeter (~25 deals, upgrades only) | LIQUID; DEWEY v2 COMPLETE [KB-270] |
| 4 | 9 Meta | CDS record 114.5 Markit / ~119.3 ICE | **DTCC 105bp (10/19) · 111bp (10/20) disseminated; Markit 114.5 and ICE ~119.3 are two vendors at two moments (ICE = 10/22 intraday high), not a disagreement.** Equity **$644.16, −0.72%** (10/23 · T1) | LIQUID [KB-270] |
| 5 | Index backdrop | HY OAS 327bp (10/21) | **HY OAS 340bp (10/22, FRED first-published), +13bp in a day.** DEWEY: of +80bp (260→340), 65% came in September's broad selloff; October's AI leg (CoreWeave ≈ +230bp, SoftBank ≈ +100) is ≈ 3bp of the ≈ +24bp since 10/13. CCC ~1,340, widest since July 2020 = the open question | fetch.py; DEWEY [KB-274] |
| 6 | Third-event candidates | — | **SK hynix / Solidigm halted its pre-IPO and IPO review (10/23, primary)** on market conditions; Korean regulator dual-listing concern (press). Not PULLED under the 10/09 letter: no application, no launched deal, issuer is a memory maker. Recorded, not scored [KB-271] | news.skhynix.com |
| 7 | Unverified | — | Search summary: "Bernstein cut CRWV to $51; facilities cover ~$9B of ~$85B needed for existing contracts." **Not found** in either article fetched ⇒ UNVERIFIED, not carried as a figure; flagged to LIQUID/BROCK [KB-273] | WebSearch 10/23 |

**Ranking unchanged from v2** (1 merchant developers and neoclouds without an IG tenant · 2 CoreWeave parent · 3 Oracle-tenanted project debt · 4 Oracle parent · 5 SoftBank · 6 labs (OpenAI, Anthropic) · 7 private-credit funds/BDCs · 8 DC CMBS/ABS · 9 Meta/Hyperion · 10 MSFT/GOOGL/AMZN). The LIQUID cells strengthen rows 2 and 8's placement: row 2's unsecured paper is the widest priced AI-infra credit; row 8's only non-IG deal failed on access, not loss.

## S5 implications, in figures

| Registered S5 test | Status 10/23 | Note |
|---|---|---|
| New issue **+150bp** over talk or **PULLED** (incl. withdrawn IPO/listing application) | **No qualifying deal.** Solidigm: review halted, never filed ⇒ NOT SCORED. Lambda SASB: unsold at 10/21 (not withdrawn on record); qualification **UNDETERMINED** (landlord sponsor, AI tenant) — goes to Will if it is reported pulled | count stays **n=2** (Firmus, Volta) |
| **2nd jurisdiction** IG tariff threshold | Still 1 (Wisconsin PSC) | Xcel/SPS pending |
| Developer **fails to post** mandated collateral | None | — |

**S5 4 · n=2 · composite 15/25 — unchanged.**

## §6 — Date-deferred past 10/24 (stated, not carried silently)

| Item | Owner | Date |
|---|---|---|
| BDC DC-loan marks in Q3 schedules of investments | BROCK | early–mid Nov |
| CoreWeave Q3 10-Q (cash bridge, principal) | VULCAN | ~11/09 modeled |
| NextDC capex review | VULCAN watch | AGM 11/20 |
| Lambda SASB final outcome | VULCAN watch / DEWEY | trade press only |
| Jupiter post-force-majeure loan level | LIQUID/BROCK — no free source | UNKNOWN |
| Anthropic public S-1 | VULCAN watch | not filed |

## Sources (new in v3)

- LIQUID packet 2026-10-22 ~19:40 ET; evidence `AGENTS/LIQUID/research/2026-10-22_after-close/REPORT.md` §4, `hyg-coreweave-receipt.json`.
- DEWEY `AGENTS/DEWEY/output/2026-10-22_data-center-abs-cmbs-holders.md` (v2 COMPLETE, e8d1e823f) and `AGENTS/DEWEY/output/2026-10-23_hy-widening-ai-vs-broad-decomposition.md`.
- SK hynix newsroom, "Solidigm to Discontinue Review of Potential IPO…", https://news.skhynix.com/en/fact-12/ (fetched 2026-10-23 ~14:45 ET).
- PROME theme home `PROME/themes/ellison/` (Oracle CDS 314bp 10/22 DTCC; reader reports A, B, J) — cited by file per PROME's 10/23 ask.
- Live: `FORGE/tools/market-data/fetch.py price …` 2026-10-23 14:39 ET; `fetch.py fred BAMLH0A0HYM2 --first-published` (340bp obs 10/22).
