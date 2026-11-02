# WQ-543 preamble text + DST cron re-set — 2026-11-01 (DOCKET L526)

**Session:** BRENT, PROME Tier-1 spawn, 2026-11-01 21:11–21:2x EST. **Ruling:** WQ-543 RULED APPROVE (a)(b)(c), DEFER (d) — Will 2026-10-29 14:34 ET, verbatim *"approve"*; record `PROME/proposals/2026-10-29_wq543-preamble-text-RULED.md`; packet `inbox/processed/2026-10-29_from-PROME_WQ543-RULED-APPROVE-install-with-DST-reset.md`.

## State: INSTALLED + VALIDATED (by PROME, 2026-11-02 02:28–02:30Z, WQ-585 A)

Updated 2026-11-02 by BRENT from PROME's packet and receipt. PROME installed these four images (SHA256SUMS verified) and the EST crons via RemoteTrigger, then fired one Thursday-fallback validation run at 02:30Z: line 1 `PREAMBLE: unshallowed=n detached=n ff=0 venv=rebuilt head=8379e8a` (commit bdfb453bf), PASS. Receipt: [PROME install receipt](../../../../PROME/reports/2026-11-01_wq543-routine-install-receipt.md). (d) stale-venv pip re-run stays DEFERRED by the ruling. Registry: [SCHEDULED_RUNS](../../SCHEDULED_RUNS.md).

### State as written 11/1 (superseded, kept verbatim)

**PREPARED, NOT INSTALLED, NOT VALIDATED**

| Leg | State | Why |
|---|---|---|
| (a)(b)(c) text in the four saved prompts | **PREPARED** — four after-images in this directory | done locally |
| `RemoteTrigger update` of the four live routines (prompt + cron) | **NOT DONE** | this session exposes no RemoteTrigger or routine tool (`ToolSearch select:RemoteTrigger` → no match, 2026-11-02 ~02:13Z). The 10/28 install was done from a session that had it. |
| DST cron re-set (+1h UTC) | **NOT DONE** | same tool |
| One validation run + run-log excerpt (reader #18) | **NOT DONE** | needs the install first |
| (d) stale-venv pip re-run | DEFERRED by the ruling | — |

## The text change (identical in all four prompts; diff against `audits/2026-10-28_L526-preamble-install/after_*.txt`)

```
- BOOT PREAMBLE (L526, installed 2026-10-28 on Will's word). Run before ANY read or write, in this order. Every step is fail-loud; never force, never reset, never rebase.
+ BOOT PREAMBLE (L526, installed 2026-10-28 on Will's word; WQ-543 (a)(b)(c) text, Will 2026-10-29). Run before ANY read or write, in this order. Every step is fail-loud; the preamble never forces, resets or rebases.
- 1. If .git/shallow exists: git fetch --unshallow origin. Otherwise: git fetch origin.
+ 1. If .git/shallow exists: git fetch --unshallow origin. Otherwise: git fetch origin. If the fetch fails, STOP and name the error.
- 2. If HEAD is detached: git checkout master.
+ 2. If HEAD is not on master (detached or another branch): git checkout master.
- 5. First line of your output file AND of your final report: PREAMBLE: unshallowed=<y/n> detached=<y/n> ff=<commits fast-forwarded> venv=<present|rebuilt>
+ 5. First line of your output file AND of your final report: PREAMBLE: unshallowed=<y/n> detached=<y/n> ff=<commits fast-forwarded> venv=<present|rebuilt> head=<post-merge HEAD short sha, 7 chars>
```

Each old string occurred exactly once per file (asserted by the edit script); the preamble block (lines 3–9) is byte-identical across the four new images. Hashes: `SHA256SUMS`.

**Not changed (deliberately):** DAEDALUS's optional receipt-placement tightening (`inbox/processed/2026-10-31_from-DAEDALUS_L526-friday-receipt-placement.md`: Friday 10/30 put the line on line 5, bold). The approved text already says "First line"; making it "plain text, no Markdown" is a new wording that WQ-543 did not approve. Carried as a candidate for Will's word, not installed.

## Exact install steps for whoever holds RemoteTrigger

For each routine: `RemoteTrigger get` (the full `ccr` job_config is required; a partial job_config replaces the whole object, `SCHEDULED_RUNS.md` § update path), replace the prompt with the matching `after_<day>.txt` here, set the cron, `RemoteTrigger update`, re-fetch, record `updated_at` and the next run.

| Routine | trigger_id | Prompt image | Cron now (EDT-era) | Cron to set (EST) | Local time after |
|---|---|---|---|---|---|
| Monday Market Open | `trig_01DHTJWiUSVYXY9vUeto57qr` | `after_monday.txt` | `45 13 * * 1` | `45 14 * * 1` | Mon 09:45 EST |
| Wednesday EIA | `trig_014CDR4kjWtc29mYxXspGAHF` | `after_wednesday.txt` | `0 15 * * 3` | `0 16 * * 3` | Wed 11:00 EST |
| Thursday EIA fallback | `trig_01ALYRXtjDGbfHeubqdvyJdf` | `after_thursday.txt` | `15 18 * * 4` | `15 19 * * 4` | Thu 14:15 EST |
| Friday Close | `trig_01GBVYAq5TwPc6JQ4hbfYYMe` | `after_friday.txt` | `15 20 * * 5` | `15 21 * * 5` | Fri 16:15 EST |

Then fire ONE validation run (Thursday fallback is the established choice) and save its line-1 receipt plus a run-log excerpt here. Acceptance: line 1 is `PREAMBLE: … head=<sha7>` and the `head` sha exists on origin/master.

**Consequence if not done before Monday 2026-11-02 13:45Z (08:45 EST):** the Monday "Market Open" pull runs 45 minutes BEFORE the 09:30 open on the old text; Wednesday runs 10:00 EST, before the 10:30 WPSR; Friday 15:15 EST, before the ~15:30 COT post (the gap the 10/02 install closed). The cron re-set alone can also be done by Will in the claude.ai/code/routines UI.
