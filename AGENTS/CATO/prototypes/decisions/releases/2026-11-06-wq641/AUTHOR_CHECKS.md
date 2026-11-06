# WQ-641 author evidence

Candidate built in /tmp/cato-wq638, prior reviewed bytes in /tmp/wq641-before; full install patch and delta are preserved here. No live application or owner acceptance has been changed while the targeted read is pending.

- 66 existing/updated Option A, batch, desk and desk-review tests pass. The prior broken batch assertion now checks per-answer confirmation. Fixtures publish received receipts before new integration.
- Eight targeted WQ-641 tests pass, including all seven stale-source cases with and without received acknowledgment, fresh-fetch behavior, historical replay after policy change, prior received enforcement, global fallback, malformed-card isolation, noninteractive refusal and real subprocess watcher turnover. The turnover test keeps the former lock held during new SessionStart. One additional PTY test proves print mode is refused even with terminal stdin (nine tests total).
- Native Chrome: fallback chat notice; approve with exact conditions; disapprove with no alternate selection; status updates on background reload, focused editing, errors/limit, sync and API failure; viewport fit. Ten assertions passed. Only disposable repositories/profile used; no live answers.
- Actual interactive PROME alert remains UNPROVEN. Claude inventory exposed only an old blocked background session; Codex inventory exposed unloaded historical PROME threads. Neither is an available current interactive transport. Probe/approval packet published as d303063702 after a transient DNS failure/retry. No receipt received at candidate freeze. Intended install is explicitly authorized fallback: app_only_enabled=false, no notification hooks installed. A headless reader is not used as fake live proof.

Single follow-up reader is native Opus, resumed from its prior independent session, hooks disabled. Scope is changed controls and fallback; no general audit. The one follow-up report is now preserved as INDEPENDENT_REVIEW.md: ACCEPT WITH NAMED RESIDUE for fallback only. Deferred notification items 3, 4, 8 and accepted same-login/owner-attestation limits survive.

Legacy receipt suite: 31 tests passed separately. Reviewer independently closed B1 and items 1, 2, 5, 6, 7; see its report for exact test counts and limits. The reviewer saw some author tests inside the delta before its own pass, so this is not labelled a fully blind read.
