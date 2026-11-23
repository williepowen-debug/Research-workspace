# Boot runner: literal first commands for the manual reads (WQ-729 item 1, Will 2026-11-23 12:17 ET, approved as restated)

**Owner:** PROME prome-77. **File changed:** `PROME/.claude/skills/boot/SKILL.md` and its identical root copy `.claude/skills/boot/SKILL.md` (the parity gate requires both). **No launcher change. No manual change:** the rule already stands in `PROME/BOOT.md` § Bounded reads ("every mandatory document read in steps 1–5 uses `python3 PROME/tools/boot_read.py <path>` from repo root, one page per tool output and one document per call ... Any read not completed to `eof: true` is SKIPPED at step 8"). The runner owns sequence and commands (`PROME/CLAUDE.md` Boot Sequence step 2, Layering), and today it names the reader only in prose.

## The defect, from the record
Boots read PARTIAL because PROME's first reads of the boot manual, its modules, the NOW page or USER.md went through the plain reader: 11/16 evening, 11/17 14:38 ET and 21:29 ET, 11/22 (PROME's own reads after `/clear` or at a pickup); 11/17 08:30 ET (launcher-started; the launcher's start text orders a plain read of USER.md). The runner says "through the bounded reader" and gives no command at the point where the first read happens, so the first act is a choice.

## Proposed text (two insertions; nothing deleted)

**Insertion A**, a new paragraph directly after the "**Mode selection:**" paragraph:

> **First commands, literal (WQ-729, Will 2026-11-23). Run these before anything else, one document per call, each continued with `--offset <next_offset> --sha256 <sha256>` until `eof: true`:**
> `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py PROME/BOOT.md`
> `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py USER.md`
> On "pick up PROME" also: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py PROME/BOOT_MODULES.md` and `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py PROME/SCRATCH.md`.
> A read of any of these with the plain file reader does not count, whoever ordered it: when a launcher's start text or an earlier step already had USER.md read plainly, read it again here with the command above. The rule is `PROME/BOOT.md` § Bounded reads; this paragraph only supplies its commands.

**Insertion B**, appended to item 1 of the index (after "Will's directed task, if any."):

> The first two reads are the literal commands in "First commands" above.

## Invariants
1. No rule is added, removed or changed: BOOT.md already requires the bounded reader for every mandatory read and already scores an incomplete read SKIPPED.
2. A complete plain read still does NOT count (no relaxation): counting it would be a rule change, which Will did not approve.
3. Root and local copies are byte-identical after the edit.
4. The commands are copied from BOOT.md's form, including the repo-root `cd`.
5. The full boot and the pickup branch both stay as they are in every other respect.

## What can still make a boot PARTIAL after this
A mandatory read not taken to `eof: true`; the five every-boot memory hooks or the macro-principals check not run; a gate line with an owed action left without a disposition; the regime memo not re-based after a regime-level change; an overdue spine audit not run; a needed tool unavailable.

## Reads
reads: 2 of 2; first figure written at the plan read (2026-11-23 12:52 ET). **Plan read (Sonnet coldreader, about 12:51 ET): 4 blocking, 4 warnings.** The commands run. The proposed wording did NOT survive: (1) "a plain read does not count, whoever ordered it" is not in BOOT.md, so the runner would have carried a rule the manual lacks; (2) "run these before anything else" and the forced re-read contradicted `BOOT_MODULES.md` § Repeat boot (reuse of acknowledged reads) and pre-empted step 0; (3) the pickup list omitted CLOSEOUT.md § Restart checkpoint and the daily note and was framed as complete; (4) invariants 1, 2 and 5 were therefore false as written.

## Text as APPLIED (replaces "Proposed text" above; the proposal above is kept as the record of what was read)
**Runner, both copies, ONE paragraph inserted after "Mode selection" (insertion B dropped):**

> **Commands for the mandatory reads (WQ-729, Will 2026-11-23).** When a mandatory read is due (`PROME/BOOT.md` § Bounded reads), its command is `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py <path>`, continued with `--offset <next_offset> --sha256 <sha256>` until `eof: true`, one document per call. On a full boot the first two are `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py PROME/BOOT.md` and `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_read.py USER.md`. On “pick up PROME” the reads are those of `PROME/BOOT_MODULES.md` § Resume after a restart step 1 (BOOT.md, CLOSEOUT.md § Restart checkpoint, SCRATCH, the daily note it names), each by the same command form, and that section is opened the same way. Repeat boot: `PROME/BOOT_MODULES.md` § Repeat boot decides whether an earlier read may be reused and adds its own flags; nothing here overrides it. This paragraph supplies commands only; the rule is BOOT.md § Bounded reads.

**Manual, `PROME/BOOT.md` § Bounded reads, ONE sentence appended** (the rule's home, so the runner carries no rule of its own):

> A mandatory document already read with the plain file reader in this context (a launcher's start text orders such a read of `USER.md`) is read again through the bounded reader; the plain read does not satisfy this paragraph (Will 2026-11-23, WQ-729 item 1).

⚠️ This sentence states in the manual what Will approved on 11/23 ("re-reads USER.md through the bounded reader even when the launcher's plain read came first") and what he called the existing rule ("Counting a complete plain read as acceptable would be a change to a rule"). The plan reader's point stands that BOOT.md did not say it in words before today. Told to Will in chat the same hour.

**Invariants as they now read:** (1) the only rule text added is the one BOOT.md sentence, on Will's word; (2) a complete plain read still does not count; (3) the two runner copies are byte-identical; (4) commands use the runner's existing repo-root `cd` form; (5) step 0, the pickup branch's own read list and Repeat-boot reuse are untouched.

## Declared residue (plan read's warnings, not fixed)
- The runner's header says its commands are "copied from BOOT.md verbatim, including the repo-root `cd`"; BOOT.md § Bounded reads shows the command without the `cd` (pre-existing wording).
- The new paragraph repeats, with commands, what the runner's item 1 says in prose.
- SCRATCH is named for the pickup only; the full boot also reads it whole at BOOT.md step 2 (the paragraph says "the first two", not "the only two").

## Result read (Sonnet coldreader, bounded, with the execution check; recorded 2026-11-23 12:54 ET)
**0 blocking, 4 warnings. Execution check PASS:** both literal commands returned JSON from `PROME/`; one was continued once with `--offset` and `--sha256` and returned JSON; the two runner copies are byte-identical. The runner paragraph states no rule the manual lacks; the BOOT.md sentence does not contradict Repeat boot (a plain read is never an acknowledged read) and does not require re-reading injected charters. No edit was made after this read.

**Declared residue (not fixed):**
- The pickup reads are named without repo-relative paths (they are `PROME/CLOSEOUT.md`, `PROME/SCRATCH.md`, `memory/YYYY-MM-DD.md`, `PROME/BOOT_MODULES.md`).
- "Mandatory document" in BOOT.md § Bounded reads is tied to steps 1 to 5, while USER.md and the charters sit in the Context-loading paragraph above the steps; on a runtime without injection a reader could wonder whether a plain read of root `CLAUDE.md` must be repeated.
- On a retained-context repeat boot, "on a full boot the first two are…" read literally re-reads BOOT.md and USER.md before the Repeat-boot sentence that follows it; a cost in tokens, not correctness.
- "That section is opened the same way" (BOOT_MODULES.md through the bounded reader) is stated only in the runner.
- BOOT.md's header "Updated" line was not bumped for this sentence (no edit after the read); `git log -p -- PROME/BOOT.md` carries it.

**State:** IMPLEMENTED · TESTED (execution check by an independent reader) · residue declared.
