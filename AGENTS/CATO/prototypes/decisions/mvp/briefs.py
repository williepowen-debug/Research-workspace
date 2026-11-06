"""Present owner-authored explanations from the already-bound options source.

The complete source is already retained in /2 answer snapshots. A brief is
display text, never a replacement for the queue, choices or response contract.
"""
from datetime import date, datetime
import hashlib
from pathlib import PurePosixPath
from zoneinfo import ZoneInfo

from pilot_files import fields, record_block


def today():
    return datetime.now(ZoneInfo("America/New_York")).date()


def text(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 10000:
        raise ValueError("Brief fields must be nonempty bounded text")


def presentation(snapshot, *, historical=False, on_date=None):
    """A broken/expired explanation falls back locally, not across the desk."""
    source = snapshot.get("options_source") or {}
    if "decisions-brief" not in source.get("text", ""):
        return {"brief": None, "brief_notice": ""}
    try:
        record = record_block(source["text"], "decisions-brief")
        fields(record, {"schema_version", "wq_id", "queue_row_sha256", "prepared_at",
                        "stale_after", "question", "what_changes", "recommendation",
                        "conditions", "supporting"}, "Brief")
        if (record["schema_version"] != "decisions-brief/1"
                or type(record["wq_id"]) not in (str, int)
                or str(record["wq_id"]) != snapshot["record"]["wq_id"]
                or record["queue_row_sha256"] != hashlib.sha256(snapshot["queue_row"].encode()).hexdigest()):
            raise ValueError("Brief does not match these queue terms")
        for key in ("prepared_at", "question", "what_changes", "stale_after"):
            text(record[key])
        expiry = date.fromisoformat(record["stale_after"])
        rec = record["recommendation"]
        fields(rec, {"status", "text"}, "Brief recommendation")
        if rec["status"] not in ("RECOMMENDED", "NONE_YET"):
            raise ValueError("Unknown recommendation status")
        text(rec["text"])
        if not isinstance(record["conditions"], list) or len(record["conditions"]) > 30:
            raise ValueError("Expected a bounded list of conditions")
        for condition in record["conditions"]:
            text(condition)
        if not isinstance(record["supporting"], list) or len(record["supporting"]) > 30:
            raise ValueError("Expected a bounded list of supporting records")
        for item in record["supporting"]:
            fields(item, {"label", "path"}, "Supporting record")
            text(item["label"])
            text(item["path"])
            path = PurePosixPath(item["path"])
            if path.is_absolute() or ".." in path.parts or path.parts[0] not in ("PROME", "AGENTS", "FORGE"):
                raise ValueError("Supporting record must name a repository document")
        if not historical and (on_date or today()) > expiry:
            return {"brief": None, "brief_notice": "The short explanation is out of date. Read the full queue wording below before responding."}
        return {"brief": record, "brief_notice": ""}
    except (ValueError, KeyError, TypeError, AttributeError) as error:
        return {"brief": None, "brief_notice": "The short explanation is unavailable. Full queue wording is shown below.",
                "brief_error": str(error)}
