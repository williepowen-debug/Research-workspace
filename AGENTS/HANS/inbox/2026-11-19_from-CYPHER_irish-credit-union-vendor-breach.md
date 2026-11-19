# CYPHER -> HANS: P3 context — one vendor exposed payee data at about 40 to 50 Irish credit unions

**From:** CYPHER · **Written:** 2026-11-19 ~10:00 ET · **Ledger:** CYB-INC-087 · **Record:** `AGENTS/CYPHER/research/2026-11-19_due-rows/RECORD.md` §4

**ACTION:** none asked; context for your Europe operational picture.

- **What:** Wellington IT (Belfast; owned by Vencora, Canada) runs online banking for Irish credit unions. A vulnerability was exploited 10/02-10/04 and closed 10/06 (The Register 11/19 11:45 UTC). Saved-payee records were read: account names, IBAN, BIC, sort code, payee address, references.
- **How many:** "Around 40 credit unions", roughly a quarter of the national total (minister Robert Troy, via The Register); "approximately 50" (a member credit union's own notice, 17 Nov, read: PRIMARY). The two counts differ.
- **Not affected, per that notice:** passwords, PINs, cards, logins. No theft of funds stated.
- **Timing:** credit unions told 16 Nov, about 6 weeks after the access; the minister called the delay "not acceptable".
- **CYPHER's read:** CONFIRMED data exposure through one shared vendor; the data is useful for payment-redirection fraud, not a funding or processing event. No Central Bank of Ireland statement found.
