#!/usr/bin/env python3
"""Revision census for CARL's prediction ledger (RED ask 2026-09-14).

Walks the git history of thesis/PREDICTIONS.tsv (workbook/PREDICTIONS.tsv before
the move) oldest -> newest and emits one row per material change to a CRL row:

  REGISTERED     row first appears
  CONF           leading confidence number changed (pp delta)
  TIMEFRAME      Timeframe cell changed
  STATUS         Status cell changed (resolution, void, retire)
  SPEC           Prediction text changed AND its set of numeric tokens changed
                 (threshold / bar / leg edits). Text-only rewrites are counted
                 separately as TEXT and are NOT revisions for RED's purpose.
  REMOVED        row disappears from the ledger

It is a CENSUS, not a classification: direction-of-benefit is judged by hand in
thesis/REVISION_LEDGER.md. Output is deterministic for a given git history.

Caveats the census cannot fix:
  - Before 2026-03-31 some IDs were reassigned to different claims (DAEDALUS H2
    audit, ROADMAP as-made thread). An ID's early rows can describe a different
    prediction; SPEC events near that date need a claim-text read.
  - Only commits that touched the file are seen. Two edits inside one commit
    collapse into one event.
  - Confidence is the FIRST "NN%" in the cell. Cells like "N/A" parse as None.

Usage (from repo root):
  .venv/bin/python3 AGENTS/CARL/scripts/revision_ledger.py              # census only
  .venv/bin/python3 AGENTS/CARL/scripts/revision_ledger.py --classify \
      > AGENTS/CARL/thesis/REVISION_LEDGER.tsv                           # census + classification

--classify adds: class, thesis_dir, benefit_final, benefit_asmade, note.
  class          REGISTRATION | RESOLUTION | REPRICE | WINDOW | RESPEC | DISPOSITION
                 | RECORD-CORRECTION | ANNOTATION   (ANNOTATION/REGISTRATION are not revisions)
  thesis_dir     FOR / AGAINST the bear thesis (raise, extension, keep-alive = FOR)
  benefit_final  effect on CARL's scored record if rows are scored at the FINAL mark
  benefit_asmade effect if rows are scored at the AS-MADE confidence (reprices are
                 then Brier-NEUTRAL; only structural moves count)
  Outcome basis: resolved Status; for OPEN rows CARL's current confidence
  (<=25% = likely MISS, >=75% = likely HIT, else UNDETERMINED) -- labelled PROV.
REPRICE rows are classified by rule; every other class comes from OVERRIDES below,
which is hand judgement and is the part a reviewer should attack.
"""
import re
import subprocess
import sys

PATHS = ["AGENTS/CARL/thesis/PREDICTIONS.tsv", "AGENTS/CARL/workbook/PREDICTIONS.tsv"]
PCT = re.compile(r"(\d{1,3}(?:\.\d+)?)\s*%")
NUM = re.compile(r"\d+(?:\.\d+)?")
ID = re.compile(r"^CRL-\d+$")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=False).stdout


def commits():
    # git ignores --follow when combined with --reverse, so reverse here.
    out = git("log", "--follow", "--format=%h\t%cI\t%s", "--", PATHS[0])
    for line in reversed(out.splitlines()):
        h, date, subj = line.split("\t", 2)
        yield h, date[:10], subj


def load(h):
    for p in PATHS:
        txt = git("show", f"{h}:{p}")
        if txt:
            return parse(txt)
    return {}


def parse(txt):
    rows, cols = {}, None
    for line in txt.splitlines():
        cells = line.split("\t")
        if cells[0] == "Pred_ID":
            cols = {c.strip(): i for i, c in enumerate(cells)}
            continue
        if cols is None or not ID.match(cells[0].strip()):
            continue

        def get(name):
            i = cols.get(name)
            return cells[i].strip() if i is not None and i < len(cells) else ""

        rows[cells[0].strip()] = {
            "status": get("Status"),
            "conf": conf(get("Confidence")),
            "timeframe": get("Timeframe"),
            "text": get("Prediction"),
        }
    return rows


def conf(cell):
    m = PCT.search(cell)
    return float(m.group(1)) if m else None


def numset(text):
    return sorted(set(NUM.findall(re.sub(r"CRL-\d+|20\d\d-\d\d-\d\d", "", text))))


def short(s, n=90):
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[: n - 1] + "…"


# Outcome per row as of 2026-09-24. H = hit, M = miss; PROV = provisional (still OPEN).
OUTCOME = {
    "CRL-01": "M", "CRL-02": "H", "CRL-03": "M", "CRL-04": "H", "CRL-05": "M PROV (tracking MISS at void)",
    "CRL-06": "H", "CRL-07": "M", "CRL-08": "M PROV (sustained bar unreachable, WQ-281)", "CRL-09": "M",
    "CRL-10": "M PROV", "CRL-11": "M", "CRL-12": "M PROV", "CRL-13": "H PROV", "CRL-14": "? (retired)",
    "CRL-16": "M", "CRL-17": "M PROV", "CRL-18": "H", "CRL-19": "? (MIXED)", "CRL-21": "M PROV",
    "CRL-24": "M", "CRL-26": "H", "CRL-30": "M PROV",
}

# Hand classification for every non-REPRICE event: (date, pred_id, event) ->
# (class, thesis_dir, benefit_final, benefit_asmade, note)
OVERRIDES = {
    ("2026-03-09", "CRL-02", "STATUS"): ("RESOLUTION", "", "", "", "resolved on a cited 7.1% later found to be 6.9% (see 04-02)"),
    ("2026-03-27", "CRL-07", "TIMEFRAME"): ("WINDOW", "FOR", "HELPS", "HELPS", "extension May-Jun -> Jun-Aug (+2mo); row MISSED 9/1 anyway"),
    ("2026-03-31", "CRL-01", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-04-02", "CRL-02", "STATUS"): ("DISPOSITION", "FOR", "HELPS", "HELPS", "kept CONFIRMED* after verified peak 6.9% vs >7.0% bar; strict letter = MISSED (as-made 70%: 0.09 vs 0.49)"),
    ("2026-04-02", "CRL-08", "TIMEFRAME"): ("WINDOW", "FOR", "HELPS", "HELPS", "extension #1: Mar20-Apr5 -> May (window expired unmet)"),
    ("2026-04-17", "CRL-04", "STATUS"): ("ANNOTATION", "", "", "", "OPEN-NEAR CONFIRMED label"),
    ("2026-04-19", "CRL-08", "TIMEFRAME"): ("WINDOW", "FOR", "HELPS", "HELPS", "extension #2: May -> May-Jun"),
    ("2026-05-03", "CRL-19", "STATUS"): ("DISPOSITION", "FOR", "HELPS", "HELPS", "recorded MIXED; own note: strict-def MISSED floor (3.2% vs 3.3-3.5% range)"),
    ("2026-05-29", "CRL-08", "TIMEFRAME"): ("ANNOTATION", "", "", "", "re-armed note, same window"),
    ("2026-05-29", "CRL-18", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-05-29", "CRL-09", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-06-08", "CRL-10", "TIMEFRAME"): ("ANNOTATION", "", "", "", "'possibly pulling forward' note; reverted 6/11"),
    ("2026-06-09", "CRL-04", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-06-11", "CRL-08", "TIMEFRAME"): ("WINDOW", "FOR", "HELPS", "HELPS", "extension #3: May-Jun -> Jun-Jul"),
    ("2026-06-11", "CRL-10", "TIMEFRAME"): ("ANNOTATION", "", "", "", "reverts 6/08 note"),
    ("2026-06-14", "CRL-08", "TIMEFRAME"): ("ANNOTATION", "", "", "", "re-test failed note"),
    ("2026-06-22", "CRL-08", "TIMEFRAME"): ("ANNOTATION", "", "", "", "DEAD-reinforced note"),
    ("2026-06-26", "CRL-25", "CONF"): ("DISPOSITION", "", "", "", "part of the 06-26 re-scope; counted on the SPEC row"),
    ("2026-06-26", "CRL-25", "TIMEFRAME"): ("ANNOTATION", "", "", "", "part of the 06-26 re-scope"),
    ("2026-06-26", "CRL-25", "SPEC"): ("DISPOSITION", "", "UNDETERMINED", "UNDETERMINED", "registered 30% same day then re-scoped to a pointer (BROCK owns count), leaving CARL scoring; if BROCK's gate count reached 2, removal avoided a HIT at 30% (0.49)"),
    ("2026-07-02", "CRL-03", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-07-02", "CRL-08", "TIMEFRAME"): ("ANNOTATION", "", "", "", "DEEPENED note"),
    ("2026-07-02", "CRL-11", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-07-02", "CRL-13", "TIMEFRAME"): ("WINDOW", "FOR", "HELPS", "HELPS", "Oct-1 window re-read as FIRST-TRANCHE; full population into Q1 2027 (extension, PROV)"),
    ("2026-07-10", "CRL-24", "TIMEFRAME"): ("ANNOTATION", "", "", "", "ALLY date correction"),
    ("2026-07-16", "CRL-06", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-07-18", "CRL-22", "TIMEFRAME"): ("ANNOTATION", "", "", "", "follows v2 re-spec"),
    ("2026-07-18", "CRL-22", "SPEC"): ("RESPEC", "AGAINST", "HURTS", "HURTS", "v1->v2 (Will-approved, POLLY-found): v1 H2-avg legs would fire mechanically in ANY year on seasonality; re-spec removed a near-certain HIT"),
    ("2026-07-24", "CRL-08", "TIMEFRAME"): ("WINDOW", "FOR", "HELPS", "HELPS", "extension #4: Jun-Jul -> Aug-Sep; expired window re-armed, not booked MISSED"),
    ("2026-07-24", "CRL-24", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-07-24", "CRL-26", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-07-24", "CRL-22", "TIMEFRAME"): ("RESPEC", "", "", "", "window move inside v3; counted on the v3 RESPEC row"),
    ("2026-07-24", "CRL-22", "SPEC"): ("RESPEC", "FOR", "HELPS", "HELPS", "v2->v3 (Will-delegated): v2 had no firing path (likely MISS at 45-55); replaced by a NEW claim at 60, old claim never scored"),
    ("2026-07-24", "CRL-07", "TIMEFRAME"): ("WINDOW", "AGAINST", "HURTS", "HURTS", "'force a call by 8/31, do not roll again' - forecloses further deferral"),
    ("2026-07-31", "CRL-14", "CONF"): ("DISPOSITION", "", "", "", "folded into the 07-31 retirement"),
    ("2026-07-31", "CRL-14", "STATUS"): ("DISPOSITION", "FOR", "HELPS", "HELPS", "STUCK -> RETIRED (Will: 'yes register' CRL-28): unresolvable in window, NOT scored (as-made 65%: a forced MISS = 0.42)"),
    ("2026-07-31", "CRL-28", "SPEC"): ("ANNOTATION", "", "", "", "registration-day wording fix (2x rationale vs 55/day trigger); pre-data"),
    ("2026-08-10", "CRL-16", "STATUS"): ("RESOLUTION", "", "", "", "forced call MISSED ahead of 8/31 deadline"),
    ("2026-09-01", "CRL-07", "STATUS"): ("RESOLUTION", "", "", "", ""),
    ("2026-09-01", "CRL-23", "SPEC"): ("RESPEC", "AGAINST", "HURTS", "HURTS", "parenthesised to (A OR B) AND C - the stricter reading; ~nil in practice, leg C already live"),
    ("2026-09-10", "CRL-03", "CONF"): ("RECORD-CORRECTION", "", "HURTS", "HURTS", "as-made re-mark 72->90 on a MISSED row (DAEDALUS H2)"),
    ("2026-09-10", "CRL-04", "CONF"): ("RECORD-CORRECTION", "", "HURTS", "HURTS", "as-made re-mark 98->88 on a CONFIRMED row"),
    ("2026-09-10", "CRL-06", "CONF"): ("RECORD-CORRECTION", "", "HURTS", "HURTS", "as-made re-mark 78->70 on a CONFIRMED row"),
    ("2026-09-10", "CRL-11", "CONF"): ("RECORD-CORRECTION", "", "HURTS", "HURTS", "as-made re-mark 83->85 on a MISSED row"),
    # 4-tuple keys (…, new value) disambiguate two same-type events on one row and date.
    ("2026-07-31", "CRL-14", "STATUS", "STUCK"): ("ANNOTATION", "", "", "", "intermediate STUCK label; the decision is the RETIRED row"),
    ("2026-07-24", "CRL-22", "CONF", "60.0"): ("RESPEC", "", "", "", "confidence of the NEW v3 claim; counted with the v3 RESPEC row"),
    ("2026-09-10", "CRL-05", "STATUS"): ("DISPOSITION", "AGAINST", "HURTS", "HELPS", "NO-VERDICT-BY-BASIS (NY Fed primary). CONVENTION-DEPENDENT: final mark 20% forfeits a 0.04 MISS; as-made 75% avoids a 0.5625 MISS"),
}


def outcome(pid):
    o = OUTCOME.get(pid, "?")
    return o[0] if o[0] in "HM" else "?", "PROV" in o


def classify(pid, event, date, d, new=""):
    for key in ((date, pid, event, new), (date, pid, event)):
        if key in OVERRIDES:
            return OVERRIDES[key]
    if event == "REGISTERED":
        return ("REGISTRATION", "", "", "", "")
    if event == "TEXT":
        return ("ANNOTATION", "", "", "", "text-only rewrite")
    if event == "CONF" and d:
        dv = float(d)
        o, prov = outcome(pid)
        tdir = "FOR" if dv > 0 else "AGAINST"
        if o == "?":
            ben = "UNDETERMINED"
        else:
            toward = (dv < 0 and o == "M") or (dv > 0 and o == "H")
            ben = ("HELPS" if toward else "HURTS") + (" PROV" if prov else "")
        return ("REPRICE", tdir, ben, "NEUTRAL", "")
    return ("UNCLASSIFIED", "", "", "", "no override - classify by hand")


def main():
    cls = "--classify" in sys.argv
    head = ["date", "commit", "pred_id", "event", "old", "new", "delta_pp", "commit_subject"]
    if cls:
        head += ["class", "thesis_dir", "benefit_final", "benefit_asmade", "note"]
    print("\t".join(head))
    prev = {}
    n = 0
    for h, date, subj in commits():
        cur = load(h)
        if not cur:
            continue
        for pid in sorted(set(prev) | set(cur), key=lambda x: int(x.split("-")[1])):
            a, b = prev.get(pid), cur.get(pid)
            ev = []
            if a is None and b is not None:
                ev.append(("REGISTERED", "", f"{b['conf']}", ""))
            elif b is None:
                ev.append(("REMOVED", a["status"], "", ""))
            else:
                if a["conf"] != b["conf"]:
                    d = "" if None in (a["conf"], b["conf"]) else f"{b['conf'] - a['conf']:+g}"
                    ev.append(("CONF", f"{a['conf']}", f"{b['conf']}", d))
                if a["status"] != b["status"]:
                    ev.append(("STATUS", a["status"], b["status"], ""))
                if a["timeframe"] != b["timeframe"]:
                    ev.append(("TIMEFRAME", short(a["timeframe"]), short(b["timeframe"]), ""))
                if a["text"] != b["text"]:
                    kind = "SPEC" if numset(a["text"]) != numset(b["text"]) else "TEXT"
                    ev.append((kind, short(a["text"]), short(b["text"]), ""))
            for e in ev:
                n += 1
                row = [date, h, pid, *e, short(subj, 120)]
                if cls:
                    row += list(classify(pid, e[0], date, e[3], e[2]))
                print("\t".join(row))
        prev = cur
    print(f"# {n} events", file=sys.stderr)


if __name__ == "__main__":
    main()
