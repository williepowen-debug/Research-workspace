#!/usr/bin/env python3
"""Generate a deduplicated reading guide without altering frozen evidence.

One catalogue entry per routed signal, DDTL correction family, or unique content.
Different recipient variants remain provenance aliases, not independent sources.
Run --write after deliberately changing catalogue generation; --check is read-only.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parents[1] / "CRWV"
TOPICS = ("Financing and credit", "Contracts and models", "Power and delivery",
          "Ownership and insider transactions", "Index and market context",
          "Trade preparation", "Broader research context")
HISTORICAL_ROLES = {"historical assignment", "historical trade preparation", "intermediate option screen"}


def classify(record):
    path = record["source"].lower()
    title = record["title"].lower()
    text = path + " " + title
    if "terry/" in path or path.endswith("/trade.md"):
        return "Trade preparation"
    if any(word in text for word in ("insider", "founder-sales", "founders")):
        return "Ownership and insider transactions"
    if any(word in text for word in ("hsbc", "model-arithmetic", "contract-economics", "20261020-007")):
        return "Contracts and models"
    if any(word in text for word in ("hedge-inference", "power-cost-is", "hedge-wording", "pjm")):
        return "Power and delivery"
    if any(word in text for word in ("qqq", "nomura", "20261010-006")):
        return "Index and market context"
    if any(word in text for word in ("credit", "cds", "ddtl", "bond", "guarantee", "20261015-005", "20261015-017", "20261015-023")):
        return "Financing and credit"
    return "Broader research context"


def role(record):
    source = record["source"].lower()
    if "/research/2026-10-20_trade-idea-slate-data/chain-" in source:
        return "dated option screen" if "final-legs" in source else "intermediate option screen"
    if record["kind"] == "data":
        return "dated supporting data"
    if any(word in source for word in ("deep-research-prompt", "cds-leg-ask", "thesis-ask")):
        return "historical assignment"
    if "/terry/" in source or source.endswith("/trade.md"):
        return "historical trade preparation"
    if "/board/" in "/" + source or "/inbox/" in source:
        return "routed evidence"
    return "research"


def build(base=BASE):
    manifest = json.loads((base / "MANIFEST.json").read_text())
    groups = defaultdict(list)
    hashes = set()
    for record in manifest["copied_sources"]:
        digest = hashlib.sha256((base / record["copy"]).read_bytes()).hexdigest()
        if digest != record["copy_sha256"]:
            raise ValueError(f"Frozen copy changed: {record['copy']}")
        hashes.add(digest)
        signal = re.search(r"SIG-W-\d{8}-\d{3}", Path(record["source"]).name)
        source = record["source"]
        # Explicit provenance families, not fuzzy semantic merging. Each differs
        # in recipient emphasis; the original research and all aliases survive.
        if "2026-07-09_coreweave" in source or (signal and signal.group() == "SIG-W-20260709-001"):
            key = "DEWEY-COREWEAVE-RESEARCH-20260709"
        elif "LIQUID/research/2026-10-19_sweep/REPORT.md" in source or (signal and signal.group() == "SIG-W-20261019-011"):
            key = "LIQUID-CREDIT-SWEEP-20261019"
        elif "batch3/verify-insiders.md" in source or (signal and signal.group() == "SIG-W-20261020-009"):
            key = "WALTER-INSIDER-VERIFICATION-20261020"
        elif signal:
            key = signal.group()
        elif "DR1-CORRECTION-ddtl4-mechanism" in record["source"]:
            key = "DEWEY-DDTL4-CORRECTION-20260802"
        else:
            key = "sha256:" + digest
        groups[key].append(record)
    entries = []
    for key, variants in groups.items():
        # BOARD generally carries the full common signal; VULCAN's correction
        # carries the recipient-specific company integration. Keep all variants.
        def priority(r):
            research = ("/DEWEY/output/" in r["source"] or
                        "/LIQUID/research/" in r["source"] or
                        "batch3/verify-insiders.md" in r["source"])
            return (-1 if research else 0 if r["source"].startswith("BOARD/") else
                    1 if "/VULCAN/" in r["source"] else 2, r["source"])
        preferred = min(variants, key=priority)
        entries.append({"key": key, "topic": classify(preferred), "role": role(preferred),
                        "title": preferred["title"], "preferred_copy": preferred["copy"],
                        "preferred_original": preferred["source"],
                        "distinct_contents": len({r["copy_sha256"] for r in variants}),
                        "aliases": [{k: r[k] for k in ("source", "copy", "owner", "copy_sha256")}
                                    for r in sorted(variants, key=lambda r: r["source"])]})
    entries.sort(key=lambda r: (TOPICS.index(r["topic"]), r["preferred_original"]))
    catalog = {"basis": "Frozen capture in MANIFEST.json; this catalogue does not refresh evidence",
               "source_copies": len(manifest["copied_sources"]), "unique_contents": len(hashes),
               "reading_entries": len(entries), "entries": entries}
    lines = ["# CoreWeave reading guide", "",
             "Generated from the frozen source manifest. Start with [current company evidence](KB.tsv) "
             "and [correction history](CORRECTIONS.md). Dates inside sources govern; this guide is not a market refresh.", "",
             f"{catalog['source_copies']} copies / {catalog['unique_contents']} unique contents / "
             f"{len(entries)} reading entries. Recipient variants remain in the [catalogue](CATALOG.json); "
             "multiple routes are not independent corroboration. [Full historical source map](SOURCE_MAP.md).", ""]
    def table_row(entry):
        title = entry["title"].replace("|", "\\|").replace("\n", " ")
        title = title[:130] + ("…" if len(title) > 130 else "")
        original = Path("../../..") / entry["preferred_original"]
        return (f"| [{title}](<{entry['preferred_copy']}>) | {entry['role']} | "
                f"[Original](<{original.as_posix()}>) · {len(entry['aliases'])} source path(s), "
                f"{entry['distinct_contents']} content variant(s) |")

    for topic in TOPICS:
        lines += ["## " + topic, "", "| Preferred source | Role | Provenance |", "|---|---|---|"]
        for entry in entries:
            if entry["topic"] != topic or entry["role"] in HISTORICAL_ROLES:
                continue
            lines.append(table_row(entry))
        lines.append("")
    lines += ["## Historical and intermediate material", "",
              "Older assignments, captured trade records and intermediate screens are retained for provenance.", "",
              "| Source | Role | Provenance |", "|---|---|---|"]
    lines += [table_row(entry) for entry in entries if entry["role"] in HISTORICAL_ROLES]
    lines.append("")
    lines += ["Trade preparation and intermediate screens are historical records. Use the "
              "[canonical VULCAN thesis](../TRADE.md) and original specialist records before any decision. "
              "No stale quote or historical assignment becomes current through inclusion here.", ""]
    return {"CATALOG.json": (json.dumps(catalog, indent=2, ensure_ascii=False) + "\n").encode(),
            "READING_GUIDE.md": "\n".join(lines).encode()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        for name, data in build().items():
            path = BASE / name
            if args.write:
                path.write_bytes(data)
            elif not path.exists() or path.read_bytes() != data:
                raise ValueError(f"{name} differs from its registered inputs; run crwv_library.py --write")
        print("CRWV catalogue/guide: PASS; frozen evidence hashes verified")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"CRWV library: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
