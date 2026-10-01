"""CATO author tests: adversarial fixtures plus the saved pinned witnesses.
Run: python3 -B -m unittest discover -s <this directory> -p test_census_v4.py -v
Set CATO_CENSUS_OUTPUT to the completed run for the pinned-output checks.
"""
import csv
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import census_v4 as c


class ExtractionTests(unittest.TestCase):
    def row(self, confidence='70%', status='FALSIFIED', claim='Claim A', extra=''):
        return c.ledger('ID\tPrediction\tConfidence\tStatus\tNotes\n'
                        f'X-1\t{claim}\t{confidence}\t{status}\t{extra}\n')[0]

    def test_probability_missing_tier_and_instruction_are_not_live(self):
        for s in ('UNKNOWN', 'HIGH', '', 'SCORE AT 75%', 'was 50%', '101%', '-5%'):
            self.assertIsNone(c.probability(s), s)
        for s, expected in [('0%',0), ('100%',1), ('65pct',.65), ('52.5% [date]',.525)]:
            self.assertEqual(c.probability(s), expected)

    def test_shape_error_does_not_read_shifted_date_as_outcome(self):
        r = c.ledger('ID\tPrediction\tConfidence\tStatus\nX-1\tclaim\t2026-05-31\n')[0]
        self.assertEqual(c.category(r, {'pending':False, 'eligibility':'UNKNOWN'}, None), ('schema_error',None))

    def test_negative_grade_retained_but_excluded(self):
        self.assertEqual(c.category(self.row(), {'pending':False,'eligibility':'EXCLUDED'}, .7),
                         ('explicitly_ineligible',0))

    def test_pending_is_not_terminal_even_with_prior_binary_grade(self):
        self.assertEqual(c.category(self.row(), {'pending':True,'eligibility':'EXCLUDED'}, .7),
                         ('pending_verification',None))
        self.assertEqual(c.category(self.row(status='NEEDS_VERIFY'), {'pending':False,'eligibility':'UNKNOWN'}, .7),
                         ('pending_verification',None))

    def test_no_annotation_does_not_infer_grade_or_eligibility(self):
        result = c.apply_annotations(self.row(), 'text', [])
        self.assertIsNone(result['p_recorded_grade'])
        self.assertEqual(result['eligibility'],'UNKNOWN')

    def test_annotation_is_source_bound_and_validated(self):
        row = self.row(extra='Score at 75%.')
        a = dict(source_sha256=c.digest('text'), field='Notes', quote='Score at 75%', p_recorded_grade=.75)
        self.assertEqual(c.apply_annotations(row,'text',[a])['p_recorded_grade'], .75)
        with self.assertRaises(ValueError): c.apply_annotations(row,'different',[a])
        with self.assertRaises(ValueError): c.apply_annotations(self.row(),'text',[a])
        with self.assertRaises(ValueError): c.apply_annotations(row,'text',[dict(a,p_recorded_grade=1.1)])
        with self.assertRaises(ValueError): c.apply_annotations(row,'text',[a,dict(a,p_recorded_grade=.6)])

    def test_full_long_notes_are_retained(self):
        notes = 'x'*500+' no calibration credit'
        self.assertEqual(c.cell(self.row(extra=notes),'Notes'),notes)

    def test_brier_and_same_cohort_baseline(self):
        s=c.stats([(.8,1),(.7,0)])
        self.assertAlmostEqual(s['brier'], .265)
        self.assertEqual(s['in_sample_baseline'], .25)
        self.assertEqual(c.stats([(.7,1)])['skill_descriptive'],'UNKNOWN')
        self.assertEqual(c.stats([])['brier'],'UNKNOWN')


class HistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='cato-census-test-')
        self.repo=Path(self.temp.name)
        self.git('init','-q')
        self.git('config','user.name','CATO test')
        self.git('config','user.email','cato-test@example.invalid')
        self.old='AGENTS/ALPHA/workbook/PREDICTIONS.tsv'
        self.archive='AGENTS/ALPHA/thesis/archive/PREDICTIONS_resolved.tsv'
        self.header='ID\tPrediction\tConfidence\tStatus\n'

    def tearDown(self): self.temp.cleanup()
    def git(self,*args): return c.git(self.repo,*args).strip()
    def write(self,path,body):
        f=self.repo/path; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(self.header+body)
    def commit(self,message):
        self.git('add','--all')  # Isolated synthetic repo only.
        self.git('commit','-qm',message)
        return self.git('rev-parse','HEAD')
    def scan(self):
        objects=c.Objects(self.repo)
        try: return c.histories(self.repo,'HEAD',{('ALPHA','X-1')},objects)[0][('ALPHA','X-1')]
        finally: objects.close()

    def test_deleted_predecessor_beats_archive_and_wrong_desk(self):
        self.write('AGENTS/BETA/workbook/PREDICTIONS.tsv','X-1\tDifferent desk\t99%\tOPEN\n')
        self.commit('other desk')
        self.write(self.old,'')
        self.commit('empty ledger')
        self.write(self.old,'X-1\tClaim A\t60%\tOPEN\n')
        first=self.commit('register')
        self.git('mv',self.old,'AGENTS/ALPHA/workbook/PREDICTIONS_old.tsv')
        self.write(self.archive,'X-1\tClaim A\t20%\tFALSIFIED\n')
        self.commit('rotate')
        candidates=self.scan()
        row=c.ledger(self.header+'X-1\tClaim A\t20%\tFALSIFIED\n')[0]
        found,flags=c.earliest(candidates,row,self.repo)
        self.assertEqual((found['commit'],found['path'],found['p']),(first,self.old,.6))
        self.assertFalse(found['at_file_birth'])
        self.assertNotIn('claim_changed_or_missing',flags)
        self.assertTrue(all('BETA' not in x['path'] for x in candidates))

    def test_first_missing_probability_is_not_replaced_by_later_mark(self):
        self.write(self.old,'X-1\tClaim A\tHIGH\tOPEN\n'); first=self.commit('tier')
        self.write(self.old,'X-1\tClaim A\t80%\tOPEN\n'); self.commit('numeric later')
        found=self.scan()[0]
        self.assertEqual(found['commit'],first)
        self.assertIsNone(found['p'])
        self.assertTrue(found['at_file_birth'])

    def test_same_commit_disagreement_and_changed_claim_are_flagged(self):
        self.write(self.old,'X-1\tClaim A\t60%\tOPEN\n')
        self.write(self.archive,'X-1\tClaim B\t80%\tOPEN\n')
        self.commit('conflicting copies')
        current=c.ledger(self.header+'X-1\tClaim C\t80%\tOPEN\n')[0]
        found,flags=c.earliest(self.scan(),current,self.repo)
        self.assertIn('same_commit_conflicting_sources',flags)
        self.assertIn('claim_changed_or_missing',flags)

    def test_workspace_changes_do_not_change_history(self):
        self.write(self.old,'X-1\tClaim A\t60%\tOPEN\n'); self.commit('register')
        self.write(self.old,'X-1\tOther claim\t99%\tCONFIRMED\n')
        self.assertEqual(self.scan()[0]['p'],.6)

    def test_malformed_first_row_retains_candidate_but_flags_uncertainty(self):
        self.write(self.old,'X-1\tClaim A\t60%\n'); self.commit('short row')
        row=c.ledger(self.header+'X-1\tClaim A\t20%\tFALSIFIED\n')[0]
        found,flags=c.earliest(self.scan(),row,self.repo)
        self.assertEqual(found['p'],.6)
        self.assertIn('first_row_schema_error',flags)

    def test_duplicate_id_in_one_history_file_is_not_silently_selected(self):
        self.write(self.old,'X-1\tClaim A\t60%\tOPEN\nX-1\tClaim A\t80%\tOPEN\n')
        self.commit('duplicate ID')
        row=c.ledger(self.header+'X-1\tClaim A\t80%\tOPEN\n')[0]
        found,flags=c.earliest(self.scan(),row,self.repo)
        self.assertIn('duplicate_id_in_first_source',flags)

    def test_unchanged_claim_with_changed_horizon_or_resolver_is_flagged(self):
        self.header='ID\tPrediction\tConfidence\tStatus\tResolve_By\tInvalidation\n'
        self.write(self.old,'X-1\tClaim A\t60%\tOPEN\t2026-06-30\tBelow 10\n')
        self.commit('original window')
        row=c.ledger(self.header+'X-1\tClaim A\t80%\tFALSIFIED\t2026-08-31\tBelow 5\n')[0]
        found,flags=c.earliest(self.scan(),row,self.repo)
        self.assertIn('window_text_changed_or_missing',flags)
        self.assertIn('resolution_terms_changed_or_missing',flags)


@unittest.skipUnless(os.environ.get('CATO_CENSUS_OUTPUT'), 'Set CATO_CENSUS_OUTPUT for pinned-output checks')
class PinnedWitnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path(os.environ['CATO_CENSUS_OUTPUT'])
        cls.rows={(r['desk'],r['pred_id']):r for r in csv.DictReader(io.StringIO((root/'rows_v4.tsv').read_text()),delimiter='\t')}
        cls.sources={(r['desk'],r['pred_id']):r for r in map(json.loads,(root/'sources_v4.jsonl').read_text().splitlines())}
        cls.meta=json.loads((root/'provenance_v4.json').read_text())

    def test_population_reconciles(self):
        self.assertEqual(len(self.rows),534)
        self.assertEqual(sum(self.meta['dispositions'].values()),534)
        self.assertEqual(self.meta['pin'],c.PIN)

    def test_otto_grades_and_eligibility(self):
        for pid,p,b in [('OTTO-29',.75,.5625),('OTTO-32',.85,.0225)]:
            r=self.rows['OTTO',pid]
            self.assertAlmostEqual(float(r['p_recorded_grade']),p)
            self.assertAlmostEqual(float(r['brier_recorded']),b)
        self.assertEqual(self.rows['OTTO','OTTO-06']['disposition'],'explicitly_ineligible')
        self.assertEqual(self.rows['OTTO','OTTO-06']['brier_recorded'],'UNKNOWN')
        self.assertEqual(self.rows['OTTO','OTTO-10']['disposition'],'pending_verification')
        self.assertEqual(self.rows['OTTO','OTTO-04']['disposition'],'explicitly_ineligible')

    def test_saved_history_and_rotation_witnesses(self):
        for pid,p in [('OTTO-05',.60),('OTTO-29',.75),('OTTO-30',.60)]:
            r=self.rows['OTTO',pid]
            self.assertEqual(float(r['p_earliest_observed']),p)
            self.assertIn('/workbook/',r['first_path'])
        vulcan=self.rows['VULCAN','VULCAN-01']
        self.assertLessEqual(vulcan['first_commit_time'][:10],'2026-07-10')
        bond=self.sources['BOND','BND-01']['history_candidates'][0]
        self.assertEqual(bond['at_file_birth'],bond['commit']==bond['file_birth_commit'])
        self.assertIn('/workbook/',bond['path'])
        for pid in ('BND-01','BND-18','BND-29'):
            self.assertEqual(self.rows['BOND',pid]['disposition'],'binary_numeric_current')

    def test_schema_header_exclusion_and_instruction_cell(self):
        for pid in ('TOUR-02','TOUR-04'):
            self.assertEqual(self.rows['MARCO/TOURISM',pid]['disposition'],'schema_error')
        self.assertEqual(self.rows['BRENT','BRT-06']['disposition'],'explicitly_ineligible')
        self.assertEqual(self.rows['CARL','CRL-03']['p_current'],'UNKNOWN')
        self.assertEqual(self.rows['CARL','CRL-03']['p_recorded_grade'],'0.9')


if __name__=='__main__': unittest.main()
