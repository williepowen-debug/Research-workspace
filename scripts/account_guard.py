#!/usr/bin/env python3
"""Refuse a commit whose STAGED additions carry a brokerage account number (WQ-455, Will 2026-10-18).

The repo is public. Two tests on added lines only:
  1. any 6-12 digit run whose sha256 is on the KNOWN list (the real numbers are never written here);
  2. 'account no./number/#' or 'acct' followed by 6+ digits (write the last four only, e.g. •1326).
rc 0 clean · 1 refused · 2 could not run. Reads the index git builds for this commit (GIT_INDEX_FILE-aware)."""
import hashlib, re, subprocess, sys

KNOWN = {"5db70a6e830c3e54a86d08a3d10328b290f99f846a4f54bebc40494451fba245"}  # Fidelity Traditional IRA (•1326)
LABELLED = re.compile(r"(?i)\b(?:account\s*(?:no\.?|number|num|#)|acct\.?\s*(?:no\.?|#)?)\s*[:#]?\s*\**\s*(\d{6,})")
# Separators allowed (2026-10-20, PROME): "123-45-6789" / "123 45 6789" / "123.45.6789" passed the
# old contiguous-only pattern. A match is hashed with its separators stripped, so only the KNOWN numbers refuse.
RUN = re.compile(r"(?<![\d])\d(?:[ .\-]?\d){5,11}(?![\d])")

def main():
    try:
        diff = subprocess.run(["git", "diff", "--cached", "-U0", "--no-color", "--text"],
                              capture_output=True, text=True, errors="replace", check=True).stdout
    except Exception as e:
        print(f"account_guard: could not read staged diff ({e})", file=sys.stderr); return 2
    hits, path = [], "?"
    for line in diff.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else line[4:]
        elif line.startswith("+") and not line.startswith("+++"):
            body = line[1:]
            if any(hashlib.sha256(re.sub(r"[ .\-]", "", m.group()).encode()).hexdigest() in KNOWN for m in RUN.finditer(body)):
                hits.append(f"{path}: a known account number (full digits)")
            elif LABELLED.search(body):
                hits.append(f"{path}: 'account no.' followed by 6+ digits")
    if hits:
        print("account_guard: commit refused — the repo is PUBLIC; write account ids as the last four only (e.g. •1326):", file=sys.stderr)
        for h in sorted(set(hits)): print("  " + h, file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
