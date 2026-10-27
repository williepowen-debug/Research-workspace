# CARL L786 — paper-sleeve disposition

Decision recorded 2026-10-26 22:30 ET, after the US regular session closed. **Paper only; no broker order or capital recommendation.** Rules: book/README.md; thesis/CARL_BOOK_DESIGN.md section 4; TERRY PAPER_BOOK_DESIGN.md fill fidelity and market-closed rule.

**Decision: EXIT all seven existing rows at the first executable regular-session quote on October 27.** Decision is complete; simulated execution is PENDING. All rows remain OPEN until a real contemporaneous quote supplies a fill. There are zero new CLOSED rows. This distinction preserves the record instead of fabricating tonight's next-open prices.

| Row | Ticker | Existing side | Antecedent | 10/26 daily-bar mark | Exit reason |
|---|---|---|---|---:|---|
| PS-0001 | XLY | SHORT | CRL-31 | 114.26 | CRL-31 credit-acceleration antecedent is arithmetically unreachable on its existing letter; formal FAIL versus VOID still waits for window-end equity test |
| PS-0002 | DG | LONG | CRL-31 | 128.42 | CRL-31 credit-acceleration antecedent is arithmetically unreachable on its existing letter; formal FAIL versus VOID still waits for window-end equity test |
| PS-0003 | DLTR | LONG | CRL-31 | 124.92 | CRL-31 credit-acceleration antecedent is arithmetically unreachable on its existing letter; formal FAIL versus VOID still waits for window-end equity test |
| PS-0004 | WMT | LONG | CRL-31 | 120.29 | CRL-31 credit-acceleration antecedent is arithmetically unreachable on its existing letter; formal FAIL versus VOID still waits for window-end equity test |
| PS-0005 | AZO | LONG | CRL-31 | 3190.07 | CRL-31 credit-acceleration antecedent is arithmetically unreachable on its existing letter; formal FAIL versus VOID still waits for window-end equity test |
| PS-0006 | SYF | SHORT | CRL-20 | 74.83 | CRL-20 remains about 1%; exercise paper exit discipline after adverse Q3 card evidence; not a declaration that the whole prediction resolved |
| PS-0007 | COF | SHORT | CRL-20 | 202.35 | CRL-20 remains about 1%; exercise paper exit discipline after adverse Q3 card evidence; not a declaration that the whole prediction resolved |

The five CRL-31 rows have lost an arithmetically reachable antecedent; an unchanged mechanism story cannot repair the letter. For SYF/COF, CRL-20 remains technically live at about 1%, so the two exits are explicit owner judgment under the existing paper experiment, rather than a new minimum-probability rule. SYF reaffirmed FY NCO <5.5% and its 30+ DQ improved YoY; COF released $225M of loan reserves. These are adverse to the paper short characterizations. Their row-specific DQ “still improving” clause never fixed QoQ versus YoY, so do not retrofit it into an automatic scored invalidation. The close decision does not resolve CRL-20 or CRL-31.

Primary source: SYF 10/20 release and results presentation, accession 0001601712-26-000040; COF 10/20 release, accession 0000927628-26-000142. ALLY remains a recorded judgment NON-entry; it is not an eighth row.

Marks were freshly retrieved through FORGE fetch.py for the October 26 daily bar. Mark-based P&L fields are UNREALIZED, not close fills, transaction returns or evidence for graduation. July entries and their conservative slippage remain untouched; no losing row was deleted. The unobserved interval since July 31 is not presented as continuous monitoring or retroactive stop execution.

October 27 completion rule: obtain the actual quote/time; LONG exit at bid, SHORT cover at ask. If only the actual opening print is available, apply the sleeve's 15bp penalty against execution (sell = open*0.9985; buy = open*1.0015), state the fallback source/time, then write close_date/close_fill and CLOSED. No valid next-session quote means no fill. Refresh source data; never use today's mark, a mid or a retrospective October 20 exit.

Both scoring gates remain shut: fewer than ten CLOSED rows and only two distinct antecedents, versus the sleeve's minimum three. The paired basket is one economic experiment, not four independent wins. No sleeve result justifies capital or new positions.

The next-open step is carried explicitly in CARL's existing catalyst docket for 2026-10-27. It requires a future market observation, not Will's approval.
