"""argus-path-v1: one segment automaton for classification and exact subtree queries.

No filesystem access, regex glob translation, guessed witness names, or legacy fallback.
A query returns bool only on a proof; EvaluationError means CANNOT-EVALUATE (CLI rc 2).
"""
from dataclasses import dataclass
from functools import lru_cache
import re

LANGUAGE = 'argus-path-v1'
STATE_LIMIT = 100_000
CLASSES = ('OWNED', 'SHARED', 'EXCLUDED')
RESERVED = frozenset(('.', '..', '.git'))
LITERAL = re.compile(r'[A-Za-z0-9_.-]+', re.ASCII)


class EvaluationError(ValueError):
    pass


def segments(path, *, directory=False):
    if directory and path == '':
        return ()
    if not isinstance(path, str):
        raise EvaluationError('path must be a string')
    parts = tuple(path.split('/'))
    if any(not p or p in RESERVED or '\0' in p or
           any(0xD800 <= ord(c) <= 0xDFFF for c in p) for p in parts):
        raise EvaluationError(f'invalid repository-relative path: {path!r}')
    return parts


def parse_tsv(raw):
    """Parse the same bytes that are hashed by freeze. No malformed row is skipped."""
    try:
        text = raw.decode('utf-8')
    except (AttributeError, UnicodeError) as exc:
        raise EvaluationError('policy is not UTF-8 bytes') from exc
    rows, header = [], False
    for number, line in enumerate(text.split('\n'), 1):
        line = line.removesuffix('\r')
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        cells = line.split('\t')
        if not header:
            if cells != ['pattern', 'class', 'reason']:
                raise EvaluationError(f'policy line {number}: expected pattern/class/reason header')
            header = True
            continue
        if len(cells) != 3:
            raise EvaluationError(f'policy line {number}: expected exactly three cells')
        rows.append(tuple(cells))
    return compile_policy(rows)


def compile_policy(rows):
    if isinstance(rows, Policy):
        return rows
    if not isinstance(rows, (list, tuple)) or not rows:
        raise EvaluationError('policy requires nonempty ordered rows')
    for i, row in enumerate(rows, 1):
        if (not isinstance(row, (list, tuple)) or len(row) != 3 or
                not all(isinstance(x, str) for x in row)):
            raise EvaluationError(f'policy row {i}: expected three strings')
    return _compile(tuple(tuple(row) for row in rows))


@lru_cache(maxsize=128)
def _compile(rows):
    predicates, rules = [], []
    for i, (pattern, cls, reason) in enumerate(rows, 1):
        try:
            if cls not in CLASSES or not reason.strip():
                raise EvaluationError('invalid class or empty reason')
            parts = segments(pattern)
            recursive = parts[-1] == '**'
            if recursive:
                parts = parts[:-1]
            if not parts:
                raise EvaluationError('recursive tail needs a nonempty prefix')
            tokens = []
            for j, part in enumerate(parts):
                if part == '*':
                    pred = ('any', '')
                elif part.startswith('*.') and j == len(parts)-1 and not recursive:
                    suffix = part[2:]
                    if not suffix or not LITERAL.fullmatch(suffix):
                        raise EvaluationError('invalid suffix')
                    pred = ('suffix', '.' + suffix)
                elif LITERAL.fullmatch(part) and part not in RESERVED:
                    pred = ('literal', part)
                else:
                    raise EvaluationError('unsupported segment expression')
                if pred not in predicates:
                    predicates.append(pred)
                tokens.append(predicates.index(pred))
            rules.append((tuple(tokens), recursive, cls, reason))
        except EvaluationError as exc:
            raise EvaluationError(f'policy row {i}, pattern {pattern!r}: {exc}') from exc
    return Policy(rows, tuple(predicates), tuple(rules))


@dataclass(frozen=True)
class Policy:
    rows: tuple
    predicates: tuple
    rules: tuple

    def mask(self, segment):
        return sum(1 << i for i, (kind, value) in enumerate(self.predicates)
                   if kind == 'any' or (segment == value if kind == 'literal'
                                        else segment.endswith(value)))

    def step(self, state, mask):
        out = []
        for pos, (tokens, recursive, _, _) in zip(state, self.rules):
            if pos < 0:
                out.append(-1)
            elif pos < len(tokens):
                out.append(pos + 1 if mask & (1 << tokens[pos]) else -1)
            else:
                out.append(len(tokens) + 1 if recursive else -1)
        return tuple(out)

    def result(self, state):
        for pos, (tokens, recursive, cls, reason) in zip(state, self.rules):
            if pos == len(tokens) + int(recursive):
                return cls, reason
        return 'UNATTRIBUTED', 'matches no declared perimeter rule'

    def feed(self, parts):
        state = (0,) * len(self.rules)
        for part in parts:
            state = self.step(state, self.mask(part))
        return state

    def classify(self, path):
        return self.result(self.feed(segments(path)))

    def atoms(self):
        """Exact predicate truth vectors, via reversed-string trie.

        Every valid segment either ends at a trie node or first leaves the trie.
        On first exit, no literal/reserved word can match and no further suffix
        terminal can be reached. Arbitrarily many remaining characters do not
        change that truth vector. A fresh next character always exists (finite
        ASCII edges, with valid non-ASCII characters available). No representative is tested.
        """
        trie = {}
        for kind, value in self.predicates:
            if kind != 'any':
                node = trie
                for c in reversed(value):
                    node = node.setdefault(c, {})
        for word in RESERVED:
            node = trie
            for c in reversed(word):
                node = node.setdefault(c, {})
        any_mask = sum(1 << i for i, (k, _) in enumerate(self.predicates) if k == 'any')
        suffix_masks = {}
        for i, (kind, value) in enumerate(self.predicates):
            if kind == 'suffix':
                suffix_masks[value] = suffix_masks.get(value, 0) | (1 << i)
        atoms, stack = set(), [(trie, '', any_mask)]
        while stack:
            node, word, inherited = stack.pop()
            mask = inherited | suffix_masks.get(word, 0)
            atoms.add(mask)  # first exit; cannot end at any reserved word
            if word and word not in RESERVED:
                atoms.add(self.mask(word))  # exact end
            stack.extend((child, c + word, mask) for c, child in node.items())
        return tuple(sorted(atoms))

    def has_protected_descendant(self, directory, *, state_limit=None):
        parts = segments(directory, directory=True)
        limit = STATE_LIMIT if state_limit is None else state_limit
        if not isinstance(limit, int) or limit < 1:
            raise EvaluationError('invalid descendant state limit')
        # After max fixed depth + 1, only dead and recursive-loop states remain.
        stop = max(len(parts) + 1, max(len(r[0]) for r in self.rules) + 1)
        frontier, count = {self.feed(parts)}, 0
        atoms = self.atoms()
        for _depth in range(len(parts) + 1, stop + 1):
            following = set()
            for state in frontier:
                for atom in atoms:
                    nxt = self.step(state, atom)
                    if nxt in following:
                        continue
                    count += 1
                    if count > limit:
                        raise EvaluationError(f'descendant analysis exceeded {limit} states')
                    if self.result(nxt)[0] != 'EXCLUDED':
                        return True
                    following.add(nxt)
            frontier = following
        return False
