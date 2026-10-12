# WATT — TRADE

**Last real data refresh: 2026-10-12** (trigger states; no security quotes or position reconciliation)

**No WATT trade proposed or executed.** Position truth is Will/broker direct; this file records research trigger states.

*(Banner-compliant per blueprint §8 / PAT-023: a trade surface must carry a FROZEN/NOT-CURRENT banner OR a live mtime alert — never the silent-rot middle. `boot.py` runs `ledger_staleness.py WATT --trade` regardless.)*

> ✅ **2026-09-06 — the standing fix WORKED and this is the receipt.** The rule written on 9/2 ("re-read this table at every boot where `power_watch` returns anything other than all-quiet") fired at today's boot and this table was refreshed **in the same session the state changed**, not 16 days later. **The episode closed 9/3; the P1 trigger below is now a SPENT fire, not a live one.**
>
> ⚠️ **THIS FILE WAS WRONG FOR 16 DAYS AND THE BANNER DID NOT CATCH IT — the L-27 failure, repeated.** Its closing note read *"P1, the only channel that could supply [a live band], is **cold**."* **P1 fired on 2026-09-02.** The banner ("no open positions") stayed **true** while the analysis under it went **false** — exactly the defect L-27 recorded on 2026-08-04, on this same file. **A banner exempts a surface from the staleness ALERT, never from being wrong.** ⇒ **Standing fix: this table is now re-read at every boot where `power_watch` returns anything other than all-quiet**, not only at closeout.

---

## Candidate expressions (thesis → instrument, not yet proposed)

| Channel | Direction | Candidate surface | Trigger state [as of 2026-10-12] |
|---|---|---|---|
| **P1** | long scarcity | IPP generators (VST/CEG/NRG/TLN) | **Score 5 held from October 7; event spent, no entry inferred.** October 12 max $52.90 through 10:35; advisories October 12–14, recall October 14 noon; new DOE request unverified as issued. WATT-12 already HIT. No security quotes or repricing measurement |
| P2 | structural | utility/IPP capacity-cost beneficiaries; industrial power-cost shorts | ⚠️ **FIRED 2026-07-14** — 28/29 BRA cleared **at cap** ($325/MW-day = **100% of the 28/29 cap**) **and 6,831 MW short** ✅ *(the old "97.5% of $333.44" was PJM's YoY cap decrease mislabelled as utilisation — resolved 9/6 at PJM primary; FIRED call unaffected)*; 3rd straight at-cap clear, 2nd straight RTO-wide shortfall. **Fired ≠ proposed** |
| P3 | long buildout | IPP load-growth beneficiaries | ⚠️ **FIRED 2026-07-31** — VULCAN-06: the 7/29-31 hyperscaler cluster **funds the WoodMac 55 GW high side**. Trigger is **SPENT — do not re-fire.** IPP guidance still **reaffirmed, not raised** (the next rung, P3→5). ⚠️ **New counterweight 9/2:** DEWEY's primary read finds GEV's "116 GW under contract" is **~53 GW firm + 63 GW slot reservations** — 54% outside the audited RPO — so the *turbine* order book is inflated. **This does NOT discount the PJM interconnection queue** (different population, different layer); **do not net them** |
| P4 | — | no candidate | **NOT-FIRED**; provisional stress-window spark +$37.23/MWh (HR7, October 6–11, n=1,142); intraday gas dated October 12 and October 7 outlier. No widening claim |
| **P2/P3 catalyst** | — | regulatory event | **WATT-10 MISS:** FERC rejected IRAS/BYONC October 9; definition/registry accepted October 12 with compliance within 30 days. WATT-08 ~50% OPEN. Consumer allocation risk rises relative to Door B; actual amount unresolved, physical/contract costs persist. EL26-67 responses November 16, suspension proviso |


**October 12 supersession:** the September entry discussion below is historical. Current entry case is not registered. No security quotes, no assumption that scarcity rent is unpriced, and no trade construction request.

## ⛔ WHY A FIRED BAND IS STILL NOT A PROPOSAL — four reasons, all about ENTRY

1. **The event has a published end date.** Hot Weather Alert runs through **9/3**; §202(c) Order 202-26-41 expires **11:59 PM ET 9/8**. **Buying scarcity exposure into a dated, forecast, already-priced heat episode is buying after the move** — PJM published the 9/3 forecast (152,496 MW) *before* the close.
2. **Root rule #6 points the other way.** Long-scarcity IPP exposure entered *during* the emergency is a **calls-on-a-red-day** trade in the wrong direction — the day-colour proxy says wait. **I hold no direct measurement that refutes the proxy**, which is the only legitimate break (root `CLAUDE.md` rule #6 test), so **the rule is not broken here.** *"The window is closing" is a chase, not a break.*
3. **A fired gate is not a thesis confirmation** (TERRY `RISK_RULES.md` **Non-Negotiable #15**). P1's band grades a **grid state**, not a security's mispricing. **Nothing in my instrument set measures whether VST/CEG/NRG/TLN already carry this.**
4. **Root rule #4 — prices must be live, and I have none.** I hold zero live equity or option quotes this session. **A proposal built on a power tape and no security price is not a proposal.**

> ⇒ **What WATT is actually delivering is a dated, primary-verified SIGNAL with its mechanism established. Construction is TERRY's and approval is Will's** (root rules #5–#8). **If a proposal is wanted, the missing inputs are named and short:** live IPP quotes, the **9/3 outcome** (did it escalate to EEA-2+?), and whether the September episode is a **weather** event or the **reserve-margin** read of PICK-UP #3 — *the last one is the only one that would make this structural rather than seasonal, and it is measurable.*

*All candidates route through TERRY for construction + Will approval before any position (root rules #5–#8). WATT produces the signal, not the execution.*
