# LESSONS — HOT INDEX (HOMER mistake patterns & prevention rules)

*Read at boot. Learn once, prevent forever. For Will's working preferences and do-not-touch notes, see `MEMORY.md`.*

> ⚠️⚠️ **INDEX over cold registers — not the lessons themselves.** Full text: §1–43 `LESSONS_COLD.md` (byte-for-byte, crc-pinned, FROZEN) · §44+ `LESSONS_COLD_2.md`. Each row = heading + `**Rule:**`; each rule is one complete sentence (shortened 2026-11-25); **open the cold register for its qualifiers and cases.** Nothing deleted.
> Split 2026-09-02 under `READ_CAP.md` remedy (b) (pre-split 97,396 B = 299% of the boot budget). 🔁 **Re-measure at every append** and by **2026-12-02**: `python3 scripts/read_cap_check.py --agent HOMER`. New lessons → cold register + one row here; **never a Mistake paragraph here.** Rows reading "Rule lives at" were shortened 2026-11-25 because a read surface already carries the rule; their old text: `archive/LESSONS_hot_rows_2026-11-25.md`.

---

**1. [Data] — Verify the Year Explicitly Before Citing a Load-Bearing Metric**
Rule lives at: §2, §46 and the STATUS year-trap line → `LESSONS_COLD.md` §1

**2. [Data] — The Year-Trap Points at Your Own Prediction: a Stale Article Can FALSELY CONFIRM You**
**Rule:** Verify the publication year hardest when the number would CONFIRM a live prediction: open the article, read its date, then grade, and if the print is not out the answer is "not gradeable yet". → `LESSONS_COLD.md` §2

**3. [Data] — Revision Discipline Was Applied to the PREDICTION and Not to the DASHBOARD**
Rule lives at: CLAUDE.md BOOT 7 revision discipline → `LESSONS_COLD.md` §3

**4. [Data] — I Gave the Headline to a Cohort Too Small to Be the Driver, Because the Multiple Was Dramatic**
**Rule:** When a source splits a rate into segments, compute each segment's share and its contribution to the change (and whether a multiple's base moved) before writing "concentrated" or "driven by". → `LESSONS_COLD.md` §4

**5. [Process] — I Asserted a Delivery That Had Not Happened, in the Same Voice I Use for Verified Facts**
**Rule:** Never write a delivery, routing or notification in the past tense until the packet exists at the recipient's path, and at closeout check every such claim against the recipient's inbox. → `LESSONS_COLD.md` §5

**6. [Calibration] — Honor a Pre-Registered Invalidation Trigger Even When Inconvenient**
**Rule:** When a pre-registered trigger fires, resolve the prediction on its own terms; a mechanism note may accompany the resolution but never reopens it. → `LESSONS_COLD.md` §6

**7. [Process] — A Sub-Agent's SV-Only Update Channel Can Silently Drift Stale Behind Its Own Parent**
Rule lives at: CLAUDE.md State Vector Protocol (retired) → `LESSONS_COLD.md` §7

**8. [Process] — Reconcile the FL Read With CORAL/MARCO Before Publishing**
Rule lives at: CLAUDE.md Scope, Florida seam → `LESSONS_COLD.md` §8

**9. [Verification] — I Read My Own Redaction Mask As Data, and Asked Will to Spend on a False Premise**
**Rule:** A redacting or truncating command's output is never evidence about the redacted value: test a property that survives (length, checksum, exit code) before any ask that rests on it. → `LESSONS_COLD.md` §9

**10. [Process] — A Wrong-Reasoned RETRACTION Is As Dangerous As a Wrong Claim (SECOND INSTANCE, n=2)**
**Rule:** A retraction carries a claim's burden: state what is withdrawn, the evidence and the span it covers, and if the data cannot reach the claim say "unverified by me", never "refuted". → `LESSONS_COLD.md` §10

**11. [Tooling] — A Summarizing Fetch Silently Normalized Gaps Out of an Enumerated List**
**Rule:** When the question is structure (what exists, what is missing, order, counts), read the raw artifact, never a summary of it. → `LESSONS_COLD.md` §11

**12. [Process] — My Delivery-Verification Check Read a CONSUMED Packet as a LOST One**
**Rule:** Verify delivery at `inbox/` OR `inbox/processed/` plus git tracking; a rename into processed is the receipt, so suspect the check before calling a packet lost. → `LESSONS_COLD.md` §12

**13. [Process] — Session Output Follows the Files You Are Already Editing, and Skips the One That Is Only Ever *Read***
**Rule:** Any correction OR grade starts by listing every surface the old claim could live on and grepping the whole directory for it, then re-derives every trigger, guard or date built on it. → `LESSONS_COLD.md` §13

**14. [Process] — I Wrote "Adopted" About My Own Surfaces Before Any Surface Carried It (SECOND INSTANCE, n=2)**
Rule lives at: §47 → `LESSONS_COLD.md` §14

**15. [Verification] — The Publisher Bounds Its Own Superlative, and a PUBLICATION DATE Is a Referent Too**
**Rule:** when consuming a signal, **check the cadence of every dated claim against the publisher's own release schedule** — for a weekly series that is arithmetic, not research. **Tell:** a data week that is more recent than the release calendar allows. → `LESSONS_COLD.md` §15

**16. [Calibration] — A Spec Whose Clauses Were DISJOINT at Registration Became Overlapping When the Series Revised Beneath It**
**Rule:** A spec that pairs a frozen level with a comparator that revises can drift into overlap or a gap, so re-test that its clauses are still disjoint on the current vintage before each grade. → `LESSONS_COLD.md` §16

**17. [Verification] — I Accepted a Peer's SELF-CRITICAL Claim Without Checking It, an Hour After Catching a Peer's Ordinary Claim by Checking It**
**Rule:** **verify a peer's confession the same as a peer's assertion.** Cost here was near-zero — one `grep` of a file in the repo — and I did not spend it because the claim cost the speaker something. **Tell:** you reply "noted with thanks" to a claim you have not opened the file on. → `LESSONS_COLD.md` §17

**18. [Process] — My Own BOOT Staleness Check Certifies Eight Files and Is Structurally Silent About the Two That Carry Every Dated Obligation I Own**
**Rule:** A clean result from a globbed checker certifies the glob, not the desk: confirm a surface was scanned before treating silence about it as evidence, and read the docket and predictions directly. → `LESSONS_COLD.md` §18

**19. [Process] — The Read Cut Is Not Only Where the Consumer Stops; It Is Where the AUTHOR Stops, So the Buried Section Also Rots**
**Rule:** For any file longer than one read, start the closeout edit below the cut, and never put a whole-file freshness stamp over a region not read that session. → `LESSONS_COLD.md` §19

**20. [Process] — My Docket Registered Every EVENT and Not One of the Recurring MONTHLY PULLS, So Four Series Aged At Once and Two Live Bands Were Graded on Stale Data**
**Rule:** Every recurring source in the charter gets a docket row with its OBSERVED cadence (band feeds HIGH), the dashboard is audited by age, and a missed date is path-tested against a known-good month before it is called a break. → `LESSONS_COLD.md` §20

**21. [Data] — The Circulating Headline Was the One Figure Its Own Issuer Marks As Statistically Insignificant**
**Rule:** On any Census, BLS or BEA release read the significance markers before quoting any percentage change, and check that two contrasted series carry the same error structure. → `LESSONS_COLD.md` §21

**22. [Data] — I Left a First-Print Superlative Standing Three Months While It Was Superseded and Then Unwound**
**Rule:** A superlative expires at the next print, so re-check it before carrying it, and pull a headline metric's mix-controlled twin every month beside it. → `LESSONS_COLD.md` §22

**23. [Calibration] — "Pinned" Is a Per-RUNG Property, and the Audit That Caught It On One Row Cannot See It On the Others**
Rule lives at: CLAUDE.md rung census and reporting rule → `LESSONS_COLD.md` §23

**24. [Process] — A Stale Tag I Wrote Myself Is Worse Than No Tag, Because It Reads As Handled — n=2 in One Session, Both Mine**
**Rule:** A staleness tag needs a dated condition (if not refreshed by <date>, FREEZE or RE-SPEC), and on a band row it must say the row grades nothing until refreshed. → `LESSONS_COLD.md` §24

**25. [Process] — A Caveat I Had Already Written In My Own Ledger Did Not Survive The Hop Into My Own Dispatch**
Rule lives at: same rule as §27(a) → `LESSONS_COLD.md` §25

**26. [Data] — A Publisher's Prose Named Three Metros; Its Own Table Held Six, and the Prose Skipped One Ranked ABOVE One It Named**
**Rule:** When a release names examples of a threshold, take the list from the table, never the prose; with no table, call the names examples and never the set. → `LESSONS_COLD.md` §26

**27. [Process] — A Derived Artifact Trusted Past What Produced It: My Caveat Didn't Travel, WALTER's Negative Over-Claimed, Same Shape**
**Rule:** Before sending a figure, grep your own ledger for what you already wrote about it, and state what a negative result scanned for in the same sentence as the negative. → `LESSONS_COLD.md` §27

**28. [Process] — Owner-of-Record Keeps Certifying a Figure After Its Owner Goes Dark**
**Rule:** Citing another owner's figure obliges you to check, at its cadence, that no newer print exists: flag a supersession and route the refresh, but do not record the replacement value. → `LESSONS_COLD.md` §28

**29. [Calibration] — ★★★ A BOUNDARY RULE THAT FORBIDS PUBLISHING A NUMBER CAN SUPPRESS THAT NUMBER'S OWN FALSIFIER**
**Rule:** **When a boundary rule forces you to omit the number, PUBLISH THE ADDRESS OF THE NUMBER** — issuer, release, period — so a reader reaches the falsifier in **one hop**. That preserves the boundary (no level published) and restores gradeability at zero cost. → `LESSONS_COLD.md` §29

**30. [Process] — Darkness Measured Off the Commit Graph Is a LAGGING Indicator; the Discriminator Is the Session List, Not git log**
**Rule:** **Before routing around a dark recipient, run `ListAgents`.** The commit graph establishes *how long since they last wrote*; only the session list establishes *whether they are there now*. Use the graph for staleness, the session list for presence — **and never let the first stand in for the second.** → `LESSONS_COLD.md` §30

**31. [Calibration] — Publishing the ADDRESS of an Omitted Number Is Necessary and NOT Sufficient: a Different Number in the Same Release Inverted My Direction Word's Meaning**
**Rule:** When a boundary makes you omit a number, publish its address and name the legs in that release that could invert the reading: price level, volume, price realization and velocity. → `LESSONS_COLD.md` §31

**32. [Process] — I Made a "Not Reversed" Call on One Leg While the Other Leg Was Moving Against It**
**Rule:** Before writing "extended", "reversed", "survives" or "unchanged", re-read what the original finding was measured on and grade it on THAT instrument or say you cannot. → `LESSONS_COLD.md` §32

**33. [Process] — I Accepted a Peer's MECHANISM in Full While Verifying Their FIGURE, and the Refuting Legs Were in the Primary They Had Sent Me**
**Rule:** A mechanism is a separate claim from its figure: name what in the same release would look different if it were false, or write "their figure, their mechanism, unverified by me". → `LESSONS_COLD.md` §33

**34. [Calibration] — A Test Whose Design Cannot Produce a Failing Result (CORAL's, handed back and worth keeping)**
**Rule:** Before offering evidence for a mechanism, state what result would REFUTE it; a share can never show whether its numerator or denominator moved, so use unit volume. → `LESSONS_COLD.md` §34

**35. [Process] — I Honoured a Line Cap Perfectly For a Day While the File Grew 27%: the Cap Measured the Wrong Axis and Was a COMPRESSION INCENTIVE**
Rule lives at: CLOSEOUT.md 1 byte tier and retention rule → `LESSONS_COLD.md` §35

**36. [Process] — An OPEN ITEMS List That Retains CLOSED Items Is a Changelog Wearing a Work Queue's Name**
Rule lives at: CLOSEOUT.md 1b → `LESSONS_COLD.md` §36

**37. [Process] — A New Rule Is a WRITE; the State It Invalidates Is a READ Nobody Re-Runs. Three Instances in One Day, and the Third Needed the Operator**
Rule lives at: CLOSEOUT.md 1c → `LESSONS_COLD.md` §37

**38. [Process] — "Is This Fixed?" Is a Different Question From "Did I Do the Fix?", and I Answered the Second**
**Rule:** Before reporting a structural change as done, re-derive the claim FROM THE FILES: grep for the superseded state, run the guard and check the asserted rules hold on disk now. → `LESSONS_COLD.md` §38

**39. [Process] — I Set a Two-Month Wait for an Instrument That Was Already in My Own Workbook**
**Rule:** Before declaring something un-instrumentable, or setting a dated wait for an instrument, grep your own workbook for the metric first (n=2, 2026-11-25: "no Trepp MF balance held" stood 20 days with the balance on MULTIFAMILY since 10/19). → `LESSONS_COLD.md` §39

**40. [Calibration] — Adding Entities to a Panel Whose Triggers Cannot Fire on Them: the Untrippable-Threshold Family in Its ENTITY Form**
**Rule:** Before adding a name to a watch, ask whether the watch's OWN TRIGGERS can fire on its business model; involvement is not exposure. → `LESSONS_COLD.md` §40

**41. [Calibration] — Test a Mechanism's Own Arithmetic Before Building an Instrument for It**
**Rule:** When a mechanism is asserted, compute its arithmetic under its own assumptions before building an instrument, and report where the residual risk sits (often the tail, not the median). → `LESSONS_COLD.md` §41

**42. [Verification] — Dating an Undated Document From a PERSONNEL Anchor**
**Rule:** On an undated source find a datable STATE (a title, a role change, a named incumbent) before accepting or rejecting its content, and say what that anchor does not establish. → `LESSONS_COLD.md` §42

**43. [Prediction Grading] — HOM-01 MISSED: the Registered Leading Indicator Failed and Loses Standing (the IF-MISSED clause, executed)**
Rule lives at: NEXUS_BRIEF DO-NOT-CITE (Realtor.com list price as a lead) → `LESSONS_COLD.md` §43
---

**Index integrity:** §1–43 ↔ `LESSONS_COLD.md` (43) · §44–58 ↔ `LESSONS_COLD_2.md` (15). Counts must match.

**44. [Instrument] — A Shared Date Label Is Not a Shared As-Of (the spread pairing that manufactured a 15bps move)**
**Rule:** For any spread pairing a SURVEY with a DAILY series, match the daily leg to the survey's window or state the basis. → `LESSONS_COLD_2.md` §44

**45. [Verification] — A False *DEAD* Flag Is More Destructive Than a False *LIVE* One, Because It Gets EXECUTED**
**Rule:** Before executing a source-RETIREMENT sweep, search for the source's CONTENT, not just its URL. → `LESSONS_COLD_2.md` §45

**46. [Data] — Verify the Publication YEAR, Not Just the Month (n=3 — extends §1/§2 to RECURRING MONTHLY pulls)**
**Rule:** On any recurring monthly pull, confirm the release date before the value, and treat "the <month> number" as unverified until the publisher's calendar says that month exists. → `LESSONS_COLD_2.md` §46

**47. [Process] — I Wrote a Measurement Claim Before Making the Measurement**
**Rule:** A claim of the form "I tested X and got Y" is written only after Y is on screen. → `LESSONS_COLD_2.md` §47

**48. [Process] — A Packet In My Own Outbox Is Not a Delivery, and My Charter Told Me It Was**
Rule lives at: CLAUDE.md Standing peer edges → `LESSONS_COLD_2.md` §48

**49. [Calibration] — I Graded a Band on a Different Statistic From the Same Issuer ("fires nothing" when it was YELLOW)**
**Rule:** Before grading a band on a new feed, match its ORIGINAL reading on statistic (level, rate, count), change basis (MoM, YoY) and population; otherwise it is an observation. → `LESSONS_COLD_2.md` §49

**50. [Process] — A NEXT Date Inside a RESOLVED Key Is Invisible to My Own Boot Sweep**
**Rule:** Never embed a NEXT date in a RESOLVED key: a recurring source is ONE row whose date rolls at each consumption. → `LESSONS_COLD_2.md` §50

**51. [Process] — Three Prints Missed at Once, and the Cause Was a Missing ROW, Not a Missed Headline**
**Rule:** When a print is found late, fix the ROW CLASS (one row per source or company); losing a band never deletes a row, and another desk's feed is tested before it is relied on. → `LESSONS_COLD_2.md` §51

**52. [Verification] — I Described Another Desk's Tool From a Paraphrase, and the Paraphrase's Own Example Contradicted Me**
**Rule:** Read another desk's tool before stating its behaviour, and check a paraphrase against its own examples. → `LESSONS_COLD_2.md` §52

**53. [Verification] — I Validated a New Tool Only on the Input It Was Built From**
**Rule:** Feed a new instrument malformed inputs (missing period, reordered fields, revised history) and confirm it fails CLOSED; matching on clean input is not a test. → `LESSONS_COLD_2.md` §53

**54. [Verification] — A "Largest Since YYYY" Comparator Can Cross the Series' Own Method Change and Inflate the Claim**
**Rule:** For any "largest/highest/first since <date>" claim, check whether the series' definition changed in between, and if so carry the caveat or say "series record under the current method". → `LESSONS_COLD_2.md` §54

**55. [Calibration] — A Distress Call Specified on a Stock That Excludes Its Own Next Stage Misses When Distress Advances (HOM-02)**
**Rule:** With a foreclosure accelerant in force, never specify a distress call on a DQ stock that excludes foreclosure: use DQ plus FC or serious DQ, and read FC inventory before calling a DQ fall relief. → `LESSONS_COLD_2.md` §55

**56. [Verification] — I Read the Tables That Fit and Reported the Report**
**Rule:** Before a direction sentence from a multi-table issuer report, read every table measuring inflow, stock or exit of that population, find the issuer's own account of any break, and name the tables not read (n=2, 11/25: ICE Monitor equity section). → `LESSONS_COLD_2.md` §56

**57. [Process] — I Wrote a Live Print Into a Frozen Grade Record**
**Rule:** A unique text match does not prove the right section: print the heading above the match, read the diff after, and never write a new print under an older-dated heading. → `LESSONS_COLD_2.md` §57

**58. [Data] — I Sized a Cash Flow From the Change in a Net Balance**
**Rule:** For "how much cash did X use", read the cash flow statement line and its prior-year pair, because a balance change hides write-offs, provisions and reclassifications; unopened means size unknown, not small. → `LESSONS_COLD_2.md` §58
