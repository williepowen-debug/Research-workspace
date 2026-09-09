"""Apply reviewed HEARTBEAT amendment projections without interpreting free prose.

Each amendment has one dashboard-amendment JSON block in the companion. Its source hash
binds it to the full amendment paragraph. Later amendments win; missing or stale
projections withhold the derived view. Authors must project every affected field:
hash equality proves synchronization, not semantic completeness.
"""
import copy
import hashlib
import json
import re

AMENDMENTS = re.compile(r"^> \*\*AMENDMENT #(\d+)\b[^\n]*(?:\n>[^\n]*)*", re.M)
PROJECTIONS = re.compile(r"^```dashboard-amendment\s*\n(.*?)\n```[ \t]*$", re.M | re.S)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate projection field: {key}")
        result[key] = value
    return result


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def prefix_matches(token, prefix):
    return token.startswith(prefix) and (len(token) == len(prefix)
                                         or token[len(prefix)].isspace())


def apply_amendments(text, base, projection_text=None):
    """Return a fresh view, or a visible error with all HEARTBEAT state withheld."""
    result = copy.deepcopy(base)
    result.update(amendments=[], errors=[])
    try:
        amendments = list(AMENDMENTS.finditer(text))
        projection_text = text if projection_text is None else projection_text
        blocks = PROJECTIONS.findall(projection_text)
        if len(blocks) != len(re.findall(r"^```dashboard-amendment\b", projection_text, re.M)):
            raise ValueError("unclosed dashboard amendment block")
        if len(amendments) != len(blocks):
            raise ValueError("each HEARTBEAT amendment needs one reviewed dashboard projection")
        if [int(m[1]) for m in amendments] != list(range(1, len(amendments) + 1)):
            raise ValueError("amendment numbers must be unique and ordered from 1")
        projections = {}
        for raw in blocks:
            item = json.loads(raw, object_pairs_hook=unique_object)
            if not isinstance(item, dict) or set(item) != {"amendment", "source_sha256", "set"}:
                raise ValueError("invalid dashboard amendment schema")
            number = item["amendment"]
            if type(number) is not int or number in projections:
                raise ValueError("invalid or duplicate amendment number")
            projections[number] = item
        for amendment in amendments:
            number = int(amendment[1])
            item = projections.get(number)
            if item is None:
                raise ValueError(f"missing projection for amendment #{number}")
            digest = hashlib.sha256(amendment[0].encode("utf-8")).hexdigest()
            if item["source_sha256"] != digest:
                raise ValueError(f"amendment #{number} changed; dashboard projection needs review")
            updates = item["set"]
            if not isinstance(updates, dict) or set(updates) - {"one", "split", "channels", "ticker", "blocking"}:
                raise ValueError(f"unsupported field in amendment #{number}")
            for key in ("one", "split"):
                if key in updates:
                    if not nonempty(updates[key]):
                        raise ValueError(f"{key} must be nonempty text")
                    result[key] = updates[key]
            channels = updates.get("channels", {})
            if not isinstance(channels, dict):
                raise ValueError("channels must be keyed by existing channel name")
            for name, replacement in channels.items():
                matches = [c for c in result["channels"] if c["name"] == name]
                if len(matches) != 1 or not isinstance(replacement, dict):
                    raise ValueError(f"unknown or ambiguous channel: {name}")
                if set(replacement) - {"headline", "body", "cls"} or not replacement:
                    raise ValueError(f"unsupported channel fields: {name}")
                if any(not nonempty(v) for v in replacement.values()):
                    raise ValueError(f"empty channel field: {name}")
                if "cls" in replacement and replacement["cls"] not in {"ok", "watch", "elev", "crit", "none"}:
                    raise ValueError(f"unknown channel status: {name}")
                matches[0].update(replacement)
            ticker = updates.get("ticker", {})
            if not isinstance(ticker, dict):
                raise ValueError("ticker must be keyed by existing token prefix")
            for prefix, replacement in ticker.items():
                if not nonempty(prefix) or not nonempty(replacement) or not prefix_matches(replacement, prefix):
                    raise ValueError("ticker replacement must retain its instrument prefix")
                matches = [i for i, t in enumerate(result["ticker"]) if prefix_matches(t, prefix)]
                if len(matches) != 1:
                    raise ValueError(f"unknown or ambiguous ticker: {prefix}")
                result["ticker"][matches[0]] = replacement
            if "blocking" in updates:
                rows = updates["blocking"]
                if not isinstance(rows, list) or any(
                    not isinstance(r, dict) or set(r) != {"cls", "text", "ref"}
                    or r["cls"] not in {"ok", "watch", "elev", "crit", "none"}
                    or not nonempty(r["text"]) or not nonempty(r["ref"]) for r in rows
                ):
                    raise ValueError("invalid blocking rows")
                result["blocking"] = rows
            result["amendments"].append(amendment[0].split("**", 2)[1])
        return result
    except (ValueError, TypeError, KeyError) as exc:
        return {"one": "", "split": "", "channels": [], "ticker": [], "blocking": [],
                "base": base["base"], "amendments": [], "errors": [str(exc)]}
