"""Recent published owner records, verbatim; no inferred ruling or answer time."""
import re
import subprocess


def recent(repo, limit=20):
    commit = repo.git("rev-parse", "origin/master").strip()
    paths = repo.git("ls-tree", "-r", "--name-only", commit, "--", "PROME/proposals").splitlines()
    paths = sorted((p for p in paths if re.fullmatch(
        r"PROME/proposals/\d{4}-\d{2}-\d{2}_[^/]+-RULED\.md", p)), reverse=True)[:limit]
    records, errors = [], []
    for path in paths:
        try:
            text = repo.read(path, commit, prefix="PROME/proposals")
            # Show the published version even during a local edit, but identify it.
            current = repo.path(path).exists() and repo.path(path).read_text() == text
            paragraphs = text.strip().split("\n\n")
            records.append({"path": path, "commit": commit, "text": text,
                            "title": paragraphs[0].lstrip("# "),
                            "opening": paragraphs[1] if len(paragraphs) > 1 else "",
                            "current": current})
        except (ValueError, OSError, subprocess.CalledProcessError) as error:
            errors.append(path + ": " + str(error))
    return {"records": records, "errors": errors, "limit": limit,
            "scope": "Recent published ruling records, including corrections (up to 20). This is not a complete ledger of every chat decision."}
