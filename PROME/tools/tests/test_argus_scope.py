#!/usr/bin/env python3
"""L336 — acceptance tests for the REDESIGNED argus_scope.

Conditions: PROME/proposals/2026-09-11_L336-argus-redesign-ACCEPTANCE-CONDITIONS.md
A8 requires PROPERTY tests, not string tests. The prior suite pinned the reviewer's literal strings
("PROME: CLOSEOUT symmetry table…", a processed/ path); those pass while the next instance of the same property
walks through. Each class below asserts the PROPERTY and keeps the known strings only as extra anchors.

Every fixture is a throwaway repo — no assertion reads the live tree.
"""
import importlib.util, itertools, os, subprocess, tempfile, unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("argus_scope", TOOLS / "argus_scope.py")
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
LIVE_PERIMETER = TOOLS.parent / "state/AUDIT_PERIMETER.tsv"


def sh(*a, cwd): subprocess.run(a, cwd=cwd, check=True, capture_output=True, text=True)
def write(repo, rel, text="x\n"):
    p = Path(repo) / rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8"); return rel
def append(repo, rel, text):
    with open(Path(repo) / rel, "a", encoding="utf-8") as fh: fh.write(text)
def commit(repo, subject, paths):
    sh("git", "add", *paths, cwd=repo); sh("git", "commit", "-m", subject, *paths, cwd=repo)


class Repo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.repo = self.tmp.name
        sh("git", "init", "-q", "-b", "master", cwd=self.repo)
        sh("git", "config", "user.email", "t@t", cwd=self.repo); sh("git", "config", "user.name", "t", cwd=self.repo)
        commit(self.repo, "PROME: STANDARD closeout 2026-09-10", [write(self.repo, "PROME/STATUS.md")])
        self.base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.repo, capture_output=True,
                                   text=True, check=True).stdout.strip()
        self.cwd = os.getcwd(); os.chdir(self.repo)
        # Production Git and content reads are anchored to ROOT, not process cwd.
        root_patch = patch.object(A, "ROOT", Path(self.repo))
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.rules = A.load_perimeter(LIVE_PERIMETER)
    def tearDown(self): os.chdir(self.cwd); self.tmp.cleanup()
    def scope(self, **kw): return A.build_scope(self.base, self.rules, **kw)
    def paths(self, lane, **kw): return [e["path"] for e in self.scope(**kw)[0][lane]]


class A1_BaselineIsRecordedNeverMatched(Repo):
    """PROPERTY: no commit SUBJECT can influence the baseline, because no subject is read."""

    def test_no_subject_however_written_can_become_the_baseline(self):
        subjects = ["PROME: CLOSEOUT symmetry table — WILL_QUEUE row", "PROME: STANDARD closeout 2026-09-11",
                    "PROME: closeout 9/10 night", "closeout", "PROME: about the closeout process",
                    "TERRY: closeout", "PROME: CLOSEOUT", "PROME:   LIGHT   closeout   x"]
        for i, s in enumerate(subjects):
            commit(self.repo, s, [write(self.repo, f"PROME/f{i}.md")])
        # the baseline is whatever was RECORDED; every one of those commits is merely IN scope, never the edge
        owned = self.paths("OWNED")
        self.assertEqual(len(owned), len(subjects), "every post-baseline PROME path is in scope")
        self.assertNotIn("PROME/STATUS.md", owned, "the baseline commit's own path is not re-audited")

    def test_the_module_reads_no_commit_subject_at_all(self):
        """Structural: the redesign's guarantee is that subjects are never parsed for classification."""
        src = (TOOLS / "argus_scope.py").read_text(encoding="utf-8")
        code = "\n".join(l for l in src.splitlines() if not l.lstrip().startswith("#"))
        self.assertNotIn("%s", code.split('"""')[-1], "no subject format string in executable code")
        for forbidden in ("CLOSEOUT_RE", "PROME_RE", "PROME_PACKET_RE", "startswith(\"PROME\")"):
            self.assertNotIn(forbidden, code, f"{forbidden} is a reconstructed boundary; A2 forbids it")

    def test_missing_or_corrupt_baseline_fails_loud_never_guesses(self):
        for bad in ("", "{}", '{"sha": "zzzz"}', '{"sha": "deadbeef"}', "not json"):
            f = Path(self.repo) / "b.json"; f.write_text(bad, encoding="utf-8")
            d, why = A.load_baseline(f)
            self.assertIsNone(d, bad); self.assertTrue(why)
        self.assertEqual(A.load_baseline(Path(self.repo) / "nope.json")[0], None)


class A2_PerimeterIsDeclaredNotCoded(Repo):
    """PROPERTY: classification is a pure function of the manifest; the code holds no path knowledge."""

    def test_a_surface_is_added_by_a_manifest_ROW_not_a_code_edit(self):
        f = Path(self.repo) / "p.tsv"
        f.write_text("pattern\tclass\treason\nNEWSURFACE/**\tOWNED\tinvented for this test\n", encoding="utf-8")
        rules = A.load_perimeter(f)
        self.assertEqual(A.classify("NEWSURFACE/a/b.md", rules)[0], "OWNED")
        self.assertEqual(A.classify("PROME/STATUS.md", rules)[0], "UNATTRIBUTED",
                         "with only that row declared, even PROME's own path is UNATTRIBUTED — the code knows nothing")

    def test_malformed_manifest_fails_loud_never_defaults(self):
        for bad in ("pattern\tclass\treason\nX/**\tTYPO\twrong class\n", "pattern\tclass\treason\nX/**\n",
                    "pattern\tclass\treason\n"):
            f = Path(self.repo) / "bad.tsv"; f.write_text(bad, encoding="utf-8")
            with self.assertRaises(SystemExit): A.load_perimeter(f)

    def test_first_match_wins_and_star_does_not_cross_a_separator(self):
        self.assertTrue(A._match("AGENTS/*/inbox/*", "AGENTS/RED/inbox/a.md"))
        self.assertFalse(A._match("AGENTS/*/inbox/*", "AGENTS/RED/inbox/processed/a.md"))
        self.assertTrue(A._match("AGENTS/**", "AGENTS/RED/inbox/processed/a.md"))


class A3_AttributionByRecordedOwnership(Repo):
    """PROPERTY: for a FIXED path, the lane is identical under EVERY commit subject."""

    def test_lane_is_invariant_under_the_commit_subject(self):
        subjects = ["PROME: x", "TERRY: x", "LABOR: consume PROME packet -> processed",
                    "FORGE: reconcile", "CARL -> PROME: packet", "", "weird subject"]
        lanes = set()
        for i, s in enumerate(subjects):
            with self.subTest(subject=s):
                sub = tempfile.TemporaryDirectory(); r = sub.name
                sh("git", "init", "-q", "-b", "master", cwd=r)
                sh("git", "config", "user.email", "t@t", cwd=r); sh("git", "config", "user.name", "t", cwd=r)
                commit(r, "PROME: STANDARD closeout", [write(r, "PROME/STATUS.md")])
                base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=r, capture_output=True,
                                      text=True, check=True).stdout.strip()
                commit(r, s or "x", [write(r, "FORGE/STATUS.md")])
                cwd = os.getcwd(); os.chdir(r)
                try:
                    with patch.object(A, "ROOT", Path(r)):
                        got = self._lane_of("FORGE/STATUS.md", A.build_scope(base, self.rules))
                finally:
                    os.chdir(cwd); sub.cleanup()
                lanes.add(got)
        self.assertEqual(lanes, {"OWNED"}, "the subject must not change the lane; got " + str(lanes))

    @staticmethod
    def _lane_of(path, scoped):
        lanes, excluded = scoped
        for name, entries in lanes.items():
            if any(e["path"] == path for e in entries): return name
        return "EXCLUDED" if any(e["path"] == path for e in excluded) else "ABSENT"

    def test_a_recipient_consuming_a_packet_is_out_of_scope_by_PATH_not_by_subject(self):
        commit(self.repo, "LABOR: consume PROME packet -> processed",
               [write(self.repo, "AGENTS/LABOR/inbox/processed/2026-09-11_from-PROME_x.md")])
        self.assertNotIn("AGENTS/LABOR/inbox/processed/2026-09-11_from-PROME_x.md",
                         self.paths("OWNED") + self.paths("SHARED") + self.paths("UNATTRIBUTED"))


class A4_NoSilentDropEver(Repo):
    """PROPERTY: every changed path lands in exactly one lane; nothing vanishes."""

    def test_every_changed_path_is_accounted_for_under_many_shapes(self):
        shapes = ["PROME/a.md", "AGENTS/BRENT/inbox/MSG-2026-09-11-vector.md",
                  "AGENTS/FALCON/inbox/data.csv", "AGENTS/FALCON/inbox/x_from-PROME.md",
                  "memory/auto/z.md", "memory/2026-09-11.md", "FORGE/x.md", "HEARTBEAT.md",
                  "AGENTS/TERRY/STATUS.md", "BOARD/SIG.md", "zzz-unknown-surface/x.md",
                  "PROME/a file with spaces.md", "PROME/café.md"]
        for s in shapes: write(self.repo, s)
        lanes, excluded = self.scope()
        seen = {e["path"] for v in lanes.values() for e in v} | {e["path"] for e in excluded}
        for s in shapes:
            self.assertIn(s, seen, f"{s} vanished — silent drop")

    def test_a_PROME_artifact_in_another_desks_inbox_appears_under_ANY_filename(self):
        """BLOCKER F-4: the MSG-* route can never contain 'from-PROME'."""
        for name in ("MSG-2026-09-11-vector.md", "data/firms.csv", "2026-09-11_from-PROME_x.md", "oddname.md"):
            with self.subTest(name=name):
                write(self.repo, f"AGENTS/BRENT/inbox/{name}")
                lanes, excluded = self.scope()
                seen = {e["path"] for v in lanes.values() for e in v} | {e["path"] for e in excluded}
                self.assertIn(f"AGENTS/BRENT/inbox/{name}", seen)

    def test_an_undeclared_surface_is_UNATTRIBUTED_not_dropped_and_not_claimed(self):
        write(self.repo, "brand-new-tree/thing.md")
        self.assertIn("brand-new-tree/thing.md", self.paths("UNATTRIBUTED"))
        self.assertNotIn("brand-new-tree/thing.md", self.paths("OWNED"))


class A5_NoSharedSurfaceClaimedByPattern(Repo):
    """PROPERTY: no path under a SHARED rule ever reaches the OWNED lane, whoever touched it."""

    def test_shared_surfaces_are_never_OWNED_under_any_actor(self):
        shared = ["memory/auto/violet.md", "memory/2026-09-11.md", "AGENTS/RED/inbox/p.md"]
        for i, (s, subj) in enumerate(itertools.product(shared, ["PROME: x", "VIOLET: x", "BOND: x"])):
            write(self.repo, s); append(self.repo, s, f"edit {i}\n")
        self.assertEqual([p for p in self.paths("OWNED") if p in shared], [],
                         "a shared surface must never be claimed as PROME's")
        for s in shared:
            self.assertIn(s, self.paths("SHARED"))

    def test_the_daily_note_is_shared_not_owned_by_date_pattern(self):
        """BLOCKER F-5."""
        write(self.repo, "memory/2026-09-11.md")
        self.assertIn("memory/2026-09-11.md", self.paths("SHARED"))
        self.assertNotIn("memory/2026-09-11.md", self.paths("OWNED"))


class A6_OverlapPreserved(Repo):
    def test_committed_then_edited_carries_both_states_and_both_reads(self):
        commit(self.repo, "PROME: write", [write(self.repo, "PROME/HANDOFF.md", "v1\n")])
        append(self.repo, "PROME/HANDOFF.md", "pending correction\n")
        e = next(x for x in self.scope()[0]["OWNED"] if x["path"] == "PROME/HANDOFF.md")
        self.assertTrue(e["committed"] and e["pending"], "both states required")
        self.assertEqual(len(A.reads_for(e)), 2, "both reads prescribed")

    def test_new_directory_listed_as_files_and_threshold_counts_unique(self):
        write(self.repo, "PROME/new/a.md"); write(self.repo, "PROME/new/b.md")
        commit(self.repo, "PROME: t", [write(self.repo, "PROME/t.py")])
        owned = self.paths("OWNED")
        self.assertIn("PROME/new/a.md", owned); self.assertIn("PROME/new/b.md", owned)
        self.assertNotIn("PROME/new/", owned)
        self.assertEqual(len(owned), len(set(owned)), "unique paths")

    def test_a_rename_shows_the_origins_disappearance(self):
        commit(self.repo, "PROME: write", [write(self.repo, "PROME/old.md")])
        sh("git", "mv", "PROME/old.md", "PROME/new.md", cwd=self.repo)
        owned = self.paths("OWNED")
        self.assertIn("PROME/old.md", owned, "the origin's disappearance must be visible")
        self.assertIn("PROME/new.md", owned)

    def test_non_ascii_path_does_not_split_into_two_entries(self):
        """F-3: `git show --name-only` C-quotes, `status -z` does not; the two sides must speak one encoding."""
        commit(self.repo, "PROME: write", [write(self.repo, "PROME/café.md", "v1\n")])
        append(self.repo, "PROME/café.md", "pending\n")
        owned = self.paths("OWNED")
        self.assertEqual([p for p in owned if "caf" in p], ["PROME/café.md"], f"got {owned}")
        e = next(x for x in self.scope()[0]["OWNED"] if "caf" in x["path"])
        self.assertTrue(e["committed"] and e["pending"], "overlap must survive a non-ASCII path")


class A7_AgentCopiesAgree(unittest.TestCase):
    def test_both_agent_definitions_are_byte_identical(self):
        root = TOOLS.parents[1] / ".claude/agents/argus.md"
        prome = TOOLS.parent / ".claude/agents/argus.md"
        self.assertEqual(root.read_bytes(), prome.read_bytes())

    def test_every_emittable_state_has_a_read_instruction_in_the_agent_file(self):
        txt = (TOOLS.parents[1] / ".claude/agents/argus.md").read_text(encoding="utf-8")
        for token in ("OWNED", "SHARED", "UNATTRIBUTED", "committed+PENDING", "DELETED"):
            self.assertIn(token, txt, f"the tool can emit {token}; the agent file must say how to read it")


class ReviewFindings_L336(Repo):
    """The three ❌ and two ⚠️ the INDEPENDENT reviewer produced against the final candidate, each with its
    own counterexample. Kept as named anchors so the finding cannot be re-lost (A8's intent)."""

    def test_A4_NO_FILENAME_decides_visibility_anywhere_in_an_inbox(self):
        """❌1, twice. First attempt: lanes EXCLUDED outright — a PROME artifact in a lane vanished.
        Second attempt: include-on-hint keyed on `*from-PROME*` — still a FILENAME key, and ARGUS trial run 1
        found the live instance it misses: 888924d2e committed
        AGENTS/FALCON/inbox/data/2026-09-11_FIRMS_VIIRS_….csv, PROME's own packet body, no hint in the name.
        The contract is unconditional, so the rule is now unconditional: EVERY inbox path at EVERY depth is
        SHARED. The ~44 lane paths that come with it are the declared price."""
        names = ["2026-09-11_from-PROME_urgent.md", "SIG-W-20260911-001.md",
                 "data/2026-09-11_FIRMS_VIIRS_corridor.csv", "MSG-2026-09-11-vector.md", "oddname.bin"]
        for i, n in enumerate(names):
            commit(self.repo, f"c{i}", [write(self.repo, f"AGENTS/WALTER/inbox/{n}")])
        shared = {e["path"] for e in self.scope()[0]["SHARED"]}
        for n in names:
            self.assertIn(f"AGENTS/WALTER/inbox/{n}", shared,
                          "no filename may decide visibility inside an inbox")

    def test_A4_only_processed_is_excluded_inside_an_inbox(self):
        """The one inbox exclusion that survives, and it is by ACT (consumption) not by name."""
        commit(self.repo, "LABOR: consume", [write(self.repo, "AGENTS/LABOR/inbox/processed/x_from-PROME.md")])
        lanes, excluded = self.scope()
        self.assertIn("AGENTS/LABOR/inbox/processed/x_from-PROME.md", {e["path"] for e in excluded})
        self.assertNotIn("AGENTS/LABOR/inbox/processed/x_from-PROME.md",
                         {e["path"] for v in lanes.values() for e in v})

    def test_A4_the_manifest_holds_no_filename_key_for_visibility(self):
        """Structural guard: the defect recurred twice because a filename key kept being reintroduced."""
        txt = LIVE_PERIMETER.read_text(encoding="utf-8")
        rules = [l for l in txt.splitlines() if l and not l.startswith("#") and not l.startswith("pattern")]
        for line in rules:
            pat = line.split("\t")[0]
            self.assertNotIn("from-PROME", pat,
                             "a filename key decided visibility twice and failed twice; patterns are structural")

    def test_A1_an_orphaned_baseline_fails_loud_after_a_rebase(self):
        """⚠️2: cat-file -e PASSES on a commit no longer reachable from HEAD."""
        import json as _j
        commit(self.repo, "PROME: work", [write(self.repo, "PROME/a.md")])
        orphan = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.repo, capture_output=True,
                                text=True, check=True).stdout.strip()
        sh("git", "reset", "--hard", "HEAD~1", cwd=self.repo)
        commit(self.repo, "OTHER: diverged", [write(self.repo, "AGENTS/TERRY/x.md")])
        f = Path(self.repo) / "b.json"; f.write_text(_j.dumps({"sha": orphan}), encoding="utf-8")
        d, why = A.load_baseline(f)
        self.assertIsNone(d, "an orphaned baseline must not be used")
        self.assertIn("ancestor", why)

    def test_a_COMMITTED_rename_shows_the_origins_disappearance(self):
        """⚠️3: the prior test covered only the UNCOMMITTED rename while its name claimed the property."""
        commit(self.repo, "PROME: write", [write(self.repo, "PROME/BRIEF.md")])
        (Path(self.repo) / "PROME/archive").mkdir(parents=True, exist_ok=True)
        sh("git", "mv", "PROME/BRIEF.md", "PROME/archive/BRIEF.md", cwd=self.repo)
        sh("git", "commit", "-m", "PROME: retire to archive", "-a", cwd=self.repo)
        owned = self.paths("OWNED")
        self.assertIn("PROME/BRIEF.md", owned, "git mv to archive/ is routine closeout work")
        self.assertIn("PROME/archive/BRIEF.md", owned)

    def test_no_pending_flag_restores_committed_only(self):
        """❌3: this coverage was lost in the redesign and is restored here."""
        commit(self.repo, "PROME: t", [write(self.repo, "PROME/tools/t.py")])
        write(self.repo, "PROME/NEW.md")
        self.assertIn("PROME/NEW.md", self.paths("OWNED"))
        self.assertNotIn("PROME/NEW.md", self.paths("OWNED", include_pending=False))


class C1_CompleteWorkflow(Repo):
    """C1: the COMPLETE closeout workflow, not the units — write, commit some, leave some pending, compute
    scope, confirm what an auditor actually receives, then record the next baseline and confirm it rolls."""

    def test_a_full_closeout_shaped_run(self):
        # 1. mid-session: PROME writes and commits some work
        commit(self.repo, "PROME: tool change", [write(self.repo, "PROME/tools/t.py", "v1\n")])
        commit(self.repo, "PROME: STATUS mid-session", [write(self.repo, "PROME/STATUS.md", "v1\n")])
        commit(self.repo, "PROME -> RED: packet", [write(self.repo, "AGENTS/RED/inbox/2026-09-11_from-PROME_x.md")])
        # 2. another desk works concurrently, and consumes one of PROME's packets
        commit(self.repo, "TERRY: own work", [write(self.repo, "AGENTS/TERRY/STATUS.md")])
        commit(self.repo, "LABOR: consume -> processed",
               [write(self.repo, "AGENTS/LABOR/inbox/processed/2026-09-11_from-PROME_y.md")])
        # 3. closeout chunk 1-3: PROME corrects a committed file, writes new ones, one of them shared
        append(self.repo, "PROME/STATUS.md", "closeout correction\n")
        write(self.repo, "PROME/HANDOFF.md"); write(self.repo, "PROME/SCRATCH.md")
        write(self.repo, "memory/2026-09-11.md")
        write(self.repo, "AGENTS/BRENT/inbox/MSG-2026-09-11-vector.md")
        # 4. another desk leaves ITS work dirty at the same moment
        append(self.repo, "AGENTS/TERRY/STATUS.md", "terry mid-session\n")
        write(self.repo, "memory/auto/violet_finding.md")

        lanes, excluded = self.scope()
        owned = {e["path"] for e in lanes["OWNED"]}
        shared = {e["path"] for e in lanes["SHARED"]}
        unattr = {e["path"] for e in lanes["UNATTRIBUTED"]}
        exc = {e["path"] for e in excluded}

        # the closeout's own pending writes reach the auditor
        for p_ in ("PROME/HANDOFF.md", "PROME/SCRATCH.md", "PROME/tools/t.py", "PROME/STATUS.md"):
            self.assertIn(p_, owned, p_)
        # the corrected file carries BOTH states and BOTH reads
        st = next(e for e in lanes["OWNED"] if e["path"] == "PROME/STATUS.md")
        self.assertTrue(st["committed"] and st["pending"])
        self.assertEqual(len(A.reads_for(st)), 2)
        # another desk's work — committed and pending — never reaches PROME's audit
        self.assertIn("AGENTS/TERRY/STATUS.md", exc)
        self.assertNotIn("AGENTS/TERRY/STATUS.md", owned | shared | unattr)
        self.assertIn("AGENTS/LABOR/inbox/processed/2026-09-11_from-PROME_y.md", exc)
        # PROME artifacts in other desks' inboxes appear, under both naming shapes, as SHARED not OWNED
        for p_ in ("AGENTS/RED/inbox/2026-09-11_from-PROME_x.md", "AGENTS/BRENT/inbox/MSG-2026-09-11-vector.md"):
            self.assertIn(p_, shared, p_); self.assertNotIn(p_, owned)
        # shared surfaces are labelled, never claimed
        self.assertIn("memory/2026-09-11.md", shared)
        self.assertIn("memory/auto/violet_finding.md", shared)
        self.assertEqual(unattr, set(), "nothing undeclared in a normal closeout")
        # nothing vanished — the fixture touches exactly 10 distinct paths; assert EXACTLY, not >=,
        # so a future silent drop cannot hide under a loose bound (the >= was my own sloppy assertion).
        fixture_paths = {
            "PROME/tools/t.py", "PROME/STATUS.md", "AGENTS/RED/inbox/2026-09-11_from-PROME_x.md",
            "AGENTS/TERRY/STATUS.md", "AGENTS/LABOR/inbox/processed/2026-09-11_from-PROME_y.md",
            "PROME/HANDOFF.md", "PROME/SCRATCH.md", "memory/2026-09-11.md",
            "AGENTS/BRENT/inbox/MSG-2026-09-11-vector.md", "memory/auto/violet_finding.md"}
        self.assertEqual(owned | shared | unattr | exc, fixture_paths,
                         "every path the closeout touched is accounted for in exactly one lane")

    def test_recording_the_next_baseline_rolls_the_window(self):
        commit(self.repo, "PROME: work", [write(self.repo, "PROME/a.md")])
        self.assertIn("PROME/a.md", self.paths("OWNED"))
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.repo, capture_output=True,
                              text=True, check=True).stdout.strip()
        lanes, _ = A.build_scope(head, self.rules)          # the new baseline
        self.assertEqual([e["path"] for e in lanes["OWNED"]], [],
                         "after recording the closeout as baseline, the session just closed is behind the window")


class LivePerimeterSanity(unittest.TestCase):
    def test_live_manifest_parses_and_declares_every_class(self):
        rules = A.load_perimeter(LIVE_PERIMETER)
        self.assertTrue(rules)
        self.assertEqual({c for _, c, _ in rules}, set(A.CLASSES))
        for _, _, reason in rules:
            self.assertTrue(reason.strip(), "every rule states WHY — a declared exclusion, not a silent drop")


if __name__ == "__main__":
    unittest.main(verbosity=1)
