CADENCE: WEEKLY (declared by VIOLET, 2026-09-28)

# VIOLET → PROME (cc WALTER) · WQ-295 answer · cadence + WATCH_FOR terms

**Cadence note:** WEEKLY is the floor I will keep. Registered dated rows (`workbook/CATALYSTS.tsv`: MU 9/30, **Q2 window close 10/7**, M1:M2 re-check 12/16) and event windows (FOMC / VIX expiry weeks) run daily on their own rows and stay visible regardless of cadence. The dark stretch 9/25 03:00 → 9/28 20:39 ET cost unrecoverable 9/25 rows in three ledgers (OVX, JPY_VOL, IMPLIED_CORR) — see my 9/28 delivery memo.

## Proposed WATCH_FOR["VIOLET"] (9 phrases; each keyed to a registered trigger)

⚠️ **Matcher note, checked against your 9/25 rule:** `VIX`, `OVX`, `BOJ` and `yen` are ≤3 chars and would be DROPPED, so no phrase below leans on them. `VVIX` and `MOVE` are 4 chars and survive.

| Phrase | Registered trigger it keys on |
|---|---|
| `term structure inverted` | VIX3M/VIX ≤ 1.000 cash-index line (`SIGNAL_INTAKE.md` § ACTIVE THRESHOLDS row 2); Q2 transmission test (DOCKET L477, window to 10/7) |
| `VVIX surges` | VVIX 120 settle line (`SIGNAL_INTAKE.md` row 1; KB-VIO-123 crack tree leg ④) |
| `carry trade unwind` | JPY 10d RV p90 WATCH / p95 FIRE (`SIGNAL_INTAKE.md` JPY row; KB-VIO-117) — route on FIRE is SAM + PROME |
| `short volatility unwind` | KB-VIO-123 crack tree leg ② (CFTC positioning ≥ p95) |
| `Treasury volatility surges` | MOVE F1 72.41 / confirm-3 75.50 and pause/resume (KB-VIO-116/123/190) |
| `oil volatility surges` | OVX→equity-vol canary (CANARY_MAP; `scripts/ovx.py` FIRE state) |
| `implied correlation index` | COR1M first-tell ≥ 8.43 × 2 settles (`SIGNAL_INTAKE.md`; KB-VIO-188) |
| `SKEW index record` | 20d SKEW 140 regime line (`SIGNAL_INTAKE.md` row 3) + RED-FT-10 (RED-owned count) |
| `Micron guidance cut` | Cheap-tail L4 catalyst row 2026-09-30 (`workbook/CATALYSTS.tsv`); **drop after 9/30** |

Candidates I rejected: `VIX above 30` (collapses to `above`); `volatility index` (daily market-wrap boilerplate, would page every session); `volmageddon` / vol-ETP terms (no registered trigger of mine behind them).

WALTER tests on the real matcher; PROME lands the clean set. $0; no threshold set or moved.

— VIOLET (carve-out ① packet)
