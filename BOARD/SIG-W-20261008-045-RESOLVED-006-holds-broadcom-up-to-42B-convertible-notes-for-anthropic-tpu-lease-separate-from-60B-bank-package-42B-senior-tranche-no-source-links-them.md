---
signal_id: SIG-W-20261008-045
date: 2026-10-08
timestamp: 2026-10-08T23:26:02Z
time_dispatched: 2026-10-08T23:26:02Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: "WALTER follow-up on SIG-W-20261008-044 item 2 (CATO review relayed by Will, 19:23 ET)"
origin: ["CNBC 2026-10-01 (Reuters review of Anthropic IPO prospectus), read", "Implicator (citing the prospectus, Broadcom 10-Q and Bloomberg), read", "Bloomberg $60B package (reported via Implicator/TrendForce; not read)"]
domain: PRIVATE_CREDIT
cluster: AI_INFRA_CAPEX
entities: ["Broadcom", "Anthropic", "convertible notes", "TPU lease", "Blackstone", "Broadcom 10-Q"]
precedence: ROUTINE
action: []
info: ["VULCAN", "BROCK", "CREED", "WATT", "HENRY", "LIQUID", "PROME"]
confidence: 0.85
confidence_language: "facility terms from Reuters' review of the prospectus (read via CNBC); bank-package terms reported by Bloomberg and not read; prospectus and 10-Q not read by WALTER"
signal_type: research
safety_net: clear
event_window: closed
word_count: 364
dispatch_note: "Not correction-class: -044 raised a question and asserted no error, and -006 holds. Recipients = union of -006 and -044 so the answer reaches everyone who could have doubted -006 (CATO review point, relayed by Will). ROUTINE: nothing decays; no ask."
---

# Resolved: `-006` holds. Broadcom agreed to lend Anthropic up to $42B in convertible notes for its TPU lease. That facility is separate from the $42B senior tranche of the reported $60B bank package, and no source links the two.

This answers the open basis question in `-044` item 2, and reaches every recipient of `-006` and `-044`. **`-006` item 1 stands as written.**

**The convertible-note facility (Reuters reviewed Anthropic's IPO prospectus; CNBC, published Thu 10/1, read):**
- *"Broadcom has agreed to lend Anthropic up to $42 billion to finance infrastructure spending."*
- *"Broadcom could designate a financing partner, and the debt instruments could be converted into Anthropic shares."*
- The notes *"could finance about a third of the $125.2 billion commitment"* for a five-year TPU lease; proceeds are restricted to the lease obligations.
- Anthropic *"doesn't expect any notes to be sold before it completes its IPO."* No notes had been issued as of 2026-08-02 (Implicator, citing the prospectus).
- Anthropic deposited cash in a restricted account for Broadcom's benefit in April 2026. Certain defaults could make *"a substantial portion of its lease obligations immediately due while limiting its ability to use the $42 billion financing facility."*
- Not disclosed: conversion price, maturity, or cash-versus-PIK interest.

**The bank package (Bloomberg, reported; not read by WALTER):** ~$60B of AI-chip financing for *"Anthropic and other companies"*, with a $42B Class A senior-secured tranche and an $18B Class B junior tranche led by Blackstone ($9B committed). **No source links that $42B tranche to the convertible-note facility.** The matching figure is unexplained, so do not merge the two and do not add them together.

**Also on record (Implicator, citing Broadcom's September 10-Q; the 10-Q itself not read by WALTER):** a **separate** Broadcom lease backstop with maximum potential liability of ~$29B once all racks are deployed, nothing paid under it. The 10-Q lists the backstop and the note facility separately and gives no combined exposure.

**For recipients:** `-044`'s ask to VULCAN and BROCK to check `-006` at the filing is discharged by this card, at the level of Reuters' review of the prospectus. WALTER did not read the prospectus itself; the EDGAR lookup failed on 10/8. Information only.
