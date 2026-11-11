"""Explicit supplemental choices; the existing queue remains authoritative."""
import hashlib
import json
import re

from pilot_files import fields, record_block
from authorization import validate_policy


def terms_hash(row):
    """Versioned opt-in: Notes are operational; their WAIT state still binds."""
    value = {"cells": row["cells"][:6], "blocked": row["blocked"]}
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def pointer_for(row):
    marker = re.findall(r"<!-- decisions-options: (PROME/proposals/[A-Za-z0-9_.-]+\.md) -->", row["row"])
    if not marker and "decisions-options" not in row["row"]:
        return None
    if len(marker) != 1 or row["row"].count("decisions-options") != 1:
        raise ValueError("Expected one explicit decisions-options source pointer")
    return marker[0]


def source_for(repo, row, commit, current=False):
    path = pointer_for(row)
    if path is None:
        return None
    if row["kind"] != "DECISION":
        raise ValueError("Options require one DECISION row; mixed/task rows need owner reconciliation")
    text = repo.read(path, commit, prefix="PROME/proposals")
    if current and repo.read(path, clean=True, prefix="PROME/proposals") != text:
        raise ValueError("Option source is not published; refresh after PROME finishes")
    record = record_block(text, "decisions-options")
    version = record.get("schema_version") if isinstance(record, dict) else None
    stable = version == "decisions-options/3"
    binding = "queue_terms_sha256" if stable else "queue_row_sha256"
    expected = {"schema_version", "wq_id", binding, "choices"}
    if stable:
        expected |= {"context", "conditions"}
    if version in {"decisions-options/2", "decisions-options/3"}:
        expected |= {"recommended_choice_id", "confirmation"}
    fields(record, expected, "Options")
    if (version not in {"decisions-options/1", "decisions-options/2", "decisions-options/3"} or type(record["wq_id"]) not in (str, int)
            or str(record["wq_id"]) != row["n"]
            or record[binding] != (terms_hash(row) if stable else hashlib.sha256(row["row"].encode()).hexdigest())):
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
    if version in {"decisions-options/2", "decisions-options/3"}:
        recommended = record["recommended_choice_id"]
        if recommended is not None and (not isinstance(recommended, str) or recommended not in ids):
            raise ValueError("Recommendation must identify an explicit choice or be null")
        result.update(recommended_choice_id=recommended, confirmation=validate_policy(record["confirmation"]))
    if stable:
        context, conditions = record["context"], record["conditions"]
        if (not isinstance(context, str) or not context.strip() or len(context) > 20000
                or not isinstance(conditions, list) or len(conditions) > 30
                or any(not isinstance(c, str) or not c.strip() or len(c) > 10000 for c in conditions)):
            raise ValueError("Stable cards require explicit bounded context and conditions")
        result.update(binding="question-options/1", context=context, conditions=conditions)
    return result
