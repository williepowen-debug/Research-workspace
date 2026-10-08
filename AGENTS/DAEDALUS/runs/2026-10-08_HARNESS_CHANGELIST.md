# Harness Audit — the one batched changelist (for Will's approval)

**Written:** 2026-10-08 16:50 EDT (from `date`) · DAEDALUS. Merges `runs/2026-10-08_HARNESS_CHANGELIST_A.md` (PROME, root canon, DAEDALUS/RAV, closeouts, WALTER, nested; 74 lines) and `_B.md` (36 domain charters; 46 lines). **119 unique lines** (B38 = A's D01+D02, counted once). Source evidence: the 10/04 audit (60/60 primary files read, `runs/2026-10-04_HARNESS_AUDIT_FINAL.md`), re-tested tonight at HEAD by two fresh Opus readers, because the fleet moved from Fable 5.1 (the 10/04 run) to Opus 5.5 and the playbook re-opens every keep/strike call on a model change.

**What the re-test changed:** 12 of the 10/04 items are already fixed at HEAD and dropped (list A §2). None was struck because of the model change alone; it only strengthens the case for removing duplicates, history and restated rules. **No git, safety, authority or position rule is weakened anywhere in this list.** Those are KEEP or are put to you below.

**Authority:** harness edits are approval-gated (playbook). Your approval authorises DAEDALUS to send each owner its lines; a live desk applies its own, and DAEDALUS edits only idle desks it has express scope for. Nothing has been edited.

## Tier 1 — git and safety (approve these first)
| Line | Desk | Problem | Proposed |
|---|---|---|---|
| D01 + D02 (= B38) | TERRY `CLOSEOUT.md:99, :105–117` | Recovery recipe ends in `git restore --source=HEAD --staged --worktree -- <dir>` on another agent's directory; reproduced wiping uncommitted work. Line 99 calls a delivered push "not landed", which sends TERRY into that recipe. PROME's 10/04 hold was filed 10/07 with no correction; DAEDALUS re-sent it tonight. | Strike the B2/post-realign/desync bullets → "Non-ff → root Git Protocol session-end step 3 in full". Receipt = safe-push's `Pushed. CONFIRMED:` line. |
| A17 | RAV charter (`builds/RAV_CHARTER.md:178, :185`) | Commits across directories on Codex with "1. Pull." and no pre-pull stop, no-amend or push guidance | Point both steps at root Git Protocol, read whole |
| C10 + E03 | PROME `tools/spine_audit.workflow.js:92` · WALTER `design/BOOT_PROTOCOL.md:152` | Tell readers to escalate on a bare non-ff recurrence; root `CLAUDE.md:99` says that is ordinary traffic | Cite root step 3 instead |
| B06 | OSPREY `CLAUDE.md:79` | "packets you deliver … stay untracked": contradicts root carve-out ① (the author must commit). **The line came from DAEDALUS's own 7/12 build template** (OTTO's copy was corrected earlier). | "Self-authored packets you deliver are yours to commit (root carve-out ①)" |
| B10 (DEFER) | OZK `CLAUDE.md:90` | Non-ff rationale is obsolete, but "escalate, don't self-recover" is stricter than root and safe | OZK + PROME: keep the behaviour, fix the reason |

## Tier 2 — instructions that contradict canon (owner applies; your OK covers the batch)
| Line | Desk | Problem | Proposed |
|---|---|---|---|
| B01 + B04 | HANS, AEOLUS, CORAL, FERT, FLG | Tell the desk to send threshold signals straight to the target's inbox; root: "never route signals around WALTER" | Route via WALTER, unless each owner confirms an approved exception |
| B21 | TERRY `CLAUDE.md:57–104` | Inline trade-card format lacks the canonical template's sizing and missing-input fields | Point at `TRADE_CARD_TEMPLATE.md`; the Will-approval line stays verbatim; TERRY must agree |
| B14 | BROCK `CLAUDE.md:62` | Self-check runs before the writes it is meant to check | Run it after 7a/7b |
| B24 (DEFER) | ZHAO `CLAUDE.md:37` vs NEXUS schema `:162–165` | ZHAO forbids the STATUS hash the schema requires | NEXUS's ruling, already asked tonight (brief-pin packet) |

## Tier 3 — your rulings (authority text in root canon; DAEDALUS cannot decide these)
| Line | Question |
|---|---|
| A-B01 | Move the Gate C custody procedure from root `CLAUDE.md:82–84` to the KERNEL runbook, keeping only the authority sentences in root? (Every activation window has expired.) |
| A-B03 | Add one discoverability clause to root's Scope note naming DAEDALUS's 7/31 `scripts/` grant (today it lives only in DAEDALUS's charter)? |
| D12 | LIQUID, TERRY and HANS closeouts say "Light: commit optional"; root session-end says commit. Which governs? |

## Tier 4 — bulk tidy (duplicates, restated canon, history in active steps) — one word approves all
**92 lines: 7 STRIKE + 85 REWRITE** (counted from the two tables: 120 rows parsed = 94 REWRITE · 15 DEFER · 8 STRIKE · 3 KEEP, less the 28 named in tiers 1–3 and owner-only). Patterns: a restated git recovery recipe on 9 desks · "Reply via outbox" on 5 · retirement rules on 4 · generic Output-Canon style blocks on 3+ (CRUISE, BOND, LIQUID; also OZK/WAL, unswept) · history and incident stories inside active steps (PROME CLOSEOUT, WALTER, DAEDALUS's own charter: 15 lines on DAEDALUS/RAV) · stale figures (WALTER `CLAUDE.md:80` "6 of 14" HANS thresholds; HANS now has 17). Every line, with file:line, current text and replacement: lists A §1 and B §1.

## Owner-only items (not for Will; routed with the batch)
A06/A09 (DAEDALUS's own charter) · C19 (PROME/Will governance, optional) · D03 (TERRY: which exit-1 reading governs) · E09 (WALTER: which spans move) · F05 (CARL/STUE live-value mirror) · B44–B46 (ZHAO, OSPREY domain method).

## Limits
Replacement texts are wording directions, verified by each owner before applying. Clauses added after 10/04 were not audited (WALTER's four commits today, PROME's 10/05 runtime text). The model-change re-test was done by reasoning, not by experiment. **The sweep closes when this batch is ruled and applied, not tonight:** `last_run` stays July 7 until then.
