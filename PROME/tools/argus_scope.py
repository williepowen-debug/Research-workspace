#!/usr/bin/env python3
"""argus_scope.py — the audit scope for ARGUS. REDESIGNED 2026-09-11 (DOCKET L336, Will-authorized).

WHY A REDESIGN AND NOT A FIFTH PATCH. An external reviewer's diagnosis, after four regex repairs in one
evening: every defect in this tool — the watermark that matched a subject ABOUT closeout, the packet pattern
that crossed `processed/`, the filename key that dropped the MSG-* route, the date pattern that claimed the
shared daily note, the lineage inference — was ONE design choice. **Authorship and audit boundaries were
RECONSTRUCTED from commit subjects and file names instead of RECORDED.** So they are recorded now:

  A1  BASELINE  -> PROME/state/argus_baseline.json   (a recorded sha; no subject is ever parsed)
  A2  PERIMETER -> PROME/state/AUDIT_PERIMETER.tsv   (declared rows; this file holds NO path patterns)
  A3  ATTRIBUTION is by recorded path ownership, never by who wrote a commit subject
  A4  NO SILENT DROP: anything matching no rule is reported UNATTRIBUTED
  A5  no SHARED surface is ever claimed as PROME's
  A6  a path both committed and pending keeps BOTH states and BOTH prescribed reads

Acceptance conditions: PROME/proposals/2026-09-11_L336-argus-redesign-ACCEPTANCE-CONDITIONS.md

Usage (from the repo root):
    python3 PROME/tools/argus_scope.py                  # human list + the skip verdict
    python3 PROME/tools/argus_scope.py --json           # machine form for the spawn prompt
    python3 PROME/tools/argus_scope.py --record-baseline <sha>   # at the closeout commit
Exit: 0 = spawn ARGUS · 3 = under the floor (skip, say so) · 2 = no recorded baseline (do not guess).
"""
import argparse
import fnmatch
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

MIN_PATHS = 3
ROOT = Path(__file__).resolve().parents[2]
PERIMETER_FILE = "PROME/state/AUDIT_PERIMETER.tsv"
BASELINE_FILE = "PROME/state/argus_baseline.json"
CLASSES = ("OWNED", "SHARED", "EXCLUDED")


def git(*args):
    # ⛔ cwd=ROOT is LOAD-BEARING, not tidiness. Without it scope was discovered from the
    # PROCESS CWD while content was read from ROOT (_committed_content_id already passed
    # cwd=ROOT). From a second worktree or clone of the same repo the baseline sha still
    # resolves — the object DB is shared — so load_baseline() succeeded, build_scope()
    # returned the OTHER checkout's scope, nothing raised, and mark_reviewed() promoted the
    # real repo's manifest to REVIEWED over an unreviewed addition. CLOSEOUT's
    # `cd "$(git rev-parse --show-toplevel)"` does NOT prevent it: inside a worktree that
    # idiom resolves to the WORKTREE root. (Independent review 2026-09-13, round 3.)
    return subprocess.run(["git", *args], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout


# ---------------------------------------------------------------- A2: the recorded perimeter

def load_perimeter(path=None):
    """Ordered [(pattern, class, reason)]. First match wins. Malformed rows FAIL LOUD, never default."""
    f = Path(path or (ROOT / PERIMETER_FILE))
    if not f.exists():
        raise SystemExit(f"ARGUS-SCOPE 2 — perimeter manifest missing: {f}")
    rules, seen_header = [], False
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cells = line.split("\t")
        if not seen_header and cells[0].strip() == "pattern":
            seen_header = True
            continue
        if len(cells) < 3:
            raise SystemExit(f"ARGUS-SCOPE 2 — {f}:{i}: need 3 tab-separated cells, got {len(cells)}")
        pat, cls, reason = cells[0].strip(), cells[1].strip(), cells[2].strip()
        if cls not in CLASSES:
            raise SystemExit(f"ARGUS-SCOPE 2 — {f}:{i}: class '{cls}' not in {CLASSES}")
        rules.append((pat, cls, reason))
    if not rules:
        raise SystemExit(f"ARGUS-SCOPE 2 — {f} declares no rules")
    return rules


def _match(pattern, path):
    """fnmatch, except `*` does NOT cross a separator and `**` does. Written out rather than trusting fnmatch,
    whose `*` matches `/` and would make `AGENTS/*/inbox/*` swallow `inbox/processed/x`."""
    rx = []
    i = 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            rx.append(".*")
            i += 2
        elif pattern[i] == "*":
            rx.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            rx.append("[^/]")
            i += 1
        else:
            rx.append(re.escape(pattern[i]))
            i += 1
    return re.fullmatch("".join(rx), path) is not None


def classify(path, rules):
    """(class, reason). First match wins. No match => UNATTRIBUTED — never dropped (A4)."""
    for pat, cls, reason in rules:
        if _match(pat, path):
            return cls, reason
    return "UNATTRIBUTED", "matches no declared rule in " + PERIMETER_FILE


# ---------------------------------------------------------------- A1: the recorded baseline

def load_baseline(path=None):
    f = Path(path or (ROOT / BASELINE_FILE))
    if not f.exists():
        return None, f"no baseline record at {f}"
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return None, f"baseline record unparseable: {e}"
    sha = (d.get("sha") or "").strip()
    if not re.fullmatch(r"[0-9a-f]{7,40}", sha):
        return None, f"baseline record has no usable sha (got {sha!r})"
    try:
        git("cat-file", "-e", sha + "^{commit}")
    except subprocess.CalledProcessError:
        return None, f"recorded baseline {sha[:9]} is not a commit in this repository"
    # A1 says the tool never silently picks a WRONG baseline. `cat-file -e` passes on a commit that is no longer
    # reachable from HEAD — exactly what the routine non-ff rebase recovery in root CLAUDE.md session-end step 3
    # produces. That is a third state the condition did not name: record PRESENT, record INVALID. Without this
    # check the tool prints a normal verdict over a scope that silently re-includes a previous closeout and
    # other desks' paths. (Independent review 2026-09-11, CE-2.)
    try:
        git("merge-base", "--is-ancestor", sha, "HEAD")
    except subprocess.CalledProcessError:
        return None, (f"recorded baseline {sha[:9]} is NOT an ancestor of HEAD — it was orphaned, most likely by "
                      f"a rebase. Re-record it: --record-baseline <the closeout commit on this history>")
    return d, ""


REVIEW_FILE = "PROME/state/argus_review.json"
# Bookkeeping ABOUT a review is never part of the candidate it describes. The review
# receipt changes every time it is written, and the baseline record changes AFTER the
# commit (--record-baseline HEAD), so including either makes re-freezing impossible and
# guarantees the next session inherits a failure. WQ-240 patch, Will 2026-09-12 21:41.
RECEIPT_PATHS = {REVIEW_FILE, BASELINE_FILE}

# A review manifest belongs to ONE closeout. Carried into the next session it would
# report last session's paths as CHANGED — a stale failure, not a finding. The manifest
# records the baseline it was taken against; a different baseline means PRIOR SESSION,
# which reads as CANNOT-EVALUATE (absent), never as a failure.
FROZEN, REVIEWED = "FROZEN", "REVIEWED"


def _content_id(path):
    """sha256 of the WORKING-TREE bytes, or None if the path is absent.

    Content, never mtime and never a commit sha: the question this answers is
    "is what ships byte-identical to what was reviewed?", and a path can be
    committed, amended, regenerated or reverted between review and commit
    without its commit id telling you so."""
    f = ROOT / path
    if not f.exists():
        return None
    return hashlib.sha256(f.read_bytes()).hexdigest()


def _current_baseline_sha():
    f = ROOT / BASELINE_FILE
    if not f.exists():
        return None
    try:
        return (json.loads(f.read_text(encoding="utf-8")).get("sha") or "").strip() or None
    except json.JSONDecodeError:
        return None


def record_review(paths, verdict=FROZEN, consumed_moves=None):
    """Freeze the identity of the candidate.

    `consumed_moves` — {DEST: ORIGIN} pairs PROME DECLARES as byte-identical `git mv`
    consumptions of its own inbound packets (WQ-289 (b), DOCKET L473). Declared here so
    ARGUS can confirm each at the artifact; `verify_review()` re-establishes the bytes
    itself and never trusts the declaration (P1/P3 in
    tests/ACCEPTANCE_argus_r100_consumed_move_WQ289.md).

    ⛔ The default verdict is FROZEN, never REVIEWED. Freezing is something PROME
    does to its own work; being reviewed is something ARGUS does to it. An earlier
    version wrote "REVIEWED" at freeze time, so the receipt asserted an audit that
    had not happened — and did so on its own delivery."""
    entries = {p: _content_id(p) for p in sorted(set(paths)) if p not in RECEIPT_PATHS}
    f = ROOT / REVIEW_FILE
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps({
        "verdict": verdict,
        "baseline": _current_baseline_sha(),
        "head": git("rev-parse", "HEAD").strip(),
        "recorded_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "recorded_by": os.environ.get("PROME_SESSION", "PROME"),
        "paths": entries,
        "consumed_moves": dict(consumed_moves or {}),
    }, indent=2) + "\n", encoding="utf-8")
    return entries


def mark_reviewed(note=""):
    """Promote FROZEN -> REVIEWED. Only an actual audit outcome may call this, and
    it refuses when the frozen candidate has since changed: a verdict may not be
    attached to content the reviewer did not see."""
    f = ROOT / REVIEW_FILE
    if not f.exists():
        return 2, "CANNOT-EVALUATE: nothing frozen — run --record-review first"
    rc, lines = verify_review()
    if rc == 2:
        # A verdict may not be attached to a candidate whose completeness could not be
        # established — that is how an unreviewed addition got promoted to REVIEWED.
        return 2, "REFUSED (CANNOT-EVALUATE): " + "; ".join(lines)
    if rc != 0:
        return 1, "REFUSED: the frozen candidate changed since the freeze — " + "; ".join(lines)
    d = json.loads(f.read_text(encoding="utf-8"))
    d["verdict"] = REVIEWED
    d["reviewed_note"] = note
    d["reviewed_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    f.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8")
    return 0, f"verdict REVIEWED over {len(d['paths'])} path(s)"


def _committed_content_id(path, ref="HEAD"):
    """sha256 of the path's contents IN THE COMMIT — the actual delivery.

    `_content_id` reads the working tree, which answers a different question: a
    path can be edited-then-reverted, or staged differently from the file on disk."""
    try:
        blob = subprocess.run(["git", "--no-replace-objects", "show", f"{ref}:{path}"], cwd=ROOT,
                              env={**os.environ, "GIT_NO_REPLACE_OBJECTS": "1"},
                              capture_output=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None
    return hashlib.sha256(blob).hexdigest()


# ---------------------------------------------------------------- WQ-289 (b): the narrow L367 form

ORIGIN_REMOTE, ORIGIN_BRANCH = "origin", "master"
ORIGIN_FULLREF = f"refs/remotes/{ORIGIN_REMOTE}/{ORIGIN_BRANCH}"
ORIGIN_REF = f"{ORIGIN_REMOTE}/{ORIGIN_BRANCH}"     # display name only — never resolved by this short form
# ⛔ Round-3 reader ❌1 (2026-09-25): `git replace <origin blob> <local blob>` is honoured by EVERY git
# object read, so an unpushed local edit read as "bytes on origin" with a clean R100 receipt. Every
# git call on the exemption path runs with replace refs DISABLED.
_NOREPLACE_ENV = {**os.environ, "GIT_NO_REPLACE_OBJECTS": "1"}


def _xgit(*args, check=True, timeout=None):
    """git on the EXEMPTION PATH: cwd=ROOT, replace refs disabled, bytes out. Raises CalledProcessError."""
    return subprocess.run(["git", "--no-replace-objects", *args], cwd=ROOT, env=_NOREPLACE_ENV,
                          capture_output=True, check=check, timeout=timeout)


def _fetch_origin_sha():
    """ONE fetch per verify, by EXPLICIT refspec into the FULL remote-tracking ref, then the
    commit sha of that full ref. Returns (sha, None) or (None, why).

    ⛔ Round-2 reader ❌A (2026-09-25): `git fetch origin master` + `cat-file origin/master:path`
    read the SHORT name, which a local branch or tag called `origin/master` shadows (git warns
    "refname is ambiguous" and picks the wrong one), and a repo with no matching fetch refspec
    updates only FETCH_HEAD, leaving the tracking ref stale — both passed a packet that was
    never on origin. The refspec pins what is fetched; the full ref pins what is read.
    ⛔ Round-1 reader ❌6: the fetch itself is load-bearing — CLOSEOUT step 10 runs before
    safe-push.sh, so the tracking ref can be stale. Failure ⇒ refusal, never a pass."""
    try:
        # ⛔ Round-3 reader ❌3: with NO remote named `origin`, `git fetch origin` treats the word as a
        # PATH — a nested clone at ./origin certified an unpushed packet. The remote must EXIST as a
        # configured remote (a URL, read-only) before anything is fetched from it.
        step = f"git remote get-url {ORIGIN_REMOTE}"
        url = _xgit("remote", "get-url", "--all", ORIGIN_REMOTE).stdout.decode("utf-8", "replace").split()
        if not url:
            return None, f"remote `{ORIGIN_REMOTE}` has no URL configured"
        # ⛔ Round-4 reader ❌1: the FETCH URL is not the PUSH URL. A `pushurl`/`pushInsteadOf` can point
        # safe-push.sh at a server that never held the packet while the fetch reads a mirror that did —
        # "on origin" must mean the server the closeout PUSHES to. Fetch set == push set, or refuse.
        push = _xgit("remote", "get-url", "--push", "--all", ORIGIN_REMOTE).stdout.decode("utf-8", "replace").split()
        if sorted(url) != sorted(push):
            return None, f"remote `{ORIGIN_REMOTE}` fetch URL(s) {url} differ from push URL(s) {push} — 'on origin' cannot mean one server for the read and another for the push"
        # ⛔ Round-4 reader ⚠️2: if the tracking ref is a SYMREF onto the checked-out branch, the forced
        # fetch below rewinds HEAD and strands the unpushed commit in the reflog. Refuse; never fetch.
        step = f"git symbolic-ref {ORIGIN_FULLREF}"
        if _xgit("symbolic-ref", "-q", ORIGIN_FULLREF, check=False).returncode == 0:
            return None, f"`{ORIGIN_FULLREF}` is a SYMBOLIC ref — a fetch through it would move a local branch; repair the ref before verifying"
        step = f"git fetch {ORIGIN_REMOTE} +refs/heads/{ORIGIN_BRANCH}:{ORIGIN_FULLREF}"
        _xgit("fetch", "-q", ORIGIN_REMOTE, f"+refs/heads/{ORIGIN_BRANCH}:{ORIGIN_FULLREF}", timeout=60)
        step = f"git rev-parse --verify {ORIGIN_FULLREF}"
        sha = _xgit("rev-parse", "--verify", f"{ORIGIN_FULLREF}^{{commit}}").stdout.decode().strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        err = getattr(e, "stderr", b"") or b""
        if isinstance(err, bytes):
            err = err.decode("utf-8", "replace")
        return None, f"`{step}` failed ({err.strip()[:80] or type(e).__name__})"   # round-4 ⚠️3: name the step that failed
    return sha, None


def _origin_blob_id(path, origin_sha):
    """sha256 of `<origin_sha>:path` — the blob at the FETCHED commit, addressed by sha, never by
    a name. Returns (hexdigest, None) or (None, why)."""
    try:
        blob = _xgit("cat-file", "-p", f"{origin_sha}:{path}").stdout
    except subprocess.CalledProcessError as e:
        err = (e.stderr or b"").decode("utf-8", "replace").strip()
        return None, f"`{ORIGIN_FULLREF}@{origin_sha[:9]}:{path}` is not readable ({err[:80] or 'no such object'})"
    return hashlib.sha256(blob).hexdigest(), None


def _index_content_id(path):
    """sha256 of the INDEX blob `:path` — what a pathspec commit ships (round-2 reader ❌B: the
    working-tree file can differ from the index under assume-unchanged / skip-worktree / line-
    ending filters while `git diff --name-only` stays quiet). None if not in the index."""
    try:
        blob = _xgit("cat-file", "-p", f":{path}").stdout
    except subprocess.CalledProcessError:
        return None
    return hashlib.sha256(blob).hexdigest()


def _git_sees_r100(origin, dest, ref):
    """Does GIT record ORIGIN→DEST as a 100%-similar rename? (reader ❌1/❌3/❌4: byte
    equality with origin/master is not a rename — an addition, or a delete+add whose bytes
    happen to match a NEWER origin blob, satisfies it; only git's own rename detection
    proves the local tree HELD the origin and moved it unchanged.)
    ref=None ⇒ the STAGED move (`git mv` stages it; an unstaged mv is refused);
    ref given ⇒ the move must be inside that commit (`ref^..ref`)."""
    if ref:
        args = ["diff", "--name-status", "-M100%", "--diff-filter=R", f"{ref}^", ref, "--", origin, dest]
    else:
        args = ["diff", "--name-status", "-M100%", "--diff-filter=R", "--cached", "--", origin, dest]
    try:
        out = _xgit(*args).stdout.decode("utf-8", "replace")
    except subprocess.CalledProcessError as e:
        return False, f"git could not evaluate the rename ({(e.stderr or b'').decode('utf-8', 'replace').strip()[:80]})"
    for line in out.splitlines():
        cells = line.split("\t")
        if len(cells) == 3 and cells[0] == "R100" and cells[1] == origin and cells[2] == dest:
            return True, None
    where = f"in {ref}^..{ref}" if ref else "in the index (is the move staged?)"
    return False, f"git does not record ORIGIN→DEST as an R100 rename {where}"


def _clean_relpath(p):
    return (isinstance(p, str) and p and not p.startswith(("/", "./", "../")) and "/../" not in p
            and not p.endswith("/..") and os.path.normpath(p) == p and "\\" not in p)


def _consumed_move_exemption(dest, origin, ref, manifest, listed, origin_sha):
    """WQ-289 (b), DOCKET L473 — the ONLY exemption from UNREVIEWED, and it is narrow:

    a DECLARED (P1), ARGUS-confirmed (P2: manifest verdict REVIEWED) `git mv` that GIT ITSELF
    records as R100 (P3/P4: rename source in the parent, identical bytes, staged or committed),
    whose ORIGIN bytes are on a FRESHLY FETCHED origin/master (P3), of PROME's OWN inbound packet
    into PROME's OWN processed/ (P5: by PATH, never by subject or filename), with BOTH halves in
    the candidate list (P8). Anything else returns (False, why) and the caller keeps blocking.
    Missing information (P6) is a refusal with the reason, never a pass.
    Returns (True, receipt_line) or (False, why)."""
    if manifest.get("verdict") != REVIEWED:
        return False, "declared consumed move but the manifest is not REVIEWED — ARGUS has not confirmed it"
    if not (_clean_relpath(origin) and _clean_relpath(dest)):
        return False, "ORIGIN/DEST must be plain normalised repo-relative paths (no `..`, `./`, leading `/`)"
    if not (_match("PROME/inbox/**", origin) and not _match("PROME/inbox/processed/**", origin)):
        return False, f"ORIGIN {origin} is not an unconsumed packet in PROME's own inbox"
    if not _match("PROME/inbox/processed/**", dest):
        return False, f"DEST {dest} is not under PROME/inbox/processed/ — a move elsewhere is not consumption"
    if Path(origin).name != Path(dest).name:
        return False, f"basename changed ({Path(origin).name} → {Path(dest).name}) — not a pure consume-move"
    if origin not in listed or dest not in listed:
        return False, "both halves of the pair must be in the --paths candidate list (the origin's disappearance and the destination's appearance are one fact)"
    if not ref:
        if os.path.lexists(ROOT / origin):
            return False, f"ORIGIN {origin} is still present in the working tree (file or link) — a copy, not a move"
        if os.path.islink(ROOT / dest):
            return False, f"DEST {dest} is a symlink — git would ship the link text, not the packet"
        if git("diff", "--name-only", "--", dest).strip():
            return False, f"DEST {dest} has unstaged changes — the shipped bytes are not the staged bytes"
    ok, why = _git_sees_r100(origin, dest, ref)
    if not ok:
        return False, why
    # the bytes that SHIP: the commit's blob in the --ref form, the INDEX blob otherwise (never the
    # working-tree file — round-2 ❌B); and the working-tree file must still equal the index blob
    now_dest = _committed_content_id(dest, ref) if ref else _index_content_id(dest)
    if now_dest is None:
        return False, f"DEST {dest} is absent {('in ' + ref) if ref else 'from the index'}"
    if not ref and _content_id(dest) != now_dest:
        return False, f"DEST {dest} on disk differs from its index blob — the shipped bytes are not the bytes on disk"
    if origin_sha is None:
        return False, "cannot establish that ORIGIN's bytes are on origin — the fetch/resolve of the remote-tracking ref failed (see the CANNOT-ESTABLISH line above)"
    on_origin, why = _origin_blob_id(origin, origin_sha)
    if on_origin is None:
        return False, f"cannot establish that ORIGIN's bytes are on origin — {why}"
    if on_origin != now_dest:
        return False, (f"DEST bytes differ from `{ORIGIN_FULLREF}@{origin_sha[:9]}:{origin}` "
                       f"({on_origin[:12]} vs {now_dest[:12]}) — not R100; a rename with any content change blocks")
    return True, (f"R100-CONSUMED-MOVE: {origin} → {dest} — git records R100; byte-identical to `{origin}` at "
                  f"{ORIGIN_FULLREF} = {origin_sha[:12]} (fetched this verify; blob {on_origin[:12]}); "
                  f"declared at freeze, manifest REVIEWED (WQ-289 (b), L473)")


def verify_review(paths=None, ref=None):
    """Compare the CURRENT working tree against the recorded review manifest.

    Returns (rc, lines). rc 0 = every reviewed path is byte-identical · rc 1 =
    at least one reviewed path CHANGED, or a path is shipping that was never
    reviewed · rc 2 = CANNOT-EVALUATE (no manifest, unreadable manifest). ⛔ rc 2
    is not a pass: with no manifest nothing was established.
    `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`"""
    f = ROOT / REVIEW_FILE
    explicit = paths is not None     # round-3 reader ❌2: the exemption belongs to the EXPLICIT-list form only
    if not f.exists():
        return 2, [f"CANNOT-EVALUATE: no review manifest at {REVIEW_FILE} — "
                   f"record one with --record-review before the audit"]
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
        reviewed = d["paths"]
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        return 2, [f"CANNOT-EVALUATE: review manifest unreadable ({type(e).__name__}: {e})"]
    cur_base = _current_baseline_sha()
    if d.get("baseline") != cur_base:
        return 2, [f"CANNOT-EVALUATE: this manifest was frozen against baseline "
                   f"{str(d.get('baseline'))[:9]} and the current baseline is {str(cur_base)[:9]} — "
                   f"it belongs to a PRIOR closeout. Re-freeze; do not read it as a failure."]
    out, bad = [], False
    for path, was in sorted(reviewed.items()):
        now = _committed_content_id(path, ref) if ref else _content_id(path)
        if now == was:
            continue
        bad = True
        if was is None:
            out.append(f"CHANGED-SINCE-REVIEW: {path} did not exist at review and does now")
        elif now is None:
            out.append(f"CHANGED-SINCE-REVIEW: {path} was reviewed and is now absent")
        else:
            out.append(f"CHANGED-SINCE-REVIEW: {path} ({was[:12]} → {now[:12]})")
    # An ADDITION nobody reviewed must be visible to EVERY caller, not only to the one that
    # happens to pass a path list. `--mark-reviewed` and the closeout gate both called this
    # with paths=None, so a file created after the freeze passed both and was caught only by
    # the post-commit check. With no list supplied, fall back to the tool's OWN computed
    # scope — the same set the freeze was taken from. (ARGUS, 2026-09-12.)
    scope_failed = None
    if paths is not None and not paths:
        # ⛔ An EMPTY list is not an answer, and it was the WORST of the three: `--paths`
        # OMITTED fell through to discovery and returned rc 1, while `--paths` supplied
        # EMPTY skipped discovery and returned rc 0 over the same unreviewed addition.
        # `nargs="*"` + an unset shell variable in the documented step-10 command is all it
        # took. Passing the flag must never be more dangerous than not passing it.
        scope_failed = ("an EMPTY candidate list was supplied, which establishes nothing. "
                        "Omitting --paths is SAFER than passing it empty (the usual cause is "
                        "an unset shell variable expanding to no arguments)")
    elif paths is None:
        try:
            base, _why = load_baseline()
            if base is None:
                # ⛔ THIS WAS A CARVE-OUT AND THE CARVE-OUT WAS THE SAME BYPASS.
                # I first treated "no baseline" as merely NOT APPLICABLE — content
                # comparison still governing rc — so that four content-only fixtures
                # would pass. But load_baseline() returns None for SEVERAL conditions,
                # not just absence, including a recorded commit git cannot reach.
                # Reproduced with REAL git breakage (.git moved aside), not a mock:
                # the run printed "recorded baseline … is not a commit in this
                # repository", then returned 0, promotion to REVIEWED succeeded, and
                # the Standard review check passed — over an unreviewed addition.
                # AN UNAVAILABLE BASELINE MAKES COMPLETENESS UNKNOWN; IT DOES NOT MAKE
                # COMPLETENESS UNNECESSARY. Printing that additions were unchecked does
                # not protect a caller that accepts rc 0.
                # My own test docstring had written "hiding the second would re-open a
                # quieter version of the same hole" — and then did it.
                scope_failed = f"baseline unusable — {_why}"
            else:
                # ⚠️ `excluded` is DROPPED here and that is a KNOWN, REGISTERED narrowing
                # (DOCKET L367), not an oversight. An independent review called it a bypass:
                # an unreviewed addition at an EXCLUDED path (CLAUDE.md, scripts/**, docs/**)
                # returns 0 from this caller while the explicit-list form returns 1 on the
                # same tree. The DIAGNOSIS is correct. Its proposed fix — append `excluded` —
                # was TESTED HERE AND IS WRONG: `AGENTS/**` is EXCLUDED, so one other desk's
                # dirty STATUS.md then blocks every PROME closeout (reproduced 2026-09-13:
                # "UNREVIEWED: AGENTS/BRENT/STATUS.md"). The real question — what "shipping"
                # means for a path PROME does not own but may commit Will-gated — is a design
                # decision, not a line edit, and is registered rather than guessed at inside a
                # third correction pass on this file.
                lanes, _ = build_scope(base["sha"], load_perimeter(), include_pending=True)
                paths = [e["path"] for e in
                         lanes["OWNED"] + lanes["SHARED"] + lanes["UNATTRIBUTED"]]
        except Exception as e:
            scope_failed = f"{type(e).__name__}: {str(e)[:120]}"
    # ⛔ EXTERNAL FINDING 2026-09-13, and it is the SAME bypass I previously called closed.
    # This block used to end `except Exception: paths = None  # ... stay silent`, so a run
    # whose scope discovery FAILED skipped the unreviewed-additions test entirely and
    # returned 0 — reproduced in a fixture: with git working an unreviewed addition gives
    # rc 1; with scope discovery raising it gives rc 0 AND prints "byte-identical to the
    # frozen candidate (verdict REVIEWED)". Promotion then succeeded and the Standard
    # review check passed. STAYING SILENT IS THE FAIL-OPEN: a completeness claim we could
    # not establish must read CANNOT-EVALUATE, never a pass.
    # `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]`
    if scope_failed is not None:
        out.append("CANNOT-EVALUATE: additions could NOT be checked — "
                   f"{scope_failed}. Completeness is UNKNOWN, which is not the same as "
                   "unnecessary: this run may NOT certify, may NOT authorize REVIEWED, and "
                   "does NOT satisfy a tier that requires a review. The only escape is an "
                   "EXPLICIT, COMPLETE candidate path list via --paths; fix the input "
                   "otherwise. (Content comparison above remains a diagnostic.)")
        return 2, out
    if paths is not None:
        # ⛔ Round-3 reader ❌2: after discovery filled `paths`, this block ALSO ran for the manifest-only
        # form (`--mark-reviewed`, prome_gate) — a network fetch on every declared move, and a
        # contradictory CANNOT-ESTABLISH line beside rc 0 with the remote down. P7 says that form is
        # untouched: the declared block runs ONLY when the caller supplied --paths.
        declared = (d.get("consumed_moves") or {}) if explicit else {}
        if not isinstance(declared, dict) or not all(isinstance(k, str) and isinstance(v, str)
                                                     for k, v in declared.items()):
            return 2, out + ["CANNOT-EVALUATE: manifest `consumed_moves` must be a mapping of DEST → ORIGIN strings"]
        # a declared move exempts BOTH of its paths, and only as a pair: the origin's
        # disappearance is half of the same fact as the destination's appearance
        listed = set(paths)
        origin_sha = None
        if declared:
            origin_sha, why = _fetch_origin_sha()
            if origin_sha is None:
                out.append(f"CANNOT-ESTABLISH origin state for the declared consumed move(s) — {why}; every declared pair is refused")
        origins = list(declared.values())
        dup_origins = {o for o in origins if origins.count(o) > 1}
        exempt = {}
        for dest, origin in declared.items():
            if origin in dup_origins:
                ok, msg = False, f"ORIGIN {origin} is declared against more than one DEST — the second is a copy"
            else:
                ok, msg = _consumed_move_exemption(dest, origin, ref, d, listed, origin_sha)
            if ok:
                exempt[dest] = msg
                exempt[origin] = None   # receipt printed once, on the destination
            else:
                exempt[dest] = False, msg
                exempt[origin] = False, msg
        for path in sorted(set(paths) - set(reviewed) - RECEIPT_PATHS):
            e = exempt.get(path, "undeclared")
            if e is None:
                continue                      # origin half of an exempt pair
            if isinstance(e, str) and e != "undeclared":
                out.append(e)                 # the R100 receipt (P8)
                continue
            bad = True
            if isinstance(e, tuple):
                out.append(f"UNREVIEWED: {path} is in the commit set and was never reviewed — "
                           f"declared consumed move REFUSED: {e[1]}")
            else:
                out.append(f"UNREVIEWED: {path} is in the commit set and was never reviewed")
    if not bad:
        where = f"in {ref}" if ref else "in the working tree"
        out.append(f"{len(reviewed)} path(s) {where} byte-identical to the frozen candidate "
                   f"(verdict {d.get('verdict','?')}, recorded {d.get('recorded_at','?')})")
    return (1 if bad else 0), out


def record_baseline(sha):
    full = git("rev-parse", sha).strip()
    subj = git("log", "-1", "--format=%s", full).strip()
    f = ROOT / BASELINE_FILE
    d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    d.update({"sha": full, "subject": subj,
              "recorded_at": git("log", "-1", "--format=%cI", full).strip(),
              "recorded_by": os.environ.get("PROME_SESSION", "PROME")})
    f.write_text(json.dumps(d, indent=2) + "\n", encoding="utf-8")
    return full, subj


# ---------------------------------------------------------------- the change sets

def porcelain_entries():
    """(status, path) from `git status --porcelain -z -uall`. -uall so a new DIRECTORY is listed as its FILES;
    -z so paths with spaces or non-ASCII survive unquoted."""
    toks = [t for t in git("status", "--porcelain", "-z", "-uall").split("\0") if t]
    out, i = [], 0
    while i < len(toks):
        tok = toks[i]
        if len(tok) < 4:
            i += 1
            continue
        st, path = tok[:2], tok[3:]
        if st[0] in "RC" and i + 1 < len(toks):
            origin = toks[i + 1]
            out.append((" D", origin))      # a rename's ORIGIN disappears; ARGUS must see that
            i += 1
        out.append((st, path))
        i += 1
    return out


def committed_changes(baseline_sha):
    """{path: [shas]} for every path touched since the baseline, whoever committed it (A3)."""
    paths = {}
    for line in git("log", "--format=%H", f"{baseline_sha}..HEAD").splitlines():
        sha = line.strip()
        if not sha:
            continue
        # -z so non-ASCII paths are NOT C-quoted (they are not on the porcelain side either).
        # --no-renames so a `git mv` reports BOTH the deletion of the origin and the addition of the
        # destination. With rename detection on, `--name-only` prints the destination alone and the origin
        # vanishes from the audit — and `git mv` to archive/ is routine PROME closeout work. The pending side
        # already synthesizes the origin; the two sides must agree. (Independent review 2026-09-11, CE-3.)
        for p in [x for x in git("show", "-z", "--no-renames", "--name-only", "--format=", sha).split("\0")
                  if x.strip()]:
            paths.setdefault(p, []).append(sha[:9])
    return paths


def commit_subjects(baseline_sha):
    """{sha9: subject} for every commit in the window — one git call, read once (WQ-417 P3)."""
    out = {}
    for line in git("log", "--format=%H%x09%s", f"{baseline_sha}..HEAD").splitlines():
        if "\t" in line:
            h, subj = line.split("\t", 1)
            out[h[:9]] = subj
    return out


PROME_SUBJECT_RE = re.compile(r"^PROME\b", re.I)                      # 'PROME:', 'PROME ->', 'Prome:' — not PROMETHEUS


def authorship_evidence(entry, subjects):
    """Evidence that PROME wrote a SHARED path: the carve-out ① filename (`from-PROME`) or a window commit whose
    subject starts `PROME`. A list of named evidence strings; empty = UNEVIDENCED. Evidence is a READING hint,
    never a reclassification: the lane stays SHARED and the path stays listed (A4/A5). Coverage test:
    PROME/tools/tests/test_argus_scope_evidence.py (the FALCON inbox/data case 888924d2e, the 10/10 packets)."""
    ev = []
    path = entry["path"]
    base = path.rsplit("/", 1)[-1]
    if re.search(r"from-prome(?![a-z0-9])", base, re.I):        # from-PROME_ / from-PROME. — not from-prometheus
        ev.append("filename carries from-PROME (carve-out ① packet naming)")
    if re.search(r"via-prome(?![a-z0-9])", base, re.I):         # relay naming: PROME is USUALLY the writer, not always (read 2 ⚠️5: 4 desk-written)
        ev.append("filename carries via-PROME (relay naming — PROME is the likely writer; CONFIRM at git log before grading it as PROME's)")
    if re.match(r"^AGENTS/[^/]+/inbox/MSG-PROME-[^/]+\.md$", path):   # Direct Messaging v1 names the sender in the file: MSG-<SENDER>-<date>-<n>__…
        ev.append("top-level inbox MSG-PROME-*.md (Direct Messaging v1 filename names PROME as the sender)")
    for sha in entry.get("committed", []):
        subj = subjects.get(sha, "")
        if PROME_SUBJECT_RE.match(subj):
            ev.append(f"commit {sha} subject '{subj[:70]}'")
    return ev


def sublane(entry, subjects):
    return "SHARED/PROME-EVIDENCED" if authorship_evidence(entry, subjects) else "SHARED/UNEVIDENCED"


def build_scope(baseline_sha, rules, include_pending=True):
    committed = committed_changes(baseline_sha)
    pending = {}
    if include_pending:
        for st, path in porcelain_entries():
            pending.setdefault(path, set()).add(st.strip() or "M")
    lanes = {"OWNED": [], "SHARED": [], "UNATTRIBUTED": []}
    excluded = []
    for path in sorted(set(committed) | set(pending)):
        cls, reason = classify(path, rules)
        entry = {"path": path, "reason": reason,
                 "committed": sorted(committed.get(path, [])),
                 "pending": sorted(pending.get(path, []))}
        if cls == "EXCLUDED":
            excluded.append(entry)
        else:
            lanes[cls].append(entry)
    subjects = commit_subjects(baseline_sha)
    for e in lanes["SHARED"]:
        e["evidence"] = authorship_evidence(e, subjects)
        e["sublane"] = sublane(e, subjects)
    return lanes, excluded


def reads_for(entry):
    r = []
    if entry["committed"]:
        r.append("git diff <baseline>..HEAD -- <path>")
    if entry["pending"]:
        r.append("read the file (new, no committed side)" if entry["pending"] == ["??"]
                 else ("the file is DELETED — read the committed side only" if entry["pending"] == ["D"]
                       else "git diff HEAD -- <path>"))
    return r


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-pending", action="store_true", help="committed only (diagnostic; NOT the closeout form)")
    ap.add_argument("--record-baseline", metavar="SHA", help="record SHA as the audit baseline (at the closeout commit)")
    ap.add_argument("--record-review", action="store_true",
                    help="freeze the content identity of the current scope as the REVIEWED candidate "
                         "(run immediately before the audit)")
    ap.add_argument("--verify-review", action="store_true",
                    help="compare against the frozen candidate; rc 1 = content changed or an unreviewed "
                         "path is shipping, rc 2 = CANNOT-EVALUATE (no manifest / prior closeout)")
    ap.add_argument("--paths", nargs="+", metavar="PATH", default=None,
                    help="with --verify-review: the EXACT intended commit paths, so an addition that was "
                         "never reviewed is detected (without this the check cannot see additions)")
    ap.add_argument("--ref", metavar="REF",
                    help="with --verify-review: verify the contents IN THIS COMMIT (e.g. HEAD) rather than "
                         "the working tree — the actual delivery")
    ap.add_argument("--consumed-move", nargs=2, action="append", metavar=("ORIGIN", "DEST"), default=None,
                    help="with --record-review: DECLARE a byte-identical git mv of PROME's own inbound packet "
                         "into PROME/inbox/processed/ (repeatable). WQ-289 (b): the only path an EXCLUDED "
                         "rename pair can pass --verify-review --paths, and only after ARGUS confirms it "
                         "(manifest REVIEWED); the tool re-checks the bytes against origin/master itself")
    ap.add_argument("--mark-reviewed", metavar="NOTE", nargs="?", const="",
                    help="promote FROZEN -> REVIEWED after the audit actually ran; refuses if the frozen "
                         "candidate changed")
    args = ap.parse_args(argv)
    if args.consumed_move and not args.record_review:
        ap.error("--consumed-move is only meaningful with --record-review (it DECLARES a move at freeze time)")
    if args.consumed_move:
        dests = [d for _o, d in args.consumed_move]
        if len(set(dests)) != len(dests):
            ap.error("the same DEST is declared more than once — one declaration per destination")

    if args.record_baseline:
        sha, subj = record_baseline(args.record_baseline)
        print(f"ARGUS-SCOPE · baseline recorded: {sha[:9]} — {subj[:90]}")
        return 0

    if args.mark_reviewed is not None:
        rc, msg = mark_reviewed(args.mark_reviewed)
        print(f"ARGUS-REVIEW {'✅' if rc == 0 else '🔴' if rc == 1 else '❓'} {msg}")
        return rc

    if args.verify_review:
        rc, lines = verify_review(paths=args.paths, ref=args.ref)
        tag = {0: "\u2705 UNCHANGED", 1: "\U0001f534 CHANGED SINCE REVIEW", 2: "\u2753 CANNOT-EVALUATE"}[rc]
        print(f"ARGUS-REVIEW {tag}")
        for ln in lines:
            print(f"  {ln}")
        return rc

    base, why = load_baseline()
    if base is None:
        print(f"ARGUS-SCOPE 2 — {why}. Do NOT guess a baseline: audit everything since HEAD~50 and say so, or "
              f"record one with --record-baseline <sha>.", file=sys.stderr)
        return 2
    rules = load_perimeter()
    lanes, excluded = build_scope(base["sha"], rules, include_pending=not args.no_pending)

    audited = lanes["OWNED"] + lanes["SHARED"] + lanes["UNATTRIBUTED"]
    total = len(audited)

    if args.record_review:
        moves = {dest: origin for origin, dest in (args.consumed_move or [])}
        entries = record_review([e["path"] for e in audited], consumed_moves=moves)
        for dest, origin in sorted(moves.items()):
            print(f"  \u21b3 declared consumed move: {origin} \u2192 {dest} (ARGUS confirms at the artifact)")
        missing = [p for p, h in entries.items() if h is None]
        print(f"ARGUS-SCOPE \u00b7 review candidate frozen: {len(entries)} path(s) \u2192 {REVIEW_FILE}")
        if missing:
            print(f"  \u26a0\ufe0f {len(missing)} path(s) absent from the working tree at review time: "
                  + ", ".join(missing[:5]))
        print("  \u21b3 after the audit: `--verify-review` must read UNCHANGED before the commit; "
              "any \u274c fix re-freezes it.")
        return 0
    verdict = "SPAWN" if total >= MIN_PATHS else f"SKIP (<{MIN_PATHS} paths)"

    if args.json:
        print(json.dumps({
            "baseline": base["sha"][:9], "baseline_subject": base.get("subject", ""),
            "baseline_source": BASELINE_FILE, "perimeter_source": PERIMETER_FILE,
            "owned": lanes["OWNED"], "shared": lanes["SHARED"], "unattributed": lanes["UNATTRIBUTED"],
            "excluded_count": len(excluded), "path_count": total, "verdict": verdict,
            "shared_prome_evidenced": sum(1 for e in lanes["SHARED"] if e.get("evidence")),
            "lane_meaning": {
                "owned": "PROME's output — audit it",
                "shared": "a shared surface; PROME may NOT have written this. Labelled, never claimed (A5). sublane SHARED/PROME-EVIDENCED = read in full and audit ON the named evidence; SHARED/UNEVIDENCED = list, open only when an OWNED hunk references it (WQ-417 P3)",
                "unattributed": "matched no declared rule. Do NOT audit; report it and ask PROME (A4)"},
        }, indent=1))
    else:
        print(f"ARGUS-SCOPE · baseline {base['sha'][:9]} — {base.get('subject','')[:80]}")
        print(f"  recorded baseline: {BASELINE_FILE} · perimeter: {PERIMETER_FILE}")
        n_ev = sum(1 for e in lanes["SHARED"] if e.get("evidence"))
        print(f"  OWNED {len(lanes['OWNED'])} · SHARED {len(lanes['SHARED'])} (PROME-evidenced {n_ev} · unevidenced {len(lanes['SHARED']) - n_ev}) · "
              f"UNATTRIBUTED {len(lanes['UNATTRIBUTED'])} · excluded {len(excluded)} entries "
              f"(STATES, not unique paths — a path changed both in-commit and pending counts twice; do NOT add this to the shown count) · verdict: {verdict}")
        for lane in ("OWNED", "SHARED", "UNATTRIBUTED"):
            for e in lanes[lane]:
                state = ("committed+PENDING" if e["committed"] and e["pending"]
                         else "committed" if e["committed"] else "PENDING")
                label = e.get("sublane", lane)
                print(f"    - [{label} · {state}] {e['path']}")
                if label == "SHARED/UNEVIDENCED":
                    print("        list only — open it ONLY if an OWNED hunk references it or a declared consumed move names it (WQ-417 P3)")
                else:
                    for r in reads_for(e):
                        print(f"        read: {r}")
                for ev in e.get("evidence", []):
                    print(f"        evidence: {ev}")
                if lane != "OWNED":
                    print(f"        ⚠️ {e['reason']}")
    return 0 if total >= MIN_PATHS else 3


if __name__ == "__main__":
    sys.exit(main())
