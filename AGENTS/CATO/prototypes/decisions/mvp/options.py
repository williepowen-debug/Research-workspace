"""Explicit supplemental choices; the existing queue remains authoritative."""
import hashlib
import re

from pilot_files import fields, record_block
from authorization import validate_policy


def source_for(repo, row, commit, current=False):
    marker = re.findall(r"<!-- decisions-options: (PROME/proposals/[A-Za-z0-9_.-]+\.md) -->", row["row"])
    if not marker and "decisions-options" not in row["row"]:
        return None
    if len(marker) != 1 or row["row"].count("decisions-options") != 1:
        raise ValueError("Expected one explicit decisions-options source pointer")
    if row["kind"] != "DECISION":
        raise ValueError("Options require one DECISION row; mixed/task rows need owner reconciliation")
    path = marker[0]
    text = repo.read(path, commit, prefix="PROME/proposals")
    if current and repo.read(path, clean=True, prefix="PROME/proposals") != text:
        raise ValueError("Option source is not published; refresh after PROME finishes")
    record = record_block(text, "decisions-options")
    version = record.get("schema_version") if isinstance(record, dict) else None
    expected = {"schema_version", "wq_id", "queue_row_sha256", "choices"}
    if version == "decisions-options/2":
        expected |= {"recommended_choice_id", "confirmation"}
    fields(record, expected, "Options")
    if (version not in {"decisions-options/1", "decisions-options/2"} or type(record["wq_id"]) not in (str, int)
            or str(record["wq_id"]) != row["n"]
            or record["queue_row_sha256"] != hashlib.sha256(row["row"].encode()).hexdigest()):
        raise ValueError("Options do not bind this exact queue row")
    choices = record["choices"]
    if not isinstance(choices, list) or not 2 <= len(choices) <= 20:
        raise ValueError("Expected 2 to 20 explicit options")
    ids = set()
    for choice in choices:
        fields(choice, {"id", "label", "meaning", "consequence"}, "Option")
        if any(not isinstance(v, str) or not v.strip() or len(v) > 10000 for v in choice.values()):
            raise ValueError("Option fields must be nonempty bounded text")
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,32}", choice["id"]) or choice["id"] in ids:
            raise ValueError("Option IDs must be unique and unambiguous")
        ids.add(choice["id"])
    result = {"path": path, "commit": commit, "text": text, "choices": choices}
    if version == "decisions-options/2":
        recommended = record["recommended_choice_id"]
        if recommended is not None and (not isinstance(recommended, str) or recommended not in ids):
            raise ValueError("Recommendation must identify an explicit choice or be null")
        result.update(recommended_choice_id=recommended, confirmation=validate_policy(record["confirmation"]))
    return result
