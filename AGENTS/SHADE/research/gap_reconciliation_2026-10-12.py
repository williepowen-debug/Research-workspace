#!/usr/bin/env python3
"""Reproduce dated source reconciliations; never grade a charter or infer a loss."""
import json
from decimal import Decimal as D
from pathlib import Path

INPUT = Path(__file__).resolve().parents[1] / "sources/2026-10-12_gap-investigation/RECONCILIATION_INPUTS.json"


def pct(numerator, denominator):
    return float(D(numerator) / D(denominator) * 100)


def reconcile(data):
    a, o, c, t, g = (data[k] for k in ("dlic_audited", "dlic_original", "clear_spring", "athene", "global_atlantic"))
    assert a["valuation_date"] == o["valuation_date"] == "2025-12-31"
    assert a["ga_admitted"] + a["sa_admitted"] == a["total_admitted"]
    assert o["ga_admitted"] + o["sa_admitted"] == o["total_admitted"]
    assert o["formal_abs"] + o["issuer_credit_obligations"] == o["bonds"]
    assert a["illiquid_abs_verified"] is None, "No approved/evidenced ABS liquidity classification exists in this input."
    floor_a = a["mortgages"] + a["schedule_ba"]
    floor_o = o["mortgage_first"] + o["mortgage_other"] + o["schedule_ba"]
    comparisons = {"floor": floor_a * 1000 - floor_o}
    for key in ("ga_admitted", "sa_admitted", "total_admitted", "formal_abs"):
        comparisons[key] = a[key] * 1000 - o[key]
    assert all(abs(v) < 2000 for v in comparisons.values()), "Presentation-precision tie failed."
    dlic = {"audit_amounts_in_thousands": {"floor": floor_a, "conditional_bond_numerator": floor_a + a["affiliate_contingent_bonds"]},
            "same_audit_percentages": {}, "original_dollars_to_audit_thousands_differences_USD": comparisons,
            "formal_abs_less_than_affiliate_bonds": a["formal_abs"] < a["affiliate_contingent_bonds"],
            "charter_grade": None}
    for label, numerator in (("floor", floor_a), ("unapproved_affiliate_bond_proxy", floor_a + a["affiliate_contingent_bonds"]),
                             ("all_formal_abs_hypothesis", floor_a + a["formal_abs"])):
        dlic["same_audit_percentages"][label] = {"GA": pct(numerator, a["ga_admitted"]), "GA_plus_SA": pct(numerator, a["total_admitted"])}
    dlic["prior_mixed_vintage_proxy_percentages"] = {"GA": pct(floor_o + o["old_rounded_affiliate_bond_proxy"], o["ga_admitted"]),
                                                    "GA_plus_SA": pct(floor_o + o["old_rounded_affiliate_bond_proxy"], o["total_admitted"])}
    rows = c["rows"]
    cs = {"percentages": {r["date"]: pct(r["affiliate"], r["invested_ga"]) for r in rows},
          "affiliate_change_millions": rows[-1]["affiliate"] - rows[0]["affiliate"],
          "affiliate_change_percent": pct(rows[-1]["affiliate"] - rows[0]["affiliate"], rows[0]["affiliate"]),
          "invested_ga_change_millions": rows[-1]["invested_ga"] - rows[0]["invested_ga"],
          "invested_ga_change_percent": pct(rows[-1]["invested_ga"] - rows[0]["invested_ga"], rows[0]["invested_ga"])}
    cs["share_change_pp"] = cs["percentages"][rows[-1]["date"]] - cs["percentages"][rows[0]["date"]]
    assert sum(t["restricted_components"]) == t["restricted_assets"]
    assert t["whco_outstanding_purchase_obligation"] is None, "Outstanding O has not been obtained; do not substitute project total."
    guarantee, reimbursement = D(t["whco_guarantee_fraction"]), D(t["whco_reimbursement_fraction"])
    athene = {"amaps_named_floor_millions": sum(t["amaps_named_single_issuer_risk"].values()),
              "fhlb_nominal_conditional_room_millions": t["fhlb_estimated_total_capacity"] - t["fhlb_drawn"],
              "fhlb_available_cash": None, "restricted_asset_sum_millions": sum(t["restricted_components"]),
              "whco_gross_formula": f"{guarantee} * O", "whco_after_reimbursement_if_collectible_formula": f"{guarantee * (1 - reimbursement)} * O",
              "whco_guarantee_dollars": None, "stressed_loss_dollars": None}
    return {"DLIC": dlic, "Clear_Spring": cs, "Athene": athene,
            "Global_Atlantic": {"AUM_excluding_included_sidecars_billions": g["insurance_aum_including_sidecars"] - g["ivy_other_sidecars_included"],
                                "not_statutory_retained_risk": True}, "source_status": "primary arithmetic; unresolved classification/access; no grades or loss estimates"}


if __name__ == "__main__":
    print(json.dumps(reconcile(json.loads(INPUT.read_text())), indent=2))
