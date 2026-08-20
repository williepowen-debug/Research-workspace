# YEYOU — MEMORY

Durable cross-session memory: false-positive rules, per-agent quirks, recurring patterns. **Not** a session recap (that's `STATUS.md`).

---

## False-positive rules (NEVER re-flag these)

*Populate as Will/PROME mark findings WONTFIX. Seeded with quirks already known from the fleet:*

- **DEWEY is stateless by design.** Its `CLAUDE.md` says it keeps **only** `output/INDEX.tsv` — no `STATUS`, `SCRATCH`, `NEXUS_BRIEF`, `thesis/`, predictions, or catalyst docket. Do **not** flag DEWEY for "missing continuity files."
- **RED's STATUS cap is 200 lines**, not 250. RED uses `SCRATCH.md` as its canonical handoff; `LAST_COMPLETION.md` and `archive/handoffs/` are **retired/frozen** — don't flag their absence or staleness.
- **`NEXUS_BRIEF.md` is required for newer agents (CORAL, RED-wave), not all.** Older agents (e.g. REGINALD) don't maintain one — don't flag REGINALD for "missing NEXUS_BRIEF."

## Per-agent quirks

- **Hardening-wave drift is expected, not an error.** Newer agents use `board_log.tsv` for WALTER consumption + symmetric boot/write-back; older agents (REGINALD) use the BOARD diff-scan + outbox model. Both are valid — do **not** flag one agent for "not matching" another's protocol. Only flag an agent against **its own** `CLAUDE.md`.
- **PROME has two homes** (`PROME/` and `AGENTS/PROME/`) and is the one agent allowed to commit to both — don't flag PROME cross-dir commits spanning those two paths.

## False-positive rules (added 2026-08-20, first pass)

- **Multi-inbox commits by a packet AUTHOR are NOT `git add -A` signatures.** Root carve-out ① (2026-07-23) *mandates* that an agent commit its self-authored packets into recipients' inboxes — WALTER signal dispatches legitimately touch 6-8 agent dirs + BOARD in one commit. Checklist §F predates this (YEY-012). Test: are all foreign paths `inbox/` files authored by the committing agent + own-dir/BOARD bookkeeping? Then legitimate. Reserve 🔴 for non-packet edits to files another agent OWNS.
- **PROME editing its OWN ruling packets inside recipients' inboxes is legitimate** (seen `f67c6c73d`: timestamp corrections to 4 self-authored packets in HAWK/OSPREY/TERRY inboxes). Authorship, not location, decides.
- **`memory/auto/` commits by any agent are carve-out ③** — never a cross-dir flag.
- **HAWK's thesis/CHANGELOG.md is 🧊 FROZEN historical** (pre-FALCON-split content, per HAWK's own FILES table) — do NOT flag HAWK FALSIFICATION/PREDICTIONS edits for "no CHANGELOG entry"; the checklist-A rule names REGINALD/CORAL/RED, not HAWK.
- **BOND annotates non-thesis THESIS.md edits in-line** ("mirror-hygiene fix, not a thesis change, no version bump") — read the edit's own provenance note before flagging a missing version bump.
- **HAWK STATUS "≤120" is a TARGET, not a cap** (its own word) — over-target = 🟡, not 🟠.
- **CREED's STATUS regime is soft-300/split-trigger-320** with a self-documented standing exception — don't flag ≤320.
- **WALTER STATUS cap is a BYTE budget (48,000 B)**, not the 250-line default — measure with `wc -c`.
- **TERRY has NO STATUS cap in its charter** (509 lines as of 8/20, flagged YEY-004 against the fleet default) — if Will/DAEDALUS bless TERRY's long-STATUS form, convert YEY-004 to WONTFIX and add the quirk here.

## Per-agent quirks (added 2026-08-20)

- **HAWK `workbook/KB.tsv` carries 10 legacy ragged rows** (KB-HAWK-040/041/042/050/051/085/088 = 12 fields; 091/092/093 = 14 fields; all Feb–Mar 2026, pre-watermark). Not introduced by any reviewed push — do not re-flag; it's DAEDALUS-sweep territory. In-range additions were clean 13-field.
- **SAM's STATUS deliberately leads with Signal Status, no Updated header** (flagged once, YEY-007) — if WONTFIX'd, record here and stop.
- **Inbound-only queue entries are normal:** an agent appears in boot.py's queue whenever ANY commit touches its dir — for dormant desks that's other agents' packets. Review the COMMITS (author-side hygiene), record PASS-inbound-only, and check the inbox backlog (checklist G) — that's the real signal on a dormant desk.

## Recurring patterns

- **2026-08-20 (n=4): dormant-desk inbox accrual** — HENRY 71 / LIQUID 59 / MARCO 36 / RED 27 unprocessed, each with 20+ items pre-8/17; LIQUID's pile includes a Will-ruled ACTION packet with review_by dates. The senders' side is working (carve-out ① compliant); the consume side has no session. This is a PROME routing/spawn-priority question, not a per-agent nit — surfaced in the 8/20 digest.
- **2026-08-20 (n=2, PROME): TSV row rewrite drops a trailing column** — both DOCKET edits that rewrote a Status cell lost the artifact-pointer field (YEY-001). Watch any hand-edit of a wide TSV row; suggest awk NF check habit at the rail owner.
