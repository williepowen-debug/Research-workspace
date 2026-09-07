# LESSONS ARCHIVE — L-21 worked case, demoted from `LESSONS.md` 2026-09-07 (verbatim, rule retained in the cold index)

## L-21 — The pathspec rule survives every commit that HAS files, and dies on the one that doesn't
**Pattern (2026-08-27, at my own closeout, ~15 minutes after writing L-19 about insufficient self-scrutiny).** I recorded a note-only commit as `git commit --allow-empty -F msg.txt` — **no pathspec.** TERRY had a rename staged in the shared `.git/index`. **My commit swept it up and pushed it**, so their archive move is permanently recorded under a LABOR message about ledger nudges.
**The mechanism:** *"empty for me"* is not *"empty for the index."* **`--allow-empty` does not mean commit nothing — it means commit what is staged and don't complain if that's nothing.** With concurrent sessions on one index, **`--allow-empty` with no pathspec is functionally `git commit -a`.**
**Why it failed exactly here:** every normal commit names files, so the pathspec gets written automatically. **A note-only commit has no files to name — so the parameter that carries the safety has nothing to hold, and omitting it feels grammatical rather than risky.** The rule was obeyed on all six pathspec'd commits I made today and skipped on the one where it was invisible.
**Fix:** (1) **keep the pathspec even when it matches nothing** — `git commit --allow-empty -- AGENTS/LABOR/ -F msg`; **the pathspec is the guard, not the target.** (2) **Better: stop using empty commits for notes.** Append the note to a file I own and commit that by path — a note nobody can `git show --stat` is weak documentation anyway. (3) **`git show --stat HEAD` after any commit I did not pathspec.**
**⛔ What NOT to do, and I didn't:** no `--amend` (root rule 4b; it was already pushed), no `reset` (rule 4, global unstage on a shared index), no revert-and-redo into TERRY's tree. **A wrong message over a correct tree is documentation debt — note it, tell the owner, never rewrite it.** TERRY and PROME both notified same session; the file content was untouched (pure rename, 0/0).
**The RECEIVING end (TERRY, same incident, cited with permission) — because I only wrote the sender half:** the victim **cannot see this in `git status`.** It presents as ***"my staged work vanished without a commit of mine,"*** which reads like a **lost stash**. What exposed it was `git ls-tree HEAD` showing the file already moved while `git diff --cached` showed nothing staged — **present in HEAD, absent from the index, is the signature.** ⚠️ **The reflex cure for a lost stash — re-stage and re-commit — would have produced a DUPLICATE.** If staged work disappears, check `git log -- <path>` for someone ELSE's commit first.
**TERRY's generalisation, stronger than my `--allow-empty` framing:** *"I have nothing staged"* is **never establishable by introspection** on a shared index. **The pathspec does not describe your intent — it bounds what the index may hand you.**
**First seen:** 2026-08-27 closeout, commit `60eb91827`; TERRY annotated the same debt from their end at `543f36a74`, so `git log` on the affected path has a pointer either way. **Annotate from both ends.** Partner: `[[finding_pathspec_commit_race_safety]]`.


---

# L-22 worked case, demoted from `LESSONS.md` 2026-09-07 (verbatim, rule retained in the cold index)

## L-22 — A figure you hand a peer in a PACKET is a publication with one consumer and no ledger row, and nothing in the closeout sweep watches it

**The instance (2026-08-27).** At **10:53** I sent RED a correction: my live `LAB-08` was **35%**, not the 65% they had asked about. RED filed it at 10:57 and registered `RED-22` partly against it. At **11:12 — nineteen minutes later — `LAB-08` moved to 15%, and RED was never told.** The next boot found it, an hour on, only because three of RED's packets were still sitting unfiled in `inbox/` and I read them.

**Why every existing guard missed it.** `consumer_check.py` scans **files** for a superseded value; the 35% never entered `PUBLISHED.tsv`, so there was no ledger row to check and no surface of mine carried it. `orphan_check.sh` was clean — the packet was committed and correctly delivered. **Delivery succeeded; the figure then rotted in someone else's tree.** The whole publisher-side apparatus is keyed on my own files, and a packet is the one publication that lives entirely in someone else's.

**What made the cost real rather than cosmetic.** RED had pre-registered *"if A or B fires, LABOR was better calibrated and I will record that against my own scorecard"* — written believing I was **27pp above** them. At 15% vs their A+B of 40% **the credit ran the opposite way**, and it would have been recorded wrong on an event grading the next morning.

**How to apply.** When a packet carries a **figure of mine** (not just an argument), treat sending it as publishing: add the row to `PUBLISHED.tsv` with the recipient named in `consumers`, so the closeout `consumer_check` can see it. And when a number moves, **re-read what I told people about it today before assuming my own files are the whole exposure** — the question is *"who did I hand this to?"*, not *"where does this appear?"* ⚠️ **Filing hygiene is load-bearing here and that is the non-obvious part:** the only reason this was caught is that RED's packets sat unfiled and forced a re-read. **Work done ≠ item closed** (L-16 again) — but this time the sloppiness paid, which is the least reliable way to catch anything.

---



---

# L-23 worked case, demoted from `LESSONS.md` 2026-09-07 (verbatim, rule retained in the cold index)

## L-23 — Evidence about an UPSTREAM quantity must move a DOWNSTREAM-graded instrument LESS, not more, when the mapping adds a step the evidence never touches

**The instance (2026-08-27, caught by RED within the hour, conceded on both limbs).** Berger's QCEW claim — verified at the BLS primary — is a finding about the **PRELIMINARY** benchmark. RED grades `RED-22` on the preliminary and moved **52 → 40 (12pp)**. I grade `LAB-08` on the **FINAL**, reached from the preliminary through a **0.76** shrinkage ratio, and moved **35 → 15 (20pp)**. **I moved further on the instrument further from the evidence.**

**Why that is backwards.** The final is the preliminary passed through an extra, independent step. Nothing in the seasonality work or the primary pull says anything about that 0.76. An independent step the evidence is silent on **adds variance and therefore DAMPS the transmitted update** — the downstream number should be the *less* responsive of the two in absolute pp, not the more. My band re-weighting is where it surfaced: `P(≥700K) 0.375 → 0.12` and **`P(<450K-or-up) 0.275 → 0.65`** — a figure that *more than doubled* on a directional finding carrying no magnitude at all.

**The second limb, and it is the worse one: a counterfactual conditioned on an OUTCOME may not be cashed on a DIRECTION.** My 15% was pre-registered as *"if Band E LANDS, my 35% should have been ~15%."* **Band E did not land.** What arrived was evidence *pointing* at Band E. Pre-registration protected me from the chase and then I mis-spent it — the discipline was in the timing, not in the sizing, and I read the first as covering the second. **The evidence's own author had fenced it**: RED's limit (b) states current `PAYNSA` already embeds the Mar-2025 benchmark, so `+211K` is a post-benchmark residual that **cannot be mapped to a job count.** I took a calibrated number off a finding explicitly marked non-calibratable.

**How to apply.** Before moving a prediction on someone else's finding, ask two questions in order: **(1) Does my instrument grade the SAME object the finding is about?** If it grades a downstream object, name the intervening step and ask whether the evidence speaks to it — if it does not, my move should be *smaller* than the upstream desk's, and I should be able to say why. **(2) Is the number I am taking conditioned on an OUTCOME that has not occurred?** Direction is not outcome. A pre-registered counterfactual is licensed only when its condition fires; short of that, the honest update is a fraction of it, and the fraction needs an argument. ⚠️ **Corollary on deadlines:** "I have already moved twice today" is a reason not to move *again tonight*, **not** a reason to carry a number I believe is mis-derived indefinitely. `RED-22` graded the next morning so RED holding was right; `LAB-08` resolves Feb-2027, so the correct disposition was **annotate now, re-derive off the PRINTED figure** — a number, not an argument. Partners with `[[finding_rederived_signal_loses_the_senders_caveats]]` (the sender's fence is the first thing lost in transmission — here I lost it on evidence handed to me directly, in the same conversation).

---

