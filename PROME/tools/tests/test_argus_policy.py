"""Independent bounded oracle + exact-language tests (no production helpers in oracle)."""
import itertools
import random
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import argus_policy as p


def reference(path, rows):
    """Direct segment matcher: deliberately no compiled parser/automaton imports."""
    words = path.split('/')
    for pattern, cls, _ in rows:
        tokens = pattern.split('/')
        recursive = tokens[-1] == '**'
        if recursive:
            tokens = tokens[:-1]
            if len(words) <= len(tokens):
                continue
        elif len(words) != len(tokens):
            continue
        matches = []
        for token, word in zip(tokens, words):
            if token == '*':
                matches.append(True)
            elif token.startswith('*.'):
                matches.append(word.endswith(token[1:]))
            else:
                matches.append(token == word)
        if all(matches):
            return cls
    return 'UNATTRIBUTED'


def rows(*pairs):
    return [(pat, cls, 'fixture') for pat, cls in pairs]


class PolicyTests(unittest.TestCase):
    def test_existing_perimeter_and_common_subtrees(self):
        policy = p.parse_tsv((Path(__file__).resolve().parents[2] / 'state/AUDIT_PERIMETER.tsv').read_bytes())
        self.assertEqual(policy.classify('CLAUDE.md')[0], 'SHARED')
        for d in ('.claude', 'AGENTS', 'AGENTS/BROCK', 'scripts', 'AGENTS/BROCK/inbox'):
            self.assertTrue(policy.has_protected_descendant(d), d)
        for d in ('AGENTS/BROCK/research', 'AGENTS/BROCK/inbox/processed', 'PROME/inbox'):
            self.assertFalse(policy.has_protected_descendant(d), d)

    def test_reject_entire_policy(self):
        invalid = ['**', 'a**', '**a', 'a**b', 'a/**/b', 'a?', '[ab]', '{a,b}', '!a',
                   'a\\b', 'foo*', 'a*b', '/a', 'a/', 'a//b', '.', '..', '.git',
                   'a/.git/b', 'a/../b', '*.md/**', 'a/*.md/b', '*.', 'é', 'a\nb']
        for pat in invalid:
            with self.subTest(pattern=pat), self.assertRaises(p.EvaluationError):
                p.compile_policy(rows(('root/**', 'EXCLUDED'), (pat, 'OWNED')))
        for raw in (b'', b'root/**\tEXCLUDED\tx\n', b'pattern\tclass\treason\na\tOWNED\tx\textra',
                    b'pattern\tclass\treason\na\tNOPE\tx', b'\xff'):
            with self.subTest(raw=raw), self.assertRaises(p.EvaluationError):
                p.parse_tsv(raw)
        for invalid in (None, [], [['x', 'OWNED']], [['x', 'OWNED', None]]):
            with self.assertRaises(p.EvaluationError):
                p.compile_policy(invalid)

    def test_unicode_newline_and_unusual_segments(self):
        rs = rows(('root/*.md', 'SHARED'), ('root/*', 'OWNED'), ('root/**', 'EXCLUDED'))
        policy = p.compile_policy(rs)
        for word in ('é', '漢字', 'a\nb', 'a\r\nb.md', '\n', '.md', '.x.md', 'a b', '-x', 'a\\b', '\t'):
            path = 'root/' + word
            self.assertEqual(policy.classify(path)[0], reference(path, rs))
        self.assertEqual(policy.classify('root')[0], 'UNATTRIBUTED')
        for path in ('', '/a', 'a/', 'a//b', 'a/../b', 'a/./b', '.git/x', 'a\0b', 'a\udcff'):
            with self.assertRaises(p.EvaluationError): policy.classify(path)

    def test_confirmed_salts_and_unmatched_depth(self):
        salts = ('x', 'y', 'z', 'other', '0', '1', '_')
        rs = rows(*[(f'root/{x}', 'EXCLUDED') for x in salts],
                  ('root/*', 'OWNED'), ('root/**', 'EXCLUDED'))
        self.assertTrue(p.compile_policy(rs).has_protected_descendant('root'))
        self.assertTrue(p.compile_policy(rows(('root/*', 'EXCLUDED'))).has_protected_descendant('root'))
        self.assertTrue(p.compile_policy(rows(('root/x', 'EXCLUDED'), ('root/*', 'OWNED'))).has_protected_descendant('root'))

    def test_overlap_shadowing_and_embedded_originals(self):
        for prefix in ('root', 'other'):
            for bad in ('a**', '**a', 'a**b'):
                with self.assertRaises(p.EvaluationError):
                    p.compile_policy(rows((f'{prefix}/{bad}/target', 'OWNED'), ('root/**', 'EXCLUDED')))
        positive = rows(('root/*/target', 'OWNED'), ('root/**', 'EXCLUDED'))
        self.assertTrue(p.compile_policy(positive).has_protected_descendant('root'))
        self.assertFalse(p.compile_policy(positive[::-1]).has_protected_descendant('root'))
        self.assertFalse(p.compile_policy(rows(('other/*/target', 'OWNED'), ('root/**', 'EXCLUDED'))).has_protected_descendant('root'))
        self.assertFalse(p.compile_policy(rows(('root/**', 'EXCLUDED'), ('root/**', 'OWNED'))).has_protected_descendant('root'))

    def test_partition_vectors_exhaustive_independent_domain(self):
        rs = rows(('root/*.md', 'EXCLUDED'), ('root/*.x.md', 'OWNED'), ('root/x.md', 'SHARED'),
                  ('root/.md', 'OWNED'), ('root/*', 'EXCLUDED'), ('root/**', 'EXCLUDED'))
        policy = p.compile_policy(rs)
        # Exercise all endpoints/exits around every trie string; independent predicate truth computation.
        words = {'.md', '.x.md', 'x.md', 'root', 'unseen', '.gitx', 'x.git', 'é', '\n'}
        for value in ('root', '.md', '.x.md', 'x.md', '.git', '.', '..'):
            for i in range(len(value)+1):
                words.add('Z' + value[i:]); words.add(value[i:] + 'Z')
        observed = set()
        for word in words:
            mask = 0
            for i, (kind, value) in enumerate(policy.predicates):
                yes = kind == 'any' or (word == value if kind == 'literal' else word.endswith(value))
                if yes: mask |= 1 << i
            observed.add(mask)
        self.assertEqual(set(policy.atoms()), observed)

    def test_exhaustive_small_policies_and_seeded_larger(self):
        # This alphabet covers every literal, suffix and complement truth class in this grammar subset.
        alphabet = ['a', 'b', 'z', '.md', 'x.md', '.x.md', 'x.x.md']
        choices = [('root/a', 'EXCLUDED'), ('root/*', 'OWNED'), ('root/**', 'EXCLUDED'),
                   ('root/*/*.md', 'SHARED'), ('root/*.md', 'EXCLUDED'), ('root/*.x.md', 'OWNED')]
        policies = [rows(*comb) for n in (1,2,3) for comb in itertools.product(choices, repeat=n)]
        rng = random.Random(835)
        policies += [rows(*[rng.choice(choices) for _ in range(12)]) for _ in range(50)]
        for rs in policies:
            policy = p.compile_policy(rs)
            depth = max(len(pat.split('/')) - (pat.endswith('/**')) for pat,_,_ in rs) + 2
            expected = False
            for n in range(1, depth):
                for words in itertools.product(alphabet, repeat=n):
                    path = 'root/' + '/'.join(words)
                    ref = reference(path, rs)
                    self.assertEqual(policy.classify(path)[0], ref, (rs, path))
                    expected |= ref != 'EXCLUDED'
            self.assertEqual(policy.has_protected_descendant('root'), expected, rs)

    def test_limits_are_unknown_not_true_or_false(self):
        policy = p.compile_policy(rows(('root/*', 'EXCLUDED'), ('root/**', 'EXCLUDED')))
        with self.assertRaises(p.EvaluationError): policy.has_protected_descendant('root', state_limit=1)
        self.assertFalse(policy.has_protected_descendant('root'))

    def test_differential_old_matcher_on_supported_ordinary_paths(self):
        import ast
        import re
        import subprocess
        root = Path(__file__).resolve().parents[3]
        old = subprocess.check_output(['git','show','cf20665b2ecf9c19980e5030bc9e38293b44f25b:PROME/tools/argus_scope.py'],cwd=root,text=True)
        function = next(n for n in ast.parse(old).body if isinstance(n,ast.FunctionDef) and n.name=='_match')
        namespace={'re':re}
        exec(compile(ast.Module(body=[function],type_ignores=[]),'<historical matcher test only>','exec'),namespace)
        for pattern in ('root/*','root/**','root/*.md','root/*/target','root/x','AGENTS/*/inbox/**'):
            policy=p.compile_policy(rows((pattern,'OWNED')))
            for depth in range(1,5):
                for words in itertools.product(('root','x','target','.md','x.md'),repeat=depth):
                    path='/'.join(words)
                    self.assertEqual(policy.classify(path)[0]=='OWNED',namespace['_match'](pattern,path),(pattern,path))
        # Intentional difference: old recursive regex dot did not cross newline.
        self.assertFalse(namespace['_match']('root/**','root/a\nb'))
        self.assertEqual(p.compile_policy(rows(('root/**','OWNED'))).classify('root/a\nb')[0],'OWNED')
