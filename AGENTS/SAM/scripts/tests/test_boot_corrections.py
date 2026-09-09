"""Regression coverage for SAM's observed startup failure modes."""
import contextlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from types import SimpleNamespace
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

SAM = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SAM/'scripts'))
from lib import boot_context as context


def module(name):
    spec = importlib.util.spec_from_file_location('review_'+name, SAM/'scripts'/f'{name}.py')
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


thresholds, cftc, boot = (module(n) for n in ('thresholds','cftc_jpy','boot'))
NOW = datetime.fromisoformat('2026-09-09T20:58:00+00:00')


class MonitorTests(unittest.TestCase):
    def quote(self, price=153.56):
        return thresholds.quote_from_info({'regularMarketPrice':price, 'regularMarketTime':NOW.timestamp(), 'previousClose':154},NOW)

    def test_crossing_is_observation_without_trade_instructions(self):
        quotes={s:self.quote() for s in ['USDJPY=X',*thresholds.CONTEXT_TICKERS]}
        with patch.object(thresholds,'get_prices',return_value=quotes), contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(thresholds.main(),0)
        rendered=out.getvalue()
        self.assertIn('mechanism unconfirmed',rendered)
        self.assertIn('2026-09-09T20:58:00+00:00',rendered)
        self.assertNotIn('THESIS CONFIRMING',rendered)
        self.assertNotIn('consider partial profits',rendered)
        self.assertNotIn('Phase 2 carry unwind onset',rendered)
        alerts=thresholds.check_thresholds({'USDJPY=X':self.quote(146)})
        self.assertTrue(any(a['level']==147 and a['status']=='BREACHED' for a in alerts))
        self.assertEqual({a[0] for a in thresholds.THRESHOLDS},{'USDJPY=X'})

    def test_previous_close_and_undated_quote_cannot_cross(self):
        for info in [{'previousClose':140,'regularMarketTime':NOW.timestamp()}, {'regularMarketPrice':140}]:
            q=thresholds.quote_from_info(info,NOW)
            self.assertIsNone(q['as_of'])
            self.assertFalse(q['eligible'])
            self.assertEqual(thresholds.check_thresholds({'USDJPY=X':q}),[])
        self.assertIsNone(thresholds.quote_from_info({'regularMarketPrice':140,'regularMarketTime':NOW.timestamp()+100},NOW)['price'])

    def test_retrieval_clock_follows_each_download(self):
        events=[]
        class Ticker:
            @property
            def info(self):
                events.append('download')
                return {'regularMarketPrice':153.56,'regularMarketTime':NOW.timestamp()}
        provider=SimpleNamespace(Tickers=lambda symbols: SimpleNamespace(tickers={'USDJPY=X':Ticker()}))
        with patch.dict(sys.modules,{'yfinance':provider}), patch.object(thresholds,'datetime') as clock:
            clock.now.side_effect=lambda zone: events.append('retrieval') or NOW
            clock.fromtimestamp.side_effect=datetime.fromtimestamp
            quotes=thresholds.get_prices(['USDJPY=X'])
        self.assertEqual(events,['download','retrieval'])
        self.assertTrue(quotes['USDJPY=X']['eligible'])

    def test_partial_coverage_is_visible_and_nonzero(self):
        with patch.object(thresholds,'get_prices',return_value={'USDJPY=X':self.quote()}), contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(thresholds.main(),1)
        self.assertIn('UNAVAILABLE FXY',out.getvalue())
        self.assertIn('incomplete quote coverage',out.getvalue())

    def test_boundary_strictness_and_all_classes_render(self):
        self.assertFalse(any(a['status']=='BREACHED' for a in thresholds.check_thresholds({'USDJPY=X':self.quote(155)}) if a['level']==155))
        with patch.object(thresholds,'THRESHOLDS',[('USDJPY=X','below',155,'stress','fixture stress watch')]), patch.object(thresholds,'CONTEXT_TICKERS',[]), patch.object(thresholds,'get_prices',return_value={'USDJPY=X':self.quote()}), contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(thresholds.main(),0)
        self.assertIn('fixture stress watch',out.getvalue())

    def test_jgb_labels_and_comparators(self):
        jgb=module('jgb_yields')
        self.assertEqual(jgb.THRESHOLDS['30Y'][0],4.0)
        self.assertIn('Conditional demand-floor',jgb.THRESHOLDS['30Y'][1])
        self.assertIn('no mechanism grade',jgb.THRESHOLDS['40Y'][1])
        breaches=jgb.check_thresholds({'10Y':2.4,'30Y':4.0,'40Y':4.0})
        self.assertEqual({r[0] for r in breaches},{'10Y','30Y','40Y'})


class CftcTests(unittest.TestCase):
    def test_reference_and_net_long(self):
        self.assertIn('49.0%',cftc.reference_description(-92227))
        self.assertIn('NET LONG',cftc.reference_description(100))
        self.assertEqual(cftc.JUL_2024_PEAK_NET,-180000)

    def test_cover_boundary_and_invalid_denominator(self):
        for current,change,expect in [(905,-95,9.5),(900,-100,10),(899,-101,10.1)]:
            self.assertAlmostEqual(cftc.short_cover_pct(current,change),expect)
            self.assertEqual(cftc.short_cover_pct(current,change)>10,expect>10)
        for current,change in [(0,0),(5,5),(-1,-100)]:
            with self.assertRaises(ValueError):cftc.short_cover_pct(current,change)

    def test_legacy_append_and_idempotency(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'positions.tsv'
            with patch.object(cftc,'CFTC_TSV',path):
                row=dict(date='2026-09-01',oi=411882,nc_long=100000,nc_short=192227,nc_net=-92227)
                self.assertTrue(cftc.append_tsv(row))
                before=path.read_bytes()
                self.assertIn(b'51.2',before)
                self.assertFalse(cftc.append_tsv(row))
                self.assertEqual(before,path.read_bytes())
                row['date']='2026-09-08';self.assertTrue(cftc.append_tsv(row))
                self.assertTrue(path.read_bytes().startswith(before))

    def test_main_cover_alert_uses_same_prior_denominator_as_display(self):
        for current,change,alert in [(905,-95,False),(900,-100,False),(899,-101,True)]:
            row=dict(date='2026-09-01',oi=10000,nc_long=500,nc_short=current,nc_net=500-current,
                     nc_spread=0,change_nc_long=0,change_nc_short=change,change_nc_net=-change)
            with patch.object(cftc,'fetch_cftc_text',return_value='fixture'), \
                 patch.object(cftc,'find_jpy_row',return_value=['fixture']), \
                 patch.object(cftc,'parse_jpy_fields',return_value=row), \
                 patch.object(cftc,'append_tsv',return_value=False), \
                 contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(cftc.main(),0)
            self.assertEqual('SHORT COVER:' in out.getvalue(),alert)
            self.assertIn(f'{-change/1000*100:.1f}%',out.getvalue())


class BootTests(unittest.TestCase):
    def result(self,success=False):
        return dict(label='fixture',script='fixture.py',exit_code=0 if success else 1,
                    stdout='ordinary diagnostic',stderr='a'*700+' END STDERR',success=success,
                    elapsed=0.,reason='' if success else 'Child exited 1')

    def test_failure_cannot_print_clean(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            boot.display_result(self.result())
        self.assertIn('FAIL',out.getvalue());self.assertNotIn('ran cleanly',out.getvalue())

    def test_raw_streams_preserved_including_success_stderr(self):
        child=subprocess.CompletedProcess([],0,'plain stdout','a'*700+' stderr tail')
        with patch.object(boot.subprocess,'run',return_value=child):
            r=boot.run_script('fixture',SAM/'scripts/boot.py',[])
        self.assertTrue(r['success']);self.assertEqual(r['stderr'],child.stderr)

    def test_timeout_and_missing_script(self):
        with patch.object(boot.subprocess,'run',side_effect=subprocess.TimeoutExpired([],1,output=b'partial',stderr=b'diagnostic')):
            r=boot.run_script('fixture',SAM/'scripts/boot.py',[],timeout=1)
        self.assertFalse(r['success']);self.assertEqual(r['stdout'],'partial');self.assertEqual(r['stderr'],'diagnostic')
        r=boot.run_script('fixture',SAM/'scripts/absent-fixture.py',[])
        self.assertIn('Missing script',r['reason'])

    def test_inventory_drift_fails_normal_boot_and_log_preserves_stderr(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(boot,'BOOT_SEQUENCE',[('fixture','fixture.py',[],'FIXTURE',False)]), patch.object(boot,'run_script',return_value=self.result(True)), patch.object(boot,'print_tool_inventory',return_value=(['orphan.py'],[])), contextlib.redirect_stdout(io.StringIO()):
            path=Path(tmp)/'boot.jsonl'
            self.assertEqual(boot.main(['--report',str(path)]),1)
            rows=[json.loads(l) for l in path.read_text().splitlines()]
            self.assertEqual(rows[1]['stderr'],self.result(True)['stderr'])
            self.assertEqual(rows[-1]['exit_code'],1)

    def test_partial_options_snapshot_does_not_skip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'options.tsv';today=datetime.now().strftime('%Y-%m-%d')
            path.write_text('Date\tExpiry\n'+today+'\t2099-01-01\n')
            self.assertFalse(boot._has_today_row(path))
            with path.open('a') as f:
                for month in [2,3,4]:f.write(f'{today}\t2099-{month:02}-01\n')
            self.assertTrue(boot._has_today_row(path))


class ContextTests(unittest.TestCase):
    def fixture(self,tmp):
        root=Path(tmp)
        for name in ['thesis/THESIS.md','STATUS.md','MEMORY.md','docket/CALENDAR.md','thesis/timeline/TIMELINE.md','thesis/PREDICTIONS.tsv','docket/PREDICTION_SCHEDULE.json']:
            target=root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(SAM/name,target)
        return root

    def test_open_set_and_due_boundaries_without_grading(self):
        report,issues=context.prediction_report(SAM,NOW)
        self.assertFalse(issues)
        self.assertIn('3 OPEN',report)
        for ident in ['SAM-28','SAM-31','SAM-33']:self.assertIn(ident+' — OPEN',report)
        self.assertIn('9 calendar days remaining',report)
        for day,expect in [('2026-09-18','review due today'),('2026-09-19','review overdue by 1')]:
            text,issues=context.prediction_report(SAM,datetime.fromisoformat(day+'T12:00:00-04:00'))
            self.assertIn(expect,text)
            self.assertIn('no activation, resolution or grade',text)

    def test_missing_schedule_and_changed_condition_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(tmp);p=root/'docket/PREDICTION_SCHEDULE.json';data=json.loads(p.read_text())
            data['predictions'].pop('SAM-28');data['predictions']['SAM-31']['condition_sha256']='bad';p.write_text(json.dumps(data))
            report,issues=context.prediction_report(root,NOW)
            self.assertEqual(len(issues),2)
            self.assertIn('missing schedule for SAM-28',report)
            self.assertIn('changed conditions for SAM-31',report)

    def test_unknown_status_and_malformed_row_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(tmp);p=root/'thesis/PREDICTIONS.tsv';old=p.read_text()
            for bad in [old.replace('\tOPEN\t','\tMAYBE\t',1),old+'\nSAM-999\tshort row\n']:
                p.write_text(bad)
                with self.assertRaises(context.ContextError):context.predictions(root)

    def test_malformed_schedule_is_visible_without_losing_open_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(tmp);p=root/'docket/PREDICTION_SCHEDULE.json'
            for invalid in ['[]','null','{broken']:
                p.write_text(invalid)
                report,issues=context.prediction_report(root,NOW)
                self.assertTrue(issues)
                self.assertIn('3 OPEN',report)
                self.assertIn('SCHEDULING GAP',report)

    def test_orientation_all_content_chunk_bounds_no_mutation_or_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(tmp);before={p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()}
            with patch('socket.socket',side_effect=AssertionError('network forbidden')), patch.object(boot,'run_script',side_effect=AssertionError('child forbidden')):
                parts,issues,schedule_hash=context.orientation(root,NOW)
                joined=''.join(p['content'] for p in parts)
                with patch.object(boot,'SAM_DIR',root),contextlib.redirect_stdout(io.StringIO()) as out:
                    self.assertEqual(boot.main(['--orient']),0)
                    self.assertIn('context NOT loaded',out.getvalue())
                    self.assertEqual(boot.main(['--orient','--part','1']),0)
            self.assertFalse(issues)
            self.assertIn('NO SUCCESSOR',joined.upper())
            self.assertIn('CURRENT UNAVAILABLE',joined)
            self.assertIn('SAM-33 — OPEN',joined)
            self.assertTrue(all(p['bytes']<=context.CHUNK_BYTES for p in parts))
            memory=''.join(p['content'] for p in parts if p['path']=='MEMORY.md')
            self.assertEqual(memory,(root/'MEMORY.md').read_text())
            self.assertEqual(before,{p.relative_to(root):p.read_bytes() for p in root.rglob('*') if p.is_file()})

    def test_missing_or_duplicate_required_heading_fails_before_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=self.fixture(tmp);p=root/'STATUS.md';old=p.read_text()
            for bad in [old.replace('## LIVE MARKET DATA','## RENAMED',1),old+'\n## LIVE MARKET DATA\nfixture\n']:
                p.write_text(bad)
                with self.assertRaises(context.ContextError):context.orientation(root,NOW)

    def test_chunking_preserves_multibyte_text_and_rejects_oversized_line(self):
        text=('円'*200+'\n')*70
        self.assertEqual(''.join(context.split_chunks(text)),text)
        with self.assertRaises(context.ContextError):context.split_chunks('円'*6000)


if __name__=='__main__':unittest.main()
