# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-04 ~3:40 AM UTC (~10:40 PM ET)

---

## RIGHT NOW — Handoff

### Done session 3 (late night):
- ✅ PREDICTIONS.tsv rolled out: 55 predictions seeded, 24 FL.tsv archived
- ✅ HENRY EOD read: Dow close corrected, ISM Mfg Prices 70.5%, HEN-01 maintained 60%
- ✅ LIQUID EOD read: HY OAS EST 315-335 (bias corrected), BX -3.82%, LIQ-01 LIKELY_EARLY
- ✅ REGINALD inbox completed

### Done session 2:
1. ✅ Stale agent refreshes: HENRY, LIQUID, REGINALD, HANS (all returned)
2. ✅ HERMES delivery run + diagnostic report (18 signals delivered, system working)
3. ✅ Inbox processing: HENRY, HAWK, LIQUID all processed inbox signals
4. ✅ ML.tsv audit trail rule pushed to ALL 13 agents + template
5. ✅ INBOX/OUTBOX symlinked to domain dirs (git-tracked, visible in repo)
6. ✅ Missing inbox steps added: OTTO, ZHAO, HANS, DARWIN, HAWK
7. ✅ Domain symlinks created: OTTO, DARWIN, HAWK
8. ✅ WILL/INBOX.md created — agents can target Will directly
9. ✅ `To: WILL` rule pushed to all 13 agent instruction files
10. ✅ Agent instruction files backed up to `AGENTS/_instruction_backups/`
11. ✅ Priority HERMES script: `scripts/check_urgent_signals.sh`
12. ✅ CARL audit spot-checked (clean: 212 lines, workbook updated)
13. ✅ PREDICTIONS.tsv implementation plan written → `PROME/PREDICTIONS_IMPLEMENTATION_PLAN.md`
14. ⏳ REGINALD inbox processing (spawned, running — should complete shortly)
15. ⚠️ LIQUID inbox run FAILED (19min timeout) — needs re-run next session

### Done last session:
- Memory condensation, OUTBOX/INBOX system, HERMES built, CORAL/TEX/RENO registered
- BUILD_AGENT.md, FL.tsv → PREDICTIONS.tsv, 8 agent audits

### Operational protocol — PRIORITY HERMES:
After any agent spawn batch, run: `scripts/check_urgent_signals.sh`
If exit 0 (🔴 found) → spawn HERMES immediately, don't wait for scheduled run.

### Next session priorities:
1. **🔴 Check FRED for HY OAS Mar 3 confirmed** (resolves LIQ-01)
2. **🔴 ADP 8:15 AM + ISM Services 10:00 AM → spawn HENRY after each**
3. **🔴 Run HERMES** (fresh OUTBOX signals from HENRY + LIQUID)
4. **🟠 Audit batch 3:** HAWK, MARCO, BROCK
5. **🟠 Audit batch 4:** HANS, ZHAO, DARWIN
6. **🟡 Remaining infra:** AGENTS.md→CLAUDE.md rename, AGENTS_DIRECTORY.md update
7. **🟡 Research threads:** Athene run risk, Korea third anchor, DHS→food inflation

### HANS ceasefire revised: 85% → 12% (30-day)
### ISM Services PMI tomorrow AM — HENRY prepped with full decision matrix

## Hot Market Context
- S&P 6,781. VIX 26.43. HY OAS ~303-355bps.
- Cash ~$2,100 for post-NFP redeployment.
- CTA trigger 6,707 armed. Zero gamma cushion at open.

---

*This file is disposable. Rewrite freely. No preservation guilt.*
