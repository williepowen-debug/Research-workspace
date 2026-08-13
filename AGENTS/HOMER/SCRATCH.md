# HOMER SCRATCH — 2026-08-13 (Thu) — Will-directed session

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

**Shape:** Booted clean (git 0/0, no pull needed, ledgers all 8/12-fresh). Will worked the slate live: GSE monthly pull → inbox → PMMS → row-45 draft → standing items. **Two registered instruments came back, two of my own claims were retracted, and the inbox drained 9 → 2.**

**Rules honored: zero thresholds moved · zero confidence moved · zero capital · superseded text preserved verbatim everywhere · nothing fired retroactively.**

---

## ★ THE FINDING — the mod-suppression test came back, and it points the predicted way

**Fannie MF *monthly* SDQ ROSE +2bps to 0.60% in June** — the first post-modification month. My docket row 6 asked this in advance, in writing: *does 0.60% hold once the modified portfolio is absorbed, or drift back up?* **It drifted up.**

**The monthly series dates and sizes the mod, which the quarterly cannot:**
`Jun-25 0.61 → … → Mar-26 0.78 (peak) → Apr 0.64 (−14) → May 0.58 (−6) → Jun 0.60 (+2)`
⇒ a **nine-month monotonic uptrend, notched by a two-month step-down, now resuming.**

**Freddie MF monthly rose +4bps to 0.51%.** ★★ **BOTH BOOKS ROSE IN JUNE — so the Q2 "two GSEs moved in opposite directions" asymmetry, which is what the marquee finding was built on, is a QUARTER-LEVEL TIMING ARTIFACT of Fannie's mod. At monthly resolution the underlying direction is COMMON.** The finding survives and strengthens; **its evidence changes shape, and that must be said rather than letting the tidier version stand.**

⚠️ **One small month. Directionally consistent, NOT a confirmation.** And it is **not established the modified portfolio is fully absorbed by June** — if it ran into May, +2bps *understates* the inflow.
✅ Basis: both GSEs 60+/UPB, **confirmed identical** ⇒ directly comparable to each other; **Trepp (30+) still is not.**

## ⚠️ TWO RETRACTIONS OF MY OWN PUBLISHED CLAIMS

1. **"post-GFC high is defensible on the MONTHLY series"** — **FALSE.** Freddie Table 6 has **Sep-2025 at 0.51%, an exact tie.** Not a new high on *either* series. ⚠️ **The "0.39% monthly prior peak" is UNVERIFIED BY ME, NOT REFUTED** — my first wording ("contradicted… RETIRED") was withdrawn later the same session: `consumer_check` traced it to BOARD/SIG-W-20260511-039 where it is a **~2010 GFC-era** peak called "already BREACHED," and a 13-month file cannot refute that. **The Sep-2025 tie carries the finding on its own.** ⚠️ Supportable line is only *"ties Sep-2025, top of a 13-month range."* **Do not invert it into an opposite superlative.**
2. **"FRED_API_KEY is empty"** — **FALSE, and the mechanism is reusable.** My grep pattern `FRED[A-Z_]*=` ends at the `=` and **echoed back my own redaction mask, which I read as absence.** Key present (len 32); `fetch.py fred` works. **New-key ask WITHDRAWN before cost.** ⚠️ Not PROME's guessed cause (wrong file) — I had the right file. **Rule: a redacting command's output is never evidence about the redacted value; test by LENGTH.**

## WHAT ELSE LANDED

- **PMMS 8/13 = 6.67%, −2bps — five-week rising streak BREAKS.** Still ORANGE; 6.72 and 7.0% uncrossed. 15Y 5.96%, 2nd straight fall; the 8/6 divergence **resolved in the 15Y's direction** (n=1, NOT promoted).
- **MBA apps caught up 2 weeks; the Freddie tension RESOLVES with both claims intact.** wk 8/7 composite **+3.6%**, refi **+5.0%** ⇒ Freddie right, my row 2 weeks stale, **never a contradiction — a 14-day ledger gap.** ⚠️ **But composite −11.6% YoY, refi −22.2% YoY: "no refi escape" survives on the LEVEL basis.** Third level-vs-rate instance of the session.
- **July GSE monthlies NOT OUT — path-tested 404 at both** while both June files 200. ⚠️ **The DOCKET DATE was the defect:** cadence is the **last week of the following month**, so "~8/12-14" was wrong by 2 weeks → re-dated **~8/25-28**.
- **Row 46 EXECUTED** — GSE-condo row re-keyed to **~10/15 `WAITING-ON-INSTRUMENT`**.
- **★ Row 45 DRAFTED → WILL-RATIFIED TWICE → ENCODED, LIVE.** Classes **E** (rescue recap ≥10% mkt cap + distress marker) · **F** (≥20% non-growth dilution) · **G** (unscheduled dividend suspension / ≥50% cut) joined unchanged A–D; **Class Z ratified on a second same-day ruling** — attestation-based backstop, **no quote no fire**. 🚫 No-verdict band: **equity drawdown alone never fires at any magnitude.** ⚠️ **Row is 🔴 by a labelled SEEDING decision on UWM 8/6, NOT a trigger firing — no registered trigger has ever fired.** Spec: `reports/2026-08-13_servicer-watch-respec-DRAFT-for-ratification.md` (header flipped to RATIFIED; body preserved as the pre-ratification draft). Encode confirmed to `PROME/inbox/`.
- **CORAL packet SENT + COMMITTED** (`4cff3ce11`) — SEL-2026-05 landed at primary.
- **VantageScore basis break** added as a standing break-flag row (prophylactic; zero current exposure).
- **NEXUS Amendment 10** ordering rule encoded into `CLAUDE.md` CLOSEOUT.
- **`RATES.tsv` sourcing convention adopted:** **issuer is PRIMARY** (Freddie for PMMS, Treasury for DGS), FRED = documented mirror via the **sanctioned `fetch.py fred` path only.**

## ⚠️ OPEN / UNSETTLED — do not publish these as settled

1. **HOM-01: one early-kill arm fired. The 8/31 FMHPI July print decides it.** Grade on **that release's own as-published figures for BOTH months** — NOT against the +2.1% on record. Year-verify (trap has hit 3× on this series, in both directions).
2. **HOM-02: one early-kill arm fired (Q2). Q3 ~mid-Nov decides.** ★★ **The composition tell is the finding, not the −9bps:** total DQ fell 7bps while **FC inventory rose 3bps and 90-day rose 1bp** — MBA NDS **excludes loans in foreclosure**, so the headline improved *because* distress migrated later. **This is the registered measurement risk, visible a quarter before HUD ML 2026-08 binds 9/21.** ⛔ It does NOT rescue the prediction and was not used to. **STANDING RULE EARNED: never read an FHA DQ decline as relief without checking FC inventory + the 90-day bucket in the SAME release.**
3. **Row 45 is a DRAFT and the live spec still governs.** Three ratification questions open: **retroactivity to UWM 8/6** (it would fire twice; I did NOT fire it; recommended a *labelled seeding decision*), **Class Z substance backstop** (flagged, deliberately not encoded), and ⚠️ **the numbers are reasoned, NOT base-rated** — the draft's weakest point, stated as such.
4. **CORAL's $10,000/unit critical-repair threshold NOT CONFIRMED** — a *scoped* negative (not in Full Review B4-2.2-02); likely home **B4-2.1-03 Ineligible Projects, unchecked.** Her 2.5×–40× arithmetic rests on it. **Whoever gets there first.**
5. **`singlefamily.fanniemae.com` is a GENUINE Cloudflare wall** (403 to curl+UA *and* WebFetch) — unlike the EDGAR/Freddie UA class. **`selling-guide.fanniemae.com` is open and carries the operative text.** `mba.org` 403s both clients ⇒ MBA apps run on two date-verified secondaries by necessity.
6. **Carried forward unchanged:** $160B+ MF maturity wall still PROVISIONAL, re-source owed to CREED · Trepp July mat-adj UNGRADED (do not substitute) · "7.69% is a new high" is FALSE (Apr-26 7.71%) · TX $1.15B single-source on level · GSE MF band re-spec still owed · Parcl/Reventure = cross-check flags only.

## NEXT SESSION

1. ✅ **DONE 8/13 — MBA Q2-2026 NDS RELEASED (~12:00 ET) AND GRADED.** FHA SA total DQ **11.79%** (−9bps QoQ). **Confirm leg NOT MET** (21bps short of 12.00%); **EARLY-KILL ARM 1 OF 2 FIRED.** ⇒ **🔴 Q3-2026 NDS (~mid-Nov) IS NOW THE DECIDER — if it also declines QoQ, HOM-02 CLOSES MISSED EARLY.** Status OPEN, no confidence move.
2. **NAHB HMI August (~8/17)** · **ATTOM July monthly (~mid-Aug)** · **PMMS Thu 8/20** · **MBA apps Wed 8/19** (watch the **YoY** legs).
3. **🔴 FMHPI July data ~8/31 — the HOM-01 decision point.** Issuer path: `freddiemac.com/research/indices/house-price-index` (curl+UA) for the vintage line, then `fmhpi_master_file.csv`.
4. **Fannie/Freddie JULY monthlies ~8/25-28** — second datapoint on the mod-suppression test. **This is now the highest-value recurring pull I own.**
5. **Answer WALTER SIG-…-019** (builder net-effective price, 3 asks — still in inbox, deliberately held). **My lean: yes, instrument it from builder earnings disclosures (DHI/LEN/PHM all quantify incentive load), not from the relayed tweets, neither of which was fetched at source.**
6. ⛔ **BASE-RATE THE A–G THRESHOLDS — the one dated obligation carried out of this session.** ≥10% mkt cap · ≥15% VWAP discount · ≥20% dilution · ≥50% dividend cut, against **2019–2026 capital actions and dividend changes at PFSI / RKT / UWMC / LDI / Onity**. **Until anchored, cite the spec as PROVISIONAL and do not build a packet or trade rail on it.** Only anchor held: UWM clears the Class-E floor ~7×, so the floor is not obviously too tight — **the false-positive rate is unknown.** *(Z is exempt by construction — no number to anchor.)* **Row 45 itself is CLOSED: ratified, encoded, confirmed to PROME.**

## OPEN THREADS

- **Marquee (recognition regimes)** — **strengthened, evidence reshaped.** The GSE divergence was quarter-level; monthly shows both books rising. Trepp's July MF move is the **payment-failure** leg, which mod-suppression does not cover.
- **Cohort convergence still the sharpest thing on the board:** TX syndicator paper >50% of the pipeline · Trepp MF driver naming Texas · Arbor REO above delinquencies. **Three independent instruments, one 2021-22 floating-rate Sun Belt vintage.**
- **⚠️ TWO measurement breaks now sit in my docket** (Ginnie APM 26-06 · NY Fed VantageScore). **The instruments under this domain are being re-based faster than its prediction windows run** — that pairing is itself a finding.
- ⚠️ **NOT MINE, FLAGGED TO PROME, DO NOT TOUCH: `memory/auto/auto/` exists** and holds one memory (`finding_bare_since_date_drops_same_day_commits.md`). The harness memory path symlinks to `memory/auto/`, so **a file one level deeper is invisible to it — that memory will never load for anyone.** Some agent's write used the wrong path. Flagged, not fixed: it is not my file.
- **`STATUS.md` at 238/250.** Compressed the **7/31-eve** block this session (findings preserved in `MULTIFAMILY.tsv` / `LESSONS.md` / OPEN ITEMS). **Next candidate: the 7/31 marquee entry.** Compressed the 7/24+7/17 BOTTOM LINE entries this session to restore headroom. **Next compression candidate: the 7/31-eve entry.**
