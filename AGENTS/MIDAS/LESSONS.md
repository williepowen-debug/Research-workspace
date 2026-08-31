# MIDAS — LESSONS (durable agent-level learning)

> **INDEX — one hook per lesson. Full bodies: `analysis/LESSONS_ARCHIVE_2026-08.md` (grep by L-number or phrase).**
>
> *Split 2026-08-27 (Will-directed). This file was 64,235 bytes on 48 lines — #2 worst bytes/line in the fleet, and **not in the boot sequence**, so it was write-only: lessons that are never re-read never fire. The hook is the trigger; the archive is the evidence. **Nothing was deleted.***
>
> ⛔ *Two supersession banners govern the bodies (the 8/19 unexplained-share band re-based four times; the computed figure is **87.7–91.1% univariate**). They travel with the bodies — see the archive header before citing any band figure out of **L-33** or **L-35**.*
>
> **Adding a lesson:** append the full row to the archive table AND one hook line here. Keep hooks ≤ ~170 chars and specific enough to trigger a look — a hook nobody greps is a lesson nobody applies.

*36 lessons · L-01 (2026-07-11) → L-36 (2026-08-27) · domain + process learning, distinct from DAEDALUS's fleet-level PATTERNS.tsv.*

| # | Date | Lesson (hook → full text in archive) |
|---|---|---|
| **L-01** | 2026-07-11 | Keep the MONETARY and INDUSTRIAL channels separate — they send different messages and can move independently without contradicting each other. |
| **L-02** | 2026-07-11 | MIDAS's edge is the *tell*, not the *price*: BOND owns the real-rate level, ZHAO owns China macro. |
| **L-03** | 2026-07-11 | Gold's divergence from real yields is the signal, not gold's price. |
| **L-04** | 2026-07-11 | `metals_watch.py` is the priority first increment — the desk was born with the real-yield leg (FRED) but no spot leg. |
| **L-05** | 2026-07-12 | CFTC COT data: WebSearch/WebFetch summarization hallucinates numbers — pull raw JSON directly. |
| **L-06** | 2026-07-12 | A build-session's narrative framing is not itself evidence — verify it against the first live pull before propagating it. |
| **L-07** | 2026-07-12 | A "% vs normal" threshold is meaningless until "normal" is defined — and the base you pick can flip the read. |
| **L-08** | 2026-07-12 | Resolve dueling figures at the primary source and note WHY they differed — usually a stage/proceeding difference, not a contradiction. |
| **L-09** | 2026-07-12 | "Primary-sourced" ≠ "machine-readable pull succeeded." |
| **L-10** | 2026-07-17 | Pre-register prediction branches for BOTH directions of the anchor variable, and anchor a date-test to the EVENT, not a calendar guess. |
| **L-11** | 2026-08-07 | Audit a detector's WINDOW against the window its registered spec names — a lookback several times wider than the detection window is a structural false-positive. |
| **L-12** | 2026-08-07 | A duration threshold needs a stated CONTINUITY rule, or it has two defensible answers and the grader picks one under pressure. |
| **L-13** | 2026-08-07 | Check whether your bands can score the regime you're actually in — a one-sided threshold set reads a live signal as "nothing happening." |
| **L-14** | 2026-08-07 | A search snippet can fuse an old article with fresh figures scraped from its "related posts" — always date the ARTICLE, not the number. |
| **L-15** | 2026-08-07 | A threshold that grades a period ONCE, at publication, is blind to the publisher revising that period — and the revision can move the figure across your kill line retroactively. |
| **L-16** | 2026-08-14 | Two rules quoting the same NUMBER are not necessarily keyed to the same CLOCK — verify each mechanism separately, or a merge silently deletes one of them. |
| **L-17** | 2026-08-14 | A registered threshold anchored to "the [date] close" inherits that print's revisability — and a vendor bar can move under a frozen boundary weeks after you froze it. |
| **L-18** | 2026-08-14 | A data window inherited from another desk's pull is a FREE PARAMETER YOU DID NOT SET — check your own series' extent before you base-rate on it. |
| **L-19** | 2026-08-21 | A continuous front-month futures ticker re-points at each roll, so every delta across it is part contract-change — cite the basis with every figure. |
| **L-20** | 2026-08-21 | A tier that bars making your falsifier harder AND your threshold easier bars ANY change to a spec that is both — escalate, never self-rule. |
| **L-21** | 2026-08-23 | A "% unexplained" is a claim about your MODEL, not the market — an omitted regressor correlated with your thesis inflates the residual you are selling. |
| **L-22** | 2026-08-23 | A load-bearing regression coefficient is not specified by ticker + window — it needs its MISSING-VALUE CONVENTION, or it will not reproduce and you will not know which of you is wrong. |
| **L-23** | 2026-08-23 | Adding a CO-SYMPTOM as a control turns your regression into a different question — a variable on the causal path is a MEDIATOR, not a control. |
| **L-24** | 2026-08-23 | A robustness check aimed at the wrong referent returns CLEAN and buys false confidence — it certifies the leg that never needed checking. |
| **L-25** | 2026-08-23 | An instrument that is ABSENT is not an instrument that is QUIET — and a verdict line that hardcodes its causes will eventually name one that did not happen. |
| **L-26** | 2026-08-23 | A number can be right while the construction label attached to it is wrong — and a citation without its construction is not reproducible. |
| **L-27** | 2026-08-23 | Retracting a claim fixes the artifact that ASSERTED it and leaves every artifact that REPEATED it standing — including packets in other desks' inboxes. |
| **L-28** | 2026-08-23 | An "unconfirmed" flag on your own tracker is a claim about YOUR RECORD, not about the other desk — and it decays into a public accusation if you never check the target. |
| **L-29** | 2026-08-23 | A two-legged comparison read at two different dates labels itself with ONE of them — and a knife-edge classifier then flips state on an in-flight bar. |
| **L-30** | 2026-08-27 | A grep is an instrument, and asserting an ABSENCE from one is a claim that the pattern could have matched the thing you say is missing. |
| **L-31** | 2026-08-27 | A document that MEASURES a drifting quantity cannot hold still — the reproducible script you ship to prove it will later impeach the write-up. |
| **L-32** | 2026-08-27 | Comparing raw percentages across two instruments with different betas is not a comparison — it MANUFACTURES anomalies. |
| **L-33** | 2026-08-27 | A residue flagged as "someone else's, not re-verified" was correct, and I carried it unverified for four days while re-basing six of my own surfaces. |
| **L-34** | 2026-08-27 | The rule I had banked fleet-wide was already violated by the document that produced it — within the same session, hours apart. |
| **L-35** | 2026-08-27 | A figure can survive a Will ruling, a fleet encode, two corrections and twelve surfaces without anyone once COMPUTING it. |
| **L-36** | 2026-08-27 | An instrument that prints a VERDICT beside a VALUE trains you to read the verdict — so a mis-set bound hides the number that would have caught it. |
| **L-37** | 2026-08-27 | A date label cannot falsify itself; a settled price can — the bar moved under a fixed 8/27 label, so pull twice and diff, never inspect metadata. |
| **L-38** | 2026-08-28 | A ledger's vocabulary is a claim about what it can SCORE — a four-branch letter in a binary-only family passes every validator and still misleads. |
| **L-39** | 2026-08-28 | A band on a 1bp-grid series is a step function of its width — five defensible σ windows collapsed to two bands, so register the print set, never "±1σ". |
| **L-40** | 2026-08-28 | Volume identifies the contract; price does not — a continuous ticker stitched history to the dying contract at 1,000 lots while its live bar was the 200,000-lot front month. |
| **L-41** | 2026-08-28 | Pre-register the COMPUTATION and freeze the distribution, not just the boundary — and write the expected value into the dry run, or a plausible failure passes as a pass. |
| **L-42** | 2026-08-28 | An over-cap surface loses whatever convention puts LAST — for STATUS files that's the summary; measure the dropped bytes, never assume them. |
| **L-43** | 2026-08-28 | The exchange's clock is not the vendor's clock — "settled at 13:30" can be true while the feed has no settle at all; verify STATIC, not just closed. |
| **L-44** | 2026-08-31 | "Converged" seen on a live feed is a claim about the INTRADAY series — the DAILY bars can still close on different contracts, and that split contaminated a published both-bases margin. |
