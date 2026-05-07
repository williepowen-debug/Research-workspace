# EDGAR Filing Radar

MVP central filing monitor for Prome. Phase 1 detects high-signal SEC filings from watched companies and writes `latest.md` / `latest.json`. It does **not** route to agent inboxes yet.

## Usage

```bash
python3 FORGE/tools/filing-watch/poll_edgar.py --dry-run --lookback-days 14
python3 FORGE/tools/filing-watch/poll_edgar.py --dry-run --lookback-days 14 --material-only
python3 FORGE/tools/filing-watch/poll_edgar.py --dry-run --new-only
```

Normal run updates `seen_filings.json`:

```bash
python3 FORGE/tools/filing-watch/poll_edgar.py
```

## Files

- `watchlist.yml` — tickers, CIKs, owner agents, forms, thesis keywords
- `poll_edgar.py` — SEC submissions API poller
- `latest.md` / `latest.json` — most recent output
- `seen_filings.json` — duplicate suppression state, created on normal runs

## MVP Scope

Watched forms: `10-K`, `10-Q`, `8-K`, `NT 10-K`, `NT 10-Q`, `4`, `SC 13D`, `SC 13G`.

Watched domains:
- REGINALD: WAL, OZK, ZION, FITB, RF
- BROCK/SHADE: APO, ARES, OWL, BX, OBDC
- CARL/OTTO: SYF, COF, ALLY, CVNA

## Next Phases

1. **Routing:** write agent inbox notes for new filings.
2. **Thin extraction:** download filing text and extract paragraphs around thesis keywords.
3. **Domain parsers:** bank CRE/FHLB/provision tables, BDC non-accrual/PIK/NAV tables, ABS 10-D servicer metrics.
