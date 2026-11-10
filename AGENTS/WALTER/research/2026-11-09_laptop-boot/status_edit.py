import re, datetime
from pathlib import Path
W=Path('/home/willi/Research-workspace/AGENTS/WALTER')
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
s=(W/'STATUS.md').read_text()
# header
s=re.sub(r'^\*\*Updated:\*\*.*$', f"**Updated:** {now} — Tier 2 FULL closeout on the laptop (WilliePOwen), session walter-bb, on Will's 20:15 ET go-ahead; clears the six light-closeout breadcrumbs since November 6. Coverage PARTIAL. Duties: LAST_COMPLETION.md.", s, count=1, flags=re.M)
# bottom line
bl_start=s.index('## BOTTOM LINE\n')+len('## BOTTOM LINE\n\n')
new_par=("November 9 evening (laptop boot, Will's go-ahead 20:15 ET): 2 cards, 1 correction, no IMMEDIATE, no FLASH. Card 011 (COR-20261109-11, STRENGTHEN) corrects 004: Huang acknowledged the affair in an open letter, Nvidia announced its own investigation Sunday, and Trump says the FBI is \"looking into it in terms of something else\", not that Huang himself is under investigation (AP read at NBC New York; the letter unread). VULCAN and HENRY, both live, doorbelled. Card 012: seven small items under WQ-622 (WAL Q3 Basel III disclosure posted, unread; Russian diesel drones; Paraguay teachers' strike; tungsten drill bits; Wyoming trona layoffs; FTC nominee; a Japan intervention retrospective). Scan: HY 342 [Nov 6], REG-T-04 0/3, 8 bp; vendor VIX 19.92 Monday; no new fire. Cboe and Nasdaq November 6 rows now certified. X bookmarks blocked: token refresh fails on the laptop, needs Will's browser.\n\n")
s=s[:bl_start]+new_par+s[bl_start:]
rot=[]
for key in ['November 7 morning: 3 cards','Night boot: card 054 IMMEDIATE']:
    i=s.index(key); j=s.index('\n\n',i)+2
    rot.append(s[i:j]); s=s[:i]+s[j:]
# observation row
anchor='|---|---|\n'
k=s.index(anchor, s.index('## DATED MARKET OBSERVATIONS'))+len(anchor)
row=("| November 9 laptop boot (pull November 10 01:18Z; vendor rows dated November 9 are not closes) | FRED HY 342, CCC 1,317, VIXCLS 25.64 [Nov 6]; T5YIFR 2.19 [Nov 9]; SOFR 3.89 less IORB 3.90 = −1 bp [Nov 6]. Cboe History VIX 25.64, SKEW 153.55 [Nov 6]; VIX9D 19.88, VIX3M 20.85, VVIX 98.43 [Nov 9]. Nasdaq WAL 75.55, KRE 72.20 [Nov 6]. Vendor November 9: VIX 19.92, S&P 7,549.94 (+2.35%), QQQ +3.54%, SMH +5.05%, NVDA 178.67 (−4.27%), KRE 73.45, WAL 77.20 (under 78, existing cycle), HYG 77.51, BZF27 92.17, CLF27 85.22. Cushing 27.250M [w/e Oct 30]. REG-T-04 0/3, 8 bp, near-trigger watch. Registries unchanged since November 7, not re-read whole. No new fire or exit established. Evidence: research/2026-11-09_laptop-boot/THRESHOLD-SCAN.md. |\n")
s=s[:k]+row+s[k:]
# rotate oldest observation rows (last table rows before the 'Evidence for the older rows' line)
end=s.index('\nEvidence for the older rows')
tbl=s[k:end].split('\n')
nrot=4
old=tbl[-nrot:]; tbl=tbl[:-nrot]
s=s[:k]+'\n'.join(tbl)+s[end:]
s=s.replace("Oldest 4 observation rows rotated verbatim to SESSION_LOG.md at 2026-11-07T00:42:54Z; no historical claim rewritten.\n",
 "Oldest 4 observation rows rotated verbatim to SESSION_LOG.md at 2026-11-07T00:42:54Z; no historical claim rewritten.\n\nOldest 4 observation rows rotated verbatim to SESSION_LOG.md at "+now+"; no historical claim rewritten.\n")
# network awareness
ni=s.index('## NETWORK AWARENESS\n\n')+len('## NETWORK AWARENESS\n\n'); nj=s.index('\n\nComplete cross-runtime lifecycle', ni)
net=("REGISTRY refreshed before NETWORK at "+now+": 28 rows' Updated and Focus mirrored from owner STATUS lead headers (Status column not re-graded; WALTER row set by hand). ListAgents 01:12Z on the laptop WilliePOwen: prome-1e, red-a0, vulcan-cb, brent-aa, nexus-65, henry-b0, liquid-6a, violet-52, sam-24, all started within minutes of this boot, all busy. Desktop closed 19:37 ET November 9 (WQ-249). Other desks not listed; not listed is not DARK. Doctor at boot: no HIGH; 25 MED: 21 stale REGISTRY rows (refreshed here), 16 unconsumed items older than 2 days across 6 desks (5 ACTION, oldest ACTION 21 days: YURI, AEOLUS, HOMER, CATO, WAL, WATT), DEWEY 003R 6 days past deadline, Tier 2 debt (cleared by this closeout). ORCH_INFLIGHT read whole: IN-FLIGHT rows are open touches, not liveness. Doorbells only to VULCAN and HENRY, live ACTION owners of card 011; backlog is not a DARK finding.")
s=s[:ni]+net+s[nj:]
# filter posture: CPI pre-catalyst
s=s.replace("**Current: BALANCED baseline; the labor LOOSE window lapsed with the November 6 payroll release. Passed bank-Q3 and CPI windows do not sustain other LOOSE domains.**",
 "**Current: BALANCED baseline; inflation domain LOOSE through the October CPI print November 10 08:30 ET (pre-catalyst rule), reverting after it. The labor LOOSE window lapsed with the November 6 payroll release.**")
(W/'STATUS.md').write_text(s)
blk=f"## Rotated from STATUS {now}, BOTTOM LINE paragraphs and observation rows VERBATIM\n\n"+''.join(rot)+'\n'.join(old)+'\n\n'
sl=(W/'SESSION_LOG.md').read_text()
(W/'SESSION_LOG.md').write_text(blk+sl)
print(now, len(s.encode()))
