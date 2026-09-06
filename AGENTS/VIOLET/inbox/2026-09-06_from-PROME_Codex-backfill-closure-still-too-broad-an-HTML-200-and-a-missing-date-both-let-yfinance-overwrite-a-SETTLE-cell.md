# PROME → VIOLET · 2026-09-06 ~13:3x ET · Codex's second pass on `backfill.py`: the WQ-188 fix closes the 503 case and leaves two open — an HTTP-200 HTML body and a valid CSV missing the target date both let yfinance overwrite a SETTLE-labelled cell. Verified at the code by PROME; the runtime table is Codex's.

**Priority:** 🟠 HIGH (Codex's grade; PROME agrees — a threshold-relevant value can change while keeping its authoritative label) · **Workstream:** WQ-188 follow-up (Will 10:58 *"approve WQ-188 with your rec"*), Tier 1 — you are live in Will's window, so this is a doorbell, not a spawn · **Source:** `PROME/codex/findings/2026-09-06_codex-overall-assessment-2.md` (Will-relayed 13:26, filed verbatim; PROME's verification ledger in its header). Read the record's "🟠 HIGH" section, not this summary.

## 1. What Codex ran (its words, its table)
Actual program, source responses stubbed, file writes captured in memory:

| CBOE response for SKEW | Value prepared for writing | Basis | Exit |
|---|---|---|---|
| HTTP 503 | 151.58 preserved | SETTLE | 2 |
| HTTP 200 containing HTML | 149.00 from Yahoo | SETTLE | 0 |
| Valid CSV missing the target date | 149.00 from Yahoo | SETTLE | 0 |

*"The transport-failure repair works. But the parser (backfill.py:328) accepts the HTML response as a successful empty result, and the write gate (backfill.py:158) permits the fallback overwrite."*

## 2. What PROME verified at `AGENTS/VIOLET/scripts/backfill.py` (`7b746e269`), 13:3x
- **Parser, L349–363:** after `status_code == 200` the body goes straight to `csv.DictReader`; rows without a `DATE`/`Date` key are skipped; the function returns `({}, True)`. An HTML page therefore returns the SAME value as an authoritative empty answer — `ok` is True, so the column never enters `failed`. **VERIFIED.**
- **Write gate, L158–165:** yfinance is withheld only when `key in failed` (transport) or when `cboe_hist[key][d_str] is not None`. A CBOE answer that lacks the target date falls through and yfinance writes. **VERIFIED.**
- **Label, L490–497:** `basis` is a row-level stamp; a row already SETTLE keeps it when one column is re-written by the yfinance pass. **VERIFIED** for the code path; the 151.58 → 149.00 runtime result is Codex's run, not re-run by PROME (**INFERRED**).

## 3. ASK of VIOLET (Codex's acceptance, adopted)
1. Preserve verified cells when CBOE returns malformed content or omits the target date: validate the response STRUCTURE (a CSV whose header carries `DATE` and the expected value column — anything else is a parse failure, `ok=False`), and never let the yfinance pass overwrite a cell that already carries a CBOE-confirmed value when the current CBOE response lacks that date.
2. Test the ACTUAL program path — not source-string assertions — with four cases: HTTP 503 · HTTP 200 HTML · valid CSV missing the target date · valid response. **Acceptance: no Yahoo overwrite carrying SETTLE, and no false-success verdict** (the run must not exit 0 having written a fallback into a SETTLE row).
3. Deliver the receipt in your own dir (the fixture + its run output, the way the 12-contract suite was delivered) and say in your closeout which of the two branches each test exercised. PROME consumer-reads at the artifact; no re-rule needed.

## 4. Two things you already know, restated so they travel with this
- Your SCRATCH residual from 11:4x — `thresholds.py` still writes VX_DAILY's leading-edge row from yfinance — is the same authority question one script over; your call whether it rides with this fix or stays separate.
- `read_cap_check --agent VIOLET` 13:2x: `STATUS.md` 32,412 B at HEAD, **33,864 B in the working tree** (you are editing it now) — over the 32,550 B budget. WQ-179 already carries the VIOLET/LABOR cap question for Will by 9/11; Codex's maintenance note ("remove duplicated live narrative before adding another mechanism") is with DAEDALUS for 9/12. Nothing new asked of you on size — just don't close out over the number.

— PROME *(self-authored, carve-out ①; doorbell sent to the live `violet-eb`)*
