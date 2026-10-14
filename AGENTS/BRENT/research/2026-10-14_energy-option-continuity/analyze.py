"""Reproduce screening economics from saved calls; no execution or gate grading."""
import datetime as dt
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
raw = ROOT / "vendor-snapshot.json"
data = json.loads(raw.read_text())
ASOF = dt.date(2026, 10, 14)
FEE = .65  # illustrative per contract per side, not verified broker pricing
specs = [
    ("USO", "2026-12-18", 162, 175),
    ("USO", "2026-12-18", 160, 175),
    ("USO", "2026-12-18", 180, None),
    ("BNO", "2027-01-15", 70, None),
    ("BNO", "2027-01-15", 69, 75),
    ("VLO", "2026-12-18", 480, 490),
    ("MPC", "2026-12-18", 500, 510),
    ("PSX", "2026-12-18", 310, 320),
]
results = []
for symbol, expiry, long_k, short_k in specs:
    item = data["symbols"][symbol]
    rows = item["chains"][expiry]
    def leg(strike):
        row = next(r for r in rows if r["strike"] == strike)
        assert 0 < row["bid"] <= row["ask"]
        assert expiry.replace("-", "")[2:] + "C" in row["contractSymbol"]
        assert row["contractSymbol"].startswith(symbol)
        assert int(row["contractSymbol"][-8:]) == int(strike*1000)
        return row
    long = leg(long_k)
    short = leg(short_k) if short_k is not None else None
    spot = item["quote"]["regularMarketPrice"]
    legs = 2 if short else 1
    debit = long["ask"] - (short["bid"] if short else 0)
    liquidate = long["bid"] - (short["ask"] if short else 0)
    cost = debit*100 + legs*FEE
    width = short_k-long_k if short else None
    assert debit > 0 and (width is None or debit < width)
    def expiry_pl(price):
        payoff = max(price-long_k, 0) - (max(price-short_k, 0) if short else 0)
        return round(payoff*100-cost, 2)
    r = {
        "symbol": symbol, "expiry": expiry, "dte_calendar": (dt.date.fromisoformat(expiry)-ASOF).days,
        "spot_reference": spot, "long_strike": long_k, "short_strike": short_k,
        "long": long, "short": short,
        "conservative_entry_debit_per_share": round(debit, 4),
        "opening_cost_including_assumed_fees": round(cost, 2),
        "max_loss_expiration_including_opening_fees": round(cost, 2),
        "max_profit_expiration_after_opening_fees": round(width*100-cost, 2) if width else None,
        "breakeven_expiration_including_opening_fees": round(long_k+cost/100, 4),
        "breakeven_rise_pct": round(((long_k+cost/100)/spot-1)*100, 4),
        "long_otm_pct": round((long_k/spot-1)*100, 4),
        "short_otm_pct": round((short_k/spot-1)*100, 4) if short else None,
        "gross_debit_fraction_of_width": round(debit/width, 6) if width else None,
        "immediate_liquidation_gross_per_share": round(liquidate, 4),
        "roundtrip_spread_and_assumed_fees_dollars": round((debit-liquidate)*100+2*legs*FEE, 2),
        "expiration_scenarios": [{"underlying_return_pct": ret, "underlying": round(spot*(1+ret/100), 4),
                                  "profit_loss": expiry_pl(spot*(1+ret/100))}
                                 for ret in [-10, 0, 5, 10, 15, 20]],
    }
    assert expiry_pl(0) == -round(cost, 2)
    if width:
        assert expiry_pl(short_k+1000) == round(width*100-cost, 2)
    results.append(r)
out = {"source_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
       "fee_assumption_per_contract_per_side": FEE,
       "method": "100x standard multiplier; buy long ask, sell short bid. Scenarios at expiry, not forecasts; no closing costs or assignment included in expiry P/L.",
       "validation": "PASS: contract ticker/expiry/strike, positive ordered bid/ask, debit within width, payoff floor and cap",
       "screens": results}
(ROOT / "analysis.json").write_text(json.dumps(out, indent=2)+"\n")
for r in results:
    print(r['symbol'],r['long_strike'],r['short_strike'],'DTE',r['dte_calendar'],
          'cost',r['opening_cost_including_assumed_fees'],'BE',r['breakeven_expiration_including_opening_fees'],
          'rise',r['breakeven_rise_pct'],'maxprofit',r['max_profit_expiration_after_opening_fees'],
          'friction',r['roundtrip_spread_and_assumed_fees_dollars'],
          'scenarios',r['expiration_scenarios'])
