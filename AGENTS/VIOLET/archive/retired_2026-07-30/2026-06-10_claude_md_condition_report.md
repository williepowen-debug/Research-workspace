# CLAUDE.md Condition Report — 2026-06-10 (Will ask; housekeeping item 3 of 4, pre-pass analysis)

**File:** `AGENTS/VIOLET/CLAUDE.md`, 197 lines. Verdict up front: **the protocol spine (SPAWN PROTOCOL + OUTPUT RULES + FILES table, ~60% of the file) is healthy and recently maintained (6/1 codification, 6/5 live-event override, 6/7 NEXUS_BRIEF, 6/10 steps 13a + 3 FILES rows). The bottom half (DOMAIN SCOPE boundary rule → RESEARCH PRIORITIES, lines ~95-168) is April-bootstrap residue that has never been touched since.** The file teaches a fresh spawn two contradictory signal-routing protocols and one falsified indicator. Three dead path/section references. One stale claim in STATUS surfaced during verification.

---

## Section-by-section condition

| Section (lines) | Condition | Notes |
|---|---|---|
| Header/Domain (1-4) | 🟡 minor | Network line says feeds HENRY/LIQUID/RED, receives BROCK/HENRY/HAWK — omits SAM + BRENT edges (both active this week) and disagrees with the fuller receive table at L111 |
| IDENTITY (8-12) | 🟢 | Sound |
| SPAWN PROTOCOL (16-60) | 🟢 mostly | The maintained core. Two nits: step 13 ends "→ `outbox/` per the Outbox Protocol below" — **no such section exists** (dangling ref), and contradicts step 12 (outbox 🔴-acute only). Step 3's MEMORY description will need a touch after the MEMORY subtraction job (dependency, not now) |
| OUTPUT RULES (64-72) | 🟡 | One broken path: "archive old research to `domain/sources/`" — **`domain/` does not exist**; also inconsistent with step 7 ("research/ or archive/") |
| DOMAIN SCOPE (76-95) | 🟠 | Owns-list lists VIX1Y (never tracked) and omits VIX9D, M1:M2 futures curve, COT positioning (all load-bearing daily). **Boundary rule (L95): "write to outbox… HERMES (the mail carrier agent) will deliver it" — HERMES is dead; contradicts the MAIL section (L54) and step 12 in the same file** |
| CROSS-AGENT SIGNALS (99-119) | 🟠 | Send-table CONDITIONS are good trigger definitions, but: row 2 "Term structure inverts" carries 🔴 with the pre-v3.1 leading-indicator framing; the implied MECHANISM (signal files to agents) is the dead channel. Receive table now **duplicates SIGNAL_INTAKE.md** (which owns inbound as of today) and omits SAM/BRENT |
| KEY THRESHOLDS (123-132) | 🔴 worst | All "Current TBD" since April (never wired — STATUS owns live values). Content errors: "VIX3M/VIX <1.0 — leading indicator" (**falsified v3.1, KB-VIO-034**); "SKEW >140 tail risk bid" (current calibration: 20d-avg 140 = regime line, single-day 140 touches are noise per MEMORY principle 10; fear line is >150); "Credit-VIX lag >5 days" isn't an operational threshold. The four DURABLE lines now live in SIGNAL_INTAKE.md with correct framing |
| CONVERGENCE MATRIX (136-158) | 🟠 split | **The 5-point scoring scale (L140-148) is load-bearing — KEEP** (it's the fleet-universal key; today's re-based 22/45 used it; 6/9's 13/40 didn't match it, which the scale's presence here resolves). The template vector rows (⚪/TBD/"Never", 5 vectors) are dead weight — STATUS owns the real matrix (currently 9 vectors) |
| RESEARCH PRIORITIES (162-168) | 🔴 dead | All 5 are the April bootstrap list: #1 regime library (built), #2 credit-vol lag (quantified — four-model synthesis), #3 term structure (falsified/refined v3.1), #4 crisis analogs (built), #5 options flow (tooled — vix_options.py). STATUS Research Queue owns live priorities |
| FILES YOU MAINTAIN (172-192) | 🟡 | Current after today's 3 adds. Two row-level issues: **`VX.tsv` is dead** (threshold-dashboard style, stale since 4/15, Current_Values 8 weeks old — same disease SAM slimmed 37→6 rows; VX_DAILY superseded the daily series) but the row claims "Daily when markets open"; **`FLOW.tsv` stale since 4/15** ("per signal" — but the 5/21 LIAISON and all NEXUS_BRIEF-era exchanges were never logged) |
| Footer (196) | 🟢 | Fine |

## Verification by-catches (not in CLAUDE.md, found while checking its claims)

1. **STATUS/SCRATCH carry a stale inbox claim — including in today's rewrite (my propagation).** "Inbox: 1 pending signal (5/14 gamma) — formal disposition deferred" is FALSE: `inbox/processed/_disposition_2026-05-14_...md` filed 6/6 (Saturday org session), status ABSORBED-closed, content mapped to KB-VIO-062/067/070. The line was carried forward from pre-6/6 STATUS text without a filesystem check (verify-counts-before-propagating class). Housekeeping item 7(e) is ALREADY DONE — strike it; fix STATUS line at EOD re-stamp.
2. `outbox/` still holds the 4/15 SIG to LIQUID (known item 7d, overtaken by events) + 4 messaging-era SIGNAL_TEMPLATE files — disposition decision pending, separate from this pass.

## Proposed fix list (ranked by behavioral impact)

1. **Boundary rule (L95):** → "signal in another agent's domain goes in NEXUS_BRIEF CROSS-DOMAIN (or `outbox/` only if 🔴-acute, per step 12). Don't deep-dive it." Kills HERMES + the contradiction.
2. **Step 13 tail:** "→ `outbox/` per the Outbox Protocol below" → "→ NEXUS_BRIEF / outbox per step 12." Kills the dangling section reference.
3. **KEY THRESHOLDS:** replace the table with a 3-line pointer block: durable trigger lines → `SIGNAL_INTAKE.md § ACTIVE THRESHOLDS` (the 4 lines, correctly framed); live values + margins → `STATUS.md`; full threshold logic → thesis. (Per orchestrator's earlier note, amended: pointer, not a second copy.)
4. **CROSS-AGENT SIGNALS:** keep send-table conditions (they're VIOLET's outbound trigger definitions — fix row 2's framing to "inversion = peak-marker broadcast"), add one mechanism line ("delivery per step 12"), replace receive table with a pointer to `SIGNAL_INTAKE.md` (inbound owner as of today; avoids the next drift), add SAM/BRENT to the send/receive edges where real.
5. **CONVERGENCE MATRIX:** keep the scale + the "STATUS must include a matrix" requirement; delete the 5 template rows; point at STATUS for the live matrix.
6. **RESEARCH PRIORITIES:** delete the list; one line: "Live research queue: STATUS.md § RESEARCH QUEUE. Durable research themes: thesis."
7. **OUTPUT RULES L69:** `domain/sources/` → `research/ or archive/` (match step 7).
8. **DOMAIN SCOPE owns-list:** drop VIX1Y; add VIX9D ratio, M1:M2 futures curve, VIX COT positioning.
9. **Header network line:** align with the (pointered) edges — add SAM/BRENT.
10. **FILES table rows:** VX.tsv + FLOW.tsv rows get honest frequency labels pending the disposition decisions below.

## Decision items for Will (not executed in the pass without a call)

- **A. VX.tsv disposition** — dead since 4/15; VX_DAILY + STATUS superseded it. Options: (i) retire to archive (recommended — VIOLET, unlike SAM, has no manual-only metrics left in it; all 13 rows are auto-pulled or STATUS-owned now), (ii) SAM-style slim to unique rows. Either way step 8 + FILES row update.
- **B. FLOW.tsv re-scope** — options: (i) re-scope to "formal outbox/LIAISON sends only" and backfill the 5/21 LIAISON row (recommended — keeps it honest at its real cadence), (ii) retire (NEXUS_BRIEF + KB carry the content now).
- **C. BOARD consumption boot step** — STATE.md §1 says propagation pending per-agent; Will-approved defaults exist. **Recommend DEFER until WALTER answers the MARKET_VOL flag** — wiring BOARD-pull before any vol signals actually route to VIOLET is dead boot-weight. Name it in the flag follow-up instead.
- **D. Boot predictions-due scan gap** (build item, not residue): VIOLET predictions live in the thesis table with no boot-time due/stale scan (SAM/OTTO run predictions_due.py; auto-memory `finding_boot_predictions_scan` caught a 24d-stale MISS elsewhere on first run). Cheap to add to boot.py later; out of scope for this pass.

## Sequencing

Items 1-10 are one pass (~30 min) + MAINTENANCE entry + commit. Decisions A/B can ride in the same pass if called now, or get parked as punchlist rows. C/D are named, deferred. The MEMORY-subtraction dependency (boot step 3 wording) waits for that session.
