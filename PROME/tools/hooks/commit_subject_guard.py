#!/usr/bin/env python3
"""PreToolUse(Bash) hook — BLOCKS a `git commit` whose SUBJECT exceeds 100 characters.

Rule: root CLAUDE.md Git Protocol 4d / WQ-171 ① (Will 2026-09-03) — the subject NAMES the change;
receipts, counts, crc figures and provenance go in the BODY.
Authority to BLOCK: WQ-244, Will 2026-09-17 22:33:18Z Decision Deck APPROVE — "PROME wires a BLOCKING
PreToolUse hook … for root rule 4d (commit subject ≤100 chars) … Hook fails OPEN on its own error,
blocks only on a clean detection — the deliberate exception to fail-closed default."
Why a hook: `scripts/validate_all.py` leg C1 already MEASURES this (11.4% of fleet subjects over the
cap, 9/07–9/13; 12 of the 40 commits before this file was written) and is report-only — the control
was downstream of a working instrument (`finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`).

ACCEPTANCE CONDITIONS (WQ-229 — written before the code, in the defect's own terms; the selftest IS this list):
 A1 a `git commit` whose DETERMINABLE subject is >100 characters is BLOCKED before it runs (exit 2, the
    reason names the length, the rule and the subject).
 A2 a subject ≤100 characters is never blocked; length is CHARACTERS, never bytes — this repo's subjects
    carry multibyte dashes and glyphs, and `wc -c` was the wrong instrument once already (2026-09-18).
 A3 a subject supplied by `-F <file>` is determinable when the SAME Bash command writes that file by
    heredoc (house style, root 4b) or when the literal path already exists on disk; otherwise the guard
    fails OPEN with a printed advisory — never a block on UNKNOWN.
 A4 prose inside heredoc BODIES is never scanned as a command — a message body that mentions
    `git commit -m "<101 chars>"` does not fire.
 A5 any hook error (unparseable input, non-object JSON, non-object tool_input, shlex failure, exception)
    exits 0 with a VISIBLE advisory — fail-open, declared.
 A6 the selftest asserts its own size (EXPECTED_DRILLS) and drives the recogniser on VERBATIM shapes
    from this session's own commits (PAT-172: a self-reported count is not an assertion).
 A7 the subject is measured the way `git log --format=%s` measures it: the first paragraph (lines up to
    the first blank line), joined by single spaces, trailing whitespace stripped — so this guard and
    validate_all C1 agree on the number.

NEIGHBOURS CONSIDERED (WQ-229): ordinary (short/long `-m`) · overlap (a first paragraph spanning two lines
= one subject in git's eyes; two `git commit` calls in one command — each checked; `-m` given twice —
the FIRST is the subject) · wrong owner (a heredoc that targets a DIFFERENT file than `-F` names is not
used; the guard never guesses) · missing information (`-F "$VAR/x"` with no heredoc in the command →
UNKNOWN → allow + advisory; `-C`/`-c <commit>` message reuse → UNKNOWN) · concurrent activity (the hook
reads the command text and, for an on-disk `-F` path, the file as it is NOW; a file rewritten between the
hook and the commit is a TOCTOU the hook cannot see — it fails open by construction and says so here).

PERIMETER (stated so a clean run cannot be over-read): a PreToolUse **Bash** hook sees the literal
command text. A message assembled at runtime (`git commit -m "$MSG"`, `-F <(…)`, `bash -c "…"`, a script
invoked by path) is UNKNOWN to it and is allowed with an advisory. validate_all C1 measures after the fact.

Protocol: stdin = JSON {tool_name, tool_input:{command}}; exit 2 + stderr = BLOCK; exit 0 = allow.
Modes: hook JSON on stdin · `--selftest` (0 = every drill behaved, 1 = a drill failed) ·
`--explain "<shell command>"` (prints the verdict for one command).
"""
import json
import os
import re
import shlex
import sys

CAP = 100  # root CLAUDE.md 4d / WQ-171 ①
GIT = r"\bgit(?:\s+(?:-C\s+\S+|-c\s+\S+|--git-dir=\S+|--work-tree=\S+|--no-pager|-p|-P|--no-optional-locks))*\s+commit\b"
_HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1")
_REDIR_TARGET = re.compile(r">>?\s*(\"[^\"]+\"|'[^']+'|\S+)")
_PUNCT = {";", "&&", "||", "|", "&", "(", ")"}


def _heredocs(cmd):
    """(heredoc bodies keyed by their REDIRECT TARGET token, the command with bodies REMOVED).

    A heredoc without a terminator is not a heredoc (git_guard's 2026-09-12 lesson): nothing is skipped
    and nothing is recorded for it."""
    bodies, out, lines, i = {}, [], cmd.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        out.append(ln)
        m = _HEREDOC.search(ln)
        if m:
            term = m.group(2)
            end = next((j for j in range(i + 1, len(lines)) if lines[j].strip() == term), None)
            if end is not None:
                tgt = _REDIR_TARGET.search(ln[:m.start()])
                if tgt:
                    bodies[tgt.group(1).strip("\"'")] = "\n".join(lines[i + 1:end])
                i = end
        i += 1
    return bodies, "\n".join(out)


def _subject_of(message):
    """git's %s: first paragraph, lines joined by single spaces, trailing whitespace stripped."""
    lines = message.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    para = []
    for ln in lines:
        if not ln.strip():
            break
        para.append(ln.strip())
    return " ".join(para).rstrip()


def _commit_arg_lists(scan):
    """Every `git … commit <args…>` in the command, as token lists (quotes resolved, $VAR kept literal)."""
    lex = shlex.shlex(scan, posix=True, punctuation_chars=True)
    lex.whitespace_split = True
    toks = list(lex)
    out, i = [], 0
    while i < len(toks):
        if toks[i] == "git":
            j = i + 1
            while j < len(toks) and (toks[j].startswith("-")):
                j += 2 if toks[j] in ("-C", "-c") else 1
            if j < len(toks) and toks[j] == "commit":
                args, k = [], j + 1
                while k < len(toks) and toks[k] not in _PUNCT:
                    args.append(toks[k]); k += 1
                out.append(args)
                i = k
                continue
        i += 1
    return out


def _message_from(args, bodies):
    """(message text or None, reason). None = UNKNOWN (allow with advisory); '' counts as known-empty."""
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("-C", "-c", "--reuse-message", "--reedit-message") or a.startswith(("--reuse-message=", "--reedit-message=")):
            return None, "message reused from another commit — subject not in the command text"
        if a == "-m" or a == "--message":
            return (args[i + 1] if i + 1 < len(args) else ""), "-m"
        if a.startswith("--message="):
            return a[len("--message="):], "-m"
        if a.startswith("-m") and len(a) > 2:
            return a[2:], "-m"
        if a in ("-F", "--file") or a.startswith(("--file=",)) or (a.startswith("-F") and len(a) > 2):
            path = a[len("--file="):] if a.startswith("--file=") else (a[2:] if a.startswith("-F") and len(a) > 2 else (args[i + 1] if i + 1 < len(args) else ""))
            if path == "-":
                return None, "-F - reads stdin — subject not in the command text"
            if path in bodies:
                return bodies[path], "-F heredoc written in this command"
            if path and "$" not in path and "`" not in path and os.path.isfile(path):
                with open(path, encoding="utf-8", errors="replace") as fh:
                    return fh.read(), "-F file already on disk"
            return None, f"-F {path!r} is neither written by a heredoc in this command nor an existing literal path"
        i += 1
    return None, "no -m/-F — editor or amend; nothing to measure pre-execution"


def diagnose(cmd):
    """(verdict, detail). verdict ∈ {'block','allow','unknown'}. Pure except for an on-disk -F read."""
    if not cmd or not isinstance(cmd, str) or not re.search(GIT, cmd):
        return "allow", ""
    bodies, scan = _heredocs(cmd)
    if not re.search(GIT, scan):
        return "allow", "git commit appears only inside a heredoc body — prose, not a command"
    try:
        lists = _commit_arg_lists(scan)
    except ValueError as e:
        return "unknown", f"could not tokenise the command ({e})"
    unknowns = []
    for args in lists:
        msg, how = _message_from(args, bodies)
        if msg is None:
            unknowns.append(how)
            continue
        subj = _subject_of(msg)
        n = len(subj)
        if n > CAP:
            return "block", (f"⛔ commit_subject_guard BLOCKED: subject is {n} chars, cap {CAP} "
                             f"(root CLAUDE.md Git Protocol 4d / WQ-171 ①; blocking per WQ-244, Will 2026-09-17).\n"
                             f"   subject: «{subj[:140]}{'…' if len(subj) > 140 else ''}»\n"
                             f"   (measured from {how}, as `git log --format=%s` would measure it)\n"
                             f"   The subject NAMES the change; receipts, counts, shas and provenance go in the BODY. "
                             f"Cut it to ≤{CAP} characters and re-run.\n")
    if unknowns:
        return "unknown", "; ".join(unknowns)
    return "allow", ""


def _handle(data):
    """Every dereference of `data` is inside the try. Never raises for a non-object input (L294 F-6)."""
    try:
        if not isinstance(data, dict):
            raise TypeError(f"hook input is {type(data).__name__}, expected an object")
        if data.get("tool_name") != "Bash":
            return 0
        ti = data.get("tool_input")
        if ti is not None and not isinstance(ti, dict):
            raise TypeError(f"tool_input is {type(ti).__name__}, expected an object")
        cmd = (ti or {}).get("command", "") or ""
        verdict, detail = diagnose(cmd)
    except Exception as e:
        sys.stderr.write(f"⚠️ commit_subject_guard: {type(e).__name__}: {e} — ALLOWING without a check. "
                         "Fail-open, DECLARED (WQ-244). validate_all C1 measures after the fact.\n")
        return 0
    if verdict == "block":
        sys.stderr.write(detail)
        return 2
    if verdict == "unknown":
        sys.stderr.write(f"⚠️ commit_subject_guard: subject NOT determinable pre-execution ({detail}) — "
                         "ALLOWING. Keep the subject ≤100 chars; validate_all C1 measures after the fact.\n")
    return 0


EXPECTED_DRILLS = 32


def selftest():
    long_subj = "PROME -> VIOLET: WQ-258 LAPSED (no word before the 9/18 open) — disposition returned per L413; L415 + queue updated"  # 115 chars, VERBATIM 16ee79eb2
    exact100 = "PROME: HEARTBEAT am.#1 — BOJ +25bp 7–2, yen weaker anyway · SOFR−IORB −5bp clean · 9/17 credit cells"  # 100 chars, VERBATIM b43dd7546 (111 BYTES)
    assert len(long_subj) == 115 and len(exact100) == 100 and len(exact100.encode()) > 100
    hd = lambda path, subj, body="": f"cat > {path} <<'MSGEOF'\n{subj}\n\n{body}\nMSGEOF\ngit commit PROME/STATUS.md -F {path}"
    import tempfile
    tmp = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8"); tmp.write(long_subj + "\n\nbody\n"); tmp.close()
    tmp2 = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8"); tmp2.write("short subject\n\nbody\n"); tmp2.close()
    cases = [
        (f'git commit PROME/STATUS.md -m "{long_subj}"', "block", "A1 ordinary — VERBATIM 115-char subject from this morning, -m"),
        ('git commit PROME/STATUS.md -m "short"', "allow", "A2 ordinary — short -m"),
        (f'git commit PROME/STATUS.md -m "{exact100}"', "allow", "A2 — exactly 100 CHARACTERS (111 bytes): chars, not bytes"),
        (f'git commit PROME/STATUS.md -m "{exact100}x"', "block", "A1 — 101 chars, one over"),
        (hd('"$SP/msg.txt"', long_subj), "block", "A3 — -F with the heredoc written IN THIS COMMAND (house style), quoted $VAR path"),
        (hd("$SP/msg.txt", "PROME: short subject"), "allow", "A3 — heredoc short subject, unquoted $VAR path"),
        (f'git commit PROME/STATUS.md -F {tmp.name}', "block", "A3 — -F literal path already on disk, long"),
        (f'git commit PROME/STATUS.md -F {tmp2.name}', "allow", "A3 — -F literal path on disk, short"),
        ('git commit PROME/STATUS.md -F "$SP/never_written.txt"', "unknown", "A3 missing information — $VAR path, no heredoc, no file ⇒ UNKNOWN (allow + advisory)"),
        (f'cat > "$SP/a.txt" <<\'EOF\'\n{long_subj}\nEOF\ngit commit PROME/STATUS.md -F "$SP/b.txt"', "unknown", "wrong owner — heredoc targets a DIFFERENT file than -F names ⇒ not used, UNKNOWN"),
        (f'cat > notes.md <<\'EOF\'\nremember: git commit -m "{long_subj}"\nEOF\necho done', "allow", "A4 — `git commit -m <long>` appears ONLY inside a heredoc body (prose)"),
        ('git commit PROME/STATUS.md', "unknown", "editor commit — nothing to measure ⇒ UNKNOWN"),
        ('git commit -C HEAD~1 PROME/STATUS.md', "unknown", "-C reuse ⇒ UNKNOWN"),
        ('ls -la && echo "git commit -m nothing here is prose in quotes"', "allow", "no real git commit — the phrase sits inside an echo string"),
        (f'git -C /tmp/repo commit -m "{long_subj}"', "block", "git global option before commit is still scanned"),
        (f'git commit --message="{long_subj}"', "block", "--message= form"),
        (f'git commit -m"{long_subj}"', "block", "-m<msg> attached form"),
        (f'git commit -m "first para line one\nline two of the same paragraph\n\nbody" PROME/STATUS.md', "allow", "A7 overlap — two-line first paragraph joins to 55 chars ⇒ allow"),
        ('git commit -m "' + "x" * 60 + '\n' + "y" * 60 + '\n\nbody"', "block", "A7 overlap — two-line first paragraph JOINS to 121 chars ⇒ block, as %s would"),
        (f'git commit -m "short" -m "{long_subj}"', "allow", "overlap — -m twice: the FIRST is the subject, the second a body paragraph"),
        (f'git commit -m "short" PROME/STATUS.md && git commit -m "{long_subj}" PROME/SCRATCH.md', "block", "overlap — two commits in one command, the second is over"),
        (f'MSG="{long_subj}"; git commit -m "$MSG"', "allow", "PERIMETER — message assembled at runtime is a 5-char literal `$MSG` to this hook; allowed, validate_all C1 catches it"),
        ('git commit -m "unbalanced \'quote', "unknown", "A5 — shlex failure ⇒ UNKNOWN, allow + advisory, no exception"),
        ("echo nothing to do with git", "allow", "no git at all — fast path"),
    ]
    fails = []
    for cmd, want, label in cases:
        got, detail = diagnose(cmd)
        mark = "✓" if got == want else "✗"
        if got != want:
            fails.append(f"{label}: expected {want}, got {got} ({detail[:80]}) — {cmd[:70]!r}")
        print(f"  {mark} {got:7} want={want:7}  {label}")
    for bad in ([], None, "ok", 3, {"tool_name": "Bash"}, {"tool_name": "Bash", "tool_input": "str"}):
        try:
            rc = _handle(bad); ok = rc == 0
        except Exception as e:
            ok = False; fails.append(f"malformed input {bad!r} raised {type(e).__name__}")
        print(f"  {'✓' if ok else '✗'} malformed hook input {str(bad)[:24]:26} -> rc 0, no exception")
    # A5 as a whole-hook drill: the blocking path really returns 2 through _handle
    rc = _handle({"tool_name": "Bash", "tool_input": {"command": f'git commit PROME/STATUS.md -m "{long_subj}"'}})
    ok = rc == 2; print(f"  {'✓' if ok else '✗'} _handle on a 115-char subject -> rc 2 (BLOCK)")
    if not ok: fails.append("_handle did not return 2 on a clean detection")
    rc = _handle({"tool_name": "Edit", "tool_input": {"file_path": "x"}})
    ok = rc == 0; print(f"  {'✓' if ok else '✗'} non-Bash tool -> rc 0")
    if not ok: fails.append("non-Bash tool did not return 0")
    os.unlink(tmp.name); os.unlink(tmp2.name)
    total = len(cases) + 6 + 2
    if total != EXPECTED_DRILLS:
        fails.append(f"SUITE SIZE CHANGED: {total} drill(s) ran, EXPECTED_DRILLS says {EXPECTED_DRILLS} (PAT-172)")
    for f in fails:
        print(f"  ❌ {f}")
    print(f"{'✅' if not fails else '❌'} COMMIT-SUBJECT-GUARD SELFTEST {total - len(fails)}/{total} drill(s) behaved")
    return 0 if not fails else 1


def main(argv):
    args = argv[1:]
    if "--selftest" in args:
        return selftest()
    if "--explain" in args:
        i = args.index("--explain")
        v, d = diagnose(args[i + 1] if i + 1 < len(args) else "")
        print(f"{v}: {d or 'no over-cap subject determinable'}")
        return 0
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"⚠️ commit_subject_guard: could not parse hook input ({type(e).__name__}) — ALLOWING. Fail-open, declared.\n")
        return 0
    return _handle(data)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
