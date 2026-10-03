#!/usr/bin/env python3
"""GATES.tsv step-3 pass, 2026-10-03 (DOCKET L418; WQ-176 legs ② + the WQ-131 state-cell contract + the WQ-166 terminal-row archive).
PROME-only cells: STATE cells of LIVE rows over 220 chars → one line + hist pointer; ENVELOPE cells (consequence_on_fire ·
last_checked · source · review_by · consumed_by) over 400 B → latest dated read + pointer; TERMINAL rows RESOLVED ≥7 days →
PROME/archive/GATES_TERMINAL_ROWS_2026-10-03.tsv verbatim. Pre-cut cells go VERBATIM + crc32 to
PROME/archive/GATES_STATE_HISTORY_2026-10-03_step3.md. Leg ① (`condition` cells) is NOT touched — owner confirms per row (DESIGN 9/4).
HY-REKILL's condition AND consequence stay whole (WQ-162). Run --plan (writes the PLAN record, no TSV change) then --apply."""
import sys, zlib, os, subprocess, datetime
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
TSV = os.path.join(ROOT, "PROME/GATES.tsv")
HIST = os.path.join(ROOT, "PROME/archive/GATES_STATE_HISTORY_2026-10-03_step3.md")
TERM = os.path.join(ROOT, "PROME/archive/GATES_TERMINAL_ROWS_2026-10-03.tsv")
PLAN = os.path.join(ROOT, "PROME/proposals/2026-10-03_gates-step3-pass-PLAN.md")
H = "hist→STATE_HISTORY_2026-10-03_step3"
TERMINAL = ["GATE-TERRY-007", "GATE-REG-T02", "GATE-TERRY-ROLL70", "GATE-TERRY-USO135C"]  # RESOLVED 9/24 · 9/1 · 9/2 · 9/9 — all ≥7 days
COL = {"condition": 3, "consequence_on_fire": 4, "state": 5, "last_checked": 6, "source": 7, "consumed_by": 8, "review_by": 11}
NEW = {
 # ---- STATE cells (≤220 chars; lead token kept; a position-watching row names its ticker) ----
 ("GATE-HY-REKILL", "state"): f"LIVE — 0 of 2 published obs <260 (strict; bp = FRED % ×100); HY 312 [9/30 first-pub] ← 308 [9/29], 52bp above (LIQUID grade 10/1, beeb3b9b2); letter SELF-GRADING · {H}",
 ("GATE-LIQ-069", "state"): f"LIVE — 2-of-2 FIRED 9/26 (legs 5+2), consequent EXECUTED, stands on every basis; NEXUS flag routing PENDING at WALTER; anchor RE-BASED WQ-301(b), both signs — a one-sign fire → Will · {H}",
 ("GATE-LIQ-072", "state"): f"LIVE — NOT FIRED: IG OAS 84 [9/30 first-pub] vs >94; HY−IG basis 228 [9/30] vs <180; leg (3) SpaceX CANNOT-FIRE; 3rd/4th-issuer + 144A legs UNGRADED (LIQUID grade 10/1, beeb3b9b2) · {H}",
 ("GATE-FALCON-001", "state"): f"LIVE — leg 1 FIRED 7/23 · leg 2 NOT FIRED (WQ-353 letter PROVISIONAL, ≥35% w/w step-down; FALCON 10/1 +144%, evening read +167% — wrong sign) · leg 3 FIRED 8/15; R3 HOLD · {H}",
 ("GATE-OSPREY-001", "state"): f"LIVE — ✅ OWNER-GRADED 9/18 (OSPREY cb31cfb31): (a) CPC SPM damage NOT FIRED (assessment 9/9) · (b) FIRED 7/24, stays fired · (c) Tengiz FM NOT FIRED; Strike# = a FLOOR, not a census · {H}",
 ("GATE-BRENT-COT-35B", "state"): f"LIVE — vintage #8 [as-of 9/29] JOINT NOT-SPENT (BRENT a43e77347): Leg A MM gross shorts 129,436 ABOVE the 109,165–118,325 deadband · Leg B 6.8901% vs 4.909% NOT-SPENT · {H}",
 ("GATE-FERT-G5", "state"): f"LIVE — NOT FIRED 7-of-7 DTN prints: MAP $970 / DAP $926 [9/30, FERT first-party]; MAP $30 (3.09%) under $1,000; 3rd up-print, pace ~0.71%/mo (log basis, not scored) · {H}",
 ("GATE-CORAL-MSI-01", "state"): f"LIVE — 🟠 STOOD DOWN 9/13, SUPPLY-SIDE leg ONLY (overall stays 🟠; bank-transmission rail UNTOUCHED both ways); re-fire letter REGISTERED 9/28 (WQ-241); reading #7 [9/28] fires neither · {H}",
 ("GATE-BRK-R2", "state"): f"LIVE — leg (a) FIRED on TWO vehicles (North Haven PIF 9/25, cae55b4c3 · OCIC 10/2 Q3-prelim, 78bc27291), consequence RAN; OCIC requests FALLING 21.9→18.8→16.8% = shrinking queue · {H}",
 ("GATE-TERRY-VLO-HELD-01", "state"): f"LIVE — VLO held share ×1: leg A NOT FIRED through 10/2 (Nov crack proxy $97.97 vs $90.16 sell / $95 notice; TERRY ⑫-bis 1857731ff) · B1 NOT FIRED (no US export-restriction text) · {H}",
 # ---- ENVELOPE cells (≤400 B) ----
 ("GATE-HY-REKILL", "last_checked"): f"2026-10-01 14:25 ET PROME consumer read of LIQUID's 9/30-cell owner grade (memo PROME/inbox/processed/2026-10-01_from-LIQUID_9-30-cell-LIQ-07-trigger-fired.md; verified at its table): HY 312 [9/30] — 0 of 2, 52bp above 260; no count moved · prior reads (10/1 00:40 · 9/28 · 9/3 · 9/2) → {H}",
 ("GATE-HY-REKILL", "review_by"): f"2026-12-31 (OWNER-RECOMMENDED in LIQUID's 9/30 review, graded 2026-10-01; set by PROME; the base-rate reason → {H}. ⚠️ LIQUID's between-session `liquid-hy-watch` timer is DESKTOP-ONLY: on the laptop this gate is graded only when a LIQUID session boots) · prior 2026-09-30 → hist→GATES_STATE_HISTORY_2026-10-01",
 ("GATE-LIQ-069", "last_checked"): f"2026-10-02 10:27 ET PROME consumer read of LIQUID's WQ-301 (b) encode (9fe811cb3), VERIFIED at AGENTS/LIQUID/workbook/KB.tsv KB-LIQ-069: both line sets and the grading rule present; state unchanged (2-of-2 FIRED) · prior reads (9/28 L510 benchmark · 9/26 owner grade 63b77a55b) → {H}",
 ("GATE-LIQ-069", "review_by"): f"2026-10-15 (SUCCESSOR SET BY PROME on LIQUID's recommendation — LIQUID declined to self-set it; reason: the 9/15 window's named driver did not print, L4's binding limb is falsified, L5 not re-verifiable from this box. ⚠ The ORCL leg's 4th cycle is what this date exists to prevent — DOCKET L345 carries the decision) · hist→STATE_HISTORY_2026-09-12_liq069",
 ("GATE-LIQ-072", "last_checked"): f"2026-10-01 14:25 ET PROME consumer read of LIQUID's 9/30-cell owner grade (memo PROME/inbox/processed/2026-10-01_from-LIQUID_9-30-cell-LIQ-07-trigger-fired.md): QUIET, NOT FIRED — IG 84 vs >94; basis 228 vs <180; leg (3) CANNOT-FIRE; legs (1)/(4) UNGRADED. ⚠️ leg (2)'s basis half restored to the condition cell 10/1 (owner-found) · prior reads → {H}",
 ("GATE-LIQ-076", "last_checked"): f"2026-09-29 13:5x PROME: the consequent's joint PROME/NEXUS write-up DELIVERED in full (LIQUID 0517a2834 + NEXUS WQ-340 page row 3, 83e6fe366); W2 MEASURED 10:1x NOT MET (PDPOSCSBND-G10 −9,286 · -G5L10 +564 $mm [as-of 9/16]) — conjunction MET on W1+W3; NO BOOT INSTRUMENT READS THIS GATE (wiring owed); review 10/09 · full reads → {H}",
 ("GATE-FALCON-001", "last_checked"): f"2026-10-01 21:55 ET PROME consumer read of FALCON's evening memo (PROME/inbox/processed/2026-10-01_from-FALCON_rulings-encoded-and-evening-drain.md, aa531bc88): leg-2 exclusion wording ALIGNED to FALCON's letter ('halt or slowdown'); WQ-353 encoded 21:43; leg 2 NOT FIRED on FALCON's 10/1 grade (cc13aa8a0) · prior reads (9/28 grade + FAL-05 D85 context) → {H}",
 ("GATE-FALCON-001", "review_by"): f"2026-10-06 (OWNER-SET 9/28 in the FAL-05 packet: weekly tanker cadence; EVENT OVERRIDE = review immediately on any Bab-theater ENFORCEMENT event; FAL-06 + the EXIT_PROTOCOL §5/THESIS rewrite owed by 10/05 are FALCON's own DOCKET row) · prior 2026-09-29 → hist→GATES_STATE_HISTORY_2026-09-28_falcon001",
 ("GATE-OSPREY-001", "last_checked"): f"2026-09-18 OWNER GRADE (OSPREY cb31cfb31 — STATUS ACTIVE item 1 + KB-OSPREY-123/124; packet PROME/inbox/processed/2026-09-18_from-OSPREY_gate-grade-dyad-ruling-provenance-and-a-ledger-hole.md §3), transcribed by PROME 21:2x ET and verified at the owner's artifacts; the grade is the owner's · priors (9/17 · 9/2) → {H}",
 ("GATE-BRENT-COT-35B", "last_checked"): f"2026-10-03 16:1x ET PROME CONSUMER READ of BRENT's #8 owner grade at AGENTS/BRENT/workbook/COT_VINTAGES.tsv row 2026-09-29 (a43e77347: 129,436 / 6.8901% NOT-SPENT; packet 7ec7fdb3a processed) — consumed_by re-dated, no state change · prior reads (9/25 · 9/19) → {H}",
 ("GATE-BRENT-COT-35B", "review_by"): f"2026-10-09 (next COT print, as-of 10/6; #8 graded same day 10/2 by the live BRENT session brent-08 — same-day grades 2-for-2 on live sessions since the schedule defect was found. Base 122,904.5 + the Leg-A exhaustive form stay on the condition cell; re-basing = NEW N1 build + Will ruling) · prior 2026-10-02 → {H}",
 ("GATE-BRENT-COT-35B", "consumed_by"): f"2026-10-09 (BRENT's next Friday pair: COT as-of Tue 10/6 posts ~15:30 ET Fri 10/9) · prior consumers CONSUMED same day (#8 10/2 · #7 9/25) → {H}. ⚠ STRUCTURAL, BRENT-owned, NOT fixed: the autonomous Friday routine fires ~14:00 ET, before the ~15:30 post, so cot_grade.py exits 3 every Friday and the grade falls to a live session that may not exist",
 ("GATE-FERT-G5", "last_checked"): f"2026-09-30 print OWNER-GRADED 2026-10-01 ~11:06 ET (FERT 52e56c6cd; PRIMARY dtnpf.com curl, KB-FERT-045; GATE_GRADES.md 9/30/26): NOT FIRED 7-of-7; MAP $970 / DAP $926. PROME consumed 10/1 11:20 ET (verified at GATE_GRADES.md + TRIGGERS.tsv T4). WQ-351 wording clarification ENCODED 10/1 13:55 (no level/operator/instrument/consequent changed) · prior → {H}",
 ("GATE-FERT-G5", "consumed_by"): f"2026-10-07 | FERT owner grade at the next DTN Wednesday print (FERT re-dated its review_by to 10/07 at the 10/1 grade; the 9/30 consumer date was MET one day late by 52e56c6cd NOT FIRED 7-of-7 + PROME's read 10/1) · prior cells → {H}",
 ("GATE-CORAL-MSI-01", "last_checked"): f"2026-09-28 reading #7 (CORAL 496403f3b) mirrored in the state cell at the WQ-241 re-date; last OWNER GRADE consumed 2026-09-13 (CORAL 7035b2b3b, Parcl; VERIFIED at AGENTS/CORAL/STATUS.md §9/13): 4-of-5 >6.0, Cape Coral 5.91 under; 🔴→🟠 on the FROZEN 8/23 letter. ⚠️ Parcl active-listing count = literal 0 (placeholder); never carry · full grade → {H}",
 ("GATE-CORAL-MSI-01", "review_by"): f"2026-10-09 (PROME RE-DATED 2026-09-28 on Will's WQ-241 ruling: CORAL's next weekly Parcl reading grades on the amended letter; owner grade + PROME consumer read) · prior review_by cells → {H}",
 ("GATE-CORAL-MSI-01", "consumed_by"): f"CORAL grades at each WEEKLY Parcl reading on the amended letter (re-fire pair pending: 0 of 2 qualifying readings; stand-down: no metro < 5.90) — the WQ-241 successor question RESOLVED 2026-09-28 · prior cell → {H}",
 ("GATE-TERRY-ROLL70-EXIT", "last_checked"): f"2026-09-24 00:0x ET OWNER GRADE (REGINALD cbafeb76d; EXIT_LOG 16 rows): 9/15–9/23 closes ALL NOT QUALIFYING (WAL $79.03 … $75.60): this gate 0-of-3; REG-T02 state FIRED (cycle 2) UNCHANGED; 9/22 = vendor-gap read, owner-labelled. PROME read 00:2x. ⛔ A sub-78 close is a SUPPRESSED RE-ENTRY on GATE-REG-T02 (terminal), never a fresh fire · full → {H}",
 ("GATE-BRK-R2", "review_by"): f"BROCK · owner-surface disagreement CLOSED 2026-09-18 (BROCK 8a6cbcc93; verified by PROME at PC_REDEMPTION_REGISTER.tsv:1 — header reads 'review 2026-10-31 (CHANGED 2026-09-18 from 2026-11-15 …)', tag JUDGEMENT) · the 9/17 note → git show 1a3fe9c53:PROME/GATES.tsv line 22",
 ("GATE-NEXUS-T12S-DFII10", "source"): f"AGENTS/NEXUS/research/2026-09-24_t12_successor_DFII10_letter.md (§1 checks · §2 the letter · §4 first grade) · PROME/inbox/processed/2026-09-24_from-NEXUS_wq261-dfii10-successor-registered-and-drain.md (734345a2e) · PROME/proposals/2026-09-24_wq-batch-282-254-261-260-276-RULED.md row 261 · the NEXUS ask → {H}",
 ("GATE-TERRY-VLO-HELD-01", "last_checked"): f"2026-10-03 16:1x ET PROME consumer read of TERRY's FOURTH owner grade (card § ⑫-bis, 1857731ff, 14:42 ET 10/2): leg A 10/2 NOT FIRED, no A-notice — Nov crack PROXY $97.97 vs $90.16 sell / $95 notice; same-day bar provisional · B1 NOT FIRED (FR API + Public Inspection 10/2). No state change · priors (10/1 · 9/30 ×2 · 9/28) → {H}",
 ("GATE-HOMER-THESIS-KILL", "last_checked"): f"2026-09-29 09:3x OWNER GRADE at build (HOMER 926bdfee3; THESIS.md §4): 0 of 5 legs FIRED — C1 (ICE Aug 90+/FC 872K ↑; FC starts +29% YoY) · C2 (Freddie MF DQ 0.64% ↑, Fannie 0.57% ↓ [Aug]; Trepp MF >6.00%) · A1/A2/A3 (PMMS 7.03% [9/24] red; LEN 15.8% GM / KBH orders −12%) all not killed. Transcribed by PROME from the packet; letter verified at THESIS.md §3–§4.",
}
def load():
    raw = open(TSV, encoding="utf-8", newline="").read()
    assert "\r" not in raw
    lines = raw.split("\n")
    if lines and lines[-1] == "": lines = lines[:-1]
    hdr = [l for l in lines if l.startswith("#")]; body = [l for l in lines if not l.startswith("#")]
    return hdr, [l.split("\t") for l in body]
def main(mode):
    hdr, rows = load(); h = rows[0]; assert h[COL["state"]] == "state" and h[COL["review_by"]] == "review_by"
    today = "2026-10-03"
    hist = [f"# GATES state history — step-3 pass {today} (DOCKET L418; WQ-176 leg ② + WQ-131 state contract + WQ-166 terminal archive): pre-cut cells of PROME/GATES.tsv, VERBATIM",
            "Each section = the byte-exact pre-cut cell of the named gate_id and column; `entry-crc32` = zlib.crc32 over the section body (UTF-8); `bytes` = its UTF-8 length. Recompute, never trust. The one-line successors live in the TSV; the owner's file stays the grading surface.", ""]
    plan = [f"# GATES.tsv step-3 pass — PLAN (no TSV change until `--apply`) · {today}", "",
            "**Rule set applied:** WQ-131 state-cell contract (lead token + ONE-LINE current state + hist pointer, ≤220 chars) · WQ-176 leg ② envelope cells ≤400 B (consequence_on_fire · last_checked · source · review_by; consumed_by treated the same way, as step 2 did for its Prior chains) · WQ-166 terminal rows RESOLVED ≥7 days → the dated TERMINAL_ROWS archive. **Not touched:** every `condition` cell (leg ① needs the owner's confirm per row — DESIGN 9/4) · HY-REKILL's condition and consequence (WQ-162) · every cell already inside its cap · no state token changes, no threshold moves, no row deleted.",
            "**Invariants the result read checks:** every lead token unchanged · every archived cell byte-identical to the pre-cut cell (crc) · every position-watching LIVE row still names its ticker in the one-liner (VLO-HELD-01 → VLO; ROLL70-EXIT → WAL in its untouched state cell) · the four terminal rows reproduce byte-for-byte in the TERMINAL_ROWS file · 12 columns on every data row (the header's field count) · `python3 PROME/tools/prome_gate.py closeout` GATES legs pass after apply.",
            "**Files this pass creates (by `python3 PROME/tools/gates_step3_pass_2026-10-03.py --apply`):** `PROME/archive/GATES_STATE_HISTORY_2026-10-03_step3.md` (every pre-cut cell, verbatim + crc32 — the destination of every `hist→STATE_HISTORY_2026-10-03_step3` pointer below) and `PROME/archive/GATES_TERMINAL_ROWS_2026-10-03.tsv` (the four terminal rows, verbatim + per-row crc32). **Declared before the read-2 pass:** two live cells are ALREADY truncated mid-word in the live file (COT-35B `last_checked` ends `…REGIST`, `consumed_by` ends `…every cyc`; a pre-existing cut from an earlier edit) and are archived as they stand · GATE-TERRY-VLO-HELD-01 `consequence_on_fire` (849 B) is deliberately KEPT WHOLE: it is TERRY's verbatim action letter on a held position and every ≤400 B form the plan reader tested dropped Will's B1 right to sell without the desk or the latency caveat · untouched over-cap cells outside leg ②'s set or on terminal rows <7 days old: BRK-R2 `scannable` (407 B, prose in a token column — its own defect, registered separately), FLG-T08 and VLO-SCALE cells (they archive at the next terminal pass) · BRK-R2 `review_by` leads `BROCK ·` with no date (pre-existing; the 2026-10-31 review date sits inside its quoted header) · the ROLL70-EXIT `state` cell is untouched; its `last_checked` is cut and keeps citing GATE-REG-T02, which this pass archives — the archive file says so in its header and is grep-able by gate_id.", ""]
    moved = 0; saved = 0
    for r in rows[1:]:
        for (g, c), new in NEW.items():
            if r[0] != g: continue
            i = COL[c]; old = r[i]
            if c == "state": assert len(new) <= 220, (g, c, len(new))
            else: assert len(new.encode()) <= 400, (g, c, len(new.encode()))
            assert "\t" not in new and "\n" not in new
            hist += [f"## {g} · {c} — pre-cut cell, rotated {today} (step-3 pass)", f"entry-crc32: {zlib.crc32(old.encode())} · bytes: {len(old.encode())} · rotated {today}", old, ""]
            plan.append(f"### {g} · `{c}`: {len(old.encode())} B → {len(new.encode())} B ({len(old)} → {len(new)} chars)\nOLD:\n> {old}\n\nNEW:\n> {new}\n")
            saved += len(old.encode()) - len(new.encode()); moved += 1
            r[i] = new
    keep = [r for r in rows[1:] if r[0] not in TERMINAL]; term = [r for r in rows[1:] if r[0] in TERMINAL]
    assert len(term) == len(TERMINAL), [t[0] for t in term]
    for t in term: assert not t[COL["state"]].startswith("LIVE"), t[0]
    term_lines = ["\t".join(t) for t in term]
    plan.append(f"### TERMINAL rows → `PROME/archive/GATES_TERMINAL_ROWS_{today}.tsv` (verbatim; per-row crc32)\n" + "\n".join(f"- {t[0]} — state leads `{t[COL['state']][:70]}…` — {len(l.encode())} B — crc32 {zlib.crc32(l.encode())}" for t, l in zip(term, term_lines)) + "\n")
    new_hdr = hdr[0] + f" · {today} step-3 pass: 4 terminal rows → archive/GATES_TERMINAL_ROWS_{today}.tsv; {moved} state/envelope cells cut → archive/GATES_STATE_HISTORY_{today}_step3.md (DOCKET L418)."
    before = len(open(TSV, encoding="utf-8").read().encode())
    out_tsv = "\n".join([new_hdr] + ["\t".join(h)] + ["\t".join(r) for r in keep]) + "\n"
    plan.append(f"### Byte receipt (projected; `measure.py` after apply is the only figure to cite)\n- cells cut: {moved} · bytes saved in cells: {saved}\n- terminal rows removed: {len(term)} · bytes: {sum(len(l.encode()) for l in term_lines)}\n- file before: {before} B · after: {len(out_tsv.encode())} B (header line grows by the archive stamp)\n")
    if mode == "--plan":
        open(PLAN, "w", encoding="utf-8").write("\n".join(plan)); print("plan written", PLAN, "cells", moved, "saved", saved, "projected", len(out_tsv.encode()))
    elif mode == "--apply":
        assert not os.path.exists(HIST) and not os.path.exists(TERM), "archives exist — refuse to overwrite"
        open(HIST, "w", encoding="utf-8").write("\n".join(hist))
        th = [f"# PROME/archive/GATES_TERMINAL_ROWS_{today}.tsv — TERMINAL fire-ledger rows ARCHIVED VERBATIM from PROME/GATES.tsv on {today} (WQ-166 rule: RESOLVED/LAPSED/RETIRED ≥7 days before the pass; this pass = step-3, DOCKET L418): GATE-TERRY-007 (RESOLVED 9/24) · GATE-REG-T02 (9/1) · GATE-TERRY-ROLL70 (9/2) · GATE-TERRY-USO135C (9/9). GATE-FLG-T08 (10/1) and GATE-TERRY-VLO-SCALE (9/30) stay live-file for the dashboard's 7-day 'done' panel.",
              "# INTEGRITY: rows below are byte-identical to the removed lines; per-row crc32 (zlib, UTF-8) in the last comment line — recompute, never trust. Standing guards that cite these rows by name (GATE-REG-T02's suppressed re-entry; ROLL70's management = consequence_on_fire + TERRY card) keep citing the gate_id; grep this file.",
              "# COLUMNS = the live file's header line, copied verbatim:", "\t".join(h)]
        open(TERM, "w", encoding="utf-8").write("\n".join(th + term_lines + ["# per-row crc32: " + " · ".join(f"{t[0]}={zlib.crc32(l.encode())}" for t, l in zip(term, term_lines))]) + "\n")
        for r in keep: assert len(r) == 12 and all("\t" not in c and "\n" not in c for c in r)
        open(TSV, "w", encoding="utf-8", newline="").write(out_tsv); print("applied; TSV", len(out_tsv.encode()), "B; cells", moved, "; terminal", len(term))
    else: print("usage: --plan | --apply")
if __name__ == "__main__": main(sys.argv[1])
