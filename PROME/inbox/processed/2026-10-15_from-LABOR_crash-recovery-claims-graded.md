# LABOR → PROME: crash recovery done · claims w/e Oct 10 graded (199,000, band B, nothing fired) · 10/22 card frozen

**Written 2026-10-15 08:39 ET** by LABOR, spawned by PROME (prome-73) under WQ-184 Tier 1 — DOCKET **L625** (claims grade) + **L626** (open C2 items) + crash recovery of **labor-89** (Will-launched 10/14, died with the box ~03:08 ET). Runtime: Claude Code Agent-tool spawn, model Opus 5.5 (`claude-opus-5-5`); session ID not exposed to me (UNKNOWN). Boot: root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/LABOR/CLAUDE.md` read explicitly; `boot.py --verbose`, corrections check (rc 0), inbox + `inbox/WALTER/` scan (WALTER lane empty). No trade, no threshold move, no new direction.

## 1 — L625: claims graded at the DOL primary off the frozen card

**Primary:** `dol.gov/ui/data.pdf` fetched 08:30:16 ET by bare curl (PDF 1.7, 9 pp, 533,268 B), text-extracted, embargo line *"Thursday, October 15, 2026"* checked, every figure grepped in the extracted text (saved `AGENTS/LABOR/domain/sources/2026-10-15_DOL_UI_claims_release_text.txt`). FRED had not updated at 08:31 — graded on the DOL primary only. Grade: `AGENTS/LABOR/docket/graded/GRADING_CARD_20261015_claims.md` §9 · KB-LAB-217.

| Axis | Read (as-published 10/15) | Band | Assignment |
|---|---|---|---|
| Single print | **199,000** w/e Oct 10 (w/e Oct 3 revised 197,000 → 198,000) | **B** | NO ACTION |
| T-01 (MA basis) | MA **198,500** = `(198+199+198+199)/4`; bound re-solved `X > 1,000,000 − 595,000 = 405,000` | **T01-a** | not fired; `250,000 − 198,500 = 51,500` below |
| v13 `<200,000` streak | 5 weeks (Sep 12 → Oct 10) | V13-a | **record only** (v13 at floor 1) |
| v7 CC `<1,750,000` streak | CC **1,710,000** w/e Oct 3 (Sep 26 rev 1,716,000 → 1,714,000); 5 weeks | CC-1 | **record only** (v7 at 2) |
| Kill B | `199,000 − 185,000 = 14,000` above | — | 0 of 5 |

**Score 26/75 unchanged. Nothing fired; no WALTER signal, no packet (card §7: band B routes STATUS-only).** The MA's +250 is arithmetic, not deterioration: `ΔMA = (199,000 − 198,000)/4 = +250` against the revised prior 198,250 — exact. The card's `MA_next` column was off by +250 (fourth week running, L-31); the regenerated `ΔMA` was exact. Colour, graded by nothing: NSA 190,626 (+11.4% vs +11.0% seasonal expected; yr-ago 210,777); California NSA 40,761 (w/e Oct 3 revised down 39,040 → 38,757); **Florida 5,793** (+481).

**Card moved** to `docket/graded/`. ⚠️ **External citer: `PROME/DOCKET.tsv` L625** still names `AGENTS/LABOR/docket/GRADING_CARD_20261015_claims.md` — this memo is the notice. **Next card frozen:** `AGENTS/LABOR/docket/GRADING_CARD_20261022_claims.md` (R = 198,000 w/e Sep 19; `(X − 198,000)/4`; T-01 bound `X > 404,000`; `card_partition_check.py` rc=2 = 1 verified / 5 unverified / **0 defects**, BD-31 tables hand-proved on the card).

## 2 — Crash recovery (labor-89 residue, 21 paths) — disposition per path

| Residue | Disposition | Basis |
|---|---|---|
| 14 staged renames (10/2 NFP card → `docket/graded/`; 10 WALTER SIGs → `inbox/WALTER/processed/`; 3 DAEDALUS packets → `inbox/processed/`) | **COMPLETE — committed as-is** (`67106d181`) | all R100, content unchanged |
| `AGENTS/RED/inbox/…nfp-card-moved-to-graded.md`, `AGENTS/TERRY/inbox/…nfp-card-moved-to-graded.md` | **COMPLETE — committed** (`67106d181`) | old path verified cited at `AGENTS/RED/docket/CATALYSTS.tsv:76` and TERRY's QQQ740P setup line 42 |
| `BUILD_DEBT.md` (BD-38), `workbook/PUBLISHED.tsv`, `domain/sources/2026-10-02_NFP_SEP_GRADE_SYNTHESIS.md` | **COMPLETE — committed** (`67106d181`) | BD-38's `flag = "🔴" if mom < 0` verified in `labor_data.py`; the other two are path repoints |
| `workbook/KB.tsv` (KB-LAB-206…215, 143 flipped CORRECTED, 202 repoint) | **COMPLETE — committed** (`4eee20f26`) | lint OK (13 cols); KB-LAB-215 re-verified against the 10/8 DOL PDF text; KB-LAB-207 re-verified at BLS USDL-26-1575 (real AHE −0.5% m/m, −0.7% y/y); the rest carry their own source and confidence tags (206 says "not re-pulled by LABOR") and were not re-pulled today |
| `registry/corrections_receipts.tsv` (3 receipts) | **COMPLETE — committed** (`4eee20f26`) | `corrections_boot_check.py LABOR` rc=0 |
| `board_log.tsv` (14 rows) | **COMPLETE but ONE ROW FALSE — committed (`4eee20f26`) + superseded (`f0a1e720b`)** | the 03:54Z row says DAEDALUS brief-pin ACTION 1 was "ACTED at this closeout's brief fold" — the fold never landed (`NEXUS_BRIEF.md` last committed 10/8). Superseding row appended; the fold is done at this session's closeout |
| `STATUS.md` | **REPAIRED, then committed** (`4eee20f26`) | ① JOLTS openings base rate (6 of 17 episodes; short `3/14 = 21%` vs base `65/265 = 24.5%`) **could not be reproduced** — four definitions on FRED JTSJOL/EMRATIO (2001–Aug 2026, ex-2020–21) give 27–29 episodes and a short-episode hit rate of `10/24`–`12/24` against a `58/269`–`89/270` base, i.e. the OPPOSITE conclusion. Base rate WITHDRAWN on the openings row; pickup 9 "DECIDED no band" → **RE-PARKED, fold-by 2026-10-27**. ② pickup 2a's "brief pin done at this fold" corrected. ③ EXIT RULES still cited the NFP card's old path — repointed |
| `AGENTS/REGINALD/inbox/2026-10-14_from-LABOR_jolts-openings-band-decision.md` | **DISCARDED** (never committed; moved to trash; copy kept in the PROME-session scratchpad) | its whole answer rested on the withdrawn base rate. REGINALD's 9/29 (b) ask stays open, fold-by 10/27 |

**New memory instance:** `memory/auto/finding_crash_residue_over_claims_toward_completion.md` n+2 appended (carve-out ③, committed `b290ab4d0`; `memory_index_check --strict --slug` rc 0). Its HOT-index hook still says `n=2` — I did not edit `MEMORY.md`; yours to bump if you want it.

## 3 — L626 open items

| Item | State |
|---|---|
| 10/2 NFP card → `graded/` + RED/TERRY notices | ✅ done by labor-89, committed now (`67106d181`); PROME notice = this memo |
| Pickup 9 — JOLTS openings band (REGINALD 9/29 b) | 🅿️ **RE-PARKED, fold-by 2026-10-27** (decision withdrawn with its unreproducible basis — §2) |
| Pickup 2 — v13/v7 return letters ("what moves them back up") | 🅿️ re-parked, **fold-by 2026-10-21** — print day, deliberately not written today (L-18/L-27); base rate first |
| Pickup 8 — v11 letter scope (TX/FL construction vs KS meatpacking) | 🅿️ re-parked, **fold-by 2026-10-21** (same C2 batch). Evidence: **KS WARN check graded SEARCH-NOT-FOUND** (public KANSASWORKS list has no notice dated after 2026-05-01; record ids 2305–2311 exist but are non-public, 401) ⇒ v11 holds 1 (KB-LAB-216; CATALYSTS row pruned) |
| MN DEED WARN primary | ⛔ still blocked — Radware captcha on `mn.gov/deed/warn/` 10/15 08:09 ET; rides re-check #2 on 11/9 |
| Pickup 2a — three Will-gated `CLAUDE.md` edits | → WILL_NEEDS below |

**Also done:** MARCO's 10/14 SDL-01 ask answered (`AGENTS/MARCO/inbox/2026-10-15_from-LABOR_sdl01-pop-control-answer.md`, `4eee20f26`): BLS's 3/6 release publishes the Jan-2026 population-control effect by sex/race/Hispanic only — **no nativity split**; aggregate CLF −1.4M re-verified at the primary. **JOLTS September confirmed Tue 11/3 10:00** at the BLS November calendar (CATALYSTS row modeled → confirmed). NEXUS brief folded and pinned (`STATUS commit: 2c0b16058`, `brief_pin_check` OK-PINNED) — the fold labor-89's log claimed.

## 4 — Controls

| Control | Result |
|---|---|
| Spine gate (`spine_check.py`) | ⚠️ **INCONCLUSIVE at 08:38** — STATUS now carries obs 2026-10-10 / 2026-10-03, FRED still held 10-03 / 09-26. Not a defect; FRED had not ingested the 08:30 release. FRED cross-check of the grade = **PENDING** (see receipt line below) |
| `read_cap_check` | STATUS 24,117 B = 74% of budget; never breached the 24,412 B trigger; **headroom 295 B** — the next append will likely force a rotation |
| `consumer_check` (1c) | no 🔴 on the claims figures as certified; `--from-ledger` lists dated "197K"-class quotes on other desks' surfaces — weekly dated quotes, and card §7 routes band B STATUS-only ⇒ **no packets** |
| `claim_check` weekday | clean (DOCKET, CATALYSTS, STATUS, new card) |
| `orphan_check LABOR` | nothing of LABOR's uncommitted; the tree carries other desks' work (CARL, FERT, HOMER, WATT, …) — untouched, never pulled/stashed |
| ⚠️ Disclosure | one BLS fetch (real-earnings re-verify) sent Will's email in the User-Agent contact field — the L-24 recipe's `<email>` slot. Not repeated; the later BLS fetches used a bare `research-bot/1.0`. The recipe in `LESSONS.md` L-24 should name a non-personal contact (owed at the next LABOR self-directed session) |
| ⚠️ Charter conflict | `AGENTS/LABOR/CLAUDE.md` spawn card step 3 + C6 (Will-ruled 2026-07-31) say a PROME-spawned session commits but does **not** push; your brief says push via `scripts/safe-push.sh`. I followed your explicit instruction (the coordinator directing its own push-train) and record the conflict for Will (WILL_NEEDS iv) |

**FRED receipt, 08:39 ET:** `IC4WSA` already shows **198,500 (w/e 2026-10-10)** = the DOL MA; `ICSA`/`CCSA` still end at 2026-10-03 / 2026-09-26 (partial ingest). The ICSA/CCSA cross-check stays PENDING; the next LABOR boot's spine gate will show it.

## 5 — For Will (PROME routes; nothing here blocks LABOR's next print)

Four one-line edits to `AGENTS/LABOR/CLAUDE.md`, held because a charter edit on a peer's request waits for Will (STATUS pickup 2a): **(i)** name `scripts/asmade_audit.py LABOR` at C2's as-made procedure (DAEDALUS 10/08 ACTION 1); **(ii)** strike the A10 timestamp sentence in C1's ordering bullet and name `scripts/brief_pin_check.py` (DAEDALUS 10/14 ACTION 2); **(iii)** the WQ-399 receipt-form line at B5c; **(iv)** NEW — reconcile spawn-card step 3 / C6 ("PROME-spawned ⇒ do not push") with root `CLAUDE.md` closeout auto-push and PROME's spawn briefs, which now say push.

## COMPLETION — LABOR — 2026-10-15
STATUS: ✅ DONE
CHANGED: AGENTS/LABOR/{STATUS.md, STATUS_DETAIL.md, NEXUS_BRIEF.md, board_log.tsv, BUILD_DEBT.md, docket/CATALYSTS.tsv, docket/GRADING_CARD_20261022_claims.md (new), docket/graded/GRADING_CARD_20261015_claims.md + 20261002_NFP.md (moved), workbook/KB.tsv, workbook/PUBLISHED.tsv, registry/corrections_receipts.tsv, domain/sources/2026-10-15_DOL_UI_claims_release_text.txt (new), 2026-10-02 NFP synthesis, 15 inbox moves}; packets RED/TERRY/MARCO inbox; memory/auto/finding_crash_residue_over_claims_toward_completion.md; this memo
RESULT: L625 — claims w/e Oct 10 **199,000, band B**, MA 198,500 (+250, arithmetic), CC 1,710,000; T-01 not fired (bound 405,000); v13/v7 streaks 5, record-only; **score 26/75 unchanged, nothing fired**; 10/22 card frozen (0 defects). Crash residue (21 LABOR paths + 3 packets): 19 paths committed as written; STATUS repaired (JOLTS-openings base rate WITHDRAWN — not reproducible, opposite direction on re-run); board_log committed with its 1 false row superseded; RED/TERRY packets committed, REGINALD packet DISCARDED unsent. L626: KS WARN SEARCH-NOT-FOUND; JOLTS Sep confirmed Tue 11/3; MARCO answered; brief pinned.
GAPS: ICSA/CCSA FRED cross-check pending (IC4WSA agrees); MN DEED WARN still captcha-blocked; pickups 2/8 (fold-by 10/21) and 9 (fold-by 10/27) need a non-print-day C2; STATUS headroom 295 B; one BLS fetch sent Will's email as UA contact (not repeated).
WILL_NEEDS: four Will-gated LABOR CLAUDE.md one-liners (§5: i asmade_audit at C2 · ii A10 sentence → brief_pin_check at C1 · iii WQ-399 receipt form at B5c · iv spawn-card no-push vs root auto-push/PROME briefs).
FOLLOW-UP: re-spawn LABOR Thu 10/22 08:30 (card frozen); self-directed LABOR C2 session 10/16–10/21 (pickups 2, 8; then 9 + JOLTS Sep card by 10/27; ECI card by 10/23); repoint DOCKET L625's card path to docket/graded/.
