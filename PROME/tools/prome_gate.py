#!/usr/bin/env python3
"""
prome_gate.py — PROME's boot/closeout gate: every mechanical check, one verdict block.

WHY (DAEDALUS T2-b, Will-approved 2026-07-28): PROME's protocol mass exceeded
single-session execution capacity — root steps 1c/1d were adopted the same
morning a closeout shipped malformed allowlist rows. Checks kept landing in
PROSE, which competes for session attention; this script is where they land
instead. NEW FLEET-WIDE CHECKS GET ADDED HERE, NOT TO BOOT/CLOSEOUT PROSE.
Precedent: HENRY/LABOR boot.py.

DESIGN CONSTRAINTS (Will-approved, in the 7/28 disposition packet):
  1. ADVISORY vs BLOCKING classes are PRESERVED, never flattened. orphan_check
     and consumer_check are advisory BY DESIGN; flattening everything into one
     FAIL trains alarm fatigue — the disease this program treats. rc=1 only on
     BLOCKING failures.
  2. Every wrapped check stays INDEPENDENTLY RUNNABLE — this is a thin shell
     dispatcher, not a monolith. Each failure prints the owner doc to read.
  3. The T3-a MECHANICAL CORE lives here (dashboard-state emptiness/vintage,
     GATES token vocabulary + ages, DOCKET overdue rows, boot↔closeout symmetry
     diff) so scriptable checks run EVERY BOOT — DAEDALUS's ~21d external sweep
     keeps only the judgment tail a script cannot do.

USAGE
  python3 PROME/tools/prome_gate.py boot        # BOOT.md step-0/3/5 mechanical stack
  python3 PROME/tools/prome_gate.py closeout    # closeout-tail mechanical stack
  (always from repo root: cd "$(git rev-parse --show-toplevel)" first — PAT-031)

rc=0 all blocking gates pass (advisories may still print — read them);
rc=1 at least one BLOCKING gate failed — disposition before proceeding;
rc=2 INCOMPLETE — one or more checks did NOT RUN, so their subjects are UNKNOWN.
     Never read as a pass, and NOT the same as rc=1: 1 means "we looked and found a
     problem", 2 means "we did not look". rc=2 outranks rc=1 when both apply.
     (Added with the L294 F-7 isolation repair; this block documented only 0 and 1.)

MANUAL-JUDGMENT STEPS THIS SCRIPT DOES NOT REPLACE (closeout): memory_index_check
--slug (needs the session's slugs) · consumer_check --old/--new (needs the
superseded values) · the HANDOFF/SCRATCH judgment writes. It prints reminders.
"""
import argparse
import csv
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = None
SESSION_JSON = None

GATES_STATES = ("LIVE", "FIRED-UNEXECUTED", "RESOLVED", "LAPSED", "RETIRED")
# GATES_AGE_DAYS retired 8/9 — the >5d raw-age rule was RETIRED by the 8/7
# consumed_by ruling (forum S2/ABN, Will-adopted); staleness keys on consumed_by.
DASH_STALE_HOURS = 72       # dashboard self-declares red past this

# Desk catalyst-summons registry (BD-02, LABOR ask 2026-08-20 — three misses:
# a frozen card only grades if a session runs, and nothing summons a session on
# a catalyst date; an external DAEDALUS sweep beat the desk's own boot by 3d).
# PROME boots regularly — this check reads each registered desk's machine
# catalyst ledger and surfaces due/past-due rows. Since WQ-184 (2026-09-05) a
# flag means "this desk needs a session and L0 says PROME spawns it" (DOCKET-
# registered rows go through spawn_list.py; this stays for desk-private
# ledgers), NEVER an instruction to grade on the owner's behalf. v1 cohort = desks that asked and
# keep the 8-col CATALYSTS schema (date/event/.../priority); add rows HERE.
SUMMONS_LEDGERS = {
    "LABOR": "AGENTS/LABOR/docket/CATALYSTS.tsv",
}
SUMMONS_WINDOW_DAYS = 2     # due within N days flags; past-due always flags
                            # (owners prune fired rows, so past-due-still-present
                            # reads as ungraded — the exact BD-02 miss shape)

BLOCK, ADVISE = "BLOCKING", "advisory"
# ERROR (L294 F-7, reproduced 2026-09-12): a check that DID NOT RUN. Before this,
# inputs were dereferenced outside any try and main() wrapped nothing, so ONE missing
# file — PROME/CLOSEOUT.md, say — raised out of the whole gate: stdout completely
# EMPTY, zero verdict lines, no summary, and the ~20 checks that had already passed
# lost with it. rc was 1, the same code a legitimate blocking failure returns, so a
# gate that evaluated NOTHING was indistinguishable from a gate that evaluated
# everything and found a problem.
#   * ERROR names the check that failed and why. It never substitutes a default so a
#     dependent check can proceed — a fabricated input buys a verdict nobody can trust.
#   * Checks that do not need the missing input still run; isolation is per-check.
#   * ANY error makes the run INCOMPLETE and rc=2 ("could not establish",
#     AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md §9). Never PASS, and distinct from
#     BLOCKED so a caller can tell "we found a problem" from "we did not look".
ERROR = "ERROR"
# CAPABILITY (WQ-239, Will-directed 2026-09-12): a machine capability — a credential, a
# feed, a tool — that some workflows need and others do not.
#   * It NEVER contributes to rc. No state of this class gates work that does not use it.
#     (env_doctor was BLOCK until today; BLOCK means "disposition before proceeding" for
#     ALL work, so a missing NASA key stopped a process edit. That is the defect.)
#   * It is reported at EVERY run until RESTORED — permanence of the report, not severity,
#     is what keeps it from going quiet. FFIEC creds sat missing from 2026-08-07 while
#     classified BLOCKING, so severity was never the binding constraint.
#   * THREE states, never two (Will 2026-09-12 20:49). UNKNOWN is not UNAVAILABLE and is
#     not AVAILABLE: a crash, an unreadable config or an unrecognised rc means the check
#     did not establish anything. Both UNAVAILABLE and UNKNOWN withhold dependent claims;
#     only AVAILABLE permits them. `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`
#   * AVAILABLE means PRESENT, never AUTHENTICATED. Presence of a key does not prove the
#     credential works; the point of use stays the authority.
CAPABILITY = "capability"
CAP_AVAILABLE, CAP_UNAVAILABLE, CAP_UNKNOWN = "AVAILABLE", "UNAVAILABLE", "UNKNOWN"
# Per-key dependent workflows. A capability probe covers MANY keys; reporting the union
# of every dependent whenever ANY key is missing overstates the blast radius (external
# review 2026-09-12: "any environment failure prints the same withheld-workflow list,
# including FRED/EIA—even when only FFIEC or NASA credentials are missing").
KEY_DEPENDENTS = {
    "FFIEC_CDR_TOKEN":    "FFIEC call-report pulls (WAL MI3)",
    "FFIEC_CDR_USERNAME": "FFIEC call-report pulls (WAL MI3)",
    "FIRMS_MAP_KEY":      "NASA FIRMS hotspot grading (FALCON/OSPREY strike claims)",
    "FRED_API_KEY":       "FRED series pulls (rates/credit officials)",
    "EIA_API_KEY":        "EIA weekly petroleum pulls (Cushing/SPR)",
    "PJM_API_KEY":        "PJM load/price pulls (WATT)",
    "ESTAT_APPID":        "Japan e-Stat CPI pulls (SAM)",
}
# A probe exits non-zero both when it CONFIRMS a gap and when it FAILS to evaluate.
# rc alone cannot tell those apart (an unreadable config and three missing keys are
# both rc=1 from env_doctor), so the output decides: a recognised finding line means
# the probe reached a verdict; a traceback or no recognisable finding means it did not.
# `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]` — unparseable is not
# a behaviour, and the safe direction here is UNKNOWN, never UNAVAILABLE.
FINDING_MARKERS = ("✗", "❌")
PROBE_FAILURE_MARKERS = ("Traceback (most recent call last)", "SyntaxError:", "ImportError:",
                         "ModuleNotFoundError:", "PermissionError:")
results = []                # (severity, name, ok, detail, owner_doc)
capabilities = []           # (name, state, detail, owner_doc, dependents, tracker)



# ---- ONE split + ONE date classifier for the WILL_QUEUE table (2026-09-18, ACCEPTANCE_queue_parsers B1/B3/B4) ----
# Copied verbatim into willq_view.py · prome_gate.py · will_brief.py · decision_deck.py (the gate is a blocking boot
# surface: no import coupling by design); queue_parser_selftest.py asserts the four copies and table_check agree.
_ESCAPED_PIPE = "\x00"


def split_cells(line):
    """table_check.split_cells semantics: `\\|` is a literal pipe, every other pipe separates (code spans included),
    one leading and one trailing pipe are structural. Cells come back stripped."""
    s = line.strip().replace("\\|", _ESCAPED_PIPE)
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.replace(_ESCAPED_PIPE, "\\|").strip() for c in s.split("|")]


_ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
_DATELIKE = re.compile(r"(?<![\w/])\d{1,2}/\d{1,2}(?:/\d{2,4})?(?![\w/])(?!\s+of\b)"      # 9/19 · 9/19/26 — not "2/3 of"
                       r"|\b\d{4}-\d{1,2}-\d{1,2}\b"                                        # 2026-9-19 (unpadded)
                       r"|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}\b"   # Sept 19
                       r"|\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\b"      # 19 Sep
                       r"|\b\d{4}/\d{1,2}/\d{1,2}\b"                                           # 2026/09/19
                       r"|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}\b", re.I)  # May 2026


def datelike_not_iso(raw):
    """B3: a needed-by with NO ISO date but a date-LIKE token. B4 (textual / empty) is its complement."""
    t = re.sub(r"\*\*|`", "", raw or "")
    return not _ISO_DATE.search(t) and bool(_DATELIKE.search(t))


def is_separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-+:?", c) for c in cells)

def record(severity, name, ok, detail, owner):
    results.append((severity, name, ok, detail, owner))


def run_capability(name, cmd, owner, dependents, tracker=None, unavailable_rc=(1,)):
    """Run a capability probe. Returns its state; NEVER affects rc.

    rc 0 -> AVAILABLE (present, not authenticated) · rc in unavailable_rc -> UNAVAILABLE
    · anything else, a crash, or a timeout -> UNKNOWN (the check established nothing).
    `dependents` names the workflows the capability gates AT THE POINT OF USE.
    `tracker` is the WILL_QUEUE row id following the gap up; past its needed-by the
    capability is presented as URGENT — escalation urgency only, never gating."""
    global LOG_DIR
    if LOG_DIR is None:
        LOG_DIR = Path(tempfile.mkdtemp(prefix="prome-gate-checks-"))
    log = LOG_DIR / f"cap-{re.sub(r'[^a-z0-9]+', '-', name.lower())[:60]}.txt"
    try:
        with log.open("x", encoding="utf-8") as output:
            p = subprocess.run(cmd, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT, timeout=120)
        rc = p.returncode
        raw = log.read_text(encoding="utf-8", errors="replace")
        tail = raw.strip().split("\n")
        findings = [l.strip() for l in tail if any(m in l for m in FINDING_MARKERS)]
        crashed = any(m in raw for m in PROBE_FAILURE_MARKERS)
        if rc == 0:
            state, detail = CAP_AVAILABLE, "present (NOT authenticated — the point of use is the authority)"
        elif rc in unavailable_rc and findings and not crashed:
            state = CAP_UNAVAILABLE
            detail = ("; ".join(f[:100] for f in findings[:3])
                      + (f" (+{len(findings) - 3} more)" if len(findings) > 3 else ""))
            named = _named_dependents(findings)
            if named:
                dependents = named          # report only what the MISSING keys gate
        elif rc in unavailable_rc:
            # non-zero, but the probe did not produce a verdict we can read
            state = CAP_UNKNOWN
            detail = ("probe exited {} but produced no readable finding{} — it did not establish "
                      "whether the capability is present".format(
                          rc, " (it crashed mid-run)" if crashed else ""))
        else:
            state, detail = CAP_UNKNOWN, f"unrecognised rc={rc} — the probe established nothing"
    except Exception as e:                       # crash / timeout / unreadable config
        state, detail = CAP_UNKNOWN, f"probe failed: {type(e).__name__}: {str(e)[:90]}"
    capabilities.append((name, state, detail + f"\n       full output: {log}", owner, dependents, tracker))
    return state


def _named_dependents(findings):
    """Dependents of ONLY the keys the probe actually named.

    Three cases, and the MIXED one is the trap: when some findings map to known keys
    and others do not, reporting just the mapped dependents presents a PARTIAL blast
    radius as a complete one. The unmapped findings are carried explicitly instead, so
    an unrecognised key reads as "dependents UNKNOWN", never as "no dependents".
      * nothing mapped      -> "" (caller keeps its declared superset)
      * all mapped          -> exactly those dependents
      * some mapped         -> those dependents + a named UNKNOWN tail
    `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`"""
    hit, unmapped = [], []
    for f in findings:
        keys = [k for k in KEY_DEPENDENTS if k in f]
        if keys:
            hit += [KEY_DEPENDENTS[k] for k in keys]
        else:
            m = re.search(r"\b([A-Z][A-Z0-9]{2,}(?:_[A-Z0-9]+)+)\b", f)
            unmapped.append(m.group(1) if m else f[:40])
    if not hit:
        return ""
    out = " · ".join(dict.fromkeys(hit))
    if unmapped:
        names = ", ".join(dict.fromkeys(unmapped))
        out += f" · ⚠️ dependents UNKNOWN for {len(set(unmapped))} unmapped finding(s): {names}"
    return out


def aggregate_rc(result_rows, capability_rows):
    """The gate's rc, as a pure function, so the contract is testable without running a
    boot. CAPABILITY rows are accepted and deliberately ignored: no capability state
    contributes to rc. Only BLOCKING failures do."""
    if [r for r in result_rows if r[0] == ERROR]:
        return 2      # could not establish: at least one check never ran
    return 1 if [r for r in result_rows if r[0] == BLOCK and not r[2]] else 0


def _tracker_overdue(row_id, today=None, queue_path=None):
    """True if the WILL_QUEUE row following a capability gap is past its needed-by.
    Missing file, missing row or unparseable date -> False: an unreadable tracker
    must not manufacture urgency it cannot establish (category 4, fail visible-not-loud
    — the capability itself is already reported every run)."""
    if not row_id:
        return False
    today = today or dt.date.today()
    try:
        qp = Path(queue_path) if queue_path else (ROOT / "PROME" / "WILL_QUEUE.md")
        for line in qp.read_text(encoding="utf-8").split("\n"):
            cells = split_cells(line)                    # B1 (9/18): the one split
            if len(cells) > 3 and cells[0] == str(row_id):
                m = re.search(r"\d{4}-\d{2}-\d{2}", cells[3])
                return bool(m) and dt.date.fromisoformat(m.group()) < today
    except Exception:
        return False
    return False


DID_NOT_RUN = "CHECK DID NOT RUN"   # the marker a check prints when it could not run at all


def run_script(severity, name, cmd, owner, ok_rc=(0,), summarize=None):
    """Keep complete evidence on disk; summarize without silently dropping flags."""
    global LOG_DIR
    if LOG_DIR is None:
        LOG_DIR = Path(tempfile.mkdtemp(prefix="prome-gate-checks-"))
    log = LOG_DIR / f"{len(results):02d}-{re.sub(r'[^a-z0-9]+', '-', name.lower())[:70]}.txt"
    try:
        with log.open("x", encoding="utf-8") as output:
            p = subprocess.run(cmd, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT, timeout=120)
        ok = p.returncode in ok_rc
        tail = log.read_text(encoding="utf-8", errors="replace").strip().split("\n")
        # ⛔ DO NOT key this on rc=2. CHECK_STANDARD §9 (RATIFIED) defines rc 2 as CANNOT-CERTIFY,
        # not did-not-run: spawn_list.py:322 returns 2 from a run that COMPLETED and found UNKNOWN
        # rows, and docket_view/willq_view/position_agreement_check all have rc-2 paths of their own.
        # A 2026-09-19 attempt to relabel every rc=2 as "DID NOT RUN" printed "establishes nothing"
        # directly above a live WQ-184 spawn candidate — caught by an independent reader before it
        # ran a second time. The did-not-run state travels on its own MARKER (§8 rule 5: the marker
        # channel is authoritative, rc agrees with it and never substitutes for it).
        body = log.read_text(encoding="utf-8", errors="replace")
        state = "DID NOT RUN (the check itself failed — establishes nothing) · " if DID_NOT_RUN in body else ""
        detail = f"rc={p.returncode} · {state}".rstrip(" ·") + ("" if ok else f" · {tail[-1][:110]}" if tail else "")
        if summarize is not None:
            try:
                ok, summary = summarize(body, p.returncode)
                detail = f"rc={p.returncode} · {state}{summary}"
            except (ValueError, KeyError) as exc:
                ok, detail = False, f"rc={p.returncode} · UNKNOWN: {exc}"
        if not ok:  # 8/29: name the flagged artifacts — a bare "1 flag(s)" cannot satisfy BOOT.md's re-read rule
            flagged = [l.strip() for l in tail if l.lstrip().startswith(("❌", "⚠️"))]
            detail += "".join(f"\n       ↳ {l[:120]}{'… [preview]' if len(l) > 120 else ''}" for l in flagged[:3])
            if len(flagged) > 3:
                detail += f"\n       ↳ {len(flagged) - 3} additional flag(s); read full log"
    except Exception as e:
        ok, detail = False, f"{type(e).__name__}: {str(e)[:100]}"
    detail += f"\n       full output: {log}"
    record(severity, name, ok, detail, owner)
    return ok


def coverage_result(body, prefix, rc, counts):
    """Strict footer parsing for the three coverage producers; no heuristic fallback."""
    lines = [line for line in body.splitlines() if line.startswith(prefix)]
    if len(lines) != 1 or not lines[0].startswith(prefix + " v1 "):
        raise ValueError(f"missing, duplicate or unsupported {prefix}")
    fields = {}
    for token in lines[0][len(prefix + " v1 "):].split():
        key, sep, value = token.partition("=")
        if not sep or not value or key in fields:
            raise ValueError("malformed or duplicate result field")
        fields[key] = value
    for key in ("rc", *counts):
        if not re.fullmatch(r"[0-9]+", fields.get(key, "")):
            raise ValueError(f"missing or invalid {key}")
        fields[key] = int(fields[key])
    if rc not in (0, 1, 2) or fields["rc"] != rc:
        raise ValueError("process/result rc disagreement or unsupported rc")
    return fields


def summarize_read_cap(body, rc):
    counts = ("assessed", "reads", "over_budget", "over_cap", "manifest_defects",
              "advisories", "generated_flagged", "rotation_due", "active_decisions_over_budget")
    f = coverage_result(body, "READ-CAP-RESULT", rc, counts)
    if f.get("mode") != "agent" or f.get("desk") != "PROME" or f["assessed"] not in (0, 1):
        raise ValueError("expected agent/PROME result with assessed=0 or 1")
    if not f["assessed"]:
        if rc != 2:
            raise ValueError("unassessed result requires rc=2")
        return False, "UNKNOWN · assessed=0; counts are unearned, not clean; declared perimeter required"
    if not (f["over_cap"] <= f["over_budget"] <= f["rotation_due"] <= f["reads"]
            and f["active_decisions_over_budget"] in (0, 1)
            and f["active_decisions_over_budget"] <= f["over_budget"]):
        raise ValueError("contradictory read-cap counts")
    findings = bool(f["over_budget"] or f["manifest_defects"])
    if rc in (0, 1) and bool(rc) != findings:
        raise ValueError("rc contradicts size/manifest findings")
    detail = "declared PROME perimeter · " + " · ".join(f"{key}={f[key]}" for key in counts)
    if rc == 2:
        detail = "CANNOT-CERTIFY · " + detail
    if f["active_decisions_over_budget"]:
        detail += " — ACTIVE_DECISIONS ≥100%: scripted-check revisit trigger FIRED"
    if f["rotation_due"]:
        detail += " — rotation due (READ_CAP.md rule 5)"
    return rc == 0 and not any(f[k] for k in ("rotation_due", "advisories", "generated_flagged")), detail


def summarize_generated(body, rc):
    f = coverage_result(body, "DOCKET-GENERATED-RESULT", rc, ("assessed",))
    dt.date.fromisoformat(f["as_of"])
    if f["assessed"] not in (0, 1) or (rc == 2) != (f["assessed"] == 0):
        raise ValueError("generated result rc/assessment disagreement")
    if not f["assessed"]:
        return False, f"CANNOT-CERTIFY · assessed=0 · as_of={f['as_of']}"
    for key in ("docket_sha256", "view_sha256"):
        if not re.fullmatch(r"[0-9a-f]{64}", f.get(key, "")):
            raise ValueError(f"missing or invalid {key}")
    return rc == 0, (f"{'FRESH' if rc == 0 else 'STALE'} generated block · assessed=1 · "
                     f"as_of={f['as_of']} · snapshot identities in full output")


def summarize_prose(body, rc):
    f = coverage_result(body, "DOCKET-PROSE-RESULT", rc,
                        ("matched", "dated", "assessed", "unassessed", "ignored"))
    if (f.get("generated") != "excluded" or f["assessed"] + f["unassessed"] != f["dated"]
            or not f["assessed"] <= f["matched"] <= f["dated"] or rc == 2):
        raise ValueError("inconsistent prose coverage")
    scope = "EMPTY dated scope" if not f["dated"] else "handwritten dated scope"
    return rc == 0 and not f["unassessed"], (scope + " · " + " · ".join(
        f"{key}={f[key]}" for key in ("matched", "assessed", "unassessed", "ignored"))
        + " · generated content EXCLUDED")


def guard(fn, *args, **kw):
    """Run ONE check in isolation. An exception becomes an ERROR row naming the check
    and the cause; every later check still runs. No value is invented for the caller."""
    try:
        return fn(*args, **kw)
    except Exception as e:
        record(ERROR, f"{fn.__name__} DID NOT RUN", False,
               f"{type(e).__name__}: {str(e)[:160]} — this check was NOT evaluated; "
               "its subject is UNKNOWN, not clean",
               "fix the missing/unreadable input, then re-run the gate — "
               "an unevaluated check is not a passed one")
        return None


# ---------------------------------------------------------- T3-a mechanical core

def scan_gates_rows(rows, today):
    """Pure scan over GATES rows (list-of-cells) → dict of flag lists. Factored
    out 2026-08-28 so the review_by leg is TESTABLE (Codex audit H1, Will-approved
    "go ahead approved"): the discriminating case is a LIVE row whose consumed_by
    is still valid while its review_by has passed — before this, that row read
    unqualified green.

    Columns (GATES.tsv header): 0 gate_id · 5 state · 6 last_checked · 8 consumed_by
    · 9 scannable · 11 review_by.

    What the registry can and cannot distinguish: a passed review_by is one of
    {review overdue · publication pending · owner dark · graded at the owner but
    registry unreconciled}. The scan prints scannable class + last_checked so the
    reader can tell which; the disposition (consume the owner's grade, re-date, or
    read the instrument yourself as a CONSUMER read — never as the grade) is human.
    """
    out = {"bad_tokens": [], "fired": [], "stale_live": [],
           "review_overdue_instrument": [], "review_overdue_judgement": [],
           "instrument_unchecked": []}
    for r in rows:
        gate, state = r[0], (r[5] if len(r) > 5 else "")
        lead = state.split(" ")[0].split("(")[0].strip()
        if not any(state.startswith(t) for t in GATES_STATES):
            out["bad_tokens"].append(f"{gate} leads '{lead[:20]}'")
        if state.startswith("FIRED-UNEXECUTED"):
            out["fired"].append(gate)
        if state.startswith("LIVE"):
            # consumed_by discipline (forum S2/ABN ruling 8/7, Will-adopted; check
            # re-keyed 8/9 — spine-audit #8 found the ruling propagated to none of
            # its three surfaces): staleness keys on the consumed_by field, NOT raw
            # last_checked age (that >5d rule is RETIRED — it over-reported by design;
            # a LIVE row with a future consumer or PRICE:/EVENT:/NONE is quiet).
            cb = r[8] if len(r) > 8 else ""
            m = re.match(r"(\d{4}-\d{2}-\d{2})", cb)
            if m and dt.date.fromisoformat(m.group(1)) < today:
                out["stale_live"].append(f"{gate} consumer-date {m.group(1)} passed")
            elif not cb.strip():
                out["stale_live"].append(f"{gate} consumed_by EMPTY (required since 8/7)")
            # review_by = the OWNER's review clock (independent of consumed_by — a
            # gate can have a valid downstream consumer and still miss its own
            # review). Leading ISO date only; prose after it is for the reader.
            scannable = (r[9] if len(r) > 9 else "").strip().split(" ")[0].split("(")[0]
            last_checked = (r[6] if len(r) > 6 else "").strip()
            rb = r[11] if len(r) > 11 else ""
            m2 = re.match(r"(\d{4}-\d{2}-\d{2})", rb)
            if m2 and dt.date.fromisoformat(m2.group(1)) < today:
                msg = (f"{gate} review_by {m2.group(1)} passed [{scannable or 'unclassed'}; "
                       f"last_checked {last_checked[:10] or 'BLANK'}]")
                key = "review_overdue_instrument" if scannable == "INSTRUMENT" else "review_overdue_judgement"
                out[key].append(msg)
            if scannable == "INSTRUMENT" and not last_checked:
                out["instrument_unchecked"].append(gate)
    return out


def check_gates_tsv():
    """Token vocabulary + FIRED-UNEXECUTED + LIVE consumed_by + review_by. The
    silent-blank class (bare-date cells 7/28, bare ARMED 7/28, SAM-30 7/11) becomes
    impossible to miss: a state cell not LEADING with an enumerated token is a
    BLOCKING fail. review_by enforcement added 2026-08-28 (Codex audit H1,
    Will-approved): a LIVE INSTRUMENT row past its review date is BLOCKING —
    the instrument may have crossed while nobody looked, which is the ledger's
    one job; JUDGEMENT rows past review are advisory (owner-graded at cadence);
    a LIVE INSTRUMENT row with blank last_checked is advisory."""
    path = ROOT / "PROME/GATES.tsv"
    today = dt.date.today()
    with open(path, encoding="utf-8") as f:
        rows = [r for r in csv.reader(f, delimiter="\t")
                if r and not r[0].startswith("#") and r[0] != "gate_id"]
    o = scan_gates_rows(rows, today)
    record(BLOCK, "GATES fired-unexecuted", not o["fired"],
           "; ".join(o["fired"]) or "none", "PROME/GATES.tsv (clear or escalate SAME session)")
    record(BLOCK, "GATES token vocabulary", not o["bad_tokens"],
           "; ".join(o["bad_tokens"]) or f"{len(rows)} rows all lead with enumerated tokens",
           "PROME/GATES.tsv header STATES line")
    record(ADVISE, "GATES consumed_by (consumer passed / cell empty)", not o["stale_live"],
           "; ".join(o["stale_live"]) or "all LIVE rows have live consumers or declared NONE",
           "PROME/GATES.tsv (resolve at the consumer, re-date, or declare NONE)")
    record(BLOCK, "GATES review_by passed — LIVE INSTRUMENT rows", not o["review_overdue_instrument"],
           "; ".join(o["review_overdue_instrument"]) or "no live INSTRUMENT row past its review date",
           "PROME/GATES.tsv (consume the owner's grade → re-date review_by; if the owner is dark, "
           "read the instrument as a CONSUMER read and say so in the row — never as the grade)")
    record(ADVISE, "GATES review_by passed — LIVE JUDGEMENT rows", not o["review_overdue_judgement"],
           "; ".join(o["review_overdue_judgement"]) or "no live JUDGEMENT row past its review date",
           "PROME/GATES.tsv (owner grades at review_by; re-date or summon the owner)")
    record(ADVISE, "GATES last_checked blank on LIVE INSTRUMENT rows", not o["instrument_unchecked"],
           "; ".join(o["instrument_unchecked"]) or "every live INSTRUMENT row carries a last_checked",
           "PROME/GATES.tsv (fill from the owner's latest grade; a blank reads as never-graded)")


def check_docket_overdue():
    """PENDING rows whose (end-)date has passed — the row-56 ballot-cert class."""
    path = ROOT / "PROME/DOCKET.tsv"
    today = dt.date.today().isoformat()
    overdue = []
    with open(path, encoding="utf-8") as f:
        for r in csv.reader(f, delimiter="\t"):
            if not r or r[0].startswith("#") or len(r) < 4 or r[3].split("(")[0] != "PENDING":
                continue
            end = r[0].split("..")[-1]
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", end) and end < today:
                # The annotation lives in STATUS — PENDING(OVERDUE-annotated …) — or in
                # NOTES; practice has used both (4 rows vs 2 on 2026-08-03). Scanning only
                # NOTES made every status-annotated row read as unannotated, so the check
                # reported work that was already done and hid the rows that weren't.
                annotation = r[3] + " " + (r[5] if len(r) > 5 else "")
                if "OVERDUE" not in annotation:
                    overdue.append(f"{r[0]} {r[1][:40]}")
    record(ADVISE, "DOCKET overdue-unannotated", not overdue,
           # ⚠️ 2026-08-08: truncation must ANNOUNCE itself. The 8/3 audit found this
           # check's column-scan bug AND named its 4-item display cap as the mechanism
           # that let false positives crowd out 4 real rows — only the column half was
           # fixed. A silent cap reads as "that's all of them."
           # [[finding_display_filter_gating_safety_net]]
           "; ".join(overdue[:4]) +
           (f" (+{len(overdue)-4} more)" if len(overdue) > 4 else "")
           or "every past-dated PENDING row carries an OVERDUE annotation",
           "PROME/DOCKET.tsv (grade, re-date, or annotate OVERDUE + owner)")


def check_docket_buried_state_token():
    """BLOCKING: a DOCKET row whose state cell contains PENDING but does not LEAD with a
    state token is INVISIBLE to the canonical reader and its obligation silently disappears.

    WHY (2026-09-19): `scripts/docket_view.py:110` classifies a row by whether its state cell
    STARTS with a token; anything else is TERMINAL. PROME annotated four of its own live rows
    that day by PREFIXING narrative (⛔ DATE CONTESTED …, ⚑ RE-SCOPED …, ✅ CONFIRMED …) and
    thereby dropped all four out of the live calendar — L433 · L435 · L441 · L444, two of them
    obligations PROME had registered hours earlier.

    ⛔ THE LESSON WAS ALREADY IN PROME'S OWN HOT MEMORY INDEX AT THE TIME, reading *a guard
    scoped by status TOKEN drops the rows someone described better*
    ([[finding_status_token_membership_test_desupervises_improved_rows]], already n=3 across
    3 files in 1 day). Knowing it did not prevent a fourth, fifth, sixth and seventh instance
    by its own author within one session — which is the argument for a mechanical guard over
    another note (WQ-229: prefer promoting or repairing a control to describing the pattern).

    Found by CATO, not by PROME, and not by any existing check: the row reads TERMINAL, so
    every downstream consumer agrees it is finished. A disappeared obligation leaves no
    absence to notice — the same shape as [[finding_truncation_returns_a_plausible_answer_not_an_error]].

    BLOCKING rather than advisory on purpose: an advisory here would be overridden exactly as
    the .claude parity gate was ([[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]).

    ⛔ KNOWN GAP, NAMED BY AN INDEPENDENT AUDITOR AND NOT CLOSED HERE (DOCKET row registered).
    This predicate is a SUBSTRING test: it fires only while the cell still contains the literal
    word "PENDING". A live row annotated WITHOUT repeating that word — ARGUS's own plant,
    `⛔ DATE CONTESTED 2026-09-19 — obligation stands, owner grades Monday` — is invisible to
    THIS GUARD and terminal to the reader. All seven rows it caught on 2026-09-19 were caught
    only because PROME's annotation style happened to preserve the prior cell verbatim, which
    carried the word along. ⇒ "falsified before being trusted" was true of the AUTHOR'S plant
    and FALSE of an independent one ([[finding_test_the_guard_not_just_the_guarded]]).

    ⚠️ PROME attempted two replacements the same session and BOTH reproduced the dependency in
    a different form (v2 searched for any state word — ARGUS's plant contains none; v3 keyed on
    future-dated TERMINAL rows and flagged legitimately-terminal ones). Reverted to this version
    deliberately: it catches the class PROME actually produced and blocks on it, which beats no
    guard, and iterating a fourth time at the tail of a closeout is the correction cascade the
    two-correction stop exists to prevent. The acceptance condition for the real fix is ARGUS's
    plant, written down rather than remembered.
    """
    import re as _re
    tok = _re.compile(r"^\s*(PENDING|RESOLVED|TOMBSTONE|SUPERSEDED|CANCELLED|EXPIRED|COVERED|"
                      r"DELIVERED|NOT RUN|RE-DATED|SLID|DISPOSED|DECLINED|LAPSED|GRADED|"
                      r"OWNER-GRADED|OWNER-DELIVERED|IN PROGRESS|MEASURED|POLLED|OVERTAKEN|"
                      r"MISSED-WINDOW-RECOVERED|LEG|OVERDUE-ANNOTATED|★)", _re.I)
    buried = []
    try:
        rows = (ROOT / "PROME" / "DOCKET.tsv").read_text(encoding="utf-8").split("\n")
    except OSError as e:
        record(ADVISE, "DOCKET buried state token", None,
               f"UNKNOWN — could not read DOCKET ({type(e).__name__})", "PROME/DOCKET.tsv")
        return
    for n, raw in enumerate(rows, 1):
        c = raw.split("\t")
        if len(c) < 4 or not c[0].strip() or c[0].startswith("#"):
            continue
        if "PENDING" in c[3].upper() and not tok.match(c[3]):
            buried.append(f"L{n}")
    record(BLOCK, "DOCKET buried state token (row invisible to the canonical reader)", not buried,
           ("; ".join(buried[:8]) + (f" (+{len(buried)-8} more)" if len(buried) > 8 else "")
            + " — state cell contains PENDING but does not LEAD with a token, so docket_view "
              "reads it TERMINAL and the obligation vanishes from the live calendar")
           if buried else "every row containing PENDING leads with a state token",
           "PROME/DOCKET.tsv — put the token FIRST and the annotation AFTER it; never prefix narrative")


def check_docket_today():
    """CLOSEOUT-ONLY, BLOCKING: PENDING rows landing TODAY, undispositioned.

    WHY (2026-08-03, the leg-(b) routing gap): PROME closed out at 11:10 with
    its own SCRATCH saying "THE ONE THING THAT MATTERS TODAY: BRENT deploy-gate
    leg (a) grades at the 16:00 close" — and PROME was the sole routing path
    between BRENT and TERRY. BRENT's request landed 11:45 and Will's tenor +
    size rulings 12:50, into an inbox nobody was reading. TERRY never got the
    size ruling and logged the item NOT DONE at its own 15:12 closeout.

    Nothing existing could catch it. check_docket_overdue() scans only PAST
    dates; GATES fired-unexecuted needs a gate to have already FIRED; an
    inbox check would have passed (inbox was 0 at 11:10 — the packets had not
    been sent yet). The missing question is the simple one: *is anything
    landing today, and does it need me after I go dark?*

    Cleared the same way overdue rows are — annotate the row. A row is
    dispositioned if its STATUS or NOTES carries COVERED (name who has it), or
    if it has already left PENDING. Deliberately BLOCKING, not advisory: the
    whole failure mode is a true line nobody read. Cheap to satisfy, impossible
    to skip. [[finding_mechanize_the_cap_not_the_ritual]]
    """
    path = ROOT / "PROME/DOCKET.tsv"
    today = dt.date.today().isoformat()
    undispositioned = []
    with open(path, encoding="utf-8") as f:
        for r in csv.reader(f, delimiter="\t"):
            if not r or r[0].startswith("#") or len(r) < 4:
                continue
            if r[3].split("(")[0] != "PENDING":
                continue
            # A row lands today if it is dated today, or is a range spanning it.
            start, end = r[0].split("..")[0], r[0].split("..")[-1]
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", end):
                continue
            if not (start <= today <= end):
                continue
            if "COVERED" in (r[3] + " " + (r[5] if len(r) > 5 else "")):
                continue
            owner = r[2][:28] if len(r) > 2 else "?"
            undispositioned.append(f"{r[1][:44]} [{owner}]")
    record(BLOCK, "DOCKET lands-today dispositioned", not undispositioned,
           "; ".join(undispositioned[:5]) +
           (f" (+{len(undispositioned)-5} more)" if len(undispositioned) > 5 else "")
           or "nothing PENDING lands today",
           "PROME/DOCKET.tsv — for EACH: grade it, or annotate COVERED:<who holds it "
           "after you go dark>. A row whose owner is PROME and that is still PENDING at "
           "closeout is the routing-gap class: say who covers it or do it now.")


def check_will_queue():
    """WILL_QUEUE.md — passed needed-by dates on OPEN rows + stale reconcile stamp.
    Born 2026-07-30 (Will-directed): the operator queue decays like any surface,
    and both failure directions are costly — DONE-reads-OPEN nags Will, OPEN-
    reads-DONE silently drops his decision. Flags only what a script can see:
    ISO dates in the Needed-by column and the content-vintage stamp
    (finding_hygiene_commit_rearms_the_staleness_lie — never key on mtime)."""
    path = ROOT / "PROME/WILL_QUEUE.md"
    check_will_queue.last_problems = []                  # reset at ENTRY so a stale list never survives an early return (parserfix2cold ⚠️)
    if not path.exists():
        record(ADVISE, "WILL_QUEUE present", False, "PROME/WILL_QUEUE.md missing",
               "PROME/WILL_QUEUE.md")
        return
    text = path.read_text(encoding="utf-8")
    today = dt.date.today()
    m = re.search(r"^\*\*Last reconciled:\*\*\s*(\d{4}-\d{2}-\d{2})", text, re.M)
    problems = []
    if not m:
        problems.append("no 'Last reconciled: YYYY-MM-DD' stamp")
    else:
        age = (today - dt.date.fromisoformat(m.group(1))).days
        if age > 2:
            problems.append(f"reconcile stamp {m.group(1)} is {age}d old")
    # DAEDALUS W1 (7/30 review): `<` shipped first and printed a green tick while
    # two rows were due THAT NIGHT — a due-today row must flag as DUE TODAY (act
    # now), distinct from PASSED (reconcile). W2: cap counts only ACTIONABLE rows
    # (dated + unblocked); undated unblocked rows age-trip at 21d instead. W5:
    # DONE rows past the ~7d window flag for roll-off (anchor-at-write makes the
    # roll always safe).
    def _mmdd(cell):
        m2 = re.search(r"(\d{1,2})/(\d{1,2})", cell)
        if not m2:
            return None
        try:
            d0 = dt.date(today.year, int(m2.group(1)), int(m2.group(2)))
        except ValueError:
            return None
        # Year-roll, BACKWARD ONLY (8/16 rider, deviation from firetime's ±183
        # stated in the write-back): Since/Done cells are PAST-only, so a parse
        # >183d in the future is last year's date (a `12/20` read in January —
        # the false-negative direction the old "revisit in Dec" comment
        # under-scoped). Rolling >183d-past dates FORWARD (firetime's other
        # half) would instead make ancient rows read as future and silence
        # AGING/roll-off — the same false-negative this rider exists to kill.
        if (d0 - today).days > 183:
            try:
                d0 = d0.replace(year=today.year - 1)
            except ValueError:
                pass
        return d0

    section, actionable, hdr_open = None, 0, None
    for line in text.splitlines():
        if line.startswith("## "):
            section = "open" if line.startswith("## OPEN") else (
                "done" if line.startswith("## RECENTLY DONE") else None)
            continue
        if not (section and line.startswith("|")):
            continue
        cells = split_cells(line)                        # B1 (9/18): the one split
        if section == "open":
            if is_separator(cells):
                continue
            if hdr_open is None:                         # B2: the FIRST table row is the header
                hdr_open = len(cells)
                if hdr_open != 7:                        # B8: width is a contract — flagged once, the table skipped, never indexed or silently zeroed
                    problems.append(f"HEADER {hdr_open} columns in § OPEN (the table is 7) — table skipped, nothing counted")
                continue
            if hdr_open != 7:
                continue
            if len(cells) != hdr_open:                   # B2: flagged BY NAME and excluded from the count, never parsed shifted
                problems.append(f"SHIFTED #{cells[0][:8]} ({len(cells)} cells vs header {hdr_open}) — an unescaped | inside a cell; write it \\|")
                continue
        if section == "open" and len(cells) >= 7:
            # Keys on the DOCUMENTED wait-declaration at the START of the Notes
            # cell — see the twin comment in will_brief.parse_actions(). WILL_QUEUE
            # canon: blocked rows carry "⛔ waits: <who>" at the start of Notes.
            # 8/22: bare "⛔" (the caveat glyph) had excluded actionable rows.
            # 9/10 (WQ-221): a whole-line "⛔ wait" search matched ITEM prose
            # ("a ⛔ waits row whose …") and hid a rulable row from the deck.
            blocked = bool(re.match(r"^[\*\s]*⛔\s*waits?\b", cells[6]))
            # MISFILED (8/16, DAEDALUS spec off PROME's queue-look defect
            # report; ruling trail in the two packets): close-in-place is a
            # silent middle state between OPEN and RECENTLY DONE — measured
            # live 8/16 at ~15 of 25 rows, printing a false 25>20 over-cap
            # and a false AGING-47d on a RESOLVED row. A terminal marker
            # LEADING the Item cell (anchored after strikethrough/bold strip,
            # never substring — "blocked until X is RESOLVED" must not match)
            # flags the row-move; excluded from actionable + AGING at once so
            # the count is honest even before the move. Roll-off applies
            # normally once moved — the MISFILED line IS the action.
            item = re.sub(r"^(?:~~[^~]+~~\s*)+", "", cells[1])
            item = re.sub(r"^[\*\s]+", "", item)
            if re.match(r"✅|DONE\b|RESOLVED\b|TERMINAL\b|DECLINED\b", item):
                problems.append(
                    f"MISFILED #{cells[0]} {cells[1][:30]} "
                    "(closed-in-place in OPEN — move to RECENTLY DONE)")
                continue
            if re.match(r"\d", cells[0]) and datelike_not_iso(cells[3]):   # B3: flagged by name, still counted; AFTER the closed-in-place exclusion (parity)
                problems.append(f"NOT-ISO #{cells[0]} needed-by '{cells[3][:24]}' (hard dates are YYYY-MM-DD)")
            d = re.search(r"\d{4}-\d{2}-\d{2}", cells[3])
            if d:
                # ⛔ F1 (L423 fourth independent read, 2026-09-19): a date that MATCHES the ISO
                # shape but is not a real day — `2026-02-30` — raised ValueError out of this
                # bare call and took the WHOLE BLOCKING CHECK down. The gate then reported
                # `check_will_queue DID NOT RUN — ValueError` with `last_problems == []`, so a
                # DUE-TODAY row and a SHIFTED row in the same table were NEVER REPORTED. A
                # crashed check that reports no problems is worse than no check: it is a clean
                # bill signed by a corpse. Fail CLOSED and by NAME instead — the impossible date
                # becomes a named problem rather than an exception.
                # Found by a reader devising its own input; no B-condition covered date VALIDITY,
                # only shape. [[finding_lenient_parser_reports_unparseable_as_a_behavior]]
                try:
                    dd = dt.date.fromisoformat(d.group(0))
                except ValueError:
                    problems.append(f"IMPOSSIBLE DATE #{cells[0]} needed-by '{d.group(0)}' "
                                    f"(ISO-shaped but not a real day — the row is UNGRADEABLE, "
                                    f"not clean)")
                    continue
                if dd == today:
                    problems.append(f"DUE TODAY #{cells[0]} {cells[1][:36]}")
                elif dd < today:
                    problems.append(f"PASSED #{cells[0]} {cells[1][:36]} (needed {d.group(0)})")
                if not blocked:
                    actionable += 1
            # `^\d` not .isdigit() (8/16, landed WITH the F2 ruling by design —
            # sequenced on the record in the MISFILED write-back): lettered row
            # IDs (32a, 36b…) failed .isdigit() and silently escaped BOTH the
            # actionable count and the 21d age-trip. Post-F2 the escape class
            # is mostly moved out anyway; this closes the hole for the future.
            elif not blocked and re.match(r"\d", cells[0]):
                actionable += 1
                s = _mmdd(cells[4])
                if s and (today - s).days > 21:
                    problems.append(f"AGING #{cells[0]} {cells[1][:30]} (undated, open {(today - s).days}d)")
        elif section == "done" and len(cells) >= 3 and cells[0] != "Item":
            # Done-date = the ruling/closing date stated in the outcome cell
            # (RULED/DONE/CLOSED/... <date>), else the Since cell. 9/2 fix: the
            # DONE table's second cell is the OPEN date, so rows ruled 9/1 in
            # the batch word flagged "done 10d ago" — aging a roll-off off the
            # wrong clock (six false flags at the 9/2 21:5x boot, zero true).
            dn = None
            m3 = re.search(r"(?:RULED|DONE|CLOSED|EXECUTED|RESOLVED|DECLINED|"
                           r"OVERTAKEN|WITHDRAWN|DELIVERED)\D{0,25}?"
                           r"(\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2})", cells[2])
            if m3:
                tok = m3.group(1)
                try:
                    dn = dt.date.fromisoformat(tok) if "-" in tok else _mmdd(tok)
                except ValueError:
                    dn = None
            if dn is None:
                dn = _mmdd(cells[1])
            if dn and (today - dn).days > 7:
                problems.append(f"ROLL-OFF {cells[0][:30]} (done {(today - dn).days}d ago)")
    if actionable > 20:
        # FIRST, not last (9/18): the detail line shows five problems; a CAP hidden behind five SHIFTED/NOT-ISO
        # lines is the silent-cap class the comment below names. The headline count leads.
        problems.insert(0, f"CAP: {actionable} actionable rows (>20) — PROME over-routing")
    check_will_queue.last_problems = list(problems)   # the FULL list, for queue_parser_selftest (the detail below shows five)
    record(ADVISE, "WILL_QUEUE fresh + nothing due/passed/aging", not problems,
           # ⚠️ 2026-08-08: same silent-cap class as check_docket_overdue above —
           # measured live at this boot, 14 roll-off-eligible rows displayed as 4.
           "; ".join(problems[:5]) +
           (f" (+{len(problems)-5} more)" if len(problems) > 5 else "")
           or "stamp current; nothing due today, passed, aging, misfiled, or overdue for roll-off",
           "PROME/WILL_QUEUE.md (act on DUE TODAY; reconcile PASSED; date/decline AGING)")


def aged_waits(rows, today, dark_days, min_days: int = 7):
    """WQ-221 (Will 2026-09-10 23:22): a ⛔-waits queue row whose BLOCKING desk has been dark ≥7 days is a
    PROME L0 drain-only spawn — woken through a PENDING DOCKET row naming the desk (one wake mechanism).
    Pure function: `rows` = decision_deck.parse_open() dicts (blocked / blocker / notes / n), `dark_days(desk)`
    = days since the desk's last self-commit (None = unknown). A wait on a DATED deliverable (a date ≥ today in
    the notes cell) is NOT aged before that date — the ruling's own exclusion (WQ-157 class)."""
    out = []
    for r in rows:
        if not r.get("blocked") or not r.get("blocker"):
            continue
        notes = r.get("notes", "")
        dated = [d for d in re.findall(r"\d{4}-\d{2}-\d{2}", notes) if d >= today.isoformat()]
        if dated:
            continue  # a dated deliverable is not an aged wait before its date
        days = dark_days(r["blocker"])
        if days is None or days < min_days:
            continue
        out.append((r["n"], r["blocker"], days))
    return out


def check_aged_waits():
    """Boot advisory (WQ-221 instrument, SCRATCH ⓜ, built 2026-09-11): lists ⛔-waits rows whose blocker is
    dark ≥7d with no dated deliverable — each is owed a PENDING DOCKET row naming the desk, which the WQ-184
    driver then spawns. Reads the queue through decision_deck (one parser home); liveness = its days_dark."""
    try:
        sys.path.insert(0, str(ROOT / "PROME/tools"))
        import decision_deck as dd  # noqa: E402
        rows = dd.parse_open((ROOT / "PROME/WILL_QUEUE.md").read_text(encoding="utf-8"))
        hits = aged_waits(rows, dt.date.today(), dd.days_dark)
    except Exception as e:  # never silent: UNKNOWN is a visible advisory
        record(ADVISE, "aged waits (WQ-221)", False, f"UNKNOWN — {type(e).__name__}: {e}",
               "PROME/WILL_QUEUE.md § OPEN (⛔ waits rows) — run by hand: decision_deck.parse_open + days_dark")
        return
    record(ADVISE, "aged waits (WQ-221): ⛔-waits rows whose blocker is dark ≥7d", not hits,
           "; ".join(f"WQ-{n} waits on {desk} — dark {d}d" for n, desk, d in hits[:5])
           + (f" (+{len(hits)-5} more)" if len(hits) > 5 else "")
           or "no ⛔-waits row has a blocker dark ≥7d without a dated deliverable",
           "each hit ⇒ register a PENDING DOCKET row naming the blocking desk (L0 drain-only, cap-counted; WQ-221 rule 3) — never a per-item ask")


def check_heartbeat_chain():
    """HEARTBEAT amendment-chain length vs the ~5 re-base rule (Cadence section).
    The rule lived in prose on 5+ surfaces and in no script until 2026-07-30
    (DAEDALUS FORGE-audit follow-up, gap (a)) — it held at chain=4 on memory,
    twice. Advisory: warn at 4 (plan the re-base), and at >=5 the rule's own
    trip has occurred. [[finding_mechanize_the_cap_not_the_ritual]]

    ⚠️ 2026-08-04 REPAIR — this check was BLIND from the 7/31 re-base until now.
    v1 matched only `> ## AMENDMENT #N`; the 7/31 re-base changed the house style
    to `> **AMENDMENT #N`, so it counted ZERO against a header that declared
    "Chain: 2" and printed a confident ✅ PASS. A heading-format change silently
    disarmed the one mechanism enforcing the re-base rule.

    Two fixes, because swapping the regex alone would just re-arm the same trap
    the next time the style moves:
      (a) match either style (and any future `#`-heading depth);
      (b) CROSS-CHECK the count against the header's own self-declared
          "Chain: N". The file states the answer in prose; v1 never read it.
          Disagreement is not resolvable from inside this check, so it reports
          UNVERIFIABLE and trips on max(counted, declared) — fail-loud, never a
          confident number it cannot stand behind.
    [[finding_test_the_guard_not_just_the_guarded]] · the "return a confident
    answer where 'cannot evaluate' is the honest one" class (PROME 2026-08-04)."""
    path = ROOT / "HEARTBEAT.md"
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        record(ADVISE, "HEARTBEAT chain length", False, f"unreadable: {e}", "HEARTBEAT.md")
        return
    # Either heading style: "> ## AMENDMENT #1 —" (pre-7/31) or "> **AMENDMENT #1 —" (current).
    counted = len(re.findall(r"^>\s*(?:#{1,6}\s*|\*\*)?AMENDMENT\s*#\d+", text, re.M))
    # The header states the chain in prose: "... Chain: 2." — v1's missing positive check.
    m = re.search(r"^\*\*Amendments append.*?Chain:\s*(\d+)", text, re.M)
    declared = int(m.group(1)) if m else None

    src = "HEARTBEAT.md Cadence section (re-base = draft -> Will approval -> archive verbatim)"
    if declared is not None and declared != counted:
        record(ADVISE, "HEARTBEAT amendment chain (<4)", False,
               f"UNVERIFIABLE — counted {counted} amendment block(s) but the header declares "
               f"Chain: {declared}. One of them is wrong and this check cannot say which: "
               f"either the header is stale or the block format moved again (a block must START a line as `> **AMENDMENT #N`). Tripping on the "
               f"larger ({max(counted, declared)}) so the re-base rule fails LOUD, not silent",
               src + " · reconcile the header stamp against the blocks before trusting either")
        return

    n = counted
    ok = n < 4
    detail = (f"chain at {n} amendment(s)"
              + ("" if declared is None else " (header-declared count agrees)")
              + ("" if ok else " — re-base rule trips at ~5: plan it into the next substantive session"
                 if n == 4 else " — the ~5 trip HAS OCCURRED: re-base (draft->Will->archive-verbatim) is due"))
    record(ADVISE, "HEARTBEAT amendment chain (<4)", ok, detail, src)


def check_dashboard_build_receipt(state_built):
    """L339: fleet_dashboard.py writes dashboard_state.json ONLY on a clean
    build, so a FAILING build leaves the previous snapshot in place and returns
    rc=1 silently — and every check below then certifies that stale snapshot and
    passes. The receipt records each baseline-advancing run's own outcome; this
    check refuses a snapshot that is not the product of the latest build.
    Compared on CONTENT stamps only, never mtime (git sync restamps mtime).
    Returns "" when the snapshot is certified current, else a stale-note prefix."""
    path = ROOT / "PROME/tools/dashboard_build.json"
    src = "PROME/tools/fleet_dashboard.py (rebuild; fix the build, never the state file)"
    name = "dashboard state is the product of the latest build (L339)"
    try:
        r = json.loads(path.read_text())
        # Everything that dereferences `r` stays INSIDE this try. A receipt that
        # is valid JSON but not an object ([], null, "ok", 3) used to raise
        # AttributeError out of this function, and main() wraps no check --
        # so every LATER gate check silently never ran. Failing open on a
        # malformed input is worse than the defect this check exists to catch.
        if not isinstance(r, dict):
            raise TypeError(f"receipt is {type(r).__name__}, expected an object")
        attempted = str(r.get("attempted", ""))
        ok = r.get("ok")
        errs = r.get("errors") or []
    except FileNotFoundError:
        # NOT the same as a failed build: nothing has been recorded either way.
        record(BLOCK, name, False,
               "NO BUILD RECEIPT — cannot establish that dashboard_state.json came "
               "from the latest build; run fleet_dashboard.py", src)
        return "UNCERTIFIED SNAPSHOT — "
    except Exception as e:
        record(BLOCK, name, False, f"build receipt unreadable: {type(e).__name__}: {e}", src)
        return "UNCERTIFIED SNAPSHOT — "
    if not ok:
        record(BLOCK, name, False,
               f"LAST BUILD FAILED at {attempted or 'unknown'} ({len(errs)} error(s)): "
               + " | ".join(str(e) for e in errs)
               + f" — dashboard_state.json still at {state_built or 'unknown'}", src)
        return "STALE SNAPSHOT (last build failed) — "
    if attempted != state_built:
        # Both stamps are YYYY-MM-DD HH:MM, so a string compare gives the
        # direction for free. Asserting "older" unconditionally printed a
        # sentence the two numbers beside it refuted, and sent a cold reader
        # to fix the wrong file.
        older = "OLDER than" if state_built < attempted else "NEWER than"
        record(BLOCK, name, False,
               f"snapshot does not match the last build — state is {older} it: "
               f"state built {state_built or 'unknown'}, last build {attempted}", src)
        return "STALE SNAPSHOT (does not match last build) — "
    record(BLOCK, name, True, f"last build {attempted} succeeded and produced this snapshot", src)
    return ""


def check_dashboard_state():
    """The publisher's own blank panels — the 4-day silent regression class.
    BLOCKING on emptiness (a degraded Will-facing page), advisory on vintage.
    L339: the checks below certify the FILE — the receipt check above certifies
    that the file is the latest build's output. A green line here over a stale
    snapshot is the exact shape that let a failed build ship."""
    path = ROOT / "PROME/tools/dashboard_state.json"
    try:
        s = json.loads(path.read_text())
    except Exception as e:
        check_dashboard_build_receipt("")
        record(BLOCK, "dashboard panels nonempty", False, f"state unreadable: {e}",
               "PROME/tools/fleet_dashboard.py")
        return
    built = s.get("built", "")
    stale = check_dashboard_build_receipt(built)
    empty = [k for k, v in (("one-liner", s.get("one")), ("channels", s.get("channels")),
                            ("levels", s.get("levels"))) if not v]
    record(BLOCK, "dashboard panels nonempty", not empty,
           stale + (("EMPTY: " + ", ".join(empty)) if empty else "one-liner/channels/levels populated"),
           "PROME/tools/fleet_dashboard.py (rebuild; if still empty a parser broke — PAT-069)")
    try:
        age_h = (dt.datetime.now() - dt.datetime.strptime(built, "%Y-%m-%d %H:%M")).total_seconds() / 3600
        record(ADVISE, f"dashboard vintage ≤{DASH_STALE_HOURS}h", age_h <= DASH_STALE_HOURS,
               stale + f"built {built} ({age_h:.0f}h ago)", "regenerate + republish to the RECORDED URL")
    except ValueError:
        record(ADVISE, "dashboard vintage", False, stale + f"unparseable built stamp '{built}'",
               "PROME/tools/fleet_dashboard.py")
    # PAT-105 content assertions (8/16, DAEDALUS sweep-1 guard rec, Will "go"):
    # nonemptiness certifies presence, not truth — every live Will-facing
    # failure this window was NONEMPTY (the one-liner rendered "SPENT", a
    # kill-on-sight token). Four cheap truth checks, advisory tier:
    bad = []
    one = (s.get("one") or "").strip().strip('"“”')
    hb_text = ""
    try:
        hb_text = (ROOT / "HEARTBEAT.md").read_text(errors="ignore")
    except OSError:
        pass
    kill_line = next((ln for ln in hb_text.splitlines()
                      if "kill-on-sight" in ln), "")
    if len(one) < 40:
        bad.append(f"one-liner suspiciously short ({len(one)} chars) — token-capture class")
    elif kill_line and one[:60] in kill_line:
        bad.append("one-liner text appears on HEARTBEAT's own kill-on-sight line")
    if not (s.get("split") or "").strip():
        bad.append("NEXUS split EMPTY (separator-drift class, blank 17d once)")
    if len(s.get("levels") or {}) < 6:
        bad.append(f"only {len(s.get('levels') or {})} gate tiles (<6 floor — "
                   "token-rename attrition class, 13→4 once)")
    try:
        import agent_freshness
        # L294 F-4: this read `(own_surface_age_days(n) or 0) > 7`, so BOTH
        # "never committed" and "the git query failed" arrived as 0 days = brand
        # new. Three states now, each reported as itself — a desk whose freshness
        # could not be established is not a desk that is fresh.
        wrong, unknown, never = [], [], []
        for n, cls in (s.get("fleet") or {}).items():
            if cls != "ok" or n == "PROME":
                continue
            state, days = agent_freshness.own_surface_age_state(n)
            if state == "aged" and days > 7:
                wrong.append(f"{n} ({days:.0f}d)")
            elif state == "never":
                never.append(n)
            elif state == "unknown":
                unknown.append(n)
        if wrong:
            bad.append("fleet grid says ok but own-surface age >7d: " + ", ".join(wrong))
        if never:
            bad.append("fleet grid says ok but NO COMMIT has ever touched their own tree: "
                       + ", ".join(never))
        if unknown:
            bad.append("fleet grid says ok but own-surface age could NOT be established "
                       "(git query failed): " + ", ".join(unknown))
    except Exception as e:
        bad.append(f"grid-agreement check unavailable ({type(e).__name__})")
    record(ADVISE, "dashboard content assertions (PAT-105)", not bad,
           stale + ("; ".join(bad) or "one-liner sane · split populated · tile floor met · grid agrees with freshness"),
           "PROME/tools/fleet_dashboard.py (rebuild + fix the parser, never the state file)")


def check_symmetry():
    """T2-c: a boot-read surface isn't wired until its CLOSEOUT symmetry row
    exists (paired-write or explicitly one-way). BOOT absorbed 4 gates in 48h
    the table never learned about — growth must register at the slow surface."""
    boot = (ROOT / "PROME/BOOT.md").read_text(errors="ignore")
    close = (ROOT / "PROME/CLOSEOUT.md").read_text(errors="ignore")
    seq = boot.split("## Boot Sequence", 1)[-1].split("## Conditional Modules")[0]
    # T2-c v1 (DAEDALUS ruling 7/28, shipped 8/9): harvest ONLY lines carrying an
    # explicit `Read` directive (case-sensitive word). Mention-harvesting registered
    # pointers and even retirement notices as reads (the TODAY.md phantom class).
    # Contract: a mandatory boot read carries the word "Read" on its line in BOOT.md.
    boot_reads = set()
    for ln in seq.splitlines():
        if re.search(r"\bRead\b", ln):
            boot_reads.update(re.findall(r"`((?:PROME/)?[A-Z][A-Za-z_]+\.(?:md|tsv))`", ln))
    sym = close.split("## Boot↔Closeout symmetry", 1)[-1].split("\n## ", 1)[0]
    missing = sorted(s for s in boot_reads
                     if Path(s).name not in sym and s not in sym)
    record(ADVISE, "boot↔closeout symmetry", not missing,
           ("boot-reads with no symmetry row: " + ", ".join(missing)) if missing
           else f"{len(boot_reads)} boot-read surfaces all registered",
           "PROME/CLOSEOUT.md symmetry table (add paired-write row or declare one-way)")


def check_desk_catalyst_summons():
    """BD-02 summons half (LABOR ask 2026-08-20). For each registered desk
    catalyst ledger: flag rows dated within SUMMONS_WINDOW_DAYS or past-due.
    Advisory — the disposition is 'flag Will to spawn the desk', nothing else."""
    today = dt.date.today()
    horizon = today + dt.timedelta(days=SUMMONS_WINDOW_DAYS)
    flags, dead_ledgers = [], []
    for desk, rel in SUMMONS_LEDGERS.items():
        path = ROOT / rel
        if not path.exists():
            dead_ledgers.append(f"{desk} ledger MISSING ({rel})")
            continue
        try:
            with path.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f, delimiter="\t"):
                    m = re.match(r"(\d{4}-\d{2}-\d{2})", (row.get("date") or "").strip())
                    if not m:
                        continue
                    d = dt.date.fromisoformat(m.group(1))
                    if d > horizon:
                        continue
                    pri = (row.get("priority") or "?").strip()
                    ev = (row.get("event") or "?").strip()[:45]
                    when = (f"PAST-DUE {(today - d).days}d — ungraded?" if d < today
                            else ("TODAY" if d == today else f"in {(d - today).days}d"))
                    flags.append((d, f"{desk} {d} [{pri}] {ev} ({when})"))
        except Exception as e:
            dead_ledgers.append(f"{desk} unreadable: {type(e).__name__}")
    flags.sort()
    detail_bits = dead_ledgers + [s for _, s in flags]
    record(ADVISE, "desk catalyst summons (BD-02)", not detail_bits,
           " · ".join(detail_bits[:4]) + (f" (+{len(detail_bits)-4} more)" if len(detail_bits) > 4 else "")
           if detail_bits else f"{len(SUMMONS_LEDGERS)} desk ledger(s) quiet inside {SUMMONS_WINDOW_DAYS}d",
           "WQ-184 L0 applies: a due desk-ledger row with a dark owner is a Tier-1 spawn (ListAgents first) — "
           "never grade on the owner's behalf; registry = SUMMONS_LEDGERS above")


# ----------------------------------------------------------------------- modes

def check_byte_budgets():
    """Declared read coverage plus the separately governed auto-memory cap."""
    run_script(ADVISE, "declared read budgets", [sys.executable,
               "scripts/read_cap_check.py", "--agent", "PROME", "--require-manifest"],
               "READ_CAP.md · PROME/registry/READS.tsv · full output names affected reads",
               summarize=summarize_read_cap)
    # Keep memory independent: an unassessed manifest must not suppress its check.
    guard(check_memory_budget)


def check_memory_budget():
    try:
        caps = (ROOT / "scripts/harness_caps.env").read_text(encoding="utf-8")
        values = re.findall(r'^MEMORY_HARNESS_CAP_BYTES=(.+)$', caps, re.M)
        if len(values) != 1:
            raise ValueError("missing or duplicate memory cap")
        cap = int(values[0].strip().strip('"'))
        if cap <= 0:
            raise ValueError("memory cap must be positive")
        size = (ROOT / "memory/auto/MEMORY.md").stat().st_size
        pct = size * 100 // cap
        ok, detail = pct < 75, f"MEMORY.md {size} B / {cap} B ({pct}%)"
        if not ok:
            detail += " — ≥75%: rotation due"
    except (OSError, ValueError) as exc:
        ok, detail = False, f"UNKNOWN: {exc}"
    record(ADVISE, "auto-memory byte budget", ok, detail,
           "scripts/harness_caps.env · MEMORY flow rule 8/12")


def check_calendar_views():
    # Both checks use the same caller date even if the pair crosses ET midnight.
    as_of = dt.datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    base = [sys.executable, "scripts/docket_view.py", "--as-of", as_of]
    run_script(ADVISE, "generated calendar freshness", base + ["--check-generated", "PROME/SCRATCH.md"],
               "Regenerate with scripts/docket_view.py --write PROME/SCRATCH.md; source is DOCKET.tsv",
               summarize=summarize_generated)
    run_script(ADVISE, "handwritten calendar coverage", base + ["--check", "PROME/SCRATCH.md",
               "--section", "catalyst calendar", "--ignore", r"\breviews?\b"],
               "Dated handwritten claims only; unassessed claims require inspection; generated content excluded",
               summarize=summarize_prose)


def check_claude_dir_drift():
    """8/29 (Will's .claude/ walkthrough): PROME/.claude/agents/ SHADOWS root .claude/agents/
    for every launch from PROME/ — the harness stops at the nearest copy. The two diverged
    silently (ANVIL's 8/14 hardened rule 10 never reached the copy PROME spawns from).
    🔴 BLOCKING since 2026-09-11 (external review, CODEX point 6). It was ADVISE and it WORKED — it would have
    printed tonight's drift, where `.claude/agents/argus.md` was repaired and `PROME/.claude/agents/argus.md`,
    the copy PROME actually launches from, kept the defective committed-history-only instruction. An advisory
    check that fires and is walked past is `finding_a_check_that_only_advises_is_overridden_the_control_is_
    downstream`: the instrument was never the problem. Promoted rather than replaced — no new checker.
    Any agent/skill file present in one tree and missing or byte-different in the other BLOCKS."""
    # L294 F-3, reproduced 2026-09-12 and fixed here: `Path.glob()` on a MISSING
    # directory yields nothing and raises nothing, so an empty result set was
    # indistinguishable from "every definition agrees". Both trees absent →
    # `bad` empty, `total` 0 → this BLOCKING gate recorded PASS with
    # "0 agent/skill definition(s) identical". A parity gate over nothing
    # establishes nothing; it must fail, and it must say WHICH of the three
    # states it is in — absent tree, empty tree, or real drift. Each is a
    # different repair. `[[finding_gate_pass_is_not_evidence_it_found_the_best_reason]]`
    bad, missing_dirs, total = [], [], 0
    for sub, pat in (("agents", "*.md"), ("skills", "*/SKILL.md")):
        root_d, prome_d = ROOT / ".claude" / sub, ROOT / "PROME/.claude" / sub
        for label, d in (("root", root_d), ("PROME", prome_d)):
            if not d.is_dir():
                missing_dirs.append(f"{label}:.claude/{sub}/")
        rel = lambda p, d: str(p.relative_to(d))
        names = {rel(p, root_d) for p in root_d.glob(pat)} | {rel(p, prome_d) for p in prome_d.glob(pat)}
        total += len(names)
        for n in sorted(names):
            a, b = root_d / n, prome_d / n
            if not a.exists() or not b.exists():
                bad.append(f"{sub}/{n} (only in {'root' if a.exists() else 'PROME'})")
            elif a.read_bytes() != b.read_bytes():
                bad.append(f"{sub}/{n} (differs)")
    if missing_dirs:
        detail = ("CANNOT COMPARE — definition directory absent: " + ", ".join(missing_dirs)
                  + ". This is not agreement; the gate inspected nothing."
                  + (" Also found drift: " + ", ".join(bad) if bad else ""))
    elif total == 0:
        detail = ("CANNOT COMPARE — both trees exist and hold ZERO agent/skill definitions. "
                  "Either the definitions were deleted or the glob patterns no longer match "
                  "(a directory rename does this silently).")
    elif bad:
        detail = "drift: " + ", ".join(bad)
    else:
        detail = f"{total} agent/skill definition(s) identical"
    record(BLOCK, ".claude/{agents,skills} root↔PROME parity",
           not bad and not missing_dirs and total > 0, detail,
           "cp .claude/agents/<name>.md PROME/.claude/agents/ (root is canonical) and commit both; "
           "an absent or empty tree is a MISSING-INPUT failure, never a pass")


def check_review_manifest(tier=None):
    """WQ-240 part 3: a review verdict certifies CONTENT, not a path list.

    BLOCKING when the reviewed candidate CHANGED after the audit — that is the
    case where an old verdict would certify content it never saw. Advisory when
    no manifest exists, because Light/Bounce tiers run no audit; the wording says
    UNKNOWN rather than clean (`[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`)."""
    # ⛔ Severity is selected BEFORE the probe runs. It used to be selected after, so a
    # verifier CRASH — a malformed manifest, a broken import — recorded an advisory and
    # the aggregate returned 0, letting a Standard closeout ship with required review
    # never established. A crash is a cannot-evaluate like any other and must stop the
    # tiers that require a review. (Reproduced by external review, 2026-09-12.)
    required = (tier or "").lower() in ("standard", "heavy")
    sev = BLOCK if required else ADVISE
    untiered = " [no --tier given: review requirement NOT enforced]" if not tier else ""
    sys.path.insert(0, str(ROOT / "PROME" / "tools"))
    try:
        import argus_scope
        rc, lines = argus_scope.verify_review()
    except Exception as e:                      # tool missing/broken => UNKNOWN, never clean
        record(sev, "ARGUS review manifest (content, not paths)", not required,
               ("REQUIRED at this tier and the verifier FAILED — " if required else "UNKNOWN — ")
               + f"{type(e).__name__}: {str(e)[:90]}", "PROME/tools/argus_scope.py")
        return
    detail = " · ".join(lines)[:300]
    if rc == 1:
        record(BLOCK, "ARGUS review manifest (content, not paths)", False, detail,
               "re-review the CHANGED portion and regenerate affected outputs, then "
               "`argus_scope.py --record-review` again — never ship under the old verdict")
        return
    if rc == 2:
        # Standard/Heavy REQUIRE a review, so "cannot evaluate" is a stop, not a note.
        # Below that tier no audit runs, and UNKNOWN is the correct resting state.
        record(sev, "ARGUS review manifest (content, not paths)", not required,
               ("REQUIRED at this tier and missing/unevaluable — " if required else "UNKNOWN" + untiered + " — ") + detail,
               "run `argus_scope.py --record-review`, spawn argus, then `--mark-reviewed`")
        return
    # rc 0: frozen and unchanged. ⛔ A FREEZE IS NOT A REVIEW.
    try:
        verdict = json.loads((ROOT / "PROME/state/argus_review.json")
                             .read_text(encoding="utf-8")).get("verdict", "?")
    except Exception:
        verdict = "?"
    if required and verdict != "REVIEWED":
        record(BLOCK, "ARGUS review manifest (content, not paths)", False,
               f"candidate is {verdict} but never REVIEWED — freezing is not an audit",
               "spawn argus, then `argus_scope.py --mark-reviewed`")
    else:
        record(sev, "ARGUS review manifest (content, not paths)", True,
               f"verdict {verdict}{untiered} · " + detail, "")


def check_publication_prereqs():
    """WQ-240 part 4: check what publication NEEDS early, not at the render.

    The mechanical half only: every OPEN WILL_QUEUE row the Deck will render has
    an explainer row. The other half — whether this session has viewed the live
    artifact — is a harness fact the repo cannot see, and the procedure moves it
    to Pre-closeout so it cannot ambush the end."""
    try:
        q = (ROOT / "PROME/WILL_QUEUE.md").read_text(encoding="utf-8")
        opn = q.split("## OPEN", 1)[-1].split("\n## ", 1)[0]
        rows = set()
        for ln in opn.splitlines():
            cells = split_cells(ln)                      # B1 (9/18): the one split
            if cells and re.fullmatch(r"\d+", cells[0]):
                rows.add(cells[0])
        expl = {ln.split("\t")[0].strip()
                for ln in (ROOT / "PROME/registry/WQ_EXPLAINERS.tsv")
                .read_text(encoding="utf-8").splitlines()[1:] if ln.strip()}
        missing = sorted(rows - expl, key=int)
    except Exception as e:
        record(ADVISE, "publication prerequisites (Deck explainer coverage)", False,
               f"UNKNOWN: {type(e).__name__}: {str(e)[:90]}", "PROME/registry/WQ_EXPLAINERS.tsv")
        return
    record(ADVISE, "publication prerequisites (Deck explainer coverage)", not missing,
           (f"{len(missing)} OPEN row(s) would render with no explainer: " + ", ".join("WQ-" + m for m in missing))
           if missing else f"all {len(rows)} OPEN row(s) have explainer rows",
           "add the row to PROME/registry/WQ_EXPLAINERS.tsv at Pre-closeout, not at the render")


def check_orch_closeout():
    run_script(ADVISE, "orchestrated touch closeout evidence (WQ-249)",
               [sys.executable, "PROME/tools/orch_closeout.py"],
               "Enumerate ORCH_LOG touches, including read-only helpers. Request closeout via the actual "
               "runtime before handoff; record evidence in notes. UNKNOWN is not DARK or a receipt. "
               "Reconcile --expected-key values from the tool record with --inventory-complete; "
               "without that attestation inventory coverage remains UNKNOWN. Reporting only, not BLOCK.")


def mode_boot(advance_board=True):
    check_orch_closeout()
    run_capability("machine credentials (env_doctor)",
                   [sys.executable, "scripts/env_doctor.py", "--quiet"],
                   "PROME/MACHINE_LOCAL.md",
                   dependents="FFIEC call-report pulls · NASA FIRMS hotspot grading (FALCON/OSPREY) · "
                              "FRED/EIA-dependent levels",
                   tracker="238")
    run_script(BLOCK, "position_agreement", [sys.executable, "scripts/position_agreement_check.py",
               "--all", "--quiet"], "owner STATUS is canonical; fix the trade surface")
    run_script(BLOCK, "board_scan", [sys.executable, "PROME/tools/board_scan.py"] +
               (["--advance"] if advance_board else []),
               "BOARD action line ⇒ disposition before proceeding (§3.5.4)")
    # 9/11 (Will "ok go ahead" 13:37 ET): the third-party check on the §3.5 EXEMPT desks. CARL's 9/1→9/11
    # skipped scan was invisible on every surface either side keeps (§3.5.6 at a second desk); this reads BOTH
    # the BOARD and each exempt desk's ledgers, so it needs nothing from the desk. rc=1 = an action-line signal
    # unlogged ≥2d at an exempt desk, or an exempt desk with no ledger at all (UNKNOWN, not PASS).
    run_script(ADVISE, "exempt-desk BOARD gap (§3.5 pull-complete desks vs their ledgers)",
               [sys.executable, "PROME/tools/exempt_gap.py"],
               "the ledger is the DESK's to fill (§3.5.2) — packet/doorbell the desk; no ledger ⇒ the desk owes one; "
               "never grade on its behalf")
    run_script(ADVISE, "firetime (owner-routed flags persist)", [sys.executable,
               "scripts/firetime_check.py", "--window", "7"],  # not --quiet: the flagged lines are the payload
               "scripts/firetime_allowlist.tsv · DATE flag = full logic re-read, never find-replace")
    # 8/14 Will-directed: agent staleness reads come from ground truth, not narrative.
    # rc=1 = unread from-agent packets sit in PROME/inbox — PROME's model of those
    # agents is stale regardless of what SCRATCH's spawn-queue prose says.
    run_script(ADVISE, "agent freshness (ground-truth vs narrative)", [sys.executable,
               "PROME/tools/agent_freshness.py", "--gate"],
               "run PROME/tools/agent_freshness.py --agent <NAME> before ANY launch brief; drain first")
    # R1 corrections check (FORUM-6 ruling ①, Will-approved 2026-08-17; wired for PROME 2026-08-28 at the
    # DAEDALUS R1 batch — BOOT.md rule: new fleet-wide checks land in THIS script, prose points here).
    # rc=1 = a NAMED correction is unreceipted → read the pointer, receipt it, commit registry/corrections_receipts.tsv.
    run_script(ADVISE, "R1 corrections check (FORUM-6 ①)", [sys.executable,
               "scripts/corrections_boot_check.py", "PROME"],
               "rc=1 = a NAMED correction is unreceipted: read the pointer, then "
               "`scripts/corrections_boot_check.py PROME --receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` "
               "and commit PROME/registry/corrections_receipts.tsv")
    guard(check_gates_tsv)
    guard(check_docket_overdue)
    guard(check_docket_buried_state_token)
    guard(check_calendar_views)
    guard(check_will_queue)
    guard(check_aged_waits)  # WQ-221 instrument — boot only; closeout slates via spawn_list
    run_script(ADVISE, "willq_view drift (SCRATCH Pending-Will block vs WILL_QUEUE OPEN)", [sys.executable,
               "PROME/tools/willq_view.py", "--check", "PROME/SCRATCH.md"],
               "WQ-185 ② (Will 2026-09-06 10:12): the operator card's Pending-Will line is GENERATED — a flag = the "
               "queue moved since the last render or a hand copy survives outside the markers; regenerate with "
               "`python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`; never edit inside the markers")
    guard(check_heartbeat_chain)
    # 2026-09-13: a markdown row with MORE cells than its header has the excess
    # DROPPED at render, silently. PROME/STATUS.md L21 lost two cells that way —
    # visible to a `cat`, invisible to the operator and to every rendered view,
    # and spine audit #13 read the file the same day without seeing it. ADVISE
    # here because the reader only needs warning; BLOCK at closeout, where the
    # rows are written. Acceptance conditions:
    # PROME/tools/tests/ACCEPTANCE_table_check_overcelled_rows.md
    run_script(ADVISE, "boot-read tables: no over-celled rows",
               [sys.executable, "PROME/tools/table_check.py", "--quiet"],
               "fix the ROW (split the content into the existing columns or add a column to the "
               "header) — never the reader; rc=2 = a manifest path could not be opened")
    guard(check_dashboard_state)
    guard(check_symmetry)
    guard(check_claude_dir_drift)
    guard(check_desk_catalyst_summons)
    # WQ-184 L1 (Will 2026-09-05 21:42 "approve WQ-184 with your recs"): the spawn driver. rc=1 = a DARK row —
    # a registered dated row has arrived and its owner has no self-commit since; under L0 that is a Tier-1
    # spawn at THIS boot (ListAgents first; cap 4; ACTIVE ⇒ consumer read at the owner's artifact first).
    run_script(ADVISE, "spawn list — L0 due-row candidates (WQ-184)",
               [sys.executable, "PROME/tools/spawn_list.py", "--horizon", "0"],
               "DARK ⇒ ListAgents same minute → Tier-1 spawn (cap 4/boot) or doorbell a live desk; "
               "ACTIVE ⇒ read the owner's artifact first (receipt gap); WILL ⇒ queue; PROME ⇒ do it")
    presence_cmd = [sys.executable, "PROME/tools/session_presence.py"]
    if SESSION_JSON:
        presence_cmd += ["--sessions-json", str(SESSION_JSON)]
    run_script(ADVISE, "session evidence beside ALL due rows — fleet presence UNKNOWN",
               presence_cmd, "read full output; snapshot is NOT native spawn preflight or proof of absence")
    guard(check_byte_budgets)


def mode_closeout(tier=None):
    check_orch_closeout()
    guard(check_review_manifest, tier)
    guard(check_publication_prereqs)
    run_script(BLOCK, "position_agreement", [sys.executable, "scripts/position_agreement_check.py",
               "--all", "--quiet"], "owner STATUS is canonical")
    guard(check_gates_tsv)          # FIRED-UNEXECUTED must never leave a session
    guard(check_docket_overdue)
    guard(check_docket_buried_state_token)
    guard(check_docket_today)       # the pre-fire analogue: don't go dark before today's items
    guard(check_calendar_views)
    guard(check_desk_catalyst_summons)  # don't go dark on a desk's catalyst eve (BD-02)
    # WQ-184 L1 closeout half: what LANDS before the next likely boot (1d weekday, 3d Fri/Sat) and who is there —
    # slate them in the closeout report (8/27 precedent); the spawn itself waits for the first boot on/after the date. Never silence.
    _gap = "3" if dt.date.today().weekday() in (4, 5) else "1"
    run_script(ADVISE, f"spawn list — rows landing before the next boot (+{_gap}d, WQ-184)",
               [sys.executable, "PROME/tools/spawn_list.py", "--horizon", _gap, "--tsv"],
               "LANDS-IN rows with a dark owner ⇒ SLATE them in the closeout report (the spawn waits for the first "
               "boot on/after the date, or Will's word from the slate); DARK ⇒ act before going dark")
    guard(check_will_queue)
    run_script(ADVISE, "willq_view drift (SCRATCH Pending-Will block vs WILL_QUEUE OPEN)", [sys.executable,
               "PROME/tools/willq_view.py", "--check", "PROME/SCRATCH.md"],
               "WQ-185 ② (Will 2026-09-06 10:12): the operator card's Pending-Will line is GENERATED — a flag = the "
               "queue moved since the last render or a hand copy survives outside the markers; regenerate with "
               "`python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`; never edit inside the markers")
    guard(check_heartbeat_chain)    # the ~5-amendment re-base rule, mechanized (was prose-only on 5 surfaces)
    guard(check_dashboard_state)    # Standard+ closeouts regenerate; this catches a skipped one
    guard(check_byte_budgets)       # flow-rule meter: >=75% here means rotate NOW, in this closeout
    # BLOCKING at closeout and advisory at boot, deliberately: closeout is where
    # these rows get WRITTEN, so this is the only run that can stop the defect
    # from shipping. Shipping it costs a rendered reader the content entirely.
    run_script(BLOCK, "boot-read tables: no over-celled rows",
               [sys.executable, "PROME/tools/table_check.py", "--quiet"],
               "fix the ROW before committing — the named cells are DROPPED in every rendered read")
    guard(check_claude_dir_drift)   # root<->PROME skill/agent parity at CLOSEOUT too (REV 8/29): a closeout that edits one tree would otherwise ship drift and find it next boot
    run_script(ADVISE, "orphan_check (advisory by design)", ["bash", "scripts/orphan_check.sh", "PROME"],
               "[likely YOURS] = commit per carve-out ① · [not yours] = flag, never sweep")
    record(ADVISE, "MANUAL: memory_index_check", True,
           "if you wrote/edited an auto-memory: scripts/memory_index_check.py --strict --slug <name> (root step 1d)",
           "root CLAUDE.md carve-out ③")
    record(ADVISE, "MANUAL: consumer_check", True,
           "if you superseded a published number: scripts/consumer_check.py --old <v> --new <v> (root step 1c); "
           "canon/threshold change ⇒ add --mirror-map (T1-b)",
           "root CLAUDE.md step 1c + PROME/SYSTEM.md Mirror Map")
    # 8/16 (RAV addition, Will-approved): the two WILL_QUEUE parsers duplicate
    # their visibility regexes by design — this synthetic-row test is what
    # keeps them agreeing (the lettered-ID fix shipped to the gate only and
    # the brief silently diverged; this would have caught it same-day).
    run_script(ADVISE, "queue-parser selftest (gate vs will_brief)",
               [sys.executable, "PROME/tools/queue_parser_selftest.py"],
               "PROME/tools/queue_parser_selftest.py")


def main():
    global LOG_DIR, SESSION_JSON
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("mode", choices=["boot", "refresh", "closeout"])
    ap.add_argument("--log-dir", type=Path, help="New directory for complete child-check output")
    ap.add_argument("--sessions-json", type=Path, help="Optional fresh same-host inventory for boot")
    ap.add_argument("--tier", choices=["bounce", "light", "standard", "heavy"],
                    help="closeout tier; standard/heavy REQUIRE a recorded ARGUS review "
                         "(missing or unevaluable becomes BLOCKING)")
    args = ap.parse_args()
    results.clear()
    capabilities.clear()
    if args.log_dir:
        args.log_dir.mkdir(parents=True, exist_ok=False)
        LOG_DIR = args.log_dir.resolve()
    else:
        LOG_DIR = Path(tempfile.mkdtemp(prefix="prome-gate-checks-"))
    SESSION_JSON = args.sessions_json.resolve() if args.sessions_json else None

    # L294 F-7: the mode call itself is the last unguarded frame. guard() covers each
    # check, but anything raising BETWEEN checks would still discard the whole run's
    # output, which is the defect's worst symptom (empty stdout, no summary). The
    # summary is now printed in every path.
    try:
        if args.mode == "boot":
            mode_boot()
        elif args.mode == "refresh":
            mode_boot(advance_board=False)
        else:
            mode_closeout(args.tier)
    except BaseException as e:
        record(ERROR, "GATE RUN ABORTED", False,
               f"{type(e).__name__}: {str(e)[:160]} — the run stopped OUTSIDE any single "
               "check; every check after this point was NOT evaluated",
               "re-run the gate after fixing the cause; results below are PARTIAL")

    errored = [r for r in results if r[0] == ERROR]
    blocking_fail = [r for r in results if r[0] == BLOCK and not r[2]]
    rc = aggregate_rc(results, capabilities)
    verdict = ("⚠️  INCOMPLETE — NOT A PASS" if errored
               else "🔴 BLOCKED" if blocking_fail else "✅ PASS")
    print(f"\n{'='*70}\n  PROME GATE · {args.mode.upper()} · {verdict} "
          f"({sum(1 for r in results if r[0]==BLOCK)} blocking / "
          f"{sum(1 for r in results if r[0]==ADVISE)} advisory"
          + (f" / {len(errored)} NOT RUN" if errored else "") + f")\n{'='*70}")
    if errored:
        print(f"  ⚠️  {len(errored)} check(s) did not run. Their subjects are UNKNOWN, not clean.")
        print("      rc=2 = COULD NOT ESTABLISH. Do not read this run as evidence of anything "
              "they cover.\n")
    for sev, name, ok, detail, owner in results:
        mark = "✅" if ok else ("⚠️ " if sev == ERROR else "🔴" if sev == BLOCK else "⚠️ ")
        print(f"  {mark} [{sev:8}] {name}: {detail}")
        if not ok:
            print(f"       → {owner}")
    if capabilities:
        print(f"  {'-'*66}\n  CAPABILITIES — never gate unrelated work; reported every run until RESTORED")
        for name, state, detail, owner, dependents, tracker in capabilities:
            urgent = state != CAP_AVAILABLE and _tracker_overdue(tracker)
            mark = {CAP_AVAILABLE: "✅", CAP_UNAVAILABLE: "⛔", CAP_UNKNOWN: "❓"}[state]
            print(f"  {mark} [{state:11}] {name}: {detail}")
            if state != CAP_AVAILABLE:
                print(f"       ↳ withholds: {dependents}")
                print(f"       ↳ unrelated work PROCEEDS — this is not a gate")
                if tracker:
                    print(f"       ↳ {'🔴 URGENT — WQ-' + tracker + ' is PAST its needed-by; escalate to Will this session' if urgent else 'tracked at WQ-' + tracker}")
                print(f"       → {owner}")
    print(f"{'='*70}")
    if errored:
        # rc=2 with zero blocking failures would otherwise have printed
        # "0 BLOCKING gate(s) failed", which reads like good news.
        print(f"  ⚠️  INCOMPLETE: {len(errored)} check(s) NOT RUN"
              + (f", {len(blocking_fail)} BLOCKING failure(s) among those that did"
                 if blocking_fail else "")
              + ". rc=2 — this run establishes nothing about the unevaluated subjects.\n")
        return rc
    if rc:
        print(f"  🔴 {len(blocking_fail)} BLOCKING gate(s) failed — disposition before new work.\n")
        return rc
    print("  ✅ all blocking gates pass — advisories above are judgment calls, read them.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
