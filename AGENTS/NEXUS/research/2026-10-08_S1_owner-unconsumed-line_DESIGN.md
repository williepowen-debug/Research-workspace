# S1 — the owner-unconsumed line: DESIGN (a spec, not code)

**Owner:** NEXUS (design) · **Row:** DOCKET L639 (due at the 2026-10-13 L554 wake; delivered early 2026-10-08 20:32 ET) · **Basis:** DOCKET L304 graded YES 2026-10-08 14:54 ET under WQ-191's pre-registered re-open condition (`PROME/proposals/2026-09-07_wq163-183-190-191-RULED.md` § WQ-191) · **Ask packet:** `AGENTS/NEXUS/inbox/processed/2026-10-08_from-PROME_S1-reopened-design-the-owner-unconsumed-line-for-10-13.md` · **Veto to be re-argued at this artifact:** WALTER, `FORUM/2026-08-07_system-review/08_dissent/04_WALTER_retire-the-delivery-layer.md` § 5 · **Build:** PROME R1 process slot (WQ-299) after Will's word — a new instrument on PROME's boot path is ask-first. **No code ships with this file; the replay scripts that produced §6–§7 are scratchpad throwaways and are not the build.**

## 0. The whole story (≤150 words)

The line is one ADVISORY block in `prome_gate.py boot`, beside the WQ-221 aged-waits check: for every roster desk with an unconsumed inbox item **≥7 days old** while the desk has had **no self-commit for ≥7 days**, print the count, the oldest item's age, and — separately — whether any of those items is an **ACTION-typed** handoff, which is the WQ-206 trigger. Zero qualifying desks ⇒ nothing prints. Replayed from git, the line would have printed AEOLUS on 2026-09-05 and 09-06 (the WQ-206 trigger: one ACTION handoff 8–9 days old, desk dark 9–10 days) and DEWEY from 2026-09-17 on (13 items, oldest 55 days, desk dark 7 days). **Caveat that survives:** the DEWEY miss was entirely **peer packets with no ACTION line** — the line *shows* it; the WQ-206 rule as ruled (WALTER `action:` handoffs only) does **not** authorize a drain on it. Extending that authorization is Will's call, not this spec's.

## 1. What prints, exactly (STRICT_TEXT form; one line per qualifying desk, printed only on a hit)

```
UNCONSUMED [NEXUS S1, advisory] — perimeter: ROSTER active + Tier-2 + special (RETIRED/OFF-FLEET/TOOL-CLASS/ARCHIVE SOURCES skipped) · as-of <date> · rule: item age ≥7d AND desk dark ≥7d
🔴 <DESK>  <n> unconsumed · oldest <k>d (<file>) · dark <d>d (last self-commit <date> <sha>) · WQ-206: <m> ACTION item(s) ≥7d → L0 drain-only spawn authorized (WQ-206 rule 1; cap 4)
🟡 aged backlog, no ACTION-typed item (no WQ-206 authorization; a wait row ⇒ WQ-221; else Will's word): <DESK> <k>d (<n>) · <DESK> <k>d (<n>) · …
   searched <N> desks · <M> items · <skipped> scaffolding files skipped · <x> items excluded by a `due:` date ≥ today
```

- **🔴 tier** = the ruled trigger (WQ-206 rule 1: an unconsumed ACTION handoff ≥7d at a dark owner). One line per desk; the desk is named first (STRICT rule 2); the authorization is named on the line so the consumer does not look it up.
- **🟡 tier** = the FACT the DEWEY instance needed: aged backlog at a dark desk with no ACTION-typed item. One summary line, sorted by oldest age descending, never one line per desk (the §5c disease WALTER named: a long advisory is a skipped advisory).
- **Last line** = what was searched and what a null result means (STRICT rule 9). A clean boot prints the header + the search line and nothing else.
- Desks tagged DORMANT on ROSTER print in the 🟡 tier with the tag (`BARON [DORMANT] 57d`); they are never 🔴 (a dormant desk is woken by Will, not by WQ-206).

## 2. Definitions (each with its tie convention — SL-5)

| Term | Definition | Tie / edge |
|---|---|---|
| **Unconsumed item** | A **file** at the top level of `AGENTS/<DESK>/inbox/` or in a lane subdirectory (`WALTER/`, `WILL/`, `DEWEY/`…), excluding any `processed/` directory and the scaffolding set `walter_doctor._HANDOFF_SCAFFOLD` (`README.md`, `.gitkeep`, `.gitignore`, `.DS_Store`) plus `*MANIFEST*.md`. **Files only, lanes separate — never `ls \| wc`** (`inbox_census.py`'s own rule; the 9/4 doorbells counted the lane directory as an item). | A file with no parseable date (§ item date) is counted in `n`, never in `oldest`. |
| **Item date** | The clock in the FILENAME: `YYYY-MM-DD` prefix (peer packets) or `SIG-W-YYYYMMDD` (WALTER handoffs). Not mtime (git sync restamps it — root Data Hygiene). | WQ-206 as ruled ages WALTER items from `routed/delivery_log.tsv` `timestamp_routed`; the filename date is the same day except at a UTC midnight. For peer packets the filename is the only clock. The build may read `delivery_log` for lane items when present; the filename is the fallback and the spec's grading basis. |
| **Age** | `today − item date` in calendar days, ET. | **≥7 is aged** (inclusive — mirrors `prome_gate.aged_waits(min_days=7)`: `days < min_days ⇒ skip`). Age 6 is fresh. |
| **ACTION-typed** | Lane `WALTER/` file: frontmatter `action:` list names the desk (word-boundary match). Top-level packet: a line starting `**ACTION`, `ACTION:`, `## ACTION` or `## Requested action` in the first 4,000 B. Everything else = UNTYPED (an `info:` handoff, a reply, a receipt, a commission written without the ACTION form). | The top-level test is a recogniser over free text — the class that recurs. Measured 2026-10-08: 71 of 140 live top-level packets carry one of the four forms. A packet that asks for work without the form is UNTYPED and reaches only the 🟡 tier (CARL → DEWEY 2026-09-11 is the instance). |
| **Dark** | `spawn_list.Liveness.last_self_commit(desk)` — subject starts with the desk's name AND the touched paths are the desk's own (`attributed()`, DOCKET L455); fails closed to DARK on a git error. **Not** `decision_deck.days_dark`, which keys on the subject alone and would read DAEDALUS's 2026-08-28 commit into `AGENTS/AEOLUS/CLAUDE.md` as nothing (correct by luck) but reads any `DESK:`-prefixed PROME body line as a self-commit (the 9/11 defect its own docstring records). **One liveness definition for the line = the spawn driver's.** | **≥7 days dark is dark** (inclusive, = WQ-221). The age clock and the dark clock are independent (`finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly`): a desk can be dark 20d with a 2d-old item (fresh — not printed) or live today with a 60d-old item (not printed — the owner is awake; the item is the owner's to drain, surfaced by its own boot). |
| **Dated-deliverable exclusion** | An item carrying an explicit header field `due: YYYY-MM-DD` (first 15 lines; `due:` is the one name — STRICT rule 5) with a date ≥ today is NOT aged until that date (the WQ-221 exclusion, reused by field, not by prose). | ⛔ **Never "any future ISO date in the header."** Census 2026-10-08: 18 of 444 live `.md` items carry a future ISO date in their first 15 lines; at most 5 are the recipient's due date (CARL 10/15 deadline · DEWEY 10/15 · DEWEY 11/13 · WATT 10/9 · WATT comment-close 10/20); the rest are bond maturities (2049-02-15 at RED), an NFIP extension (2026-12-11 at MARCO), a window close (2026-11-14 at CRUISE), a MOFCOM date (2027-01-10). A prose-keyed exclusion would suppress ~13 of 18 wrongly. Legacy packets with no `due:` field are never excluded — the fail-loud direction (an advisory false positive is visible; a suppressed aged item is the gap L304 measured). An ISO-shaped string that is not a date (`3125-26-00`, VULCAN → VIOLET/WATT 10/1) must not parse. |
| **Perimeter** | Every desk with a `PROME/ROSTER.md` row in ACTIVE (all classes), TIER-2, SPECIAL, DORMANT (tagged). Skipped: RETIRED (YEYOU), OFF-FLEET, TOOL-CLASS, ARCHIVE SOURCES — their inboxes are not a consumption obligation; a packet addressed to a RETIRED desk is a misroute, printed once as `misrouted: <desk> <n>` on the search line. PROME's own inbox (`PROME/inbox/`, repo root) is included as a desk. | A directory under `AGENTS/` with no ROSTER row is NOT printed (ROSTER wins; the folder-existence pass is the TOOL-CLASS trap). |

## 3. The instrument — `PROME/tools/inbox_census.py` today, and what it does not expose

The census (WQ-178, 2026-09-04) returns, per desk, the top-level file list and per-lane file lists, `processed/` excluded. That is the **count** field and the **file-not-directory** discipline. It does **not** expose: ① item date / age (no filename parse); ② ACTION typing (never opens a file); ③ the scaffolding skip (counts `README.md` and `*MANIFEST*.md` — DEWEY's `WALTER/README.md` and `2026-07-02_BATCH-2_MANIFEST.md` were counted; the same README topped `walter_doctor`'s "oldest 57d" on 2026-08-23, rider R2); ④ liveness; ⑤ the `due:` field; ⑥ a machine-readable return (it prints). **The build adds a function (`census_line(desk, today)` → the fields of §1) beside `census()`, reusing its file walk and `spawn_list.Liveness` for ④; `prome_gate` imports the function. The CLI's existing output is unchanged.** No new ledger, no new state file: every field is recomputed from the tree and git at each boot.

## 4. Home — `prome_gate.py boot`, ADVISORY, beside aged-waits — tested against WALTER's §5

PROME's proposal is the right home, and here is the test, not the assertion:

| WALTER §5 objection | How this form answers it |
|---|---|
| *"S1 instruments the gap instead of removing it"* | The line instruments a **RULED rule's trigger** (WQ-206 rule 1: aged ACTION item + dark owner ⇒ L0 drain) that today has **no boot instrument** — `prome_gate` carries aged-waits (WQ-221) and the exempt-desk BOARD gap only; the aged-ACTION path fires on WALTER's census or a desk's doorbell (L304's mechanism finding). Removing the gap means the rule's trigger is observed where its consumer acts: PROME's boot, which drives the spawn (WQ-184). |
| *"makes the delivery layer self-justifying"* | The line reads **inbox files and git self-commits**. It opens no `delivery_log.tsv`, no `board_log.tsv`, no doorbell ledger. Of 455 live inbox files on 2026-10-08 (444 `.md` items), **148 are top-level peer packets** and 307 are lane files (301 WALTER handoffs; 6 in `WILL/` / `DEWEY/` lanes): if WALTER's delivery layer were retired tomorrow the lane third disappears and the line keeps measuring the peer-packet surface — the DEWEY instance was entirely peer packets. The line's value does not rest on the layer it would then measure less of. |
| *"TERRY's revert falsifier fires only if S1 names TERRY"* | The line names TERRY only when TERRY has an aged item while dark — the same rule as every desk; it carries no TERRY-specific logic and references no T-2 class. Whether the §3.5.5 revert falsifier can be graded off a uniform line is WALTER's argument to re-make at this artifact; the spec neither presupposes nor forecloses it. TERRY on 2026-10-08: 4 items, oldest 0d, dark 0d — not printed. |
| *"a fifth advisory line agents learn to skip"* (P1's own risk) | Print-on-hit only; one 🔴 line per triggered desk; the 🟡 tier is ONE line however many desks. Expected volume measured in §7: 5 🔴 + 1 🟡 today. WALTER's own P1 tightening rule is adopted verbatim: **if the 🔴 tier routinely prints ten, the scope is wrong and is tightened, not tolerated.** |

**Homes rejected, with the reason:** a `SessionStart` hook at every desk (P1's original home — runs on whoever boots, but the consumer that can act is PROME's spawn driver, and a desk reading its own inbox at its own boot is the existing owner duty); a `spawn_list.py` class change (ruled out by L639 — cadence and classes stay as WQ-184 ruled; the line informs PROME, who registers a DOCKET row, which the driver spawns — one wake mechanism, WQ-221 rule 3); `walter_doctor` (WALTER's launch cadence, the gap P1 named — and `delivered_but_unconsumed` there is lane-only and type-blind: it keeps running as WALTER's own instrument; nothing here retires it, that is WALTER's call).

## 5. Acceptance cases (WQ-229: written before any code; the build reports IMPLEMENTED / TESTED / INDEPENDENTLY VERIFIED / STILL UNRESOLVED, never merged)

| # | Case | Expected | Replay evidence (git tree at the date's last commit; `spawn_list.Liveness(until=…)`) |
|---|---|---|---|
| A1 | **AEOLUS, boot of 2026-09-06** (L304 instance ②) | 🔴 line: WQ-206 ≥1 | AEOLUS: 6 items, oldest 9d, last self-commit 2026-08-27 `b6281d60e` ⇒ dark 10d; `SIG-W-20260828-036` ACTION 9d ⇒ **WQ-206: 1** (and already on 09-05: 8d/9d). On 09-08: 2 ACTION items (036 11d, 011 7d). **Surfaces.** |
| A2 | **DEWEY, boot of 2026-09-18** (L304 instance ①) | 🟡 line names DEWEY with its age | DEWEY: 13 items, oldest 56d (`2026-07-24_from-PROME_gate079…`), last self-commit 2026-09-10 `c8413bc65` ⇒ dark 8d. **ACTION-typed items: 0** — CARL's 9/11 request (`**Ask:**`), the 8/15 commission, PROME's 9/10–9/14 packets all lack the ACTION form. ⇒ **🟡 `DEWEY 56d (13)`**, no 🔴, no WQ-206 authorization. Prints identically 09-17 (dark 7d — the first qualifying day) through 09-22 (60d/14). On 09-24 after the drain: 1 scaffolding file, nothing printed. **Surfaces — in the FACT tier only.** |
| A3 | A fresh ACTION item (<7d) at a dark desk | not counted | AEOLUS 09-05: `SIG-W-20260901-011` ACTION 4d ⇒ not aged; the desk still prints on 036. DEWEY 09-18: PROME's 9/14 HALT packet 4d ⇒ not aged. |
| A4 | A dated deliverable before its date | excluded only via `due:` | `2026-10-01_from-HANS_rerun-DR4-for-HNS-07.md` at DEWEY reads *"due before 2026-10-15"* in prose, no `due:` field ⇒ counted (aged from 10/8). With `due: 2026-10-15` ⇒ excluded through 10/14, counted from 10/15. CARL-DR-5 (8/15, *"target ~8/29"* in prose) ⇒ counted at 7d on 8/22 under this spec; a `due:` field would have held it to 8/30. |
| A5 | A future date in the header that is NOT a due date | NOT excluded | `2026-10-08_from-BOND_F2…` at RED (maturities 2049-02-15…) · `2026-09-28_from-CORAL…` at MARCO (NFIP to 2026-12-11) · `2026-09-12_from-OTTO…` at DEWEY (a termination extended to 2026-09-18) — all counted. |
| A6 | An ISO-shaped non-date | must not parse | `3125-26-00` (VULCAN → VIOLET and WATT, 10/1): month 26 ⇒ not a date ⇒ no exclusion. |
| A7 | Ties | inclusive both clocks | age exactly 7 ⇒ aged (DEWEY 09-18: four 9/11 packets at 7d counted); dark exactly 7 ⇒ dark (DEWEY 09-17: 7d ⇒ prints). |
| A8 | n = 0 · n = 1 | nothing · prints if aged+dark | NEXUS 10/8: 0 items ⇒ no line. BOND 10/8: 1 lane item 0d ⇒ not printed. BARON 10/8: 1 item 57d, dark 238d ⇒ 🟡 `BARON [DORMANT] 57d (1)`. |
| A9 | A desk live today with an old item | not printed | CORAL 10/8: 21 items, oldest 7d, dark 0d ⇒ not printed (the owner is awake; its own boot owes the drain). HANS: 29/7d/0d ⇒ same. |
| A10 | Scaffolding | skipped, counted on the search line | DEWEY `WALTER/README.md` (no date) and `2026-07-02_BATCH-2_MANIFEST.md` (77d) ⇒ skipped, never `oldest`. |
| A11 | RETIRED desk with items | skipped, `misrouted:` note | YEYOU 10/8: 4 items 57d, dark 49d ⇒ not a line; `misrouted: YEYOU 4` on the search line. |
| A12 | git failure | fails closed to DARK, visibly | `Liveness` returns `!ERR` ⇒ the desk is treated as dark and the line carries `dark ?? (git error)`; never silently "live". |

## 6. Today's would-be output (2026-10-08, replay definitions; NOT the build's output)

```
UNCONSUMED [NEXUS S1, advisory] — perimeter ROSTER (RETIRED/OFF-FLEET/TOOL-CLASS skipped) · as-of 2026-10-08 · item ≥7d AND dark ≥7d
🔴 HAWK    65 unconsumed · oldest 10d · dark 10d · WQ-206: 2 ACTION ≥7d → L0 drain-only authorized
🔴 MARCO   14 unconsumed · oldest 21d · dark 14d · WQ-206: 1
🔴 ORACLE   7 unconsumed · oldest 10d · dark 10d · WQ-206: 1
🔴 RAV      5 unconsumed · oldest 65d · dark 64d · WQ-206: 2   [SPECIAL — Will-driven; the authorization line is PROME's to apply or not]
🔴 SHADE   17 unconsumed · oldest  7d · dark  7d · WQ-206: 1
🟡 aged backlog, no ACTION-typed item: BARON [DORMANT] 57d (1) · WATT 10d (24) · WAL 10d (6) · VIOLET 9d (18) · CREED 7d (13) · DEWEY 7d (4) · FLG 7d (6) · SAM 7d (24) · ZHAO 7d (12)
   searched 42 inboxes (41 under AGENTS/ + PROME/inbox/) · 455 files (148 top-level · 307 lane; 444 `.md` items) · ACTION-typed 143 · scaffolding skipped · misrouted: YEYOU 4 (RETIRED)
```

Caveats on the numbers: the ACTION typing of top-level packets is the four-form recogniser of §2; `dark` is `spawn_list.Liveness` as of 20:4x ET; HAWK's 65 includes 60 lane handoffs at a desk NEXUS reads only on cross-war questions — the count is a fact about the inbox, not a judgment about the desk. **Volume: 5 🔴 lines + 1 🟡 line tonight.** WALTER's P1 expected 0–5 lines/day on a narrower scope (role=action AND four signal types AND >72h); this scope prints at that ceiling on its first day. The tightening rule (§4, last row) is live from day one.

## 7. Findings that must reach Will beside the design (the caveats that survive simplification)

1. **WQ-206 would not have authorized the DEWEY drain.** The rule as ruled (2026-09-10) is *"an unconsumed `action:` handoff older than 7 days at a DARK owner … age from WALTER `routed/delivery_log.tsv`; the set is WALTER `registry/DOORBELL_LOG.tsv`; ACTION-line only."* DEWEY's items were peer packets with no ACTION line; the 9/24 drain came on CARL's doorbell to a live PROME. This line surfaces that class as a FACT (🟡); acting on it under a standing rule needs either a WQ-221 wait row (there was none — CARL's docket row was CARL's) or an extension of WQ-206 to peer packets carrying an ACTION line ≥7d at a dark owner. **That extension is a separate ask-first item; the spec does not assume it.**
2. **Two liveness definitions live in PROME's own tools** — `decision_deck.days_dark` (subject-only) and `spawn_list.Liveness.last_self_commit` (subject + path-attributed, fail-closed). The WQ-221 check uses the former; this line must use the latter. The disagreement is a PROME defect to name, not this spec's to fix; the build should not add a third.
3. **`due:` is a next-write convention.** Legacy packets are never excluded; the first weeks over-print dated commissions at dark desks by design (A4). Whether to add `due:` to the packet template is DAEDALUS/STRICT_TEXT territory — one line in the template, no retrofit.
4. **Not measured and not claimed:** that PROME would have ACTED on a 🟡 `DEWEY 56d (13)` line on 9/18. The line makes the fact visible at the consumer; the consequent is PROME's boot discipline, which L304 shows booted seven mornings without the fact in front of it.

## 8. Who holds what

- **Will:** the build (R1 slot; a new instrument on PROME's boot path) · finding 1's extension, if wanted · nothing else is decided here.
- **WALTER:** re-argue §5 at this artifact, for or against the boot-check form (packet copy in `AGENTS/WALTER/inbox/`); say whether `delivered_but_unconsumed` is retired, kept or re-scoped — WALTER's instrument, WALTER's call.
- **PROME:** consume; register the design DELIVERED at L639 (early); carry findings 1–3 to the queue in PROME's words; build only on Will's word.
- **NEXUS:** nothing further unless asked; the replay scripts are scratchpad and are not kept.

## 9. Residue (declared)

- The four-form ACTION recogniser is the weak leg (STRICT_TEXT's own class). A header `ACTION:` line is already the packet template's form; packets outside it are UNTYPED by construction. No retrofit proposed.
- Lane items' age uses the filename date; `delivery_log` `timestamp_routed` differs by ≤1 day at a UTC midnight. The build may prefer the log for lane items; the spec's acceptance cases grade on the filename.
- The 🟡 tier's one-line form hides the per-desk file list; the consumer runs `inbox_census.py <DESK>` for the names — one command, already built.
