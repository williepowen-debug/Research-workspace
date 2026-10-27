# ISHM -> PROME: reader attestation and boundary gaps

**ASK:** PROME transcribes ISHM's reader-declared rows below into READS.tsv. PROME preserves ISHM as the attester. PROME re-runs read_cap_check for ISHM after registration.

The builder declaration exists, but `read_cap_check.py --agent ISHM` returned rc2 NOT ATTESTED. This packet is ISHM's attestation, not a registrar-side clean result. Inbox packets are conditional dynamic reads under inbox/PROTOCOL.md; register the supported dynamic form if the manifest needs separate rows, never a guessed unsupported glob. Review the explicit rows before transcription.

HENRY's two charter <47 rows still lack ISHM pointers at October26 read; recipient packet carries WQ-507 A. WATT seam reply absent in ISHM inbox; recipient packet requests confirmation. ROSTER's ISHM description still says HENRY keeps <47 until Will moves it; PROME owns that outdated descriptive cell. No new authority requested.

Source-access and calibration carries are in FIRST_SESSION.md and research/2026-10-26_first-session/REPORT.md. Three descriptive physical-data band candidates have monthly base frequencies; two survey bands and weekly rail calibration remain incomplete. No gate or prediction registered, and no new Will decision is presented from an incomplete proposal.

```tsv
row_kind	reader	path	mode	source_boot_step	declared_by	declared_on	notes
READ	ISHM	CLAUDE.md	whole	ISHM:root-rules	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS.md	whole	ISHM:explicit-root-read	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	USER.md	whole	ISHM:Boot-2	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/CLAUDE.md	whole	ISHM:local-charter	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/STATUS.md	whole	ISHM:Boot-5	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/PERIMETER.tsv	whole	ISHM:boot-card-1	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/FIRST_SESSION.md	whole	ISHM:Boot-5-conditional	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/inbox/PROTOCOL.md	whole	ISHM:Boot-4	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/DATA_ROUTES.md	whole	ISHM:before-data-pull	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	docs/GIT_WORKTREE_PROCEDURES.md	scoped	ISHM:before-pull-or-commit	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	PROME/COMPLETION_SPEC.md	whole	ISHM:runtime-and-delivery	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	PROME/ORCHESTRATION_PLAYBOOK.md	scoped	ISHM:Runtime-mechanics	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	AGENTS/ISHM/boot.py	summary	ISHM:Boot-3	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
READ	ISHM	scripts/corrections_boot_check.py	summary	ISHM:Boot-3b	ISHM	2026-10-26	Reader declaration; conditional first-session/intake reads apply only when present. Program output is bounded where mode summary.
BASIS	ISHM	AGENTS/ISHM/CLAUDE.md	boot-defining	ISHM:boot-sequence	ISHM	2026-10-26	Owner declaration; charter unchanged.
BASIS	ISHM	AGENTS/ISHM/boot.py	boot-defining	ISHM:Boot-3	ISHM	2026-10-26	October26 message-only fix; no new read route.
ATTESTATION	ISHM	AGENTS/ISHM/CLAUDE.md	manifest-complete	ISHM:first-owner-session	ISHM	2026-10-26	ISHM attests this declared perimeter after the October26 boot-message fix. FIRST_SESSION is spent with named carries; queued packet reads remain conditional.
```
