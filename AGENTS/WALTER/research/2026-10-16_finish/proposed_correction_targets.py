"""Review-only R1 pointer resolver; not installed in the shared checker.
Prefer all explicit corrects IDs. Filename fallback accepts only unambiguous
YYYYMMDD-NNN or same-day NNN; never guess cross-date shorthand014-018.
"""
import re
from pathlib import Path

def originals(filename, metadata):
    value=metadata.get('corrects', '')
    if value:
        ids=list(dict.fromkeys(re.findall(r'SIG-W-\d{8}-\d{3}\b', str(value))))
        return ids, 'frontmatter' if ids else 'unresolved-explicit'
    full=re.search(r'-to-(\d{8})-(\d{3})(?!-\d{3}\b)\b',filename)
    if full:return ['SIG-W-'+full[1]+'-'+full[2]],'filename-full'
    short=re.search(r'-to-(\d{3})(?!-\d{3}\b)\b',filename)
    own=re.match(r'SIG-W-(\d{8})-\d{3}',filename)
    if short and own:return ['SIG-W-'+own[1]+'-'+short[1]],'filename-same-day'
    return [],'unresolved'

def frontmatter(path):
    lines=Path(path).read_text().splitlines(); out={}
    if not lines or lines[0]!='---':return out
    for line in lines[1:]:
        if line=='---':break
        key,sep,value=line.partition(':')
        if sep:out[key.strip()]=value.strip().strip('\"\'')
    return out

if __name__=='__main__':
    import csv,json
    root=Path(__file__).resolve().parents[4]; board=root/'BOARD'
    reg=list(csv.DictReader((line for line in (root/'AGENTS/WALTER/registry/CORRECTIONS.tsv').open() if line.strip() and not line.startswith('#')),delimiter='\t'))
    results=[]
    for n in ('005','006'):
        sid='SIG-W-20261015-'+n; path=next(board.glob(sid+'-*.md')); fm=frontmatter(path)
        ids,basis=originals(path.name,fm); union=set()
        for target in [sid]+ids:
            tf=frontmatter(next(board.glob(target+'-*.md')))
            for k in ('action','info'):union.update(re.findall(r'[A-Z][A-Z0-9_]+',tf.get(k,'')))
        row=next(r for r in reg if sid in r.get('pointer','')); actual=set(row['targets'].split(','))
        assert union<=actual,(sid,union-actual)
        results.append(dict(signal=sid,originals=ids,basis=basis,required=sorted(union),missing=sorted(union-actual)))
    assert originals('SIG-W-20261015-005-CORRECTION-to-014-018-x.md',{})==([], 'unresolved')
    assert originals('SIG-W-20261015-005-CORRECTION-to-014-x.md',{})[0]==['SIG-W-20261015-014']
    assert originals('SIG-W-20261015-005-CORRECTION-to-20261014-018-x.md',{})[0]==['SIG-W-20261014-018']
    assert originals('SIG-W-20261015-005-CORRECTION-to-014-x.md',{'corrects':'EXTERNAL: claim'})[0]==[]
    print(json.dumps({'scope':'two actual repaired rows plus four pointer fixtures; not installed','results':results},indent=2))
