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


def finding_lines(out, n=4):
    keys = ("DUE:", "CANNOT", "❌", "🔴", "⏰", "🟠", "STALE", "FINDINGS", "likely YOURS", "over", "NOT ON ORIGIN", "UNKNOWN")
    ls = [l.strip() for l in out.splitlines() if any(k in l for k in keys)]
    return ls[:n]


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
        note = ("fetch FAILED (offline?) — ahead/behind is against the CACHED ref; " if rc != 0 else "")
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

    steps.append(child_step("B4", "read_cap_check --agent DAEDALUS (ADVISORY at boot; BLOCKING at closeout)",
                            [sys.executable, os.path.join(root, "scripts/read_cap_check.py"), "--agent", AGENT], {0: CLEAN, 1: ADVISORY, 2: UNKNOWN}))
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

    steps.append(child_step("C7", "read_cap_check --agent DAEDALUS (BLOCKING at closeout)",
                            [sys.executable, os.path.join(root, "scripts/read_cap_check.py"), "--agent", AGENT], {0: CLEAN, 1: BLOCKING, 2: UNKNOWN}))
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


# ---------------------------------------------------------------- runner
def run(mode, steps, ctx, receipt_dir, log_row=True):
    root = ctx["root"]
    os.makedirs(os.path.join(receipt_dir, "logs"), exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    fp, head = fingerprint(root)
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
            print(f"        · {l[:160]}")
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
        print(f"✅ VALID — receipt {r['ts']} {r['mode']} still describes this tree (HEAD {head[:9]})")
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
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("mode", nargs="?", choices=["boot", "closeout", "verify", "verify-receipt"])
    ap.add_argument("receipt", nargs="?", help="verify-receipt: path to a receipt JSON")
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
