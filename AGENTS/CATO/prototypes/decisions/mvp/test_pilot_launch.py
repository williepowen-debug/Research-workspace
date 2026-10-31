#!/usr/bin/env python3
"""Launch-boundary checks; no real responses, browser opens or Git mutations."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import pilot_launch as launch
import test_pilot_files


class LaunchTests(unittest.TestCase):
    def test_default_preview_and_check_cannot_silently_enable(self):
        self.assertFalse(launch.parser().parse_args([]).supervised)
        self.assertFalse(launch.parser().parse_args(["--check"]).supervised)
        with self.assertRaises(SystemExit):
            launch.parser().parse_args(["--check", "--supervised"])

    def test_fixed_scope_and_opt_in_are_passed_to_store(self):
        with patch.object(launch, "accepted_repo", return_value="repo"), patch.object(launch, "PilotStore") as store:
            launch.make_store(Path("local.sqlite3"))
            store.assert_called_once_with(Path("local.sqlite3"), "repo", launch.SOURCE,
                                          "558", "558.L884", enable_submissions=False)
            launch.make_store(Path("local.sqlite3"), True)
            self.assertTrue(store.call_args.kwargs["enable_submissions"])

    def test_original_acceptance_does_not_authorize_the_changed_core(self):
        with self.assertRaisesRegex(ValueError, "Reviewed pilot code changed"):
            launch.accepted_repo()

    def test_dirty_reviewed_core_prevents_launch(self):
        original = Path.read_bytes
        def altered(path):
            return b"different" if path == launch.HERE / "pilot_files.py" else original(path)
        with patch.object(Path, "read_bytes", altered), self.assertRaisesRegex(ValueError, "Reviewed pilot code changed"):
            launch.accepted_repo()

    def test_unavailable_acceptance_never_opens_browser(self):
        with patch.object(launch, "accepted_repo", side_effect=ValueError("No acceptance")), patch.object(launch.subprocess, "run") as run:
            self.assertEqual(launch.main(["--open-browser"]), 1)
            run.assert_not_called()

    def test_default_store_refuses_real_response_shape(self):
        fixture = test_pilot_files.PilotFileTests(methodName="test_default_is_read_only_and_creates_no_response_directory")
        fixture.setUp()
        try:
            fixture.store.enable_submissions = False
            with patch.object(launch, "make_store", return_value=fixture.store), patch.object(launch, "make_server") as server:
                server.return_value.server_port = 12345
                server.return_value.serve_forever.side_effect = KeyboardInterrupt
                self.assertEqual(launch.main([]), 0)
                server.return_value.server_close.assert_called_once()
            with self.assertRaisesRegex(ValueError, "disabled"):
                fixture.store.save(fixture.request())
            self.assertFalse(fixture.store.responses()["events"])
        finally:
            fixture.doCleanups()


if __name__ == "__main__":
    unittest.main()
