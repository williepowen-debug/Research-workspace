# Keeper: what the research says about building a thinking companion
**Date:** 2026-10-17 | **Mode:** Cold (design research) + fleet lessons | **Confidence:** Medium. Strong on AI agreeableness, memory design and interruptions; thin on ADHD/autism and on this exact use.
**Commission:** Will, 13:16 ET, carrying CATO's revised brief (five questions). Investigation and recommendations only, not a build.
**Reads against:** DAEDALUS draft `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/agents/keeper/agent.md` and PROME plan `PROME/plans/2026-10-17_console-memory-agent-PLAN.md` (both as of 10/17 ~13:00 ET).

## Key Finding
The idea holds up, but **the biggest risk is not forgetting. It is agreeing.** Giving an AI a stored profile of the user produced the *largest* increase in sycophancy in a CHI 2026 study of 38 real users (e.g. +45% for one model). The research also shows that **summaries quietly lose detail when they are rewritten from themselves**, and that **people later remember an AI's improvements to their idea as their own.** Most of what makes Keeper good follows from guarding against those three. Initiative is fine, and wanted, if it is short, comes at a pause, and is cheap to wave off.

---

## The short version (Will-facing)

1. **Build pushback in, because memory makes the AI agree with you more.** Users also *rate* agreeable AIs higher and come back to them more (Cheng et al., *Science* 2026). So Keeper should never be tuned on "what Will liked". The challenge role has to be in its instructions, not left to its mood.
2. **Keep your raw words as the memory. Summaries are only an index.** On long-memory benchmarks, swapping raw conversation for summaries *lowered* recall. Adding extracted facts *on top of* the raw text raised it.
3. **Don't rewrite the "picture" from yesterday's picture.** One paper watched a fully rewritten context shrink from 18,282 tokens to 122 in one step, and accuracy fell below doing nothing at all. Rebuild it from the threads and captures, or edit it in small dated steps.
4. **Always mark who said what.** When people improve someone else's idea, they later recall it as their own at roughly double the rate. A chatbot induced over 3× more false memories than control in one study. Keeper's developments should sit visibly apart from your words.
5. **Initiative: yes, but at a pause, short and cheap to dismiss.** In a coding study 90% preferred a proactive assistant, but only 47% did when it got pushier. Suggestions made mid-task were dismissed 62% of the time; at natural stopping points they got about 52% engagement.
6. **Let your idea come first.** AI-suggested ideas make people's ideas more alike: a meta-analysis put the drop in diversity at g = −0.86. In one large trial, a *coach-style* AI made people's later unassisted thinking worse, and direct answers did not.
7. **The profile should be a log of evidence, not a verdict.** Treat observations as passing states by default. Never infer from a diagnosis label, because LLMs given an autism disclosure produced stereotyped advice. Show each new inference the moment it's made, so it can be binned.
8. **Don't optimise for how much you use it.** In a 4-week randomized trial (n=981), heavier voluntary chatbot use went with worse loneliness and dependence; this is a correlation. Plan for lapses: a "welcome back, here's where you left off", never a nag.

---

## What it changes in the current draft

| Draft element (DAEDALUS `agent.md`) | What the evidence says | Suggested change |
|---|---|---|
| Capture reply = one line, "say nothing else" | Proactive help wins on average, but loses when pushy or mid-flow (Chen 2025; Pu 2025; Kuo 2026) | Keep the one-line file receipt as the default. Allow **one** optional hook ("connects to X, more?") **after a pause**, never between rapid captures. |
| Speaks unprompted only in the 06:00 brief | Batching pushes ~3×/day beat both constant alerts and none (Fitz 2019). Replying to something you just sent is a different thing from a push. | Keep unprompted pushes batched (the morning brief is defensible). Allow contributions *inside* a conversation you started. |
| `picture.md` rewritten each morning | Full rewrites erode detail ("context collapse", ACE 2025); chains of rewrites drift (telephone-game study) | Rebuild it daily **from threads and raw captures, never from yesterday's picture**, or apply dated delta edits. Keep old versions so drift is visible. |
| Thread `what` "in Will's words where possible" | People absorb improvements to their ideas as their own (Perfect &amp; Stark 2012) | Split each thread into **Will said** (verbatim, dated) and **Keeper added**. Quote him; don't paraphrase him. |
| `profile.md`: STATED vs `INFERRED:` with evidence | The right shape (Kay's scrutable models), but labelling alone isn't shown to stop harm. In a simulation, a sycophantic bot drove a fully rational user into false beliefs even when the user was warned (Chandra 2026). | Keep it, plus: a dated evidence log per item; **state not trait** by default; promote to "lasting" only on recurrence weeks apart; **never infer from ADHD/autism labels**; announce each new inference in one line with keep/edit/bin. |
| Corrections: "his words win" | A correction to one fact often leaves facts built on it un-updated (ripple effects, Cohen 2024: an analogy from weight editing) | When you correct something, Keeper flags every entry that rested on it. |
| `kill` / `park` move files | Memory systems are worst at updating and forgetting (MemoryAgentBench: ≤28% on selective forgetting) | Supersede, don't delete. Parked stays searchable. (The draft already moves rather than deletes, which is good.) |
| ≤3 questions in the brief | Stacked questions can blank a neurodivergent reader (one Reddit-sourced report, weak). Horvitz: ask only when the answer resolves a real uncertainty. | One question at a time, ideally as a closed choice ([push] [file]). |
| No streaks or guilt | Self-tracking research: people lapse for ordinary reasons; support re-entry, accept "happy abandonment" (Epstein 2016) | Supported. Add a "welcome back" re-entry shape. |
| Two-week test: "did it catch thoughts you'd have lost?" | Capture-everything archives are rarely used. Value comes from the right cue at the right time (Sellen &amp; Whittaker 2010). | Judge it by "did it hand something back that mattered", not by how much it holds. |

---

## Example exchanges

**Capture burst, then one hook at the pause**
> *(4 voice notes in 90 seconds)*
> Keeper: → 4 filed (CRE-refi ×2, keeper-design, misc).
> *(5 minutes of quiet)*
> Keeper: One thought on the two CRE notes. Want it?

**Challenge tied to your own criteria, not generic devil's advocacy**
> Will: convinced regional banks are fine now
> Keeper: On 9/14 you said you'd change your mind if deposit betas kept rising. Have they? I can check.

**Who said what**
> Will: what did I say the pricing model was?
> Keeper: Your words, Oct 2: "flat fee, no tiers." The usage-based variant was my suggestion on Oct 5, not yours.

**An inference shown when it's made**
> Keeper: New note, INFERRED: money worries spike before Fridays. Keep, edit, or bin?
> Will: bin, that's payroll not worry
> Keeper: Binned. Kept "payroll Fridays" as something you said.

**Interest vs commitment**
> Will: I'm going to learn Rust.
> Keeper: Logged as an interest, third mention since August. Mark it a commitment with a date, or leave it as a recurring interest?

**Re-entry after a lapse**
> Will *(3 weeks later)*: hey
> Keeper: Welcome back. 3 open threads; the liveliest is the FL insurance idea from 9/24. Pick it up, or just dump?

---

## Mistakes most worth avoiding

1. **The flattering mirror.** Memory plus preference-tuning leads to agreement, which leads to confidence without correction. This is the single best-evidenced risk.
2. **Summary-of-summary drift.** Rewriting the picture or profile from its previous version until your hedged "maybe" reads as a plan.
3. **Mixing up who said what.** Keeper's elaborations slowly become "what Will thinks".
4. **Essay replies.** Models are trained toward length, and "filling the vacuum" on a fragmentary input is a named failure. A thought dump is exactly that kind of input.
5. **Ideas before yours.** It pulls your thinking toward the model's defaults (homogenisation, fixation).
6. **Inference from labels.** "Since you have ADHD…" is stereotyping the evidence shows LLMs already do.
7. **Engagement as the goal.** More use is not better use. Stopping can mean it worked.
8. **One vendor holding the only copy.** Humane's pin was bricked and its data deleted (2/2025). Rewind/Limitless capture was shut off after Meta bought it (12/2025). Users reported ChatGPT memories wiped (11/2025).

---

## Evidence that challenges our assumptions

- **An always-available partner may thin your own thinking.** After LLM help, people's *unassisted* creativity was worse (Kumar 2025, n≈1,100). Knowledge workers who trust AI more report less critical thinking (Lee 2025, survey). The most-cited EEG study (Kosmyna 2025) is a small preprint; treat it as weak.
- **Good challenge costs liking.** The anti-overreliance designs that worked best were the least liked (Buçinca 2021). Disagreement reduced willingness to return (CHB Reports 2026, via a news summary). A Keeper that pushes back well may be the one you stop opening. That is a real tension, not a solved one.
- **Labelling inferences may not be enough** (Chandra 2026, a simulation, not a user study).
- **Your memory of what you hand off fades.** People remember offloaded material less. Saving can free memory for new things, but only when the store feels reliable (Storm &amp; Stone 2015; replications mixed).
- **The value may be in the dump itself.** Archives are rarely revisited (Sellen &amp; Whittaker). If so, fast capture plus occasional good resurfacing is the product, and the rest is optional.
- **Generic devil's advocacy barely works.** An interactive devil's advocate improved decision accuracy by a margin that only just reached significance (p = 0.047), and challenging the group majority did nothing (Chiang 2024). Challenge has to be specific and grounded.
- **Nothing tests this exact thing.** No study covers a long-running, single-user, voice-captured AI thinking partner. Almost all of the evidence comes from short lab tasks, often coding, with students or online panels.
- **ADHD/autism evidence is thin.** The one useful clinical signal is a single study: adult ADHD prospective-memory difficulty sat mostly in *planning*, not recall (Fuermaier 2013, n=45+45). That argues for help turning a thought into a next step, not for more reminders. Body doubling is essentially community lore.

---

## Fleet lessons that transfer (from our own memory files)

| Fleet lesson | How it shows up in Keeper |
|---|---|
| The summary is the part that travels and merges what the body kept separate | `picture.md` becomes "what Will thinks". Hedges die there first. |
| A sender's caveats don't survive a hop unless deliberately carried | "Maybe I'd like to…" becomes "Will plans to…" |
| A correction annotated beside an old line leaves both readable | Profile corrections must *replace* the old line; history goes elsewhere |
| Adoption is not validation | An inference read every morning starts to feel established without anyone testing it |
| Carried claims never self-expire | `next:` steps and "Will wants X" sit forever. Keeper needs an age on every claim. |
| A fresh header over a stale body certifies it | A bumped `last_touch` with no real change reads as live |
| Will prefers one living page and fewer, plainer messages (`feedback_research_sessions_living_page_plain_updates`) | Matches the outside evidence on batching and brevity |

---

## Practical note (separate, short)

- **Exportability.** Every lesson from products that died says keep a plain-text copy you control. The Console memory store versions every change, but it is the only copy. PROME and DAEDALUS already ruled out mirroring it into the fleet repo (different trust domain); a personal export (e.g. a periodic zip to your own drive) is a different thing and your call.
- **Voice transcription.** Not researched in this pass. DAEDALUS's relay spec proposes local faster-whisper, which is not installed. One relevant result: messaging inside an app you already use (Telegram) matches what neurodivergent interviewees asked for (Andrabi 2026, abstract only).

---

## Source Quality Assessment

- **Strong:** AI agreeableness (several peer-reviewed papers, the OpenAI postmortem); memory-benchmark findings (ICLR/NeurIPS papers plus vendor preprints that agree against their own interest); interruption and notification science (field studies, 20 years of work); idea homogenisation (meta-analyses).
- **Medium:** proactive-assistant studies (randomized, but small samples of students on coding tasks); scrutable user models (design principle, untested on outcomes); source misattribution (lab psychology carried over to this setting).
- **Weak:** ADHD/autism interaction needs (Reddit analyses, small interview studies, abstracts); resurfacing of self-generated notes (thin and mixed); everything about this exact use case (none exists).
- **Verified by DEWEY at the source this session:** Jain 2025/26, Chandra 2026, Fang 2025, Chen 2025 (incl. 90%/47%, p=0.005, "distracting"/"annoying"), Kumar 2025 (coach condition worst: originality p=0.009; convergent −10.6 points, 95% CI −18.6 to −2.7), ACE 2025 (18,282→122 tokens; 66.7→57.1 vs 63.7 baseline). Everything else was read by a research leg; the table below marks which were only seen as snippets or abstracts.

## References

Tags: [A] academic, [A-pre] preprint, [P] primary, [N] news, [U] unverified/practitioner. "snippet" = a leg saw only a search snippet; "abstract" = abstract only; ✔ = DEWEY re-checked at the source 10/17.

| Claim area | Source | Tag / read level |
|---|---|---|
| Memory profiles raise sycophancy | Jain et al., CHI 2026, https://arxiv.org/abs/2509.12517 | [A] ✔ |
| Memory-induced sycophancy benchmark | PersistBench, https://arxiv.org/abs/2602.01146 | [A-pre] abstract |
| Sycophancy and preference models | Sharma et al. 2023, https://arxiv.org/abs/2310.13548 | [A-pre] |
| GPT-4o rollback postmortem | OpenAI 2025-05-02, https://openai.com/index/expanding-on-sycophancy/ | [P] via quotes (403 to direct fetch) |
| Users prefer sycophantic AI | Cheng et al., *Science* 2026, https://arxiv.org/abs/2510.01395 | [A] |
| Spiraling despite warnings | Chandra et al. 2026, https://arxiv.org/abs/2602.19141 | [A-pre] ✔ simulation |
| Autism-disclosure stereotyping | Wohn et al., CHI 2026, https://arxiv.org/abs/2601.12690 | [A] abstract |
| State vs trait variance | Harry et al., ACL Findings 2026, https://arxiv.org/abs/2601.15395 | [A] |
| Scrutable user models | Kay, Personis https://pythonhosted.org/personis/Intro.html | [A] docs |
| Reactions to AI memory | Chen/Molina/Liao/Cho, CHI 2026 (DOI 10.1145/3772318.3791635); Monteiro 2026 https://arxiv.org/abs/2605.10013 | [A] abstract / [A-pre] |
| Intention→behaviour gap | Webb &amp; Sheeran 2006 https://eprints.whiterose.ac.uk/1580 | [A] abstract |
| Summaries vs raw in memory | LongMemEval https://arxiv.org/html/2410.10813 ; LoCoMo https://arxiv.org/html/2402.17753 ; Mem0 https://arxiv.org/html/2504.19413 | [A] / [A-pre] / vendor |
| Context collapse | ACE, Zhang et al. https://arxiv.org/html/2510.04618 | [A-pre] ✔ |
| Telephone-game drift | https://arxiv.org/abs/2407.04503 | [A] |
| Forgetting is hardest | MemoryAgentBench https://arxiv.org/html/2507.05257 | [A-pre] |
| Ripple effects of corrections | Cohen et al., TACL 2024 https://aclanthology.org/2024.tacl-1.16/ | [A] analogy |
| Filing vs search | Whittaker et al., CHI 2011 https://research.ibm.com/publications/am-i-wasting-my-time-organizing-email-a-study-of-email-refinding | [A] abstract |
| Capture archives rarely used | Sellen &amp; Whittaker, CACM 2010 https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/p70-sellen.pdf | [A] full text |
| Resumption cues | Hodgetts &amp; Jones 2006 https://pure.cardiffmet.ac.uk/en/publications/contextual-cues-aid-recovery-from-interruption-the-role-of-associ/ | [A] abstract |
| Improving ideas leads to misattribution | Perfect &amp; Stark 2012 https://www.psycharchives.org/handle/20.500.12034/1134 | [A] abstract |
| Chatbot-induced false memories | Chan et al. 2024 https://arxiv.org/abs/2408.04681 | [A-pre] |
| Mixed-initiative principles | Horvitz, CHI 1999 https://erichorvitz.com/chi99horvitz.pdf | [A] full text |
| Proactive coding assistant | Chen et al., CHI 2025 https://arxiv.org/abs/2410.04596 | [A] ✔ |
| Proactive agent disruption | Pu et al., CHI 2025 https://arxiv.org/abs/2502.18658 | [A] |
| Timing at stopping points | Kuo et al., IUI 2026 https://arxiv.org/abs/2601.10253 | [A-pre] |
| Interruption cost | Iqbal &amp; Horvitz, CHI 2007 https://www.erichorvitz.com/CHI_2007_Iqbal_Horvitz.pdf | [A] full text |
| Notification batching | Fitz et al. 2019 https://scholars.duke.edu/publication/1402953 | [A] |
| Verbosity bias | Singhal et al. 2024 https://arxiv.org/abs/2310.03716 ; YapBench https://arxiv.org/abs/2601.00624 | [A] / [A-pre] |
| Neurodivergent LLM use | Carik et al. https://arxiv.org/abs/2410.06336 ; Giri et al., CHI 2026 (DOI 10.1145/3772318.3791334); Andrabi 2026 | [A-pre] / secondary / abstract |
| Idea homogenisation | Doshi &amp; Hauser 2024 https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532 ; Meincke et al. 2025 https://www.nature.com/articles/s41562-025-02173-x ; Holzner meta https://arxiv.org/abs/2505.17241 | [A] / [A] summary / [A-pre] |
| AI help hurts later unassisted work | Kumar et al., CHI 2025 https://arxiv.org/abs/2410.03703 | [A] ✔ |
| Critical thinking and AI trust | Lee et al., CHI 2025 https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf | [A] survey |
| Devil's advocate | Chiang et al., IUI 2024 https://par.nsf.gov/servlets/purl/10524816 | [A] full text |
| Questions beat explanations | Danry et al., CHI 2023 https://dspace.mit.edu/handle/1721.1/150613 | [A] |
| Effective but disliked | Buçinca et al., CSCW 2021 https://arxiv.org/abs/2102.09692 | [A] |
| Creativity-support principles | Shneiderman, CACM 2007 https://www.cs.umd.edu/~ben/papers/Shneiderman2007Creativity.pdf | [A] full text |
| Heavy use and worse outcomes | Fang et al. 2025 https://arxiv.org/abs/2503.17473 | [A-pre] ✔ RCT |
| Identity change and grief | De Freitas et al. https://arxiv.org/abs/2412.14190 | [A-pre] |
| Plan-making quiets open loops | Masicampo &amp; Baumeister 2011 (JPSP 101(4)) | [A] snippet; no replication found |
| Reminders and follow-through | Gilbert 2014 https://discovery.ucl.ac.uk/id/eprint/1457331/ | [A] snippet |
| Self-tracking abandonment | Epstein et al., CHI 2016 https://pmc.ncbi.nlm.nih.gov/articles/PMC5428074/ | [A] full text |
| ADHD planning vs recall | Fuermaier et al. 2013 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3590133/ | [A] snippet |
| Product shutdowns | TechCrunch 2025-02-18 (Humane); 9to5Mac 2025-12-05 (Limitless); PiunikaWeb 2025-11-05 (ChatGPT memories) | [N] snippet |

## Process Report
**Searches run:** five parallel Opus research legs, one per CATO question, with about 210 tool calls between them (~625K sub-agent tokens), plus six source re-checks by DEWEY. The full `/deep-research` harness was not used; Will asked for light process on this experiment (`feedback_experiments_run_light_not_fleet_process`).
**Data gaps:** no study of a long-running single-user AI thinking partner; no ADHD/autism-specific trial of an ideation or memory partner; no evidence on how *often* an AI should challenge; no measured drift of an LLM-kept user profile; no controlled test of "say more?" disclosure in chat; Masicampo &amp; Baumeister replication not found; voice transcription not researched.
**Source frustrations:** OpenAI pages returned 403 (postmortem quoted via search extracts and Simon Willison); Amershi et al.'s guideline table wouldn't open; several 2026 papers were readable only as abstracts.
**Confidence in findings:** Medium overall. High that memory amplifies agreement and that summaries should not replace raw records; medium on initiative design (good studies, wrong domain); low on anything neurodivergent-specific.
**Process note:** a fleet memory (`feedback_subagent_web_tools_not_autoloaded`) prompted a mid-run reminder to all legs to load web tools explicitly. All five confirmed the tools were live, so no leg's "not found" is a tooling artefact.
**If I had more time/tools:** PubMed pass on adult-ADHD external memory aids; full text of Kay's and Amershi's papers; a one-week trial on Keeper's own model, measuring agreement with and without `profile.md` loaded (Jain-style), since effects vary by model.
**Suggestions:** the cheapest high-value test once Keeper runs is to ask it the same judgment question with and without the profile loaded and compare.
