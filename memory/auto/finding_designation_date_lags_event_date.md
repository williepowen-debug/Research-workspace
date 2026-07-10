---
name: finding_designation_date_lags_event_date
description: "An official disaster/aid DESIGNATION date (USDA FSA, FEMA, SBA) lags the physical event by weeks-to-months — never attribute a designation to its announcement month in a time-window analysis; trace to the underlying event date"
metadata: 
  node_type: memory
  type: finding
  originSessionId: cb850d17-5aa7-48f3-a41d-56fcd6c45a8a
---

Official **disaster/aid designation dates are administrative, not physical** — USDA FSA Secretarial disaster designations, FEMA major-disaster declarations, and SBA declarations routinely lag the underlying weather/loss event by **weeks to months** (the paperwork/qualification pipeline). If you catalog shocks by *designation date*, you will mis-bin events into the wrong period.

**How to apply:** in any time-window analysis (which shocks happened in month/quarter X?), treat a designation as a **pointer to an event whose date you must look up separately** — never count it in the window its announcement fell in. Read the "due to" cause + underlying-event date in the designation text before binning.

**Live instance (DEWEY prompt-11, 2026-07-10):** a USDA FSA "20 Florida counties" freeze designation was **dated 4/29/2026** but the underlying freeze was **Jan-23→Feb-5 2026**; GA/SC peach (~80%/~50-75% loss) and FL strawberry (~$3.1B) were likewise Q4-2025/Q1-2026 freezes whose FSA designations merely *landed* in April. Binning them as "April produce shocks" would have **double-counted the winter-freeze catastrophes into the Apr-Jun window** and falsely inflated the fresh-supply-shock read behind an elevated F&V-CPI print — inverting the forward call (a fading base effect looks like a fresh shock). Caught by reading the designation cause/date, not the announcement date.

**Recurs for:** any climate/ag/insurance/disaster research — [[project_energy_strike_ledger]] adjacency, and especially AEOLUS (climate), CORAL (FL insurance/disaster), MARCO (migration/disaster displacement), CARL (food-CPI). Kin to [[finding_number_carries_threshold_unit_source]] and [[finding_tool_default_asof_date_drift]] (a datum carries its own as-of/vintage; here the vintage that matters is the *event* date, not the *record* date). Same family as [[finding_refuted_claim_citation_vs_fact_failure]] — surface features of a source (its date field) can mislead if consumed uncritically.
