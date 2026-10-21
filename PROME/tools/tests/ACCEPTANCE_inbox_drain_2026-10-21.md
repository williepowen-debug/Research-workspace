# ACCEPTANCE — PROME inbox drain becomes a required step (Will 2026-10-21 13:08 ET, "Okay we need to fix this")

**Written before the edit** (WQ-229). This is process change 6 this session, an OVERRUN of the standing ceiling of five. Will's word ("Okay we need to fix this") authorized the fix but did not name the ceiling, so the overrun is disclosed in the closeout report.

## Defect, in its own terms
`PROME/inbox/` is PROME's sole delivery surface (BOOT.md step 6), but no boot or closeout step says to read and disposition it. The only enforcement is the gate's "agent freshness" check, labelled `[advisory]`.
- Packets dated 10/12–10/18 were all filed (221 in `processed/`); from 10/19 the inbox stopped being drained: 72 + 38 + 17 = 127 unread at 10/21 13:06 ET (`ls PROME/inbox/2026-10-1{9}* …`).
- On 10/21 PROME launched five desks without draining, despite the check's "drain first before ANY launch brief", and missed REGINALD's REG27 encode packet (11:42 ET) until ARGUS caught it.

## Acceptance conditions
- **ID1 — the label matches the rule (AMENDED after independent read 1, ❌1):** a new check, "PROME/inbox drained", counts EVERY file under `PROME/inbox/` outside `processed/`, whatever its name or sender (dotfiles excluded). At boot and refresh it prints `[ACTION OWED]` when any remain and ✅ only when none remain. It stays non-blocking. The agent-freshness check returns to advisory: it keys on `from-<AGENT>` names and cannot measure the whole inbox.
- **ID2 — the manual names the act:** BOOT.md step 6 states the drain. Every packet in `PROME/inbox/` gets a disposition before any desk launch and before the report: consumed (filed to `processed/` with its act done), routed, or registered as a DOCKET/WILL_QUEUE row. The step 8 ACTION OWED rule then makes an undrained inbox a PARTIAL headline.
- **ID3 — closeout carries it:** CLOSEOUT Pre-closeout names the inbox. Packets that arrived during the session are dispositioned, or listed as carried with their count, in the closeout report.
- **ID4 — tests (AMENDED after ARGUS closeout #2):** the AO6 set-of-ACTION-checks test now lists "PROME/inbox drained" (agent freshness went back to advisory). Two new tests execute `check_prome_inbox`. ⚠️ The AO6 comparison was loosened from `sorted(sites)` to `sorted(set(sites))` because the new check records under one name at two sites. A duplicated ACTION site is therefore no longer caught. Declared residue.

## Neighbours
- **Ordinary:** an empty inbox gives ✅ `[action]`.
- **Overlap:** a desk packet already read by message (today's five returns) still needs filing to `processed/`. A message is not a disposition.
- **Wrong owner:** packets addressed to PROME only. Desks' own inboxes are unaffected.
- **Missing information:** a tool crash prints under the class with its error, never ✅ (run_script, pre-existing).
- **Concurrent activity:** packets landing mid-session are covered by ID3.

## Reads
- reads: 1 (see below).
- **Read 1 (2026-10-21 ~13:12 ET, Opus): HOLD, 2 ❌ · 5 ⚠️.**
  - **❌1 FIXED:** agent_freshness missed 9 of 12 name shapes (2 live ANVIL packets were invisible), so it is replaced as the drain measure by `check_prome_inbox` (every unfiled file). Two tests cover the nine shapes plus processed/dotfiles exclusion.
  - **❌2 FIXED:** BOOT.md line 111 no longer calls the check "ADVISORY class".
  - **⚠️1 FIXED:** step 6 now says every disposition ends with filing to `processed/`, and citing rows point at the processed path.
  - **⚠️2:** step 6 now says a due-row wake may precede a large drain only if the report names the undrained count.
  - **⚠️3 (residue):** CLOSEOUT 3b covers only arrivals during the session, and the closeout gate does not run the count.
  - **⚠️4:** tests now execute the check.
  - **⚠️5:** no change.
  - **State:** IMPLEMENTED · TESTED; post-read fixes NOT independently verified.

