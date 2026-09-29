#!/usr/bin/env python3
"""mirror_check.py -- closeout check 3/4: MIRROR SYNC across STATUS / THESIS / TRADE.

Built 2026-09-29 on Will's question ("maybe it needs to be checked at closeout
normally? Do we not do that?") after THESIS.md carried the 8/10 "CONTESTED"
regime label for 28 DAYS past the 9/1 TWO-PART ruling, and said "no add-gate
has fired" for 19 days after both gates fired -- through 28 closeouts in which
step 17 ("mirror-consistency check") was a self-assessed human step and step 16's
assertion_check knew four shapes that none of these claims fit (no number, no
date, no direction word, no file claim). PROME's cold read found it; nothing on
this desk did. Same afternoon, TRADE.md cited THESIS v1.2.3 against a v1.2.9 file,
and an hour after that was fixed it cited v1.2.9 against v1.2.10.

THE MECHANISM: prose is not compared; a TOKEN is. Each of the three surfaces
carries one machine line

    <!-- bond-state: thesis=v1.2.10; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=NOT-FIRED; posture=HOLD-NO-ADD -->

placed beside the prose it summarises. The check fails CLOSED: a missing token
is a finding, a field present in one file and absent in another is a finding,
any differing value is a finding, and `thesis=` must equal THESIS's H1 version.
A writer who changes state in STATUS and forgets THESIS now gets told at
closeout instead of by a reviewer four weeks later.

WHAT IT CANNOT DO (said out loud so the pass is not over-read): it does not
know whether the PROSE beside the token agrees with the token. A writer can
update all three tokens and leave the banner wrong. Two mitigations, not
cures: (1) the tokens sit on the lines the writer is already editing;
(2) RETIRED_PHRASES sweeps for the exact strings that were the 9/29 defects,
unless the line is a labelled quote (assertion_check's GUARD list + a few
local guards). New defects in new words are outside its scope entirely.

rc: 0 clean / 1 finding(s). `--selftest` runs the fixtures, which are the real
9/29 defects.
"""
from __future__ import annotations
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # AGENTS/BOND
SURFACES = ["STATUS.md", "thesis/THESIS.md", "TRADE.md"]
TOKEN_RE = re.compile(r"<!--\s*bond-state:\s*(.*?)\s*-->", re.S)
H1_RE = re.compile(r"^# BOND THESIS\s+[—-]+\s+v(\d+\.\d+\.\d+)", re.M)
FIELD_RE = re.compile(r"^\*\*Version:\*\*\s*(\d+\.\d+\.\d+)", re.M)
CITE_RE = re.compile(r"THESIS\.md[`*]*\s*\**v(\d+\.\d+\.\d+)")

# (lowercase needle, why it is retired) -- the 9/29 defects, verbatim
RETIRED_PHRASES = [
    ("none has fired", "both add-gates fired (9/10 level; 9/23 re-arm); the add was DECLINED (WQ-280)"),
    ("no pre-registered add-gate has fired", "same"),
    ("contested (~50%)", "C-36 ruled TWO-PART 2026-09-01 (Will)"),
    ("29 consecutive", "retracted 2026-08-15; the run is a DERIVED figure that lives in STATUS"),
    ("single-digit bp away", "DFII10 has been THROUGH the gate since 2026-09-10"),
    ("20 consecutive benign", "the benign run ended at the 2026-09-23 5Y"),
]
LOCAL_GUARD = ('read *"', ' said "', "rewritten", "reconciled", "snapshot", "pre-edit", "old text",
               "this line read", "retired_phrases", "mirror_check")


def _guarded(line: str) -> bool:
    low = line.lower()
    if any(g in low for g in LOCAL_GUARD):
        return True
    try:
        spec = importlib.util.spec_from_file_location("assertion_check", HERE / "monitors" / "assertion_check.py")
        ac = importlib.util.module_from_spec(spec); spec.loader.exec_module(ac)
        return ac.guarded(line)
    except Exception:                                   # noqa: BLE001
        return False


def parse_token(text: str):
    m = TOKEN_RE.search(text)
    if not m:
        return None
    out = {}
    for part in m.group(1).split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            out[part] = ""
            continue
        k, v = part.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def check_texts(texts: dict) -> list:
    """Pure function over {surface: text}. Returns a list of finding strings."""
    f = []
    thesis = texts.get("thesis/THESIS.md", "")
    h1 = H1_RE.search(thesis)
    fld = FIELD_RE.search(thesis)
    h1v = h1.group(1) if h1 else None
    fldv = fld.group(1) if fld else None
    if not h1v:
        f.append("VERSION: THESIS H1 '# BOND THESIS — vX.Y.Z' not found")
    if not fldv:
        f.append("VERSION: THESIS '**Version:** X.Y.Z' field not found")
    if h1v and fldv and h1v != fldv:
        f.append(f"VERSION: THESIS H1 v{h1v} != Version field {fldv} (the 8/21 self-contradiction class)")
    for name in ("TRADE.md", "STATUS.md"):
        for cv in CITE_RE.findall(texts.get(name, "")):
            if h1v and cv != h1v:
                f.append(f"VERSION: {name} cites THESIS v{cv} but THESIS is v{h1v}")
    # token
    toks = {}
    for name in SURFACES:
        t = parse_token(texts.get(name, ""))
        if t is None:
            f.append(f"TOKEN: {name} carries no <!-- bond-state: ... --> line (fail closed)")
        else:
            toks[name] = t
    if toks:
        keys = set().union(*[set(t) for t in toks.values()])
        for k in sorted(keys):
            vals = {name: t.get(k) for name, t in toks.items()}
            present = {n: v for n, v in vals.items() if v is not None}
            if len(present) < len(toks):
                missing = [n for n, v in vals.items() if v is None]
                f.append(f"TOKEN: field '{k}' absent in {missing}")
            if len(set(present.values())) > 1:
                f.append(f"TOKEN: field '{k}' DIFFERS: " + "; ".join(f"{n}={v}" for n, v in present.items()))
        for name, t in toks.items():
            tv = t.get("thesis", "").lstrip("v")
            if h1v and tv and tv != h1v:
                f.append(f"TOKEN: {name} token says thesis=v{tv} but THESIS H1 is v{h1v}")
    # retired phrases
    for name, text in texts.items():
        for i, line in enumerate(text.split("\n"), 1):
            low = line.lower()
            for needle, why in RETIRED_PHRASES:
                if needle in low and not _guarded(line):
                    f.append(f"RETIRED-PHRASE: {name}:{i} '{needle}' — {why}")
    return f


def check_files() -> int:
    texts = {}
    for rel in SURFACES:
        p = HERE / rel
        texts[rel] = p.read_text(encoding="utf-8") if p.exists() else ""
    findings = check_texts(texts)
    for x in findings:
        print(f"  🔴 MIRROR — {x}")
    if not findings:
        print("   ✅ mirror sync: THESIS version cited consistently · bond-state token identical on "
              f"{len(SURFACES)} surfaces · no retired phrase outside a labelled quote")
        print("      (scope: the TOKEN and the version strings — not whether the prose beside them is true)")
    return len(findings)


# ---------------------------------------------------------------------------
TOK = ("<!-- bond-state: thesis=v1.2.10; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; "
       "rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=NOT-FIRED; posture=HOLD-NO-ADD -->")
GOOD = {
    "thesis/THESIS.md": "# BOND THESIS — v1.2.10\n\n**Version:** 1.2.10 (x)\n" + TOK + "\nbanner ok\n",
    "STATUS.md": "# s\n" + TOK + "\nFull ruling → `thesis/THESIS.md` **v1.2.10**\n",
    "TRADE.md": "# t\n**Regime:** `thesis/THESIS.md` **v1.2.10**\n" + TOK + "\n",
}
def _mut(surface, old, new, base=GOOD):
    d = dict(base); d[surface] = d[surface].replace(old, new); return d

FIXTURES = [
    ("clean set → 0 findings", GOOD, 0, 0),
    ("REAL 9/29 defect: TRADE cites v1.2.9 against THESIS v1.2.10",
     _mut("TRADE.md", "**v1.2.10**", "**v1.2.9**"), 1, None),
    ("REAL 9/29 defect: THESIS banner label behind the 9/1 ruling (token regime differs)",
     _mut("thesis/THESIS.md", "regime=C-36-TWO-PART@2026-09-01", "regime=CONTESTED@2026-08-10"), 1, None),
    ("REAL 9/29 defect: 'none has fired' unguarded in THESIS conviction line",
     _mut("thesis/THESIS.md", "banner ok", "**Conviction:** the add-gates are pre-registered and none has fired."), 1, None),
    ("labelled quote of the same phrase → NOT a finding",
     _mut("thesis/THESIS.md", "banner ok", '*(This line read "none has fired" until 9/29.)*'), 0, 0),
    ("token missing on one surface → fail closed",
     _mut("STATUS.md", TOK, ""), 1, None),
    ("token field present in two files, absent in the third",
     _mut("TRADE.md", "; posture=HOLD-NO-ADD", ""), 1, None),
    ("REAL 8/21 class: THESIS H1 != Version field",
     _mut("thesis/THESIS.md", "**Version:** 1.2.10", "**Version:** 1.2.9"), 1, None),
    ("token thesis= behind the H1 bump (STATUS token stale)",
     _mut("STATUS.md", "thesis=v1.2.10", "thesis=v1.2.9"), 1, None),
]


def selftest() -> int:
    bad = 0
    print("-" * 74)
    print(f"  mirror_check SELFTEST — {len(FIXTURES)} fixtures (the real 9/29 defects + guards)")
    print("-" * 74)
    for name, texts, min_f, max_f in FIXTURES:
        got = check_texts(texts)
        ok = len(got) >= min_f and (max_f is None or len(got) <= max_f)
        print(f"  {'✅' if ok else '❌'} {name}: {len(got)} finding(s)")
        if not ok:
            bad += 1
            for g in got:
                print("       ", g)
    print(f"  {'ALL PASS' if not bad else str(bad) + ' FAILURE(S)'}")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(1 if check_files() else 0)
