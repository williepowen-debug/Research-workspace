#!/usr/bin/env python3
"""Prepare one explicit card and queue-pointer patch; never publish or answer.

The output directory must be new. Apply with --apply PREPARED_DIRECTORY,
then commit/publish the two named source paths together.
"""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

from options import pointer_for, source_for, terms_hash
from pilot_files import fields, strict_json
from queue_store import QUEUE, open_rows
from store import reader


def read_exact(path):
    with Path(path).open(encoding='utf-8', newline='') as stream:
        return stream.read()


def prepare(root, wq, specification, *, replace_source=False):
    root = Path(root).resolve()
    if not re.fullmatch(r'[1-9][0-9]*[a-z]?', wq):
        raise ValueError('Expected one WQ number')
    fields(specification, {'choices', 'recommended_choice_id', 'context', 'conditions'}, 'Card input')
    queue_path = root / QUEUE
    if queue_path.is_symlink() or not queue_path.resolve().is_relative_to(root):
        raise ValueError('Queue must be a regular file inside the repository')
    before = read_exact(queue_path)
    row = open_rows(before).get(wq)
    if not row or row['kind'] != 'DECISION' or row['blocked']:
        raise ValueError('Card authoring requires an open, unblocked DECISION row')
    old_pointer = pointer_for(row)
    path = old_pointer or f'PROME/proposals/wq{wq}-app-options.md'
    target = root / path
    if target.is_symlink() or not target.resolve().is_relative_to(root):
        raise ValueError('Source must stay inside the repository without a symlink')
    if target.exists() and not replace_source:
        raise ValueError('Existing source preserved; review it and use --replace-source explicitly')
    if old_pointer and not target.is_file():
        raise ValueError('Existing pointer has no source; reconcile it before authoring')
    previous_source = read_exact(target) if target.exists() else ''
    if not before.endswith('\n') or (previous_source and not previous_source.endswith('\n')):
        raise ValueError('Source files must end in a newline before preparing a patch')
    if old_pointer:
        updated = row['row']
    else:
        updated = row['row'].rstrip()
        if not updated.endswith('|'):
            raise ValueError('Queue row must have its closing table delimiter')
        updated = updated[:-1].rstrip() + f' <!-- decisions-options: {path} --> |'
    lines = before.splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.rstrip('\r\n') == row['row']]
    if len(hits) != 1:
        raise ValueError('Queue row is ambiguous; no patch generated')
    ending = '\r\n' if lines[hits[0]].endswith('\r\n') else '\n'
    lines[hits[0]] = updated + ending
    after = ''.join(lines)
    updated_row = open_rows(after)[wq]
    record = dict(schema_version='decisions-options/3', wq_id=wq,
                  queue_terms_sha256=terms_hash(updated_row), **specification,
                  confirmation={'mode': 'chat', 'scope': 'other',
                                'reason': 'Matching PROME-chat confirmation remains required under the installed fallback.'})
    source = ('# WQ-' + wq + ' — explicit decision card\n\n'
              'Question, options, context and conditions are decision terms. Queue Notes are operational; '
              'put changed conditions here or in the question, not only in Notes.\n\n'
              '```decisions-options\n' + json.dumps(record, ensure_ascii=False, indent=2) + '\n```\n')
    class Source:
        def read(self, *args, **kwargs):
            return source
    source_for(Source(), updated_row, 'candidate')  # Use the installed reader's full validation.
    patch = ''
    for name, old, new, exists in ((QUEUE, before, after, True), (path, previous_source, source, target.exists())):
        if old == new:
            if name == QUEUE:
                # A replacement still needs the exact target row as a patch precondition.
                start, end = max(0, hits[0] - 3), min(len(lines), hits[0] + 4)
                number, count = start + 1, end - start
                patch += (f'--- a/{QUEUE}\n+++ b/{QUEUE}\n'
                          f'@@ -{number},{count} +{number},{count} @@\n')
                for i in range(start, end):
                    patch += ('-' + lines[i] + '+' + lines[i]) if i == hits[0] else ' ' + lines[i]
            continue
        patch += ''.join(difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True),
                         fromfile='a/' + name if exists else '/dev/null', tofile='b/' + name))
    return {'wq': wq, 'source_path': path, 'source': source, 'patch': patch,
            'patch_sha256': hashlib.sha256(patch.encode()).hexdigest(),
            'queue_preimage_sha256': hashlib.sha256(before.encode()).hexdigest(),
            'source_preimage_sha256': hashlib.sha256(previous_source.encode()).hexdigest() if target.exists() else None,
            'queue_terms_sha256': record['queue_terms_sha256']}


def apply_prepared(root, directory):
    """Owner-controlled apply: verify both full preimages, then apply without staging.

    The owner must have exclusive write custody of queue/source during this short
    operation, as for ordinary Git application. This is not a cross-process lock.
    """
    root, directory = Path(root).resolve(), Path(directory).resolve()
    manifest = strict_json((directory / 'manifest.json').read_text())
    fields(manifest, {'wq', 'source_path', 'queue_preimage_sha256',
                     'source_preimage_sha256', 'queue_terms_sha256', 'patch_sha256'}, 'Prepared card')
    source = manifest['source_path']
    if not isinstance(source, str) or not source.startswith('PROME/proposals/') or '..' in Path(source).parts:
        raise ValueError('Invalid prepared source path')
    patch = directory / 'card.patch'
    patch_bytes = patch.read_bytes()
    if hashlib.sha256(patch_bytes).hexdigest() != manifest['patch_sha256']:
        raise ValueError('Prepared patch changed; prepare it again')

    def check_preimages():
        for name, expected in ((QUEUE, manifest['queue_preimage_sha256']),
                               (source, manifest['source_preimage_sha256'])):
            path = root / name
            if path.is_symlink() or not path.resolve().is_relative_to(root):
                raise ValueError('Owner path must stay inside the repository without a symlink')
            actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
            if actual != expected:
                raise ValueError('Owner file changed since preparation: ' + name)

    check_preimages()
    for arguments in (['--check'], []):
        check_preimages()
        result = subprocess.run(['git', 'apply', *arguments, '-'], input=patch_bytes,
                                cwd=root, capture_output=True)
        if result.returncode:
            raise ValueError('Prepared patch refused: ' + result.stderr.decode(errors='replace').strip())
    return {'applied': str(directory), 'source': source,
            'next': 'Owner reviews and publishes queue/source together; nothing was staged or sent.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=reader.ROOT)
    parser.add_argument('--apply', type=Path, help='Apply a prepared directory after checking both owner-file preimages')
    parser.add_argument('--wq')
    parser.add_argument('--input', type=Path, help='JSON: choices, recommended_choice_id, context, conditions')
    parser.add_argument('--output', type=Path, help='New artifact directory; existing directories are refused')
    parser.add_argument('--replace-source', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.apply:
            if args.wq or args.input or args.output or args.replace_source:
                raise ValueError('--apply cannot be combined with preparation arguments')
            print(json.dumps(apply_prepared(args.root, args.apply)))
            return 0
        if not (args.wq and args.input and args.output):
            raise ValueError('Preparation requires --wq, --input and --output')
        result = prepare(args.root, args.wq, strict_json(args.input.read_text()), replace_source=args.replace_source)
        args.output.mkdir(parents=True, exist_ok=False)
        (args.output / 'source.md').write_text(result.pop('source'))
        (args.output / 'card.patch').write_text(result.pop('patch'))
        (args.output / 'manifest.json').write_text(json.dumps(result, indent=2) + '\n')
        print(json.dumps({'prepared': str(args.output), 'source': result['source_path'],
                          'next': 'Owner uses --apply on this directory, then publishes queue/source together; nothing was applied or sent.'}))
        return 0
    except (ValueError, OSError) as error:
        parser.exit(2, f'Card operation refused: {error}\n')


if __name__ == '__main__':
    main()
