# Acceptance — Bash guard warns on an unquoted heredoc that would expand, 2026-11-20

reads: 1 of 3 (one result read; no plan read)

Authority: WQ-713 (Will 2026-11-17 20:42 ET, "yes go ahead"), DOCKET L1188 item 2: extend the EXISTING Bash guard (`PROME/tools/hooks/git_guard.py`), no new tool. A warning, never a block.

Defect: a heredoc whose delimiter is not quoted is expanded by the shell before the text is written. "$1.8B" ships as ".8B", "$0" ships as the shell's name, and a backtick pair runs as a command. The file or message is written, the command returns 0, and nothing says the text changed (`memory/auto/finding_unquoted_heredoc_expands_dollar_figures.md`, n=8).

Written before any edit to the guard.

Properties:
1. Ordinary: a Bash command holding a heredoc with an unquoted delimiter (`<<EOF`, `<<-EOF`) whose body holds a dollar sign the shell would expand (followed by a letter, digit, underscore, `{`, `(` or one of `? $ ! # @ * -`) or a backtick, neither escaped by a backslash, produces a warning that reaches the model in the same turn. The warning names the delimiter and quotes the first such line. The command still runs: the hook's exit code is 0.
2. Overlap:
   - a quoted delimiter (`<<'EOF'`, `<<"EOF"`, `<<\EOF`) produces no warning, whatever the body holds;
   - an escaped `\$` or an escaped backtick produces no warning; an even run of backslashes before the sign does not escape it and does warn;
   - a dollar sign the shell leaves alone (followed by a space, a full stop, a comma or the end of the line) produces no warning;
   - a here-string (`<<<`) produces no warning;
   - a marker with no terminator line is not a heredoc (the guard's existing rule) and produces no warning;
   - two heredocs in one command are judged separately: a quoted one beside an unquoted one warns for the unquoted one only;
   - a command the guard already blocks is still blocked with exit code 2 and its existing message; the block wins;
   - every existing fixture in `test_git_guard.py` returns what it returned before.
3. Wrong owner: N/A. The guard cannot know who wrote the command; it is a per-command text check. Declared limit: Claude Code sessions only; Codex desks are not covered.
4. Missing information: unusable hook input stays on the existing declared fail-open path, unchanged. A failure inside the new detector never blocks and never raises out of the hook: the command is allowed.
5. Concurrent activity: N/A, the guard is a stateless per-command check.

Declared limits before the build:
- A warning does not stop the command. Intended expansion (`$NOW`, `$(date)`) inside an unquoted heredoc is ordinary shell and also warns; the message says so in one line.
- The guard reads the literal command text. A heredoc inside a script run by path is not seen.
- Whether the warning text reaches the model on a hook that exits 0 depends on the Claude Code hook contract; the mechanism used and how it was confirmed are recorded in the disposition below.

## Disposition 2026-11-20 13:21 ET (WQ-229 states)

IMPLEMENTED · TESTED (182 of 182, the 82 earlier fixtures each run twice: exit code, and no warning on stdout) · INDEPENDENTLY VERIFIED by one Opus reader on the candidate before it went live (own counterexamples; 16 constructed commands matched the prior version on exit code and stderr, blocking unchanged; no crash on seven inputs of about 200 KB) · STILL UNRESOLVED: the residue below. The candidate was installed byte-for-byte as read; nothing was fixed after the read.

Mechanism: the hook prints JSON `hookSpecificOutput.additionalContext` on stdout and exits 0. OBSERVED in a live Claude Code session (PROME's own, same day): an unquoted heredoc holding "$1.8B" ran, wrote ".8B", and the warning text arrived in the model's context with the tool result. Not observed: any other session or Claude Code version.

Declared residue (reader's flags, none fixed; no property 1 to 5 failed on the fixtures):
- Missed warnings, the shell expands and the guard stays quiet: a second heredoc on the same line as a first (only the first marker on a line is read) · a delimiter holding a hyphen or a full stop (`END-MSG`, `END.TXT`) · a line that only looks like the terminator (indented, or with a trailing space) ends the guard's reading early, so later lines are not read · the old arithmetic form `$[1+2]`.
- False warnings: a marker inside a quoted string or a comment earlier on the line hides the real, quoted delimiter after it.
- A wrong delimiter can be named when a quoted mention precedes the real marker; the quoted line is still the right one.
- Speed: on a pathological command of about 28,000 unterminated markers the hook takes about 27 seconds against about 11 before; the slow pattern predates this change and the block decision runs first.
- Not tested: CRLF command text, shells other than bash, heredocs inside `bash -c "..."`, the hook timeout.
