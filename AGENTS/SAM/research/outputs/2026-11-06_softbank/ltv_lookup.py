"""SAM SoftBank LTV lookup for the 11/10 print (written 2026-11-09, before results).

Put in SoftBank's REPORTED 9/30 figures; get the roll-forward to a chosen Arm price.
Same arithmetic as ltv_remark.py (roll-forward reproduces its 11/6 rows; --selftest).

  python3 ltv_lookup.py --nd 11.10 --v 72.86 --arm 187.71
  python3 ltv_lookup.py --nd 11.10 --v 72.86 --arm 187.71 --oct-in-nd --svf2-inside

nd  = SBG stand-alone adjusted net interest-bearing debt at 9/30, yen trillions (reported)
v   = equity value of holdings at 9/30, yen trillions (reported)
Roll-forward moves only: Arm (923M shares, 9/30 $289.66) and the October OpenAI tranche
($10B into both debt and value). T-Mobile, SoftBank Corp, SVF listed marks, the OpenAI mark,
new borrowing or sales after 9/30 are NOT moved: add them by hand from the deck.
FX: --fx converts ONLY the post-9/30 Arm move and October tranche; the 9/30 base stays at 157.35.
CORRECTED 2026-11-11: this is NOT "under 0.1pt" -- at 158.81 the full revaluation is 22.5% vs 22.7% here,
and across rates this script gives the WRONG SIGN. For any FX sensitivity use ltv_fx_sensitivity.py.
"""
import argparse

ARM_SH, ARM_930 = 923e6, 289.66
OCT_TRANCHE_USD, SVF2_USD = 10e9, 10e9


def roll(nd, v, arm, fx, oct_in_nd=False):
    t = OCT_TRANCHE_USD * fx / 1e12
    l2 = nd + (0 if oct_in_nd else t)
    v2 = v + (0 if oct_in_nd else t) + ARM_SH * (arm - ARM_930) * fx / 1e12
    return l2, v2


def arm_for(target, l2, v2, arm, fx):
    # Arm price at which l2 / v2' = target, holding everything else.
    need_v = l2 / target
    return arm + (need_v - v2) * 1e12 / (ARM_SH * fx)


def report(nd, v, arm, fx, oct_in_nd, svf2_inside):
    print(f"Reported 9/30: net debt {nd:.2f}T / value {v:.2f}T = {nd / v * 100:.1f}%")
    l2, v2 = roll(nd, v, arm, fx, oct_in_nd)
    s = SVF2_USD * fx / 1e12
    views = {"reported basis rolled": (l2, v2)}
    if not svf2_inside:
        views["plus guaranteed SVF2 loan (view C)"] = (l2 + s, v2 + s)
    for name, (l, vv) in views.items():
        print(f"  {name:38s} Arm ${arm:.2f}: {l:.2f}/{vv:.2f} = {l / vv * 100:.1f}%"
              f"   Arm for 25%: ${arm_for(0.25, l, vv, arm, fx):.0f}"
              f"   for 35%: ${arm_for(0.35, l, vv, arm, fx):.0f}")


def selftest():
    # ltv_remark.py 11/6: model 9/30 A = 11.10/72.86, C = 12.69/74.45; 11/6 A 22.1%, C 24.2% at fx 158.5
    for nd, v, want in ((11.10, 72.86, 22.1), (12.69, 74.45, 24.2)):
        l2, v2 = roll(nd, v, 172.34, 158.5)
        got = round(l2 / v2 * 100, 1)
        assert abs(got - want) <= 0.1, (nd, v, got, want)
    print("selftest OK: roll-forward reproduces ltv_remark.py 11/6 A 22.1% and C 24.2%")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--nd", type=float)
    p.add_argument("--v", type=float)
    p.add_argument("--arm", type=float, default=187.71)
    p.add_argument("--fx", type=float, default=158.0)
    p.add_argument("--oct-in-nd", action="store_true", help="9/30 net debt already carries the October tranche")
    p.add_argument("--svf2-inside", action="store_true", help="SoftBank's net debt already includes the SVF2 $10B loan")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args()
    if a.selftest or a.nd is None:
        selftest()
    if a.nd is not None:
        report(a.nd, a.v, a.arm, a.fx, a.oct_in_nd, a.svf2_inside)
