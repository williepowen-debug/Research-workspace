---
request_id: REQ-DEWEY-20261022-006
from: WALTER (Will-approved in the WALTER terminal, 2026-10-22 ~12:30 ET, option B of WALTER's shortlist)
to: DEWEY
created: 2026-10-22 (UTC stamp in the commit)
state: NEW
flag_trigger: T3 load-bearing but thin (the fleet grades a live tanker campaign with no historical base rate) + T5 (claims vs confirmations keep diverging; a base rate helps judge them)
originating_evidence: SIG-W-20261018-002 (UKMTO: at least 10 vessels attacked in the week to 10/17, a record for this war) + SIG-W-20261022-007 (Iran full sweep: IRGC claims 4 STS tankers hit plus 3 mine strikes, CLAIM-ONLY; FALCON losses 4 confirmed + 1 contested; IRGC threat to US bases over escorts) + anchors/IRAN_WAR.md ladder item 2
clusters: IRAN_HORMUZ (secondary HYDROCARBON_INFRA)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-006
kill_condition: At intake, grep AGENTS/FALCON, AGENTS/BRENT and AGENTS/HAWK for an existing 1980-88 Tanker War base-rate table. If one exists, report its location and only fill its gaps.
deliver_by: no hard date; useful before the next FALCON 7-day review (10/28)
---

# DEEP-RESEARCH REQUEST — The 1984–88 Tanker War as a base rate for today's Gulf tanker campaign

**Why now:** attacks on merchant ships in the Gulf hit a record for this war in mid-October, Iran keeps claiming hits that operators and UKMTO do not confirm, and the IRGC is threatening US bases over escorts. FALCON and BRENT grade each event but have no historical base rate for how such a campaign evolves.

**Decision question:** in the Iran–Iraq Tanker War (roughly 1984–88), how many merchant ships were attacked, what share were sunk or declared total losses, how did attack rates, war-risk insurance and Gulf traffic evolve, and what ended it? Which of those patterns carry over to 2026 and which do not?

**What changes with the answer:** FALCON gets a reference rate for "attacks per sinking" and for how claims compared with confirmed damage, to calibrate its loss ladder; BRENT gets the historical traffic and price response to compare with today's transit floors; both get a view of what US escorts (Operation Earnest Will, 1987–88) did to attack rates.

## Scope (in bounds)

1. **Attack and loss counts.** Ships attacked per year by side (Iraq vs Iran), weapon type (aircraft missile, mines, small boats), and outcome (damaged, total loss, sunk, killed crew). Use Lloyd's, academic studies and US Navy histories; give each source's count separately where they differ, never average.
2. **Claims versus confirmation.** Evidence on how often belligerent claims of hits exceeded confirmed incidents.
3. **Insurance.** War-risk premium levels over time (percent of hull value), Lloyd's listed-area changes, and whether cover was ever withdrawn.
4. **Traffic and oil.** Gulf export volumes and tanker traffic through the period; oil price response to escalation phases; use of pipelines and shuttle tankers to avoid the danger zone.
5. **Escorts and ending.** Kuwaiti reflagging, Earnest Will, Operation Praying Mantis (April 1988), the USS Stark and Samuel B. Roberts incidents, and what changed attack rates. How the war's end (ceasefire August 1988) closed the campaign.
6. **Differences from 2026.** Drones and anti-ship missiles, ship tracking (AIS), insurance market structure, US posture. State which historical rates are unsafe to carry over and why.

## Out of bounds

Grading FALCON's ladder or BRENT's thesis; trade ideas (TERRY); current-day news collection (WALTER and FALCON own that).

## Deliverable

Tables over prose, every cell sourced and dated: (1) annual attack/loss table by side and weapon, with source disagreement shown; (2) insurance table; (3) traffic and price table; (4) escort-phase comparison; (5) carry-over vs not-carry-over table for 2026; (6) explicit UNKNOWNs.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-006. WALTER routes it as a research-output signal: FALCON action; BRENT, HAWK, SAM, RED and PROME info.
