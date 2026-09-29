# SAM-42 DRAFT — Does the BOJ hike on October 30? (NOT REGISTERED — awaiting Will's word)

**Drafted:** 2026-09-29 10:21 ET. **Status: DRAFT.** It is not in `thesis/PREDICTIONS.tsv` and has no sidecar entry. It becomes a registered prediction only when this letter is committed to the ledger **before** the first new evidence lands (BOJ Summary of Opinions + Tankan, **Thu Oct-1 08:50 JST = Wed Sep-30 19:50 ET**). Registering after that is design-fixed, not time-fixed (WQ H4 rule), and would be labelled so.

## The call, in one line
**The BOJ does NOT raise its policy rate by October 31. SAM's probability of a hike: 25%**, against the market's ~36% (frozen below). **SAM is betting the market is overpricing October.**

## Letter (the exact row, as it would be pasted)

| Field | Value |
|---|---|
| **Pred_ID** | SAM-42 |
| **Date_Made** | 2026-09-29 |
| **Prediction** | The Bank of Japan RAISES its target for the uncollateralized overnight call rate above 1.25% at any Monetary Policy Meeting (scheduled or unscheduled) concluding between 2026-09-30 00:00 JST and 2026-10-31 23:59 JST. |
| **Confidence** | 25% (probability of TRUE, i.e. of a hike) |
| **Timeframe** | Registered 2026-09-29; resolves 2026-10-31 23:59 JST — IMMOVABLE calendar anchor |
| **Status** | OPEN |

### Resolution (MECE — every outcome lands in exactly one branch)
- **TRUE:** a BOJ *Statement on Monetary Policy* published in the window sets the call-rate target **above 1.25%**, of any size.
- **FALSE:** as of 2026-10-31 23:59 JST the most recent target announced is **≤1.25%**. This covers a hold, a cut, and a postponed or cancelled meeting (no hike by the date = FALSE).
- **NO-VERDICT (declared catch-all):** only if the BOJ replaces the uncollateralized overnight call rate as its operating target inside the window, so the letter's instrument no longer exists.
- **Grading basis:** the BOJ's own statement PDF (`boj.or.jp/en/mopo/mpmdeci/`, `k26MMDDa.pdf`), the **announced** target in JST. The effective date is irrelevant, and press reports never substitute for the statement.

### Anchor (why this date)
**IMMOVABLE.** Oct-31 is a calendar date nobody controls. The event it is built around (the Oct 29–30 MPM) *could* slip, and the letter handles that: a slip past Oct-31 grades FALSE, it does not hang (the rule on anchors that inherit an event's slip risk).

### Market reference — FROZEN at registration (value + date)
| Reference | Value | Basis / caveat |
|---|---|---|
| **Totan ICAP meeting-OIS, Oct-30 row** | **36%** incremental 25bp equivalent (OIS 1.3163%, +0.0892 vs the prior meeting) | Chart 2026-09-29 15:15 JST, SHA `ed4f664d…`, SAM transcription in `workbook/BOJ_MEETING_OIS.tsv`. ⛔ **An incremental 25bp equivalent is NOT strictly a probability** — used here as the market's reference, not as a number the grade reads. |
| Bloomberg swaps | ~30% October | 9/25 afternoon, secondary |
| Economist survey | 58% January, ~35% December | Bloomberg / Japan Times, 2026-09-28 |
| Momma (ex-BOJ ED) | 20–30% back-to-back | 2026-09-27 |

### Base rate (computed at registration)
BOJ hikes this cycle: **Mar-2024 · Jul-2024 (0.25%) · Jan-2025 (0.50%) · Dec-2025 (0.75%) · Jun-2026 (1.00%) · Sep-2026 (1.25%)** (web sources 9/29 for 2024–25; THESIS / KB-SAM-253 for 2026). Five intervals of **~4, 6, 11, 6 and 3 months: 0 of 5 back-to-back.** October would be the **first consecutive-meeting hike of the cycle**, six weeks after September. ⚠️ A cycle count of n=5 is a prior, not a rate: the BOJ is more hawkish now than at any point in it (July minutes: "anchoring", "double shock").

### Why 25%, not the market's ~36%
From :
- the 3-month pace and the 0/5 base rate;
- a board already split 7–2 with two dovish dissents;
- a verbal campaign that is working (USD/JPY 159.04 → 156.50), lowering FX urgency;
- the independence optics of moving six weeks after public US lobbying;
- domestic politics (the Diet opens Oct-5; ~75% floating-rate mortgages).

Against, and why it is not lower: political cover (the PM herself calls the weak yen a problem), hot inputs (services PPI +3.7%), hawkish July minutes, pricing that drifted **22% → 27% → 36%** over 9/18 → 9/29, and an Outlook-Report meeting.

### Premise, stated and marked (the rule on two-branch tests that share a premise)
- *"The US endorsement lowers the BOJ's FX urgency for October"* — **ASSUMED**, not observed.
- The TRUE/FALSE grade does **not** depend on it: the letter is outcome-only.

### Re-marks — pre-registered, the only ones allowed
The grade scores the **as-made 25%**. A re-mark is logged, dated and cited, never discretionary, and the calibration record keeps both marks.
- **(a) → 50%** if Ueda, Himino or Uchida publicly frames the October meeting as live before the BOJ's pre-meeting quiet period.
- **(b) → 45%** if a SAM-reviewed Totan chart shows the Oct-30 incremental equivalent **≥60%**.

Nothing else moves the mark: not a CPI print, not a USD/JPY level, not a wire story.

### Deliberately NOT registered (mechanism separated from outcome)
**"If the BOJ hikes in October, the yen strengthens on the decision."** This is SAM's real analytical claim: a hike about two-thirds unpriced should move the yen, where September's fully priced hike did not. **DEFERRED:** its base rate is not computable today — the only partial-pricing precedent is Jul-2024, n=1. Under the conditional-swap rule it is deferred, not registered un-base-rated. Can be registered separately if a base rate is built before Oct-29.

### Calibration note
Registered **below the market**. **A TRUE at 25% is a calibrated miss, not a broken thesis.** Worth registering either way, because the record is what makes SAM's BOJ reads checkable (the rule on registering a call you expect may lose).

### On Will's word, the mechanics
1. Paste the row into `thesis/PREDICTIONS.tsv` (9 fields, LF, no CRLF).
2. Add the sidecar entry to `docket/PREDICTION_SCHEDULE.json`: due 2026-10-31, timezone Asia/Tokyo, `condition_sha256` from `closeout_check.py`'s `_row_hash`.
3. Re-derive the scoreboard from the file (1 → 2 OPEN) on STATUS, THESIS § PREDICTIONS and the brief.
4. Add docket rows.
5. Commit **before Wed Sep-30 19:50 ET**.
