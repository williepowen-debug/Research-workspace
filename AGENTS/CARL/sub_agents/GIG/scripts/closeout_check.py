#!/usr/bin/env python3
"""
GIG closeout runner: executes the MECHANICAL closeout steps in CLOSEOUT.md,
reports RAN / FAILED / LOOK per step, then NAMES the judgement steps it cannot
verify.  Adapted 2026-10-28 (Will: "adopt and improve the close out now") from
PHAN's runner (AGENTS/CARL/sub_agents/PHAN/scripts/closeout_check.py), which is
itself modelled on HANS's.  Keep their rules.

INTERIM.  PHAN has proposed ONE shared runner for all seven CARL sub-agents
(AGENTS/CARL/inbox/2026-10-28_from-PHAN_shared-subagent-closeout-runner-proposal.md).
If CARL adopts it, GIG moves to the shared runner and this file is retired.
The GIG-specific settings are the CONFIG block below; the extra checks GIG adds
(marked GIG+) are offered back to the shared design.

  ⛔ THIS SCRIPT DOES NOT CERTIFY THE CLOSEOUT.
  It certifies that the mechanical steps EXECUTED and what they returned.
  Judgement steps are listed as UNVERIFIED BY DESIGN.

RULES CARRIED FROM HANS/PHAN (each was learned by a runner lying once):
  - A step passes only if it did not crash AND printed its own completion
    line.  rc alone cannot tell a verdict from a traceback.
  - Signalling exits (consumer/ledger tools exit non-zero to mean "found
    something") are accepted only with the completion line present.
  - git porcelain is parsed raw, never .strip()ped (a strip hides the first file).
  - --post scopes "ahead of origin" to GIG-touching commits; the tree is shared.

USAGE (from anywhere):
  python3 AGENTS/CARL/sub_agents/GIG/scripts/closeout_check.py            # before commit
  python3 AGENTS/CARL/sub_agents/GIG/scripts/closeout_check.py --post     # after safe-push
  options: --memory-slug <slug>          (repeat; root 1d memory checks)
           --superseded OLD:NEW[:SERIES] (repeat; root 1c consumer_check)

Exit: 0 every mechanical step ran and passed · 1 a step FAILED or errored.
      LOOK lines never change the exit code; they need a human decision.
"""
import argparse, datetime, re, subprocess, sys, zlib
from pathlib import Path

# ---- CONFIG (what differs per sub-agent; maps onto PHAN's proposed SUBAGENT_CLOSEOUT.tsv) ----
AGENT = "GIG"
HOME = Path(__file__).resolve().parent.parent
ROOT = HOME.parents[3]                       # GIG -> sub_agents -> CARL -> AGENTS -> repo root
REL = HOME.relative_to(ROOT).as_posix()      # AGENTS/CARL/sub_agents/GIG
SURFACE = "STATUS.md"                        # the whole-read boot surface
CAP = 32_550                                 # root read-cap budget (bytes)
ROTATE_AT = 0.75                             # fleet read_cap_check rotate-tier
LIVE_LEDGERS = ["PLATFORM.tsv", "DRIVER_ECONOMICS.tsv", "VX.tsv", "ML.tsv", "PREDICTIONS.tsv"]
FROZEN_LEDGERS = {"FLOW.tsv": "FROZEN", "AV_TRACKER.tsv": "RETIRED"}
ARCHIVE_GLOB = "archive/STATUS_ARCHIVE_*.md"
# -----------------------------------------------------------------------------------------------

VENV_PY = ROOT / ".venv/bin/python3"
PY = str(VENV_PY) if VENV_PY.exists() else sys.executable
TODAY = datetime.date.today()
TODAY_S = TODAY.isoformat()


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


def git_raw(args):
    """Raw git stdout (never stripped). None on failure."""
    try:
        p = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True, timeout=60)
    except Exception:
        return None
    return p.stdout if p.returncode == 0 else None


def tsv_integrity():
    bad, info = [], []
    for f in sorted((HOME / "workbook").glob("*.tsv")):
        raw = f.read_bytes().decode("utf-8", "replace")
        lines = raw.split("\n")
        if lines and lines[-1] == "":
            lines = lines[:-1]
        crlf = [l.endswith("\r") for l in lines]
        if any(crlf):
            bad.append(f"{f.name}: CRLF present ({sum(crlf)}/{len(crlf)}); every GIG ledger is LF")
        if "" in [l.rstrip("\r") for l in lines]:
            bad.append(f"{f.name}: blank line inside the file")
        rows = [l.rstrip("\r") for l in lines if l.strip() and not l.startswith("#")]
        if rows:
            n = rows[0].count("\t") + 1
            off = [i for i, r in enumerate(rows[1:], 2) if r.count("\t") + 1 != n]
            if off:
                bad.append(f"{f.name}: {len(off)} row(s) != {n} cols (data rows {off[:5]})")
        info.append(f"{f.name}: {len(rows) - 1 if rows else 0} rows")
    return bad, info


def two_clock():
    bad, info = [], []
    for name in LIVE_LEDGERS:
        first = (HOME / "workbook" / name).read_text(encoding="utf-8", errors="replace").split("\n", 1)[0]
        m = re.search(r"Last real data refresh:\s*(\d{4}-\d{2}-\d{2})", first)
        h = re.search(r"Last hygiene/no-event check:\s*(\d{4}-\d{2}-\d{2})", first)
        if not m:
            bad.append(f"{name}: row 1 lacks 'Last real data refresh: YYYY-MM-DD'")
        if not h:
            bad.append(f"{name}: row 1 lacks 'Last hygiene/no-event check: YYYY-MM-DD'")
        if m and h:
            info.append(f"{name}: data {m.group(1)} · hygiene {h.group(1)}")
    return bad, info


def frozen_ledgers():
    """GIG+: frozen/retired ledgers carry their banner and were not edited (vs HEAD and in index)."""
    bad, info = [], []
    changed = git_raw(["status", "--porcelain", "--", *[f"{REL}/workbook/{f}" for f in FROZEN_LEDGERS]])
    for name, word in FROZEN_LEDGERS.items():
        p = HOME / "workbook" / name
        if not p.exists():
            info.append(f"{name}: absent")
            continue
        first = p.read_text(encoding="utf-8", errors="replace").split("\n", 1)[0]
        if not first.startswith(f"# {word}"):
            bad.append(f"{name}: row 1 lacks the '# {word} <date>' banner")
        else:
            info.append(f"{name}: {word} banner present")
    if changed is None:
        bad.append("git status failed; cannot prove frozen ledgers untouched")
    elif changed.strip():
        bad += [f"EDITED: {l}" for l in changed.splitlines()]
    return bad, info


def status_stamp():
    """GIG+: STATUS 'Last Updated' restamped today (a stale header = an unread file)."""
    head = (HOME / SURFACE).read_text(encoding="utf-8", errors="replace")[:600]
    m = re.search(r"\*\*Last Updated:\*\*\s*(\d{4}-\d{2}-\d{2})", head)
    return (m and m.group(1) == TODAY_S), [f"Last Updated = {m.group(1) if m else 'NOT FOUND'} (today {TODAY_S})"]


def archive_integrity():
    """GIG+: every rotated block still matches its recorded bytes + CRC32."""
    bad, n = [], 0
    for a in sorted(HOME.glob(ARCHIVE_GLOB)):
        text = a.read_text(encoding="utf-8")
        for m in re.finditer(r"`bytes=(\d+) crc32=([0-9a-f]{8})`\n\n<!-- BEGIN VERBATIM -->\n(.*?)\n<!-- END VERBATIM -->",
                             text, re.S):
            n += 1
            b = m.group(3).encode()
            if len(b) != int(m.group(1)) or f"{zlib.crc32(b) & 0xffffffff:08x}" != m.group(2):
                bad.append(f"{a.name}: block {n} bytes/crc mismatch")
    return bad, [f"{n} archived block(s) verified"]


def window_end(tf):
    """Best-effort end date of a free-text timeframe; None = cannot parse (LOOK)."""
    t = tf.upper()
    y = re.findall(r"20\d\d", t)
    if not y:
        return None
    yr = int(y[-1])
    if "EOY" in t or re.fullmatch(r"\s*20\d\d\s*", t):
        return datetime.date(yr, 12, 31)
    q = re.findall(r"Q([1-4])", t)
    if q:
        mo = int(q[-1]) * 3
        return datetime.date(yr + (mo == 12), mo % 12 + 1, 1) - datetime.timedelta(days=1)
    h = re.findall(r"H([12])", t)
    if h:
        return datetime.date(yr, 6, 30) if h[-1] == "1" else datetime.date(yr, 12, 31)
    return None


def prediction_due_scan():
    """GIG+: OPEN/TRACKING rows whose window has passed are DUE (resolve, re-arm or re-date with a reason)."""
    lines, due = [], False
    rows = (HOME / "workbook/PREDICTIONS.tsv").read_text(encoding="utf-8").splitlines()
    hdr = next(i for i, l in enumerate(rows) if l.startswith("Pred_ID"))
    for l in rows[hdr + 1:]:
        f = l.split("\t")
        if len(f) < 6 or f[5].upper() not in ("OPEN", "TRACKING"):
            continue
        end = window_end(f[4])
        if end is None:
            lines.append(f"{f[0]}: timeframe '{f[4]}' unparsed — eyeball it"); due = True
        elif end < TODAY:
            lines.append(f"{f[0]}: window ended {end} — DUE"); due = True
        else:
            lines.append(f"{f[0]}: open, window ends {end} ({(end - TODAY).days}d)")
    return not due, lines or ["no OPEN/TRACKING rows"]


def pending_rulings():
    """GIG+: state vectors / packets that ask CARL to rule and carry no 'rulings applied' line."""
    out = []
    for p in sorted((HOME / "state_vectors").glob("SV-GIG-*.md")):
        t = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r"must rule on", t, re.I) and not re.search(r"rulings? applied", t, re.I):
            out.append(f"{p.name}: CARL ruling asked, none recorded")
    return out


def next_docket_row():
    cat = ROOT / "AGENTS/CARL/docket/CATALYSTS.tsv"
    rows = []
    for l in cat.read_text(encoding="utf-8", errors="replace").splitlines():
        f = l.split("\t")
        if len(f) > 1 and re.match(r"\d{4}-\d{2}-\d{2}$", f[0]) and AGENT in f[1] and f[0] >= TODAY_S:
            rows.append((f"{f[0]}  {f[1][:84]}", l))   # (display, full row): flag tests the FULL row
    return sorted(rows)


def agent_dirty():
    # Parse git's raw porcelain; a .strip() eats the first line's leading space (PHAN 2026-10-28).
    out = git_raw(["status", "--porcelain", "--untracked-files=all"])
    if out is None:
        return None
    hits = []
    for l in out.splitlines():
        m = re.match(r"^.. (.+)$", l)
        if not m:
            continue
        path = m.group(1).split(" -> ")[-1]
        if path.startswith(REL + "/") or re.search(rf"(^|/)inbox/[^/]*from-{AGENT}", path):
            hits.append(l)
    return hits


def main():
    ap = argparse.ArgumentParser(description=f"{AGENT} closeout runner (see module docstring)")
    ap.add_argument("--post", action="store_true", help="after safe-push: prove nothing is left uncommitted/unpushed")
    ap.add_argument("--memory-slug", action="append", default=[])
    ap.add_argument("--superseded", action="append", default=[], help="OLD:NEW[:SERIES]")
    a = ap.parse_args()
    R = Report()

    print("=" * 78)
    print(f"  {AGENT} CLOSEOUT RUNNER ({'POST-PUSH' if a.post else 'PRE-COMMIT'}) · {TODAY_S}")
    print("=" * 78)

    if a.post:
        dirty = agent_dirty()
        R.local(f"git · nothing {AGENT}-authored left uncommitted",
                dirty == [], (dirty or ["clean"]) if dirty is not None else ["git status failed"])
        rc, _ = run(["git", "fetch", "-q", "origin"])
        rc2, ahead = run(["git", "log", "--format=%h %s", "origin/master..HEAD", "--",
                          REL, f"AGENTS/*/inbox/*from-{AGENT}*", f"PROME/inbox/*from-{AGENT}*"])
        mine = [l for l in ahead.splitlines() if l.strip()] if rc2 == 0 else ["?"]
        R.local(f"git · every {AGENT}-touching commit is on origin/master (fresh fetch)",
                rc == 0 and rc2 == 0 and not mine,
                (mine or [f"0 {AGENT}-touching commits ahead of origin"]) +
                ["other sessions' unpushed commits are theirs, not GIG's"])
        return finish(R)

    # ---- GIG-local mechanical checks ---------------------------------------------------------
    size = (HOME / SURFACE).stat().st_size
    pct = size / CAP
    R.local(f"read cap · {SURFACE} (whole read) {size:,} B = {pct:.0%} of {CAP:,}",
            size <= CAP, ["OVER the cap: rotate to archive/ before commit"] if size > CAP else [])
    if size <= CAP and pct >= ROTATE_AT:
        R.local(f"rotation trigger · {SURFACE} ≥{ROTATE_AT:.0%}", False,
                ["rotate settled sections verbatim to archive/STATUS_ARCHIVE_<YYYY-MM>.md (bytes + CRC32) THIS session"],
                look=True)

    ok, lines = status_stamp()
    R.local("STATUS · Last Updated restamped today", ok, lines, look=True)

    bad, info = archive_integrity()
    R.local("archive · rotated blocks match recorded bytes + CRC32", not bad, bad or info)

    bad, info = tsv_integrity()
    R.local("workbook TSVs · column counts, LF endings, no blank lines", not bad, bad or info)

    bad, info = two_clock()
    R.local("live ledgers · two-clock headers on row 1", not bad, bad + info)

    bad, info = frozen_ledgers()
    R.local("frozen/retired ledgers · banner present, not edited", not bad, bad or info)

    ok, lines = prediction_due_scan()
    R.local("predictions · OPEN rows inside their window", ok, lines, look=True)

    pend = pending_rulings()
    R.local(f"CARL rulings · {len(pend)} asked and not yet recorded", not pend,
            pend + (["carry each in STATUS CROSS-AGENT LINKS; re-ask if older than ~7 days"] if pend else []),
            look=True)

    inbox = sorted(p.relative_to(HOME).as_posix() for p in (HOME / "inbox").rglob("*.md")
                   if "processed" not in p.parts and p.name != "README.md")
    R.local(f"inbox re-scan · {len(inbox)} unprocessed packet(s)", not inbox,
            inbox + (["git mv consumed packets to inbox/processed/; PARKED note in STATUS for the rest"] if inbox else []),
            look=True)

    nxt = next_docket_row()
    R.local(f"next run docketed · future {AGENT} row in CARL docket/CATALYSTS.tsv", bool(nxt),
            [d for d, _ in nxt] or ["NONE: ask CARL for a docket row in the closeout packet (CARL owns the docket)"])
    # Test the FULL row, not the 84-char display: the first version missed 'UNVERIFIED' past the cut (2026-10-29).
    if any("UNVERIFIED" in full.upper() for _, full in nxt):
        R.local("docket row · date still marked UNVERIFIED", False,
                ["if GIG has confirmed the date, ask CARL to re-date it (state vector or packet)"], look=True)

    # ---- fleet / root checks ---------------------------------------------------------------
    dated = [f"{REL}/{f}" for f in (SURFACE, "CLAUDE.md", "CLOSEOUT.md") if (HOME / f).exists()] + \
            [f"{REL}/workbook/{f}" for f in LIVE_LEDGERS] + \
            [p.relative_to(ROOT).as_posix() for p in sorted((HOME / "state_vectors").glob(f"SV-GIG-{TODAY_S}-*.md"))]
    R.tool("root 1e · claim_check weekday (GIG dated surfaces)",
           [sys.executable, "scripts/claim_check.py", "--check", "weekday", *dated],
           (0,), r"CLAIM-CHECK")
    R.tool("root 1b · orphan_check CARL (GIG lines shown)",
           ["bash", "scripts/orphan_check.sh", "CARL"], (0,), r"not yours|likely YOURS|nothing|clean|orphan",
           show=AGENT)
    R.tool("root 1c-bis · ledger_staleness (GIG workbook)",
           [sys.executable, "scripts/ledger_staleness.py", "CARL", "--glob", f"sub_agents/{AGENT}/workbook/*.tsv"],
           (0, 1), r"perimeter \[CARL\]", show=rf"{AGENT}/workbook/(?!.*(FROZEN|RETIRED))|→")
    R.tool("CARL consistency_check · Check E covers GIG PREDICTIONS.tsv",
           [PY, "AGENTS/CARL/scripts/consistency_check.py", "--quiet"],
           (0, 1), r"✅ CHECK E", show=rf"{AGENT}|CHECK E|SUMMARY")
    rc, out = run([sys.executable, "scripts/read_cap_check.py", "--agent", AGENT])
    R.total += 1; R.ran += 1
    if rc is None or crashed(out) or not re.search(r"READ-CAP-RESULT v1", out):
        print(f"  🔴 FAILED  fleet read_cap_check --agent {AGENT}"); R.failed.append("read_cap_check")
    else:
        res = re.search(r"READ-CAP-RESULT v1.*", out).group(0)
        rot = re.search(r"rotation_due=(\d+)", res)
        mark = "✅ RAN    " if rc == 0 else "🔴 FAILED "
        print(f"  {mark} fleet read_cap_check --agent {AGENT}   rc={rc}")
        print(f"              {res[:96]}")
        if rc != 0:
            R.failed.append("read_cap_check")
        elif rot and rot.group(1) != "0":
            print("              rotation_due>0 → see the local rotation trigger above")

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

    dirty = agent_dirty()
    print(f"  ℹ️  INFO    git · {len(dirty) if dirty is not None else '?'} {AGENT} path(s) to commit (explicit pathspecs only)")
    for l in (dirty or [])[:14]:
        print(f"              {l}")
    return finish(R, pre=True, a=a)


JUDGEMENT = [
    ("STATUS", "top tables match the ledgers; old wording of anything changed is gone from the WHOLE file"),
    ("ledgers", "new reading = new row with As_Of + primary source; data clock only on real data"),
    ("corrections", "a withdrawn read is corrected where it was written (row Notes), not only in STATUS"),
    ("predictions", "graded only on the Instrument series; GIG proposes, CARL disposes"),
    ("state vector", "SV-GIG-<date>-NN.md if anything moved; rulings asked are listed under 'CARL must rule on'"),
    ("routing", "signals (a threshold firing) -> WALTER inbox; analysis/asks -> CARL inbox, committed (①)"),
    ("consumer check", "if a figure others cite was superseded: --superseded OLD:NEW:SERIES"),
    ("memory", "only if a transferable lesson was earned: extend before create; --memory-slug"),
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
            print(f"     ·  {label:15s} {ask}")
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
