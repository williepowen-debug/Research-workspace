# SHADE MEMORY — Persistent Learnings
**Created:** 2026-06-15 ET

Durable SHADE-specific learnings. This is the tier between ephemeral `SCRATCH.md` and cross-agent auto-memory. Keep it short; promote transferable process lessons to auto-memory and remove duplication here.

---

## Domain boundary — SHADE vs BROCK

- **BROCK owns asset/fund stress:** private-credit funds, BDCs, interval/non-traded BDCs, redemption gates, PIK, dividend cuts, NAV marks, CLO/BDC mechanics, alt-manager equity tape.
- **SHADE owns insurance-wrapper transmission:** PE-owned insurers, captive/offshore reinsurance, statutory reserve credit, affiliated assets, Schedule BA/private-credit holdings inside insurers, FABN/FHLB/funding-agreement liabilities, NAIC/SVO/AG 55/PBR regulatory pressure.
- Trigger SHADE when the question becomes: **did the insurer wrapper absorb, hide, finance, or amplify private-credit stress?**
- Do not duplicate BROCK's fund dashboard. Reference BROCK facts with `[CONF BROCK date]`, then analyze the insurer balance-sheet/funding consequence.

## Core transmission question

Private-credit impairment becomes more dangerous when it enters an insurance wrapper that is:
1. liability-matched on paper but exposed to illiquid/Level-3/affiliated assets;
2. dependent on optimistic statutory treatment, permitted practices, or offshore/captive reserve credit;
3. funded partly through runnable or refinance-sensitive liabilities (FABN, FHLB advances, funding agreements, deposit-type contracts);
4. vulnerable to NAIC/SVO/AG 55/rating-agency changes that turn opacity into forced capital pressure.

## Source-quality caveats

- Statutory insurance filings and primary regulatory documents beat media summaries. Use annual statements / NAIC / state insurance filings / SEC filings when trade-relevant.
- Old SHADE `STATUS.md` contains March position rows and market prices. Treat them as historical until refreshed.
- Bank NDFI exposure numbers should be routed through REGINALD/BROCK/LIQUID owner docs before SHADE uses them as system-wide facts.

## SHADE forensic-discipline lessons

- **FHLB "borrowing capacity" ≠ the drawn book.** An FHLB figure on an insurer's IR liquidity slide is often *undrawn available capacity*, not advances outstanding. (6/21: baseline carried "$2.4B FHLB capacity"; the FI deck showed **$28B advances out / $38B pledged collateral** — the $2.4B was the undrawn line.) Always pull advances-outstanding + pledged collateral from the FI deck / statutory, and net encumbered assets out of the "highly liquid" cushion. Concrete instance of auto-memory `finding_number_carries_threshold_unit_source`.
- **A funding-spread threshold needs a peer-relative sub-row.** An absolute spread can sit in the green band while the issuer is the *widest* of its cohort. (6/21: Athene 5Y FABN T+123 = green absolutely, but +43–48bp vs IG peers = the load-bearing kill-path-1 canary.) The peer-relative penalty, not the absolute level, is the signal. Single-issuer-vs-peers variant of auto-memory `finding_blended_index_masks_bifurcation`.
- **Surveillance ≠ a rating action.** Authoritative quantification (Moody's/FSB/FSOC/Treasury/Proskauer) can rise in chorus while zero downgrades/negative-outlooks land on watchlist PE-insurers. Keep "rising attention" on the surveillance side of the green/yellow line until a rating-agency *action* or enforcement *escalation* actually fires. Catalyst ≠ consequence (`finding_catalyst_vs_consequence_conflation`).
- **APO price is not a SHADE stress gauge.** Athene is ~60% of Apollo equity value but the wrapper risk is a balance-sheet/funding/ratings mechanism that can crack while the equity holds. The March APO threshold band is a stale tape level; confirm the canonical APO mark with BROCK rather than carrying a fixed band as "green = no stress."

## Session arc

- **2026-06-15:** Prome architecture pass created SCRATCH/MEMORY/MAINTENANCE and modernized SHADE `CLAUDE.md` boot/write-back protocol, then did a live STATUS refresh (🟠 structural/latent).
- **2026-06-21:** First agent-run SHADE boot. WALTER intake (`board_log.tsv` created; SIG-008 `noted`). 5-vector adversarially-verified domain sweep of the 6/15→6/21 gap → net **relief/clock-advance, not breach**: NAIC CLO RBC slipped (MM-CLOs deferred to 2027), FSOC SIFI bar raised; offset by the Athene FABN peer-penalty canary (T+123, +43–48bp) + $28B FHLB correction + AMAPS disclosure-channel split. Retracted an inverted Nationwide/MassMutual reinsurance claim. Detail: `research/SHADE_BOOT_SWEEP_2026-06-21.md`.
