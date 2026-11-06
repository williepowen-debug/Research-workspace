#!/usr/bin/env python3
"""Print every gross-charge-off-by-origination-year block (consumer automotive line + headers) from the Ally filings."""
import re,sys
for fn in ['ally-20230930','ally-20231231','ally-20240930','ally-20241231','ally-20250930','ally-20251231','ally-20260930']:
    L=open(fn+'.htm.txt').read().split('\n')
    idx=[i for i,l in enumerate(L) if re.search(r'present gross charge-offs',l)]
    print('=====',fn,idx)
    for i in idx:
        print('  ',L[i][:200])
        for k in range(i+1,i+40):
            l=L[k]
            if re.match(r'(Origination year|September 30|December 31|Year ended|\t?20\d\d\t|\t20)',l) or l.startswith('Consumer automotive') or re.match(r'\(a\)',l):
                print('   ',k,l[:170].replace('\t','|'))
