# CORAL SCRATCH — 2026-08-03 ~11:15AM ET (Will-directed boot + 9-day catch-up)

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (7/25 scoped HOA re-check)

**9-day gap. Four catalysts came and went unattended; all four now resolved or honestly marked open.**

1. **SBCF Q2 GRADED — the owed item, 6 days late.** BENIGN 0-of-4 off primary 8-K acc. `0001628280-26-050147`. **Q2 FL-bank window is now EMPIRICALLY closed: 7-of-7 benign, final sync 0-of-≥2.** Rail NOT met, NOT armed.
2. **⭐ THE SESSION'S REAL FINDING: the sharpest pre-registered tell of the whole window is FALSIFIED — in the opposite direction.** The frozen tell was "SBCF nonaccrual 3rd consecutive rise >$95M + CRE-non-OO charge-off/specific reserve build." **Neither leg happened.** Nonaccrual **reversed**: $72.0M (4Q25) → $95.0M (1Q26) → **$86.5M (2Q26), −8.9%**. And it reversed on the **whole aging ladder at once** (30-89d $28.2M→$20.1M, NPL 0.75%→0.66%, NPA 0.47%→0.42%, OREO down, NCO flat 10bps) — so the **LESSONS up-migration trap explicitly does NOT apply**: that rule fires when an early bucket falls while a late one rises, and here *nothing rose*. The 100%-FL bellwether's leading edge — the closest thing CORAL had to a precursor — **turned. Bank-transmission timeline gets LATER, not earlier.** Carried as a genuine negative, not softened.
3. **🏦 GSE financing channel went live TODAY (8/3), and it is now CORAL's sharpest live mechanism.** Limited/Streamlined Review eliminated for applications dated on/after 8/3; >10-unit projects → mandatory Full Review (reserves, deferred maintenance, open assessments, litigation, master insurance). **NEW second gate 1/4/2027: reserves 10%→15%.** ⭐ **The arithmetic:** non-warrantable flag triggers at **unfunded repairs >$10K/unit within 12mo**; CORAL's assessments are **$25K–$100K/unit (to $400K)** = **2.5–40× the threshold** → **the SIRS cohort is non-warrantable BY CONSTRUCTION.**
4. **HOMER's rank-vs-level correction ACCEPTED — it qualifies CORAL's hardest 🔴 leg.** "FL #1 foreclosure" is a **RANK** claim; FL's *level* (0.435% in 2025) is **~31% below its own 2019**; FY26 projects ~0.58% vs a 0.63–0.72% pre-COVID band. **What survives and is genuinely anomalous: conversion SPEED** (563d, lowest since 2013; REO +33%).

## WHAT I DID THIS SESSION

- Full boot: STATUS, SCRATCH, LESSONS, MEMORY, CALENDAR, `scripts/boot.py`, git state. **Did NOT pull** — 5 other agents had uncommitted work in-tree (protocol). Verified we were **1 behind / 7 ahead**, the one origin commit being BRENT's and untouching CORAL, so the boot read was not stale.
- **SBCF:** entity disambiguated FIRST via EDGAR submissions API (Seacoast Banking Corp of **FLORIDA**, CIK 0000730708, Stuart FL — *not* SouthState/SSB CIK 0000764038), then pulled ex-99.1 + ex-99.2 direct (curl+UA; WebFetch 403s on SEC as always), converted to text, graded mechanically on the frozen 4-axis frame with **zero threshold moves**. Ran the strictest-reading check (2-of-4, bar ≥3 → robust). Pulled the tape independently (yfinance daily closes): $33.65 print → $35.20 8/3 = **+4.6% vs KRE +0.4%**, no divergence.
- **Fresh primaries pulled:** Parcl 5 metro pages (8/3), citizensfla.com policies-in-force (8/3), CSU forecasting page (8/3), NHC TWO (8/3), SBCF 8-K (primary).
- **WALTER lane DRAINED** — 10 signals read, dispositioned, logged to `board_log.tsv`, `git mv`'d to `processed/`. One `acted` (NOAA 81% very-strong El Niño → written into the STATUS hurricane row); two `skipped` with reasons (Jazan refinery, Lake Powell — outside FL).
- **Surfaces written:** STATUS (8/3 block + header + Signal Status + 5 dashboard rows + bank table + BOTTOM LINE; **held at exactly the 250-line cap** by archiving superseded BKU/VLY blocks → `workbook/STATUS_archive_20260721.md`), FL_BANK_WATCHLIST (row 7 SBCF + headline + final sync + live window + **HOA line synced**, closing the item flagged un-synced on 7/25), CALENDAR (4 resolved, 4 added incl. the new 1/4/2027 gate), KB **ML-CORAL-054/-055/-056/-057**, NEXUS_BRIEF **re-pinned** (clears NEXUS's 7/31 CONTENT-STALE flag), outbox→HOMER (delivered to their inbox).
- Commit `c1a1c7497`, pathspec-scoped.

## ⚠️ THREE SOURCE-QUALITY CATCHES — the pattern worth carrying forward

Search-summary tier failed **three times in one session, in three different directions**, and every failure was caught by fetching the underlying source and checking its date:

| # | Summary claimed | Source actually said | Damage if trusted |
|---|---|---|---|
| 1 | Tampa MSI **4.92** | **6.99** (Parcl page direct) | Would have broken the 🔴 leg's breadth condition on a false reading |
| 2 | CSU moved to **11/5/2** | **9/4/1** (CSU primary) | Would have manufactured a **false correction to a CORRECT dashboard row** |
| 3 | Ocala June UR article | Article dated **2025-07-22, reporting JUNE 2025** | Would have written a **year-old figure** in as the current metro read |

**#2 is the nastiest class:** a summary that induces you to "fix" something that was already right. **#3 is `finding_anniversary_article_is_a_consensus_decoy` firing live.**

## NEXT SESSION (mechanical, in order)

1. **Wed 8/5 — CSU hurricane update** (off the verified 9/4/1 / ACE 50 baseline) + NOAA August outlook. Tropics were empty 8/3; NOAA has 81% on a very strong El Niño Oct-Dec.
2. **Two OPEN verification items on the GSE rule — both matter, and one cuts against my own framing.** (a) Land the **GSE primary** (LL-2026-03, 2026-03-18) — `singlefamily.fanniemae.com` Cloudflare-403'd on curl+UA *and* WebFetch, and Selling Guide B4-2.2-01 still shows pre-change text dated 04/02/2025. Try an alternate host/API per `finding_blocked_mirror_is_not_an_unreachable_primary`. (b) **SEL-2026-05 may partially LOOSEN FL requirements** (waiver expanded to ≤10 units, **FL-specific PERS requirement retired**, 50% investor-concentration limit retired). If true, "the GSE screw only tightens" is wrong. **Summary-tier, NOT adopted, flagged in STATUS + KB + the HOMER packet.**
3. **Amendment 3 ruling** — Judge David Frank, 2nd Judicial Circuit (Leon County) heard 3 consolidated challenges 7/29, **did not rule**, set an August briefing deadline **whose date I could not confirm** (WFLA + Florida Phoenix both 403'd). **Pre-reg branch ML-CORAL-042 stays UNRESOLVED — do not score any branch until the ruling lands.** Remedy sought is a **rewrite, not removal**.
4. **Ocala June-2026 UR — still owed.** BLS bot-blocked, FRED 403 across 3 endpoints, deptofnumbers retired. **Re-attempt via the FloridaCommerce LMS primary** (`lmsresources.labormarketinfo.com`). ⭐ Useful baseline salvaged from the decoy: Marion County's *normal* June seasonal shape is **+0.6pp** (4.3%→4.9% in 2025, education/student driven) — so a ~+0.5-0.6pp June-2026 rise is **not** signal.
5. **Tue 8/18 — Citizens assumption round #2**, off the **278,061 (7/24)** base. ⭐ Watch closely: **depopulation has STALLED flat** (−0.07% in 3.5 weeks after −29% in five months). Takeout capacity winding down while the residual book concentrates in thin carriers = the VX-CORAL-TKOUT-01 setup.
6. **~Aug — three FL-bank 10-Qs.** The leading-bucket detail (30-59/60-89 sub-buckets, CRE-non-OO cuts) that the 8-Ks don't carry; the nearest bank-leg observable now that Q2 is swept. REGINALD carries these as unscored too.
7. **~Aug 20 — FL Realtors July.** Post-8/3, the sharper cut is **warrantable vs non-warrantable**, not the blended median.
8. **Root inbox: 9 unprocessed** (below). At least MARCO 7/31 (an ANSWER to a CORAL question) and CREED 7/27 (says CORAL's pillar-4 names CREED as owner-doc and is CORAL's stalest lane) deserve a dedicated pass.

## OPEN THREADS

- **Bank-transmission rail: NOT met, NOT armed. Q2 CLOSED 7-of-7 benign, final sync 0-of-≥2** — and the sharpest pre-registered tell **falsified**. Next re-test Q3 ~late Oct; nearer observable = the ~Aug 10-Qs. **Do not re-fit the frozen frame.**
- **🔴 MSI supply-side leg: HOLDS, sustained not intensifying.** 8/3 pull: Tampa 6.99 · Punta Gorda 6.75 · North Port 6.43 · Cape Coral 6.07 · Lakeland 6.04 — **5-of-5 >6.0 on a 3rd consecutive reading**, but **4 of 5 drifted DOWN** vs 7/23. Leg stays 🔴 as Will-ratified; characterise honestly.
- **NEW — SBCF CRE concentration is a two-sided watch:** 224%→**230%** of bank-level RBC, C&D 35%→**40%**. Under the 300%/100% guidance, but exposure is *growing* while credit improves. Contrast EGBN de-risking 295%→268% (REGINALD).
- **NEW — the condo→bank wire is structurally unobservable, and that is now evidenced, not asserted.** Zero HOA/condo/association/SIRS disclosure across **all seven** Q2 releases. HOA transcript-mine closed at **3-of-4** (SSB transcript never located; stale-marked, low residual value since its release+deck were already grep-clean).
- **CORAL's hardest 🔴 leg is now qualified** (rank-vs-level). Not retired — rank deterioration and conversion speed are real — but it can no longer carry an implication of crisis-magnitude *levels*.

## MAIL STATE

- **`inbox/WALTER/`: DRAINED** — 10 signals consumed, logged, `git mv`'d to `processed/`.
- **`inbox/` (root): 9 unprocessed**, all pre-dating this session: AEOLUS 7/22 · DEWEY ×4 (7/24, FHA/VA waterfall + STR trio) · MARCO ×2 (7/25) · CREED 7/27 · **MARCO 7/31 (an ANSWER to a CORAL question — SWFL convergence, third dataset, no divergence)**. **3 processed this session** (HOMER ×2, NEXUS — all acted on).
- **`outbox/`: NEW `2026-08-03_to-HOMER_...`** — delivered to `AGENTS/HOMER/inbox/`. Prior 7/21–7/24 PROME notes still in root outbox (in-flight/delivered-pending-sweep).
- **NEXUS 7/31 CONTENT-STALE flag: CLEARED** by the brief re-pin (their packet said the re-pinned brief *is* the acknowledgment — no reply owed).
- Other agent sessions ARE live on box — committed pathspec-only; **did not pull** on protocol.

## ⚠️ PUSH DEFERRED — ACTION FOR NEXT SESSION (or whoever closes out next)

**Two CORAL commits are local-only and NOT on origin:**
- `c1a1c7497` — the catch-up work (STATUS / FL_BANK_WATCHLIST / CALENDAR / KB ×4 / board_log / mail moves)
- `859a2331a` — closeout (NEXUS_BRIEF re-pin / SCRATCH / MEMORY / HOMER packet, incl. the copy in `AGENTS/HOMER/inbox/`)

**`scripts/safe-push.sh` ABORTED non-ff** (correctly, fails safe): origin carries `e8c178dcd` (BRENT, 8/3 Monday data pull) which we don't have locally. **I did NOT `git pull --rebase`**, because the working tree holds uncommitted work from **BRENT (live session — board_log, WALTER processed ×5, inbox processed ×3, a message receipt), SAM (FXY_OPTIONS/JGB_YIELDS), WALTER (an OTTO inbox signal), and `memory/auto/`** — the "Before pulling" rule says stop when other agents have uncommitted changes, and BRENT is visibly mid-session.

**This is routine, not an incident** — serial multi-machine, same box, concurrent agents. **Resolution:** once the tree is clean outside CORAL, `git pull --rebase` then re-push; or simply let the next agent's closeout push sweep both commits (the push-train). **Never force.** ⚠️ **`AGENTS/HOMER/inbox/2026-08-03_from-CORAL_...` is committed but unpushed — HOMER will not see the packet until this lands.**
