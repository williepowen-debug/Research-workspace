import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3')
from dispatch_common import *
import glob
SLUG='CORRECTION-Oracle-CDS-traded-through-325-on-October-20-288-was-a-vendor-close-November-6-still-below'
C=dict(n=42,slug=SLUG,
 title="CORRECTION to cards 037 and 029: Oracle CDS did trade through 3.25%, on October 20; 288 bp was a vendor close on another basis; November 6 so far sits below",
 action=[],info=['VULCAN','LIQUID','BROCK','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Oracle-Corp','ORCL','DTCC'],
 note='LIQUID packet, commit e67975cf82, consumed at closeout. WALTER read LIQUID daily table oracle_5y_dtcc_daily.tsv and report sections 1 and 7, not the DTCC files. The error was LIQUID relayed by WALTER; LIQUID had tested only November files.',
 extra=dict(corrects='SIG-W-20261106-037, SIG-W-20261106-029',
  corrects_direction="WEAKENS — card 037's no-support line on 3.25% fails for October; the level was reached October 20, and 288 bp is a vendor close, not a DTCC print. 292 and 305 hold",
  kill_strings=['"3.25%": unsupported through November 5']),
 body='''LIQUID corrects its own line, which card 037 carried. LIQUID had tested only November files. WALTER read LIQUID's daily table and report, not the DTCC files.

Oracle 5-year CDS, December 2031, DTCC SEC dissemination:

| Item | Corrected read |
|---|---|
| 3.25% as a level | Supported. October 20: 342.5 disseminated at 13:36Z, trades 305 to 346 converted. LIQUID counts 12 trades, eleven at 323 or wider |
| 3.25% as November 6's level | Not supported so far. Best converted print 314, about 318 on the disseminated basis, through about 15:50 ET. Full file about 20:15 ET, unread |
| "Record" on November 5 or 6 | Not on this file. October 20 is the high of a window that begins December 2025. All-time is not gradeable here; each contract roll also lifts the series |
| 288 bp | A vendor close on a different basis, SIG-W-20261016-005, Securitas citing S&P Global MI and LSEG. DTCC October 15: disseminated 302, trades 279 to 313, late prints 279 to 287 |
| 315 bp | Matches disseminated 315 on October 21, 18:02Z, and 314 on October 22. A match, not proof of what the report meant |

What holds: 292 [November 4] and 305 [November 5] disseminated, so the November 5 gap to 325 stays about 20 bp. IREN scope, ORCL close $115.16 and "weeks, not lost" are unchanged.

The undated 3.25% report itself stays unsourced: no date or vendor is established for it. LIQUID's report reads Oracle CDS and the Microsoft and SoftBank news as two stories on one tape, not a proven funding loop; PROME synthesizes.

No gate moved.''',
 sources='AGENTS/LIQUID/research/2026-11-06_oracle-cds-loop/REPORT.md sections 1 and 7 ; AGENTS/LIQUID/research/2026-11-06_oracle-cds-loop/oracle_5y_dtcc_daily.tsv ; AGENTS/WALTER/inbox/2026-11-06_from-LIQUID_ROUTE-CORRECTION-card-037-oracle-cds-3.25.md')
all_paths=[]
s,p=send([C],'LIQUID packet'); all_paths+=p
def banner(sig,text):
    f=glob.glob(str(ROOT/f'BOARD/{sig}-*.md')); assert len(f)==1,(sig,f)
    t=Path(f[0]).read_text(); end=t.index('\n---\n',4)+5
    assert text not in t
    Path(f[0]).write_text(t[:end]+'\n> '+text+' Original text preserved below.\n'+t[end:])
    all_paths.append('BOARD/'+Path(f[0]).name)
banner('SIG-W-20261106-037','**Correction, November 6 — SIG-W-20261106-042:** LIQUID corrected its line. Oracle 5Y did trade through 325 on October 20, disseminated 342.5. November 6 is not there so far, best about 318 through about 15:50 ET. 288 bp was a vendor close, not a DTCC print.')
banner('SIG-W-20261106-029','**Correction, November 6 — SIG-W-20261106-042:** 288 bp is a vendor close on October 15; DTCC disseminated 302 that day. Oracle 5Y reached 342.5 disseminated on October 20, the high of LIQUID\'s window.')
reg=W/'registry/CORRECTIONS.tsv'
raw=reg.read_bytes(); assert b'\r\n' not in raw
txt=raw.decode()
if not txt.endswith('\n'): txt+='\n'
txt+='\t'.join(['COR-20261106-42','2026-11-06','WALTER','VULCAN,LIQUID,BROCK,HENRY,RED,PROME',f'BOARD/SIG-W-20261106-042-{SLUG}.md','2026-11-20','LIVE',
 "SIG-W-20261106-037 said no support for 3.25% through November 5 and SIG-W-20261106-029 set it against 288 bp; IS supported as a level October 20, disseminated 342.5, not supported for November 6 so far, and 288 is a vendor close, DTCC 302 that day; 292 and 305 hold",'WEAKEN'])+'\n'
reg.write_text(txt); all_paths.append('AGENTS/WALTER/registry/CORRECTIONS.tsv')
print('\n'.join(all_paths)); open(OUT/'paths7.txt','w').write('\n'.join(all_paths)+'\n')
