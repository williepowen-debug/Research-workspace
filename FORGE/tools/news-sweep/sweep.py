#!/usr/bin/env python3
"""
News Sweep — v2 with entity classification, WATCH_FOR matching, and inbox routing.

Usage:
    python3 sweep.py                    # full sweep, markdown output
    python3 sweep.py --compact          # Telegram-friendly summary
    python3 sweep.py --agent BROCK      # filter to single agent
    python3 sweep.py --alerts-only      # 🔴 items only
    python3 sweep.py --json             # raw JSON output
    python3 sweep.py --route            # write to agent inboxes
    python3 sweep.py --priority high    # high-priority sources only
    python3 sweep.py --dry-run          # classify but don't save/route

Schedule: M-F 8:30 AM ET auto (cron), plus on-demand.
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

import feedparser

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOL_DIR)
from config import (
    GOOGLE_NEWS_QUERIES, RSS_FEEDS, WEB_SCRAPE,
    DEDUP_HOURS, CACHE_DIR, MAX_ARTICLES_PER_SOURCE,
    REQUEST_TIMEOUT, GOOGLE_NEWS_DELAY,
    WORKSPACE, AGENTS_DIR,
    google_news_rss_url, get_source_weight, classify_article,
)

CACHE_PATH = os.path.join(TOOL_DIR, CACHE_DIR)
SEEN_FILE = os.path.join(CACHE_PATH, "seen.json")
LATEST_JSON = os.path.join(TOOL_DIR, "latest.json")
LATEST_MD = os.path.join(TOOL_DIR, "latest.md")

os.makedirs(CACHE_PATH, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (compatible; Prome/1.0; +research)"


# ---------------------------------------------------------------------------
# Dedup / seen tracking
# ---------------------------------------------------------------------------

def load_seen():
    if os.path.exists(SEEN_FILE):
        try:
            with open(SEEN_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {}


def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(seen, f)


def headline_hash(title):
    normalized = re.sub(r'[^a-z0-9\s]', '', title.lower().strip())
    normalized = re.sub(r'\s+', ' ', normalized)
    return hashlib.md5(normalized.encode()).hexdigest()


def prune_seen(seen, hours=None):
    if hours is None:
        hours = DEDUP_HOURS
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=hours)).isoformat()
    return {k: v for k, v in seen.items() if v.get("ts", "") > cutoff}


# ---------------------------------------------------------------------------
# Fetchers
# ---------------------------------------------------------------------------

def fetch_url(url, timeout=None):
    if timeout is None:
        timeout = REQUEST_TIMEOUT
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        resp = urlopen(req, timeout=timeout)
        return resp.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError, TimeoutError, OSError) as e:
        print(f"  ⚠ Fetch failed: {url} — {e}", file=sys.stderr)
        return None


def fetch_google_news(queries, priority_filter=None):
    articles = []
    for q in queries:
        if priority_filter and q.get("priority") != priority_filter:
            continue
        label = q.get("label", "unknown")
        agents = q.get("agents", [])
        url = google_news_rss_url(q["query"])

        print(f"  📡 Google News: {label}", file=sys.stderr)
        feed = feedparser.parse(url)

        if feed.bozo and not feed.entries:
            print(f"  ⚠ Parse error for {label}: {feed.bozo_exception}", file=sys.stderr)
            continue

        for entry in feed.entries[:MAX_ARTICLES_PER_SOURCE]:
            source = ""
            if hasattr(entry, "source") and hasattr(entry.source, "title"):
                source = entry.source.title
            elif hasattr(entry, "source"):
                source = getattr(entry.source, "value", str(entry.source))

            pub_time = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                try:
                    pub_time = datetime(*entry.published_parsed[:6],
                                        tzinfo=timezone.utc).isoformat()
                except (TypeError, ValueError):
                    pass

            title = entry.get("title", "").strip()
            if not title:
                continue

            if source and title.endswith(f" - {source}"):
                title = title[: -(len(source) + 3)].strip()

            articles.append({
                "title": title,
                "source": source,
                "url": entry.get("link", ""),
                "published": pub_time,
                "agents": agents,
                "feed_label": label,
                "origin": "google_news",
            })

        time.sleep(GOOGLE_NEWS_DELAY)

    return articles


def fetch_rss_feeds(feeds, priority_filter=None):
    articles = []
    for feed_cfg in feeds:
        if priority_filter and feed_cfg.get("priority") != priority_filter:
            continue
        name = feed_cfg["name"]
        agents = feed_cfg.get("agents", ["ALL"])

        print(f"  📡 RSS: {name}", file=sys.stderr)
        feed = feedparser.parse(feed_cfg["url"])

        if feed.bozo and not feed.entries:
            print(f"  ⚠ Parse error for {name}: {feed.bozo_exception}", file=sys.stderr)
            continue

        for entry in feed.entries[:MAX_ARTICLES_PER_SOURCE]:
            pub_time = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                try:
                    pub_time = datetime(*entry.published_parsed[:6],
                                        tzinfo=timezone.utc).isoformat()
                except (TypeError, ValueError):
                    pass

            title = entry.get("title", "").strip()
            desc = entry.get("description", "").strip()
            if not title:
                continue

            articles.append({
                "title": title,
                "source": name,
                "url": entry.get("link", ""),
                "published": pub_time,
                "description": desc,
                "agents": agents,
                "feed_label": name.lower().replace(" ", "-"),
                "origin": "rss",
            })

    return articles


def fetch_web_headlines(targets, priority_filter=None):
    articles = []
    for target in targets:
        if priority_filter and target.get("priority") != priority_filter:
            continue
        name = target["name"]
        agents = target.get("agents", ["ALL"])

        print(f"  📡 Web: {name}", file=sys.stderr)
        html = fetch_url(target["url"])
        if not html:
            continue

        headlines = []
        for m in re.finditer(r'\[([^\]]{15,200})\]\((/[^\)]+)\)', html):
            headlines.append({"title": m.group(1).strip(), "path": m.group(2)})
        for m in re.finditer(r'<h[1-4][^>]*>([^<]{15,200})</h[1-4]>', html):
            headlines.append({"title": m.group(1).strip(), "path": ""})
        for m in re.finditer(r'<a[^>]*href="(/[^"]+)"[^>]*>([^<]{15,200})</a>', html):
            headlines.append({"title": m.group(2).strip(), "path": m.group(1)})

        seen_titles = set()
        for h in headlines[:MAX_ARTICLES_PER_SOURCE]:
            t = h["title"].strip()
            if t in seen_titles or len(t) < 20:
                continue
            seen_titles.add(t)
            base = target["url"].rstrip("/")
            url = f"{base}{h['path']}" if h.get("path") else ""
            articles.append({
                "title": t,
                "source": name,
                "url": url,
                "published": datetime.now(timezone.utc).isoformat(),
                "agents": agents,
                "feed_label": name.lower().replace(" ", "-"),
                "origin": "web",
            })

    return articles


# ---------------------------------------------------------------------------
# Processing
# ---------------------------------------------------------------------------

def deduplicate(articles, seen):
    unique = []
    now = datetime.now(timezone.utc).isoformat()
    for art in articles:
        h = headline_hash(art["title"])
        if h in seen:
            continue
        seen[h] = {"ts": now, "title": art["title"][:80]}
        unique.append(art)
    return unique, seen


def classify_all(articles):
    """Run full classification pipeline on all articles."""
    for art in articles:
        cls = classify_article(art["title"], art.get("description", ""))
        art.update(cls)
        art["source_weight"] = get_source_weight(art.get("source", ""))

        # Merge entity-derived agents with feed-derived agents
        if cls.get("entity_info") and cls["entity_info"].get("agents"):
            entity_agents = cls["entity_info"]["agents"]
            feed_agents = art.get("agents", [])
            # Union, preserving order
            merged = list(feed_agents)
            for a in entity_agents:
                if a not in merged:
                    merged.append(a)
            art["agents"] = merged

    # Sort by priority
    cls_order = {
        "NEW_WATCH_HIT": 0, "NEW_ALERT": 1, "DEVELOPMENT": 2,
        "NEW_WATCH": 3, "NEW": 4, "KNOWN": 5, "NOISE": 6,
    }
    articles.sort(key=lambda a: (
        cls_order.get(a.get("classification", "NEW"), 4),
        -a.get("source_weight", 1),
    ))
    return articles


def filter_articles(articles, agent=None, alerts_only=False, include_suppressed=False):
    filtered = articles
    if not include_suppressed:
        filtered = [a for a in filtered if not a.get("suppressed")]
    if agent:
        agent_upper = agent.upper()
        filtered = [a for a in filtered
                    if agent_upper in a.get("agents", [])
                    or "ALL" in a.get("agents", [])]
    if alerts_only:
        filtered = [a for a in filtered
                    if a.get("classification") in ("NEW_ALERT", "NEW_WATCH_HIT")]
    return filtered


# ---------------------------------------------------------------------------
# Inbox routing
# ---------------------------------------------------------------------------

def route_to_inboxes(articles, dry_run=False):
    """Write classified articles to agent inboxes."""
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M")

    # Collect articles per agent (only non-suppressed)
    agent_articles = {}
    for art in articles:
        if art.get("suppressed"):
            continue
        for agent in art.get("agents", []):
            if agent == "ALL":
                continue  # Don't spam every agent with generic news
            agent_articles.setdefault(agent, []).append(art)

    routed_count = 0
    for agent, arts in agent_articles.items():
        if not arts:
            continue

        inbox_dir = os.path.join(AGENTS_DIR, agent, "inbox")
        if not os.path.exists(os.path.join(AGENTS_DIR, agent)):
            continue  # Agent doesn't exist
        os.makedirs(inbox_dir, exist_ok=True)

        filename = f"sweep_{date_str}_{time_str}.md"
        filepath = os.path.join(inbox_dir, filename)

        lines = [f"# News Sweep — {date_str} {time_str} UTC\n"]
        for art in arts:
            cls = art.get("classification", "NEW")
            icon = {
                "NEW_WATCH_HIT": "🔴 WATCH_FOR HIT",
                "NEW_ALERT": "🔴 ALERT",
                "DEVELOPMENT": "🟡 DEVELOPMENT",
                "NEW_WATCH": "🟡 WATCH",
                "NEW": "📰 NEW",
            }.get(cls, "📰")

            kw = f" [{art.get('keyword')}]" if art.get("keyword") else ""
            esc = f" [escalation: {art.get('escalation')}]" if art.get("escalation") else ""
            wh = ""
            if art.get("watch_hits"):
                items = [f"{a}: {w}" for a, w in art["watch_hits"]]
                wh = f" [WATCH_FOR: {'; '.join(items)}]"
            src = f" ({art.get('source', '?')}, wt:{art.get('source_weight', 1)})"

            lines.append(f"- **{icon}:** {art['title']}{kw}{esc}{wh}{src}")
            if art.get("url"):
                lines.append(f"  {art['url']}")
        lines.append("")

        if not dry_run:
            with open(filepath, "w") as f:
                f.write("\n".join(lines))
            routed_count += 1
            print(f"  📬 {agent}: {len(arts)} items → {filename}", file=sys.stderr)
        else:
            print(f"  📬 [DRY RUN] {agent}: {len(arts)} items", file=sys.stderr)

    return routed_count


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_compact(articles):
    """Telegram-friendly summary — high-priority items only + confirmation counts."""
    # Will only sees: WATCH_FOR hits, ALERTs, DEVELOPMENTs, and top WATCH keyword hits
    priority_cls = {"NEW_WATCH_HIT", "NEW_ALERT", "DEVELOPMENT"}
    priority_items = [a for a in articles if a.get("classification") in priority_cls]
    watch_kw = [a for a in articles if a.get("classification") == "NEW_WATCH"]
    suppressed = [a for a in articles if a.get("classification") == "KNOWN"]
    noise = [a for a in articles if a.get("classification") == "NOISE"]
    new_generic = [a for a in articles if a.get("classification") == "NEW"]

    lines = []
    now = datetime.now(timezone.utc).strftime("%H:%M")
    total = len(articles)

    lines.append(f"🔍 News Sweep {now} UTC — {len(priority_items)} priority, "
                 f"{len(new_generic)} new, {len(suppressed)} suppressed\n")

    for art in priority_items:
        cls = art.get("classification", "NEW")
        icon = {
            "NEW_WATCH_HIT": "🔴",
            "NEW_ALERT": "🔴",
            "DEVELOPMENT": "🟡",
            "NEW_WATCH": "🟡",
            "NEW": "📰",
        }.get(cls, "📰")

        agents = ",".join(a for a in art.get("agents", []) if a != "ALL")
        src = f" ({art.get('source', '')})" if art.get("source") else ""
        wh = ""
        if art.get("watch_hits"):
            items = [w for _, w in art["watch_hits"]]
            wh = f" ⭐WATCH_FOR: {items[0]}"

        tag = f" [{agents}]" if agents else ""
        lines.append(f"{icon} {art['title']}{src}{tag}{wh}")

    # Add top watch keyword items (limit 5)
    if watch_kw:
        lines.append(f"\n🟡 Watch keywords ({len(watch_kw)}):")
        for art in watch_kw[:5]:
            agents = ",".join(a for a in art.get("agents", []) if a != "ALL")
            src = f" ({art.get('source', '')})" if art.get("source") else ""
            lines.append(f"  • {art['title']}{src} [{agents}]")
        if len(watch_kw) > 5:
            lines.append(f"  ... +{len(watch_kw) - 5} more")

    # Routed-but-not-shown count
    if new_generic:
        lines.append(f"\n📬 {len(new_generic)} new headlines routed to agent inboxes")

    # Confirmation density for suppressed KNOWN items
    if suppressed:
        entity_counts = {}
        for art in suppressed:
            e = art.get("entity", "unknown")
            entity_counts[e] = entity_counts.get(e, 0) + 1
        top = sorted(entity_counts.items(), key=lambda x: -x[1])[:5]
        density = ", ".join(f"{e} ({c})" for e, c in top)
        lines.append(f"\n📊 Confirmation density: {density}")

    return "\n".join(lines) if lines else "No new articles found."


def format_markdown(articles):
    """Full markdown output."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"# News Sweep — {now}\n"]

    for cls_name, cls_label in [
        ("NEW_WATCH_HIT", "🔴 WATCH_FOR HITS"),
        ("NEW_ALERT", "🔴 ALERTS"),
        ("DEVELOPMENT", "🟡 DEVELOPMENTS"),
        ("NEW_WATCH", "🟡 WATCH KEYWORD HITS"),
        ("NEW", "📰 NEW HEADLINES"),
    ]:
        items = [a for a in articles if a.get("classification") == cls_name]
        if not items:
            continue
        lines.append(f"## {cls_label} ({len(items)})\n")
        for art in items:
            agents = ", ".join(a for a in art.get("agents", []) if a != "ALL")
            src = art.get("source", "?")
            wt = art.get("source_weight", 1)
            lines.append(f"- **{art['title']}**")
            detail_parts = [f"{src} (wt:{wt})"]
            if agents:
                detail_parts.append(agents)
            if art.get("keyword"):
                detail_parts.append(f"keyword: {art['keyword']}")
            if art.get("escalation"):
                detail_parts.append(f"escalation: {art['escalation']}")
            if art.get("watch_hits"):
                items_str = "; ".join(f"{a}: {w}" for a, w in art["watch_hits"])
                detail_parts.append(f"WATCH_FOR: {items_str}")
            lines.append(f"  {' | '.join(detail_parts)}")
            if art.get("url"):
                lines.append(f"  {art['url']}")
            lines.append("")

    # Suppressed summary
    suppressed = [a for a in articles if a.get("classification") == "KNOWN"]
    noise = [a for a in articles if a.get("classification") == "NOISE"]
    if suppressed or noise:
        lines.append(f"## Suppressed\n")
        if suppressed:
            entity_counts = {}
            for art in suppressed:
                e = art.get("entity", "unknown")
                entity_counts[e] = entity_counts.get(e, 0) + 1
            for e, c in sorted(entity_counts.items(), key=lambda x: -x[1]):
                lines.append(f"- KNOWN: {e} ({c} articles)")
        if noise:
            lines.append(f"- NOISE: {len(noise)} articles filtered")
        lines.append("")

    # Stats
    total = len(articles)
    actionable = len([a for a in articles if not a.get("suppressed")])
    lines.append(f"---\n*{total} total, {actionable} actionable, {len(suppressed)} KNOWN, {len(noise)} noise*")
    return "\n".join(lines)


def format_json(articles):
    return json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total": len(articles),
        "actionable": len([a for a in articles if not a.get("suppressed")]),
        "known": len([a for a in articles if a.get("classification") == "KNOWN"]),
        "noise": len([a for a in articles if a.get("classification") == "NOISE"]),
        "articles": [a for a in articles if not a.get("suppressed")],
        "suppressed_summary": _suppressed_summary(articles),
    }, indent=2, default=str)


def _suppressed_summary(articles):
    suppressed = [a for a in articles if a.get("classification") == "KNOWN"]
    entity_counts = {}
    for art in suppressed:
        e = art.get("entity", "unknown")
        entity_counts[e] = entity_counts.get(e, 0) + 1
    return entity_counts


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Prome News Sweep v2")
    parser.add_argument("--compact", action="store_true", help="Telegram-friendly output")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--agent", type=str, help="Filter to single agent")
    parser.add_argument("--alerts-only", action="store_true", help="Only ALERT + WATCH_FOR items")
    parser.add_argument("--priority", type=str, help="Filter sources by priority")
    parser.add_argument("--no-dedup", action="store_true", help="Skip dedup")
    parser.add_argument("--no-cache", action="store_true", help="Don't save seen cache")
    parser.add_argument("--route", action="store_true", help="Write to agent inboxes")
    parser.add_argument("--dry-run", action="store_true", help="Classify but don't save")
    parser.add_argument("--include-suppressed", action="store_true", help="Show KNOWN items too")
    args = parser.parse_args()

    priority = args.priority

    print("🔍 Starting news sweep v2...", file=sys.stderr)
    all_articles = []

    # Phase 1: Google News RSS
    articles = fetch_google_news(GOOGLE_NEWS_QUERIES, priority)
    print(f"  → {len(articles)} from Google News", file=sys.stderr)
    all_articles.extend(articles)

    # Phase 2: Direct RSS
    articles = fetch_rss_feeds(RSS_FEEDS, priority)
    print(f"  → {len(articles)} from RSS feeds", file=sys.stderr)
    all_articles.extend(articles)

    # Phase 3: Web scrape
    articles = fetch_web_headlines(WEB_SCRAPE, priority)
    print(f"  → {len(articles)} from web scrape", file=sys.stderr)
    all_articles.extend(articles)

    print(f"  Total raw: {len(all_articles)}", file=sys.stderr)

    # Dedup
    if not args.no_dedup:
        seen = load_seen()
        seen = prune_seen(seen)
        all_articles, seen = deduplicate(all_articles, seen)
        if not args.no_cache and not args.dry_run:
            save_seen(seen)
        print(f"  After dedup: {len(all_articles)}", file=sys.stderr)

    # Classify
    all_articles = classify_all(all_articles)

    # Stats
    by_cls = {}
    for a in all_articles:
        c = a.get("classification", "NEW")
        by_cls[c] = by_cls.get(c, 0) + 1
    print(f"  Classification: {by_cls}", file=sys.stderr)

    # Route to inboxes
    if args.route:
        route_to_inboxes(all_articles, dry_run=args.dry_run)

    # Filter for output
    output_articles = filter_articles(
        all_articles,
        agent=args.agent,
        alerts_only=args.alerts_only,
        include_suppressed=args.include_suppressed,
    )

    # Output
    if args.json:
        output = format_json(all_articles)
    elif args.compact:
        output = format_compact(all_articles)
    else:
        output = format_markdown(all_articles)

    print(output)

    # Save latest
    if not args.dry_run:
        try:
            with open(LATEST_JSON, "w") as f:
                f.write(format_json(all_articles))
            with open(LATEST_MD, "w") as f:
                f.write(format_markdown(all_articles))
        except IOError as e:
            print(f"  ⚠ Could not save output files: {e}", file=sys.stderr)

    # Summary
    actionable = len([a for a in all_articles if not a.get("suppressed")])
    known = by_cls.get("KNOWN", 0)
    noise = by_cls.get("NOISE", 0)
    watch_hits = by_cls.get("NEW_WATCH_HIT", 0)
    alerts = by_cls.get("NEW_ALERT", 0)
    print(f"\n✅ Sweep complete: {len(all_articles)} total, {actionable} actionable, "
          f"{known} KNOWN, {noise} noise", file=sys.stderr)
    if watch_hits > 0:
        print(f"⭐ {watch_hits} WATCH_FOR HIT(S)", file=sys.stderr)
    if alerts > 0:
        print(f"🔴 {alerts} ALERT(S)", file=sys.stderr)


if __name__ == "__main__":
    main()
