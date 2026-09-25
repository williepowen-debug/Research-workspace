"""spawn_list.py desk-commit ATTRIBUTION — subject at a word boundary as the candidate filter, PATHS decide.

Defect (DOCKET L455, 2026-09-21): `^DESK( ->|:)` misses `DESK closeout …` / `DESK 9/17 …` / `DESK (orch):` /
`DESK memory:` / `DESK S46:` — toward DARK, the WQ-184 spawn trigger. A word-boundary-only loosening over-attributes
(measured 5/386 on 2026-09-25) toward ACTIVE, the invisible direction.

Acceptance conditions -> PROME/tools/tests/ACCEPTANCE_spawn_list_desk_commit_attribution_L455.md
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_spawn_list_desk_commit_attribution_L455.py
Throwaway repo only — nothing here reads the live tree.
"""
import os, pathlib, re, subprocess, sys, tempfile, types, unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME" / "tools"))
import spawn_list as S            # noqa: E402
import desk_activity as DA        # noqa: E402

OLD = lambda d: re.compile(rf"^{re.escape(d)}( ->|:)")   # the pre-L455 pattern, kept only to falsify the guard


def _git(repo, *a, **k):
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, check=True, **k)


def _commit(repo, subject, paths, body="", empty=False):
    for p in paths:
        f = repo / p; f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(f"{subject}\n{os.urandom(4).hex()}\n", encoding="utf-8")
        _git(repo, "add", "--", p)
    msg = subject + ("\n\n" + body if body else "")
    args = ["commit", "-q", "-m", msg] + (["--allow-empty"] if empty else [])
    _git(repo, *args)
    return _git(repo, "rev-parse", "--short", "HEAD").stdout.strip()


class Fixture(unittest.TestCase):
    """One throwaway repo; every commit is a fixture row. Order = git order (newest last)."""
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.repo = pathlib.Path(cls.tmp.name)
        _git(cls.repo, "init", "-q", "-b", "master")
        _git(cls.repo, "config", "user.email", "t@t"); _git(cls.repo, "config", "user.name", "t")
        c = cls.c = {}
        # (1) ORDINARY — seven subject forms, all touching AGENTS/BROCK/
        for i, subj in enumerate(["BROCK: CRMT grade", "BROCK -> PROME: packet", "BROCK 2026-09-02 addendum",
                                  "BROCK closeout 2026-09-19: notes", "BROCK (orch): reconcile", "BROCK memory: lesson",
                                  "BROCK S46: follow-up"]):
            c[f"ord{i}"] = _commit(cls.repo, subj, [f"AGENTS/BROCK/f{i}.md"])
        # (2) OVERLAP — WAL vs WALTER
        c["walter"] = _commit(cls.repo, "WALTER: 15 handoffs", ["AGENTS/WALTER/BOARD/x.md", "AGENTS/WAL/inbox/WALTER/SIG-1.md"])
        c["wal"] = _commit(cls.repo, "WAL closeout 2026-09-24 (session #7)", ["AGENTS/WAL/STATUS.md"])
        # (3) WRONG OWNER
        c["bond_move"] = _commit(cls.repo, "BOND session-COMPLETE packet -> processed", ["PROME/inbox/processed/2026-09-01_from-BOND_x.md"])
        c["yuri_root"] = _commit(cls.repo, "YURI registered on the shared routing surfaces", ["AGENTS.md", "AGENTS/_NETWORK.md"])
        c["zhao_midas"] = _commit(cls.repo, "ZHAO refuted my STATED amendment rule", ["AGENTS/MIDAS/OPEN_ITEMS.md", "PROME/inbox/2026-09-02_from-MIDAS_q.md"])
        c["body_mention"] = _commit(cls.repo, "PROME: closeout", ["PROME/STATUS.md"], body="MIDAS: consumed its packet")
        # (4) CARVE-OUTS / GRANTS / EMPTY
        c["packets_only"] = _commit(cls.repo, "OTTO s022: packets to BROCK x2, CARL (carve-out 1)",
                                    ["AGENTS/BROCK/inbox/2026-09-12_from-OTTO_a.md", "AGENTS/CARL/inbox/2026-09-12_from-OTTO_b.md"])
        c["scripts_only"] = _commit(cls.repo, "DAEDALUS scripts/: two guards fixed", ["scripts/claim_check.py", "PROME/inbox/2026-09-24_from-DAEDALUS_c.md"])
        c["memory_only"] = _commit(cls.repo, "HAWK auto-memory: killed phrasing repaired", ["memory/auto/finding_x.md"])
        c["empty_marker"] = _commit(cls.repo, "OTTO s022: ledger nudge answered", [], empty=True)
        c["prome_forge"] = _commit(cls.repo, "PROME (FORGE): mirror the query", ["FORGE/tools/news-sweep/config.py"])
        S.ROOT = cls.repo

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def lsc(self, desk):
        return S.Liveness(None).last_self_commit(desk)

    # ── (1) ordinary
    def test_ordinary_seven_forms_attributed(self):
        for i in range(7):
            live = S.Liveness("2100-01-01")
            # bound the window to this commit so each form is tested on its own
            r = _git(self.repo, "log", "-n", "40", "--format=%x1e%cs\t%h\t%s", "--name-only", "--extended-regexp",
                     f"--grep={S.grep_pattern('BROCK')}").stdout
            hits = [h.split("\t")[1] for h, paths in S.parse_log_records(r)
                    if S.attributed("BROCK", h.split("\t", 2)[2], paths)]
            self.assertIn(self.c[f"ord{i}"], hits, f"form {i} not attributed")
        # newest BROCK-owned commit is ord6 (OTTO's packet INTO BROCK's inbox is OTTO's, not BROCK's)
        self.assertEqual(self.lsc("BROCK")[1], self.c["ord6"])

    def test_guard_falsified_old_pattern_misses_five_forms(self):
        missed = [s for s in ["BROCK 2026-09-02 addendum", "BROCK closeout 2026-09-19: notes", "BROCK (orch): reconcile",
                              "BROCK memory: lesson", "BROCK S46: follow-up"] if not OLD("BROCK").match(s)]
        self.assertEqual(len(missed), 5)                       # the defect, demonstrated
        self.assertTrue(all(S.subject_pattern("BROCK").match(s) for s in missed))

    # ── (2) overlap
    def test_overlap_walter_never_attributed_to_wal(self):
        self.assertEqual(self.lsc("WAL")[1], self.c["wal"])
        self.assertFalse(S.attributed("WAL", "WALTER: 15 handoffs", ["AGENTS/WALTER/BOARD/x.md"]))
        self.assertFalse(S.attributed("WAL", "WALTER: 15 handoffs", ["AGENTS/WAL/inbox/WALTER/SIG-1.md"]))   # a lane packet INTO WAL is the sender's

    def test_overlap_walter_own_commit_still_walter(self):
        self.assertEqual(self.lsc("WALTER")[1], self.c["walter"])

    # ── (3) wrong owner
    def test_wrong_owner_processed_move_is_not_bond(self):
        self.assertIsNone(self.lsc("BOND"))

    def test_wrong_owner_root_doc_is_not_yuri(self):
        self.assertIsNone(self.lsc("YURI"))

    def test_wrong_owner_other_desk_home_is_not_zhao(self):
        self.assertIsNone(self.lsc("ZHAO"))

    def test_wrong_owner_body_mention_is_not_midas(self):
        self.assertIsNone(self.lsc("MIDAS"))

    # ── (4) carve-outs, grants, empty
    def test_carveout_packets_only_commit_is_otto(self):
        self.assertIn(self.lsc("OTTO")[1], (self.c["packets_only"], self.c["empty_marker"]))
        self.assertTrue(S.attributed("OTTO", "OTTO s022: packets", ["AGENTS/BROCK/inbox/2026-09-12_from-OTTO_a.md"]))

    def test_grant_scripts_only_commit_is_daedalus(self):
        self.assertEqual(self.lsc("DAEDALUS")[1], self.c["scripts_only"])

    def test_memory_only_commit_is_hawk(self):
        self.assertEqual(self.lsc("HAWK")[1], self.c["memory_only"])

    def test_empty_marker_attributed_by_subject(self):
        self.assertEqual(self.lsc("OTTO")[1], self.c["empty_marker"])   # newest OTTO-owned

    def test_prome_forge_is_prome(self):
        self.assertTrue(S.attributed("PROME", "PROME (FORGE): mirror", ["FORGE/tools/news-sweep/config.py"]))

    # ── (5) missing information — the fail-closed path survives
    def test_git_failure_still_err(self):
        orig = S.subprocess.run
        S.subprocess.run = lambda *a, **k: types.SimpleNamespace(returncode=128, stdout="", stderr="fatal: index.lock")
        try:
            self.assertEqual(S.Liveness(None).last_self_commit("BROCK")[0], "!ERR")
        finally:
            S.subprocess.run = orig

    # ── (8) sibling parity
    def test_sibling_desk_activity_agrees(self):
        for desk in ["BROCK", "WAL", "WALTER", "BOND", "YURI", "ZHAO", "MIDAS", "OTTO", "DAEDALUS", "HAWK"]:
            a = self.lsc(desk); b = DA.last_commit(self.repo, desk)
            if a is None:
                self.assertIsNone(b, desk)
            else:
                self.assertTrue(b["sha"].startswith(a[1]), desk)

    # ── (4b) the convention form is the author's word even on a PROME-perimeter path (VIOLET -> PROME: DOCKET edit, 4b570a23b)
    def test_strong_anchor_attributed_by_subject(self):
        self.assertTrue(S.attributed("VIOLET", "VIOLET -> PROME: record L376 review return", ["PROME/DOCKET.tsv"]))
        self.assertTrue(S.attributed("LIQUID", "LIQUID: SIGNALS.md row (carve-out 2)", ["AGENTS/SIGNALS.md"]))
        self.assertFalse(S.attributed("WAL", "WALTER: x", ["AGENTS/WALTER/x.md"]))          # the anchor is not a prefix match

    def test_carveout_two_shared_log_loose_form(self):
        self.assertTrue(S.attributed("REGINALD", "REGINALD 9/1 REG-T-02 fired", ["AGENTS/SIGNALS.md", "AGENTS/WAL/inbox/2026-09-01_from-REGINALD_x.md"]))
        self.assertFalse(S.attributed("CARL", "CARL 9/10 audit", ["AGENTS/WALTER/registry/OTHER.tsv"]))   # not a carve-out ② log

    # ── reader round 1 (2026-09-25): three false-ACTIVE counterexamples
    def test_reader_cx1_mail_into_own_inbox_is_the_senders_act(self):
        self.assertFalse(S.attributed("HAWK", "HAWK L433 re-grade request from MIDAS", ["AGENTS/HAWK/inbox/2026-09-25_from-MIDAS_x.md", "AGENTS/MIDAS/STATUS.md"]))
        self.assertFalse(S.attributed("HAWK", "HAWK packet delivered by PROME", ["AGENTS/HAWK/inbox/2026-09-25_from-PROME_x.md"]))
        # …but a desk sweeping incoming packets in WITH its own files is still its own (WALTER 0542eff05 shape)
        self.assertTrue(S.attributed("WALTER", "WALTER boot: swept two packets", ["AGENTS/WALTER/inbox/2026-09-25_from-X_a.md", "AGENTS/WALTER/STATUS.md"]))

    def test_reader_cx3_quoted_non_ascii_path_is_refused(self):
        self.assertFalse(S.attributed("ZHAO", "ZHAO refuted my amendment rule", ['"AGENTS/MIDAS/analysis/caf\\303\\251.md"']))

    def test_reader_cx4_root_shared_dirs_are_prome_perimeter(self):
        for paths in (["docs/x.md", ".claude/skills/y.md", "memory/2026-09-25.md"], ["BOARD/INDEX.md", ".claude/agents/z.md"], ["reviews/r.md"]):
            self.assertFalse(S.attributed("YURI", "YURI note", paths), paths)

    def test_merge_commits_are_never_attributed(self):
        _git(self.repo, "checkout", "-q", "-b", "side")
        _commit(self.repo, "OTTO side work", ["AGENTS/OTTO/side.md"])
        _git(self.repo, "checkout", "-q", "master")
        _git(self.repo, "merge", "-q", "--no-ff", "-m", "OTTO merge side", "side")
        hit = self.lsc("OTTO")
        self.assertNotEqual(hit[1], _git(self.repo, "rev-parse", "--short", "HEAD").stdout.strip())   # the merge is skipped
        self.assertEqual(hit[1], _git(self.repo, "rev-parse", "--short", "side").stdout.strip())     # the real commit counts

    # ── (9) direction on ambiguity: a path under another desk's home with NO home path of one's own ⇒ not attributed
    def test_ambiguity_fails_toward_dark(self):
        self.assertFalse(S.attributed("ZHAO", "ZHAO 9/25 note", ["AGENTS/MIDAS/x.md", "AGENTS/HAWK/inbox/2026-09-25_from-ZHAO_p.md"]))   # loose form + another desk's home


if __name__ == "__main__":
    unittest.main()
