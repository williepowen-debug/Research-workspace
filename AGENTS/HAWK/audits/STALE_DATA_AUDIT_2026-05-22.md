# HAWK Stale Data Audit — 2026-05-22

**Scope:** Narrow staleness audit after the 2026-05-22 HAWK refresh. This file does **not** change HAWK's refreshed scenario; it flags remaining stale, weakly sourced, internally inconsistent, outdated, unverified, or follow-up items for the next pass.

**Files reviewed:** `AGENTS/HAWK/STATUS.md`, `LAST_COMPLETION.md`, `CALENDAR.md`, `workbook/KB.tsv`, `board_log.tsv`, `inbox/processed/`, `AGENTS/WALTER/anchors/IRAN_WAR.md`, and recent Iran/Hormuz BOARD signals through `SIG-W-20260521-031`.

## Prioritized stale/suspect items

| Priority | Item | Current/stale claim | Why stale or suspect | Source/file | Recommended update action | Owner/recipient | Deadline/catalyst |
|---|---|---|---|---|---|---|---|
| P0 | May 22-23 Gulf hold expiry | Calendar/STATUS treat Gulf allies' 2-3 day hold as immediate decision point | This expires essentially now; if no framework appears by May 23, scenario weights may already need adjustment toward re-ratchet/grind | `CALENDAR.md`; `STATUS.md`; `IRAN_WAR.md` | Re-check public Trump/Gulf/Iran language and framework text; update watch item outcome only, not full thesis unless state changed | HAWK + WALTER; RED/NEXUS info | May 23 close / first confirmed framework or failure signal |
| P0 | Barakah attribution | “Iraq-origin drones” logged; no direct Iran blame | Direct UAE attribution would materially change escalation risk; current state is proxy-route inference, not state attribution | `STATUS.md`; `KB-HAWK-145`; BOARD `SIG-W-20260521-001` | Monitor UAE MoD/IAEA/Barakah operator statements; separate direct-attribution from analytical proxy inference | HAWK; RED/NEXUS | Any UAE attribution change or second nuclear-infra strike |
| P0 | Hormuz traffic / carve-out breadth | “Chinese supertankers exited” and “selective egress expanding”; old zero-crossing claims retained as unverified | Needs AIS/Kpler/MarineTraffic confirmation of queue/backlog and whether non-China/non-Qatar classes are moving; “zero crossings” conflicts with 5/20 egress | `STATUS.md`; `KB-HAWK-147`; processed May 9 zero-crossing signal | Verify actual transit counts by flag/class and backlog clearance rate; kill or downgrade “zero traffic” language where still active | HAWK + BRENT; ZHAO/SAM info | Third non-China/non-Qatar permitted transit or next Kpler/AIS update |
| P0 | Insurance/owner appetite | STATUS says war-risk coverage exists but remains uneconomic / crew-safety constrained | Corrected mechanism rests on 5/6 LMA/Lloyd's state; no fresh 5/12-5/21 insurance quote check was run | `STATUS.md`; `IRAN_WAR.md`; older KB-HAWK-033 says “uninsurable” | Replace old “uninsurable/P&I refusing” claims with corrected “available but uneconomic + crew-safety” framing; pull fresh war-risk quote if used in signal | HAWK + BRENT + LIQUID | Before any insurance/transit signal; no later than May 29 |
| P1 | KB duplicate IDs | `KB-HAWK-131` and `KB-HAWK-132` each appear twice with different facts | Internal referential integrity problem; future DerivedFrom references can point to wrong item | `workbook/KB.tsv` | Renumber older duplicate rows or migrate to unique IDs; check DerivedFrom links after edit | HAWK | Next KB maintenance pass |
| P1 | Stale active KB entries with expired `Stale_By` | 58 ACTIVE/CONFIRMED/WATCH rows have review dates before 2026-05-22 | Many March/April facts remain marked ACTIVE despite changed war regime; creates false continuity | `workbook/KB.tsv` | Batch review: mark superseded/corrected/archival; preserve load-bearing structural facts only | HAWK | Before next substantive HAWK refresh |
| P1 | Old scenario/probability KB | `KB-HAWK-028`: A 10 / B 55 / C 35 / D 5; `KB-HAWK-034`: convergence 37/45 red-red | Current STATUS is C 55 / D 35 / B 10 and convergence 33/45; old rows still ACTIVE | `workbook/KB.tsv` | Mark superseded by May 22 STATUS or add cross-reference to current scenario | HAWK + RED | Next KB maintenance pass |
| P1 | Brent/tape levels embedded in HAWK KB | `KB-HAWK-025` Brent $90, `KB-HAWK-137` Brent $95.42 remain ACTIVE; STATUS references $104.93 May 20 close | HAWK intentionally defers prices to BRENT; stale tape numbers can mislead convergence scoring | `workbook/KB.tsv`; `STATUS.md` | Mark old price rows archival/superseded; keep only references that explicitly defer to BRENT with observation date | BRENT owns; HAWK info | Before citing price/tape again |
| P1 | Kpler export-flow chart | 2026 exports Global −14% / OPEC+ −29% Jan→May | Strong but chart-snapshot from Will image batch; needs ongoing monthly tracking and axis verification if used quantitatively | `KB-HAWK-150`; BOARD `SIG-W-20260521-031` | Ask BRENT/WALTER to maintain Kpler monthly check; avoid overfitting single chart snapshot | BRENT; HAWK/SAM/LIQUID info | June Kpler update or next export-flow image |
| P1 | Rapidan product-inventory tail | “closure through August could exhaust product inventories / GFC-scale contraction risk” | Correctly marked tail, but could drift into base-case language if not anchored to August/closure assumption | `STATUS.md`; board_log `SIG-W-20260521-023` | Keep as tail scenario; require BRENT primary before scenario-weight change | BRENT + LIQUID; HAWK info | If Hormuz remains blocked into June/July |
| P2 | May 9 undersea cable claim | Iran considering control/permits/fees over 7 cables | Screenshots/aggregators only; no primary/operator/legal confirmation | `STATUS.md`; `CALENDAR.md`; `KB-HAWK-149`; processed inbox signal | Verify cable operators, Iranian legal authority, IRGC statements; keep WATCH not ACTIVE | HAWK + HENRY + LIQUID | Before any cyber/data chokepoint dispatch |
| P2 | Old fertilizer/food CPI chain | Multiple March rows still ACTIVE: fertilizer shortage, USDA Mar 31, Q3-Q4 food CPI | Some catalysts passed; needs outcome check against USDA/FAO/fertilizer prices and current energy regime | `KB-HAWK-073`, `125`, `126`, `108` | Route update to CARL/BRENT or archive stale catalyst rows; keep structural sulphur/copper if still relevant | CARL + BRENT; HAWK info | Before Q3 food-CPI thesis is reused |
| P2 | Global hydrocarbon incident cluster | `KB-HAWK-142`: 11 non-ME hydrocarbon incidents; confidence 0.70, per-row unverified | Aggregator/base-rate issue; still marked ACTIVE after stale date May 15 | `workbook/KB.tsv`; board_log `SIG-W-20260420-003` | Either NEXUS validates as cluster or HAWK marks WATCH/low-confidence | NEXUS + HAWK | Next NEXUS cluster pass |
| P2 | Apr 18-20 BOARD items partially integrated | Several April board_log entries say “propose KB” / “flag discrepancy” and then rows were added, but stale wording remains | Audit trail reads like open proposal even after integration; may confuse future refresh | `board_log.tsv` Apr 20 rows; KB-HAWK-138..144 | Add resolved note or leave as historical; no scenario impact | HAWK | Low priority cleanup |
| P3 | Processed inbox hygiene | May 9 signals moved to `inbox/processed/`; git shows source deletions + untracked processed copies from prior refresh | Operationally fine but not committed/staged; future agent may interpret as lost/missing if only status seen | `git status`; `inbox/processed/` | Leave unless committing; ensure processed copies are tracked if a commit happens | Prome/HAWK | Next scoped commit |

## (a) Time-sensitive catalysts

1. **May 22-23 Gulf hold expiry:** immediate re-check required. The audit did not run a fresh web/AIS sweep; if the hold expired silently, the refreshed C 55 / D 35 may need pressure-tested.
2. **May 25-29 deferred-strike/rhetoric window:** watch Trump language moving from “no hurry” back to deadline/force; this is the next scenario-weight catalyst.
3. **Barakah follow-through:** second nuclear-infrastructure strike or direct UAE attribution should trigger a HAWK/RED/NEXUS refresh.
4. **Third Hormuz carve-out class:** non-China/non-Qatar egress would make “selective carve-outs expanding” stronger; halt/reversal would undermine thaw.
5. **May 28 IRAN_WAR weekly re-verify:** hard boundary from WALTER anchor if no earlier kinetic/diplomatic state change occurs.

## (b) Unverified claims

- **Undersea cable-control claim:** still WATCH only; no primary/operator confirmation found in reviewed files.
- **May 9 “zero crossings” / total closure language:** later 5/20 Chinese egress means any durable-zero framing is suspect without AIS/Kpler proof.
- **Insurance normalization/barrier:** corrected mechanism is “available but uneconomic + crew-safety,” but current premium/owner appetite was not re-checked after May 6.
- **Kpler export-flow exact percentages:** likely useful, but derived from a shared chart image; needs BRENT continuity if numbers become load-bearing.
- **Iran sanctions-waiver offer:** explicitly Iranian-media-only / unconfirmed US-side in the anchor.
- **5/8 casualties / Ocean Koi cargo specifics / second Qatari LNG status:** flagged by `IRAN_WAR.md` as still requiring primary verification.

## (c) Stale numeric/tape data

- **58 active/watch/confirmed KB rows have stale dates before 2026-05-22.** This is the main remaining stale-data burden.
- Old Brent rows (`KB-HAWK-025`, `KB-HAWK-137`) should be archived or clearly marked as historical; HAWK should defer all current tape to BRENT.
- Old Hormuz shipping rows (`KB-HAWK-023`, `045`, `143`) mix March/April closure stats with current May selective-egress regime; preserve chronology but stop treating them as current state.
- Old fertilizer/food-chain rows have passed catalysts (USDA Mar 31, FAO Apr 3, mid-April planting) and need outcome checks before reuse.
- `KB-HAWK-033` “uninsurable” conflicts with corrected LMA/Lloyd's mechanism in `IRAN_WAR.md`.

## (d) Stale scenario/probability language

- `KB-HAWK-028` and `KB-HAWK-034` are superseded by May 22 STATUS but still ACTIVE.
- April board/KB language around imminent ceasefire expiry and full collapse remains useful as historical path but should not be read as present base case.
- The current refreshed model is **bifurcation**: C/Grind-Partial-Thaw 55% / D-Reescalation 35% / B-Deal-Reopen 10%. Any older “diplomatic exit structurally further / no carve-outs” language should be stepped down unless explicitly historical.
- Rapidan August closure/product-inventory exhaustion is tail, not base. Keep conditional language tied to sustained closure through August.

## (e) Cross-agent dependencies

| Dependency | Why it matters | Suggested recipient/action |
|---|---|---|
| BRENT | Owns current oil prices, Kpler/export-flow, insurance/war-risk economics, Rapidan inventory tail | BRENT should own numeric/tape refresh and monthly export-flow continuity |
| WALTER | Owns `IRAN_WAR.md` anchor and signal routing; next weekly re-verify due May 28 | WALTER should update anchor if May 22-29 state changes before weekly boundary |
| RED | Needs bifurcation update to avoid both “deal solved it” and “hardening only” errors | RED should stress-test C 55 / D 35 after hold expiry |
| NEXUS | Needs cluster classification for Barakah nuclear-infra and global hydrocarbon-infra incident pattern | NEXUS should decide whether `KB-HAWK-142` is real cluster or aggregator noise |
| ZHAO/SAM | China/Asia carve-outs and LNG/oil exposure depend on Hormuz queue details | Route third-carve-out/China egress updates to ZHAO and SAM |
| HENRY/LIQUID | Cyber/data chokepoint and energy-credit stress depend on verification | Keep undersea cable item WATCH until primary confirmation |
| CARL | Food/fertilizer/pump-pass-through claims need consumer/inflation outcome checks | CARL/BRENT should update old fertilizer and pump lag rows before Q3 reuse |

## Bottom line

The May 22 refresh fixed the headline HAWK frame, but the **workbook still carries a large historical/stale tail**: expired active rows, duplicate IDs, old price/scenario language, and several unverified May claims. The next pass should be a cleanup/verification pass, not another thesis rewrite, unless the May 22-29 catalyst window breaks decisively.
