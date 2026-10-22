# DEWEY → REGINALD: regional and community banks, legacy technology and exposure to the October 2026 cyber wave (ACTION)

**State:** NEW · **From:** DEWEY · **Date:** 2026-10-22 (~16:45 ET) · **Request:** Will-directed (live session)
**📄 Report (canonical; read it rather than this stub):** `AGENTS/DEWEY/output/2026-10-22_bank-legacy-technology-exposure.md`
**Data files:** `AGENTS/DEWEY/output/2026-10-22_bank-legacy-technology_kre-tech-map.tsv` (167 KRE banks) · `..._breach-notices.tsv` (88 classified notices)

**Headline:**
- **Old tech is widespread.** 77% of community banks outsource core processing; the main cores are decades old (IBM i, mainframe); OCC and Fed flagged end-of-life technology in 2025–26.
- **The breach record points elsewhere.** 0 of 88 bank and credit-union breach notices (2023–26) cite outdated software. Routes: file-transfer zero-days 34%, own network (route not stated) 25%, email 24%, vendors 10%. NCUA: 69% of credit-union incidents came through third parties.
- **For PHP2Shell the exposed layer is websites and vendor web platforms, not cores.**

## Your action block
1. **Vendor map (§2):** core vendor named in a 2024–26 primary document for **22 of 167 KRE banks**; **UNKNOWN for 108 (58% of KRE by weight)**. Fleet updates:
   - SSB is STALE Fiserv Premier (2021 425).
   - EGBN is STALE FIS (2011).
   - FLG → Finxact (REPORTED only, 2027–28).
   - PNFP Jack Henry → FIS, 1Q27.
   - BPOP leaves Evertec by Sep 2028.
2. **Website check (§3), passive, homepages only:**
   - PHP-based website software at HOMB and AMTB (WordPress) and WAL and FHB (Drupal); EGBN probably Drupal.
   - HOMB declares WordPress 5.9.10, a 2022 line; WordPress maintains only 7.1.
   - No eMudhra certificates.
   - FLG, HBAN, UCB, EBC, PNFP and COLB blocked the check.
3. **Watch suggestion:** re-run the passive website check in 2–4 weeks, and watch for vendor PHP2Shell advisories (none found). This pairs with REQ-008 checklist rows 3–5.

**Guardrail:** the bank-level website findings (§3) stay with desks. Do not post them to the BOARD as a list of exposed banks. They are passive homepage observations, not confirmed vulnerabilities.
