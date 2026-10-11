"""L546: WIDE is strictly above 15.00% at displayed percent precision."""
import contextlib
import io
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

import chain_fetch
import chain_parse


def main():
    row = dict(strike=100, type="P", bid=0.185, ask=0.215, mark=0.2,
               iv=20, volume=100, open_interest=1000, last_trade="TEST",
               quote_flag=[], moneyness_pct=0)
    for spread, expected in ((15.000000000000004, 0), (15.01, 1), (14.99, 0)):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            chain_fetch.display("TEST", "TEST", "put", 100, "TEST",
                                [dict(row, spread_pct=spread)], {}, 15, 0)
        assert f"Wide spread rows >15% of mark: {expected}" in output.getvalue()

    with TemporaryDirectory() as directory:
        source = Path(directory) / "chain.csv"
        source.write_text("strike,type,bid,ask,mark,open interest\n"
                          "100,P,0.185,0.215,0.2,1000\n")
        args = SimpleNamespace(file=str(source), expiry=None, type=None,
                               min_oi=None, underlying="TEST", limit=40,
                               wide_spread_pct=15, thin_oi=0)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            chain_parse.run(args)
        assert "Wide spread rows >15% of mark in displayed set: 0" in output.getvalue()
    print("SPREAD PRECISION: 4 integration cases PASS (tie, above, below, parser quote).")


if __name__ == "__main__":
    main()
