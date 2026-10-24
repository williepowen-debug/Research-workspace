"""Regional-bank put cluster arithmetic, TERRY 2026-10-24 (Sat). Inputs are dated:
lines + basis + 10/22 marks = PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md (FORGE ec5a7058b);
underlying = 10/23 regular-session closes from FORGE/tools/market-data/fetch.py price (pulled 2026-10-24 14:42 ET).
Scenario = expiry intrinsic under a UNIFORM % fall in every underlying by each line's expiry (MODEL; no time value)."""
LINES = [  # ticker, expiry, strike, qty, basis $, value $ at 10/22 11:01 ET broker last
    ("KRE", "2026-11-20", 66, 3, 133.99, 120.00), ("KRE", "2026-11-27", 67, 4, 510.65, 200.00),
    ("KRE", "2026-11-27", 70, 2, 281.33, 244.00), ("KRE", "2026-12-18", 60, 2, 513.34, 58.00),
    ("KRE", "2026-12-18", 60, 3, 878.02, 87.00), ("KRE", "2026-12-31", 65, 2, 337.33, 164.00),
    ("OZK", "2026-11-20", 40, 4, 322.65, 20.00), ("ZION", "2026-11-20", 62.5, 2, 435.33, 130.00),
    ("WAL", "2026-12-18", 65, 4, 682.65, 220.00), ("WAL", "2026-12-18", 70, 2, 551.33, 320.00)]
PX = {"KRE": 72.46, "OZK": 50.61, "ZION": 66.20, "WAL": 76.12}
ACCT = 39876.06  # displayed account total, 10/22 11:01 ET capture

def intrinsic(fall_pct):
    return sum(max(k - PX[t] * (1 - fall_pct / 100), 0) * 100 * q for t, e, k, q, b, v in LINES)

if __name__ == "__main__":
    B = sum(l[4] for l in LINES); V = sum(l[5] for l in LINES)
    print(f"contracts {sum(l[3] for l in LINES)} basis ${B:,.2f} value(10/22) ${V:,.2f} "
          f"basis/acct {B/ACCT:.2%} value/acct {V/ACCT:.2%}")
    for t, e, k, q, b, v in LINES:
        be = k - b / q / 100
        print(f"{t} {e} {k}P x{q}: OTM {(PX[t]-k)/PX[t]:.1%}  BE {be:.2f} ({(PX[t]-be)/PX[t]:.1%} fall)  basis ${b:,.2f}")
    for d in (0, 5, 10, 15, 20, 25):
        print(f"uniform fall {d:>2}%: intrinsic ${intrinsic(d):,.0f}  vs basis ${intrinsic(d)-B:,.0f}")
    d = 0.0
    while intrinsic(d) < B: d += 0.01
    print(f"cluster breakeven (uniform fall, expiry intrinsic): {d:.2f}%")
