"""T-SHADE-01 sign-leg window sweep, 2026-10-10 (SHADE shade-1010).
Equal-weighted simple % change on CLOSES, wrappers ARCC/FSK/OBDC/BIZD vs managers APO/ARES.
RAW = yfinance auto_adjust=False (split-adjusted, NOT dividend-adjusted) - the basis of prior readings.
ADJ = yfinance auto_adjust=True (vendor dividend-adjusted, as served on the run date).
Run: .venv/bin/python AGENTS/SHADE/research/tshade01_signleg_2026-10-10.py
"""
import yfinance as yf
W = ["ARCC", "FSK", "OBDC", "BIZD"]; M = ["APO", "ARES"]
END = "2026-10-09"
STARTS = ["2026-08-28", "2026-09-24", "2026-09-25", "2026-09-28", "2026-09-29",
          "2026-09-30", "2026-10-01", "2026-10-02", "2026-10-05"]
raw, adj = {}, {}
for t in W + M:
    raw[t] = yf.Ticker(t).history(start="2026-08-25", end="2026-10-11", auto_adjust=False)["Close"]
    adj[t] = yf.Ticker(t).history(start="2026-08-25", end="2026-10-11", auto_adjust=True)["Close"]
def px(s, t, d):
    return [v for i, v in s[t].items() if str(i.date()) == d][0]
def ret(s, t, a, b):
    return (px(s, t, b) / px(s, t, a) - 1) * 100
def verdict(w, m):
    if w < 0 and m < 0:
        return "MET (both down, wrappers more)" if w < m else "NOT MET (managers led down)"
    if w < 0 <= m:
        return "MIXED (wrappers down, managers up)"
    return "NOT MET (wrappers not down)"
print(f"end={END}")
for a in STARTS:
    row = [a]
    for s in (raw, adj):
        w = sum(ret(s, t, a, END) for t in W) / 4; m = sum(ret(s, t, a, END) for t in M) / 2
        row += [f"{w:+.2f}", f"{m:+.2f}", f"{w - m:+.2f}pp", verdict(w, m)]
    print(" | ".join(row))
for a in ["2026-08-28", "2026-09-24", "2026-09-30"]:
    print(a, "RAW", {t: round(ret(raw, t, a, END), 2) for t in W + M})
    print(a, "ADJ", {t: round(ret(adj, t, a, END), 2) for t in W + M})
print("RAW closes:", {t: {d: round(px(raw, t, d), 2) for d in ["2026-08-28", "2026-09-24", "2026-09-30", END]} for t in W + M})
