#!/usr/bin/env python3
"""commit_check.py — pre-commit intent + post-commit verification for pathspec commits.

WHY (RAV review 2026-08-29, Will-endorsed): two PROME commits in 24h (d3915f75d,
6704cfc37) carried messages claiming file changes that a script had failed to make
before the commit ran. A post-hoc check DETECTS an overclaim; a pre-commit manifest
PREVENTS it. This tool does both and wraps them in one command so neither step is
a remembered ritual (finding_mechanize_the_cap_not_the_ritual).

MODES
  commit  -F MSG_FILE -- PATH [PATH...]      the normal path: write intent → git commit
                                             <paths> -F MSG → verify HEAD against intent
                                             AND against paths named in the message.
  intent  PATH [PATH...]                     write the manifest only (for multi-step flows)
  verify  [--ref HEAD] [--strict-message]    compare a commit's paths to the manifest
                                             (+ message-named paths); exit 1 on mismatch

CHECKS (commit, pre-flight)
  0. Commit SUBJECT (first non-empty line of MSG_FILE) ≤100 chars — root Git Protocol 4d
     (WQ-171, 2026-09-03); refused before the intent manifest is written.

CHECKS (verify)
  1. Every manifest path is in the commit; no commit path is outside the manifest
     (exact string match on repo-relative paths, rename-aware via --name-status).
  2. Every repo path NAMED IN THE MESSAGE (backticked, exists in the tree or in the
     commit) that is an EDIT claim must be in the commit. Bare citations ("see
     PROME/BOOT.md step 6") are legitimate, so message-path mismatches are
     ADVISORY by default and blocking under --strict-message.
  3. Manifest paths that show NO change in the commit (nothing to commit for them)
     are reported — that is exactly the d3915f75d failure shape (script died, file
     unchanged, message written anyway).

The manifest lives inside .git/ (per-clone, never committed, no gitignore needed).
Exit: 0 clean · 1 mismatch · 2 usage/unknown state (never guess).
Preflight parses `git status --porcelain=v2 -z` (RAV 8/29: v1 is not robust for quoted/unusual
filenames or renames; renames count BOTH paths as dirty).
"""
from __future__ import annotations
import argparse, os, re, subprocess, sys
from pathlib import Path

def sh(*args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit(2)
    return r.stdout

ROOT = Path(sh("rev-parse", "--show-toplevel").strip())
GITDIR = Path(sh("rev-parse", "--git-dir").strip())
if not GITDIR.is_absolute():
    GITDIR = ROOT / GITDIR
MANIFEST = GITDIR / "prome_commit_intent.txt"

def norm(p: str) -> str:
    """repo-relative, forward-slash, no leading ./"""
    q = Path(p)
    if q.is_absolute():
        try:
            q = q.resolve().relative_to(ROOT.resolve())
        except ValueError:
            sys.stderr.write(f"✗ {p} is outside the repo\n"); raise SystemExit(2)
    else:
        # resolve relative to CWD (may be a subdir), then make repo-relative
        q = (Path.cwd() / q).resolve()
        try:
            q = q.relative_to(ROOT.resolve())
        except ValueError:
            sys.stderr.write(f"✗ {p} is outside the repo\n"); raise SystemExit(2)
    return q.as_posix()

def write_intent(paths: list[str]) -> list[str]:
    rel = sorted({norm(p) for p in paths})
    if not rel:
        sys.stderr.write("✗ intent: no paths\n"); raise SystemExit(2)
    MANIFEST.write_text("\n".join(rel) + "\n", encoding="utf-8")
    return rel

def read_intent() -> list[str]:
    if not MANIFEST.exists():
        sys.stderr.write(f"✗ no manifest at {MANIFEST} — run `intent` or `commit` first\n")
        raise SystemExit(2)
    return [l.strip() for l in MANIFEST.read_text(encoding="utf-8").splitlines() if l.strip()]

def commit_paths(ref: str) -> dict[str, str]:
    """{path: status} for a commit; renames contribute BOTH old and new paths."""
    out = sh("show", "--name-status", "--format=", "-M", ref)
    res: dict[str, str] = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        st = parts[0]
        if st.startswith(("R", "C")) and len(parts) >= 3:
            res[parts[1]] = st; res[parts[2]] = st
        elif len(parts) >= 2:
            res[parts[1]] = st
        else:
            sys.stderr.write(f"✗ unparseable name-status line: {line!r}\n"); raise SystemExit(2)
    return res

PATH_RE = re.compile(r"`([^`\s]+/[^`\s]+|[^`\s]+\.(?:md|py|tsv|sh|json|js|txt|yml|yaml))`")

def message_paths(ref: str) -> list[str]:
    msg = sh("log", "-1", "--format=%B", ref)
    cands = set()
    for m in PATH_RE.findall(msg):
        c = m.rstrip(".,;:)")
        # strip trailing ":<line>" cites like PROME/CLOSEOUT.md:151
        c = re.sub(r":\d+$", "", c)
        if "<" in c or "*" in c or "{" in c:
            continue  # templates / globs are citations, not edit claims
        cands.add(c)
    return sorted(cands)

def verify(ref: str, strict_message: bool) -> int:
    intent = read_intent()
    actual = commit_paths(ref)
    short = sh("log", "-1", "--format=%h %s", ref).strip()[:110]
    print(f"commit_check · verify {ref} → {short}")
    rc = 0
    missing = [p for p in intent if p not in actual]
    extra = [p for p in actual if p not in intent]
    if missing:
        rc = 1
        print(f"  ❌ INTENDED BUT NOT IN COMMIT ({len(missing)}) — the d3915f75d shape: file unchanged when the commit ran")
        for p in missing: print(f"     - {p}")
    if extra:
        rc = 1
        print(f"  ❌ IN COMMIT BUT NOT INTENDED ({len(extra)}) — sweep or wrong pathspec")
        for p in extra: print(f"     - {p} [{actual[p]}]")
    if not missing and not extra:
        print(f"  ✅ intent ↔ commit: {len(intent)} path(s) match exactly")
    named = message_paths(ref)
    tree_named = []
    for p in named:
        exists = (ROOT / p).exists() or p in actual
        if exists:
            tree_named.append(p)
    unclaimed = [p for p in tree_named if p not in actual]
    if unclaimed:
        tag = "❌" if strict_message else "⚠️ "
        print(f"  {tag} message names {len(unclaimed)} repo path(s) NOT in the commit "
              f"({'blocking' if strict_message else 'advisory — citations are legitimate; edit-claims are not'}):")
        for p in unclaimed: print(f"     - {p}")
        if strict_message: rc = 1
    elif tree_named:
        print(f"  ✅ message-named paths ({len(tree_named)}) all present in the commit")
    print("  → rc", rc, "(0 clean · 1 mismatch — fix by a FOLLOW-UP commit, never --amend [root 4b])" if rc else "")
    return rc

def do_commit(msg_file: str, paths: list[str], strict_message: bool, extra_git: list[str]) -> int:
    # root Git Protocol 4d (WQ-171, 2026-09-03): the SUBJECT names the change, ≤100 chars;
    # receipts live in the body. Checked before any intent is written so a refusal leaves no trace.
    try:
        subject = next((ln for ln in open(msg_file, encoding="utf-8").read().split("\n") if ln.strip()), "")
    except OSError as e:
        print(f"  ❌ cannot read message file {msg_file}: {e}"); return 2
    if len(subject) > 100:
        print(f"  ❌ commit SUBJECT is {len(subject)} chars (>100, root Git Protocol 4d) — move the receipts to the body and re-run:")
        print(f"     {subject[:100]}…"); return 1
    rel = write_intent(paths)
    print(f"commit_check · intent written: {len(rel)} path(s) → {MANIFEST.relative_to(ROOT)}")
    # pre-flight: every intended path must actually have something to commit.
    # porcelain v2 + NUL (RAV 8/29): v1 line-splitting is not robust for quoted /
    # unusual filenames or renames. v2 -z entries: "1 <xy> ... <path>" (changed),
    # "2 <xy> ... <path>\0<origpath>" (rename/copy — BOTH paths count as dirty),
    # "? <path>" (untracked), "! <path>" (ignored).
    raw = subprocess.run(["git", "status", "--porcelain=v2", "-z", "--untracked-files=all", "--", *rel],
                         capture_output=True, cwd=ROOT).stdout
    fields = raw.split(b"\0")
    dirty, untracked = set(), set()
    i = 0
    while i < len(fields):
        f = fields[i].decode("utf-8", "surrogateescape")
        if not f:
            i += 1; continue
        kind = f[0]
        if kind == "1":
            dirty.add(f.split(" ", 8)[8]); i += 1
        elif kind == "2":
            dirty.add(f.split(" ", 9)[9])
            if i + 1 < len(fields):
                dirty.add(fields[i + 1].decode("utf-8", "surrogateescape"))
            i += 2
        elif kind == "?":
            untracked.add(f[2:]); i += 1
        elif kind == "!":
            i += 1
        else:
            print(f"  ❌ unparseable porcelain-v2 entry {f[:40]!r} — refusing (unknown state)"); return 2
    staged = set(sh("diff", "--cached", "--name-only", "--", *rel).splitlines())
    nothing = [p for p in rel if p not in dirty and p not in staged and p not in untracked]
    if nothing:
        print(f"  ❌ {len(nothing)} intended path(s) have NO change to commit — refusing before git runs "
              f"(this is the overclaim, caught early):")
        for p in nothing: print(f"     - {p}")
        return 1
    still_untracked = [p for p in rel if p in untracked and p not in staged]
    if still_untracked:
        print(f"  ❌ {len(still_untracked)} intended path(s) are UNTRACKED — `git add <exact paths>` first (root recipe 2), then re-run:")
        for p in still_untracked: print(f"     - {p}")
        return 1
    r = subprocess.run(["git", "commit", *extra_git, "-F", msg_file, "--", *rel], cwd=ROOT)
    if r.returncode != 0:
        print("  ❌ git commit failed — nothing verified"); return 1
    return verify("HEAD", strict_message)

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)
    a = sub.add_parser("intent"); a.add_argument("paths", nargs="+")
    v = sub.add_parser("verify"); v.add_argument("--ref", default="HEAD"); v.add_argument("--strict-message", action="store_true")
    c = sub.add_parser("commit"); c.add_argument("-F", "--file", required=True, help="message file (quoted-heredoc; root 4b)")
    c.add_argument("--strict-message", action="store_true")
    c.add_argument("paths", nargs="+", help="exact paths (put `--` before them)")
    args = ap.parse_args()
    if args.mode == "intent":
        rel = write_intent(args.paths); print(f"intent: {len(rel)} path(s) → {MANIFEST}"); return 0
    if args.mode == "verify":
        return verify(args.ref, args.strict_message)
    return do_commit(args.file, args.paths, args.strict_message, [])

if __name__ == "__main__":
    sys.exit(main())
