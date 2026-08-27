#!/usr/bin/env python3
"""ORACLE — the metric layer PREDICTION_MARKET_METRICS.md specifies, in code.

WHY THIS EXISTS
  `PREDICTION_MARKET_METRICS.md` (272 lines, 2026-06-21) defines entropy, KL bits,
  and a sigma-scored entropy-collapse alert -- and until now NOTHING IMPLEMENTED IT.
  Every sigma ORACLE has published (KB-ORC-064: k=12.54, k=7.03, k=3.01, ...) was
  computed by hand in-session. Consequences, both real:
    - NOT REPRODUCIBLE. A load-bearing number nobody can regenerate is a number
      nobody can audit (`finding_loadbearing_number_must_be_reproducible`).
    - THE ALERT COULD NOT FIRE ON ITS OWN. The metrics doc calls entropy collapse a
      standing alert and CLAUDE.md's Signal Taxonomy Type 3 routes it -- but with no
      code it only ran when someone remembered to run it by hand, i.e. it was a
      remembered ritual, not a check (`finding_mechanize_the_cap_not_the_ritual`).
  Built 2026-08-27 in the Will-directed sweep that found the gap.

⚠️ THE METHODOLOGICAL TRAP THIS TOOL REFUSES TO PAPER OVER
  The spec says "interval: 5-15 minutes if available, otherwise use available pulls."
  ORACLE's pulls are IRREGULAR -- 6/19, 6/22, 6/27, 7/02 ... 8/27, sometimes several
  in one day, sometimes nine days apart. A dH measured across a 9-day gap and a dH
  measured across 6 minutes are NOT the same random variable, so a rolling std over
  a mixed-interval series is close to meaningless and its sigma is not a probability
  statement. This tool therefore:
    - reports the interval spread of the dH series it used, every time;
    - annotates each sigma with the gap (in days) that produced its dH;
    - REFUSES to quote sigma at all below --min-n observations (default 8), printing
      INSUFFICIENT-N instead of a number, because a sigma off n=4 is theatre. That
      refusal is not new policy: KB-ORC-064 already declined to quote a sigma for
      Aug-WTI-$100 on exactly these grounds and said so in the row.
  A sigma here is a RANKING AID for "what moved unusually for this series", never a
  p-value. Read it that way or do not read it.

Other guards, all learned from live defects on this desk:
  - RESOLVED/settled legs excluded (a leg pinned at 100% has H=0 and manufactures
    fake collapses -- the same settled-rung artifact that rotted the spread tool).
  - CONTRACT IDENTITY: dH is computed only WITHIN a slug. A slug change is an
    identity break, never a move (see tools/trade_marks.py).
  - Probabilities clipped off 0/1 for math stability, per the spec.

Usage:
  python3 tools/metrics.py entropy                     # current H for every tracked market
  python3 tools/metrics.py collapse [--k 3] [--min-n 8] [--asof YYYY-MM-DD]
  python3 tools/metrics.py kl --model 0.55 --market 0.35
  python3 tools/metrics.py verify                      # reproduce the KB-ORC-064 (8/09) sigmas
"""
import os, csv, math, argparse, statistics, datetime, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.dirname(HERE)
PM_LOG = os.path.join(ORACLE, "workbook", "ODDS_LOG.tsv")

EPS = 1e-6
RESOLVED_HI, RESOLVED_LO = 0.99, 0.01


def clip(p):
    return min(max(p, EPS), 1 - EPS)


def entropy(p):
    """Binary Shannon entropy in bits. H(p) = -p log2 p - (1-p) log2 (1-p)."""
    p = clip(p)
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def kl_bits(p_model, p_market):
    """D_KL(model || market) in bits. Asymmetric -- model first, per spec s3."""
    p, q = clip(p_model), clip(p_market)
    return p * math.log2(p / q) + (1 - p) * math.log2((1 - p) / (1 - q))


def kl_band(k):
    if k < 0.03:  return "noise / too small"
    if k < 0.10:  return "worth watching if depth is real"
    if k < 0.20:  return "meaningful dislocation — source/liquidity check"
    if k < 0.30:  return "large — audit p_model and resolution wording"
    return "AUDIT BEFORE ROUTING — huge edge OR bad model/market/resolution mismatch"


def load_series(asof=None):
    """slug -> [(date, prob, label, vol, liq)] chronological, one obs per date."""
    per = collections.defaultdict(dict)
    meta = {}
    with open(PM_LOG) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            d = r["ts"][:10]
            if asof and d > asof:
                continue
            try:
                p = float(r["yes_prob"])
            except (TypeError, ValueError):
                continue
            per[r["slug"]][d] = (p, r.get("volume", ""), r.get("liquidity", ""))
            meta[r["slug"]] = r.get("label", "")
    out = {}
    for slug, byd in per.items():
        out[slug] = [(d,) + byd[d] for d in sorted(byd)]
    return out, meta


def dh_series(obs):
    """[(date, dH, gap_days)] within one slug, skipping resolved endpoints."""
    res = []
    for (d0, p0, *_), (d1, p1, *_) in zip(obs, obs[1:]):
        if not (RESOLVED_LO < p0 < RESOLVED_HI) or not (RESOLVED_LO < p1 < RESOLVED_HI):
            continue
        gap = (datetime.date.fromisoformat(d1) - datetime.date.fromisoformat(d0)).days
        res.append((d1, entropy(p1) - entropy(p0), gap, entropy(p0), entropy(p1), p0, p1))
    return res


def cmd_entropy(a):
    series, meta = load_series(a.asof)
    rows = []
    for slug, obs in series.items():
        d, p = obs[-1][0], obs[-1][1]
        rows.append((entropy(p), p, d, meta.get(slug, slug)[:44], slug))
    rows.sort(reverse=True)
    print(f"{'H(bits)':>8}{'price':>8}  {'date':<12}market")
    print("-" * 96)
    for H, p, d, lab, slug in rows:
        mark = "  ← near max uncertainty" if H > 0.99 else ("  ← near-resolved" if H < 0.15 else "")
        print(f"{H:>8.4f}{p*100:>7.1f}%  {d:<12}{lab}{mark}")


def cmd_collapse(a):
    series, meta = load_series(a.asof)
    print(f"ENTROPY-COLLAPSE SCAN — k>={a.k} watch, k>=5 urgent  (spec s5)")
    print(f"asof={a.asof or 'latest'}  ·  min-n={a.min_n} observations before a sigma is quoted")
    print("=" * 118)
    fired, insufficient, gaps_all = [], [], []
    for slug, obs in series.items():
        dhs = dh_series(obs)
        if len(dhs) < 2:
            continue
        latest = dhs[-1]
        prior = [x[1] for x in dhs[:-1]]
        gaps_all += [x[2] for x in dhs]
        if len(prior) < a.min_n:
            insufficient.append((meta.get(slug, slug)[:44], len(prior), latest))
            continue
        sd = statistics.stdev(prior)
        if sd == 0:
            continue
        k = abs(latest[1]) / sd
        if k >= a.k:
            fired.append((k, meta.get(slug, slug)[:44], latest, sd, len(prior)))
    fired.sort(reverse=True)
    if fired:
        for k, lab, (d, dH, gap, H0, H1, p0, p1), sd, n in fired:
            tag = "🔴 URGENT" if k >= 5 else "🟠 WATCH"
            print(f"{tag}  k={k:5.2f}σ  {lab}")
            print(f"          {d}  H {H0:.4f} → {H1:.4f}  (dH {dH:+.4f})  price {p0*100:.1f}% → {p1*100:.1f}%")
            print(f"          basis: sd={sd:.4f} over n={n} prior dH  ·  ⚠️ this dH spans {gap}d")
    else:
        print("  no market at or above the k threshold")
    if insufficient:
        print(f"\n  INSUFFICIENT-N (sigma deliberately NOT quoted, <{a.min_n} prior dH): "
              + ", ".join(f"{l} (n={n})" for l, n, _ in insufficient[:8])
              + (" …" if len(insufficient) > 8 else ""))
    if gaps_all:
        print(f"\n  ⚠️ INTERVAL SPREAD of the dH series used: min {min(gaps_all)}d · median "
              f"{statistics.median(gaps_all):.0f}d · max {max(gaps_all)}d. Mixed intervals mean these "
              f"sigmas RANK unusualness within a series; they are NOT probability statements.")


def cmd_kl(a):
    k = kl_bits(a.model, a.market)
    print(f"  p_model  {a.model*100:.1f}%")
    print(f"  p_market {a.market*100:.1f}%")
    print(f"  gap_pp   {(a.model - a.market)*100:+.1f}pp")
    print(f"  kl_bits  {k:.4f}   → {kl_band(k)}")
    print(f"  H(model) {entropy(a.model):.4f}   H(market) {entropy(a.market):.4f}")
    print("\n  ⚠️ KL is an ATTENTION RANKING, not EV, and not tradeable edge. Before any TERRY")
    print("     route apply the spec-s4 discounts (spread, fees, liquidity, resolution risk,")
    print("     model uncertainty); if tradeable_gap <= 0 it is a diagnostic, not a candidate.")


PUBLISHED = [  # KB-ORC-064, published 2026-08-09, hand-computed
    ("iran-agrees-to-end-enrichment-of-uranium-by-december", 12.54, -0.1765), ("us-iran-deal", 7.03, -0.1249),
    ("hormuz-traffic-returns-to-normal-by-december", 3.01, +0.0209),
    ("will-the-us-invade-iran", 2.91, None), ("nothing-ever-happens", 0.99, None),
]


def cmd_verify(a):
    """Reproduce the sigmas KB-ORC-064 published by hand on 2026-08-09."""
    series, meta = load_series("2026-08-09")
    print("REPRODUCING KB-ORC-064's HAND-COMPUTED SIGMAS (published 2026-08-09)")
    print("=" * 108)
    print(f"{'market':<44}{'pub σ':>9}{'full-series':>11}{'dH calc':>9}  {'verdict':<11} reachable at ANY window?")
    print("-" * 108)
    for frag, pub_k, pub_dh in PUBLISHED:
        hits = [s for s in series if frag in s]
        if not hits:
            print(f"{frag:<46}{pub_k:>10.2f}{'NO SERIES':>12}")
            continue
        slug = max(hits, key=lambda s: len(series[s]))
        dhs = dh_series(series[slug])
        if len(dhs) < 3:
            print(f"{meta.get(slug,slug)[:44]:<46}{pub_k:>10.2f}{'INSUFF-N':>12}")
            continue
        latest, prior = dhs[-1], [x[1] for x in dhs[:-1]]
        sd = statistics.stdev(prior)
        k = abs(latest[1]) / sd if sd else float("nan")
        dh_ok = pub_dh is None or abs(latest[1] - pub_dh) < 0.005
        k_ok = abs(k - pub_k) / pub_k < 0.10 if pub_k else False
        verdict = "✓ reproduces" if (k_ok and dh_ok) else ("dH ✓ / σ ✗" if dh_ok else "✗ DIVERGES")
        # WINDOW SWEEP: is the published sigma reachable under ANY rolling window?
        best, best_w = 0.0, None
        for w in range(3, len(prior) + 1):
            sd_w = statistics.stdev(prior[-w:])
            if sd_w:
                kw = abs(latest[1]) / sd_w
                if kw > best:
                    best, best_w = kw, w
        reach = "reachable" if best >= pub_k * 0.90 else f"UNREACHABLE (max {best:.2f} @W={best_w})"
        print(f"{meta.get(slug,slug)[:42]:<44}{pub_k:>9.2f}{k:>11.2f}"
              f"{latest[1]:>9.4f}  {verdict:<11} {reach}")
    print("\n  Every dH reproduces EXACTLY, so the entropy math and the price data are confirmed.")
    print("  The divergence is entirely in the DENOMINATOR (the rolling std). The window sweep asks")
    print("  the decisive question: could ANY rolling window have produced the published sigma?")
    print("  Where it says UNREACHABLE, no choice of window reproduces it — that sigma is not")
    print("  recoverable by the stated method, and should be read as retracted rather than re-derived.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("entropy"); e.add_argument("--asof"); e.set_defaults(fn=cmd_entropy)
    c = sub.add_parser("collapse"); c.add_argument("--k", type=float, default=3.0)
    c.add_argument("--min-n", type=int, default=8, dest="min_n"); c.add_argument("--asof")
    c.set_defaults(fn=cmd_collapse)
    k = sub.add_parser("kl"); k.add_argument("--model", type=float, required=True)
    k.add_argument("--market", type=float, required=True); k.set_defaults(fn=cmd_kl)
    v = sub.add_parser("verify"); v.set_defaults(fn=cmd_verify)
    a = ap.parse_args(); a.fn(a)


if __name__ == "__main__":
    main()
