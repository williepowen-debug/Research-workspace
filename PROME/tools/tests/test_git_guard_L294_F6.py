#!/usr/bin/env python3
"""L294 F-6 — git_guard's INPUT-VALIDATION path, and only that path.

SCOPE, stated precisely because an earlier PROME summary overstated it (Will,
2026-09-12 22:5x): the guard's BLOCKING path was never broken. A normal hook
request carrying `git add .` returns 2 and names the prohibition, before and
after this repair. What was broken is the one failure path:

    input that PARSES but is not an object ([], null, "ok", 3) reached
    `data.get(...)` outside the try and raised AttributeError → rc=1 with a
    traceback. PreToolUse reserves rc=2 for blocking, so rc=1 is non-blocking —
    but the honest description is "the validation path crashed", not "the guard
    returns the wrong blocking code".

REPAIR: the shape check moved INSIDE the existing try, so a non-object payload
takes the hook's own already-declared path for uninterpretable input — fail-open
rc=0 with a loud stderr notice, exactly as an unparseable body does. No third
policy was invented, and the fail-open policy itself was not revisited: that
would be a different decision from the one this finding supports.

★ A SECOND INSTANCE, found by this suite's own overlap case and not present in
the source report: `tool_input` that is a STRING or LIST hit the identical
unguarded `.get` one level down. Validating only the top-level object fixed the
reproduction and left its nested twin live at rc=1.
`[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]`

NEIGHBOUR CATEGORIES
  ordinary ....... prohibited command blocks (2); allowed passes (0).      TESTED
  overlap ........ valid object MISSING the keys the guard reads — parses,
                   is an object, but `tool_input` absent. Two conditions at
                   once: well-formed and incomplete. Must pass, not crash.   TESTED
  wrong owner .... a non-Bash tool call must never be linted.               TESTED
  missing info ... [] / null / "ok" / 3 / unparseable → declared path,
                   never a traceback, never a bare rc=1.                    TESTED
  concurrent ..... N/A — one process, stdin read once, no shared state.
"""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
GUARD = ROOT / "PROME/tools/hooks/git_guard.py"


def hook(payload, raw=None):
    """Run the guard; return (rc, stderr). `raw` sends bytes verbatim."""
    body = raw if raw is not None else json.dumps(payload)
    p = subprocess.run([sys.executable, str(GUARD)], input=body,
                       capture_output=True, text=True)
    return p.returncode, p.stderr


def bash(cmd):
    return {"tool_name": "Bash", "tool_input": {"command": cmd}}


class BlockingPathUnchanged(unittest.TestCase):
    """The half that was NOT broken. These must stay green through any repair
    of the validation path — the repair must not buy correctness there by
    loosening the guard here."""

    def test_git_add_dot_blocks_with_2(self):
        rc, err = hook(bash("git add ."))
        self.assertEqual(rc, 2)
        self.assertIn("BLOCKED", err)

    def test_git_add_all_blocks_with_2(self):
        self.assertEqual(hook(bash("git add -A"))[0], 2)

    def test_allowed_git_command_passes(self):
        rc, err = hook(bash("git status --short"))
        self.assertEqual(rc, 0)
        self.assertEqual(err, "")

    def test_pathspec_add_is_not_blocked(self):
        self.assertEqual(hook(bash("git add PROME/STATUS.md"))[0], 0)

    def test_non_bash_tool_is_never_linted(self):
        rc, err = hook({"tool_name": "Read", "tool_input": {"file_path": "git add ."}})
        self.assertEqual(rc, 0)
        self.assertEqual(err, "")


class HeredocBypass(unittest.TestCase):
    """Independent review 2026-09-12: `_drop_heredocs` skipped forward from ANY
    `<<WORD` token and, finding no terminator, consumed every remaining line — so a
    command that merely MENTIONS the token hid the rest from the scanner. Root
    CLAUDE.md 4b prescribes heredocs for every commit message, so this is house
    style, not an edge case."""

    def test_spurious_marker_no_longer_hides_a_prohibited_command(self):
        rc, _ = hook(bash('grep -n "<<EOF" scripts/x.sh\ngit add -A'))
        self.assertEqual(rc, 2)

    def test_spurious_marker_mid_line(self):
        self.assertEqual(hook(bash("echo use <<END here\ngit reset HEAD"))[0], 2)

    def test_a_REAL_heredoc_still_shields_its_prose(self):
        """The behaviour the dropper exists for must survive the fix."""
        rc, _ = hook(bash("cat > /tmp/m.txt <<'EOF'\ndo not git add -A in here\nEOF\n"
                          "git commit -F /tmp/m.txt -- PROME/STATUS.md"))
        self.assertEqual(rc, 0)

    def test_a_REAL_heredoc_does_not_shield_what_comes_AFTER_it(self):
        rc, _ = hook(bash("cat > /tmp/m.txt <<'EOF'\nmsg\nEOF\ngit push --force"))
        self.assertEqual(rc, 2)


class MalformedInputTakesTheDeclaredPath(unittest.TestCase):
    """THE DEFECT. Each of these raised AttributeError → rc=1 + traceback."""

    CASES = ("[]", "null", '"ok"', "3", "3.5", "true")

    def test_non_object_payloads_return_0_not_1(self):
        for raw in self.CASES:
            with self.subTest(raw=raw):
                rc, err = hook(None, raw=raw)
                self.assertEqual(rc, 0, f"{raw} → rc {rc}")

    def test_non_object_payloads_never_traceback(self):
        for raw in self.CASES:
            with self.subTest(raw=raw):
                self.assertNotIn("Traceback", hook(None, raw=raw)[1])

    def test_the_fail_open_is_ANNOUNCED_not_silent(self):
        """A silent allow is worse than the crash: it looks like coverage."""
        for raw in self.CASES:
            with self.subTest(raw=raw):
                err = hook(None, raw=raw)[1]
                self.assertIn("ALLOWING without a check", err)
                self.assertIn("fail-open, not coverage", err)

    def test_the_notice_names_the_actual_type(self):
        self.assertIn("list", hook(None, raw="[]")[1])
        self.assertIn("NoneType", hook(None, raw="null")[1])
        self.assertIn("str", hook(None, raw='"ok"')[1])

    def test_unparseable_body_keeps_its_pre_existing_behaviour(self):
        """The path the non-object case now joins — unchanged by this repair."""
        rc, err = hook(None, raw="not json at all")
        self.assertEqual(rc, 0)
        self.assertIn("ALLOWING without a check", err)
        self.assertNotIn("Traceback", err)

    def test_empty_stdin(self):
        rc, err = hook(None, raw="")
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)


class WellFormedButIncomplete(unittest.TestCase):
    """Overlap: an OBJECT that is missing what the guard reads. Well-formed and
    incomplete at once — the shape check must not turn these into failures."""

    def test_object_with_no_tool_name(self):
        rc, err = hook({})
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)

    def test_bash_call_with_no_tool_input(self):
        rc, err = hook({"tool_name": "Bash"})
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)

    def test_bash_call_with_null_tool_input(self):
        rc, err = hook({"tool_name": "Bash", "tool_input": None})
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)

    def test_bash_call_with_no_command_key(self):
        rc, err = hook({"tool_name": "Bash", "tool_input": {}})
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)

    def test_tool_input_as_a_STRING_takes_the_declared_path(self):
        """FOUND BY THIS SUITE, not by the source report: the same F-6 shape one
        level down. Validating only the top-level object fixed the reproduction
        and left its nested twin raising AttributeError at rc=1."""
        rc, err = hook({"tool_name": "Bash", "tool_input": "git add ."})
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)
        self.assertIn("unusable tool_input", err)
        self.assertIn("ALLOWING without a check", err)

    def test_tool_input_as_a_LIST_takes_the_declared_path(self):
        rc, err = hook({"tool_name": "Bash", "tool_input": ["git add ."]})
        self.assertEqual(rc, 0)
        self.assertNotIn("Traceback", err)

    def test_command_of_a_non_string_type_does_not_crash(self):
        for bad in (123, ["git", "add", "."], {"x": 1}):
            with self.subTest(bad=bad):
                rc, err = hook({"tool_name": "Bash", "tool_input": {"command": bad}})
                self.assertIn(rc, (0, 2))
                self.assertNotIn("Traceback", err)


if __name__ == "__main__":
    unittest.main()
