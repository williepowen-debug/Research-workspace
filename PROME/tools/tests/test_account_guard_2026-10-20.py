#!/usr/bin/env python3
"""scripts/account_guard.py — separator and neighbour forms (ARGUS ❌1, 2026-10-20).

The real account number can never live in the repo, so KNOWN is swapped for the hash of a
fake number (123456789) and the guard's real `_known()` is driven directly.

Run: python3 PROME/tools/tests/test_account_guard_2026-10-20.py
"""
import hashlib
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("account_guard", ROOT / "scripts/account_guard.py")
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)
FAKE = "123456789"


class AccountGuardForms(unittest.TestCase):
    def setUp(self):
        self._known_set = guard.KNOWN
        guard.KNOWN = {hashlib.sha256(FAKE.encode()).hexdigest()}

    def tearDown(self):
        guard.KNOWN = self._known_set

    def test_refused_forms(self):
        for s in ["123456789", "123-45-6789", "123 45 6789", "123.45.6789", "123/45/6789",
                  "123–45–6789", "qty 5 123456789", "2026-10-20 123-45-6789",
                  "x123456789x", "71234567893"]:
            with self.subTest(s=s):
                self.assertTrue(guard._known(f"IRA {s}"))

    def test_allowed_forms(self):
        for s in ["•6789", "987-65-4321", "2026-10-20 15:30", "e4511a622 1225 rows 37,840.91"]:
            with self.subTest(s=s):
                self.assertFalse(guard._known(f"IRA {s}"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
