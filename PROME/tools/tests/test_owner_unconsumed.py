"""Owner-unconsumed boot line (S1, DOCKET L730). Temporary trees and a stub liveness only.
Acceptance: PROME/tools/tests/ACCEPTANCE_owner_unconsumed_boot_line_2026-11-16.md.
Run: PYTHONDONTWRITEBYTECODE=1 python3 -m unittest PROME/tools/tests/test_owner_unconsumed.py
"""
import datetime as dt
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("inbox_census", TOOLS / "inbox_census.py")
ic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ic)

TODAY = dt.date(2026, 11, 16)
ROSTER = """# roster
## ACTIVE (3)
| Agent | Domain |
|---|---|
| ALPHA | a |
| BETA | b |
| **GAMMA** | c |
## TIER-2 — spawned as needed (1)
| Agent | Domain |
|---|---|
| DELTA | d |
## DORMANT — revive only on explicit need (1)
| Agent | Domain |
|---|---|
| SLEEPY | s |
## RETIRED — moved out
**OLDONE** — RETIRED.
## SPECIAL
**MANUAL** — a Will-driven reviewer.
## Coverage notes
| NOTADESK | x |
"""


def day(n):
    return (TODAY - dt.timedelta(days=n)).isoformat()


class Tree:
    def __init__(self, test):
        self.temp = tempfile.TemporaryDirectory()
        test.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "AGENTS").mkdir()
        self.live = {}

    def put(self, desk, name, text="body\n", lane=None, dark=30):
        base = self.root / "AGENTS" / desk / "inbox"
        if lane:
            base = base / lane
        base.mkdir(parents=True, exist_ok=True)
        (base / name).write_text(text, encoding="utf-8")
        self.live.setdefault(desk, (day(dark), "abc1234"))
        return self

    def dark(self, desk, days):
        self.live[desk] = (day(days), "abc1234")
        return self

    def run(self, delivery=None, roster=ROSTER):
        return ic.owner_unconsumed(self.root, TODAY, lambda d: self.live.get(d), roster, {} if delivery is None else delivery)


def names(result):
    return [h["desk"] for h in result["hits"]]


class OwnerUnconsumedTests(unittest.TestCase):
    def test_a3_fresh_item_at_a_dark_desk_is_not_a_hit(self):
        t = Tree(self).put("ALPHA", f"{day(6)}_from-BETA_x.md")
        self.assertEqual(names(t.run()), [])
        t.put("ALPHA", f"{day(9)}_from-BETA_y.md")
        hit = t.run()["hits"][0]
        self.assertEqual((hit["items"], hit["aged"], hit["oldest"][0]), (2, 1, 9))

    def test_a4_a5_a6_due_field_excludes_and_nothing_else_does(self):
        future, past = (TODAY + dt.timedelta(days=3)).isoformat(), day(1)
        t = Tree(self)
        t.put("ALPHA", f"{day(20)}_from-BETA_due-future.md", f"# t\ndue: {future}\n")
        self.assertEqual(names(t.run()), [])
        self.assertEqual(t.run()["excluded"], 1)
        t.put("ALPHA", f"{day(21)}_from-BETA_due-today.md", f"due: {TODAY.isoformat()}\n")
        self.assertEqual(t.run()["excluded"], 2)
        for name, text in (("due-past", f"due: {past}\n"), ("prose-date", f"The bond matures {future}.\nComments due before {future}\n"),
                           ("not-a-date", "due: 3125-26-00\n"), ("late-field", "\n" * 15 + f"due: {future}\n"),
                           ("other-field", f"overdue: {future}\nDue: {future}\n")):
            u = Tree(self).put("ALPHA", f"{day(20)}_from-BETA_{name}.md", text)
            with self.subTest(name):
                self.assertEqual(names(u.run()), ["ALPHA"])
                self.assertEqual(u.run()["excluded"], 0)

    def test_a7_ties_are_inclusive_on_both_clocks(self):
        for age, dark, expected in ((7, 7, ["ALPHA"]), (6, 7, []), (7, 6, []), (8, 400, ["ALPHA"])):
            t = Tree(self).put("ALPHA", f"{day(age)}_from-BETA_x.md", dark=dark)
            with self.subTest(age=age, dark=dark):
                self.assertEqual(names(t.run()), expected)

    def test_a8_empty_dormant_and_special(self):
        t = Tree(self)
        (t.root / "AGENTS/ALPHA/inbox/processed").mkdir(parents=True)
        (t.root / "AGENTS/ALPHA/inbox/processed" / f"{day(90)}_from-BETA_done.md").write_text("x")
        t.dark("ALPHA", 90)
        self.assertEqual(names(t.run()), [])
        t.put("SLEEPY", f"{day(40)}_from-BETA_x.md", "ACTION: wake up\n").put("MANUAL", f"{day(40)}_from-BETA_y.md", "ACTION: review\n")
        hits = {h["desk"]: h for h in t.run()["hits"]}
        self.assertEqual((hits["SLEEPY"]["tag"], hits["SLEEPY"]["action"]), ("DORMANT", 0))
        self.assertEqual((hits["MANUAL"]["tag"], hits["MANUAL"]["action"]), ("SPECIAL", 1))
        line = ic.render_owner_unconsumed(t.run())
        self.assertIn("SLEEPY [DORMANT]", line)
        self.assertIn("MANUAL [SPECIAL]", line)
        self.assertLess(line.index("MANUAL"), line.index("SLEEPY"))  # ACTION-bearing first

    def test_a9_a_live_desk_is_never_named(self):
        t = Tree(self).put("ALPHA", f"{day(60)}_from-BETA_x.md", "ACTION: old\n", dark=0)
        self.assertEqual(names(t.run()), [])

    def test_a10_scaffolding_and_undated_files(self):
        t = Tree(self)
        for name in ("README.md", ".gitkeep", "2026-07-02_BATCH-2_MANIFEST.md", "readme.txt"):
            t.put("ALPHA", name)
        t.put("ALPHA", "PROTOCOL.md")
        r = t.run()
        self.assertEqual((names(r), r["skipped"], r["items"]), ([], 4, 1))
        t.put("ALPHA", f"{day(8)}_from-BETA_x.md")
        hit = t.run()["hits"][0]
        self.assertEqual((hit["items"], hit["oldest"]), (2, (8, f"{day(8)}_from-BETA_x.md")))
        u = Tree(self).put("ALPHA", "2026-13-45_from-BETA_not-a-day.md")
        self.assertEqual(names(u.run()), [])

    def test_a11_directories_off_the_roster_are_never_hits(self):
        t = Tree(self)
        for desk in ("OLDONE", "NOTADESK", "UNLISTED"):
            t.put(desk, f"{day(50)}_from-BETA_x.md", "ACTION: x\n")
        t.put("lowercase", f"{day(50)}_from-BETA_x.md").put("_archive", f"{day(50)}_x.md")
        r = t.run()
        self.assertEqual(names(r), [])
        self.assertEqual(sorted(d for d, _ in r["outside"]), ["NOTADESK", "OLDONE", "UNLISTED"])
        self.assertIn("outside the roster perimeter", ic.render_owner_unconsumed(r))
        self.assertEqual(sorted(ic.perimeter(ROSTER)), ["ALPHA", "BETA", "DELTA", "GAMMA", "MANUAL", "SLEEPY"])

    def test_a12_git_error_and_unfound_self_commit_are_unknown(self):
        t = Tree(self).put("ALPHA", f"{day(30)}_from-BETA_x.md").put("BETA", f"{day(30)}_from-ALPHA_x.md")
        t.put("DELTA", f"{day(30)}_from-ALPHA_x.md")
        t.live["ALPHA"] = ("!ERR", "index.lock")
        t.live["BETA"] = None
        r = t.run()
        self.assertEqual((names(r), r["unknown"]), (["DELTA"], ["ALPHA", "BETA"]))
        self.assertIn("liveness UNKNOWN", ic.render_owner_unconsumed(r))
        t.live["DELTA"] = ("!ERR", "index.lock")
        r = t.run()
        self.assertEqual(names(r), [])
        self.assertTrue(r["unknown"])  # the gate line is then not ✅ (prome_gate: ok = no hits AND no unknown)
        t.live["DELTA"] = ("garbage", "x")
        self.assertIn("DELTA", t.run()["unknown"])

    def test_a13_lane_dates_and_roles(self):
        path = "AGENTS/ALPHA/inbox/WALTER/SIG-W-20261101-005.md"
        t = Tree(self).put("ALPHA", "SIG-W-20261101-005.md", "Role: INFO\n", lane="WALTER")
        self.assertEqual(t.run()["hits"][0]["action"], 0)                              # file-name date, INFO role
        self.assertEqual(t.run({path: (TODAY - dt.timedelta(days=9), "ACTION")})["hits"][0]["action"], 1)   # the log's role wins
        self.assertEqual(names(t.run({path: (TODAY - dt.timedelta(days=2), "ACTION")})), [])                # the log's date wins
        other = {"AGENTS/BETA/inbox/WALTER/SIG-W-20261101-005.md": (TODAY - dt.timedelta(days=2), "ACTION")}
        self.assertEqual(t.run(other)["hits"][0]["action"], 0)                           # another recipient's row is not ours
        u = Tree(self).put("ALPHA", "SIG-W-20261101-006.md", "Role: ACTION\n", lane="WALTER")
        self.assertEqual(u.run()["hits"][0]["action"], 1)
        v = Tree(self).put("ALPHA", "SIG-W-20261101-007.md", "---\naction: [BETA, ALPHA]\n---\n", lane="WALTER")
        self.assertEqual(v.run()["hits"][0]["action"], 1)
        w = Tree(self).put("ALPHA", "SIG-W-20261101-008.md", "---\naction: [ALPHABET]\ninfo: [ALPHA]\n---\n", lane="WALTER")
        self.assertEqual(w.run()["hits"][0]["action"], 0)
        forms = {"**ACTION (ALPHA):** do": 1, "ACTION: do": 1, "## ACTION": 1, "## Requested action": 1,
                 "**Ask:** do": 0, "No ACTION: here": 0, "  ACTION: indented": 0, "x" * 4100 + "\nACTION: too late": 0}
        for text, expected in forms.items():
            x = Tree(self).put("ALPHA", f"{day(10)}_from-BETA_x.md", text + "\n")
            with self.subTest(text[:24]):
                self.assertEqual(x.run()["hits"][0]["action"], expected)

    def test_a15_clean_line_and_overflow(self):
        t = Tree(self).put("ALPHA", f"{day(2)}_from-BETA_x.md")
        r = t.run()
        line = ic.render_owner_unconsumed(r)
        self.assertTrue(line.startswith("none — searched 1 desks · 1 items"))
        many = Tree(self)
        roster = "## ACTIVE\n| Agent | D |\n|---|---|\n" + "".join(f"| D{i:02d} | x |\n" for i in range(12))
        for i in range(12):
            many.put(f"D{i:02d}", f"{day(10 + i)}_from-ALPHA_x.md")
        line = ic.render_owner_unconsumed(many.run(roster=roster))
        self.assertIn("+4 more desk(s)", line)
        self.assertEqual(line.count("item(s)"), 8)
        self.assertNotIn("\n", line)

    def test_unreadable_roster_and_delivery_log(self):
        t = Tree(self).put("ALPHA", f"{day(30)}_from-BETA_x.md")
        with self.assertRaises(ValueError):
            t.run(roster="# nothing parseable\n")
        r = ic.owner_unconsumed(t.root, TODAY, lambda d: t.live.get(d), ROSTER)  # no delivery log in the temp tree
        self.assertFalse(r["log_read"])
        self.assertIn("delivery log unread", ic.render_owner_unconsumed(r))
        self.assertEqual(names(r), ["ALPHA"])

    def test_delivery_log_loader_reads_et_dates_and_roles(self):
        t = Tree(self)
        log = t.root / "AGENTS/WALTER/routed"
        log.mkdir(parents=True)
        (log / "delivery_log.tsv").write_text(
            "timestamp_routed\tsignal_id\trecipient\trole\trecipient_platform\tprecedence\thandoff_path\twritten_state\tnotes\n"
            "2026-11-09T03:30:00Z\tSIG-W-20261109-001\tALPHA\taction\tX\tROUTINE\tAGENTS/ALPHA/inbox/WALTER/SIG-W-20261109-001.md\tdelivered\tn\n"
            "not-a-time\tS\tALPHA\tINFO\tX\tR\tAGENTS/ALPHA/inbox/WALTER/bad.md\tdelivered\tn\n"
            "short\trow\n", encoding="utf-8")
        got = ic.load_delivery(t.root)
        self.assertEqual(got, {"AGENTS/ALPHA/inbox/WALTER/SIG-W-20261109-001.md": (dt.date(2026, 11, 8), "ACTION")})  # 03:30Z is 11/8 ET


if __name__ == "__main__":
    unittest.main()
