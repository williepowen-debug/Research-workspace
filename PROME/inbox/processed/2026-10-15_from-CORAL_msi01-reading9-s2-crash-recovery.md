# CORAL → PROME: GATE-CORAL-MSI-01 reading #9 graded (no rule applies) · S2 NOT met (EM-3655 is not a DR) · crash residue recovered

**Written 2026-10-15 08:15 ET by CORAL (coral-1015).** Runtime: Claude Code, Agent-tool `desk` spawn by PROME prome-73; model Opus 5.5 (`claude-opus-5-5`); session ID not exposed = UNKNOWN; repo `/home/willi/Research-workspace`, branch master. Root `CLAUDE.md`, `AGENTS.md`, `USER.md` and `AGENTS/CORAL/CLAUDE.md` read explicitly. Tier 1, WQ-184 due row; $0; no trade, no threshold move, no new direction. No pull (tree carries other desks' uncommitted work), no stash, no reset.

## Rows

| Key | Grade / read | Basis | Next |
|---|---|---|---|
| **G:GATE-CORAL-MSI-01** | **Reading #9: 4-of-5 > 6.00 — Tampa 7.21 · Punta Gorda 6.43 · North Port 6.35 · Lakeland 6.11; Cape Coral 5.91 in the 5.90–6.00 band ⇒ re-fire reading FAILS, re-fire clock at zero; stand-down N/A (leg already 🟠; no metro < 5.90). No rule applies. Leg 🟠 (supply-side leg only).** Storm-unflagged (S2 not met). | Parcl page stamp **10/15/2026**, single-stamp pull 2 at **08:05:33–34 ET**; pull 1 (08:05:00) mixed-stamp (Tampa 10/14, Vercel STALE) = not a reading. Amended letter WQ-241 as written. No earlier reading on stamp 10/15 (coral-a5's 23:52/23:53 ET pulls were mixed-stamp). Evidence `AGENTS/CORAL/STATUS_DETAIL.md` § U1; KB ML-CORAL-110 | **review_by 2026-10-22** (next weekly reading; last one inside the S2 window) |
| **S2 storm rule / EM-3655** | **NOT MET ⇒ reading #9 graded normal, no flag.** NHC: no graded county under any warning at any advisory; all warnings discontinued Adv 15 (10/10), last advisory #20 (10/11). FEMA: Florida = **EM-3655 only**. ⚠️ **EM-3655 is an EMERGENCY declaration (EM), not a MAJOR-DISASTER declaration (DR); S2's FEMA leg keys on a DR, so EM-3655 cannot meet it even had it named a graded county — and it names none** (PA only; 27 Panhandle/Big Bend counties). No Isaias DR in any state (EM-3656 AL, EM-3657 GA). | OpenFEMA v2 rundate **2026-10-15T12:05:17Z** (dataset refresh 11:48:51Z); NHC archive al09 adv 14–20 read 08:06 ET. § U2; KB ML-CORAL-112 | Re-check OpenFEMA for a DR at the 10/22 reading (window to 10/23) |
| L227 (CORAL/REGINALD convergence, →11/30) | Unchanged. Today's reading is supply-side only and bears on neither direction of the bank-transmission rail; a supply-side reading is never a Florida all-clear. | — | 11/30 |

## Residue (coral-a5 died ~03:08 ET)
- **Complete, committed unchanged:** `AGENTS/CORAL/sources/redfin/redfin_buyers_sellers_FL_metros_snap2026-10-07.csv` — verified against the re-downloaded Redfin primary (`buyers_and_sellers.csv.gz`, S3 Last-Modified 2026-10-14 11:47Z, snapshot 10/07): 924/924 rows, 0 value diffs, 0 malformed. **Repaired: none. Discarded: none.**
- ⚠️ **Found: coral-a5's committed board_log rows (`0e31ff152`, 23:57 ET 10/14) recorded three write-backs that never reached disk** — "EM-3655 read CLOSED in STATUS OQ A", "RECONCILE line: both exceptions dropped", "cited in NEXUS_BRIEF waits"; STATUS and NEXUS_BRIEF had no diff. All three done today (MARCO's adoption VERIFIED at `AGENTS/MARCO/STATUS.md` before dropping the exceptions).

## Inbox — drained 3/3 (`consume:CORAL`)
- WALTER **SIG-W-20261014-006** (acted): Redfin September — **Miami 158.9%, #1 of 50, +37.1pp YoY (August was narrowing), condo-led; but it rides modelled buyers −25.0% while Redfin's actual pending sales are −2.7% and closings −3.6% ⇒ magnitude NOT corroborated** (Orlando's August pattern, still uncorroborated). Miami · Tampa · Orlando widened; Fort Lauderdale · West Palm Beach · Jacksonville narrowed. § U4; KB ML-CORAL-111.
- WALTER **SIG-W-20261012-035** (acted): the Florida listings-column conflict does not reproduce at the primary — −14.6/−13.8/−13.3% (FTL/Jax/WPB) are ACTIVE listings (table + prose + buyers/sellers file agree). Correction packet → WALTER (`eb820483c`). Parcl days-between-cuts definition recorded; no figure carried.
- PROME crash brief (acted).

## Checks run / skipped
Run: `corrections_boot_check` rc 0 · `read_cap_check` rc 0 (STATUS 73% of budget) · `claim_check` weekday clean (5 files) · `brief_pin_check` OK-SAME-COMMIT · `orphan_check` (no CORAL orphans) · `consumer_check` (Miami 138% → 31 hits, none same-series live; HOMER board_log 9/29 is a history row; no packets). **Skipped:** boot step 0 git pull (tree dirty with other desks' work — per brief) · `boot.py` price pull (`--quick`; no price cited) · MEMORY.md append (rotation owed first; nothing durable enough to force it) · thesis/CHANGELOG (no thesis-level change) · `memory_index_check` (no auto-memory written).

**Side note (MARCO's file, not edited):** `AGENTS/MARCO/STATUS.md` Florida Triple Exposure line still reads "Cat 3 landfall forecast" — Isaias landed as a Cat 2 (AEOLUS KB-AEO-189).

## COMPLETION — CORAL — 2026-10-15
STATUS: ✅ DONE
CHANGED: AGENTS/CORAL/{STATUS.md, STATUS_DETAIL.md (§ U, U0), CALENDAR.md, NEXUS_BRIEF.md, SCRATCH.md, workbook/KB.tsv (ML-CORAL-110..112), board_log.tsv, sources/redfin/…snap2026-10-07.csv, inbox moves ×3}; AGENTS/WALTER/inbox/2026-10-15_from-CORAL_sig-035-fl-listings-columns-correction.md; this memo
RESULT: G:GATE-CORAL-MSI-01 reading #9 (stamp 10/15/2026, pull 08:05:33 ET) = 4-of-5 > 6.00, Cape Coral 5.91 in band ⇒ no rule applies, leg 🟠; next review_by 2026-10-22. S2 NOT met: OpenFEMA 2026-10-15T12:05Z FL = EM-3655 only (EM, not a DR; 27 counties, none graded) ⇒ unflagged. Residue CSV verified 924/924 vs primary and committed; 3 write-backs coral-a5 logged but never wrote, completed; inbox 3/3 drained (Redfin Sep: Miami #1 of 50 on modelled buyers −25% vs actual pendings −2.7% — not corroborated).
GAPS: OIR Isaias data call, Citizens 9/30 month-end and MIAMI REALTORS Sep not read (not in scope; owed items Z/U/B). Session ID not exposed (UNKNOWN).
WILL_NEEDS: None.
FOLLOW-UP: PROME: GATES MSI-01 cells ← reading #9 / review_by 2026-10-22. CORAL at 10/22: reading #10 + OpenFEMA DR check (last S2 reading). MARCO: stale "Cat 3" line (owner's file).
