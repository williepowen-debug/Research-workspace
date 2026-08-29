#!/usr/bin/env python3
"""
SENTRY Feed Fetcher — v1.0
Pulls RSS/Atom feeds, deduplicates, writes to SIGNALS/inbound.md
Run by GitHub Actions twice daily (6 AM / 6 PM ET)
"""

import html as _html
import yaml
import feedparser
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Paths
ROOT = Path(__file__).parent.parent
FEEDS_YML = ROOT / "SIGNALS" / "feeds.yml"
INBOUND_MD = ROOT / "SIGNALS" / "inbound.md"
SEEN_JSON = ROOT / "SIGNALS" / "seen.json"
ARCHIVE_DIR = ROOT / "SIGNALS" / "archive"

# Config
MAX_AGE_HOURS = 48  # Only fetch items from last 48 hours
MAX_ITEMS_PER_FEED = 20


def load_seen():
    """Load deduplication state."""
    if SEEN_JSON.exists():
        with open(SEEN_JSON) as f:
            return json.load(f)
    return {}


def save_seen(seen):
    """Save deduplication state."""
    with open(SEEN_JSON, "w") as f:
        json.dump(seen, f, indent=2)


def item_guid(item):
    """Generate unique ID for feed item."""
    # Prefer id/guid, fallback to link+title hash
    uid = item.get("id", item.get("guid", ""))
    if uid:
        return hashlib.md5(uid.encode()).hexdigest()[:16]
    
    content = f"{item.get('link', '')}:{item.get('title', '')}"
    return hashlib.md5(content.encode()).hexdigest()[:16]


CIK_RE = re.compile(r"/data/(\d+)/")
_HTML_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")


def extract_cik(link):
    """Pull CIK from SEC EDGAR archive link (pattern: /data/<CIK>/...)."""
    if not link:
        return None
    m = CIK_RE.search(link)
    return str(int(m.group(1))) if m else None


def strip_html(text):
    """Strip HTML tags, unescape entities, collapse whitespace.

    SEC EDGAR summaries embed `<b>Filed:</b> ...` boilerplate which is
    just visual noise in the markdown surface; we want plain text.
    Safe on already-plain strings (no tags = no-op).
    """
    if not text:
        return ""
    no_tags = _HTML_TAG_RE.sub("", text)
    unescaped = _html.unescape(no_tags)
    return _WS_RE.sub(" ", unescaped).strip()


def fetch_feed(feed_config):
    """Fetch a single feed and return new items."""
    url = feed_config["url"]
    name = feed_config["name"]
    tags = feed_config.get("tags", [])
    headers = feed_config.get("headers", {}) or {}
    include_types = feed_config.get("include_types", []) or []
    # Normalize CIK keys to canonical-int-string form so config-side
    # leading zeros (e.g. "0000038264") still match link-extracted CIKs.
    cik_watchlist = {
        str(int(k)): v
        for k, v in (feed_config.get("cik_watchlist") or {}).items()
    }

    # Build a prefix-anchored regex from include_types (e.g., "8-K" matches
    # "8-K - Foo Inc." but "SCHEDULE 13D" does NOT match "SCHEDULE 13D/A"
    # unless explicitly listed).
    type_re = None
    if include_types:
        escaped = [re.escape(t) for t in include_types]
        type_re = re.compile(r"^(" + "|".join(escaped) + r")\s+-\s+")

    print(f"Fetching: {name}...", file=sys.stderr)

    try:
        parsed = feedparser.parse(url, request_headers=headers) if headers else feedparser.parse(url)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return []

    # Surface fetch failures instead of silently returning empty
    status = getattr(parsed, "status", None)
    if status and status >= 400:
        print(f"  WARN: HTTP {status} from {url}", file=sys.stderr)
        return []
    if parsed.bozo and not parsed.entries:
        print(f"  WARN: parse error, no entries — {parsed.bozo_exception}", file=sys.stderr)
        return []

    items = []
    skipped_by_filter = 0
    matched_fleet = 0
    cutoff = datetime.now(timezone.utc).timestamp() - (MAX_AGE_HOURS * 3600)

    for entry in parsed.entries[:MAX_ITEMS_PER_FEED]:
        title = entry.get("title", "No title")

        # Filing-type whitelist (e.g., SEC EDGAR — drop noise like 424B2, 144)
        if type_re and not type_re.match(title):
            skipped_by_filter += 1
            continue

        # Parse date
        pub_date = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
            pub_date = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)

        if pub_date and pub_date.timestamp() < cutoff:
            continue

        guid = item_guid(entry)
        link = entry.get("link", "")

        # Enrich SEC items with fleet-watchlist tags when the link's CIK
        # matches a configured watchlist entry.
        item_tags = list(tags)
        if cik_watchlist:
            cik = extract_cik(link)
            if cik and cik in cik_watchlist:
                item_tags.extend(["watched", cik_watchlist[cik]])
                matched_fleet += 1

        items.append({
            "guid": guid,
            "title": title,
            "link": link,
            "summary": strip_html(entry.get("summary", entry.get("description", "")))[:500],
            "published": pub_date.isoformat() if pub_date else "",
            "feed": name,
            "tags": item_tags,
        })

    suffix = f" (filtered {skipped_by_filter} by include_types)" if skipped_by_filter else ""
    fleet_suffix = f" — {matched_fleet} fleet-watched" if matched_fleet else ""
    print(f"  Got {len(items)} items{suffix}{fleet_suffix}", file=sys.stderr)
    return items


def format_inbound(items):
    """Format items as inbound.md content."""
    lines = []
    lines.append(f"# SENTRY Inbound Feed")
    lines.append(f"**Generated:** {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"**Items:** {len(items)}")
    lines.append("")
    
    # Group by feed
    by_feed = {}
    for item in items:
        feed = item["feed"]
        by_feed.setdefault(feed, []).append(item)
    
    for feed_name, feed_items in sorted(by_feed.items()):
        lines.append(f"## {feed_name}")
        lines.append("")
        
        for item in feed_items:
            tags_str = " ".join([f"#{t}" for t in item["tags"]])
            lines.append(f"### {item['title']}")
            lines.append(f"- **Link:** {item['link']}")
            lines.append(f"- **Date:** {item['published']}")
            lines.append(f"- **Tags:** {tags_str}")
            lines.append(f"- **GUID:** {item['guid']}")
            if item["summary"]:
                lines.append(f"- **Summary:** {item['summary']}")
            lines.append("")
    
    return "\n".join(lines)


def rotate_inbound():
    """Rotate current inbound.md to archive if it exists and is >30 days old."""
    if not INBOUND_MD.exists():
        return
    
    # Check age
    stat = INBOUND_MD.stat()
    age_days = (datetime.now().timestamp() - stat.st_mtime) / 86400
    
    if age_days > 30:
        date_str = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m")
        archive_path = ARCHIVE_DIR / f"inbound-{date_str}.md"
        
        # Append to monthly archive
        mode = "a" if archive_path.exists() else "w"
        with open(archive_path, mode) as f:
            if mode == "a":
                f.write("\n\n---\n\n")
            f.write(INBOUND_MD.read_text())
        
        # Clear current
        INBOUND_MD.unlink()
        print(f"Rotated inbound.md to {archive_path}", file=sys.stderr)


def main():
    # Load config
    if not FEEDS_YML.exists():
        print(f"ERROR: {FEEDS_YML} not found", file=sys.stderr)
        sys.exit(1)
    
    with open(FEEDS_YML) as f:
        config = yaml.safe_load(f)
    
    feeds = [f for f in config.get("feeds", []) if f.get("enabled", True)]
    
    # Load dedup state
    seen = load_seen()
    
    # Fetch all feeds.
    #   all_items: everything currently in the freshness window — written to inbound.md
    #   new_items: subset first seen this run — added to seen.json (audit trail)
    all_items = []
    new_items = []
    for feed_config in feeds:
        items = fetch_feed(feed_config)
        all_items.extend(items)
        for item in items:
            if item["guid"] not in seen:
                seen[item["guid"]] = {
                    "first_seen": datetime.now(timezone.utc).isoformat(),
                    "title": item["title"],
                    "feed": item["feed"],
                }
                new_items.append(item)

    print(f"\nIn window: {len(all_items)} items ({len(new_items)} new)", file=sys.stderr)

    # Always overwrite inbound.md with the current freshness-window snapshot.
    # History is preserved via git log of this file (every CI commit = one snapshot).
    # Writing on every run also lets SENTRY distinguish "ran, no items" from "stale".
    content = format_inbound(all_items)
    INBOUND_MD.write_text(content)
    print(f"Wrote {len(all_items)} items to {INBOUND_MD}", file=sys.stderr)

    # Save dedup state
    save_seen(seen)

    # Output for GitHub Actions
    print(f"items_fetched={len(new_items)}")


if __name__ == "__main__":
    main()
