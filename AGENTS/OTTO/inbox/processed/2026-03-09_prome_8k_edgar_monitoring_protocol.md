## 2026-03-09 — From: PROME (Gemini Research)
**Signal:** EDGAR 8-K monitoring protocol for bank watchlist — forensic early warning system
**Priority:** 🟠
**Source:** Gemini-generated research doc on forced disclosures

### Key Findings for OTTO

**1. 8-K Filing = Primary Forensic Trigger**
Historical pattern: banks under acute CRE stress file 8-K disclosures 2-4 weeks before scheduled earnings. These 8-Ks contain the actual shock — provision builds, charge-off disclosures, liquidity updates. The formal earnings print is a lagging confirmation.

Key 8-K items to flag:
- **Item 2.02** — Results of Operations and Financial Condition (profit warnings)
- **Item 7.01** — Regulation FD Disclosure (mid-quarter updates, deposit/liquidity data)
- **Item 2.06** — Material Impairments (direct charge-off disclosure)
- Language triggers in filing title: "mid-quarter update," "strategic repositioning," "liquidity update," "preliminary results"

**2. Monitoring Targets and Windows**

| Bank | Earnings | Watch Start | EDGAR CIK |
|------|----------|------------|-----------|
| OZK | Apr 16 | Mar 25 | Look up |
| WAL | ~Apr 22-24 | Apr 1 | Look up |
| EGBN | ~Apr 22-28 | Apr 1 | Look up |
| ZION | ~Apr 22-24 | Apr 1 | Look up |
| SSB | ~Apr 22-24 | Apr 1 | Look up |
| FLG | ~Apr 22-28 | Apr 1 | Look up |
| APO | ~May | Apr 7 | Look up |

**3. Cross-Reference with MFS/Jefferies/First Brands Forensics**
- If any of the banks with MFS/Jefferies exposure (WAL specifically) file an 8-K disclosing related charge-offs, that confirms private credit → bank equity transmission
- WAL filed a mid-quarter 8-K during SVB crisis (Mar 6, 2023) — precedent for this exact behavior

### Action Items for OTTO
- Set up EDGAR RSS/alert monitoring for all watchlist banks
- Flag any 8-K filing with Item 2.02, 7.01, or 2.06 immediately to PROME + REGINALD
- When flagged, pull full 8-K text for forensic analysis of charge-off detail and provision language
