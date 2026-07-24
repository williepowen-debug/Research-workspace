# CORAL SCRATCH — 2026-07-24 ~11:25AM ET (PROME-spawned scoped: SSB Q2 adjudication + HOA transcript-mine)

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (7/23 AMC gate-day re-run)

PROME-spawned deferred-grade session. **Two headline outcomes:**

1. **SSB Q2 GRADED BENIGN (0-of-4 pre-registered axes).** Entity disambiguated first (load-bearing per spawn packet): **SSB = SouthState Corporation, NYSE:SSB**, Winter Haven FL — **NOT Seacoast Banking Corp of Florida (ticker SBCF)**, a different bank printing separately 7/28. Confirmed via CORAL's own prior CLUSTER_FL_BANK_LEG.md text ("SSB [SouthState, FL-HQ, multi-state SE]"; "CORAL short thesis retired [SSB $90P expired worthless]") and EDGAR company lookup (CIK 0000764038, "SouthState Bank Corp"). Pulled Q2 8-K direct (EDGAR acc. 0001104659-26-086278, filed 7/23 4:25PM ET; WebFetch 403'd as usual, curl+UA worked). All 4 axes graded BENIGN: NCO 6bps (↓ from 9bps Q1), provision $15.9M growth-funded (loans +$1.4B/11% QoQ, ACL ratio fell — no named specific reserve, same standard already applied to USCB), ACL 1.15% declining, NPA/classified/special-mention all down QoQ. Strictest-reading check done: even conservative provision-as-deteriorating reading is only 1-of-4.

2. **Q2 SYNC-BAR IS NOW MATHEMATICALLY CLOSED — the most important state-file consequence this session.** With SSB benign, six of seven FL/near-FL Q2 surfaces are now BENIGN (CCBG, BKU, VLY, USCB, AMTB, SSB). Only SBCF (7/28) remains, and the sync diagnostic requires **≥2** synchronized deteriorating names — one bank alone cannot satisfy that bar no matter how badly it prints. **Flagged prominently to PROME/REGINALD:** SBCF 7/28 should be reframed from "gate decider" to "single-name mechanism confirm/disconfirm" feeding next quarter's baseline, not this quarter's synchronization test. This is a framing change, not a rail move (rail stays untouched, 0-of-≥2).

3. **HOA transcript-mine (ML-CORAL-046) — partial, honest.** Only VLY's call transcript was live (Motley Fool, read in full — zero HOA/condo/association/SIRS mentions). AMTB and SSB calls both happened today 9AM ET but transcripts were not yet posted as of this session (~11AM ET; checked Motley Fool direct URLs, got 404s, not just absent from search). USCB's call hasn't even happened yet (11AM ET today). All 4 press releases/decks were grep-checked fresh regardless (SSB ex-99.1+ex-99.2 today; AMTB re-verified) — zero HOA/condo/association disclosure across the board, consistent null result. **Did not fabricate or guess at transcript content that doesn't exist yet.**

## WHAT I DID THIS SESSION

- Boot: CLAUDE + STATUS + SCRATCH + CLUSTER_FL_BANK_LEG + FL_BANK_WATCHLIST + CALENDAR + yesterday's grade packet, per spawn instructions.
- Confirmed SSB entity via EDGAR company-search atom feed (CIK 0000764038, "SouthState Bank Corp", Winter Haven FL) before pulling anything — load-bearing disambiguation done first.
- Pulled SSB 8-K ex-99.1 (press release + financial tables) and ex-99.2 (earnings presentation w/ classified/special-mention trend charts) via curl+UA; parsed HTML to text; graded mechanically against the frozen `FL_BANK_WATCHLIST.md` 4-axis read-shape (no new axes invented, no thresholds moved).
- Ran the "strictest reading" sanity check on the one judgment call (provision growth-driven vs notable-$-increase) — verdict unaffected either way (0-of-4 vs 1-of-4, both far below the ≥3 bar).
- Pulled live SSB price (fetch.py, $106.08 +4.77%) rather than citing a stale STATUS number.
- WebSearched + WebFetched for USCB/VLY/AMTB/SSB Q2 call transcripts; confirmed VLY's is live (read, zero HOA hits) and AMTB/SSB's are not yet posted (404 on direct URL, not just search-absence) and USCB's call hasn't occurred yet (11AM ET today).
- Re-verified AMTB's press release fresh (grep for hoa/condo/association — zero hits) to have an independently-confirmed null across all 4 releases this session, not just relying on yesterday's grading notes.
- **Files:** FL_BANK_WATCHLIST.md (row 6 SSB, headline, live-window, old Q1-table SSB row), CLUSTER_FL_BANK_LEG.md (diagnostic status + reconciled-number addendum), STATUS.md (new 7/24 block + header + Signal Status line), workbook/KB.tsv (ML-CORAL-052), CALENDAR.md (7/23 row closed, SBCF row reframed), outbox `2026-07-24_to-PROME_ssb-q2-adjudication-and-hoa-transcript-mine.md`, this SCRATCH.
- Commit local, pathspec-only. Push via `scripts/safe-push.sh` at closeout (defer if non-ff / foreign dirty tree).

## NEXT SESSION (mechanical, in order)

1. **HOA transcript-mine completion (ML-CORAL-046) — the one open loop from today.** Re-pull Motley Fool (or Seeking Alpha/Investing.com as fallback) for AMTB, SSB, and USCB Q2 call transcripts later today/tonight once posted. USCB's call is 7/24 11AM ET — transcript won't exist until well after that. Grep each for hoa/condo/association/SIRS/special assessment; update this file + FL_BANK_WATCHLIST + KB with the completed 4-of-4 read. If the null result holds across all 4 transcripts too, that's the clean close of the window's last unobservable per SCRATCH's prior framing.
2. **Tue 7/28: SBCF Q2 (AMC, call Wed 10a)** — now graded as a single-name mechanism confirm/disconfirm, NOT a sync-gate decider (gate is mathematically closed regardless). Sharpest pre-registered tell unchanged: nonaccrual 3rd consecutive rise >$95M + CRE-non-OO charge-off/specific reserve build. Read the whole aging ladder.
3. **Wed 7/29:** BLS metro employment (June) — Ocala UR; Amendment-3 ballot-language hearing (pre-reg ML-CORAL-042/037).
4. Carried unchanged: Bertha already dissipated (resolved 7/23); HO-premium reconcile (resolved 7/23); FL Realtors county cash-share build (done 7/23); Sep-Oct Citizens takeout dates.

## OPEN THREADS

- **Bank-transmission gate: NOT met, 0-of-≥2, and MATHEMATICALLY CLOSED for Q2** — this is a state upgrade from "gate day incomplete" to "gate day complete and closed." Pre-registrations frozen, do not re-fit.
- **MSI supply-side leg: 🔴 FIRED + Will-ratified 7/23** — unaffected by today's bank-leg work, separate leg, still applied across all surfaces.
- **HOA transcript-mine: 1-of-4 complete, 3-of-4 pending posting** — the one incomplete deliverable this session, honestly flagged rather than guessed.

## MAIL STATE

- `inbox/` (root): NOT scanned (narrow one-off spawn — protocol step 8/9 exemption, consistent with 7/23 session). `inbox/WALTER/`: not scanned.
- `outbox/`: NEW `2026-07-24_to-PROME_ssb-q2-adjudication-and-hoa-transcript-mine.md` (🟡, PROME receives report directly). Prior 7/23 gate-day note, 7/22 BKU note, 7/21 muni-credit memo still in root outbox (in-flight/delivered-pending-sweep).
- Other agent sessions may be LIVE on box — committed pathspec-only per protocol; push deferred if non-ff.
