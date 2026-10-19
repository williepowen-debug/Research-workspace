"""Bounded October 19 research arithmetic; no collection, grading or monitoring."""
import datetime as dt
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent


def main():
    # USD millions. June figures from the two June 30 10-Qs; source IDs in RESULT.
    rcl = dict(cash=875.0, room=6000.0, principal=23407.0, op_income_h1=2469.0)
    nclh = dict(cash=218.1, room=1300.0, principal=15467.745, op_income_h1=596.270)
    out = {"units": "USD millions / percent / percentage points", "june": {}}
    for name, v in [("RCL", rcl), ("NCLH", nclh)]:
        out["june"][name] = dict(
            **v, general_liquidity=v["cash"] + v["room"],
            liquidity_principal_pct=100 * (v["cash"] + v["room"]) / v["principal"],
            cash_principal_pct=100 * v["cash"] / v["principal"],
            operating_income_principal_pct=100 * v["op_income_h1"] / v["principal"],
        )
    principal_uses = 525 + 376.3 + 42.2
    out["nclh_transaction_only"] = dict(
        new_face=950, net_proceeds_before_fees=941.7,
        principal_uses=principal_uses,
        cash_change_before_premium_accruals_fees=941.7 - principal_uses,
        net_principal_change=950-principal_uses,
        nominal_revolver_room_change=376.3+315,
        old_2028_bond_annual_coupon=525*.06125,
        new_2031_bond_annual_coupon=950*.0875,
        same_525_principal_coupon_increase=525*(.0875-.06125),
        hypothetical_principal=nclh["principal"]+950-principal_uses,
        hypothetical_liquidity_before_fees=nclh["cash"]+nclh["room"]+376.3+315+941.7-principal_uses,
    )
    n = out["nclh_transaction_only"]
    n["hypothetical_liquidity_principal_pct"] = 100*n["hypothetical_liquidity_before_fees"]/n["hypothetical_principal"]
    # Use the prospectus's OWN as-adjusted principal and leases, rather than
    # silently mixing its $9M different June principal table with the 10-Q.
    out["rcl_transaction_only"] = dict(
        prospectus_as_adjusted_cash=855,
        prospectus_as_adjusted_principal_plus_leases=23250+159,
        july_commitment_increase=250,
        hypothetical_liquidity=855+6000+250,
        hypothetical_liquidity_principal_pct=100*(855+6000+250)/(23250+159),
        prospective_sandals_debt=3000,
        hypothetical_post_sandals_ratio_pct=100*(855+6000+250)/(23250+159+3000),
        prospectus_actual_vs_q2_principal_difference=23257+159-23407,
    )
    out["transaction_sensitivity_warning"] = (
        "NOT actual September/October balances. Omits operating flows, deposits, "
        "ship funding/capex, amortization, dividends, buybacks, FX, other draws, "
        "fees and NCLH redemption premium. Sandals is prospective, not funded."
    )
    series = {}
    hashes = {}
    for name in ["RCL", "NCLH"]:
        path = HERE / "sources" / f"walter-{name}.json"
        payload = path.read_bytes()
        hashes[name] = hashlib.sha256(payload).hexdigest()
        d = json.loads(payload)["chart"]["result"][0]
        series[name] = {
            dt.datetime.fromtimestamp(t, ZoneInfo("America/New_York")).date().isoformat(): v
            for t, v in zip(d["timestamp"], d["indicators"]["adjclose"][0]["adjclose"])
            if v is not None
        }
    dates = ["2026-09-18", "2026-09-21", "2026-09-22", "2026-09-23", "2026-09-29",
             "2026-09-30", "2026-10-01", "2026-10-02", "2026-10-14", "2026-10-15", "2026-10-16"]
    out["walter_chart_sha256"] = hashes
    out["dated_path_from_september18_pct"] = []
    for day in dates:
        row = {"date": day}
        for name in series:
            row[name] = 100*(series[name][day]/series[name]["2026-09-18"]-1)
        row["NCLH_minus_RCL_pp"] = row["NCLH"]-row["RCL"]
        out["dated_path_from_september18_pct"].append(row)
    out["grading"] = "CRU-11 untouched; no prediction resolver executed"
    (HERE / "calculations.json").write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({"june":out["june"], "nclh_transaction_only":n,
                      "rcl_transaction_only":out["rcl_transaction_only"],
                      "window_close":out["dated_path_from_september18_pct"][-1]}, indent=2))


if __name__ == "__main__":
    main()
