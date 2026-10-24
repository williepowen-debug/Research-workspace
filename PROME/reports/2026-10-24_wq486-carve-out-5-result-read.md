COLDREADER RESULT READ · /home/willi/Research-workspace/CLAUDE.md § Git Protocol · WQ-486 carve-out ⑤

Five-field ledger: claim -> artifact -> command/read -> observed -> proposed change

1. DIFF SCOPE · ✅
 claim: exactly three places changed, nothing else.
 artifact: CLAUDE.md:78 (lead-in), :83 (new bullet ⑤), :105 (Never line).
 command: git diff HEAD -- CLAUDE.md ; --stat
 observed: "1 file changed, 3 insertions(+), 2 deletions(-)". Hunk 1 = line 78 "①–④ — four" -> "①–⑤ — five" (the "(④ activation-gated)" clause and the "separate PROME-only Gate C custody grant" tail are untouched), plus the added ⑤ bullet directly after ④ and before the Gate C custody paragraph. Hunk 2 = line 105 "①–④" -> "①–⑤". No other hunks.
 change: none.

2. GRANT MATCHES THE RULING · ✅
 claim: ⑤ grants exactly "a desk's own explicitly pathed forum post" and nothing more.
 artifact: CLAUDE.md:83 vs ruling text (WQ_LEDGER.tsv:1337, "carve-out ⑤ for a desk's own explicitly pathed forum post; no authority over others' posts or shared directories").
 read: bullet says post "you authored" ... "yours to commit, explicitly pathed, and only that file"; "conveys no authority to edit or commit another desk's post, to sweep a shared directory, or to touch any other FORUM/ file (a session charter, a rulings record, README.md)".
 observed: all three ruling limbs present (own post · explicit path · no others' posts / no sweep). No edit authority over others' posts. Adds one explicit exclusion (other FORUM/ files) that the ruling implies but did not state; it narrows, never widens. Existing-procedure limb (WQ-486 record: plan read -> one insertion -> result read) is process, not text.
 change: none.

3. POINTERS / PATTERN
 3a. "WQ-486 A, Will 2026-10-24" · ✅ — ledger 1337: RULED 2026-10-24 19:39, "RULED A". Registered row 1236 item text offers the same carve-out ⑤ wording as option A.
 3b. "WQ-482 A" · ✅ (supported, but only indirectly) — grep '^482<TAB>' -> 2 rows: 1228 REGISTERED (item offers "A: run it as a light one-day experiment"); 1229 RULED "RULED APPROVE A, verbatim ...". The title ("— A FORUM: ...") is NOT the letter, but the RULED event text itself says "APPROVE A". Also WQ-486's registered item (ledger 1236) says "The forum rule you approved (WQ-482 A)". FORUM/README.md:25 and :32 say "WQ-482" with NO letter, so the README alone does not support "A"; the ledger does.
 3c. "FORUM/README.md § standing buckets" · ✅ — README.md:25 "## Standing buckets — the lightweight mode". Resolves (case/wording differs trivially).
 3d. filename pattern FORUM/<bucket>/<stamp>_<YOU>_<slug>.md · ✅ — ls FORUM/banks: 2026-10-22_1117_OZK_l520-call-read.md etc.; FORUM/orchestration: 2026-10-22_1115_PROME_forum-opened-wq482.md. README.md:29 defines the same form (<YYYY-MM-DD>_<HHMM>_<DESK>_<slug>.md). <stamp> = date_HHMM (contains an underscore) — consistent with real files.
 3e. ⚠️ "<stamp>", "<YOU>", "<bucket>" and "standing-bucket" are not defined in root; a root-only reader must open FORUM/README.md (the bullet does cite it). Not a widening risk. change: none required; optionally "(e.g. FORUM/banks/2026-10-22_1117_OZK_l520-call-read.md)".

4. WIDENING MISREADS · mostly ✅, two ⚠️
 ✅ session-tree posts (FORUM/2026-08-10_war-theaters/<topic>/NN_AGENT_slug.md): path has two levels and an ordinal, so does not match FORUM/<bucket>/<stamp>_<YOU>_<slug>.md; README.md:16 keeps "orchestrator commits the forum tree" for sessions. Bullet's own exclusion of "a session charter, a rulings record" reinforces it.
 ✅ README.md and other FORUM/ files: expressly excluded.
 ✅ "Never" line (:105) now lists ①–⑤ "each for its narrow scope only" — consistent with narrowness.
 ⚠️ keeper/: FORUM/keeper/NNN_AGENT_slug.md uses ordinals, not a stamp, so ⑤ does not cover it. Yet FORUM/keeper/README.md says "This folder is the one shared surface where every agent commits its own files" and "Commit only your own posts" — keeper commits have no root grant under ⑤. Not a widening of ⑤ (narrow reading is correct), but a cold reader may assume keeper is covered. change: none to root; keeper owner/PROME may want to note it. (Outside the scope of this edit.)
 ⚠️ "<bucket>" could be read by a stranger as any FORUM/ subfolder (README lists only banks/ and orchestration/ as open standing buckets; session trees are dated folders). The stamped filename requirement limits the damage. change: optional "(a dateless bucket folder PROME has opened)".
 ⚠️ "and only that file": ambiguous between "one post per commit" and "each own post, individually pathed"; the intended (and ruling) reading is the latter. Narrow either way. No change needed.
 ⚠️ Stale companion: FORUM/README.md:32 still says "Commit authority PENDING ROOT CANON ... until he rules". Outside CLAUDE.md, but now false. change: PROME updates README line 32 to cite carve-out ⑤ (an owner's follow-up, not part of this edit).

5. NUMBERING ①–⑤ CONSISTENT · ✅
 grep -n 'carve-out\|①' CLAUDE.md: :78 "Carve-outs ①–⑤ — five", :79–:83 bullets ① ② ③ ④ ⑤ in order, :93 "(carve-out ①)", :96 "(carve-out ③'s enforcement ...)", :105 "carve-outs ①–⑤". No remaining "①–④" or "four fleet-wide" in the file (repo-wide grep hits for "①–④" are only in unrelated WALTER/KERNEL logs). The Gate C custody paragraph (:85) remains outside the numbering as :78 states. "(④ activation-gated)" still correct — ⑤ has no activation gate.

6. READ CAP · ✅
 command: python3 PROME/tools/measure.py CLAUDE.md -> "CLAUDE.md 23257 B (wc -c) 122 lines". 23,257 B < 32,550 B cap (9,293 B headroom).

COUNTS: ❌ 0 · ⚠️ 5 (3e, keeper, <bucket>, "only that file", FORUM/README.md:32 stale) · ✅ 9 (1, 2, 3a, 3b, 3c, 3d, 5, 6, plus the session-tree/README exclusions in 4)

VERDICT: RELEASE
