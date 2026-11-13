import sys, re, glob, os
d = sys.argv[1]
rows = []
for f in sorted(glob.glob(os.path.join(d, '*CFR.txt'))):
    q = os.path.basename(f)[:6]
    t = re.sub(r'\s+', ' ', open(f).read())
    m = re.search(r'Collateral Outstanding at ([A-Z][a-z]+ \d+, \d{4}) \(dollars in millions\)(.{0,700}?)Based on', t)
    if not m:
        print(q, 'NO TABLE'); continue
    body = m.group(2)
    nums = [int(x.replace(',', '')) for x in re.findall(r'(?<![\d.])(\d{1,3}(?:,\d{3})+)(?![\d.])', body)]
    pcts = [float(x) for x in re.findall(r'(\d+\.\d) ?%', body)]
    if len(nums) == 4 and len(pcts) == 2:  # older layout: advances + collateral only
        all_c = max(nums); rest = [n for n in nums if n != all_c]
        lg_c = min(rest, key=lambda n: abs(n - all_c * pcts[1] / 100)); rest.remove(lg_c)
        all_a = max(rest); lg_a = min(rest)
        all_o = lg_o = 0
    elif len(nums) == 6 and len(pcts) == 3:
        all_c = max(nums); rest = [n for n in nums if n != all_c]
        lg_c = min(rest, key=lambda n: abs(n - all_c * pcts[2] / 100)); rest.remove(lg_c)
        all_a = max(rest); rest.remove(all_a)
        lg_a = min(rest, key=lambda n: abs(n - all_a * pcts[0] / 100)); rest.remove(lg_a)
        all_o, lg_o = max(rest), min(rest)
    else:
        print(q, 'UNPARSED', nums, pcts); continue
    r_all = all_c / (all_a + all_o); r_lg = lg_c / (lg_a + lg_o)
    rows.append((q, all_a, all_o, all_c, r_all, r_lg))
    print(f"{q} adv_all {all_a/1e3:7.1f}B oth_all {all_o/1e3:6.1f}B coll_all {all_c/1e3:7.1f}B ratio_all {r_all:4.2f} ratio_lg {r_lg:4.2f}")
