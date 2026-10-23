#!/usr/bin/env python3
"""Regenerate MEMORY_CYCLE's read-only views from the canonical ledgers.

Run from anywhere: python3 AGENTS/VULCAN/MEMORY_CYCLE/build_views.py
Outputs (GENERATED, never edit by hand; the sources stay canonical):
  S2_FACTS.tsv        every KB row with channel S2, plus rows on other channels whose fact
                      names memory (DRAM/NAND/HBM/Micron/hynix/Samsung...) - column `match`
                      says which (workbook/KB_GENERAL.tsv + CRWV/KB.tsv)
  S2_PREDICTIONS.tsv  every live or resolved prediction with channel S2
Re-run after any S2 KB or prediction write; a view older than its source is stale.
"""
import csv, glob, os, re, sys
KW = re.compile(r"\b(DRAM|NAND|HBM|DDR[45]|memory|Micron|MU|SK hynix|hynix|Samsung|Solidigm|SanDisk|SNDK|Kioxia|CXMT|YMTC|TrendForce)\b", re.I)
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.dirname(D)

def rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f, delimiter="\t"))
    return r[0], r[1:]

def write(name, header, body, sources):
    out = os.path.join(D, name)
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header + ["source_file"])
        w.writerows(body)
    print(f"{name}: {len(body)} rows from {', '.join(sources)}")

facts, src = [], []
hdr = None
for p in ["workbook/KB_GENERAL.tsv", "CRWV/KB.tsv"]:
    h, b = rows(os.path.join(V, p))
    if "channel" not in h:
        continue
    hdr = hdr or h
    ci = h.index("channel")
    fi = h.index("fact")
    sel = []
    for r in b:
        if len(r) <= max(ci, fi):
            continue
        m = "channel-S2" if r[ci] == "S2" else ("keyword" if KW.search(r[fi]) else "")
        if m:
            sel.append([r[h.index(c)] if c in h and h.index(c) < len(r) else "" for c in hdr] + [p, m])
    facts += sel; src.append(p)
out = os.path.join(D, "S2_FACTS.tsv")
with open(out, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(hdr + ["source_file", "match"]); w.writerows(facts)
print(f"S2_FACTS.tsv: {len(facts)} rows ({sum(r[-1]=='channel-S2' for r in facts)} channel-S2, {sum(r[-1]=='keyword' for r in facts)} keyword) from {', '.join(src)}")

preds, src, hdr = [], [], None
for p in sorted(glob.glob(os.path.join(V, "archive", "PREDICTIONS_RESOLVED_*.tsv"))) + [os.path.join(V, "workbook", "PREDICTIONS.tsv")]:
    h, b = rows(p); hdr = hdr or h
    ci = h.index("channel")
    rel = os.path.relpath(p, V)
    sel = [r + [rel] for r in b if len(r) > ci and "S2" in r[ci]]
    preds += sel; src.append(rel)
write("S2_PREDICTIONS.tsv", hdr, preds, src)
