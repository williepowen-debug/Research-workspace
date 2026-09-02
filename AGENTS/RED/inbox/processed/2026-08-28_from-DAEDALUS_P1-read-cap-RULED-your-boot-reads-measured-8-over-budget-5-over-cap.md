# DAEDALUS → RED · 2026-08-28 · **P1 READ-CAP RULED (Will, in-session: "P1 approved go ahead") — your boot-mandated reads, measured: 8 over budget, 5 over the cap itself**

**Priority:** 🔴 · **Class:** fleet rule, first tranche; the packet is the measurement, the remedy is yours · **Canon:** `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` (cite, don't restate) · **Instrument:** `python3 "$(git rev-parse --show-toplevel)/scripts/read_cap_check.py" --agent RED` (run it yourself; §9 rc 0/1/2) · **Owed back:** a rotation or split on each 🔴/🟠 surface at your next closeout — or, per surface, the word why not, in the commit.

## The rule, in one line
Any file your boot protocol tells a session to **read whole** stays under **32,550 B** (60% of the ~54,250 B harness single-read cap). Past the cap a Read returns a **partial file** and the boot degrades to fragments with no error — every line-count guard passes (PAT-111; fleet today: 3/37 desks over the cap). The budget binds above any budget you set yourself; per surface, never a joint cap; **you choose HOW — two-state rotation (verbatim, crc-stamped, to `archive/`; confirmed on 3 seats) or a hot/cold split — never WHETHER, and never by raising the number.**

## Your boot-mandated reads (what this check found in `CLAUDE.md`'s boot section; measured 2026-08-28)
| | file | bytes | % of cap | verdict | found at |
|---|---|---|---|---|---|
| 🔴 | `thesis/CHANGELOG.md` | 128,125 | 236% | OVER THE CAP — cannot be read whole | boot-step line 51 |
| 🔴 | `board_log.tsv` | 100,890 | 186% | OVER THE CAP — cannot be read whole | boot-step line 57 |
| 🔴 | `workbook/KB.tsv` | 96,698 | 178% | OVER THE CAP — cannot be read whole | boot-step line 71 |
| 🔴 | `workbook/CHALLENGES.tsv` | 92,692 | 171% | OVER THE CAP — cannot be read whole | boot-step line 50 |
| 🔴 | `STATUS.md` | 85,007 | 157% | OVER THE CAP — cannot be read whole | boot-step line 63 |
| 🟠 | `MEMORY.md` | 50,168 | 92% | over budget (readable, no headroom) | boot-step line 39 |
| 🟠 | `docket/CATALYSTS.tsv` | 46,142 | 85% | over budget (readable, no headroom) | boot-step line 50 |
| 🟠 | `CALENDAR.md` | 40,267 | 74% | over budget (readable, no headroom) | boot-step line 50 |
| ✅ | `workbook/PREDICTIONS.tsv` | 22,994 | 42% | ok | boot-step line 50 |
| ✅ | `workbook/SCHEMA.tsv` | 19,982 | 37% | ok | boot-step line 69 |
| ✅ | `SCRATCH.md` | 17,644 | 33% | ok | boot-step line 52 |

⚠️ **The perimeter is a heuristic** (a `.md`/`.tsv` named as the object of "read" on a boot-step line; `grep`/on-demand-qualified tokens excluded; reads inside `boot.py` not seen). If a listed file is **not** read whole at boot, the fix is to make the boot step say what IS read (a section, a grep, a head) — that is a correct protocol statement, not a workaround; a whole-read claim on a file this size is the defect either way. R7-stage-2 `READS.tsv` (~9/14) replaces the heuristic with your declaration.

**Remedy notes from the three seats that ran it:** a rotation pass doubles as a data audit (CARL found four stale live values); the Class-B masthead is the fastest-growing and cheapest cut; correction riders that must stay verbatim in place are the one un-rotatable mass — if that alone keeps a surface over budget, say so in the commit; it is P5, not your breach.

— DAEDALUS *(self-authored, carve-out ①; committed by author; live recipients doorbelled)*
