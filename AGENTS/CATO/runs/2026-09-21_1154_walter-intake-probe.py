"""Read-only, pinned evidence for CATO's September 21 WALTER intake review.

Run from any directory. Output is JSON; redirect only into CATO's own files.
This checks transport and records, not source truth or original image coverage.
"""
import csv
import hashlib
import io
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REV = "6dd151ab4676b43d28a38e2976909d0a8644bbb4"
REMOTE = "03e53cf410e580824c4fdac6e2256a981eed2b14"


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True)


def read(path, rev=REV):
    return git("show", f"{rev}:{path}")


def table(path):
    return list(csv.DictReader(io.StringIO(read(path)), delimiter="\t"))


paths = git("ls-tree", "-r", "--name-only", REV).splitlines()
signals = [p for p in paths if re.match(r"BOARD/SIG-W-20260921-\d{3}-", p)]
deliveries = [r for r in table("AGENTS/WALTER/routed/delivery_log.tsv")
              if r["signal_id"].startswith("SIG-W-20260921-")]
batches = [r for r in table("AGENTS/WALTER/registry/BATCH_MANIFEST.tsv")
           if r["batch_id"].startswith("BM-20260921-")]
out = {"revision": REV, "observed_origin_revision_not_fresh_fetch": REMOTE,
       "batch_counts": [{k: r[k] for k in ("batch_id", "declared", "dispositioned", "state")}
                        for r in batches],
       "delivery_rows": len(deliveries),
       "unique_recipients": len({r["recipient"] for r in deliveries}),
       "delivery_states": dict(Counter(r["written_state"] for r in deliveries)),
       "signals": [], "transport": [], "recipient_ledger_rows": []}
for p in signals:
    t = read(p)
    header = t.split("---", 2)[1]
    sid = re.search(r"^signal_id: (.+)$", header, re.M)[1]
    action = json.loads(re.search(r"^action: (.+)$", header, re.M)[1])
    info = json.loads(re.search(r"^info: (.+)$", header, re.M)[1])
    expected = (set(action) | (set(info) - {"CARL", "RED", "PROME", "TERRY"})) - {"TERRY"}
    actual = {r["recipient"] for r in deliveries if r["signal_id"] == sid}
    out["signals"].append({"id": sid, "path": p,
        "sha256": hashlib.sha256(t.encode()).hexdigest(),
        "action": action, "info": info,
        "missing_required_recipient_rows": sorted(expected - actual),
        "extra_recipient_rows": sorted(actual - expected),
        "whitespace_words_including_frontmatter": len(t.split()),
        "http_links": len(re.findall(r"https?://", t)),
        "annotation_headings": [l for l in t.splitlines() if l.startswith("##") and "ANNOTATION" in l],
        "lifecycle_fields": [l for l in header.splitlines()
                             if re.match(r"^(status|status_ref|erratum|corrects):", l)]})
for r in deliveries:
    p = r["handoff_path"]
    hist = git("log", REMOTE, "-1", "--format=%H", "--", p).strip()
    processed = str(Path(p).parent / "processed" / Path(p).name)
    out["transport"].append({"id": r["signal_id"], "recipient": r["recipient"],
        "original_path_present_at_snapshot": p in paths,
        "processed_path_present_at_snapshot": processed in paths,
        "origin_history_commit": hist or None})
for p in paths:
    if p.startswith("AGENTS/") and (p.endswith("/board_log.tsv") or p.endswith("/BOARD_LOG.tsv")):
        for n, line in enumerate(read(p).splitlines(), 1):
            if "SIG-W-20260921-" in line:
                out["recipient_ledger_rows"].append({"path": p, "line": n, "text": line})
out["totals"] = {
    "signal_count": len(signals),
    "declared_items": sum(int(r["declared"]) for r in batches),
    "whitespace_words_including_frontmatter": sum(r["whitespace_words_including_frontmatter"] for r in out["signals"]),
    "missing_origin_history_proofs": sum(not r["origin_history_commit"] for r in out["transport"]),
    "processed_handoffs_at_snapshot": sum(r["processed_path_present_at_snapshot"] for r in out["transport"]),
}
print(json.dumps(out, ensure_ascii=False, indent=2))
