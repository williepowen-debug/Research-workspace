# HAWK — POST-DEADLINE PLAYBOOK (Apr 22–24)

**Created:** 2026-04-20 evening | **Trigger:** Apr 21 8pm ET ceasefire lapse without extension
**Pre-scenario:** D 75% / C 20% / B 5% | **Brent close Apr 20:** $95.42 [CONF TE]
**Use:** Execute Wed AM through Fri close without re-thinking strategy. Read BOTTOM LINE, then section matching current hour.

---

## 1. TRIGGER CONFIRMATION — Has D fired?

**Confirms D (any ONE is sufficient):**
- [ ] Brent closes **>$100** Apr 22 session (live price, not STATUS — defer to BRENT)
- [ ] New facility strike on named target: **Yanbu, ADCOP extension, Samref, Jubail, Mesaieed, Al Hosn, Ras Tanura, Abqaiq**
- [ ] Houthi Red Sea kinetic: tanker hit, anti-ship missile launch, or formal statement ending stand-down
- [ ] **US vessel hit** (navy or merchant) — instant D5
- [ ] Iranian naval asset struck by US — D4/D5
- [ ] Hormuz transit **= 0** for 24h+ (from 16/day baseline)
- [ ] Israel unilateral strike on Iran nuclear sites outside US framework — D3

**False positives (looks like D but ISN'T):**
- Gunboat warning fire on commercial ship without damage = still C territory (baseline since Apr 18)
- Brent intraday $100 spike that fades to <$98 close = market noise, not regime
- "Statement" from Iran without kinetic follow-through = Tier 4 fade (see DURABILITY SCORECARD)
- Single tanker rocketing off Oman without sinking = already priced
- US blockade enforcement action on Iranian-flagged vessel = continuation, not escalation

**Confirms NOT-D (upgrade toward B/C):**
- Trump or Vance tweets/announces extension with specific hour or day count (not "progress")
- Araghchi confirms Round 2 attendance + Round 2 produces joint communique with hour-count
- Brent retraces <$90 close and holds 48h

---

## 2. FIRST 24H ACTIONS — Wed Apr 22

### 2a. Probability reset (open-of-session)
Write to STATUS.md header:
- **If any trigger in §1 fires:** D 90% / C 8% / B 2% | Convergence 42–44/45
- **If deadline lapses silently (no extension, no new strike):** D 80% / C 18% / B 2% | Convergence 41/45
- **If extension announced:** D 35% / C 45% / B 20% | Convergence 34/45 → switch to CONTAINMENT playbook

### 2b. KB entries — paste-ready templates

```
KB-HAWK-NNN	2026-04-22	WAR	Deadline	Apr 21 8pm ET ceasefire expired without extension announcement; Trump silent / Trump confirmed lapse	[Source] Apr 21-22	B2	EMPIRICAL	CONFIRMED	2026-05-22		VX-HAWK-06,→ALL	Ends 14-day window; Phase 3 pathway opens
```
```
KB-HAWK-NNN	2026-04-22	WAR	Facility	[Facility] struck [time UTC] — [damage scope: train/berth/pipeline]; claimant [Iran/proxy/unclear]	[Source] Apr 22	B2	EMPIRICAL	ACTIVE	2026-05-22		VX-HAWK-04,→BRENT,→SAM	Phase 3 resumption; add to OIL_FACILITY_DAMAGE_TRACKER
```
```
KB-HAWK-NNN	2026-04-22	HORMUZ	Transit	Hormuz transit count [N] ships 24h window ending [time]; down from 16 baseline Apr 19	Lloyd's List/MarineTraffic Apr 22	B2	EMPIRICAL	ACTIVE	2026-04-29		VX-HAWK-01,→BRENT,→LIQUID	Physical closure confirmation tier
```
```
KB-HAWK-NNN	2026-04-22	DIPLOMATIC	Round2	Islamabad Round 2 outcome: [no-show / collapsed / deal / postponed]; Araghchi statement [quote]	[Source] Apr 22	B2	EMPIRICAL	CONFIRMED	null		VX-HAWK-06,→RED,→ALL	Resolves PREDICTIONS HAW-xx; diplomatic track exhaustion
```
```
KB-HAWK-NNN	2026-04-22	KINETIC	USNavy	[US vessel/asset] [engaged/struck] by [IRGC/Iranian asset] at [location] [time]; casualties [N]	DoD/USNI Apr 22	A2	EMPIRICAL	CONFIRMED	null		VX-HAWK-08,→ALL	D5 trigger; instant cross-agent red
```
```
KB-HAWK-NNN	2026-04-22	INSURANCE	WarRisk	Lloyd's JWC Gulf war-risk rate [%] of hull — up from [prior]; Hormuz transit premium [%]	Lloyd's List/Reuters Apr 22	B2	EMPIRICAL	ACTIVE	2026-04-29		VX-HAWK-07,→LIQUID,→BRENT	Insurance reinstatement moving opposite direction
```
```
KB-HAWK-NNN	2026-04-22	PROXY	Houthi	Houthi [statement/kinetic]: [detail]; Red Sea transit [N] ships	[Source] Apr 22	C3	EMPIRICAL	ACTIVE	2026-04-29		VX-HAWK-05,→BRENT,→LIQUID	Stand-down durability test
```
```
KB-HAWK-NNN	2026-04-22	ISRAEL	UnilateralStrike	Israeli action on [Natanz/Fordow/Isfahan] — [scope]; US [distance/support]	[Source] Apr 22	B2	EMPIRICAL	CONFIRMED	null		VX-HAWK-02,→ALL	D3 nuclear trigger; cross-agent instant
```

**Rule:** Every entry MUST have Source tag + Conf code. No naked claims. If source is aggregator (X, Telegram), use D3/D4; if named outlet (Reuters, Lloyd's List, DoD), B2.

### 2c. Watch items — Wed AM tape
Track continuously, log only on state change:
| Item | Threshold | Owner | Action |
|------|-----------|-------|--------|
| Hormuz transit | hits 0, or rebounds >25 | BRENT reads, HAWK logs | KB + VX-01 flip |
| Lloyd's JWC Gulf rate | >2% hull (from ~0.5% pre-war) | HAWK | KB + signal LIQUID |
| Brent (live) | crosses $100, $110, $130 | BRENT | Do NOT cite level; reference BRENT |
| Yanbu status | any report of kinetic | HAWK | KB + VX-04 → 5, cross-agent red |
| US Navy 5th Fleet | posture change, escort launched | HAWK | KB + VX-08 |
| Vance location | Islamabad arrival / early departure | HAWK | KB + resolves HAW-xx predictions |
| Tehran retaliation claim | any IRGC/MFA statement | HAWK | KB |

### 2d. STATUS.md update (single overwrite by end of Wed PM)
- Header line: War Day 53, Scenario D XX%, Convergence Y/45
- Replace §"T-MINUS" section with §"POST-DEADLINE HOURS 1-24"
- Update CEASEFIRE DURABILITY SCORECARD: add Apr 21 8pm row (Tier 1 kinetic confirmation or Tier 2 silent lapse)
- Bump Exit Protocol to 0/7 explicit (strip "DEGRADING" hedge on row 1)
- New BOTTOM LINE (3-4 sentences): what fired, what's next gate, Thu/Fri priorities

---

## 3. 48–72H DECISION GATES — Wed PM through Fri close

| # | Gate (observation) | Action if YES | Action if NO by Thu 4pm ET |
|---|--------------------|---------------|-----------------------------|
| G1 | Yanbu struck (drone/missile/fire reported) | D5 confirmation; Brent $140–180 framing; KB + VX-04→5; red-signal ALL; update FOUR_BREAKS framework | C-containment remains possible; hold D 80% |
| G2 | US Navy asset engages or is engaged by IRGC | D4/D5; instant red ALL; STATUS convergence 43–45/45; consider RED re-engagement on thesis-kill path failure | D remains 80%; watch overnight |
| G3 | IAEA expelled from Iran / Fordow access cut | Nuclear escalation path; D3 weight up; signal RED + SAM (Israel strike convexity) | Nuclear path dormant |
| G4 | Israel unilateral strike on Natanz/Fordow | D3 confirmed outside US framework; instant red ALL; SAM oil-pass-through + HENRY vol spike | Israel-restraint track intact; no action |
| G5 | Tehran retaliates for Apr 19 ship seizure (kinetic) | Cascade accelerator; KB + signal ALL; watch G2 next 12h | Retaliation latent — stays loaded for Fri window |
| G6 | Hormuz transit collapses to 0 (24h window) | Physical closure; D5 baseline; BRENT $130+ framing; signal ALL red | If 10–16 range: still closed-in-practice; monitor |
| G7 | Houthi resumes Red Sea kinetic | Proxy activation confirmed; second-chokepoint risk; BRENT + LIQUID red; CARL on gas pass-through | Stand-down holding; contain |
| G8 | Trump/Vance announces extension Wed AM | Thesis-kill partial; scenario reset B 30% / C 45% / D 25%; update EXIT_PROTOCOL row 1; alert RED | Lapse confirmed |
| G9 | Round 2 no-show or collapse (Iran absent, or talks <6h with no joint statement) | D-anchor confirmed; resolves HAW-xx predictions; KB + signal ALL | If Iran attends and talks extend >12h: C-upgrade candidate |
| G10 | Brent closes <$90 (48h sustained) | Thesis-kill candidate; check G1–G9 for false-positive; ping RED; lower D to 50% | Thesis intact |

**Decision order Wed AM:** G8 (extension?) → G2 (US-Iran kinetic overnight?) → G9 (Round 2 outcome) → G1 (Yanbu?) → G5/G6 (retaliation/transit).

---

## 4. CROSS-AGENT PRE-REGISTERED SIGNALS

Write each to STATUS.md "Cross-Agent Transmission" table and/or `outbox/` per CLAUDE.md protocol. Write ONCE per event; WALTER routes.

| Gate fires | → Agent | One-line signal |
|------------|---------|-----------------|
| §1 trigger confirmed | ALL | "Scenario D confirmed Apr 22 [HH:MM ET]; ceasefire lapsed + [trigger]; convergence [N]/45" |
| G1 Yanbu | BRENT | "Yanbu strike confirmed; Scenario D5; frame Brent $140–180 tail, defer to BRENT for exact" |
| G1 Yanbu | SAM | "Saudi last-route threatened; Dubai crude co-move; JPY safe-haven bid window open" |
| G1 Yanbu | CARL | "Gas pump pressure extends to late May; demand destruction thesis ($64) dead" |
| G2 US-Iran kinetic | HENRY | "Direct US-Iran engagement — VIX catalyst live; HENRY owns level (watch 28 → 35 → 45)" |
| G2 US-Iran kinetic | LIQUID | "Flight-to-safety event; HY OAS widening; HAWK frames thresholds 420/500/600, LIQUID owns spread" |
| G3 IAEA expelled | RED | "Nuclear inspection framework severed; thesis-kill exit row 1 now blocked for months; reassess" |
| G4 Israel strike | ALL | "Israel unilateral — outside US framework; D3 confirmed; defer oil levels BRENT, vol HENRY" |
| G5 Tehran retaliation | ALL | "Tehran kinetic retaliation Apr 22; cascade pathway live; next-step US counter-strike risk 12–24h" |
| G6 Hormuz 0 | BRENT, LIQUID, CARL | "Hormuz physical closure confirmed (0 transit 24h); Phase 5 baseline; tanker/insurance collapse" |
| G7 Houthi | BRENT, LIQUID | "Red Sea stand-down broken; second chokepoint; shipping re-routing + insurance re-spike" |
| G8 Extension | ALL | "Extension announced [time]; scenario reset D 25%/C 45%/B 30%; thesis-kill path partially open" |
| G9 Round 2 fail | RED | "Diplomatic track exhausted; thesis-kill exit row 1 off-table for this cycle; stress-test containment" |
| G10 Brent <$90 48h | RED, BRENT | "Oil retrace inconsistent with D; reassess D probability downward; check false-positive filters" |

**Pre-framed levels (HAWK frames the catalyst; other agents own the number):**
- Brent: **$110 / $130 / $150** (HAWK frames as C/D4/D5 anchors; BRENT owns live level)
- VIX: **28 / 35 / 45** (HAWK flags catalyst; HENRY owns VIX)
- HY OAS: **420 / 500 / 600 bps** (HAWK flags risk-off trigger; LIQUID owns spread)
- USDJPY: **155 / 150 / 145** (yen strengthening on risk-off; SAM owns level)

Context for framing (from BOARD signals):
- **MS/Piper counter (SIG-021):** 2026 real economy insulated vs 1990/91 (consumer 1.8% vs 3% gasoline share, margins +15% vs -4%, US net exporter, liquid credit, fiscal impulse). HAWK acknowledges — oil-to-recession transmission dampened, but facility-damage duration channel and financial-conditions channel still active. Don't let MS frame underweight the infrastructure channel.
- **Netherlands LCP-O Phase 1 (SIG-029):** First formal national oil crisis framework activation; follows IEA 400M bbl release Mar 11 + France SAGESS draw. State-response envelope widening; watch Germany/Italy/Japan for Phase 1 equivalents Wed–Fri.
- **Tuapse 3rd-theater (SIG-001):** Hydrocarbon attack now spans Persian Gulf + Red Sea/Qatar + Black Sea/Russia. If Apr 22 adds a 4th theater hit (Ras Tanura, Yanbu, Kharg direct), the multi-theater premium becomes structural.
- **Qatar LNG >90% crash (SIG-030):** Verified. Ras Laffan 3–5yr repair baseline holds regardless of Apr 21 outcome — price floor on LNG-to-oil substitution.

---

## 5. WHAT HAWK DOES NOT DO

- Do NOT chase Telegram/X headlines before KB-logging with Source + Conf code
- Do NOT cite Brent, VIX, HY OAS, or USDJPY levels in STATUS — reference the owning agent's tag
- Do NOT update FLOW/VX unless state genuinely changed (G gate fired, threshold crossed)
- Do NOT edit BRENT, HENRY, LIQUID, SAM, RED STATUS files — outbox signals only
- Do NOT send duplicate cross-agent signals — write once to STATUS + one outbox file; WALTER delivers
- Do NOT predict political intent ("Trump will…") — track positioning and kinetic only
- Do NOT re-open oil fundamentals file (OIL_FACILITY_DAMAGE_TRACKER) unless a new facility struck
- Do NOT overwrite CEASEFIRE DURABILITY SCORECARD rows — append only
- Do NOT assume MS counter-frame (SIG-021) kills thesis — it softens consumer/credit channel, not infrastructure
- Do NOT commit outside `AGENTS/HAWK/` — flag shared-file edits to Prome

---

## 6. FALSIFICATION GATES — What kills D thesis

Any ONE of these → move to CONTAINMENT playbook (thesis partial kill):
- **Extension announced with credibility:** Trump/Vance statement + diplomatic follow-through (Vance in Islamabad >24h, joint statement, specific next-meeting date) — soft-kill D, upgrade B to 30–40%
- **Kinetic event isolated + de-escalated within 48h without facility strike:** e.g. gunboat incident stops, no Yanbu, no US vessel — D→C downgrade, -15pp D
- **Brent retraces <$90 sustained 48h+:** market disagrees with D framing — check false-positive filters in §1; if clean, drop D to 50%
- **Hormuz transit recovers >25 ships/day sustained 48h:** physical de-escalation — C→B pathway opens
- **Iran ceasefire re-signed with observable mechanics** (UN/IAEA observers, mine clearance announced, insurance rates fall) — full thesis kill toward A; initiate EXIT_PROTOCOL §Scenario A steps

**None of the above → D holds. Do not exit overlay on headline-only events (Tier 3/4 per DURABILITY SCORECARD).**

---

## 7. HANDOFF PROTOCOL — If HAWK session ends before Fri close

Write the handoff to `AGENTS/HAWK/SCRATCH.md` at closeout (LAST_COMPLETION.md was retired 2026-06-26; SCRATCH is the canonical session handoff — see CLAUDE.md SPAWN PROTOCOL step 13). Use this state block:

```
## HAWK Handoff — [Date] [Time ET]
### State
- War Day: [N] | Scenario: D X% / C Y% / B Z% | Convergence: [N]/45
- Brent: defer to BRENT (last seen in STATUS: $X Apr YY)
- Hormuz transit: [N] ships
### Gates fired this session
- G[N]: [observation] → [action taken] → [KB-HAWK-NNN logged]
### Gates still open
- G[N]: [what to watch, threshold, decision]
### Cross-agent signals sent
- [Agent]: [filename in outbox/]
### Next session must do
1. Resolve PREDICTIONS.tsv entries whose Timeframe has passed
2. Check inbox/ for replies from [agents]
3. Read §[N] of POST_DEADLINE_PLAYBOOK.md for current hour context
4. Verify Brent/VIX/HY OAS against live sources, not STATUS
### Pending
- [Anything blocked, waiting on Prome/Will/other agent]
```

**Git:** Follow CLAUDE.md protocol — `git add AGENTS/HAWK/` only, commit before push, never resolve other agents' files.

---

## BOTTOM LINE

If Apr 21 8pm ET lapses without extension, execute §2 actions Wed AM (probability reset, KB templates, STATUS update), then work §3 gates in order G8→G2→G9→G1→G5/G6 through Thu. Every gate has a pre-registered cross-agent signal in §4. HAWK frames the catalyst; BRENT/HENRY/LIQUID/SAM own their numbers. Thesis kill requires observable mechanics, not headlines — trust the DURABILITY SCORECARD pattern (only Tier 1–2 kinetic events hold). If session ends, §7 handoff is non-negotiable.
