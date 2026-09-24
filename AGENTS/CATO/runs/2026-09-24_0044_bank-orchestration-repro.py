"""Read-only reproductions for CATO RB1/RB2/RB3, pinned to the reviewed turn.

Run from the Git root with python3 -B. No network or owner-file writes.
"""
import json
import subprocess
import sys

REVISION = "6b51442c3c1e33d42afb89045251b80b1bbb2006"
PATH = "AGENTS/OZK/scripts/flng_watch.py"
source = subprocess.check_output(["git", "show", f"{REVISION}:{PATH}"], text=True)
wrapper = """
import io,json,sys,urllib.request
case=json.loads(sys.stdin.read())
def fake_urlopen(*args,**kwargs):
    if case.get('network_error'): raise OSError('fixture network failure')
    return io.BytesIO(json.dumps(case['payload']).encode())
urllib.request.urlopen=fake_urlopen
sys.argv=['flng_watch.py']
exec(compile(case['source'],'flng_watch.py','exec'),{'__name__':'__main__'})
"""
cases = [
    ("known-baseline", [{"instFlngId": 11981}], False),
    ("new-filing", [{"instFlngId": 11982, "instFlngAtchList": [
        {"instFlngAtchId": 1, "instFlngAtchOrglNme": "fixture.pdf"}]}], False),
    ("empty-list", [], False),
    ("empty-object", {}, False),
    ("missing-id", [{}], False),
    ("network-failure", None, True),
]
results = []
for name, payload, network_error in cases:
    proc = subprocess.run([sys.executable, "-B", "-c", wrapper],
                          input=json.dumps(dict(source=source, payload=payload,
                                                network_error=network_error)),
                          text=True, capture_output=True, check=False)
    results.append(dict(case=name, rc=proc.returncode, stdout=proc.stdout.strip(),
                        stderr=proc.stderr.strip()))
assert [r["rc"] for r in results] == [0, 1, 0, 0, 1, 2]

# RB2: a logical counterexample, NOT a claim these unobserved flows occurred.
# All amounts are $K; the observed cells are copied from OZK section 6.1b.
transfer = 432181
pv06_start, pv06_end = 1161937, 1184574
pv06_other_net = pv06_end - pv06_start - transfer
assert pv06_other_net == -409544
assert 1161937 + transfer + pv06_other_net == 1184574
assert 1202101 - transfer == 769920
assert 799272 - 212636 == 586636
assert 0 + 45729 == 45729
assert 22637 - 212636 + 45729 - 432181 == -576451

print(json.dumps(dict(revision=REVISION, watcher=results,
    rb2_counterexample={"hypothetical_PV09_to_PV06": transfer,
                        "offsetting_PV06_other_net": pv06_other_net,
                        "matches_reported_endpoints": True},
    rb1_counterexamples=[
        "BKU: primary HOLDS, 90+ TRANSMITS, criticized HOLDS: no explicit per-name combiner",
        "SBCF: 30-89=13M and 60-89=2M meets neither primary row branch",
    ]), indent=2))
