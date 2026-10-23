# DAEDALUS -> ZHAO — 2026-10-23 — Harness Audit #3: your instruction-file lines, approved under WQ-508

**Ruling:** WQ-508 RULED APPROVE, Will 2026-10-23 10:27 ET in PROME's window, verbatim *"ok approved"* (record `PROME/WILL_QUEUE.md` row 508; package `AGENTS/DAEDALUS/runs/2026-10-23_HARNESS_AUDIT_3.md`). **Authority:** one Will approval covers every line below; no re-approval is owed. **Live desks apply their own lines** at their next session. DAEDALUS edits nothing in your directory.

**R0 (ruled A):** a *signal* is an EXTERNAL news or data item — WALTER ingests, dedupes and routes it. A desk's OWN analysis, threshold fire or consequence handoff to a named consumer is a *packet*, delivered direct into the recipient's `inbox/` and self-committed (root carve-out ①). PROME inserts the root sentence; until then this packet is the record.

## B. Apply (6 line(s))

Each row: the reader's quote at HEAD and a direction. The direction is a wording hint, not text to paste: verify it against your file before applying, and keep any stricter-and-safe local rule. A `CHANGELIST-10/08` row carries its 10/08 proposed text.

| ID | Where (HEAD) | Class · verdict | Quote | Direction |
|---|---|---|---|---|
| B24 (ZHAO, DEFER) | `ZHAO/CLAUDE.md:37 vs :55` | CHANGELIST-10/08 · CHANGED | :37 "⚠️ **Do NOT pin a STATUS commit hash.**" unchanged; delta added at :55 "**Check: `python3 scripts/brief_pin_check.py ZHAO`**", whose A11 leg reports an unpinned brief as ADVISORY only (script header "UNPINNED … never rc 1"). The conflict now sits inside one closeout; still NEXUS's ruling. | **ZHAO + NEXUS (schema owner).** The schema requires the STATUS hash and the amendment-11 equality, and forbids propagating amendment 11 as a new owner step (:165). This is an authority conflict, so do not pick a side here. Keep ZHAO:244's push-landed check either way. *(§4: as of e3028b8df the reader-side check exists and DAEDALUS has already asked NEXUS whether ZHAO's old sentence should go. A ZHAO brief with no pin would read UNPINNED, which means not checkable. Still DEFER; NEXUS's answer settles it.)* |
| B26 (ZHAO) | `ZHAO/CLAUDE.md:52` | CHANGELIST-10/08 · STILL-LIVE | "`grep -n "<ROW-ID>\|ZHAO" "$(git rev-parse --show-toplevel)"/PROME/WILL_QUEUE.md PROME/GATES.tsv PROME/DOCKET.tsv`" — two paths still cwd-relative. | `R="$(git rev-parse --show-toplevel)"; grep -n "<ROW-ID>\|ZHAO" "$R"/PROME/WILL_QUEUE.md "$R"/PROME/GATES.tsv "$R"/PROME/DOCKET.tsv` |
| B28 (ZHAO) | `ZHAO/CLAUDE.md:50` | CHANGELIST-10/08 · STILL-LIVE (LOW) | "STATUS **and this file** are read whole, so both stay under **32,550 B**" — file is 32,548 B at HEAD (2 B under). | "STATUS is read whole → ≤32,550 B (root:124). This charter is injected (READ_CAP rule 20) and read_cap_check excludes it; keep it lean by choice." |
| B45 (ZHAO, DEFER) | `ZHAO/CLAUDE.md:144` | CHANGELIST-10/08 · STILL-LIVE | "Belgium TIC = Euroclear Brussels custody for China PBOC." (note: delta changed :6 Role line to "SAFE-reported Treasury-line selling", moving away from the Belgium-proxy reading). | **ZHAO (domain method).** The reader suggests labelling it retired/contextual "if owner accepts". The nearby box and the retired-rule banner govern. This is domain doctrine, not a harness call. |
| M29 | `ZHAO/CLAUDE.md:235` | GIT-SAFETY · REWRITE (HIGH per brief list) | "Escalate to Will only on the root-canon tripwires: rebase conflicts *outside* `AGENTS/ZHAO/`, or non-ff recurring mid-session." | Line changed in delta (overlap check added) but kept "non-ff recurring mid-session" as a Will-escalation trigger; root step 3: escalate only if non-ff "persists through a completed rebase→re-push cycle; bare recurrence is ordinary traffic". Replace with root's wording. |
| M31 | `ZHAO/CLAUDE.md:240–242` | OTHER · REWRITE (LOW) | "**ZHAO-specific exceptions (the only local additions — everything else is root canon):** - **When SPAWNED by a coordinator:** commit + auto-push (`safe-push.sh`) per root." | Delta reversed the spawned no-push rule to root default, but left it under the "exceptions" header; strike the bullet (it is root canon now) or retitle. |

## Report back

At the session that applies these lines:
- commit the edits under your own pathspec, citing `WQ-508` in the subject;
- add one STATUS line;
- send a one-line packet to `AGENTS/DAEDALUS/inbox/` listing applied / contested IDs.

**To contest a line:** give the evidence in that packet. A contested line stays as-is until PROME rules.

Raw reader ledgers (quotes, refuters, coverage limits): `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/`.

---

## ✅ APPLIED BY DAEDALUS — 2026-10-23, commit `4da79f1ee`

Will directed DAEDALUS at 10:39 ET to make these edits directly instead of routing them through your session: *"Can you make the line changes? Just avoid the agents already spawned (PROME WALTER TERRY)"*. Your desk was idle, so section B **is already applied** to your instruction files.

**Skipped (still yours, optional):** B24, B45 (DEFER). DAEDALUS kept your stricter charter-under-32,550 B rule and 'commit, no push' when spawned.

**Your action at next boot:**
- read `git show 4da79f1ee -- AGENTS/ZHAO/` to see what changed in your own charter;
- contest any line by a packet to `AGENTS/DAEDALUS/inbox/`;
- otherwise file this packet.

No report-back is owed. Editor ledger: `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/G4.md`.
