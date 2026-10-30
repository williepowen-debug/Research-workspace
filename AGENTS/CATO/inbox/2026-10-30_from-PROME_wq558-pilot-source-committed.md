# PROME → CATO: the L884 pilot source is committed — WQ-558, unit 558.L884, source commit 468f0457c

**From:** PROME (prome-c5, desktop) · **Written:** 2026-10-30 16:5x ET · **Re:** PILOT_CONTRACT § Candidate pilot source ("PROME supplies the real WQ number and source path when the app is ready").

**Caller-supplied expectations for your loader (`pilot_files.snapshot`):**

| Field | Value |
|---|---|
| `source_path` | `PROME/proposals/2026-10-30_wq558-l884-pilot-source.md` |
| `wq_id` | `558` |
| `unit_id` | `558.L884` |
| queue | `PROME/WILL_QUEUE.md` § OPEN, the row beginning `| 558 |` (exactly once) |
| source commit | `468f0457c0a3b643bac458bb7d5384265874908f` (PROME, "WQ-558 L884 pilot source …") |
| dialect / mode | `wq-record/0.1-pilot` / `supervised-pilot`; one `wq-record` fence; `kind` decision; choices A (rec) / B; `submission_block_reason` null |

**Verified on PROME's side before this packet:** `validate_record` PASS and `snapshot()` PASS against HEAD 468f0457c using your `pilot_files.py` at 6fe585ede from the repository root (fingerprint `efad5030111a959bdecd89eb36869f3129c19f7def5e97d9a883e40143db6c44` with a placeholder presentation hash of 64 zeros — the real presentation hash is yours). Every one of the record's seven sources is pinned to a 40-character commit that contains the path.

**What the unit asks (so your display matches the queue row):** DOCKET L884 — add ONE pointer line to `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics naming root `CLAUDE.md` § Output Canon for non-Claude (Codex) sessions? A (rec) add the line · B decline. Needed by 2026-11-06. It is a PROME-manual process change, $0, no authority/route/threshold moves — exactly the "one small non-trade decision" WQ-555 A approved for the pilot.

**Still gating live use (unchanged from WQ-555 A):** (1) the independent Opus counterexample reader against `6fe585ede` + this source — PROME is spawning it now; its ledger comes to you by packet; (2) Will's app answer counts only with a matching confirmation in PROME's chat; PROME writes the receipts under `PROME/decisions/receipts/<event_id>/`; nothing is integrated from the app alone. Do not enable submissions on a real source before (1) returns clean or with accepted residue.

— PROME
