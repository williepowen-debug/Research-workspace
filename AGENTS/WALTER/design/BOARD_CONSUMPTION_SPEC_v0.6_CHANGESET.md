# BOARD_CONSUMPTION_SPEC → v0.6 — Platform-Collapse Changeset (DRAFT)

**Authored:** 2026-06-26 by WALTER (OpenClaw cutover, "WALTER-can-do-now" item). **Status:** DRAFT — ready to apply, but **lands in lockstep** with the root `CLAUDE.md` reframe + `walter_doctor` collapse + the dependents (CHECKLIST / STATE / REGISTRY), NOT ahead of them (a live v0.6 while root still says "two platforms" + doctor still short-circuits on `OPENCLAW` = a half-migrated contradiction). Two slots wait on a Will ruling — see the defaults memo. Source: `design/OPENCLAW_CUTOVER_PLAN.md` Phase 2/3.

---

## 📋 Recommended-defaults memo — ratify these 3 (the low-stakes Phase-0 calls)

Each avoids a lockstep schema migration and has near-zero blast radius. My recommendation in **bold**; say the word and they're locked.

| # | Decision | Options | Recommendation |
|---|----------|---------|----------------|
| 0e | REGISTRY.tsv **Platform column** | drop (TSV schema change — must land in the same commit as `walter_doctor` `header.index('Platform')` or ValueError → silent stale fallback) vs keep-uniform-CC | **KEEP, uniform `CC`.** Vestigial but zero-risk; revisit later. |
| 0f | `delivery_log.tsv` **recipient_platform** (col 5; 42 historical `OPENCLAW` rows) | drop (forces migrating 191 rows + doctor col-index + CHECKLIST + STATE in lockstep) vs keep-as-constant | **KEEP, stamp `CLAUDE_CODE` going forward.** Zero migration; preserves the append-only audit. Never rewrite the 42 historical rows. |
| 0g | **FLASH/IMMEDIATE auto-push authority** (was PROME's per §3.4/§7) | Will-coordinated window vs WALTER-self-on-verified-clean-tree | **WALTER-self on a verified-clean tree via `scripts/safe-push.sh` ff-gate** (PROME is no longer an always-on push agent; the ff-gate is the safety). |

If ratified as above, the changeset below resolves with **no schema migration** — the columns stay, only the *values* and the *delivery semantics* simplify.

---

## Section-by-section v0.6 changeset

> Convention: **APPEND** a v0.6 history entry — never rewrite the v0.1–v0.5 history (append-only record of real past state). Bump the status header to v0.6 and add a "single-machine collapse" line.

- **§1 Vocabulary** — `delivered` collapses to one definition: *a handoff is `delivered` when its `inbox/WALTER/` file is **committed AND on origin** (reachable on the recipient's next pull).* Drop the OpenClaw "shared-clone = delivered on commit" branch. `published` / `consumed` unchanged.
- **§3.3 Platform-nuanced `delivered` table** — **RETIRE the two-row table.** Replace with the single §1 definition above. (This is the core collapse.)
- **§3.4 scoped-push fallback** — drop the `(Claude-Code recipients)` qualifier (there is only one platform now). **KEEP the mechanism** (FLASH/IMMEDIATE may scoped-push on a verified-clean tree); **reassign its authority per 0g** (default: WALTER-self via the ff-gate). `written_not_delivered_pending_push` **STAYS** — it is still true single-machine (a recipient cannot pull an unpushed handoff); only the *platform gate* around it drops.
- **§4 `delivery_log.tsv` schema** — `recipient_platform` per 0f (default: keep, constant `CLAUDE_CODE`). No row migration.
- **§6.1 / §6.2 git-derived sync telemetry** — collapse the OpenClaw INFO branch → one ladder: committed-not-on-origin = MED, uncommitted = LOW. **KEEP the shallow-clone / no-origin INFO guards** (valid git edge cases single-machine).
- **§7 Push authority** — was "PROME/Will-scoped." → per 0g (default: WALTER-self-on-clean-tree via ff-gate for FLASH/IMMEDIATE; PRIORITY/ROUTINE ride the normal closeout push). Drop the PROME-as-push-agent premise.
- **§8 / §8.1 Consume rollout** — drop "OpenClaw via PROME installs the boot step / CC self-apply" split → **all recipients self-apply the consume boot-step** (one platform). The per-recipient `inbox/WALTER/` consume-and-`git mv` mechanism is **UNCHANGED and STAYS** (intra-machine, platform-agnostic).
- **§9 Quick/Full WALTER mode reference** — per Phase-0 **0d** ruling (retire vs repurpose-as-CC-route-only). If repurposed: strip "PROME spawns a temporary OpenClaw copy" → "a CC-spawned route-only session"; keep the registry-only whitelist + Iran-anchor guard.
- **§10 cost/rationale** — drop the VPS/shared-clone justification prose.

## Dependents that must move in the SAME lockstep landing (Phase 3)
- `walter_doctor.py` — retire `_cc_agents()`/`_CC_FALLBACK` per 0e; drop the `platform=='OPENCLAW'` short-circuit (delivered_but_unconsumed) + the OpenClaw branch (written_but_undelivered); repoint cron_liveness → Scout. **If 0e = keep-uniform-CC, the `header.index('Platform')` lookup still resolves — lower urgency, but the OPENCLAW short-circuits should still go.**
- `SIGNAL_PROCESSING_CHECKLIST.md` Phase 3.5 — uniform delivered; Quick L414 per 0d; bump version + sweep `STATE.md §1`.
- `WALTER CLAUDE.md` step 11 + RULE 10 + KEY DESIGN FILES rows — uniform delivered, drop "platform-nuanced".
- `REGISTRY.tsv` Platform per 0e; `delivery_log.tsv` per 0f; `STATE.md §1` pointers in lockstep (version_drift guard).
- Root `CLAUDE.md` "Two platforms" reframe — ROOT scope, Will-coordinated, same window.

## Landing order (when Will greenlights)
1. Ratify 0e/0f/0g (the memo above) + 0d (Quick) + 0a (PROME→CC).
2. Land root reframe + this v0.6 + walter_doctor + CHECKLIST + STATE + REGISTRY/delivery_log **in one coordinated commit/window** (canonical-source rule: owners first, but they ship together so no doc contradicts).
3. Run `version_drift_check.py` + `walter_doctor.py` — confirm at-or-below the pre-migration baseline (doctor exit 38, drift clean, captured 2026-06-26).

---

*Companion to `design/OPENCLAW_CUTOVER_PLAN.md`. This changeset is the WALTER-side draft of the cutover's Phase 2/3; it does not modify the live spec until the lockstep landing.*
