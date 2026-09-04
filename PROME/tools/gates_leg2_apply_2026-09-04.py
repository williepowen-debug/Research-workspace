#!/usr/bin/env python3
"""WQ-176 leg ② — cap the four PROME-owned prose cells of GATES.tsv at ≤400 B; originals → GATES_STATE_HISTORY_2026-09-04_leg2.md verbatim+crc.
Run with --plan to write the plan (no TSV change); with --apply to write TSV + archive. HY-REKILL consequence exempt (WQ-162)."""
import csv, sys, zlib, io, os, subprocess
ROOT=subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip()
TSV=os.path.join(ROOT,"PROME/GATES.tsv"); ARCH=os.path.join(ROOT,"PROME/archive/GATES_STATE_HISTORY_2026-09-04_leg2.md")
H="hist→STATE_HISTORY_2026-09-04_leg2"
NEW={
 ("GATE-HY-REKILL","last_checked"): f"2026-09-03 12:5x PROME step-2 package (gloss only, no count moved): 263 = the AS-OF value on both 8/27 and 8/31; the 8/28 as-of print = 260, published 8/31. 2026-09-02 21:3x WQ-162 EXECUTED (self-grading letter; NOT FIRED 0-of-2; HY 265 [9/1], 260 [8/28] ON the line) · {H}",
 ("GATE-LIQ-079","consequence_on_fire"): f"funding-seizure pre-emption memo → PROME/NEXUS/BROCK/HENRY under X1 riders R1–R4 (BROCK 7/20): R1 separate funding root, never 'X1 MET' (X1 = wrapper-leads AND HY>280) · R2 opens NO X1 sizing gate · R3 SUSPENDS BROCK's wrapper-leads read · R4 RRP = wrong regime variable; LIQUID call at fire-time. Memo: BROCK→LIQUID 7/20 (supersedes KB-LIQ-074) · {H}",
 ("GATE-FALCON-001","last_checked"): f"2026-09-01 OWNER (FALCON abdf4efe5): 9/1 consumer date CONSUMED; FALCON's own Kharg GATE 1 FIRM-NEGATIVE (CENTCOM no-target release; re-adjudicate on any CENTCOM list/BDA) and Kharg GATE 2 NOT FIRED — neither is this row's leg 1 (FIRED 7/23) or leg 2; D 60→65 / C 35→30 (KB-FALCON-116/117/120) · {H}",
 ("GATE-FALCON-001","source"): f"AGENTS/FALCON/reports/2026-08-15_gate-falcon-001-leg3-yanbu-wc0803-fire-adjudication.md (leg-3 fire) · AGENTS/FALCON/reports/2026-07-23_babelmandeb-leg1-adjudication.md (leg-1 fire) · frozen spec AGENTS/FALCON/reports/2026-07-21_babelmandeb-SIG-003-adjudication.md · the 8/06 · 8/05 · 8/02 basis/re-check reports + the 7/23 outbox → {H}",
 ("GATE-OSPREY-001","last_checked"): f"2026-09-02 OWNER GRADE (OSPREY e82b1f79b, ANALYSIS_2026-09-02.md §6): (a) NOT FIRED — no July-episode assessment 8/20→9/2; every SPM claim = the 2025-11-29 SPM-2 arc; CPC full loading · (c) NOT FIRED — SEARCH-NOT-FOUND for any Aug/Sep 2026 Tengiz FM (all = the Jan-2026 GTES-4 arc) · (b) FIRED 7/24. Fresh verification (8/15 was absence-by-default) · {H}",
 ("GATE-FERT-G3","last_checked"): f"2026-09-02 OWNER GRADE (FERT 9a9e6fff5): NOT FIRED both legs — quota 3.3 Mt UNCHANGED (SEARCH-NOT-FOUND); $660/$670 floor lifted June, lower unpublished guidance; China offers into India <$400/mt CFR vs ~$415–445/mt intl [Profercy 8/13]. ⛔ kill-on-sight: '5–5.5 Mt quota' = the historical export range (2025 actual 4.9 Mt), not a quota action · {H}",
 ("GATE-TERRY-007","review_by"): f"2026-09-08 RE-DATED at PROME 9/3 closeout (9/2 review passed, TERRY dark). PROME consumer read 9/1: DGS10 4.79 window high, 0-of-5, 29bp; DFII10 2.44 NO-ADD (GATES_STATE_HISTORY_2026-09-03_step2.md) — NOT a grade; TERRY grades 9/2–9/4 at next boot (with the Sep-18/30 expiry pass), then weekly; expiry 9/30 may moot ⇒ NO-VERDICT · {H}",
 ("GATE-REG-T02","last_checked"): f"2026-09-01 OWNER GRADE (REGINALD 5c94c9622, NOTES.md §REG-T-02): scripts/market.py → Yahoo WAL close $77.26, $0.74 = 0.95% below; attribution SECTOR-WIDE (WAL −1.11% vs KRE −1.28%, cohort median 14/26, Spearman ρ +0.253 wrong sign) ⇒ LEVEL fire, V1/V3 UNCHANGED, carry the attribution with the fire. REG-T-01 UN-FIRED (KRE $72.62, 21.0% buffer) · {H}",
 ("GATE-CORAL-MSI-01","last_checked"): f"2026-09-02 OWNER GRADE (CORAL 70025dcc3, Parcl direct, stamp 9/3/2026 UTC): Tampa 7.01 · Punta Gorda 6.52 · North Port 6.29 · Cape Coral 5.95 · Lakeland 5.97 = 3-of-5 >6.0, all FELL; sub-threshold reading 1 of 2 (8/23 letter) ⇒ 🔴 HOLDS; second countable reading NOT BEFORE 2026-09-13 (≥10d; nothing de-fires). listings SEARCH-NOT-FOUND (never zero) · {H}",
 ("GATE-FLG-T08","consequence_on_fire"): f"ACTION ON FIRE: PROME spawns FLG (Tier 1) to grade T-08 vs its MF book, route REGINALD/HOMER; no capital path. REFINED 8/28 (FLG 2c1b48b7f, RGB #58): leases commencing 2026-10-01→2027-09-30, phased (FY2027 first full year); a 0% guideline CAPS revenue (DSCR grinds); trigger/level/action UNCHANGED; FLG T-11 2028-08-04 registered for the bite, T-09 demoted · {H}",
}
def load():
    raw=open(TSV,encoding="utf-8").read().split("\n"); hdr=[l for l in raw if l.startswith("#")]; body=[l for l in raw if not l.startswith("#") and l!=""]
    rows=[l.split("\t") for l in body]; return hdr, rows
def main(mode):
    hdr,rows=load(); h=rows[0]; out=["# GATES.tsv history — WQ-176 leg ② (2026-09-04, Will '173 and 176 approved with your recs' 09:52): the four PROME-owned prose cells capped at ≤400 B","",
      "*Each section = the VERBATIM pre-cut cell (`last_checked`, `consequence_on_fire`, `source` or `review_by`) of the named gate_id, byte-exact; `entry-crc32` = zlib.crc32 over the section body (UTF-8), `bytes` = its UTF-8 length. Recompute to verify — never trust the banner. The live cell keeps the latest dated read in ≤400 B and points here. HY-REKILL `consequence_on_fire` is EXEMPT (WQ-162 ruled exception) and does not appear.*",""]
    plan=[]
    for r in rows[1:]:
        d=dict(zip(h,r))
        for (g,c),new in NEW.items():
            if r[0]==g:
                old=d[c]; assert len(new.encode())<=400,(g,c,len(new.encode()))
                out+= [f"## {g} · {c} — pre-cut cell, rotated 2026-09-04 (leg ②)", f"entry-crc32: {zlib.crc32(old.encode())} · bytes: {len(old.encode())} · rotated 2026-09-04", old, ""]
                plan.append(f"### {g} · {c}: {len(old.encode())} → {len(new.encode())} B\nOLD:\n{old}\nNEW:\n{new}\n")
                r[h.index(c)]=new
    if mode=="--plan":
        open(os.path.join(ROOT,"PROME/proposals/2026-09-04_gates-leg2-PLAN.md"),"w",encoding="utf-8").write("# WQ-176 leg ② PLAN — ten cells, old → new (no TSV change until --apply)\n\nRule (WQ-176 design, Will 09:52): cap `consequence_on_fire` · `last_checked` · `source` · `review_by` at ≤400 B. The cell keeps the STATE — the latest dated read, its verdict tokens, the load-bearing levels and the ruling/commit cites — and points at the archive; DETAIL (sub-levels, secondary cites, rationale prose) moves to PROME/archive/GATES_STATE_HISTORY_2026-09-04_leg2.md, where the pre-cut cell is preserved VERBATIM with an entry-crc32 (the crc is computed at --apply and printed in that file's section banners; the plan shows text only). Nothing is lost from the repo; what the LIVE cell loses is detail a grader reaches through the pointer. HY-REKILL consequence exempt (WQ-162).\n\n"+"\n".join(plan)); print("plan written")
    elif mode=="--apply":
        open(ARCH,"w",encoding="utf-8").write("\n".join(out))
        assert all("\t" not in c and "\n" not in c for r in rows for c in r)
        open(TSV,"w",encoding="utf-8").write("\n".join(hdr)+"\n"+"\n".join("\t".join(r) for r in rows)+"\n"); print("applied")
if __name__=="__main__": main(sys.argv[1])
