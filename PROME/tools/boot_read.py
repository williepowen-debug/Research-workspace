#!/usr/bin/env python3
"""Bounded, digest-checked UTF-8 reads. One page per tool call; continue to EOF."""
import argparse
import hashlib
import json
import re
from pathlib import Path

PAGE_CHARS = 6000
PAGE_TEXT_BYTES = 6000  # Serialized text only; leave room for the JSON envelope.
ORCH_VIEW = "orch-compact-v1"
ORCH_HEADER = re.compile(
    r"ORCH_LOG closeout evidence — \d{4}-\d{2}-\d{2} \+ unresolved prior touches; "
    r"attributed records, not native receipt authentication\n")
GAP_REASON = "missing or duplicate structured closeout evidence"
GAP_ROW = re.compile(
    r"UNKNOWN: (\d{4}-\d{2}-\d{2} \S+ touch [1-9][0-9]*"
    r"(?:[A-Za-z][A-Za-z0-9_-]*|-[A-Za-z0-9_-]+)? \[[0-9a-f]{64}\]): "
    + GAP_REASON + r"\n")


def compact_orch(content):
    """Factor only identical gap wording. All identities and other text survive.

    No age, disposition, severity or rc inference. Unknown formats stay verbatim.
    Consecutive runs preserve record order; full logs remain the drill-down source.
    """
    if not ORCH_HEADER.match(content):
        return content, 0
    lines = content.splitlines(keepends=True)
    output, groups, index = [], 0, 0
    while index < len(lines):
        end = index
        identities = []
        while end < len(lines):
            match = GAP_ROW.fullmatch(lines[end])
            if not match:
                break
            identities.append(match.group(1))
            end += 1
        if len(identities) >= 2:
            output.append(f"UNKNOWN (each entry): {GAP_REASON}\n")
            output.extend(f"  {identity}\n" for identity in identities)
            groups += 1
            index = end
        else:
            output.append(lines[index])
            index += 1
    return "".join(output), groups


def page(path, offset=0, expected_sha=None, view="full"):
    if view not in ("full", ORCH_VIEW):
        raise ValueError("Unknown view; read the full log")
    raw = Path(path).read_bytes()
    source_sha = hashlib.sha256(raw).hexdigest()
    # Bind offsets to BOTH the source and representation. A compact offset must
    # never silently resume in the original text (or vice versa).
    sha = source_sha if view == "full" else hashlib.sha256(view.encode() + b"\0" + raw).hexdigest()
    if offset < 0 or (offset and not expected_sha):
        raise ValueError("Continuation requires a nonnegative offset and --sha256")
    if expected_sha is not None and sha != expected_sha:
        raise ValueError("Source or view changed; restart this document at offset 0")
    content = raw.decode("utf-8")
    groups = 0
    if view == ORCH_VIEW:
        content, groups = compact_orch(content)
    if offset > len(content):
        raise ValueError("Offset beyond EOF")
    end, used = offset, 0
    for char in content[offset:offset + PAGE_CHARS]:
        cost = len(json.dumps(char, ensure_ascii=False)[1:-1].encode("utf-8"))
        if used + cost > PAGE_TEXT_BYTES:
            break
        used += cost
        end += 1
    result = {"path": str(Path(path).resolve()), "sha256": sha, "offset": offset,
            "text": content[offset:end], "next_offset": end if end < len(content) else None,
            "eof": end == len(content)}
    if view == ORCH_VIEW:
        result.update(view=view, source_sha256=source_sha, compacted_groups=groups,
                      representation="grouped" if groups else "full-fallback")
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--sha256")
    ap.add_argument("--view", choices=("full", ORCH_VIEW), default="full",
                    help="Only orch-compact-v1 factors repeated UNKNOWN evidence-gap wording; other text stays full")
    args = ap.parse_args()
    try:
        print(json.dumps(page(args.path, args.offset, args.sha256, args.view), ensure_ascii=False))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "eof": False}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
