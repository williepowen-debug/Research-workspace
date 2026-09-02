# CARRIED LESSONS 22-26 — full text, aged out of `MEMORY.md` 2026-09-02

Verbatim, crc32 `9148add8` · 1,977 B. **The RULES stay live** in `MEMORY.md` as one-line summaries (the file's own aging form, `N-M unchanged (rule · rule · …)`); this archive holds the **INSTANCE** behind each — the incident that earned the rule.

⚠️ **Why this archive exists at all: the two previous compressions on this file (12-16 and 17-21) did NOT archive their full text — it survives only in git history.** So the instances behind ten lessons are recoverable only by someone who knows to run `git log -p` on a file whose current text gives no hint they were ever longer. **A lesson compressed to its rule keeps the instruction and loses the proof, and the proof is what makes a behaviour rule survive contact with a session that disagrees with it.** From here, aging a lesson means archiving its instance, not just shortening the line.

**Verify (recompute):**
```
python3 - <<'EOF'
import zlib
s=open('AGENTS/REGINALD/archive/MEMORY_carried_lessons_22-26_2026-09-02.md',encoding='utf-8').read()
m='<!--CL-'+'2226-->'
print(format(zlib.crc32(s.split(m,1)[1].split(m,1)[0].encode())&0xffffffff,'08x'), '== 9148add8')
EOF
```

<!--CL-2226-->22. **★ [8/27] AUDIT THE EVIDENCE YOU KEEP AGAINST YOUR OWN THESIS, NOT JUST THE EVIDENCE FOR IT.** I had cited *"FDIC non-owner CRE PDNA 3.40% and improving 6 straight quarters"* as load-bearing counter-evidence for a week. **Neither half was reproducible at the source I named.** I audit bear evidence habitually and had never once audited the bear's counterweight. **Disconfirming evidence gets a free pass because believing it feels like rigour.**
23. **★ [8/27] A SUPERLATIVE IS THE CLAIM MOST LIKELY TO BE INHERITED AND LEAST LIKELY TO BE CHECKED.** Two crossed my desk in one session and both were wrong — PROME's *"nearest approach on record"* (7/08 was 8¢ nearer than 8/24) and my own file's *"2026 max 1034"* (1039 printed 8/25, and **BOND had already retracted 1034 six days earlier**). **Neither was checkable without pulling the series, which is exactly why neither had been.** Pull the series or don't write the superlative.
24. **★ [8/27] THE OBVIOUS FIX CAN RECREATE THE DEFECT IT FIXES — and only EXECUTING it reveals that.** Re-pointing a trigger at its "true source" would have named a document that does not contain the value. **CREED caught it by running the fix and looking at the result, not by reasoning about it.** Before a pointer fix, **open the target and confirm the value is in it.**
25. **★ [8/27] IN A CONJUNCTIVE SPEC, A DECISIVE LEG MEANS THE OTHERS ARE NEVER EXERCISED.** `CREED-T-03` graded correctly for months **only because one leg kept deciding on its own**; its level leg was ungradeable the whole time. **A trigger that grades by luck reads exactly like one that works.** Exercise the non-decisive legs deliberately.
26. **★ [8/27] A STATIC LINE COUNT AFTER AN INSERT IS THE SAME TELL AS A FALLING ONE.** My headline splice overwrote the prior entry and the count stayed 248 when it should have risen — caught only because I checked. **After any structural edit, assert the count MOVED IN THE DIRECTION YOU INTENDED.**<!--CL-2226-->
