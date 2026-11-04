#!/usr/bin/env python3
"""WQ-289 (b) / DOCKET L473 — the narrow L367 form in `argus_scope.verify_review(paths=...)`.

Conditions: PROME/tools/tests/ACCEPTANCE_argus_r100_consumed_move_WQ289.md (written BEFORE the edit).
Test numbers below are that file's test list (1–13). Every fixture is a throwaway repo WITH A BARE
ORIGIN so `origin/master` is real git state, not a mock; nothing reads the live tree.

Run: python3 -W error::ResourceWarning -m unittest PROME.tools.tests.test_argus_r100_consumed_move_WQ289
"""
import importlib.util, os, subprocess, tempfile, unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("argus_scope_wq289", TOOLS / "argus_scope.py")
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
LIVE_PERIMETER = TOOLS.parent / "state/AUDIT_PERIMETER.tsv"

PKT = "2026-09-24_from-VIOLET_walkback.md"
ORIGIN = f"PROME/inbox/{PKT}"
DEST = f"PROME/inbox/processed/{PKT}"


def sh(*a, cwd):
    return subprocess.run(a, cwd=cwd, check=True, capture_output=True, text=True).stdout


def write(repo, rel, text="x\n"):
    p = Path(repo) / rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8"); return rel


def commit(repo, subject, paths):
    sh("git", "add", *paths, cwd=repo); sh("git", "commit", "-q", "-m", subject, "--", *paths, cwd=repo)


class _Base(unittest.TestCase):
    """A repo whose origin already holds the packet under the SENDER's commit (the 9/24 shape). No tests here."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.repo = str(Path(self.tmp.name) / "work")
        self.bare = str(Path(self.tmp.name) / "origin.git")
        sh("git", "init", "-q", "--bare", "-b", "master", self.bare, cwd=self.tmp.name)
        sh("git", "init", "-q", "-b", "master", self.repo, cwd=self.tmp.name)
        sh("git", "config", "user.email", "t@t", cwd=self.repo); sh("git", "config", "user.name", "t", cwd=self.repo)
        sh("git", "remote", "add", "origin", self.bare, cwd=self.repo)
        (Path(self.repo) / "PROME/state").mkdir(parents=True, exist_ok=True)
        (Path(self.repo) / "PROME/state/AUDIT_PERIMETER.tsv").write_bytes(LIVE_PERIMETER.read_bytes())
        commit(self.repo, "PROME: STANDARD closeout", [write(self.repo, "PROME/STATUS.md", "s\n"),
                                                    "PROME/state/AUDIT_PERIMETER.tsv"])
        commit(self.repo, "VIOLET -> PROME: walkback", [write(self.repo, ORIGIN, "packet body v1\n")])
        sh("git", "push", "-q", "-u", "origin", "master", cwd=self.repo)
        self.cwd = os.getcwd(); os.chdir(self.repo)
        rp = patch.object(A, "ROOT", Path(self.repo)); rp.start(); self.addCleanup(rp.stop)
        self.addCleanup(self._teardown)
        A.record_baseline(sh("git", "rev-parse", "HEAD", cwd=self.repo).strip())
        # PROME's own reviewed work this "session"
        write(self.repo, "PROME/SCRATCH.md", "scratch v2\n")

    def _teardown(self):
        os.chdir(self.cwd); self.tmp.cleanup()

    def move(self, origin=ORIGIN, dest=DEST):
        (Path(self.repo) / dest).parent.mkdir(parents=True, exist_ok=True)
        sh("git", "mv", origin, dest, cwd=self.repo)

    def freeze(self, moves=None, reviewed=True):
        A.record_review(["PROME/SCRATCH.md"], consumed_moves=moves)
        if reviewed:
            rc, msg = A.mark_reviewed("fixture audit"); self.assertEqual(rc, 0, msg)

    def verify(self, paths=("PROME/SCRATCH.md", ORIGIN, DEST), ref=None):
        return A.verify_review(paths=list(paths), ref=ref)


class MoveRepo(_Base):
    """P1–P8, the author's tests (acceptance list 1–13 + guard falsification)."""

    # 1 — ordinary
    def test_01_declared_confirmed_r100_move_passes_with_a_receipt(self):
        self.move(); self.freeze({DEST: ORIGIN})
        rc, out = self.verify()
        self.assertEqual(rc, 0, out)
        self.assertEqual(sum("R100-CONSUMED-MOVE" in l for l in out), 1, out)
        self.assertTrue(any(ORIGIN in l and DEST in l for l in out))

    # 2 — undeclared
    def test_02_undeclared_identical_move_still_blocks(self):
        self.move(); self.freeze(None)
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertTrue(any("UNREVIEWED" in l and DEST in l for l in out))
        self.assertFalse(any("R100" in l for l in out))

    # 3 — declared but not ARGUS-confirmed
    def test_03_declared_under_a_FROZEN_manifest_blocks(self):
        self.move(); self.freeze({DEST: ORIGIN}, reviewed=False)
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertTrue(any("not REVIEWED" in l for l in out), out)

    # 4 — overlap: renamed AND edited
    def test_04_move_then_edit_is_not_R100_and_blocks(self):
        self.move(); write(self.repo, DEST, "packet body v1\nconsumed note\n"); self.freeze({DEST: ORIGIN})
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)   # unstaged edit refused
        sh("git", "add", DEST, cwd=self.repo); self.freeze({DEST: ORIGIN})
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)   # staged edit: git sees no R100

    # 5 — bytes never on origin
    def test_05_local_only_packet_blocks_with_the_reason(self):
        local = "PROME/inbox/2026-09-25_from-LOCAL_never-pushed.md"
        commit(self.repo, "LOCAL -> PROME", [write(self.repo, local, "local\n")])   # committed, NOT pushed
        ldest = "PROME/inbox/processed/2026-09-25_from-LOCAL_never-pushed.md"
        self.move(local, ldest); self.freeze({ldest: local})
        rc, out = self.verify(("PROME/SCRATCH.md", local, ldest))
        self.assertEqual(rc, 1); self.assertTrue(any("on origin" in l for l in out), out)
        self.assertFalse(any("R100-CONSUMED" in l for l in out))

    # 6 — no origin ref at all
    def test_06_without_origin_master_the_exemption_is_withheld_not_granted(self):
        sh("git", "remote", "remove", "origin", cwd=self.repo)
        self.move(); self.freeze({DEST: ORIGIN})
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)
        self.assertTrue(any("cannot establish" in l for l in out), out)

    # 7 — a copy, not a move
    def test_07_origin_still_present_blocks(self):
        (Path(self.repo) / DEST).parent.mkdir(parents=True, exist_ok=True)
        write(self.repo, DEST, "packet body v1\n"); self.freeze({DEST: ORIGIN})
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertTrue(any("copy, not a move" in l for l in out), out)

    # 8 — wrong owner: another desk's inbox. NOTE: `AGENTS/*/inbox/**` is SHARED, so such a move enters the
    # ordinary review (ARGUS sees it, labelled SHARED) and never reaches the exemption; the property to hold is
    # that the exemption FUNCTION refuses it if ever asked — tested at the function, with a REVIEWED manifest.
    def test_08_the_exemption_refuses_another_desks_inbox_pair(self):
        o = f"AGENTS/BRENT/inbox/{PKT}"; d = f"AGENTS/BRENT/inbox/processed/{PKT}"
        commit(self.repo, "WALTER -> BRENT", [write(self.repo, o, "b\n")]); sh("git", "push", "-q", cwd=self.repo)
        self.move(o, d)
        ok, why = A._consumed_move_exemption(d, o, None, {"verdict": A.REVIEWED}, {d, o}, "0"*40)
        self.assertFalse(ok); self.assertIn("PROME's own inbox", why)

    # 9 — wrong owner: destination is a PROME surface, not consumption (PROME/reports is OWNED, same note as 8)
    def test_09_the_exemption_refuses_a_move_out_of_inbox_into_a_prome_surface(self):
        d = f"PROME/reports/{PKT}"
        self.move(ORIGIN, d)
        ok, why = A._consumed_move_exemption(d, ORIGIN, None, {"verdict": A.REVIEWED}, {d, ORIGIN}, "0"*40)
        self.assertFalse(ok); self.assertIn("not under PROME/inbox/processed/", why)

    def test_09b_the_exemption_refuses_a_basename_change(self):
        d = "PROME/inbox/processed/renamed.md"
        self.move(ORIGIN, d)
        ok, why = A._consumed_move_exemption(d, ORIGIN, None, {"verdict": A.REVIEWED}, {d, ORIGIN}, "0"*40)
        self.assertFalse(ok); self.assertIn("basename", why)

    # 10 — every other EXCLUDED addition keeps blocking beside an exempt move
    def test_10_an_exempt_move_does_not_launder_a_neighbouring_excluded_addition(self):
        self.move(); write(self.repo, "scripts/new_tool.py", "print()\n"); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(("PROME/SCRATCH.md", ORIGIN, DEST, "scripts/new_tool.py"))
        self.assertEqual(rc, 1)
        self.assertTrue(any("R100-CONSUMED-MOVE" in l for l in out), "the move itself is still receipted")
        self.assertTrue(any("UNREVIEWED: scripts/new_tool.py" in l for l in out), out)

    # 11 — the --ref HEAD (committed) reader
    def test_11_ref_form_passes_the_committed_move_and_blocks_a_changed_one(self):
        self.move(); self.freeze({DEST: ORIGIN})
        sh("git", "add", "PROME/SCRATCH.md", DEST, cwd=self.repo)   # ORIGIN's removal is already staged by git mv
        sh("git", "commit", "-q", "-m", "PROME: consume", "--", "PROME/SCRATCH.md", ORIGIN, DEST, cwd=self.repo)   # the deletion must be IN the commit, or HEAD holds a copy
        rc, out = self.verify(ref="HEAD"); self.assertEqual(rc, 0, out)
        write(self.repo, DEST, "packet body v1\nedited after\n")
        commit(self.repo, "PROME: edit", [DEST])
        # the frozen SCRATCH is unchanged; only the move's byte-identity is broken
        rc, out = self.verify(ref="HEAD"); self.assertEqual(rc, 1); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)

    # 12 — manifest-only form untouched
    def test_12_manifest_only_form_is_unchanged_by_a_declaration(self):
        self.move()
        self.freeze(None); before = A.verify_review(paths=None)
        self.freeze({DEST: ORIGIN}); after = A.verify_review(paths=None)
        self.assertEqual(before[0], after[0])
        self.assertEqual([l for l in before[1] if "R100" in l], [])
        self.assertEqual([l for l in after[1] if "R100" in l], [], "paths=None never prints a move receipt")

    # 13 — concurrent: origin moved under us
    def test_13_origin_advanced_so_the_packet_is_gone_from_origin_master_blocks(self):
        self.move(); self.freeze({DEST: ORIGIN})
        peer = str(Path(self.tmp.name) / "peer"); sh("git", "clone", "-q", self.bare, peer, cwd=self.tmp.name)
        sh("git", "config", "user.email", "p@p", cwd=peer); sh("git", "config", "user.name", "p", cwd=peer)
        sh("git", "rm", "-q", ORIGIN, cwd=peer); sh("git", "commit", "-q", "-m", "peer: removed", cwd=peer)
        sh("git", "push", "-q", cwd=peer); sh("git", "fetch", "-q", cwd=self.repo)
        rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertTrue(any("on origin" in l for l in out), out)

    # guard falsification: the receipt line cannot appear without ALL legs (induce, watch, restore)
    def test_14_the_receipt_never_prints_on_a_refused_pair(self):
        self.move(); self.freeze({DEST: ORIGIN})
        with patch.object(A, "_origin_blob_id", lambda *a, **k: (None, "forced")):
            rc, out = self.verify()
        self.assertEqual(rc, 1); self.assertFalse(any("R100-CONSUMED-MOVE" in l for l in out))
        rc, out = self.verify(); self.assertEqual(rc, 0, "restored")

    def test_15_cli_declares_the_move_into_the_manifest(self):
        self.move()
        A.main(["--record-review", "--consumed-move", ORIGIN, DEST])
        import json
        d = json.loads((Path(self.repo) / A.REVIEW_FILE).read_text())
        self.assertEqual(d["consumed_moves"], {DEST: ORIGIN}); self.assertEqual(d["verdict"], A.FROZEN)



class ReaderCounterexamples(_Base):
    """Independent reader round 1 (2026-09-25, Opus): 7 ❌ against the first implementation. Each test
    below FAILED against that implementation (checked, not assumed) and is the regression for its ❌."""

    def _peer(self):
        peer = str(Path(self.tmp.name) / "peer")
        if not Path(peer).exists():
            sh("git", "clone", "-q", self.bare, peer, cwd=self.tmp.name)
            sh("git", "config", "user.email", "p@p", cwd=peer); sh("git", "config", "user.name", "p", cwd=peer)
        return peer

    # ❌1 CE1 — an addition that is not a move (the packet was never in local HEAD)
    def test_ce1_a_plain_addition_matching_an_origin_blob_is_not_a_move(self):
        peer = self._peer(); pk = "2026-09-25_from-PEER_new.md"
        commit(peer, "PEER -> PROME", [write(peer, f"PROME/inbox/{pk}", "peer body\n")]); sh("git", "push", "-q", cwd=peer)
        sh("git", "fetch", "-q", cwd=self.repo)                      # fetched, never pulled
        o, d = f"PROME/inbox/{pk}", f"PROME/inbox/processed/{pk}"
        write(self.repo, d, "peer body\n"); sh("git", "add", d, cwd=self.repo)
        self.freeze({d: o})
        rc, out = self.verify(("PROME/SCRATCH.md", o, d)); self.assertEqual(rc, 1, out)
        self.assertFalse(any("R100-CONSUMED" in l for l in out)); self.assertTrue(any("R100 rename" in l for l in out), out)
        sh("git", "add", "PROME/SCRATCH.md", cwd=self.repo); sh("git", "commit", "-q", "-m", "PROME: add", "--", "PROME/SCRATCH.md", d, cwd=self.repo)
        rc, out = self.verify(("PROME/SCRATCH.md", o, d), ref="HEAD"); self.assertEqual(rc, 1, out)

    # ❌2 CE2 — one ORIGIN declared against two DESTs
    def test_ce2_one_origin_two_dests_blocks_both(self):
        self.move(); d2 = f"PROME/inbox/processed/dup/{PKT}"
        write(self.repo, d2, "packet body v1\n"); sh("git", "add", d2, cwd=self.repo)
        self.freeze({DEST: ORIGIN, d2: ORIGIN})
        rc, out = self.verify(("PROME/SCRATCH.md", ORIGIN, DEST, d2)); self.assertEqual(rc, 1, out)
        self.assertFalse(any("R100-CONSUMED" in l for l in out)); self.assertTrue(any("more than one DEST" in l for l in out), out)

    # ❌3 CE3 — local rename + edit to match a NEWER origin blob is not R100
    def test_ce3_rename_plus_edit_matching_a_newer_origin_blob_blocks(self):
        peer = self._peer(); write(peer, ORIGIN, "packet body v2\n"); commit(peer, "PEER: edit", [ORIGIN]); sh("git", "push", "-q", cwd=peer)
        sh("git", "fetch", "-q", cwd=self.repo)
        self.move(); write(self.repo, DEST, "packet body v2\n"); sh("git", "add", DEST, cwd=self.repo)
        self.freeze({DEST: ORIGIN})
        rc, out = self.verify(); self.assertEqual(rc, 1, out); self.assertFalse(any("R100-CONSUMED" in l for l in out))

    # ❌6 CE3b — stale origin/master: a peer's newer edit not yet fetched must not pass
    def test_ce3b_verify_fetches_so_a_stale_tracking_ref_cannot_certify(self):
        self.move(); self.freeze({DEST: ORIGIN})
        peer = self._peer(); write(peer, ORIGIN, "packet body v2\n"); commit(peer, "PEER: edit", [ORIGIN]); sh("git", "push", "-q", cwd=peer)
        rc, out = self.verify()                                       # no local fetch — the tool must do it
        self.assertEqual(rc, 1, out); self.assertTrue(any("differ" in l for l in out), out)

    # ❌4 CE4/CE5 — symlinks
    def test_ce4_a_dangling_symlink_recreated_at_origin_blocks(self):
        self.move(); os.symlink("/nonexistent", Path(self.repo) / ORIGIN); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(); self.assertEqual(rc, 1, out); self.assertTrue(any("file or link" in l for l in out), out)

    def test_ce5_a_symlink_at_dest_blocks(self):
        outside = Path(self.tmp.name) / "outside.md"; outside.write_text("packet body v1\n")
        sh("git", "rm", "-q", ORIGIN, cwd=self.repo)
        (Path(self.repo) / DEST).parent.mkdir(parents=True, exist_ok=True); os.symlink(outside, Path(self.repo) / DEST)
        sh("git", "add", DEST, cwd=self.repo); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(); self.assertEqual(rc, 1, out); self.assertFalse(any("R100-CONSUMED" in l for l in out))

    # ❌5 CE8 — ORIGIN listed, DEST omitted: no silent half-pass
    def test_ce8_a_half_listed_pair_blocks(self):
        self.move(); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(("PROME/SCRATCH.md", ORIGIN)); self.assertEqual(rc, 1, out)
        self.assertTrue(any("both halves" in l for l in out), out)

    # ⚠️9 CE7 — a null value must be CANNOT-EVALUATE, not a crash
    def test_ce7_a_non_string_declaration_is_cannot_evaluate(self):
        import json
        self.move(); self.freeze({DEST: ORIGIN})
        f = Path(self.repo) / A.REVIEW_FILE; d = json.loads(f.read_text()); d["consumed_moves"] = {DEST: None}; f.write_text(json.dumps(d))
        rc, out = self.verify(); self.assertEqual(rc, 2, out)

    # ⚠️10 CE10b — dotted DEST refused even when --paths carries the same string
    def test_ce10b_a_dotted_dest_is_refused(self):
        self.move(); dotted = f"PROME/inbox/processed/../processed/{PKT}"; self.freeze({dotted: ORIGIN})
        rc, out = self.verify(("PROME/SCRATCH.md", ORIGIN, dotted)); self.assertEqual(rc, 1, out)
        self.assertTrue(any("normalised" in l for l in out), out)

    # ⚠️11 CE11/CE11b — the CLI refuses silent input
    def test_ce11_flag_without_record_review_is_an_error(self):
        with self.assertRaises(SystemExit): A.main(["--verify-review", "--consumed-move", ORIGIN, DEST])

    def test_ce11b_duplicate_dest_is_an_error(self):
        self.move()
        with self.assertRaises(SystemExit): A.main(["--record-review", "--consumed-move", ORIGIN, DEST, "--consumed-move", "PROME/inbox/other.md", DEST])

    # an unstaged mv (plain `mv`, not `git mv`) is not a recorded rename
    def test_unstaged_mv_blocks(self):
        (Path(self.repo) / DEST).parent.mkdir(parents=True, exist_ok=True)
        os.rename(Path(self.repo) / ORIGIN, Path(self.repo) / DEST); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(); self.assertEqual(rc, 1, out); self.assertTrue(any("staged" in l for l in out), out)


class ReaderRound2(_Base):
    """Independent reader round 2 (2026-09-25 01:26 ET, Opus): 4 ❌ against the second implementation.
    Each test FAILED against it (checked) and is the regression for its ❌."""

    def _peer(self):
        peer = str(Path(self.tmp.name) / "peer")
        if not Path(peer).exists():
            sh("git", "clone", "-q", self.bare, peer, cwd=self.tmp.name)
            sh("git", "config", "user.email", "p@p", cwd=peer); sh("git", "config", "user.name", "p", cwd=peer)
        return peer

    # ❌A R2-6 — a LOCAL branch named origin/master must not shadow the remote-tracking ref
    def test_r2_6_a_local_branch_named_origin_master_cannot_certify_an_unpushed_packet(self):
        pk = "2026-09-25_from-LOCAL_unpushed.md"; o, d = f"PROME/inbox/{pk}", f"PROME/inbox/processed/{pk}"
        commit(self.repo, "LOCAL -> PROME", [write(self.repo, o, "local only\n")])   # never pushed
        sh("git", "branch", "origin/master", "HEAD", cwd=self.repo)                  # the shadow
        self.move(o, d); self.freeze({d: o})
        sh("git", "add", "PROME/SCRATCH.md", cwd=self.repo)
        sh("git", "commit", "-q", "-m", "PROME: consume", "--", "PROME/SCRATCH.md", o, d, cwd=self.repo)
        rc, out = self.verify(("PROME/SCRATCH.md", o, d), ref="HEAD")
        self.assertEqual(rc, 1, out); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)

    # ❌A R2-7 — no fetch refspec: FETCH_HEAD alone must not certify
    def test_r2_7_without_a_fetch_refspec_a_peers_newer_edit_still_blocks(self):
        sh("git", "config", "--unset-all", "remote.origin.fetch", cwd=self.repo)
        self.move(); self.freeze({DEST: ORIGIN})
        peer = self._peer(); write(peer, ORIGIN, "packet body v2\n"); commit(peer, "PEER: edit", [ORIGIN]); sh("git", "push", "-q", cwd=peer)
        sh("git", "add", "PROME/SCRATCH.md", cwd=self.repo)
        sh("git", "commit", "-q", "-m", "PROME: consume", "--", "PROME/SCRATCH.md", ORIGIN, DEST, cwd=self.repo)
        rc, out = self.verify(ref="HEAD"); self.assertEqual(rc, 1, out); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)

    # ❌B R2-1 — assume-unchanged: the working-tree file differs from the index blob
    # ── round-3 reader (2026-09-25): three holes, one edit
    def test_r3_1_git_replace_cannot_make_an_unpushed_edit_read_as_on_origin(self):
        """❌1 P3: `git replace <origin blob> <local blob>` is honoured by every git object read."""
        write(self.repo, ORIGIN, "packet body LOCAL EDIT\n"); commit(self.repo, "PROME: local edit", [ORIGIN])
        self.move(); self.freeze({DEST: ORIGIN})
        rc0, _ = self.verify(); self.assertEqual(rc0, 1)
        X = sh("git", "rev-parse", f"origin/master:{ORIGIN}", cwd=self.repo).strip()
        Y = sh("git", "rev-parse", f":{DEST}", cwd=self.repo).strip()
        sh("git", "replace", X, Y, cwd=self.repo)
        rc, out = self.verify()
        self.assertEqual(rc, 1, out); self.assertFalse(any("R100-CONSUMED-MOVE" in l for l in out), out)
        rc_ref, out_ref = self.verify(ref="HEAD")          # the committed form too
        self.assertEqual(rc_ref, 1, out_ref)

    def test_r3_2_manifest_only_form_never_fetches_and_prints_the_same_lines(self):
        """❌2 P7: paths=None (`--mark-reviewed`, prome_gate) must not run the declared block."""
        self.move()
        calls = []
        real = A._fetch_origin_sha
        def spy():
            calls.append(1); return real()
        with patch.object(A, "_fetch_origin_sha", spy):
            self.freeze(None); base = A.verify_review(paths=None); n0 = len(calls)
            self.freeze({DEST: ORIGIN}); n1 = len(calls)
            after = A.verify_review(paths=None); n2 = len(calls)
            sh("git", "remote", "set-url", "origin", str(Path(self.tmp.name) / "gone.git"), cwd=self.repo)
            down = A.verify_review(paths=None)
        self.assertEqual((n0, n1 - n0, n2 - n1), (0, 0, 0), calls)     # zero fetches in the manifest-only form
        self.assertEqual(base, after)                                     # a declaration changes nothing there
        self.assertEqual(down, after)                                     # …and neither does a dead remote
        self.assertFalse(any("CANNOT-ESTABLISH" in l for l in down[1]), down)

    def test_r3_3_without_a_remote_named_origin_a_nested_clone_at_dot_origin_cannot_certify(self):
        """❌3 P6: `git fetch origin` falls back to a PATH when no such remote exists."""
        pk = "2026-09-25_from-LOCAL_unpushed.md"; o, dd = f"PROME/inbox/{pk}", f"PROME/inbox/processed/{pk}"
        commit(self.repo, "LOCAL -> PROME", [write(self.repo, o, "local only\n")])       # never pushed
        sh("git", "remote", "remove", "origin", cwd=self.repo)
        sh("git", "clone", "-q", self.repo, str(Path(self.repo) / "origin"), cwd=self.repo)
        (Path(self.repo) / ".git/info/exclude").write_text("origin/\n")
        self.move(o, dd); self.freeze({dd: o})
        rc, out = self.verify(("PROME/SCRATCH.md", o, dd))
        self.assertEqual(rc, 1, out)
        self.assertTrue(any("CANNOT-ESTABLISH" in l and "remote" in l for l in out), out)
        self.assertFalse(any("R100-CONSUMED-MOVE" in l for l in out), out)

    # ── round-4 reader (2026-09-25): the push URL is the origin that matters
    def test_r4_1_a_pushurl_pointing_elsewhere_refuses_the_exemption(self):
        """❌1: fetch from a mirror that holds an unpushed packet, push to the real origin that lacks it."""
        mirror = str(Path(self.tmp.name) / "mirror.git")
        sh("git", "clone", "-q", "--mirror", self.bare, mirror, cwd=self.tmp.name)
        pk = "2026-09-25_from-LOCAL_unpushed.md"; o, dd = f"PROME/inbox/{pk}", f"PROME/inbox/processed/{pk}"
        commit(self.repo, "LOCAL -> PROME", [write(self.repo, o, "mirror only\n")])
        sh("git", "push", "-q", mirror, "master", cwd=self.repo)          # the packet reaches the MIRROR only
        sh("git", "remote", "set-url", "origin", mirror, cwd=self.repo)
        sh("git", "remote", "set-url", "--push", "origin", self.bare, cwd=self.repo)
        self.move(o, dd); self.freeze({dd: o})
        rc, out = self.verify(("PROME/SCRATCH.md", o, dd))
        self.assertEqual(rc, 1, out)
        self.assertTrue(any("differ from push URL" in l for l in out), out)
        self.assertFalse(any("R100-CONSUMED-MOVE" in l for l in out), out)

    def test_r4_2_a_symref_tracking_ref_is_refused_and_head_does_not_move(self):
        """⚠️2: refs/remotes/origin/master as a SYMREF onto the checked-out branch must never be fetched through."""
        self.move(); self.freeze({DEST: ORIGIN})
        commit(self.repo, "PROME: unpushed", [write(self.repo, "PROME/HANDOFF.md", "h\n")])
        head = sh("git", "rev-parse", "HEAD", cwd=self.repo).strip()
        sh("git", "symbolic-ref", "refs/remotes/origin/master", "refs/heads/master", cwd=self.repo)
        rc, out = self.verify(("PROME/SCRATCH.md", ORIGIN, DEST))
        self.assertEqual(rc, 1, out)
        self.assertTrue(any("SYMBOLIC ref" in l for l in out), out)
        self.assertEqual(sh("git", "rev-parse", "HEAD", cwd=self.repo).strip(), head)     # HEAD untouched

    def test_r2_1_assume_unchanged_worktree_edit_blocks(self):
        self.move(); sh("git", "update-index", "--assume-unchanged", DEST, cwd=self.repo)
        write(self.repo, DEST, "packet body v2\n"); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(); self.assertEqual(rc, 1, out); self.assertFalse(any("R100-CONSUMED" in l for l in out), out)

    # the receipt names the fetched commit sha, and the ordinary case still passes after the round-2 rewrite
    def test_receipt_names_the_fetched_origin_commit(self):
        self.move(); self.freeze({DEST: ORIGIN})
        rc, out = self.verify(); self.assertEqual(rc, 0, out)
        remote = sh("git", "rev-parse", "master", cwd=self.bare).strip()
        self.assertTrue(any(remote[:12] in l for l in out if "R100-CONSUMED" in l), out)

if __name__ == "__main__":
    unittest.main()
