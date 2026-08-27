#!/usr/bin/env python3
"""Roll FULLY-PROMOTED proposal blocks out of KURA's spec into its proposal archive.

WHY THIS EXISTS (2026-08-27, Will-directed)
-------------------------------------------
`subagent_memory_roll.py` (2026-08-20) capped the sub-agents' MEMORY files. It worked.
But it left the other half of every spawn read untouched, and for KURA that half is the
bigger one:

    METSUKE   spec  24K   memory 288K
    KOYOMI    spec  24K   memory 112K
    KURA      spec 184K   memory 172K   <-- the SPEC is the larger file

Measured 2026-08-27: **96% of KURA.md is one section, `## PROPOSED ADDS`**, holding every
proposal from Run 2 (June) onward -- 45 of 49 already promoted into KB.tsv. KURA re-read
roughly **44K tokens of its own completed homework at every spawn**, before looking at a
single artifact. Same shape as the defect the memory tool fixed; different file; nothing
was watching it.

⚠️ THE "158K CAP" THAT PROMPTED THIS DOES NOT EXIST. KURA reported being "over the 158K
spec". `subagent_memory_roll.py` defines NO numeric cap -- 158K was a one-off MEASUREMENT
in its docstring, taken 2026-08-20, and it is already stale (the file is 184K now). A
measurement in a comment was read as a limit. Recorded because the misread is the more
transferable finding than the bloat.

WHY A SEPARATE TOOL AND NOT A FLAG ON THE MEMORY ROLLER
-------------------------------------------------------
The two use DIFFERENT closure criteria and must not be merged:
  * memory roll  -> a block is terminal when EXPLICITLY MARKED closed. Silence != closure.
  * this tool    -> a block is terminal when every row it proposed is PROVABLY LANDED, by
                    ID lookup in KB.tsv or KB_ARCHIVE.tsv. That is mechanical proof, which
                    is STRONGER than a marker -- and it is available here precisely because
                    a proposal has a verifiable destination that a run-history entry lacks.

⚠️ CHECK BOTH DESTINATIONS. A promoted row can later be ARCHIVED, so KB.tsv alone is the
wrong referent -- SAM's own first pass at this diagnostic checked only KB.tsv and wrongly
reported 4 proposals as "still pending" when all four were in KB_ARCHIVE.tsv
([[finding_instrument_reports_clean_against_the_wrong_reference]]).

DESIGN RULES (inherited deliberately from subagent_memory_roll.py)
-----------------------------------------------------------------
1. MOVE, NEVER DELETE -- appended verbatim to the archive; byte conservation verified.
2. PROOF, NOT SILENCE -- a block with ANY unlanded proposal STAYS, and is reported.
3. ARCHIVES ARE NOT SPAWN-READ -- the spec keeps a pointer; the archive is reference-only.
4. REPORT-ONLY BY DEFAULT -- --apply required to write.
5. --keep-runs N (default 1) keeps the most recent N blocks regardless, for continuity.

Usage:
    kura_proposal_roll.py [--apply] [--keep-runs N]
"""
import argparse, re, sys
from pathlib import Path

SAM = Path(__file__).resolve().parent.parent
SPEC = SAM / "workbook" / "KURA.md"
ARCHIVE = SAM / "workbook" / "KURA_PROPOSALS_ARCHIVE.md"
KB = SAM / "workbook" / "KB.tsv"
KB_ARC = SAM / "workbook" / "KB_ARCHIVE.tsv"
SECTION = "## PROPOSED ADDS"


def landed_ids():
    """Every KB id that PROVABLY exists — live OR archived. Both, deliberately."""
    out = set()
    for p in (KB, KB_ARC):
        if p.exists():
            for line in p.read_text(encoding="utf-8").split("\n")[1:]:
                if line.strip():
                    out.add(line.split("\t")[0])
    return out


def plan(keep_runs):
    s = SPEC.read_text(encoding="utf-8")
    if SECTION not in s:
        return None, "no PROPOSED ADDS section", [], []
    head, seg = s[:s.index(SECTION)], s[s.index(SECTION):]
    done = landed_ids()
    hdrs = [(m.start(), m.group(0)) for m in re.finditer(r"^### Run \d+ .*$", seg, re.M)]
    blocks = []
    for j, (p, h) in enumerate(hdrs):
        e = hdrs[j + 1][0] if j + 1 < len(hdrs) else len(seg)
        body = seg[p:e]
        n = int(re.search(r"Run (\d+)", h).group(1))
        proposed = sorted(set(re.findall(r"^(KB-SAM-\d+)\t", body, re.M)))
        missing = [x for x in proposed if x not in done]
        blocks.append({"n": n, "hdr": h, "body": body, "start": p, "end": e,
                       "proposed": proposed, "missing": missing})
    newest = sorted((b["n"] for b in blocks), reverse=True)[:keep_runs] if keep_runs else []
    roll, keep = [], []
    for b in blocks:
        if b["n"] in newest:
            b["why"] = f"kept: most recent {keep_runs}"; keep.append(b)
        elif not b["proposed"]:
            b["why"] = "kept: proposes no rows (nothing to prove)"; keep.append(b)
        elif b["missing"]:
            b["why"] = "KEPT — unlanded: " + ", ".join(b["missing"]); keep.append(b)
        else:
            roll.append(b)
    return (head, seg), None, roll, keep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--keep-runs", type=int, default=1)
    a = ap.parse_args()

    parts, err, roll, keep = plan(a.keep_runs)
    if err:
        print(f"  {err}"); return 1
    head, seg = parts
    print(f"\n── KURA.md  {len(SPEC.read_text(encoding='utf-8'))//1024}K  "
          f"({len(seg)//1024}K in {SECTION})")
    for b in sorted(keep, key=lambda x: x["n"]):
        flag = "🔴" if b["missing"] else "  "
        print(f"   {flag} keep  Run {b['n']:<3} {len(b['body'])//1024:>3}K  {b['why']}")
    for b in sorted(roll, key=lambda x: x["n"]):
        print(f"      roll  Run {b['n']:<3} {len(b['body'])//1024:>3}K  "
              f"all {len(b['proposed'])} landed")
    if not roll:
        print("   ✅ nothing to roll"); return 0

    freed = sum(len(b["body"]) for b in roll)
    print(f"\n   would move {len(roll)} block(s), {freed//1024}K "
          f"(~{freed//4//1000}K tokens per spawn)")
    if not a.apply:
        print("   report-only. --apply to write.\n"); return 0

    # BYTE CONSERVATION: spec + archive must be preserved exactly.
    before = len(SPEC.read_text(encoding="utf-8")) + (len(ARCHIVE.read_text(encoding="utf-8")) if ARCHIVE.exists() else 0)
    kept_seg = seg
    for b in sorted(roll, key=lambda x: x["start"], reverse=True):
        ptr = (f"{b['hdr']}\n\n> ⤴️ **ROLLED TO `KURA_PROPOSALS_ARCHIVE.md` 2026-08-27** — "
               f"all {len(b['proposed'])} proposed rows verified landed in KB.tsv/KB_ARCHIVE.tsv "
               f"({', '.join(b['proposed'])}). Reference-only; not spawn-read.\n\n")
        kept_seg = kept_seg[:b["start"]] + ptr + kept_seg[b["end"]:]
    arc_head = "" if ARCHIVE.exists() else (
        "# KURA PROPOSED-ADDS ARCHIVE\n\nRolled out of `KURA.md` by `kura_proposal_roll.py`. "
        "**Reference-only — NOT read at spawn.** A block appears here only when every row it "
        "proposed was verified landed in `KB.tsv` or `KB_ARCHIVE.tsv`. Move, never delete.\n")
    ARCHIVE.write_text((ARCHIVE.read_text(encoding="utf-8") if ARCHIVE.exists() else arc_head)
                       + "\n" + "\n".join(b["body"].rstrip() for b in sorted(roll, key=lambda x: x["n"])) + "\n",
                       encoding="utf-8")
    SPEC.write_text(head + kept_seg, encoding="utf-8")
    after = len(SPEC.read_text(encoding="utf-8")) + len(ARCHIVE.read_text(encoding="utf-8"))
    ok = after >= before - 200   # pointers replace headers; tiny net loss is the header text only
    print(f"   {'✅' if ok else '🔴'} applied · byte-conservation {'OK' if ok else 'FAILED'} "
          f"({before:,} → {after:,})")
    print(f"   KURA.md now {len(SPEC.read_text(encoding='utf-8'))//1024}K\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
