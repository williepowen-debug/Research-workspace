# SPEC — `ledger_staleness.py` registered-surfaces extension (per-agent manifest)

**Status:** SPEC — no code yet. Will-visible batch pattern per the 7/31 `scripts/` grant; PROME GO 2026-08-15 (war-triad answer packet §2). Build after review; wire into Staleness Sweep run #4 (~9/1) as the first consumer.

## Problem (measured, 2026-08-15 war-triad review)

The enforcer's coverage is its glob: `workbook/*.tsv` (+ `--trade` for TRADE.md/POSITIONS). Everything load-bearing outside that glob is outside every staleness gate — the **coverage-inversion class** (BRENT F6: the enforcer watches the convenient surface, not the at-risk one; same family as PAT-035's original TRADE.md gap).

Measured instances, one review:

| Surface | Why it matters | State found |
|---|---|---|
| `AGENTS/FALCON/FRESH_LEG_BASELINE.md` | Self-designated consumer-facing ("cite it directly") | Contradicted by STATUS 9 days, ungated |
| `AGENTS/FALCON/thesis/TIMELINE.md` | Load-bearing timeline | 19d stale, ungated |
| `AGENTS/FALCON/workbook/BYPASS_INTEGRITY_BASELINE.md` | Feeds a live threshold pair | Ungated |
| `AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv` | Born 8/10 **WITH a two-clock header** | Outside the glob — **nothing reads the header it correctly carries** |
| `AGENTS/HAWK/domain/energy-strikes/CROSS_WAR_SUMMARY.md` | Derived cross-war aggregate | 18d stale, WRONG sibling marks, 4 closeout skips |
| `AGENTS/HAWK/domain/war-risk/CROSS_THEATER_WAR_RISK.md` | Derived war-risk aggregate | Re-stamp missed again 8/15, one session after repair |

The worst case is VESSELS.tsv: an owner adopting the PAT-044 convention correctly, at birth, gets zero enforcement because of a path. Compliance without coverage.

## Mechanism

1. **Per-agent manifest, owner-maintained:** `AGENTS/<NAME>/workbook/SURFACES.tsv` — one row per extra surface: `path (repo-relative) · class (LIVE-DATA | DERIVED | CONSUMER-FACING) · staleness_days · note`. TSV not flag-soup; the manifest itself is a workbook ledger, so the existing glob self-covers it.
2. **Enforcer change:** after the glob pass, if the manifest exists, grade each listed path with the existing recognizer stack unchanged (two-clock header preferred → banner vocabulary auto-exempt → git-time fallback; PAT-035/044 semantics identical). Per-row `staleness_days` overrides the global default (DERIVED surfaces rot at their regeneration cadence, not the data's — HAWK 13/13a is the type case).
3. **Fail-loud on a dead manifest row:** a listed path that doesn't exist prints `MANIFEST ROW DEAD: <path>` rc≥1 — a manifest that silently skips dead rows is the firetime URL-as-path class (fixed 8/11) reborn.
4. **Perimeter line in output (CHECK_STANDARD §2):** `graded: N workbook + M manifest · manifest absent for <NAME>` — absence of a manifest is stated, never silent, so "no manifest" and "all fresh" stop being the same output.
5. **Non-breaking:** no manifest → byte-identical behavior for all existing callers. Rollout opt-in at next owner touch; DAEDALUS seeds manifests for the six measured instances above via the normal packet path (owners ratify — the manifest lives in their tree).

## Guards on the guard

- CHECK_STANDARD §3: watch the capable case (a manifest row with a stale two-clock header flags) AND the null (absent manifest states itself) before shipping. §4: manifest rows beyond any display cap announce `(+N more)`.
- Failure-direction (§6): bias toward flagging — a false stale-flag on a derived surface costs one look; a silent rot repeat cost HAWK four closeouts and wrong sibling marks.
- CHECKS.tsv row updates in the same commit as the code (PAT-084 discipline; on-FAIL column = "owner named in manifest note").

## Explicitly out of scope

Auto-discovery of unregistered surfaces (that is the Falsification/Staleness sweeps' judgment layer, not the mechanical enforcer's); editing owners' manifests (theirs, packet-route); mtime-keyed anything (PAT-039).
