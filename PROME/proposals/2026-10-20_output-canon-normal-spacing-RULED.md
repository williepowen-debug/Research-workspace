# RULED — root Output Canon: write normal spaced words

**Status:** RULED and INSERTED (2026-10-21); approved by Will 2026-10-20 22:41 ET (verbatim *"okay go ahead"*, answering PROME's question whether to add a normal-spacing rule to the root Output Canon). This is a root `CLAUDE.md` canon amendment, so it follows `PROME/CLAUDE.md` § "Canon drafts live in the ruling record":
1. Plan read (cold, on this record)
2. ONE edit to root CLAUDE.md
3. Result read
4. At most one further ❌-only edit

Renamed `…-RULED.md` at insertion. **INSERTED 2026-10-21 ~08:20 ET (session af287aee), ONE edit to root CLAUDE.md § Output Canon, text exactly as proposed below; `$` bytes verified by grep after the edit.**

## Defect
On 10/20, text written in Codex windows glued words and numbers together to save bytes:
- TERRY packet: "QQQOct20 720P sold1at6.66/net665.32"
- BRENT: "BRT31weekNON-QUALIFYING"
- REGINALD: "canonical10-column", "FROZEN10/10, last data9/11"
- Also WALTER and BOND packets

BRENT raised it in its own sweep (in BRENT's Codex window, relayed to PROME by Will; wording paraphrased: it saves little space and makes files harder to scan). Claude-runtime desks write normal spacing, so this is a runtime habit, not a desk rule. Fixing it desk by desk would not hold. The root canon is the one surface every runtime reads.

## Proposed text (one sentence, appended to the first paragraph of § Output Canon)
Current paragraph ends: *"…Agent-specific rules (STATUS line caps, domain caveats) stay local."*

Insert after it:

> **Write normal spaced words and numbers** ("BRT-31 week NON-QUALIFYING", "sold 1 at $6.66, net $665.32"); never glue words together to save bytes — byte budgets are met by moving history out, not by compressing what remains.

## Invariants (for the plan read)
- It changes no other Output Canon rule, number or authority. The read-cap budget is unchanged; the clause only says how NOT to meet it.
- It applies forward only. No mass rewrite of existing text is required or implied.
- It does not conflict with machine-read state tokens (`STATE_VOCABULARY.md`): tokens like `RESOLVED`, `GATE-BRENT-COT-35B`, `WQ-463` are identifiers, not glued prose.
- One sentence. It does not restate the dense-surface clause.

## Reads
- **Plan read — DONE 2026-10-21 ~08:19–08:20 ET** (corrected after ARGUS: an earlier '~08:18' was written from narrative) (coldreader, Sonnet, blind; ledger was in session scratchpad, findings recorded here): **0 ❌ · 4 ⚠️ · insertion point ✅** — verdict "insert as written".
- **Result read — DONE 2026-10-21 08:20 ET** (coldreader, Sonnet, blind): **0 ❌ · 3 ⚠️** — inserted bytes `cmp`-identical to the proposed text (227 B, both `$` figures present); one hunk, no CR bytes; no other rule changed meaning. Episode closed at two reads; no further edit.

## Declared residue (WQ-178 — ⚠️ not fixed; dated 2026-10-21)
1. **Local caps vs "moving history out":** a desk could read the clause as overriding a local STATUS line cap met by terseness. Reading: local caps stand (same paragraph, "stay local"); they are met by cutting content, never by gluing words.
2. **Registered token spellings:** the sentence itself does not say identifiers/state tokens keep their registered spelling (`STATE_VOCABULARY.md` e.g. `NOT-FIRED`); the invariant above says it. Candidate wording if a desk misreads: "(identifiers and state tokens keep their registered spelling)".
3. **Forward-only** is in the invariants, not the sentence; no mass rewrite is implied or owed.
4. **Dense surfaces** ("stay dense", Operator-surface clause) means tables and terse records, not glued words — the two clauses do not conflict.
Trivial: the invariants' `WQ-463` token example is illustrative (that row is in WILL_QUEUE as `463`, not the spelled form).
Result-read additions (⚠️, 2026-10-21):
5. The fill example ("sold 1 at $6.66, net $665.32") is a spacing example, not a price citation; root rule #4 is untouched.
6. Scope: the clause governs text; machine-read TSV cells and script output stay under `STRICT_TEXT.md` / `STATE_VOCABULARY.md` (see residue 2).
7. "Moving history out" names no new home; the existing retirement/rotation rules (Data Hygiene, read-cap canon) are the referent — no new duty.
