import pathlib, subprocess, types, tempfile, contextlib, io, json
REPO=pathlib.Path('/home/willi/Research-workspace'); SHA='408e87e20'
def load(rel):
 m=types.ModuleType(rel); m.__file__=str(REPO/rel)
 src=subprocess.check_output(['git','show',f'{SHA}:{rel}'],cwd=REPO,text=True)
 exec(compile(src,m.__file__,'exec'),m.__dict__); return m
R=load('scripts/read_cap_check.py')
with tempfile.TemporaryDirectory() as d:
 root=pathlib.Path(d); home=root/'AGENTS/TEST'; home.mkdir(parents=True)
 (home/'CLAUDE.md').write_text('# TEST\n## Boot\nRead `STATUS.md`.\n')
 (home/'STATUS.md').write_text('small')
 (home/'large.md').write_text('x'*40000)
 R.ROOT=d; R.READS_TSV=str(root/'READS.tsv'); R.fleet_desks=lambda:['TEST']
 def run(label,manifest):
  pathlib.Path(R.READS_TSV).write_text(manifest)
  for args in [['--agent','TEST'],['--fleet']]:
   b=io.StringIO()
   with contextlib.redirect_stdout(b): rc=R.main(['check']+args)
   print(label, args, 'rc=',rc); print(b.getvalue())
 run('MALFORMED HEADER','broken\n')
 hdr=R.HDR+'\n'; att='ATTESTATION\tTEST\tAGENTS/TEST/CLAUDE.md\tmanifest-complete\tboot\tTEST\t2026-09-12\tfixture\n'
 run('MISSING DECLARED FILE',hdr+att+'READ\tTEST\tAGENTS/TEST/deleted.md\twhole\tboot\tTEST\t2026-09-12\tfixture\n')
 run('INVALID READ MODE',hdr+att+'READ\tTEST\tAGENTS/TEST/large.md\twhloe\tboot\tTEST\t2026-09-12\tfixture\n')
 run('INVALID ATTESTATION MODE',hdr+att.replace('manifest-complete','NOT-COMPLETE')+'READ\tTEST\tAGENTS/TEST/STATUS.md\twhole\tboot\tTEST\t2026-09-12\tfixture\n')
G=load('scripts/pipeline_rc_guard.py')
for cmd in ['set +o pipefail; python3 scripts/read_cap_check.py --agent PROME | tail -2; echo "RC=$?"','python3 scripts/read_cap_check.py --agent PROME | tail -2; echo "RC=$?"; # use PIPESTATUS next time', 'python3 scripts/read_cap_check.py --agent PROME | tail -2\nrc=$?\necho "$rc"']:
 print('GUARD',repr(cmd),'hit=',G.diagnose(cmd)[0])
