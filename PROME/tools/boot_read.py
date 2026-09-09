#!/usr/bin/env python3
"""Bounded, digest-checked UTF-8 reads. One page per tool call; continue to EOF."""
import argparse
import hashlib
import json
from pathlib import Path

PAGE_CHARS = 6000
PAGE_TEXT_BYTES = 6000  # Serialized text only; leave room for the JSON envelope.


def page(path, offset=0, expected_sha=None):
    raw = Path(path).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if offset < 0 or (offset and not expected_sha):
        raise ValueError("Continuation requires a nonnegative offset and --sha256")
    if expected_sha is not None and sha != expected_sha:
        raise ValueError("Source changed; restart this document at offset 0")
    content = raw.decode("utf-8")
    if offset > len(content):
        raise ValueError("Offset beyond EOF")
    end, used = offset, 0
    for char in content[offset:offset + PAGE_CHARS]:
        cost = len(json.dumps(char, ensure_ascii=False)[1:-1].encode("utf-8"))
        if used + cost > PAGE_TEXT_BYTES:
            break
        used += cost
        end += 1
    return {"path": str(Path(path).resolve()), "sha256": sha, "offset": offset,
            "text": content[offset:end], "next_offset": end if end < len(content) else None,
            "eof": end == len(content)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--sha256")
    args = ap.parse_args()
    try:
        print(json.dumps(page(args.path, args.offset, args.sha256), ensure_ascii=False))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "eof": False}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
