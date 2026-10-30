#!/usr/bin/env python3
"""Render the three pinned design copies. No live queue, intake or owner writes."""
from __future__ import annotations

from copy import deepcopy
from datetime import date
from functools import lru_cache
from html import escape
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
COPY_REV = "e948bfdbf4b01038ad9f2f3cb707bcdf1ff83cc5"
SCHEMA_REV = "ddb8148bcba7ce13204aceff865799fb66fb920b"
COPY_DIR = "PROME/prototypes/wq-record-copies-2026-10-30"
SCHEMA_PATH = "AGENTS/CATO/prototypes/decisions/record-draft/record.schema.json"
GROUPS = ("Decisions", "Tasks for me", "Follow-through", "History")
SLUGS = {name: f"view-{i}" for i, name in enumerate(GROUPS)}


@lru_cache(maxsize=None)
def source_text(commit: str, path: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("A full pinned commit is required for this comparison")
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError("Out-of-workspace source path")
    resolved = (ROOT / candidate).resolve()
    if not resolved.is_relative_to(ROOT):
        raise ValueError("Source symlink escapes workspace")
    return subprocess.check_output(
        ["git", "show", f"{commit}:{path}"], cwd=ROOT, text=True,
        encoding="utf-8", stderr=subprocess.PIPE,
    )


def unique(values, label):
    if len(set(values)) != len(values):
        raise ValueError(f"Duplicate {label}")


def validate_record(record, schema):
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(record)
    units = record["units"]
    unique([u["id"] for u in units], "unit ID")
    unique([s["id"] for s in record["sources"]], "source ID")
    sources = {s["id"]: s for s in record["sources"]}
    for unit in units:
        if not unit["id"].startswith(record["wq_id"] + "."):
            raise ValueError("Unit belongs to another WQ")
        choices = [c["id"] for c in unit["proposal"]["choices"]]
        unique(choices, "choice ID")
        rec = unit["proposal"]["recommendation"]["option_id"]
        if rec is not None and rec not in choices:
            raise ValueError("Unresolved recommended option")
        refs = unit["proposal"]["source_ids"] + unit["disposition"]["source_ids"]
        refs += [f["source_id"] for f in unit["follow_through"]]
        ruling = unit["disposition"]["ruling"]
        if ruling:
            refs += [ruling["source_id"], *ruling["proposal_source_ids"]]
            if (ruling["answered_proposal_revision"] == unit["proposal"]["revision"]
                    and ruling["selected_option_id"] is not None
                    and ruling["selected_option_id"] not in choices):
                raise ValueError("Selected option missing from the answered revision")
        if any(ref not in sources for ref in refs):
            raise ValueError("Unresolved source reference")
    for correction in record["corrections"]:
        if correction["source_id"] not in sources:
            raise ValueError("Unresolved correction source")
        if not set(correction["affected_unit_ids"]) <= {u["id"] for u in units}:
            raise ValueError("Correction refers to an unknown unit")
    for src in sources.values():
        source_text(src["commit"], src["path"])


def load_records():
    schema = json.loads(source_text(SCHEMA_REV, SCHEMA_PATH))
    Draft202012Validator.check_schema(schema)
    records = []
    for wq in ("495", "551", "552"):
        record = json.loads(source_text(COPY_REV, f"{COPY_DIR}/WQ-{wq}.json"))
        if record["wq_id"] != wq:
            raise ValueError("Copy name and WQ ID disagree")
        validate_record(record, schema)
        records.append(record)
    return records


def observe(source, key):
    """Small explicit adapters for these copies; no general owner-state parser."""
    text = source_text(source["commit"], source["path"])
    out = {"source_id": source["id"], "key": key, "commit": source["commit"],
           "status": "unknown", "evidence": "No supported completion interpretation."}
    if source["path"] == "PROME/DOCKET.tsv" and re.fullmatch(r"L[1-9][0-9]*", key):
        # L numbers are the canonical, append-only physical-line citation keys.
        line = int(key[1:])
        lines = text.splitlines()
        if line > len(lines):
            return out
        cells = lines[line - 1].split("\t")
        if len(cells) < 4 or lines[line - 1].startswith("#"):
            return out
        out.update(owner=cells[2], due=cells[0], evidence=cells[3])
        if re.match(r"^PENDING\b", cells[3]):
            out["status"] = "pending_at_snapshot"
        # A terminal docket label alone would not certify required verification.
    elif source["path"].endswith(".md") and key.startswith("Completion (WQ-229):"):
        lines = [line for line in text.splitlines() if line.startswith("**Completion (WQ-229):**")]
        if len(lines) == 1:
            out["evidence"] = lines[0]
            if all(marker in lines[0] for marker in (
                "IMPLEMENTED", "TESTED", "INDEPENDENTLY VERIFIED", "STILL UNRESOLVED: none"
            )):
                out["status"] = "owner_reports_complete"
    elif source["id"] == "boot-encoded":
        out.update(status="supporting_artifact", evidence="Pinned implementation artifact exists; its behavior was not reverified by CATO.")
    return out


def placement(unit, observations):
    state = unit["disposition"]["state"]
    if unit["kind"] == "hands" and state == "outstanding":
        return "Tasks for me"
    if unit["kind"] == "decision" and state == "awaiting_answer":
        return "Decisions"
    if state in {"deferred", "changes_requested", "reported_done", "unknown"}:
        return "Follow-through"
    statuses = {o["status"] for o in observations}
    if statuses & {"pending_at_snapshot", "unknown"}:
        return "Follow-through"
    if observations and "owner_reports_complete" not in statuses:
        return "Follow-through"
    return "History"


def project(records):
    unique([r["wq_id"] for r in records], "WQ ID across records")
    groups = {name: [] for name in GROUPS}
    for record in records:
        sources = {s["id"]: s for s in record["sources"]}
        for unit in record["units"]:
            obs = [observe(sources[f["source_id"]], f["key"]) for f in unit["follow_through"]]
            entry = {"wq_id": record["wq_id"], "title": record["title"],
                     "unit": deepcopy(unit), "sources": deepcopy(record["sources"]),
                     "observations": obs, "controls": [],
                     "corrections": [deepcopy(c) for c in record["corrections"] if unit["id"] in c["affected_unit_ids"]]}
            ruling = unit["disposition"]["ruling"]
            entry["snapshot_assessment"] = None
            if ruling:
                entry["snapshot_assessment"] = (
                    "PROME labels this snapshot exact. Exact displayed terms are not established by this comparison; a letter naming a committed option does not prove the full chat display."
                    if ruling["snapshot_quality"] == "exact" else
                    f"{ruling['snapshot_quality'].capitalize()} snapshot: the original ruling is retained; the exact display is not claimed."
                )
            groups[placement(unit, obs)].append(entry)
    return {"kind": "pinned design-copy comparison; no live authority", "mapping_commit": COPY_REV,
            "schema_commit": SCHEMA_REV, "counts": {k: len(v) for k, v in groups.items()}, "groups": groups}


def md(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def anchor(uid):
    return "unit-" + uid.replace(".", "-")


def unit_summary(unit, include_basis=False):
    state = unit["disposition"]["state"]
    ruling = unit["disposition"]["ruling"]
    selected = f" {ruling['selected_option_id']}" if ruling and ruling["selected_option_id"] else ""
    terms = " ".join(ruling["conditions"]) if ruling else unit["disposition"]["basis"]
    basis = " Recorded basis (owner account): " + unit["disposition"]["basis"] if include_basis else ""
    return f"{unit['id']} = {state.upper()}{selected}. {terms}{basis} [Full terms](index.html#{anchor(unit['id'])})"


def queue_markdown(records):
    out = ["# Generated comparison — copies only", "", f"Mapping source: `{COPY_REV}`. Pinned history, not the live queue.", "",
           "## OPEN", "", "| # | Item | Type | Needed by | Since | Recommendation | Notes |", "|---|---|---|---|---|---|---|"]
    done, deferred = [], []
    for record in records:
        active = [u for u in record["units"] if (u["kind"] == "hands" and u["disposition"]["state"] == "outstanding")
                  or (u["kind"] == "decision" and u["disposition"]["state"] == "awaiting_answer")]
        if active:
            kinds = {u["kind"] for u in active}
            kind = "HANDS" if kinds == {"hands"} else "RULE" if kinds == {"decision"} else "MIXED"
            item = " · ".join(f"{u['id']} — {u['proposal']['question']} {u['proposal']['context']}" for u in active)
            settled = [u for u in record["units"] if u not in active]
            if settled:
                item += " Settled units for context only, not asked: " + " · ".join(unit_summary(u) for u in settled)
            dated = sorted((u["timing"]["needed_by"], u["id"]) for u in active if u["timing"]["needed_by"])
            due = f"{dated[0][0]} ({dated[0][1]})" if dated else "—"
            since = date.fromisoformat(record["registered_on"]).strftime("%m/%d") if record["registered_on"] else "—"
            rec = "Personal action; nothing to approve." if kind == "HANDS" else " · ".join(u["proposal"]["recommendation"]["reason"] for u in active)
            notes = " · ".join(c for u in active for c in u["proposal"]["caveats"])
            out.append("| " + " | ".join(md(x) for x in [record["wq_id"], item, kind, due, since, rec, notes]) + " |")
        else:
            text = " · ".join(unit_summary(u, include_basis=True) for u in record["units"])
            for correction in record["corrections"]:
                text += " CORRECTION — " + correction["summary"]
            stamps = sorted({u["disposition"]["ruling"]["as_recorded_at"] for u in record["units"]
                             if u["disposition"]["ruling"] and u["disposition"]["ruling"]["as_recorded_at"]})
            done.append("| " + " | ".join(md(x) for x in [record["wq_id"], " · ".join(stamps) or "Unknown", text]) + " |")
        for unit in record["units"]:
            if unit["disposition"]["state"] == "deferred":
                deferred.append("| " + " | ".join(md(x) for x in [unit["id"], "DEFERRED — not approved or declined",
                    unit["timing"]["revisit_condition"] or "Revisit condition unspecified", f"[Full terms](index.html#{anchor(unit['id'])})"]) + " |")
    out += ["", "## RECENTLY DONE — ruling state, not implementation completion", "", "| WQ | Ruling recorded at | Record |", "|---|---|---|", *done,
            "", "## Deferred — re-present on", "", "Display of existing conditions only; this creates no boot routine or automatic re-ask.", "",
            "| Unit | State | Condition | Evidence |", "|---|---|---|---|", *deferred, ""]
    return "\n".join(out)


def source_link(source):
    url = f"https://github.com/williepowen-debug/Research-workspace/blob/{source['commit']}/{quote(source['path'])}"
    return f'<a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(source["id"])} · {escape(source["path"])} @ {source["commit"][:9]}</a>'


def card(entry):
    u = entry["unit"]
    p, d = u["proposal"], u["disposition"]
    e = escape
    parts = [f'<article id="{anchor(u["id"])}" data-unit="{u["id"]}" data-state="{d["state"]}">',
             f'<div class="eyebrow">WQ-{entry["wq_id"]} · {e(u["kind"])}</div><h2>{e(u["id"])} <span class="badge">{e(d["state"].replace("_", " "))}</span></h2>',
             f'<h3>{e(p["question"])}</h3><p>{e(p["context"])}</p>']
    for correction in entry["corrections"]:
        parts.append(f'<div class="notice correction"><strong>Implementation correction — original ruling retained</strong><p>{e(correction["summary"])}</p></div>')
    if entry["snapshot_assessment"]:
        parts.append(f'<div class="notice snapshot">{e(entry["snapshot_assessment"])}</div>')
    if u["timing"]["revisit_condition"]:
        parts.append(f'<div class="notice revisit"><strong>Re-present when</strong><p>{e(u["timing"]["revisit_condition"])}</p><p>No approval, decline or automatic re-ask is inferred.</p></div>')
    if u["timing"]["needed_by"]:
        parts.append(f'<p><strong>Source date: {e(u["timing"]["needed_by"])}</strong> — {e(u["timing"]["meaning"] or "Meaning unavailable")}</p>')
    parts.append('<ul class="caveats">' + "".join(f'<li>{e(c)}</li>' for c in p["caveats"]) + '</ul>')
    if d["ruling"]:
        r = d["ruling"]
        parts += [f'<blockquote>{e(r["verbatim"])}</blockquote>', f'<p class="muted">Ruling recorded: {e(r["as_recorded_at"] or "Unknown")}</p>',
                  '<ul>' + ''.join(f'<li>{e(c)}</li>' for c in r["conditions"]) + '</ul>']
    parts.append(f'<p><strong>Recorded basis:</strong> {e(d["basis"])}</p>')
    if entry["observations"]:
        parts.append('<h3>Linked owner evidence at the pinned revision</h3>')
        for o in entry["observations"]:
            label = {"pending_at_snapshot": "Pending at source snapshot", "owner_reports_complete": "Owner reports completion; CATO has not independently verified implementation", "supporting_artifact": "Supporting artifact", "unknown": "Unknown"}[o["status"]]
            parts.append(f'<details class="observation"><summary>{e(o["key"])} — {label}</summary><p>{e(o["evidence"])}</p><p class="muted">Source commit {o["commit"]}</p></details>')
    if p["choices"]:
        parts.append('<details><summary>Choices in PROME’s mapping — historical reference, no response controls</summary>')
        for c in p["choices"]:
            parts.append(f'<h4>Mapping choice {e(c["id"])} · {e(c["label"])}</h4><p>{e(c["meaning"])}</p><p>{e(c["consequence"])}</p>')
        parts.append('</details>')
    parts.append('<details><summary>Original sources at pinned commits</summary><ul class="sources">' + ''.join('<li>' + source_link(s) + '</li>' for s in entry["sources"]) + '</ul></details>')
    parts.append('<p class="muted">Read-only comparison. No response is saved or sent.</p></article>')
    return '\n'.join(parts)


def html_document(model, queue):
    nav, panels = [], []
    for group in GROUPS:
        slug = SLUGS[group]
        nav.append(f'<button class="nav" data-view="{slug}" aria-pressed="false">{escape(group)} <span>{model["counts"][group]}</span></button>')
        cards = ''.join(card(entry) for entry in model["groups"][group])
        panels.append(f'<section id="{slug}" class="panel" hidden><h2 class="section-title">{escape(group)}</h2>{cards or "<p class=empty>No units in this category in these three copies.</p>"}</section>')
    nav.append('<button class="nav" data-view="queue" aria-pressed="false">Generated queue</button>')
    panels.append('<section id="queue" class="panel" hidden><h2>Generated queue representation</h2><p>Copy only. Dates below label the ruling; implementation completion is separate. Existing deferral conditions are made visible without adding a routine.</p><pre>' + escape(queue) + '</pre></section>')
    counts = model["counts"]
    summary = f'{counts["Tasks for me"]} personal task(s) · {counts["Follow-through"]} follow-through unit(s) · {counts["History"]} history unit(s) · {counts["Decisions"]} unanswered decision(s) in this sample.'
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'none'; form-action 'none'; base-uri 'none'">
<title>Decisions — three-record comparison</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f1e9;color:#223b3a;font:16px/1.6 system-ui,sans-serif}header{padding:30px 6vw 24px;background:#173e3a;color:#fff}header h1{font:38px/1.2 Georgia,serif;margin:6px 0 12px}header p{max-width:960px;margin:6px 0}.small{font-size:13px;opacity:.85}.layout{max-width:1300px;margin:auto;display:grid;grid-template-columns:235px minmax(0,1fr);gap:30px;padding:30px}nav{align-self:start;position:sticky;top:20px;display:grid;gap:10px}.nav{font:inherit;text-align:left;padding:12px;border:1px solid #ccd8d1;background:#fffdf7;color:#173e3a;border-radius:9px;cursor:pointer}.nav span{float:right}.nav[aria-pressed=true]{background:#173e3a;color:white}main{min-width:0}article{background:#fffdf7;border:1px solid #d8ded5;border-radius:13px;padding:27px;margin:0 0 24px;overflow-wrap:anywhere}h2{font:27px/1.3 Georgia,serif;margin:6px 0 14px}h3{font-size:18px;line-height:1.4}h4{margin-bottom:4px}.eyebrow{text-transform:uppercase;letter-spacing:1px;font-size:12px;color:#526c68}.badge{font:12px system-ui,sans-serif;display:inline-block;background:#e4ede6;border:1px solid #bed1c5;padding:6px 9px;border-radius:14px;vertical-align:middle}.notice{background:#f7ecd2;border-left:4px solid #b58b32;border-radius:4px;padding:13px 17px;margin:16px 0}.notice p{margin:6px 0}.revisit{background:#e4efed;border-color:#397e75}.caveats{padding-left:20px}.muted{font-size:13px;color:#5a6d69}blockquote{border-left:3px solid #6b9389;padding:6px 17px;margin:22px 0;font:22px/1.5 Georgia,serif}details{margin:12px 0;padding:12px 14px;background:#f1f3eb;border-radius:6px}summary{cursor:pointer;font-weight:600}a{color:#226d61}.sources{padding-left:20px;font-size:13px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.7 ui-monospace,monospace;background:#fffdf7;border:1px solid #d8ded5;border-radius:10px;padding:20px}.empty{background:#fffdf7;padding:28px;border-radius:10px}.section-title{margin-bottom:20px}[hidden]{display:none!important}@media(max-width:760px){header{padding:24px}header h1{font-size:30px}.layout{display:block;padding:18px}nav{position:static;grid-template-columns:1fr 1fr;margin-bottom:24px}article{padding:20px}.nav{font-size:14px}}
</style></head><body><header><div class="small">CATO × PROME · DESIGN COMPARISON</div><h1>Real records, separate meanings</h1><p>Three pinned copies: WQ-495, WQ-551 and WQ-552. These are historical snapshots for review. Nothing here changes the live queue or accepts responses.</p><p class="small">''' + summary + '</p></header><div class="layout"><nav aria-label="Views">' + ''.join(nav) + '</nav><main>' + ''.join(panels) + '''</main></div><script>
function show(id){document.querySelectorAll('.panel').forEach(p=>p.hidden=p.id!==id);document.querySelectorAll('.nav').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===id)));}
document.querySelectorAll('.nav').forEach(b=>b.addEventListener('click',()=>show(b.dataset.view)));
function followHash(){const target=document.getElementById(location.hash.slice(1));if(target&&target.closest('.panel')){show(target.closest('.panel').id);target.scrollIntoView();}}
show('view-1');addEventListener('hashchange',followHash);if(location.hash)followHash();
</script></body></html>'''


def build():
    records = load_records()
    model = project(records)
    queue = queue_markdown(records)
    artifacts = {"view.json": json.dumps(model, ensure_ascii=False, indent=2) + "\n",
                 "queue.md": queue, "index.html": html_document(model, queue)}
    # All reads and validation finish before writing only our generated copies.
    for name, content in artifacts.items():
        (HERE / name).write_text(content, encoding="utf-8")
    print(json.dumps({"mapping_commit": COPY_REV, "counts": model["counts"],
                      "outputs": {k: hashlib.sha256(v.encode()).hexdigest() for k, v in artifacts.items()}}, indent=2))


if __name__ == "__main__":
    build()
