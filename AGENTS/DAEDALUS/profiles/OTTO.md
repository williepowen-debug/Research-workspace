# Agent Profile — OTTO

**Profile vintage:** 2026-09-05 (metadata clarified 2026-09-08: the existing 9/5 record below covers refreshed §§1–3/6–8 and item-by-item re-verification of §§4–5; no new content review or clock reset).

**Built by:** DAEDALUS · **Body:** 2026-07-07, **§1–§3 + §6–§8 refreshed 2026-09-05**; **§4–§5 carried forward and RE-VERIFIED item by item** (they were still true — except §5.6, see F-1)
**Method:** solo read + **guards RUN** — `scripts/boot.py` rc=0 (3.6s) · `scripts/predictions_due.py` rc=0 (11 OPEN, 0 overdue) · `read_cap_check --agent OTTO` · CR-byte count on four TSVs
**Staleness:** refresh at the next post-CARL-sitting session or >45d → checkpoint **2026-10-20**

> **Not a whole rewrite, deliberately.** OTTO's §4 (deviations) and §5 (do-not-touch) were still accurate structural knowledge — the upgrade unit is one section, not one agent. What had gone stale is the *state*: three of the four L5 blockers my map row carried are **discharged**, and one do-not-touch instruction has become **actively dangerous**.

---

## 1. Identity
Auto-industry **fraud & stress** — Market class, **Tier-2** spawn-on-need. Two theses: **"The Cockroach"** (find one fraud, there are more — 4 confirmed cases + 1 alleged carve-out) and **"The Invisible Exit"** (immigrant subprime skip-defaults bypassing the 30→60→90 DQ chain, **criminally charged** Jun 24 2026). **Both systemic transmission legs are self-disconfirmed** (funding Jul 4; bank-contagion Aug 14, OTTO-30 FALSIFIED) — pattern + fraud-recovery magnitude stand. Sub-agent **WINTERKORN** stewards the docket. **Spawnable by:** PROME / Will.

## 2. File anatomy — what changed since 7/07
| File | State |
|---|---|
| `STATUS.md` | **172 ln / 32,489 B** — was 261 ln / 69,591 B. **Hot/cold split executed 9/2** after a 214%-of-cap breach; cold half → `STATUS_COLD.md` (211 ln / 56,588 B, explicitly *not* a boot read, hot wins on disagreement) |
| `CLAUDE.md` (558 ln) | edited 9/2 (the SIGNALS.md correction) — ⚠️ **both version stamps untouched since June**, F-2 |
| `thesis/PREDICTIONS.tsv` | **20 rows, 11 OPEN, 0 overdue.** ⚠️ lives at `thesis/`, **not** `workbook/` — my own map row cited a bare "PREDICTIONS.tsv:6" and I tripped on it this pass |
| `workbook/` | PANEL_10D (137 rows, `collection_period` 137/137 zero blanks) · KB · VX (partial-FROZEN) · FLOW · ML · SHELF_ACTIVITY (**FROZEN + EVENT-DRIVEN 9/2**) · ABS_ISSUANCE · EXTENSION_PROXY · CROSS_AGENT_LOG · VX_HISTORY |
| `scripts/` | boot · predictions_due · catalyst_countdown · panel_10d (35 KB) · severity_divergence · shelf_halt_monitor · backfill_collection_period · 2 declared stubs |
| 3-log taxonomy | `CHANGELOG` analytical · `MAINTENANCE` structural · `STALE_PUNCHLIST` forward — ⚠️ the punchlist is itself stale, F-3 |

## 3. Per-dimension — unchanged in form
Convergence substance across 4 local forms (SIGNAL DASHBOARD, stage tables, VX registry, panel) · exit bounds **calendar-dated not session-counted** (defensible: dockets and prints resolve theses, not sessions) · predictions with `Resolve_Date` + `Invalidation` columns and a working due-check · routing via NEXUS_BRIEF + WALTER lane + PROME packets · TRADE lane correctly **FROZEN-dormant with an explicit unfreeze condition**.

## 4. Deviations from standard (+ why) — CARRIED 2026-07-07, re-verified 2026-09-05
- **Convergence = equivalent-titling case (ruled 7/7):** substance CONFORMANT across 4 local forms; the universal 5-pt + Independence *handles* are the only gap — additive, never replace the dashboard/stage-table (PAT-015/022/038). ✅ still the case.
- **Calendar-dated (not session-counted) exit bounds** — ADAPTED, not debt.
- **🔴🔴 double-red severity extension** beyond the root 4-state key — local richness, keep. ✅ live in STATUS.
- **Boot↔closeout numbering cross is deliberate** (catalysts swept before predictions resolved, CLAUDE L129-33). Not a symmetry defect.
- **Stub scripts that say so** — `extension_proxy` / `abs_issuance` print "placeholder data" every run; a markdown-only read of "script-generated monitoring series" would OVER-rate them (inverse PAT-037). ✅ both still present and still declared.
- **Tier-2** = spawn-on-need cadence; structurally uncapped.

## 5. Load-bearing context / DO NOT TOUCH — carried, **item-by-item re-verified 2026-09-05**
1. **`boot.py` keyword filter is a coupling contract** (boot.py:104-5): child-script alert lines must contain 🔴/🟠/"OVERDUE"/"IMMINENT"/"OPEN |" or they are suppressed at boot. Renaming alert strings silently drops them. ✅ verified — `predictions_due` output still emits `OPEN |`.
2. **`predictions_due` rc=1 = "overdue exists," not failure** — boot.py depends on it. ✅ verified: rc=0 today with `🔴 0 overdue`, consistent.
3. **FROZEN banners are load-bearing + position-sensitive** — `ledger_staleness` reads only the first lines. `VX.tsv`'s is a **partial** freeze (registry durable, `Current_Value` dead) — ✅ confirmed at line 1. `VX_HISTORY` is name-exempt ("history" substring); renaming it re-arms scanning.
4. **WINTERKORN ownership boundaries:** `CATALYSTS.tsv` WINTERKORN-maintained · CALIBRATION inside `WINTERKORN_MEMORY` OTTO-write-only · PENDING append-by-WINTERKORN/clear-by-OTTO · the spec forbids WINTERKORN editing `WINTERKORN.md` (hence its stale "Last run: none" header — **artifact, not neglect**). CATALYSTS↔CRITICAL TIMELINE is a curated subset, **not** a mirror. ✅ all three files present.
5. **OTTO-04 resolution convention is Will-ratified** (stays on the blended Fitch index; Sep-30 miss = falsified-on-window / confirmed-on-substance). Don't "fix" the metric.
6. ~~**TSV convention is CRLF**~~ — 🔴 **STRUCK 2026-09-05, see F-1.** Schema locks stand and are unaffected: `predictions_due` → `thesis/PREDICTIONS.tsv` columns; `catalyst_countdown` → 8-col lowercase CATALYSTS header incl. `date_class`.
7. **INBOX not processed on normal spawns** (separate spawn purpose) — don't import boot-auto-triage.
8. **NEXUS_BRIEF Tier-2 opt-in, locked schema** — protect CROSS-DOMAIN + CALIBRATION under length pressure.
9. **3-log taxonomy** (CHANGELOG analytical / MAINTENANCE structural / STALE_PUNCHLIST forward) — don't merge.

## 6. Findings

**🔴 F-1 — A DO-NOT-TOUCH INSTRUCTION IN *MY OWN* PROFILE IS FALSE OF THE FILES, AND OBEYING IT WOULD CAUSE THE HARM IT WAS WRITTEN TO PREVENT.**
Old §5.6 read: *"TSV convention is CRLF (deliberate; LF-normalizing 'cleanup' recorrupts)."* Measured today — **CR bytes = 0** on `thesis/PREDICTIONS.tsv` (21 ln), `workbook/VX.tsv` (89), `docket/CATALYSTS.tsv` (40), `workbook/PANEL_10D.tsv` (138). **Every OTTO TSV is LF.** Either the convention was abandoned or the 7/07 claim was wrong; the git history does not show a normalization commit, which favours the second. **Why this is the dangerous class:** a session obeying the instruction would *add* CRLF to "restore" the convention — the rule inverts into corruption. A stale prohibition is worse than a stale fact, because a fact reads as merely old while a prohibition reads as protective. **STRUCK; schema locks kept** (those are separately true and were the useful half).

**🟠 F-2 — CHARTER VERSION STAMPS ARE 3 MONTHS STALE ON A FILE EDITED THREE DAYS AGO, AND THEY DISAGREE WITH EACH OTHER.** `CLAUDE.md:3` header **`Version: 2.5 | Updated: 2026-06-08`**; `CLAUDE.md:558` footer **`v2.7 | 2026-06-09`**. The file was edited **2026-09-02** (the SIGNALS.md correction, itself well done). This was carried **UNVERIFIED** on my map row since 7/07 — **now VERIFIED live.** Cheap fix, but a booting reader takes the header at face value, and two stamps that disagree mean neither can be trusted.

**🟡 F-3 — `STALE_PUNCHLIST.md` lists a discharged item as DEFERRED.** Its `(b)` — *"delete the dead `AGENTS/SIGNALS.md` append instruction"* — was **fixed 9/2**; `CLAUDE.md:320` now carries a ⛔ CORRECTED banner and `:325` the carve-out-② explanation. The punchlist still shows it deferred. The forward-log has the same rot the desk built it to prevent.

**🟡 F-4 — STATUS regrew to the rotation trigger in three days.** `read_cap_check --agent OTTO`: **32,489 B = 🟡 rotate-tier (≥75% of budget)**, i.e. **99.8% of the 32,550 B budget** — under cap, one edit from over. OTTO fixed a **214%** breach on 9/2 by a verbatim hot/cold split; the hot half is back at the trigger on 9/5. That is the **compress-then-regrow** class (PAT-055) at three days rather than ten. Not a criticism of the split — the split was right — but the split alone only resets the clock, and the cold file is 56,588 B, so there is somewhere to put things.

### ⚠️ Where MY MAP ROW was wrong — three L5 "blockers" are discharged
- **"dead `Append to AGENTS/SIGNALS.md` instruction (CLAUDE.md:320)"** → **FIXED 9/2.** Struck.
- **"OTTO-07 re-instrument before 12/31"** → **instrument was REBUILT 7/25** (`scripts/shelf_halt_monitor.py`, after the old one was found default-zero, PAT-060) and the row records it.
- **"SHELF_ACTIVITY.tsv probe ran once 7/25 — Staleness #4 packet (PAT-095)"** → **ANSWERED, and answered well.** The file now carries `# FROZEN 2026-09-02 — not maintained; STATUS is canonical` **plus a declared EVENT-DRIVEN cadence naming the exact re-run trigger** (OTTO-07 needing a fresh reading, or any reported shelf withdrawal) **and its own reasoning** (*"a re-run of an instrument whose last reading was unanimous buys no decision before the 12/31 resolve"*). That is the declare-and-freeze branch of the two-state rule, chosen explicitly and cited to the sweep that asked. **My row would have carried this as an open gap.**
- **"STATUS 261, still >250"** → **172 lines.** Line cap met; the byte tier is the live issue (F-4).

## 7. Grade — **L4 (H) HELD**, but the remaining distance is now three small things
| Leg | Verdict | Basis |
|---|---|---|
| L1–L2 floor | **PASS** | STATUS + BOTTOM LINE; 10 accruing ledgers, schemas valid |
| L3 convergence matrix | **PASS** | substance across 4 local forms (equivalent-titling, ruled 7/7) |
| L3 exit rules | **PASS** | calendar-dated bounds + executed channel-kill (OTTO-30 FALSIFIED, both systemic legs self-disconfirmed) |
| L3 predictions resolving | **PASS** | 20 rows / 11 OPEN / 0 overdue; OTTO-07 re-priced 55%→15% **on first real measurement** |
| L3 dated falsification surface | **PASS** | `Invalidation` column per row + CHANGELOG pivots |
| L4 TRADE feeding proposals | **ADAPTED-PASS** | TRADE lane FROZEN-dormant **with an explicit unfreeze condition** (CARL/LIQUID no-book-by-design precedent) |
| L4 signals flowing and consumed | **PASS** | CARL leg-spec packet consumed (`inbox/processed` 8/20); 9/2 packets to CARL + WALTER; panel figures matched CARL's independent pull **to the cent** |
| L5 clean closeouts | **PASS** | s020 and s021 both closed clean with measured before/after figures |
| L5 zero YEYOU flags | **FAIL→ (1 open)** | YEY-003 (STATUS 148 vs own ≤120 target) logged 8/20, **still OPEN in YEYOU's ledger** — though see `profiles/YEYOU.md` F-1: that ledger is not being reconciled, so an OPEN row there is weak evidence either way |
| L5 current | **PASS** | last session 9/2 |
| Role gap | **FAIL** | §2 universal 5-pt + Independence overlay (punchlist (a)) — the one genuine unmet handle |

**Conf H.** **L5 line is now: §2 overlay + the two version stamps + a byte-tier rotation.** All three are small and none needs a research session. *(The YEYOU leg is noted, not weighted — its ledger has two demonstrably-closed rows still reading OPEN.)*

## 8. Open questions
- `WAL/` spinout folder (12.4 MB) — lifecycle question for PROME/Will at spinout, not OTTO debt. **Still open.**
- WINTERKORN "weekly-Tue" cadence claim vs actual on-demand behaviour — drop the weekly claim or restore the cadence?
- STATUS Outbound Signals "📤 QUEUED" rows (CARL, NEXUS) — dated now, or still undated queue state?
