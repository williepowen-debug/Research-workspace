"""L835 integration: real disposable Git, real ARGUS entry points, no live state changes."""
import contextlib
import copy
import hashlib
import io
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_argus_contract import ContractFixture, PERIMETER, sc, ac
import argus_policy as policy
import prome_gate as gate


class Phase2Tests(ContractFixture):
    def setUp(self):
        super().setUp()
        self.set_policy(PERIMETER)

    def set_policy(self, text):
        self.write(sc.PERIMETER_FILE, text)
        self.commit(sc.PERIMETER_FILE)
        self.base = self.git('rev-parse', 'HEAD')
        sc.record_baseline(self.base)

    def custom(self, *pairs):
        self.set_policy('pattern\tclass\treason\n' + ''.join(f'{p}\t{c}\tfixture\n' for p,c in pairs)
                        + 'PROME/**\tOWNED\tdelivery\n')

    def cli(self, *args):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rc = sc.main(list(args))
        return rc, out.getvalue()

    def standard(self):
        with patch.object(gate, 'ROOT', self.root):
            gate.results.clear()
            gate.check_review_manifest('standard')
            return gate.aggregate_rc(gate.results, []), list(gate.results)

    def test_actual_ignore_nested_protection_and_attributes(self):
        for parent, hidden in [('.claude', '.claude/agents/new.md'),
                               ('AGENTS/RED', 'AGENTS/RED/inbox/new.md'),
                               ('scripts', 'scripts/docket_view.py')]:
            with self.subTest(parent=parent):
                # One fixture per control; clear previous untracked paths via explicit unlink.
                self.freeze()
                ignore = parent + '/.gitignore'
                self.write(ignore, '*\n!.gitignore\n')
                self.write(hidden, 'hidden owned/shared source')
                self.assertEqual(self.git('check-ignore', '--', hidden), hidden)
                entries = dict((p,s) for s,p in sc.porcelain_entries())
                self.assertNotIn(hidden, entries)
                self.assertIn(ignore, entries)
                self.assertEqual(sc.verify_review()[0], 1)
                with self.assertRaises(ValueError): ac.observe(sc, {ignore:self.unrelated()})
                with self.assertRaises(ValueError): self.freeze()
                (self.root / hidden).unlink(); (self.root / ignore).unlink()
        self.freeze()
        self.write('.claude/.gitattributes', '*.md -diff\n')
        self.assertEqual(sc.verify_review()[0], 1)

    def test_false_positive_supported_equivalent_standard_and_strict_ref(self):
        self.custom(('other/*/target','OWNED'), ('root/**','EXCLUDED'))
        self.freeze()
        self.assertEqual(self.standard()[0], 1)  # unchanged FROZEN is not reviewed
        self.assertEqual(sc.mark_reviewed('synthetic fixture ONLY')[0], 0)
        self.assertEqual(self.standard()[0], 0)
        self.write('root/.gitignore', '*.csv\n')
        self.write('root/hidden.csv', 'hidden excluded')
        self.assertEqual(self.git('check-ignore','root/hidden.csv'),'root/hidden.csv')
        self.assertEqual(sc.verify_review()[0], 0)
        self.assertEqual(self.standard()[0], 0)
        delivery = self.commit('PROME/result')
        self.assertEqual(sc.verify_review(ref=delivery)[0], 1)  # existing strict control-file rule at ref

    def test_controls_staged_committed_overlap_and_force_added(self):
        self.freeze()
        ignore = '.claude/.gitignore'
        self.write(ignore, '*\n!.gitignore\n')
        self.git('add','--',ignore)
        self.assertEqual(sc.verify_review()[0], 1)
        self.git('commit','-qm','RED: control file','--',ignore)
        self.assertEqual(sc.verify_review()[0], 1)
        self.write(ignore, '*.md\n')
        self.assertEqual(sc.verify_review()[0], 1)
        self.write('.claude/agents/hidden.md','force-added protected')
        self.git('add','-f','--','.claude/agents/hidden.md')
        self.git('commit','-qm','RED: forced source','--','.claude/agents/hidden.md')
        delivery = self.commit('PROME/result')
        self.assertEqual(sc.verify_review(ref=delivery, snapshot=delivery)[0], 1)
        self.plan['delivered'].update({ignore:'explicit control delivery', '.claude/agents/hidden.md':'explicit source'})
        self.freeze()
        self.assertEqual(sc.mark_reviewed('synthetic fixture')[0], 0)
        (self.root / ignore).unlink()
        # Candidate bytes remain immutable; post-freeze working changes are retained for later delivery.
        deletion = self.commit(ignore)
        self.assertEqual(sc.verify_review(ref=deletion)[0], 1)

    def test_unsupported_and_malformed_policy_rejected_at_freeze(self):
        originals = ['root/a**/target','root/**a/target','root/a**b/target','other/a**/target']
        for pat in originals:
            self.write(sc.PERIMETER_FILE, f'pattern\tclass\treason\n{pat}\tOWNED\toriginal failed example\nroot/**\tEXCLUDED\tx\n')
            with self.assertRaises(policy.EvaluationError): self.freeze()
        (self.root / sc.PERIMETER_FILE).unlink()
        with self.assertRaises(OSError): self.freeze()

    def test_policy_binding_digest_mirror_and_reuse(self):
        self.freeze(); sc.mark_reviewed('synthetic')
        old = self.manifest()
        self.assertEqual(old['schema'], 3)
        self.assertEqual(old['contract']['policy']['language'], policy.LANGUAGE)
        self.assertEqual(old['contract_sha256'], ac.digest(old['contract']))
        new = self.freeze()
        self.assertIn('PROME/result', new['contract']['reused'])
        self.save(old)
        changed = PERIMETER.replace('PROME/inbox/**\tEXCLUDED', 'PROME/inbox/**\tSHARED')
        self.write(sc.PERIMETER_FILE, changed)
        self.plan['delivered'][sc.PERIMETER_FILE] = 'authorized fixture policy change'
        new = self.freeze()
        self.assertEqual(new['contract']['reused'], {})
        for mutate in [lambda d:d['contract']['policy'].update(language='future'),
                       lambda d:d['perimeter'].update(sha256='0'*64),
                       lambda d:d['contract'].pop('policy'),
                       lambda d:d.update(perimeter=None),
                       lambda d:d['contract']['policy'].update(rules=[['**','OWNED','unsupported']])]:
            d=copy.deepcopy(old);mutate(d); self.save(d)
            self.assertEqual(sc.verify_review()[0],2)

    def test_legacy_migration_refreeze_and_rollback_evidence(self):
        self.freeze();sc.mark_reviewed('synthetic');original=self.manifest()
        for version in (None,1,2,4):
            legacy=copy.deepcopy(original)
            if version is None: legacy.pop('schema')
            else: legacy['schema']=version
            self.save(legacy)
            raw=(self.root/sc.REVIEW_FILE).read_bytes()
            self.assertEqual(sc.verify_review()[0],2)
            self.assertEqual(sc.mark_reviewed('must not promote')[0],2)
            self.assertEqual(self.standard()[0],2)
            with self.assertRaises(ValueError):ac.observe(sc,{})
            with self.assertRaises(ValueError):ac.deliver(sc,self.root/'not-read')
            with self.assertRaises(ValueError):sc._current_candidate_review(self.base)
            self.assertEqual((self.root/sc.REVIEW_FILE).read_bytes(),raw)
            migrated=self.freeze()
            self.assertEqual(migrated['verdict'],sc.FROZEN)
            self.assertEqual(migrated['contract']['reused'],{})
            self.assertEqual(self.standard()[0],1)
            self.save(legacy)  # rollback receipt bytes; no semantics converted
            self.assertEqual((self.root/sc.REVIEW_FILE).read_bytes(),raw)
        self.assertEqual(self.cli('--record-review')[0],2)

    def test_limits_and_errors_propagate_every_consumer(self):
        self.custom(('root/*','EXCLUDED'),('root/**','EXCLUDED'))
        self.write('root/.gitignore','*.csv\n')
        self.plan['observed']['root/.gitignore']=self.unrelated()
        self.freeze();sc.mark_reviewed('synthetic')
        delivery=self.commit('PROME/result')
        self.write('plan.json',json.dumps(self.plan));self.write('observe.json','{}')
        # Forced unknown even with a delivered control: analysis in validation/inventory is required.
        for failure in (policy.EvaluationError('state limit'),RuntimeError('evaluation failure')):
            with patch.object(policy.Policy,'has_protected_descendant',side_effect=failure):
                for kwargs in ({},{'ref':delivery},{'ref':delivery,'snapshot':delivery}):
                    self.assertEqual(sc.verify_review(**kwargs)[0],2)
                for args in [('--verify-review',),('--mark-reviewed','fixture'),('--observe',str(self.root/'observe.json')),
                             ('--record-review','--contract',str(self.root/'plan.json')),
                             ('--deliver-candidate','-F',str(self.root/'message'))]:
                    self.assertEqual(self.cli(*args)[0],2,args)
                self.assertEqual(self.standard()[0],2)
        # Actual limit, not only injected exception, with ordinary excluded pending control.
        with patch.object(policy,'STATE_LIMIT',1):
            self.assertEqual(sc.verify_review()[0],2)

    def test_path_inventory_roundtrip_and_delivery_refusal(self):
        self.freeze()
        for path in ('AGENTS/RED/research/é.md','AGENTS/RED/research/a\nb','AGENTS/RED/research/a\r\nb',
                     'AGENTS/RED/research/\n','AGENTS/RED/research/a\tb','AGENTS/RED/research/a\\b'):
            self.write(path,'foreign')
            self.assertIn(path,[p for _,p in sc.porcelain_entries()])
        self.assertEqual(sc.verify_review()[0],0)
        self.write('PROME/a\nb','delivery cannot safely serialize')
        self.plan['delivered']['PROME/a\nb']='fixture'
        with self.assertRaises(ValueError):self.freeze()
        if os.name=='posix':
            name=os.fsencode(self.root)+b'/bad\xff'
            with open(name,'wb') as f:f.write(b'x')
            self.assertEqual(sc.verify_review()[0],2)
            self.assertEqual(self.cli('--json')[0],2)

    def test_inventory_boundaries_are_demonstrated_not_fixed(self):
        self.freeze()
        self.write('.claude/.gitignore','*\n')
        self.write('.claude/agents/hidden.md','hidden')
        self.assertNotIn('.claude/.gitignore',[p for _,p in sc.porcelain_entries()])
        self.assertEqual(sc.verify_review()[0],0)  # LIMITATION: invisible control
        self.write('.git/info/exclude','PROME/info-hidden\n')
        self.write('PROME/info-hidden','hidden')
        self.assertNotIn('PROME/info-hidden',[p for _,p in sc.porcelain_entries()])
        self.assertEqual(sc.verify_review()[0],0)

    def test_actual_subprocess_cli_and_old_reader_schema_refusal(self):
        import shutil
        source = Path(__file__).resolve().parents[1]
        for name in ('argus_scope.py', 'argus_contract.py', 'argus_policy.py'):
            target = self.root / 'PROME/tools' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / name, target)
        self.commit(*['PROME/tools/' + n for n in ('argus_scope.py','argus_contract.py','argus_policy.py')])
        self.base=self.git('rev-parse','HEAD');sc.record_baseline(self.base)
        with __import__('tempfile').TemporaryDirectory() as td:
            plan=Path(td)/'plan.json';plan.write_text(json.dumps(self.plan))
            def run(*args):
                return subprocess.run([sys.executable,str(self.root/'PROME/tools/argus_scope.py'),*args],
                    cwd=self.root,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
            self.assertEqual(run('--record-review','--contract',str(plan)).returncode,0)
            self.assertEqual(run('--mark-reviewed','synthetic fixture').returncode,0)
            self.assertEqual(run('--verify-review').returncode,0)
            delivery=self.commit('PROME/result')
            self.assertEqual(run('--verify-review','--ref',delivery,'--snapshot',delivery).returncode,0)
            # Exact named baseline's old implementation, only inside this disposable repository.
            old=subprocess.check_output(['git','show','cf20665b2ecf9c19980e5030bc9e38293b44f25b:PROME/tools/argus_scope.py'],cwd=source)
            (self.root/'PROME/tools/argus_scope.py').write_bytes(old)
            result=run('--verify-review')
            self.assertEqual(result.returncode,2,result.stdout+result.stderr)
            self.assertIn('unsupported schema',result.stdout)

    def test_actual_historical_reviewed_receipt_is_byte_preserved(self):
        source = Path(__file__).resolve().parents[1]
        raw=subprocess.check_output(['git','show','cf20665b2ecf9c19980e5030bc9e38293b44f25b:PROME/state/argus_review.json'],cwd=source)
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'fc2ca6087fe49cc3e8d4a412f30cdef44fda855a5ff5c173a7b532653b779e65')
        self.assertEqual(json.loads(raw)['verdict'],'REVIEWED')
        target=self.root/sc.REVIEW_FILE;target.write_bytes(raw)
        for args in [('--verify-review',),('--mark-reviewed','no authorization'),('--json',)]:
            self.assertEqual(self.cli(*args)[0],2)
        self.assertEqual(self.standard()[0],2)
        self.assertEqual(target.read_bytes(),raw)
        migrated=self.freeze()
        self.assertEqual(migrated['verdict'],'FROZEN')
        self.assertEqual(migrated['contract']['reused'],{})
        target.write_bytes(raw)
        self.assertEqual(target.read_bytes(),raw)
        self.assertEqual(sc.verify_review()[0],2)

    def test_more_existing_inventory_blind_spots(self):
        self.freeze()
        with __import__('tempfile').TemporaryDirectory() as td:
            excludes=Path(td)/'global-ignore';excludes.write_text('PROME/global-hidden\n')
            self.git('config','core.excludesFile',str(excludes))
            self.write('PROME/global-hidden','hidden')
            self.assertNotIn('PROME/global-hidden',[p for _,p in sc.porcelain_entries()])
            self.assertEqual(sc.verify_review()[0],0)
            (self.root/'PROME/global-hidden').unlink()
        self.git('update-index','--assume-unchanged','PROME/old')
        self.write('PROME/old','hidden tracked change')
        self.assertNotIn('PROME/old',[p for _,p in sc.porcelain_entries()])
        self.assertEqual(sc.verify_review()[0],0)
        self.git('update-index','--no-assume-unchanged','PROME/old')
        self.assertIn('PROME/old',[p for _,p in sc.porcelain_entries()])
        self.assertEqual(sc.verify_review()[0],1)

    def test_full_disposable_schema2_to_schema3_and_rollback_drill(self):
        import tempfile
        source=Path(__file__).resolve().parents[1]
        names=('argus_scope.py','argus_contract.py','argus_policy.py')
        new={n:(source/n).read_bytes() for n in names}
        old={n:subprocess.check_output(['git','show',f'cf20665b2ecf9c19980e5030bc9e38293b44f25b:PROME/tools/{n}'],cwd=source)
             for n in names[:2]}
        def install(files):
            for n,data in files.items():
                f=self.root/'PROME/tools'/n;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(data)
        def run(*args):
            return subprocess.run([sys.executable,str(self.root/'PROME/tools/argus_scope.py'),*args],
                cwd=self.root,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        install(old)
        self.commit(*['PROME/tools/'+n for n in old])
        self.base=self.git('rev-parse','HEAD');sc.record_baseline(self.base)
        with tempfile.TemporaryDirectory() as td:
            plan=Path(td)/'plan.json';plan.write_text(json.dumps(self.plan))
            self.assertEqual(run('--record-review','--contract',str(plan)).returncode,0)
            self.assertEqual(run('--mark-reviewed','historical synthetic audit').returncode,0)
            receipt=self.root/sc.REVIEW_FILE;archived=receipt.read_bytes()
            self.assertEqual(json.loads(archived)['schema'],2)
            install(new)
            self.assertEqual(run('--verify-review').returncode,2)
            self.assertEqual(receipt.read_bytes(),archived)
            # Code changes are explicit delivery, never hidden by moving the baseline.
            migrated_plan={'delivered':{**self.plan['delivered'],**{'PROME/tools/'+n:'fixture code migration' for n in new}}}
            plan.write_text(json.dumps(migrated_plan))
            r=run('--record-review','--contract',str(plan));self.assertEqual(r.returncode,0,r.stdout+r.stderr)
            candidate=json.loads(receipt.read_text())
            self.assertEqual((candidate['schema'],candidate['verdict'],candidate['contract']['reused']),(3,'FROZEN',{}))
            # Roll back exact bytes without rewriting any branch, baseline, or approval fields.
            install(old);(self.root/'PROME/tools/argus_policy.py').unlink();receipt.write_bytes(archived)
            self.assertEqual(run('--verify-review').returncode,0)  # unchanged HISTORICAL fixture only
            self.assertEqual(receipt.read_bytes(),archived)
            install(new)
            self.assertEqual(run('--verify-review').returncode,2)

    def test_light_omission_is_not_invalid_receipt_permission(self):
        with patch.object(gate,'ROOT',self.root):
            gate.results.clear();gate.check_review_manifest('light')
            self.assertEqual(gate.aggregate_rc(gate.results,[]),0)  # no review required, none exists
            self.save({'schema':2,'verdict':'REVIEWED'})
            gate.results.clear();gate.check_review_manifest('light')
            self.assertEqual(gate.aggregate_rc(gate.results,[]),2)  # incompatible approval is never permission
