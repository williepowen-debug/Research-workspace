"""Session-local notification queue; never a PROME read/ruling receipt."""
from contextlib import contextmanager
from datetime import datetime, timezone
import os
from pathlib import Path
import sqlite3
import time


def process_identity(pid):
    try:
        stat = Path(f'/proc/{int(pid)}/stat').read_text()
        tail = stat[stat.rfind(')')+2:].split()
        return {'pid': int(pid), 'start': tail[19],
                'boot': Path('/proc/sys/kernel/random/boot_id').read_text().strip()}
    except (OSError, ValueError, IndexError):
        return None


def session_parent():
    pid = os.getppid()
    for _ in range(10):
        try:
            name = Path(f'/proc/{pid}/comm').read_text().strip()
            if name in {'claude', 'claude-code'}:
                return process_identity(pid)
            raw = Path(f'/proc/{pid}/stat').read_text()
            pid = int(raw[raw.rfind(')')+2:].split()[1])
        except (OSError, ValueError, IndexError):
            return None
    return None


def interactive_parent(identity):
    """Only a real interactive Claude stdin supports this installed watcher."""
    try:
        argv = Path(f"/proc/{identity['pid']}/cmdline").read_bytes().decode().split('\0')
        if any(arg == '--print' or arg.startswith('--print=')
               or (arg.startswith('-') and not arg.startswith('--') and 'p' in arg[1:])
               for arg in argv[1:]):
            return False  # `claude -p PROMPT` can inherit a terminal stdin.
        fd = os.open(f"/proc/{identity['pid']}/fd/0", os.O_RDONLY | os.O_NONBLOCK)
        try:
            return os.isatty(fd)
        finally:
            os.close(fd)
    except (OSError, KeyError, TypeError):
        return False


class Notifications:
    def __init__(self, state):
        self.state = Path(state)
        self.state.mkdir(parents=True, exist_ok=True)
        self.path = self.state / 'notifications.sqlite3'

    @contextmanager
    def connect(self):
        with sqlite3.connect(self.path, timeout=2) as db:
            db.row_factory = sqlite3.Row
            db.executescript('''
                CREATE TABLE IF NOT EXISTS notices (
                  id TEXT PRIMARY KEY, sha TEXT NOT NULL, packet TEXT NOT NULL,
                  queued REAL NOT NULL, attempted_session TEXT, attempted REAL, acknowledged INTEGER NOT NULL DEFAULT 0);
                CREATE TABLE IF NOT EXISTS listener (
                  singleton INTEGER PRIMARY KEY CHECK(singleton=1), session TEXT NOT NULL,
                  pid INTEGER NOT NULL, start TEXT NOT NULL, boot TEXT NOT NULL,
                  beat REAL NOT NULL, ended INTEGER NOT NULL);
            ''')
            yield db

    def enqueue(self, repo, event):
        from delivery import published_packet, validate
        from pilot_files import encoded
        validate(repo, event)
        packet = published_packet(repo, event)
        if not packet:
            raise ValueError('Only a verified published packet can notify PROME')
        from delivery import event_path
        if repo.read(event_path(event), 'origin/master') != encoded(event)+'\n':
            raise ValueError('Published response is missing or changed')
        with self.connect() as db:
            old = db.execute('SELECT * FROM notices WHERE id=?', (event['id'],)).fetchone()
            if old and (old['sha'] != event['sha256']):
                raise ValueError('Notification identity conflict')
            db.execute('INSERT OR IGNORE INTO notices (id,sha,packet,queued) VALUES (?,?,?,?)',
                       (event['id'],event['sha256'],packet,time.time()))
        return self.status()

    def claim(self, session, identity, *, replace=False):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT * FROM listener WHERE singleton=1').fetchone()
            active = row and not row['ended'] and process_identity(row['pid']) == {
                'pid':row['pid'], 'start':row['start'], 'boot':row['boot']}
            if active and (row['session'] == session or not replace):
                return False
            # Claim before waiting for the old process's lock. Its next heartbeat
            # fails; old SessionEnd cannot end the new session. Beat zero means
            # starting/UNKNOWN until this watcher actually owns the lock.
            db.execute('INSERT OR REPLACE INTO listener VALUES (1,?,?,?,?,0,0)',
                       (session, identity['pid'], identity['start'], identity['boot']))
            return True

    def heartbeat(self, session, identity, starting=False):
        with self.connect() as db:
            if starting:
                db.execute('INSERT OR REPLACE INTO listener VALUES (1,?,?,?,?,?,0)',
                           (session,identity['pid'],identity['start'],identity['boot'],time.time()))
                return True
            return db.execute('UPDATE listener SET beat=? WHERE session=? AND pid=? AND start=? AND boot=? AND ended=0',
                              (time.time(),session,identity['pid'],identity['start'],identity['boot'])).rowcount == 1

    def end(self, session):
        with self.connect() as db:
            db.execute('UPDATE listener SET ended=1, beat=? WHERE session=?', (time.time(),session))

    def pending(self, session):
        with self.connect() as db:
            return [dict(row) for row in db.execute('SELECT * FROM notices WHERE acknowledged=0 AND (attempted_session IS NULL OR attempted_session!=?) ORDER BY queued LIMIT 20', (session,))]

    def attempted(self, session, ids):
        with self.connect() as db:
            db.executemany('UPDATE notices SET attempted_session=?,attempted=? WHERE id=?',
                           [(session,time.time(),eid) for eid in ids])

    def acknowledge(self, event_id):
        # Caller must have obtained an actual validated owner receipt.
        with self.connect() as db:
            db.execute('UPDATE notices SET acknowledged=1 WHERE id=?', (event_id,))

    def status(self):
        with self.connect() as db:
            row = db.execute('SELECT * FROM listener WHERE singleton=1').fetchone()
        if not row:
            return {'state':'unknown', 'message':'PROME notification connection is not established. Delivered answers remain in its inbox.'}
        if row['ended']:
            return {'state':'offline', 'message':'The registered PROME session has ended. Delivered answers are waiting in its inbox.'}
        current = process_identity(row['pid'])
        if current and (current['start'] != row['start'] or current['boot'] != row['boot']):
            return {'state':'unknown', 'message':'PROME session identity changed; notification is unconfirmed.'}
        if current is None or time.time()-row['beat'] > 20:
            return {'state':'unknown', 'message':'PROME notification connection is unavailable; delivery does not mean it has read your answer.'}
        return {'state':'listening', 'message':'PROME notification listener is connected. It will be alerted after delivery; reading is confirmed separately.'}
