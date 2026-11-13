import sys, re, os, glob
from concurrent.futures import ProcessPoolExecutor
from pdfminer.high_level import extract_text
d = sys.argv[1]
def one(p):
    out = p[:-4] + '.txt'
    if not os.path.exists(out):
        t = extract_text(p)
        open(out, 'w').write(t)
    return p
with ProcessPoolExecutor(8) as ex:
    for p in ex.map(one, sorted(glob.glob(os.path.join(d, '*.pdf')))):
        pass
for out in sorted(glob.glob(os.path.join(d, '*.txt'))):
    t = re.sub(r'\s+', ' ', open(out).read())
    m1 = re.search(r'collateralization ratio for borrowers with at least \$1\.0 billion[^.]*?was ([0-9.]+)', t)
    m2 = re.search(r'collateralization ratio for all borrowers was ([0-9.]+)', t)
    m3 = re.search(r'there were (\d+) individual FHLBank borrowers', t)
    print(os.path.basename(out)[:6], m1.group(1) if m1 else None, m2.group(1) if m2 else None, m3.group(1) if m3 else None)
