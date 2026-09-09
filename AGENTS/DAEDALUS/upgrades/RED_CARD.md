# Upgrade Card — RED (read-only re-verification, no agent files touched)

> **Current receipt queue (2026-09-08):** `runs/2026-09-08_INBOX_DISPOSITIONS.md` + current FLEET_MAP row. This card’s old section table remains historical; newly verified closures and explicit deferrals are in the receipt record.

> ✅ **CLOSED/SUPERSEDED 2026-07-22 (self-sweep fix-batch, Will-approved):** the 97-item backlog DRAINED 7/10 (`a6d6b745`), NEXUS_BRIEF created, FLOW.tsv consciously FROZEN 7/5. Remaining = 2 optional labels. Current truth = FLEET_MAP row + `upgrades/PRODUCTION_REVIEW_2026-07-22.md`. States below are HISTORICAL.

**By:** DAEDALUS · **Date:** 2026-07-04 · **Class:** Utility (adversarial analysis — thesis stress-testing, counter-evidence, confirmation-bias detection)
**Method:** fast-follow promotion of `UTILITY_FIRMING_2026-07-03.md` into DAEDALUS's durable per-agent format, **re-verified live against RED's current files** (not just the firming doc) · graded vs `BLUEPRINTS/utility-agent.md` (the floor; NOT `market-agent.md`) · comprehension in `profiles/RED.md`
**Verdict: L4 (conf H), firmed 7/3, RE-VERIFIED IN-FILE 7/4 — no regression.** RED is **conformant or exemplary on all 8 floor sections** post-bundle; its calibration loop (predictions + challenges ledger) is genuinely live, not named-but-unbuilt. The one open item is **operational, not structural**: the new §5.5 WALTER-intake handle is installed but has never run — a 97-file backlog (was ~71 at bundle time) sits unprocessed because RED hasn't booted since 7/3. Nothing new is proposed here beyond what 7/3 already queued; this pass **confirms the bundle landed** and **flags the growing backlog** as the thing to watch.

**↳ 7/3 bundle — re-verified IN-FILE, not re-applied (all four confirmed present, quoted line ranges in `profiles/RED.md` §6):**
- ✅ §2 CONTRACT block — `CLAUDE.md` L20-27.
- ✅ §8 labeled BOTTOM LINE — `STATUS.md` L135-137.
- ✅ §5.5 WALTER consume-step (cwd-proofed) — `CLAUDE.md` L49-52.
- ✅ HERMES-vestige fix — `OUTBOX.md` L3.

---

## Section grade — one row per `utility-agent.md` floor section (+ DARWIN guard, + role-ceiling)

| § | Blueprint section | RED current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 1 | **Header + IDENTITY** (class, role, no-overlap, File>verbal) | `CLAUDE.md` IDENTITY + "Role in Network" one-liner; class=Utility stated implicitly ("You do NOT own any domain data. You do NOT generate original research."); `#1 RULE` = File>verbal, explicit and bolded | ✅ APPLIES | conformant | None material. *(Optional polish: an explicit "where-it-sits/no-overlap" table like ORACLE's — low value; the prose already states it clearly.)* | 0 |
| 2 | **THE CONTRACT** (produces/consumed-by/proof) — *the defining handle* | ✅ **APPLIED 7/3.** `CLAUDE.md` L20-27: PRODUCES (steelman→honest odds + formal challenges), CONSUMED BY (PROME via OUTBOX, domain agents via challenges/, Will via PROME synthesis), PROOF OF CONSUMPTION (qualitative — routed packets + CONVERGED dialogues, e.g. SAM v1.6) + explicit PAT-028 ceiling note for un-instrumentable decision-shifts | ✅ APPLIES | **✅ APPLIED 7/3** (was missing-handle) | None — verified in-file 7/4, content matches the firming doc's proposal exactly | 0 |
| 3 | **Role rubric** (explicit, consistently applied — L3 gate) | `thesis/FRAMEWORK.md` (67 ln): Analytical Hierarchy (6 principles: steelman-first → independence test → market-price test → counter-signal weight → falsification-over-confirmation → timeline discipline), Competing Hypotheses Method, Network Unanimity Protocol, Assessment Scale | ✅ APPLIES | conformant (exemplary) | None — thin but exact; visibly applied every session (S21b Unanimity-Protocol residual hunt, S20 six-agent sweep) | 0 |
| 4 | **Structured record (logging)** — valid, accruing, class-aware (L2 floor) | `workbook/`: KB (53 rows), VX (25, RED-unique bull/bear+Flip_If), ML (94, append-only findings), CHALLENGES (42, RED-unique, cross-linked, resolution-disposed), PREDICTIONS (19, network-standard, 7W/9C/3A), FLOW (7, RED-unique break-pathway), VX_HISTORY (60, audit trail) | ✅ APPLIES | conformant (exemplary) | None — best-in-class utility logging per FLEET_MAP's own note. *(FLOW.tsv staleness is a separate L4→L5 item below, not a schema gap.)* | 0 |
| 5 | **Standing disciplines** (boot↔closeout symmetry + Δ-discipline + cwd-proof, PAT-031) | `CLAUDE.md` SPAWN PROTOCOL: BOOT (0-9a) ↔ WRITE-BACK (W1-W10) explicit read→write pairings, live-event override, Doc-Mirror table (canonical→display, 4 rows); every counter-signal weight carries an as-of date; `boot.py` + `ledger_staleness.py` + the new §5.5 glob/`git mv` are ALL wrapped in `cd "$(git rev-parse --show-toplevel)"` | ✅ APPLIES | conformant (exemplary) | None — cwd-proof CLEAN across every runnable invocation, confirmed by FLEET_MAP's "cwd-proof CLEAN" note and this pass's direct read of the boot steps | 0 |
| 6 | **Cross-agent routing** (route-matrix + NEXUS_BRIEF-equiv writeback + crisis-only outbox) | `OUTBOX.md` (PROME-facing) + `challenges/` (domain-agent packets) + `/BOARD/` §1.5 scan (network-wide) + **`inbox/WALTER/` §5.5 delivery lane (NEW 7/3)** — per-recipient, distinct from the BOARD scan | ✅ APPLIES | **handle present, substance UN-EXERCISED** (a fresh flavor: not missing-handle, not missing-substance in the blueprint sense — the handle is installed correctly but has literally never run) | **Not a DAEDALUS edit** — this is RED's own next-boot job. Nothing to fix in the file; flag that **97 files (was ~71 at bundle-apply time) now sit unprocessed** and `board_log.tsv` doesn't exist yet. Will self-resolve on RED's next boot. | **1 (operational, owner-side)** |
| 7 | **AUTHORITY & SAFETY** (state read-only boundary if no write power) | CONTRACT block states explicitly: "RED holds NO cross-fleet write power — it flags via `OUTBOX.md`, never edits another agent's files" | ✅ APPLIES | conformant | None. *(7/3 firming doc's "labeled read-only-boundary handle" suggestion is effectively already satisfied by this CONTRACT-block sentence; a separate heading would be cosmetic.)* | 0 |
| 8 | **BOTTOM LINE** (required; STATUS under cap) | ✅ **APPLIED 7/3.** `STATUS.md` L135-137, labeled, synthesizes RED's own S21/S21b header (HOLD 69/56) + explicit "refresh at next boot" note. STATUS is 141 ln, well under the 200-line cap | ✅ APPLIES | **✅ APPLIED 7/3** (was missing-label; content pre-existed as an unlabeled footer) | None — verified in-file 7/4 | 0 |
| — | **DARWIN guard** — *KB/VX/FLOW/CHALLENGES/PREDICTIONS* | RED legitimately owns these as **adversarial-flavored** schema: VX = counter-evidence vectors w/ explicit Bull_Wt/Bear_Wt + Flip_If (not a thesis KB); FLOW = break-pathway/cascade-failure tracking (not a convergence matrix); CHALLENGES = formal-dispute ledger (RED-unique) | N/A by design | **N/A-by-design (PAT-030)** | None — do NOT DARWIN-strip or generic-ize toward plain-utility shape; this schema IS the role. `registry/FALSIFICATION_TRIGGERS.tsv` (WALTER's hard auto-fire surface, 7 rows) is correctly kept separate from RED's own `docket/WATCHLINES.tsv` (soft display, 12 rows) — never merge or cross-populate | 0 |
| — | **Role calibration loop** (ceiling — blueprint's RED row: "steelman/odds hit-rate") | `workbook/PREDICTIONS.tsv` (7W/9C/3A, reconciled repeatedly — MEMORY's Calibration Record shows RED catching its own prior miscounts 3× over) + `workbook/CHALLENGES.tsv` (RESOLVED/RESOLVED-CONVERGED/VINDICATED dispositions) + `VX_HISTORY.tsv` (strength-change audit trail) | ✅ APPLIES | conformant (exemplary) | None — this is a genuinely **live, accruing, self-correcting** truth-loop (unlike ORACLE's named-but-unbuilt Brier gap). The rigor of RED's own reconciliation history (S17's mechanical-scan-beats-vigilance catch) is itself evidence the loop works | 0 |

**Gap-type tally:** 6 conformant (3 exemplary: §3/§4/§5, plus the role-calibration-loop row exemplary) · 2 ✅-APPLIED-7/3 (§2 CONTRACT, §8 BOTTOM LINE — now conformant, were missing-handle) · 1 handle-present-substance-unexercised (§6, operational not structural) · 1 N/A-by-design (DARWIN guard).

---

## Separately — the real L4→L5 work (operational/staleness, not section-handle gaps)

| Item | Why | Net-new vs 7/3 firming | Effort |
|---|---|---|---|
| **Run the new §5.5 WALTER-intake for the first time** | The handle is installed and cwd-proofed, but RED hasn't booted since the 7/3 17:32 bundle commit — `board_log.tsv` doesn't exist, `inbox/WALTER/processed/` is empty. The backlog described as "~71 files" at bundle-apply time has grown to **97** (WALTER kept routing through 7/4). This is RED's own operational catch-up, not a DAEDALUS edit | **net-new observation** (not in the 7/3 firming doc, which pre-dates this growth) | S (RED's own next boot; per CLAUDE.md's own guidance: read ACTION items first, bulk-dispose INFO ccs) |
| **`workbook/FLOW.tsv` freeze-vs-refresh call** | Last touched 2026-04-07 (~3 months). Per 7/3 disposition this is explicitly **RED's own boot-9a `ledger_staleness.py` call, NOT silent-rot** — but worth a live check of whether that script has actually been surfacing the alert each session and RED has been consciously not-touching it (legitimate freeze) vs. the check going unnoticed | carried from 7/3 (unresolved, unchanged) | S (verify, then freeze-banner or refresh) |
| **`SCRATCH.md` push-state line refresh** | Still reads "6 unpushed commits... push deferred (Will-coordinated)" — `git status` now shows a clean tree in sync with origin (push-train swept it 7/2-7/4). Cosmetic only; self-heals at RED's next W5 rewrite | carried from 7/3 ("ephemeral + moot") | trivial (self-resolving) |
| **No-overlap table + labeled read-only-boundary handle** | §1/§7 optional polish flagged in the 7/3 firming doc's "remaining minor" list — both are already substantively covered inline (prose no-overlap statement, CONTRACT-block read-only sentence); a dedicated heading is cosmetic | carried from 7/3, unchanged, low value | XS |
| **Zero-YEYOU clean bill** | L5 requires it | n/a (YEYOU-side) | n/a |

---

## The queue (quick wins first)

1. ✅ **APPLIED 7/3, RE-VERIFIED IN-FILE 7/4.** **§2 CONTRACT block** — `CLAUDE.md` L20-27, exact match to the firming-doc proposal. Closes the biggest structural gap.
2. ✅ **APPLIED 7/3, RE-VERIFIED IN-FILE 7/4.** **§8 labeled BOTTOM LINE** — `STATUS.md` L135-137, sourced from RED's own S21b header.
3. ✅ **APPLIED 7/3, RE-VERIFIED IN-FILE 7/4.** **§5.5 WALTER consume-step, cwd-proofed** — `CLAUDE.md` L49-52. *Installed correctly but **UN-EXERCISED*** — see item 5 below, the actual next action.
4. ✅ **APPLIED 7/3, RE-VERIFIED IN-FILE 7/4.** **HERMES-vestige fix** — `OUTBOX.md` L3.
5. **RED's own next boot: drain the WALTER inbox backlog** (97 files and growing) using the now-installed §5.5 step. *Not a DAEDALUS action — flagging because the gap is widening daily and is the single biggest live discrepancy between "designed" and "operating."*
6. **FLOW.tsv freeze-vs-refresh** — RED's own boot-9a ledger call; carried unresolved from 7/3, ~3mo stale now.
7. **SCRATCH push-line** — cosmetic, self-heals at next W5 rewrite; no action needed.
8. **No-overlap table / read-only-boundary heading** — optional §1/§7 polish, low value, carried from 7/3.

> **Note for application:** this pass **touched no RED files** — pure re-verification. All four 7/3 bundle items are confirmed live in RED's current file state (commit `c5867d57`, `git status` clean, no RED-authored commits since). The only drift found since 7/3 is the WALTER-inbox backlog growing from ~71 to 97 files, which is expected given RED hasn't booted — not a regression, just the natural consequence of a still-idle agent with an always-on delivery lane feeding it. Full detail → `profiles/RED.md`.
