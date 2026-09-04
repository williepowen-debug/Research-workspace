#!/usr/bin/env python3
"""gen_board_index.py — GENERATE `BOARD/INDEX.md` from signal frontmatter (WQ-174, Will "174 - approved" 2026-09-04).

Design: AGENTS/WALTER/design/BOARD_INDEX_GENERATION_DESIGN.md v0.1.

    --check        derive the row set from BOARD/SIG-W-*.md and DIFF it against the LIVE INDEX.md:
                   ID set · per-cluster counts · TOTAL · every lifecycle/correction marker on a live row
                   must have a frontmatter source (status: on the signal, or an inverted corrects: from
                   another signal). Exit 1 on any gap. NEVER writes.
    --write PATH   render the generated index to PATH (default BOARD/INDEX.generated.md). Refuses to
                   write over BOARD/INDEX.md unless --cutover is also given.
    --cutover      allow --write to target BOARD/INDEX.md (the swap; Will-gated, WQ-174 leg 3).
    --sha          print the row-set sha256 only (what the doctor's index_generated_fresh compares).

Fail-closed: a signal missing signal_id/date/cluster/precedence is a HARD error naming the file.
Structure preserved EXACTLY for walter_doctor's parser: ToC rows `| [NAME](#anchor) | N | latest | theme |`,
section headings `## NAME (N)`, and the `| **TOTAL** | **N** |` row.
"""
from __future__ import annotations
import argparse, hashlib, os, re, sys, glob
from collections import OrderedDict, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BOARD = os.path.join(ROOT, "BOARD")
LIVE = os.path.join(BOARD, "INDEX.md")
TAXONOMY = os.path.join(ROOT, "AGENTS", "WALTER", "design", "CLUSTER_TAXONOMY.md")
TITLE_CAP = 140
SIG_RE = re.compile(r"^(SIG-W-\d{8}-\d{3})")
ROW_RE = re.compile(r"^\s*\| (SIG-W-\d{8}-\d{3}) \|")
MARK_RE = re.compile(r"SUPERSEDED|FALSIFIED|EVENT-PASSED|PARTIALLY-CORRECTED|PARTIALLY-SUPERSEDED|ERRATUM \d|CORRECTED 2026|→ `SIG-W")

# ---------------------------------------------------------------- frontmatter
def parse_front(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    fm = {}
    for line in text[4:end].split("\n"):
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    fm["__body"] = text[end + 5:]
    return fm

def listify(v: str) -> list[str]:
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    return [x.strip().strip("`'\"") for x in v.split(",") if x.strip()]

def h1(body: str, fallback: str) -> str:
    for line in body.split("\n"):
        if line.startswith("# "):
            t = line[2:].strip()
            return t
    return fallback

LEGACY_TITLES = os.path.join(ROOT, "AGENTS", "WALTER", "registry", "INDEX_LEGACY_TITLES.tsv")
DIRECTION_FIELD_SINCE = "2026-09-04"  # FORMAT_SPEC v0.20 — DIRECTION-MISSING is flagged only on corrections dated from here

def legacy_titles() -> dict:
    out = {}
    if os.path.exists(LEGACY_TITLES):
        for line in open(LEGACY_TITLES, encoding="utf-8"):
            if line.startswith("#") or line.startswith("signal_id\t") or "\t" not in line:
                continue
            k, v = line.rstrip("\n").split("\t", 1)
            out[k] = v
    return out

def load_signals() -> OrderedDict:
    sigs = OrderedDict()
    errors = []
    legacy = legacy_titles()
    for f in sorted(glob.glob(os.path.join(BOARD, "SIG-W-*.md"))):
        base = os.path.basename(f)
        sid = SIG_RE.match(base).group(1)
        text = open(f, encoding="utf-8", errors="replace").read()
        fm = parse_front(text)
        if not fm:
            errors.append(f"{base}: no frontmatter block"); continue
        # date: v0.8+ `date:`; v0.1 `timestamp:`; `dispatched:`; last resort the filename YYYYMMDD
        def clean(v):  # strip a trailing inline comment ("INFLATION_TRANSMISSION  # reclassified …")
            return re.split(r"\s+#", v or "", 1)[0].strip()
        date = clean(fm.get("date")) or clean(fm.get("timestamp"))[:10] or clean(fm.get("dispatched"))[:10]
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            date = f"{sid[6:10]}-{sid[10:12]}-{sid[12:14]}"  # filename date — always present, recorded as fallback
        fm["date"] = date
        for k in ("cluster", "precedence"):
            fm[k] = clean(fm.get(k))
            if not fm.get(k):
                errors.append(f"{base}: missing `{k}:`")
        action = listify(fm.get("action") or fm.get("to", ""))
        info = listify(fm.get("info", ""))
        sigs[sid] = dict(
            id=sid, file=base, date=fm.get("date", ""), domain=fm.get("domain", ""),
            cluster=fm.get("cluster", ""), precedence=fm.get("precedence", ""),
            action=action, info=info, confidence=fm.get("confidence", ""),
            title=(h1(fm["__body"], "") or legacy.get(sid) or fm.get("verdict", "").split(". ")[0] or base[19:-3].replace("-", " ")),
            status=fm.get("status", ""), status_ref=fm.get("status_ref", ""), status_date=fm.get("status_date", ""),
            corrects=[x for x in re.findall(r"SIG-W-\d{8}-\d{3}", fm.get("corrects", "")) if x != sid],
            corrects_direction=fm.get("corrects_direction", ""),
        )
    return sigs, errors

def derive_markers(sigs: OrderedDict) -> dict[str, list[str]]:
    """Back-markers: inverted corrects: (from the correcting signal) + the signal's own status."""
    marks = defaultdict(list)
    for sid, s in sigs.items():
        for t in s["corrects"]:
            if t in sigs:
                d = s["corrects_direction"]
                tag = f" ({d.split(' — ')[0].strip()})" if d else (" (DIRECTION-MISSING)" if s["date"] >= DIRECTION_FIELD_SINCE else "")
                line = f"⚠️ **CORRECTED {s['date']} → `{sid}`{tag}**"
                if d and " — " in d:
                    line += " " + d.split(" — ", 1)[1].strip()
                marks[t].append(line)
    for sid, s in sigs.items():
        if s["status"]:
            marks[sid].append(f"🚩 **{s['status']} {s['status_date']}** — {s['status_ref']}".rstrip(" —"))
    return marks

# ---------------------------------------------------------------- live index
def parse_live(path: str = LIVE):
    text = open(path, encoding="utf-8", errors="replace").read()
    rows = {}; section = None; counts = OrderedDict()
    for line in text.split("\n"):
        m = re.match(r"^## ([A-Z_]+) \((\d+)\)\s*$", line)
        if m:
            section = m.group(1); counts[section] = int(m.group(2)); continue
        r = ROW_RE.match(line)
        if r and section:
            rows[r.group(1)] = (section, line)
    tot = re.search(r"\| \*\*TOTAL\*\* \| \*\*(\d+)\*\* \|", text)
    return rows, counts, (int(tot.group(1)) if tot else None), text

# ---------------------------------------------------------------- render
def cluster_order(sigs):
    counts = defaultdict(int)
    for s in sigs.values():
        counts[s["cluster"]] += 1
    return sorted(counts, key=lambda k: (-counts[k], k)), counts

def themes_from_live(text: str) -> dict:
    out = {}
    for m in re.finditer(r"^\| \[([A-Z_]+)\]\(#[a-z_]+-\d+\) \| \d+ \| [^|]* \| ([^|]*) \|", text, re.M):
        out[m.group(1)] = m.group(2).strip()
    for m in re.finditer(r"^## ([A-Z_]+) \(\d+\)\n\*([^\n]*)\*", text, re.M):
        out.setdefault(m.group(1) + "__pre", m.group(2))
    return out

def render_row(s, marks) -> str:
    who = "WALTER → " + (", ".join(s["action"]) if s["action"] else "(info only)")
    if s["info"]:
        who += " · info: " + ", ".join(s["info"])
    title = s["title"]
    if len(title) > TITLE_CAP:
        title = title[:TITLE_CAP - 1].rstrip() + "…"
    mk = (" " + " ".join(marks.get(s["id"], []))) if marks.get(s["id"]) else ""
    return f"| {s['id']} | {s['date']} | {s['domain']} | {s['precedence']} | {who} | **{title}** {s['confidence']}{mk} | [{s['file']}]({s['file']}) |"

def render(sigs, live_text: str) -> str:
    marks = derive_markers(sigs)
    order, counts = cluster_order(sigs)
    themes = themes_from_live(live_text)
    total = sum(counts.values())
    latest = {}
    for s in sigs.values():
        c = s["cluster"]
        if c not in latest or (s["date"], s["id"]) > latest[c]:
            latest[c] = (s["date"], s["id"])
    rowsha = hashlib.sha256("\n".join(sorted(render_row(s, marks) for s in sigs.values())).encode()).hexdigest()
    out = []
    out.append("# BOARD — Network Signal Archive")
    out.append("")
    out.append(f"<!-- GENERATED by AGENTS/WALTER/tools/gen_board_index.py — do not hand-edit. rowset_sha256={rowsha} signals={total} -->")
    out.append("")
    out.append("Central, network-shared archive of every signal WALTER has dispatched. **This file is a GENERATED projection of the `SIG-W-*.md` frontmatter** (WQ-174, 2026-09-04): each row = id · date · domain · precedence · action/info · H1 title · confidence · derived lifecycle/correction markers · file. The signal file is the record; this index is for discovery. Delivery and consumption semantics: `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` §2. Cluster definitions: `AGENTS/WALTER/design/CLUSTER_TAXONOMY.md`.")
    out.append("")
    out.append("**Other agents:** scan the Cluster overview, then drill into your cluster section; pull-complete desks glob `BOARD/SIG-W-*.md` directly. **Markers are derived:** a `🚩 STATUS` marker comes from the signal's own `status:` header; a `⚠️ CORRECTED → SIG` marker is the inverse of the correcting signal's `corrects:` (+ `corrects_direction:`). Hand edits here are overwritten at the next generation.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Cluster overview")
    out.append("")
    out.append("Sorted by signal count descending.")
    out.append("")
    out.append("| Cluster | Count | Latest signal | Theme |")
    out.append("|---------|------:|---------------|-------|")
    for c in order:
        d, i = latest[c]
        out.append(f"| [{c}](#{c.lower()}-{counts[c]}) | {counts[c]} | {d} · {i} | {themes.get(c, '')} |")
    out.append(f"| **TOTAL** | **{total}** | | |")
    out.append("")
    out.append("---")
    for c in order:
        out.append("")
        out.append(f"## {c} ({counts[c]})")
        pre = themes.get(c + "__pre")
        if pre:
            out.append(f"*{pre}*")
        out.append("")
        out.append("| ID | Date | Domain | Precedence | Action → Info | Summary | File |")
        out.append("|----|------|--------|-----------|---------------|---------|------|")
        for s in sorted((s for s in sigs.values() if s["cluster"] == c), key=lambda s: (s["date"], s["id"])):
            out.append(render_row(s, marks))
    out.append("")
    return "\n".join(out), rowsha

# ---------------------------------------------------------------- check
def check(sigs, errors) -> int:
    rc = 0
    if errors:
        print("HARD ERRORS (fail closed):"); [print("  ", e) for e in errors]; rc = 1
    rows, counts, total, live_text = parse_live()
    live_ids = set(rows); gen_ids = set(sigs)
    if live_ids != gen_ids:
        rc = 1
        print(f"ID SET DIFFERS: live-only {sorted(live_ids - gen_ids)[:10]} generated-only {sorted(gen_ids - live_ids)[:10]}")
    else:
        print(f"ID set: {len(gen_ids)} identical")
    order, gcounts = cluster_order(sigs)
    for c, n in counts.items():
        if gcounts.get(c, 0) != n:
            rc = 1; print(f"COUNT DIFFERS {c}: live {n} generated {gcounts.get(c, 0)}")
    # section membership: a signal whose cluster: differs from the live section it sits in
    moved = [(sid, sec, sigs[sid]["cluster"]) for sid, (sec, _) in rows.items() if sid in sigs and sigs[sid]["cluster"] != sec]
    if moved:
        rc = 1; print(f"SECTION MISMATCH ({len(moved)}): " + "; ".join(f"{s}: live {a} vs cluster: {b}" for s, a, b in moved[:8]))
    if total != len(gen_ids):
        rc = 1; print(f"TOTAL DIFFERS: live {total} generated {len(gen_ids)}")
    marks = derive_markers(sigs)
    # Rows whose live summary CONTAINS a marker word as CONTENT (about another signal/figure), not as a
    # lifecycle state of the row itself. Audited by hand 2026-09-04 (design note §5); a new entry here
    # needs the same by-hand reading — this is an allowlist, not a suppression.
    CONTENT_FALSE_POSITIVES = {
        "SIG-W-20260627-017": "dispatch guidance ('route the decomposition'); 2nd-est figure superseded by an EARLIER signal, text in body",
        "SIG-W-20260725-002": "'ACTIVELY FALSIFIED' is about servicer DQ data, not this row",
        "SIG-W-20260727-001": "supersedes SIG-W-20260725-008's call; that status sits on the target",
        "SIG-W-20260727-014": "adopts BRENT's 92% and retires the ANCHOR's >70%; this row is the corrector",
        "SIG-W-20260730-008": "says 7/25 packets are superseded; this row is the corrector",
        "SIG-W-20260815-001": "'OTTO-30 resolved FALSIFIED' is OTTO's prediction, not this row",
        "SIG-W-20260815-006": "notes that -014 is tagged SUPERSEDED at both surfaces; about another row",
    }
    hand_only = [sid for sid, (sec, line) in rows.items()
                 if MARK_RE.search(line.split("| [")[0]) and not marks.get(sid) and sid not in CONTENT_FALSE_POSITIVES]
    unmarked = [sid for sid in sigs if marks.get(sid) and sid in rows and not MARK_RE.search(rows[sid][1].split("| [")[0])]
    print(f"markers: live rows with a marker {sum(1 for _, (s, l) in rows.items() if MARK_RE.search(l.split('| [')[0]))} · derivable {sum(1 for s in sigs if marks.get(s))} · HAND-ONLY (would be LOST) {len(hand_only)} · derivable-but-unmarked-live (would be GAINED) {len(unmarked)}")
    if hand_only:
        rc = 1; print("  hand-only:", hand_only)
    print("CHECK", "PASS" if rc == 0 else "FAIL")
    return rc

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true"); ap.add_argument("--write", nargs="?", const=os.path.join(BOARD, "INDEX.generated.md"))
    ap.add_argument("--cutover", action="store_true"); ap.add_argument("--sha", action="store_true")
    a = ap.parse_args()
    sigs, errors = load_signals()
    if a.sha:
        _, live_text = parse_live()[3], parse_live()[3]
        print(render(sigs, live_text)[1]); return 0
    if a.check or not (a.write or a.sha):
        return check(sigs, errors)
    if errors:
        print("refusing to write with hard errors; run --check"); return 1
    target = a.write
    if os.path.abspath(target) == os.path.abspath(LIVE) and not a.cutover:
        print("refusing to overwrite BOARD/INDEX.md without --cutover"); return 1
    text, sha = render(sigs, parse_live()[3])
    open(target, "w", encoding="utf-8").write(text)
    print(f"wrote {target} {len(text.encode())} B rowset_sha256={sha}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
