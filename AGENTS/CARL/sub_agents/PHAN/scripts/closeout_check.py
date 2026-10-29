#!/usr/bin/env python3
"""
PHAN closeout runner: executes the MECHANICAL closeout steps in CLOSEOUT.md,
reports RAN / FAILED / LOOK per step, then NAMES the judgement steps it cannot
verify.  Modelled on AGENTS/HANS/scripts/closeout_check.py (keep its rules).

WHY THIS EXISTS
---------------
PHAN's closeout was prose only.  On 2026-10-28 a full closeout ran four root
checks that the PHAN checklist never listed (orphan, claim, ledger staleness,
consumer), and a check's exit code was misread from a pager until a fleet hook
caught it.  A checklist with an item omitted does not look like a failure; it
looks like a shorter checklist.  This runner makes a step that did not execute
show up as a gap.

  ⛔ THIS SCRIPT DOES NOT CERTIFY THE CLOSEOUT.
  It certifies that the mechanical steps EXECUTED and what they returned.
  Judgement steps are listed as UNVERIFIED BY DESIGN.

RULES CARRIED FROM HANS (each was learned by the runner lying once):
  - A step passes only if it did not crash AND printed its own completion
    line.  rc alone cannot tell a verdict from a traceback.
  - Signalling exits (consumer/ledger tools exit non-zero to mean "found
    something") are accepted only with the completion line present.

USAGE (from anywhere):
  python3 AGENTS/CARL/sub_agents/PHAN/scripts/closeout_check.py            # before commit
  python3 AGENTS/CARL/sub_agents/PHAN/scripts/closeout_check.py --post     # after safe-push
  options: --memory-slug <slug>      (repeat; runs root 1d memory checks)
           --superseded OLD:NEW[:SERIES]  (repeat; runs root 1c consumer_check)

Exit: 0 every mechanical step ran and passed · 1 a step FAILED or errored.
      LOOK lines never change the exit code; they need a human decision.
"""
import argparse, datetime, re, subprocess, sys
from pathlib import Path

PHAN = Path(__file__).resolve().parent.parent
ROOT = PHAN.parents[3]                       # PHAN -> sub_agents -> CARL -> AGENTS -> repo root
REL = PHAN.relative_to(ROOT).as_posix()      # AGENTS/CARL/sub_agents/PHAN
VENV_PY = ROOT / ".venv/bin/python3"
PY = str(VENV_PY) if VENV_PY.exists() else sys.executable

CAP = 32_550                                 # root read-cap budget (bytes), whole-read surfaces
ROTATE_AT = 0.75                             # rotation trigger = fleet read_cap_check "rotate-tier" (>=75% of budget)
LIVE_LEDGERS = ["COCKROACH.tsv", "REGULATORY.tsv", "PROVIDER.tsv", "PREDICTIONS.tsv"]
TODAY = datetime.date.today().isoformat()


def run(cmd, cwd=ROOT):
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=300)
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError as e:
        return None, f"tool not found: {e}"
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:                   # fail loud, never silent
        return None, f"{type(e).__name__}: {e}"


def crashed(out):
    low = (out or "").lower()
    return any(m in low for m in (
        "traceback (most recent call last)", "modulenotfounderror", "importerror",
        "no such file or directory", "can't open file", "command not found",
        "syntaxerror", "indentationerror", "unrecognized arguments", "usage:"))


class Report:
    def __init__(self):
        self.ran = self.total = 0
        self.failed, self.look = [], []

    def tool(self, label, cmd, codes, expect, show=None):
        """Run an external check. Pass = rc in codes AND no crash AND completion line present."""
        self.total += 1
        rc, out = run(cmd)
        if rc is None:
            print(f"  ⛔ ERROR   {label}\n              {out.splitlines()[0][:90] if out else ''}")
            self.failed.append(label)
            return rc, out
        self.ran += 1
        ok = rc in codes and not crashed(out) and (
            not expect or re.search(expect, out, re.S | re.M | re.I))
        if ok:
            print(f"  ✅ RAN     {label}   rc={rc}")
            lines = [l for l in out.splitlines() if show and re.search(show, l)] if show else out.splitlines()[-1:]
            for ln in lines[:6]:
                print(f"              {ln.strip()[:96]}")
        else:
            print(f"  🔴 FAILED  {label}   rc={rc}")
            for ln in out.splitlines()[-3:]:
                print(f"              {ln[:96]}")
            self.failed.append(label)
        return rc, out

    def local(self, label, ok, lines, look=False):
        """An in-process check. look=True marks a human decision, not a failure."""
        self.total += 1
        self.ran += 1
        mark = "✅ RAN    " if ok else ("⚠️  LOOK   " if look else "🔴 FAILED ")
        print(f"  {mark} {label}")
        for ln in lines[:8]:
            print(f"              {ln[:96]}")
        if not ok:
            (self.look if look else self.failed).append(label)


def tsv_integrity():
    bad, info = [], []
    for f in sorted((PHAN / "workbook").glob("*.tsv")):
        raw = f.read_bytes().decode("utf-8", "replace")
        lines = raw.split("\n")
        if lines and lines[-1] == "":
            lines = lines[:-1]
        crlf = [l.endswith("\r") for l in lines]
        if any(crlf) and not all(crlf):
            bad.append(f"{f.name}: MIXED line endings ({sum(crlf)}/{len(crlf)} CRLF)")
        rows = [l.rstrip("\r") for l in lines if l.strip() and not l.startswith("#")]
        if rows:
            n = rows[0].count("\t") + 1
            off = [i for i, r in enumerate(rows[1:], 2) if r.count("\t") + 1 != n]
            if off:
                bad.append(f"{f.name}: {len(off)} row(s) != {n} cols (data rows {off[:5]})")
        info.append(f"{f.name}: {len(rows) - 1 if rows else 0} rows, {'CRLF' if all(crlf) else 'LF'}")
    return bad, info


def two_clock():
    bad, info = [], []
    for name in LIVE_LEDGERS:
        text = (PHAN / "workbook" / name).read_text(encoding="utf-8", errors="replace")
        m = re.search(r"Last real data refresh:\s*(\d{4}-\d{2}-\d{2})", text)
        h = re.search(r"(?:Last hygiene/no-event check|Hygiene/touch):\s*(\d{4}-\d{2}-\d{2})", text)
        if not m:
            bad.append(f"{name}: no 'Last real data refresh: YYYY-MM-DD' header")
        else:
            info.append(f"{name}: data {m.group(1)} · hygiene {h.group(1) if h else 'MISSING'}")
            if not h:
                bad.append(f"{name}: no hygiene/no-event clock")
    return bad, info


def next_docket_row():
    cat = ROOT / "AGENTS/CARL/docket/CATALYSTS.tsv"
    rows = []
    for l in cat.read_text(encoding="utf-8", errors="replace").splitlines():
        f = l.split("\t")
        if len(f) > 1 and re.match(r"\d{4}-\d{2}-\d{2}$", f[0]) and "PHAN" in l and f[0] >= TODAY:
            rows.append(f"{f[0]}  {f[1][:80]}")
    return sorted(rows)


def phan_dirty():
    # ⛔ Do NOT use run(): it .strip()s output, which eats the leading space of the FIRST
    # porcelain line (" M path"), shifts l[3:] by one and makes that file INVISIBLE. In --post
    # that reads an uncommitted file as clean. Caught by dogfooding 2026-10-28 (CLAUDE.md
    # was dirty and unlisted). Parse git's raw output; porcelain v1 is "XY <path>".
    try:
        p = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"],
                           cwd=str(ROOT), capture_output=True, text=True, timeout=60)
    except Exception:
        return None
    if p.returncode != 0:
        return None
    hits = []
    for l in p.stdout.splitlines():
        m = re.match(r"^.. (.+)$", l)
        if not m:
            continue
        path = m.group(1).split(" -> ")[-1]
        if path.startswith(REL + "/") or re.search(r"(^|/)inbox/[^/]*from-PHAN", path):
            hits.append(l)
    return hits


def main():
    ap = argparse.ArgumentParser(description="PHAN closeout runner (see module docstring)")
    ap.add_argument("--post", action="store_true", help="after safe-push: prove nothing is left uncommitted/unpushed")
    ap.add_argument("--memory-slug", action="append", default=[])
    ap.add_argument("--superseded", action="append", default=[], help="OLD:NEW[:SERIES]")
    a = ap.parse_args()
    R = Report()

    print("=" * 78)
    print(f"  PHAN CLOSEOUT RUNNER ({'POST-PUSH' if a.post else 'PRE-COMMIT'}) · {TODAY}")
    print("=" * 78)

    if a.post:
        dirty = phan_dirty()
        R.local("git · nothing PHAN-authored left uncommitted",
                dirty == [], dirty or ["clean"] if dirty is not None else ["git status failed"])
        # ⛔ Scope to PHAN-touching commits. The working tree is SHARED: other sessions commit
        # here between your commit and your push, so "HEAD ahead of origin" counts THEIR work
        # (2026-10-28: --post failed on 2 WAL/FERT commits; safe-push's NOT PUSHED named WAL's
        # HEAD while PHAN's own commit was already on origin).
        rc, out = run(["git", "fetch", "-q", "origin"])
        rc2, ahead = run(["git", "log", "--format=%h %s", "origin/master..HEAD", "--",
                          REL, "AGENTS/*/inbox/*from-PHAN*", "PROME/inbox/*from-PHAN*"])
        mine = [l for l in ahead.splitlines() if l.strip()] if rc2 == 0 else ["?"]
        R.local("git · every PHAN-touching commit is on origin/master (fresh fetch)",
                rc == 0 and rc2 == 0 and not mine,
                (mine or ["0 PHAN-touching commits ahead of origin"]) +
                ["other sessions' unpushed commits are theirs, not PHAN's",
                 "the receipt is still safe-push's 'Pushed. CONFIRMED' line, or this check"])
        return finish(R)

    # ---- PHAN-local mechanical checks --------------------------------------------------------
    size = (PHAN / "DOSSIER.md").stat().st_size
    pct = size / CAP
    R.local(f"read cap · DOSSIER.md (whole read) {size:,} B = {pct:.0%} of {CAP:,}",
            size <= CAP, [f"OVER the cap: rotate to PASSES.md before commit"] if size > CAP else [])
    if size <= CAP and pct >= ROTATE_AT:
        R.local(f"rotation trigger · DOSSIER.md ≥{ROTATE_AT:.0%}", False,
                ["rotate settled narrative / closed rows to PASSES.md THIS session"], look=True)
    for f in ("FRAMEWORKS.md", "PASSES.md", "CLOSEOUT.md"):
        p = PHAN / f
        if p.exists():
            print(f"              (info) {f} {p.stat().st_size:,} B (not a boot whole-read; no cap claim)")

    bad, info = tsv_integrity()
    R.local("workbook TSVs · column counts + line endings consistent", not bad, bad or info)

    bad, info = two_clock()
    R.local("live ledgers · two-clock headers present", not bad, bad + info)

    inbox = sorted(p.relative_to(PHAN).as_posix() for p in (PHAN / "inbox").rglob("*.md")
                   if "processed" not in p.parts and p.name != "README.md")
    R.local(f"inbox re-scan · {len(inbox)} unprocessed packet(s)", not inbox,
            inbox + (["git mv consumed packets to inbox/processed/; PARKED note for the rest"] if inbox else []),
            look=True)

    nxt = next_docket_row()
    R.local("next run docketed · future PHAN row in CARL docket/CATALYSTS.tsv", bool(nxt),
            nxt or ["NONE: ask CARL for a docket row in the closeout packet (CARL owns the docket)"])

    # ---- fleet / root checks ---------------------------------------------------------------
    dated = [f"{REL}/{f}" for f in ("DOSSIER.md", "PASSES.md", "FRAMEWORKS.md", "CLOSEOUT.md")
             if (PHAN / f).exists()] + [f"{REL}/workbook/{f}" for f in LIVE_LEDGERS]
    R.tool("root 1e · claim_check weekday (PHAN dated surfaces)",
           [sys.executable, "scripts/claim_check.py", "--check", "weekday", *dated],
           (0,), r"CLAIM-CHECK")
    R.tool("root 1b · orphan_check CARL (PHAN lines shown)",
           ["bash", "scripts/orphan_check.sh", "CARL"], (0,), r"not yours|likely YOURS|nothing|clean|orphan",
           show=r"PHAN")
    R.tool("root 1c-bis · ledger_staleness (PHAN workbook)",
           [sys.executable, "scripts/ledger_staleness.py", "CARL", "--glob", "sub_agents/PHAN/workbook/*.tsv"],
           (0, 1), r"perimeter \[CARL\]", show=r"PHAN/workbook/(?!.*(FROZEN))|→")
    R.tool("CARL consistency_check · Check E covers PHAN PREDICTIONS.tsv",
           [PY, "AGENTS/CARL/scripts/consistency_check.py", "--quiet"],
           (0, 1), r"✅ CHECK E", show=r"PHAN|CHECK E|SUMMARY")
    rc, out = run([sys.executable, "scripts/read_cap_check.py", "--agent", "PHAN"])
    R.total += 1; R.ran += 1
    if rc is None or crashed(out) or not re.search(r"READ-CAP-RESULT v1", out):
        print("  🔴 FAILED  fleet read_cap_check --agent PHAN"); R.failed.append("read_cap_check")
    elif "DOSSIER.md" not in out:
        print(f"  ⚠️  LOOK    fleet read_cap_check --agent PHAN   rc={rc}")
        print("              grades frozen STATUS.md, not DOSSIER.md: no PHAN rows in PROME/registry/READS.tsv")
        print("              (packet sent to PROME 2026-10-28). Its verdict is NOT about the dossier; use the local check above.")
        R.look.append("read_cap_check wrong file")
    else:
        print(f"  ✅ RAN     fleet read_cap_check --agent PHAN   rc={rc}")
        if rc != 0:
            R.failed.append("read_cap_check")

    for spec in a.superseded:
        parts = spec.split(":")
        if len(parts) < 2:
            print(f"  🔴 FAILED  --superseded '{spec}' must be OLD:NEW[:SERIES]"); R.failed.append(spec); continue
        cmd = [sys.executable, "scripts/consumer_check.py", "--agent", "CARL", "--old", parts[0], "--new", parts[1]]
        if len(parts) > 2:
            cmd += ["--series", parts[2]]
        R.tool(f"root 1c · consumer_check {spec}", cmd, (0, 1, 2), r"CONSUMER CHECK", show=r"🔴|🟠|✅")
    for slug in a.memory_slug:
        R.tool(f"root 1d · memory_index_check --slug {slug}",
               [sys.executable, "scripts/memory_index_check.py", "--strict", "--slug", slug], (0,), r"SCOPED|OK|0 blocking")
        R.tool("root 1d · check_memory_length", ["bash", "scripts/check_memory_length.sh"], (0, 1), r"cap")

    dirty = phan_dirty()
    print(f"  ℹ️  INFO    git · {len(dirty) if dirty is not None else '?'} PHAN path(s) to commit (explicit pathspecs only)")
    for l in (dirty or [])[:12]:
        print(f"              {l}")
    return finish(R, pre=True, a=a)


JUDGEMENT = [
    ("CURRENT STATE", "updated IN PLACE (never a new section); stamps advanced; addendum true"),
    ("OWED block", "closed what you did; added what PHAN or CARL now owes, with dates"),
    ("predictions", "re-marked with a dated note, NOT resolved; resolution routed to CARL"),
    ("PROVIDER.tsv", "new reading = new row; superseded row's Notes prefixed SUPERSEDED <date>"),
    ("live ledgers", "DID_NOT_APPEAR null if a sweep found nothing; data clock only on real data"),
    ("routing", "signals (a threshold firing) -> WALTER inbox; analysis/asks -> CARL inbox + outbox copy"),
    ("consumer check", "if you superseded a figure others cite: --superseded OLD:NEW:SERIES; bare 2-sig-fig -> targeted grep"),
    ("memory", "only if a transferable lesson was earned: extend before create; --memory-slug"),
    ("PASSES.md", "pass narrative + closeout record written"),
    ("final report", "(a) findings persisted (b) checks run / not run / failed (c) commit vs verified push"),
]


def finish(R, pre=False, a=None):
    print("\n" + "-" * 78)
    print(f"  MECHANICAL: {R.ran}/{R.total} executed · {len(R.failed)} failed · {len(R.look)} need a look")
    print("-" * 78)
    if pre:
        if not a.superseded:
            print("  ⚪ NOT RUN  root 1c consumer_check: no --superseded given. If a figure was superseded, re-run with it.")
        if not a.memory_slug:
            print("  ⚪ NOT RUN  root 1d memory checks: no --memory-slug given (correct only if no auto-memory was written).")
        print("\n  ⛔ NOT VERIFIED BY THIS SCRIPT (judgement steps, listed so they are visible as obligations):")
        for label, ask in JUDGEMENT:
            print(f"     ·  {label:16s} {ask}")
        print("\n  Next: commit (explicit pathspecs) -> Will-launched: bash scripts/safe-push.sh (do not pipe it)")
        print("        -> re-run with --post.   CARL-spawned: commit only; CARL's push carries it.")
    print("\n  ⚠️  A clean run means THE STEPS EXECUTED, never that the closeout is correct.")
    if R.failed:
        print(f"\n  EXIT 1 — {len(R.failed)} step(s) need a fix: {'; '.join(R.failed)}")
        return 1
    print("\n  EXIT 0 — every mechanical step executed and passed" + (" (LOOK items still need a decision)." if R.look else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
