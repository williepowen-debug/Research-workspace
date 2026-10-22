# BUILD RECORD — FERT re-charter · 2026-08-16 · DAEDALUS

**Authorization:** Will-ruled 2026-08-16 (`PROME/proposals/2026-08-16_fert-recharter-RULED.md`); commission = `inbox/2026-08-16_from-PROME_fert-recharter-COMMISSIONED-...md`. DOCKET checkpoint 2026-08-23 — **landed 8/16, 7 days inside the window.**
**Shape:** market-agent blueprint variant · **EVENT-DRIVEN SPECIALIST** cadence (wakes on named triggers; decision tempo weekly-to-monthly, assessment §4c).

## What shipped

| Artifact | Content |
|---|---|
| `AGENTS/FERT/CLAUDE.md` | New charter from scratch. Spine = benchmark discipline (benchmark+unit+date+source on every price cell; 6-benchmark table). Scope: nitrogen + phosphate, China policy as LIVE vector (never a frozen constant), transmission watch as OPEN instrumented question, CF single-name. Exclusions register per PAT-073 ② (potash = NO OWNER flagged · clean-ammonia = NO OWNER · QAFCO damage = OSPREY/FALCON event, FERT owns consequence, March LNG→fertilizer inference marked UNVERIFIED). First-live-session protocol keyed to STATUS's own FROZEN banner (self-spending section). Gates: §5B candidates stay PROPOSALS, base-rate-then-Will; `urea NOLA >$800` do-not-re-register; dormancy = registration event. HERMES-free mail model (carve-out ① direct delivery). |
| `AGENTS/FERT/archive/CLAUDE_2026-03_SUPERSEDED.md` | Old charter `git mv`'d intact with its SUPERSEDED banner (supersession discipline — preserved, not deleted). |
| `AGENTS/FERT/boot.py` | Wall clock · ledger staleness (marker-contract, see regression below) · predictions-due (`Resolve_By`) · triggers-due (`Next_Check`). Exit 0/1/2. Pure stdlib (PAT-103 n/a). |
| `workbook/PREDICTIONS.tsv` | Header re-cut while EMPTY (verified header-only — the March calendar never entered the ledger): + `Resolve_By` (boot-scan key) + `If_Falsified_Action` + Class-3 token enum in header comment (checklist #15). |
| `workbook/TRIGGERS.tsv` | NEW wake register, 10 rows seeded from assessment §2d/§4a with [EST] marks preserved; two-clock header (PAT-044). An event-driven agent with an empty trigger register can never wake — seeding is build-lane wiring, dates re-verified at first live session. |
| `TRADE.md` | Untouched — already correctly FROZEN 2026-07-04; disposition = first-session task 6. |

## Capable-case record (★ no guard ships unverified — all watched)

| Run | Case | Watched result |
|---|---|---|
| 1-2 | Real state | Leg 1 fires ⚠️ on the 4 genuinely stale March ledgers (truthful REVIEW — drives first-session work); legs 2-3 print null-with-scope (`none due (triggers: 10 data row(s) scanned on Next_Check)`) |
| 3 | Synthetic OPEN prediction past `Resolve_By` + trigger past `Next_Check` | Both `DUE:` lines printed; REVIEW verdict. Drill rows removed after |
| 4 | TRIGGERS.tsv absent | `MISSING — the register this leg certifies does not exist` + `a leg FAILED` (rc-2 path) |

## ⚠️ Regression found while building (shared-check contract, MY 8/11 change)

`ledger_staleness.py --trade` has printed an **unconditional scope line** (`trade perimeter: ...`) since my 8/11 CHECK_STANDARD null-states-its-scope hardening. The **WATT/VULCAN/MIDAS boot.py** consumers flag on bare output-nonempty (the 7/31 PAT-074 fix), so **all three boots have printed a false REVIEW on every clean boot since 8/11** — verified live on VULCAN (S2 fresh, verdict still REVIEW). I fixed one guard and broke its consumers; the consumers' contract and the producer's contract changed hands independently. FERT ships the corrected contract: **flag = marker-present (⚠️/🔴), scope lines don't flag.** Trio fix = same one-line edit ×3, **cross-agent → Will/PROME approval required** (proposed in the 8/16 session report). CHECKS.tsv ledger_staleness row updated with the marker-contract note.

## Registration checklist walk (`builds/REGISTRATION_CHECKLIST.md`)

| Row | State |
|---|---|
| 1 ROSTER · 2 root mirror (Will-gated) · 3 AGENTS.md · 4 _INDEX · 5 _NETWORK · 6 five group pages | **PROME at flip** (commission §1.6; enumerated in my confirm packet so the flip pass is complete) |
| 7 WALTER routing | Packet sent this session (`AGENTS/WALTER/inbox/`) |
| 8 FLEET_MAP row · 9 directory regen · 12 `maturity_scan.py` SKIP removal (+ render_directory SPECIAL/DROP check) | **DEFERRED to flip, mine, one pass** — PAT-047 forbids FLEET_MAP before ROSTER; SKIP removal is same-pass-paired with the FLEET_MAP row by its own registration rule. Wake owner: confirm packet asks PROME to packet me at flip; belt = my STATUS Next-actions line |
| 10 peer/parent · 13 parent behavioral registries · 16 sub-agents | N/A (re-charter, no split/parent; the one legacy behavioral trigger — `>$800` — is ruled dead, never in GATES.tsv). 13-inverse checked: no other live surface routes on FERT triggers |
| 11 consumer handoff | CARL already info-packeted by PROME 8/16; WALTER = row 7 |
| 14 content seeding | ② exclusions register in charter (the build's sharpest requirement — potash now an ORPHANED class, flagged) · ① N/A · ③ FILES table role-tense ✓ |
| 15 state-tokens / STRICT_TEXT | Class-3 enum in PREDICTIONS header · Class-6 tokens in charter benchmark rules · banners use canonical FROZEN/SUPERSEDED ✓ |

**Profile:** deferred to first firming touch per checklist deferred-surface note (standard for new builds).
