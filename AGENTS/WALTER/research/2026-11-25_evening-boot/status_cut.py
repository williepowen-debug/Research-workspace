import datetime,re
from pathlib import Path
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
p=Path('AGENTS/WALTER/STATUS.md'); s=p.read_text()
a=s.index('## BOTTOM LINE\n')+len('## BOTTOM LINE\n'); b=s.index('\n\n\n',a)
old=s[a:b].strip('\n')
new=('\n**November 25, full closeout (walter-4d, laptop, '+now+'):** cards 20261125-037 to -044 this session; BOARD 2,388. **IMMEDIATE: 037** DeLand official forecast 6.4 ft Sat 11/28 over the 6.33 record (NWS 20:32 ET unchanged); **042** Jazan Port HIT, minor damage (coalition spokesman, via relays), Jeddah drone intercepted, no barrel lost (FALCON graded FAL-13 CONFIRMED; BRENT: BRT-32, BG-02 NOT MET). 038 1Password breach (CYPHER); 039 CoreWeave 10-Q at the SEC: 2027 principal $10.974B, covenants met 9/30, no 8-K since 11/10; 040 co-movement hand-off (SAM, VULCAN); 041 LIQUID DTCC: no valid CoreWeave 5Y 11/25, 4Y about +130 bp; 043 NYC rent freeze upheld (titles, FLG); 044 small items. Close (vendor, provisional): S&P 7,182.78, VIX 28.29; no WALTER row fired; HY 11/25 unposted. The walter-7f window closed by accident at about 15:48 ET; its open items were recovered from the transcript (LAST_COMPLETION).\n')
p.write_text(s[:a]+new+s[b:])
s=p.read_text()
s=re.sub(r'\*\*Updated:\*\* [^\n]*','**Updated:** '+now+' — walter-4d **Tier 2 FULL closeout** on Will\'s 22:46 ET word ("lets close out for the day"); clears 2 light breadcrumbs. Duties: LAST_COMPLETION.md.',s,count=1)
row=('| November 25 close and evening (vendor and FRED; read 16:05 to 22:47 ET) | S&P 7,182.78 close (HENRY red 7,037.04 NOT FIRED), ^VIX 28.29 at the 16:15 print (VIOLET provisional; high 28.89 since 14:25), KRE 69.84, WAL 70.76, HYG 76.52, BZF27 95.18 at 22:36 ET evening trade (not a settle), ES 7,239.75 evening. FRED HY 372, CCC 1,405, VIXCLS 26.36, T5YIFR 2.13, SOFR 3.94 [11/24]; claims 189,000 [w/e 11/21]. TE 11/25: Bund 3.2209, gilt 5.136, BTP 4.3685, OAT 4.738. Cushing 25.613M [w/e 11/20]. UNKNOWN: SKEW, HY Energy, HANS-T-08, T-14. Evidence: research/2026-11-25_evening-boot/THRESHOLD-SCAN.md. |\n')
s=s.replace('|---|---|\n','|---|---|\n'+row,1)
# rotate the 11/24 night row verbatim
m=re.search(r'\n\| November 24 night \(FRED[^\n]*\|',s)
rot_row=m.group(0).strip('\n') if m else ''
if m: s=s.replace(m.group(0),'',1)
s=s.replace('Oldest 2 observation rows (November 23) rotated verbatim to SESSION_LOG.md at 2026-11-25T16:53:57Z; no historical claim rewritten.','Oldest 2 observation rows (November 23) rotated verbatim to SESSION_LOG.md at 2026-11-25T16:53:57Z; no historical claim rewritten.\n\nOldest observation row (November 24 night) rotated verbatim to SESSION_LOG.md at '+now+'; no historical claim rewritten.',1)
na=s.index('## NETWORK AWARENESS\n')+len('## NETWORK AWARENESS\n'); nb=s.index('\n## ',na)
s=s[:na]+'\nREGISTRY refreshed at this full closeout (step 13, '+now+'): Updated and Focus mirrored from owner STATUS heads for the 10 desks that committed a STATUS after 19:04Z (BRENT and NEXUS leads carry no dated line; HOMER\'s lead not parsed, row unchanged). Status colours not re-derived. Live in ListAgents at 20:06 ET: liquid-bd, homer-e8, daedalus-b6, prome-77, nexus-99, reginald-9a, henry-7d, violet-29. Absent desks are UNKNOWN, not dark. 0 cluster_mediating. HANS registry THRESHOLDS.tsv at 85% of budget (rotate tier; HANS owns it).\n'+s[nb:]
p.write_text(s)
L=Path('AGENTS/WALTER/SESSION_LOG.md'); t=L.read_text()
L.write_text('## '+now+' TIER 2 FULL CLOSEOUT — walter-4d, laptop, Wed 11/25, Will\'s word 22:46 ET (\'lets close out for the day\')\n\nClears the two light breadcrumbs (19:30:30Z walter-7f, 22:05:38Z walter-4d). This session: cards 037 to 044 (037 and 042 IMMEDIATE); boot PARTIAL at 16:04 ET; recovered the walter-7f open items after its window closed by accident. 0 kills, 0 cluster_mediating. FILTER POSTURE unchanged. Near-trigger: DeLand 6.4 forecast against 6.33; VIX 28.29 under 30. Errors and late items: LAST_COMPLETION GAPS.\n\n### STATUS text rotated verbatim at this closeout\n\nBOTTOM LINE paragraphs as they stood:\n\n'+old+'\n\nDated observation row:\n\n'+rot_row+'\n\n'+t)
print(now, len(old), bool(rot_row))
