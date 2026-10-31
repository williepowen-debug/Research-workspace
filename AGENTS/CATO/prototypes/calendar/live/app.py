#!/usr/bin/env python3
"""Local, read-only calendar server. No write or agent-dispatch routes."""
import argparse
import json
import subprocess
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit
from pathlib import Path

from reader import HERE, ROOT, REGISTRY, read, snapshot


def make_server(root=ROOT, port=0):
    lock = threading.Lock()
    allowed = set()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def reply(self, code, data, kind):
            self.send_response(code)
            self.send_header('Content-Type', kind + '; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; frame-ancestors 'none'; base-uri 'none'")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            valid = {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}
            if self.headers.get('Host') not in valid or (self.headers.get('Origin') and self.headers['Origin'] not in {'http://' + v for v in valid}):
                return self.reply(403, b'Local calendar origin required', 'text/plain')
            target = urlsplit(self.path)
            if target.path == '/health':
                return self.reply(200, b'Calendar reader ready', 'text/plain')
            if target.path == '/':
                return self.reply(200, (HERE / 'index.html').read_bytes(), 'text/html')
            if target.path == '/api/calendar':
                if not lock.acquire(blocking=False):
                    return self.reply(503, b'Refresh already running; try again', 'text/plain')
                try:
                    result = snapshot(root)
                    allowed.clear()
                    allowed.update(item['path'] for item in result['coverage'])
                    allowed.add(REGISTRY)
                    return self.reply(200, json.dumps(result).encode(), 'application/json')
                finally:
                    lock.release()
            if target.path == '/source':
                name = parse_qs(target.query).get('path', [''])[0]
                if name not in allowed:
                    return self.reply(404, b'Source is not in calendar coverage', 'text/plain')
                try:
                    return self.reply(200, read(root, name).encode(), 'text/plain')
                except (OSError, ValueError):
                    return self.reply(404, b'Source unavailable; preserved excerpts remain in event details', 'text/plain')
            return self.reply(404, b'Not found', 'text/plain')

    return ThreadingHTTPServer(('127.0.0.1', port), Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--open-browser', action='store_true')
    parser.add_argument('--check', action='store_true', help='Read sources and print coverage; no server')
    parser.add_argument('--pause', action='store_true', help='Keep source-check output visible')
    parser.add_argument('--port', type=int, default=0)
    args = parser.parse_args()
    if args.check:
        data = snapshot()
        print(json.dumps({k: v for k, v in data.items() if k != 'events'}, indent=2))
        print(f"{len(data['events'])} displayed source records")
        if args.pause:
            input('Press Enter to close this window.')
        return 1 if any(x['status'] != 'loaded' for x in data['coverage']) else 0
    server = make_server(port=args.port)
    url = f'http://127.0.0.1:{server.server_port}/'
    print('Read-only calendar: ' + url, flush=True)
    if args.open_browser:
        powershell = Path('/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe')
        if powershell.exists():
            # WSL localhost forwarding can lag binding. Open only after Windows can reach it.
            command = f"$u='{url}'; for($i=0;$i -lt 30;$i++){{try{{Invoke-WebRequest -UseBasicParsing -TimeoutSec 2 ($u+'health') | Out-Null; Start-Process $u; exit 0}}catch{{Start-Sleep -Milliseconds 250}}}}; Write-Error 'Calendar localhost forwarding unavailable; retry the printed URL.'; exit 1"
            subprocess.Popen([str(powershell), '-NoProfile', '-NonInteractive', '-Command', command])
        else:
            webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
