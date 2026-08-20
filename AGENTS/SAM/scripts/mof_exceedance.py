"""MOF 4-week-rolling exceedance base rates, computed BOTH ways (all overlapping
observations AND de-clustered episodes), each side of the median quoted separately.

Built 2026-08-20 for BOND (FL-BND-11 successor bar). WHY IT EXISTS:
  A 4wk rolling sum sampled weekly shares 75% of its data with its neighbour, so one
  genuine extreme yields up to four consecutive breaches and a naive base rate
  OVER-COUNTS. Measured over-count: 1.80x-3.22x -- and it is WORST at the LOOSEST bar
  (3.22x at median-1.0sigma) and mildest at the tightest (1.80x at +2.0sigma), i.e.
  the naive rate flatters a loose bar most, which is the dangerous direction.
  The series is LEFT-skewed (mean +0.648T < median +0.723T; min sits 7.05T below the
  median vs max 5.87T above), so the bar must be TWO numbers with separately-quoted
  base rates, never one +/-k*sigma. Centre on the MEDIAN, never zero -- Japan is a
  structural net buyer and a zero-centred bar reports that structure as signal.
"""
import csv, statistics as st

rows = list(csv.DictReader(open("AGENTS/SAM/workbook/MOF_FLOWS.tsv"), delimiter="\t"))
v = [float(r["LT_Debt_Net_T_yen"]) for r in rows
     if r.get("LT_Debt_Net_T_yen") not in (None, "", "-")]
roll = [sum(v[i-3:i+1]) for i in range(3, len(v))]
n = len(roll)
med, sd, mean = st.median(roll), st.pstdev(roll), st.mean(roll)

print(f"4wk rolling sums: n={n}  mean={mean:+.3f}T  median={med:+.3f}T  sigma={sd:.3f}T")
print(f"SKEW: mean - median = {mean-med:+.3f}T  =>  {'LEFT' if mean < med else 'RIGHT'}-skewed")
print(f"  min {min(roll):+.3f}T = {med-min(roll):.2f}T BELOW median")
print(f"  max {max(roll):+.3f}T = {max(roll)-med:.2f}T ABOVE median")
print(f"  => fat tail on the {'SELLING' if (med-min(roll)) > (max(roll)-med) else 'BUYING'} side\n")


def declust(idx):
    """A run of CONSECUTIVE breaching weeks = ONE episode."""
    if not idx:
        return 0
    ep = 1
    for a, b in zip(idx, idx[1:]):
        if b != a + 1:
            ep += 1
    return ep


hdr = f"{'bar':>26} | {'level':>9} | {'obs':>5} {'obs %':>7} | {'episodes':>8} {'ep %':>7} | {'ratio':>6}"
print(hdr)
print("-" * len(hdr))
for k in (1.0, 1.5, 2.0):
    for side in ("-", "+"):
        lvl = med - k * sd if side == "-" else med + k * sd
        idx = [i for i, x in enumerate(roll)
               if (x <= lvl if side == "-" else x >= lvl)]
        ep = declust(idx)
        ratio = (len(idx) / ep) if ep else float("nan")
        print(f"{'median ' + side + f'{k:.1f}s':>26} | {lvl:>+9.3f} | {len(idx):>5} "
              f"{100*len(idx)/n:>6.2f}% | {ep:>8} {100*ep/n:>6.2f}% | {ratio:>5.2f}x")

print(f"\nnon-overlapping 4wk blocks available: n/4 = {n/4:.0f}")
print(f"latest 4wk = {roll[-1]:+.3f}T  =>  {(roll[-1]-med)/sd:+.2f}s vs MEDIAN "
      f"(vs {(roll[-1]-mean)/sd:+.2f}s vs mean)")
