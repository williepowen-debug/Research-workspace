#!/usr/bin/env python3
"""EDGAR Filing Radar — MVP detection + latest summaries.

Dry-run first:
  python3 FORGE/tools/filing-watch/poll_edgar.py --dry-run --lookback-days 14

Normal run writes latest.json/latest.md and updates seen_filings.json for newly seen
filings. It does not route to agent inboxes yet.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml

TOOL_DIR = Path(__file__).resolve().parent
WATCHLIST = TOOL_DIR / "watchlist.yml"
SEEN_FILE = TOOL_DIR / "seen_filings.json"
LATEST_JSON = TOOL_DIR / "latest.json"
LATEST_MD = TOOL_DIR / "latest.md"
USER_AGENT = "Prome Filing Radar contact: research@local"
SEC_DELAY = 0.12  # stay below SEC's 10 req/sec guidance
DEFAULT_FORMS = {"10-K", "10-Q", "8-K", "NT 10-K", "NT 10-Q", "4", "SC 13D", "SC 13G"}


@dataclass
class Entity:
    ticker: str
    name: str
    cik: str
    agents: list[str]
    forms: set[str]
    keywords: list[str]

    @property
    def cik10(self) -> str:
        return str(self.cik).lstrip("0").zfill(10)

    @property
    def cik_nolead(self) -> str:
        return str(self.cik).lstrip("0")


def load_entities(path: Path = WATCHLIST) -> list[Entity]:
    data = yaml.safe_load(path.read_text()) or {}
    entities = []
    for row in data.get("entities", []):
        entities.append(Entity(
            ticker=str(row["ticker"]).upper(),
            name=str(row.get("name", row["ticker"])),
            cik=str(row["cik"]),
            agents=[str(a).upper() for a in row.get("agents", [])],
            forms=set(row.get("forms") or DEFAULT_FORMS),
            keywords=[str(k) for k in row.get("keywords", [])],
        ))
    return entities


def load_seen() -> set[str]:
    if not SEEN_FILE.exists():
        return set()
    try:
        data = json.loads(SEEN_FILE.read_text())
        return set(data if isinstance(data, list) else data.get("seen", []))
    except Exception:
        return set()


def save_seen(seen: set[str]) -> None:
    SEEN_FILE.write_text(json.dumps(sorted(seen), indent=2) + "\n")


def fetch_submissions(entity: Entity) -> dict[str, Any]:
    url = f"https://data.sec.gov/submissions/CIK{entity.cik10}.json"
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def sec_url(entity: Entity, accession: str, doc: str) -> str:
    acc_clean = accession.replace("-", "")
    if doc:
        return f"https://www.sec.gov/Archives/edgar/data/{entity.cik_nolead}/{acc_clean}/{doc}"
    return f"https://www.sec.gov/Archives/edgar/data/{entity.cik_nolead}/{acc_clean}/"


def iter_recent_filings(entity: Entity, data: dict[str, Any], lookback: date, limit: int) -> list[dict[str, Any]]:
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accs = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])
    descs = recent.get("primaryDocDescription", [])
    out = []
    for i, form in enumerate(forms):
        if len(out) >= limit:
            break
        form = str(form)
        if form not in entity.forms:
            continue
        filed = dates[i] if i < len(dates) else ""
        try:
            filed_date = datetime.strptime(filed, "%Y-%m-%d").date()
        except Exception:
            filed_date = date.min
        if filed_date < lookback:
            continue
        acc = accs[i] if i < len(accs) else ""
        doc = docs[i] if i < len(docs) else ""
        desc = descs[i] if i < len(descs) else ""
        fid = f"{entity.ticker}:{acc}"
        out.append({
            "id": fid,
            "ticker": entity.ticker,
            "company": entity.name,
            "cik": entity.cik10,
            "agents": entity.agents,
            "form": form,
            "filingDate": filed,
            "accession": acc,
            "document": doc,
            "description": desc,
            "url": sec_url(entity, acc, doc),
            "keywords": entity.keywords,
        })
    return out


def priority(form: str) -> str:
    if form in {"NT 10-K", "NT 10-Q"}:
        return "🔴"
    if form in {"10-K", "10-Q", "8-K"}:
        return "🟠"
    return "🟡"


def write_latest(rows: list[dict[str, Any]], dry_run: bool, new_count: int, errors: list[str]) -> None:
    generated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {"generated": generated, "dryRun": dry_run, "newCount": new_count, "errors": errors, "filings": rows}
    LATEST_JSON.write_text(json.dumps(payload, indent=2) + "\n")
    lines = [f"# EDGAR Filing Radar — latest", "", f"Generated: {generated}", f"Dry run: {dry_run}", f"New filings: {new_count}", ""]
    if errors:
        lines += ["## Errors", ""] + [f"- {e}" for e in errors] + [""]
    if not rows:
        lines += ["No matching filings in lookback window.", ""]
    else:
        lines += ["## Filings", ""]
        for r in rows:
            new_tag = "NEW " if r.get("isNew") else ""
            agents = ", ".join(r.get("agents", [])) or "—"
            lines.append(f"- {priority(r['form'])} **{new_tag}{r['ticker']} {r['form']}** — {r['filingDate']} → {agents}")
            lines.append(f"  - {r.get('description') or r.get('company')}")
            lines.append(f"  - {r['url']}")
    LATEST_MD.write_text("\n".join(lines).rstrip() + "\n")


def main() -> int:
    ap = argparse.ArgumentParser(description="Poll SEC EDGAR submissions for watched companies")
    ap.add_argument("--dry-run", action="store_true", help="Do not update seen_filings.json; still writes latest outputs")
    ap.add_argument("--lookback-days", type=int, default=14, help="Only show filings within this many days")
    ap.add_argument("--limit-per-entity", type=int, default=8)
    ap.add_argument("--new-only", action="store_true", help="Only print filings not in seen file")
    ap.add_argument("--material-only", action="store_true", help="Exclude ownership forms (4/SC 13D/SC 13G); show 10-K/10-Q/8-K/NT only")
    args = ap.parse_args()

    entities = load_entities()
    seen = load_seen()
    lookback = date.today() - timedelta(days=args.lookback_days)
    rows: list[dict[str, Any]] = []
    errors: list[str] = []

    for ent in entities:
        try:
            data = fetch_submissions(ent)
            filings = iter_recent_filings(ent, data, lookback, args.limit_per_entity)
            for f in filings:
                if args.material_only and f["form"] not in {"10-K", "10-Q", "8-K", "NT 10-K", "NT 10-Q"}:
                    continue
                f["isNew"] = f["id"] not in seen
                if args.new_only and not f["isNew"]:
                    continue
                rows.append(f)
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            errors.append(f"{ent.ticker}: {e}")
        except Exception as e:
            errors.append(f"{ent.ticker}: {type(e).__name__}: {e}")
        time.sleep(SEC_DELAY)

    rows.sort(key=lambda r: (r.get("filingDate", ""), r.get("ticker", "")), reverse=True)
    new_ids = {r["id"] for r in rows if r.get("isNew")}
    if new_ids and not args.dry_run:
        seen |= new_ids
        save_seen(seen)
    write_latest(rows, args.dry_run, len(new_ids), errors)

    print(f"EDGAR Filing Radar: {len(rows)} matching filings ({len(new_ids)} new) across {len(entities)} entities")
    if errors:
        print("Errors:")
        for e in errors:
            print(f"  - {e}")
    for r in rows[:40]:
        tag = "NEW " if r.get("isNew") else ""
        print(f"{priority(r['form'])} {tag}{r['filingDate']} {r['ticker']:<5} {r['form']:<8} -> {','.join(r['agents'])} {r['url']}")
    if len(rows) > 40:
        print(f"... {len(rows)-40} more in {LATEST_MD}")
    print(f"Wrote {LATEST_MD} and {LATEST_JSON}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
