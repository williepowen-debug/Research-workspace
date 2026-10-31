#!/usr/bin/env python3
"""Local Decisions desk: current queue, exact replies, transport and owner receipts."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import threading
import webbrowser

import delivery
import history
from pilot_files import PilotStore, Repo, RESPONSES, RECEIPTS, strict_json
from queue_store import QueueStore, QUEUE, REPLIES, open_rows, unit_for
from server import make_server
from store import HERE, identifier, reader

ACCEPTANCE = "PROME/decisions/app-acceptance.json"
BUILD_FILES = ("app.py", "desk.html", "queue_store.py", "delivery.py", "pilot_files.py", "store.py", "server.py", "owner_receipt.py", "options.py", "history.py")
PILOT_SOURCE = "PROME/proposals/2026-10-30_wq558-l884-pilot-source.md"
POWERSHELL = "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"


def build_hashes():
    values = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in BUILD_FILES}
    for name in ("PROME/tools/willq_view.py", "AGENTS/CATO/prototypes/decisions/comparison/render.py",
                 "scripts/safe-push.sh", "scripts/install-git-hooks.sh", "scripts/claim_check.py", "scripts/orphan_check.sh",
                 "scripts/githooks/commit-msg", "scripts/githooks/pre-commit", "scripts/githooks/pre-push", "scripts/account_guard.py"):
        values[name] = hashlib.sha256((reader.ROOT / name).read_bytes()).hexdigest()
    return values


def accepted(repo):
    try:
        if repo.git("config", "--get", "core.hooksPath").strip() != "scripts/githooks":
            raise ValueError("Expected the repository's reviewed Git hooks")
        raw = repo.read(ACCEPTANCE, clean=True, prefix="PROME/decisions")
        if repo.read(ACCEPTANCE, "origin/master") != raw:
            raise ValueError("Acceptance is not published")
        record = strict_json(raw)
        if record.get("schema_version") != "decisions-app-acceptance/1" or record.get("build_hashes") != build_hashes():
            raise ValueError("Build differs from independently accepted version")
        if record.get("queue_responses") is not True or record.get("matching_chat_confirmation") is not True:
            raise ValueError("Daily reply contract is not accepted")
        review = record["independent_review"]
        repo.git("merge-base", "--is-ancestor", review["commit"], "origin/master")
        repo.read(review["path"], review["commit"], prefix="PROME").strip()
        return True, ""
    except (ValueError, KeyError, TypeError, AttributeError, OSError, subprocess.CalledProcessError) as error:
        return False, "Read-only until final independent acceptance: " + str(error)


class Desk:
    html_path = HERE / "desk.html"

    def __init__(self, repo, state, enable_responses=False):
        self.repo, self.state, self.requested = repo, Path(state), enable_responses
        self.state.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()
        self.sync_receipt = None
        self.stores = {}
        self.loaded_hashes = build_hashes()

    def permissions(self):
        if build_hashes() != self.loaded_hashes:
            return False, "Application files changed. Reopen Decisions before responding."
        ok, reason = accepted(self.repo)
        return self.requested and ok, reason or ("Preview only." if not self.requested else "")

    def queue_store(self, wq, enabled):
        store = self.stores.get(wq)
        if not store:
            store = QueueStore(self.state / ("queue-" + wq + ".sqlite3"), self.repo, wq, enabled)
            self.stores[wq] = store
        store.enabled = enabled
        return store

    def display(self):
        with self.lock:
            enabled, limit = self.permissions()
            cards, errors, rows = [], [], {}
            try:
                rows = open_rows(self.repo.path(QUEUE).read_text())
            except (ValueError, OSError) as error:
                errors.append("Queue unavailable: " + str(error))
            ids = set(rows)
            for path in self.state.glob("queue-*.sqlite3"):
                wq = path.stem.removeprefix("queue-")
                if (re.fullmatch(r"[1-9][0-9]*[a-z]?", wq)
                        and self.queue_store(wq, enabled).responses()["events"]):
                    # Viewing creates a snapshot cache, not a pending answer.
                    # A later owner closure must not turn an empty cache into
                    # a missing-source error that disables the whole desk.
                    ids.add(wq)
            for path in self.repo.files(REPLIES):
                try:
                    event = strict_json(self.repo.read(path, clean=True, prefix=REPLIES))
                    wq = event["display"]["record"]["wq_id"]
                    if not re.fullmatch(r"[1-9][0-9]*[a-z]?", wq):
                        raise ValueError("Invalid saved WQ")
                    ids.add(wq)
                except (KeyError, ValueError, OSError, subprocess.CalledProcessError) as error:
                    errors.append(path + ": " + str(error))
            # An orphan receipt must be visible even when its response disappeared.
            known_paths = set(self.repo.files(REPLIES) + self.repo.files(RESPONSES))
            for path in self.repo.files(RECEIPTS):
                parts = path.split("/")
                eid = parts[-2] if len(parts) == 5 else ""
                if not re.fullmatch(r"[0-9a-f]{32}", eid) or not any(f"{prefix}/{eid}.json" in known_paths for prefix in (REPLIES, RESPONSES)):
                    errors.append("Receipt without a committed response: " + path)
            for wq in sorted(ids, key=lambda x: (rows.get(x, {}).get("due") or "9999", x)):
                try:
                    card = self.queue_store(wq, enabled and not errors).display()
                    if card["last"]:
                        card["delivery"] = delivery.delivery_state(self.repo, card["last"])
                    cards.append(card)
                except (ValueError, OSError, subprocess.CalledProcessError) as error:
                    errors.append("WQ-" + wq + ": " + str(error))
                    if wq in rows:
                        cards.append({"wq_id": wq, "unit": unit_for(rows[wq]), "hash": None,
                                      "group": "Tasks for me" if rows[wq]["kind"] == "HANDS" else "Decisions",
                                      "last": None, "receipt": None, "can_respond": False,
                                      "errors": [str(error)], "response_type": "queue"})
            # Preserve the completed real pilot in its original event dialect/store.
            if self.repo.files(RESPONSES):
                try:
                    pilot = PilotStore(self.state / "wq558.sqlite3", self.repo, PILOT_SOURCE, "558", "558.L884")
                    data = pilot.display()
                    events = data["responses"]["events"]
                    if events:
                        e = events[-1]
                        receipt = data["responses"]["integrated"].get("558.L884") or data["responses"]["receipts"].get(e["id"])
                        completed = None
                        if receipt and receipt["state"] == "integrated":
                            line = self.repo.read("PROME/DOCKET.tsv").splitlines()[883]
                            columns = line.split("\t")
                            if len(columns) > 3 and columns[3].startswith("RESOLVED") and "WQ-558" in columns[3]:
                                completed = {"label": "PROME reports implementation complete", "evidence": columns[3],
                                             "path": "PROME/DOCKET.tsv", "line": 884}
                        cards.append({"wq_id": "558", "unit": data["snapshot"]["record"]["units"][0],
                                      "snapshot": data["snapshot"], "hash": data["hash"], "last": e, "events": events,
                                      "receipt": receipt, "group": "History" if receipt and receipt["state"] == "integrated" else "Follow-through",
                                      "errors": [x["reason"] for x in data["import_errors"]], "can_respond": False,
                                      "delivery": delivery.delivery_state(self.repo, e), "response_type": "pilot",
                                      "completion": completed})
                except (ValueError, OSError, subprocess.CalledProcessError, IndexError) as error:
                    errors.append("Pilot history unavailable: " + str(error))
            if errors:
                for card in cards:
                    card["can_respond"] = False
            rulings = history.recent(self.repo)
            return {"mode": "decisions-desk", "cards": cards, "errors": errors, "limit": limit,
                    "rulings": rulings,
                    "can_deliver": enabled and not errors, "sync": self.sync_receipt,
                    "head": self.repo.git("rev-parse", "HEAD").strip()}

    def save(self, request):
        with self.lock:
            state = self.display()
            unit = request.get("unit_id") if isinstance(request, dict) else None
            card = next((c for c in state["cards"] if c["unit"]["id"] == unit), None)
            if not card or card["response_type"] != "queue":
                raise ValueError("Select a current queue item")
            store = self.stores[card["wq_id"]]
            if not card["can_respond"]:
                store.enabled = False
            return store.save(request)

    def operate(self, path, request):
        with self.lock:
            if path == "/api/sync":
                self.sync_receipt = delivery.sync(self.repo)
                return self.sync_receipt
            if path == "/api/deliver":
                eid = identifier(request.get("id"))
                state = self.display()
                if not state["can_deliver"]:
                    raise ValueError("Delivery is unavailable until final acceptance or reconciliation")
                event = next((c["last"] for c in state["cards"] if c.get("last") and c["last"]["id"] == eid), None)
                if event is None:
                    raise ValueError("Only the latest saved response can be delivered; review its replacement")
                def guard():
                    if not self.permissions()[0]:
                        raise ValueError("Acceptance or application changed during delivery; reopen Decisions")
                return delivery.deliver(self.repo, event, guard=guard)
            raise ValueError("Unknown desk operation")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--open-browser", action="store_true")
    p.add_argument("--preview", action="store_true")
    p.add_argument("--check", action="store_true")
    p.add_argument("--pause", action="store_true")
    p.add_argument("--state", type=Path, default=HERE / "local-state")
    p.add_argument("--port", type=int, default=0)
    args = p.parse_args(argv)
    try:
        desk = Desk(Repo(reader.ROOT), args.state, enable_responses=not args.preview)
        initial = desk.display()
        if args.check:
            print(json.dumps({"cards": len(initial["cards"]), "errors": initial["errors"],
                              "acceptance": initial["limit"], "host": __import__('socket').gethostname()}, indent=2))
            return 1 if initial["errors"] else 0
        server = make_server(desk, args.port)
        url = f"http://127.0.0.1:{server.server_port}/"
        print("Decisions: " + url, flush=True)
        print("Keep this window open. Ctrl+C closes the service.", flush=True)
        if args.open_browser:
            if Path(POWERSHELL).exists():
                subprocess.run([POWERSHELL, "-NoProfile", "-Command", f"Start-Process '{url}'"], check=True, timeout=15)
            else:
                webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
        return 0
    finally:
        if args.pause:
            input("Press Enter to close this window.")


if __name__ == "__main__":
    raise SystemExit(main())
