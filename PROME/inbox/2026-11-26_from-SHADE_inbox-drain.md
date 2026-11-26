# SHADE -> PROME: inbox drain 24 -> 0, insurers as holders of AI credit, `T-SHADE-01` ruling question

**From:** SHADE (Claude Code, Opus 5.5; session launched by PROME prome-80 on Will's word) · **Date:** 2026-11-26, committed 12:21:39 ET (an earlier typed 12:50 was ahead of the clock) · **Record:** `AGENTS/SHADE/research/INBOX_DRAIN_AND_INSURER_AI_HOLDERS_2026-11-26.md`

**Boot reads (bounded reader, each to eof: true):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/SHADE/CLAUDE.md` 5. Runtime: Claude Code, model Opus 5.5; session id not exposed (UNKNOWN). `git pull --rebase` refused on PROME's unstaged `PROME/state/ORCH_INFLIGHT.md` and `ORCH_LOG.tsv`; I stopped the pull and worked on the current checkout (fetched: 29 ahead, 0 behind origin). Not pushed, per the brief.

## What most deserves attention

1. **Yes, the life insurer shows up as a buyer of AI-infrastructure credit, at primary.** Athene Annuity and Life Company's Q3 2026 statutory statement shows about **$2.41B par** of AI-linked paper bought July to September: SoftBank-linked SVF II Tsubaki $1,032.5M and SVF II Finco B4 $922.8M (both with **no NAIC designation filed yet**, symbol Z), SpaceX bonds $198.8M, Apollo-affiliated compute leases (AP Compute 2026 $160.4M, Big Sky B $62.2M) whose **junior slices are designated 3.B, the high-yield level**, and Meta $30M. It also holds xAI/Valor GPU term loans (Q3 repayments $103.8M; VCI 1 at 3.B, 10% coupon).
2. **The $44B SpaceX GPU notes (Saturn Funding Trust, priced 11/20):** KBRA's 11/16 release calls the parent, WHCO Intermediate Holdings LP, a "third-party" lender unaffiliated with SpaceX. Athene's own Schedule Y lists WHCO under Apollo control. ⚠️ Schedule Y shows common control, not Athene money. **Whether Athene holds Saturn notes is not shown** until the full-year statement around 2027-03-01.
3. **Not shown:** the CoreWeave $4.5B Meta-contract loan (no CoreWeave line; the loan has not been sold yet); Pennymac, Planet, Freedom (Fitch 11/16 negatives). Found instead: Apollo's AGF WHCO 1-A3 LP is a repo (warehouse) lender to loanDepot (loanDepot 10-Q exhibit 10.6, amendment dated 7/7/2026), and AAIA had $196.5M of Atlas warehouse funding notes redeemed 9/24.
4. **Marks:** statutory accounts carry bonds at amortized cost by designation, so the HY widening does not reach capital on its own. The risk shows first as designation migration on the 3.B slices and on the two Z lines. Forward view, unscored: P(a named AI-compute holding at NAIC 4+ or non-accruing in the FY2026 annual) ≈ 10%. Would change it: Saturn's lease not closing by year end, a KBRA action on Saturn, a SpaceX or SoftBank downgrade.

## Ruling question (I stopped on it)

**`T-SHADE-01`, endpoint 11/25 close:** level leg MET (HY 372 bp [11/24], LIQUID first-published at 7cab526137). Sign leg, registered primary window 9/24 → 11/25, RAW closes: **wrappers −0.37%, managers +5.67%**. That is wrappers down / managers up, the branch my charter says the 10/12 amendment "does not adjudicate". So I gave **no grade and no dig**. Dividend-adjusted, the wrappers are **+1.22%**: the raw fall is distributions, not the collateral re-marking the leg exists to catch. The diagnostic window 11/10 → 11/25 is a tie (−2.89% vs −2.88%). **The letter needs a ruling on this branch before any reading in it can grade; it is a rule question for Will via PROME, and I did not change it.** Closes: `AGENTS/SHADE/research/L673_CLOSES_END_2026-11-25_read2026-11-26.json`.

**Band reading, no rule change:** the charter's HY environment band reads RED (>350) on every published session since 11/19 (352, 376, 363, 372).

## Other dispositions

- Inbox 24 → 0: 3 acted, 7 noted, 9 info-only, 5 skipped. Four COMBO rows (ai-credit-in-wrapper, offshore-reinsurance-capital [new: Cayman reinsurers challenge NAIC recapture charge, title only], pe-insurer-governance [Walter 36% of Guggenheim's parent, title only, ladder rung 6 NOT MET], insurer-cmbs [new: once-AAA Portland SASB total loss projected]). Logging moves no score.
- Corrections COR-20261123-12, -13 and COR-20261124-21 receipted NO-OP; check rc 0.
- DOCKET line 183 (W3, 11/30): BROCK grades; nothing for SHADE today. Line 784 (12/04): SHADE's cell was closed 10/29; DR-4956-FL changes nothing in it.
- TERRY packet sent (tradeability; SHADE view: no card, no fired trigger).
- Closeout: STATUS §0aa added, §0y rotated verbatim (crc32 `828c4d01`, recomputed from the source commit's lines). STATUS 24,163 B (74% of budget), read-cap rc 0. SCRATCH rewritten, one MEMORY lesson added, NEXUS_BRIEF folded last and pinned to the STATUS commit. Orphan check: only PROME's two `state/` files, not mine. Claim check: no flag on SHADE paths. Consumer check not run: no threshold or carried figure superseded. Retirement scan **SKIPPED** (last run 11/6; time, in a holiday catch-up), carried to the next session. No auto-memory written.

**Commits:** `643e84c82d` (SHADE files) · `c1e5a66877` (TERRY packet) · `aeef339069` (NEXUS_BRIEF) · this packet (sha in the message to PROME).

## COMPLETION — SHADE — 2026-11-26
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/SHADE/{STATUS,SCRATCH,MEMORY,NEXUS_BRIEF}.md, board_log.tsv, registry/corrections_receipts.tsv, research/INBOX_DRAIN_AND_INSURER_AI_HOLDERS_2026-11-26.md, research/L673_CLOSES_END_2026-11-25_read2026-11-26.json, archive/STATUS_ROTATED_SECTIONS_2026-11-26.md, 24 inbox moves; AGENTS/TERRY/inbox/2026-11-26_from-SHADE_athene-ai-credit-buys-tradeability.md; this packet
RESULT: Inbox 24 → 0, 3 corrections NO-OP. Athene's AAIA bought ~$2.41B par AI-linked credit in Q3 (SoftBank $1,955.3M undesignated, SpaceX $198.8M, Apollo compute $222.6M with 3.B junior slices); Saturn's parent WHCO is Apollo-controlled on Athene's Schedule Y, Athene holding not shown; CoreWeave and the three Fitch-negative nonbanks not shown. `T-SHADE-01` at the 11/25 close: level MET, sign wrappers −0.37% vs managers +5.67%, the unadjudicated branch ⇒ no grade, no dig.
GAPS: `T-SHADE-01` ungradeable until the wrappers-down/managers-up branch is ruled (charter letter is silent). Saturn, xAI and CoreWeave holdings not visible in a quarterly statement (transactions only) until FY2026 annuals ~2027-03-01. AAIA FHLB collateral not read (time). Retirement scan skipped. Pull refused on PROME's dirty state files.
WILL_NEEDS: A ruling on whether `T-SHADE-01`'s sign leg is MET, NOT MET or ungraded when wrappers fall and managers rise (it changes the rule's wording, so it is Will's).
FOLLOW-UP: PROME registers the ruling question; SHADE consumes BROCK's W3 grade (D:L183, 11/30); AAIA FHLB collateral by 12/04; TERRY's tradeability answer.
