#!/usr/bin/env python3
"""Bounded read-only research worker. JSON lines over stdin/stdout, no launches."""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CONFIG = Path(__file__).with_name('research_sources.json')
EXCLUDED = {'archive', 'archives', '_archive', 'backup', 'backups', 'raw',
            'source', 'sources', 'data', 'cache', '__pycache__'}
MAX_FILE = 1024 * 1024
MAX_BYTES = 32 * MAX_FILE
MAX_DOCS = 1000
MAX_ENTRIES = 10000
MAX_DEPTH = 12
MAX_SECONDS = 10


def parts(path):
    if not isinstance(path, str) or not path or '\\' in path or '\x00' in path:
        raise ValueError('Invalid document path')
    p = PurePosixPath(path)
    if p.is_absolute() or any(x in {'.', '..', ''} for x in path.split('/')):
        raise ValueError('Document path must stay inside configured roots')
    return p.parts


def excluded(name):
    return name.startswith('.') or name.casefold() in EXCLUDED


def stamp(st):
    return [st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns]


class Reader:
    def __init__(self, root=ROOT, config=CONFIG):
        self.root = Path(root)
        config = json.loads(Path(config).read_text(encoding='utf-8-sig'))
        if config.get('version') != 1 or not isinstance(config.get('desks'), list):
            raise ValueError('Unsupported research configuration')
        self.desks = config['desks']
        names, roots = set(), set()
        for desk in self.desks:
            if not isinstance(desk.get('name'), str) or not desk['name'] or desk['name'] in names:
                raise ValueError('Invalid/duplicate research desk')
            rp = parts(desk['root'])
            if rp in roots or any(rp[:len(r)] == r or r[:len(rp)] == rp for r in roots):
                raise ValueError('Overlapping research roots')
            roots.add(rp); names.add(desk['name'])
            for key in ('overview', 'directories'):
                if not isinstance(desk.get(key), list):
                    raise ValueError('Missing research locations')
                for value in desk[key]:
                    p = parts(value)
                    if len(p) != 1 or excluded(value):
                        raise ValueError('Research locations must be direct, non-hidden children')
                    if key == 'overview' and not value.lower().endswith('.md'):
                        raise ValueError('Overview must be Markdown')
            if any(v not in {'research', 'reports', 'audits'} for v in desk['directories']):
                raise ValueError('Unsupported research category')
        self.documents = []
        self.issues = []
        self.scanned_at = None

    def _open(self, path, directory=False):
        """Walk descriptors with O_NOFOLLOW, including every parent and final file."""
        elements = parts(path)
        fd = os.open(self.root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            for i, element in enumerate(elements):
                isdir = i < len(elements) - 1 or directory
                flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
                if isdir:
                    flags |= os.O_DIRECTORY
                child = os.open(element, flags, dir_fd=fd)
                os.close(fd); fd = child
            return fd
        except BaseException:
            os.close(fd)
            raise

    def location(self, path):
        p = parts(path)
        for desk in self.desks:
            prefix = parts(desk['root'])
            if p[:len(prefix)] != prefix:
                continue
            rel = p[len(prefix):]
            if len(rel) == 1 and rel[0] in desk['overview']:
                return desk['name'], 'Overview'
            if (len(rel) >= 2 and rel[0] in desk['directories']
                    and len(rel) <= MAX_DEPTH and rel[-1].lower().endswith('.md')
                    and not excluded(rel[-1]) and not any(excluded(x) for x in rel[:-1])):
                return desk['name'], rel[0].title()
        raise ValueError('Document is outside the configured research collection')

    def read(self, path):
        self.location(path)
        fd = self._open(path)
        try:
            before = os.fstat(fd)
            if not stat.S_ISREG(before.st_mode):
                raise ValueError('Not a regular document')
            if before.st_size > MAX_FILE:
                raise ValueError('Document exceeds 1 MiB; not read or truncated')
            with os.fdopen(fd, 'rb', closefd=False) as stream:
                raw = stream.read(MAX_FILE + 1)
            if len(raw) > MAX_FILE:
                raise ValueError('Document grew beyond the 1 MiB limit')
            if stamp(os.fstat(fd)) != stamp(before):
                raise ValueError('Document changed during reading; reload')
            # Detect atomic replacement of the pathname as well as in-place writes.
            current = self._open(path)
            try:
                if stamp(os.fstat(current)) != stamp(before):
                    raise ValueError('Document was replaced during reading; reload')
            finally:
                os.close(current)
            text = raw.decode('utf-8-sig', errors='strict')
            if any(ord(c) < 32 and c not in '\t\r\n' for c in text):
                raise ValueError('Unsupported control character; cannot display the full source safely')
            return text, stamp(before)
        finally:
            os.close(fd)

    def scan(self):
        docs, issues = [], []
        started = time.monotonic()
        total, entries = 0, 0

        def issue(path, error):
            if len(issues) < 100:
                issues.append({'path': path, 'message': str(error)})

        def budget():
            if time.monotonic() - started > MAX_SECONDS:
                raise ValueError('10-second scan limit reached')
            if entries > MAX_ENTRIES:
                raise ValueError('10,000-entry scan limit reached')

        def add(path):
            nonlocal total
            budget()
            if len(docs) >= MAX_DOCS:
                raise ValueError('1,000-document scan limit reached')
            try:
                text, version = self.read(path)
            except (OSError, ValueError, UnicodeError) as exc:
                issue(path, exc); return
            size = version[2]
            if total + size > MAX_BYTES:
                raise ValueError('32 MiB scan limit reached')
            total += size
            desk, category = self.location(path)
            title = next((line.lstrip('#').strip() for line in text.splitlines()
                          if re.match(r'^#{1,6} ', line)), Path(path).stem)
            path_date = ''
            for component in reversed(parts(path)):
                m = re.match(r'^(\d{4}-\d{2}-\d{2})(?:\D|$)', component)
                if m:
                    try:
                        path_date = date.fromisoformat(m[1]).isoformat(); break
                    except ValueError:
                        pass
            docs.append(dict(path=path, desk=desk, category=category, title=title[:300],
                             path_date=path_date, size=size, version=version, text=text))

        def walk(path, depth):
            nonlocal entries
            budget()
            if depth >= MAX_DEPTH:
                issue(path, 'Depth limit reached'); return
            try:
                fd = self._open(path, directory=True)
            except OSError as exc:
                issue(path, exc); return
            try:
                for name in sorted(os.listdir(fd)):
                    entries += 1; budget()
                    if excluded(name):
                        continue
                    child = path + '/' + name
                    try:
                        st = os.stat(name, dir_fd=fd, follow_symlinks=False)
                        if stat.S_ISLNK(st.st_mode):
                            issue(child, 'Symlink excluded'); continue
                        if stat.S_ISDIR(st.st_mode):
                            walk(child, depth + 1)
                        elif name.lower().endswith('.md'):
                            add(child)
                    except OSError as exc:
                        issue(child, exc)
            finally:
                os.close(fd)

        try:
            for desk in self.desks:
                for filename in desk['overview']:
                    add(desk['root'] + '/' + filename)
                for folder in desk['directories']:
                    walk(desk['root'] + '/' + folder, 1)
        except ValueError as exc:
            issue('Collection', exc)
        docs.sort(key=lambda d: d['path'])
        docs.sort(key=lambda d: d['path_date'], reverse=True)
        docs.sort(key=lambda d: d['category'] != 'Overview')
        self.documents, self.issues = docs, issues
        self.scanned_at = datetime.now(timezone.utc).isoformat()

    def search(self, query='', desk='All three', category='All documents'):
        if not isinstance(query, str) or len(query) > 1000:
            raise ValueError('Search must contain at most 1,000 characters')
        if desk != 'All three' and desk not in [d['name'] for d in self.desks]:
            raise ValueError('Unknown desk filter')
        if category not in {'All documents', 'Overview', 'Research', 'Reports', 'Audits'}:
            raise ValueError('Unknown document type')
        if self.scanned_at is None:
            self.scan()
        pattern = re.compile(re.escape(query), re.IGNORECASE) if query else None
        rows = []
        for doc in self.documents:
            if desk != 'All three' and doc['desk'] != desk:
                continue
            if category != 'All documents' and doc['category'] != category:
                continue
            match = pattern.search(doc['text']) if pattern else None
            metadata_match = pattern and (pattern.search(doc['title']) or pattern.search(doc['path']))
            if pattern and not match and not metadata_match:
                continue
            row = {k: v for k, v in doc.items() if k != 'text'}
            row['match_kind'] = 'Text' if match else ('Title/path' if metadata_match else '')
            row['snippet'] = doc['text'][max(0, match.start()-35):match.end()+100].replace('\n', ' ') if match else ''
            rows.append(row)
        return dict(documents=rows, total=len(self.documents), issues=self.issues,
                    complete=not self.issues, scanned_at=self.scanned_at,
                    desks=[d['name'] for d in self.desks])

    def handle(self, request):
        if not isinstance(request, dict) or type(request.get('id')) is not int:
            raise ValueError('Invalid reader request')
        op = request.get('op')
        if op in {'scan', 'search'}:
            if op == 'scan':
                self.scan()
            result = self.search(request.get('query', ''), request.get('desk', 'All three'),
                                 request.get('category', 'All documents'))
        elif op == 'open':
            path = request['path']
            text, version = self.read(path)
            result = dict(path=path, text=text, version=version,
                          read_at=datetime.now(timezone.utc).isoformat())
        elif op == 'stat':
            path = request['path']; self.location(path)
            fd = self._open(path)
            try:
                st = os.fstat(fd)
                if not stat.S_ISREG(st.st_mode):
                    raise ValueError('Not a regular document')
                result = dict(path=path, version=stamp(st))
            finally:
                os.close(fd)
        else:
            raise ValueError('Unknown read-only operation')
        return dict(id=request['id'], op=op, ok=True, **result)


def serve(reader, inp=sys.stdin, out=sys.stdout):
    while True:
        line = inp.readline(16385)
        if not line:
            return
        if len(line) > 16384:
            # Refuse the stream, not a truncated request or its remaining tail.
            out.write(json.dumps({'id': None, 'ok': False, 'message': 'Request too large'})+'\n');out.flush();return
        request = None
        try:
            request = json.loads(line)
            result = reader.handle(request)
        except (OSError, ValueError, KeyError, TypeError, UnicodeError) as exc:
            result = {'id': request.get('id') if isinstance(request, dict) else None,
                      'op': request.get('op') if isinstance(request, dict) else None,
                      'ok': False, 'message': str(exc)}
        out.write(json.dumps(result, ensure_ascii=True)+'\n');out.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serve', action='store_true', required=True)
    parser.parse_args()
    try:
        serve(Reader())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr); sys.exit(2)
