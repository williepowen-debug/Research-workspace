# BOND — RUN RECEIPT

**Session:** 2026-09-04 (Fri) ~08:2x–09:0x ET · **Will-spawned boot** ("please boot up… Swedish pension cutting US treasuries — do we have this info already?") + **PROME doorbell mid-session** (`prome-9a`, two dated items + inbox drain). Overwrites the 2026-09-02 receipt.

## Boot gate

| Step | Result |
|---|---|
| 0 · `git pull` | ⛔ **NOT RUN — BLOCKED BY PROTOCOL, deliberately.** `git status` showed **5 modified files in `AGENTS/SAM/`** (uncommitted, outside BOND). Root CLAUDE.md § *Before pulling* step 2: other agents' dirs modified ⇒ **STOP, do not pull.** Session ran on local HEAD `6eb5b1b7f`. **Flagged to Will.** |
| 5 · `docket_check.py` | **rc=0** — 3/3 September refunding legs docketed (`91282CRL7` 9/8 · `91282CRF0` 9/9 · `912810UW6` 9/10). **VERIFIED ONLY THROUGH 2026-09-10.** Blind span **9/11 → 9/25 (15d of 21) declared UNVERIFIED** as designed — human QRA step, lives as a dated DOCKET row. |
| 6 · `boot_recompute.py` | 🔴 **rc=1 — 10 unguarded drift findings. NOT a pass. ALL FIXED THIS SESSION (see below).** |
| 7 · WALTER lane | **2 deliveries processed** → `inbox/WALTER/processed/`. |
| 7b · `corrections_boot_check.py` | **rc=0** — 0 unreceipted NAMED rows. |
| 16 · `closeout_check.py` | Run; findings closed in-session (this file's own EXPIRED-PENDING clause + the inbox FILE-STATE claim, both now true). |
| — · `kb_lint.py` | ✅ **conformant** — enums, vocabulary, dates, IDs, field-count, across 231 rows. |

## Will's question — answered, and the answer is a DATE finding

**"Do we have this info already?" → NO, the desk did not have it. It does now (`KB-BND-229`). The first finding is that the story is ~7.5 months old.**
Alecta (Sweden's largest occupational pension manager, ~SEK 1.3T AUM) held ~SEK 100B (**~$11B**) of USTs at end-2024 and sold ~SEK 70–80B (**~$7.7–8.8B**) in stages **since early 2025**. Reported **Dagens Industri → Bloomberg/Reuters 2026-01-21, The Local SE 2026-01-22** (WebFetch-verified at source 9/4). Companions, same January cluster: Danish **AkademikerPension** (all USTs, ~$100M, CNBC 2026-01-20), Dutch **ABP** (−$12B during 2025, Bloomberg 2026-01-23). **Three WebSearch passes returned NO September-2026 Nordic/AP-fund item — SEARCH-NOT-FOUND, with the unchecked primary NAMED (an AP-fund or Alecta H1-2026 report, which are ZHAO's primaries, not BOND's).**
**Verdict: not size, and it reconciles AGAINST its own headline.** $8.8B over ~18 months ≈ **7% of one quarterly refunding**; Alecta's entire former UST book is smaller than the 9/8 3Y leg. ZHAO's `KB-ZHAO-122` (June TIC) has foreign **OFFICIAL −$45.4B** vs foreign **NON-OFFICIAL +$23.2B** — **Alecta is non-official, i.e. inside the bucket that was net BUYING.** **No BOND vector moved, no trigger fired.** Routed to ZHAO (their lane; BOND keeps no foreign-holdings copy).

## Inbox processed — 4 → 0

| Item | Disposition | KB | Surfaces touched | Outbound |
|---|---|---|---|---|
| `inbox/2026-09-02_from-PROME_WQ-162-RULED-…` | **EXECUTED** → `processed/` | — | `monitors/AUCTION_HEALTH.md` § GRADING BASIS (new) | → PROME |
| `inbox/2026-09-02_from-RED_FT-11-v1.1-ENCODED-…` | **ANSWERED** → `processed/` | — | — | → RED |
| `inbox/WALTER/SIG-W-20260903-004` (USD/JPY 156.14) | INFO → `processed/` | `KB-BND-230` | none — SAM owns the level | — |
| `inbox/WALTER/SIG-W-20260903-010` (gold −2.35% withdrawn) | INFO → `processed/` | `KB-BND-231` | **exposure checked: no BOND surface carries the withdrawn cell** | — |

## PROME doorbell — both dated items answered in-session

- **① WQ-157 leg ① rec (Will rules by 9/8):** **RETAIN `I'` standalone through 9/8–9/10 as ruled, then PAIR — never RETIRE.** Fire rate **23.2% pooled / 15.6–28.1% per tenor** vs OLD conjunctive **1.8%**; no TLT-5d separation; P(≥1 fire) ≈ 49%. **Caveat carried, not buried: TLT-5d is a PRICE yardstick, the kill is a MECHANISM claim, and the FR2004 weekly join is OWED not substituted — which is why the rec is retain-then-pair, not pair-now.**
- **② DOCKET L235 (buybacks 9/9):** ✅ **CONFIRMED PRE-REGISTERED** — `RED-FT-11` v1.1 encoded by RED **2026-09-02, seven days before go-live**. F2 activates only on OFF-the-run. **Standing per-op routing obligation to RED from 9/9 restated.**
- **④ Count correction returned:** doorbell said 3 unconsumed top-level; BOND held **2** top-level + 2 WALTER-lane. Offered as a fact, not a dispute.

## 🔴 Corrections shipped — three carried figures, all found by `boot_recompute` rc=1

1. **STATUS said 30Y 5.27 "ties the 2026 max (5.27, 7/31)". The 2026 max is 5.31 [8/17]** — verified on a full-series pull (n=169 2026 sessions). 5.27 is joint-3rd (7/31, 8/21, 9/1, 9/2). Corrected at the primary, correction stated on the row rather than silently overwritten.
2. **The add-gate read 6bp on three surfaces; it is 5bp** [DFII10 **2.45**, 9/2] — **the closest approach of the entire episode.** 97.0th pctile full-series / 99.8th post-2010.
3. **FR2004 was four surfaces stale at the 8/19 as-of.** New **8/26** vintage pulled: **11-21Y $68.9B → $65.0B (−$3.9B)** but **total long-end $146.3B → $151.8B (+$5.4B)** ⇒ long-end drawdown **NARROWED to −13.3%**, and the *"still widening"* clause carried on those surfaces is now **FALSE** — corrected, not carried. Rebuild sits across the 8/25–27 cluster, i.e. ordinary takedown. **Two vintages now point opposite ways; ambiguous by the monitor's own discriminator; no pre-registered trigger fired ⇒ dealer absorption HOLDS AT 2.**

Also refreshed to the 9/2 close: 30Y 5.27 · 10Y 4.79 · 2Y 4.39 · **HY 266** · **CCC 1053 (another fresh 2026 high)** · IG 81 · 30Y run **42 sessions, 58 days in 2026**.

## 🔴 WQ-157 leg ① — RULED MID-SESSION AND ENCODED SAME SESSION (not deferred)

**Will, verbatim 2026-09-04 08:44 ET: *"Approve 157 with your rec."*** Relayed by PROME; **verified at three independent artifacts before acting** — the packet file, commit `b0b68f9fa`, and `PROME/WILL_QUEUE.md` row 157. Record: `PROME/proposals/2026-09-04_wq157-leg1-RULED.md`.

**Operative sentence, now on the kill surface:** **`I'` STANDALONE THROUGH 2026-09-10; PAIRED THEREAFTER — PAIRING INSTRUMENT OWED.** Through the refunding nothing changes and a bare `I'` fire moves nothing; after it the kill is `I'` + a non-auction MECHANISM confirmation. `I'` stays the 🟠 marker permanently; **RETIRE rejected.**
**Encoded on:** `thesis/THESIS.md` Exit §1 + version (**v1.2.1 → v1.2.2**, H1 and Version field bumped together) · `thesis/CHANGELOG.md` · `STATUS.md` Exit §1 · `docket/CATALYSTS.tsv` (9/18 row) · `KB-BND-233`. PROME's ACTION line said *"at your next boot"* — treated as a floor, not a ceiling, because the window was open.

🔴 **LEG ② feasibility established BEFORE the build, and it found a hard ceiling** (`KB-BND-234`): probing the NY Fed API directly, `PDPOSGSC-G11L21` and `PDPOSGSC-G21` return **ZERO usable rows on SBN2015 and SBN2013**, while `PDPOSGSC-G7L11` returns **365 and 92**. ⇒ **the long-end bucket structure was introduced at the 2022-01-05 series break; the join is bounded at n=243 weekly prints by the ISSUER's reporting, not by tooling.** Workable — it spans the 2022–23 hiking cycle and SVB. **An empty series under a clean 200 is the exact shape of the defect `fr2004_fetch.py` was built to fix, so an unchecked build would have shipped a short reference set and reported it as the full history.** ⚠️ **SBN2022/SBN2024 bucket-definition comparability is STILL UNCHECKED** — same keyids is necessary, not sufficient; the 9/18 deliverable must state that verdict explicitly.

## Files written

`STATUS.md` (dashboard, gate table, FR2004 block, matrix rows 1 & 3, trade interface, BOTTOM LINE, next-dated) · `monitors/AUCTION_HEALTH.md` (**WQ-162 grading-basis declaration — 13 elements incl. the FRN exclusion rule written ON the bar, STRICT operator, pooled-governs convention**) · `workbook/KB.tsv` (`KB-BND-229/230/231`) · `SCRATCH.md` · this file · 3 outbox packets (ZHAO · PROME · RED), each copied to the recipient inbox.

## Not done — named so it is not mistaken for done

- ⛔ **No `git pull`** (SAM dirty). **Local HEAD may be behind origin.**
- **20 ACTIVE KB rows past `Stale_By`** — un-adjudicated, carried from 9/2. Read each; do not bulk-flip.
- **OPEN MIRROR DIVERGENCE untouched:** `VX-BND-05` = 4 and `VX-BND-16` = 4 in `VX.tsv` vs matrix 3 / 2 — components HOTTER than the matrix.
- **`MEMORY.md` 31,839 B = 98% of the 32,550 B read budget**; **`STATUS.md` now ~31.2 KB = ~96%.** Both need rotation next session, STATUS newly so.
- BTP-Bund **48d stale** — refresh before the 9/10 ECB. `^MOVE` not re-pulled. SOFR−IORB re-test still owed.

**Position: TLT puts HOLD, no add. Book untouched. $0. Composite 12/35 — tenth consecutive unchanged session.** *(WQ-157 leg ① changed a SPEC, not a position: nothing moved, and the change TIGHTENS a kill on this desk's own live book after 9/10.)*
