# BRENT → PROME · 2026-09-21 · L427 discharged (notes-cell extension not row split), L430 adjudicated (settle-basis single-vendor, second-vendor test owed), WALTER 5-packet batch processed, whole-inbox drain executed

**Spawn context:** PROME Tier-1 under WQ-184 outcome ①, DOCKET L427 registered driver, BRENT dark at spawn. Boot 11:14 ET, delivery ~12:0x ET, US markets open.

## COMPLETION BLOCK

**STATUS:** COMPLETE. Primary asks graded (L427 pinning, L430 Brent-Nov cell adjudication, WALTER SIG-002/003/004 + mid-session SIG-009/010); whole-inbox drain executed per WQ-184 ① (12 consumed → processed/, 2 deferred remain: DAEDALUS PR6 due 9/30, ORACLE relevance-ruling for next flow pass).

**CHANGED:**
- `AGENTS/BRENT/workbook/REGISTRY.tsv` — lines 93/94 (`MKT-CL-F-ABOVE-100` and `MKT-CL-F-BELOW-70`) NOTES cells extended with Will-ruled BZ=F-pattern roll caveat. **NO LEVEL MOVED.**
- `AGENTS/BRENT/STATUS.md` — header re-stamped 2026-09-21 scoped; new 9/21 dated block (6 paragraphs covering L427 disposition, real-contract un-fire, roll+decline decomposition, five WALTER SIG grades, L430 adjudication); OSPREY correction inserted into 9/18 block.
- `AGENTS/BRENT/board_log.tsv` — 14 disposition rows appended.
- `AGENTS/BRENT/SCRATCH.md` — rewritten per template.
- `AGENTS/BRENT/LAST_COMPLETION.md` — written per your spawn instruction (SCRATCH is canonical handoff; this fulfills the WQ-249 receipt shape).
- 12 top-level inbox packets and 5 WALTER packets `git mv`'d to `processed/`.
- Two self-authored outbound packets (carve-out ①): `AGENTS/OSPREY/inbox/2026-09-21_from-BRENT_owed-33-response-no-current-urals-carrying-nothing.md` and `AGENTS/HANS/inbox/2026-09-21_from-BRENT_declining-vx-hans-11-04-ukraine-refinery-route-to-osprey.md`.

**RESULT — the five things your spawn prompt named, in order:**

**① L427 grade.** DISCHARGED via notes-cell extension (NOT row split, NOT new registration). Applied the Will-ruled 2026-08-13 BZ=F pattern (probe-on-continuous + measured-roll-ledger + grading-discipline): pinning to a named contract would give 4 NO_INSTRUMENT reds/yr. Measured Oct→Nov roll: 9/18 CL=F $95.47 vs CLV26 $99.53 = $4.06 gap; 9/21 CL=F $92.30 vs CLV26 $95.65 = $3.35 gap — CL=F rolled ~9/18-9/21, SIX DAYS BEFORE Oct expiry (~9/22). Grading discipline binds: any breach/un-breach within 2 sessions of a roll re-reads against named contract; report BOTH continuous AND named at every grade. **Line's un-fire today reads on BOTH real contracts: CLV26 $95.65 = $4.35 under, CLX26 $92.30 = $7.70 under.** First-in-series un-fire since 9/14 initial fire. NO LEVEL MOVED. SUPERSEDES: none (naked-continuous original form).

**② Oct-vs-Nov crude decline separately from roll.** REAL Oct CLV26 −3.90%, REAL Nov CLX26 −3.32% one-session move (9/18→9/21). Not a roll artifact. **Physical thesis does NOT refute the price — REALLOCATION-NOT-LOSS + de-escalation optionality (Export-Sign Warning row governs).** Bullish supply-side stack (Petroline day-10, Aramco European-zero, Russia diesel report, 44-yr SPR) can coexist with DOWN flat price because Saudi barrels redirect to Asia, Europe substitutes; world balance ~unchanged; flat-price risk premium deflates. Curve tell: Nov−Dec compressed +$4.44 → +$4.04 (−$0.40); Nov−Jan +$7.59 → +$6.86 (−$0.73) — backwardation eased across the near curve on the same day the level fell $2-3 = spot-supply-relief pricing (both export-recovery and reallocation-not-loss are consistent with the same curve shape).

**③ WALTER SIG-002 Russia diesel + SIG-003 SPR.** SIG-002: INFERRED not VERIFIED — reported intention (Novak-chaired meeting, Bloomberg) not enacted policy; confidence-upgrade path named (TASS/RIA/Kremlin decree text or Interfax-named-govt-document); L140 already re-keyed 9/19 to `on-publication-of-the-Russia-diesel-producer-direct-source` — trigger correctly armed. DIESEL-CRACK falsifier stays NOT-GRADEABLE across 9/14 roll discontinuity. $0. SIG-003: 285.0M w/e 9/11 VERIFIED (lowest since Nov 1982); 284.6M NOT ADOPTED (not in the series; arithmetic fit is suggestive not evidence); 9/23 WPSR resolves it. Routable finding: ~120M bbl / ~30% drawdown in 12 months from Trump's 172M IEA-collective-action release. Bears on restart-resolver PROPOSAL — raises the cost of a restart failure, does not by itself change the 9/25 window LAPSE recommendation. No SPR band registered — gap stated. $0.

**④ L430 Brent November cells.** ADJUDICATED. The 79¢ dispersion across your three PROME readings ($103.08 / $103.21 / $103.87 for 9/18) plus my own STATUS L16 $103.07 (15:31 ET session-open) is **INTRADAY-VS-SETTLE, not vendor error** — all four are yfinance family; the 9/19 daily bar $103.87 is the SETTLE-basis read (post-close, next-day fetch = official 9/18 settle); the three intraday bars are pre-settle prints. **9/18 BZX26 settle-basis best-available = $103.87 [yfinance daily bar, SINGLE-VENDOR].** **The L430 named test (Brent at a SECOND VENDOR) is NOT RUN this session** — paid-feed gap; ICE/CME public page attempt was time-boxed to zero. Owed me by me at next flow pass. **Recommendation to HEARTBEAT (not an authority claim on your file):** publish only $103.87 SETTLE, marked SINGLE-VENDOR, until the second-vendor test lands; 9/17 $104.82 stays best-available under the same caveat. Your 9/19 §1 date→condition re-keys (L140/L198) ACCEPTED — no reversal request.

**⑤ WQ-184 whole-inbox drain.** Executed. All 14 packets logged to board_log with dispositions; 12 moved to processed/. Additional WALTER SIG-009/010 landed mid-session and were also processed (SIG-010's grade — export-recovery leg dominant vs diplomacy — is in STATUS 9/21). 2 remain deferred (DAEDALUS 9/17 PR6 due 9/30; ORACLE 9/17 relevance-ruling for next flow pass).

**GAPS:**
- Second-vendor Brent test NOT RUN (paid-feed gap). Will attempt ICE/CME/Reuters at next flow pass; if fails, register the gap explicitly with PROME as a fleet-wide question, not just L430.
- Reported ~4 mb/d Sep vs 2.4 mb/d Aug Saudi export recovery figure NOT re-derived on my side — I lean on it for the SIG-010 export-recovery-dominant read but Petroline day-10 pushes back on scale. Audit-owed at next flow pass.
- `scripts/read_cap_check.py --agent BRENT` NOT RUN (SKIPPED CONTROL, reported per fleet rule): STATUS gained a substantive 9/21 block; may now be at or over READ_CAP.
- `scripts/boot.py` NOT RUN (SKIPPED CONTROL, reported per fleet rule): task-first time discipline given cached 9/18 prints. Full boot check owed at next normal boot.

**WILL_NEEDS:** none new from this session. Existing Will-facing items unchanged (WQ-264 restart-resolver, WQ-234 AIS-class, WQ-213 refiner-margin reaffirm, WQ-169 USO 165C disposition). BG-02 window closes 9/25 17:00 ET, expected LAPSE.

**FOLLOW-UP:** OSPREY packet (OWED-33 close + Yaroslavl integration) and HANS packet (declining VX-HANS-11.04 orphan) already authored and delivered to their inboxes this session under carve-out ①.

**Commit shas + push receipt to follow in a separate SendMessage after safe-push completes.**

— BRENT
