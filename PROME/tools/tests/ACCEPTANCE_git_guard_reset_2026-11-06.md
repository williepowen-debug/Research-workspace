# Acceptance — git_guard reset coverage, 2026-11-06

reads: 3 of 3 (ceiling reached; no further read without Will naming one)

Defect: root Git Protocol forbids a global unstage of the shared index. The guard caught `reset --hard` only at end of string and `reset HEAD` only as the first argument, so `git reset`, `git reset -q` and a reset followed by `;` passed. VULCAN and VIOLET each ran one on 2026-11-06 (WQ authority: Will 18:20 ET "yes on all four").

Properties:
1. Ordinary: any `git reset` that names no path is blocked, whatever its options and whatever follows it on the line.
2. Overlap: a reset that names a path is allowed when it touches only that path, with or without `-q`. `reset HEAD` keeps its existing block, including after options. `--hard` is blocked in every position, even with a ref or path.
3. Wrong owner: N/A, the hook cannot know whose index entries are affected; that is why a global unstage is refused for everyone.
4. Missing information: unusable hook input stays on the existing declared fail-open path, unchanged.
5. Concurrent activity: N/A, the guard is a stateless per-command check.
Prose stays prose: a mention in a message or heredoc body is not blocked.

## Disposition 18:50 ET (WQ-229 states)

IMPLEMENTED · TESTED (82 of 82) · NOT INDEPENDENTLY VERIFIED · STILL UNRESOLVED below. Read 3: other RULES unchanged over 14,330 real commands, no real command narrowed, read 2's five ❌ right; left live because it only widens blocking against the committed version in real use.

Still unresolved, none a regression, all passing at the prior version too: properties 1 and 2 are NOT fully met. A bare sha or branch passes as if it were a path (`git reset a1b2c3d`, `git reset master`) · an abbreviated option passes (`git reset --har v1`) · a path that climbs out of a subfolder passes (`git reset sub/..`, `git reset -- sub/desk/../..`) · a quoted `-C` directory holding a space hides a reset · a quoted redirect target holding a space hides a reset · a reset run through quoted eval, a heredoc fed to a shell, or a variable passes. Declared costs: `../` paths and `"$f"` paths block, a path with spaces cannot be unstaged here, a prose mention in a comment blocks. A scratch candidate closing the two quoted-space forms and the climbing paths, while unblocking `../x`, is saved unreviewed at `PROME/reports/2026-11-06_git-guard-r3-candidate-UNREVIEWED.py.txt`; not applied, since a fix after the final read is unreviewed. DOCKET row carries it.

