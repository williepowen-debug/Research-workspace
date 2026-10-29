# PROME -> CATO: WQ-527 option B — add an ORACLE daily-read task preset to the Agent Launcher (DOCKET L848, due 2026-11-02)

**Will, 2026-10-28 20:59 ET, verbatim:** "527 C approve" (record `PROME/proposals/2026-10-28_wq527-528-RULED.md`). Option C = A (ORACLE's scheduled pulls-only routine, ORACLE builds) + B (a launcher preset, yours).

**ACTION (CATO, next session):** add one **Task preset** to the launcher (`scripts/agents.json`, documented in `scripts/AGENT_LAUNCHER.md` § Task preset, your custody since 117a07b90) that boots ORACLE for its daily $110-oil read. ORACLE sends you the one-line preset text (the DOCKET L729 / VX-ORC-04 read instruction); if it has not arrived when you sit, use: "ORACLE daily read: run the L729 / VX-ORC-04 business-day read (Polymarket and Kalshi pulls, spread tool), grade the logged rows, packet PROME; then close out." Keep the existing rule that choosing a preset starts nothing. Extend your launcher tests to cover the new preset. Commit under your custody; PROME verifies at the commit.

No authority, route or threshold moves. Not a schedule: Will launches.
