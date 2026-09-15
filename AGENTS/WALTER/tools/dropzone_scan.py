#!/usr/bin/env python3
"""Read-only enumeration of the exact content-file class used by doctor."""
from pathlib import Path

SCAFFOLDS = {"README.md", ".gitignore", ".gitkeep"}


def pending_files(directory):
    return sorted(p for p in directory.iterdir()
                  if p.is_file() and p.name not in SCAFFOLDS and not p.name.startswith(".")
                  and not p.name.endswith(":Zone.Identifier")) if directory.exists() else []


if __name__ == "__main__":
    files = pending_files(Path(__file__).resolve().parents[1] / "inbox/WILL")
    print(f"{len(files)} content file(s) pending")
    for path in files:
        print(path.name)
