import csv,sys,collections
for y in [2021,2022,2023,2024,2025]:
    rows=list(csv.DictReader(open(f'hmda/ufb_{y}.csv')))
    mf=[r for r in rows if r['total_units'] not in ('1','2','3','4')]
    orig=[r for r in mf if r['action_taken'] in ('1','6')]
    tot=sum(float(r['loan_amount']) for r in orig)
    print(f"== {y}: all rows {len(rows)}, MF rows {len(mf)}, MF originated/purchased {len(orig)}, ${tot/1e6:,.1f}M")
    st=collections.Counter(); amt=collections.Counter(); pur=collections.Counter(); purp=collections.Counter(); act=collections.Counter(); rate=[]; term=collections.Counter(); units=collections.Counter(); lt=collections.Counter(); intonly=collections.Counter()
    for r in orig:
        st[r['state_code']]+=1; amt[r['state_code']]+=float(r['loan_amount'])
        pur[r['purchaser_type']]+=1; purp[r['loan_purpose']]+=1; term[r['loan_term']]+=1; units[r['total_units']]+=1; lt[r['loan_type']]+=1; intonly[r['interest_only_payment']]+=1
        act[r['action_taken']]+=1
        try: rate.append(float(r['interest_rate']))
        except: pass
    print(' states $M:', {k: round(v/1e6,1) for k,v in amt.most_common()})
    print(' purchaser_type:',dict(pur),' purpose:',dict(purp),' action:',dict(act),' loan_type:',dict(lt))
    print(' term:',dict(term.most_common(8)),' IO:',dict(intonly),' units:',dict(units))
    if rate: rate.sort(); print(' rate min/med/max', rate[0], rate[len(rate)//2], rate[-1])
    mfl=[r for r in mf if r['action_taken'] not in ('1','6')]
    if mfl: print(' other MF actions:', collections.Counter(r['action_taken'] for r in mfl))
