# C7 STAGED SUBMISSIONS — NOT SUBMITTED, NOT LIVE COMMANDS

These two files are byte-frozen SAM-33 command candidates generated 2026-08-27
(`prepare_pilot.py`, disposable mirror, `submitted_at=2026-08-27T15:54:43.715467Z`,
source commit `1d9400425f7415083a9ffbd10964670bf255abf2`).

**A command exists only at `AGENTS/SAM/outbox/kernel/submissions/` (C1 contract).**
This directory is a planning staging area so the activation document can pin
exact sha256 values BEFORE Will's ruling without creating live commands.
At ruling time SAM copies these bytes to its own submission path and commits
them itself (C1: the submitting agent authors and explicitly commits its own
immutable command file). Until then, nothing here is readable by any live-shadow
mode: `load_live_submissions` reads only the activation-pinned `AGENTS/` paths
from a named commit.

- CMD-…033 (RegisterQuestion): sha256 `71996c763e4d4150e4380814f476fe24513f148e335f832fc42f4eb5d7a7bbe2`
- CMD-…034 (SubmitForecast):  sha256 `2dd24caee3884198dd440224b209b50e9ab8a52821b170065b06e91b043797e2`
