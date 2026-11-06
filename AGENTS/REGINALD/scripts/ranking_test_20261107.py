#!/usr/bin/env python3
"""One-time run of the FROZEN 11/07 ranking test (reports/2026-10-23_ranking-test_FROZEN_protocol.md).

Retrospective validation of frozen 8/20 scores, not a blind test. Will froze the protocol
2026-10-23; this script implements it and changes no choice in it. Refuses to run if the
protocol's sha256 differs. A defect found later is recorded in the results, never repaired
in the protocol.

Run from repo root, on or after 2026-11-07:
    .venv/bin/python3 AGENTS/REGINALD/scripts/ranking_test_20261107.py
Mechanics only, on quarters that carry no Q3 outcome (safe before the frozen date):
    .venv/bin/python3 AGENTS/REGINALD/scripts/ranking_test_20261107.py --mechanics
"""
import datetime
import hashlib
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import mi3_cohort_screen as m  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[3]
PROTOCOL = ROOT / "AGENTS/REGINALD/reports/2026-10-23_ranking-test_FROZEN_protocol.md"
SHA = "06e37edad2d583074a20f0ca70d0f84079a3eed95fba891204060662bcd00672"
FROZEN_DATE = datetime.date(2026, 11, 7)

# Fixed by the protocol: bank -> (S1, S2, B1)
FROZEN = {
    "FLG": (6, 5, 4.88), "EGBN": (5, 4, 2.05), "AMTB": (5, 4, 2.46), "VLY": (3, 3, 0.88),
    "OZK": (2, 2, 0.92), "WAL": (2, 1, 0.86), "SSB": (2, 2, 0.53), "BKU": (2, 1, 0.95),
    "SBCF": (2, 2, 0.66), "ZION": (1, 1, 0.47), "MTB": (1, 1, 0.84), "CUBI": (1, 1, 0.31),
    "CFG": (0, 0, 0.96), "HBAN": (0, 0, 0.84),
}


def avg_ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2.0 + 1
        i = j + 1
    return ranks


def spearman(a, b):
    ra, rb = avg_ranks(a), avg_ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    da = sum((x - ma) ** 2 for x in ra) ** 0.5
    db = sum((y - mb) ** 2 for y in rb) ** 0.5
    return num / (da * db) if da and db else float("nan")


def top_vs_rest(score, outcome):
    third = sorted(score, reverse=True)[2]        # ties at third place join the top group
    top = [o for s, o in zip(score, outcome) if s >= third]
    rest = [o for s, o in zip(score, outcome) if s < third]
    return len(top), sum(top) / len(top), (sum(rest) / len(rest) if rest else float("nan"))


def field(d, code):
    for p in ("RCON", "RCFD", "RIAD"):
        if p + code in d:
            return d[p + code]
    return None


def pull(user, token, rssd, period):
    sdf = m.facsimile(user, token, rssd, period, use_cache=False)   # both endpoints one vintage
    return m.parse(sdf) if sdf else None


def selftest():
    assert avg_ranks([1, 2, 2, 3]) == [1.0, 2.5, 2.5, 4.0]
    assert abs(spearman([1, 2, 3, 4], [1, 2, 3, 4]) - 1) < 1e-12
    assert abs(spearman([1, 2, 3, 4], [4, 3, 2, 1]) + 1) < 1e-12
    assert top_vs_rest([5, 4, 3, 3, 1], [1, 1, 1, 1, 9])[0] == 4     # tie at third included
    print("selftest ok")


def run(prior_q, base_q, end_q, ytd_base_q, label):
    user, token = m.creds()
    rows, missing = {}, []
    for row in m.COHORT:
        tk, rssd = row[0], row[1]
        a, b, c = pull(user, token, rssd, prior_q), pull(user, token, rssd, base_q), pull(user, token, rssd, end_q)
        if not (a and b and c):
            missing.append(tk)
            continue
        la, lb, lc = field(a, "2122"), field(b, "2122"), field(c, "2122")
        na, nb, nc = field(a, "1403"), field(b, "1403"), field(c, "1403")
        ytd = pull(user, token, rssd, ytd_base_q)
        co = (field(c, "4635") or 0) - (field(c, "4605") or 0)
        cob = (field(ytd, "4635") or 0) - (field(ytd, "4605") or 0)
        if None in (la, lb, lc, na, nb, nc) or field(c, "4635") is None:
            missing.append(tk)
            continue
        s1, s2, b1 = FROZEN[tk]
        rows[tk] = dict(s1=s1, s2=s2, b1=b1, b2=100.0 * (nb / lb - na / la),
                        primary=100.0 * (nc / lc - nb / lb), secondary=100.0 * (co - cob) / lc * 4)
    n = len(rows)
    print(f"{label}; n = {n} of 14; missing: {missing or 'none'}")
    print("bank  S1 S2   B1    B2     primary  secondary")
    for tk, r in rows.items():
        print(f"{tk:5} {r['s1']:2} {r['s2']:2} {r['b1']:5.2f} {r['b2']:6.3f} {r['primary']:8.3f} {r['secondary']:8.3f}")
    corr = {}
    for out in ("primary", "secondary"):
        print(f"\nOutcome: {out}")
        for k in ("s1", "s2", "b1", "b2"):
            sc, oc = [r[k] for r in rows.values()], [r[out] for r in rows.values()]
            corr[(out, k)] = spearman(sc, oc)
            t, mt, mr = top_vs_rest(sc, oc)
            print(f"  {k.upper()}: Spearman {corr[(out, k)]:+.3f}; top group n={t} mean {mt:+.3f}; other {n - t} mean {mr:+.3f}")
    print("\nReading rule: differences under 0.2 = no distinguishable difference. No significance claims.")
    for out in ("primary", "secondary"):
        print(f"  {out}: S1 vs B1 difference {corr[(out, 's1')] - corr[(out, 'b1')]:+.3f}; S1 vs B2 {corr[(out, 's1')] - corr[(out, 'b2')]:+.3f}")


SIDE_LIST = (("Preferred", 1918344), ("NexBank", 652874))  # WQ-624 A: beside the score, not in it


def side_list():
    user, token = m.creds()
    print("\nSide list (WQ-624 A): reported beside the score, in no statistic. $K, 9/30/2026")
    for name, rssd in SIDE_LIST:
        d = pull(user, token, rssd, "9/30/2026")
        if not d:
            print(f"  {name}: no Q3 Call Report at retrieval")
            continue
        print(f"  {name}: " + " ".join(f"{c}={field(d, c)}" for c in ("2746", "3499", "F179", "3501", "F183", "1403", "2122")))


def main():
    got = hashlib.sha256(PROTOCOL.read_bytes()).hexdigest()
    if got != SHA:
        sys.exit(f"REFUSED: protocol sha256 {got} does not match the frozen value")
    selftest()
    if "--mechanics" in sys.argv:
        run("12/31/2025", "3/31/2026", "6/30/2026", "3/31/2026",
            "MECHANICS CHECK ONLY, old quarters, not the frozen test")
        return
    if datetime.date.today() < FROZEN_DATE:
        sys.exit("REFUSED: the frozen protocol is the November 7 evaluation; use --mechanics before then")
    run("3/31/2026", "6/30/2026", "9/30/2026", "6/30/2026",
        "Retrospective validation of frozen 8/20 scores, not a blind test")
    side_list()


if __name__ == "__main__":
    main()
