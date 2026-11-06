import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3')
from dispatch_common import *
import glob
SLUG='CORRECTION-SoftBank-leverage-22-to-24-percent-bridge-repaid-ABB-prohibition-is-China-business-only'
C=dict(n=41,slug=SLUG,
 title="CORRECTION to cards 036, 003 and 040: SoftBank leverage about 22% to 24%; its $40B bridge is repaid; China's ABB ban covers the China business",
 action=[],info=['VULCAN','SAM','LIQUID','BROCK','ZHAO','HENRY','VIOLET','RED','REGINALD','SHADE','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['SoftBank','Arm','ABB-robotics','OpenAI','SB-Energy','NVIDIA','Apollo'],
 note='SAM packet, commit 0a7c2e3d8a, relayed by PROME, replaces SAM leverage line of commit 87f84f9d84. WALTER read SoftBank notices of November 6 and October 1 and reran ltv_remark.py; inputs, loan terms, S-1 and press items are SAM read.',
 extra=dict(corrects='SIG-W-20261106-036, SIG-W-20261106-003, SIG-W-20261106-040',
  corrects_direction="WEAKENS — card 036 cushion was thinner than stated on the recourse view; card 003 deal-dead reading withdrawn. The bridge wall is gone, which helps",
  kill_strings=['China prohibited its $5.4B ABB robotics deal','about 21.5%','$40B bridge due March 2027']),
 body='''SAM replaces its earlier leverage line. WALTER read SoftBank's ABB and October 1 notices itself and reran SAM's script; the inputs, loan terms, S-1 and press items are SAM's read.

Leverage, SAM's estimate, not SoftBank's number, Arm $172, USD/JPY 158.5:

| View | Now | September 30 estimate | Arm price for 25% |
|---|---:|---:|---:|
| SoftBank's definition | 22.1% | 15.2% | $128 |
| Counting the $10B loan SoftBank Group guarantees | 24.2% | 17.0% | $160 |

This supersedes card 036's 21.5%, $118 and 13.7% to 16.5%. $160 is 7% below Arm's price. Other SVF values stay at June 30, and listed holdings have probably fallen; monetizations are unknown. The ⛔ on November 10 stands: the headline will be as of September 30.

- Bridge: dead as a wall. $25.9B prepaid September 15, undrawn $10B cancelled September 30, nothing outstanding, SoftBank. Next large maturity: Arm margin loan, about $25B, September 2027, press.
- $10B loan: filing lists a cash collateral account, guarantor SoftBank Group, and prepayment on a significant fall in OpenAI's fair value, threshold undisclosed. "Backed entirely by OpenAI shares" and card 040's "OpenAI-share margin loan" overstate. Drawdown unconfirmed.
- $11.87B facility: "OpenAI-share" is unproven. Bloomberg says "to support its investment"; collateral undisclosed.
- Debt added $40.4B: no document read prints it. Do not carry.
- OpenAI: $64.6B, about 13%, third tranche October 1, SoftBank. Card 030's $64B holds.
- ABB: SoftBank, November 6: China "prohibited the acquisition of ABB's robotics business in China"; both parties "working constructively". Notified November 4. Card 003 overstated it. Do not say the deal is dead.

New, SAM: subsidiary SB Energy is OpenAI's landlord at Milam, 753 MW, and PORTS-Pike, 8.0 GW. NVIDIA, not SoftBank, gives a residual value guaranty up to $105B on the first 4.25 GW. SoftBank and Oracle share a counterparty, OpenAI, with no financing link found in text read; slide images unread.

SHADE: Apollo is a lead arranger and SoftBank Group guarantor on the $10B loan. That fits your arithmetic; it does not prove it.

No score or grade moved here.''',
 sources='https://group.softbank/en/news/press/20261106 ; https://group.softbank/en/news/press/20261001 ; AGENTS/SAM/research/outputs/2026-11-06_softbank/SOFTBANK_FUNDING_STACK.md ; AGENTS/SAM/research/outputs/2026-11-06_softbank/ltv_remark.py ; AGENTS/WALTER/inbox/processed/2026-11-06_from-SAM_correction-to-card036-and-003.md')
all_paths=[]
s,p=send([C],'SAM packet'); all_paths+=p
def banner(sig,text):
    f=glob.glob(str(ROOT/f'BOARD/{sig}-*.md')); assert len(f)==1,(sig,f)
    t=Path(f[0]).read_text(); end=t.index('\n---\n',4)+5
    assert text not in t
    Path(f[0]).write_text(t[:end]+'\n> '+text+' Original text preserved below.\n'+t[end:])
    all_paths.append('BOARD/'+Path(f[0]).name)
banner('SIG-W-20261106-036','**Correction, November 6 — SIG-W-20261106-041:** SAM replaced this leverage line. About 22% on SoftBank\'s definition, about 24% counting the loan it guarantees; 25% near Arm $128 or $160; September 30 about 15% to 17%. All SAM estimates.')
banner('SIG-W-20261106-003','**Correction, November 6 — SIG-W-20261106-041:** SoftBank says China prohibited the acquisition of ABB\'s robotics business in China, and both parties are working constructively. Do not say the deal is dead. Results are November 10, 15:30 JST.')
banner('SIG-W-20261106-040','**Correction, November 6 — SIG-W-20261106-041:** the $10B loan\'s filing lists a cash collateral account and SoftBank Group as guarantor, so "OpenAI-share margin loan" overstates it. Athene figures are unaffected.')
banner('SIG-W-20261106-030','**Correction, November 6 — SIG-W-20261106-041:** SAM\'s leverage estimate is now about 22% to 24%, replacing card 036\'s. OpenAI $64.6B holds. Debt added $40.4B is unconfirmed; do not carry.')
reg=W/'registry/CORRECTIONS.tsv'
raw=reg.read_bytes(); assert b'\r\n' not in raw
txt=raw.decode()
if not txt.endswith('\n'): txt+='\n'
txt+='\t'.join(['COR-20261106-41','2026-11-06','WALTER','VULCAN,SAM,LIQUID,BROCK,ZHAO,HENRY,VIOLET,RED,REGINALD,SHADE,PROME',f'BOARD/SIG-W-20261106-041-{SLUG}.md','2026-11-20','LIVE',
 "SIG-W-20261106-036 said SoftBank leverage 21.5%, 25% near Arm $118; IS 22.1%, or 24.2% counting the guaranteed $10B loan, 25% near Arm $128 or $160 (SAM estimate); SIG-W-20261106-003 said China prohibited the ABB deal; IS the China business only, deal not dead (SoftBank notice); bridge repaid, card 030 marginal-funder reading holds",'WEAKEN'])+'\n'
reg.write_text(txt); all_paths.append('AGENTS/WALTER/registry/CORRECTIONS.tsv')
print('\n'.join(all_paths)); open(OUT/'paths6.txt','w').write('\n'.join(all_paths)+'\n')
