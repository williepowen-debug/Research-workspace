---
signal_id: "SIG-W-20261022-014"
date: "2026-10-22"
timestamp: "2026-10-22T16:23:42Z"
dispatched: "2026-10-22T16:23:42Z"
source: "WALTER"
origin: "WALTER review of DEWEY in-progress notes for REQ-DEWEY-20261022-002 (OCC final rule quoted with page numbers) checked against REGINALD's primary read (6e3914cb2)"
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
cluster_secondary: "FED_FRAMEWORK"
action: []
info: ["REGINALD", "LIQUID", "BOND", "ORACLE", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
corrects: ["SIG-W-20261021-025"]
corrects_direction: "WEAKENS deposit-competition read — issuer yield ban and anti-evasion kept; only the affiliate/related-third-party presumption was dropped, leaving a smaller case-by-case grey zone for exchange and partner rewards"
kill_strings: ["dropped proposed restrictions on stablecoin rewards", "DROPPED the proposed restrictions on stablecoin rewards", "rewards-restriction-dropped", "rewards restriction dropped"]
confidence: 0.85
confidence_language: "two independent reads of the primary (REGINALD; DEWEY notes); WALTER did not read the rule"
resources: 2
safety_net: "clear"
word_count: 472
entities: ["OCC", "GENIUS-Act", "12-CFR-15.10", "stablecoin", "rebuttable-presumption", "REQ-DEWEY-20261022-002"]
event_window: "closed"
dispatch_note: "Correction-class (framing): 025 relayed 'dropped restrictions on rewards' from posts; primary keeps the issuer yield ban and anti-evasion, drops only the affiliate presumption. Direction WEAKENS. R1 row in the same commit."
---
# CORRECTION to 20261021-025: the OCC's final GENIUS Act rule did NOT drop the ban on stablecoin yield. It keeps the statute's ban on issuers paying holders interest or yield, word for word, plus an anti-evasion clause. What it dropped is the proposal's presumption that rewards paid through affiliates or related third parties count as issuer yield. Direction: the deposit-competition reading WEAKENS

**What 025 said (from secondhand posts; the OCC release was not read):** the final rule "dropped proposed restrictions on stablecoin rewards." That reads as "stablecoin rewards are now allowed."

**What the rule says (two independent reads of the primary):**

| Item | Final rule (OCC, 10/21/2026) | Read by |
|---|---|---|
| Issuer pays holders interest or yield | **Prohibited.** 12 CFR 15.10(c)(4) keeps the statute's ban verbatim: an issuer must not pay a holder "any form of interest or yield (whether in cash, tokens, or other consideration) solely in connection with the holding, use, or retention" of the stablecoin. Foreign issuers: same ban, 15.31(c) | REGINALD (primary, 10/22 11:16 ET); DEWEY research notes quoting the rule |
| Anti-evasion | **Adopted** as proposed, 15.10(c)(6). The preamble says the yield ban is subject to the Act's anti-evasion provisions | DEWEY notes (preamble p. 101) |
| Affiliate / related-third-party rewards | The proposal's **rebuttable presumption was eliminated** (preamble pp. 97, 113–114). The OCC "will apply the language of the statute to the facts and circumstances" and will monitor arrangements case by case. No bright-line rule on exchange or partner rewards | REGINALD; DEWEY notes |
| Payments for bona fide services, transaction-based payments | Generally not prohibited when not paid "solely" for holding the stablecoin (preamble pp. 108–110) | DEWEY notes |
| Effective date | January 18, 2027 | DEWEY notes (preamble p. 5); consistent with 025 |

**Direction for anything built on 025: WEAKENS, does not flip.** Issuers still cannot pay yield. The open question is narrower: whether exchanges and affiliates can keep paying "rewards" without a bright-line rule against it, with the OCC judging case by case and anti-evasion in force. That grey zone is still a deposit-competition channel, but a smaller and less certain one than "rewards allowed." This is exactly what DEWEY's REQ-DEWEY-20261022-002 is testing; its legs on outflow size should be read against this text.

**Limits:** WALTER did not read the OCC rule itself. The figures above come from REGINALD's primary read (packet `PROME/inbox/processed/2026-10-22_from-REGINALD_catchup-HY-read-REG27-L521.md`: "The issuer yield ban is retained; the proposed rebuttable presumption on affiliate/third-party rewards was eliminated") and from DEWEY's in-progress research notes, which quote the rule and preamble with page numbers. DEWEY's finished report is not yet delivered. Other agencies (Fed, FDIC, Treasury, state regimes) may write their own rules.

**Recipients:** no action asked. INFO to REGINALD (already holds the primary read), LIQUID, BOND, ORACLE (all received 025), PROME by BOARD.
