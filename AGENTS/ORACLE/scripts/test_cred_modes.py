#!/usr/bin/env python3
"""Offline test of kalshi.py's two credential modes (added 2026-10-15, WQ-436 recovery).

The 10/14-15 laptop session made creds optional: with no key on the box kalshi.py reads
UNSIGNED (public market data) instead of dying at import. This test exercises BOTH modes
with a THROWAWAY RSA key in a temp dir — no real creds, no network (requests.get is stubbed):

  1 signed: SIGNED=True, three KALSHI-ACCESS-* headers, signature VERIFIES under the
    throwaway public key over ts+GET+/trade-api/v2<path> (query string excluded)
  2 no creds: SIGNED=False, headers == {}, stderr notice printed
  3 key_id present, PEM missing -> unsigned      4 env KALSHI_KEY_ID set, PEM missing -> unsigned
  5 malformed PEM -> import FAILS LOUD (never silently unsigned)
  6 `status` rc: signed -> returns (rc 0); unsigned -> SystemExit(3)

What it cannot show: a live AUTHENTICATED round-trip. That needs the real key (desktop only,
PROME/MACHINE_LOCAL.md row 15) — run `python3 scripts/kalshi.py status` there (rc=0 = signed lane live).
Run: python3 scripts/test_cred_modes.py   (exit 0 = all pass)
"""
import os, sys, io, base64, tempfile, importlib.util, contextlib
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "kalshi.py")
ENV_KEYS = ("KALSHI_CRED_DIR", "KALSHI_KEY_ID", "KALSHI_PRIVATE_KEY_PATH")
results = []


def check(name, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}{('  -- ' + detail) if detail else ''}")


def load(env, tag):
    """Import a fresh copy of kalshi.py under `env`; return (module, stderr_text)."""
    saved = {k: os.environ.get(k) for k in ENV_KEYS}
    for k in ENV_KEYS:
        os.environ.pop(k, None)
    os.environ.update(env)
    err = io.StringIO()
    try:
        spec = importlib.util.spec_from_file_location(f"kalshi_{tag}", SRC)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stderr(err):
            spec.loader.exec_module(mod)
        return mod, err.getvalue()
    finally:
        for k, v in saved.items():
            os.environ.pop(k, None)
            if v is not None:
                os.environ[k] = v


class FakeResp:
    def raise_for_status(self):
        pass

    def json(self):
        return {"ok": True}


def stub(mod):
    seen = {}

    def fake_get(url, headers=None, params=None, timeout=None):
        seen.update(url=url, headers=dict(headers or {}), params=params)
        return FakeResp()
    mod.requests.get = fake_get
    return seen


def main():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pem = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                            serialization.NoEncryption())
    pub = key.public_key()
    real_get = None
    with tempfile.TemporaryDirectory() as d_full, tempfile.TemporaryDirectory() as d_empty, \
            tempfile.TemporaryDirectory() as d_half, tempfile.TemporaryDirectory() as d_bad:
        open(os.path.join(d_full, "key_id.txt"), "w").write("TEST-KEY-ID\n")
        open(os.path.join(d_full, "private_key.pem"), "wb").write(pem)
        open(os.path.join(d_half, "key_id.txt"), "w").write("TEST-KEY-ID\n")
        open(os.path.join(d_bad, "key_id.txt"), "w").write("TEST-KEY-ID\n")
        open(os.path.join(d_bad, "private_key.pem"), "wb").write(b"-----BEGIN PRIVATE KEY-----\nnot a key\n-----END PRIVATE KEY-----\n")

        # 1 signed
        m, err = load({"KALSHI_CRED_DIR": d_full}, "signed")
        real_get = m.requests.get
        check("1a signed: SIGNED=True, KEY_ID read from file", m.SIGNED is True and m.KEY_ID == "TEST-KEY-ID")
        check("1b signed: no UNSIGNED notice on stderr", "UNSIGNED" not in err)
        seen = stub(m)
        m._get("/markets", params={"event_ticker": "KXFED-26DEC"})
        h = seen["headers"]
        check("1c signed: three KALSHI-ACCESS-* headers sent",
              set(h) == {"KALSHI-ACCESS-KEY", "KALSHI-ACCESS-TIMESTAMP", "KALSHI-ACCESS-SIGNATURE"})
        msg = f"{h.get('KALSHI-ACCESS-TIMESTAMP')}GET/trade-api/v2/markets".encode()
        try:
            pub.verify(base64.b64decode(h["KALSHI-ACCESS-SIGNATURE"]), msg,
                       padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                   salt_length=hashes.SHA256().digest_size), hashes.SHA256())
            ok = True
        except Exception as e:  # noqa: BLE001
            ok = False
        check("1d signed: RSA-PSS signature verifies over ts+GET+path (query excluded)", ok)
        check("1e signed: params passed through as query", seen["params"] == {"event_ticker": "KXFED-26DEC"})
        m.requests.get = real_get

        # 2 no creds
        m, err = load({"KALSHI_CRED_DIR": d_empty}, "empty")
        check("2a no creds: SIGNED=False, import survives", m.SIGNED is False and m.KEY_ID is None)
        check("2b no creds: UNSIGNED notice on stderr", "UNSIGNED public read" in err)
        seen = stub(m)
        m._get("/markets/KXFED-26DEC-T4.00")
        check("2c no creds: request carries NO auth headers", seen["headers"] == {})
        m.requests.get = real_get

        # 3 / 4 partial creds
        m, _ = load({"KALSHI_CRED_DIR": d_half}, "half")
        check("3  key_id present, PEM missing -> unsigned", m.SIGNED is False)
        m, _ = load({"KALSHI_CRED_DIR": d_empty, "KALSHI_KEY_ID": "ENV-ID"}, "envid")
        check("4  env KALSHI_KEY_ID set, PEM missing -> unsigned", m.SIGNED is False)

        # 5 malformed PEM must fail loud
        try:
            load({"KALSHI_CRED_DIR": d_bad}, "bad")
            ok = False
        except Exception:  # noqa: BLE001
            ok = True
        check("5  malformed PEM -> import raises (fail loud, not silently unsigned)", ok)

        # 6 status exit codes
        m, _ = load({"KALSHI_CRED_DIR": d_full}, "st_signed")
        stub(m)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                m.cmd_status(None)
            ok = True
        except SystemExit:
            ok = False
        check("6a status signed -> returns (rc 0)", ok)
        m, _ = load({"KALSHI_CRED_DIR": d_empty}, "st_unsigned")
        stub(m)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                m.cmd_status(None)
            code = None
        except SystemExit as e:
            code = e.code
        check("6b status unsigned -> SystemExit(3)", code == 3, f"got {code}")

    n, k = len(results), sum(results)
    print(f"{k}/{n} pass")
    sys.exit(0 if k == n else 1)


if __name__ == "__main__":
    main()
