#!/usr/bin/env python3
"""daedalus_gate.py — thin runner over DAEDALUS's EXISTING boot / closeout / post-push checks.

Spec + acceptance set (written first): design/2026-09-17_DAEDALUS_GATE_SPEC.md.
Authority: Will "approved go ahead" 2026-09-17 on CATO 87776263a step 2.

It ORCHESTRATES. Each child runs as a direct subprocess (list argv, no shell, no pipe —
CHECK_STANDARD §14(b)), its NATIVE rc is kept, and rc → class uses THAT child's own
documented contract. It never commits, pushes, regenerates or rotates. It writes only:
  · a receipt JSON + per-step logs in the receipt dir (scratchpad; not committed)
  · one appended row in AGENTS/DAEDALUS/runs/GATE_LOG.tsv (the committed trace)

Classes (kept distinct — DUE is neither clean nor failed):
  CLEAN · DUE · ADVISORY · BLOCKING · UNKNOWN · NOT-APPLICABLE · ENUMERATED · DECLARED
Overall rc: 2 if any UNKNOWN (dominates, §9) · else 1 if any BLOCKING · else 0.

Usage (cwd-proof):
  python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py boot
  python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py closeout \
      (--no-superseded | --superseded OLD NEW [--superseded OLD NEW ...]) \
      (--no-memory | --slug NAME [--slug NAME ...]) --rule-declared <path|none>
  python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py verify --subject "<commit subject>"
  python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py verify-receipt <receipt.json>
  python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py candidate-verify <v2-receipt> --review <review.json> [--commit <full-id> [--delivery]]
  # closeout --candidate <scope.json> opts into v2 (spec section7). Legacy VALID is identity only.
  python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py --selftest

PRODUCTION ACCEPTANCE SET (§3e — real cases, re-run at every version; record runs/2026-09-17_DAEDALUS_GATE_BUILD.md):
  defective: `boot` on 2026-09-17 evening — sweeps_due rc 2 (profile_clock CANNOT-EVALUATE HENRY/HOMER/OSPREY) → UNKNOWN row, rc 2
  clean:     `corrections_boot_check DAEDALUS` rc 0 and `read_cap_check --agent DAEDALUS` rc 0 the same evening → CLEAN rows
  blocking:  `complete_check.py --since 2026-08-17` (range holds pairing violation 383051aeb) → BLOCKING row
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.abspath(__file__)
AGENT = "DAEDALUS"
AGENT_DIR = "AGENTS/DAEDALUS"
TIMEOUT = 180

CLEAN, DUE, ADVISORY, BLOCKING, UNKNOWN, NA, ENUM, DECL = (
    "CLEAN", "DUE", "ADVISORY", "BLOCKING", "UNKNOWN", "NOT-APPLICABLE", "ENUMERATED", "DECLARED")
GLYPH = {CLEAN: "✅", DUE: "⏰", ADVISORY: "ℹ️ ", BLOCKING: "❌", UNKNOWN: "❓", NA: "—", ENUM: "·", DECL: "✍️ "}


def repo_root():
    try:
        return subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


def sh(args, cwd, timeout=TIMEOUT):
    """Direct subprocess: returns (rc, combined output). rc None = not runnable / timeout."""
    try:
        p = subprocess.run(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True, timeout=timeout)
        return p.returncode, p.stdout
    except FileNotFoundError as e:
        return None, f"child not runnable: {e}"
    except subprocess.TimeoutExpired:
        return None, f"child timed out after {timeout}s"
    except Exception as e:  # noqa: BLE001
        return None, f"child failed to start: {e!r}"


def fingerprint(root):
    """sha256 over HEAD + diff of own dir & scripts/ + untracked list in own dir + this file."""
    h = hashlib.sha256()
    rc, head = sh(["git", "rev-parse", "HEAD"], root)
    if rc != 0:
        return None, "HEAD unreadable"
    h.update(head.encode())
    rc, diff = sh(["git", "diff", "HEAD", "--", AGENT_DIR, "scripts"], root)
    if rc != 0:
        return None, "diff unreadable"
    h.update(diff.encode())
    rc, unt = sh(["git", "ls-files", "--others", "--exclude-standard", "--", AGENT_DIR], root)
    if rc != 0:
        return None, "untracked list unreadable"
    for line in sorted(unt.split()):
        h.update(line.encode())
        try:
            with open(os.path.join(root, line), "rb") as f:
                h.update(hashlib.sha256(f.read()).digest())
        except OSError:
            h.update(b"<unreadable>")
    with open(SELF, "rb") as f:
        h.update(hashlib.sha256(f.read()).digest())
    return h.hexdigest(), head.strip()


# ---------------------------------------------------------------- step primitives
class Step:
    def __init__(self, sid, name, fn):
        self.sid, self.name, self.fn = sid, name, fn


def child_step(sid, name, argv, rc_map, cwd_rel="."):
    """rc_map: {0: class, 1: class, 2: class}; None/other rc → UNKNOWN."""
    def run(ctx):
        rc, out = sh(argv, os.path.join(ctx["root"], cwd_rel))
        if rc is None:
            return UNKNOWN, f"{out}", out, rc
        cls = rc_map.get(rc, UNKNOWN)
        reason = {CLEAN: "child rc 0", DUE: "child rc %d = owed work per its contract" % rc,
                  ADVISORY: "child rc %d = advisory per its contract" % rc,
                  BLOCKING: "child rc %d = defect per its contract" % rc,
                  UNKNOWN: "child rc %r = cannot-certify / outside its contract" % rc}[cls]
        return cls, reason, out, rc
    return Step(sid, name, run), argv


def read_cap_step(sid, name, argv, rc_map):
    """Native rc is unchanged; the producer's separate rotation obligation is DUE."""
    step, argv = child_step(sid, name, argv, rc_map)
    child = step.fn

    def run(ctx):
        cls, reason, out, rc = child(ctx)
        if rc != 0:
            return cls, reason, out, rc
        lines = [line for line in out.splitlines() if line.startswith("READ-CAP-RESULT")]
        try:
            if len(lines) != 1 or not lines[0].startswith("READ-CAP-RESULT v1 "):
                raise ValueError("expected one v1 result")
            if lines[0] != out.rstrip().splitlines()[-1]:
                raise ValueError("result is not the final line")
            pairs = [part.split("=", 1) for part in lines[0].split()[2:]]
            fields = dict(pairs)
            if len(fields) != len(pairs):
                raise ValueError("duplicate result key")
            if any(fields.get(k) != v for k, v in
                   {"mode": "agent", "desk": AGENT, "rc": "0", "assessed": "1"}.items()):
                raise ValueError("result mode/desk/rc/assessment mismatch")
            if not re.fullmatch(r"[0-9]+", fields.get("rotation_due", "")):
                raise ValueError("missing or invalid rotation_due")
            rotation = int(fields["rotation_due"])
        except (ValueError, TypeError) as exc:
            return UNKNOWN, f"child rc 0; read-cap result cannot certify: {exc}", out, rc
        if rotation:
            return DUE, f"child rc 0; rotation_due={rotation} — maintenance owed (see paths below)", out, rc
        return cls, reason, out, rc

    step.fn = run
    return step, argv


def finding_lines(out, n=4):
    """Keep all warning blocks; n bounds secondary context, never required actions."""
    keys = ("DUE:", "CANNOT", "❌", "🔴", "⏰", "🟠", "🟡", "⚠", "⛔",
            "STALE", "FINDINGS", "likely YOURS", "NOT ON ORIGIN", "UNKNOWN")
    warnings, context, results = [], [], []
    warning_indent = None
    for raw in out.splitlines():
        line = raw.strip()
        indent = len(raw) - len(raw.lstrip())
        if line.startswith("READ-CAP-RESULT"):
            results.append(line)
            warning_indent = None
        elif any(k in line for k in keys):
            warnings.append(line)
            # A deeper marked continuation does not start a new block: subsequent
            # unmarked actions may be siblings at that same deeper indentation.
            warning_indent = indent if warning_indent is None else min(warning_indent, indent)
        elif line and warning_indent is not None and (indent > warning_indent or line.startswith("↳")):
            warnings.append(line)
        elif line:
            warning_indent = None
            if "over" in line:
                context.append(line)
    return list(dict.fromkeys(warnings + context[:n] + results))


# ---------------------------------------------------------------- registries
def boot_registry(ctx):
    root = ctx["root"]
    steps = []

    def git_state(ctx):
        rc, f = sh(["git", "fetch", "-q", "origin"], root, timeout=60)
        rc2, ab = sh(["git", "rev-list", "--left-right", "--count", "HEAD...origin/master"], root)
        rc3, st = sh(["git", "status", "--porcelain"], root)
        if rc2 != 0 or rc3 != 0:
            return UNKNOWN, "git state unreadable", f + ab + st, None
        outside = [l for l in st.splitlines() if l[3:] and not l[3:].startswith(AGENT_DIR + "/")]
        error = f.strip() or f"no diagnostic output (rc={rc!r})"
        note = (f"fetch FAILED: {error} — ahead/behind is against the CACHED ref; " if rc != 0 else "")
        note += f"ahead/behind {ab.strip().replace(chr(9), '/')} · dirty outside own dir: {len(outside)}"
        if outside:
            note += " ⛔ do NOT pull (root 'Before pulling' 2)"
        return (UNKNOWN if rc != 0 else ENUM), note, f + ab + st, rc
    steps.append((Step("B0", "git state (fetch · ahead/behind · dirty outside own dir)", git_state), ["git", "fetch/rev-list/status"]))

    steps.append(child_step("B1", "sweeps_due (cadence · profile clocks · SELF-ROW · DIRECTORY-STALE)",
                            [sys.executable, os.path.join(HERE, "sweeps_due.py")], {0: CLEAN, 1: DUE, 2: UNKNOWN}))
    steps.append(child_step("B2", "corrections_boot_check DAEDALUS",
                            [sys.executable, os.path.join(root, "scripts/corrections_boot_check.py"), AGENT], {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}))

    def inbox(ctx):
        d = os.path.join(root, AGENT_DIR, "inbox")
        if not os.path.isdir(d):
            return UNKNOWN, "inbox/ directory ABSENT — cannot enumerate (positive control failed)", "", None
        top = sorted(f for f in os.listdir(d) if f.endswith(".md"))
        sub = {}
        for s in sorted(os.listdir(d)):
            p = os.path.join(d, s)
            if os.path.isdir(p) and s != "processed":
                sub[s] = sorted(f for f in os.listdir(p) if f.endswith(".md"))
        n = len(top) + sum(len(v) for v in sub.values())
        detail = "\n".join(["inbox/" + f for f in top] + [f"inbox/{k}/{f}" for k, v in sub.items() for f in v])
        return ENUM, f"{n} packet(s) to read whole (SPAWN 3b) — positive control: dir listed, {len(sub)} subdir(s)", detail, 0
    steps.append((Step("B3", "inbox enumerate", inbox), ["listdir", "inbox/"]))

    steps.append(read_cap_step("B4", "read_cap_check --agent DAEDALUS (rotation DUE; rc1 ADVISORY at boot)",
                            [sys.executable, os.path.join(root, "scripts/read_cap_check.py"), "--agent", AGENT, "--charter-mode", "explicit"], {0: CLEAN, 1: ADVISORY, 2: UNKNOWN}))
    # B5 (2026-10-01): the DOCKET -> DAEDALUS hop. Four rows assigned 9/28-9/29 never reached STATUS
    # because no boot step read the DOCKET for rows naming DAEDALUS (record runs/2026-10-01_DOCKET_OWED_BUILD.md).
    steps.append(child_step("B5", "docket_owed (open DOCKET rows naming DAEDALUS, uncited in STATUS)",
                            [sys.executable, os.path.join(HERE, "docket_owed.py")], {0: CLEAN, 1: DUE, 2: UNKNOWN}))
    return steps


def closeout_registry(ctx):
    root = ctx["root"]
    a = ctx["args"]
    steps = []
    steps.append(child_step("C0", "sweeps_due (SELF-ROW · DIRECTORY-STALE · cadence)",
                            [sys.executable, os.path.join(HERE, "sweeps_due.py")], {0: CLEAN, 1: DUE, 2: UNKNOWN}))

    def orphan(ctx):
        rc, out = sh(["bash", os.path.join(root, "scripts/orphan_check.sh"), AGENT], root)
        if rc is None:
            return UNKNOWN, out, out, rc
        if rc != 0:
            return UNKNOWN, f"orphan_check rc {rc} — its contract is always-0; nonzero = broke", out, rc
        mine = [l for l in out.splitlines() if "likely YOURS" in l]
        if mine:
            return DUE, f"{len(mine)} self-authored packet(s) uncommitted — commit them (carve-out ①)", out, rc
        return CLEAN, "no [likely YOURS] orphan (advisory tool, rc always 0; class keyed on its marker)", out, rc
    steps.append((Step("C1", "orphan_check DAEDALUS", orphan), ["bash", "scripts/orphan_check.sh", AGENT]))

    def consumer(ctx):
        if a.no_superseded:
            return NA, "declared: no figure superseded this session (--no-superseded)", "", None
        if not a.superseded:
            return UNKNOWN, "UNDECLARED — pass --no-superseded or --superseded OLD NEW", "", None
        worst, outs = CLEAN, []
        for old, new in a.superseded:
            for extra in ([], ["--self"]):
                argv = [sys.executable, os.path.join(root, "scripts/consumer_check.py"), "--agent", AGENT, "--old", old, "--new", new] + extra
                rc, out = sh(argv, root)
                outs.append(f"$ {' '.join(argv[1:])}\n{out}")
                if rc is None or rc == 2:
                    return UNKNOWN, f"consumer_check unrunnable/cannot-certify on {old}->{new}", "\n".join(outs), rc
                if rc == 1 or "🔴" in out:
                    worst = DUE
        return worst, ("🔴 STALE owner(s) — packets owed, never edit their files" if worst == DUE else "no stale consumer of the superseded figure(s)"), "\n".join(outs), 0
    steps.append((Step("C2", "consumer_check (declaration-gated)", consumer), ["python3", "scripts/consumer_check.py", "--agent", AGENT, "--old/--new", "…"]))

    steps.append(child_step("C3", "ledger_staleness --nudge DAEDALUS",
                            [sys.executable, os.path.join(root, "scripts/ledger_staleness.py"), "--nudge", AGENT], {0: CLEAN, 1: DUE, 2: UNKNOWN}))

    def memory(ctx):
        outs, cls, reason = [], CLEAN, []
        if a.no_memory:
            reason.append("index-check N/A: declared no auto-memory written (--no-memory)")
        elif not a.slug:
            return UNKNOWN, "UNDECLARED — pass --no-memory or --slug NAME per memory written", "", None
        else:
            for s in a.slug:
                rc, out = sh([sys.executable, os.path.join(root, "scripts/memory_index_check.py"), "--strict", "--slug", s], root)
                outs.append(out)
                if rc is None or rc == 2:
                    return UNKNOWN, f"memory_index_check cannot-certify on {s}", "\n".join(outs), rc
                if rc == 1:
                    cls = BLOCKING
                    reason.append(f"slug {s}: index/file mismatch — commit the file or fix the ignore rule")
        rc, out = sh(["bash", os.path.join(root, "scripts/check_memory_length.sh")], root)
        outs.append(out)
        if rc is None:
            return UNKNOWN, "check_memory_length not runnable", "\n".join(outs), rc
        if rc in (1, 2) and cls != BLOCKING:
            cls = DUE
            reason.append(f"MEMORY.md length rc {rc} — FLAG PROME, never compact it yourself")
        if not reason:
            reason.append("index-check clean" if a.slug else "")
            reason.append("MEMORY.md length ok")
        return cls, "; ".join(r for r in reason if r), "\n".join(outs), rc
    steps.append((Step("C4", "memory (index-check per slug · length cap)", memory), ["python3", "scripts/memory_index_check.py", "--strict", "--slug", "…", "&&", "bash", "scripts/check_memory_length.sh"]))

    def claims(ctx):
        cands = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md", f"{AGENT_DIR}/STATUS.md",
                 f"{AGENT_DIR}/workbook/CATALYSTS.tsv", f"{AGENT_DIR}/CALENDAR.md"]
        paths = [p for p in cands if os.path.exists(os.path.join(root, p))]
        rc, out = sh([sys.executable, os.path.join(root, "scripts/claim_check.py"), "--check", "weekday"] + paths, root)
        if rc is None or rc == 2:
            return UNKNOWN, out if rc is None else "claim_check rc 2 usage/environment", out, rc
        return (ADVISORY if rc == 1 else CLEAN), (f"weekday flags — LOOK, never find-replace ({len(paths)} paths)" if rc == 1 else f"no weekday mismatch in {len(paths)} paths"), out, rc
    steps.append((Step("C5", "claim_check --check weekday", claims), ["python3", "scripts/claim_check.py", "--check", "weekday", "<existing paths>"]))

    def hot_conservation(ctx):
        try:
            hot = open(os.path.join(root, AGENT_DIR, "PATTERNS_HOT.md"), encoding="utf-8").read(3000)
            tsv = open(os.path.join(root, AGENT_DIR, "PATTERNS.tsv"), encoding="utf-8").read()
        except OSError as e:
            return UNKNOWN, f"cannot read PATTERNS surfaces: {e}", "", None
        m = re.search(r"Generated (\d{4}-\d{2}-\d{2}) · (\d+) hot \+ (\d+) cold = (\d+) rows", hot)
        if not m:
            return UNKNOWN, "PATTERNS_HOT.md carries no parseable 'Generated … = N rows' line", hot[:300], None
        data_rows = sum(1 for l in tsv.splitlines() if re.match(r"PAT-\d+[a-z]?\t", l))
        gen_total = int(m.group(4))
        if data_rows != gen_total:
            return BLOCKING, f"PATTERNS.tsv has {data_rows} rows, hot index generated for {gen_total} — run scripts/regen_patterns_hot.py", "", None
        return CLEAN, f"conservation holds: {data_rows} rows == {m.group(2)}+{m.group(3)} (generated {m.group(1)}); NOT checked: whether a row's TEXT changed since generation", "", 0
    steps.append((Step("C6", "PATTERNS_HOT conservation (read-only)", hot_conservation), ["compare", "PATTERNS_HOT.md", "vs", "PATTERNS.tsv"]))

    steps.append(read_cap_step("C7", "read_cap_check --agent DAEDALUS (rotation DUE; rc1 BLOCKING at closeout)",
                            [sys.executable, os.path.join(root, "scripts/read_cap_check.py"), "--agent", AGENT, "--charter-mode", "explicit"], {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}))
    cc = [sys.executable, os.path.join(HERE, "complete_check.py")] + (["--since", a.complete_since] if getattr(a, "complete_since", None) else [])
    steps.append(child_step("C8", "complete_check (pairing · pair-symmetry · EVOLUTION placement · claim walk-list)", cc, {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}))

    def status_stamp(ctx):
        try:
            t = open(os.path.join(root, AGENT_DIR, "STATUS.md"), encoding="utf-8").read()
        except OSError as e:
            return UNKNOWN, f"STATUS.md unreadable: {e}", "", None
        today = ctx["today"]
        hdr = re.search(r"Last Updated:\s*(\d{4}-\d{2}-\d{2})", t)
        bl = t.split("## BOTTOM LINE", 1)[1] if "## BOTTOM LINE" in t else ""
        probs = []
        if not hdr or hdr.group(1) != today:
            probs.append(f"header 'Last Updated' is {hdr.group(1) if hdr else 'ABSENT'}, not {today}")
        if today not in bl:
            probs.append("BOTTOM LINE carries no today-dated stamp (charter: update every session)")
        if probs:
            return DUE, "; ".join(probs), "", None
        return CLEAN, "header and BOTTOM LINE both stamped today", "", 0
    steps.append((Step("C9", "STATUS stamped today (header + BOTTOM LINE)", status_stamp), ["grep", "STATUS.md"]))

    def rule_decl(ctx):
        if a.rule_declared is None:
            return UNKNOWN, "UNDECLARED — pass --rule-declared <path>|none (SPAWN 9: apply a declared rule to its own artifact)", "", None
        if a.rule_declared.lower() == "none":
            return DECL, "operator declares: no rule declared or amended this session", "", None
        return DECL, f"operator declares a rule was declared/amended at {a.rule_declared} — RE-READ it before closing (not machine-checked)", "", None
    steps.append((Step("C10", "rule-declared-this-session (judgment, DECLARED only)", rule_decl), ["declaration"]))
    return steps


def verify_registry(ctx):
    root = ctx["root"]
    subj = ctx["args"].subject
    steps = []
    steps.append(child_step("V1", "verify_push.sh <subject>", ["bash", os.path.join(HERE, "verify_push.sh"), subj], {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}))

    def content(ctx):
        rc, f = sh(["git", "fetch", "-q", "origin"], root, timeout=60)
        if rc != 0:
            return UNKNOWN, "fetch failed — cannot compare against a fresh origin/master", f, rc
        rc, sha = sh(["git", "log", "origin/master", "-1", "--fixed-strings", f"--grep={subj}", "--format=%H"], root)
        sha = sha.strip()
        if rc != 0 or not sha:
            return UNKNOWN, "no commit on origin/master with that subject (V1 covers presence; nothing to compare)", "", rc
        rc, paths = sh(["git", "show", "--name-only", "--format=", sha], root)
        paths = [p for p in paths.split("\n") if p.strip()]
        diff, missing = [], []
        for p in paths:
            r1, o = sh(["git", "show", f"origin/master:{p}"], root)
            r2, h = sh(["git", "show", f"HEAD:{p}"], root)
            if r1 != 0 or r2 != 0:
                missing.append(p)
                continue
            if hashlib.sha256(o.encode()).hexdigest() != hashlib.sha256(h.encode()).hexdigest():
                diff.append(p)
        if missing:
            return UNKNOWN, f"{len(missing)} path(s) unreadable on one side: {missing[:3]}", "", None
        if diff:
            return BLOCKING, f"origin/master ≠ HEAD on {len(diff)} path(s) of commit {sha[:9]}: {diff[:3]} — pushed or overtaken?", "", None
        return CLEAN, f"{len(paths)} path(s) of {sha[:9]} byte-identical origin/master vs HEAD", "", 0
    steps.append((Step("V2", "content check: located commit's paths origin/master vs HEAD", content), ["git", "show", "origin/master:<p>", "vs", "HEAD:<p>"]))
    return steps


# ---------------------------------------------------------------- bounded candidate receipts (v2)
CANDIDATE_LOG = AGENT_DIR + "/runs/GATE_LOG.tsv"
CANDIDATE_STEPS = {f"C{i}" for i in range(11)}
MAINTENANCE_UNKNOWN = {"C0", "C3"}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def exact_path(path):
    if (not isinstance(path, str) or not path or path.startswith(("/", "-")) or
            any(x in path for x in ("\\", "\x00", "\n", "\r", "*", "?", "[")) or
            any(x in ("", ".", "..", ".git") for x in path.split("/"))):
        raise ValueError(f"not an exact repository path: {path!r}")
    return path


def raw_git(root, *args):
    p = subprocess.run(["git", "--literal-pathspecs", *args], cwd=root,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    if p.returncode:
        raise ValueError(f"git {args[0]} failed (rc {p.returncode})")
    return p.stdout


def object_id(root, ref):
    if not isinstance(ref, str) or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", ref):
        raise ValueError("commit must be a full immutable object ID")
    if raw_git(root, "rev-parse", "--verify", ref + "^{commit}").decode().strip() != ref:
        raise ValueError("not an exact commit")
    return ref


def image_bytes(data, mode):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "mode": mode}


def work_image(root, path):
    import stat
    exact_path(path)
    # Never traverse directory symlinks, including dangling links.
    here = root
    for part in path.split("/")[:-1]:
        here = os.path.join(here, part)
        if os.path.islink(here):
            raise ValueError(f"directory symlink traversal: {path}")
    p = os.path.join(root, path)
    try:
        st = os.lstat(p)
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(st.st_mode):
        return image_bytes(os.fsencode(os.readlink(p)), "120000")
    if not stat.S_ISREG(st.st_mode):
        raise ValueError(f"unsupported file type: {path}")
    with open(p, "rb") as stream:
        return image_bytes(stream.read(), "100755" if st.st_mode & 0o111 else "100644")


def tree_image(root, commit, path):
    exact_path(path)
    entries = raw_git(root, "ls-tree", "-z", commit, "--", path).split(b"\0")
    entries = [x for x in entries if x]
    if not entries:
        return None
    if len(entries) != 1:
        raise ValueError("ambiguous tree entry")
    meta, actual = entries[0].split(b"\t", 1)
    mode, kind, oid = meta.decode().split()
    if actual != os.fsencode(path) or kind != "blob" or mode not in ("100644", "100755", "120000"):
        raise ValueError(f"unsupported tree entry: {path}")
    return image_bytes(raw_git(root, "cat-file", "blob", oid), mode)


def validate_scope(scope, step_ids):
    if scope.get("schema") != 1 or type(scope.get("review_required")) is not bool or not scope.get("review_policy"):
        raise ValueError("scope requires schema1, review_required boolean and review_policy")
    sets = []
    for name in ("candidates", "bookkeeping", "separate"):
        rows = scope[name]
        paths = [exact_path(row["path"]) for row in rows]
        if len(set(paths)) != len(paths) or any(not row.get("reason") for row in rows):
            raise ValueError(f"duplicate paths or missing reason: {name}")
        sets.append(set(paths))
    if not sets[0] or any(sets[i] & sets[j] for i in range(3) for j in range(i)):
        raise ValueError("empty candidate set or overlapping classifications")
    if sets[1] != {CANDIDATE_LOG}:
        raise ValueError("only exact runner GATE_LOG bookkeeping exclusion is supported; declare it")
    deps = scope["dependencies"]
    if set(deps) != set(step_ids):
        raise ValueError("dependencies must name every registry step exactly once")
    for sid, dep in deps.items():
        if not dep.get("completeness"):
            raise ValueError(f"missing dependency completeness declaration: {sid}")
        for path in dep.get("paths", []) + dep.get("optional_paths", []):
            exact_path(path)
            if path in sets[1]:
                raise ValueError("bookkeeping cannot also be a check dependency")
        for item in dep.get("context", []):
            if item.get("basis") not in ("current", "historical") or not item.get("reason"):
                raise ValueError("context requires basis and reason")
    return scope


def context_value(root, item):
    import platform
    import time
    kind = item["kind"]
    if kind == "day":
        return {"day": dt.date.today().isoformat(), "timezone": list(time.tzname),
                "offset": time.timezone, "TZ": os.environ.get("TZ")}
    if kind == "runtime":
        return {"python": sys.executable, "version": sys.version, "platform": platform.platform(), "cwd": root,
                "environment_sha256": {k: digest(os.environ.get(k)) for k in
                                       ("PATH", "LANG", "LC_ALL", "LC_TIME", "TZ", "PYTHONPATH", "PYTHONHASHSEED")}}
    paths = [exact_path(p) for p in item["paths"]]
    if not paths:
        raise ValueError("history/status context needs exact nonempty paths")
    if kind == "history":
        out = raw_git(root, "log", "--format=%H", "--", *paths)
    elif kind == "status":
        out = raw_git(root, "status", "--porcelain=v1", "--untracked-files=all", "--", *paths)
    else:
        raise ValueError(f"unsupported context {kind}")
    return image_bytes(out, "query")


def candidate_snapshot(root, scope, scope_path, base, historical=None, invocation=None):
    import glob
    result = {"invocation": invocation or {}, "candidates": {}, "dependencies": {}, "runner": image_bytes(open(SELF, "rb").read(), "source"),
              "scope": image_bytes(open(scope_path, "rb").read(), "source")}
    for row in scope["candidates"]:
        path = row["path"]
        old, new = tree_image(root, base, path), work_image(root, path)
        if old is None and new is None:
            raise ValueError(f"candidate absent both at base and working tree: {path}")
        result["candidates"][path] = {"before": old, "after": new}
    for sid, dep in scope["dependencies"].items():
        if dep.get("limitations"):
            raise ValueError(f"unsupported dependency context for {sid}: {dep['limitations']}")
        images, members, contexts = {}, {}, []
        for path in dep.get("paths", []) + dep.get("optional_paths", []):
            value = work_image(root, path)
            if value is None and path not in dep.get("optional_paths", []):
                raise ValueError(f"missing required input {sid}: {path}")
            images[path] = value
        for pattern in dep.get("globs", []):
            # Globs are dependency inventories only; no escaping the repository.
            if not isinstance(pattern, str) or pattern.startswith("/") or any(p in ("..", ".git", "") for p in pattern.split("/")):
                raise ValueError("unsafe dependency glob")
            paths = sorted(os.path.relpath(p, root) for p in glob.glob(os.path.join(root, pattern), recursive=True))
            members[pattern] = paths
            for path in paths:
                if path == CANDIDATE_LOG:
                    raise ValueError("dependency inventory includes excluded log")
                images[path] = work_image(root, path)
        for i, item in enumerate(dep.get("context", [])):
            if historical is not None and item["basis"] == "historical":
                value = historical["dependencies"][sid]["context"][i]
            else:
                value = context_value(root, item)
            contexts.append(value)
        result["dependencies"][sid] = {"paths": images, "members": members, "context": contexts}
    return result


def scope_inventory(root, scope, extra=()):
    # Path lists are NUL separated: no whitespace/rename heuristics.
    changed = raw_git(root, "diff", "--name-only", "-z", "HEAD", "--", AGENT_DIR)
    added = raw_git(root, "ls-files", "--others", "--exclude-standard", "-z", "--", AGENT_DIR)
    actual = {os.fsdecode(p) for p in (changed + added).split(b"\0") if p}
    known = {r["path"] for key in ("candidates", "bookkeeping", "separate") for r in scope[key]} | set(extra)
    missing = actual - known
    if missing:
        raise ValueError(f"unclassified own paths: {sorted(missing)}")


def start_candidate(root, path, step_ids, receipt_dir, invocation=None):
    scope_path = os.path.abspath(path)
    # The mechanism must not create excluded-by-directory files inside its subject.
    if os.path.commonpath([os.path.realpath(root), os.path.realpath(receipt_dir)]) == os.path.realpath(root):
        raise ValueError("candidate receipt-dir must be outside the repository")
    scope = validate_scope(json.load(open(scope_path, encoding="utf-8")), step_ids)
    base = raw_git(root, "rev-parse", "HEAD").decode().strip()
    scope_inventory(root, scope)
    before = candidate_snapshot(root, scope, scope_path, base, invocation=invocation)
    return {"scope": scope, "scope_path": scope_path, "base": base, "before": before,
            "boundary_sha256": digest({"scope": scope, "before": before}), "errors": []}


def finish_candidate(root, candidate):
    try:
        candidate["after"] = candidate_snapshot(root, candidate["scope"], candidate["scope_path"], candidate["base"], invocation=candidate["before"]["invocation"])
        scope_inventory(root, candidate["scope"])
        if candidate["after"] != candidate["before"]:
            candidate["errors"].append("candidate/dependency/context changed during checks")
    except (OSError, ValueError, KeyError, IndexError, AttributeError, TypeError, subprocess.SubprocessError) as e:
        candidate["after"] = None
        candidate["errors"].append(str(e))


def candidate_assess(receipt, root, review_path=None, commit=None, delivery=False):
    """Evidence dimensions, not a new authority or whole-closeout grade."""
    out = {"identity": UNKNOWN, "checks": UNKNOWN, "review": UNKNOWN,
           "commit": UNKNOWN if commit else "NOT-REQUESTED", "delivery": UNKNOWN if delivery else "NOT-REQUESTED", "issues": []}
    states = []
    try:
        if receipt.get("version") != 2 or receipt.get("mode") != "closeout":
            raise ValueError("requires a v2 closeout receipt; legacy identity is not acceptance")
        c = receipt["candidate"]
        scope = validate_scope(c["scope"], CANDIDATE_STEPS)
        rows = receipt["steps"]
        if len(rows) != 11 or {r["id"] for r in rows} != CANDIDATE_STEPS or any(r["class"] not in GLYPH or not r.get("reason") or "rc" not in r for r in rows):
            raise ValueError("incomplete/malformed registry results")
        out["checks"] = {"rows": rows, "blocking": [r["id"] for r in rows if r["class"] == BLOCKING],
                         "unknown": [r["id"] for r in rows if r["class"] == UNKNOWN],
                         "due": [r["id"] for r in rows if r["class"] == DUE]}
        states += [BLOCKING for r in rows if r["class"] == BLOCKING]
        states += [UNKNOWN for r in rows if r["class"] == UNKNOWN and r["id"] not in MAINTENANCE_UNKNOWN]
        if c["errors"] or c["after"] != c["before"]:
            raise ValueError(f"run never established stable boundary: {c['errors']}")
        if c["boundary_sha256"] != digest({"scope": scope, "before": c["before"]}):
            raise ValueError("corrupt boundary digest")
        current = candidate_snapshot(root, scope, c["scope_path"], c["base"], historical=c["before"], invocation=c["before"]["invocation"])
        out["identity"] = CLEAN if current == c["before"] else BLOCKING
        states.append(out["identity"])
        out["historical_context"] = {sid: [x for x in dep.get("context", []) if x["basis"] == "historical"]
                                      for sid, dep in scope["dependencies"].items()}
        evidence = {}
        if review_path:
            review_rel = exact_path(os.path.relpath(os.path.abspath(review_path), root))
            review = json.load(open(review_path, encoding="utf-8"))
            if review.get("schema") != 1 or review.get("boundary_sha256") != c["boundary_sha256"] or not review.get("policy"):
                raise ValueError("review schema/boundary/policy missing or stale")
            evidence[review_rel] = work_image(root, review_rel)
            if evidence[review_rel] is None or evidence[review_rel]["mode"] not in ("100644", "100755"):
                raise ValueError("review attestation must be a regular file")
            if review["status"] == "EXEMPT":
                ok = not scope["review_required"] and not review.get("reports")
            else:
                ok = review["status"] == "ACCEPTED" and bool(review.get("reviewer")) and bool(review.get("reports"))
            for report in review.get("reports", []):
                p = exact_path(report["path"])
                im = work_image(root, p)
                if not im or im["mode"] not in ("100644", "100755") or im["sha256"] != report["sha256"]:
                    ok = False
                evidence[p] = im
            if set(evidence) & ({r["path"] for r in scope["bookkeeping"]} | set(c["before"]["candidates"])):
                raise ValueError("review evidence overlaps candidate/bookkeeping (circular boundary)")
            out["review"] = CLEAN if ok else UNKNOWN
            out["review_limits"] = review.get("limitations", [])
        states.append(out["review"])
        scope_inventory(root, scope, evidence)
        if commit:
            object_id(root, commit)
            parents = raw_git(root, "rev-list", "--parents", "-n", "1", commit).decode().split()[1:]
            if len(parents) != 1:
                raise ValueError("only single-parent commits supported")
            parent = parents[0]
            delta = {os.fsdecode(p) for p in raw_git(root, "diff-tree", "--no-commit-id", "--name-only", "--no-renames", "-z", "-r", commit).split(b"\0") if p}
            expected = {p for p, pair in c["before"]["candidates"].items() if pair["before"] != pair["after"]}
            allowed = expected | set(evidence) | {CANDIDATE_LOG}
            mismatch = sorted((delta - allowed) | (expected - delta))
            for p, pair in c["before"]["candidates"].items():
                if tree_image(root, parent, p) != pair["before"] or tree_image(root, commit, p) != pair["after"]:
                    mismatch.append(p)
            for p, im in evidence.items():
                if im is None or tree_image(root, commit, p) != im:
                    mismatch.append(p)
            out["commit"] = BLOCKING if mismatch else CLEAN
            out["commit_id"] = commit
            out["commit_mismatches"] = sorted(set(mismatch))
            states.append(out["commit"])
        if delivery:
            if not commit:
                raise ValueError("delivery requires --commit")
            raw_git(root, "fetch", "-q", "origin")
            origin = raw_git(root, "rev-parse", "--verify", "refs/remotes/origin/master^{commit}").decode().strip()
            p = subprocess.run(["git", "merge-base", "--is-ancestor", commit, origin], cwd=root, capture_output=True, timeout=60)
            out["delivery"] = {0: CLEAN, 1: BLOCKING}.get(p.returncode, UNKNOWN)
            out["origin"] = origin
            states.append(out["delivery"])
    except (OSError, ValueError, KeyError, IndexError, TypeError, AttributeError, subprocess.SubprocessError) as e:
        out["issues"].append(str(e))
        states.append(UNKNOWN)
    debt = isinstance(out["checks"], dict) and any(r["class"] in (DUE, UNKNOWN, ADVISORY) for r in out["checks"]["rows"])
    out["eligibility"] = UNKNOWN if UNKNOWN in states else BLOCKING if BLOCKING in states else "WITH-DEBT" if debt else CLEAN
    out["rc"] = 2 if UNKNOWN in states else 1 if BLOCKING in states else 0
    out["perimeter"] = "Declared evidence only; no authority, honest-reading proof, transient change/revert guarantee, consumer acceptance or whole-sweep completion."
    return out


def verify_candidate(path, root, review=None, commit=None, delivery=False):
    try:
        result = candidate_assess(json.load(open(path, encoding="utf-8")), root, review, commit, delivery)
    except (OSError, ValueError, TypeError) as e:
        result = {"eligibility": UNKNOWN, "rc": 2, "issues": [str(e)]}
    print(json.dumps(result, indent=2))
    return result["rc"]


# ---------------------------------------------------------------- runner
def run(mode, steps, ctx, receipt_dir, log_row=True):
    root = ctx["root"]
    os.makedirs(os.path.join(receipt_dir, "logs"), exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ" if getattr(ctx.get("args"), "candidate", None) else "%Y%m%dT%H%M%SZ")
    fp, head = fingerprint(root)
    candidate = None
    if getattr(ctx.get("args"), "candidate", None):
        try:
            invocation = {k: getattr(ctx["args"], k, None) for k in
                          ("no_superseded", "superseded", "no_memory", "slug", "rule_declared", "complete_since")}
            invocation["today"] = ctx["today"]
            candidate = start_candidate(root, ctx["args"].candidate, [s.sid for s, _ in steps], receipt_dir, invocation)
        except (OSError, ValueError, KeyError, IndexError, AttributeError, TypeError, subprocess.SubprocessError) as e:
            print(f"CANDIDATE UNKNOWN: {e}")
            return 2
    results = []
    print(f"GATE {mode} — {AGENT} · {stamp} · HEAD {head[:9] if head else '?'}")
    for step, argv in steps:
        cls, reason, out, rc = step.fn(ctx)
        logp = os.path.join(receipt_dir, "logs", f"{stamp}_{step.sid}.txt")
        with open(logp, "w", encoding="utf-8") as f:
            f.write(f"$ {' '.join(map(str, argv))}\nrc={rc}\n\n{out}")
        fl = finding_lines(out)
        results.append({"id": step.sid, "name": step.name, "cmd": [str(x) for x in argv], "rc": rc,
                        "class": cls, "reason": reason, "log": logp, "findings": fl})
        print(f"  {GLYPH[cls]} {step.sid:<3} {cls:<15} {step.name}\n      ↳ {reason}")
        for l in fl:
            print(f"        · {l}")
    counts = {}
    for r in results:
        counts[r["class"]] = counts.get(r["class"], 0) + 1
    rc = 2 if counts.get(UNKNOWN) else (1 if counts.get(BLOCKING) else 0)
    judg = [r["id"] for r in results if r["class"] in (DECL, ENUM)]
    checked = [r["id"] for r in results if r["class"] not in (DECL, ENUM)]
    perim = (f"GATE {mode} rc={rc} · checked: {len(checked)} steps {checked} · NOT checked (declared/enumerated only): {judg} · "
             f"proves nothing about: completion of work beyond complete_check's legs, owner consumption of packets, "
             f"the truth of any DECLARED value, or anything a child's own PASS line disclaims.")
    receipt = {"mode": mode, "agent": AGENT, "ts": stamp, "head": head, "fingerprint": fp,
               "runner_sha256": hashlib.sha256(open(SELF, "rb").read()).hexdigest(),
               "steps": results, "counts": counts, "rc": rc, "perimeter": perim}
    if candidate is not None:
        finish_candidate(root, candidate)
        receipt.update(version=2, candidate=candidate)
        if candidate["errors"]:
            rc = receipt["rc"] = 2
            print("CANDIDATE UNKNOWN: " + "; ".join(candidate["errors"]))
        print("Candidate boundary: " + candidate["boundary_sha256"] + " (review/commit not yet verified)")
    rp = os.path.join(receipt_dir, f"{stamp}_{mode}.json")
    with open(rp, "w", encoding="utf-8") as f:
        json.dump(receipt, f, indent=1)
    rsha = hashlib.sha256(open(rp, "rb").read()).hexdigest()[:8]
    summary = " · ".join(f"{k} {v}" for k, v in sorted(counts.items()))
    print(f"\n{perim}\n  counts: {summary}\n  receipt: {rp} (sha {rsha}) — fingerprint {'unavailable' if fp is None else fp[:12]}")
    if fp is None:
        print("  ❓ fingerprint unavailable (git unreadable) — receipt cannot be re-verified; rc raised to 2")
        rc = 2
    if log_row:
        lp = os.path.join(root, AGENT_DIR, "runs", "GATE_LOG.tsv")
        new = not os.path.exists(lp)
        with open(lp, "a", encoding="utf-8") as f:
            if new:
                f.write("date_utc\tmode\thead\trc\tcounts\treceipt_sha8\n")
            f.write(f"{stamp}\t{mode}\t{head[:9] if head else '?'}\t{rc}\t{summary}\t{rsha}\n")
        print(f"  logged: {lp} (the only tree write this runner makes)")
    return rc


def verify_receipt(path, root=None):
    try:
        r = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"❓ CANNOT-CERTIFY: receipt unreadable ({e})")
        return 2
    root = root or repo_root()
    if not root:
        print("❓ CANNOT-CERTIFY: not in a git repo")
        return 2
    fp, head = fingerprint(root)
    if fp is None:
        print("❓ CANNOT-CERTIFY: fingerprint unavailable now")
        return 2
    if r.get("fingerprint") is None:
        print("❓ receipt carries no fingerprint — it was never re-verifiable")
        return 2
    if fp == r["fingerprint"]:
        print(f"✅ VALID — receipt {r['ts']} {r['mode']} still matches this fingerprint (HEAD {head[:9]}); IDENTITY ONLY, checks/review may have failed")
        return 0
    why = []
    if head != r.get("head"):
        why.append(f"HEAD moved {str(r.get('head'))[:9]} → {head[:9]}")
    if r.get("runner_sha256") != hashlib.sha256(open(SELF, "rb").read()).hexdigest():
        why.append("runner changed")
    if not why:
        why.append("tree changed (own dir / scripts diff or untracked set)")
    print(f"❌ INVALIDATED — {'; '.join(why)}. Re-run the gate; do not cite this receipt.")
    return 1


# ---------------------------------------------------------------- candidate acceptance (independent fixture contribution)
def candidate_selftest():
    """Independent DC7 acceptance fixtures; only disposable repositories are mutated."""
    import contextlib
    import copy
    import io
    from types import SimpleNamespace
    from unittest.mock import patch
    import datetime as datetime_module
    failures, passed = [], []

    def check(ok, detail):
        if not ok:
            raise AssertionError(detail)

    def command(repo, *args):
        return subprocess.run(["git", "-C", repo, *args], check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode().strip()

    class Fixture:
        def __init__(self, td):
            self.td, self.root = td, os.path.join(td, "repo")
            os.makedirs(self.root)
            command(self.root, "init", "-q", "-b", "master")
            command(self.root, "config", "user.email", "fixture@example.invalid")
            command(self.root, "config", "user.name", "fixture")
            self.own, self.external = AGENT_DIR + "/output.md", "AGENTS/OTHER/inbox/DAEDALUS.md"
            self.dep = "deps/input.txt"
            self.put(self.own, "old\n")
            self.put(self.external, "old packet\n")
            self.put(self.dep, "input\n")
            self.put(CANDIDATE_LOG, "existing bookkeeping\n")
            self.commit_all("base")
            self.put(self.own, "new\n")
            self.put(self.external, "new packet\n")
            self.scope_path, self.receipt_dir = os.path.join(td, "scope.json"), os.path.join(td, "receipts")
            self.scope = {"schema": 1, "candidates": [{"path": p, "reason": "authored output"} for p in (self.own, self.external)],
                          "bookkeeping": [{"path": CANDIDATE_LOG, "reason": "runner bookkeeping only"}], "separate": [],
                          "review_required": True, "review_policy": "fixture independent review",
                          "dependencies": {f"C{i}": {"paths": [self.dep], "optional_paths": [], "globs": [], "context": [],
                                                        "completeness": "all synthetic check inputs"} for i in range(11)}}
            self.review_path = os.path.join(self.root, "review.json")
            self.report_path = "review.md"
            self.receipt = None

        def put(self, path, text):
            full = os.path.join(self.root, path)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as stream:
                stream.write(text)

        def commit_all(self, message):
            command(self.root, "add", "-A")
            command(self.root, "commit", "-q", "-m", message)
            return command(self.root, "rev-parse", "HEAD")

        def capture(self, finish=True):
            with open(self.scope_path, "w") as stream:
                json.dump(self.scope, stream)
            candidate = start_candidate(self.root, self.scope_path, CANDIDATE_STEPS, self.receipt_dir)
            if finish:
                finish_candidate(self.root, candidate)
            self.receipt = {"version": 2, "mode": "closeout", "candidate": candidate,
                            "steps": [{"id": f"C{i}", "class": CLEAN, "reason": "synthetic success", "rc": 0} for i in range(11)]}
            return self.receipt

        def review(self, **changes):
            self.put(self.report_path, "Independent fixture review of the exact boundary.\n")
            review = {"schema": 1, "boundary_sha256": self.receipt["candidate"]["boundary_sha256"],
                      "status": "ACCEPTED", "reviewer": "independent fixture", "policy": "fixture policy",
                      "reports": [{"path": self.report_path, "sha256": work_image(self.root, self.report_path)["sha256"]}],
                      "limitations": []}
            review.update(changes)
            with open(self.review_path, "w") as stream:
                json.dump(review, stream)

        def assess(self, **kwargs):
            return candidate_assess(self.receipt, self.root, self.review_path, **kwargs)

        def ready(self):
            self.capture()
            self.review()
            return self

    def case(name, fn):
        try:
            with tempfile.TemporaryDirectory(prefix="daedalus-v2-selftest-") as td:
                fn(Fixture(td))
            passed.append(name)
            print("  PASS candidate: " + name)
        except Exception as exc:
            failures.append(name + ": " + str(exc))
            print("  FAIL candidate: " + failures[-1])

    def stable(f):
        f.ready()
        out = f.assess()
        check(out["rc"] == 0 and out["identity"] == CLEAN and out["review"] == CLEAN, out)
        f.put(CANDIDATE_LOG, "bookkeeping changed\n")
        check(f.assess()["rc"] == 0, "exact bookkeeping exclusion invalidated boundary")
    case("stable boundary and bookkeeping write", stable)

    def changed(f, path):
        f.ready()
        f.put(path(f), "changed after checks\n")
        out = f.assess()
        check(out["identity"] == BLOCKING and out["rc"] == 1, out)
    case("authored external packet changed after checks", lambda f: changed(f, lambda x: x.external))
    case("substantive own output changed after checks", lambda f: changed(f, lambda x: x.own))
    case("required dependency changed after checks", lambda f: changed(f, lambda x: x.dep))

    def during(f):
        f.capture(finish=False)
        f.put(f.external, "changed during checks\n")
        finish_candidate(f.root, f.receipt["candidate"])
        f.put(f.external, "new packet\n")
        f.review()
        out = f.assess()
        check(out["rc"] == 2 and bool(f.receipt["candidate"]["errors"]), out)
    case("during-check external edit persists as invalid after restoration", during)

    def reverted(f):
        f.capture(finish=False)
        f.put(f.own, "transient\n")
        f.put(f.own, "new\n")
        finish_candidate(f.root, f.receipt["candidate"])
        f.review()
        out = f.assess()
        check(out["rc"] == 0 and "transient change/revert" in out["perimeter"], out)
    case("endpoint-only transient revert limitation disclosed", reverted)

    def outcomes(f, mapping, expected, eligibility):
        f.ready()
        for row in f.receipt["steps"]:
            if row["id"] in mapping:
                row["class"], row["rc"] = mapping[row["id"]], 2 if mapping[row["id"]] == UNKNOWN else 1
        out = f.assess()
        check(out["identity"] == CLEAN and out["rc"] == expected and out["eligibility"] == eligibility, out)
        check(out["checks"]["blocking"] == [sid for sid, cls in mapping.items() if cls == BLOCKING], out)
    case("matching bytes with BLOCKING is not acceptance", lambda f: outcomes(f, {"C1": BLOCKING}, 1, BLOCKING))
    case("mixed required UNKNOWN preserves BLOCKING details", lambda f: outcomes(f, {"C1": BLOCKING, "C2": UNKNOWN}, 2, UNKNOWN))
    case("maintenance UNKNOWN plus BLOCKING remains blocked", lambda f: outcomes(f, {"C0": UNKNOWN, "C1": BLOCKING}, 1, BLOCKING))
    case("DUE and maintenance UNKNOWN stay explicit debt", lambda f: outcomes(f, {"C0": UNKNOWN, "C3": DUE}, 0, "WITH-DEBT"))
    case("required UNKNOWN withholds eligibility", lambda f: outcomes(f, {"C9": UNKNOWN}, 2, UNKNOWN))

    def review_failure(f, kind):
        f.ready()
        if kind == "missing":
            os.unlink(f.review_path)
        elif kind == "changed-report":
            f.put(f.report_path, "changed\n")
        elif kind == "stale":
            f.review(boundary_sha256="0" * 64)
        else:
            f.review(status="QUALIFIED")
        out = f.assess()
        check(out["rc"] == 2 and out["review"] == UNKNOWN, out)
    for kind in ("missing", "changed-report", "stale", "qualified"):
        case("review " + kind + " remains unknown", lambda f, kind=kind: review_failure(f, kind))

    def exemption(f):
        f.scope["review_required"] = False
        f.capture()
        f.review(status="EXEMPT", reports=[])
        check(f.assess()["rc"] == 0, f.assess())
        f.scope["review_required"] = True
        f.capture()
        f.review(status="EXEMPT", reports=[])
        check(f.assess()["rc"] == 2, "required review bypassed by exemption")
    case("review exemption follows explicit scope policy", exemption)

    def malformed(f, kind):
        f.ready()
        r = f.receipt
        if kind == "legacy": r.pop("version")
        elif kind == "missing-row": r["steps"].pop()
        elif kind == "duplicate-row": r["steps"][-1] = copy.deepcopy(r["steps"][0])
        elif kind == "bad-class": r["steps"][0]["class"] = "PASS"
        elif kind == "missing-reason": r["steps"][0].pop("reason")
        elif kind == "digest": r["candidate"]["boundary_sha256"] = "0" * 64
        elif kind == "scope": r["candidate"]["scope"] = []
        out = f.assess()
        check(out["rc"] == 2, out)
    for kind in ("legacy", "missing-row", "duplicate-row", "bad-class", "missing-reason", "digest", "scope"):
        case("malformed receipt " + kind, lambda f, kind=kind: malformed(f, kind))

    def bad_scope(f, kind):
        if kind == "unclassified": f.put(AGENT_DIR + "/unclassified.txt", "new\n")
        elif kind == "excluded-substantive": f.scope["bookkeeping"].append({"path": "runs/output.md", "reason": "pretend bookkeeping"})
        elif kind == "missing-input": f.scope["dependencies"]["C0"]["paths"].append("deps/missing.txt")
        elif kind == "missing-step": del f.scope["dependencies"]["C10"]
        elif kind == "context-limit": f.scope["dependencies"]["C0"]["limitations"] = ["unsupported input"]
        elif kind == "missing-new-candidate": f.scope["candidates"].append({"path": "absent", "reason": "absent"})
        elif kind == "unsafe-path": f.scope["candidates"][0]["path"] = "../escape"
        elif kind == "inside-receipts": f.receipt_dir = os.path.join(f.root, "receipts")
        try:
            f.capture()
        except (ValueError, KeyError, TypeError, OSError, AttributeError):
            return
        raise AssertionError("unsafe/incomplete scope accepted")
    for kind in ("unclassified", "excluded-substantive", "missing-input", "missing-step", "context-limit", "missing-new-candidate", "unsafe-path", "inside-receipts"):
        case("reject scope " + kind, lambda f, kind=kind: bad_scope(f, kind))

    def optional(f):
        f.scope["dependencies"]["C0"]["optional_paths"] = ["deps/optional.txt"]
        f.ready()
        f.put("deps/optional.txt", "new input\n")
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("optional absence becoming present invalidates", optional)

    def members(f):
        f.scope["dependencies"]["C0"]["globs"] = ["deps/*.txt"]
        f.ready()
        f.put("deps/another.txt", "new membership\n")
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("dependency glob membership addition invalidates", members)

    def mode(f):
        f.ready()
        os.chmod(os.path.join(f.root, f.own), 0o755)
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("executable mode drift invalidates", mode)

    def deleted(f):
        os.unlink(os.path.join(f.root, f.own))
        f.ready()
        oid = f.commit_all("delete reviewed candidate")
        check(f.assess(commit=oid)["commit"] == CLEAN, f.assess(commit=oid))
    case("tracked candidate deletion matches actual commit", deleted)

    def rename(f):
        new = AGENT_DIR + "/renamed.md"
        os.rename(os.path.join(f.root, f.own), os.path.join(f.root, new))
        f.scope["candidates"].append({"path": new, "reason": "rename destination"})
        f.ready()
        oid = f.commit_all("rename reviewed candidate")
        check(f.assess(commit=oid)["commit"] == CLEAN, f.assess(commit=oid))
    case("rename binds old deletion and new bytes", rename)

    def symlink(f):
        path = AGENT_DIR + "/link"
        os.symlink("output.md", os.path.join(f.root, path))
        f.scope["candidates"].append({"path": path, "reason": "authored link"})
        f.ready()
        os.unlink(os.path.join(f.root, path))
        os.symlink("different.md", os.path.join(f.root, path))
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("symlink target bytes are bound", symlink)

    def symlink_dir(f):
        os.symlink("deps", os.path.join(f.root, "alias"))
        f.scope["dependencies"]["C0"]["paths"] = ["alias/input.txt"]
        try: f.capture()
        except ValueError: return
        raise AssertionError("directory symlink traversal accepted")
    case("directory symlink traversal rejected", symlink_dir)

    def context_day(f, basis):
        f.scope["dependencies"]["C9"]["context"] = [{"kind": "day", "basis": basis, "reason": "date-sensitive check"}]
        f.ready()
        real = dt.date
        class LaterDate(real):
            @classmethod
            def today(cls): return real.today() + datetime_module.timedelta(days=1)
        with patch.object(dt, "date", LaterDate):
            out = f.assess()
        check(out["identity"] == (BLOCKING if basis == "current" else CLEAN), out)
        if basis == "historical": check(bool(out["historical_context"]["C9"]), out)
    case("current day rollover invalidates", lambda f: context_day(f, "current"))
    case("historical day retained and explicitly disclosed", lambda f: context_day(f, "historical"))

    def history(f):
        f.scope["dependencies"]["C1"]["context"] = [{"kind": "history", "basis": "current", "reason": "history-dependent", "paths": [f.dep]}]
        f.ready()
        f.put(f.dep, "intermediate\n")
        command(f.root, "add", "--", f.dep)
        command(f.root, "commit", "-q", "-m", "intermediate dependency")
        f.put(f.dep, "input\n")
        command(f.root, "add", "--", f.dep)
        command(f.root, "commit", "-q", "-m", "restore dependency")
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("relevant history drift despite identical current bytes", history)

    def commit_good(f):
        f.ready()
        f.put("unrelated.txt", "peer before\n")
        command(f.root, "add", "--", "unrelated.txt")
        command(f.root, "commit", "-q", "-m", "peer before")
        check(f.assess()["identity"] == CLEAN, f.assess())
        oid = f.commit_all("reviewed candidate")
        f.put("unrelated.txt", "peer after\n")
        command(f.root, "add", "--", "unrelated.txt")
        command(f.root, "commit", "-q", "-m", "peer after")
        out = f.assess(commit=oid)
        check(out["rc"] == 0 and out["commit"] == CLEAN and out["commit_id"] == oid, out)
    case("unrelated HEAD before and after exact candidate commit", commit_good)

    def commit_bad(f, kind):
        f.ready()
        if kind == "extra":
            f.put("foreign.txt", "not authorized\n")
            oid = f.commit_all("extra path")
        elif kind == "missing":
            command(f.root, "add", "--", f.own, "review.json", "review.md")
            command(f.root, "commit", "-q", "-m", "omitted external packet")
            oid = command(f.root, "rev-parse", "HEAD")
        elif kind == "staged-bytes":
            f.put(f.own, "wrong staged\n")
            command(f.root, "add", "-A")
            f.put(f.own, "new\n")
            command(f.root, "commit", "-q", "-m", "wrong staged bytes")
            oid = command(f.root, "rev-parse", "HEAD")
        elif kind == "staged-mode":
            command(f.root, "add", "-A")
            command(f.root, "update-index", "--chmod=+x", f.own)
            command(f.root, "commit", "-q", "-m", "wrong staged mode")
            oid = command(f.root, "rev-parse", "HEAD")
        elif kind == "parent-mode":
            command(f.root, "update-index", "--chmod=+x", f.own)
            command(f.root, "commit", "-q", "-m", "intervening candidate mode")
            oid = f.commit_all("reviewed candidate after parent mutation")
        elif kind == "missing-review":
            command(f.root, "add", "--", f.own, f.external)
            command(f.root, "commit", "-q", "-m", "missing review evidence")
            oid = command(f.root, "rev-parse", "HEAD")
        out = f.assess(commit=oid)
        check(out["identity"] == CLEAN and out["commit"] == BLOCKING and out["rc"] == 1, out)
    for kind in ("extra", "missing", "staged-bytes", "staged-mode", "parent-mode", "missing-review"):
        case("actual commit mismatch " + kind, lambda f, kind=kind: commit_bad(f, kind))

    def remote(f, kind):
        f.ready()
        bare = os.path.join(f.td, "origin.git")
        subprocess.run(["git", "init", "-q", "--bare", "-b", "master", bare], check=True, capture_output=True)
        command(f.root, "remote", "add", "origin", bare)
        command(f.root, "push", "-q", "origin", "master")
        oid = f.commit_all("candidate")
        if kind == "advanced":
            command(f.root, "push", "-q", "origin", "master")
            f.put("peer.txt", "advance origin\n")
            command(f.root, "add", "--", "peer.txt")
            command(f.root, "commit", "-q", "-m", "peer advancement")
            command(f.root, "push", "-q", "origin", "master")
        elif kind == "fetch-failed":
            command(f.root, "remote", "set-url", "origin", os.path.join(f.td, "missing.git"))
        out = f.assess(commit=oid, delivery=True)
        expected = {"advanced": 0, "absent": 1, "fetch-failed": 2}[kind]
        check(out["rc"] == expected and out["commit"] == CLEAN, out)
        if kind == "advanced": check(out["delivery"] == CLEAN, out)
        elif kind == "absent": check(out["delivery"] == BLOCKING, out)
    for kind in ("advanced", "absent", "fetch-failed"):
        case("fresh origin " + kind, lambda f, kind=kind: remote(f, kind))

    def real_runner(f, mutate):
        with open(f.scope_path, "w") as stream: json.dump(f.scope, stream)
        def fn(ctx):
            if mutate: f.put(f.external, "during real run\n")
            return CLEAN, "fixture check", "ok", 0
        steps = [(Step(f"C{i}", "synthetic actual runner step", fn if i == 1 else lambda ctx: (CLEAN, "fixture check", "ok", 0)), []) for i in range(11)]
        with contextlib.redirect_stdout(io.StringIO()):
            rc = run("closeout", steps, {"root": f.root, "today": "2026-10-04", "args": SimpleNamespace(candidate=f.scope_path)}, f.receipt_dir)
        receipts = [p for p in os.listdir(f.receipt_dir) if p.endswith(".json")]
        check(len(receipts) == 1, receipts)
        with open(os.path.join(f.receipt_dir, receipts[0])) as stream: f.receipt = json.load(stream)
        if mutate: f.put(f.external, "new packet\n")
        f.review()
        out = f.assess()
        check(rc == (2 if mutate else 0) and out["rc"] == (2 if mutate else 0), out)
        check("closeout" in open(os.path.join(f.root, CANDIDATE_LOG)).read(), "runner did not append log")
    case("real runner own log does not invalidate immediate verification", lambda f: real_runner(f, False))
    case("real runner captures mutation during checks permanently", lambda f: real_runner(f, True))

    def invocation_boundary(f):
        with open(f.scope_path, "w") as stream: json.dump(f.scope, stream)
        steps = [(Step(f"C{i}", "synthetic step", lambda ctx: (CLEAN, "fixture check", "ok", 0)), []) for i in range(11)]
        boundaries = []
        for index, (superseded, slug) in enumerate([([["old-A", "new-A"]], ["memory-A"]), ([["old-B", "new-B"]], ["memory-A"]), ([["old-B", "new-B"]], ["memory-B"]) ]):
            rdir = os.path.join(f.td, "invocation-" + str(index))
            args = SimpleNamespace(candidate=f.scope_path, superseded=superseded, slug=slug)
            with contextlib.redirect_stdout(io.StringIO()):
                rc = run("closeout", steps, {"root": f.root, "today": "2026-10-04", "args": args}, rdir)
            check(rc == 0, "synthetic invocation failed")
            rp = next(p for p in os.listdir(rdir) if p.endswith(".json"))
            with open(os.path.join(rdir, rp)) as stream: receipt = json.load(stream)
            boundaries.append(receipt["candidate"]["boundary_sha256"])
        check(len(set(boundaries)) == 3, "different OLD/NEW or slug declaration reused same boundary")
    case("real runner binds OLD NEW and memory slug declarations", invocation_boundary)

    def malformed_historical_context(f):
        f.scope["dependencies"]["C9"]["context"] = [{"kind": "day", "basis": "historical", "reason": "date-sensitive check"}]
        f.ready()
        c = f.receipt["candidate"]
        c["before"]["dependencies"]["C9"]["context"] = []
        c["after"] = copy.deepcopy(c["before"])
        c["boundary_sha256"] = digest({"scope": c["scope"], "before": c["before"]})
        f.review()
        out = f.assess()
        check(out["rc"] == 2, out)
    case("malformed historical context array returns UNKNOWN", malformed_historical_context)

    def report_symlink(f):
        f.ready()
        f.put("original-report.md", open(os.path.join(f.root, f.report_path)).read())
        os.unlink(os.path.join(f.root, f.report_path))
        os.symlink("original-report.md", os.path.join(f.root, f.report_path))
        with open(f.review_path) as stream: review = json.load(stream)
        review["reports"][0]["sha256"] = work_image(f.root, f.report_path)["sha256"]
        with open(f.review_path, "w") as stream: json.dump(review, stream)
        check(f.assess()["rc"] == 2, f.assess())
    case("review report symlink cannot attest unchecked target bytes", report_symlink)

    def substantive_run_report(f):
        path = AGENT_DIR + "/runs/substantive.md"
        f.put(path, "substantive output\n")
        f.scope["candidates"].append({"path": path, "reason": "substantive report"})
        f.ready()
        f.put(path, "changed substantive output\n")
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("substantive runs report is not a directory-wide exclusion", substantive_run_report)

    def runner_changed(f):
        global SELF
        original = SELF
        copy_path = os.path.join(f.td, "runner-copy.py")
        with open(original, "rb") as source, open(copy_path, "wb") as target: target.write(source.read())
        try:
            SELF = copy_path
            f.ready()
            with open(copy_path, "a") as stream: stream.write("\n# changed runner fixture\n")
            check(f.assess()["identity"] == BLOCKING, f.assess())
        finally:
            SELF = original
    case("running checker source mutation invalidates boundary", runner_changed)

    def new_external(f):
        path = "AGENTS/OTHER/inbox/new-DAEDALUS.md"
        f.put(path, "new untracked packet\n")
        f.scope["candidates"].append({"path": path, "reason": "new authored external packet"})
        f.ready()
        f.put(path, "changed untracked packet\n")
        check(f.assess()["identity"] == BLOCKING, f.assess())
    case("new untracked external candidate change invalidates", new_external)

    def dependency_disappears(f):
        f.ready()
        os.unlink(os.path.join(f.root, f.dep))
        check(f.assess()["rc"] == 2 and f.assess()["identity"] == UNKNOWN, f.assess())
    case("required dependency disappears and remains UNKNOWN", dependency_disappears)

    def during_dependency(f):
        with open(f.scope_path, "w") as stream: json.dump(f.scope, stream)
        def modifies_input(ctx):
            f.put(f.dep, "modified by purported clean checker\n")
            return CLEAN, "claims clean", "CLEAN", 0
        steps = [(Step(f"C{i}", "synthetic step", modifies_input if i == 1 else lambda ctx: (CLEAN, "fixture check", "ok", 0)), []) for i in range(11)]
        with contextlib.redirect_stdout(io.StringIO()):
            rc = run("closeout", steps, {"root": f.root, "today": "2026-10-04", "args": SimpleNamespace(candidate=f.scope_path)}, f.receipt_dir)
        rp = next(p for p in os.listdir(f.receipt_dir) if p.endswith(".json"))
        with open(os.path.join(f.receipt_dir, rp)) as stream: f.receipt = json.load(stream)
        f.put(f.dep, "input\n")
        f.review()
        check(rc == 2 and f.assess()["rc"] == 2, f.assess())
    case("checker printing CLEAN while mutating dependency is rejected", during_dependency)

    def timezone(f):
        f.scope["dependencies"]["C9"]["context"] = [{"kind": "day", "basis": "current", "reason": "timezone-dependent"}]
        f.ready()
        with patch.dict(os.environ, {"TZ": "Fixture/ChangedTimezone"}):
            out = f.assess()
        check(out["identity"] == BLOCKING, out)
    case("declared timezone context changes invalidate current reuse", timezone)

    def conversion(f):
        command(f.root, "config", "core.autocrlf", "true")
        command(f.root, "config", "core.safecrlf", "false")
        with open(os.path.join(f.root, f.own), "wb") as stream: stream.write(b"new\r\n")
        f.ready()
        oid = f.commit_all("Git newline conversion")
        out = f.assess(commit=oid)
        check(out["identity"] == CLEAN and out["commit"] == BLOCKING, out)
    case("Git raw blob conversion rejected against checked bytes", conversion)

    def staged_revert(f):
        f.ready()
        command(f.root, "add", "-A")
        command(f.root, "reset", "-q", "HEAD", "--", f.own)
        command(f.root, "commit", "-q", "-m", "staged revert omits candidate")
        out = f.assess(commit=command(f.root, "rev-parse", "HEAD"))
        check(out["identity"] == CLEAN and out["commit"] == BLOCKING, out)
    case("staged revert rejected despite matching working bytes", staged_revert)

    def unchanged_included(f):
        f.scope["candidates"].append({"path": f.dep, "reason": "included unchanged artifact"})
        f.ready()
        oid = f.commit_all("candidate includes unchanged artifact")
        check(f.assess(commit=oid)["commit"] == CLEAN, f.assess(commit=oid))
    case("unchanged included artifact binds commit tree", unchanged_included)

    def due_only(f):
        outcomes(f, {"C3": DUE}, 0, "WITH-DEBT")
    case("DUE only remains owed with permitted delivery", due_only)

    print("CANDIDATE SELFTEST: %d passed, %d failed" % (len(passed), len(failures)))
    for failure in failures: print("  " + failure)
    return 1 if failures else 0


# ---------------------------------------------------------------- selftest (fixture-driven; never touches real files)
def selftest():
    fails = []
    py = sys.executable
    with tempfile.TemporaryDirectory() as td:
        # a real temp git repo so fingerprint/receipt/verify have something honest to bind to
        repo = os.path.join(td, "repo")
        os.makedirs(os.path.join(repo, AGENT_DIR, "runs"))
        subprocess.run(["git", "init", "-q", "-b", "master", repo], check=True)
        subprocess.run(["git", "-C", repo, "config", "user.email", "t@t"], check=True)
        subprocess.run(["git", "-C", repo, "config", "user.name", "t"], check=True)
        open(os.path.join(repo, AGENT_DIR, "f.txt"), "w").write("a\n")
        subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
        subprocess.run(["git", "-C", repo, "commit", "-q", "-m", "init"], check=True)
        ctx = {"root": repo, "today": "2026-01-01", "args": None}
        fx = lambda code, text: [py, "-c", f"import sys; print({text!r}); sys.exit({code})"]  # noqa: E731
        steps = [
            child_step("T0", "clean child", fx(0, "ok"), {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}),
            child_step("T1", "DUE child (sweeps_due-shaped rc 1)", fx(1, "DUE: x"), {0: CLEAN, 1: DUE, 2: UNKNOWN}),
            child_step("T2", "cannot-certify child", fx(2, "CANNOT-CERTIFY"), {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}),
            child_step("T3", "A5 pipe-proof: prints clean, exits 1", fx(1, "✅ clean"), {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}),
            child_step("T4", "A1 missing child", ["/nonexistent/check.py"], {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}),
        ]
        rdir = os.path.join(td, "rcpt")
        rc = run("selftest", steps, ctx, rdir, log_row=False)
        rp = [f for f in os.listdir(rdir) if f.endswith(".json")][0]
        r = json.load(open(os.path.join(rdir, rp)))
        cls = {s["id"]: s["class"] for s in r["steps"]}
        exp = {"T0": CLEAN, "T1": DUE, "T2": UNKNOWN, "T3": BLOCKING, "T4": UNKNOWN}
        for k, v in exp.items():
            if cls.get(k) != v:
                fails.append(f"{k}: expected {v}, got {cls.get(k)}")
        if rc != 2:
            fails.append(f"overall rc expected 2 (UNKNOWN dominates), got {rc}")
        # DUE must not move rc on its own
        rc_due = run("selftest-due", [steps[0], steps[1]], ctx, rdir, log_row=False)
        if rc_due != 0:
            fails.append(f"A8: DUE-only run should be rc 0, got {rc_due}")
        # A3 receipt binding
        if verify_receipt(os.path.join(rdir, rp), root=repo) != 0:
            fails.append("A3: unchanged tree should verify VALID")
        open(os.path.join(repo, AGENT_DIR, "f.txt"), "a").write("b\n")
        if verify_receipt(os.path.join(rdir, rp), root=repo) != 1:
            fails.append("A3: modified tree should INVALIDATE")
        # A4 declaration gating
        class A:  # noqa: D401
            no_superseded = False; superseded = []; no_memory = False; slug = []; rule_declared = None; complete_since = None
        ctx["args"] = A()
        reg = {s.sid: s for s, _ in closeout_registry(ctx)}
        c2 = reg["C2"].fn(ctx)
        if c2[0] != UNKNOWN or "UNDECLARED" not in c2[1]:
            fails.append(f"A4: undeclared consumer scope should be UNKNOWN/UNDECLARED, got {c2[:2]}")
        A.no_superseded = True
        c2 = reg["C2"].fn(ctx)
        if c2[0] != NA or "declared" not in c2[1]:
            fails.append(f"A4: declared N/A should carry its reason, got {c2[:2]}")
        # A12 content-check divergence: bare origin, push, then diverge origin
        bare = os.path.join(td, "origin.git")
        subprocess.run(["git", "init", "-q", "--bare", "-b", "master", bare], check=True)
        subprocess.run(["git", "-C", repo, "remote", "add", "origin", bare], check=True)
        subprocess.run(["git", "-C", repo, "checkout", "-q", "--", "."], check=True)
        open(os.path.join(repo, AGENT_DIR, "g.txt"), "w").write("g\n")
        subprocess.run(["git", "-C", repo, "add", "-A"], check=True)
        subprocess.run(["git", "-C", repo, "commit", "-q", "-m", "subject-XYZ add g"], check=True)
        subprocess.run(["git", "-C", repo, "push", "-q", "origin", "master"], check=True)

        class V:
            subject = "subject-XYZ"
        ctx["args"] = V()
        vreg = {s.sid: s for s, _ in verify_registry(ctx)}
        ok = vreg["V2"].fn(ctx)
        if ok[0] != CLEAN:
            fails.append(f"A12: identical push should be CLEAN, got {ok[:2]}")
        # diverge origin via a second clone
        clone = os.path.join(td, "clone")
        subprocess.run(["git", "clone", "-q", bare, clone], check=True)
        subprocess.run(["git", "-C", clone, "config", "user.email", "t@t"], check=True)
        subprocess.run(["git", "-C", clone, "config", "user.name", "t"], check=True)
        open(os.path.join(clone, AGENT_DIR, "g.txt"), "w").write("changed\n")
        subprocess.run(["git", "-C", clone, "commit", "-qam", "overtake"], check=True)
        subprocess.run(["git", "-C", clone, "push", "-q", "origin", "master"], check=True)
        bad = vreg["V2"].fn(ctx)
        if bad[0] != BLOCKING:
            fails.append(f"A12: diverged origin should be BLOCKING, got {bad[:2]}")
    # First real run 2026-09-17: the hot-conservation regex missed PAT-074b (letter-suffixed ID) and this
    # selftest verified receipts against the CWD repo, not the fixture — both fixed; PAT-146 in the author's own hand.
    print("\nSELFTEST " + ("PASS — A1 A3 A4 A5 A8 A12 + class map exercised (fixtures; §3e real cases are in the build record)" if not fails else "FAIL:\n  " + "\n  ".join(fails)))
    candidate_rc = candidate_selftest()
    return 1 if fails or candidate_rc else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("mode", nargs="?", choices=["boot", "closeout", "verify", "verify-receipt", "candidate-verify"])
    ap.add_argument("receipt", nargs="?", help="verify-receipt: path to a receipt JSON")
    ap.add_argument("--candidate", help="closeout: explicit schema1 candidate scope JSON")
    ap.add_argument("--review", help="candidate-verify: schema1 independent review attestation")
    ap.add_argument("--commit", help="candidate-verify: full immutable commit ID")
    ap.add_argument("--delivery", action="store_true", help="candidate-verify: fetch origin and verify commit membership")
    ap.add_argument("--subject", help="verify: the commit subject to locate on origin/master")
    ap.add_argument("--superseded", nargs=2, action="append", metavar=("OLD", "NEW"), default=[])
    ap.add_argument("--no-superseded", action="store_true")
    ap.add_argument("--slug", action="append", default=[])
    ap.add_argument("--no-memory", action="store_true")
    ap.add_argument("--rule-declared", help="<path>|none")
    ap.add_argument("--complete-since", help="closeout: pass a range start to complete_check (the §3e BLOCKING drill uses 2026-08-17)")
    ap.add_argument("--receipt-dir", default=os.environ.get("DAEDALUS_GATE_DIR") or os.path.join(tempfile.gettempdir(), "claude-1000", "daedalus-gate"))
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.mode == "verify-receipt":
        if not a.receipt:
            print("❓ CANNOT-CERTIFY: verify-receipt needs a receipt path"); return 2
        return verify_receipt(a.receipt)
    root = repo_root()
    if not root:
        print("❓ CANNOT-CERTIFY: not inside a git repo"); return 2
    if a.mode == "candidate-verify":
        if not a.receipt:
            print("CANDIDATE UNKNOWN: receipt path required"); return 2
        return verify_candidate(a.receipt, root, a.review, a.commit, a.delivery)
    if a.candidate and a.mode != "closeout":
        print("CANDIDATE UNKNOWN: --candidate is closeout-only"); return 2
    ctx = {"root": root, "today": dt.date.today().isoformat(), "args": a}
    if a.mode == "boot":
        return run("boot", boot_registry(ctx), ctx, a.receipt_dir)
    if a.mode == "closeout":
        return run("closeout", closeout_registry(ctx), ctx, a.receipt_dir)
    if a.mode == "verify":
        if not a.subject:
            print("❓ CANNOT-CERTIFY: verify needs --subject"); return 2
        return run("verify", verify_registry(ctx), ctx, a.receipt_dir)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
