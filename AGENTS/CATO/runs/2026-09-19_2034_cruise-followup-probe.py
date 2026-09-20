"""Review arithmetic; pinned owner inputs, not certification of market prices."""
from pathlib import Path
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[3]
REV = "b6e36086d891b5bc016c4fece317c07606c1ae98"
print("Committed review snapshot:", REV)
for name in ("STATUS.md", "TRADE.md", "WATCHLIST_CCL_PREANNOUNCE.md",
             "workbook/KB.tsv", "workbook/FLOW.tsv", "workbook/VX.tsv"):
    path = "AGENTS/CRUISE/" + name
    data = subprocess.check_output(["git", "show", REV + ":" + path], cwd=ROOT)
    print("committed sha256", hashlib.sha256(data).hexdigest(), path)

print("\nCash-dividend-held-as-cash basis; no reinvestment")
c = [22.75, 22.56, 22.11, 22.35, 22.17, 21.84]
r = [260.14, 255.34, 249.30, 253.92, 249.74, 245.81]
daily_wins = cumulative_wins = 0
for i in range(1, 6):
    dividend_today = 1.50 if i == 4 else 0
    accrued = 1.50 if i >= 4 else 0
    cr = 100 * (c[i] / c[i-1] - 1)
    rr = 100 * ((r[i] + dividend_today) / r[i-1] - 1)
    raw = 100 * (r[i] / 265.55 - c[i] / 23.48)
    adjusted = 100 * ((r[i] + accrued) / 265.55 - c[i] / 23.48)
    daily_wins += cr > rr
    cumulative_wins += adjusted < 0
    print(f"Sep {13+i}: daily CCL={cr:.4f}% RCL={rr:.4f}%; cumulative DD raw={raw:.4f}pp adjusted={adjusted:.4f}pp")
print("CCL wins individual days:", daily_wins, "negative cumulative readings:", cumulative_wins)
assert daily_wins == 4 and cumulative_wins == 1
offset = 100 * 1.50 / 265.55
print("Cash-basis offset on EVERY subsequent fixed-base observation:", offset, "pp")
print("Synthetic later raw=4.6pp => adjusted=", 4.6 + offset, "pp; >5 flips")
assert 4.6 < 5 < 4.6 + offset
print("RCL weekly cash-dividend return:", 100*((245.81+1.5)/260.14-1))

print("\nFunding draft reconstruction, USD millions; approximate rounded owner inputs")
uses, cash, revolver = 3805., 218.1, 1300.
for growth in (.02, 0., -.05, -.0784, -.10, -.15, -.20):
    ocf = 2089.7*(1+growth) - 1414.0 + 2089.7*(1+growth)**2
    headroom = ocf + cash + revolver - uses
    print(f"annual growth={growth:.4%}: future OCF={ocf:.3f}; endpoint headroom={headroom:.3f}; +200 capex headroom={headroom-200:.3f}")
headroom_5 = 2089.7*.95 - 1414 + 2089.7*.95**2 + cash + revolver - uses
assert headroom_5 > 0 > headroom_5 - 200
print("A positive final balance alone cannot prove interim liquidity: synthetic 100 start, 150 due before 100 inflow => -50 then +50.")
print("\nCausal-test counterexamples, illustrative yield percentage points")
print("1.15 baseline + (-0.65 unrelated weakness) + 0 NCLH effect = 0.50: hits confirmation bar without mechanism")
print("1.15 baseline + 0.65 other strength + (-0.65 NCLH effect) = 1.15: hits refutation bar despite mechanism")
print("These are identification counterexamples, not estimates of Carnival's actual mix.")
