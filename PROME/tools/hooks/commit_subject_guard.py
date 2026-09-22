#!/usr/bin/env python3
"""PreToolUse(Bash) hook — BLOCKS a `git commit` whose SUBJECT exceeds 100 characters.

Rule: root CLAUDE.md Git Protocol 4d / WQ-171 ① (Will 2026-09-03) — the subject NAMES the change;
receipts, counts, crc figures and provenance go in the BODY.
Authority to BLOCK: WQ-244, Will 2026-09-17 22:33:18Z Decision Deck APPROVE — "PROME wires a BLOCKING
PreToolUse hook … for root rule 4d (commit subject ≤100 chars) … Hook fails OPEN on its own error,
blocks only on a clean detection — the deliberate exception to fail-closed default."
Why a hook: `scripts/validate_all.py` leg C1 already MEASURES this (11.4% of fleet subjects over the
cap, 9/07–9/13) and is report-only — the control was downstream of a working instrument.

v3 (2026-09-18, after the SECOND independent cold read `wq244cold2`, 6 ❌ on this file — each a drill below):
 ❌1 a `>>`-APPEND heredoc's body was measured as the subject while the real subject was already on disk (FAIL-CLOSED).
    Now: an append heredoc or `tee -a` makes the path UNKNOWN.
 ❌2 a heredoc-written path later REWRITTEN by a redirect in the same command was judged on the heredoc (bodies were
    checked before rewrites). Now: a path that is both a heredoc target and a redirect target elsewhere is UNKNOWN.
 ❌3 the heredoc terminator test was looser than bash (`strip() == term`), so an INDENTED terminator quoted inside a body
    resumed scanning prose as commands. Now: `<<WORD` needs the exact line; `<<-WORD` strips leading tabs only.
 ❌4 a relative `-F` path with no `cd` was read from the HOOK's cwd, which is not the shell's persistent cwd.
    Now: only ABSOLUTE literal paths are ever read from disk; every relative path is UNKNOWN.
 ❌5 a second `git commit` on a NEW LINE was swallowed as arguments of the first (silent bypass). Now: the whole
    text is tokenised at once and a commit's argument scan stops at the next `git` command word (v3, restated in v5
    after r4 ❌8 — the earlier "per line" wording described code that never shipped).
 ❌6 `eval "git commit …"` was read as quoted prose (silent bypass). Now: `eval` bodies are lifted like `-c` bodies;
    `$GIT commit` is UNKNOWN with an advisory.
v6 (2026-09-18, after the FIFTH independent cold read `wq244cold5`, 7 ❌ on this file — the LAST pass today; the
   convergence question is WQ-263, Will's):
 ❌1 `python3 - > msg.txt <<'PYEOF' … PYEOF; git commit -F msg.txt` — the heredoc is the INTERPRETER's stdin and the
    file gets its stdout; the guard measured the python source (FALSE POSITIVE). Now: a heredoc body is a message
    only when the heredoc line's command word is `cat` or `tee`; any other writer makes the target UNKNOWN.
 ❌2 `git commit --dry-run … -m "<115>"` was blocked; a dry run commits nothing (FALSE POSITIVE). Now: allowed.
 ❌3 `echo git commit -m "<115>" >> notes.md` was blocked — no command-position test (FALSE POSITIVE; the wrapper next
    door learned this on round 2). Now: `git` must be the command word of its segment (after `cd …&&`, env
    assignments, `time`-class prefixes); a `git commit` that is an ARGUMENT of echo/printf/grep is prose.
 ❌6 ``out=`git commit -m "<115>"` `` — the backtick opener was invisible (silent bypass). Now: backticks are lifted.
 ❌7 `bash -c $'git commit …'` — ANSI-C normalisation ran AFTER the `-c` lift (silent bypass). Now: before.
 ❌8 `--file -` (space form) was not read as stdin. Now it is.
 ❌11/❌12 docstring: the v4 note contradicted v5 and a wrapper-side perimeter sentence sat in this file — corrected.
 Neighbours found by the author while fixing (not a reader's): `-n` is --no-verify, never dry-run; `{ … }` / `if` /
    `!` heads are transparent (git still runs); backslash-newline is joined as bash joins it; prose piped to a
    shell (`echo git commit … | bash`, xargs) is UNKNOWN, never allow.
v5 (2026-09-18, after the FOURTH independent cold read `wq244cold4`, 4 ❌ on this file — each a drill below):
 ❌1 `$'…'` with backslash ESCAPES (`$'subject\n\nbody'`) was measured as one 230-char line — a FALSE POSITIVE. Now: any
    ANSI-C message carrying a backslash is UNKNOWN + advisory; escape-free `$'…'` is measured as plain single quotes.
 ❌2 two heredocs feeding two `-F -` commits shared one stdin body, so the LAST body was attributed to BOTH (silent
    bypass). Now: more than one stdin heredoc in a command makes every `-F -` UNKNOWN.
 ❌9 the FIRST line was left-stripped; git keeps a subject's leading whitespace. Now: nothing is left-stripped
    (supersedes v4's "only the first line is left-stripped" below).
 ❌7/❌8 two docstring claims the code did not hold (a "disk read" exception in diagnose's own docstring; a per-line
    tokeniser that v3 replaced) — corrected below and in the v3 note.
v4 (2026-09-18, after the THIRD independent cold read `wq244cold3`, 5 ❌ on this file — each a drill below):
 ❌1 an INDENTED continuation line of the first paragraph was under-counted (each line was stripped; git keeps the
    leading whitespace of continuation lines when it joins them). v4: only the first line was left-stripped;
    v5 removed that too (see r4 ❌9 above).
 ❌2 `-F -` / `--file=-` with the message heredoc on stdin was reported UNKNOWN though fully determinable. Now: a
    heredoc on a `git commit … -F -` line is that commit's message.
 ❌3 the absolute-path ON-DISK read still blocked when the same command rewrote the file under ANOTHER SPELLING
    (`./msg.txt`, `$HOME/../..`, a `python3 -` writer, `sed -i`) — path-string comparison cannot see that. Now: this
    hook NEVER reads a message file from disk; a `-F` message is determinable ONLY from a WRITE heredoc in the same
    command (or `-F -`). Everything else is UNKNOWN + advisory. A3 is narrowed accordingly.
 ❌4 `$'…'` ANSI-C quoting left a phantom `$` in the measured text. Now: `$'` is normalised to `'` before tokenising
    (escape sequences inside may differ by a character — declared).
 ❌8 (wiring) the settings command `python3 "$(git rev-parse --show-toplevel)/…"` would exit 2 — the BLOCK code — if
    the root ever failed to resolve, blocking every Bash command. Now: the wiring tests the script path first and
    fails OPEN with an advisory when it is missing.
v2 (after `wq244cold`): stale-file `-F` rewrites, `cd` + relative `-F`, `$VAR`/`$(…)` messages, `bash -c` bodies,
`/usr/bin/git`, combined short flags (`-am`), NFC measurement, redirect-after-marker and `tee` heredoc targets.

ACCEPTANCE CONDITIONS (WQ-229; the selftest IS this list):
 A1 a `git commit` whose DETERMINABLE subject is >100 characters is BLOCKED before it runs (exit 2, the reason names
    the length, the rule and the subject) — including a second commit on a later line and an `eval`/`bash -c` body.
 A2 a subject ≤100 characters is never blocked; length is CHARACTERS after NFC normalisation, never bytes.
 A3 a subject supplied by `-F <file>` is determinable ONLY when the SAME Bash command writes that file by a WRITE
    heredoc that nothing else in the command rewrites, or by `-F -` with the heredoc on stdin; this hook never
    reads a message file from disk; every other `-F` is UNKNOWN — allow + advisory.
 A4 prose inside heredoc BODIES (bash-exact terminators) and whitespace-bearing quoted strings is never scanned as
    a command.
 A5 any hook error (unparseable input, non-object JSON, non-object tool_input, shlex failure, exception) exits 0
    with a VISIBLE advisory — fail-open, declared.
 A6 the selftest asserts its own size (EXPECTED_DRILLS) and drives the recogniser on VERBATIM shapes from this
    session's own commits and from both cold readers' counterexamples (PAT-172).
 A7 the subject is measured the way `git log --format=%s` measures it: first paragraph joined by single spaces,
    ALL leading whitespace kept (first line included), trailing whitespace stripped, NFC-normalised.

PERIMETER: a PreToolUse **Bash** hook sees the literal command text. A `git commit` that is VISIBLE but whose message
is not determinable is ALLOWED WITH AN ADVISORY. A commit that is NOT visible — a script invoked by path, a git alias,
a wrapper binary, a command assembled at runtime beyond `$GIT` — is allowed SILENTLY. validate_all C1 measures after
the fact in both cases. A `$0`-style literal inside a double-quoted `-m` expands in the shell but is measured here as
typed (±4 chars) — declared residue. Unbalanced quoting anywhere in the command makes the whole command UNKNOWN.
Perimeter left after five independent reads (declared, not fixed): a `$GIT`/alias-held git is UNKNOWN or unseen;
a single-quoted `$` in a subject is UNKNOWN; a commit inside a construct this hook does not lift is unseen.

Protocol: stdin = JSON {tool_name, tool_input:{command}}; exit 2 + stderr = BLOCK; exit 0 = allow.
Modes: hook JSON on stdin · `--selftest` · `--explain "<shell command>"`.
"""
import json
import os
import re
import shlex
import sys
import unicodedata

CAP = 100  # root CLAUDE.md 4d / WQ-171 ①
GIT_CMD = re.compile(r"(?:^|[\s;&|('\"`])(?:\S*/)?git(?:\s+(?:-C\s+\S+|-c\s+\S+|--git-dir=\S+|--work-tree=\S+|--no-pager|-p|-P|--no-optional-locks))*\s+commit\b")
_HEREDOC = re.compile(r"<<(-?)\s*(['\"]?)(\w+)\2")
_REDIR_TARGET = re.compile(r">>?\s*(\"[^\"]+\"|'[^']+'|[^\s;&|<>]+)")
_APPEND = re.compile(r">>\s*(\"[^\"]+\"|'[^']+'|[^\s;&|<>]+)|\btee\s+-a\b")
_TEE_TARGET = re.compile(r"\btee\s+(?:-a\s+)?(\"[^\"]+\"|'[^']+'|[^\s;&|<>]+)")
_SHELL_C = re.compile(r"\b(?:bash|sh|zsh|dash)\s+(?:-[a-zA-Z]*c[a-zA-Z]*\s+)(['\"])(.*?)\1", re.S)
_EVAL = re.compile(r"\beval\s+(['\"])(.*?)\1", re.S)
_QUOTED = re.compile(r"'([^']*)'|\"([^\"]*)\"")
_RUNTIME = re.compile(r"\$[A-Za-z_{(]|`")
_GITVAR = re.compile(r"\$\{?GIT\}?\s+commit\b")
_STDIN_F = re.compile(r"(?:^|\s)(?:-F\s*-|--file[= ]-)(?=\s|$)")
_ANSIC = re.compile(r"\$'((?:[^'\\]|\\.)*)'")
_ANSIC_ESCAPED = "__ANSI_C_WITH_ESCAPES__"
_STDIN_AMBIGUOUS = "__MORE_THAN_ONE_STDIN_HEREDOC__"
_PUNCT_CHARS = set(";&|<>()\n")             # newline INCLUDED: a command on its own line is its own segment (r5 ❌3 fix, r2 ❌5 kept)
_PIPE_TO_SHELL = re.compile(r"\|\s*(?:\S*/)?(?:ba|z|da)?sh\b|\bxargs\b")
_GIT_GLOBAL_WITH_ARG = ("-C", "-c")
_PREFIX_CMDS = ("time", "env", "nice", "sudo", "timeout", "nohup", "stdbuf", "exec", "command")
_MSG_FLAGS = ("-m", "-F", "--message", "--file")
_TRANSPARENT = {"{", "}", "!", "if", "then", "else", "elif", "do", "while", "until"}   # heads that RUN what follows
_WRITERS = ("cat", "tee")


def _strip(tok):
    return tok.strip("\"'")


def _is_punct(tok):
    return bool(tok) and set(tok) <= _PUNCT_CHARS


def _ansic_norm(text):
    """`$'…'` → `'…'`; a body with backslash escapes becomes the sentinel (the shell decodes, this hook does not)."""
    return _ANSIC.sub(lambda m: "'" + _ANSIC_ESCAPED + "'" if "\\" in m.group(1) else "'" + m.group(1) + "'", text)


def _is_dry_run(args):
    """`--dry-run` as a FLAG of this commit (not as a message value). `-n` is --no-verify, never dry-run."""
    for i, a in enumerate(args):
        if a == "--dry-run" and not (i and (args[i - 1] in _MSG_FLAGS or (args[i - 1].startswith("-") and not args[i - 1].startswith("--") and args[i - 1][-1] in "mF"))):
            return True
    return False


def _lift(text):
    """Lift `bash -c '…'` / `eval '…'` bodies out of their quotes and drop backtick fences (r5 ❌6) so what the shell
    would RUN is scanned as commands."""
    text = _SHELL_C.sub(lambda m: " " + m.group(2) + " ", text)
    text = _EVAL.sub(lambda m: " " + m.group(2) + " ", text)
    return text.replace("`", " ")


def _heredocs(cmd):
    """(write-heredoc bodies keyed by target, targets of APPEND heredocs, the command with bodies REMOVED,
    the line indexes of the heredoc lines in that scan text). Terminators are bash-exact: `<<W` needs the line
    to equal W; `<<-W` strips leading tabs only. A heredoc without a terminator is not a heredoc."""
    bodies, appended, out, hd_idx, lines, i = {}, set(), [], set(), cmd.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        out.append(ln)
        m = _HEREDOC.search(ln)
        if m:
            dash, term = m.group(1) == "-", m.group(3)
            end = next((j for j in range(i + 1, len(lines)) if (lines[j].lstrip("\t") if dash else lines[j]) == term), None)
            if end is not None:
                hd_idx.add(len(out) - 1)
                tgt = _REDIR_TARGET.search(ln) or _TEE_TARGET.search(ln)
                if tgt:
                    path = _strip(tgt.group(1))
                    seg = re.split(r"&&|\|\||;|(?<!\|)\|(?!\|)", ln[:m.start()])[-1].split()
                    while seg and (seg[0] in ("(", "{") or re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", seg[0]) or os.path.basename(seg[0]) in _PREFIX_CMDS):
                        seg.pop(0)
                    writer = os.path.basename(seg[0]) if seg else ""
                    if _APPEND.search(ln) or writer not in _WRITERS:
                        appended.add(path)          # appended, or written by an interpreter whose stdin the heredoc feeds (r5 ❌1)
                    else:
                        bodies[path] = "\n".join(lines[i + 1:end])
                elif GIT_CMD.search(ln) and _STDIN_F.search(ln):
                    bodies["-"] = _STDIN_AMBIGUOUS if "-" in bodies else "\n".join(lines[i + 1:end])
                i = end
        i += 1
    return bodies, appended, "\n".join(out), hd_idx


def _rewritten_targets(scan, hd_idx):
    """Every path the command redirects or tees into on lines OTHER than heredoc lines."""
    out = set()
    for k, ln in enumerate(scan.split("\n")):
        if k in hd_idx:
            continue
        out |= {_strip(m.group(1)) for m in _REDIR_TARGET.finditer(ln)}
        out |= {_strip(m.group(1)) for m in _TEE_TARGET.finditer(ln)}
    return out


def _subject_of(message):
    lines = message.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    para = []
    for ln in lines:
        if not ln.strip():
            break
        para.append(ln.rstrip())
    return unicodedata.normalize("NFC", " ".join(para).rstrip())


def _unquote_or_drop(m):
    body = m.group(1) if m.group(1) is not None else m.group(2)
    return body if not re.search(r"\s", body) else " "


def _commit_arg_lists(scan, raw=False):
    """Every `git … commit <args…>` in the command, as token lists. The whole text is tokenised at once (a quoted
    message may span lines), and a commit's argument scan STOPS at punctuation OR at the next `git` command word —
    so a second commit on a new line (r2 ❌5) is its own command, never swallowed as arguments of the first."""
    # WQ-263 CATO fix: raw=True parses the command AS TYPED — no `bash -c`/`eval`/backtick lift, no ANSI-C
    # normalisation — so a commit found only by reconstruction can be told apart from one git will certainly run.
    lifted = (scan if raw else _lift(_ansic_norm(scan))).replace("\\\n", " ")   # r3 ❌4 / r4 ❌1 / r5 ❌7 (ANSI-C first, then lift); backslash-newline joined as bash joins it
    lex = shlex.shlex(lifted, posix=True, punctuation_chars="".join(sorted(_PUNCT_CHARS)))
    lex.whitespace = " \t\r"                  # newline is punctuation, not whitespace: a new line is a new segment
    lex.whitespace_split = True
    toks = list(lex)                          # ValueError propagates → UNKNOWN
    out, i, prose = [], 0, 0
    seg_start = 0                                    # index of the first token of the current segment
    while i < len(toks):
        if _is_punct(toks[i]):
            seg_start = i + 1
        if os.path.basename(toks[i]) == "git":
            # r5 ❌3: `git` must be the COMMAND WORD of its segment. The segment's head (first token after env
            # assignments) must be git itself or a PREFIX command that runs its arguments (`sudo -u x git …`,
            # `timeout 30 git …`); under any other head — echo, printf, grep — `git commit` is an ARGUMENT: prose.
            head = next((t for t in toks[seg_start:i] if not (re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", t) or t in _TRANSPARENT)), None)
            if head is not None and os.path.basename(head) not in _PREFIX_CMDS:
                prose += 1
                i += 1
                continue
            j = i + 1
            while j < len(toks) and toks[j].startswith("-"):
                j += 2 if toks[j] in _GIT_GLOBAL_WITH_ARG else 1
            if j < len(toks) and toks[j] == "commit":
                args, k = [], j + 1
                while k < len(toks) and not _is_punct(toks[k]) and os.path.basename(toks[k]) != "git":
                    args.append(toks[k]); k += 1
                out.append((args, head is None))     # WQ-263: True ⇔ `git` is the literal command word, no prefix command
                i = k
                continue
        i += 1
    return out, lifted, prose


def _file_message(path, bodies, appended, rewritten):
    if path == "-":
        if bodies.get("-") == _STDIN_AMBIGUOUS:
            return None, "-F - with MORE THAN ONE stdin heredoc in this command — which body is whose is not determinable"
        if "-" in bodies:
            return bodies["-"], "-F - with the heredoc on stdin in this command"
        return None, "-F - reads stdin and no heredoc feeds it in this command"
    if path in appended:
        return None, f"-F {path!r} is APPENDED to by a heredoc in this command — the subject is whatever is already on disk"
    if path in bodies and path in rewritten:
        return None, f"-F {path!r} is heredoc-written and then REWRITTEN by a later redirect in this command"
    if path in bodies:
        return bodies[path], "-F heredoc written in this command"
    if not path or _RUNTIME.search(path):
        return None, f"-F {path!r} is not a literal path"
    if path in rewritten:
        return None, f"-F {path!r} is REWRITTEN by this command (> or tee) with no heredoc body"
    return None, f"-F {path!r} is not written by a heredoc in this command — this hook never reads a message file from disk (a same-command writer under another spelling made that unsafe)"


def _message_from(args, bodies, appended, rewritten):
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
            return _file_message(nxt(i), bodies, appended, rewritten)
        if a.startswith("--file="):
            return _file_message(a[len("--file="):], bodies, appended, rewritten)
        if a.startswith("-") and not a.startswith("--") and len(a) > 1:
            cluster = a[1:]
            for j, ch in enumerate(cluster):
                rest = cluster[j + 1:]
                if ch == "m":
                    return (rest if rest else nxt(i)), "-m"
                if ch == "F":
                    return _file_message(rest if rest else nxt(i), bodies, appended, rewritten)
                if ch in ("C", "c", "t"):
                    return None, "message reused or templated — subject not in the command text"
        i += 1
    return None, "no -m/-F — editor or amend; nothing to measure pre-execution"


def diagnose(cmd):
    """(verdict, detail). verdict ∈ {'block','allow','unknown'}. Pure: this hook never reads a file from disk."""
    if not cmd or not isinstance(cmd, str):
        return "allow", ""
    if not GIT_CMD.search(cmd) and not _GITVAR.search(cmd):
        return "allow", ""
    bodies, appended, scan, hd_idx = _heredocs(cmd)
    probe = _QUOTED.sub(_unquote_or_drop, _lift(_ansic_norm(scan)))
    gitvar = bool(_GITVAR.search(probe))
    if not GIT_CMD.search(probe) and not gitvar:
        return "allow", "git commit appears only inside a heredoc body or a quoted string — prose, not a command"
    try:
        pairs, lifted, prose = _commit_arg_lists(scan)
    except ValueError as e:
        return "unknown", f"could not tokenise the command ({e})"
    lists = [a for a, _ in pairs]
    try:                                               # WQ-263: commits git will CERTAINLY run, from the as-typed parse
        certain = [tuple(a) for a, is_git in _commit_arg_lists(scan, raw=True)[0] if is_git]
    except ValueError:
        certain = []
    if prose and not lists and not gitvar:
        if _PIPE_TO_SHELL.search(lifted):
            return "unknown", "git commit appears as an argument of another command that is piped to a shell — subject not determinable"
        return "allow", "git commit appears only as an argument of another command (echo/printf/grep) — prose, not a command"
    rewritten = _rewritten_targets(scan, hd_idx)
    unknowns = []
    if gitvar:
        unknowns.append("git is invoked through a variable ($GIT) — the command word is not literal")
    if not lists and not gitvar:
        unknowns.append("a git commit is visible but not parseable as a command word")
    for args in lists:
        if _is_dry_run(args):
            continue                                  # r5 ❌2: a dry run commits nothing (`-n` is --no-verify, NOT dry-run)
        msg, how = _message_from(args, bodies, appended, rewritten)
        if msg is None:
            unknowns.append(how)
            continue
        if _RUNTIME.search(msg):
            unknowns.append(f"runtime-assembled message ({how} contains $VAR, $(…) or a backtick) — subject not determinable pre-execution")
            continue
        if _ANSIC_ESCAPED in msg:
            unknowns.append("ANSI-C quoted message with backslash escapes — the shell decodes them, this hook does not; subject not determinable")
            continue
        subj = _subject_of(msg)
        n = len(subj)
        if n > CAP and not (how == "-m" and tuple(args) in certain):
            # WQ-263 (Will 2026-09-22 "with CATO fix"): over the cap, but the commit was found by INFERENCE — a -F /
            # heredoc message, a prefix command (env/timeout/sudo/command…), or a bash -c/eval/backtick/$'…' lift. A
            # recogniser that is unsure what runs must not block: WARN, exit 0. validate_all C1 measures after the fact.
            unknowns.append(f"OVER CAP ({n} chars > {CAP}) but inferred ({how}; command word not a literal top-level `git`"
                            f" or message not a plain -m) — NOT blocked, WQ-263. Subject: «{subj[:100]}{'…' if len(subj) > 100 else ''}»")
            continue
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


EXPECTED_DRILLS = 83


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
        (hd('"$SP/msg.txt"', long_subj), "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: A3 — -F with the WRITE heredoc in this command (house style), quoted $VAR path"),
        (hd("$SP/msg.txt", "PROME: short subject"), "allow", "A3 — heredoc short subject, unquoted $VAR path"),
        (f'git commit PROME/STATUS.md -F {stale.name}', "unknown", "A3 v4 — -F absolute path on disk, long: NEVER read from disk ⇒ UNKNOWN (r3 ❌3 made disk reads unsafe)"),
        (f'git commit PROME/STATUS.md -F {short.name}', "unknown", "A3 v4 — -F absolute path on disk, short ⇒ UNKNOWN"),
        ('git commit PROME/STATUS.md -F "$SP/never_written.txt"', "unknown", "A3 missing information — $VAR path, no heredoc, no file ⇒ UNKNOWN"),
        (f'cat > "$SP/a.txt" <<\'EOF\'\n{long_subj}\nEOF\ngit commit PROME/STATUS.md -F "$SP/b.txt"', "unknown", "wrong owner — heredoc targets a DIFFERENT file than -F names ⇒ UNKNOWN"),
        (f'cat > notes.md <<\'EOF\'\nremember: git commit -m "{long_subj}"\nEOF\necho done', "allow", "A4 — `git commit -m <long>` appears ONLY inside a heredoc body (prose)"),
        ('git commit PROME/STATUS.md', "unknown", "editor commit — nothing to measure ⇒ UNKNOWN"),
        ('git commit -C HEAD~1 PROME/STATUS.md', "unknown", "-C reuse ⇒ UNKNOWN"),
        ('ls -la && echo "git commit -m nothing here is prose in quotes"', "allow", "A4 — the phrase sits inside a whitespace-bearing quoted string"),
        (f'git -C /tmp/repo commit -m "{long_subj}"', "block", "git global option before commit is still scanned"),
        (f'git commit --message="{long_subj}"', "block", "--message= form"),
        (f'git commit -m"{long_subj}"', "block", "-m<msg> attached form"),
        (f'git commit -m "first para line one\nline two of the same paragraph\n\nbody" PROME/STATUS.md', "allow", "A7 overlap — two-line first paragraph joins to 55 chars ⇒ allow"),
        ('git commit -m "' + "x" * 60 + '\n' + "y" * 60 + '\n\nbody"', "block", "A7 overlap — two-line first paragraph JOINS to 121 chars ⇒ block"),
        (f'git commit -m "short" -m "{long_subj}"', "allow", "overlap — -m twice: the FIRST is the subject"),
        (f'git commit -m "short" PROME/STATUS.md && git commit -m "{long_subj}" PROME/SCRATCH.md', "block", "overlap — two commits in one line, the second is over"),
        ('git commit -m "unbalanced \'quote', "unknown", "A5 — shlex failure ⇒ UNKNOWN, no exception"),
        ("echo nothing to do with git", "allow", "no git at all — fast path"),
        # ── wq244cold (first read), VERBATIM ──
        (f'printf \'%s\\n\' "PROME: short new subject" > {stale.name} && git commit PROME/STATUS.md -F {stale.name}', "unknown", "r1 ❌1 — -F file REWRITTEN by printf > (stale long file on disk) ⇒ UNKNOWN"),
        (f'echo "short" > {stale.name}; git commit PROME/STATUS.md -F {stale.name}', "unknown", "r1 ❌1 — echo > form ⇒ UNKNOWN"),
        (f'cat {stale.name} | tee {stale.name}.new; git commit PROME/STATUS.md -F {stale.name}.new', "unknown", "r1 ❌1 — tee target ⇒ UNKNOWN"),
        ("cd sub && git commit PROME/STATUS.md -F msg.txt", "unknown", "r1 ❌2 — relative -F after a cd ⇒ UNKNOWN (never read)"),
        (f'MSG="{long_subj}"; git commit -m "$MSG"', "unknown", "r1 ❌4 — runtime-assembled $MSG ⇒ UNKNOWN + advisory"),
        (f'bash -c \'git commit -m "{long_subj}"\'', "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r1 ❌4 — bash -c body lifted and scanned"),
        ('git commit -m "$(cat /tmp/m.txt)"', "unknown", "r1 ❌4 — $(…) ⇒ UNKNOWN + advisory"),
        (f'/usr/bin/git commit -m "{long_subj}"', "block", "r1 ❌4 — git matched by basename"),
        (f'bash scripts/commit_helper.sh "{long_subj}"', "allow", "PERIMETER — a script by path: no `git commit` visible ⇒ allowed SILENTLY"),
        (f'git commit -am "{long_subj}"', "block", "r1 ❌5 — combined short flags -am"),
        (f'git commit -qm "{long_subj}"', "block", "r1 ❌5 — -qm"),
        (f'git commit PROME/STATUS.md -m "{nfd100}"', "allow", "r1 ❌6 — 100 NFC chars arriving NFD ⇒ allow"),
        (f"cat <<'M' > x.txt\n{long_subj}\n\nbody\nM\ngit commit PROME/STATUS.md -F x.txt", "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r1 ⚠️7 — redirect AFTER the marker is still a heredoc target"),
        (f"tee y.txt <<'M'\n{long_subj}\n\nbody\nM\ngit commit PROME/STATUS.md -F y.txt", "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r1 ⚠️7 — tee as the heredoc target"),
        ('grep -n "git commit" PROME/STATUS.md || true', "allow", "a search for the phrase — quoted, whitespace-bearing ⇒ prose"),
        # ── wq244cold2 (second read), VERBATIM ──
        (f"cat >> {short.name} <<'EOF'\n{long_subj}\n\nbody\nEOF\ngit commit PROME/STATUS.md -F {short.name}", "unknown", "r2 ❌1 — >> APPEND heredoc: the real subject is on disk already ⇒ UNKNOWN, never a block"),
        (f'cat > "$SP/m.txt" <<\'EOF\'\n{long_subj}\nEOF\nprintf \'%s\\n\' "short" > "$SP/m.txt"; git commit PROME/STATUS.md -F "$SP/m.txt"', "unknown", "r2 ❌2 — heredoc-written then REWRITTEN later in the command ⇒ UNKNOWN"),
        (f"cat > notes.md <<'EOF'\nexample:\n  cat > x <<'EOF'\n  body\n  EOF\ngit commit -m \"{long_subj}\" is prose here\nEOF\necho done", "allow", "r2 ❌3 — an INDENTED terminator inside a body does not end the heredoc (bash-exact) ⇒ prose"),
        ("git commit PROME/STATUS.md -F msg.txt", "unknown", "r2 ❌4 — relative -F with NO cd, a long ./msg.txt in the hook's cwd ⇒ UNKNOWN, never read (cwd drill)"),
        (f'git commit -m "short" PROME/STATUS.md\ngit commit -m "{long_subj}" PROME/SCRATCH.md', "block", "r2 ❌5 — a second commit on a NEW LINE is its own command ⇒ block"),
        (f'eval "git commit -m \'{long_subj}\'"', "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r2 ❌6 — eval body lifted and scanned"),
        (f'$GIT commit -m "{long_subj}"', "unknown", "r2 ⚠️ — git through a variable ⇒ UNKNOWN + advisory (was silent)"),
        # ── wq244cold3 (third read), VERBATIM ──
        ('git commit -m "' + "x" * 50 + '\n   ' + "y" * 48 + '\n\nbody"', "block", "r3 ❌1 — an INDENTED continuation line keeps its leading spaces when git joins: 50+1+3+48 = 102 ⇒ block"),
        (f"git commit PROME/STATUS.md -F - <<'EOF'\n{long_subj}\n\nbody\nEOF", "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r3 ❌2 — -F - with the heredoc on stdin is determinable ⇒ block"),
        (f"cd /tmp/cr3 && printf '%s\\n' \"short\" > ./msg.txt && git commit PROME/STATUS.md -F /tmp/cr3/msg.txt", "unknown", "r3 ❌3 — same file rewritten under ANOTHER spelling: no disk read ⇒ UNKNOWN, never a block"),
        ("git commit PROME/STATUS.md -m $'" + exact100 + "'", "allow", "r3 ❌4 — $'…' ANSI-C quoting, exactly 100 chars ⇒ allow (no phantom $)"),
        ("git commit PROME/STATUS.md -m $'" + exact100 + "x'", "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r3 ❌4 — $'…' with 101 chars ⇒ block"),
        # ── wq244cold4 (fourth read), VERBATIM ──
        ("git commit PROME/STATUS.md -m $'PROME: short subject\\n\\nbody " + "x" * 200 + "'", "unknown", "r4 ❌1 — $'…' WITH escapes: git's %s is 20 chars; measuring the literal gave 230 ⇒ UNKNOWN, never a block"),
        (f"git commit A -F - <<'EOF'\n{long_subj}\nEOF\ngit commit B -F - <<'EOF'\nshort\nEOF", "unknown", "r4 ❌2 — two stdin heredocs for two -F - commits ⇒ UNKNOWN (bodies not attributable)"),
        ("git commit PROME/STATUS.md -m '     " + "x" * 98 + "'", "block", "r4 ❌9 — git KEEPS a subject's leading whitespace: 5 + 98 = 103 ⇒ block"),
        # ── wq244cold5 (fifth read), VERBATIM ──
        (f"python3 - > msg.txt <<'PYEOF'\nprint('PROME: short subject')\n# {long_subj}\nPYEOF\ngit commit PROME/STATUS.md -F msg.txt", "unknown", "r5 ❌1 — the heredoc feeds the INTERPRETER; the file gets stdout ⇒ UNKNOWN, never measured"),
        (f'git commit --dry-run PROME/STATUS.md -m "{long_subj}"', "allow", "r5 ❌2 — a dry run commits nothing ⇒ allow"),
        (f'echo git commit -m "{long_subj}" >> notes.md', "allow", "r5 ❌3 — `git` is echo's ARGUMENT, not the command word ⇒ prose"),
        (f'out=`git commit -m "{long_subj}"`', "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r5 ❌6 — backtick command substitution runs the commit ⇒ block"),
        (f"bash -c $'git commit -m \"{long_subj}\"'", "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r5 ❌7 — ANSI-C body normalised BEFORE the -c lift ⇒ block"),
        (f"git commit PROME/STATUS.md --file - <<'EOF'\n{long_subj}\n\nbody\nEOF", "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r5 ❌8 — `--file -` space form reads stdin ⇒ block"),
        # ── neighbours of the r5 fixes (author's own, not a reader's) ──
        (f'git commit -n PROME/STATUS.md -m "{long_subj}"', "block", "r5 nbr — `-n` is --no-verify, NOT a dry run ⇒ block"),
        (f'git commit -m "{long_subj}" -m "--dry-run"', "block", "r5 nbr — `--dry-run` as a MESSAGE value (2nd -m) is not the flag ⇒ block"),
        (f'sudo -u willi git commit -m "{long_subj}"', "unknown", "WQ-263 S2/S4 (was block) — inferred, so WARN not block: r5 nbr — a prefix command with a NON-flag argument still runs git ⇒ block"),
        (f'echo git commit -m "{long_subj}" | bash', "unknown", "r5 nbr — prose piped to a shell RUNS ⇒ UNKNOWN, never allow"),
        (f'printf "%s" git commit -m "{long_subj}"\ngit commit -m "short" PROME/STATUS.md', "allow", "r5 nbr — prose on line 1, a short real commit on line 2 ⇒ allow"),
        (f'grep -l "git commit" notes.md; git commit PROME/STATUS.md -m "{long_subj}"', "block", "r5 nbr — prose in one segment, a long real commit in the next ⇒ block"),
        (f'{{ git commit PROME/STATUS.md -m "{long_subj}"; }} 2>err.log', "block", "r5 nbr — a brace-group head is transparent: git still runs ⇒ block"),
        (f'if git commit PROME/STATUS.md -m "{long_subj}"; then echo ok; fi', "block", "r5 nbr — `if` runs its condition ⇒ block"),
        (f'git commit PROME/STATUS.md \\\n  -m "{long_subj}"', "block", "r5 nbr — backslash-newline continuation is ONE command ⇒ block"),
        # WQ-263 (Will 2026-09-22 "with CATO fix") — S3: CATO's three false blocks, none of which runs git ⇒ never block
        (f'command -v git commit -m "{long_subj}"', "unknown", "WQ-263 S3 CATO — `command -v` LOOKS UP git, runs nothing ⇒ warn, never block"),
        (f'env printf %s git commit -m "{long_subj}"', "unknown", "WQ-263 S3 CATO — env runs PRINTF; git commit is its argument ⇒ warn, never block"),
        (f'timeout 1 echo git commit -m "{long_subj}"', "unknown", "WQ-263 S3 CATO — timeout runs ECHO ⇒ warn, never block"),
        # S4 — the STATED COST Will accepted: real commits behind a prefix command now warn
        (f'env FOO=1 git commit -m "{long_subj}"', "unknown", "WQ-263 S4 stated cost — env prefix: real commit, WARN not block"),
        (f'timeout 5 git commit -m "{long_subj}"', "unknown", "WQ-263 S4 stated cost — timeout prefix: real commit, WARN not block"),
        # S5 — a bare assignment is NOT a prefix command: git is still the literal command word ⇒ block
        (f'FOO=1 git commit -m "{long_subj}"', "block", "WQ-263 S5 — bare VAR=… assignment, git is the command word ⇒ block"),
        (f'git commit -m "short subject" PROME/STATUS.md', "allow", "WQ-263 S6 — ordinary short -m ⇒ allow"),
    ]
    fails = []
    here = os.getcwd()
    for cmd, want, label in cases:
        if "cwd drill" in label:
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
