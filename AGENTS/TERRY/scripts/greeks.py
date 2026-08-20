#!/usr/bin/env python3
"""
TERRY greeks.py — Black-Scholes Greeks incl. 2nd-order (vanna, vomma, charm)
and a GATE-REACHABILITY SURFACE for long-premium harvest gates.

WHY THIS EXISTS
---------------
The 2026-08-18 measurement on TRY-FIRE-004 established that its harvest gate is
a VOLATILITY gate, not a price gate, and recorded one headline branch:

    "IV >= 18% CLEARS WITH NO PRICE MOVE AT ALL (0.374 flat)"   [43 DTE, gate $0.33]

That is a MOMENT property (RISK_RULES #14). Two things have since moved AGAINST it:
  - DTE 43 -> 41 (vega decays as expiry nears)
  - the gate was ruled FEES-IN: $0.33 -> $0.3469 (Will, queue row 61, 8/19)

This tool re-measures the boundary on demand instead of letting a dated figure
stand as if current, and adds the second-order term the flat-vol read omits:

  VANNA (dVega/dSpot). The 8/18 read priced the price-leg and the vol-leg as if
  SEPARABLE ("needs -2.37%" OR "IV>=18 clears flat"). For a long OTM put they are
  NOT separable: as spot falls toward the strike, vega RISES. The realistic joint
  path (selloff + vol pop) therefore pays MORE than the sum of the two legs read
  independently, and the "no price move at all" branch is the LEAST likely route
  to the gate rather than the cheapest one.

METHOD LIMITS - STATED, NOT BURIED
----------------------------------
  * Black-Scholes, FLAT vol, European. TLT options are AMERICAN; for a deep-OTM
    put with ~zero intrinsic the early-exercise premium is negligible, but it is
    not zero and this tool does not model it.
  * Flat vol means NO SKEW. A real TLT selloff steepens put skew, so the OTM put's
    own IV rises MORE than ATM IV. This tool's IV input is the OPTION's IV, so a
    skew move must be entered by hand as a higher IV. Direction of the omission:
    the tool UNDERSTATES the payoff in a selloff. Bias is stated so it is not
    mistaken for precision.
  * r is a parameter, not a fetched rate.
  * Model-vs-chain gap is real: on 8/18 the model backed out 13.53% at the mark
    vs the chain's printed 12.70%. Treat every boundary as a BAND, never a line.

NOTHING HERE IS A PROPOSAL. This measures what would have to happen.
"""
import argparse
import math
import sys
from datetime import date, datetime

SQRT2PI = math.sqrt(2.0 * math.pi)


def _n_pdf(x):
    return math.exp(-0.5 * x * x) / SQRT2PI


def _n_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def d1_d2(S, K, T, r, sigma, q=0.0):
    if T <= 0 or sigma <= 0 or S <= 0:
        return None, None
    v = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * T) / v
    return d1, d1 - v


def bs_price(S, K, T, r, sigma, kind="put", q=0.0):
    """European BS price. T in YEARS."""
    if T <= 0:
        return max(0.0, (K - S) if kind == "put" else (S - K))
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    df, dq = math.exp(-r * T), math.exp(-q * T)
    if kind == "put":
        return K * df * _n_cdf(-d2) - S * dq * _n_cdf(-d1)
    return S * dq * _n_cdf(d1) - K * df * _n_cdf(d2)


def greeks(S, K, T, r, sigma, kind="put", q=0.0):
    """
    Returns the full set. Conventions, stated so nobody has to guess:
      delta  per $1 underlying
      gamma  per $1^2
      vega   per 1.00 VOL POINT (i.e. 100% -> divide by 100 for 'per 1 IV point')
      theta  per YEAR (divide by 365 for per-calendar-day)
      vanna  d(vega)/d(spot), same vol units as vega
      vomma  d(vega)/d(vol), same vol units
      charm  d(delta)/d(time-to-expiry), per YEAR
    """
    out = {k: float("nan") for k in
           ("price delta gamma vega theta vanna vomma charm").split()}
    if T <= 0 or sigma <= 0:
        return out
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    sqT = math.sqrt(T)
    df, dq = math.exp(-r * T), math.exp(-q * T)
    pdf = _n_pdf(d1)

    out["price"] = bs_price(S, K, T, r, sigma, kind, q)
    out["gamma"] = dq * pdf / (S * sigma * sqT)
    out["vega"] = S * dq * pdf * sqT
    out["vanna"] = -dq * pdf * d2 / sigma
    out["vomma"] = out["vega"] * d1 * d2 / sigma

    if kind == "put":
        out["delta"] = -dq * _n_cdf(-d1)
        out["theta"] = (-S * dq * pdf * sigma / (2 * sqT)
                        + r * K * df * _n_cdf(-d2) - q * S * dq * _n_cdf(-d1))
        out["charm"] = (-q * dq * _n_cdf(-d1)
                        - dq * pdf * (2 * (r - q) * T - d2 * sigma * sqT)
                        / (2 * T * sigma * sqT))
    else:
        out["delta"] = dq * _n_cdf(d1)
        out["theta"] = (-S * dq * pdf * sigma / (2 * sqT)
                        - r * K * df * _n_cdf(d2) + q * S * dq * _n_cdf(d1))
        out["charm"] = (q * dq * _n_cdf(d1)
                        - dq * pdf * (2 * (r - q) * T - d2 * sigma * sqT)
                        / (2 * T * sigma * sqT))
    return out


def implied_vol(target, S, K, T, r, kind="put", q=0.0, lo=1e-4, hi=5.0):
    """Bisection. Returns None if the target is outside the achievable band."""
    if T <= 0 or target <= 0:
        return None
    if bs_price(S, K, T, r, hi, kind, q) < target:
        return None
    if bs_price(S, K, T, r, lo, kind, q) > target:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bs_price(S, K, T, r, mid, kind, q) < target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def move_to_gate(gate, S, K, T, r, sigma, kind="put", q=0.0):
    """
    % move in S required to reach `gate` at the given (T, sigma).
    Returns None when the gate clears with NO move (or is unreachable).
    """
    if bs_price(S, K, T, r, sigma, kind, q) >= gate:
        return 0.0            # clears flat
    lo, hi = 0.0, 0.60        # search down to -60% for a put
    if kind == "put":
        if bs_price(S * (1 - hi), K, T, r, sigma, kind, q) < gate:
            return None       # unreachable inside the search band
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if bs_price(S * (1 - mid), K, T, r, sigma, kind, q) < gate:
                lo = mid
            else:
                hi = mid
        return -0.5 * (lo + hi)
    if bs_price(S * (1 + hi), K, T, r, sigma, kind, q) < gate:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bs_price(S * (1 + mid), K, T, r, sigma, kind, q) < gate:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _fmt_pct(x):
    return "  clears FLAT" if x == 0.0 else ("  unreachable" if x is None
                                             else f"{x * 100:+8.2f}%")


def main():
    p = argparse.ArgumentParser(
        description="BS Greeks + harvest-gate reachability surface (TERRY).")
    p.add_argument("--spot", type=float)
    p.add_argument("--strike", type=float)
    p.add_argument("--expiry", help="YYYY-MM-DD")
    p.add_argument("--iv", type=float, help="decimal, e.g. 0.127")
    p.add_argument("--rate", type=float, default=0.042, help="decimal, default 0.042")
    p.add_argument("--kind", choices=("put", "call"), default="put")
    p.add_argument("--gate", type=float, help="harvest gate in $ (per contract, e.g. 0.3469)")
    p.add_argument("--asof", help="YYYY-MM-DD, default today")
    p.add_argument("--contracts", type=int, default=1)
    p.add_argument("--surface", action="store_true",
                   help="print the (move x IV) gate-reachability surface")
    p.add_argument("--decay", action="store_true",
                   help="print how the vol-only route to the gate decays with DTE")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args()

    if a.selftest:
        return selftest()

    missing = [f for f in ("spot", "strike", "expiry", "iv") if getattr(a, f) is None]
    if missing:
        print("greeks.py: missing required argument(s): "
              + ", ".join("--" + m for m in missing), file=sys.stderr)
        return 2

    asof = datetime.strptime(a.asof, "%Y-%m-%d").date() if a.asof else date.today()
    exp = datetime.strptime(a.expiry, "%Y-%m-%d").date()
    dte = (exp - asof).days
    if dte <= 0:
        print(f"greeks.py: expiry {exp} is not after as-of {asof}", file=sys.stderr)
        return 2
    T = dte / 365.0
    S, K, r, sig = a.spot, a.strike, a.rate, a.iv

    g = greeks(S, K, T, r, sig, a.kind)
    moneyness = (K - S) / S * 100 if a.kind == "put" else (S - K) / S * 100

    print(f"TERRY greeks — {a.kind.upper()} {K:g} exp {exp}  (as-of {asof}, {dte} DTE)")
    print("=" * 68)
    print(f"  spot {S:.2f} · strike {K:g} · {moneyness:+.2f}% OTM · "
          f"IV {sig*100:.2f}% · r {r*100:.2f}%")
    print(f"  BS price      ${g['price']:.4f}"
          + (f"   x{a.contracts} = ${g['price']*100*a.contracts:,.2f}"
             if a.contracts != 1 else ""))
    print()
    print("  FIRST ORDER")
    print(f"    delta        {g['delta']:+.4f}   per $1 underlying")
    print(f"    vega         {g['vega']/100:+.4f}   per 1 IV POINT "
          f"(= ${g['vega']/100*100*a.contracts:,.2f} on {a.contracts} ct)")
    print(f"    theta        {g['theta']/365:+.4f}   per calendar day "
          f"(= ${g['theta']/365*100*a.contracts:,.2f}/day on {a.contracts} ct)")
    print()
    print("  SECOND ORDER")
    print(f"    gamma        {g['gamma']:+.5f}   per $1^2")
    print(f"    vanna        {g['vanna']/100:+.5f}   d(vega per IV pt)/d($1 spot)")
    print(f"    vomma        {g['vomma']/10000:+.5f}  d(vega per IV pt)/d(1 IV pt)")
    print(f"    charm        {g['charm']/365:+.5f}   d(delta)/d(calendar day)")
    print()

    # --- VANNA, in the only form that answers a trading question ----------
    dS = -0.01 * S
    v_now = g["vega"] / 100
    v_down = greeks(S + dS, K, T, r, sig, a.kind)["vega"] / 100
    print("  VANNA READ (the separability test)")
    print(f"    vega per IV pt at spot {S:.2f}          {v_now:+.4f}")
    print(f"    vega per IV pt at spot {S+dS:.2f} (-1%)  {v_down:+.4f}"
          f"   [{(v_down/v_now-1)*100:+.1f}%]")
    if v_down > v_now:
        print("    => vega RISES as spot falls. The price-leg and the vol-leg are")
        print("       NOT separable: a selloff makes each IV point worth MORE.")
    else:
        print("    => vega FALLS as spot falls (past the vega peak for this strike).")
    print()

    if a.gate:
        print(f"  GATE ${a.gate:.4f}")
        need = move_to_gate(a.gate, S, K, T, r, sig, a.kind)
        print(f"    at IV {sig*100:.2f}%, {dte} DTE, move needed: {_fmt_pct(need)}")
        iv_flat = implied_vol(a.gate, S, K, T, r, a.kind)
        if iv_flat is None:
            print("    IV that clears the gate with NO price move: "
                  "NONE inside 0-500% — the vol-only route is CLOSED.")
        else:
            print(f"    IV that clears the gate with NO price move: "
                  f"{iv_flat*100:.2f}%  (now {sig*100:.2f}%, "
                  f"needs {(iv_flat-sig)*100:+.2f} pts)")
        print()

    if a.surface and a.gate:
        ivs = [0.10, 0.1270, 0.15, 0.18, 0.20, 0.25, 0.30]
        print(f"  GATE-REACHABILITY SURFACE — move needed to reach ${a.gate:.4f}")
        print("    " + "IV:".ljust(8) + "".join(f"{i*100:>9.1f}%" for i in ivs))
        print("    " + "-" * (8 + 10 * len(ivs)))
        row = "".join(_fmt_pct(move_to_gate(a.gate, S, K, T, r, i, a.kind))
                      for i in ivs)
        print(f"    {dte:>3d} DTE" + row)
        print()

    if a.decay and a.gate:
        print(f"  VOL-ONLY ROUTE, DECAYING — the IV needed to clear "
              f"${a.gate:.4f} with NO price move")
        print("    (MenthorQ Vega row: 'drops as expiry nears'. Measured, not assumed.)")
        print(f"    {'DTE':>5}  {'date':<12} {'IV needed':>10}  {'vega/pt':>9}")
        for d in (43, 41, 35, 30, 25, 21, 14, 10, 7, 5, 3, 1):
            if d > dte + 5:
                continue
            Td = d / 365.0
            iv_need = implied_vol(a.gate, S, K, Td, r, a.kind)
            vg = greeks(S, K, Td, r, sig, a.kind)["vega"] / 100
            dt_lab = (exp - date.fromordinal(exp.toordinal() - d)).days
            day = date.fromordinal(exp.toordinal() - d).isoformat()
            need_s = f"{iv_need*100:9.2f}%" if iv_need else "   CLOSED "
            print(f"    {d:>5}  {day:<12} {need_s}  {vg:>9.4f}")
        print()
    return 0


def selftest():
    """Synthetic-defect + known-value assertions. Exit 1 on any failure."""
    fails = []

    def chk(name, cond, detail=""):
        if cond:
            print(f"  PASS  {name}")
        else:
            fails.append(name)
            print(f"  FAIL  {name}  {detail}")

    print("greeks.py selftest")
    print("=" * 68)

    # 1. Put-call parity: C - P = S*e^-qT - K*e^-rT
    S, K, T, r, sig = 100.0, 95.0, 0.5, 0.04, 0.25
    c = bs_price(S, K, T, r, sig, "call")
    pu = bs_price(S, K, T, r, sig, "put")
    parity = S - K * math.exp(-r * T)
    chk("put-call parity", abs((c - pu) - parity) < 1e-9, f"{c-pu} vs {parity}")

    # 2. Vega identical for call and put (same strike/expiry)
    gc, gp = greeks(S, K, T, r, sig, "call"), greeks(S, K, T, r, sig, "put")
    chk("vega call==put", abs(gc["vega"] - gp["vega"]) < 1e-9)
    chk("gamma call==put", abs(gc["gamma"] - gp["gamma"]) < 1e-9)

    # 3. Numerical-derivative agreement: delta, vega, gamma, vanna
    h = 1e-4
    num_d = (bs_price(S + h, K, T, r, sig, "put")
             - bs_price(S - h, K, T, r, sig, "put")) / (2 * h)
    chk("delta == dPrice/dS", abs(num_d - gp["delta"]) < 1e-5,
        f"{num_d} vs {gp['delta']}")
    num_v = (bs_price(S, K, T, r, sig + h, "put")
             - bs_price(S, K, T, r, sig - h, "put")) / (2 * h)
    chk("vega == dPrice/dSigma", abs(num_v - gp["vega"]) < 1e-4,
        f"{num_v} vs {gp['vega']}")
    num_g = (greeks(S + h, K, T, r, sig, "put")["delta"]
             - greeks(S - h, K, T, r, sig, "put")["delta"]) / (2 * h)
    chk("gamma == dDelta/dS", abs(num_g - gp["gamma"]) < 1e-5)
    num_vanna = (greeks(S + h, K, T, r, sig, "put")["vega"]
                 - greeks(S - h, K, T, r, sig, "put")["vega"]) / (2 * h)
    chk("vanna == dVega/dS", abs(num_vanna - gp["vanna"]) < 1e-4,
        f"{num_vanna} vs {gp['vanna']}")
    num_vomma = (greeks(S, K, T, r, sig + h, "put")["vega"]
                 - greeks(S, K, T, r, sig - h, "put")["vega"]) / (2 * h)
    chk("vomma == dVega/dSigma", abs(num_vomma - gp["vomma"]) < 1e-3,
        f"{num_vomma} vs {gp['vomma']}")

    # 4. implied_vol round-trips
    px = bs_price(S, K, T, r, 0.3131, "put")
    iv = implied_vol(px, S, K, T, r, "put")
    chk("implied_vol round-trip", iv is not None and abs(iv - 0.3131) < 1e-6)

    # 5. Deep-OTM put has POSITIVE vanna (vega rises as spot falls)
    g_otm = greeks(83.0, 77.0, 41 / 365, 0.042, 0.127, "put")
    v0 = greeks(83.0, 77.0, 41 / 365, 0.042, 0.127, "put")["vega"]
    v1 = greeks(82.0, 77.0, 41 / 365, 0.042, 0.127, "put")["vega"]
    chk("OTM put: vega rises as spot falls", v1 > v0, f"{v1} !> {v0}")
    chk("OTM put vanna sign matches", g_otm["vanna"] < 0,
        "put vanna convention: dVega/dS < 0 for OTM put")

    # 6. THE 8/18 REGRESSION — permanent, per the desk's selftest convention.
    #    Card claim: at 43 DTE, S=81.64, K=77, IV 18% => price ~0.374, clears $0.33.
    p818 = bs_price(81.64, 77.0, 43 / 365, 0.042, 0.18, "put")
    chk("8/18 regression: IV 18 @43DTE ~ 0.374", abs(p818 - 0.374) < 0.02,
        f"got {p818:.4f}")
    chk("8/18 regression: that price cleared the OLD $0.33 gate", p818 >= 0.33,
        f"{p818:.4f}")

    # 7. Vega decays with DTE, all else equal (the MenthorQ claim under test)
    v_far = greeks(83.0, 77.0, 43 / 365, 0.042, 0.127, "put")["vega"]
    v_near = greeks(83.0, 77.0, 10 / 365, 0.042, 0.127, "put")["vega"]
    chk("vega decays as expiry nears", v_near < v_far, f"{v_near} !< {v_far}")

    # 8. move_to_gate: a gate already cleared returns 0.0, not a fake move
    chk("move_to_gate returns 0.0 when already clear",
        move_to_gate(0.01, 83.0, 77.0, 41 / 365, 0.042, 0.127, "put") == 0.0)
    chk("move_to_gate returns None when unreachable",
        move_to_gate(999.0, 83.0, 77.0, 41 / 365, 0.042, 0.127, "put") is None)

    # 9. Expired option: intrinsic only, no NaN leak
    chk("T=0 put = intrinsic", bs_price(70.0, 77.0, 0.0, 0.042, 0.127, "put") == 7.0)

    print("=" * 68)
    if fails:
        print(f"SELFTEST FAILED: {len(fails)} — {', '.join(fails)}")
        return 1
    print("SELFTEST PASS (all assertions)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
