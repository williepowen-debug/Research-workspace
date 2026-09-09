# Dashboard attention and coverage — September 9, 2026

Will approved the five dashboard additions: immediate broker actions, exact-position management coverage, evidence dates, PROME outstanding work and confirmed changes; reconcile stale priorities and already-ruled queue entries.

## Implementation contract

Holdings remain in FORGE/STATUS.md. Management metadata lives in FORGE/position_management.tsv, keyed by account, ticker, instrument and explicit expiry, with source evidence and its hash. No quantity or mark is copied into this registry. A changed or missing evidence file invalidates the associated metadata; missing coverage is visible. The renderer handles all three FORGE table schemas, preserves individual lots, and never associates a rule by ticker mention alone. Older holdings/account figures keep their original dates; the newly recorded QQQ contract carries its separate screenshot attribution.

Broker approval, order state and fill state are independent fields. No action is executed by these pages. Receipt amounts come from the receipt table, not recomputed account cash. PROME work comes from existing DOCKET rows, including overdue rows; a pending ledger row is not proof that an owner has not delivered. Build time, source dates and hosted publication are distinct.

Queue reconciliation preserves historical open rows below and records direct owner rulings, without substituting PROME's earlier recommendations. No unrelated agent file is edited.

## Prior queue rows (verbatim preservation)

### WQ-196

```text
| 196 | OSPREY batch: (a) withdraw frozen ~33% re-centre; (b) restrict Channel3 kill geography; (c) expand buyer-pullback to carriers/insurers or retire. | RULE | 2026-09-11 | 9/8 | (a) WITHDRAW, retain ~30%,25–35%[EST]; (b) RETAIN unqualified letter; (c) RETAIN pending reachable proposal, no carrier/buyer substitution. | PROME/proposals/2026-09-08_inbox-decisions-PROPOSAL.md §WQ-196; batched at owner request. No band or letter changed. |
```

### WQ-197

```text
| 197 | OSPREY strike-feed candidates: one DAEDALUS build session and bounded four-week evaluation, per owner spec. | RULE | 2026-09-11 | 9/8 | APPROVE with unique run IDs, explicit failure/freshness, publication-vs-event date separation, candidate-only matching and WALTER routing boundary; no automatic grading. | PROME/proposals/2026-09-08_inbox-decisions-PROPOSAL.md §WQ-197; build not started, boot integration pending owner verification. |
```

### WQ-199

```text
| 199 | OSPREY Tuesday/Friday sessions while elevated: bounded cadence trial, not a background scheduler. | RULE | 2026-09-11 | 9/8 | APPROVE four-week trial through October6, review then; reuse live owners and normal due-row preflight. | PROME/proposals/2026-09-08_inbox-decisions-PROPOSAL.md §WQ-199; no cadence activated or new session launched. |
```

### WQ-198

```text
| 198 | OSPREY downgrade-path draft for BRENT/HAWK comment and return to Will; no automatic adoption. | RULE | 2026-09-15 | 9/8 | REVIEW/REVISE ONLY; reject silence-as-approval and self-logging absence; require calibrated thresholds, source/missingness and transition rules. | PROME/proposals/2026-09-08_inbox-decisions-PROPOSAL.md §WQ-198; current marks and rules stay in force. Existing OWED15 work, no data-feed spend. |
```

### WQ-164

```text
| 164 | **CRUISE — retire the 7/2 arm-CCL fuel ladder, no replacement level** (DOCKET L220; *"Brent sustained >$85–90 = arm CCL"*, never Will-ratified, in-band 47 days; BZX26 $95.23 [9/2] satisfies it today). CRUISE's evidence (`PROME/inbox/processed/2026-09-02_from-CRUISE_PROPOSAL-retire-the-arm-CCL-fuel-ladder-no-replacement-level.md`, `98210a24f`; full memo `AGENTS/CRUISE/2026-09-02_LADDER_DISPOSITION_MEMO.md`): the 8/14→9/2 drawdown ranks by DEMAND tier, not hedge ratio — NCLH −18.1% (52% hedged) > CCL −15.6% (0% hedged, verified at two primaries) > RCL −12.9% (58%) — so a CCL trigger keyed to a Brent level reads clean while measuring something else; CCL's own sensitivity table (Q2 FY26 8-K 6/23, Ex-99.1) prices a 10% fuel move at $56M vs $60M per 1% of net yield ($0.041/sh vs $1.35 guided 3Q EPS), and corrects CRUISE's own carried "$145–156M per 10%" (~2.7× too large, fixed). Counterfactual DISCLOSED: armed at the 7/17 breach it would have paid (CCL −9.6%) for the wrong reason — ~12% underwater first, no drawdown clause, and NCLH would have paid double. Falsifiers registered so the retirement is gradeable: CRU-08 (80%) — a Q3 fuel-attributable EPS hit >$0.10 ⇒ this proposal is wrong; VX-CRU-06 — CCL excess drawdown over RCL >5pp. Fuel stays a tracked cost line (VX-CRU-02, graded at CCL's own $812/mt at the Q3 print). | RULE | — | 9/2 | **RULED 2026-09-03 07:41 ET (Will verbatim *"Approve WQ-151 with your rec and WQ-164 retire"*) = RETIRE the 7/2 arm-CCL fuel ladder, NO replacement level.** EXECUTED: DOCKET L220 RESOLVED; CRUISE packeted (dark; retires the ladder on STATUS:134 + the disposition memo at its next boot; fuel stays a cost line VX-CRU-02; falsifiers CRU-08 / VX-CRU-06 stand as the retirement's own grade). Any future cruise trigger = a NEW registration keyed to the demand tier, two legs, drawdown clause. *(pre-ruling rec + proposal text → `git show HEAD:PROME/WILL_QUEUE.md` row 164.)* | done
```

### WQ-162

```text
| 162 | **RULED 2026-09-02 21:29 ET (Will verbatim *"Approve WQ-162 with your recs"*; record `PROME/proposals/2026-09-02_wq162-RULED.md`) — EXECUTED same sitting:** GATE-HY-REKILL letter rewritten SELF-GRADING (no state change: NOT FIRED 0-of-2) · vintage convention (AS FIRST PUBLISHED, per observation, as a CONVENTION) on LIQUID's five gates · registration rule "name the grading basis; a grade on an unnamed basis is NO-VERDICT" in `FORGE/PREDICTION_DISCIPLINE.md` § Registration · fleet sweep (vintage-check AND blind grade-read, non-owner, negative control) → DAEDALUS · packets LIQUID/RED/VIOLET/BOND/DAEDALUS. *(Pre-ruling row text → `git show cae911a7b:PROME/WILL_QUEUE.md`.)* | RULE | — | 9/2 | done | GATES diff blind-cold-read before commit (two-correction line) |
```

### WQ-159

```text
| 159 | **RULED 2026-09-02 21:55 ET (Will verbatim *"Approve 159 with your rec"*) = LET IT STAND, NO RETUNE.** T-03 = EPOP Δ vs a ROLLING 3-month referent ≤ −0.3pp; August's referent rolls to May 59.2 (LABOR's frozen card `docket/graded/GRADING_CARD_20260904_NFP.md`, `0fa661ba4`, item 4), so a FLAT 58.9 print Fri 9/4 08:30 FIRES T-03 and routes CARL + HENRY same day — a routing, not capital. The letter is frozen and the rolling referent is its registered design; a level-decline trigger, if wanted, is a NEW row graded from October, never a rewrite. EXECUTED: LABOR packeted `AGENTS/LABOR/inbox/2026-09-02_from-PROME_WQ-159-RULED-T-03-stands-no-retune.md` (carve-out ①); PROME re-pings LABOR after the 08:30 print (WQ-156 mechanics). *(Pre-ruling row text → `git show 038bc8211:PROME/WILL_QUEUE.md`.)* | RULE | — | 9/2 | done | ⛔ attribution bar unchanged: no desk carries a demand-vs-supply attribution from LABOR before NFP is graded |
```

### WQ-151

```text
| 151 | **CARL V2 downgrade leg — spec the word "sustained" BEFORE the August print, ON THE REGISTERED BASIS (matched-collection-month YoY, per OTTO's leg spec SIG-W-20260828-004 — NOT month-over-month).** Registered deep tier (EART 2022-2/2022-3/2023-1/2024-1) July print at EDGAR primary vs Jul-2025: **WORSE YoY on 4 of 4** (+1.31/+0.74/+1.47/+1.33pp) ⇒ with OTTO's 26/26, **30 of 30 matched-month deal-months worse YoY, zero improving, all three tiers — V2 HOLDS 4, no downgrade is near.** The real signal is deceleration of deterioration (broad gap +1.92→+1.63→+1.00pp; deep +2.29→+1.85→+1.21pp). ⚠️ CARL's first pass tonight graded MoM (3 of 4 fell) and read as an imminent 4→3 — self-corrected same session, AGAINST its own thesis; the basis is why this row exists. Owner also found it had graded the WRONG four Exeter deals since 8/27 (disjoint from the registered panel; both pulls clean) — corrected in STATUS `33d609f81`. WQ-107 table NOT registered (OTTO column absent + `collection_period` inferred as filing-month−1 breaks on Exeter's cadence) | RULE | — | 9/1 | **RULED 2026-09-03 07:41 ET (Will verbatim *"Approve WQ-151 with your rec and WQ-164 retire"*) = the registered letter read STRICTLY + ③(a) PERSISTENCE + CARL's reporting rule:** ① improving = per-deal matched-COLLECTION-month YoY delta ≤ 0.00pp in PERCENTAGE POINTS, deceleration satisfies nothing, NO materiality floor · ② sustained = 2 consecutive collection months · ③(a) the improving set INTERSECTS in ≥2 of 4 deep AND ≥2 of 3 broad across both months · ④ graded PER DEAL on a COUNT, tier mean DERIVATIVE · ⑤ matched on disclosed `collection_period`, verdict for month M waits for the later-filing tier (~M+2), issuer-stated 60+ definition, L4 unchanged · REPORTING RULE: every L1 grade cell publishes the per-deal pp deltas, the Δ(2026 level) vs Δ(2025 base) decomposition, and the double-matched control with its n. EXECUTED: CARL packeted (dark; encodes at its ≤9/10 sitting; first application = the ~9/15 August print), OTTO cc. *(pre-ruling rec + proposal text → `git show HEAD:PROME/WILL_QUEUE.md` row 151.)* | done
```

## Previous DOCKET L307 (verbatim)

```text
2026-09-15	OSPREY OWED30/32 paired scope/observability follow-up: precise reachable buyer-pullback proposal, source, counterexample and Channel2 overlap; compare proposed geography to existing letter. OWED15 existing downgrade work remains separate.	OSPREY (owner) / PROME (consumer)	PENDING	AGENTS/OSPREY/STATUS.md + PROME/proposals/2026-09-08_inbox-decisions-PROPOSAL.md	September8 inbox disposition; WQ196 owns the three original specification choices; WQ198 downgrade review. No letter/mark changed; source project not commissioned.
```

## Prior WQ-98 wording (verbatim)

```text
| 98 | **FFIEC hand-carry** (broker half DELIVERED 8/29: screenshot pair + activity view → FORGE reconciled by ANVIL, row 125) — **remaining: FFIEC** — ⚠️ **and the mirror is now STALE for two 9/2 transactions by Will's hand: WAL Dec-18 $70P ×1 @ $2.20 in ROBINHOOD (not the card's Fidelity IRA) · one USO Oct-16 $135C SOLD (price owed) — ANVIL reconciles both at the next export or on the fill price** — FORGE mirror 13d stale (TLT put marks off ~$100, TERRY-flagged); `inbox/WILL/` empty since 8/3 so TERRY's day-trade ledger is starved | BROKER | none — convenience | 8/27 | one export + drop captures whenever convenient; ANVIL reconcile spawns on arrival | D-10 rider class; FORGE header carries its own 8/14 vintage |
```

## Verification receipt

VERIFIED at generated local artifacts:

| Claim | Artifact | Verification | Observed result | Change |
|---|---|---|---|---|
| Immediate broker tasks distinguish authority from execution | Both generated pages, `#broker-actions` | Actual HTML inspection and behavioral test | Three tasks: QQQ disposition not approved; XLE/TLT85 approved, orders/fills UNKNOWN | Source-bound management records, independent fields, owner/review/completion evidence |
| Holdings are complete for the supported source formats | `FORGE/STATUS.md`; `desk_attention.holdings` | All-three-schema regression and generated coverage table | 21 recorded rows: 17 Fidelity, four unverified Robinhood; both KRE December lots preserved; TLT77/WAL September legs retained; USO spread distinct; sold call absent | Exact account/instrument/expiry mapping; anchored closure states preserve live rows whose notes mention earlier realized/closed events |
| Missing or stale coverage cannot masquerade as a verified mapping | `FORGE/position_management.tsv`; module/tests | Change source, remove evidence, duplicate key | Affected mapping withheld; holdings retained; visible errors; unrelated valid mapping preserved where possible | Source hashes, explicit unknown coverage; no ticker-only gate join |
| Receipt facts do not fabricate current cash | Linked September 9 USO receipt and `#confirmed-changes` | Receipt-table parser and rendered output | Net proceeds $1,754.30; scheduled settlement September 10; no newly settled cash/account total | Recent confirmed events discovered from links in FORGE and read from receipt fields |
| Already-ruled decisions stop being fresh asks | WILL_QUEUE and both pages | Queue parser plus original-row round-trip equality | WQ151/159/162/164/196–199 absent from open asks; original rows preserved verbatim above | Decision closure only; owner implementation/evaluation remains separate |
| OSPREY follow-through survives decision closure | DOCKET | Compare each physical line against pre-edit HEAD | Existing line identifiers unchanged; L307 resolved in place, two follow-through rows appended | September 15 objection disposition and October 6 feed evaluation remain PENDING; cadence sunset not invented |
| Work visibility includes overdue items | `#prome-work`; DOCKET | Synthetic overdue/terminal/distant/control-owner cases | Overdue retained; terminal, distant and unrelated owner rows excluded; physical line ID retained | PROME work list comes directly from docket, with source status and delivery caveats |
| Rebuilds and checks pass | Both HTML files; tools/tests | Nine new tests; 12 prior amendment regressions; four gate tests; queue parser 22/22; weekday claim check; `git diff --check` | PASS; actual HTML has no degraded notices and every new relative source link resolves locally | Test renders leave both change-feed and FleetOps baselines unchanged |

PLAN review: no blocker; required all three position schemas, full option/spread identity, account/date caveats and actual OSPREY ruling terms. Independent RESULT reviewed both actual pages and passed all nine new tests. It found one blocker: unlabeled completion conditions could imply USO-share/rates proposals had already been delivered. Fixed by explicitly rendering **Complete when:**; added assertions for both phrases, rebuilt both pages, and reran the nine tests successfully. No new market grade, threshold or trade authorization was inferred.

## Declared residue and publication

- Current supported holdings normalize correctly, but an unfamiliar future instrument label defaults to Stock. Future schema hardening should reject ambiguous labels rather than guessing. This was a non-blocking review flag for the inspected book.
- Whole-file evidence hashes deliberately invalidate multiple mappings after an unrelated change to FORGE or another linked source. Review the actual source before refreshing a hash; do not silence the warning mechanically.
- Broker actions with the same review date currently sort by the full review label; their order is not a scored urgency ranking. QQQ's explicit September 10 expiry remains visible.
- Historical source notes remain visible behind details with their dates; source receipt time does not establish the image's capture timestamp or account header. Robinhood is unverified. Positions without a validated management mapping remain explicitly unrecorded, not presumed unmanaged or approved for a new trade.
- DOCKET pending work may be delivered at its owner but unreconciled here. The page does not claim continuous owner monitoring, a fresh market-data sweep, or an overall fleet completion/regrade.
- Local builds are verified. Existing Claude-hosted tabs remain unrepublished; no compatible publisher is available in this session. Header navigation still points to those hosted tabs; use the direct local pages below for the corrected versions. Local relative evidence links require repository access.

[Local Helm](../artifacts/handbook.html) · [Local FleetOps](../artifacts/fleet_dashboard.html). Remaining broker records and commissioned USO-share/rates position work are the next operator/research priorities; publishing the existing hosted tabs remains an independent completion step.
