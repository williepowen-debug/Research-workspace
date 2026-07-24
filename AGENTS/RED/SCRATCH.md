# RED SCRATCH — Canonical Session Handoff

<!-- TEMPLATE (rewrite in place at W5 every session; git history versions this file):
## CHANGES SINCE (what moved while RED was offline)
## WHAT I DID
## NEXT SESSION (dated, priority-ordered)
## OPEN THREADS
## PENDING WILL-DECISIONS
## GIT STATE (one line)
-->

**Session 25 — Fri 2026-07-24 evening (live, Will in-session)** — inbound-correction pass. S24 closed ~12:45 the same day; five packets landed after closeout, one of which falsified a load-bearing premise in the framework S24 had just shipped. **HOLD 69 / net-bear 62 — UNCHANGED. This was a specification pass, not an evidence pass, and I am explicitly not letting a methodology correction read as a thesis move.**

## CHANGES SINCE (S24 closeout ~12:45 → 19:30, same day)
- **Tape drifted back up:** Brent **98.38** (S24 logged $96.11 intraday) — the "reversibility" datum I logged at midday is **weaker** than written. VIX 18.58, HY 277 (FRED 7/23), CCC 991, USDJPY 163.79. FT-01 + FT-07 firing; WL-03 (HY>280) **3bps**, WL-06 (CCC>1000) **9bps**.
- **5 inbox packets, all post-closeout:** CARL ×2 (⚠️ FOMC-premise correction + lag-poke all-six-adopted receipt), LABOR (KFRC date + FOMC labor leg + ECI), NEXUS (CHG-043-B adopted as Discipline H + HY-vintage push-back), PROME (BROCK assigned PC-gate; S22 flag closed).

## WHAT I DID (S25)
1. **⚠️ Verified CARL's correction independently — and it's STRONGER than he reported.** He and HENRY derived "the oil doesn't land in the July CPI" from **retail gasoline** (GASREGW, needs a pass-through-lag assumption). I pulled **spot Brent** (DCOILBRENTEU, needs none): **June avg $85.40** (n=22, ran 98→70) vs **July $83.3-85.0** (n=23) → **negative MoM on every final-week path** (−2.5%/−1.4%/−0.4% at $92/$96/$100). Near-identical monthly averages, opposite trajectories. Three independent derivations, two supply-chain layers. **The error appears TWICE in my v1.0** (the 8/13 framing *and* the setup table's "oil +$24" — true as a level, ~zero as monthly-average inflation). KB-070, ML-110.
2. **★ Found the second error myself — uncaught by CARL, and the worse one.** CHG-028 is a **core/services** falsifier; oil→core is a **2-6 month** channel, so it can't resolve on the first **headline-energy** print in *any* month. Fixing the date alone would have left the channel mismatch intact. Plus rockets-and-feathers (my own S24 point to CARL) makes ~9/10 hot in **both** branches = weak discriminator. **CHG-028 re-anchored 8/13 → Sept (~10/13) + Oct (~11/10), two-print requirement**; 8/13 and ~9/10 are pre-registered **non-events** for it. KB-071/074, ML-111/115.
3. **Adopted CARL's arithmetic, REJECTED his inference.** He argued it favors a hike-now Warsh ("the next print he sees will understate the pressure"). Wrong on sequencing: **the operative print is the last one before the next decision.** Ladder = 8/13 soft → ~9/10 hot → ~9/15-16 Sept FOMC, so the decisive print lands ~5-6d before the meeting with perfect cover — waiting is cheap. **S1 52→54 / S4 23→21** (small: the base effect is public; I'm fading an $18.2M-deep market on a reasoning edge, not an information edge). **S3 held at 7 — won't trim the branch nobody's positioned for to balance arithmetic.** ML-112, KB-072.
4. **FOMC framework → v1.1, amended pre-data, corrections struck-and-marked in place** (v1.0 priors stay readable so the amendment is separately gradeable). Added **§0/§0b** (correction + CHG-028 re-spec ladder), **§L oil-language third cell** (CARL's catch: L2 "look-through" — my v1.0 binary would have mis-scored it hawkish while the market read it soft; I set **30% vs his 40%**, because the 6/17 line was delivered into a *falling* pump), **§LAB labor-language leg** adopted unmodified from LABOR (70/25/5 — was **fleet-unowned**) + my overlay that the June minutes' "payroll gains strengthened" is **already superseded** by the 7/2 print, **Guard 6** (level-vs-average, general form), **Guard 7 / ECI 7/31**. KB-073, ML-113.
5. **KFRC re-dated 8/04 → Mon 7/27 AMC** (LABOR, 3-source verified) — 8 days off **in the direction that matters**: the canary triple now completes *before* the Fed, an **input** to FOMC week. Bar is set not open; **grade the guide, not the tape** (RHI in-line + up-guide 7/23, still −7% AH). KB-075, ML-114.
6. **Ledger sweep:** ML-110…115 · KB-070…076 · **RED-21 registered** (July CPI energy negative MoM, 85% — the arithmetic as a scored object; a CORRECT here is *not* bear evidence) · CHG-028 row → `LIVE-RE-ANCHORED` · docket: KFRC re-dated, July-CPI row re-specced 🔴→🟠, **5 rows added** (Aug CPI ~9/10, Sept ~10/13, Oct ~11/10, ECI 7/31, Sept FOMC ~9/15) · STATUS/CHANGELOG/NEXUS_BRIEF/MAINTENANCE updated · KB.tsv stray blank line removed (pre-existing, verified via `git show HEAD:` first).
7. **Routed 4:** PROME outbox memo (fleet-wide items 1-2); **CARL** (verified-stronger + inference rejected + **the rationalization attack he invited, pre-registered as a dated test**: ~8/15 HHDC benign AND V2 not 4→3 = scored rationalization finding); **LABOR** (all three adopted + a discriminator-gap note on frozen-vs-tight); **NEXUS** (HY vintage settled — my 277 = FRED **7/23**, their 268 = FRED **7/22**, day split, both correct). 5 packets `git mv`'d to processed + board_log logged.
8. **Auto-memory ×2 promoted:** `finding_level_vs_monthly_average_cpi_landing`, `finding_redated_falsifier_inherits_premise` (+ index entries).

## NEXT SESSION (dated, priority-ordered)
1. **🔴 FIRST ACTION — verify the [EST] dates.** Aug CPI ~9/10 · Sept CPI ~10/13 · Oct CPI ~11/10 · Sept FOMC ~9/15-16, against the **published BLS/Fed schedules**. **CHG-028's re-anchor is not pre-registered until these are confirmed** — this is exactly ML-RED-064 (MI3 pre-registered against an assumed FFIEC window that never printed). Do not let the re-anchor sit on modeled dates the way the KFRC row did for weeks.
2. **🔴 Mon 7/27:** **KFRC Q2 AMC** (5pm ET call) — grade the **guide** vs $344-352M / $0.67-0.75; watch the Tech-Flex-vs-F&A split (freeze-axis, 3-for-3). **+ BDC marks 7/25-28** (FSK/OBDC/OCSL/MFIC → ARCC 7/28) = the CHG-027 structural-narrowing test; benign → run the capitulation review **honestly**.
3. **🔴 Tue-Wed 7/28-29: FOMC — execute framework v1.1, do not improvise.** Score S-axis (54/16/7/21/2) **and** v1.0's (52/16/7/23/2) separately; score §L and §LAB independently; record the oil-language cell and whether the superseded labor line is repeated verbatim. Grade both axes at the 7/29 close + next-day confirm. Guards 1-3 live (HY-280 attribution / DISH 7/31 trap / sinking-watch overlap).
4. **🟠 Fri 7/31: ECI Q2 08:30** — if the Fed leaned hawkish-on-wages Wed and ECI prints ~3.4% flat, log the composition-contamination as its **own** dated entry, never laundered into an FOMC cell.
5. **🟡 Verify / watch:** EGBN Q2 grade (still unlocated) · sinking-watch 7/26 outcome · June MF-starts · EIA weekly diesel from ~8/3 (CARL's natural experiment — grade **timing** only, he's not claiming a clean coefficient) · OSPREY rotation test to ~8/24 · whether FALCON folds the CHG-043 P/R split-scalar · BROCK's PC register when PROME routes it (I offered to red-team it).
6. **Daily:** HY >280 (3bps) · CCC >1000 (9bps; DISH 7/31 mechanical-tightening trap) · SKEW vs 140 · Brent vs $85 book levels.
7. **~10/6:** pre-write the Sept-CPI **core** decision tree (CHG-028's real test). **Nothing is owed by 8/6 anymore** — that deadline died with the premise.

## OPEN THREADS
- **CHG-028 re-anchor is provisional until the BLS dates are confirmed** (item 1 above). Treat it as un-pre-registered until then.
- **CARL rationalization test ARMED and dated:** ~8/15 HHDC prints benign-or-better on the subprime/DQ legs **AND** V2 does not go 4→3 → I file a scored rationalization finding against CARL. If it moves, the hold was correct sequencing and I say so in writing. *(Caveat sent: make sure the ~8/15 leg names a series that actually exists — his V2 downgrade was previously armed against a series the HHDC doesn't publish.)*
- **CHG-027 capitulation-review condition armed** (BDC + SBCF/EGBN benign) — do not soften it if it fires.
- **CHG-042 residual** = de-escalation decay-split (crude fast vs freight/insurance sticky). Muscat/Oman Article-5 vehicle unexercised.
- **Claims 187K sits at 75/25 bull on my counter-signal table.** If LABOR's frozen-vs-tight artifact framing is right, that weight is too bull. Not moving it on argument alone — asked LABOR what would move it and to pre-register a threshold.
- Q2 FFIEC MI3 leg (~mid-Aug; confirm cadence before pre-registering — same lesson as item 1).

## PENDING WILL-DECISIONS
- None new. Broker-confirm at convenience: OZK Jul-17 $42.5P ×2 expired dead-OTM.

## GIT STATE (one line)
On master, clean outside RED at boot (only DEWEY scratch_*.js untracked, not mine); S25 commits RED-dir files + 3 self-authored packets into CARL/LABOR/NEXUS inboxes per the carve-out → safe-push at closeout.
