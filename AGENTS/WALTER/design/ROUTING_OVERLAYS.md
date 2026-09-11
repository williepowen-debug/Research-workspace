# WALTER Routing Overlays v0.33

**Read this file WHOLE at boot immediately after `ROUTING_TABLE.md`.** This is the second part of that spec, not optional background. The parent owns domain defaults; this file owns the following type/tag, boundary, convergence, safety-net, escalation and MINIMIZE rules. Both apply at dispatch; `ROUTING_CARVEOUTS.md` remains the per-agent dispatch consult.

Split 2026-09-08: the complete contiguous suffix beginning "By Signal Type" was moved verbatim. Historical examples retain their dates; superseded pre-v0.8 conventions do not override current FORMAT/CHECKLIST rules. Measure after append and at each Tier-2; next calendar check 2026-09-30. Reapply the fleet rotation tiers if needed. The split preserves total rule-reading cost; see `../research/2026-09-08_boot-maintenance/rotation-receipt.json` for measured bytes and obligation conservation.

## By Signal Type

| Signal Type | Default Precedence | Upgrade Condition |
|-------------|-------------------|-------------------|
| `threshold-crossed` | IMMEDIATE | → FLASH if position directly affected |
| `pattern-match` | PRIORITY | → IMMEDIATE if convergence (2+ agents flagging same theme) |
| `thesis-frame` | PRIORITY | Stays PRIORITY. Can upgrade to IMMEDIATE only if the synthesis/framework directly changes position sizing or catalyst read (rare — most thesis-frame content is analytical context, not threshold breach). |
| `catalyst` | IMMEDIATE | → FLASH if pre-written framework exists and threshold met |
| `divergence` | IMMEDIATE | Always IMMEDIATE minimum |
| `research` | PRIORITY | Stays PRIORITY unless thesis-critical finding |
| `position-risk` | IMMEDIATE | → FLASH if stop-loss or margin proximity |
| `context` | ROUTINE | Stays ROUTINE unless safety net triggers |
| `manual-flag` | PRIORITY | Follows Will's specified urgency if given |

---

## By Tag/By Verdict (NEW v0.7)

Augments the By Signal Domain and By Signal Type tables. Applies AFTER domain + signal_type routing has been determined. Adds RED to the info line when specific tag/verdict conditions fire — adversarial overlay needs visibility into bifurcation-state and corrected-framing dispatches without requiring separate signals. Falsification-trigger rule additionally turns WALTER into an auto-dispatcher when pre-registered RED thresholds cross.

| Tag/Verdict | Rule | De-dupe behavior |
|-------------|------|------------------|
| `signal_role: cluster_mediating` (v0.8 canonical) OR legacy `cluster_mediating: true` boolean | Add **RED** to info line unconditionally regardless of domain. **v0.19: also add NEXUS to info** — FORMAT_SPEC v0.8 gives NEXUS **authoritative-voice precedence on this exact tag** (*NEXUS > WALTER (tagger) > action-primary*) and says **NEXUS owns cluster-narrative-update interpretation**. Until v0.19 the tag routed to RED but **not to the agent that owns it** — NEXUS could be out-voiced on a call the spec assigns it, on a signal it never received. | If RED/NEXUS already in to/info, no add; stays at one occurrence |
| **v0.19 — signal bears on a registered NEXUS prediction** (`PRED-NN` in `AGENTS/NEXUS/PREDICTIONS_MONITOR.md`): the signal **resolves / partially resolves / materially counter-evidences** a row, OR the row's named resolution route points at this signal's subject | **NEXUS = ACTION** (not info). A registered prediction moving off its mark is an **owner re-mark**, which is action by definition | If NEXUS already action, no change; if already info, **promote to action** |
| `verify_research_verdict: CORRECTED-FRAMING` (in dispatch_note) | Add RED to info line | If RED already in to/info, no add; stays at one occurrence |
| `falsification_trigger: <RED-FT-NN>` (auto-fired by WALTER from `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` per JOINT_PROPOSAL §2 eval logic) | Action = trigger.recipient_chain.action; Info = trigger.recipient_chain.info; precedence per trigger.action enum mapping (IMMEDIATE-FALSIFY/PATH-B-CONFIRM/ADD-POSITION/etc.) | n/a — auto-generated signal, recipient chain pre-determined per FALSIFICATION_TRIGGERS row |

**De-dupe rule (general):** when multiple v0.7 rules fire on the same dispatch (e.g., signal is both `cluster_mediating: true` AND CORRECTED-FRAMING), RED is added once. Composition is informative-only; consumption mode (full-read for cluster_mediating vs body-skim for CORRECTED-FRAMING per RED CLAUDE.md boot-step 1.5 b3/b4) is RED's choice at boot.

### Interim period (pre-v0.8)

`cluster_mediating: true` is a v0.8 field (pending Will sign-off on JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2a). Until v0.8 lands, the prose-tagged equivalent is dispatch_note language carrying "paper-vs-structural" / "tape-vs-substance" / "bifurcation" / "divergence" tokens. Interim WALTER discipline:

> When dispatch_note contains paper-vs-structural / tape-vs-substance / bifurcation / divergence framing, ensure RED in info line.

This carries the v0.7 rule operationally before the field formally exists. RED's bifurcation classification TSV (LIAISON Turn 5 deliverable, `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv`) seeds the historical pass; new prose-tagged signals from this point forward apply the rule.

### Composition example

SIG-W-20260505-012 (Brent intraday tape divergence vs Iran cluster confluence) — cluster_mediating + (would have been) CORRECTED-FRAMING if verdict run. Under v0.7 rules: RED auto-cc once; dispatch_note flags both rule-fires explicitly so RED knows the routing rationale; consumption mode = full-read (cluster_mediating dominates over body-skim).

### Why this is here, not in FORMAT_SPEC

`cluster_mediating` is a FORMAT_SPEC field; CORRECTED-FRAMING is a CHECKLIST verdict; falsification_trigger is a generated body field. The recipient-augmentation behavior is a routing decision — it belongs in this table per the canonical-source lookup in `WALTER/CLAUDE.md` ("Domain → recipient routing rules" → ROUTING_TABLE owns).

---

## By Boundary Threshold (NEW v0.8)

Augments the By Signal Domain table with explicit threshold-cross dispatch rows for BRENT's 8-row IMMEDIATE list per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2c (BRENT+CARL+WALTER 3-way cosigned 2026-05-05/06; Will sign-off 2026-05-08). Threshold-cross signals carry `signal_type: threshold-crossed` + boundary-row reference in dispatch_note (e.g., `boundary: §2c-row-1`).

Distinct from the boundary-trigger CARL-side rule under "Iran-cluster CARL-info override" (Brent ≤$95×5sess and ≥$115×5sess fire IMMEDIATE → CARL): THIS section codifies the BRENT-action 8-row list at finer thresholds with broader cross-recipient routing.

| # | Threshold | Precedence | Action → Info | Cadence |
|---|-----------|------------|---------------|---------|
| 1 | **Brent close ≥ $120 sustained 3 sessions** | IMMEDIATE | BRENT → CARL, HENRY, LIQUID, SAM, HAWK, RED | 2-3 sess sustained = dispatch |
| 2 | **Brent close ≤ $75 sustained 3 sessions** | IMMEDIATE | BRENT → CARL, HENRY, LIQUID, RED | 2-3 sess sustained = dispatch |
| 3 | **Cushing < 20M bbl single print** | IMMEDIATE | BRENT → LIQUID, HENRY, RED | Single print = dispatch (operational minimum, WTI dislocation risk) |
| 4 | **HY Energy OAS > 400bps** | IMMEDIATE | BRENT → LIQUID-cross-feed (LIQUID may want primary depending on broader-credit context — flag at dispatch) | 2-3 sess sustained = dispatch |
| 5 | **VLCC Worldscale ≥ 2× trailing 30-day median sustained** | PRIORITY | BRENT → HAWK, SAM, RED | Sustained-cross-from-baseline (≥3 sess) — operational definition avoids absolute-threshold drift in war-risk-elevated baseline |
| 6 | **Gasoline crack — re-cross from <$30 back ≥$30 OR single-day spike ≥$50** | IMMEDIATE | BRENT → CARL, HENRY, RED | Threshold-cross logic only; standing $42 baseline = no fresh dispatch. Inverse extremum captures demand-destruction-via-crack-collapse OR refinery-substitution-exhausted scenarios |
| 7 | **US oil rigs +50 from 408 trough** | PRIORITY | BRENT → CARL (capex/wage), HENRY, RED | 2-3 sess sustained = dispatch |
| 8 | **Brent 3:2:1 crack > $50/bbl** | IMMEDIATE | BRENT → CARL (refining-margin pass-through), HENRY, REGINALD (refinery-bank) | 2-3 sess sustained = dispatch |

### Cadence convention (locked)

- **Single-day breach** = watch (no dispatch)
- **2-3 sessions sustained** = dispatch
- **Single-print operational minima** (#3 Cushing): dispatch on the print itself
- **Re-fire convention:** after initial cross, no re-fire on continued state; only on re-cross of boundary in either direction. Sustained-above-#1 stays one signal until it falls back below or escalates further to a higher threshold.

### Detection responsibility

- **WALTER:** monitors price/spread/inventory data via FORGE/tools/market-data + EIA/Baker Hughes scheduled scans (per JOINT_PROPOSAL §2b — Phase 2 dependency, calendars not yet landed at v0.8 ship)
- **BRENT:** mirrors via own data tools and STATUS refresh (BRENT self-task: PREDICTIONS.tsv BRT-04/BRT-08/BRT-15 cross-refs to these row numbers)
- **Convention:** BRENT-fire-as-primary on threshold-cross dispatches; WALTER-fire-as-fallback if BRENT stale (>5d STATUS lag)

### Composition with other rules

- v0.7 By Tag/By Verdict still applies — a threshold-crossed signal with `signal_role: cluster_mediating` AND CORRECTED-FRAMING verdict still de-dupe-collapses RED to one occurrence.
- Safety Net Auto-Upgrades below still apply — VIX>30 or HY OAS +25bps single session can override boundary-threshold precedence to FLASH.

### Q-trail

BRENT LIAISON Q4 (BRENT→WALTER, Turn 1, 8-row list proposed) → WALTER Turn 2 ACCEPT-WITH-REDLINES (#5 PRIORITY-not-IMMEDIATE; #6 standing-state-not-fresh-dispatch) → BRENT Turn 3 ACCEPT (with #5 ≥2× median definition + #6 dual-extremum >$50 inverse trigger) → WALTER Turn 4 LOCK → Will sign-off 2026-05-08.

---

## By Convergence (NEW v0.9)

Augments By Signal Domain + By Signal Type + By Tag/By Verdict + By Boundary Threshold sections. Applies AT DISPATCH after all other routing decisions. **Trigger:** when BOARD INDEX scan (cluster sections preferred for speed) finds N≥2 prior signals within 5-session window referencing the same bank ticker OR the same multi-channel exposure pattern, auto-fire `signal_type: convergence_event` precedence IMMEDIATE override.

### Rule

| Detection condition | Action | Recipient chain |
|---------------------|--------|-----------------|
| N≥2 prior BOARD signals within 5-session window mention same bank ticker (from `design/CROSS_REFS/REGINALD.md` §1 watchlist: TIER-1 / TIER-2 / NEW-TRACKING / EXTERNAL-WATCH tiers) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | **REGINALD action** + originating-channel agents info + **RED info** |
| N≥2 prior BOARD signals within 5-session window touch same cross-bank pattern key (from `design/CROSS_REFS/REGINALD.md` §5: `cohort_fade_pattern` / `fhlb_bifurcation` / `provisions_mask_deterioration` / `office_single_point_concentration` / `hidden_cre_relabeling_trajectory` / `mi3_rcon2746_screen` / `ndfi_breakout_decomposition`) | Auto-fire `signal_type: convergence_event` + override precedence to IMMEDIATE | **REGINALD action** + originating-channel agents info + **RED info** (cohort-level convergence is RED-watchable as a structural-bifurcation candidate) |

### Detection mechanics

- **At dispatch:** scan BOARD INDEX cluster sections (filtered to BANK_COLLATERAL + PC_STRESS + FED_FRAMEWORK + CONSUMER_STAGFLATION primary; expand secondary on bank-ticker hit) for prior 5-session window
- **Lookup:** use CROSS_REFS/REGINALD.md §1 ticker → watchlist row mapping + §5 pattern key list (denormalized cache, grep-speed at dispatch)
- **Cost:** cluster-filtered grep ~50-200ms per dispatch
- **Volume estimate:** ~1-2 convergence_events per week at current dispatch volume; peaks during Q1 earnings windows + threshold-cross windows

### dispatch_note format

When convergence_event fires, include in dispatch_note:

- **Prior signals (count + IDs + cluster + date):** e.g., `Convergence: SIG-W-20260420-008 (BANK_COLLATERAL, 4/20) + SIG-W-20260424-005 (BANK_COLLATERAL, 4/24) + SIG-W-20260426-009 (BANK_COLLATERAL, 4/26) — 3 signals in 6 sessions on office-distress + WAL/MTB ticker overlap`
- **Convergence type:** ticker-convergence vs pattern-key-convergence (or both)
- **Channel codes touched** (from REGINALD's 8-channel framework): e.g., `Channels: cre,hidden_cre,cmbs_maturity`
- **Cluster-mediating tag:** if convergence spans multiple clusters, set `cluster_mediating: true` + tag `cluster_secondary` per FORMAT_SPEC v0.7+

### De-dupe behavior

- If `cluster_mediating: true` already fires on the trigger signal (per v0.7 By Tag/By Verdict), convergence_event composition adds RED **once** (no double-count of RED-info)
- If multiple convergence_event triggers fire on same dispatch (e.g., signal hits both ticker-convergence AND pattern-key-convergence), single convergence_event dispatched with both reasons listed in dispatch_note
- If incoming signal IS the 2nd-or-later signal that COMPLETES a convergence window, dispatch fires from incoming-signal-dispatch side; prior signals stay at their original precedence (not retroactively re-dispatched)

### Composition with other rules

- v0.7 By Tag/By Verdict still applies — convergence_event signal with `signal_role: cluster_mediating` + CORRECTED-FRAMING verdict still de-dupe-collapses RED to one occurrence
- v0.8 By Boundary Threshold still applies — if convergence_event also crosses a BRENT-IMMEDIATE row (e.g., Brent ≥$120 sustained 3 sessions), BRENT row recipient chain composes with REGINALD primary; precedence stays IMMEDIATE (highest)
- Safety Net Auto-Upgrades still apply — VIX>30 or HY OAS +25bps single session can compose with convergence_event (precedence already IMMEDIATE; multi-trigger composition surfaces in dispatch_note)

### Examples (illustrative — not historical dispatch)

**Ticker convergence example:** signal SIG-W-20260512-NNN mentions WAL. WALTER greps BOARD INDEX for prior 5-session window — finds SIG-W-20260507-004 (Sternlicht-Starwood CMBS) mentions WAL + SIG-W-20260508-011 (FWRD covenant default) mentions WAL bank-covenant pattern. N=3 within 5 sessions → convergence_event fires; recipient chain REGINALD action / BRENT info / RED info. dispatch_note: `Convergence (ticker): SIG-W-20260507-004 + SIG-W-20260508-011 + (current) — 3 signals in 5 sessions on WAL; channels: cre,cmbs_maturity,private_credit`.

**Pattern-key convergence example:** signals across 4 sessions all touch `cohort_fade_pattern` (REGINALD's structural framework) — VLY provisions tell + CFG cohort-fade signal + WAL ex-fraud NCO read. Even though no single ticker repeats N≥2, pattern-key fires same convergence_event mechanics. RED-info important here because cohort-level convergence is bifurcation candidate.

### Q-trail

REGINALD LIAISON Q5 (REGINALD → WALTER, Turn 1, framework proposed) → WALTER Turn 2 DECISION (YES, build atop named-entity grep from Q3) → REGINALD Turn 3 LOCK (preference: ROUTING_TABLE v0.9 section, not standalone) → WALTER Turn 4 SHIP (this section).

---

## Safety Net Auto-Upgrades

These conditions override the routing table and force minimum IMMEDIATE precedence:

| Trigger | Detection Method | Upgrade To |
|---------|-----------------|------------|
| VIX > 30 (or +5 intraday) | Market data check | IMMEDIATE minimum |
| HY OAS widening > 25bps single session | Market data check | IMMEDIATE minimum |
| Held-position liquidity drop | Bid-ask spread monitoring | FLASH |
| 2+ agents flag same theme in 24h | Signal correlation | IMMEDIATE + flag convergence |
| Correlation break (r drops >0.3 in correlated pair) | Statistical check | IMMEDIATE minimum |

---

## Escalation Paths

Receiving agents can request WALTER re-route at higher precedence:

| Scenario | Agent Action | WALTER Response |
|----------|-------------|-----------------|
| Agent finds signal more urgent than classified | Writes to WALTER outbox: "ESCALATE SIG-W-YYYYMMDD-NNN to IMMEDIATE" | WALTER re-routes to broader group at higher precedence |
| Agent identifies cross-domain relevance | Writes to WALTER outbox: "ROUTE SIG-W-YYYYMMDD-NNN to AGENT (ACTION)" | WALTER sends copy to new recipient |
| Agent flags false positive | Writes to WALTER outbox: "REJECT SIG-W-YYYYMMDD-NNN — reason" | WALTER logs rejection, stops further routing |

---

## MINIMIZE Routing Adjustments

During MINIMIZE, routing table precedence thresholds shift:

| MINIMIZE Level | ROUTINE Signals | PRIORITY Signals | IMMEDIATE Signals | FLASH Signals |
|---------------|-----------------|------------------|-------------------|---------------|
| **Normal** | Route normally | Route normally | Route normally | Route normally |
| **MINIMIZE-1** | Queue in WALTER | Route normally | Route normally | Route normally |
| **MINIMIZE-2** | Queue in WALTER | Queue in WALTER | Route normally | Route normally |
| **MINIMIZE-3** | Queue in WALTER | Queue in WALTER | Queue in WALTER | Route normally |

---
