import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "KERNEL" / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from git_policy_check import check_text  # noqa: E402


class GitPolicyCheckTests(unittest.TestCase):
    def codes(self, text: str) -> set[str]:
        return {finding.code for finding in check_text(text)}

    def test_explicit_single_submission_path_is_allowed(self):
        text = (
            "Gate C Kernel rule: an agent may commit only "
            "`AGENTS/<NAME>/outbox/kernel/submissions/<command_id>.json`."
        )
        self.assertEqual(self.codes(text), set())

    def test_directory_wide_kernel_stage_is_rejected(self):
        self.assertIn("KERNEL_UNSAFE_PATHSPEC", self.codes("Kernel operator runs `git add KERNEL/`."))

    def test_directory_wide_agent_stage_is_rejected_in_kernel_context(self):
        text = "Kernel submission procedure:\nRun `git add AGENTS/<NAME>/`."
        self.assertIn("KERNEL_UNSAFE_PATHSPEC", self.codes(text))

    def test_automatic_push_is_rejected(self):
        self.assertIn("KERNEL_AUTO_GIT", self.codes("Kernel tools automatically push results."))

    def test_agent_kernel_write_grant_is_rejected(self):
        text = "Domain agents may edit KERNEL/shadow/events/ after acceptance."
        self.assertIn("AGENT_KERNEL_WRITE_GRANT", self.codes(text))

    def test_explicit_prohibitions_are_allowed(self):
        text = (
            "Kernel tools never commit or push automatically.\n"
            "Never use `git add KERNEL/` or `git commit -a`.\n"
            "Agents may not edit KERNEL/shadow/events/."
        )
        self.assertEqual(self.codes(text), set())


if __name__ == "__main__":
    unittest.main()
