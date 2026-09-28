---
name: finding_unquoted_heredoc_expands_dollar_figures
description: A bash heredoc without a quoted terminator expands $0/$1/$2 inside prose — "$1.8B" ships as ".8B", "$0" as "/bin/bash", "$110" as "10"; the write succeeds, the file reads plausibly, and only a reader who knows the figure sees it. n=2 in one night (VIOLET memo, PROME brief), both caught by a second reader.
metadata:
  type: feedback
symptoms: "dollar amounts missing their leading digit" · "/bin/bash appears in a report" · "$0 became /bin/bash" · "figure lost a digit after a heredoc write" · "grep pattern with $ in double quotes matched nothing"
---

**The fact.** `cat > file <<EOF` (unquoted terminator) is a shell-expansion context: `$1`, `$2`… expand to positional parameters (empty in a plain shell), `$0` to the shell name (`/bin/bash`), backticks execute. In prose, "$1.8B" → ".8B", "−$83.6B" → "−3.6B", "+$100B" → "+00B", "$110" → "10", "$0 moved" → "/bin/bash moved". The write succeeds, `measure.py` reports a healthy size, and the text still parses as a sentence. The same trap bit the VERIFICATION: a `grep "…\$0…"` in double quotes expanded before grep saw it, so the residue check reported clean.

**Why it matters.** A brief is Will-facing; a missing leading digit is a wrong number that reads as a right one (`finding_plausible_stale_value_evades_review`'s sibling — plausible CORRUPTED value). CATO caught it on 2026-09-25 01:4x in `PROME/reports/2026-09-25_six-desk-decision-brief.md`; VIOLET hit the same class ~00:5x the same night ("unquoted heredoc + backticks", its own memo).

**How to apply.** Every heredoc that carries prose or figures uses a QUOTED terminator: `<<'EOF'`. Every grep/sed pattern containing `$` goes in single quotes. After writing any Will-facing file by heredoc, grep it for `bin/bash` and for a bare `.` before a digit-B/T/M (`[^$0-9.]\.[0-9]+[BMT]\b`) — with the pattern single-quoted. Sibling: [[finding_heredoc_terminator_ends_the_and_chain]] (a different heredoc failure; same reflex — treat heredocs as code, not as paste).

**Instance n=3 (WALTER, 2026-09-28 ~18:2x ET).** An R3 results packet to PROME written with `cat > file <<EOF` ended "**ASK (BRENT):** concur or strike any phrase. /bin/bash. No trade." — the fleet's standard "$0. No trade." closer. The author CHOSE the unquoted form deliberately so `$(date …)` would expand in the header; the same choice expanded `$0` in the footer. PROME caught it on read. **Lesson beyond n=2:** the tempting reason to leave a heredoc unquoted (one wanted substitution) is exactly what arms it. Compute the value first (`TS=$(date …)`), then write with `<<'EOF'` and a placeholder that `sed` replaces, or keep the one substitution out of the prose body. The post-write `grep 'bin/bash'` step would have caught it and was skipped.
