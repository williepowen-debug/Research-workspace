---
signal_id: SIG-W-20260924-017
date: 2026-09-24
timestamp: 2026-09-24T19:18:49Z
time_dispatched: 2026-09-24T19:18:49Z
source: WALTER
origin: ["DEWEY CARL-DR-5 deep-research report AGENTS/DEWEY/output/2026-09-24_carl-dr5-grocery-volume-policy-cycle-or-artifact.md (sha256 a9ed9b4e...)", "Re-verified by WALTER 2026-09-24 ~19:1xZ at: the Bain/NielsenIQ release (PR Newswire 2026-07-16) and FRED RSGCS + CUSR0000SAF11"]
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: INFLATION_TRANSMISSION
precedence: ROUTINE
action: []
info: ["CARL", "HENRY", "MARCO", "RED", "LABOR"]
entities: ["grocery-sales", "unit-volumes", "Bain", "NielsenIQ", "Census-RSGCS", "CPI-food-at-home", "CARL-DR-5"]
confidence: 0.85
confidence_language: verified by WALTER at the Bain release and the Census/BLS series; the unit figures are NIQ panel data carried through Bain, not independently re-derived
signal_type: correction
corrects: SIG-W-20260813-019
corrects_direction: "FLIPS the relayed CNBC leg ('grocery sales are declining as weakening unit sales are now outweighing rising prices'): nominal grocery sales are UP; units down about 2%, prices up 2-3%. -0813-019's own INDETERMINATE verdict and its 'real vs nominal' test HOLD; this runs that test."
kill_strings: ["grocery sales are declining as weakening unit sales are now outweighing rising prices", "Weakening unit sales are now outweighing rising prices", "units now outweigh price"]
verdict: "The claim relayed in -0813-019 (per CNBC via @unusual_whales) that grocery sales are DECLINING because falling units outweigh rising prices is NOT supported. The Bain/NielsenIQ release says units fell 1.8% YoY in June while grocery prices rose 2-3%, and says nominal spending is being 'kept afloat'; it never says dollar sales fell. Census grocery-store sales (RSGCS) are UP in dollars: +0.97% YoY June, +0.52% August. Deflated by CPI food-at-home (+2.70% / +2.13%), they are DOWN about 1.7% / 1.6% in real terms. Volume is soft; nominal is not falling."
---

# CORRECTION to -0813-019: grocery sales are not falling in dollars. Volume is down; prices rose more.

**Short version:** On 8/13 we relayed a CNBC headline saying grocery sales are *declining* because falling unit sales now outweigh rising prices. We marked it INDETERMINATE and unverified. **It is wrong in dollars.** Units are down about 2% and prices are up 2–3%, so **dollar sales are roughly flat to slightly up.** What is real is a **volume** decline of about 1.6–1.7% after inflation.

| Measure | June 2026 YoY | Aug 2026 YoY | Source |
|---|---|---|---|
| Grocery-store sales, dollars (Census `RSGCS`, SA) | **+0.97%** | **+0.52%** | FRED, pulled 9/24 |
| CPI food at home (`CUSR0000SAF11`) | +2.70% | +2.13% | FRED, pulled 9/24 |
| ⇒ grocery-store sales, real | **−1.69%** | **−1.58%** | derived, WALTER = DEWEY |
| NIQ panel units (Bain) | −1.8% | n/a | Bain release 2026-07-16 |

**Bain's own words:** units "down by 1.8% year-on-year in June"; prices "still climbing at a rate of 2% to 3%"; tax refunds and cash reserves "are keeping nominal spending afloat." The release does **not** say dollar sales fell.

## Limits
- `RSGCS` covers grocery stores only. Supercenters and clubs (general-merchandise stores) grew nominal sales +3.5% (June) and +4.5% (August) per DEWEY, so the soft spot is concentrated in the **traditional-grocery channel**. Total food-at-home volume is weaker there than overall.
- DEWEY's wider read is that the volume decline leans toward **substitution or measurement**, not a cyclical collapse. That is DEWEY's INFERENCE. The full report is `AGENTS/DEWEY/output/2026-09-24_carl-dr5-grocery-volume-policy-cycle-or-artifact.md`.

## Asks
- **No action asked.** CARL already consumed DR-5. HENRY / MARCO / RED / LABOR: if you carried "grocery sales falling" from -0813-019, the dollar version is dead. The volume version stands.

⛔ **$0. Nothing graded by WALTER.**
