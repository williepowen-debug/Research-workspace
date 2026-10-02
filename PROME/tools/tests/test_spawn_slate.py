"""spawn_slate.py — the prepared spawn SLATE.

Acceptance conditions (written before the tool): PROME/tools/tests/ACCEPTANCE_spawn_slate_2026-10-02.md
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_spawn_slate.py
Throwaway repo only — nothing here reads the live tree. Condition numbers in the test names are the
acceptance file's.
"""
import argparse, datetime as dt, os, pathlib, re, subprocess, sys, tempfile, unittest

REAL = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REAL / "PROME" / "tools"))
import spawn_list as S            # noqa: E402
import spawn_slate as SS          # noqa: E402

TODAY = "2026-03-10"              # a Tuesday
GATES_HDR = "gate_id\tregistered\towner\tcondition\tconsequence_on_fire\tstate\tlast_checked\tsource\tconsumed_by\tscannable\tdefinition_surface\treview_by"
ROSTER = ("## ACTIVE (9)\n| Agent | Does |\n|---|---|\n" + "".join(f"| {d} | x |\n" for d in
          ("ALPHA", "BETA", "GAMMA", "DELTA", "WAL", "WALTER", "EPS", "ZETA", "ETA", "THETA", "IOTA", "KAPPA", "LAMBDA", "MUON", "NUON", "OMEGA")) +
          "## DORMANT (1)\n| Agent | Does |\n|---|---|\n| OLDIE | x |\n## DESK CADENCE\n| Agent | Cadence | x |\n|---|---|---|\n| ALPHA | WEEKLY | - |\n\n## NEXT\n")


def _git(repo, *a, date=None):
    env = dict(os.environ)
    if date:
        env["GIT_AUTHOR_DATE"] = env["GIT_COMMITTER_DATE"] = f"{date}T12:00:00"
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, check=True, env=env)


def _commit(repo, subject, files, date, body=""):
    for p, text in files.items():
        f = repo / p; f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text, encoding="utf-8")
        _git(repo, "add", "--", p)
    _git(repo, "commit", "-q", "--allow-empty", "-m", subject + ("\n\n" + body if body else ""), date=date)
    return _git(repo, "rev-parse", "--short", "HEAD").stdout.strip()


def _row(date, desc, owner, state="PENDING — registered", source="", notes=""):
    return "\t".join((date, desc, owner, state, source, notes))


class Fixture(unittest.TestCase):
    """DOCKET lines (physical line = key):
    L1 comment · L2 ALPHA dark · L3 BETA answered by commit · L4 GAMMA hedged · L5 DELTA no evidence ·
    L6 PROME · L7 Will · L8 unparseable owner · L9 WAL (WALTER packet must not count) · L10 EPS dark + L11 EPS active ·
    L12 ZETA answered by packet (inbox+processed) · L13 ETA touched a cited file · L14 OLDIE dormant dark ·
    L15 THETA: PROME cites it, the desk does not · L16 IOTA clean then hedged (newest decides) · L17 ALPHA lands +5d ·
    L18 KAPPA: owner packet cites ANOTHER row · L19 LAMBDA: id in a commit BODY only (weak) ·
    L20 MUON: hedged strong return, then a later clean body mention."""
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        r = cls.repo = pathlib.Path(cls.tmp.name)
        _git(r, "init", "-q", "-b", "master"); _git(r, "config", "user.email", "t@t"); _git(r, "config", "user.name", "t")
        long_desc = "ALPHA grades the print " + " ".join(f"w{i}" for i in range(150)) + ". ⛔ Never grade before the release is public. Wake after 15:30 ET. Tail."
        docket = "\n".join([
            "# header",
            _row(TODAY, long_desc, "ALPHA (grader) / BETA (consumer)", notes="Done when ALPHA's ledger carries the grade and PROME holds the sha."),
            _row(TODAY, "BETA re-reads ALP-07 and BET-03 after the auction", "BETA"),
            _row(TODAY, "GAMMA verifies publication then grades GAM-11", "GAMMA"),
            _row(TODAY, "DELTA weekly wake", "DELTA"),
            _row(TODAY, "PROME does a thing", "PROME"),
            _row(TODAY, "Will decides a thing", "Will"),
            _row(TODAY, "nobody owns this", "(tbd)"),
            _row(TODAY, "WAL deck read", "WAL"),
            _row(TODAY, "EPS second row due today", "EPS"),
            _row("2026-03-05..2026-03-09", "EPS windowed row", "EPS"),
            _row(TODAY, "ZETA encodes WQ-900", "ZETA"),
            _row(TODAY, "ETA refreshes the ledger", "ETA", source="AGENTS/ETA/workbook/KB.tsv"),
            _row(TODAY, "OLDIE dormant row", "OLDIE"),
            _row(TODAY, "THETA grades the thing", "THETA"),
            _row(TODAY, "IOTA grades IOT-02", "IOTA"),
            _row("2026-03-15", "ALPHA later row", "ALPHA"),
            _row(TODAY, "KAPPA grades KAP-01", "KAPPA"),
            _row(TODAY, "LAMBDA grades LAM-04", "LAMBDA"),
            _row(TODAY, "MUON grades MUO-09", "MUON"),
            _row("2026-03-05..2026-03-10", "NUON grades NUO-01 at the window's end", "NUON/BETA", state="PENDING — annotated 2026-03-07 by PROME: plan seen"),
            _row("2026-03-14", "OMEGA later row", "OMEGA"),
        ]) + "\n"
        orch = ("date\tdesk\ttier\ttouch\ttrigger\tdrained\tdelivered\n"
                f"{TODAY}\tEPS (eps-1)\t1\t1-SPAWN\tD:L10 second row\t\tIN-FLIGHT\n")
        _commit(r, "PROME: registry", {"PROME/DOCKET.tsv": docket, "PROME/GATES.tsv": GATES_HDR + "\n", "PROME/ROSTER.md": ROSTER,
                                       "PROME/state/ORCH_LOG.tsv": orch}, "2026-03-01")
        for d in ("ALPHA", "OLDIE"):
            _commit(r, f"{d}: old work", {f"AGENTS/{d}/STATUS.md": "x"}, "2026-03-02")
        _commit(r, "NUON: NUO-01 plan registered for the due-scan", {"AGENTS/NUON/STATUS.md": "x"}, "2026-03-06")
        _commit(r, "OMEGA: old work", {"AGENTS/OMEGA/STATUS.md": "x"}, "2026-03-06")
        # git stops a --since walk at the first older commit, so fixture dates must be monotone (real history is)
        _commit(r, "EPS: closeout", {"AGENTS/EPS/STATUS.md": "x"}, "2026-03-06")
        cls.c_beta = _commit(r, "BETA: L3 re-read done, ALP-07 holds", {"AGENTS/BETA/STATUS.md": "x"}, TODAY)
        _commit(r, "GAMMA: GAM-11 not yet out, armed", {"AGENTS/GAMMA/STATUS.md": "x"}, TODAY)
        _commit(r, "DELTA: closeout", {"AGENTS/DELTA/STATUS.md": "x"}, TODAY)
        _commit(r, "WAL closeout", {"AGENTS/WAL/STATUS.md": "x"}, TODAY)
        _commit(r, "WALTER -> PROME: L9 routed", {"PROME/inbox/2026-03-10_from-WALTER_L9-note.md": "about L9"}, TODAY)
        cls.c_zeta = _commit(r, "ZETA -> PROME: encoded", {"AGENTS/ZETA/STATUS.md": "x", "PROME/inbox/2026-03-10_from-ZETA_WQ-900-encoded.md": "WQ-900 ENCODED in the letter."}, TODAY)
        _commit(r, "PROME: ZETA packet -> processed", {"PROME/inbox/processed/2026-03-10_from-ZETA_WQ-900-encoded.md": "WQ-900 ENCODED in the letter."}, TODAY)
        _commit(r, "ETA: ledger refresh", {"AGENTS/ETA/workbook/KB.tsv": "x"}, TODAY)
        _commit(r, "THETA: closeout", {"AGENTS/THETA/STATUS.md": "x"}, TODAY)
        _commit(r, "PROME: annotate", {"PROME/inbox/2026-03-10_from-THETA_fake.md": "L15 graded"}, TODAY, body="THETA: L15 graded")
        _commit(r, "IOTA: IOT-02 graded HIT", {"AGENTS/IOTA/STATUS.md": "a"}, TODAY)
        _commit(r, "IOTA: IOT-02 correction, grade withdrawn, unresolved", {"AGENTS/IOTA/STATUS.md": "b"}, TODAY)
        _commit(r, "KAPPA -> PROME: other", {"AGENTS/KAPPA/STATUS.md": "x", "PROME/inbox/2026-03-10_from-KAPPA_other.md": "L3 looks fine to me"}, TODAY)
        _commit(r, "LAMBDA: closeout", {"AGENTS/LAMBDA/STATUS.md": "x"}, TODAY, body="calendar: LAM-04 sits beside the auction")
        _commit(r, "MUON: MUO-09 not yet out, armed", {"AGENTS/MUON/STATUS.md": "a"}, TODAY)
        _commit(r, "MUON: events calendar", {"AGENTS/MUON/STATUS.md": "b"}, TODAY, body="MUO-09 resolves on the print")
        S.ROOT = r
        cls.args = argparse.Namespace(horizon=0, as_of=TODAY, docket="PROME/DOCKET.tsv", gates="PROME/GATES.tsv",
                                      roster="PROME/ROSTER.md", orch_log="PROME/state/ORCH_LOG.tsv")
        cls.today, cls.rev, cls.body, cls.rc, cls.top, cls.n = SS.compose(cls.args, "stamp")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup(); S.ROOT = REAL

    def stanza(self, desk):
        m = re.search(rf"^### {desk} — .*?(?=^### |^## )", self.body, re.S | re.M)
        self.assertIsNotNone(m, f"no stanza for {desk}")
        return m.group(0)

    # 1 — conservation
    def test_c01_conservation_line_ok_and_every_row_once(self):
        self.assertIn("· OK", self.body); self.assertNotIn("SLATE INCOMPLETE", self.body)
        census = self.body.split("## Mechanical census")[1]
        for n in range(2, 22):
            if n == 17:
                continue                                   # lands +5d: outside horizon 0
            self.assertEqual(len(re.findall(rf"(?m)^(?:⚠️ |⛔ )?D:L{n}\t", census)), 1, f"L{n} census")
        self.assertNotIn("D:L17\t", census)

    def test_c01_prome_will_unowned_have_no_stanza(self):
        for name in ("PROME", "WILL", r"\?"):
            self.assertIsNone(re.search(rf"(?m)^### {name} —", self.body))
        self.assertIn("D:L8 (owner cell unparseable)", self.body)

    # 2 — rc parity
    def test_c02_rc_equals_spawn_list_rc(self):
        self.assertEqual(self.rc, 2)                       # the unparseable owner row is UNKNOWN in spawn_list ⇒ 2

    # 3 — the pre-check is a POINTER (v2, after Reader A failed the verdict classes)
    def test_c03_no_verdict_token_is_ever_printed(self):
        stanzas = self.body.split("## Desk stanzas")[1].split("## Census rows")[0]
        for tok in ("ALREADY ANSWERED", "PARTIAL ANSWER", "NO SPAWN"):
            self.assertNotIn(tok, stanzas)

    def test_c03_return_found_by_commit_key(self):
        s = self.stanza("BETA")
        self.assertIn("**RETURN FOUND**", s); self.assertIn(self.c_beta, s); self.assertIn("READ FIRST", s.split("\n")[0])
        self.assertIn("`AGENTS/BETA/STATUS.md`", s)                    # a commit line names a file, not only a sha
        self.assertNotIn("Bounded assignment", s); self.assertIn("If the read shows a row is still owed", s)

    def test_c03_hint_words_never_change_the_token(self):
        s = self.stanza("GAMMA")
        self.assertIn("**RETURN FOUND**", s); self.assertIn("hint words: 'not yet'", s)
        self.assertIn("**RETURN FOUND**", self.stanza("IOTA"))

    def test_c03_no_citing_return(self):
        s = self.stanza("DELTA")
        self.assertIn("**NO CITING RETURN**", s); self.assertIn("Re-ping text", s)

    def test_c03_cited_file_touch_is_shown_but_is_not_a_return(self):
        s = self.stanza("ETA")
        self.assertIn("**NO CITING RETURN**", s); self.assertIn("touched `AGENTS/ETA/workbook/KB.tsv`", s)

    def test_c03_dark_is_not_prechecked(self):
        self.assertIn("n/a — no owner self-commit", self.stanza("ALPHA"))

    def test_c03_git_failure_is_unchecked_never_no_citing_return(self):
        ev = SS.Evidence("0000000000000000000000000000000000000000", None)
        rows = S.collect(S.read_text("PROME/DOCKET.tsv"), GATES_HDR, dt.date.fromisoformat(TODAY), 0, S.Liveness(TODAY + " 23:59"), ROSTER)
        d = next(x for x in SS.details(rows, S.read_text("PROME/DOCKET.tsv"), GATES_HDR) if x.key == "D:L5")
        self.assertEqual(SS.precheck(d, ev, {})[0], "UNCHECKED")

    def test_c03_body_mention_alone_is_labelled(self):
        s = self.stanza("LAMBDA")
        self.assertIn("**RETURN FOUND**", s); self.assertIn("only body mentions", s)

    def test_c03_strong_return_is_listed_before_a_newer_body_mention(self):
        lines = [l for l in self.stanza("MUON").split("\n") if l.strip().startswith("- commit")]
        self.assertIn("not yet out", lines[0]); self.assertIn("(body mention)", lines[1])

    def test_c03_return_dated_before_the_due_date_is_flagged(self):
        s = self.stanza("NUON")
        self.assertIn("BEFORE the due date 2026-03-10", s)

    def test_c03_uncited_owner_packets_are_listed(self):
        self.assertRegex(self.stanza("KAPPA"), r"do NOT cite the row[^\n]*2026-03-10 other")

    def test_c03_gate_owner_dark_this_cycle_is_said(self):
        """Reader A round 2: a gate's ACTIVE class dates from REGISTRATION; an owner silent all cycle must not read as 'in session'."""
        g = GATES_HDR + "\nGATE-D-1\t2026-02-01\tDELTA\tcond\tcons\tLIVE\t\tsrc\t\tJUDGEMENT\tdef\t2026-03-20\n"
        (self.repo / "G2.tsv").write_text(g)
        a = argparse.Namespace(**{**vars(self.args), "gates": "G2.tsv", "as_of": "2026-03-20"})
        body = SS.compose(a, "s")[2]
        self.assertRegex(body, r"`G:GATE-D-1` → \*\*NO CITING RETURN\*\*\n\s+- ⚠ the owner has NO self-commit since 2026-03-14")

    def test_c05c_prome_annotation_any_case(self):
        self.assertIn("PROME annotated the row 2026-03-07", self.stanza("NUON"))

    def test_c08_slash_joined_co_owners_are_seen(self):
        self.assertEqual(SS.desk_tokens("SHADE/BROCK/CREED"), ["SHADE", "BROCK", "CREED"])
        self.assertEqual(SS.desk_tokens("ALPHA (reads `AGENTS/BETA/x.md`) / GAMMA"), ["ALPHA", "GAMMA"])
        self.assertIn("`D:L21` NUON + BETA", self.body)

    def test_c03_decimal_identifier_is_not_truncated(self):
        self.assertNotIn("VX-3", SS.row_ids("CREED VX-3.01 availability")); self.assertIn("FERT-11", SS.row_ids("grade FERT-11."))

    # 4 — wrong owner
    def test_c04_walter_packet_is_not_wal_evidence(self):
        s = self.stanza("WAL")
        self.assertIn("**NO CITING RETURN**", s); self.assertNotIn("from-WALTER", s)

    def test_c04_prome_citation_is_not_an_owner_return(self):
        s = self.stanza("THETA")
        self.assertIn("**NO CITING RETURN**", s); self.assertNotIn("from-THETA_fake", s)

    def test_c04_owner_packet_citing_another_row_is_not_evidence(self):
        self.assertIn("**NO CITING RETURN**", self.stanza("KAPPA"))

    # 5 — overlap
    def test_c05a_dark_plus_active_is_one_stanza(self):
        self.assertEqual(len(re.findall(r"(?m)^### EPS —", self.body)), 1)
        s = self.stanza("EPS")
        self.assertIn("`D:L10` [DARK]", s); self.assertIn("`D:L11` [ACTIVE]", s)

    def test_c05b_packet_in_inbox_and_processed_counts_once(self):
        s = self.stanza("ZETA")
        self.assertIn("**RETURN FOUND**", s); self.assertEqual(s.count("from-ZETA_WQ-900-encoded.md"), 1); self.assertIn(self.c_zeta, s)

    def test_c05d_inflight_is_flagged_never_suppressed(self):
        head = self.stanza("EPS").split("\n")[0]
        self.assertIn("SPAWN CANDIDATE", head); self.assertIn("check liveness first", head)
        self.assertRegex(self.body, r"IN-FLIGHT\) touch today[^\n]*EPS")

    # 6 — assignment
    def test_c06_assignment_word_budget_and_verbatim(self):
        rows = S.collect(S.read_text("PROME/DOCKET.tsv"), GATES_HDR, dt.date.fromisoformat(TODAY), 0, S.Liveness(TODAY + " 23:59"), ROSTER)
        dets = SS.details(rows, S.read_text("PROME/DOCKET.tsv"), GATES_HDR)
        for n in (1, 2, 4, 8, 12):
            ds = (dets * 3)[:n]
            text = SS.assignment("X", ds)
            self.assertLessEqual(len(SS.words(text)), SS.ASSIGN_WORDS, f"n={n}")
            for d, q in zip(ds, re.findall(r'due \w+ \d\d/\d\d\): "([^"]*)"', text)):
                self.assertTrue(d.desc.startswith(q), f"quote not a verbatim prefix (n={n})")
        a = SS.assignment("ALPHA", [d for d in dets if d.key == "D:L2"])
        self.assertIn("[…] read D:L2 whole", a); self.assertIn("Done when ALPHA's ledger carries the grade", a)

    def test_c06_caveat_travels_outside_the_word_budget(self):
        s = self.stanza("ALPHA")
        self.assertIn("Must travel", s); self.assertIn("⛔ Never grade before the release is public.", s)

    # 8 — related
    def test_c08_related_rows_and_second_owner(self):
        s = self.stanza("ALPHA")
        self.assertIn("Would also fit", s); self.assertIn("`D:L17`", s)
        self.assertNotIn("D:L17", s.split("Would also fit")[0])
        self.assertIn("`D:L2` ALPHA + BETA", self.body)
        self.assertRegex(self.stanza("BETA"), r"non-first owner[^\n]*`D:L2`")

    def test_c04_key_pattern_boundaries(self):
        class D:                                            # the two attributes key_pattern reads
            kind, key = "D", "D:L47"
        pat = SS.key_pattern(D)
        for yes in ("graded L47 today", "(L47)", "D:L47 done", "DOCKET L47: done", "L47."):
            self.assertIsNotNone(pat.search(yes), yes)
        for no in ("L475 done", "STATUS.md:L47", "XL47", "L47a", "file#L47", "see L4"):
            self.assertIsNone(pat.search(no), no)
        D.kind, D.key = "G", "G:GATE-X-1"
        self.assertIsNotNone(SS.key_pattern(D).search("review of GATE-X-1 done"))
        self.assertIsNone(SS.key_pattern(D).search("GATE-X-12 and GATE-X-1-B"))

    # 9 — cap
    def test_c09_slots_only_for_launchable_dark(self):
        self.assertRegex(self.stanza("ALPHA").split("\n")[0], r"slot [12] of 4")
        self.assertIn("⏱", self.stanza("ALPHA").split("\n")[0]); self.assertRegex(self.body, r"Spawn candidates[^\n]*ALPHA ⏱")
        self.assertIn("NOT A SPAWN", self.stanza("OLDIE").split("\n")[0])
        self.assertEqual(len(re.findall(r"(?m)^### .*slot \d", self.body)), 2)       # ALPHA + EPS; OLDIE (dormant) takes none

    def test_c09_beyond_cap_is_labelled(self):
        docket = "# h\n" + "\n".join(_row(TODAY, f"row {d}", d) for d in ("ALPHA", "OLDIE")) + "\n"
        docket += "\n".join(_row(TODAY, f"row {i}", f"NEW{i}X") for i in range(6)) + "\n"
        roster = ROSTER.replace("| ALPHA | x |", "| ALPHA | x |\n" + "".join(f"| NEW{i}X | x |\n" for i in range(6)), 1)
        (self.repo / "D2.tsv").write_text(docket); (self.repo / "R2.md").write_text(roster)
        a = argparse.Namespace(**{**vars(self.args), "docket": "D2.tsv", "roster": "R2.md"})
        body = SS.compose(a, "s")[2]
        self.assertEqual(len(re.findall(r"(?m)^### .*slot \d", body)), 7)
        self.assertEqual(len(re.findall(r"(?m)^### .*beyond the ordinary cap", body)), 3)

    def test_c07_lands_only_desk_is_a_table_row_and_is_conserved(self):
        a = argparse.Namespace(**{**vars(self.args), "horizon": 7})
        body = SS.compose(a, "s")[2]
        self.assertIn("## Not yet due", body); self.assertRegex(body, r"(?m)^\| OMEGA \| `D:L22`")
        self.assertIsNone(re.search(r"(?m)^### OMEGA", body)); self.assertIn("· OK", body)
        self.assertIn("`D:L17`", body.split("### ALPHA")[1].split("###")[0])     # a desk with a due row keeps its landing row in its stanza

    # 10 — missing information
    def test_c10_unreadable_roster_and_orch_are_named(self):
        a = argparse.Namespace(**{**vars(self.args), "roster": "NOPE.md", "orch_log": "NOPE.tsv"})
        body = SS.compose(a, "s")[2]
        self.assertIn("CANNOT-EVALUATE (ROSTER unreadable)", body); self.assertIn("CANNOT-EVALUATE (ORCH_LOG unreadable)", body)
        self.assertIn("### ALPHA —", body)

    def test_c10_unreadable_docket_overwrites_with_failed_banner(self):
        out = self.repo / "SLATE.md"; out.write_text("stale but plausible")
        r = subprocess.run([sys.executable, str(REAL / "PROME/tools/spawn_slate.py"), "--docket", "NOPE.tsv", "--out", str(out)],
                           cwd=self.repo, capture_output=True, text=True, env={**os.environ, "PYTHONPATH": str(REAL / "scripts")})
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("FAILED", out.read_text()); self.assertNotIn("stale but plausible", out.read_text())

    # 11 / 12 / 13
    def test_c11_header_carries_stamp_weekday_head_and_bytes(self):
        text, n = SS.header("2026-03-10 09:00 EDT", self.today, 0, self.rev, self.body)
        first = text.split("\n")[0]
        self.assertIn("(Tue)", first); self.assertIn(self.rev, first); self.assertEqual(n, len(text.encode()))
        self.assertIn(f"{n:,} B", first)

    def test_c12_over_budget_is_bannered(self):
        self.assertIn("OVER BUDGET", SS.header("s", self.today, 0, self.rev, "x" * 40000)[0].split("\n")[0])

    def test_c13_deterministic(self):
        self.assertEqual(SS.compose(self.args, "other stamp")[2], self.body)

    def test_c13_imports_are_stdlib_plus_spawn_list(self):
        src = (REAL / "PROME/tools/spawn_slate.py").read_text()
        mods = set(re.findall(r"(?m)^import ([\w, ]+)", src)) | set(re.findall(r"(?m)^from (\w+) import", src))
        flat = {m.strip().split(" as ")[0] for g in mods for m in g.split(",")}
        self.assertEqual(flat - {"argparse", "contextlib", "datetime", "io", "re", "subprocess", "sys", "pathlib", "spawn_list"}, set())


if __name__ == "__main__":
    unittest.main()
