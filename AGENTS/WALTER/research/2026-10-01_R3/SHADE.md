# R3 test — SHADE WATCH_FOR proposal (10 phrases + 5 alternatives) · run 2026-10-01T16:34:21Z

Packet: `PROME/inbox/2026-10-01_from-SHADE_cadence-and-watch-terms.md` (665964489). Tool: `tools/watch_for_harness.py --desk SHADE` (real matcher). Lane: 10,405 headlines 6/29–9/30. Live: Google News 90d; run 1 = 8 subject queries / 307 headlines; run 2 = 5 queries / 183. **Live fetch verified working:** per-subject counts Delaware Life 88 · Clear Spring Life 52 · TWG Global 100 · Egan-Jones 61 · Guggenheim probe 44 · PHL Variable 15 · Athene Global Funding 13 · Actuarial Guideline 12. ⇒ **a 0 below is a 0 against an ACTIVE news flow — a recall signal, not only "unproven".**

| # | Phrase | Lane | Live | Read | Verdict |
|---|---|---|---|---|---|
| 1 | Delaware Life distribution | 0 | 2 | both TRUE (Truist/Fifth Third pause; Yahoo + Seeking Alpha). **Misses CNBC's "pause sale"** | ADOPT, or replace with `Delaware Life pause` (below) |
| 2 | Delaware Life downgrade | 0 | 0 | **RECALL MISS:** AM Best "Revises Outlooks to Negative for Subsidiaries of Group 1001" (Business Wire / InsuranceNewsNet) is a rating action this phrase cannot see | NO VERDICT; low recall evidenced |
| 3 | Delaware Life indictment | 0 | 0 | no indictment has occurred; 0 expected | NO VERDICT (event not yet happened) |
| 4 | Clear Spring Life | 0 | 0 | 52-headline subject query, none carries the name in-title | NO VERDICT |
| 5 | Guggenheim subpoena | 0 | 0 | **RECALL MISS:** 12 live headlines on the Guggenheim probe widening say "probe"/"SEC interviews"/"FBI seized phone" | NO VERDICT; low recall evidenced |
| 6 | TWG Global Delaware Life | 0 | 0 | 100 TWG headlines; none pairs it with Delaware Life | NO VERDICT |
| 7 | Athene Global Funding | 0 | 0 | the FABN issuer name rarely appears in headlines | NO VERDICT |
| 8 | Egan-Jones indictment | 0 | 0 | no indictment yet; DOJ records-request headlines exist | NO VERDICT (event not yet happened) |
| 9 | Actuarial Guideline 55 | 0 | 0 | NAIC offshore-reinsurance news uses other words | NO VERDICT |
| 10 | PHL Variable liquidation | 0 | 0 | PHL news is "RICO suit", "class action" | NO VERDICT |

**Alternatives tested:**
| Phrase | Live | Read | Result |
|---|---|---|---|
| `Delaware Life pause` | 3 | all TRUE (CNBC, Yahoo, Seeking Alpha) | **CLEAN; strictly better recall than #1** |
| `Guggenheim probe` | 12 | all on-subject (probe widening: Bloomberg, FT, Crain's, SEC interviews) | **0 false, but ~12 in 90d ≈ weekly during an active probe; partly one story syndicated. SHADE asked to drop weekly pagers: SHADE's call** |
| `Group 1001` | 4 | 2 TRUE (AM Best outlooks) + 2 FALSE (AriBio "AR1001"; Nigerian "1001 Reasons… Integrity Group") | **REJECT by name.** Untested idea: `Group 1001 Insurance` |
| `PHL Variable` | 2 | LPL class action (PHL-related) + Forbes commentary | REJECT by strict rule (commentary is not an event); SHADE's call |
| `Delaware Life sued` | 0 | lawsuit headlines say "lawsuit claims", "sued over" with the owner's name | NO VERDICT |

Lane coverage: **0 lane hits for every phrase.** The lane does not appear to fetch this subject; any adopted phrase needs a lane query (PROME's).

## Follow-up test (SHADE asked, 1736814d9): `Group 1001 Insurance`
Lane 0 · live 2 (queries `Group 1001`, `Group 1001 Insurance Holdings`, `Delaware Life`; 136 headlines, 90d): both TRUE (AM Best "Revises Outlooks to Negative for Subsidiaries of Group 1001 Insurance Holdings", Business Wire + InsuranceNewsNet). **CLEAN (2 true, 0 false)**. It catches the rating action `Delaware Life downgrade` missed.
