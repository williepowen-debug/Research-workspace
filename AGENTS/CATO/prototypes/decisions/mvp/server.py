#!/usr/bin/env python3
"""Loopback-only fictional Decisions rehearsal. Live submissions are unavailable."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets

from store import HERE, Store, reader


def make_server(store, port=0):
    capability = secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def send(self, status, value, mime="application/json"):
            body = (json.dumps(value, ensure_ascii=False) if mime == "application/json" else value).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", mime + "; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Referrer-Policy", "no-referrer")
            self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'")
            self.end_headers()
            self.wfile.write(body)

        def expected_host(self):
            return f"127.0.0.1:{self.server.server_port}"

        def host_ok(self):
            return self.headers.get("Host") == self.expected_host()

        def do_GET(self):
            if not self.host_ok():
                return self.send(403, {"error": "Unexpected host"})
            try:
                if self.path == "/":
                    html = (HERE / "index.html").read_text(encoding="utf-8")
                    return self.send(200, html.replace("__CAPABILITY__", json.dumps(capability)), "text/html")
                if self.path == "/api/display":
                    return self.send(200, store.display())
                if self.path == "/comparison":
                    records = reader.load_records()
                    return self.send(200, reader.html_document(reader.project(records), reader.queue_markdown(records)), "text/html")
                return self.send(404, {"error": "Unknown route"})
            except ValueError as error:
                return self.send(409, {"error": str(error)})
            except Exception as error:
                return self.send(503, {"error": f"Source/store unavailable: {type(error).__name__}. No empty inbox or permission is inferred."})

        def do_POST(self):
            if (not self.host_ok() or self.headers.get("Origin") != "http://" + self.expected_host()
                    or not secrets.compare_digest(self.headers.get("X-Decisions-Session", ""), capability)):
                return self.send(403, {"error": "Local session validation failed"})
            if self.path != "/api/responses":
                return self.send(404, {"error": "Unknown route"})
            if self.headers.get("Content-Type") != "application/json":
                return self.send(415, {"error": "JSON required"})
            try:
                size = int(self.headers.get("Content-Length", "0"))
                if not 0 < size <= 600000:
                    return self.send(413, {"error": "Response exceeds request limit"})
                self.connection.settimeout(10)
                request = json.loads(self.rfile.read(size))
                return self.send(200, store.save(request))
            except (ValueError, TypeError) as error:
                return self.send(409, {"error": str(error)})
            except Exception as error:
                return self.send(503, {"error": f"Save not confirmed ({type(error).__name__}); keep your draft and retry the same response."})

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--store", type=Path, required=True, help="Machine-local SQLite file; never a shared/synced database")
    parser.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    server = make_server(Store(args.store), args.port)
    print(f"Fictional rehearsal: http://127.0.0.1:{server.server_port}/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
