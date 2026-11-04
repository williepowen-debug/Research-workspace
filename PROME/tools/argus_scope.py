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
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
import argus_policy as policy

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
                          capture_output=True, check=True).stdout.decode("utf-8")


# ---------------------------------------------------------------- A2: the recorded perimeter

def load_perimeter(path=None):
    return policy.parse_tsv(Path(path or (ROOT / PERIMETER_FILE)).read_bytes())


def _match(pattern, path):
    return policy.compile_policy([(pattern, 'OWNED', 'internal match')]).classify(path)[0] == 'OWNED'


def classify(path, rules):
    return policy.compile_policy(rules).classify(path)


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


def record_review(paths, verdict=FROZEN, consumed_moves=None):
    raise policy.EvaluationError('legacy freeze disabled; use --record-review --contract PLAN for schema 3; authorized review required')


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
    if d.get("schema") == 3:
        d["reviewed_contract_sha256"] = d["contract_sha256"]
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


def verify_review(paths=None, ref=None, snapshot=None):
    try:
        d = json.loads((ROOT / REVIEW_FILE).read_text(encoding='utf-8'))
        if not isinstance(d, dict) or d.get('schema') != 3:
            raise policy.EvaluationError('historical/unsupported manifest; re-freeze schema 3 and obtain authorized review')
        import argus_contract
        return argus_contract.verify(sys.modules[__name__], d, paths, ref, snapshot)
    except Exception as exc:
        return 2, [f'CANNOT-EVALUATE: {type(exc).__name__}: {exc}']


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
            raise policy.EvaluationError("malformed Git porcelain record")
        st, path = tok[:2], tok[3:]
        policy.segments(path)
        if st[0] in "RC" and i + 1 < len(toks):
            origin = toks[i + 1]
            policy.segments(origin)
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
                  if x]:
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


def _current_candidate_review(base_sha):
    f = ROOT / REVIEW_FILE
    if not f.exists():
        return None
    d = json.loads(f.read_text(encoding='utf-8'))
    if not isinstance(d, dict) or d.get('schema') != 3:
        raise policy.EvaluationError('historical/unsupported candidate manifest; explicitly re-freeze schema 3')
    import argus_contract
    argus_contract.validate(sys.modules[__name__], d)
    return d if d.get('candidate') else None


def _main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-pending", action="store_true", help="committed only (diagnostic; NOT the closeout form)")
    ap.add_argument("--record-baseline", metavar="SHA", help="record SHA as the audit baseline (at the closeout commit)")
    ap.add_argument("--record-review", action="store_true",
                    help="freeze the content identity of the current scope as a FROZEN candidate "
                         "(run immediately before the audit)")
    ap.add_argument("--contract", type=Path, help="with --record-review: explicit schema 3 delivery/evidence/observed plan JSON")
    ap.add_argument("--observe", type=Path, help="append attributed unrelated-version classifications; never changes the contract")
    ap.add_argument("--observe-at", help="with --observe: classify inventory at this outgoing/fetched snapshot")
    ap.add_argument("--snapshot", help="with --verify-review --ref: compare relevant content at this outgoing/fetched commit")
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
    ap.add_argument("--deliver-candidate", action="store_true",
                    help="WQ-583: put the REVIEWED candidate's bytes on master as one commit (needs -F); "
                         "never pushes — run --verify-review --ref <printed sha> --paths <printed paths>, then safe-push")
    ap.add_argument("-F", "--message-file", type=Path, help="with --deliver-candidate: the commit message file")
    ap.add_argument("--carry", nargs="+", default=(), metavar="PATH",
                    help="with --deliver-candidate: post-freeze edits deliberately left for the bookkeeping commit")
    ap.add_argument("--mark-reviewed", metavar="NOTE", nargs="?", const="",
                    help="promote FROZEN -> REVIEWED after the audit actually ran; refuses if the frozen "
                         "candidate changed")
    args = ap.parse_args(argv)
    if args.record_review and not args.contract:
        raise policy.EvaluationError('legacy freeze disabled; use --record-review --contract PLAN for schema 3')
    if args.contract and (not args.record_review or args.consumed_move):
        raise policy.EvaluationError("--contract requires --record-review; legacy consumed-move declarations are disabled")
    if args.snapshot and (not args.verify_review or not args.ref):
        ap.error("--snapshot requires --verify-review --ref")
    if args.observe_at and not args.observe:
        ap.error("--observe-at requires --observe")
    if args.deliver_candidate and not args.message_file:
        ap.error("--deliver-candidate requires -F <message file>")
    if args.observe or args.contract or args.deliver_candidate:
        import argus_contract
        try:
            sc = sys.modules[__name__]
            if args.deliver_candidate:
                sha, paths = argus_contract.deliver(sc, args.message_file, args.carry)
                print(f"DELIVERED {sha} ({len(paths)} path(s)) — not pushed. Next, from the repo root:")
                print(f"  python3 PROME/tools/argus_scope.py --verify-review --ref {sha} --paths " + " ".join(paths))
                return 0
            if args.observe:
                argus_contract.observe(sc, json.loads(args.observe.read_text()), args.observe_at)
                print("ARGUS inventory classifications appended; review contract unchanged")
            else:
                d = argus_contract.freeze(sc, json.loads(args.contract.read_text()))
                c = d['contract']
                print(f"ARGUS contract FROZEN: {d['contract_sha256']}; {len(d['paths'])} delivered paths; "
                      f"candidate {d['candidate']['sha'][:9]} ({argus_contract.CANDIDATE_REF}, on no branch); "
                      f"{len(c['mechanical_moves'])} mechanical move(s); {len(c['reused'])} reused review(s); "
                      f"changed portion {len(d['paths']) - len(c['reused'])}")
                for path, rec in sorted(d['foreign_at_freeze'].items()):   # WQ-583: a PROME file in a shared folder
                    print(f"  FOREIGN at freeze (NOT delivered — name it in `delivered` if it is PROME's, e.g. the "
                          f"daily memory file): {path} [{rec['lane']}]")
            return 0
        except (ValueError, KeyError, TypeError, OSError, RuntimeError, subprocess.CalledProcessError) as exc:
            print(f"CANNOT-EVALUATE: {exc}")
            return 2
    if args.consumed_move:
        raise policy.EvaluationError('legacy consumed-move declarations disabled; use explicit schema 3 contract')

    if args.record_baseline:
        sha, subj = record_baseline(args.record_baseline)
        print(f"ARGUS-SCOPE · baseline recorded: {sha[:9]} — {subj[:90]}")
        return 0

    if args.mark_reviewed is not None:
        rc, msg = mark_reviewed(args.mark_reviewed)
        print(f"ARGUS-REVIEW {'✅' if rc == 0 else '🔴' if rc == 1 else '❓'} {msg}")
        return rc

    if args.verify_review:
        rc, lines = verify_review(paths=args.paths, ref=args.ref, snapshot=args.snapshot)
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
    rev = _current_candidate_review(base["sha"])   # WQ-583: the frozen candidate, if this baseline has one
    cand9 = moves = reused = None
    if rev:
        c = rev["contract"]
        cand9, moves, reused = rev["candidate"]["sha"][:9], c.get("mechanical_moves", {}), c.get("reused", {})
        legs = set(moves) | {r["origin"] for r in moves.values()}
        for lane in lanes:
            lanes[lane] = [e for e in lanes[lane] if e["path"] not in legs]
            for e in lanes[lane]:
                if e["path"] in c["delivered"]:
                    e["candidate_read"] = f"git diff {base['sha'][:9]}..{cand9} -- <path>   (the reviewed candidate)"
                if e["path"] in reused:
                    e["reused"] = reused[e["path"]]

    audited = lanes["OWNED"] + lanes["SHARED"] + lanes["UNATTRIBUTED"]
    total = len(audited)

    verdict = "SPAWN" if total >= MIN_PATHS else f"SKIP (<{MIN_PATHS} paths)"

    if args.json:
        print(json.dumps({
            "baseline": base["sha"][:9], "baseline_subject": base.get("subject", ""),
            "baseline_source": BASELINE_FILE, "perimeter_source": PERIMETER_FILE,
            "owned": lanes["OWNED"], "shared": lanes["SHARED"], "unattributed": lanes["UNATTRIBUTED"],
            "excluded_count": len(excluded), "path_count": total, "verdict": verdict,
            "candidate": cand9, "mechanical_moves": moves or {}, "reused": sorted(reused or {}),
            "shared_prome_evidenced": sum(1 for e in lanes["SHARED"] if e.get("evidence")),
            "lane_meaning": {
                "owned": "PROME's output — audit it",
                "shared": "a shared surface; PROME may NOT have written this. Labelled, never claimed (A5). sublane SHARED/PROME-EVIDENCED = read in full and audit ON the named evidence; SHARED/UNEVIDENCED = list, open only when an OWNED hunk references it (WQ-417 P3)",
                "unattributed": "matched no declared rule. Do NOT audit; report it and ask PROME (A4)"},
        }, indent=1))
    else:
        print(f"ARGUS-SCOPE · baseline {base['sha'][:9]} — {base.get('subject','')[:80]}")
        print(f"  recorded baseline: {BASELINE_FILE} · perimeter: {PERIMETER_FILE}")
        if cand9:
            print(f"  CANDIDATE {cand9} (WQ-583) — the reviewed bytes, on no branch: read every path marked 'candidate' "
                  f"from it, never the working tree (post-freeze bookkeeping lives there) · mechanical moves "
                  f"{len(moves)} (byte-identical pairs the tool verified — not audited) · reused {len(reused)} "
                  f"(this exact version already reviewed — audit only claims ABOUT it in other files)")
            for dest, r in sorted(moves.items()):
                print(f"    = MECHANICAL MOVE {r['origin']} -> {dest}")
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
                if e.get("reused"):
                    src = e["reused"].get("receipt") or f"contract {e['reused'].get('contract', '')[:12]}"
                    print(f"        REUSED review (exact version; {e['reused']['source']}: {src}) — do not re-audit its content")
                elif e.get("candidate_read"):
                    print(f"        read: {e['candidate_read']}")
                elif label == "SHARED/UNEVIDENCED":
                    print("        list only — open it ONLY if an OWNED hunk references it or a declared consumed move names it (WQ-417 P3)")
                else:
                    for r in reads_for(e):
                        print(f"        read: {r}")
                for ev in e.get("evidence", []):
                    print(f"        evidence: {ev}")
                if lane != "OWNED":
                    print(f"        ⚠️ {e['reason']}")
    return 0 if total >= MIN_PATHS else 3


def main(argv=None):
    try:
        return _main(argv)
    except Exception as exc:
        print(f'CANNOT-EVALUATE: {type(exc).__name__}: {exc}')
        return 2


if __name__ == "__main__":
    sys.exit(main())
