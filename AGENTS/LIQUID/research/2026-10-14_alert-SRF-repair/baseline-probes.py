"""Offline negative controls and captured-data transition replay; no network."""
import gzip
import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'AGENTS/LIQUID/scripts'))
import test_alert_srf_repair as tests
import hy_oas_watch as current
import boot


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


old = load('liquid_before_watcher', HERE/'archive/scripts/hy_oas_watch.py')
old_boot = load('liquid_before_boot', HERE/'archive/scripts/boot.py')
negative_controls = []
for cls, name, target, module in [
        (tests.WatcherConsumerTests, 'test_ordinary_kill_actual_main_consumers_and_repeat', 'watcher', old),
        (tests.WatcherConsumerTests, 'test_mixed_lost_state_all_consumers_original_event_date', 'watcher', old),
        (tests.WatcherConsumerTests, 'test_first_published_value_distinct_from_latest_quote', 'watcher', old),
        (tests.WatcherConsumerTests, 'test_first_published_frontier_behind_latest_keeps_original_date', 'watcher', old),
        (tests.SRFTests, 'test_domestic_dashboard_calls_guard_without_network', 'boot', old_boot)]:
    stream = io.StringIO()
    with mock.patch.object(tests, target, module):
        result = unittest.TextTestRunner(stream=stream).run(unittest.TestSuite([cls(name)]))
    assert len(result.failures) == 1 and not result.errors, (name, stream.getvalue())
    negative_controls.append({'test': name, 'baseline_rejected': True,
                              'failure': result.failures[0][1].splitlines()[-1]})

source = ROOT/'AGENTS/LIQUID/research/2026-10-14_credit-funding-refresh/evidence-full.json.gz'
raw = json.load(gzip.open(source, 'rt'))
classify, hy = current._load_config()
latest = sorted(raw['latest_revised'][current.HY_ID], key=lambda r: r['date'])
fp = raw['first_published'][current.HY_ID]['rows']
first = sorted([(r['date'], float(r['value'])*hy['multiply']) for r in fp])
new_first = [(d, round(v)) for d, v in first]
prior_old = prior_new = {}
replay = []
fields = ('zone', 'sev', 'marker', 'sub260', 'obs_date', 'kill_met_on', 'count_basis', 'bps')
for r in latest:
    d = r['date']
    if not first or d < first[0][0]:
        continue
    history_old = [(dt, v) for dt, v in first if dt <= d]
    history_new = [(dt, v) for dt, v in new_first if dt <= d]
    original_event = old.first_kill_date(history_old, hy['kill_below'])
    revised_event = current.first_kill_date(history_new, hy['kill_below'])
    assert original_event == revised_event
    bps = float(r['value'])*hy['multiply']
    before = old.decide(bps, d, prior_old, hy, classify, list(reversed(history_old))[:10],
                        late_kill=original_event if original_event and original_event != d else None)
    after = current.decide(round(bps), d, prior_new, hy, classify, list(reversed(history_new))[:10],
                           late_kill=revised_event if revised_event and revised_event != d else None)
    assert all(before['state'].get(f) == after['state'].get(f) for f in fields), d
    assert len(before['fired']) == len(after['fired']), d
    replay.append({'date': d, 'bps': round(bps), 'zone': after['zone'],
                   'sub260': after['state']['sub260'], 'events': len(after['fired']), 'state_matches': True})
    prior_old, prior_new = before['state'], after['state']

out = {'negative_controls': negative_controls, 'transition_replay': replay,
       'replay_source': str(source.relative_to(ROOT)),
       'basis': 'Saved October14 latest zone observations and as-first-published returned HY window, not a fresh pull or full-history census',
       'replay_observations': len(replay), 'replay_start': replay[0]['date'], 'replay_end': replay[-1]['date'],
       'limits': 'Synthetic counterexamples were not live events; author controls are not independent review.'}
(HERE/'baseline-probes.json').write_text(json.dumps(out, indent=2)+'\n')
print(len(negative_controls), 'baseline defects rejected by actual consumer tests')
print(len(replay), 'captured published-observation transitions unchanged', replay[0]['date'], 'to', replay[-1]['date'])
