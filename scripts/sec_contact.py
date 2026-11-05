#!/usr/bin/env python3
"""The fleet's declared SEC contact, read from one gitignored local setting (WQ-600).

SEC fair access requires a contact in the User-Agent, so tools still need a value.
It lives in FORGE/tools/market-data/.env as SEC_CONTACT=<address>, the fleet's
single home for local settings, or in the SEC_CONTACT environment variable, which
wins. It must never enter a tracked file. Each box needs its own copy: see
PROME/MACHINE_LOCAL.md.

sec_ua() never raises, because these tools are imported by tests, base-rate scripts
and desk boots that may make no SEC call at all. When the setting is absent it
returns a header value carrying the fix instruction and a newline. Python's HTTP
libraries refuse a header containing a newline before they connect, so nothing
reaches the network. It also prints the fix to stderr, because some tools report
only the exception type. Use sec_contact() when
a value reaches something other than urllib, http.client or requests, such as
curl: it raises at once.
"""
import os
import pathlib
import sys

_ROOT = pathlib.Path(__file__).resolve().parents[1]
ENV_FILE = _ROOT / "FORGE" / "tools" / "market-data" / ".env"
MISSING = ("SEC_CONTACT is not set: add SEC_CONTACT=<address> to "
           "FORGE/tools/market-data/.env (gitignored), see PROME/MACHINE_LOCAL.md")


class SecContactMissing(RuntimeError):
    """SEC_CONTACT is absent from the environment and from the local .env."""


def _read(env_file=None):
    value = os.environ.get("SEC_CONTACT", "").strip()
    if value:
        return value
    try:
        lines = pathlib.Path(env_file or ENV_FILE).read_text(encoding="utf-8").splitlines()
    except OSError:
        return ""
    for line in lines:
        key, sep, val = line.strip().removeprefix("export ").partition("=")
        if sep and key.strip() == "SEC_CONTACT":
            return val.strip().strip("'\"")
    return ""


def sec_contact(env_file=None):
    """Return the contact, or raise SecContactMissing with the fix instruction."""
    value = _read(env_file)
    if not value:
        raise SecContactMissing(MISSING)
    return value


def sec_ua(template="{}", env_file=None):
    """Fill template's {} with the contact. Absent setting: see the module docstring."""
    value = _read(env_file)
    if value:
        return template.format(value)
    print(MISSING, file=sys.stderr)  # some tools report only the exception type
    return f"{MISSING}\n"
