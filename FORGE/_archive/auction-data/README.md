# Treasury Auction Data Tool

Fetches US Treasury auction results from the Treasury FiscalData API.

## Usage

```bash
python3 fetch_auctions.py recent                    # last 30 days
python3 fetch_auctions.py recent --json             # JSON output
python3 fetch_auctions.py security 5Y               # 5Y note history
python3 fetch_auctions.py security 10Y --limit 5    # last 5 auctions
python3 fetch_auctions.py compare 5Y                # compare to historical avg
python3 fetch_auctions.py dashboard                 # full dashboard
```

## Output Fields

| Field | Description |
|-------|-------------|
| Date | Auction date |
| Security | Standardized term (2Y, 5Y, 10Y, 30Y) |
| BTC | Bid-to-cover ratio |
| Yield | High yield awarded |
| Awarded | Amount awarded ($B) |
| Status | 🟢 Strong / 🟡 Average / 🔴 Weak |

## Data Source

- Treasury FiscalData API: https://fiscaldata.treasury.gov/
- Updated daily
- Historical data back to 1979

## Limitations

- No true "tail" calculation (API doesn't provide expected/when-issued yield)
- Bidder breakdown (dealer/direct/indirect %) not always available
- Bill auctions excluded from dashboard (focus on notes/bonds)

## Integration

Add to cron for regular monitoring:
```bash
0 16 * * 1-5 cd /path/to/auction-data && python3 fetch_auctions.py dashboard >> /var/log/auctions.log
```
