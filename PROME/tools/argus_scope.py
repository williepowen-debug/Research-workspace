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
    return d, ""


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
        # -z + --name-only so non-ASCII paths are NOT C-quoted (they are on the porcelain side either)
        for p in [x for x in git("show", "-z", "--name-only", "--format=", sha).split("\0") if x.strip()]:
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
    args = ap.parse_args(argv)

    if args.record_baseline:
        sha, subj = record_baseline(args.record_baseline)
        print(f"ARGUS-SCOPE · baseline recorded: {sha[:9]} — {subj[:90]}")
        return 0

    base, why = load_baseline()
    if base is None:
        print(f"ARGUS-SCOPE 2 — {why}. Do NOT guess a baseline: audit everything since HEAD~50 and say so, or "
              f"record one with --record-baseline <sha>.", file=sys.stderr)
        return 2
    rules = load_perimeter()
    lanes, excluded = build_scope(base["sha"], rules, include_pending=not args.no_pending)

    audited = lanes["OWNED"] + lanes["SHARED"] + lanes["UNATTRIBUTED"]
    total = len(audited)
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
              f"UNATTRIBUTED {len(lanes['UNATTRIBUTED'])} · excluded {len(excluded)} · verdict: {verdict}")
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
