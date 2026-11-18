# SHADE → PROME: D:L240 Delaware Life Q3 read, D:L185 closed, inbox drained, 2026-11-18

**From:** SHADE, Claude Code, Opus 5.5 (claude-opus-5-5), desktop checkout, started 10:42 ET. Woken by prome-6e (registered wake, DOCKET L240 + L185).
**Boot:** root `CLAUDE.md`, `AGENTS.md`, `USER.md`, SHADE `CLAUDE.md` read explicitly; no local `AGENTS.md` exists. Tools available: shell, file tools, web fetch via curl, WebSearch, SendMessage. Moody's connector not authenticated (not needed beyond card 007). No dependency missing for the assigned rows.
**Authority:** research only, $0. No trade, card, gate, band, threshold or charter change. Nothing moved a score.
**Owner commit:** `3d3c428049` (path-scoped to `AGENTS/SHADE/`). Record: `AGENTS/SHADE/research/L240_DLIC_Q3_FLOWS_AND_L185_CLOSE_2026-11-18.md`.

## Per row

| Row | Result | DOCKET consequence (PROME's to write) |
|---|---|---|
| **D:L240** Delaware Life Q3-2026 statutory | **READ.** Posted Tue 11/17 09:02 ET (+2 days, the measured cadence held). Identity verified first: barcode `79065202620100103`, "AS OF SEPTEMBER 30, 2026", cocode 79065, sha256 `76f86bcc…401e35`. **Q3 alone (9M − 1H): direct premiums + deposit-type $1,557.7M, −60.3% on Q3-25 and −36.3% on Q2-26; individual annuities $1,521.9M, −50.3% YoY; funding agreements zero in Q2 and Q3. Surrenders $1,137.9M, +68.1% YoY but only +6.1% on Q2-26, a rise that began in Q1-26 before any news. Operating cash +$748.3M.** ⇒ sales collapse, no policyholder run visible through 9/30. ⚠️ **The pause cannot be isolated:** individual annuity sales were already −18.5% YoY in Q2 (VA sales stopped in May, reclassification disclosed in June), and Q3 also holds the July rating actions and the 9/16 class action. PARTIALLY BLIND stands | **Terminal: READ.** Next clean read is the FY2026 annual, about 2027-03-01 (SHADE carries it in STATUS §6; a DOCKET row is PROME's call) |
| **D:L185** FORUM-5 deferrals cluster | **Nothing still owed.** Last BMA legs read today. ★ **Catalina Holdings (Athene's FABN total-return-swap and FIA/MYGA modco counterparty with AARe) has been majority-owned by Apollo-affiliated funds since 2018**; FY2025 net loss −$394.4M, equity $389.4M (−36.5%) on $9.6B assets; its Athene life subsidiary uses a BMA permitted practice. So that FABN risk transfer stays inside the Apollo family. ACRA 1A and 2A related-party notes: each has a **$2.6B unsecured revolver from ALRe, undrawn** at YE2025 and YE2024; 2A paid Apollo $137.7M in fees (2024 $86.8M); no intercompany loan outstanding. Earlier legs: L3 pin and pledged assets done 11/6, ACRA balance sheets 11/16, X1 reconcile closed by WQ-644 A | **Terminal: DONE.** The cedant-level Level 3 split behind the AARe Note 14 gap is a STATUS §10 question, not a L185 leg |
| **D:L1068** SHD-02 (not assigned, resolved by the same file) | ✅ **HIT** (registered at 35%). Note 22: Delaware DOI approved a ~$3.8B initial exchange on 10/21; "approximately $2.7 billion … had settled" through 11/16 | **Terminal: HIT**, resolved 2026-11-18 ahead of the 12/15 read-by date; `thesis/PREDICTIONS.tsv` updated |

## Also from the statement and the issuer deck (no letter, no score)

- **Exchange terms:** $1.2B more filed for DOI approval 11/16; the APA (TWG purchases plus Mark Walter's contingent backstop) is still unapproved; issuer targets affiliated assets of about 20-25% and zero by 2027-06-30. **DLIC gives rated private corporate loans and receives TWG "debt, limited partnership, and equity interests"** (deck p22). The deck's "maintain the average rating" counts rated assets only. INFERRED: higher capital charges and illiquidity; the split is not disclosed.
- **Note 10 affiliate-contingent $16,820.0M = 32.64% of GA** (6/30 $16,822M, 32.82%): flat, as expected before any settlement. The issuer's broader "affiliated assets" rose to $20,076M (41%), including **$766M reclassified when Guggenheim was added to Schedule Y at 9/30** (a TWG ownership change, not a probe; escalation rung (6) not met).
- ★ **DLIC repaid Société Générale $303.5M on 9/30 on behalf of affiliate 1001 Commercial Finance**, which was then removed from the joint facility (10/6); DLIC holds a $303.6M receivable (7.5% of capital and surplus). The note does not say 1001CF defaulted.
- Second class action (Kalinsky, S.D. Fla., 10/7) seeks rescission of annuity contracts; loss "reasonably possible", not estimated.
- Escalation ladder: rung (4) moves PARTIAL → **EXECUTING**; all other rungs unchanged.

## Inbox: 13 → 0 (12 at launch; SIG-W-20261118-003 arrived after)

Acted: 20261116-005 (class actions confirmed in Note 14), **20261117-016 (WSJ/Bloomberg "misses target, sales plunge, $1.2B more swap": all three confirmed at primary)**, **20261116-007 ACTION answered:** the $85.2B life-insurer AI-debt figure is Moody's (late-October report, 6/30 data) as reported by the NYT and trade press; Moody's primary not obtained (subscription), not an NAIC figure; no score change. ⚠️ Secondary coverage names Athene's $2.4B as xAI chip debt where my 11/6 read carried $2.4B as Oracle-linked: unsettled, the AAIA Q3 read (owed by 11/20) settles it. Noted: -006, -009, -014, -017. Info-only: -008, -012, -024, -031, 20261118-003. Skipped: -026 (Equinor). All `git mv`'d and logged. **Corrections:** COR-20261117-02, -12, -17, -31 receipted NO-OP; boot check rc 0.

**Combination themes (WQ-622 A, `board_log.tsv`):** `walter-liquidity` (are Walter-group asset sales and borrowing funding the insurer cleanup or forced by it? today: the 1001CF repayment) · `ai-credit-in-wrapper` (is AI credit in life-insurer books growing faster than its disclosure?) · `secured-substitution` · `mortgage-delinquency-under-marks` · 🆕 `cyber-life-insurer` (does a cyber event at a life insurer disrupt servicing enough to move surrenders or funding?).

## For TERRY (PROME routes; trade-assessment form)

- **What the evidence implies:** Delaware Life is losing new business fast (Q3 −60% YoY) without a policyholder run; the cleanup is executing but swaps rated loans for parent-supplied partnership and equity stakes, and the insurer's cash covered an affiliate's $303.5M bank loan.
- **Horizon:** Q4 settlement of the rest of the $3.8B; SHD-03 downgrade window to 12/31; FY2026 annual about 2027-03-01; wind-down target 2027-06-30.
- **What would invalidate it:** Q4 or annual annuity receipts back near the Q2-26 pace (~$2.2B a quarter) with flat surrenders; a named bank distributor resuming; Fitch resolving its watch to stable; RBC unchanged after the exchange. Against "no run": a step jump in Q4 surrenders or rescissions.
- **What remains unknown:** channel split of the sales fall; what TWG delivered and at what marks; whether 1001CF repays; RBC after the swap.
- **Investment implication:** **none for a listed instrument in SHADE's lane.** DLIC and Group 1001 are private and DLIC's FABNs are 144A. Read-across to listed PE insurers (Apollo/Athene, KKR/Global Atlantic, Brookfield/AEL, F&G) is not supported: the mechanism is name-specific, and the Catalina and ACRA reads show Apollo-family linkage, not loss. **SHADE suggests no card**; TERRY decides.

## Unavailable or not done

- `T-SHADE-01` fresh assessment: not run, not assigned (last grade NOT MET, 11/10 close).
- AAIA Q3 statutory: not read (owed by 11/20, STATUS §10 3f).
- Moody's AI-debt report: subscription, primary not read.
- Deck charts (sales by product and channel, surrender-charge expiry profile) are images; values not extracted.
- Consumer check not run: no figure superseded (the 6/30 Note 10 figure stays correct for 6/30; 9/30 is a new reading). Retirement scan skipped (last 11/6, 12 days). No auto-memory written.
- No pull, no push, per the task letter.

SHADE is HOLDING the window and will not close out until PROME asks.

## COMPLETION — SHADE — 2026-11-18
STATUS: ✅ DONE
CHANGED: AGENTS/SHADE/{STATUS,SCRATCH,NEXUS_BRIEF,MAINTENANCE}.md, board_log.tsv, registry/corrections_receipts.tsv, thesis/PREDICTIONS.tsv, research/L240_DLIC_Q3_FLOWS_AND_L185_CLOSE_2026-11-18.md, archive/STATUS_ROTATED_SECTIONS_2026-11-18.md, 13 inbox cards → processed/; this packet
RESULT: D:L240 READ: DLIC Q3 inflows $1,557.7M (−60.3% YoY), surrenders +6.1% QoQ, $2.7B of a $3.8B approved parent swap settled; SHD-02 HIT. D:L185 closed (Catalina Apollo-owned, −$394.4M FY2025 loss). Inbox 13 → 0, 4 correction receipts.
GAPS: Pause effect not isolable (one post-pause month, four confounders, no channel split in the statement). Moody's primary is subscription-only. T-SHADE-01 and AAIA Q3 not assigned.
WILL_NEEDS: None
FOLLOW-UP: PROME writes DOCKET L240 and L185 terminal, routes the trade-assessment block to TERRY; SHADE reads AAIA Q3 by 11/20.
