# WQ-701 — the outside pass-8 rules review: eight items, exact text for one batch approval

**Status:** RULED B, the core set (A2, B, D, G, H2), by Will 2026-11-16 22:07 ET; see § Ruling and as-applied text at the end. Sections A to H below are the proposal as he saw it and are kept as written; where § Ruling's text differs, § Ruling governs. **Written:** 2026-11-16 22:0x ET by PROME (session prome-d2, laptop).
**Source:** an outside read-only review Will pointed PROME at in chat 21:47 ET, saved as received at `PROME/reports/2026-11-16_pass8-rules-review/REVIEW_as-received.md` (its repository pin 544159ad81fc). PROME's check of its claims: chat 21:5x ET, summarized in § Verification below.
**Will's word so far:** PROME's chat 2026-11-16 22:01 ET, verbatim: *"can you fix these 8 items now?"* PROME's reading, stated back to him: act on all eight; text that changes what a root rule means, a number, or PROME's own limits is shown to him exactly before it is applied. Under that word PROME already did item H1 below (commit named there). Everything else in this file waits for his word on this text.

Canon drafts live here and are transplanted once (`PROME/CLAUDE.md` § Session Process Controls). Each lettered item can be approved or dropped alone.

## A — Charter read cap (review item 1) · root `CLAUDE.md` § Data Hygiene, the read-cap bullet

**Problem:** root makes 32,550 B binding for any surface read whole. `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` rule 20 (DAEDALUS, 2026-09-19) exempts charters because the harness injects them. Since WQ-385 (2026-10-05) every spawn reads its charter explicitly (`PROME/COMPLETION_SPEC.md`, the spawn-brief paragraph), and Codex desks get no injection. Twelve of 45 desk charters are over 32,550 B (measured 2026-11-16 with `wc -c`): LABOR 55,594 · OSPREY 55,284 · FALCON 51,475 · AEOLUS 50,695 · CARL 49,162 · OTTO 48,602 · SAM 41,844 · HOMER 41,649 · HENRY 37,886 · DEWEY 35,944 · BOND 34,353 · VULCAN 34,215. The single-read limit the cap was derived from is about 54,250 B (`docs/CANON_PROVENANCE.md`, key `data-read-cap`); LABOR and OSPREY are past it.

| Choice | What it is | Trims owed |
|---|---|---|
| A1 | Charters are bound by the same 32,550 B | 12 |
| **A2 (PROME's recommendation)** | Charters get their own ceiling, 50,000 B | 4: LABOR, OSPREY, FALCON, AEOLUS |
| A3 | No number; LABOR and OSPREY trim under 54,250 B once | 2 |

**Proposed text for A2**, appended to the read-cap bullet after "(A different constant from the `MEMORY.md` 25,600 B auto-load cap.)":

> **Charters have their own ceiling: a desk's `CLAUDE.md` stays under 50,000 B** (it is read explicitly at every spawn, and one read cuts off near 54,250 B). Below that ceiling a charter is a context-cost surface under `READ_CAP.md` rule 20; the owner trims by moving history out, never by compressing what remains.

**Follow-through if ruled:** DAEDALUS adds one sentence to rule 20 naming the ceiling (its own blueprint, by packet). The four desks trim at their next sessions, each its own charter, history moved to its own archive, no rule's meaning changed; PROME verifies bytes and reads each diff. PROME's reason for A2 over A1: the harm the cap exists to prevent is a cut-off read, and that starts near 54,250 B; eight more trims buy context savings only. ⚠️ The 50,000 figure is PROME's choice of margin, not a measured threshold.

## B — Follow-through on rulings (review item 2) · no new checker

**Problem:** root rule #10 (close the proposal loop) relied on memory. Since 2026-11-16 PROME writes a dated DOCKET row "CLOSE THE PROPOSAL LOOP on WQ-n" at each ruling with an owed execution (four exist), but no manual says so and no instrument checks it.

**Proposed:** extend the EXISTING closeout check "done rows … rulings-reach-ledger (WQ-417 P1)" in `PROME/tools/prome_gate.py` with one advisory line: a RECENTLY DONE row marked RULED whose text names neither an execution receipt nor a DOCKET row is listed. No new script, no new rule text. Built under the repair-completion discipline (acceptance conditions first, one independent reader) at PROME's next working session. ⚠️ Advisory only: it lists, it does not block.

## C — Value sweep of prose rules (review item 3) · Will's standing words must be lifted for it

**Conflict:** Will, 2026-11-11 14:02 ET (no further general review, no broad retrospective) and 2026-11-16 19:16 ET (no other study or review cycle). This item is a review cycle.

**Proposed, if he lifts them for this one pass:** ONE read-only Opus reader, root `CLAUDE.md` and `PROME/CLAUDE.md` only (about 55 KB), after the 11/24 follow-ups. For each rule: cited, fired or prevented anything in the last 60 days of commits and records, yes or no with the evidence. Output: one list of retirement candidates, brought to Will as ONE trim batch (item D). Desk charters are not in this pass. **PROME's recommendation: approve it for after 11/24, not now.**

## D — Cheaper trims (review item 4) · `PROME/CLAUDE.md` § Session Process Controls, Review budget

**Problem:** WQ-679 removed about 4 KB of rule text behind 55 KB of ruling records (`2026-11-12_wq678-RULED.md` 25,332 B, `2026-11-12_wq679-RULED.md` 29,697 B) plus DAEDALUS's packet. Class C13 (2026-11-11) already gives PROME's own manuals a one-read path; root, `AGENTS.md` and PROME's charter are excluded from it.

**Proposed text**, a new sentence at the end of the Review-budget bullet:

> **Trim batch:** an edit that only deletes text or moves it out verbatim, adds no rule and loosens none, in root `CLAUDE.md`, `AGENTS.md` or this charter, is ONE ruling by Will for the batch, ONE blind result read confirming that no rule's meaning changed, and a record of at most one page; no plan read. A trim the reader cannot confirm is meaning-neutral leaves the batch and takes the ordinary path.

⚠️ This lowers PROME's own review requirement for one class of edit. It is Will's to grant.

## E — Unwritten owners and one citation form (review item 5) · root `CLAUDE.md`, Scope note

**What PROME found at the files (last 60 days of commit subjects):** `scripts/` is committed by CATO (34), PROME (22), DAEDALUS (21), WALTER (4). The `REGINALD_CHANNEL.md` files in OZK and WAL are committed mostly by OZK (13) and WAL (16) themselves, REGINALD 8. The review's ownership list is therefore not exact, and PROME does not propose naming owners per file.

**Proposed text**, appended to the Scope note:

> **Shared tool paths:** a tool under `scripts/` or a definition under `.claude/` is committed by the desk that authored the change, explicitly pathed. **Any commit outside the committer's own directory and the carve-outs names its authority in the commit body as one line, `Authority: <WQ-n, or Will's dated word, or the ruling record's path>`.**

## F — Precedence (review item 6) · root `CLAUDE.md` § How The System Works

**Proposed text**, appended to the PROME bullet after "unless it conflicts with Will or higher-priority instructions.":

> **Order when instructions conflict:** Will's word in the session, then root `CLAUDE.md`, then `USER.md`, then a PROME task packet, then the desk's own charter, then memory files. `PROME/ROSTER.md` and `AGENTS/_NETWORK.md` keep their named subjects. A conflict this order does not settle goes to PROME.

⚠️ The review cites no actual conflict that this would have settled; PROME found none tonight. It is cheap and it is a new line of root text.

## G — Sites that block automation (review item 7) · root `CLAUDE.md` § Data Hygiene, new bullet

**Proposed text:**

> **Blocked sites:** a site that challenges or refuses automated access (a CAPTCHA, a bot challenge, a block on this address) is unusable by automation. Stop, use another source, and tell Will. Never change an identity string, rotate an address or use a proxy to get past a block. A plain client string on an open public endpoint is not evasion; SEC's required contact string stays (WQ-600).

**Not proposed:** a sweep of the roughly 163 Python scripts under `AGENTS/` and `FORGE/` that send a browser identity string (`grep -rl "Mozilla/5.0" --include=*.py`). A string on an open endpoint is not evasion. Each desk fixes a script at its next ordinary touch only where the string was added AFTER a block. The review's BRENT and CFTC instance is NOT verified by PROME; BRENT is asked by packet to state what happened.

## H — Small fixes (review item 8)

- **H1, DONE on Will's 22:01 ET word:** the boot line in eight charters (BOND, BROCK, FALCON, LABOR, OSPREY, OTTO, SAM, VIOLET) now reads `git pull --rebase`. One token per file, no meaning change. Commit: `git log -1 --format=%h -- AGENTS/SAM/CLAUDE.md`.
- **H2, proposed:** delete root's now-unneeded sentence, the last of the Git Protocol **Never** paragraph: *A desk charter's bare "`git pull`" boot line means this form.* A grep of every desk charter for a bare `git pull` boot line returns nothing after H1.
- **H3, PROME recommends NO change:** `.claude/` and `PROME/.claude/` stay two copies. The review says they can drift unnoticed; they cannot: the boot gate's BLOCKING parity check compares them every boot (2026-11-16 21:15 ET: 9 definitions identical). Replacing one copy with a pointer risks the boot runner for no gain.

## Net effect on root `CLAUDE.md` if A2, E, F, G and H2 are all applied

Four additions and one deletion: root grows by roughly 1.3 KB. This is the opposite direction from Will's 10/31 word (fewer rules); A, F and G each settle a question the rules now leave to each session, E and F are the two PROME would drop first.

## Verification (PROME, 2026-11-16 21:5x ET)

VERIFIED at the files: the twelve charter sizes · rule 20's text and date · the spawn-brief explicit-read paragraph · the eight bare `git pull` lines · the two ruling-record sizes · `read_cap_check.py --fleet` 4 desks over budget and 25 in the 70 to 75% band. DIFFERS: manifest defects 1 desk tonight, not 6; browser-identity scripts 163 `.py` files, not 167. WRONG: "skills can drift unnoticed" (H3). OUT OF DATE: "nothing follows up after a ruling" (B). NOT CHECKED: the review's three companion passes (not on this machine), its growth table, its 267-of-12,364 scope count, the BRENT and CFTC instance.

## Review plan if ruled

Root canon: this file is the plan-read artifact. ONE blind read of the approved items' text here before the transplant; ONE edit of root `CLAUDE.md` carrying all approved root items; ONE blind read of the result; ❌ only, at most one further edit; residue declared here. `PROME/CLAUDE.md` (item D) the same, in the same two reads. On the word this file is renamed `…-RULED.md`.

## Ruling and as-applied text (added 2026-11-16 22:1x ET, PROME prome-d2)

**Will's word:** PROME's chat 2026-11-16 22:07 ET (prompt clock), verbatim: *"okay go ahead with your recommendations"*, in reply to PROME's block on WQ-701 whose recommendation was B, the core set: A2, B, D, G, H2. **Not approved, not applied:** C (rule sweep), E (shared-tools line), F (precedence line). H3: no change. A1 and A3 were not chosen.

**Plan read:** ONE blind reader (coldreader, Sonnet), ledger `PROME/reports/2026-11-16_pass8-rules-review/plan_read_ledger.md`: 3 blocking, 14 minor, 2 clean. The three blocking findings were fixed in the text BEFORE the transplant; each fix narrows or clarifies what Will approved and none widens it:

| Finding | Fix |
|---|---|
| A-1: the 50,000 sentence did not say it replaces 32,550 for charters, so a literal reader held a charter to both | The sentence now says "in place of 32,550 B" and names the path `AGENTS/<NAME>/CLAUDE.md`; the citation of READ_CAP rule 20 is gone from root (which also removes minor A-2) |
| D-2: a rule could be deleted as a "duplicate" or moved to a file nobody reads | The record must list every sentence deleted or moved and where the same rule still stands on a boot-read path; a sentence that is the only home of a rule, number, level or owner is out of the class |
| G-2: a refusal caused by a MISSING required client string read as "stop" | Supplying a string the site itself requires is stated as compliance, not evasion; the WQ-600 pointer is dropped from root |

**As applied, root `CLAUDE.md` § Data Hygiene, end of the read-cap bullet (A2):**

> **Desk charters are the one exception: for a desk's `AGENTS/<NAME>/CLAUDE.md` the ceiling is 50,000 B, in place of 32,550 B** (it is read explicitly at every spawn, and one read cuts off near 54,250 B); the owner meets it by moving history out, never by compressing what remains.

**As applied, root `CLAUDE.md` § Data Hygiene, new bullet before Direct Messaging (G):**

> **Blocked sites:** a site that challenges or refuses automated access (a CAPTCHA, a bot challenge, a block on this address) is unusable by automation. Stop, use another source, and tell Will. Never change an identity string, rotate an address or use a proxy to get past a block. Supplying a client or contact string the site itself requires (SEC's is the example) is compliance, not evasion, and a plain client string on an open public endpoint is not evasion.

**As applied, root `CLAUDE.md` Git Protocol, the Never paragraph (H2):** its last sentence, *A desk charter's bare "`git pull`" boot line means this form.*, is deleted. The header's Latest-amendment line names this record.

**As applied, `PROME/CLAUDE.md` § Session Process Controls, end of the Review-budget bullet (D):**

> **Trim batch (WQ-701 D, Will 2026-11-16)** — an edit that only deletes text or moves it out verbatim, in root `CLAUDE.md`, `AGENTS.md` or this charter, is ONE ruling by Will for the batch, ONE blind result read, and a record of at most one page; no plan read. The record lists every sentence deleted or moved and, for each, where the same rule still stands on a boot-read path, or that it stated no rule. A sentence that is the only home of a rule, number, level or owner is not in this class. A trim the reader cannot confirm is meaning-neutral leaves the batch and takes the ordinary path.

`docs/CANON_PROVENANCE.md` gains two reason entries (keys `data-charter-ceiling`, `data-blocked-sites`).

**Declared residue (minor flags NOT fixed, from the plan read):**
- A-3: sub-agent charters, root `CLAUDE.md` and `PROME/CLAUDE.md` are not named by the ceiling; it covers `AGENTS/<NAME>/CLAUDE.md` only.
- A-4: no instrument enforces 50,000; `read_cap_check.py` excludes charters by rule 20. CARL (49,162 B) is 838 B under the ceiling.
- A-5: the byte list in § A was 9 B stale for three desks at the read.
- D-1: the trim batch is an exception to this charter's own Pre-edit cold read bullet; that bullet is not cross-referenced.
- D-3: "batch", "one page" and who may be the blind reader are not defined.
- D-4: the reader's doubt is not required to be written down.
- G-1, G-3, G-4: "a block on this address" and "a proxy" are not defined; a 429 rate limit or a 5xx is not addressed (PROME's reading: a rate limit is waited out, not a block).
- G-5: "tell Will" does not say how a desk does it; PROME's reading: a desk flags PROME by packet and PROME tells Will.
- G-6: existing scripts that send a browser string are not judged by this rule.
- H-2, H-3: bare `git pull` lines remain in archived copies and in `AGENTS/DAEDALUS/builds/hawk_split/MANIFEST_A_core.md:33` (a planned charter, DAEDALUS's).
- READ_CAP rule 20 still says charters are never rotated on read-cap grounds until DAEDALUS amends it (packet sent); root governs meanwhile.

**Result read (2026-11-16 22:11 ET):** ONE second blind reader (coldreader, Sonnet; it saw the diff and the two files, not this record or the plan ledger), ledger `PROME/reports/2026-11-16_pass8-rules-review/result_read_ledger.md`: blocking 0, minor 7, clean 3. No further edit was made. Its minor flags, added to the declared residue: the charter exception names desk charters only (as A-3) · READ_CAP rule 20 conflicts until DAEDALUS amends it (as above) · no grace period is stated for charters already over 50,000 B (PROME's reading: the four trim at their next ordinary sessions, packets sent) · a default client string refused with 403 and replaced by a plain one sits between "never change an identity string" and "a plain client string is not evasion" (PROME's reading: a refusal is a block, so stop and flag; the plain-string sentence covers endpoints that are open) · a 429 may be read as a block and "tell Will" names no channel (as G-3, G-5) · "no plan read" in the trim batch is not cross-referenced to the Pre-edit cold read bullet (as D-1) · "only home" is not qualified by "on a boot-read path".

**Completion states:** root and charter text IMPLEMENTED and INDEPENDENTLY READ (plan read 3 blocking, fixed before the transplant; result read 0 blocking; this episode's reads: 2 of 3) · A2 trims (LABOR, OSPREY, FALCON, AEOLUS) NOT DONE, the desks' own work · B (the advisory line on the existing check) NOT BUILT · DAEDALUS's rule 20 sentence NOT DONE.
