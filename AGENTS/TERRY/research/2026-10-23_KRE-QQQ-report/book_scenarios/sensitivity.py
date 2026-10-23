"""Per-leg sensitivities of the see-saw book (MODEL; same inputs/pricer as scenarios.py).
$ change for a 1% / 3% / 5% move in each leg's driver (other leg unchanged), and $ decay per day.
Run: python3 -I sensitivity.py
"""
import contextlib, io, datetime as dt, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import scenarios as S
f = lambda x: f"{'+' if x >= 0 else '−'}${abs(x):,.0f}"
groups = [("Bank/credit puts (31 contracts)", lambda l: l["leg"] == "bank", "KRE"),
          ("QQQ Oct-26 710P + 705P×2 (expire Mon)", lambda l: l["tk"] == "QQQ" and l["exp"] == "2026-10-26", "QQQ"),
          ("QQQ Nov-20 690/670 spread ×2", lambda l: l["tk"] == "QQQ" and l["exp"] == "2026-11-20", "QQQ")]
now = S.ASOF
def v(ls, kre, qqq, when):
    return sum(S.value(l, kre, qqq, 1, 1, when) for l in ls)
print(f"MODEL, quotes {now:%Y-%m-%d %H:%M} ET; vol unchanged; driver = KRE for bank names (via betas), QQQ for QQQ lines\n")
print("| Group | Value now | Driver −1% | −3% | −5% | Driver +1% | +3% | +5% | Decay/day (flat, next session) |")
print("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
tomorrow = dt.datetime(2026, 10, 26, 16, 0)   # next session close (Mon)
nxt = dt.datetime(2026, 10, 27, 16, 0)        # one session after Mon, for the post-Monday book
for name, sel, drv in groups:
    ls = [l for l in S.book if sel(l)]
    base = v(ls, 0, 0, now)
    cells = []
    for m in (-.01, -.03, -.05, .01, .03, .05):
        k, q = (m, 0) if drv == "KRE" else (0, m)
        cells.append(f(v(ls, k, q, now) - base))
    dec = v(ls, 0, 0, tomorrow) - base
    print(f"| {name} | {f(base)} | " + " | ".join(cells) + f" | {f(dec)} (to Mon close) |")
# post-Monday book: daily decay averaged over the next 5 sessions after Monday
post = [l for l in S.book if l["exp"] > "2026-10-26"]
d0 = dt.datetime(2026, 10, 26, 16, 0); d5 = dt.datetime(2026, 11, 2, 16, 0)
avg = (v(post, 0, 0, d5) - v(post, 0, 0, d0)) / 5
print(f"\nPost-Monday book (bank puts + Nov-20 spread): average decay {f(avg)}/session over 10/26→11/2 if nothing moves.")
# swing needed in ONE week for one side's gain to cover the whole post-Monday book's decay
for name, sel, drv in (groups[0], groups[2]):
    ls = [l for l in post if sel(l)]
    whole_decay = v(post, 0, 0, d5) - v(post, 0, 0, d0)
    for m in [x / 1000 for x in range(5, 200, 5)]:
        k, q = (-m, 0) if drv == "KRE" else (0, -m)
        gain = v(ls, k, q, d5) - v(ls, 0, 0, d0)
        rest = [l for l in post if not sel(l)]
        rest_chg = v(rest, 0, 0, d5) - v(rest, 0, 0, d0)
        if gain + rest_chg >= 0:
            print(f"{name}: a {m*100:.1f}% {drv} drop over 10/26→11/2 (other side flat) breaks the post-Monday book even")
            break
