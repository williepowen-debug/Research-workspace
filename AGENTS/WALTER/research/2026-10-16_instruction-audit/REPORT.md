# WALTER instruction audit — 2026-10-16

Requested by Will: identify material that can be condensed, pruned or shortened, including superseded, redundant and duplicated instructions. **Review only: no charter, design spec, threshold, approval or shared operating rule was changed.** The later approval concerning missing-source searches (#4) is separate and is recorded in LAST_COMPLETION.md after this audit.

The main problem is current procedure mixed with accumulated incident history and copied facts. Shortening should leave an executable checklist, retain the reasons in on-demand history, and replace copied inventories with trips to their actual owners. Some copies have already drifted enough to change behavior.

## Scope and size

Whole-document review: WALTER CLAUDE.md, MEMORY.md, design/BOOT_PROTOCOL.md and design/SPEC_OWNERSHIP.md. Root CLAUDE.md, AGENTS.md and USER.md were explicitly read; selected claims were checked against the owning specifications, registries, code and dated evidence listed below. This is not an exhaustive audit of every linked spec, all fleet instructions, or every old research file. Snapshot hashes and measurements: [inventory.json](inventory.json).

| WALTER file | Bytes | Lines | Assessment |
|---|---:|---:|---|
| CLAUDE.md | 70,223 | 204 | Primary priority: above the canonical 32,550-byte whole-read budget. Long lines hide the size. |
| design/BOOT_PROTOCOL.md | 71,306 | 221 | On-demand rationale; duplicated and historically layered. Do not turn it into another required whole read. |
| design/SPEC_OWNERSHIP.md | 24,016 | 82 | Navigation table carries lengthy version histories and copied authority claims. |
| MEMORY.md | 22,545 | 98 | Within the current byte/line limits; several findings still carry long incident narratives. Adjudicate before moving. |

No savings percentage is certified: a complete shortened draft and a rule-conservation comparison have not been produced. The rotation stop is below70% of the binding budget: **22,785 bytes**, not merely below32,550. Target that stop without dropping operational conditions. A line-count target alone will not do that.

## Confirmed superseded or misleading copies

Locations refer to the inventory snapshot. BP means design/BOOT_PROTOCOL.md; SO means design/SPEC_OWNERSHIP.md.

| ID | Location and finding | Proposed correction and what must survive |
|---|---|---|
| A01 | CLAUDE:46–52 retires Quick mode, then the Iran guard still says to escalate to Full and refers to route-only mode. | Replace obsolete branches with the actual verification requirement and qualified-routing behavior. Keep the Iran guard, not the retired mode machinery. |
| A02 | CLAUDE:80 says not to hardcode HANS counts, then embeds a 14-row inventory. HANS now has 17 rows. | Read the complete ID set and eligibility from HANS/registry/THRESHOLDS.tsv. Keep daily/monthly/event distinctions, both compound legs, post-hoc evidentiary weight, and T12's no-feed limitation. Do not merely change 14 to another soon-stale number. |
| A03 | CLAUDE:76 repeats the old FT-08 monthly-CPI AND three-month condition. | Refer to RED/registry/FALSIFICATION_TRIGGERS.tsv and the owner's current grade. Its machine metric is CORE-CPI-3MO-ANN ≥3.0; the October14 owner ruling explicitly resolves the 0.3 monthly-print case under the later approved tree. The registry itself preserves conflicting older text for review: do not pretend the whole row is internally clean or rewrite it from WALTER. Preserve current-fire versus future-fire weights and exit conditions. |
| A04 | CLAUDE:99 calls the X refresh-failure path not live validated. | X_BOOKMARKS_ACCEPTANCE.md:124–128 records October10 HTTP400 → exit1, nothing marked. State **one cause observed once**; N1 and L4 remain untested live. Consolidate the acceptance doc's earlier status with this later update while preserving dated history. No silent fallback or broader validation claim. |
| A05 | CLAUDE Rule12 and SO's operator-brief row claim WALTER's caveat-placement wording is absent from fleet rules / not adopted elsewhere. | Root CLAUDE.md §Output Canon now contains the wording. Cite that rule; retain WALTER's delivery mechanism and worked-example spec. Remove the false exception and duplicated seven-rule exposition. |
| A06 | BP §6b describes registries as identical eight-column files and an old RED inventory. | RED currently has 19 columns; REGINALD has its own schema. Describe reading each canonical schema and all rows, not a copied fixed shape. Preserve old schema descriptions only as explicitly historical provenance. |
| A07 | BP §7e repeats HY ≥280; current charter step7e records the corrected strict >280 operator. | Reconcile the stale copy to the current boundary letter, including its BROCK conjunction. Equality is meaningful: this is not cosmetic shortening. |
| A08 | BP §11 speaks of automatic closeout pushing, while charter16 and BP §16 carry WALTER's coordinated-push exception. | Point to BOARD_CONSUMPTION_SPEC §7 and root Git protocol. Keep foreign-work deferral, narrow FLASH/IMMEDIATE exception, exact-path commits, recovery checks and post-publication reconciliation. |
| A09 | BP §0.5 check28 presents TERRY's old override/falsifier gate as a live control. | tools/walter_doctor.py:2404–2480 explicitly reports the retired lane as historical INFO. Update the description, not the historical evidence or checker by assumption. TERRY's current BOARD choice remains distinct from other pull-complete desks. |
| A10 | SO still names Quick-escalation and old cron boot dependencies; its closeout footer refers to an in-STATUS session log. | Remove dead dependencies. Keep retired cron paths as short tombstones pointing to RESEARCH-INTAKE. Current session entries go directly to SESSION_LOG.md under charter12(d). |

## Safe condensation candidates, with guardrails

| ID | Material | Recommended treatment |
|---|---|---|
| B01 | Charter's lengthy incident accounts: anchor cap (68), old carry (70), intake miss (87), availability anecdote (106), batch miss (114), Trepp example (121), STATUS-heading losses (142–145), 774 delivery repairs (160). | Leave trigger → action → condition/failure → canonical pointer. Move unique incident text verbatim to labeled history; deduplicate against BP only after comparison. The charter itself already declares this action/history split at56–58. |
| B02 | Identity, Rules1/3/4/10/13 and procedure repeat role, routing, readiness and durable delivery obligations. Rules7/11 also repeat root rules. | Keep a short identity and stable rule anchors; point to the enforcing procedure/root rule. Preserve an explicit trip to that procedure, not a passive reference nobody reads. Do not renumber externally cited rules. |
| B03 | SO's BOARD_CONSUMPTION_SPEC cell contains a long version-by-version narrative immediately before saying the cell should contain only current version and concept map. | Keep purpose, canonical concept map and current-header pointer. Version history belongs in the spec's own history. Same treatment for copied domain, channel and schema counts elsewhere in SO. |
| B04 | COP retirement repeated in steps5/10 and embedded memory; Quick and dead cron descriptions repeatedly explained. | Keep short no-op tombstones at stable step IDs and one history pointer. Do not reintroduce their reads or launch branches. |
| B05 | MEMORY findings28/29/41/43 and the opening size-history block contain lengthy recurrence stories. | Retain one actionable trigger and owning-surface link; preserve unique incidents in MEMORY_PROMOTED.md before reducing. Finding29's late-work reconciliation, finding41's unknown availability and finding43's basis protection remain active. Do not perform a blind date-based rotation. |
| B06 | CLAUDE:101/106 and BP §9 copy file counts, historical total bytes and the ORCH view's old approximate size. | Replace with actual discovery/measurement. ORCH_INFLIGHT is 26,433 bytes at this snapshot. Remove the categorical claim that rows appear only at delivery: MEMORY41 documents spawn-time rows. Re-read current coordination evidence before judging availability. Dirty files alone do not prove a desk is running now. |
| B07 | Runtime-specific instructions: embedded image-capability assertion, Telegram Claude settings/launch flags, ~/.claude auto-memory path, verification-helper dollar estimate. | Separate universal duties from conditional runtime adapters. Canonical auto-memory is documented in docs/AUTO_MEMORY.md; the Claude path remains a valid adapter, not a dead path. Detect actual image/messaging tools. Remove the unsupported fixed cost claim while retaining helper scope and authorization. |
| B08 | BP repeats rationale within cluster_review; charter Rule8 says the lookup table is “below” after it moved out. | Delete exact prose duplication and fix the link to SO. Keep check names and BP section anchors used by guards. |

## Resolve meaning before shortening

| ID | Problem | Required treatment |
|---|---|---|
| C01 | Rule3's “if no REGISTRY row, it doesn't exist” and SO's authority description conflict with root AGENTS.md's membership/classification authority. | Split concepts explicitly: PROME/ROSTER.md owns roster membership/classes; WALTER's routing sources own routing; domain owners own evidence/judgment. A missing mirror row is a defect, not proof a desk does not exist. |
| C02 | Rule6 says FLASH bypasses the filesystem; Rule10/step11 require durable BOARD and handoffs. | Clarify notification timing versus durable delivery under BOARD_CONSUMPTION_SPEC §3.4. Do not delete either obligation or infer that urgent routing waives its record. |
| C03 | Rule13 says “I never spawn”; Rule9 authorizes bounded verification helpers. | Qualify the ban as domain-desk orchestration, preserving the helper permission and its limits. Runtime availability still controls whether a permitted method can be used. |
| C04 | Rule5's HY +25 shorthand, overlays' >25 single-session threshold, and differing FLASH versus minimum-IMMEDIATE descriptions. | Reconcile exact operator, session basis and precedence at the canonical routing rule. Do not silently choose an interpretation while editing prose. |
| C05 | CLAUDE:82 gives one blanket FRED publication clock, including weekly ICSA. | Use series-specific observation and publication dates, preserving first-published grading and owner calendar rules. The October16 morning HY October15 witness in research/2026-10-16_finish/verify-red-reg.md already defeats a universal session-before-last assumption. This correction does not change any threshold. |
| C06 | CLAUDE:73/83 still show September30 review dates; registry/signal_read_companions.json also has review_due2026-09-30. | Treat the companion expiry as an unresolved review duty. Check actual evidence/hashes and resolve or explicitly carry it; do not erase the date or automatically renew it as housekeeping. Other stale calendar reminders may be condensed only after distinguishing them from enforceable expiry. |

The short “three gates” wording versus FILTER_SPEC's two hard gates plus soft credibility/pre-gate bypass also merits terminology cleanup, but is not sufficient evidence of a behavioral contradiction by itself.

## Keep intact

- Approval conditions, numbered step/rule anchors, 7g-before-7e ordering and REGISTRY13-before-STATUS12(b) ordering.
- Different CARL/RED/PROME/TERRY delivery exemptions; saved versus published versus consumed distinctions; correction recipient unions; fail-loud source and runtime limits.
- Signal intake template: SO records active consumer references and explicitly retracts its earlier proposed retirement. Age does not establish supersession.
- Dated historical quotations, frozen approval records and registered pending-event artifacts. Move provenance if useful; do not rewrite history as current procedure or destroy it as duplication.
- October17 X pilot review and other upcoming duties. An approaching date is not stale clutter.
- Read-cap and attestation failures until actually repaired. Selected successful checks do not certify a whole boot.

## Recommended sequence

1. Correct confirmed stale current claims at their WALTER-owned locations, with canonical-source references. Resolve C-class ambiguities separately; do not hide policy choices inside editorial edits.
2. Produce a shorter charter retaining every action, condition, exception and stable anchor. Move unique rationale/history verbatim; use conservation checks for moved text and a rule-by-rule semantic comparison for shortened instructions.
3. Condense SO to ownership/navigation and BP to current rationale plus clearly labeled history. Stop maintaining copied inventories. Update dependent pointers and versions together.
4. Reduce MEMORY only where an owning surface exists; preserve the firing trigger. Then remeasure and run the relevant existing pointer/version/read-cap/closeout guards.
5. Separately classify old research/source artifacts under root's >60-day, non-boot-read, non-live-reference rule and pending-event exception. That exhaustive archival sweep remains unperformed; this audit does not certify deletion eligibility.

PROME was concurrently changing fleet procedures, so this audit takes a measured snapshot and leaves shared files untouched. Before implementation, re-read changed owners; root CLAUDE.md is24,961bytes and the ORCH view26,433bytes at this snapshot. Both are below the budget but above the75% rotation trigger; their maintenance advisories remain valid. The generated ORCH view requires a source/generator remedy by its owner, not manual rotation.

## Missing-source searches (#4), separately approved

Will approved stopping repeated searches after this audit. Close the search attempts, not the evidence gaps: Iran reopens on fresh official evidence or owner review; Volta yield on final documents or materially better reporting; Korea/freight on the next relevant update if the exact reading matters; oil settlement/property census on a reliable source or owner record. This approval does not retire mandatory boot checks, change a threshold, supply missing data, or install monitoring. The operative carry and reopen conditions belong in LAST_COMPLETION.md, not another obligation registry.
