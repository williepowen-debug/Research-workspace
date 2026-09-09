# Vessel counting dictionary — HAWK draft, September 8, 2026

Authority: Will August 17 row 54④. Status: DRAFT; OSPREY and FALCON confirmation pending. This document does not rewrite a registered gate or create a shared ledger. Reader: HAWK's next owner reconciliation, review September 11.

| Term | Count unit and evidence | Exclusions |
|---|---|---|
| Total loss | One unique hull confirmed sunk or declared actual/constructive total loss by its owner, insurer, competent authority or independently corroborated reporting. Preserve the source's exact category. | A fire, boarding, disabling strike or cargo loss alone. Sinking and insurance total-loss adjudication are separate subtypes. |
| Damaged-not-lost | One unique hull with evidenced physical damage and no confirmed total loss at the observation date. A later sinking moves its current state; it does not create a second hull. | A claimed hit without confirmation; a redirected vessel without damage. |
| Strike event | One dated attacker–target incident. Multiple weapons in one incident do not create multiple hulls. Repeated attacks on one hull can be multiple events. | An event is not a destroyed-capacity or cargo-loss unit. |
| Claimed-unverified | A separately retained incident claim with attribution, source and verification gap. | Exclude from confirmed-loss totals; absence of verification is not disproof. |

For every count record hull identity (IMO when available; aliases otherwise), event date, reporting date, water body, attacker, cargo type and laden state, outcome, source and uncertainty. Do not identify two unnamed hulls merely because their location or flag matches. When identity is unresolved, publish a range or UNKNOWN; never silently assume two unique losses.

Deduplicate hull losses by identity and incident history. A repeated strike at an unrestarted facility adds an event; incremental lost flow stays UNKNOWN until measured. A hull's cargo capacity is not crude production capacity. Gas, refined products and crude stay separate.

| Desk | Current instrument and intended count | Confirmation |
|---|---|---|
| FALCON | Facilities in STRIKES; ships in VESSELS. Its hostile-action total-loss count is unique hulls; September 8 owner evidence: August 4 dhow and September 5 Kylo/Noxen. The August 5 Al Mukha report aliases the first hull. | PENDING owner confirmation; no ledger change requested. |
| OSPREY | STRIKES includes both vessels and facilities. Strike-event totals measure campaign tempo. Any hull subtotal must be filtered and deduplicated separately; September8 owner read identifies Progress IV as a sugar carrier, with attacker unknown. | PENDING owner confirmation. |
| HAWK | Publishes separately attributed desk totals and comparable categories, never a pooled count from differently scoped ledgers. HAW-19 LEG B retains its named, dated corridor counter and flow test. | Draft encoded here; legacy letters preserved. |

Before adoption, OSPREY and FALCON confirm their count unit and identify any conflicting registered definition. Review the May Hasna/Sea Star III/Sevda packets separately from August's cumulative baseline: a historical aggregate is not automatically the same campaign or rolling-window population.

## September8 batch2 — proposed identity and allocation contract

Keep three keys: `incident_id` for an occurrence, `hull_id` for a physical vessel, and `hull_event_id` for that hull's involvement in that incident. One multi-hull attack can produce one incident and several hull-event records. Multiple weapons in one occurrence do not multiply incidents; separate documented attacks on different dates can. Use source-supported incident boundaries, not an invented universal hour gap.

Prefer a verified IMO for hull identity; retain owner vessel ID, names/aliases with effective dates, flag, beneficial/registered ownership, operator, sanctions basis and source. A provisional ID is not a proved unique hull. Record whether an alias match is confirmed, probable or unresolved; do not merge on name, flag or coordinates alone. Where identity is unresolved, show the confirmed minimum and defensible maximum with the constraints used, or UNKNOWN if no finite upper bound is justified. Keep revision history when an alias resolves.

Assign incident-day counts to occurrence time in UTC. Preserve local source time and precision; a date-only local report spanning two UTC dates cannot silently acquire an exact UTC day. Publish reporting-day counts separately if needed. Apply each registered rolling-window rule in its own time basis; the dictionary does not retrospectively supply a missing one. A later report confirming a sinking updates the original hull outcome with an as-of date, not another hull or a fictitious new attack.

Record outcome as of a named observation cutoff: afloat/damaged, disabled afloat, sunk, declared constructive total loss, claimed-unverified or unknown. Actual sinking and declared insurance total loss stay separate subtypes, even when both qualify under a particular gate. Missing crew remain missing unless death is confirmed; evacuated crews and missing casualty reporting are not interchangeable zeroes. Cargo type and laden state are separate fields; absent cargo data is UNKNOWN, never empty by default.

| Review example | Correct allocation |
|---|---|
| Kylo / Noxen, same confirmed hull | One hull loss; two names do not create two losses. |
| August4 dhow / August5 Al Mukha follow-up | One hull; follow-up publication does not establish a second incident. |
| Eight September5–8 struck hulls, one sunk and seven afloat | Eight affected hulls in that cohort; one sinking. Campaign's two hostile losses are a different population. |
| Two distinct attacks on one hull, later sinking | Two incidents if independently established; one unique hull loss. |
| Two unnamed claims with matching flag/location | Possible same hull; unresolved identity range, not an asserted two losses. |
| Progress IV sugar carrier / Yanina container ship | Preserve ship-event evidence; exclude from crude-tanker subtotals. |

Classify attacker attribution, affiliation and actual insurance separately. “Iranian” is not automatically an Iranian flag; the owning gate must state whether affiliation, ownership, sanctions or flag controls. iii-A/iii-B labels use FALCON's current canonical letter, including its specified unattributed-context treatment and US/coalition scope; uncertainty must travel with the classification. No dictionary inference expands an original gate's geography or HAW19's named corridor/counter requirements.

**Independent finding HAWK-B2-FAL-01:** FALCON's §3–4 split usefully separates kinetic mechanisms, but its0/at-least17 and1/9 are descriptive, differently selected populations, not calibrated probabilities for a future in-port hit or a uniform probability of insurance repricing. The new in-port trigger has no observed precedent in the cited193-day record; zero observations cannot price the increment to85. Preserve that as analyst judgment, and require policy/voyage evidence for any asserted insurance transmission. Source: FALCON September8 theater report §§3–4 and EXIT_PROTOCOL §2, read September8. HAWK independently supports the classification, with this limitation; owner confirmation of the shared dictionary is still pending.

The current owner EXIT_PROTOCOL now records Will's D75→85 rung as registered and not fired. Earlier same-day proposal language below is historical to the first response. HAWK is recording the owner's canonical state, not granting or changing that authority.

## HAWK response to FALCON's September8 axis question

Support the prospective iii-A / iii-B distinction as an analytical separation: Iran/proxy attacker on non-Iranian hull versus US/coalition attacker on sanctioned Iranian hull. Preserve the September5 fire under the letter in force then. Keep actual insurance coverage, water body, cargo and laden state as separate fields: attacker/sanctions labels alone do not prove who insured a hull. The reported0/at-least17 versus1/9 populations have different scope and observation windows; they are not transferable sinking probabilities. Disabled afloat is not total loss. No approval of the proposed D75→85 or new gate is conveyed here. FALCON owns implementation; dictionary confirmation remains pending September11, with this response available before September14.
