"""Acceptance cases for tools/dispatch_card.py (Will 2026-11-16 19:21 ET). Every case runs in a temporary
repository root: no card, handoff or log row is ever written to the real BOARD or any desk."""
import contextlib, io, json, tempfile, unittest
from pathlib import Path
import dispatch_card as d

DESKS = ["CYPHER", "GIBBS", "CARL", "RED", "TERRY", "HENRY", "VIOLET", "CATO"]


def card(n=1, **kw):
    c = dict(id=f"SIG-W-20991231-{n:03d}", slug=f"fixture card {n} $2.6B loan", title=f"Fixture {n}: loan of $2.6B",
             body="**What.** A $1.5 billion facility at S+550; $0 position action.\n\nSecond paragraph.",
             source="test", origin=["test"], action=["CYPHER"], info=["GIBBS"], precedence="ROUTINE",
             signal_type="context", confidence=0.5, confidence_language="test", cluster="MISC", domain="TEST",
             entities=["X"], dispatch_note="test", route_origin="test", route_summary="test $0.8B")
    c.update(kw)
    return c


class Dispatch(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for x in DESKS:
            (self.root / "AGENTS" / x).mkdir(parents=True)
        (self.root / "AGENTS" / "WALTER" / "routed").mkdir(parents=True)
        (self.root / "BOARD").mkdir()
        (self.root / "PROME" / "inbox").mkdir(parents=True)
        for f in ("route_log.tsv", "delivery_log.tsv"):
            (self.root / "AGENTS" / "WALTER" / "routed" / f).write_text("header\n")

    def tearDown(self):
        self.tmp.cleanup()

    def run_cards(self, cards, *extra):
        p = self.root / "cards.json"
        p.write_text(json.dumps(cards))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = d.main([str(p), "--root", str(self.root), *extra])
        return rc, out.getvalue()

    def files(self):
        return sorted(str(x.relative_to(self.root)) for x in self.root.rglob("*") if x.is_file() and x.name != "cards.json")

    def rows(self, name):
        return (self.root / "AGENTS/WALTER/routed" / name).read_text().splitlines()[1:]

    def test_D1_card_handoffs_rows_and_bodies(self):
        rc, out = self.run_cards([card()])
        self.assertEqual(rc, 0, out)
        board = list((self.root / "BOARD").glob("SIG-W-20991231-001-*.md"))
        self.assertEqual(len(board), 1)
        text = board[0].read_text()
        self.assertIn("$1.5 billion", text)
        self.assertIn("$0 position action", text)
        for desk in ("CYPHER", "GIBBS"):
            h = (self.root / f"AGENTS/{desk}/inbox/WALTER/SIG-W-20991231-001.md").read_text()
            self.assertIn("Second paragraph.", h)
            self.assertIn("$1.5 billion", h)
        self.assertEqual(len(self.rows("delivery_log.tsv")), 2)
        self.assertEqual(len(self.rows("route_log.tsv")), 1)
        self.assertTrue(all(len(r.split("\t")) == 9 for r in self.rows("delivery_log.tsv")))

    def test_D2_pull_complete_and_board_only_rules_preserved(self):
        rc, out = self.run_cards([card(action=["RED", "TERRY"], info=["CARL", "PROME", "GIBBS"])])
        self.assertEqual(rc, 0, out)
        got = {r.split("\t")[2] + ":" + r.split("\t")[3] for r in self.rows("delivery_log.tsv")}
        self.assertEqual(got, {"RED:ACTION", "GIBBS:INFO"})
        self.assertFalse((self.root / "AGENTS/CARL/inbox").exists())
        self.assertFalse((self.root / "AGENTS/TERRY/inbox").exists())
        self.assertEqual(list((self.root / "PROME/inbox").iterdir()), [])

    def test_D3_prome_action_gets_a_packet_and_row(self):
        rc, out = self.run_cards([card(action=["PROME"], info=["VIOLET", "HENRY"])])
        self.assertEqual(rc, 0, out)
        pk = self.root / "PROME/inbox/2099-12-31_from-WALTER_SIG-W-20991231-001.md"
        self.assertIn("Role: ACTION", pk.read_text())
        prow = [r for r in self.rows("delivery_log.tsv") if r.split("\t")[2] == "PROME"]
        self.assertEqual(len(prow), 1)
        self.assertIn("board_scan rc 1 expected", prow[0])

    def test_D4_cato_refused_on_either_line_and_nothing_written(self):
        before = self.files()
        for kw in (dict(action=["CATO"]), dict(info=["GIBBS", "CATO"])):
            rc, out = self.run_cards([card(**kw)])
            self.assertEqual(rc, 2)
            self.assertIn("CATO", out)
            self.assertIn("never routed", out)
            self.assertEqual(self.files(), before)

    def test_D5_missing_body_refused(self):
        before = self.files()
        for body in ("", "   \n", "# Heading only\n\n## another"):
            rc, out = self.run_cards([card(body=body)])
            self.assertEqual(rc, 2, body)
            self.assertIn("body is empty", out)
        self.assertEqual(self.files(), before)

    def test_D6_shell_damaged_dollar_text_refused(self):
        before = self.files()
        for kw in (dict(body="Raised .8B in notes."), dict(title="Loss of .5 billion"),
                   dict(body="price /bin/bash per share"), dict(route_summary="cut .25B")):
            rc, out = self.run_cards([card(**kw)])
            self.assertEqual(rc, 2, kw)
            self.assertIn("shell", out)
        self.assertEqual(self.files(), before)
        for ok in ("Raised $0.8B and 0.8B and 1.5 billion; $.", "S&P down 1.92%, VIX 23.02"):
            rc, out = self.run_cards([card(n=9, body=ok)], "--check")
            self.assertEqual(rc, 0, (ok, out))

    def test_D7_terry_info_unknown_desk_duplicate_refused(self):
        for kw in (dict(info=["TERRY"]), dict(action=["NOSUCHDESK"]), dict(action=["GIBBS"], info=["GIBBS"])):
            rc, _ = self.run_cards([card(**kw)])
            self.assertEqual(rc, 2, kw)

    def test_D8_one_bad_card_blocks_the_whole_batch(self):
        before = self.files()
        rc, out = self.run_cards([card(1), card(2, action=["CATO"])])
        self.assertEqual(rc, 2)
        self.assertEqual(self.files(), before)

    def test_D9_existing_card_or_handoff_refused(self):
        self.assertEqual(self.run_cards([card()])[0], 0)
        rc, out = self.run_cards([card(slug="other slug")])
        self.assertEqual(rc, 2)
        self.assertIn("already exists", out)

    def test_D10_check_mode_writes_nothing(self):
        before = self.files()
        rc, out = self.run_cards([card()], "--check")
        self.assertEqual(rc, 0, out)
        self.assertEqual(self.files(), before)

    def test_D11_post_write_body_check_catches_a_header_only_handoff(self):
        orig = d.Path.write_text

        def truncating(self, text, *a, **k):
            if "/inbox/" in str(self):
                text = text.split("\n\n", 1)[0] + "\n\n"
            return orig(self, text, *a, **k)
        with unittest.mock.patch.object(d.Path, "write_text", truncating):
            with self.assertRaises(RuntimeError):
                self.run_cards([card()])

    # D12 to D15: weekday refusal (PROME packet 2026-11-17 20:42 ET, WQ-713; live case SIG-W-20261117-014)
    def test_D12_wrong_weekday_refused_nothing_written(self):
        before = self.files()
        rc, out = self.run_cards([card(id="SIG-W-20261117-001", body="Published Thu 11/13; no card until today.")])
        self.assertEqual(rc, 2, out)
        self.assertIn("weekday mismatch", out)
        self.assertIn("Friday", out)
        self.assertEqual(self.files(), before)

    def test_D13_right_weekday_passes(self):
        rc, out = self.run_cards([card(id="SIG-W-20261117-001", title="Fed report Fri 11/13",
                                       body="Published Fri 2026-11-13; card Tue 11/17.")], "--check")
        self.assertEqual(rc, 0, out)

    def test_D14_override_with_reason_writes_and_records_it(self):
        reason = "quoted from the source's own mislabel, kept verbatim"
        rc, out = self.run_cards([card(id="SIG-W-20261117-001", body="The release said Thu 11/13.",
                                       weekday_override=reason)])
        self.assertEqual(rc, 0, out)
        self.assertIn("WEEKDAY OVERRIDDEN", out)
        text = next((self.root / "BOARD").glob("SIG-W-20261117-001-*.md")).read_text()
        self.assertIn(f'weekday_override: "{reason}"', text)

    def test_D15_override_without_a_reason_is_refused(self):
        rc, out = self.run_cards([card(id="SIG-W-20261117-001", body="Due Thu 11/13.", weekday_override="ok")])
        self.assertEqual(rc, 2, out)
        self.assertIn("weekday mismatch", out)


    def test_D16_doorbell_prompt_lists_action_without_a_row_and_never_refuses(self):
        reg = self.root / "AGENTS/WALTER/registry"
        reg.mkdir(parents=True)
        (reg / "DOORBELL_LOG.tsv").write_text(
            "# header\ndate\tdesk\tsig_id\treferent\n2099-12-31\tHENRY\tSIG-W-20991231-001\tNONE\n")
        for mode in (["--check"], []):
            rc, out = self.run_cards([card(action=["CYPHER", "HENRY"], info=["GIBBS"])], *mode)
            self.assertEqual(rc, 0, out)
            self.assertIn("DOORBELL PROMPT: 1 ACTION", out)
            self.assertIn("\tCYPHER\tSIG-W-20991231-001\t", out)
            self.assertNotIn("\tHENRY\t", out)   # has a row
            self.assertNotIn("\tGIBBS\t", out)   # INFO only

    def test_D17_doorbell_prompt_missing_log_says_unknown(self):
        rc, out = self.run_cards([card()], "--check")
        self.assertEqual(rc, 0, out)
        self.assertIn("rows for this batch are UNKNOWN", out)

import unittest.mock  # noqa: E402

if __name__ == "__main__":
    unittest.main()
