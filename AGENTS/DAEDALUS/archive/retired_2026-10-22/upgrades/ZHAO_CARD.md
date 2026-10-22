# Upgrade Card — ZHAO (read-only assessment; edits routed as task-packet — ZHAO is LIVE)

> 🗄 **ROUTED 2026-07-08 — CLOSED AS A QUEUE 2026-08-17 (self-audit F5 banner pass).** This card's findings were routed to the owner/FLEET_MAP when written; per-row states below are historical. Not maintained — current gaps live on the agent's FLEET_MAP row. Do not work rows from here without re-verifying at the agent.

**By:** DAEDALUS · **Date:** 2026-07-07 · **Class:** Market (China macro → U.S. transmission; research/signal, no position)
**Method:** `UPGRADE_PROTOCOL.md` · graded vs `BLUEPRINTS/market-agent.md` · comprehension in `profiles/ZHAO.md` · tasked by PROME packet 2026-07-05 (Will-approved, relaying ZHAO's reactivation ask #2)
**Verdict: L3 (Conf H), provisional-L4 — first scan ever** (came off the dormant/unscanned list; reactivated 7/4 after ~2.5mo). The 7/4 self-rehab is high quality (STATUS rewrite, boot.py staleness guard, exemplary NEXUS_BRIEF, clean ZHA-08 falsification-per-stated-criterion). **L4 is gated on consumption evidence, not structure** — the LIQUID outbox is written-awaiting-route and the brief is 3 days old; one session post-reactivation can't score "signals flowing" (PAT-028/PAT-034 sequencing). Expect L4 in 2-3 sessions if the loop fires. The architecture gap is a **pre-dormancy rotted layer in CLAUDE.md** (6 drift instances) + the missing fleet-norm files ZHAO itself listed.

| § | Blueprint section | ZHAO current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 2 | Convergence matrix | Titled, scored, 11 vectors 5-pt, total 27/55 + concentration note — rescored 7/4 | ✅ | conformant | Optional: Independence col (the standard sweep handle). CLAUDE.md's stale "10 vectors / 34/50 CRITICAL" note → fix in drift cluster below | 3 |
| 4 | Invalidation / exit | Thesis-kill (2-print/3-print counts) + falsification tripwires + per-prediction Invalidation col + TRADE 5-session exits | ✅ | conformant (adapted) | None — print-counting fits monthly TIC data; session counts N/A | 0 |
| 7 | Staleness discipline | **boot.py = exemplary mechanism** (14d/21d bars, TIC-release-watch computing whether a newer print *should* exist, catalyst docket, VX age scan) + KB Stale_By + STATUS self-flags | ✅ | conformant (exemplary) | None — candidate *fleet pattern*: the TIC-release-watch "should a newer print exist?" check generalizes to any scheduled-release domain (BLUEPRINTS §8 note candidate) | 0 |
| 6 | Cross-agent routing | Route-matrix (7 conditions) + NEXUS_BRIEF w/ RED counter-frame + WAITING-FOR + outbox w/ honest "awaiting PROME route" state | ✅ | conformant (brief = exemplary) | MAIL SYSTEM section is broken text → drift cluster below | 1 |
| 1 | Thesis structure | 2-anchor demand-hole frame + Belgium-direction methodology + growth-vs-capital-account decoupling — all substantive, but living in STATUS + CLAUDE with **no thesis/ dir, no version stamp** | ✅ | missing handle/structure | Stand up `thesis/THESIS.md` (v1.0 = the Jul-4 re-frame + Belgium methodology moved from CLAUDE) — ZHAO self-identified; fleet norm 11/21 | 2 |
| 5 | Predictions | 10 made / 2 resolved, Invalidation col, confidence-move audit trails | ✅ | missing build | Light `PREDICTIONS_ARCHIVE` + scoreboard + failure-synthesis: ZHA-08 (falsified) and ZHA-09 (likely-missed) both sit un-post-mortemed — the Gulf-leg miss is exactly the lesson-material the OTTO/BRENT pattern feeds back | 2 |
| 3 | Thresholds | Durable table exists in CLAUDE **but its `Current` column rotted** (TIC $683.5B vs live $651.1B; HIBOR "AT THRESHOLD" vs live EASED) — contradicts ZHAO's own no-stale-copies rule | ✅ | correctness | **Drop the `Current` column entirely** (values live in STATUS — the split done right), fix HK-AB threshold inconsistency (<$40B vs <$45B) | **1** |
| 8 | BOTTOM LINE | Substance present mid-doc (STATUS L22 "Bottom line:") — no trailing labeled handle | ✅ | missing handle | Move/duplicate as trailing `## BOTTOM LINE` (2-4 sentences) — the standard quick win | 1 |

### The CLAUDE.md drift cluster (one fix-pass, ZHAO-lane — all verified in-file 7/7)
| # | Item | Detail |
|---|---|---|
| D1 | `domain/sources/` ×2 (L47, L181) | Dir doesn't exist (the PROME-flagged bug). Point at `sources/` / `archive/` |
| D2 | KEY THRESHOLDS `Current` col (L105-110) | Stale by 2 regimes — §3 above. Highest-value single fix |
| D3 | CONVERGENCE MATRIX note (L126) | "10 vectors… 34/50 🔴 CRITICAL" vs live 11 / 27/55 🟠. Drop the numbers, point at STATUS |
| D4 | MAIL SYSTEM section (L136-150 + L183) | Literal "removed" scrub artifact ×2, HERMES (retired), PROTOCOL.md/RECEIPT.md (don't exist). Rewrite to the live WALTER-lane + outbox reality |
| D5 | PAT-031: SPAWN 1b bare invocation | Wrap: `(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python AGENTS/ZHAO/scripts/boot.py)` — **preserve the venv interpreter** (yfinance) |
| D6 | TRADE.md banner rationale | DAEDALUS-authored 7/4 banner says "ZHAO dormant" — reactivated same day. Freeze stays (Mar-9 four-anchor content, superseded; no position); reword rationale to "superseded content / no active position" |

### Fleet-norm absences (all 6 self-identified gaps VERIFIED absent; build-on-need, not urgent)
MEMORY.md (16/21 have) · MAINTENANCE.md (8/21) · thesis/ + PREDICTIONS_ARCHIVE (§1/§5 above) · board_log.tsv (tie to WALTER consume-loop rollout — **PROME/WALTER's call whether ZHAO joins**, not a ZHAO unilateral) · domain/ (don't build — fix the reference instead, D1).

### The queue
1. **FLEET_MAP row + dormant-list flip + this card + task-packet** (DAEDALUS own files + sanctioned packet) — DONE this session.
2. **ZHAO next session:** D1-D5 drift cluster + §8 BOTTOM LINE handle (~30 min, all own-file) + D6 banner reword.
3. **ZHAO following sessions:** §1 thesis/ graduation + §5 ARCHIVE/scoreboard (post-mortem ZHA-08/09 while fresh) + inbox backlog spawn (3 stale + 2 fresh items, its own STATUS Next-5).
4. **DAEDALUS watch:** consumption evidence for the L4 re-grade (LIQUID absorption read + NEXUS brief-read); Korea/SAM one-figure reconciliation at next SAM firming; VX_HISTORY revive-or-freeze (ZHAO's call).

> **DO-NOT-TOUCH (profile §5):** Belgium-direction methodology (signature asset — D2/D3 fixes must not simplify it); boot.py venv requirement + TIC-watch regex dependency on VX-ZHAO-1.02's Source cell format; KB enum/SCHEMA/VOCABULARIES discipline; prediction Notes audit trails; unfreeze TRADE only on a concrete position re-emerging.
