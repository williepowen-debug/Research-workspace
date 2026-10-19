"""Read-only reconstruction from committed ID sets and authored disposition records."""
import collections,csv,datetime,json,re,statistics,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT,text=True)
start='2026-10-03T16:44:07+00:00'; end='2026-10-17T16:44:07+00:00'
previous=set(); observations=[]
for line in git('log','--reverse','--format=%H %cI','--since=2026-10-02','--until='+end,'--','AGENTS/WALTER/registry/x_bookmarks_seen.json').splitlines():
 commit,stamp=line.split(' ',1)
 current=set(map(str,json.loads(git('show',commit+':AGENTS/WALTER/registry/x_bookmarks_seen.json'))['consumed']))
 if previous:
  for post in sorted(current-previous):
   created=((int(post)>>22)+1288834974657)/1000
   observations.append(dict(post_id=post,mark_commit=commit,commit_at=stamp,post_to_commit_hours=(datetime.datetime.fromisoformat(stamp).timestamp()-created)/3600))
 previous=current
rows=list(csv.DictReader((l for l in (ROOT/'AGENTS/WALTER/registry/BATCH_MANIFEST.tsv').read_text().splitlines() if not l.startswith('#')),delimiter='\t'))
cohort=[r for r in rows if '2026-10-03'<=r['opened_utc']<'2026-10-17' and 'bookmark' in r['source'].lower()]
counts=collections.Counter()
for r in cohort: counts.update(re.findall(r'(?:^|;)\d+=([^:;]+):',r['items']))
# Complete saved 40-item October16 sample. Store handles/IDs only, never post text.
sample=json.loads((ROOT/'AGENTS/WALTER/research/2026-10-16_codex-boot/bookmarks.json').read_text())
accounts=collections.Counter(x['username'] for x in sample)
lat=sorted(x['post_to_commit_hours'] for x in observations)
result=dict(window_start=start,window_end=end,seed_excluded=287,new_post_ids=len(observations),new_post_ids_per_calendar_day=len(observations)/14,manifest_batches=len(cohort),manifest_content_items=sum(int(r['declared']) for r in cohort),manifest_dispositions=dict(counts),dispatch_content_rate=counts['DISPATCH']/sum(counts.values()),screenshot_baseline=.42,latency_basis='post creation decoded from X snowflake to first commit that adds ID to consumed; upper bound for actual disposition, not time since bookmarking',median_hours=statistics.median(lat),p75_nearest_rank_hours=lat[__import__('math').ceil(.75*len(lat))-1],min_hours=min(lat),max_hours=max(lat),account_sample_items=len(sample),account_sample_distinct=len(accounts),account_sample_counts=accounts.most_common(),account_census='INCOMPLETE: sample only; no predeclared 15-account list to test',observations=observations)
print(json.dumps(result,indent=2))
