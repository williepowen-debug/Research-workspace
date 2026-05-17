# PROME STATUS.md
**Updated:** 2026-05-17 10:45 ET

## Core State

**Regime:** BDC/private-credit credit/mark stress is confirmed, but public-credit contagion remains unconfirmed. Surface tape is still calm: HY OAS **276bps** and VIX **18.43**. Stress is concentrated in Brent/gas, USD/JPY, BIZD, WAL/KRE, and pending bank/BDC decision rails.

**Working model:** sponsor-supported private-credit/BDC deterioration + vol-suppressed public tape. Treat HY OAS <300 and VIX <20 as constraint against broad cascade adds, not as an all-clear.

---

## Latest Sync / Architecture State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Complete | Pulled cleanly; local `master` = `origin/master` at `270b6d1d`. |
| REGINALD update | ✅ Pulled | WAL Investor Day findings + May 17 closeout integrated into Prome state. |
| WALTER update | ✅ Pulled | Multi-session closeout confirms signal-routing ownership and May 18 callbacks. |
| Claude Code Prome scaffold | ✅ Present | Phase 2 complete; Phase 3 dry run still pending. |
| WALTER/Prome split | ✅ Codified | WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis. |

---

## Active Decision Layer

| Artifact | Status | Purpose |
|---|---|---|
| `HEARTBEAT.md` | ✅ Fresh May 16; levels rechecked May 17 | Scenario, levels, catalyst/position rails |
| `PROME/SCRATCH.md` | ✅ Fresh May 17 | Ephemeral next-action state |
| `PROME/TODAY.md` | ✅ Fresh May 17 | Today's priorities/levels |
| `PROME/HANDOFF.md` | ✅ Fresh May 17 | Fresh-session / clear-ready handoff |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | ✅ Active | FSK Q1 branch-to-action rails |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | ✅ Active | Bank expiry / Call Report triage rails |
| `PROME/TOSCANINI/QUEUE.md` | ⚠️ Stale | Historical only until rebuilt |

---

## Pending Work

| Action | Pri | Status |
|---|---:|---|
| **Regional-bank Call Report / WAL triage** | 🔴 | REGINALD May 17: WAL 10-Q filed but not integrated; Schedule O / Table 16 cross-credit inventory test pending; MI3/FFIEC PDD status check due. |
| **Bank decision prompt** | 🔴 | Prome-owned synthesis: KRE/WAL/OZK/ZION/SSB cleanup, hold/roll/cut rails, live tape and option pricing required. |
| **BDC/private-credit decision prompt** | 🔴 | FSK Strong Bear allows fresh downside discussion. Needs live pricing and Will approval before trade. |
| **APO / ARES June premium review** | 🔴 | APO above $130 watch; do not roll/rescue dead premium without fresh evidence + pricing. |
| **May 18 Iran / TIC watch** | 🔴 | WALTER flags Iran-war anchor T-1d re-verify and TIC March release / Japan UST-flow read. Route Japan to SAM persistent workflow, not spawn. |
| **Claude Code Prome Phase 3 dry run** | 🟠 | Still pending; first run should be non-mutating except `PROME/CLAUDE_CODE_HANDOFF.md`. |
| **Toscanini QUEUE rebuild** | 🟡 | Stale Mar 26; lower priority than live decision rails. |

---

## Agent / Domain Notes

| Domain | Status | Note |
|---|---|---|
| WALTER / signal routing | 🟠 | Owns signal/news routing. May 17 closeout: BOARD 213; May 18 Iran + TIC callbacks. |
| REGINALD / banks | 🔴 | Persistent/managed — do not spawn. WAL Investor Day bearish increment; 10-Q/MI3 checks due. |
| BROCK / private credit | 🔴 | FSK validates stress; BROCK stale and has WALTER NDFI scope-correction REQ pending. |
| LIQUID | 🟠 | HY OAS benign is main falsification pressure; VIOLET flagged CCC/HY proximity. |
| HENRY / market structure | 🟠 | Stale and pre-NVDA 5/20 catalyst; tape/vol suppression follow-up remains relevant. |
| SAM / Japan | 🔴 | USD/JPY above red threshold; route via persistent SAM, not spawn. TIC March May 18 is live. |
| NEXUS | 🟠 | Stale but high-leverage if multiple domains converge; WALTER still wants revival. |
| PROME | 🔴 | Chief of staff: keep rails/state current, assign decision work, synthesize Will-ready prompts. |

---

## Rules of Engagement

- **No trade execution without Will approval.**
- **No fresh broad cascade short** while HY OAS <300 and VIX <20.
- **No broad bank-premium add** unless Call Reports/tape move to Bear / Strong Bear.
- **No rolling every losing June contract.** Prefer one or two higher-delta roll candidates only if confirmed.
- **Do not panic-sell Sep/Dec runway into green tape.**
- **Do not spawn REGINALD, CARL, SAM, RED, or BRENT.**
- **WALTER routes signals/news; Prome tasks and synthesizes.**
- **Use explicit path staging only; never `git add .` or `git add -A`.**

---

## Next Best Action

Commit/push this Prome/OpenClaw state refresh if Will wants repo state saved, then build Monday bank + BDC decision prompts with live market/option data.
