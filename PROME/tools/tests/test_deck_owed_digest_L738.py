"""L738 / WQ-446 A — the Deck OWED view republishes only when the owed set changed (fixture-only; never the live tree).
Acceptance: ACCEPTANCE_L738_deck_owed_digest.md (A1 · A2 · A2b · A3 · A4 · A4b · A4c · A5 · A8 · A9 collision + the guard falsified)."""
import datetime
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import decision_deck as D  # noqa: E402

HDR = "| # | Item | Type | Needed by | Open since | PROME rec | Notes |\n|---|---|---|---|---|---|---|\n"
ROW_A = "| 1 | Ordinary ask | RULE | 2026-10-20 | 10/15 | Rec A | note a |\n"
ROW_B = "| 2 | APPROVED hands owed | ACTION | 2026-10-21 | 10/15 | Complete hands | answered, hands owed |\n"
ROW_C = "| 3 | Blocked ask | RULE | | 10/15 | Wait | ⛔ waits: OTHER |\n"
DONE = "## RECENTLY DONE\n| 9 Historical | 2026-10-14 | ruling kept |\n"
EXPL_HDR = "wq\tname\twhat\twhy_yours\tif_yes\tif_no\tif_nothing\trec_reason\toptions\toptions_source\n"


def expl_row(n, what="what"):
    return f"{n}\tname{n}\t{what}\twhy\tyes\tno\tnothing\treason\t\t\n"


class OwedDigest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.email=t@t", "-c", "user.name=t",
                        "commit", "-q", "--allow-empty", "-m", "x"], check=True)
        paths = {k: self.root / k for k in ("Q", "AD", "DOCKET", "EXPL", "LEDGER")}
        self.addCleanup(patch.stopall)
        patch.multiple(D, ROOT=self.root, ARCH=[], HOSTED_REFERENCE_STATE=self.root / "ref_hosted.json", **paths).start()
        self.write_queue(ROW_A + ROW_B + ROW_C)
        D.EXPL.write_text(EXPL_HDR + expl_row(1) + expl_row(2) + expl_row(3), encoding="utf-8")
        D.AD.write_text("## Live Decision Index\n| Decision | State | Owner | Next | Backstop | Source |\n|---|---|---|---|---|---|\n", encoding="utf-8")
        D.DOCKET.write_text("2026-10-20\tWill catalyst\tWill\tPENDING\tartifact\n", encoding="utf-8")
        D.LEDGER.write_text("", encoding="utf-8")
        D.HOSTED_REFERENCE_STATE.write_text('{"built": "2026-09-26 16:03", "version": "v12"}', encoding="utf-8")
        self.out = self.root / "deck.html"

    def hosted_build(self, day=D.dt.date(2026, 10, 15)):
        return D.build(day, self.out, owed_url=D.OWED_ARTIFACT_URL, reference_url="https://claude.ai/artifact/RefRefRefRefRefRefRef1")

    def write_queue(self, rows):
        D.Q.write_text("## OPEN\n" + HDR + rows + DONE, encoding="utf-8")

    def current(self):
        return D.owed_fingerprints(D.parse_open(D.Q.read_text(encoding="utf-8")), D.load_explainers())

    # A1 — two renders of the same sources ⇒ same digest; the build receipt is the RENDER record
    def test_a1_same_sources_same_digest_and_receipt_written(self):
        r1 = D.build(D.dt.date(2026, 10, 15), self.out)
        rec1 = json.loads(D._owed_build_path().read_text(encoding="utf-8"))
        r2 = D.build(D.dt.date(2026, 10, 15), self.out)
        rec2 = json.loads(D._owed_build_path().read_text(encoding="utf-8"))
        self.assertEqual(r1["owed_digest"], r2["owed_digest"])
        self.assertEqual(rec1["digest"], rec2["digest"])
        self.assertEqual(rec1["fingerprints"], rec2["fingerprints"])
        self.assertEqual(set(rec1["fingerprints"]), {"1", "2", "3"})
        self.assertEqual(rec1["build_id"], r1["build_id"])
        self.assertFalse(D._owed_hosted_path().exists(), "a render never writes the hosted record")
        emb = D.page_receipt(self.out)
        self.assertEqual((emb["fingerprints"], emb["digest"], emb["build_id"]), (rec1["fingerprints"], rec1["digest"], rec1["build_id"]))

    # A2 — four edits, four different digests, each named correctly by the gate line
    def test_a2_four_edits_four_digests_named(self):
        base = self.current()
        hosted = self.root / "h.json"
        self._host(base, hosted, "v1")
        digests = {D.owed_digest(base)}
        # changed notes cell
        self.write_queue(ROW_A.replace("note a", "note a2") + ROW_B + ROW_C)
        fps = self.current(); digests.add(D.owed_digest(fps))
        self.assertEqual(D.republish_verdict(fps, hosted), ("OWED", "OWED — since v1 (t): ~1"))
        # changed explainer `what` cell
        self.write_queue(ROW_A + ROW_B + ROW_C)
        D.EXPL.write_text(EXPL_HDR + expl_row(1, "what2") + expl_row(2) + expl_row(3), encoding="utf-8")
        fps = self.current(); digests.add(D.owed_digest(fps))
        self.assertEqual(D.republish_verdict(fps, hosted), ("OWED", "OWED — since v1 (t): ~1"))
        D.EXPL.write_text(EXPL_HDR + expl_row(1) + expl_row(2) + expl_row(3) + expl_row(4), encoding="utf-8")
        # added row
        self.write_queue(ROW_A + ROW_B + ROW_C + "| 4 | New ask | RULE | 2026-10-22 | 10/15 | Rec | n |\n")
        fps = self.current(); digests.add(D.owed_digest(fps))
        self.assertEqual(D.republish_verdict(fps, hosted), ("OWED", "OWED — since v1 (t): +4"))
        # a row ruled out of OPEN
        self.write_queue(ROW_A + ROW_C)
        fps = self.current(); digests.add(D.owed_digest(fps))
        self.assertEqual(D.republish_verdict(fps, hosted), ("OWED", "OWED — since v1 (t): −2"))
        self.assertEqual(len(digests), 5)

    # A2b (Will) — {a,b,c} hosted vs {a,b′,d} current ⇒ exactly "−c +d ~b"; an aggregate digest alone is not a record
    def test_a2b_row_differences_are_real(self):
        hosted = {"a": "fa", "b": "fb", "c": "fc"}
        current = {"a": "fa", "b": "fb2", "d": "fd"}
        self.assertEqual(D.owed_diff(hosted, current), (["d"], ["c"], ["b"]))
        hp = self.root / "h.json"
        hp.write_text(json.dumps({"fingerprints": hosted, "version": "v7", "published_at": "t", "extras": {}}), encoding="utf-8")
        self.assertEqual(D.republish_verdict(current, hp), ("OWED", "OWED — since v7 (t): −c +d ~b"))
        hp.write_text(json.dumps({"fingerprints": hosted, "version": "v7", "published_at": "t"}), encoding="utf-8")
        self.assertEqual(D.republish_verdict(current, hp)[0], "UNKNOWN", "a record without extras is malformed (pre-read-1 shape never shipped)")
        hp.write_text(json.dumps({"digest": D.owed_digest(hosted), "version": "v7", "published_at": "t"}), encoding="utf-8")
        self.assertEqual(D.republish_verdict(current, hp)[0], "UNKNOWN", "a digest without the per-row map is not a record")

    # A3 🔴 overlap — answered rows count; RECENTLY DONE and closed-in-place rows never do (parse_open decides)
    def test_a3_membership_is_the_pages_rule(self):
        fps = self.current()
        self.assertIn("2", fps, "an ANSWERED (hands-owed) row is rendered, so it is in the set")
        self.assertNotIn("9", fps, "a RECENTLY DONE row is not")
        self.write_queue(ROW_A + ROW_B + ROW_C + "| 5 | ✅ DONE closed in place | RULE | 2026-10-20 | 10/15 | - | - |\n")
        self.assertNotIn("5", self.current(), "a closed-in-place row is skipped by parse_open, so it never counts")

    # A4 — no hosted record ⇒ UNKNOWN ⇒ republish; unreadable too
    def test_a4_missing_or_unreadable_record_is_unknown(self):
        fps = self.current()
        state, line = D.republish_verdict(fps, self.root / "absent.json")
        self.assertEqual(state, "UNKNOWN"); self.assertIn("republish", line)
        bad = self.root / "bad.json"; bad.write_text("{not json", encoding="utf-8")
        self.assertEqual(D.republish_verdict(fps, bad)[0], "UNKNOWN")
        bad.write_text(json.dumps({"fingerprints": "notadict", "version": "v1", "published_at": "t", "extras": {}}), encoding="utf-8")
        self.assertEqual(D.republish_verdict(fps, bad)[0], "UNKNOWN")
        bad.write_text(json.dumps({"fingerprints": {}, "version": "v1", "published_at": "t", "extras": "no"}), encoding="utf-8")
        self.assertEqual(D.republish_verdict(fps, bad)[0], "UNKNOWN")

    # A4b (Will) — build A, queue moves to B, publish A: the hosted record carries A (from the receipt); the gate names B's rows
    def test_a4b_record_copies_the_build_receipt_not_the_queue(self):
        ra = self.hosted_build()
        fps_a = self.current()
        self.write_queue(ROW_A.replace("note a", "note b") + ROW_B + ROW_C)      # the queue moves to B after the render
        fps_b = self.current()
        self.assertNotEqual(fps_a["1"], fps_b["1"])
        page_a = self.root / "published-A.html"; page_a.write_bytes(self.out.read_bytes())   # the copy that was published
        self.hosted_build()                                                          # B rendered over the same -o path
        rc, msg = D.record_hosted_owed("v100", page_a)                               # A's page was published
        self.assertEqual(rc, 0, msg)
        hosted = json.loads(D._owed_hosted_path().read_text(encoding="utf-8"))
        self.assertEqual(hosted["fingerprints"], fps_a, "the record describes the page that reached the host, not the latest render")
        self.assertEqual(hosted["page_sha256"], __import__("hashlib").sha256(page_a.read_bytes()).hexdigest())
        self.assertEqual(hosted["version"], "v100"); self.assertEqual(hosted["build_id"], ra["build_id"])
        self.assertEqual(D.republish_verdict(fps_b), ("OWED", f"OWED — since v100 ({hosted['published_at']}): ~1"))
        self.assertEqual(D.republish_verdict(fps_a)[0], "NO-OP")

    # A4c (Will) — a failed publish preserves the previous record; a build-id mismatch refuses and writes nothing
    def test_a4c_failed_publish_preserves_record_and_mismatch_refuses(self):
        ra = self.hosted_build()
        self.assertEqual(D.record_hosted_owed("v1", self.out)[0], 0)
        before = D._owed_hosted_path().read_bytes()
        self.write_queue(ROW_A.replace("note a", "note c") + ROW_B + ROW_C)
        self.hosted_build()                                                          # a new render; its publish FAILS
        self.assertEqual(D._owed_hosted_path().read_bytes(), before, "a render alone never touches the hosted record")
        bare = self.root / "bare.html"; bare.write_text('<html><body data-build="x">no receipt</body></html>', encoding="utf-8")
        rc, msg = D.record_hosted_owed("v2", bare)                                   # a page without its receipt ⇒ refuse
        self.assertEqual(rc, 2); self.assertIn("embedded owed receipt", msg)
        self.assertEqual(D._owed_hosted_path().read_bytes(), before)
        rc, msg = D.record_hosted_owed("", self.out)                                 # empty version ⇒ refuse
        self.assertEqual(rc, 2)
        tam = self.root / "tampered.html"
        tam.write_text(self.out.read_text(encoding="utf-8").replace('"digest": "', '"digest": "0'), encoding="utf-8")
        rc, msg = D.record_hosted_owed("v2", tam)                                    # a receipt that does not match itself ⇒ refuse
        self.assertEqual(rc, 2); self.assertIn("does not match", msg)
        rc, msg = D.record_hosted_owed("v2", self.root / "absent.html")             # no file ⇒ refuse
        self.assertEqual(rc, 2)
        self.assertEqual(D._owed_hosted_path().read_bytes(), before)

    # A5 wrong owner — the reference record and its note are untouched by every L738 write
    def test_a5_reference_record_untouched(self):
        ref_before = D.HOSTED_REFERENCE_STATE.read_bytes()
        self.hosted_build()
        D.record_hosted_owed("v1", self.out)
        self.assertEqual(D.HOSTED_REFERENCE_STATE.read_bytes(), ref_before)
        self.assertIn("hosted build 2026-09-26 16:03 (v12)", self.out.read_text(encoding="utf-8"))

    # A8 — existing contract: every pre-L738 return key survives; the blank-deck refusal is unchanged
    def test_a8_build_contract_kept(self):
        r = D.build(D.dt.date(2026, 10, 15), self.out)
        for k in ("owed", "actionable", "answered_hands", "decided", "active", "docket", "explainers_missing",
                  "options_rows", "options_warnings", "done_rows_skipped", "bytes", "out", "reference_out", "reference_bytes", "link_mode"):
            self.assertIn(k, r)
        D.Q.write_text("## OPEN\n| # | Item | Type | Needed by |\n|---|---|---|---|\n| 1 | x | RULE | 2026-10-20 |\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            D.build(D.dt.date(2026, 10, 15), self.out)

    # the guard falsified — the fingerprint ignores exactly what it must and nothing else
    def test_guard_fingerprint_excludes_stamp_includes_every_cell(self):
        rows = D.parse_open(D.Q.read_text(encoding="utf-8")); expl = D.load_explainers()
        base = D.owed_fingerprints(rows, expl)
        for cell in D.OWED_ROW_CELLS:
            if cell == "n":
                continue
            mutated = [dict(r, **{cell: r[cell] + "x"}) if r["n"] == "1" else r for r in rows]
            self.assertNotEqual(D.owed_fingerprints(mutated, expl)["1"], base["1"], f"cell {cell} must be in the fingerprint")
        derived = [dict(r, name="other", blocked=not r["blocked"]) if r["n"] == "1" else r for r in rows]
        self.assertEqual(D.owed_fingerprints(derived, expl)["1"], base["1"], "derived fields are not in the set")
        self.assertEqual(D.owed_fingerprints(rows, {})["1"] != base["1"], True, "a missing explainer row changes the fingerprint")

    # read 1 ❌2 / ⚠️10 — a renderer change or a reference-note change reads OWED even with the owed set unchanged
    def test_r1_extras_renderer_and_reference_note_trigger_owed(self):
        self.hosted_build()
        self.assertEqual(D.record_hosted_owed("v1", self.out)[0], 0)
        fps = self.current()
        self.assertEqual(D.republish_verdict(fps, extras=D.current_extras())[0], "NO-OP")
        ex = dict(D.current_extras(), renderer="deadbeef")
        self.assertEqual(D.republish_verdict(fps, extras=ex), ("OWED", f"OWED — since v1 ({json.loads(D._owed_hosted_path().read_text())['published_at']}): renderer changed"))
        D.HOSTED_REFERENCE_STATE.write_text('{"built": "2026-10-20 10:00", "version": "v13"}', encoding="utf-8")
        state, line = D.republish_verdict(fps, extras=D.current_extras())
        self.assertEqual(state, "OWED"); self.assertTrue(line.endswith("reference note changed"), line)
        self.assertEqual(D.republish_verdict(fps, extras=None)[0], "NO-OP", "extras=None compares the owed set only (legacy callers)")

    # read 1 ⚠️6 — the build id is read FROM THE PUBLISHED FILE, never retyped; a different page refuses
    def test_r1_page_build_id_read_from_file(self):
        ra = self.hosted_build()
        self.assertEqual(D.page_build_id(self.out), ra["build_id"])
        self.assertEqual(D.page_receipt(self.out)["build_id"], ra["build_id"])
        self.assertIsNone(D.page_build_id(self.root / "ref_hosted.json"))
        # the embedded block survives the host's wrapper (a downloaded copy is wrapped in a skeleton) and `</` inside JSON cannot end it
        wrapped = self.root / "downloaded.html"
        wrapped.write_text("<!doctype html><html><body>\n" + self.out.read_text(encoding="utf-8") + "\n</body></html>", encoding="utf-8")
        self.assertEqual(D.page_receipt(wrapped)["digest"], D.page_receipt(self.out)["digest"])
        self.assertEqual(D.record_hosted_owed("v1", wrapped)[0], 0)
        # a cell containing "</script>" cannot close the embedded block early (the JSON escapes "</")
        self.write_queue(ROW_A.replace("note a", "note </script><b>x") + ROW_B + ROW_C)
        self.hosted_build()
        self.assertEqual(self.out.read_text(encoding="utf-8").count('id="deck-owed-receipt">'), 1)
        self.assertEqual(D.page_receipt(self.out)["fingerprints"], self.current())

    # read 1 ❌1 — countdown pills carry their inputs and the page script recomputes them; pin marks follow data-due
    def test_r1_pills_carry_inputs_and_script_recomputes(self):
        D.build(D.dt.date(2026, 10, 15), self.out)
        page = self.out.read_text(encoding="utf-8")
        self.assertIn('data-by="2026-10-20"', page)
        self.assertRegex(page, r'<span class="pill ok" data-by="2026-10-20" data-ck="">5d left · 2026-10-20</span>')
        self.assertIn("function refreshPills()", page); self.assertIn("refreshPills();", page)
        self.assertIn('class="pill pin" title="Due, clocked or money-moving: visible under every filter" hidden>PINNED', page,
                      "an unpinned card still carries a hidden PINNED mark for the script to reveal")
        self.assertEqual(D.due_pill("2026-10-20", -3, False), '<span class="pill crit" data-by="2026-10-20" data-ck="">overdue 3d · 2026-10-20</span>')
        self.assertNotIn("data-by", D.due_pill(None, None, False)); self.assertNotIn("data-by", D.due_pill("2026-10-20", 1, True, "OTHER"))

    # read 1 ⚠️12 — the gate check itself, wired: UNKNOWN / NO-OP / OWED / incoherent queue ⇒ UNKNOWN
    def test_r1_gate_check_wiring(self):
        import prome_gate as G
        # WQ-460: exercise the preserved active branch only inside this fixture.
        patch.object(G, "DECISION_DECK_PAUSED", False).start()
        patch.object(G, "ROOT", self.root).start()
        (self.root / "PROME").mkdir(exist_ok=True)
        (self.root / "PROME/WILL_QUEUE.md").write_text(D.Q.read_text(encoding="utf-8"), encoding="utf-8")
        def run():
            G.results.clear(); G.check_deck_republish(); return G.results[-1]
        sev, name, ok, detail, owner = run()
        self.assertEqual((sev, ok, detail[:7]), (G.ADVISE, False, "UNKNOWN"))
        self.hosted_build(); D.record_hosted_owed("v1", self.out)
        sev, name, ok, detail, owner = run()
        self.assertEqual((ok, detail[:5]), (True, "NO-OP"))
        D.Q.write_text(D.Q.read_text(encoding="utf-8").replace("note a", "note z"), encoding="utf-8")
        (self.root / "PROME/WILL_QUEUE.md").write_text(D.Q.read_text(encoding="utf-8"), encoding="utf-8")
        sev, name, ok, detail, owner = run()
        self.assertEqual((ok, detail[:4]), (False, "OWED")); self.assertIn("~1", detail)
        (self.root / "PROME/WILL_QUEUE.md").write_text("## OPEN\n| # | Item | Type | Needed by |\n|---|---|---|---|\n| 1 | x | RULE | 2026-10-20 |\n", encoding="utf-8")
        sev, name, ok, detail, owner = run()
        self.assertEqual((ok, detail[:7]), (False, "UNKNOWN")); self.assertIn("0 rows", detail)

    # read 2 ⚠️5 — a LOCAL-link build (relative Reference href) is refused by the record command
    def test_r2_local_link_build_is_never_recorded_as_hosted(self):
        rl = D.build(D.dt.date(2026, 10, 15), self.out)
        self.assertEqual(json.loads(D._owed_build_path().read_text())["link_mode"], "local")
        rc, msg = D.record_hosted_owed("v1", self.out)
        self.assertEqual(rc, 2); self.assertIn("LOCAL-link", msg); self.assertFalse(D._owed_hosted_path().exists())
        self.hosted_build()
        self.assertEqual(json.loads(D._owed_build_path().read_text())["link_mode"], "hosted")
        self.assertEqual(D.page_receipt(self.out)["link_mode"], "hosted")
        self.assertEqual(D.record_hosted_owed("v1", self.out)[0], 0)

    # A9 — CATO's SP6 collision (AGENTS/CATO/runs/2026-10-15_2025_prome-simplification-l738-collision-probe.py, ported as a
    # regression case; Will 2026-10-16 00:44 ET): build A, save A's page, change the queue, build B within the SAME MINUTE
    # (same HEAD, same build id); record A as published ⇒ the record must be A (never B's), and current B must read OWED.
    def test_a9_same_minute_collision_records_the_published_page(self):
        real = datetime.datetime
        class Frozen(real):
            @classmethod
            def now(cls, tz=None):
                v = cls(2026, 10, 16, 4, 30, 10, tzinfo=datetime.timezone.utc)
                return v.astimezone(tz) if tz else v.replace(tzinfo=None)
        with patch.object(D.dt, "datetime", Frozen):
            a = self.hosted_build(); fps_a = self.current()
            page_a = self.root / "published-A.html"; page_a.write_bytes(self.out.read_bytes())
            self.write_queue(ROW_A.replace("note a", "note B NOT HOSTED") + ROW_B + ROW_C)
            b = self.hosted_build(); fps_b = self.current()
            self.assertNotEqual(fps_a, fps_b); self.assertEqual(a["build_id"], b["build_id"], "the collision CATO reproduced")
            rc, msg = D.record_hosted_owed("v-A", page_a)
            self.assertEqual(rc, 0, msg)
            hosted = json.loads(D._owed_hosted_path().read_text(encoding="utf-8"))
            self.assertEqual(hosted["fingerprints"], fps_a, "A was published, A is recorded")
            self.assertNotEqual(hosted["fingerprints"], fps_b, "B's receipt never masquerades as A's")
            state, line = D.republish_verdict(fps_b, extras=D.current_extras())
            self.assertEqual((state, line.endswith("~1")), ("OWED", True), line)
            # and the other way: B's page published ⇒ NO-OP for current B
            self.assertEqual(D.record_hosted_owed("v-B", self.out)[0], 0)
            self.assertEqual(D.republish_verdict(fps_b, extras=D.current_extras())[0], "NO-OP")

    def _host(self, fps, path, version):
        path.write_text(json.dumps({"fingerprints": fps, "version": version, "published_at": "t", "extras": {}}), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
