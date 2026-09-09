# Agent Profile — FERT

**Built by:** DAEDALUS · **Date:** 2026-09-05 (**FIRST BUILD** — owed "at the first firming touch"; that touch was 2026-08-17)
**Method:** solo full-tree read + `boot.py` RUN (rc=1) + the L3 gate re-measured at `PREDICTIONS.tsv`
**Sources read:** `CLAUDE.md` (189 ln) · `STATUS.md` (126) · `TRADE.md` · `workbook/` (5 TSV + `EXIT_PROTOCOL.md`) · `boot.py` · `archive/CLAUDE_2026-03_SUPERSEDED.md` · `board_log.tsv` · inbox/outbox
**Staleness:** event-keyed (next World Bank Pink Sheet / named trigger) or **>21d** → checkpoint **2026-09-26**

> **Receipt update 2026-09-08.** Before this update: `archive/2026-09-08_INBOX_PROFILE_BEFORE_IMAGES.json` (verbatim bodies + SHA-256). Evidence and dispositions: `runs/2026-09-08_INBOX_DISPOSITIONS.md`.

---

## 1. Identity
**Fertilizer supply / price / policy → food-CPI transmission → CF Industries positioning.** Market class, **EVENT-DRIVEN SPECIALIST** (wakes on named triggers, no standing cadence). **L3 (H), graded 2026-09-08.**
**Re-chartered 2026-08-16, Will-ruled**, built by DAEDALUS against `BLUEPRINTS/market-agent.md`. The March-2026 charter is SUPERSEDED (`archive/CLAUDE_2026-03_SUPERSEDED.md`, whose banner lists the three verified load-bearing defects that caused the re-charter).

**⭐ The tagline IS the desk's control:** *"Benchmark + unit + date on every price cell, or the cell is wrong."* This desk was **re-chartered over a basis mislabel**, and its charter is built around not repeating it: *"'urea' is NOT one price. DTN retail $/ton ≠ NOLA barge $/st ≠ India CFR $/mt ≠ Egypt FOB futures $/mt — levels differ by hundreds of dollars between benchmarks."*

## 2. File anatomy
| File | Holds |
|---|---|
| `CLAUDE.md` (189 ln) | charter · **the SPAWNED-MODE BOOT CARD** (§4.1) · benchmark semantics · the potash clause |
| `STATUS.md` (126 ln) | live state, rebuilt from primaries at the 8/17 session |
| `workbook/EXIT_PROTOCOL.md` ⭐ | dated kill rail — `re-derived 2026-08-17`, **next mandatory 2026-11-15** |
| `workbook/TRIGGERS.tsv` | the named triggers this desk wakes on (T-*, e.g. T11 World Bank Pink Sheet) |
| `workbook/PREDICTIONS.tsv` | **12 rows: 10 resolved + FERT-11/12 OPEN** — verified 2026-09-08 |
| `workbook/KB.tsv` · `FLOW.tsv` · `VX.tsv` · `SCHEMA.tsv` | record + transmission + vectors |
| `boot.py` | trigger-due scan (rc=1 = something due) |
| `TRADE.md` · `archive/` · `board_log.tsv` | CF positioning surface · superseded charter · board record |

## 3. Per-dimension
| Dimension | Where | Form |
|---|---|---|
| Thesis | `CLAUDE.md` + STATUS | supply/price/policy → food-CPI → CF |
| Convergence | `STATUS.md` Live Vectors + `workbook/VX.tsv` | Standing eight-vector matrix, universal score /5 and Independence column; exercised 9/2 and 9/5. The prior trigger-only description was wrong. |
| Exit / kill ⭐ | `workbook/EXIT_PROTOCOL.md` | **dated re-derivation + a dated NEXT-MANDATORY (2026-11-15)** — a rail that schedules its own re-grade |
| Predictions | `PREDICTIONS.tsv` | full schema incl. `Resolve_By`, `If_Falsified_Action`, and a **STATE_VOCABULARY Class-3 enum declared in the file header** |
| Routing | `TRADE.md` + outbox | GATE-FERT-G3/G5 graded and routed to PROME 9/2 |

### §3b. Invalidation-surface inventory
| Surface | Kills / flips | Stamp | Fired-state |
|---|---|---|---|
| `workbook/EXIT_PROTOCOL.md` | the supply→CPI→CF chain | in-content `re-derived 2026-08-17`; **next mandatory 2026-11-15** | per-leg |
| `workbook/TRIGGERS.tsv` | wake conditions | per-row | GATE-FERT-G3/G5 graded NOT FIRED 9/2 |
| `PREDICTIONS.tsv` | individual calls | `Resolve_By` + declared enum | HIT / MISS / VOID / OPEN / STUCK |

## 4. Deviations — two worth copying

**4.1 — The SPAWNED-MODE BOOT CARD solves a real harness problem.** `CLAUDE.md` opens with: *"⚡ SPAWNED-MODE BOOT CARD (coordinator spawns — **your CLAUDE.md did NOT auto-load**)"*, then restates the four things a spawned session must know as **full repo-root paths**. Claude Code auto-loads `CLAUDE.md` by walking up from the launch dir, so a coordinator-spawned session in another cwd **never sees the charter** — and this desk noticed and put the recovery instructions in the file's first screen, where a session that *does* load it will pass them on. **Portable to every desk PROME spawns.**

**4.2 — Scope and guard registered in the SAME EDIT.** The potash clause (Will-ruled 8/18, triage depth) states its own design rule: the benchmark row is registered *"in the same edit as its scope, deliberately: **scope-first, guard-later is exactly the failure**"* — on a desk re-chartered over a basis mislabel, and with potash flagged as **"a FOURTH benchmark family arriving on a desk re-chartered over a basis mislabel."** A desk naming its own elevated risk while accepting new scope is the behaviour I would want everywhere.

## 5. Findings

**F-1 — CLOSED-VERIFIED 2026-09-08.** FERT-11 and FERT-12 are OPEN with Resolve_By 2026-10-09 / 2026-12-02, grading bases and falsified actions. Together with the existing graded book, standing matrix and dated exit rail, these meet L3. The separate policy question about requiring an OPEN count remains at the September 14 ladder sitting; registering two rows does not settle that incentive question.

**F-2 — prior T11 lapse CLOSED-VERIFIED.** The September 5 owner session checked the edition; TRIGGERS T11 now points to 2026-10-02 and requires verification before grading. Other due triggers remain the owner/PROME lane, not covered by this closure.

**🟢 F-3 — the desk grades its own gates NOT FIRED and says so.** GATE-FERT-G5 and G3 both graded **NOT FIRED** and routed to PROME on 9/2, with the phosphate approach rate reported. Publishing a clean negative against a registered gate is what keeps a trigger set honest.

## 6. DO NOT TOUCH
1. **"Benchmark + unit + date on every price cell."** This is the control the desk was re-chartered to install. ⛔ Never quote a fertilizer price without its benchmark — DTN retail, NOLA barge, India CFR and Egypt FOB differ by **hundreds of dollars**.
2. **Potash is TRIAGE DEPTH ONLY** (Will-ruled 2026-08-18) — log + flag PROME, **no deep-dive**. It is a *fourth* benchmark family; treat every potash price cell as a mislabel risk until its benchmark row is cited.
3. **The SPAWNED-MODE BOOT CARD must stay at the top of `CLAUDE.md`.** Moving it below the fold defeats its purpose.
4. **The VOID rows (FERT-02, FERT-06) are verdicts, not gaps** — "unfalsifiable-as-written" and "broken-as-instrument" are real gradings of inherited predictions. Never re-open them as unresolved.
5. **`EXIT_PROTOCOL.md`'s next-mandatory date (2026-11-15)** is a rail that schedules its own re-grade. Keep the dated form.
6. **The superseded March charter's banner lists three verified load-bearing defects** — that is the re-charter's evidence base; do not archive it further away.

## 7. Receipt closure and remaining scope
- G3/G5 ratification verified in PROME/GATES.tsv; matrix exercise verified in STATUS. The three carried questions are discharged.
- The old “4 ledgers +150d post-session” claim was unverified and is withdrawn. Do not turn its ambiguous wording into a new 2027 audit obligation.
- L4 not adjudicated in this bounded receipt read; TRADE remains deliberately frozen with a dated re-look. No request to create capital exposure.
- Profile day checkpoint remains 2026-09-26; this is a targeted update, not a new full-profile clock.
