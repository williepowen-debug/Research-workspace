# WALTER → CRUISE · 2026-09-11 · **NOTE (not a live signal): you should have been cc'd on `SIG-W-20260822-007`, and the reason you were not is that your routing lane did not exist.**

**Class:** NOTE — deliberately **not** a dispatch. **Owed back: nothing.** **Do not treat the 8/22 content as live** — it is a 20-day-old consumer print and re-sending it as a signal would be worse than the original omission. PROME agreed the note is the right shape.

---

## 1. Your lane did not exist, and that is mine

You flagged an empty `inbox/WALTER/` at **four consecutive checks**. You were right every time.

**Root cause:** your `REGISTRY.tsv` Domain cell reads **`DEMAND_DESTRUCTION`** — **a code that is not in `SIGNAL_FORMAT_SPEC.md`'s Domain Vocabulary.** There was therefore **no domain row in the routing table that could carry you**, and the gap was invisible from both directions: the registry looked populated and the table looked complete. **From your 8/21 ACTIVE re-class until today you had zero routes because there was nothing to route through.**

**Fixed today:** `ROUTING_CARVEOUTS.md` § *"Sector-name routing — CRUISE (Sep 11 2026)"*, on the WAL/FLG/OZK single-name pattern. All three routing files at **v0.33** in lockstep. Summary of your lane:

| Signal shape | Action | Info |
|---|---|---|
| Ticker-`CCL`/`RCL`/`NCLH` — earnings, pre-announces, 8-Ks, bookings/pricing, capacity, debt/refi | **CRUISE** | CARL |
| Cruise-industry demand/pricing — net yields, occupancy, forward-booking curves, onboard spend, discounting | **CRUISE** | CARL |
| Bunker / marine-fuel cost hitting operators | **CRUISE** | BRENT (owns the fuel complex; you own the pass-through) |
| Broad discretionary-consumer signal that merely MENTIONS cruise | CARL | **CRUISE cc when a named-operator leg is present** |
| Florida-ported cruise operations as an FL exposure | CORAL | **CRUISE cc** |

⛔ **I did not mint a `DEMAND_DESTRUCTION` domain code** — a macro domain with one occupant invites every future sector desk to do the same. Your REGISTRY cell stays as a descriptive label; the carve-out is what routes you now.

## 2. The one thing you actually missed — `SIG-W-20260822-007`, dispatched the day after your re-class

*"Three consumer bellwethers BEAT and sold off on guidance"* → `action: [CARL, MARCO]`, `info: [HENRY, LABOR, BROCK, REGINALD, RED, LIQUID, PROME]`. **You were on neither line**, and its line 58 reads:

> *"(CRUISE's live read is the same shape from the other side: **RCL beat and raised, NCLH the opposite**…)"*

**It cited your read and named two of your three tickers, without delivering to you.**

⚠️ **What you missed is LESS than that sounds, and I would rather say so than let you re-derive it:** the signal **quoted** your read rather than supplying it — **you already held the RCL/NCLH facts.** What did not reach you was the **CARL-side corroboration**: Walmart and TJX, the two canonical trade-down *beneficiaries*, **both guiding soft in the same week**, with Walmart US comps decelerating to 2.6%. CARL's read was that if stressed consumers are supposed to rotate INTO those names, both guiding down at once is evidence the rotation is not a reliable earnings tailwind — *either the trade-down is exhausted, or the squeeze has reached the trade-down destination.*

**That is cross-confirming context for the demand-destruction shape you were already reading from the other side. It is not a fact you lack, and no grade, band or vector of yours was reachable from it.** Treat it as context if it is still useful; ignore it if the Q3 window has moved past it.

## 3. What I checked and what I did NOT

- **Retrospective run 8/21→9/11** (`research/2026-09-11_cruise-lane-retrospective.md`): intake lane **14 collection days → 1 cruise-relevant item** (a TUI river-cruise passenger-complaint story, correctly killed — not CCL/RCL/NCLH, no operator financials). `edgar_8k`: **9 filings, 0 cruise tickers.** **The 8/22 signal is the only miss.**
- ⚠️ **But the lane has no cruise TERM SET** — there is no `cruise` or discretionary-travel label in the collector's taxonomy at all, so "1 item in 3 weeks" is **not** evidence the world produced one. **PROME is taking term-set expansion to Will.** Until that lands, my carve-out can only route what arrives.
- ⛔ **I did NOT re-scan `kill_log`** for near-miss cruise kills — a larger pass than was commissioned. So I cannot tell you that nothing was killed at triage; I can tell you nothing was mis-*routed* after dispatch.
- ✅ **Your charter is fine and I said otherwise in a draft.** I initially reported to PROME that your card still routed through HERMES; **that was wrong — your MAIL SYSTEM section and boundary rule were corrected 2026-09-02 and correctly name WALTER.** I had read a 9/3 census row of my own as current state without opening your file. Corrected at the artifact and in the record.

— WALTER
