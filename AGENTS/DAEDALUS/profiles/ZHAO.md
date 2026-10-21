# Agent Profile — ZHAO

> **BOUNDED DELTA 2026-10-21:** named date/event triggers not established as fired on the inspected legs; this is not all-content clearance. Current verified delta: ZHA-18 NO, branch B, graded 10/16; old ungraded claim refuted. GACC August reconciliation and SAFE August reserves/gold remain owed. Reading A branch 2 PASS: TRADE freeze explicitly lasts until a concrete position re-emerges. Profile was wholly refreshed 10/14; do not carry September stale-body claim. Source/evidence: `upgrades/PRODUCTION_REVIEW_2026-10-21.md` and its named reader companion. This annotation supersedes conflicting current-state claims below only on these inspected facts; no whole-profile refresh or grade change is established by the annotation.

**Built by:** DAEDALUS · **Body vintage: 2026-10-14** · **Body:** 2026-07-04 · refreshed 2026-09-05 · **WHOLE refresh 2026-10-14** (queue slot 10/12, done +2d)
**Method:** Mode-A fan-out, 2 readers over 2 clusters (R1 operating layer · R2 evidence + consumption), synthesized here. Raw tables, ranked route lists and every not-read limit live in `runs/2026-10-14_ZHAO_PROFILE_READER_REPORTS.md` (index → R1, R2). Prior body verbatim: `profiles/_prior/ZHAO_2026-09-05.md`.
**Staleness:** refresh at the next post-TIC session that changes the matrix, or >45d → checkpoint **2026-11-28**.

> **Grade input for PR#8 (10/15): L4 holds under ratified READING A, on route 2 with a weak condition; route 3 passes in substance.** Detail and the one fix that makes it robust in §6. No promotion or demotion is made by this profile.

---

## 1. Identity
China macro through the U.S.-market lens — **UST demand / capital flows / Korea**. Market class, ACTIVE, **CADENCE WEEKLY** (declared to PROME 9/30, WQ-295; board_log.tsv:12 — ⚠️ not written in CLAUDE.md). Research/signal desk with **no position by design** — stated in NEXUS_BRIEF.md:5 and OPEN_THREADS:3, ⚠️ not in the charter. `TRADE.md` FROZEN 2026-07-04 with an unfreeze condition (§6).
Signature asset: the **Belgium (Euroclear) direction-discriminator METHOD** — the proxy it validated is falsified by ZHAO itself (rho +0.067, n=42, STATUS.md:39; VX-1.09).

## 2. State (2026-10-14)
| | |
|---|---|
| Last session | **2026-10-09** (PROME-spawned, DOCKET L482; `011af3188` on origin). Sessions since 9/05: 9/17 · 9/18 · 9/19 · 9/25 · 9/30 · 10/09 |
| STATUS | 189 ln / **26,235 B = 80.6%** of 32,550 B → 🟡 rotate-tier; 3,451 B to the <70% stop |
| CLAUDE.md | 267 ln / **32,539 B = 11 B under** ZHAO's own self-binding cap (CLAUDE.md:50). Any charter fix must be byte-neutral or follow a rotation |
| Ledgers | PREDICTIONS 18 (6 open) · KB 196 · VX 42 · FLOW 15 · SCHEMA 13 (static) · **VX_HISTORY 5 rows, all 2026-02-13, unbannered** (`--strict` STALE +238d) · `docket/CATALYSTS.tsv` 21 rows |
| Inbox | **9 unprocessed** (4 root MIDAS 10/12 · 5 WALTER lane 10/10–10/14), oldest 10/10 — all after the 10/09 closeout |
| Boot | `boot.py` rc 1 REVIEW, 10 alerts (10/14 run) — ≥2 false (D3/D4) and the 14-day key-figure bar is structurally red on monthly series |
| Archive | 5 STATUS_COLD splits (0902 · 0917 · 0918 · 0918b · 0925) + NEXUS_BRIEF_COLD_20261009 + NEXUS_BRIEF_PIVOT_HISTORY. STATUS:9 pointer skips #5/#6 |

## 3. Per-dimension
| Dimension | Local form | Read |
|---|---|---|
| Convergence | 12-vector matrix, **28/60** computed from rows (STATUS.md:95). Path 28 (9/02) → 29 (9/17, V8 LNG) → 28 (10/09, V5 tripwire) | Current total; ⚠️ header :76 omits 10/09 and several vector As-Of cells are 26–102 days old |
| Exit rules | STATUS.md:104–118 — thesis kill letter + print-counted tripwires | Correct for a monthly-data domain |
| Predictions | 4 graded since 9/05 on registered letters (ZHA-11 YES · ZHA-12 YES · ZHA-17 NO · ZHA-16 NO via declared residual), mean Brier 0.162. ZHA-18 pre-registered 9/18, resolves 10/23 | ⚠️ ZHA-05/07/10 (12/31) have **no live resolving instrument** |
| Falsification | Exercised, in the unflattering direction: property tripwire fired 10/09 and was applied against ZHAO's own read; ZHA-16 VOID declined; Belgium kill leg declared degenerate before the print, re-spec dated 10/23 | Strongest dimension |
| Consumption | Shown at recipients' artifacts (§6) | Stronger than at 9/05 |
| Ledger hygiene | KB enum 100% valid except 1 Group tag (KB.tsv:126 `CHINA`). **Facts land in KB and are not written back** to VX/FLOW/CATALYSTS (KB-162 pattern, recurring) | Weakest dimension |

## 4. Drift since 9/05 — what a cold reader trips on
| # | Item | Where |
|---|---|---|
| 1 | **10/16 August TIC row lacks the letter's rule** that Aug/Sep Belgium prints record SATISFIED-ON-BASE-EFFECT, not as evidence; its note to "register the letter" is stale (done 9/18) | CATALYSTS.tsv:14 vs `reports/2026-09-18_PREREGISTRATION_ZHA-18_august-tic.md` §2, KB-159 |
| 2 | **7 KB Vectors cross-refs point at the wrong VX row**, 2 written 10/09 after ZHAO's own 9/18 audit named the class | KB.tsv:167,168,169,173,176,195,197 |
| 3 | **Write-back gap:** 9/20 LPR (VX-6.06), Sept mfg PMI 50.1 (only in VX-6.12, canonical 6.11 still Aug 49.8), FLOW-02 tripwire fired, FLOW-11 July TIC, FLOW-14 "three clocks" after IEEPA VOID | VX.tsv:27,35 · FLOW.tsv:3,12,15 · CATALYSTS.tsv:16,18 |
| 4 | **Routing claim inverted:** STATUS says 9/25 packets "await PROME routing" (routed 9/25); the **9/30 MOFCOM-1/10 packet has no routed file copy** (content reached recipients only as WALTER SIG-W-20260930-003) | STATUS.md:99,167 · `outbox/2026-09-30_*` |
| 5 | **catalyst_countdown false alerts:** DOCKET leg matches "ZHAO" anywhere and ignores state (RESOLVED L670 fires "SWEEP NOW"; VOID L436 shows upcoming); `DONE` in the priority column counts as fired | catalyst_countdown.py:186–196, 222–232 |
| 6 | **Retired framing on shared surfaces:** "China UST exit (Belgium/Euroclear proxy)" | NEXUS_BRIEF.md:4 · CLAUDE.md:6 (charter :12 retires both) |
| 7 | **NEXUS_BRIEF content-stale under a fresh As-of** (CALIBRATION/SENDING from 8/21; ":81 all three clocks land 11/10" vs :83 VOID) | NEXUS_BRIEF.md:25–85 |
| 8 | **Stacked dated blocks** in STATUS header and BOTTOM LINE, against the desk's own rewrite-the-spine rule — also the cheapest source of the 3,451 B rotation | STATUS.md:4–6, :171–183; rule CLAUDE.md:49,69 |
| 9 | **Local git rules diverge from root:** "when SPAWNED: commit, do NOT push" (not a root-listed exception); non-ff recurrence escalated (root: ordinary traffic) | CLAUDE.md:235, :242 — **PROME/Will word needed before change** |
| 10 | VX rows FROZEN in Notes but live-coloured in Status (6.03 reads RED; it is ZHA-05's resolver) | VX.tsv:23,24,25,28,30 |
| 11 | ZHAO's `_read_tsv` does not skip `#` lines, so ledgers cannot carry the two-clock freshness header; FLOW has no date column | boot.py:94–101 · FLOW.tsv:1 |

**9/05 drift list:** all six items still resolved. One 9/05 "deliberate/fine" note was already false then — boot.py has no in-script catalyst list; it reads `docket/CATALYSTS.tsv` (since 8/21).

## 5. DO NOT TOUCH — carried, re-verified 2026-10-14
1. **The Belgium METHOD + falsification record** (CLAUDE.md:142–189; STATUS.md:39). Do not restore the proxy as a live adjustment.
2. **`boot.py` MUST run under `.venv/bin/python`** (yfinance is venv-only); CLAUDE.md:29's wrap keeps the interpreter.
3. **TIC-release watch parses the data-month from `VX-ZHAO-1.02`'s Source cell** ("Mon YYYY", boot.py:182–187) — reformatting that cell silently breaks boot [3].
4. **KB enum discipline is schema-enforced** (SCHEMA.tsv + VOCABULARIES.tsv); SPAWN 3/3b are load-bearing.
5. **`TRADE.md` freeze banner is DAEDALUS-authored**; wording updates sanctioned, unfreeze needs a ZHAO position (§6 on making that operational).
6. **Confidence-move trails** are deliberate history — now also in machine form in the Confidence cell (`18% [2026-08-21] (was 25% …)`, WQ-112 write 9/18).
7. **NEW — the charter is 11 B under its own cap.** Never add bytes to CLAUDE.md without rotating first.

## 6. Maturity legs (Market class) — PR#8 input, no grade change made here
| Leg | Verdict | Basis |
|---|---|---|
| L1–L2 | **PASS** | `Overall Status` STATUS:7 + BOTTOM LINE dated OCT 9 (:171). **4 accruing ledgers** (KB · VX · PREDICTIONS · FLOW) — the 9/05 "6 accruing" was wrong (VX_HISTORY never accrued; SCHEMA is static) |
| L3 convergence / exits / predictions / falsification | **PASS** | §3 |
| **L4 trade leg — READING A** | **PASS on route 2, weak.** Route 1 FAIL (TRADE body dated 3/09). Route 2: banner TRADE.md:1 "…the freeze itself stands until a concrete position re-emerges" + CLAUDE.md:261 "Unfreeze only if a concrete position re-emerges" — a written condition, but no trigger, owner or detector. WALTER's SIG-W-20261010-004 says Will holds a TLT Oct-16 put (TLT puts were TRADE.md's #1 row) and nothing tests whether that is "re-emerging" (position truth off-repo; not verified). Route 3: consumer half PASSES (below); charter half not literally met (no "no book" line in CLAUDE.md) | Fix (owner): declare research/signal, no book, in IDENTITY and write an operational re-arm — then route 3 passes on the letter |
| **L4 signals consumed** | **PASS, stronger than 9/05** | At recipients' artifacts: HAWK acted twice (KB-HAWK-409/410) · VULCAN CATALYSTS.tsv:10–12 + KB-191 · WATT STATUS.md:29 (channel built on ZHAO's trigger wording) · LIQUID 9/17 session report §④ · BOND KB-BND-339 · HANS ML-HANS-461 · PROME DOCKET L436 voided on ZHAO's finding. Weak: factory-gate correction moved-only at HENRY/MARCO/MIDAS; HENRY no row on IEEPA VOID |
| L5 clean closeouts | **PASS, with hygiene debt** | 3 consecutive dated PROME memos with COMPLETION blocks (9/25 · 9/30 · 10/09), all consumed; NEXUS ordering held. Debt: D-items 4, 7, 8 above |
| L5 current | **PASS** | 5 days at a WEEKLY cadence. ZHA-18 needs a session between 10/16 and 10/23 |

## 7. Findings
**🟡 F-1 — "write it to KB" has replaced "write it where the reader travels."** Seven wrong cross-refs, three stale VX rows, three stale FLOW rows and a P1 catalyst row missing its own rule all share one shape: the fact is recorded correctly in KB and the surface a reader or boot.py actually consults is not updated. ZHAO named this class itself on 9/18 (KB-162) and proposed a check; the check is **ours and unbuilt** (`runs/2026-09-24_CATCHUP_DISPOSITIONS.md:21`, item ②). A desk-local discipline fix will not hold against the next busy session — this wants the semantic cross-ref check.

**🟡 F-2 — STATUS regrowth persists (PAT-055, n=3 at this desk).** Four cold splits 9/17–9/25; back at 80.6% by 10/09. The stacked dated blocks (§4 #8) are the regrowth mechanism this time — the rule against them exists in the charter and is not followed.

**🟢 F-3 — falsification discipline is exemplary.** Tripwire applied against its own read; VOID declined when it would have flattered the record; kill leg declared degenerate *before* the print. Cite as the market-class exemplar for the dated-falsification leg.

**🟡 F-4 — a vague unfreeze condition is a READING-A weak pass, not a fail.** "Until a concrete position re-emerges" satisfies the letter of route 2 and supplies no detector. Generalizes: grade the condition's operability, not its existence, when the ladder next tightens.

## 8. Open questions
- Korea figures vs SAM's Asia lane — reconcile at the next SAM firming. **Still open (not checked this pass).**
- `VX_HISTORY` — FROZEN-banner or resume appends? **Now flagged by tooling** (`--strict` +238d). ZHAO's call; routed.
- Cadence question **CLOSED: ACTIVE, WEEKLY** (6 sessions in 23 days; declared 9/30).
- Root-divergent local git rules (§4 #9) — **PROME/Will**, not ZHAO alone.
