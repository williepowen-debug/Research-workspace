# Design-bundle disposition — PROME 2026-07-31 (+ addendum) · ruled 2026-08-03

**Inputs:** `inbox/2026-07-31_from-PROME_design-bundle-…` (4 items) + `inbox/2026-07-31b_from-PROME_bundle-addendum-…` (1 count correction, 2 evidence upgrades, 1 live instance). Items 1-2 were *evaluate-and-propose*; 3-4 carried PROME recs. **PROME's own words: "No reply owed — your disposition doc is the ack." This is that doc**; a reply packet went out anyway because two items produced live findings PROME owns.

**Method note:** every premise was re-verified against the tree before ruling. Three of the four moved on verification — one to a much cheaper fix, one to a *stricter* answer than proposed, one confirmed at the corrected number. That is not diligence theatre: the bundle's own item 3 exists because a relayed count was wrong.

---

## Item 1 — Weekday-check mechanization → **DO NOT BUILD. IT ALREADY EXISTS. WIRE IT, SCOPED.**

**The ask** was to evaluate "a boot/closeout check that scans dated ledger rows + gate specs for weekday-name-plus-date pairs", estimated as "~10 lines added to an existing enforcer".

**`scripts/claim_check.py` has had a `weekday` check since 2026-07-27** (Will-directed, and its docstring already records n=3: WALTER's "Fri 2026-07-25", HEARTBEAT's "Mon 7/28", WALTER's mislabeled 6/20). **Verified by running it, not by reading it** — pointed at the CARL packet PROME cited, it prints:

```
“Sunday 8/3” — 2026-08-03 is a Monday, not Sunday
```

**So detection was never the gap. Invocation was.** `claim_check` is wired into exactly one place fleet-wide — `PROME/CLOSEOUT.md:178`. It appears in **no** agent's `CLAUDE.md`, `boot.py`, or closeout. CARL was never on it. This is the same shape as the memory-index orphans (9+ in one day with a working detector) and PAT-065's placement rule: **a control that exists in one agent's closeout is not a fleet control.**

### But it could not be wired as it stood — measured, not assumed

A genuine fleet-wide run was impossible and *said the opposite*: passing directories (`claim_check.py AGENTS PROME`) read the two **directory names** as files, failed silently, and printed **`✓ 2 file(s) clean`** — a whole-fleet pass claimed off zero bytes read. PAT-074 exactly. Once made to recurse: **271 flags across 6,197 files**, and most were false — the year heuristic borrowed *any* 4-digit number on the line, so `2006-07-23`, `2022-08-05`, `2025-07-31` appeared, and **correct text got flagged** (`BOND/STATUS.md:96` "Fri 7/31" → resolved to 2025 → "Thursday, not Fri", when 7/31 **is** a Friday in 2026).

**Two break-fixes shipped** (`scripts/` ownership, break-fix duty; both narrow, both regression-tested in each direction):

| Fix | Before | After |
|---|---|---|
| Directory arguments expand recursively | `✓ 2 file(s) clean` over 0 bytes | 6,197 files actually read |
| A year inside a complete ISO date no longer hijacks a bare M/D | CARL line 15 flagged the **correct** "Mon 8/3" as Tuesday, borrowing `2027-01-04`'s year | flag gone; the real "Sunday 8/3" retained |
| Year borrow bounded to ±30 chars (`YEAR_PROXIMITY`) | 271 fleet flags, mostly wrong-year | **131**, and `BOND:96`'s FP gone while `BOND:160`'s real error stays |

Regression: the case the original heuristic was *built* for — DOCKET's `Q2-2024 precedent = Tue 8/6`, correct in 2024 — still resolves to 2024 and stays clean (22 chars, inside the window). Deliberately reasoned prior behaviour preserved; I read the rationale before changing it.

### Ruling — scope by surface class, and the numbers pick the scope

| Scope | Files | Flags | Verdict |
|---|---:|---:|---|
| DOCKET / GATES / WILL_QUEUE / CATALYSTS / CALENDAR | 13 | **1** | ✅ **wire here** |
| + every live `STATUS.md` | 39 | 12 | ✅ wire (advisory) |
| Whole tree | 6,197 | 131 | ❌ **alert fatigue** — 21 of the top hits are `PROME/archive`, the rest mostly processed packets and KB rows where a historical mislabel is inert |

**Wire `claim_check --check weekday` at CLOSEOUT, scoped to the decision-bearing classes, not at boot** — the error is created at *write* time, so the closeout run catches it in the session that made it. PROME's instinct to start with DOCKET/CATALYSTS is right, and the flag counts are why.

### 🔴 It found a live one on its first scoped run — PROME's surface

`PROME/DOCKET.tsv:10` writes the same start gate **three times: "Mon 8/3" ×2 and "Mon 8/4" ×1.** 8/3 is a Monday; **8/4 is a Tuesday.** This is not a cosmetic typo — the row is a **PENDING** gate for **6 packets across 7 agents** (DEWEY/VULCAN/WATT/HENRY/ZHAO/SAM/BOND), and it disagrees with itself about which day the gate opens. The weekday name is merely what made it *detectable*; the defect is the date disagreement. **Routed to PROME.** This is a second live instance of the class PROME flagged, on the coordinator's own docket, found in 13 files.

---

## Item 2 — Intra-agent propagation self-sweep → **APPROVED IN PRINCIPLE. SPEC BELOW, BUILD ON WILL'S NOD.**

`consumer_check.py --agent X --old .. --new ..` already solves this shape **across** agents; the gap is **within** one. The change is genuinely small: `--agent` currently *excludes* `AGENTS/<NAME>/` from the scan, and `--self` **inverts that restriction** rather than adding new machinery.

**Not built today, deliberately.** A new *mode* is behaviour-changing, not break-fix, so it stays Will-visible per the `scripts/` grant. Spec, so it can be built in one pass:

1. `--self` restricts the scan to `AGENTS/<NAME>/` (invert the existing `own_dir` exclusion; keep `--old/--new/--from-ledger` semantics unchanged).
2. **Scope must include ledgers, trackers and handoff files — not just STATUS/THESIS.** PROME's addendum is decisive: MARCO's own `s020b` found 3 more carriers past the audit's list, one a KB ledger, and its SCRATCH + KB were exactly what a narrative sweep missed.
3. **Match on superseded TOKENS (figures, IDs), never on vintages, and grep by PATTERN never by line list.** The line-targeted failure mode is n=3 in one night (CARL's third consecutive line-targeted sweep left a hit on its highest-blast-radius surface *and* minted a new error mid-fix).
4. **This is the sharpest requirement and it is not in the original ask:** STUE's freshly-stamped, in-glob CASCADE/TIMELINE TSVs carry a retired prediction's twice-superseded confidence. **A staleness enforcer passes a fresh file carrying a stale claim** — so `--self` must not be gated on file age in any way. It is the *positive* check that `ledger_staleness` structurally cannot be (cf. `finding_freshness_check_cannot_catch_a_fresh_lie`).
5. Runs at closeout **whenever the session superseded one of its own published figures** — the same trigger as root step 1c, pointed inward.

---

## Item 3 — Bless CARL's `LEDGER_GLOB` as the parent-agent pattern → **BLESSED, at 44**

**Count verified myself before blessing, per PROME's own correction.** Measured on the tree today:

| | |
|---|---:|
| `sub_agents/*/workbook/*.tsv` | 43 |
| `sub_agents/*/workbook/*.md` | 1 |
| **Sub-agent files matched** | **44** |
| CARL's own `workbook/*.tsv` | 8 |
| **Total under CARL's declaration** | **52** |

**44 is right; 37 does not reconcile with anything measurable.** PROME was correct to refuse to let its own relayed number stand — the relayed 37 and STUE's processed 44 differed and no artifact reconciled them.

**Blessed as the required pattern for any parent agent, with two additions of mine:**
- **Declare `*.md` as well as `*.tsv`.** The default glob is `workbook/*.tsv`, so a markdown tracker is invisible. Exactly 1 of CARL's 44 is `.md` — a single file, and it is the one that proves the rule. **LIQUID is a live same-class instance** (`workbook/EXPECTED_SIGNALS_TRACKER.md`, no `LEDGER_GLOB` at all): verified today, and I have told PROME to send the interim one-liner rather than leave it unenforced while the pattern work finishes.
- **⚠️ A `LEDGER_GLOB` covers what it can *see*: `AGENTS/CARL/sub_agents/META/` has NO `workbook/` at all**, so it matches nothing and is outside enforcement even under the fixed glob — the same "enumerated but empty" signature as TERRY's `workbook/`. The declaration fixes *depth*; it does not fix *absence*. Named on the checklist row so a parent cannot mistake one for the other.

---

## Item 4 — Sub-agent receive-channel → **THE QUESTION IS CLOSED BY WILL. ADOPT *BOTH* HALVES, NOT EITHER/OR.**

Will ruled 8/02 that **all seven** sub-agents get inboxes (CARL builds). That supersedes options A-D. What remains is design: making sure the *next* sub-agent inherits the answer instead of re-deriving it.

**My ruling: Will's inboxes and PROME's option C are not alternatives — they solve different halves, and each is inert alone.**

- An inbox solves **delivery**: mail has somewhere to land.
- PROME's parent fan-down line (*"which sub-agents does this finding touch?"*) solves **addressing**: it is what causes anyone to send. **An inbox nobody sends to is exactly as dead as one nobody reads** — and the DEWEY/FHA case was an addressing failure, not a delivery one. The finding reached CARL; nobody asked who else it touched, so STUE's TRANSMISSION section stayed on credit cards (a channel the same packet had just demoted to ~2% of balances / ≤⅓ of the gap) while carrying `0` FHA mentions for a week. It surfaced because **Will asked a question**, not because a mechanism ran.

**So: keep the inboxes AND put the fan-down line in the parent's closeout.** Adopting only Will's half would leave the failure that actually happened unaddressed.

**STUE's own three mitigations are now the layer standard** — and they are STUE's, credited, because it argued *against* the option it then engineered for:
1. Scan on **both** boot paths, **including the spawned-mode card** — a scoped spawn is exactly where it gets skipped.
2. **Everything present is unprocessed by definition** (no read-marker, no other reader).
3. **Packet age >~30d is a finding about the SENDER**, not just a stale packet — it means someone has been acting on a false assumption about what the sub-agent knows, and telling them outranks actioning the packet.

**My addition — publish the cadence at the channel.** STUE boots ~5×/quarter. A low-cadence inbox that does not say so is a trap for senders, so the channel itself must carry its own cadence plus the escalation route (*"for anything time-critical send the parent as well, and say so in the packet"*). That is a property of the channel, not a disclaimer — and it is what makes the write-only→bidirectional change safe rather than merely complete.

**Same mitigation set applied to RAV's inbox today** (scaffolded this morning): charter §8 step 0 makes reading it a numbered step in the context RAV is handed, because RAV — like a spawn-gated sub-agent — has no boot that would otherwise reach it.

---

## Shipped from this disposition

| | |
|---|---|
| `scripts/claim_check.py` | 3 break-fixes (directory recursion · ISO-year exclusion · bounded year borrow), each regression-tested in both directions; 271→131 fleet flags with the real errors retained |
| `builds/REGISTRATION_CHECKLIST.md` **row 16** | Sub-agent layer: parent `LEDGER_GLOB` (incl. `*.md`, + the absence-vs-depth warning) · receive-channel with STUE's 3 mitigations · cadence published at the channel · parent fan-down line |
| Packets | PROME (reply + the live DOCKET:10 finding) |
| Deferred, named | `consumer_check --self` — spec above, build on Will's nod (behaviour-change, not break-fix) |

**Not in this bundle, still owed:** RAV-QC-20260801-002, the computed-staged-pathspec race review.
