#!/usr/bin/env python3
"""scripts/sec_contact.py: alert and clean paths, including that no connection is attempted."""
import importlib.util
import io
import os
import pathlib
import socket
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from unittest import mock

sys_path = pathlib.Path(__file__).with_name("sec_contact.py")
spec = importlib.util.spec_from_file_location("sec_contact", sys_path)
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)
FAKE = "contact@example.invalid"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.env = pathlib.Path(self.tmp.name) / ".env"
        patch = mock.patch.dict(os.environ)
        patch.start()
        self.addCleanup(patch.stop)
        os.environ.pop("SEC_CONTACT", None)


class Reading(Base):
    def test_reads_env_file(self):
        self.env.write_text(f"FRED_API_KEY=x\nSEC_CONTACT={FAKE}\n")
        self.assertEqual(sc.sec_ua("X-Research {}", self.env), f"X-Research {FAKE}")

    def test_strips_quotes_and_export(self):
        self.env.write_text(f'export SEC_CONTACT="{FAKE}"\n')
        self.assertEqual(sc.sec_contact(self.env), FAKE)

    def test_environment_wins(self):
        self.env.write_text("SEC_CONTACT=file@example.invalid\n")
        os.environ["SEC_CONTACT"] = FAKE
        self.assertEqual(sc.sec_contact(self.env), FAKE)

    def test_similar_key_is_not_the_setting(self):
        self.env.write_text(f"XSEC_CONTACT={FAKE}\nSEC_CONTACT_OLD={FAKE}\n")
        with self.assertRaises(sc.SecContactMissing):
            sc.sec_contact(self.env)

    def test_empty_value_is_absent(self):
        self.env.write_text("SEC_CONTACT=\n")
        with self.assertRaises(sc.SecContactMissing):
            sc.sec_contact(self.env)


class Absent(Base):
    def test_sec_contact_raises_with_fix(self):
        with self.assertRaisesRegex(sc.SecContactMissing, "FORGE/tools/market-data/.env"):
            sc.sec_contact(self.env)

    def test_sec_ua_does_not_raise_at_import_time(self):
        self.assertIn("SEC_CONTACT is not set", sc.sec_ua("X {}", self.env))

    def test_sec_ua_prints_the_fix_to_stderr(self):
        with mock.patch("sys.stderr", new=io.StringIO()) as err:
            sc.sec_ua("X {}", self.env)
        self.assertIn("FORGE/tools/market-data/.env", err.getvalue())

    def test_present_value_prints_nothing(self):
        self.env.write_text(f"SEC_CONTACT={FAKE}\n")
        with mock.patch("sys.stderr", new=io.StringIO()) as err:
            sc.sec_ua("X {}", self.env)
        self.assertEqual(err.getvalue(), "")

    def test_urllib_refuses_before_connecting(self):
        """A live listener proves the refusal: it must see no connection at all."""
        server = socket.socket()
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        server.settimeout(1.0)
        seen = []

        def accept():
            try:
                seen.append(server.accept())
            except OSError:
                pass

        thread = threading.Thread(target=accept)
        thread.start()
        url = f"http://127.0.0.1:{server.getsockname()[1]}/"
        request = urllib.request.Request(url, headers={"User-Agent": sc.sec_ua("X {}", self.env)})
        with self.assertRaisesRegex(ValueError, "SEC_CONTACT is not set") as caught:
            urllib.request.urlopen(request, timeout=1)
        self.assertNotIsInstance(caught.exception, urllib.error.URLError)
        thread.join()
        server.close()
        self.assertEqual(seen, [], "a connection reached the listener")

    def test_requests_refuses_before_connecting(self):
        try:
            import requests
        except ImportError:
            self.skipTest("requests not installed")
        with mock.patch("requests.adapters.HTTPAdapter.send") as send:
            with self.assertRaisesRegex(requests.exceptions.InvalidHeader, "SEC_CONTACT is not set"):
                requests.get("http://127.0.0.1:9/", headers={"User-Agent": sc.sec_ua("X {}", self.env)})
        send.assert_not_called()

    def test_present_value_passes_urllib_header_check(self):
        """Clean path: a set contact reaches the listener."""
        self.env.write_text(f"SEC_CONTACT={FAKE}\n")
        server = socket.socket()
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        server.settimeout(2.0)
        got = []

        def accept():
            conn, _ = server.accept()
            got.append(conn.recv(4096))
            conn.sendall(b"HTTP/1.0 200 OK\r\nContent-Length: 0\r\n\r\n")
            conn.close()

        thread = threading.Thread(target=accept)
        thread.start()
        url = f"http://127.0.0.1:{server.getsockname()[1]}/"
        urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": sc.sec_ua("X {}", self.env)}), timeout=2)
        thread.join()
        server.close()
        self.assertIn(f"X {FAKE}".encode(), got[0])


if __name__ == "__main__":
    unittest.main()
