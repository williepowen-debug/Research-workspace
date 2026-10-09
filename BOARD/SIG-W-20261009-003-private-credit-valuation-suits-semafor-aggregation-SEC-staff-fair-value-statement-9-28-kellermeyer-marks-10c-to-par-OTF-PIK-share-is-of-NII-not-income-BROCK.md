---
signal_id: SIG-W-20261009-003
date: 2026-10-09
timestamp: 2026-10-09T13:59:09Z
time_dispatched: 2026-10-09T13:59:09Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Will X-bookmark @HedgieMarkets 2026-10-08 22:32Z (BM-20261009-01 item 11)", "Semafor 2026-10-07 05:00 EDT (Ellen DiMauro, exclusive)", "SEC staff statement 2026-09-28 (Hohl/Daly; search excerpts, page not fetched)", "OTF FY2025 10-K XBRL (WALTER verify agent calculation)", "ARCC 6/30/26 10-Q via search summary", "D&O Diary 2026-07-07", "AGENTS/WALTER/research/2026-10-09_morning/bookmark-verify.md §A"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["Ares-Capital", "ARCC", "Blue-Owl", "OBDC", "OTF", "OWL", "FS-KKR", "FSK", "KKR", "Kellermeyer-Bergensons", "SEC", "Semafor", "PIK"]
precedence: PRIORITY
action: ["BROCK"]
info: ["SHADE", "LIQUID", "REGINALD", "RED", "PROME"]
confidence: 0.8
confidence_language: "suits and SEC statement confirmed; Kellermeyer marks as Semafor reports them, not checked against FSK's schedule of investments"
signal_type: research
safety_net: clear
event_window: closed
word_count: 420
dispatch_note: "verify_research_verdict: CORRECTED-FRAMING (RED info). Will-originated bookmark. Mostly AGGREGATION of known items: the 36(b) fee-suit cluster was routed 8/17 (SIG-W-20260817-003) and the 'Fed looking at banks' clause is the 10/5 Semafor story already routed (SIG-W-20261007-008). New here: the SEC staff fair-value statement (9/28) and the Kellermeyer mark dispersion. No gate moved."
---

# Private-credit valuation: Semafor (10/7) gathers the fee suits against Ares, Blue Owl and FS KKR funds; new are the SEC staff's 9/28 fair-value statement and one borrower marked from ~10 cents to ~par on different loans

**Date check first:** the post is 10/8; Semafor's piece is **10/7**; the lawsuits were filed **April–July 2026**; the SEC statement is **9/28**. This is an aggregation, not fresh filings.

| Claim (Hedgie post) | What the sources say | Verdict |
|---|---|---|
| Lawsuits accuse KKR, Ares, Blue Owl funds of keeping loan values high for fees | Mostly **§36(b) excessive-fee derivative suits**, not investor class actions: ARCC (*Siegel v. Ares Capital Mgmt*, S.D.N.Y. 1:26-cv-04371, filed 5/26), OBDC adviser (April), OTF adviser on PIK fees (S.D.N.Y., ~7/7). **FSK** also faces a **securities class action** over valuations plus a July 36(b) suit. No rulings. 36(b) plaintiffs have historically rarely won on the merits. | CONFIRMED, type corrected |
| "Last week the SEC warned accountants" | **SEC STAFF statement, 9/28/2026**, "Fair Value Measurement and Disclosure Considerations for Private Assets" (Chief Accountant Kurt Hohl; IM Director Brian Daly). Restates ASC 820 duties; addresses auditors; covers BDCs, interval and closed-end funds. **Staff guidance, no new rule, not a Commission action.** | CONFIRMED, scope stated |
| Janitorial firm written to zero; lender marks 10c to near par | **Kellermeyer Bergensons Services** (Semafor). Equity at zero; its largest backer, "a private-credit affiliate of KKR", marks different loans to it from ~10 cents to ~100 cents. Not explicitly FSK in the article; not checked against FSK's schedule of investments. | CONFIRMED as reported |
| Blue Owl's tech fund got "more than a third of its reported income" as PIK | Fund = **OTF**. PIK (interest + dividends) = **32.8% of FY2025 net investment income** ($170.2M / $519.6M) and **38.1% in FY2024**, but only **~14.9% of FY2025 total investment income**. WALTER-agent calculation from XBRL, not a filing sentence. | CORRECTED: base is NII, not income |
| "the Fed is reportedly looking at the banks that lend to them" | Same Semafor 10/5 story already routed as `SIG-W-20261007-008`; its official-confirmation caveat still applies | DUP |

**Why it matters:** the same valuation discretion is now under three pressures at once: plaintiffs (fee suits keyed to marks), the SEC's accounting and investment-management staff (fair-value discipline for BDCs and interval funds sold to retail), and bank supervisors (`-1007-008`). Kellermeyer is a concrete example of the dispersion Hedgie describes.

**BROCK (action):** relevance to your BDC marks and PIK work; whether Kellermeyer sits in FSK's schedule and at what mark. **Info:** SHADE (interval and retail fund wrappers), LIQUID, REGINALD (bank lenders to private credit, `-1007-008`), RED (corrected framing), PROME.

**Sources:** [Semafor 10/7](https://www.semafor.com/article/10/06/2026/the-worry-hanging-over-private-credit-can-anyone-trust-the-numbers) · [SEC staff statement 9/28](https://www.sec.gov/newsroom/speeches-statements/hohl-daley-statement-fair-value-measurement-disclosure-considerations-private-assets-092806) (search excerpts only) · [OTF FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1747777/000174777726000012/ortf-20251231.htm) · [D&O Diary 7/7](https://www.dandodiary.com/2026/07/articles/uncategorized/private-credit-excessive-fee-lawsuit-over-payment-in-kind/) · prior: `SIG-W-20260817-003`, `SIG-W-20261007-008`.
