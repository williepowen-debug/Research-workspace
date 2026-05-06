#!/usr/bin/env python3
"""
SENTRY Feed Fetcher — v1.0
Pulls RSS/Atom feeds, deduplicates, writes to SIGNALS/inbound.md
Run by GitHub Actions twice daily (6 AM / 6 PM ET)
"""

import yaml
import feedparser
import hashlib
import json
import os
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


def fetch_feed(feed_config):
    """Fetch a single feed and return new items."""
    url = feed_config["url"]
    name = feed_config["name"]
    tags = feed_config.get("tags", [])
    
    print(f"Fetching: {name}...", file=sys.stderr)
    
    try:
        parsed = feedparser.parse(url)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return []
    
    items = []
    cutoff = datetime.now(timezone.utc).timestamp() - (MAX_AGE_HOURS * 3600)
    
    for entry in parsed.entries[:MAX_ITEMS_PER_FEED]:
        # Parse date
        pub_date = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
            pub_date = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc)
        
        if pub_date and pub_date.timestamp() < cutoff:
            continue
        
        guid = item_guid(entry)
        
        items.append({
            "guid": guid,
            "title": entry.get("title", "No title"),
            "link": entry.get("link", ""),
            "summary": entry.get("summary", entry.get("description", ""))[:500],
            "published": pub_date.isoformat() if pub_date else "",
            "feed": name,
            "tags": tags,
        })
    
    print(f"  Got {len(items)} items", file=sys.stderr)
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
    
    # Fetch all feeds
    all_new_items = []
    for feed_config in feeds:
        items = fetch_feed(feed_config)
        
        for item in items:
            if item["guid"] not in seen:
                seen[item["guid"]] = {
                    "first_seen": datetime.now(timezone.utc).isoformat(),
                    "title": item["title"],
                    "feed": item["feed"],
                }
                all_new_items.append(item)
    
    print(f"\nTotal new items: {len(all_new_items)}", file=sys.stderr)
    
    # Rotate if needed
    rotate_inbound()
    
    # Write inbound.md
    if all_new_items:
        content = format_inbound(all_new_items)
        
        # Append to existing or create new
        if INBOUND_MD.exists():
            with open(INBOUND_MD, "a") as f:
                f.write("\n\n---\n\n")
                f.write(content)
        else:
            with open(INBOUND_MD, "w") as f:
                f.write(content)
        
        print(f"Wrote {len(all_new_items)} items to {INBOUND_MD}", file=sys.stderr)
    else:
        print("No new items to write", file=sys.stderr)
    
    # Save dedup state
    save_seen(seen)
    
    # Output for GitHub Actions
    print(f"items_fetched={len(all_new_items)}")


if __name__ == "__main__":
    main()
