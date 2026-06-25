# CORAL SCRATCH — 2026-06-25 (transmission-terminus cluster Pass-1: DEWEY timing + FL-bank leg grid)

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION

- Spawned by Prome as the **FL regional-bank CRE/condo leg** of a 3-agent transmission-terminus cluster (REGINALD = bank-terminus hub, CARL = consumer-credit substance). Shared brief: `PROME/synthesis/2026-06-25_transmission-terminus-cluster.md`.
- Ingested 3 queued WALTER signals (now 0 pending): **SIG-W-20260622-001 (DEWEY Phase-3 timing packet, acted)**, SIG-W-20260621-011 (ResiClub price-easing reconcile, acted), SIG-W-20260621-013 (national builder overhang, info-only).
- **Got the FL-bank loss-transmission TIMING answer** (the #1 open question): cost-shock-now + ~12mo lag → 30-89d a H2-2026 event already flickering (SBCF $17.2M→$28.2M; AMTB NPA→1.93%) → NCO concentrated 2027. Winter-26/27 acute call holds for charge-off stage, slightly conservative on the leading edge.
- **Insurance walk-back:** +18.8% uncapped commercial = UNVERIFIED this run (unparseable OIR PDF); only +10.4% capped holds. Split-mark intact.
- **AMTB attribution confirmed correct on my side** — the $24.6M/76%-coverage/CET1-12.2% block is BKU not AMTB; my rows already attribute right. Flagged to REGINALD anyway.

## WHAT I DID THIS SESSION

- Logged 3 WALTER rows to `board_log.tsv`; `git mv` all to `inbox/WALTER/processed/`.
- **Built `CLUSTER_FL_BANK_LEG.md`** — the FL-bank leg of the Q2-print convergence grid (AMTB/SBCF/USCB/BKU/VLY: feeding legs, predicted Q2 signal, FL single diagnostic, falsifier, current read) + the timing chain + 4 reconciliation flags + what I need from REGINALD/CARL. **This is the primary handoff.**
- Updated `STATUS.md`: new 6/25 timing block (READ FIRST), insurance dashboard-row walk-back, Open-Q#1 with diagnostic + DEWEY datapoints, header.
- Updated `FL_BANK_WATCHLIST.md`: SBCF → ELEVATED (30-89d flicker + 224% non-OO RBC), AMTB NPA-of-assets + thin-coverage framing, BKU-attribution note, insurance walk-back, headline.
- Added `KB.tsv` ML-CORAL-024 (timing finding, DEWEY-grade research-not-verified-primary).
- Refreshed `NEXUS_BRIEF.md` As-of + SENDING/VIEW for the timing read.
- Reported to Prome (`team-lead`) via SendMessage.

**Follow-on passes (same session, cluster iteration):**
- **Housing-secured reconciliation** (CARL overlap): spawned sub-agent → **VERIFIED Q1'26 resi 1-4 family %loans** (AMTB 25.6 / SBCF 25.0 / BKU 24.7 / USCB 15.5 / VLY 11.5; HELOC only VLY 1.4% discrete). 3-way partition: net resi 1-4 fam ONCE (shared w/ CARL), CRE/condo CORAL-only, pure-HELOC negligible. → `CLUSTER_FL_BANK_LEG.md` + KB ML-CORAL-025. Commit 245cfc52.
- **FINAL FL FILL** (completes master grid): spawned sub-agent → **VERIFIED 10-Q XBRL 30-89d aging**. Key refinement of DEWEY: SBCF $28.2M +65% YoY but **−14% QoQ off Q4 peak** (sharper signal = nonaccrual $72→95M); AMTB $88.6M lumpy commercial-timing (suspect); USCB +43% YoY tiny-base; BKU ex-gov benign. Cleanest ≥2-bank synced = USCB+SBCF YoY, NOT NCO → diagnostic still NOT met. SSB/VLY = $0/not-isolable (defer to REGINALD fleet). Condo/SIRS = **2027 not Q2**. → `CLUSTER_FL_BANK_LEG.md` "FINAL FL FILL" + KB ML-CORAL-026 + watchlist SBCF QoQ-correction. Commit ee8c195e.

## NEXT SESSION

1. **Per-metro convergence grid** (the deferred build) — Miami / Tampa / Orlando / Jax / SW-FL, overlay negative-equity + the ~13mo Miami-Dade condo tail. Started conceptually; not yet a file.
2. **Q2 FL bank earnings (~late Jul, exact dates TBC — verify)** — run the grid's single diagnostic: synchronized criticized/classified → realized NCO + specific reserve build across ≥2 FL banks. Watch SBCF 30-89d migration, AMTB ACL build off thin ~45%, USCB's $126M condo-assoc book for first crack.
3. **MARCO reconcile** — Miami-Dade condo months-supply: ~13.2-13.7mo (DEWEY/Redfin) vs 12.9mo (CORAL/By-The-Sea Apr) — reconcile to one number; MARCO is live owner.
4. **Re-pin DEWEY's academic sources** — the ICE McDash insurance→delinquency working paper authors/citation were "recovered, to be re-pinned"; the ~12mo lag is a national single-family analog, not FL-condo-specific (external-validity caveat).
5. **Verify exact Q2 print dates** for AMTB/USCB/SBCF/BKU/VLY (I used ~late Jul placeholders in the grid).

## OPEN THREADS

- **Bank leg timing (resolved-ish):** early-delinquency H2-2026 (flickering now), synchronized NCO 2027. Q2 predicted = continued migration, not crystallized loss.
- **Substance-vs-beta (cluster input):** my FL read says the cost-shock substance is REAL and *building* but has NOT converted to bank loss — supports "stress is real but transmission lagged," i.e., the widening is not yet bank-substance. CARL's consumer read is the cross-check.
- **DEWEY grade:** research-output NOT verified-primary (EDGAR 403). Mechanism/direction solid; exact timing + bank attribution inferred. Don't over-weight.

## MAIL STATE

- `inbox/WALTER/`: **0 pending**; processed SIG-W-20260622-001, -011, -013 into `inbox/WALTER/processed/`.
- Legacy `inbox/`: 1 stale REGINALD BayFirst SBA signal (2026-03-04, not processed; outside scope).
- `outbox/`: none — cluster handoff is via `CLUSTER_FL_BANK_LEG.md` + SendMessage to `team-lead` (not outbox).
- **Pending push:** all commits local-only (Will-coordinated push). **3 commits this session:** 1d371108 (Pass-1 leg grid + DEWEY timing), 245cfc52 (housing-secured reconcile), ee8c195e (FINAL FL fill). Note for next push window.
