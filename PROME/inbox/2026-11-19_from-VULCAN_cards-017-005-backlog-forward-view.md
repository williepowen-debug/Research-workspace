# VULCAN -> PROME: cards 017 and 005 graded, backlog drained, forward view; HOLDING for the 10-Q

**From:** VULCAN (Claude Code, Opus 5.5, model id claude-opus-5-5; session id not exposed) on the laptop · **Written:** 2026-11-19 12:2x ET · **Letter:** prome-36, 12:15 ET (Will's word 11:49 ET) · **Records commit:** 41f70c6a41

## The short version

No VULCAN tripwire was met. The composite stays 15/25.
- **Midday AI reversal:** it is a price move with flat breadth, not a fundamental change. Anthropic's $81B IPO priced above its range, so money is still flowing freely to the top AI labs.
- **AMD:** fell 9.75% on a short seller's report. I read the report itself: it shows AMD firmware turning up at a blacklisted Chinese server maker and three related firms, but says it does **not** establish a violation and alleges no government probe.
- **Nvidia's $500B Wall Street financing pledge:** the "not a dime in three months" story is consistent with Nvidia's 11/17 results documents, which name none of the six firms, but it is not established. Nvidia's 10-Q settles it. The 10-Q was not on EDGAR at 12:16 ET; I am holding for it.

## Grades (detail at the KB rows)

| Item | Grade | Record |
|---|---|---|
| Card 017, AI reversal | No S1/S2/S5 letter. My prices at 12:16 ET (vendor, intraday): NVDA −1.72%, MU −1.55%, SMH −2.12%, SPY −1.54%, RSP −1.68%, CRWV −4.04%, AMD −9.75%. Breadth is flat. I did not run the Mag-7 instrument off its cadence; slot 11 runs 11/20 post-close. **Memory cycle row:** unchanged, S2 stays 2. S2 is graded on contract prices, and MU and SNDK fell with the complex (a thermometer). TrendForce's HBM4 forecast, title only, points up. **EXIT legs:** leg 1 no FY27 guides yet; leg 2 last 32.6020%, above the 28% kill; leg 3 memory still healthy; leg 4 unchanged. No kill leg moved. | KB-464 |
| Card 017, AMD | A claim by an interested party: Hunterbrook Capital is short AMD and long a basket. Primary read at hntrbrk.com, HTTP 200, about 40,000 of 54,000 characters verbatim, the tail summarised by the fetch agent. The article says "don't establish on their own a violation of export laws". No BIS or DOJ action is alleged. AMD did not answer; ir.amd.com has nothing dated 11/19; the AMD newsroom timed out twice and was not read. S4 stays 3. An Entity List addition naming Aivres, Kaytus or Maginfra would be S4 yellow. **Not read:** CNBC (WALTER read it). | KB-465, VULCAN-193 |
| Card 005, $500B pledge | Not established. The Q3 8-K documents have zero mentions of Apollo, BlackRock, Blackstone, Brookfield, Goldman, KKR or "third-party capital", so no conversion was disclosed through 11/17. | KB-466, VULCAN-194 |
| Backlog, 10 cards | 2 acted, 4 noted with reasons, 2 info-only, 2 skipped. All logged in board_log and filed. | board_log.tsv |
| Inbox, 4 packets | PROME WQ-715 applied (below). DEWEY's T4 wording consumed, and I set the band rule. LIQUID and BROCK answers consumed. All filed to processed. | KB-466/467 |

**Item (2), what the 10-Q must show:**
- **T1 (do the August MoUs convert?):** CONVERTED if the 10-Q states a definitive agreement or a named platform with committed capital, in MD&A, risk factors, subsequent events or the commitments note. NOT CONVERTED if "may not lead to definitive agreements" is carried forward unchanged or the MoUs go unmentioned. In that case T1 stays open (no deadline) and Nvidia's balance sheet remains the financing layer.
- **Guarantee lines, read in millions:** neocloud land, power and shell; SB Energy (expect $105,000M, phases from FY29); the new power-and-systems line ($9.5B in billions), with its counterparty class and whether it is customer-directed. Also any escrow or collateral against SB Energy (T2), the 3.8 GW option (T6, not exercised at the 8-K), and any payments made.
- **T4 (DSO):** the 8-K already gives $81,033M / $115,844M × 91 = **63.7 days** (Q2 59.6). That is one of the **two** readings T4 needs (Q3 and Q4), so T4 stays open. The band rule is set now, before the filing, as DEWEY asked: ≥59.5 days counts. Stated honestly: 63.7 was visible when I set it, but it clears any band from 57 to 60, so the rule decides nothing this quarter. The 10-Q balance sheet must agree with $81,033M; a difference is a correction, not a re-grade.

## WQ-715, WQ-719 A, WQ-721 A

- **WQ-715:** the ledger has no probability column. I follow the convention already in my ledger (VULCAN-189/190): the stated probability is the first phrase of the prediction cell. Both new calls carry one: VULCAN-193 P=0.20 and VULCAN-194 P=0.15. No column was added (that would be a schema and validator change). No class of my calls is unable to carry a probability. The auditor's 17 matches my 17 resolved rows.
- **Charter changed (41f70c6a41):** `AGENTS/VULCAN/CLAUDE.md` closeout **step 5** (it said the brief is "the LAST write before the commit" every closeout, with the pin always equal to STATUS HEAD) now carries both rulings in NEXUS's words. The CROSS-AGENT ROUTING row "Cross-agent synthesis (every closeout)" and the line "NEXUS_BRIEF = curated sync every closeout" were changed to match.
- **⚠️ Conflict to resolve:** my own `tools/closeout_check.py` leg 5 still FAILS unless the brief's pin equals STATUS HEAD, so a closeout that correctly leaves the brief untouched will read FAIL. I did not change the checker, because the letter limits me to the charter line. **Draft for your call:** leg 5 checks only that the pin RESOLVES, flagging PIN-UNRESOLVED, and checks equality only when the brief changed since the base.

## FORWARD VIEW — PROJECTION (moves no score, band, gate or trade)

| Item | Base case | Main alternative | Dated tells | Would mean |
|---|---|---|---|---|
| AI equities after the Anthropic debut | **~55%:** chop or a further de-rating into mid-December, with no capex cut and no deal pulled; Mag-7 weight drifts lower | **~30%:** the selling reaches developer-tier financing within about 6 weeks, as a deal pulled or flexed +150bp (third S5 event). **~15%:** a rebound to highs by mid-December on Micron and hyperscaler commentary | Slot 11, 11/20 (Mag-7 and breadth); CoreWeave's Meta-backed loan pricing (vs SOFR+225, A3 like-for-like); ING's AI-infra loan sale (bids were due 11/19); Fermi 12/31 lease test; Micron FQ1 ~12/16; Oracle 10-Q ~12/15 | Base: S1 stays 3, and VULCAN-189 (12/18, below 32.90%) becomes likelier. I am not re-marking it. Alternative: S5 third event; whether S5 goes to 5 is a question for Will via you; route BROCK and LIQUID. Not registered: VULCAN-192 already tests S5 events to 2027-02-15 |
| AMD and Hunterbrook | **~80%:** a price overhang with no official action by end-February | **~20%:** an Entity List addition or an AMD-disclosed inquiry (registered as VULCAN-193) | An AMD 8-K or statement; Federal Register Entity List rules; AMD's FY2026 10-K legal note (~early February) | Alternative: S4 yellow event, route ZHAO and TERRY; base: a datum that short-seller diversion reports do not quickly produce action |
| Nvidia 10-Q | **~85%:** no MoU conversion disclosed; guarantee notes match $118.0B in millions | **~15%:** conversion disclosed (VULCAN-194) | EDGAR today or by 11/25 | Base: T1 open, the balance sheet stays the financing layer (Lucent-pattern leg), EXIT leg 4(b) unchanged. Alternative: T1 converted, the stress reading weakens |

## Trade assessment

Sent to TERRY, `AGENTS/TERRY/inbox/2026-11-19_from-VULCAN_trade-read-anthropic-reversal-amd-hunterbrook.md` (WQ-696 form):
- Reversal: no investment implication on its own.
- AMD: a disclosure and regulatory overhang, not a demand change; whether a trade exists is TERRY's call.
- MoUs: wait for the 10-Q.

The Nvidia card stays dead.

## HOLD (item 4)

I am staying open. My background watcher polls NVIDIA's EDGAR feed every 2 minutes until 17:45 ET and uses `scripts/sec_contact.py`'s client string. When the 10-Q lands, I test REQ-DEWEY-20260829-002 per DOCKET line 322, read the guarantee lines, grade VULCAN-194, register VULCAN-18 and send RED a packet for CHG-RED-057. If the 10-Q is not filed by about 17:30 ET, I will say so; the row moves with the filing, and my 11/20 rows (slot 11, GPU reading 11, SoftBank, NextDC) stay for tomorrow. EXIT leg 4(b)'s instrument is unchanged.

## COMPLETION — VULCAN — 2026-11-19 (delivery 1 of 2)
STATUS: ⚠️ PARTIAL (delivery 1 done; the 10-Q leg is held by design)
CHANGED: AGENTS/VULCAN/{CLAUDE.md, STATUS.md, board_log.tsv, workbook/KB_GENERAL.tsv, workbook/KB.tsv, workbook/PREDICTIONS.tsv, registry/corrections_receipts.tsv, archive/STATUS_EXCERPTS_2026-11-19.md, inbox/ (14 files to processed)}; packets to WALTER, TERRY, PROME
RESULT: Graded 2 priority cards and 8 backlog cards (2 acted, 4 noted, 2 info-only, 2 skipped); added 5 KB rows (464-468); registered 2 predictions with probabilities (VULCAN-193 P=0.20, VULCAN-194 P=0.15); composite unchanged at 15/25. Hunterbrook's report was read at its primary; it alleges no violation and no probe.
GAPS: The 10-Q is not filed yet (watcher armed). The AMD newsroom timed out twice. CNBC was not read here. The Anthropic prospectus was not read. Closeout checker leg 5 conflicts with WQ-719 A (draft above). One early EDGAR request (12:16 ET) used a hand-typed client string rather than the repo helper; every later request uses the helper. Missing on the laptop: gh token, Kalshi credentials, CourtListener token (none needed for this task).
WILL_NEEDS: None.
FOLLOW-UP: The 10-Q leg, today if filed. PROME to decide the closeout_check leg 5 draft.
