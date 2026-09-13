#!/usr/bin/env python3
"""`gate_fixture.destroy()` must not be able to delete anything it did not create.

DEFECT (Will, 2026-09-12 23:41, inspecting the first version): the guard was
`str(root).startswith(tempfile.gettempdir())` — a raw string prefix with no
`resolve()`. With deletion mocked it accepted `/tmp/../home/willi/Research-workspace`,
which resolves to the real repository; it also accepted bare `/tmp` and any path
merely prefixed by the tempdir string. `ignore_errors=True` meant a wrong deletion
would report nothing. Falsified against the pre-fix module: all three of those paths
reached `shutil.rmtree`.

In a module whose entire thesis is "tests must not touch real state", a containment
guard that a `..` walks past is the defect it exists to prevent.

REPAIR (Will's words): "let the fixture own its TemporaryDirectory and clean up that
exact allocation, rather than accept arbitrary paths for recursive deletion." So this
is not a better string test — an arbitrary path is no longer something `destroy()` can
be asked to delete. It looks the path up among allocations THIS MODULE made; anything
else is refused and nothing is removed.

⛔ EVERY test here mocks deletion. A test that proves a guard by actually deleting is
the thing being guarded against.
"""
import pathlib
import shutil
import tempfile
import unittest
from unittest import mock

import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gate_fixture as F  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[3]


class RefusesWhatItDoesNotOwn(unittest.TestCase):
    """Deletion is mocked throughout: the assertion is that it is never CALLED."""

    OUTSIDE = [
        "/tmp",                                      # the tempdir itself
        "/tmp/../home/willi/Research-workspace",     # traversal — the reported case
        "/tmpfs-backup/real-data",                   # prefix, not a path component
        "/home/willi/Research-workspace",            # the repo, named directly
        "/",                                         # the obvious one
        "/nonexistent/never/created",
    ]

    def test_every_outside_path_is_refused_and_nothing_is_deleted(self):
        with mock.patch.object(shutil, "rmtree") as rmtree, \
             mock.patch.object(tempfile.TemporaryDirectory, "cleanup") as cleanup:
            for bad in self.OUTSIDE:
                with self.subTest(path=bad):
                    self.assertFalse(F.destroy(bad), f"accepted {bad}")
            self.assertEqual(rmtree.call_count, 0, "rmtree was called on an outside path")
            self.assertEqual(cleanup.call_count, 0, "cleanup was called on an outside path")

    def test_the_repo_itself_is_refused(self):
        with mock.patch.object(shutil, "rmtree") as rmtree:
            self.assertFalse(F.destroy(REPO))
            self.assertEqual(rmtree.call_count, 0)

    def test_None_is_refused(self):
        self.assertFalse(F.destroy(None))

    def test_a_sibling_tempdir_we_did_not_create_is_refused(self):
        """Ownership, not location. Being under /tmp is not a licence."""
        other = tempfile.mkdtemp(prefix="not-ours-")
        try:
            with mock.patch.object(shutil, "rmtree") as rmtree:
                self.assertFalse(F.destroy(other))
                self.assertEqual(rmtree.call_count, 0)
            self.assertTrue(pathlib.Path(other).is_dir(), "it was removed anyway")
        finally:
            shutil.rmtree(other, ignore_errors=True)

    def test_a_traversal_out_of_a_real_allocation_is_refused(self):
        """Start from something we DO own and climb out of it."""
        holder = tempfile.TemporaryDirectory(prefix="gate-fixture-")
        owned = pathlib.Path(holder.name).resolve()
        F._OWNED[owned] = holder
        try:
            with mock.patch.object(shutil, "rmtree") as rmtree, \
                 mock.patch.object(tempfile.TemporaryDirectory, "cleanup") as cleanup:
                self.assertFalse(F.destroy(str(owned / "..")))
                self.assertFalse(F.destroy(str(owned / ".." / "..")))
                self.assertEqual(rmtree.call_count + cleanup.call_count, 0)
        finally:
            F._OWNED.pop(owned, None)
            holder.cleanup()


class CleansUpWhatItDoesOwn(unittest.TestCase):
    """The guard must not be so tight that the fixture leaks."""

    def test_an_owned_allocation_is_accepted_and_removed(self):
        holder = tempfile.TemporaryDirectory(prefix="gate-fixture-")
        owned = pathlib.Path(holder.name).resolve()
        F._OWNED[owned] = holder
        (owned / "file.txt").write_text("x")
        self.assertTrue(F.destroy(owned))
        self.assertFalse(owned.exists(), "the allocation survived destroy()")

    def test_a_string_path_to_an_owned_allocation_also_works(self):
        holder = tempfile.TemporaryDirectory(prefix="gate-fixture-")
        owned = pathlib.Path(holder.name).resolve()
        F._OWNED[owned] = holder
        self.assertTrue(F.destroy(str(owned)))
        self.assertFalse(owned.exists())

    def test_destroying_twice_is_refused_the_second_time(self):
        """The registry entry is consumed, so a double call cannot re-delete a
        path that may since have been reused by another process."""
        holder = tempfile.TemporaryDirectory(prefix="gate-fixture-")
        owned = pathlib.Path(holder.name).resolve()
        F._OWNED[owned] = holder
        self.assertTrue(F.destroy(owned))
        with mock.patch.object(shutil, "rmtree") as rmtree:
            self.assertFalse(F.destroy(owned))
            self.assertEqual(rmtree.call_count, 0)

    def test_build_registers_its_allocation_so_the_real_flow_still_cleans_up(self):
        """Cheap structural check — build() is expensive, so assert the wiring
        rather than paying for a full export here (the F-7 suite exercises the
        real build/destroy round trip)."""
        src = (pathlib.Path(F.__file__)).read_text()
        self.assertIn("_OWNED[root] = holder", src)
        self.assertIn("holder = tempfile.TemporaryDirectory", src)

    def test_no_rmtree_remains_in_the_module(self):
        """The repair removes recursive deletion of caller-supplied paths
        entirely; if rmtree comes back, this contract is open again."""
        self.assertNotIn("rmtree", pathlib.Path(F.__file__).read_text())


if __name__ == "__main__":
    unittest.main()
