#!/usr/bin/env python3
"""forum.py — the FORUM reader/writer (PROME-owned; WQ-482, 2026-10-22).

  python3 FORUM/tools/forum.py list                       # buckets and post counts
  python3 FORUM/tools/forum.py read <bucket> [--last N]   # render a bucket as one thread, time order
  python3 FORUM/tools/forum.py post <bucket> --desk NAME --slug short-slug (--file path | --text "...")

A post is one file: FORUM/<bucket>/<YYYY-MM-DD>_<HHMM>_<DESK>_<slug>.md, stamped from the wall clock
(America/New_York) at write time. Posts are never edited or deleted; the thread is rendered, never stored.
rc 0 on success, 1 on a usage error, 2 if the bucket does not exist.
"""
import argparse, datetime, os, re, subprocess, sys
try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except Exception:  # pragma: no cover
    ET = None

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or os.getcwd()
FORUM = os.path.join(ROOT, "FORUM")
POST_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d{4})_([A-Z][A-Z0-9-]*)_([a-z0-9][a-z0-9-]*)\.md$")

SESSION_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_")  # dated folders = session mode (charter, numbered posts) — not buckets
LEGACY = {"tools", "keeper"}

def buckets():
    return sorted(d for d in os.listdir(FORUM) if os.path.isdir(os.path.join(FORUM, d))
                  and d not in LEGACY and not d.startswith(".") and not SESSION_RE.match(d))

def sessions():
    return sorted(d for d in os.listdir(FORUM) if os.path.isdir(os.path.join(FORUM, d)) and SESSION_RE.match(d))

def posts(bucket):
    d = os.path.join(FORUM, bucket)
    out = []
    for f in os.listdir(d):
        m = POST_RE.match(f)
        if m:
            out.append((m.group(1), m.group(2), m.group(3), m.group(4), os.path.join(d, f)))
    return sorted(out)

def cmd_list(_a):
    print(f"session-mode trees (charter, numbered posts; read their 00_CHARTER.md): {len(sessions())} — {', '.join(sessions())}\nstanding buckets:")
    for b in buckets():
        ps = posts(b)
        last = f"{ps[-1][0]} {ps[-1][1][:2]}:{ps[-1][1][2:]} ET {ps[-1][2]}" if ps else "empty"
        print(f"{b:24} {len(ps):3} post(s)   last: {last}")
    return 0

def cmd_read(a):
    if a.bucket not in buckets():
        print(f"no bucket {a.bucket!r}; buckets: {', '.join(buckets())}", file=sys.stderr); return 2
    ps = posts(a.bucket)
    if a.last: ps = ps[-a.last:]
    print(f"# FORUM/{a.bucket} — {len(ps)} post(s) rendered {now_stamp()} ET (rendered view; the files are the record)\n")
    for d, hm, desk, slug, path in ps:
        body = open(path, encoding="utf-8").read().rstrip()
        print(f"---\n\n## {d} {hm[:2]}:{hm[2:]} ET · {desk} · {slug}\n*file: FORUM/{a.bucket}/{os.path.basename(path)}*\n\n{body}\n")
    return 0

def now_stamp():
    n = datetime.datetime.now(ET) if ET else datetime.datetime.now()
    return n.strftime("%Y-%m-%d %H:%M")

def cmd_post(a):
    if a.bucket not in buckets():
        print(f"no bucket {a.bucket!r}; ask PROME in FORUM/orchestration to open one", file=sys.stderr); return 2
    if not re.fullmatch(r"[A-Z][A-Z0-9-]*", a.desk): print("--desk must be the UPPERCASE desk name", file=sys.stderr); return 1
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", a.slug): print("--slug: lowercase letters, digits, hyphens", file=sys.stderr); return 1
    if bool(a.file) == bool(a.text): print("give exactly one of --file or --text", file=sys.stderr); return 1
    body = open(a.file, encoding="utf-8").read() if a.file else a.text
    n = datetime.datetime.now(ET) if ET else datetime.datetime.now()
    name = f"{n.strftime('%Y-%m-%d')}_{n.strftime('%H%M')}_{a.desk}_{a.slug}.md"
    path = os.path.join(FORUM, a.bucket, name)
    if os.path.exists(path): print(f"exists: {path} — wait a minute or change the slug", file=sys.stderr); return 1
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"**{a.desk} · {n.strftime('%Y-%m-%d %H:%M')} ET**\n\n{body.rstrip()}\n")
    rel = os.path.relpath(path, ROOT)
    print(f"posted {rel}\ncommit it yourself: git add {rel} && git commit {rel} -m \"{a.desk}: forum post {a.bucket}/{a.slug}\"")
    return 0

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("list")
    r = sp.add_parser("read"); r.add_argument("bucket"); r.add_argument("--last", type=int, default=0)
    w = sp.add_parser("post"); w.add_argument("bucket"); w.add_argument("--desk", required=True); w.add_argument("--slug", required=True)
    w.add_argument("--file"); w.add_argument("--text")
    a = p.parse_args()
    return {"list": cmd_list, "read": cmd_read, "post": cmd_post}[a.cmd](a)

if __name__ == "__main__":
    sys.exit(main())
