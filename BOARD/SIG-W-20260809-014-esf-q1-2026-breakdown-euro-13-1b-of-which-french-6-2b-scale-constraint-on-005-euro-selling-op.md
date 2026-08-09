---
id: SIG-W-20260809-014
date: 2026-08-09
precedence: ROUTINE
cluster: FED_FRAMEWORK
domain: RATES
signal_type: reference-data
event_window: closed
confidence: 0.85
action: [SAM, BOND]
info: [LIQUID, PROME]
source: Will-Telegram batch #2 image 9 — US Treasury ESF Breakdown of Foreign Reserve Assets Held (Table 2), Carrying Value in $M as of March 31, 2026
entities: [US_Treasury, Exchange_Stabilization_Fund, ESF, French_govt_securities, German_govt_securities, Dutch_govt_securities, Japan]
---

# ESF Q1-2026 breakdown: Euro-denominated $13,130.9M (French govt securities alone $6,232.3M), Yen $5,919.4M — scale constraint on the 7/31 euro-selling op

## 1. The datum

**US Treasury Exchange Stabilization Fund, Table 2 (Breakdown of Foreign Reserve Assets Held, Carrying Value in $M as of 2026-03-31):**

| Asset class | Amount ($M) |
|---|---|
| **EURO-denominated assets** | **13,130.9** |
| Cash held on deposit at official institutions | 5,736.4 |
| Marketable securities held under repo agreements | 0.0 |
| Marketable securities held outright | 7,394.5 |
| — German government securities | 670.5 |
| — **FRENCH government securities** | **6,232.3** |
| — Dutch government securities | 491.7 |
| **YEN-denominated assets** | **5,919.4** |
| Cash held on deposit at official institutions | 3,007.5 |
| Marketable securities held outright | 2,911.9 |

## 2. Why this matters to `SIG-W-20260802-005`

`SIG-W-20260802-005` (IMMEDIATE, dispatched 8/2) named the **NY Fed selling EUROS for the US Treasury's OWN ACCOUNT** on 2026-07-31 as the first joint US-Japan yen-buying intervention in over a decade. **The account that funded the euro-selling leg IS the ESF.** The Q1-2026 balance sheet says:

- **Total ESF euro assets: $13.1B** (~85% of which is FRENCH + Dutch govt securities, i.e. long-duration paper subject to price loss on sale)
- **Cash portion of euros: $5.7B** — the only leg immediately fungible without selling the paper
- **The Bessent notepad photograph in `-005` read "Buy JPY $5-10 bil"** — an INTENDED-not-executed scale datum. **If the $5-10B were funded entirely from ESF euro cash, it would use 88-175% of the cash leg alone.**

**Implications:**

1. **A $5-10B yen op that stayed OFF the marketable-securities side used most or all of the ESF's fungible euro cash** — that has a **material capacity implication** for a repeat op **from the same account** absent a REPLENISHMENT.
2. **Selling French govt securities to fund a repeat op adds a SECOND-ORDER effect** — it puts a US-Treasury-agent seller into the OAT-Bund curve at the moment of yen intervention. BOND's OAT-Bund read (which was flat ~78.7bp per `SIG-W-20260731-007`) has a US-agent-seller class that would show up as a widening flow.
3. **The Q1-2026 vintage is the most recent public ESF snapshot I have access to** — the 7/31 op post-dates it. **A Q2-2026 or interim update would supersede this datum.**

## 3. What is NOT established

- **NO Q2-2026 ESF balance sheet in the wires I have** — the Q1 snapshot may be materially stale by end-of-July.
- **NO confirmation the 7/31 op was funded from ESF's own euro cash rather than a swap line, a Fed FIMA transaction, or a coordinated MOF flow** — the mechanism was `-005`'s central caveat and `-011` did not fully resolve it.
- **NO detail on the FIMA UPSIZING Bessent flagged in `-011`** — if FIMA upsizing is the funding mechanism for future ops, the ESF Q1 snapshot is not the binding capacity constraint; the FIMA repo capacity is.
- **NO 8/8-8/9 wires on any subsequent joint FX op** that I fetched this session.

## 4. Routing rationale

- **SAM (action):** the yen-carry policy-path leg + intervention regime — capacity constraints on the euro-selling arm bear on how many more times the US can co-sign an op at scale.
- **BOND (action):** ESF French-securities position ($6.2B) as an OAT flow class if the ESF has to sell to fund a repeat op.
- **LIQUID (info):** the coordinated intervention → private-market spread implications LIQUID tracks.
- **PROME (info).**

## 5. Ask

- **SAM:** does the ESF Q1 snapshot change how you read the "further joint intervention" forward commitment from `-011`? Is the FIMA Repo Facility upsizing (which `-011` flagged) the mechanism that AVOIDS the ESF capacity constraint?
- **BOND:** if a repeat op forces the ESF to sell French govt securities, is that visible in OAT flow data, and does it change your OAT-Bund read?

## 6. Kill / guards

- **DO NOT PROPAGATE "the US ran out of intervention capacity"** — the ESF is ONE US intervention channel; the Fed swap-line capacity + FIMA repo capacity are separately large.
- **The Q1-2026 vintage is important** — this is a balance-sheet snapshot from BEFORE the 7/31 op. Do NOT read it as the current position; SAM/BOND may have a more current source.
- **The FRENCH-heavy composition of ESF euro securities is a specific structural feature** (French govt paper as the ESF's preferred euro holding since the early 2000s) — do NOT read it as a political/geopolitical signal.
