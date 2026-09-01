# 2026-09-01 — FALCON → PROME: combined-touch return (Tier 1, prome-98 spawn ~17:40 ET)

**Trigger:** WALTER `SIG-W-20260901-005` (IMMEDIATE, rule-6b doorbell). **Clock:** `date` 2026-09-01 ~17:4x ET. **$0 moved. No gate STATE edited — PROME flips.**

## 1. Adjudicated / re-marked — on which letter and basis

| Item | Verdict | Letter / basis | Artifact |
|---|---|---|---|
| **GATE 1 / FAL-01-class (production/export-infra hit)** | **FIRM-NEGATIVE on the 9/1 record** [VERIFIED at CENTCOM-relaying primaries; target list INFERRED — Iranian-media only] | **CENTCOM's own 12:00 ET release NAMES NO TARGETS** (*"striking IRGC targets in Iran"* after *"attempted attacks by the IRGC against commercial shipping… and against American service members"*; Stars & Stripes: *"CENTCOM did not reveal what the targets were"*). ⇒ **The Iranian-media list (Bandar Abbas · Jask · Chabahar · Konarak · Minab · Sirik · Qeshm · Jiroft airport) is the ONLY list in existence and is the one adjudicated** — all ports/bases/airport/IRGC sites. Negative rests on three absences: no US energy claim · no Iranian energy allegation (the side with every incentive) · no operator/NIOC statement or imagery. **Stamp: adjudicated 9/1 ~17:4x ET; RE-ADJUDICATE on any CENTCOM target list / BDA.** | STATUS 9/1 block item 1 · `KB-FALCON-116` |
| **GATE 2 / D-indicator #6 / `VX-FALCON-SUNK-01` (mine detonation on a hull / hostile sinking)** | **NOT FIRED** | IRGC "supertanker hit two mines" (Tasnim 8/31 ~04:37Z) = **CENTCOM-denied disinformation**, unnamed vessel, no UKMTO match, ~15h older than the real hits. *Sidr* / *Senegal Prosperity* = projectile hits, crews safe, no fire/sinking. **Confirmed hostile-action total losses = 1.** | false-fire register row 9/1 · `KB-FALCON-119` · `VESSELS.tsv` VI-2026-0020/0021 (`KB-FALCON-117`) |
| **Kinetic-RESUMPTION re-mark (owed since 8/31)** | **MADE: B 5 (hold) / C 35→30 / D 60→65. Convergence 43/50 UNCHANGED; P 23 / K 15 / R 13 unchanged.** | `workbook/EXIT_PROTOCOL.md` §2–3: **no D→70+ indicator fires** (#3 tempo NOT nightly — two waves in three days = campaign; target set NOT into energy; no crude offline; no sinking/mine; no US fatality; bypass gauge UNGRADED tonight; WC-Saudi war-risk no print). But the 7/30 D=60 was priced *in terms* off "ONE wave, not a nightly campaign" — that condition lapsed. Composite can't move: every kinetic vector already at 5 (the under-read flagged 7/30). Held loosely; flagged to Will/PROME as on 7/30. **No OPEN prediction keyed on the pause** (FAL-04 closed 8/20; FAL-05 still OWED, base rate first). | STATUS 9/1 block item 4 · `KB-FALCON-120` · EXIT_PROTOCOL §2 marks line + §3 #3 status |

## 2. GATES sync PROME must do — `GATE-FALCON-001`

- **Consumer 2026-09-01: CONFIRMED / CONSUMED by the owner at this touch.** Leg read: **leg 1 FIRED 7/23 — stands · leg 2 OPEN, NOT FIRED** (the 8/31 Khasab hits are **HORMUZ** theater; leg 2 grades **Bab** tanker transits on TankerMap like-for-like; no fresh enforcement-attributable Bab step-down; PortWatch Hormuz 8/23 = 3/88 DEEPENING, rc 0, lagging corroborator only) **· leg 3 FIRED 8/15 — stands.** Gate stays **LIVE**.
- **Proposed new cell text (state col):** `LIVE — leg 3 (Yanbu) FIRED 8/15; leg 2 open (owner re-read 9/1: NOT FIRED — 8/31 Khasab VLCC hits are Hormuz theater, not Bab); 8/17 discriminator R3 = HOLD; PortWatch chokepoint6 impeached · hist→GATES_STATE_HISTORY`
- **Proposed last-adjudicated:** `2026-09-01 (owner combined touch abdf4efe5: legs 1/3 FIRED stand, leg 2 NOT FIRED; 9/1 consumer CONSUMED)`
- **Proposed `review_by`:** `2026-09-08 | RE-DATED at owner's 9/1 consume: next tanker-weekly ~9/8, or immediately on any Bab-theater enforcement event` (owner-confirmed 2026-09-01).
- Canonical letter home unchanged: `AGENTS/FALCON/domain/FRESH_LEG_BASELINE.md` (9/1 leg-state line appended there).

## 3. DOCKET dispositions (FALCON-side)

- **Line 10** (FALCON leg-3 sweep #2, 8/19–21, PENDING/COVERED:FALCON): remainder was the w/c-8/10 Yanbu print — **still UNPUBLISHED (press relay, not a release; 3rd overdue week class).** Owner disposition: **CLOSE as RESOLVED-NEGATIVE (no print will relay; leg 3 already FIRED 8/15 on w/c-8/3; FAL-04 graded 8/20; discriminator consumed 8/20)** — PROME tombstones; no further FALCON work on this row.
- **Line 229** (Iran–Oman permanent-route window 9/25–10/26): unchanged, still pending; US acceptance now materially harder after wave 2 (WALTER ADD#23) — annotate if you wish; no FALCON action.
- No other FALCON-owned open rows found (`grep FALCON PROME/DOCKET.tsv`).

## 4. ⚖️ Will item — ONE
**⚖️ Mark move for Will's eye (not a gate, not a trade): FALCON re-marked D 60→65 / C 35→30 on the campaign.** Standing "marks held loosely, my call, flagged" convention (7/30). Nothing to approve unless Will wants the desk's marks Will-gated; no threshold, gate state or capital path moved.

## 5. Instruments / owed / counts
- `bypass_watch.py` **CRASHED** (IndexError — one PortWatch port series returned EMPTY; rc-2 class) ⇒ D-indicator #7 **UNGRADED tonight**, last good 8/31 91,834 t/d vs 26,208 floor. Fix owed (empty-series guard).
- WARRISK: 5/5 rows EXPIRED +29d; registered falsifier (WC Saudi 0.1%) at 40d; no open-source print newer than 7/22–23. Data clock NOT advanced.
- `hormuz_transit_watch` rc 0 (8/23 = 3/88 DEEPENING, 9d lag). `baghdad_watch`: 2 generic alerts (9/1 security alert; 8/29 Level-4), 0 REVIEW.
- R1 corrections: `COR-20260828-01` receipted **APPLIED** (`registry/corrections_receipts.tsv` created).
- STATUS read-cap: two 8/20 blocks archived → `domain/sources/STATUS_archive_2026-08-20_session_blocks.md` (−14.5 KB); **still over 32,550 B — further rotation owed** (7/30 PART 1–3 material next).
- **Inbox: 1/1 drained** (WALTER lane; root inbox empty). `board_log.tsv` row 9/1.
- **Still owed to a full FALCON session:** FAL-05 (base rate first) · remaining STATUS rotation · bypass guard · WARRISK re-pull on any print · 8/20 deferred bundles.
- **Commit:** see the return message (hash verified with `git log -1 --format=%h -- AGENTS/FALCON/STATUS.md`).
