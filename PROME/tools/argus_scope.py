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
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


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


def record_review(paths, verdict=FROZEN):
    """Freeze the identity of the candidate.

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
        blob = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=ROOT,
                              capture_output=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None
    return hashlib.sha256(blob).hexdigest()


def verify_review(paths=None, ref=None):
    """Compare the CURRENT working tree against the recorded review manifest.

    Returns (rc, lines). rc 0 = every reviewed path is byte-identical · rc 1 =
    at least one reviewed path CHANGED, or a path is shipping that was never
    reviewed · rc 2 = CANNOT-EVALUATE (no manifest, unreadable manifest). ⛔ rc 2
    is not a pass: with no manifest nothing was established.
    `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`"""
    f = ROOT / REVIEW_FILE
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
    if paths is None:
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
        for path in sorted(set(paths) - set(reviewed) - RECEIPT_PATHS):
            bad = True
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
    ap.add_argument("--paths", nargs="*", metavar="PATH", default=None,
                    help="with --verify-review: the EXACT intended commit paths, so an addition that was "
                         "never reviewed is detected (without this the check cannot see additions)")
    ap.add_argument("--ref", metavar="REF",
                    help="with --verify-review: verify the contents IN THIS COMMIT (e.g. HEAD) rather than "
                         "the working tree — the actual delivery")
    ap.add_argument("--mark-reviewed", metavar="NOTE", nargs="?", const="",
                    help="promote FROZEN -> REVIEWED after the audit actually ran; refuses if the frozen "
                         "candidate changed")
    args = ap.parse_args(argv)

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
        entries = record_review([e["path"] for e in audited])
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
            "lane_meaning": {
                "owned": "PROME's output — audit it",
                "shared": "a shared surface; PROME may NOT have written this. Labelled, never claimed (A5)",
                "unattributed": "matched no declared rule. Do NOT audit; report it and ask PROME (A4)"},
        }, indent=1))
    else:
        print(f"ARGUS-SCOPE · baseline {base['sha'][:9]} — {base.get('subject','')[:80]}")
        print(f"  recorded baseline: {BASELINE_FILE} · perimeter: {PERIMETER_FILE}")
        print(f"  OWNED {len(lanes['OWNED'])} · SHARED {len(lanes['SHARED'])} · "
              f"UNATTRIBUTED {len(lanes['UNATTRIBUTED'])} · excluded {len(excluded)} entries "
              f"(STATES, not unique paths — a path changed both in-commit and pending counts twice; do NOT add this to the shown count) · verdict: {verdict}")
        for lane in ("OWNED", "SHARED", "UNATTRIBUTED"):
            for e in lanes[lane]:
                state = ("committed+PENDING" if e["committed"] and e["pending"]
                         else "committed" if e["committed"] else "PENDING")
                print(f"    - [{lane} · {state}] {e['path']}")
                for r in reads_for(e):
                    print(f"        read: {r}")
                if lane != "OWNED":
                    print(f"        ⚠️ {e['reason']}")
    return 0 if total >= MIN_PATHS else 3


if __name__ == "__main__":
    sys.exit(main())
