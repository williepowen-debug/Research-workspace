# LESSONS hot rows shortened 2026-11-25 14:32 ET

Verbatim from `LESSONS.md` at commit `47d954b1e0` (sha256 `34fc2fab44874fc57f23fc974af6ff63e6120e52f01bc5550a8361b184a05291`). Full lesson text was and stays in `LESSONS_COLD.md` / `LESSONS_COLD_2.md`.

---

**1. [Data] — Verify the Year Explicitly Before Citing a Load-Bearing Metric**
**Rule:** Before citing any web-pulled metric as **load-bearing** (capable of changing a prediction confidence, a STATUS color, or a transmission-chain status), confirm the year explicitly from the primary source — either the article's publication date or an explicit year-stamp on the cited number itself. Relative … → `LESSONS_COLD.md` §1

**3. [Data] — Revision Discipline Was Applied to the PREDICTION and Not to the DASHBOARD**
**Rule:** For any series that **revises prior months as a matter of course** (Census new-home sales, starts/permits, construction spending, BLS payrolls, BEA GDP, FMHPI), a dashboard row must either **(a)** be refreshed from the newest release — carrying the revised prior alongside the current print — or **(b)** carry … → `LESSONS_COLD.md` §3

**7. [Process] — A Sub-Agent's SV-Only Update Channel Can Silently Drift Stale Behind Its Own Parent**
**Rule:** As a top-level agent, HOMER now owns its own boot-time staleness check (`scripts/ledger_staleness.py`, two-clock workbook headers) instead of relying on an SV harvest cadence set by another agent's spawn schedule. Never let the authoritative copy of a domain's data be a file the domain owner doesn't itself … → `LESSONS_COLD.md` §7

**8. [Process] — Reconcile the FL Read With CORAL/MARCO Before Publishing**
**Rule:** Before publishing an FL housing figure, check whether CORAL or MARCO already owns an overlapping read. Different metrics on the same geography aren't automatically contradictory, but an unreconciled divergence sitting silently across two agents' STATUS files is data fiction waiting to be cited wrong. Flag … → `LESSONS_COLD.md` §8

**14. [Process] — I Wrote "Adopted" About My Own Surfaces Before Any Surface Carried It (SECOND INSTANCE, n=2)**
**Rule:** **"Adopted," "encoded," "applied," "re-keyed" and "now reads" are claims about ARTIFACTS and must not be written until the artifact carries the change.** Concretely: **make the edit, then write the sentence** — never the reverse, and never in the same breath as agreeing to the recommendation. If the edit is … → `LESSONS_COLD.md` §14

**23. [Calibration] — "Pinned" Is a Per-RUNG Property, and the Audit That Caught It On One Row Cannot See It On the Others**
**Rule:** **Audit thresholds per RUNG, not per row**, and phrase the verdict as a claim about the sample unless the window is long enough to be a claim about the metric. **The fix for a pinned rung is a REPORTING rule, not a level change:** state the highest **UNCROSSED** rung and the distance to it, never the highest … → `LESSONS_COLD.md` §23

**25. [Process] — A Caveat I Had Already Written In My Own Ledger Did Not Survive The Hop Into My Own Dispatch**
**Rule:** **When a figure carries a caveat you recorded yourself, the packet must be written from the LEDGER ROW, not from the release.** Concretely: before sending a figure, grep your own ledger for it and read what you already said about it. This is `finding_rederived_signal_loses_the_senders_caveats` **with the … → `LESSONS_COLD.md` §25

**35. [Process] — I Honoured a Line Cap Perfectly For a Day While the File Grew 27%: the Cap Measured the Wrong Axis and Was a COMPRESSION INCENTIVE**
**Rule:** **Size-govern a document on the axis a READER actually consumes — bytes — and make the control a RETENTION rule, not a compression target.** ⛔ *(the 150/170KB tier below is RETIRED 2026-09-29 — live tier = soft 22,785 B / hard 32,550 B, `CLAUDE.md` CLOSEOUT 1)* Adopted here: soft **150KB** / hard **170KB**, derived from a measured irreducible core (~127KB of dashboard + open items + catalysts) rather than invented; **one … → `LESSONS_COLD.md` §35

**36. [Process] — An OPEN ITEMS List That Retains CLOSED Items Is a Changelog Wearing a Work Queue's Name**
**Rule:** **A closed item leaves the live queue at the closeout that closes it** — `git mv` to `archive/` with a one-line pointer naming the item numbers. **Retain in archive, never delete**, because several will be cited elsewhere and must stay reachable. ⚠️ **Test to apply: "if a reader worked only the rows in this … → `LESSONS_COLD.md` §36

**37. [Process] — A New Rule Is a WRITE; the State It Invalidates Is a READ Nobody Re-Runs. Three Instances in One Day, and the Third Needed the Operator**
**Rule:** **When a session adopts, demotes, retires or re-scopes a rule, GREP FOR THE SUPERSEDED TERM before committing** — excluding archives and processed mail — **and ask of each hit "does this assert the OLD rule as LIVE?"** Historical and past-tense mentions are fine; an undemoted live assertion is not. **Wired … → `LESSONS_COLD.md` §37

**43. [Prediction Grading] — HOM-01 MISSED: the Registered Leading Indicator Failed and Loses Standing (the IF-MISSED clause, executed)**
**Rules:** ① The Realtor.com headline median list YoY is DOWNGRADED to context — never again the named mechanism of a registered prediction unless re-validated against a completed cycle. ② Any candidate list-price lead must be specified on the MIX-CONTROLLED series ($/sqft), not the median. ③ A lead-lag claim … → `LESSONS_COLD.md` §43

---

**Index integrity:** §1–43 ↔ `LESSONS_COLD.md` (43) · §44–57 ↔ `LESSONS_COLD_2.md` (14). Counts must match.

**48. [Process] — A Packet In My Own Outbox Is Not a Delivery, and My Charter Told Me It Was**
**Rule:** A delivery claim is verified at the RECIPIENT'S path, never the sender's. Packets go INTO … → `LESSONS_COLD_2.md` §48
