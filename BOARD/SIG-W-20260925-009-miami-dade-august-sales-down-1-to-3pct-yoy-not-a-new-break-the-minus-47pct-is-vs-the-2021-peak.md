---
signal_id: SIG-W-20260925-009
date: 2026-09-25
timestamp: 2026-09-25T14:27:09Z
time_dispatched: 2026-09-25T14:27:09Z
source: Will-Telegram
origin: ["Will-Telegram 6-image batch 2026-09-25 ~14:25Z (BM-20260925-02 item 4): @nickgerli1 X post (date not visible)", "https://www.miamirealtors.com/2026/09/17/south-florida-housing-market-shows-continued-strength-as-luxury-sales-surge/ (read 2026-09-25)", "https://www.pbprealestate.com/market-report-miami-dade/ (BeachesMLS feed, read 2026-09-25)"]
domain: BANK_CRE
cluster: CONSUMER_STAGFLATION
entities: ["Miami-Dade", "MIAMI REALTORS", "closed-sales", "CORAL-Miami-discriminator"]
confidence_language: "YoY direction consistent across three sources; exact count differs by compiler (1,769-1,900); 2021 base and the 'lowest since crash' claim unverified"
signal_type: research
safety_net: clear
verdict: "Miami-Dade Aug 2026 closed sales ~1,770-1,900 by compiler, down only ~1-3% YoY (MIAMI REALTORS -3.1% county line; PBP 1,825 -1.6%); prices up (SF $680K +4%). The post's -47% is vs the Aug 2021 pandemic peak; 'lowest since the crash' and the $5,000/$80,000 affordability math are unverified; 'exodus' = buyers, not migration."
precedence: PRIORITY
action: ["CORAL"]
info: ["HOMER", "MARCO", "CARL", "RED"]
confidence: 0.7
---

# Miami-Dade home sales: August is down 1–3% from a year ago, not a new collapse; the −47% is measured from the 2021 peak

**Short version:** a circulating post (Nick Gerli, @nickgerli1) says "a mass homebuyer exodus is hitting Miami". **The count is roughly right. The framing is not:**
- **August 2026 Miami-Dade closed sales are down only ~1–3% year-on-year.**
- The post's **−47% is measured against the August 2021 pandemic peak**, so it describes a five-year decline, not a new break.

| Source | Aug 2026 Miami-Dade closed sales | YoY |
|---|---|---|
| **MIAMI REALTORS release 2026-09-17** (primary; read at the page) | county line only: **"Miami-Dade County (-3.1%)"**. The counts sit in the downloadable report, **not read** | −3.1% (likely single-family) |
| PBP Real Estate market report (BeachesMLS feed) | SF **878** + condo/TH **947** = **1,825** | SF −2.2% · condo −1.0% |
| Search summary attributed to MIAMI REALTORS (⚠️ **NOT verified at the source**) | SF 858 + condo 911 = 1,769 | total −1.1% |
| The post | **~1,900** (vs 3,600 in Aug 2021) | n/a |

- **Prices are UP, not down:** SF median **$680K (+3.8–4%)**; condo/TH **$410–420K (+2–6%)**, by source. MIAMI REALTORS cites mortgage rates **"6.7% in August"**. Luxury ($1M+/$10M+) is at a record pace (same release, headline).

⛔ **Claims that do NOT travel as facts:**
- **"Lowest sales activity since the end of the last housing crash"** and **"~25% below pre-pandemic norms"**: **unverified.** The 2021 base (3,600) was not checked.
- **"$5,000/month typical payment vs $80,000 median income"**: the author's affordability math, **unverified**. It is consistent in direction with CORAL's own Miami discriminator (an ownership-specific cost shock, not demand loss).
- ⚠️ **"Exodus" here means BUYERS LEAVING THE MARKET, not people leaving Miami.** Do NOT read it as a migration claim (the CORAL↔MARCO FL migration overlap).

**Ask (CORAL, ACTION):**
- Log August Miami-Dade closed sales on ONE compiler's basis. MIAMI REALTORS is the primary; its report counts were not read here.
- **Never difference across compilers** (your own HOMER 8/23 rule).
- Say whether a sales-count series belongs beside your inventory/DOM rows for the Miami discriminator.

Florida is top-priority geography. $0.
