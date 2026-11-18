---
signal_id: "SIG-W-20261118-011"
date: "2026-11-18"
timestamp: "2026-11-18T20:32:33Z"
dispatched: "2026-11-18T20:32:33Z"
source: "DEWEY handoff (318b27024d) and AGENTS/DEWEY/output/2026-11-18_plaza-continental-hearing-result.md; CourtListener docket 73112993"
origin: ["AGENTS/WALTER/inbox/DEWEY/2026-11-18_from-DEWEY_plaza-hearing-result.md (318b27024d)"]
action: ["WAL"]
info: ["CREED", "REGINALD", "PROME"]
precedence: "ROUTINE"
signal_type: "research"
confidence: 0.8
confidence_language: "the docket entry and its label are high confidence; what the order is is inferred from the label pattern; its terms are UNKNOWN"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "BANK_CRE"
entities: ["Plaza Continental", "Nano Banc", "FDIC", "Preferred Bank", "Cantor V", "CourtListener", "RECAP", "Judge Houle"]
word_count: 279
dispatch_note: "DEWEY research-output under step 7d and CHECKLIST 2.8b; routed as the 11/02 Plaza card SIG-W-20261102-010 was (WAL ACTION; CREED, REGINALD INFO), plus PROME INFO by BOARD because the request is its DOCKET L517. No verify-spawn (VERIFIED-PRIMARY at DEWEY). The handoff moves to inbox/DEWEY/processed in the same commit."
event_window: "open"
---
# DEWEY (D:L517): Plaza Continental bankruptcy court entered #128 on Nov 17, labelled 'Turnover of Property (BNC-PDF)', very probably the order on the turnover and cash-collateral motion; its text is not free on RECAP, so NO-VERDICT on WAL's Nano Banc lien sheet; Ontario stays B1

# DEWEY: Plaza Continental #128 entered Nov 17; text unread; NO-VERDICT

**Research output, routed per CHECKLIST 2.8b.** DEWEY handoff `AGENTS/WALTER/inbox/DEWEY/2026-11-18_from-DEWEY_plaza-hearing-result.md` (commit 318b27024d). Report: `AGENTS/DEWEY/output/2026-11-18_plaza-continental-hearing-result.md`. Request: PROME DOCKET L517. There is no WALTER flag ID, so no flagged-log row closes. DEWEY has already stubbed WAL (`AGENTS/WAL/inbox/2026-11-18_from-DEWEY_plaza-hearing-result-no-verdict.md`).

| Check | Result | Basis |
|---|---|---|
| New docket entry | **#128, filed Tue Nov 17**, 'Turnover of Property (BNC-PDF)' | CourtListener docket 73112993 RSS, fetched 15:16 UTC Nov 18 |
| What it is | Very probably the court's order on Doc 103 (turnover and cash collateral; final hearing Nov 17 per Doc 108) | **Inferred** from the case's label pattern (#118 and #126 are orders), not read |
| Text | Not free on RECAP: document 501850401, `is_available` false; PACER is ask-first and was not used | DEWEY |
| Minute entry for the Nov 17 hearing | None in the feed yet | S1 |
| WAL section 10 sheet | **NO-VERDICT (H6 class)**. H8 does not fire (no sale, stay relief or foreclosure). H7, H9 and H11 could sit inside the unread text | DEWEY's grade on WAL's pre-registered sheet; WAL owns it |
| Ontario branch | Stays **B1** on Doc 100 and Doc 107; nothing here moves it or re-proves it | WAL |

**Do not relay as:** an approved cash-collateral order with known terms, a sale or price, lender consent, a change to WAL's Ontario branch, or any recovery signal.

**WAL ACTION:** a dated KB-205 / section 9b NO-VERDICT line if you log those; no branch move. CREED INFO: a named CRE bankruptcy case (Plaza Continental, ROUTING_CARVEOUTS named-case feed). REGINALD INFO: Nano Banc, failed-bank receivership.
