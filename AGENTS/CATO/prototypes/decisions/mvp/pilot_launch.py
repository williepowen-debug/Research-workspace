#!/usr/bin/env python3
"""Open the accepted WQ-558 pilot locally; default is a submissions-disabled preview."""
import argparse
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
from urllib.request import urlopen

from pilot_files import PilotStore, Repo
from server import make_server
from store import HERE, reader

SOURCE = "PROME/proposals/2026-10-30_wq558-l884-pilot-source.md"
VERDICT = "AGENTS/CATO/inbox/2026-10-30_from-PROME_reread-verdict-submissions-may-be-enabled.md"
ACCEPTANCE = "eeab020bb"
REVIEWED = "7fc79dbc9"
CORE = ("pilot_files.py", "store.py", "server.py", "index.html")
POWERSHELL = "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"


def accepted_repo():
    repo = Repo(reader.ROOT)
    # This command launches only the accepted pilot implementation/source family.
    # No pull, fetch, Git write, receipt synthesis or general source discovery.
    commit = repo.git("rev-parse", ACCEPTANCE + "^{commit}").strip()
    repo.git("merge-base", "--is-ancestor", commit, "origin/master")
    repo.read(VERDICT, commit)
    for name in CORE:
        path = (HERE / name).relative_to(repo.root).as_posix()
        reviewed = repo.git("show", f"{REVIEWED}:{path}").encode("utf-8")
        if (HERE / name).read_bytes() != reviewed or repo.read(path).encode("utf-8") != reviewed:
            raise ValueError("Reviewed pilot code changed; reconcile acceptance before launch: " + name)
    return repo


def make_store(path, supervised=False):
    return PilotStore(path, accepted_repo(), SOURCE, "558", "558.L884", enable_submissions=supervised)


def check_device():
    # Uses a disposable database and GET only. Never writes an answer or receipt.
    with tempfile.TemporaryDirectory(prefix="cato-decisions-device-") as tmp:
        store = make_store(Path(tmp) / "preview.sqlite3")
        server = make_server(store)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            url = f"http://127.0.0.1:{server.server_port}/"
            with urlopen(url + "api/display", timeout=10) as result:
                display = json.load(result)
            if display["submissions_enabled"] or display["import_errors"]:
                raise ValueError("Device preview has unresolved history or enabled submissions")
            windows = subprocess.run([POWERSHELL, "-NoProfile", "-Command",
                f"$u='{url}api/display'; for($i=0;$i -lt 20;$i++) {{ try {{ "
                "$d=Invoke-RestMethod -TimeoutSec 2 $u; "
                "if($d.submissions_enabled -or $d.snapshot.record.wq_id -ne '558') {exit 2}; "
                "$env:COMPUTERNAME; exit 0 } catch { Start-Sleep -Milliseconds 250 } }; exit 1"],
                capture_output=True, text=True, timeout=55)
            if windows.returncode:
                raise ValueError("Windows could not read the local pilot preview: " + windows.stderr.strip())
            return {"kind": "decisions-device-check/1", "windows_computer": windows.stdout.strip(),
                    "wsl_host": socket.gethostname(), "distro": os.environ.get("WSL_DISTRO_NAME"),
                    "source_revision": display["snapshot"]["record"]["record_revision"],
                    "source_commit": display["snapshot"]["source_commit"],
                    "fingerprint": display["snapshot"]["fingerprint"],
                    "submissions_enabled": False, "python_http": "PASS", "windows_http": "PASS",
                    "limit": "GET-only preview; not browser pixels, real answer, delivery or acknowledgment"}
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    mode = result.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Check this computer using GET only and a temporary database")
    mode.add_argument("--supervised", action="store_true", help="One real pilot only, after both-device checks; matching PROME chat confirmation remains mandatory")
    result.add_argument("--open-browser", action="store_true")
    result.add_argument("--pause", action="store_true", help="Keep a check/error console open until Enter")
    result.add_argument("--store", type=Path, default=HERE / "local-state" / "wq558.sqlite3")
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.check:
            print(json.dumps(check_device(), indent=2), flush=True)
            return 0
        store = make_store(args.store, args.supervised)
        display = store.display()  # refuse bad source before opening a browser
        if args.supervised and (display["import_errors"] or not display["submissions_enabled"]):
            raise ValueError("Response history needs reconciliation; live launch refused")
        server = make_server(store)
        url = f"http://127.0.0.1:{server.server_port}/"
        print(("Supervised WQ-558 pilot" if args.supervised else "WQ-558 preview — answers disabled") + ": " + url, flush=True)
        print("Keep this window open. Ctrl+C stops the app. Saving is local export, not delivery or acknowledgment.", flush=True)
        print("A real answer also needs your matching confirmation in PROME's chat.", flush=True)
        if args.open_browser:
            # Generated loopback URL only; no caller-provided shell text.
            subprocess.run([POWERSHELL, "-NoProfile", "-Command", f"Start-Process '{url}'"], check=True, timeout=15)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
        return 0
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print("Decisions could not open: " + str(error), file=sys.stderr, flush=True)
        return 1
    finally:
        if args.pause:
            input("Press Enter to close this window.")


if __name__ == "__main__":
    raise SystemExit(main())
