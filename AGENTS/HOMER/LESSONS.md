# LESSONS — HOT INDEX (HOMER mistake patterns & prevention rules)

*Read at boot. Learn once, prevent forever. For Will's working preferences and do-not-touch notes, see `MEMORY.md`.*

> ⚠️⚠️ **THIS IS AN INDEX OVER A COLD REGISTER, NOT THE LESSONS THEMSELVES. Full text of all 43 entries — Mistake, diagnosis, corollaries, every secondary rule — is at `LESSONS_COLD.md`, reproduced BYTE-FOR-BYTE. Nothing was deleted.**
> **Split 2026-09-02** under `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` remedy (b): the pre-split file was **97,396 B = 180% of the 54,250 B read cap** and **299% of the 32,550 B boot budget**, so *every* boot was silently reading a fragment — and rule 12 says the fragment lost is whatever convention puts LAST, which here was the newest lessons.
> **Each row below carries the entry's heading and its `**Rule:**` line.** A row ending `…` is truncated — **open the cold register before acting on a truncated rule.** The Mistake narrative is never here.
> 🔁 **DATED RE-TRIGGER, not a leanness claim (`READ_CAP.md` rule 7):** re-measure this file at **every append** and unconditionally by **2026-12-02**, whichever first — `python3 scripts/read_cap_check.py --agent HOMER`. **New lessons append to the COLD register and add one row here.** ⚠️ If you ever find yourself writing a full Mistake paragraph into this file, the split has failed.

---

**1. [Data] — Verify the Year Explicitly Before Citing a Load-Bearing Metric**
**Rule:** Before citing any web-pulled metric as **load-bearing** (capable of changing a prediction confidence, a STATUS color, or a transmission-chain status), confirm the year explicitly from the primary source — either the article's publication date or an explicit year-stamp on the cited number itself. Relative … → `LESSONS_COLD.md` §1

**2. [Data] — The Year-Trap Points at Your Own Prediction: a Stale Article Can FALSELY CONFIRM You**
**Rule:** Year-verify **hardest** when the number would CONFIRM a live prediction, not just when it would surprise you. Two specific triggers: **(a)** an annually-recurring release (monthly HPI, quarterly DQ surveys) whose prior-year article occupies the same headline shape — search relevance ranks these … → `LESSONS_COLD.md` §2

**3. [Data] — Revision Discipline Was Applied to the PREDICTION and Not to the DASHBOARD**
**Rule:** For any series that **revises prior months as a matter of course** (Census new-home sales, starts/permits, construction spending, BLS payrolls, BEA GDP, FMHPI), a dashboard row must either **(a)** be refreshed from the newest release — carrying the revised prior alongside the current print — or **(b)** carry … → `LESSONS_COLD.md` §3

**4. [Data] — I Gave the Headline to a Cohort Too Small to Be the Driver, Because the Multiple Was Dramatic**
**Rule:** **When a source breaks a rate into segments, compute each segment's share and its contribution to the change BEFORE writing any sentence with "concentrated," "driven by," or "the real story is."** Three lines of arithmetic. A large *rate* move on a small *weight* is not a driver, and a large multiple on a … → `LESSONS_COLD.md` §4

**5. [Process] — I Asserted a Delivery That Had Not Happened, in the Same Voice I Use for Verified Facts**
**Rule:** **Never write a delivery, routing, or notification in the past tense until the artifact exists.** Concretely: (a) if the packet isn't written yet, write the intention — *"routing to CARL next"* / *"CARL: not yet sent"* — never *"I've flagged it to them"*; (b) **write the cc packet before the sentence … → `LESSONS_COLD.md` §5

**6. [Calibration] — Honor a Pre-Registered Invalidation Trigger Even When Inconvenient**
**Rule:** When a pre-registered trigger fires, resolve the prediction on its own terms — don't retroactively construct a mechanism-survives argument to keep it alive. A mechanism note can (and should) accompany the resolution ("CRE/MF stress isn't gone — the CMBS book still diverges") without reopening the specific … → `LESSONS_COLD.md` §6

**7. [Process] — A Sub-Agent's SV-Only Update Channel Can Silently Drift Stale Behind Its Own Parent**
**Rule:** As a top-level agent, HOMER now owns its own boot-time staleness check (`scripts/ledger_staleness.py`, two-clock workbook headers) instead of relying on an SV harvest cadence set by another agent's spawn schedule. Never let the authoritative copy of a domain's data be a file the domain owner doesn't itself … → `LESSONS_COLD.md` §7

**8. [Process] — Reconcile the FL Read With CORAL/MARCO Before Publishing**
**Rule:** Before publishing an FL housing figure, check whether CORAL or MARCO already owns an overlapping read. Different metrics on the same geography aren't automatically contradictory, but an unreconciled divergence sitting silently across two agents' STATUS files is data fiction waiting to be cited wrong. Flag … → `LESSONS_COLD.md` §8

**9. [Verification] — I Read My Own Redaction Mask As Data, and Asked Will to Spend on a False Premise**
**Rule:** **A redacting or truncating command's output can never be evidence about the redacted value.** To test presence/absence without disclosure, measure a property that survives redaction — **length** (`awk -F= '/^KEY=/{print length($2)}'`), a checksum, or an exit code. Never infer a value from a pattern you … → `LESSONS_COLD.md` §9

**10. [Process] — A Wrong-Reasoned RETRACTION Is As Dangerous As a Wrong Claim (SECOND INSTANCE, n=2)**
**Rule:** **A retraction is a claim and carries the same evidentiary burden.** Before publishing one, state (a) exactly which assertion is being withdrawn, (b) the evidence, and (c) **the span/scope that evidence covers** — then check (b) actually reaches (a). **If your data cannot reach the claim, the honest verdict … → `LESSONS_COLD.md` §10

**11. [Tooling] — A Summarizing Fetch Silently Normalized Gaps Out of an Enumerated List**
**Rule:** **When the question is about structure — what exists, what is missing, ordering, numbering, counts — read the raw artifact, not a summary of it.** Summarizers optimize for a clean reading and will regularize irregularities. Reserve summarizing fetches for prose content; use `curl` + `grep` on links/IDs … → `LESSONS_COLD.md` §11

**12. [Process] — My Delivery-Verification Check Read a CONSUMED Packet as a LOST One**
**Rule:** verify delivery as **`inbox/<file>` OR `inbox/processed/<file>`, plus git-tracked.** Better still, when the path is absent from both, check `git log --diff-filter=RD -- <inbox path>` for an `R100` rename before concluding anything — **the rename IS the receipt, and it is stronger evidence than presence** (it … → `LESSONS_COLD.md` §12

**13. [Process] — Session Output Follows the Files You Are Already Editing, and Skips the One That Is Only Ever *Read***
**Rule:** **A correction pass must ENUMERATE its surfaces before it starts, not follow the ones the session happens to be editing.** Write the list first — every file where the superseded claim could live — and tick them off. **Then grep for the superseded string across the whole agent directory** rather than trusting … → `LESSONS_COLD.md` §13

**14. [Process] — I Wrote "Adopted" About My Own Surfaces Before Any Surface Carried It (SECOND INSTANCE, n=2)**
**Rule:** **"Adopted," "encoded," "applied," "re-keyed" and "now reads" are claims about ARTIFACTS and must not be written until the artifact carries the change.** Concretely: **make the edit, then write the sentence** — never the reverse, and never in the same breath as agreeing to the recommendation. If the edit is … → `LESSONS_COLD.md` §14

**15. [Verification] — The Publisher Bounds Its Own Superlative, and a PUBLICATION DATE Is a Referent Too**
**Rule:** when consuming a signal, **check the cadence of every dated claim against the publisher's own release schedule** — for a weekly series that is arithmetic, not research. **Tell:** a data week that is more recent than the release calendar allows. → `LESSONS_COLD.md` §15

**16. [Calibration] — A Spec Whose Clauses Were DISJOINT at Registration Became Overlapping When the Series Revised Beneath It**
**Rule:** **any spec pairing a frozen absolute level with a vintage-floating relative comparator will drift into overlap — or into a dead gap — as the series revises beneath it.** **Re-reading the spec cannot catch this**, because the spec never changed. **Only re-evaluating the CLAUSE GEOMETRY against the current … → `LESSONS_COLD.md` §16

**17. [Verification] — I Accepted a Peer's SELF-CRITICAL Claim Without Checking It, an Hour After Catching a Peer's Ordinary Claim by Checking It**
**Rule:** **verify a peer's confession the same as a peer's assertion.** Cost here was near-zero — one `grep` of a file in the repo — and I did not spend it because the claim cost the speaker something. **Tell:** you reply "noted with thanks" to a claim you have not opened the file on. → `LESSONS_COLD.md` §17

**18. [Process] — My Own BOOT Staleness Check Certifies Eight Files and Is Structurally Silent About the Two That Carry Every Dated Obligation I Own**
**Rule:** **`rc=0` from a globbed checker certifies THE GLOB, not the desk.** Before trusting a clean scan, ask **what it enumerated** — and treat *"it did not complain about X"* as evidence only if you have confirmed X is **in scope**. ⇒ **PROME's formulation from the same evening is the general fix and I am adopting … → `LESSONS_COLD.md` §18

**19. [Process] — The Read Cut Is Not Only Where the Consumer Stops; It Is Where the AUTHOR Stops, So the Buried Section Also Rots**
**Rule:** **for any file with content past the single-read cut, the closeout edit pass must START below the cut, not end there.** Concretely: `sed -n '<cut>,$p'` the file and re-read the tail **before** touching the head — the head is what you were going to edit anyway. **And never let a whole-file freshness stamp sit … → `LESSONS_COLD.md` §19

**20. [Process] — My Docket Registered Every EVENT and Not One of the Recurring MONTHLY PULLS, So Four Series Aged At Once and Two Live Bands Were Graded on Stale Data**
**Rule:** **Every recurring data source named in the charter gets a docket row with its OBSERVED cadence — not a remembered ritual** (`finding_mechanize_the_cap_not_the_ritual`). A source that feeds a band gets `HIGH` priority and the band named in its `threshold_signal` cell. **And audit the dashboard by AGE, not … → `LESSONS_COLD.md` §20

**21. [Data] — The Circulating Headline Was the One Figure Its Own Issuer Marks As Statistically Insignificant**
**Rule:** **On any Census/BLS/BEA release, read the significance markers before quoting ANY percentage change**, and never inherit a percentage from a summary that has stripped them (`finding_effect_below_instrument_detection_floor` — below the noise floor is *no* evidence, not weak evidence). **Then check whether the … → `LESSONS_COLD.md` §21

**22. [Data] — I Left a First-Print Superlative Standing Three Months While It Was Superseded and Then Unwound**
**Rule:** **A superlative is a claim about a DISTRIBUTION and expires the moment the next print lands.** Never carry one past the next release without re-checking it, and **when a publisher offers a mix-controlled twin of a headline metric, pull BOTH every month** — the divergence between them is the finding, and it … → `LESSONS_COLD.md` §22

**23. [Calibration] — "Pinned" Is a Per-RUNG Property, and the Audit That Caught It On One Row Cannot See It On the Others**
**Rule:** **Audit thresholds per RUNG, not per row**, and phrase the verdict as a claim about the sample unless the window is long enough to be a claim about the metric. **The fix for a pinned rung is a REPORTING rule, not a level change:** state the highest **UNCROSSED** rung and the distance to it, never the highest … → `LESSONS_COLD.md` §23

**24. [Process] — A Stale Tag I Wrote Myself Is Worse Than No Tag, Because It Reads As Handled — n=2 in One Session, Both Mine**
**Rule:** **A staleness tag is only permitted with a dated condition attached** — *"`[STALE — Jan]`; if not refreshed by <date>, FREEZE or RE-SPEC"* — because a tag without an expiry is a note that replaced the work. **And when tagging a row that feeds a BAND, say what the band now grades: "this row grades nothing … → `LESSONS_COLD.md` §24

**25. [Process] — A Caveat I Had Already Written In My Own Ledger Did Not Survive The Hop Into My Own Dispatch**
**Rule:** **When a figure carries a caveat you recorded yourself, the packet must be written from the LEDGER ROW, not from the release.** Concretely: before sending a figure, grep your own ledger for it and read what you already said about it. This is `finding_rederived_signal_loses_the_senders_caveats` **with the … → `LESSONS_COLD.md` §25

**26. [Data] — A Publisher's Prose Named Three Metros; Its Own Table Held Six, and the Prose Skipped One Ranked ABOVE One It Named**
**Rule:** **When a release names exemplars of a threshold, take the list from the TABLE, never from the prose.** If no table is published, report the named members as **exemplars** (*"including Charlotte, Denver and Dallas"*) and never as the set. ⚠️ **A publisher's narrative selection from its own data is neither a … → `LESSONS_COLD.md` §26

**27. [Process] — A Derived Artifact Trusted Past What Produced It: My Caveat Didn't Travel, WALTER's Negative Over-Claimed, Same Shape**
**Rule (two halves, both adopted):** **(a) Before sending a figure, grep your own ledger for it and read what you already wrote about it** — the dispatch must be written FROM the ledger, not from the source the ledger already corrected. **(b) A negative result must state what it scanned for**, in the same sentence as … → `LESSONS_COLD.md` §27

**28. [Process] — Owner-of-Record Keeps Certifying a Figure After Its Owner Goes Dark**
**Rule:** **A cited owner-of-record figure carries the CITER's obligation to check that a newer print exists** — that is not the same as the obligation to publish one, and on a boundary-ruled figure it must not become one. **Flag the supersession in place, route the refresh to the owner (or to PROME if the owner is … → `LESSONS_COLD.md` §28

**29. [Calibration] — ★★★ A BOUNDARY RULE THAT FORBIDS PUBLISHING A NUMBER CAN SUPPRESS THAT NUMBER'S OWN FALSIFIER**
**Rule:** **When a boundary rule forces you to omit the number, PUBLISH THE ADDRESS OF THE NUMBER** — issuer, release, period — so a reader reaches the falsifier in **one hop**. That preserves the boundary (no level published) and restores gradeability at zero cost. → `LESSONS_COLD.md` §29

**30. [Process] — Darkness Measured Off the Commit Graph Is a LAGGING Indicator; the Discriminator Is the Session List, Not git log**
**Rule:** **Before routing around a dark recipient, run `ListAgents`.** The commit graph establishes *how long since they last wrote*; only the session list establishes *whether they are there now*. Use the graph for staleness, the session list for presence — **and never let the first stand in for the second.** → `LESSONS_COLD.md` §30

**31. [Calibration] — Publishing the ADDRESS of an Omitted Number Is Necessary and NOT Sufficient: a Different Number in the Same Release Inverted My Direction Word's Meaning**
**Rule:** **When a boundary forces you to omit a number, publish its address AND name the legs in the same release that could invert its interpretation.** ⚠️⚠️ **AND THE LEG SET WAS CORRECTED HOURS LATER BY THIS RULE FAILING ON ME. I first wrote "the inverting leg is almost always price and volume." THE LEGS THAT … → `LESSONS_COLD.md` §31

**32. [Process] — I Made a "Not Reversed" Call on One Leg While the Other Leg Was Moving Against It**
**Rule:** **Before writing "extended," "reversed," "survives" or "unchanged" about a prior finding, re-read what the ORIGINAL finding was measured on — and grade it on THAT instrument or say you cannot.** A domain label ("FL condo") is not an instrument, and two legs of the same market routinely move in opposite … → `LESSONS_COLD.md` §32

**33. [Process] — I Accepted a Peer's MECHANISM in Full While Verifying Their FIGURE, and the Refuting Legs Were in the Primary They Had Sent Me**
**Rule:** **A mechanism claim is a separate claim from the figure it rides on, and needs its own falsifier named before acceptance.** Before writing *"which I accept"* about a causal reading, ask: **what in this same release would look different if the mechanism were false?** If the answer is "I don't know," the … → `LESSONS_COLD.md` §33

**34. [Calibration] — A Test Whose Design Cannot Produce a Failing Result (CORAL's, handed back and worth keeping)**
**Rule (adopted, mine to run too):** **before proposing evidence for a mechanism, state what result would REFUTE it.** If no available value of the proposed measure refutes it, the measure is not evidence. ⚠️ **For share-based tests specifically: a share moves when EITHER numerator or denominator moves, so a share can … → `LESSONS_COLD.md` §34

**35. [Process] — I Honoured a Line Cap Perfectly For a Day While the File Grew 27%: the Cap Measured the Wrong Axis and Was a COMPRESSION INCENTIVE**
**Rule:** **Size-govern a document on the axis a READER actually consumes — bytes — and make the control a RETENTION rule, not a compression target.** Adopted here: soft **150KB** / hard **170KB**, derived from a measured irreducible core (~127KB of dashboard + open items + catalysts) rather than invented; **one … → `LESSONS_COLD.md` §35

**36. [Process] — An OPEN ITEMS List That Retains CLOSED Items Is a Changelog Wearing a Work Queue's Name**
**Rule:** **A closed item leaves the live queue at the closeout that closes it** — `git mv` to `archive/` with a one-line pointer naming the item numbers. **Retain in archive, never delete**, because several will be cited elsewhere and must stay reachable. ⚠️ **Test to apply: "if a reader worked only the rows in this … → `LESSONS_COLD.md` §36

**37. [Process] — A New Rule Is a WRITE; the State It Invalidates Is a READ Nobody Re-Runs. Three Instances in One Day, and the Third Needed the Operator**
**Rule:** **When a session adopts, demotes, retires or re-scopes a rule, GREP FOR THE SUPERSEDED TERM before committing** — excluding archives and processed mail — **and ask of each hit "does this assert the OLD rule as LIVE?"** Historical and past-tense mentions are fine; an undemoted live assertion is not. **Wired … → `LESSONS_COLD.md` §37

**38. [Process] — "Is This Fixed?" Is a Different Question From "Did I Do the Fix?", and I Answered the Second**
**Rule:** **Before reporting a structural change as done, re-derive the claim FROM THE FILES, not from the session's own record of what it did.** Concretely: grep for the superseded state, run the guard, and check that the retention/consistency rules the change asserts actually hold on disk *right now*. ⚠️ **And … → `LESSONS_COLD.md` §38

**39. [Process] — I Set a Two-Month Wait for an Instrument That Was Already in My Own Workbook**
**Rule:** **Before declaring something un-instrumentable — or setting a dated wait for an instrument — GREP YOUR OWN WORKBOOK for the metric first.** The question to ask is not *"is this measurable?"* but **"have I already measured it?"** ⚠️ Highest-risk moment is exactly when writing a *negative* conclusion, because … → `LESSONS_COLD.md` §39

**40. [Calibration] — Adding Entities to a Panel Whose Triggers Cannot Fire on Them: the Untrippable-Threshold Family in Its ENTITY Form**
**Rule:** **Before adding a name to a watch, ask whether the watch's OWN TRIGGERS can fire on that name's business model** — not merely whether the name is involved in the phenomenon. **Involvement is not exposure.** ⚠️ A coverage gap that is really correct scoping looks identical to a real gap from the outside: … → `LESSONS_COLD.md` §40

**41. [Calibration] — Test a Mechanism's Own Arithmetic Before Building an Instrument for It**
**Rule:** **When a mechanism is asserted, compute its own arithmetic under its own assumptions BEFORE instrumenting it.** A mechanism that fails its own worst case needs no instrument. ★ **And when it survives, the computation names the DISCRIMINATOR** — here, hold period, which then tested against the population (NAR … → `LESSONS_COLD.md` §41

**42. [Verification] — Dating an Undated Document From a PERSONNEL Anchor**
**Rule:** **On any undated source, hunt for a datable STATE — a title, a role transition, a "soon to be," a named incumbent — before accepting or rejecting its content.** ⚠️ **And state what the anchor does NOT establish:** here it bounded the *quote*, not the *video*, and I could not date the video itself. **Two … → `LESSONS_COLD.md` §42

**43. [Prediction Grading] — HOM-01 MISSED: the Registered Leading Indicator Failed and Loses Standing (the IF-MISSED clause, executed)**
**Rules:** ① The Realtor.com headline median list YoY is DOWNGRADED to context — never again the named mechanism of a registered prediction unless re-validated against a completed cycle. ② Any candidate list-price lead must be specified on the MIX-CONTROLLED series ($/sqft), not the median. ③ A lead-lag claim … → `LESSONS_COLD.md` §43

---

**Index integrity:** 43 entries here, 43 in `LESSONS_COLD.md` — the counts must match, and a mismatch means an append skipped one side. 39 rules are truncated and marked `…`.
