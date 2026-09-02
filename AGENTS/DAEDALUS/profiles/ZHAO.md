# Agent Profile — ZHAO

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** one session since reactivation rewrote canon (8/21) · 55d > 45d. Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-15**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*

**Built by:** DAEDALUS · **Date:** 2026-07-07 · **Comprehension method:** solo direct read (full core: CLAUDE, STATUS, boot.py, NEXUS_BRIEF, TRADE, workbook ×6 TSV, LAST_COMPLETION, inbox/outbox; subagent readers lost to a credit outage — small enough to hold)
**Sources read:** all of the above + PROME reactivation packet (7/5) + ZHAO's own reactivation outbox (7/4). · **Staleness:** refresh after ZHAO's next 2-3 sessions (freshly reactivated — profile will age fast) or >45d.
**Context:** reactivated **2026-07-04 after ~2.5mo dormancy** (8 commits: STATUS rewrite, KB-076..087, VX/FLOW/PREDICTIONS refresh, boot.py + NEXUS_BRIEF built). PROME flipped ROSTER dormant→ACTIVE 7/5. Architecture is a **pre-June-buildout vintage** + a high-quality 7/4 self-rehab layer.

---

## 1. Identity
China macro → U.S. transmission: China UST exit (Belgium/Euroclear proxy methodology — its signature analytical asset), PBOC/CNY, property·LGFV·fiscal, HK peg, trade war, Taiwan-econ, Korea contagion node, India oil. **Market** (research/signal agent, no position — self-described). Primary edges: →LIQUID (UST demand hole), →SAM (Korea/Asia), →HAWK/BRENT (energy), →HENRY (10Y), →HANS (Euroclear).

## 2. File anatomy (where the richness lives)

| File | Holds | Richness? |
|---|---|---|
| STATUS.md (153 ln) | **The thesis lives here** (no thesis/ dir): Jul-4 regime re-frame table (EMERGENCY 43/55 → ELEVATED 27/55), dashboard w/ [CONF]/[EST] tags, 11-vector scored convergence matrix, exit rules + falsification tripwires, calendar, predictions mirror | live state + durable rails, mixed |
| scripts/boot.py (252 ln, NEW 7/4) | 6-section boot brief: live FX/Brent pull + band check, key-figure age (14d bar), **TIC-release-watch (computes whether a newer print should exist)**, catalyst docket, open predictions, VX staleness — built explicitly to kill the 2.5mo-drift failure mode | **the crown asset** — self-built staleness guard |
| NEXUS_BRIEF.md (72 ln, NEW 7/4) | Full schema + **RED counter-frame with rebuttal + discriminating test**, honest counter-weight (April record aggregate inflow masks the hole), WAITING-FOR table | exemplary — among the best briefs in fleet |
| workbook/KB.tsv (87 rows) | 13-col, Admiralty + Epistemic, Stale_By self-dating, → routing tags in Notes | permanent record, accruing |
| workbook/VX.tsv (33 rows) | 11-col banded vectors, refreshed 7/4 | live |
| workbook/PREDICTIONS.tsv (10) | Invalidation col + confidence-move audit trails in Notes (ZHA-01 70→55→25%); ZHA-02 CONFIRMED, ZHA-08 FALSIFIED 7/4 *per its stated criterion* | disciplined; no ARCHIVE/scoreboard |
| workbook/FLOW.tsv (12) | 9-col pathways w/ FIRING/DE-ESCALATED/DORMANT states + re-arm conditions | live |
| workbook/VX_HISTORY.tsv (5) | Feb-13 seed rows only — append discipline never took | dormant |
| TRADE.md | **FROZEN 7/4 by DAEDALUS** (dormant-cluster sweep) — banner rationale now stale ("ZHAO dormant"; it reactivated same day) but freeze itself still correct (Mar-9 four-anchor content, superseded thesis, no position) | frozen, banner-wording debt |
| CLAUDE.md (183 ln) | Identity/scope/routing solid; **carries a rotted layer** — see §4 | operating spec w/ drift |
| sources/ (RP-ZHAO-1..9 + 2) | Feb-Mar research corpus (Belgium proxy, LGFV, HK peg, Taiwan, insurers) | archival, referenced |
| inbox/ | 3 stale items (May-9, May-22 HAWK Hormuz — now OBE, Jun-26 PROME triage) + fresh 7/5 PROME synthesis + WALTER SIG 7/6 — dedicated inbox spawn owed (STATUS Next-5) | backlog |

## 3. Per-dimension local representation

| Dimension | Where it lives | Form | Rich? |
|---|---|---|---|
| Thesis structure | STATUS (re-frame table + nuance block) + CLAUDE Belgium-methodology section | 2-anchor demand-hole frame; growth-vs-capital-account decoupling explicitly argued | ✅ substance / ❌ no thesis/ dir, no version stamp |
| Convergence | STATUS titled CONVERGENCE MATRIX | 11 vectors, 5-pt, total 27/55 + concentration note | ✅ handle present (no Independence col) |
| Invalidation / exit | STATUS EXIT RULES + tripwires; TRADE exit signals (5+ sessions); per-prediction Invalidation col | thesis-kill = **print-counted** (2/3 consecutive prints — apt for monthly TIC data) | ✅ adapted |
| Thresholds | CLAUDE KEY THRESHOLDS (durable) + STATUS dashboard (live) | split exists BUT CLAUDE's `Current` column rotted (see §4) | 🟡 |
| Predictions | workbook/PREDICTIONS.tsv | 10 made / 2 resolved; confidence-move audit trails; no ARCHIVE, no calibration scoreboard, no failure-synthesis | 🟡 |
| Cross-agent routing | CLAUDE route-matrix (7 conditions) + NEXUS_BRIEF SENDING/WAITING + outbox w/ "awaiting PROME route" state | ✅ (consumption not yet proven — 3d post-reactivation) |
| Staleness discipline | boot.py (14d/21d bars, TIC-watch) + KB Stale_By + STATUS self-flags ("do not cite as current") | ✅ exemplary — mechanism, not discipline |

## 4. Deviations from standard (+ why)

**The 7/4 rehab layer is excellent; the CLAUDE.md carries a pre-dormancy rotted layer** — 6 distinct drift instances:
1. **`domain/sources/` referenced ×2 (L47, L181) — dir doesn't exist** (the PROME-flagged bug; real archive targets: `sources/`, `archive/`).
2. **KEY THRESHOLDS `Current` column stale** (L105-110: TIC $683.5B / Belgium $477.3B / CNY 6.85 / HIBOR −211bps "AT THRESHOLD") — all superseded by 7/4 STATUS ($651.1B / $454B / 6.80 / −136bps EASED). A boot-loaded durable file contradicting the live read = the BRENT-line-168 class; also violates ZHAO's own "don't maintain stale copies" rule.
3. **CONVERGENCE MATRIX note stale** (L126: "10 vectors… 34/50 🔴 CRITICAL" vs live 11 vectors, 27/55 🟠).
4. **MAIL SYSTEM section broken** (L136-150): "All inter-agent communication lives in removed:" — a cleanup scrub left literal "removed" text ×2 (+ FILES row L183), plus refs to HERMES (retired) and PROTOCOL.md/RECEIPT.md (don't exist). Contradicts the live WALTER-lane reality (inbox/WALTER/ exists).
5. **PAT-031 violation:** SPAWN 1b runnable invocation is bare root-relative (`.venv/bin/python AGENTS/ZHAO/scripts/boot.py`, "from repo root" in prose, no `rev-parse` wrap anywhere in the doc — scanner heuristic would fire). boot.py itself self-locates fine; the *invocation* breaks from an own-dir launch.
6. **HK AB threshold inconsistency:** CLAUDE <HK$40B vs STATUS dashboard <$45B = 🟡.
Also: **no MEMORY.md / MAINTENANCE.md / thesis/ / PREDICTIONS_ARCHIVE / board_log.tsv / domain/** (all six self-identified gaps VERIFIED absent). BOTTOM LINE substance sits mid-doc (STATUS L22) — no trailing labeled handle.

**Deliberate/fine:** print-counted exits (monthly-data domain); boot.py's in-script CATALYSTS list (documented as maintained); research/signal no-position stance.

## 5. Load-bearing context / DO NOT TOUCH
1. **Belgium proxy methodology (CLAUDE L114-121) is the signature analytical asset** — the direction-discriminator (Belgium-flat + China-falling = genuine exit) just carried the 7/4 headline call. Never simplify it away.
2. **boot.py MUST run under `.venv/bin/python`** (yfinance lives in the venv, not system python3) — its ModuleNotFoundError message documents this; any cwd-proofing fix must preserve the venv interpreter.
3. **boot.py TIC-release-watch parses the data-month from VX-ZHAO-1.02's Source cell** (regex on "Mon YYYY") — changing that cell's format silently breaks section [3].
4. **KB enum discipline is schema-enforced** (SCHEMA.tsv allowed_values + AGENTS/VOCABULARIES.tsv) — SPAWN steps 3/3b are load-bearing, don't trim.
5. **TRADE.md freeze banner is DAEDALUS-authored** (7/4 sweep) — wording update is sanctioned, but *unfreezing* requires a concrete ZHAO position re-emerging, not just reactivation.
6. **Confidence-move audit trails in PREDICTIONS Notes** (70→55→25%) are deliberate history, not clutter.

## 6. Maturity snapshot
**L3 (Conf H), provisional-L4** — first scan ever (was on the dormant/unscanned list; reactivated 7/4). L2 floor solid (schema-valid accruing ledgers); L3 legs all present (titled scored matrix, print-counted exits + tripwires, predictions resolving incl a clean 7/4 falsification-per-stated-criterion). **L4 gate = consumption evidence**, not structure: the 7/4 LIQUID outbox is written-awaiting-PROME-route, NEXUS_BRIEF is 3 days old — one session post-reactivation is too early to score "signals flowing" (PAT-028/PAT-034: sequencing, not defect). Expect L4 within 2-3 sessions if the loop fires. Work queue → `upgrades/ZHAO_CARD.md`.

## 7. Open questions / comprehension gaps
- **Will the reactivation hold?** One excellent session ≠ live cadence (the 2.5mo drift happened once already; boot.py now guards, but only if ZHAO spawns). Boot-cadence watch = PROME/Will lane.
- Korea coverage (USD/KRW, BoK, NPS) overlaps SAM's Asia lane — scoped OK today (Korea=ZHAO, Japan=SAM) but worth a one-figure reconciliation check next SAM firming.
- VX_HISTORY: revive append discipline or FROZEN-banner it? ZHAO's call.
- inbox backlog (3 stale + 2 fresh) — dedicated inbox spawn owed per its own STATUS Next-5.
