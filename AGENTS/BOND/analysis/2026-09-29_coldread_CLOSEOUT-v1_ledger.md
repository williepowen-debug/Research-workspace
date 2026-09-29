COLDREADER · AGENTS/BOND/CLOSEOUT.md · 5291 B · 39 claims
SCORE: 10/39 ✅ · 25 ⚠️ · 4 ❌
❌ 10 L16 "Standard ... | Steps C1–C12" vs L36 "C11. Charter check (Heavy)." — Standard includes a step labelled Heavy-only; a reader cannot tell whether C11 runs at Standard.
❌ 12 L18 "Addendum | Any ending after the first in the same day | Floor A1–A3 + the conditionals" vs L20 "End-of-day runs at least Standard." — an end-of-day ending that is not the day's first is both Addendum (floor only) and >=Standard. Tiers are keyed on three different axes (restart time / session content / ordinal in day) with no precedence.
❌ 23 L34 "C9. NEXUS_BRIEF.md — LAST content write." vs L35 "C10 ... Transferable lesson → auto-memory ... BOND-only lesson → `MEMORY.md`. Outbox packets" and L36 "C11 ... `CLAUDE.md` and this file agree with it today" — L22 says "run in order", so C10/C11 content writes come after the "LAST" one.
❌ 27 L39 "`python3 monitors/closeout_run.py`" (resolves only from AGENTS/BOND) vs L43 "`bash scripts/safe-push.sh`" (ls AGENTS/BOND/scripts/safe-push.sh → DEAD; resolves only from repo root) and L42 pathspecs "`AGENTS/BOND/...`" (root-relative). No cwd stated; C12.2 and C12.4 need different directories.
⚠️ 4 L4 "Tier words match PROME/CLOSEOUT.md, LIQUID, TERRY, HANS" — siblings bold only Bounce/Light/Standard/Heavy; none has an Addendum tier (PROME uses "addendum" as Bounce's action). Claim partly false; LIQUID/TERRY/HANS given without paths.
⚠️ 6 L8 "run the rest after" — after the window closes, or at the next session? What if the session ends inside the window?
⚠️ 7 L10 "pass it to the runner" — table capitalises (Bounce…); runner argparse choices are lowercase {bounce,light,standard,heavy,addendum}; `--tier Standard` is rejected. Also unclear whether Bounce/Light/Addendum run the runner at all.
⚠️ 8 L14 Bounce commit "Optional" vs L7 includes "a machine switch" — a Bounce before a machine switch strands uncommitted work.
⚠️ 9 L15 Light "the ledger touched" — which ledger? Undefined. Runner/C12 at Light: yes or no?
⚠️ 11 L17 Heavy "+ MEMORY/auto-memory + CHANGELOG" — already in Standard via C10 and C4; implies Standard skips them.
⚠️ 14 L24 pair list vs L53–62 table — L24 has thesis→C4 (no table row); table has MEMORY(3)→C10, boot 6→C6/C9, 7/7b→C8 (absent from L24). Which set is canonical?
⚠️ 15 L26 "under 75% of the read cap" — read cap never defined (value, unit, source).
⚠️ 16 L27 "Flip ACTIVE rows past Stale_By" — flip to what token?
⚠️ 17 L28 "Register owed rows with a base rate" — "owed rows" undefined.
⚠️ 18 L29 `bond-state` token — values/location undefined; version-bump scheme (major/minor) unstated.
⚠️ 20 L31 "no marks" — "marks" undefined for a stranger.
⚠️ 21 L32 STATE AT WRITING block contents undefined; Heavy/Addendum SCRATCH mode unstated.
⚠️ 24 L34 "re-pin block", "Owner pointers only", "Fold it" — all undefined.
⚠️ 25 L35 auto-memory location not given.
⚠️ 26 L38 FREEZE — no mechanism in the text binds the commit to the run (no hash/tree check); runner itself writes registry/CLOSEOUT_LOG.tsv after freeze; C12 edits to fix rc=1 findings are not addressed. Self-discipline only.
⚠️ 29 L41 "rc=1 is not a pass" — does not say DO NOT COMMIT; rc=2 unmentioned. A tired reader commits on rc=1.
⚠️ 30 L41 "declare it" — declare how? `--superseded OLD NEW` fits figures, not a score/state change.
⚠️ 31 L42 "carve-out ①" — undefined here (lives in root CLAUDE.md).
⚠️ 32 L43 "the receipt line" never quoted; "root step 3" — root CLAUDE.md has several step 3s (session-end, before-committing, before-pulling).
⚠️ 33 L46 Addendum floor A1–A3 omits C12.1–2 (freeze + runner); L10 says every tier goes to the runner. Also no path for DUE predictions (C3) or fired catalysts (C5) in an Addendum.
⚠️ 34 L47 score change → "C4 mandatory" vs L29 C4 only on "Thesis-level change" — is a score change a thesis bump?
⚠️ 36 L51 "never content" vs L40 runner does numeric drift + assertions; "`coldreader`" and "restructure" undefined.
⚠️ 37 L61 "closeout_check 1/4" — 0- or 1-based over L40's four parts? (runner code: 0-based, 1/4 = numeric; not stated in file).
⚠️ 38 L62 "board_log" — no C-step writes it; only `board_log.tsv` exists.
✅ 1 L3 docs/PROTOCOL_PROVENANCE.md resolves (from AGENTS/BOND; untracked) and crc32 = 4276224127 matches.
✅ 2 L3 git log pointer · ✅ 3 L4 root Git Protocol · ✅ 5 L7 when-to-run · ✅ 13 L22 run in order/name no-op · ✅ 19 L30 C5 · ✅ 22 L33 C8 · ✅ 28 L40 runner step list (flags exist) · ✅ 35 L48 one-question test · ✅ 39 L56–60 table rows.
POINTERS: 14 tested; 12 resolve from some base; dead: `board_log` (only board_log.tsv), `scripts/safe-push.sh` from the AGENTS/BOND cwd C12.2 needs.
ONE-LINE VERDICT: no — tier choice collides (Addendum vs end-of-day, C11 in/out of Standard), C12 needs two unstated cwds, `--tier` casing fails, and nothing stops a commit on rc=1.
