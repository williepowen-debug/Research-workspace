"""Independent regression tests; synthetic fixtures and fake transports only."""
import copy
import csv
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location('review_pilot_runner', Path(__file__).with_name('runner.py'))
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


def task():
    return {
        'id': 'fixture', 'question': 'Update both surfaces.',
        'fields': [{'id': 'canonical', 'format': 'integer'}, {'id': 'summary', 'format': 'integer'}],
        'initial_documents': [{'id': 'old', 'text': 'The count is 10.'}],
        'initial_state': {}, 'update_documents': [{'id': 'new', 'text': 'The current count is 12.'}],
        'initial_key': {f: {'value': '10', 'sources': ['old']} for f in ('canonical', 'summary')},
        'final_key': {f: {'value': '12', 'sources': ['new']} for f in ('canonical', 'summary')},
        'private_annotation': 'SECRET_KEY_METADATA',
    }


def answer(value='10', source='old'):
    return {'answers': [{'field': f, 'value': value, 'source_ids': [source]} for f in ('canonical', 'summary')]}


def flag(field='canonical', value='12', sources=None):
    return {'field': field, 'problem': 'Current evidence differs.', 'proposed_value': value,
            'source_ids': ['new'] if sources is None else sources}


def usage(total=20):
    return {'totalTokens': total, 'inputTokens': total - 1, 'outputTokens': 1,
            'cachedInputTokens': 0, 'reasoningOutputTokens': 0}


def result(draft, flags, final):
    return {'stages': [{'text': json.dumps(draft)}, {'text': json.dumps({'flags': flags})},
                       {'text': json.dumps(final)}]}


class GradeTests(unittest.TestCase):
    def test_correct_answer_passes(self):
        self.assertTrue(runner.grade(answer(), task()['initial_key'])['acceptable'])

    def test_missing_duplicate_extra_or_unsupported_assertions_fail(self):
        cases = []
        a = answer(); a['answers'].pop(); cases.append(a)
        a = answer(); a['answers'][1] = copy.deepcopy(a['answers'][0]); cases.append(a)
        a = answer(); a['answers'].append({'field': 'invented', 'value': 'yes', 'source_ids': ['old']}); cases.append(a)
        a = answer(); a['commentary'] = 'Invented assertion'; cases.append(a)
        a = answer(); a['answers'][0]['commentary'] = 'Invented assertion'; cases.append(a)
        a = answer(); a['answers'][0]['value'] = '10 and another unsupported claim'; cases.append(a)
        for a in cases:
            with self.subTest(answer=a):
                self.assertFalse(runner.grade(a, task()['initial_key'])['acceptable'])

    def test_bad_citations_fail(self):
        for citations in ([], ['invented'], ['old', 'invented'], ['old', 'old'], 'old', [1], [None]):
            with self.subTest(citations=citations):
                a = answer(); a['answers'][0]['source_ids'] = citations
                self.assertFalse(runner.grade(a, task()['initial_key'])['acceptable'])

    def test_malformed_field_ids_fail_without_crashing(self):
        for field in ([], {}, ['canonical'], {'name': 'canonical'}, None, 1):
            with self.subTest(field=field):
                a = answer(); a['answers'][0]['field'] = field
                self.assertFalse(runner.grade(a, task()['initial_key'])['acceptable'])

    def test_malformed_shapes_fail_without_crashing(self):
        for a in (None, [], {}, {'answers': None}, {'answers': {}}, {'answers': [None, 1]}):
            with self.subTest(answer=a):
                self.assertFalse(runner.grade(a, task()['initial_key'])['acceptable'])


class ScoreTests(unittest.TestCase):
    def test_initial_and_final_use_distinct_evidence_keys(self):
        scored = runner.score_run(task(), result(answer(), [flag()], answer('12', 'new')))
        self.assertTrue(scored['first']['acceptable'])
        self.assertFalse(scored['draft_against_final_evidence']['acceptable'])
        self.assertTrue(scored['final']['acceptable'])
        self.assertEqual(set(scored['repaired_fields']), {'canonical', 'summary'})
        self.assertEqual(scored['introduced_errors'], [])

    def test_unrevised_draft_is_graded_against_final_key_after_stopping(self):
        scored = runner.score_run(task(), {'stages': [{'text': json.dumps(answer())}]})
        self.assertTrue(scored['first']['acceptable'])
        self.assertFalse(scored['final']['acceptable'])

    def test_changed_no_change_control_is_damage(self):
        t = task(); t['final_key'] = copy.deepcopy(t['initial_key'])
        final = answer(); final['answers'][0]['value'] = '12'
        scored = runner.score_run(t, result(answer(), [], final))
        self.assertEqual(scored['introduced_errors'], ['canonical'])
        self.assertEqual(scored['repaired_fields'], [])

    def test_unchanged_value_is_not_evidence_that_invalid_flag_was_acted_on(self):
        t = task(); t['final_key'] = copy.deepcopy(t['initial_key'])
        scored = runner.score_run(t, result(answer(), [flag(value='10', sources=['old'])], answer()))
        self.assertFalse(scored['flag_scores'][0]['valid'])
        self.assertFalse(scored['flag_scores'][0]['acted_on'])

    def test_citation_only_flag_can_be_ignored_or_repaired(self):
        draft = answer('12', 'old')
        for final, acted in ((draft, False), (answer('12', 'new'), True)):
            with self.subTest(acted=acted):
                scored = runner.score_run(task(), result(draft, [flag()], final))
                self.assertTrue(scored['flag_scores'][0]['valid'])
                self.assertEqual(scored['flag_scores'][0]['acted_on'], acted)

    def test_valid_flag_is_ignored_when_another_field_changes(self):
        final = answer(); final['answers'][1] = answer('12', 'new')['answers'][1]
        scored = runner.score_run(task(), result(answer(), [flag()], final))
        self.assertTrue(scored['flag_scores'][0]['valid'])
        self.assertFalse(scored['flag_scores'][0]['acted_on'])
        self.assertEqual(scored['repaired_fields'], ['summary'])

    def test_citation_order_does_not_change_acted_on_classification(self):
        t = task()
        t['final_key']['canonical']['sources'] = ['new', 'also-new']
        final = answer('12', 'new')
        final['answers'][0]['source_ids'] = ['also-new', 'new']
        scored = runner.score_run(t, result(answer(), [flag(sources=['new', 'also-new'])], final))
        self.assertTrue(scored['flag_scores'][0]['acted_on'])
        draft = copy.deepcopy(final)
        draft['answers'][0]['source_ids'] = ['new', 'also-new']
        scored = runner.score_run(t, result(draft, [flag(sources=['also-new', 'new'])], final))
        self.assertFalse(scored['flag_scores'][0]['acted_on'])

    def test_malformed_review_flags_are_invalid(self):
        flags = []
        f = flag(); f['extra_assertion'] = 'unsupported'; flags.append(f)
        f = flag(); f['source_ids'] = ['new', 'new']; flags.append(f)
        f = flag(); f['problem'] = ['not a string']; flags.append(f)
        f = flag(); f.pop('problem'); flags.append(f)
        for f in flags:
            with self.subTest(flag=f):
                scored = runner.score_run(task(), result(answer(), [f], answer('12', 'new')))
                self.assertFalse(scored['flag_scores'][0]['valid'])

    def test_duplicate_review_flags_are_invalid(self):
        scored = runner.score_run(task(), result(answer(), [flag(), flag()], answer('12', 'new')))
        self.assertFalse(any(f['valid'] for f in scored['flag_scores']))

    def test_removing_bad_duplicate_is_a_repair_and_action(self):
        draft = answer('12', 'new')
        draft['answers'].append({'field': 'canonical', 'value': '10', 'source_ids': ['old']})
        scored = runner.score_run(task(), result(draft, [flag()], answer('12', 'new')))
        self.assertEqual(scored['repaired_fields'], ['canonical'])
        self.assertTrue(scored['flag_scores'][0]['valid'])
        self.assertTrue(scored['flag_scores'][0]['acted_on'])

    def test_malformed_outputs_and_flag_ids_do_not_abort_scoring(self):
        for final in ({'answers': None}, {'answers': {}}, {'answers': 1}):
            with self.subTest(final=final):
                scored = runner.score_run(task(), result(answer(), [flag()], final))
                self.assertFalse(scored['final']['acceptable'])
        for field in ([], {}):
            with self.subTest(field=field):
                scored = runner.score_run(task(), result(answer(), [flag(field=field)], answer('12', 'new')))
                self.assertFalse(scored['flag_scores'][0]['valid'])


class FakeRpc:
    """Runs the real Worker.turn without opening a process or network connection."""
    def __init__(self, usage, status='completed', items=None, late_usage=False):
        self.events = []
        self.usage = usage
        self.status = status
        self.items = items if items is not None else [{'type': 'agentMessage', 'text': json.dumps(answer())}]
        self.late_usage = late_usage
        self.calls = []

    def call(self, method, params, **kwargs):
        self.calls.append((method, params))
        return {'turn': {'id': 'turn-1'}}

    def wait_event(self, method, predicate, timeout):
        event = {'method': 'thread/tokenUsage/updated', 'params': {
            'threadId': 'thread-1', 'turnId': 'turn-1', 'tokenUsage': {'last': self.usage}}}
        if method == 'turn/completed':
            if self.usage is not None and not self.late_usage:
                self.events.append(event)
            return {'threadId': 'thread-1', 'turn': {'id': 'turn-1', 'status': self.status, 'items': self.items}}
        if self.usage is not None and self.late_usage:
            self.events.append(event)
            return event['params']
        raise TimeoutError('No usage notification')


def worker_turn(rpc):
    worker = runner.Worker.__new__(runner.Worker)
    worker.settings = {'effort': 'low', 'timeout_seconds': 1}
    worker.rpc = rpc
    return worker.turn('thread-1', 'Synthetic fixture only', runner.schema(task()))


class TransportTests(unittest.TestCase):
    def test_missing_usage_fails(self):
        self.assertIn('error', worker_turn(FakeRpc(None)))

    def test_invalid_usage_fails(self):
        for usage in ({}, {'inputTokens': 1}, {'totalTokens': -1}, {'totalTokens': '20'}, {'totalTokens': True}):
            with self.subTest(usage=usage):
                self.assertIn('error', worker_turn(FakeRpc(usage)))

    def test_late_usage_is_retained_in_event_record(self):
        row = worker_turn(FakeRpc(usage(), late_usage=True))
        self.assertEqual(row['usage']['totalTokens'], 20)
        self.assertNotIn('error', row)
        self.assertTrue(any(e['method'] == 'thread/tokenUsage/updated' for e in row['events']))

    def test_valid_usage_and_output_succeed(self):
        self.assertNotIn('error', worker_turn(FakeRpc(usage())))

    def test_timeout_preserves_observed_events_and_attempts_interrupt(self):
        class TimeoutRpc(FakeRpc):
            def wait_event(self, method, predicate, timeout):
                self.events.append({'method': 'item/started', 'params': {
                    'threadId': 'thread-1', 'turnId': 'turn-1', 'item': {'type': 'reasoning', 'id': 'item-1'}}})
                raise TimeoutError('Synthetic timeout')
        rpc = TimeoutRpc(usage())
        row = worker_turn(rpc)
        self.assertIn('error', row)
        self.assertTrue(any(method == 'turn/interrupt' for method, _ in rpc.calls))
        self.assertTrue(any(event['method'] == 'item/started' for event in row.get('events', [])))

    def test_tool_attempt_in_lifecycle_event_alone_fails(self):
        for event_method in ('item/started', 'item/completed'):
            with self.subTest(event_method=event_method):
                class ToolEventRpc(FakeRpc):
                    def wait_event(self, method, predicate, timeout):
                        completed = super().wait_event(method, predicate, timeout)
                        self.events.append({'method': event_method, 'params': {
                            'threadId': 'thread-1', 'turnId': 'turn-1',
                            'item': {'type': 'commandExecution', 'id': 'tool-1'}}})
                        return completed
                row = worker_turn(ToolEventRpc(usage()))
                self.assertIn('commandExecution', row['error'])
                self.assertTrue(any(e['method'] == event_method for e in row['events']))

    def test_failed_status_and_tool_items_fail(self):
        self.assertIn('error', worker_turn(FakeRpc(usage(), status='failed')))
        self.assertIn('error', worker_turn(FakeRpc(usage(), items=[{'type': 'commandExecution'}])))

    def test_malformed_json_fails(self):
        self.assertIn('error', worker_turn(FakeRpc(usage(), items=[{'type': 'agentMessage', 'text': '{'}])))


class RunAndFreezeTests(unittest.TestCase):
    def fake_worker(self, outcomes):
        class FakeWorker:
            instances = []

            def __init__(self, settings, directory):
                self.init = {}; self.prompts = []; self.closed = False; self.thread_count = 0
                self.instances.append(self)

            def thread(self):
                self.thread_count += 1
                return {'thread': {'id': 'thread-' + str(self.thread_count)}}

            def turn(self, tid, prompt, output_schema):
                self.prompts.append((tid, prompt))
                return copy.deepcopy(outcomes[len(self.prompts) - 1])

            def close(self):
                self.closed = True
        return FakeWorker

    def run_fake(self, outcomes, limit=100, arm='self'):
        fake = self.fake_worker(outcomes)
        with tempfile.TemporaryDirectory() as directory, patch.object(runner, 'Worker', fake):
            record = runner.run_one(task(), arm, 1, {'stop_before_next_turn_tokens': limit}, Path(directory))
            self.assertTrue(fake.instances[0].closed)
            self.assertEqual(json.loads((Path(directory) / 'result.json').read_text())['status'], record['status'])
        return record, fake.instances[0]

    def test_failure_stops_before_next_call_and_is_retained(self):
        row, worker = self.run_fake([{'text': '', 'usage': None, 'error': 'Usage unavailable'}])
        self.assertEqual(row['status'], 'FAILED')
        self.assertEqual(len(worker.prompts), 1)
        self.assertIn('error', row['stages'][0])

    def test_soft_budget_exhaustion_retains_last_deliverable(self):
        row, worker = self.run_fake([{'text': json.dumps(answer()), 'usage': usage(110)}])
        self.assertEqual(row['status'], 'BUDGET_EXHAUSTED')
        self.assertEqual(len(worker.prompts), 1)
        self.assertTrue(runner.score_run(task(), row)['first']['acceptable'])

    def test_public_task_excludes_keys_updates_and_private_metadata(self):
        public = runner.public_task(task())
        self.assertEqual(set(public), {'id', 'question', 'fields', 'initial_documents', 'initial_state'})
        self.assertNotIn('SECRET_KEY_METADATA', json.dumps(public))
        self.assertNotIn('final_key', json.dumps(public))
        self.assertNotIn('update_documents', public)

    def test_separate_reviewer_gets_evidence_and_draft_but_no_keys(self):
        outputs = [{'text': json.dumps(answer()), 'usage': usage(1)},
                   {'text': json.dumps({'flags': [flag()]}), 'usage': usage(1)},
                   {'text': json.dumps(answer('12', 'new')), 'usage': usage(1)}]
        row, worker = self.run_fake(outputs, arm='separate')
        self.assertEqual(row['status'], 'COMPLETED')
        self.assertEqual([tid for tid, _ in worker.prompts], ['thread-1', 'thread-2', 'thread-1'])
        self.assertIn(json.dumps(answer()), worker.prompts[1][1])
        self.assertIn('The current count is 12.', worker.prompts[1][1])
        self.assertNotIn('The current count is 12.', worker.prompts[0][1])
        for _, prompt in worker.prompts:
            self.assertNotIn('initial_key', prompt)
            self.assertNotIn('final_key', prompt)
            self.assertNotIn('SECRET_KEY_METADATA', prompt)

    def test_freeze_rejects_modified_inputs(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(runner, 'ROOT', Path(directory)):
            frozen_input = Path(directory) / 'fixture.json'
            frozen_input.write_text('{"version": 1}\n')
            runner.write(Path(directory) / 'FREEZE.json', {'sha256': {'fixture.json': runner.digest(frozen_input)}})
            runner.verify_freeze()
            frozen_input.write_text('{"version": 2}\n')
            with self.assertRaises(SystemExit):
                runner.verify_freeze()

    def test_invalid_usage_logging_keeps_declared_two_failure_stop(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            t = task(); t['split'] = 'practice'
            runner.write(root / 'corpus.json', {'tasks': [t]})
            runner.write(root / 'settings.json', {'random_seed': 17})
            def fake_run(*args):
                return {'task_id': 'fixture', 'status': 'FAILED', 'stages': [
                    {'text': '', 'usage': {'inputTokens': 1}, 'error': 'Invalid usage'}]}
            capture = io.StringIO()
            with patch.object(runner, 'ROOT', root), patch.object(runner, 'run_one', side_effect=fake_run) as run_mock, \
                    patch.object(runner.tempfile, 'mkdtemp', return_value=str(root)), \
                    patch.object(sys, 'argv', ['runner', '--phase', 'practice', '--out', str(root / 'runs')]), \
                    redirect_stdout(capture):
                runner.main()
            self.assertEqual(run_mock.call_count, 2)
            logged = [json.loads(line) for line in capture.getvalue().splitlines() if line.startswith('{')]
            self.assertEqual(len(logged), 2)
            self.assertTrue(all(row['known_token_lower_bound'] == 0 and not row['usage_complete'] for row in logged))
            finished = json.loads((root / 'runs' / 'finished.json').read_text())
            self.assertEqual(finished['attempted'], 2)


class AnalyzeCoverageTests(unittest.TestCase):
    def test_missing_or_invalid_usage_has_unknown_total_and_null_paired_difference(self):
        spec = importlib.util.spec_from_file_location('review_pilot_analyze', Path(__file__).with_name('analyze.py'))
        analyze = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {'runner': runner}):
            spec.loader.exec_module(analyze)
        for missing_usage in (None, {'inputTokens': 1}):
            with self.subTest(usage=missing_usage), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                t = task(); t.update(family='supersession', no_change_control=False)
                runner.write(root / 'corpus.json', {'tasks': [t]})
                out = root / 'runs'; out.mkdir()
                order = [{'task': t['id'], 'rep': rep, 'condition': arm}
                         for rep in (1, 2) for arm in ('self', 'separate')]
                runner.write(out / 'order.json', order)
                runner.write(out / 'run-000.json', {'status': 'FAILED', 'stages': [
                    {'text': json.dumps(answer()), 'usage': usage()},
                    {'text': '', 'usage': missing_usage, 'error': 'Usage unavailable'}]})
                complete = result(answer(), [flag()], answer('12', 'new'))
                complete['status'] = 'COMPLETED'
                for stage in complete['stages']:
                    stage['usage'] = usage()
                runner.write(out / 'run-001.json', complete)
                with patch.object(analyze, 'ROOT', root), \
                        patch.object(sys, 'argv', ['analyze', str(out)]), redirect_stdout(io.StringIO()):
                    analyze.main()
                summary = json.loads((out / 'summary.json').read_text())
                groups = summary['groups']['all']
                self.assertIsNone(groups['self']['total_tokens'])
                self.assertEqual(groups['self']['known_token_lower_bound'], 20)
                self.assertEqual(groups['self']['scheduled'], 2)
                self.assertEqual(groups['self']['completed'], 0)
                self.assertEqual(groups['separate']['total_tokens'], 60)
                self.assertIsNone(summary['paired'][0]['separate_minus_self']['total_tokens'])
                with (out / 'outcomes.csv').open(newline='') as stream:
                    rows = list(csv.DictReader(stream))
                self.assertEqual(len(rows), 4)
                self.assertEqual(rows[0]['total_tokens'], '')
                self.assertEqual(rows[0]['known_token_lower_bound'], '20')
                self.assertEqual(rows[0]['measured_turns'], '1')
                self.assertEqual(rows[0]['usage_complete'], 'False')
                self.assertEqual(rows[2]['status'], 'NOT_RUN')
                self.assertEqual(rows[2]['final_acceptable'], 'False')


if __name__ == '__main__':
    unittest.main()
