#!/usr/bin/env python3
"""index_cold_shard.py — one-shot: shard memory/auto/INDEX_COLD.md by theme (PROME flow rule; pre-registered 8/28 next-wave form; prepared 2026-09-06, RUN ONLY AFTER scripts/memory_index_check.py + memory_citation_census.py read INDEX_COLD*.md — DAEDALUS 9/6 delivery): the eight 'embedded → canon' sections → INDEX_COLD_EMBEDDED.md.
Usage: python3 shard_cold.py [--write]   (default = dry-run, prints sizes + slug conservation, writes nothing)
Invariants asserted: slug union (HOT ∪ COLD ∪ SHARD) unchanged; every moved section appears verbatim in the shard;
INDEX_COLD.md keeps its header, a pointer section, and every non-embedded section; both files < 51,200 B."""
import re, sys, zlib
from pathlib import Path
W = "--write" in sys.argv
ROOT = Path(__file__).resolve()
import subprocess; ROOT = Path(subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip())
HOT, COLD, SHARD = ROOT/"memory/auto/MEMORY.md", ROOT/"memory/auto/INDEX_COLD.md", ROOT/"memory/auto/INDEX_COLD_EMBEDDED.md"
SLUG = re.compile(r'(?<![A-Za-z0-9_])((?:finding|feedback|project|reference)_[a-z0-9_]+)')
def slugs(t): return set(SLUG.findall(t))
hot = HOT.read_text(encoding="utf-8"); cold = COLD.read_text(encoding="utf-8")
before = slugs(hot) | slugs(cold)
lines = cold.split("\n")
heads = [i for i,l in enumerate(lines) if l.startswith("## ")]
sections = []  # (title, start, end)
for k,i in enumerate(heads):
    j = heads[k+1] if k+1 < len(heads) else len(lines)
    sections.append((lines[i], i, j))
MOVE_PREFIXES = ("## Boot / closeout", "## Closeout-moment rows", "## Sub-agents, teams", "## Spawn delivery contract",
                 "## Git rows verbatim", "## Prediction & calibration", "## Trade / position / risk", "## Deep-research method")
moved = [s for s in sections if s[0].startswith(MOVE_PREFIXES)]
assert len(moved) == 8, [s[0][:40] for s in moved]
keep_idx = set(range(len(lines)))
for _,a,b in moved:
    for x in range(a,b): keep_idx.discard(x)
header_end = heads[0]
shard_body = "\n".join("\n".join(lines[a:b]).rstrip("\n") for _,a,b in moved)
shard = ("# Fleet Auto-Memory — COLD INDEX, shard `EMBEDDED` (split from `INDEX_COLD.md` 2026-09-06, PROME flow rule)\n\n"
         "> The eight **embedded → canon** census sections — every row here has a canon embed home (BOOT.md · CLOSEOUT.md · ORCHESTRATION_PLAYBOOK.md · COMPLETION_SPEC.md · root CLAUDE.md Git Protocol · FORGE/PREDICTION_DISCIPLINE.md · AGENTS/TERRY/RISK_RULES.md · DEWEY) and is promotion-EXEMPT (Will 8/22). Moved VERBATIM; per-file ceiling **51,200 B** applies to this file too (`read_cap_check.py memory/auto/INDEX_COLD_EMBEDDED.md`). Readers treat `INDEX_COLD.md + INDEX_COLD_*.md` as ONE cold set (memory_index_check · memory_citation_census, shard-aware 9/6). ⛔ Never delete a row; rows move, never vanish.\n\n"
         + shard_body + "\n")
pointer = ("## Embedded → canon sections — MOVED to `memory/auto/INDEX_COLD_EMBEDDED.md` (shard 2026-09-06)\n"
           "- The eight census sections (Boot/closeout · Closeout-moment · Sub-agents/orchestration · Spawn delivery · Git rows · Prediction & calibration · Trade/risk · Deep-research) live verbatim in the shard, crc32 " + "{CRC}" + " over its body; every slug they carry is still indexed (readers glob `INDEX_COLD*.md`). This file keeps the agent pointers, project-state, tool gotchas, rare infra and every demotion wave.\n\n")
new_lines = [l for i,l in enumerate(lines) if i in keep_idx]
# insert the pointer section right after the header (before the first remaining '## ')
first_head = next(i for i,l in enumerate(new_lines) if l.startswith("## "))
crc = zlib.crc32(shard_body.encode("utf-8")) & 0xffffffff
pointer = pointer.replace("{CRC}", str(crc))
new_cold = "\n".join(new_lines[:first_head]) + "\n" + pointer + "\n".join(new_lines[first_head:])
new_cold = re.sub(r"\n{3,}", "\n\n", new_cold)
if not new_cold.endswith("\n"): new_cold += "\n"
new_hot = hot.replace("> **COLD/EMBED tiers → `memory/auto/INDEX_COLD.md`**",
                      "> **COLD/EMBED tiers → `memory/auto/INDEX_COLD.md` + `INDEX_COLD_EMBEDDED.md` (the embedded-in-canon census, sharded 2026-09-06; readers glob `INDEX_COLD*.md`)**", 1)
assert new_hot != hot, "MEMORY.md header anchor not found"
after = slugs(new_hot) | slugs(new_cold) | slugs(shard)
assert before == after, (before - after, after - before)
for t,a,b in moved:
    body = "\n".join(lines[a:b]).rstrip("\n"); assert body in shard, t[:40]
bc, bs, bh = len(new_cold.encode()), len(shard.encode()), len(new_hot.encode())
assert bc < 51200 and bs < 51200, (bc, bs)
print(f"COLD {len(cold.encode())} → {bc} B ({bc/51200:.1%}) · SHARD {bs} B ({bs/51200:.1%}) · HOT {len(hot.encode())} → {bh} B ({bh/25600:.1%}) · slugs {len(before)}=={len(after)} · shard crc32 {crc}")
if W:
    SHARD.write_text(shard, encoding="utf-8"); COLD.write_text(new_cold, encoding="utf-8"); HOT.write_text(new_hot, encoding="utf-8")
    print("WRITTEN")
else:
    print("dry-run — nothing written")
