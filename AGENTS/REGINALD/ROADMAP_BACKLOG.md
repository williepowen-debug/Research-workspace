# REGINALD — INVESTIGATIONS BACKLOG (cold half of `ROADMAP.md`)

**SPLIT 2026-09-02** out of `ROADMAP.md` under `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rule 4(b). Moved **verbatim**, contiguous, crc32 `6d6ce8a5`, 6,229 B.

**NOT a boot read.** By its own definition this is *"research / deep-dive ideas not yet started — pull from here when there's a research session and no urgent catalyst."* Nothing here is dated or owed, so a session pays for it at every boot and acts on it almost never. **Pull it deliberately when starting research; do not wire it into a boot step.**

⚠️ **Rule 7 — dated re-trigger, not a leanness claim: re-check this file's size at any append, or on 2026-10-02, whichever is first.**

**Verify the split was verbatim (rule 11 — recompute):**
```
python3 - <<'EOF'
import zlib
s=open('AGENTS/REGINALD/ROADMAP_BACKLOG.md',encoding='utf-8').read()
m='<!--BL-'+'BODY-->'
print(format(zlib.crc32(s.split(m,1)[1].split(m,1)[0].encode())&0xffffffff,'08x'), '== 6d6ce8a5')
EOF
```

---

<!--BL-BODY-->## INVESTIGATIONS BACKLOG
*Research / deep-dive ideas not yet started. Each: what / why / scope. Pull from here when there's a research session and no urgent catalyst.*

| Topic | Why interesting | Scope |
|-------|-----------------|-------|
| 🟡 **Sponsor-serviced securitizations as bank-facility EODs** (DEWEY CRMT playbook 8/27: ABS ring-fenced for payment, cross-defaulted for CONTROL via servicer-termination events, §8.1(p)) | Do any bank-syndicate credits I cover carry the same construction? If yes, an ABS servicer event is a bank-facility EOD where exposure maps don't look. n=1 today; base-rate before building. | 2026-09-01 |
| **★ Bank-credit instrument gap — no CDS, no financials-sector OAS** (opened 7/30, bank-side HY attribution) | I can read the bank channel through equity + quarterly fundamentals, but **not through bank credit** — and on 7/30 the bank-credit leg was the *discriminating* datum (bank preferreds flat-to-up while HY widened +19bp; WAL equity −3.53% with WAL-PA +0.10% same session). **FRED hosts no financials-sector OAS** — series search run 7/30, the ICE BofA family there is **rating / maturity / EM only**; don't re-run it. No free bank CDS feed found. Current stand-in = listed junior-sub/preferred basket (ZIONP·HBANM·OZKAP·TFC-PR·WAL-PA·VLYPP·VLYPO·CFG-PE·HBANL·KEY-PI) + PFF + IG-index ceiling + fin-CP/SOFR/discount-window; workable but thin/low-beta, hence conf 0.8 not 0.95. **Scope:** (a) ask PROME/LIQUID whether the fleet has a paid credit source; (b) if not, script the preferred basket into `scripts/boot.py` as a standing daily read. | Quick-Medium |
| **"Juris banking" — what is it** (carried from SCRATCH 5/1) | Named repeatedly in WAL Q1 transcript as the "real surprise driver"; still no KB row capturing the business / counterparty / monetization. | Quick |
| **WAL Investor Day Slide 113 stress test** (carried from SCRATCH 5/15-17) | 5.3% total loan-loss rate under 2026 severely-adverse, CET1 stressed to 9.0% — *exceeds* v2.2 Bear-fast assumptions. Mgmt pre-positioning "we can absorb worse than bears model." Cross-check vs SCENARIOS bear legs. | Quick-Medium (pairs with SCENARIOS EV refresh) |
| **WAL Investor Day Slide 89 NDFI peer chart** (carried from SCRATCH 5/15-17) | "13% 12% 12% 11%" chart text vs 10-Q's 25.2%-of-HFI / 7.9% Business+PE — likely different denominator. PDF deck would resolve. | Quick, low priority |
| **Apollo Atlas SP warehouse counterparty mapping** | $7.155B WAL warehouse exposure + Atlas SP $6.9B PFSI 78% concentration = transmission landing point analysis. APO May 6 print may surface. WAL/CFG/MTB/etc. exposure to Atlas SP needs explicit mapping. | Medium (1 session, possibly cross-agent with BROCK) |
| **Cantor mortgage-fraud-policy precedent** | WAL Cantor recovery cited mortgage fraud insurance policy. Industry precedent? Other banks reaching for same? Insurance industry exposure to bank-loan-fraud claims at scale? | Quick-Medium |
| **First Brands transmission landing at peer banks** | Jefferies took $17M Q1; WAL silent in Q1 — where else did the loss land? PE/credit fund chain analysis (BROCK has primary). | Medium (cross-agent) |
| **Sector silence pattern as data — meta-thesis on disclosure quality** | WAL Apr 21 + RITM Apr 28 both went silent on broader sector stress. Reliability of "silence = no material exposure" needs Q2 print confirmation. Develop disclosure-quality scoring framework. | Medium |
| **Cohort fade pattern continuation** | 12/12 in Q1. Does Q2 break the model? If yes, why; if no, when does this become consensus? | Light tracking; Q2 print monitoring (~late Jul) |
| **Hidden CRE methodology v2** | If banks migrate classification again post-MI3 (mark-to-model, off-balance-sheet), need new screening method. Track Q1/Q2 RC-C composition shifts beyond Memo Item 3. | Medium |
| **DEF 14A pass (~90pp WAL proxy)** | Audit fees YoY (RSM hours up?), governance signals, audit committee composition, RSM 32-yr tenure | One session post-Wave 2 |
| ~~**Cross-bank Hidden CRE comparison v2**~~ ✅ **DONE 2026-08-13 — superseded by the cohort re-run** | The backlog item read *"update the Mar-25 baseline screen (WAL 24.2%, OZK 37.6%, EGBN 23.7%) with Q1-26 Call Report data"*. **Executed, and two of those three anchors did not survive it:** OZK's `37.6%` is **KILL-ON-SIGHT** (no reproducible provenance at any quarter; live 9.35% legacy / 5.46% uniform, rank 5 of 14, dollars −64% YoY), and the **`>20%` flag the screen was built around is RETIRED** (non-comparable basis; `registry/NOTES.md` 2026-08-13). WAL 24.2% and EGBN 23.7% both reproduce to 2dp at the 12/31/2025 vintage. Canonical → `reports/2026-08-13_MI3_cohort_rerun.md` · `workbook/MI3_COHORT.tsv` · `workbook/MI3_COHORT_SUMMARY.md`. | Nothing owed on this row. Successor questions are on the two live MI3 threads above. | RESOLVED 2026-08-13 |
| **Office maturity wall — bank-by-bank quantification** | WAL $946M known; need similar for OZK/CFG/SSB/EGBN. Bridge structure exposure mapped against 2026 maturity calendar. | Medium |
| **Convergence Day pricing decay analysis** | Feb 27 -10.64% / Mar 2 -10.82% events on zero firm-specific news. Has the "vulnerability premium" decayed? Re-pricing odds for next event? | Quick (chart + Greek analysis) |
| **WAL leading-bucket rate-of-build forecast** | 30-89d PD +45% QoQ; Special Mention +24% QoQ. Historical bank patterns: how often does leading-bucket buildup translate to lagging deterioration in 1-2 quarters? | Medium |
| **MTB Baltimore CRE expansion** | If SIG-026-009 verifies (Sun primary), MTB joins active watchlist. Build MTB exposure file. | Quick once verified |
| **ZION quarter-end AOCI/TBVPS re-pull** (promoted from SCRATCH 6/25 at 7/17 prune) | ZION re-registered onto the AOCI/NIM axis 6/25; the 6/30 quarter-end mark was never pulled. Now best sourced from the ZION Q2 print (~late Jul). | Quick, print-week |
| **CCC/HY consecutive-count check in scripts/boot.py** (promoted from SCRATCH 6/25 at 7/17 prune) | Wire VX-REG-18.04's 3-consec counter into the boot sweep so fire/reset states are computed, not hand-checked — the 7/13 fire was only caught 4 days late by a manual FRED pull. | Quick-Medium |

---
<!--BL-BODY-->
