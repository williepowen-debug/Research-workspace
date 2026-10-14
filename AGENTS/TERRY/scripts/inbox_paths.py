"""List desk packet files identically at boot and closeout; no writes or triage."""
from pathlib import Path


def packet_paths(root: Path) -> list[Path]:
    """All file formats, excluding metadata, processed subtrees and WILL intake."""
    if not root.is_dir():
        return []
    return [
        path for path in sorted(root.rglob("*"))
        if path.is_file()
        and path.name.lower() not in {"readme.md", ".gitkeep"}
        and "processed" not in path.relative_to(root).parts
        and path.relative_to(root).parts[0] != "WILL"
    ]
