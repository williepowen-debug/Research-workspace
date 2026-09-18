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

v2 (2026-09-18, after the independent cold read `wq244cold`, 6 ❌ — every one is now a drill below, VERBATIM):
 ❌1 a `-F` file REWRITTEN by the same command via `>`/`>>`/`tee` (no heredoc) was judged on its STALE on-disk
    contents — a false positive that FAILED CLOSED. Now: a `-F` path that the command redirects into is UNKNOWN.
 ❌2 a relative `-F` path after a `cd` was resolved against the HOOK's cwd. Now: relative + any `cd` ⇒ UNKNOWN.
 ❌4 runtime-assembled messages (`"$MSG"`, `$(cat f)`) were allowed SILENTLY while the docstring promised an
    advisory; `bash -c '…'` bodies and `/usr/bin/git` were invisible. Now: `$`/backtick ⇒ UNKNOWN + advisory;
    `-c` bodies are lifted; git is matched by basename. A script invoked by PATH stays silent — no `git commit`
    is visible to this hook and it says nothing it cannot see (perimeter, below).
 ❌5 combined short flags (`-am`, `-qm`) were reported as "no -m". Now: short-flag clusters are parsed.
 ❌6 a 100-character subject arriving NFD-normalised measured 119 code points. Now: NFC before measuring.
 ⚠️7 `cat <<'M' > x.txt` (redirect AFTER the marker) and `tee x.txt <<'M'` were not read as heredocs. Now they are.

ACCEPTANCE CONDITIONS (WQ-229 — written before the code, in the defect's own terms; the selftest IS this list):
 A1 a `git commit` whose DETERMINABLE subject is >100 characters is BLOCKED before it runs (exit 2, the
    reason names the length, the rule and the subject).
 A2 a subject ≤100 characters is never blocked; length is CHARACTERS after NFC normalisation, never bytes.
 A3 a subject supplied by `-F <file>` is determinable when the SAME Bash command writes that file by
    heredoc (house style, root 4b) or when the literal path already exists on disk AND the command neither
    rewrites it nor changes directory; otherwise the guard fails OPEN with a printed advisory — never a
    block on UNKNOWN, never a block on a file the shell would not read.
 A4 prose inside heredoc BODIES and whitespace-bearing quoted strings is never scanned as a command.
 A5 any hook error (unparseable input, non-object JSON, non-object tool_input, shlex failure, exception)
    exits 0 with a VISIBLE advisory — fail-open, declared.
 A6 the selftest asserts its own size (EXPECTED_DRILLS) and drives the recogniser on VERBATIM shapes
    from this session's own commits and from the cold reader's counterexamples (PAT-172).
 A7 the subject is measured the way `git log --format=%s` measures it: the first paragraph (lines up to
    the first blank line), joined by single spaces, trailing whitespace stripped, NFC-normalised.

PERIMETER (stated so a clean run cannot be over-read): a PreToolUse **Bash** hook sees the literal
command text. A `git commit` that is VISIBLE but whose message is not determinable (a `$VAR`, `$(…)`, a
reused `-C`, an editor commit, a rewritten or unresolvable `-F` path) is ALLOWED WITH AN ADVISORY. A commit
that is NOT visible at all — a script invoked by path, a git alias, a wrapper binary — is allowed SILENTLY:
this hook does not report on what it cannot see. validate_all C1 measures after the fact in both cases.
A `$0`-style literal inside a double-quoted `-m` expands in the shell but is measured here as typed
(±4 chars) — declared residue, a false block needs a subject within that of the cap.

Protocol: stdin = JSON {tool_name, tool_input:{command}}; exit 2 + stderr = BLOCK; exit 0 = allow.
Modes: hook JSON on stdin · `--selftest` (0 = every drill behaved, 1 = a drill failed) ·
`--explain "<shell command>"` (prints the verdict for one command).
"""
import json
import os
import re
import shlex
import sys
import unicodedata

CAP = 100  # root CLAUDE.md 4d / WQ-171 ①
GIT_CMD = re.compile(r"(?:^|[\s;&|('\"])(?:\S*/)?git(?:\s+(?:-C\s+\S+|-c\s+\S+|--git-dir=\S+|--work-tree=\S+|--no-pager|-p|-P|--no-optional-locks))*\s+commit\b")
_HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1")
_REDIR_TARGET = re.compile(r">>?\s*(\"[^\"]+\"|'[^']+'|[^\s;&|<>]+)")
_TEE_TARGET = re.compile(r"\btee\s+(?:-a\s+)?(\"[^\"]+\"|'[^']+'|[^\s;&|<>]+)")
_SHELL_C = re.compile(r"\b(?:bash|sh|zsh|dash)\s+(?:-[a-zA-Z]*c[a-zA-Z]*\s+)(['\"])(.*?)\1", re.S)
_QUOTED = re.compile(r"'([^']*)'|\"([^\"]*)\"")
_CD = re.compile(r"(?:^|[;&|(]\s*|\n\s*)cd\b")
_RUNTIME = re.compile(r"\$[A-Za-z_{(]|`")
_PUNCT = {";", "&&", "||", "|", "&", "(", ")", ">", "<", ">>", "<<", ">&", "<&", "|&"}
_GIT_GLOBAL_WITH_ARG = ("-C", "-c")


def _strip(tok):
    return tok.strip("\"'")


def _heredocs(cmd):
    """(heredoc bodies keyed by their redirect/tee TARGET token, the command with bodies REMOVED).
    A heredoc without a terminator is not a heredoc (git_guard's 2026-09-12 lesson): nothing is skipped."""
    bodies, out, lines, i = {}, [], cmd.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        out.append(ln)
        m = _HEREDOC.search(ln)
        if m:
            term = m.group(2)
            end = next((j for j in range(i + 1, len(lines)) if lines[j].strip() == term), None)
            if end is not None:
                tgt = _REDIR_TARGET.search(ln) or _TEE_TARGET.search(ln)
                if tgt:
                    bodies[_strip(tgt.group(1))] = "\n".join(lines[i + 1:end])
                i = end
        i += 1
    return bodies, "\n".join(out)


def _rewritten_targets(scan):
    """Every path the command redirects or tees into (heredoc bodies already removed)."""
    return {_strip(m.group(1)) for m in _REDIR_TARGET.finditer(scan)} | {_strip(m.group(1)) for m in _TEE_TARGET.finditer(scan)}


def _subject_of(message):
    """git's %s: first paragraph, lines joined by single spaces, trailing whitespace stripped; NFC."""
    lines = message.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    para = []
    for ln in lines:
        if not ln.strip():
            break
        para.append(ln.strip())
    return unicodedata.normalize("NFC", " ".join(para).rstrip())


def _unquote_or_drop(m):
    body = m.group(1) if m.group(1) is not None else m.group(2)
    return body if not re.search(r"\s", body) else " "


def _commit_arg_lists(scan):
    """Every `git … commit <args…>` in the command, as token lists (quotes resolved, $VAR kept literal).
    `bash -c '…'` bodies are lifted first; git is matched by BASENAME so `/usr/bin/git` counts."""
    lifted = _SHELL_C.sub(lambda m: " " + m.group(2) + " ", scan)
    lex = shlex.shlex(lifted, posix=True, punctuation_chars=True)
    lex.whitespace_split = True
    toks = list(lex)
    out, i = [], 0
    while i < len(toks):
        if os.path.basename(toks[i]) == "git":
            j = i + 1
            while j < len(toks) and toks[j].startswith("-"):
                j += 2 if toks[j] in _GIT_GLOBAL_WITH_ARG else 1
            if j < len(toks) and toks[j] == "commit":
                args, k = [], j + 1
                while k < len(toks) and toks[k] not in _PUNCT:
                    args.append(toks[k]); k += 1
                out.append(args)
                i = k
                continue
        i += 1
    return out, lifted


def _file_message(path, bodies, rewritten, has_cd):
    if path == "-":
        return None, "-F - reads stdin — subject not in the command text"
    if path in bodies:
        return bodies[path], "-F heredoc written in this command"
    if not path or _RUNTIME.search(path):
        return None, f"-F {path!r} is not a literal path"
    if path in rewritten:
        return None, f"-F {path!r} is REWRITTEN by this command (> or tee) with no heredoc body — the on-disk content is stale"
    if has_cd and not os.path.isabs(path):
        return None, f"-F {path!r} is relative and the command changes directory — the hook cannot resolve it"
    if os.path.isfile(path):
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(), "-F file already on disk"
    return None, f"-F {path!r} is neither written by a heredoc in this command nor an existing literal path"


def _message_from(args, bodies, rewritten, has_cd):
    """(message text or None, reason). None = UNKNOWN (allow with advisory)."""
    def nxt(i):
        return args[i + 1] if i + 1 < len(args) else ""
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("-C", "-c", "--reuse-message", "--reedit-message") or a.startswith(("--reuse-message=", "--reedit-message=")):
            return None, "message reused from another commit — subject not in the command text"
        if a == "--message":
            return nxt(i), "-m"
        if a.startswith("--message="):
            return a[len("--message="):], "-m"
        if a == "--file":
            return _file_message(nxt(i), bodies, rewritten, has_cd)
        if a.startswith("--file="):
            return _file_message(a[len("--file="):], bodies, rewritten, has_cd)
        if a.startswith("-") and not a.startswith("--") and len(a) > 1:
            cluster = a[1:]                       # -am, -qm, -m<msg>, -F<path>, -aF …
            for j, ch in enumerate(cluster):
                rest = cluster[j + 1:]
                if ch == "m":
                    return (rest if rest else nxt(i)), "-m"
                if ch == "F":
                    return _file_message(rest if rest else nxt(i), bodies, rewritten, has_cd)
                if ch in ("C", "c", "t"):      # reuse / template take an argument — stop here
                    return None, "message reused or templated — subject not in the command text"
        i += 1
    return None, "no -m/-F — editor or amend; nothing to measure pre-execution"


def diagnose(cmd):
    """(verdict, detail). verdict ∈ {'block','allow','unknown'}. Pure except for an on-disk -F read."""
    if not cmd or not isinstance(cmd, str) or not GIT_CMD.search(cmd):
        return "allow", ""
    bodies, scan = _heredocs(cmd)
    probe = _QUOTED.sub(_unquote_or_drop, _SHELL_C.sub(lambda m: " " + m.group(2) + " ", scan))
    if not GIT_CMD.search(probe):
        return "allow", "git commit appears only inside a heredoc body or a quoted string — prose, not a command"
    try:
        lists, lifted = _commit_arg_lists(scan)
    except ValueError as e:
        return "unknown", f"could not tokenise the command ({e})"
    rewritten = _rewritten_targets(scan)
    has_cd = bool(_CD.search(lifted))
    unknowns = []
    if not lists:
        unknowns.append("a git commit is visible but not parseable as a command word")
    for args in lists:
        msg, how = _message_from(args, bodies, rewritten, has_cd)
        if msg is None:
            unknowns.append(how)
            continue
        if _RUNTIME.search(msg):
            unknowns.append(f"runtime-assembled message ({how} contains $VAR, $(…) or a backtick) — subject not determinable pre-execution")
            continue
        subj = _subject_of(msg)
        n = len(subj)
        if n > CAP:
            return "block", (f"⛔ commit_subject_guard BLOCKED: subject is {n} chars, cap {CAP} "
                             f"(root CLAUDE.md Git Protocol 4d / WQ-171 ①; blocking per WQ-244, Will 2026-09-17).\n"
                             f"   subject: «{subj[:140]}{'…' if len(subj) > 140 else ''}»\n"
                             f"   (measured from {how}, as `git log --format=%s` would measure it, NFC)\n"
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


EXPECTED_DRILLS = 46


def selftest():
    import tempfile
    long_subj = "PROME -> VIOLET: WQ-258 LAPSED (no word before the 9/18 open) — disposition returned per L413; L415 + queue updated"  # 115 chars, VERBATIM 16ee79eb2
    exact100 = "PROME: HEARTBEAT am.#1 — BOJ +25bp 7–2, yen weaker anyway · SOFR−IORB −5bp clean · 9/17 credit cells"  # 100 chars, VERBATIM b43dd7546 (110 bytes)
    assert len(long_subj) == 115 and len(exact100) == 100 and len(exact100.encode()) > 100
    accented = unicodedata.normalize("NFC", ("Résumé café naïve Zürich Genève Perú Añejo Håkan Ångström Ørsted Łódź São Tomé Cañón " * 2))[:100]
    nfd100 = unicodedata.normalize("NFD", accented)
    assert len(accented) == 100 and len(nfd100) > 100
    hd = lambda path, subj, body="": f"cat > {path} <<'MSGEOF'\n{subj}\n\n{body}\nMSGEOF\ngit commit PROME/STATUS.md -F {path}"
    stale = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8"); stale.write(long_subj + "\n\nbody\n"); stale.close()
    short = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8"); short.write("short subject\n\nbody\n"); short.close()
    cwd_dir = tempfile.mkdtemp(); open(os.path.join(cwd_dir, "msg.txt"), "w", encoding="utf-8").write(long_subj + "\n")
    cases = [
        (f'git commit PROME/STATUS.md -m "{long_subj}"', "block", "A1 ordinary — VERBATIM 115-char subject from this morning, -m"),
        ('git commit PROME/STATUS.md -m "short"', "allow", "A2 ordinary — short -m"),
        (f'git commit PROME/STATUS.md -m "{exact100}"', "allow", "A2 — exactly 100 CHARACTERS (110 bytes): chars, not bytes"),
        (f'git commit PROME/STATUS.md -m "{exact100}x"', "block", "A1 — 101 chars, one over"),
        (hd('"$SP/msg.txt"', long_subj), "block", "A3 — -F with the heredoc written IN THIS COMMAND (house style), quoted $VAR path"),
        (hd("$SP/msg.txt", "PROME: short subject"), "allow", "A3 — heredoc short subject, unquoted $VAR path"),
        (f'git commit PROME/STATUS.md -F {stale.name}', "block", "A3 — -F literal path already on disk, long, untouched by the command"),
        (f'git commit PROME/STATUS.md -F {short.name}', "allow", "A3 — -F literal path on disk, short"),
        ('git commit PROME/STATUS.md -F "$SP/never_written.txt"', "unknown", "A3 missing information — $VAR path, no heredoc, no file ⇒ UNKNOWN (allow + advisory)"),
        (f'cat > "$SP/a.txt" <<\'EOF\'\n{long_subj}\nEOF\ngit commit PROME/STATUS.md -F "$SP/b.txt"', "unknown", "wrong owner — heredoc targets a DIFFERENT file than -F names ⇒ not used, UNKNOWN"),
        (f'cat > notes.md <<\'EOF\'\nremember: git commit -m "{long_subj}"\nEOF\necho done', "allow", "A4 — `git commit -m <long>` appears ONLY inside a heredoc body (prose)"),
        ('git commit PROME/STATUS.md', "unknown", "editor commit — nothing to measure ⇒ UNKNOWN"),
        ('git commit -C HEAD~1 PROME/STATUS.md', "unknown", "-C reuse ⇒ UNKNOWN"),
        ('ls -la && echo "git commit -m nothing here is prose in quotes"', "allow", "A4 — the phrase sits inside a whitespace-bearing quoted string"),
        (f'git -C /tmp/repo commit -m "{long_subj}"', "block", "git global option before commit is still scanned"),
        (f'git commit --message="{long_subj}"', "block", "--message= form"),
        (f'git commit -m"{long_subj}"', "block", "-m<msg> attached form"),
        (f'git commit -m "first para line one\nline two of the same paragraph\n\nbody" PROME/STATUS.md', "allow", "A7 overlap — two-line first paragraph joins to 55 chars ⇒ allow"),
        ('git commit -m "' + "x" * 60 + '\n' + "y" * 60 + '\n\nbody"', "block", "A7 overlap — two-line first paragraph JOINS to 121 chars ⇒ block, as %s would"),
        (f'git commit -m "short" -m "{long_subj}"', "allow", "overlap — -m twice: the FIRST is the subject, the second a body paragraph"),
        (f'git commit -m "short" PROME/STATUS.md && git commit -m "{long_subj}" PROME/SCRATCH.md', "block", "overlap — two commits in one command, the second is over"),
        ('git commit -m "unbalanced \'quote', "unknown", "A5 — shlex failure ⇒ UNKNOWN, allow + advisory, no exception"),
        ("echo nothing to do with git", "allow", "no git at all — fast path"),
        # ── wq244cold's counterexamples, VERBATIM (2026-09-18) ──
        (f'printf \'%s\\n\' "PROME: short new subject" > {stale.name} && git commit PROME/STATUS.md -F {stale.name}', "unknown", "❌1 — -F file REWRITTEN by this command via printf > (stale 115-char file on disk) ⇒ UNKNOWN, never a block"),
        (f'echo "short" > {stale.name}; git commit PROME/STATUS.md -F {stale.name}', "unknown", "❌1 — echo > form ⇒ UNKNOWN"),
        (f'cat {stale.name} | tee {stale.name}.new; git commit PROME/STATUS.md -F {stale.name}.new', "unknown", "❌1 — tee target ⇒ UNKNOWN"),
        ("cd sub && git commit PROME/STATUS.md -F msg.txt", "unknown", "❌2 — relative -F after a cd, with a stale ./msg.txt in the hook's cwd ⇒ UNKNOWN (cwd drill runs from that dir)"),
        (f'MSG="{long_subj}"; git commit -m "$MSG"', "unknown", "❌4 — runtime-assembled $MSG ⇒ UNKNOWN + advisory (was: silent allow)"),
        (f'bash -c \'git commit -m "{long_subj}"\'', "block", "❌4 — bash -c body lifted and scanned"),
        ('git commit -m "$(cat /tmp/m.txt)"', "unknown", "❌4 — $(…) ⇒ UNKNOWN + advisory"),
        (f'/usr/bin/git commit -m "{long_subj}"', "block", "❌4 — git matched by basename"),
        (f'bash scripts/commit_helper.sh "{long_subj}"', "allow", "PERIMETER — a script by path: no `git commit` visible ⇒ allowed SILENTLY (documented)"),
        (f'git commit -am "{long_subj}"', "block", "❌5 — combined short flags -am (git_guard separately refuses -a)"),
        (f'git commit -qm "{long_subj}"', "block", "❌5 — -qm"),
        (f'git commit PROME/STATUS.md -m "{nfd100}"', "allow", "❌6 — 100 NFC chars arriving NFD-normalised ⇒ allow (NFC before measuring)"),
        (f"cat <<'M' > x.txt\n{long_subj}\n\nbody\nM\ngit commit PROME/STATUS.md -F x.txt", "block", "⚠️7 — redirect AFTER the heredoc marker is still a heredoc target"),
        (f"tee y.txt <<'M'\n{long_subj}\n\nbody\nM\ngit commit PROME/STATUS.md -F y.txt", "block", "⚠️7 — tee as the heredoc target"),
        (f'grep -n "git commit" PROME/STATUS.md || true', "allow", "a search for the phrase — quoted, whitespace-bearing ⇒ prose"),
    ]
    fails = []
    here = os.getcwd()
    for cmd, want, label in cases:
        if label.startswith("❌2"):
            os.chdir(cwd_dir)
        try:
            got, detail = diagnose(cmd)
        finally:
            os.chdir(here)
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
    rc = _handle({"tool_name": "Bash", "tool_input": {"command": f'git commit PROME/STATUS.md -m "{long_subj}"'}})
    ok = rc == 2; print(f"  {'✓' if ok else '✗'} _handle on a 115-char subject -> rc 2 (BLOCK)")
    if not ok: fails.append("_handle did not return 2 on a clean detection")
    rc = _handle({"tool_name": "Edit", "tool_input": {"file_path": "x"}})
    ok = rc == 0; print(f"  {'✓' if ok else '✗'} non-Bash tool -> rc 0")
    if not ok: fails.append("non-Bash tool did not return 0")
    for p in (stale.name, short.name, stale.name + ".new", os.path.join(cwd_dir, "msg.txt")):
        if os.path.exists(p): os.unlink(p)
    os.rmdir(cwd_dir)
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
