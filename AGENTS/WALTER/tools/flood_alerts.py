#!/usr/bin/env python3
"""NWS flood alerts for Florida and California (charter step 7j; Will 2026-11-23 17:12 ET, AEOLUS request).

Prints each alert NEW since the last --mark, plus every later Update that carries RECORD, with EMERGENCY or RECORD prompts. Read-only until --mark
(which records what was last printed as seen). A failed fetch prints UNKNOWN and exits 2; nothing is marked.
Catches only what is live when a session runs it. RECORD is a word match in the text: a prompt to read, not a grade.
"""
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SEEN = ROOT / "AGENTS/WALTER/registry/flood_alerts_seen.json"
EVENTS = {"Flash Flood Warning", "Flash Flood Watch", "Coastal Flood Warning", "Flood Watch", "Flood Warning"}


def emergency(p):
    """Flash flood emergency: text, or the damage-threat tag CATASTROPHIC, on a Flash Flood Warning."""
    tag = " ".join((p.get("parameters") or {}).get("flashFloodDamageThreat") or []).upper()
    text = " ".join(str(p.get(k) or "") for k in ("headline", "description")).lower()
    return p.get("event") == "Flash Flood Warning" and ("CATASTROPHIC" in tag or "flash flood emergency" in text)


def record(p):
    return "record" in " ".join(str(p.get(k) or "") for k in ("headline", "description")).lower()


def rows(features, state, seen):
    """(is_new, flags, props) for each watched alert. An Update whose referenced alert was seen is not new."""
    out = []
    for f in features:
        p = f["properties"]
        if p.get("event") not in EVENTS:
            continue
        refs = {r.get("identifier") for r in p.get("references") or []}
        keys = [k for k in [p["id"], *refs] if k in seen]
        old = seen[keys[0]] if keys else None
        flags = [n for n, fn in (("EMERGENCY", emergency), ("RECORD", record)) if fn(p)]
        # an Update keeps the same word flag while the fact can change (near a record, then past it): show every
        # new-ID update that still carries RECORD (AEOLUS, 2026-11-23)
        is_new = old is None or any(x not in old for x in flags) or ("RECORD" in flags and p["id"] not in seen)
        out.append((is_new, flags, p, state))
    return out


def fetch(state):
    r = subprocess.run(["curl", "-sS", "--max-time", "40", f"https://api.weather.gov/alerts/active?area={state}"],
                       capture_output=True, text=True)
    if r.returncode:
        raise OSError(r.stderr.strip() or f"curl rc {r.returncode}")
    return json.loads(r.stdout)["features"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mark", action="store_true", help="record the alerts live now as seen")
    a = ap.parse_args()
    try:
        seen = json.loads(SEEN.read_text()) if SEEN.exists() else {}
        found = [x for s in ("FL", "CA") for x in rows(fetch(s), s, seen)]
    except (OSError, ValueError, KeyError) as e:
        print(f"UNKNOWN: alert read failed ({e}); not a clean result")
        return 2
    new = [x for x in found if x[0]]
    print(f"{len(found)} watched alert(s) live, {len(new)} new or changed since the last mark")
    for _, flags, p, s in new:
        print(s, "|", p["event"], "|", (p.get("areaDesc") or "")[:90], "|", (p.get("sent") or "")[:16], "|",
              p.get("messageType"), "|", p.get("ends"), "|", " ".join(flags))
    if a.mark:
        keep = {x[2]["id"]: x[1] for x in found}
        SEEN.write_text(json.dumps(keep, indent=1, sort_keys=True) + "\n")
        print(f"marked {len(keep)} as seen")
    return 0


if __name__ == "__main__":
    sys.exit(main())
