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


ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                      check=False).stdout.strip()


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True, check=False).stdout


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
            "inval": get("Invalidation"),
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


# ---------------------------------------------------------------------------
# CLASSIFICATION (v1, 2026-09-24 eve, after an adversarial Opus challenge pass).
# Two books, per FORGE/PREDICTION_DISCIPLINE.md WQ-112:
#   scored     = the LATEST DATED pre-resolution mark governs (WQ-112 i); an
#                undated re-mark does not score (WQ-112 ii)
#   firstcall  = the as-made (Date_Made) confidence; reprices and as-made
#                restorations are NEUTRAL here by construction
# A trailing "*" = ex-ante only: the move changed the odds but realised nothing.
# initiator: CARL includes CARL's sub-agents (POLLY/PHAN/STUE), HOMER-supplied
# data where CARL made the call, and Will-approved/-directed CARL calls.
# OUTSIDE = a mechanical restoration another desk ran (DAEDALUS H2).
# ---------------------------------------------------------------------------

# Outcome per row as of 2026-09-24. H = hit, M = miss, ? = never scored / mixed.
# PROV = still OPEN; basis is CARL's own current confidence (<=25 M, >=75 H).
OUTCOME = {
    "CRL-01": "M", "CRL-02": "H", "CRL-03": "M", "CRL-04": "H", "CRL-05": "? (voided, never scored)",
    "CRL-06": "H", "CRL-07": "M", "CRL-08": "M PROV (sustained bar unreachable, WQ-281)", "CRL-09": "M",
    "CRL-10": "M PROV", "CRL-11": "M", "CRL-12": "M PROV", "CRL-13": "H PROV", "CRL-14": "? (retired)",
    "CRL-16": "M", "CRL-17": "M PROV", "CRL-18": "H", "CRL-19": "? (MIXED)", "CRL-21": "M PROV",
    "CRL-24": "M", "CRL-26": "H", "CRL-30": "M PROV",
}

R = "RESOLUTION"
A = ("ANNOTATION", "", "", "", "", "")
# (date, pred_id, event[, new]) -> (class, initiator, thesis_dir, benefit_scored, benefit_firstcall, note)
OVERRIDES = {
    # --- resolutions graded strictly on their letter (challenge pass checked 01/03/09/11/18/24; 04 asterisk dropped on evidence)
    ("2026-03-31", "CRL-01", "STATUS"): (R, "", "", "", "", ""),
    ("2026-05-29", "CRL-09", "STATUS"): (R, "", "", "", "", ""),
    ("2026-05-29", "CRL-18", "STATUS"): (R, "", "", "", "", ""),
    ("2026-06-09", "CRL-04", "STATUS"): (R, "", "", "", "", ""),
    ("2026-07-02", "CRL-03", "STATUS"): (R, "", "", "", "", "invalidation honoured (contrast CRL-08 July)"),
    ("2026-07-02", "CRL-11", "STATUS"): (R, "", "", "", "", ""),
    ("2026-07-24", "CRL-24", "STATUS"): (R, "", "", "", "", ""),
    ("2026-03-09", "CRL-02", "STATUS"): (R, "", "", "", "", "resolved on a cited 7.1%; see the 04-02 disposition"),
    # --- discretionary grading calls
    ("2026-04-02", "CRL-02", "STATUS"): ("DISPOSITION", "CARL", "FOR", "HELPS", "HELPS", "kept CONFIRMED* on 6.9% vs a >7.0% bar; registered 'Currently 6.9%' and resolved 3/09 for a Q2 window not yet open; Feb later 6.80% (KB-CARL-359). Honest alt = NO-VERDICT, so the stake is a 0.09 HIT kept vs unscored"),
    ("2026-05-03", "CRL-19", "STATUS"): ("DISPOSITION", "CARL", "FOR", "HELPS", "HELPS", "recorded MIXED though own note says strict-def MISSED; CRL-01, same pattern, was booked MISSED. Also a post-data registration: registered 5/01 after March PCE printed 4/30"),
    ("2026-07-16", "CRL-06", "STATUS"): ("DISPOSITION", "CARL", "FOR", "HELPS", "HELPS", "SERIES SWAP AT RESOLUTION: registered on NY Fed/Equifax notations (58,140 Q4, KB-CARL-024; 59K Q1, never 70K), CONFIRMED on ATTOM starts, already ~78K/qtr at Made_Date (Feb 25,928, VX-CARL-FC-01). finding_rebased_metric_check_made_date => retire, no credit. First-call 70: 0.09 HIT kept vs unscored"),
    ("2026-07-24", "CRL-26", "STATUS"): ("DISPOSITION", "CARL", "FOR", "HELPS", "HELPS", "PENDING AAA CHECK: letter names AAA >=$4.00 by 7/20; graded on EIA GASREGW 4.001 (w/e 7/20, FRED-verified) + GasBuddy; no in-window AAA >=4.00 documented (AAA 3.992 on 7/18)"),
    ("2026-08-10", "CRL-16", "STATUS"): ("DISPOSITION", "CARL", "AGAINST", "HURTS", "HURTS", "graded MISSED on an UNPUBLISHED series; canon WQ-162 = NO-VERDICT. Hurts at first-call 60 (0.36); on CARL's published undated 35% it scores 0.1225 and HELPS the aggregate"),
    ("2026-09-01", "CRL-07", "STATUS"): ("DISPOSITION", "CARL", "AGAINST", "HURTS", "HURTS", "graded MISSED with NO NUMERIC BAR; canon WQ-162 = NO-VERDICT. Hurts at first-call 80 (0.64); on CARL's published undated 40% it scores 0.16 and HELPS the aggregate"),
    ("2026-05-29", "CRL-08", "TIMEFRAME"): ("DISPOSITION", "CARL", "AGAINST", "NEUTRAL", "HURTS", "DECLINED A TOUCH: EIA GASREGW w/e 5/11 = $4.500 (FRED-verified), AAA peak $4.564 5/21; letter said 'hit $4.50+', no sustained clause on the confirm side (sustained entered via the 4/02 Invalidation; ratified only 9/24 WQ-281). First-call: HIT at 85 = 0.0225 vs MISS 0.7225 (+0.70). Scored: HIT at 92 0.0064 vs MISS at 7 0.0049"),
    ("2026-07-31", "CRL-14", "STATUS", "STUCK"): A,
    ("2026-07-31", "CRL-14", "STATUS"): ("DISPOSITION", "CARL", "REMOVES", "UNDETERMINED", "UNDETERMINED", "RETIRED, not scored (STUE; Will 'yes register' CRL-28). At 55% the row was UNDETERMINED; canon alt was STUCK, not a forced MISS"),
    ("2026-09-10", "CRL-05", "STATUS"): ("DISPOSITION", "CARL", "REMOVES", "HELPS", "HELPS", "NO-VERDICT-BY-BASIS, right on the merits (NY Fed primary 8/11; PHAN found). The 20% mark is UNDATED, so under WQ-112 ii first-call 75 governs: a MISS scoring 0.5625 was removed. CARL's 9/10 'the void costs me a good score' is withdrawn"),
    ("2026-06-26", "CRL-25", "SPEC"): ("DISPOSITION", "CARL", "REMOVES", "UNDETERMINED", "UNDETERMINED", "registered at 30% and re-scoped the SAME DAY to a pointer (BROCK owns the count); left CARL scoring. BROCK shows a Q2 gate wave under way, so 'already met at registration' is possible"),
    ("2026-06-26", "CRL-25", "CONF"): ("DISPOSITION", "", "", "", "", "part of the 06-26 re-scope; counted on the SPEC row"),
    ("2026-06-26", "CRL-25", "TIMEFRAME"): A,
    ("2026-06-26", "CRL-25", "INVALIDATION"): A,
    # --- windows
    ("2026-03-27", "CRL-07", "TIMEFRAME"): ("WINDOW", "CARL", "FOR", "HELPS*", "HELPS*", "extension May-Jun -> Jun-Aug; missed anyway 9/1"),
    ("2026-04-02", "CRL-08", "TIMEFRAME"): ("WINDOW", "CARL", "FOR", "HELPS", "HELPS*", "extension #1 Mar20-Apr5 -> May, window expired unmet. Realised on the scored book: it let an 85 row be walked to a dated 7 (0.7225 -> 0.0049)"),
    ("2026-04-19", "CRL-08", "TIMEFRAME"): ("WINDOW", "CARL", "FOR", "HELPS", "HELPS*", "extension #2 -> May-Jun"),
    ("2026-06-11", "CRL-08", "TIMEFRAME"): ("WINDOW", "CARL", "FOR", "HELPS", "HELPS*", "extension #3 -> Jun-Jul"),
    ("2026-07-24", "CRL-08", "TIMEFRAME"): ("WINDOW", "CARL", "FOR", "HELPS", "HELPS*", "extension #4 -> Aug-Sep, of a row whose own kill clause had ALREADY FIRED (see ~07-06)"),
    ("2026-07-02", "CRL-13", "TIMEFRAME"): ("WINDOW", "CARL", "FOR", "HELPS*", "HELPS*", "Oct-1 window re-read as a first tranche; full population into Q1 2027"),
    ("2026-07-24", "CRL-07", "TIMEFRAME"): ("WINDOW", "CARL", "AGAINST", "HURTS*", "HURTS*", "'force a call by 8/31, do not roll again' (Will-directed Brier audit)"),
    # --- specs and kill clauses
    ("2026-04-02", "CRL-08", "INVALIDATION"): ("RESPEC", "CARL", "FOR", "HELPS*", "HELPS*", "KILL CLAUSE LOOSENED: 'Brent below $80 before Mar 20' -> 'below $80 sustained 2 weeks', same commit as extension #1"),
    ("2026-07-18", "CRL-22", "SPEC"): ("RESPEC", "CARL", "AGAINST", "HURTS", "HURTS", "v1 -> v2 (POLLY, a CARL sub-agent, found it; Will approved): v1 would fire in ANY year on seasonality, so a near-certain HIT was removed"),
    ("2026-07-18", "CRL-22", "CONF"): ("RESPEC", "", "", "", "", "v2 claim's confidence; counted on the v2 RESPEC row"),
    ("2026-07-18", "CRL-22", "TIMEFRAME"): A,
    ("2026-07-18", "CRL-22", "INVALIDATION"): A,
    ("2026-07-24", "CRL-22", "SPEC"): ("RESPEC", "CARL", "FOR", "UNDETERMINED", "UNDETERMINED", "v2 -> v3 (Will-delegated): v2 had no firing path, a resolvability defect (canon: STATUS, not MISS); replaced by a new claim at 60, v2 never scored"),
    ("2026-07-24", "CRL-22", "CONF", "60.0"): ("RESPEC", "", "", "", "", "v3 claim's confidence; counted on the v3 RESPEC row"),
    ("2026-07-24", "CRL-22", "TIMEFRAME"): ("RESPEC", "", "", "", "", "window move inside v3"),
    ("2026-07-24", "CRL-22", "INVALIDATION"): A,
    ("2026-09-01", "CRL-23", "SPEC"): ("RESPEC", "CARL", "AGAINST", "HURTS*", "HURTS*", "parenthesised to (A OR B) AND C, stricter than conventional precedence; DAEDALUS flagged, CARL ruled the reading. Leg C runs 'through Q4 2026', not yet met"),
    ("2026-09-10", "CRL-27", "CONF"): ("RESPEC", "CARL", "AGAINST", "HURTS*", "HURTS*", "leg (a) struck as basis-refuted (PHAN finding). ⚠ Prediction+Invalidation text STILL carry the 13.74% leg: the row has two readings until the letter is fixed"),
    ("2026-07-31", "CRL-28", "SPEC"): A,
    ("2026-08-03", "CRL-28", "INVALIDATION"): A,
    ("2026-03-09", "CRL-01", "INVALIDATION"): A,
    ("2026-03-09", "CRL-02", "INVALIDATION"): A,
    # --- record corrections
    ("2026-07-24", "CRL-15", "CONF"): ("RECORD-CORRECTION", "CARL", "AGAINST", "UNDETERMINED", "NEUTRAL", "65 -> 35 MONOTONICITY fix across ledgers, not an evidence move"),
    ("2026-09-10", "CRL-03", "CONF"): ("RECORD-CORRECTION", "OUTSIDE", "", "HURTS", "NEUTRAL", "DAEDALUS H2 as-made restoration 72 -> 90; reverses the earlier -18 helping reprice (nets to zero with it)"),
    ("2026-09-10", "CRL-04", "CONF"): ("RECORD-CORRECTION", "OUTSIDE", "", "HURTS", "NEUTRAL", "H2 restoration 98 -> 88; reverses +7 +2 +1"),
    ("2026-09-10", "CRL-06", "CONF"): ("RECORD-CORRECTION", "OUTSIDE", "", "HURTS", "NEUTRAL", "H2 restoration 78 -> 70; reverses +8"),
    ("2026-09-10", "CRL-11", "CONF"): ("RECORD-CORRECTION", "OUTSIDE", "", "HURTS", "NEUTRAL", "H2 restoration 83 -> 85; reverses -2"),
    ("2026-07-31", "CRL-14", "CONF"): None,  # plain reprice (the cell calls it 'the genuine world-update')
    # --- 2026-09-24 re-grades applied from this ledger's own findings (Will: "approve all six with your leans")
    ("2026-09-24", "CRL-06", "STATUS"): ("RECORD-CORRECTION", "CARL", "REMOVES", "HURTS", "HURTS", "RE-GRADE CONFIRMED -> RETIRED, no credit (series swap); removes a 0.09 HIT"),
    ("2026-09-24", "CRL-02", "STATUS"): ("RECORD-CORRECTION", "CARL", "REMOVES", "HURTS", "HURTS", "RE-GRADE CONFIRMED* -> NO-VERDICT; removes a 0.09 HIT"),
    ("2026-09-24", "CRL-26", "STATUS"): ("RECORD-CORRECTION", "CARL", "REMOVES", "HURTS", "HURTS", "RE-GRADE CONFIRMED -> NO-VERDICT (no in-window AAA print); removes a 0.09 HIT"),
    ("2026-09-24", "CRL-07", "CONF"): ("RECORD-CORRECTION", "CARL", "", "HURTS", "NEUTRAL", "undated 40% -> first-call 80 (WQ-112 ii): 0.16 -> 0.64 on the published record"),
    ("2026-09-24", "CRL-09", "CONF"): ("RECORD-CORRECTION", "CARL", "", "HURTS", "NEUTRAL", "undated 73% (walked 4/06) -> first-call 75 (WQ-112 ii): 0.5329 -> 0.5625"),
    ("2026-09-24", "CRL-16", "CONF"): ("RECORD-CORRECTION", "CARL", "", "HURTS", "NEUTRAL", "undated 35% -> first-call 60 (WQ-112 ii): 0.1225 -> 0.36 on the published record"),
    ("2026-04-17", "CRL-04", "STATUS"): A,
    ("2026-06-08", "CRL-10", "TIMEFRAME"): A,
    ("2026-06-11", "CRL-10", "TIMEFRAME"): A,
    ("2026-06-14", "CRL-08", "TIMEFRAME"): A,
    ("2026-06-22", "CRL-08", "TIMEFRAME"): A,
    ("2026-07-02", "CRL-08", "TIMEFRAME"): A,
    ("2026-07-10", "CRL-24", "TIMEFRAME"): A,
}

# Calls that never reached the TSV as an event (found by the 9/24 challenge pass).
MANUAL = [
    ("2026-07-06", "manual", "CRL-08", "INVALIDATION-FIRED", "", "", "", "not in TSV: kill clause met, never applied",
     ("DISPOSITION", "CARL", "FOR", "HELPS", "NEUTRAL", "KILL CLAUSE FIRED, NOT BOOKED: FRED DCOILBRENTEU < $80 every trading day 6/22 ($76.49) to 7/10 ($74.34), 15 sessions, low $68.53 7/02 (verified 9/24). CARL cut 40 -> 28 're-arm, not miss' and extended 7/24. Scored: booked then at 28 = 0.0784 vs 0.0049 at the eventual dated 7")),
    ("2026-09-10", "manual", "CRL-07/16", "REMARK-WITHHELD", "", "", "", "not in TSV: as-made triage",
     ("RECORD-CORRECTION", "CARL", "", "HELPS", "NEUTRAL", "9/10 H2 triage left CRL-07 (40%, undated) and CRL-16 (35%, undated) at walked marks. Canon WQ-112 ii already scores both at first-call (80-85 / 60), so the published record is flattered by +0.72 to +0.80 Brier")),
] + [
    ("2026-09-10", "manual", pid, "ASMADE-ANNOTATED", "", "", "", "not in TSV as an event: leading % unchanged",
     ("RECORD-CORRECTION", "OUTSIDE", "", "NEUTRAL", "NEUTRAL", "H2 as-made value written into the cell after the leading mark"))
    for pid in ("CRL-05", "CRL-10", "CRL-12", "CRL-13", "CRL-17", "CRL-20")
]


def outcome(pid):
    o = OUTCOME.get(pid, "?")
    return o[0] if o[0] in "HM" else "?", "PROV" in o


def classify(pid, event, date, d, new=""):
    for key in ((date, pid, event, new), (date, pid, event)):
        if key in OVERRIDES:
            if OVERRIDES[key] is None:
                break
            return OVERRIDES[key]
    if event == "REGISTERED":
        return ("REGISTRATION", "", "", "", "", "")
    if event == "TEXT":
        return ("ANNOTATION", "", "", "", "", "text-only rewrite")
    if event == "CONF" and d:
        dv = float(d)
        o, prov = outcome(pid)
        tdir = "FOR" if dv > 0 else "AGAINST"
        if o == "?":
            ben = "UNDETERMINED"
        else:
            toward = (dv < 0 and o == "M") or (dv > 0 and o == "H")
            ben = ("HELPS" if toward else "HURTS") + (" PROV" if prov else "")
        return ("REPRICE", "CARL", tdir, ben, "NEUTRAL", "")
    return ("UNCLASSIFIED", "", "", "", "", "no override - classify by hand")


def main():
    cls = "--classify" in sys.argv
    head = ["date", "commit", "pred_id", "event", "old", "new", "delta_pp", "commit_subject"]
    if cls:
        head += ["class", "initiator", "thesis_dir", "benefit_scored", "benefit_firstcall", "note"]
    print("\t".join(head))
    out = []
    prev = {}
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
                if a["inval"] != b["inval"]:
                    ev.append(("INVALIDATION", short(a["inval"]), short(b["inval"]), ""))
                if a["text"] != b["text"]:
                    kind = "SPEC" if numset(a["text"]) != numset(b["text"]) else "TEXT"
                    ev.append((kind, short(a["text"]), short(b["text"]), ""))
            for e in ev:
                row = [date, h, pid, *e, short(subj, 120)]
                if cls:
                    row += list(classify(pid, e[0], date, e[3], e[2]))
                out.append(row)
        prev = cur
    if cls:
        for m in MANUAL:
            out.append(list(m[:8]) + list(m[8]))
        out.sort(key=lambda r: r[0])  # stable: TSV order kept within a date
    for row in out:
        print("\t".join(row))
    print(f"# {len(out)} events", file=sys.stderr)


if __name__ == "__main__":
    main()
