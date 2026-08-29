# Blind cold-reader transcript — proposed root, 2026-08-29 ~15:1x ET

**Method:** fresh Explore-class agent, read ONLY `CLAUDE.proposed.md` (pre-clarity-fix revision, commit `23062b4cc`), 16 ground-truth questions whose answers live in the live root; quote + line required; NOT ANSWERED allowed. **Result: 16/16 correct.**

| # | Question (short) | Answer given | Correct |
|---|---|---|---|
| 1 | Where does CARL write to request PROME action | `PROME/inbox/` at repo root, not under AGENTS | ✅ |
| 2 | Forbidden git add forms | `git add .`, `-A`, `AGENTS/<YOUR_NAME>/` as a directory; under Gate C also computed lists / `commit -a` | ✅ |
| 3 | Memory file under memory/auto/ — may/must commit, which carve-out | Yes and MUST — ③ | ✅ |
| 4 | Enforcement command + forbidden form | `memory_index_check.py --strict --slug <name>`; never bare `--strict` | ✅ |
| 5 | Read-cap budget; same as MEMORY cap? | 32,550 B; NO, different from 25,600 B | ✅ (trap) |
| 6 | Non-ff: run what, check what, escalate when | pull --rebase --autostash after overlap check; escalate on out-of-dir conflict or persistence through a cycle | ✅ |
| 7 | Renumber rule 6? Citation form | Never; "root rule #6" / "Non-Negotiable #6" | ✅ |
| 8 | Roster canonical; tie-break | ROSTER.md; ROSTER wins | ✅ |
| 9 | Potash depth; where is the rule | triage-only; FERT CLAUDE.md §POTASH | ✅ |
| 10 | FORGE/STATUS owner; position truth | PROME; off-repo | ✅ |
| 11 | --amend ever? message method | Never; heredoc file + `commit -F` | ✅ |
| 12 | 90d-old, index-only ref, pending DOCKET artifact — retirable? | No — clause ① overrides; index ref wouldn't count anyway | ✅ (trap) |
| 13 | Literal push receipt | `Pushed. CONFIRMED: HEAD … on origin/master` | ✅ |
| 14 | Who commits HEARTBEAT/FORGE; who must not | PROME; domain agents flag | ✅ |
| 15 | Carve-out ④: may commit what; never afterwards | own submission JSON at the named path; never edit/delete; submission only | ✅ |
| 16 | Where do reasons live | docs/CANON_PROVENANCE.md; git log -p | ✅ |

**Ambiguities the reader flagged (verbatim class) → disposition:**
- Bare "rule 6"/"rule 6b" at the messaging line breaks the doc's own citation rule → FIXED ("messaging rule 6/6b", home named). *Inherited from live root.*
- 1d "a hard cap" with no number → FIXED (~200 lines / 25,600 B restored). *Draft regression — live root had it.*
- Non-ff overlap check: no method → FIXED (merge-base diff vs porcelain). *Inherited.*
- Receipt line has a literal ellipsis → FIXED (`HEAD <sha> is on origin/master (fresh fetch).`, from safe-push.sh:104). *Inherited.*
- "flag to Prome, don't commit" absolute with no forward pointer to carve-outs → FIXED. *Inherited.*
- Rule 3 has no example → BY DESIGN (PSEC example lives in provenance, key `critical-rule-3`).
- `LEDGER_GLOB` undefined → FIXED (`AGENTS/<NAME>/workbook/LEDGER_GLOB`). *Inherited.*
- Gate C ④ names no activation surface → FIXED (`KERNEL/GATE_C_*_ACTIVATION_*.json`, `revoked_at` empty). *Inherited.*
- Unopenable dependencies (AGENTS.md, MESSAGING, TERRY, FERT, DAEDALUS blueprints, WALTER spec) → expected; pointers, not rules.

**Reading:** 6 of the 8 actionable ambiguities are carried by the LIVE root today. The restructure is a net clarity gain even before the byte savings.
