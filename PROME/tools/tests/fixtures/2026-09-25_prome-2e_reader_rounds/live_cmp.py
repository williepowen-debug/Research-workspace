import csv, re, os, sys
sys.path.insert(0, "PROME/tools")
import prome_gate as G
with open("PROME/GATES.tsv", encoding="utf-8") as f:
    rows = [r for r in csv.reader(f, delimiter="\t") if r and not r[0].startswith("#") and r[0] != "gate_id"]
with open("PROME/GATES.tsv", encoding="utf-8") as f:
    R = [r for r in csv.reader(f, delimiter="\t") if r and not r[0].startswith("#")]
h = R[0]; print("header idx: cond", h.index("condition"), "state", h.index("state"), "defsurf", h.index("definition_surface"), "ncols", len(h))
live = [r for r in rows if len(r) > 10 and r[5].startswith("LIVE")]
live_all = [r for r in rows if len(r) > 5 and r[5].startswith("LIVE")]
print("rows", len(rows), "LIVE (len>10)", len(live), "LIVE any-len", len(live_all))
short = [ (r[0], len(r)) for r in rows if len(r) <= 10]
print("rows with len<=10:", short)
o = G.scan_gate_citability(rows, G.ROOT)
print(G.citability_detail(o)); print("unreachable", o["unreachable"])
# one-liner set (isfile relative to cwd)
oneliner = sorted({p for r in live_all for p in re.findall(r'[\w./-]+\.(?:md|tsv)', r[10]) if os.path.isfile(p)})
allpaths = sorted({p for r in live_all for p in re.findall(r'[\w./-]+\.(?:md|tsv)', r[10])})
leg = sorted({p for r in live for p in re.findall(r'[\w./-]+\.(?:md|tsv)', r[10]) if p not in G.CITABILITY_NEVER_SCAN and (G.ROOT/p).is_file()})
print("oneliner n", len(oneliner), "leg n", len(leg), "same", oneliner == leg)
print("all extracted", len(allpaths)); print("unreachable in oneliner (silently dropped):", [p for p in allpaths if not os.path.isfile(p)])
for r in live:
    print("---", r[0], "|", r[5][:40], "|", r[10][:200])
    print("    extracted:", re.findall(r'[\w./-]+\.(?:md|tsv)', r[10]))
