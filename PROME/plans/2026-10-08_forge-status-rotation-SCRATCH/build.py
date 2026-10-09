import sys, zlib, pathlib, subprocess
ROOT = pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'], text=True).strip())
SP = pathlib.Path(sys.argv[1])
src = subprocess.check_output(['git','show','ef2bc83f1:FORGE/STATUS.md'],cwd=ROOT,text=True)
assert src.endswith('\n')
L = src.split('\n')[:-1]            # L[i] = line i+1, newline stripped
def ln(n): return L[n-1]
def rng(a,b): return L[a-1:b]       # inclusive 1-based
# ---- sanity anchors (fail loud if the file moved under us) ----
anchors = {5:'> ✅ **2026-10-08 (Thu) — RECONCILE BY ANVIL', 9:'> **Updated:** 2026-10-08', 15:'Current regime + scenario weights',
           28:'| VLO | Stock | 1 | $412.00 |', 94:'> ⚠️ **NOT CAPTURED IN THIS 10/8 RECEIPT', 112:'### EXPIRING — Fri 10/09',
           117:'| **D-60** |', 123:'### Will supplies / PROME re-reads', 127:'| **D-71**', 128:'| **D-75**', 129:'| **D-70**',
           130:'| **D-74**', 131:'| **D-66**', 132:'| **D-69**', 133:'| **D-62**', 147:'| **D-1**', 149:'### Owner decides',
           156:'| — | **APD thesis tag', 158:'### CLOSED this pass', 162:'- **QTY CHANGE ×2 + NEW ×1:**', 166:'## Immediate Actions',
           181:'*History → `_archive/JOURNAL.md`', 183:'> 🤖 **PARSED BY MACHINE', 174:'| 🟡 **D-71 / D-69 / D-66**', 177:'| 🟡 Older Activity / detail', 36:'*No live event-box rows', 104:'*No rows. VLO ×1'}
for n,pre in anchors.items():
    assert ln(n).startswith(pre), (n, ln(n)[:60])
assert len(L)==183, len(L)
# ---- chunks: verbatim contiguous line ranges ----
chunks = [('A',5,5,'the 10/8 reconcile banner paragraph (ANVIL verification receipt)'),
          ('B',94,94,'§ Robinhood NOT-CAPTURED blockquote (9/29 card detail, prediction-market line, dead-by-date bookings)'),
          ('C',112,121,'§ Reconcile discrepancies → ### EXPIRING subsection (header, table, 6 rows incl. D-60)'),
          ('D1',128,128,'facts-owed row D-75 (OZK basis 1¢, record-only)'),
          ('D2',131,147,'facts-owed rows D-66 · D-69 and the 15 carried rows D-62 → D-1'),
          ('E',149,156,'### Owner decides — ruled / gated subsection (header, table, D-47 · WQ-386/VLO-SCALE · WQ-200 · APD)'),
          ('F',158,162,'### CLOSED this pass (D-72 · D-73 · the 10/8 QTY/NEW/MARK summary)'),
          ('G',183,183,'the PARSED-BY-MACHINE footer line (consumer registry + pass notes)'),
          ('H',28,28,'§ Longs VLO row (the full prior owner note)'),
          ('I',174,177,'§ Immediate Actions — the four 🟡 discrepancy rows as built 10/8')]
def crc(s): return zlib.crc32(s.encode('utf-8')) & 0xffffffff
rec = []
body = []
for tag,a,b,desc in chunks:
    text = '\n'.join(rng(a,b)) + '\n'
    (SP/f'chunk_{tag}.txt').write_text(text, encoding='utf-8')
    rec.append((tag,a,b,desc,len(text.encode('utf-8')),crc(text)))
    body.append(f'## Chunk {tag} — source line{"s" if a!=b else ""} {a}' + (f'–{b}' if a!=b else '') + f'\n\n{text}')
head = ('# FORGE/STATUS.md — ROTATION RECORD 2026-10-08 (read-cap relief; superseded or cold 10/8-reconcile material, verbatim)\n\n'
 '> **Source:** `FORGE/STATUS.md` as committed at `ef2bc83f1` (the 10/8 intraday reconcile; the later mappings pass a1eb75287 changed only `FORGE/position_management.tsv`; working file byte-identical to HEAD at rotation start — `git diff --quiet -- FORGE/STATUS.md` clean; receipt: `git show ef2bc83f1:FORGE/STATUS.md`). **Rotated:** 2026-10-08 evening by PROME (`prome-07`, laptop), NOT inside a reconcile — no position, mark, quantity or basis changes; plan + reads: `PROME/plans/2026-10-08_forge-status-rotation-PLAN.md`. **Reason:** read-cap relief — the live file measured 32,523 B = 100% of the 32,550 B budget (`scripts/read_cap_check.py FORGE/STATUS.md`, rotate-tier) with Friday 10/9 fills to book next. **Every chunk below is COLD or SUPERSEDED in the hot file by a pointer or a shorter restatement; every OPEN obligation it carries is still OPEN at its owner — the plan\'s obligation audit names where each survives. Cite as history, never as current.**\n>\n'
 '> **Chunks are verbatim source line ranges** (each line newline-terminated as in source; the single blank line between chunks is the separator, not source). Receipts = `PROME/tools/measure.py` semantics over each chunk as extracted, before insertion (bytes = UTF-8 incl. the final newline; crc32 over the same bytes):\n')
for tag,a,b,desc,nb,c in rec:
    head += f'> - **Chunk {tag}** — source line{"s" if a!=b else ""} {a}' + (f'–{b}' if a!=b else '') + f' ({desc}): **{nb} B · crc32 {c}**\n'
(SP/'STATUS_ROTATION_2026-10-08.md').write_text(head + '\n' + '\n'.join(body), encoding='utf-8')
# ---- hot candidate ----
R = {}
R[5] = ('> ✅ **2026-10-08 (Thu) — RECONCILE BY ANVIL to Will\'s Fidelity capture RECEIVED ≤15:26 ET TODAY: positions + Activity. INTRADAY; exact capture time UNKNOWN; marks are NOT closes.** Source `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md`; ANVIL re-verified 19/19 rows (Decimal) and the tie: Σ positions **$21,945.52** + cash **$11,421.19** + pending **+$1,283.98** = **$34,650.69 to the cent**. **Vs 10/7 (`git show e8fd99acf:FORGE/STATUS.md`): 1 NEW (QQQ $750C Oct-09 ×1) · 0 GONE · 2 QTY CHANGE (755P Oct-09 2→1 · 745P Oct-15 2→1, sold to close 10/8) · 16 MARK ONLY.** Full receipt → rotation 10/08 chunk A.')
R[9] = ln(9).replace('rotations → `_archive/STATUS_ROTATION_2026-10-01.md`', 'rotations → `_archive/STATUS_ROTATION_2026-10-08.md`, `_archive/STATUS_ROTATION_2026-10-01.md`')
assert R[9] != ln(9)
R[15] = ln(15).replace('`HEARTBEAT.md` (7/18 re-base + amendment #1 = current)', '`HEARTBEAT.md` (its own header names the current base and amendment count)')
assert R[15] != ln(15)
vlo_cells = ln(28).split(' | ')[:7]
assert vlo_cells[0].startswith('| VLO') and len(vlo_cells)==7, vlo_cells
R[28] = ' | '.join(vlo_cells) + ' | Today +$21.89. Bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Holding confirmed by Will 2026-10-07: “Yes, still one share”**. WQ-213: 1 of 3; **the remaining 2 sh STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there). **The held share\'s exit rule is `GATE-TERRY-VLO-HELD-01` — the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386 (`PROME/proposals/2026-10-07_VLO-december-management-RULED.md`, approved 10/7); nothing of it is restated here.** The gate reads the crack and the text, not the share\'s mark. The prior note, which restated the letter, is verbatim in rotation 10/08 chunk H |'
_unused36 = '*No live event-box rows — the VIX $20C/$25C spread (CLOSED 7/30, −$111.60) and the five Aug-21-2026 EXPIRED rows (−$2,816.72) are terminal → rotation records.*'
_unused104 = '*No rows. VLO ×1 moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*'
R_I = ['| 🟡 **D-71** — the same Activity scrolled to 10/1 (the roll\'s exit fill; = WQ-347) | one view | **Will** |', '| 🟡 **D-70 / D-74** — mappings re-review; cards; new bank-put ownership · **carried discrepancies (18)** — the summary row in § facts owed, owners per row; Robinhood not captured (the four 10/8-built 🟡 rows → rotation 10/08 chunk I) | owner integration | **PROME / TERRY / Will** |']
R[94] = ('> ⚠️ **NOT CAPTURED IN THIS 10/8 RECEIPT (nor 10/7, 10/1 or 9/30) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.')
R_C = ('*EXPIRING — Fri 10/09: QQQ $755P ×1 · QQQ $750C ×1 (NEW, no card) · USO $150C ×1 (15:00 ET stop) · Thu 10/15: QQQ $745P ×1 + $740P ×4 · Fri 10/16: TLT $82P ×1 + HBAN $16P ×2. Facts and cards: the position rows above; urgency and owners: § Immediate Actions; the 10/8-built six-row table verbatim → rotation 10/08 chunk C. WQ-347 (cited there for the QQQ lines) now carries only D-71, the row after D-60 below. D-60 (ITM expiry handling UNOBSERVED) stays live, first row of the next table.*')
R_D = ('| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |')
R_E = ('*Owner-decides rows (D-47 — RH WAL Dec-18 $70P ×1, `GATE-TERRY-ROLL70-EXIT` 0-of-3 as last recorded, no resting exit order, time stop 12/4: Will harvests · REGINALD grades · TERRY proposes · WQ-386 / VLO-SCALE: TERRY grades, Will executes · WQ-200 — USO 37 sh, no rule live, Will\'s hand · the APD tag / "D" badge: PROME / Will) verbatim → rotation 10/08 chunk E; live letters: § Longs (VLO · USO · APD), the Robinhood WAL $70P row, `PROME/GATES.tsv` (canonical for every gate here).*')
R_F = ('*CLOSED this pass (receipts = the 10/8 Activity view, transcription §①): **D-72** — Oct-02 740P ×4 −$886.90 · Oct-05 735P ×5 −$1,302.97 (derived; per-row contract counts NOT shown) · **D-73** — the five 10/2–10/7 entries; running balance $15,524.70 → $12,993.82 → $11,421.19, every link holds; the 10/7 pending −$1,572.64 settled at −$1,572.63 (D-75) · **QTY CHANGE ×2 + NEW ×1**, realized 10/8 +$918.30 (derived), 16 MARK ONLY. Bullets verbatim → rotation 10/08 chunk F.*')
g = ln(183)
cut = g.index(' *(Pass notes 9/27')
assert cut > 0 and '(10/8 pass:' in g
R[183] = g[:cut] + ' *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)* *(10/8 EVENING rotation pass, read-cap relief, no reconcile: no structural change inside any `## Fidelity` / `## Robinhood` / `## Account` region; the only position-row change is the VLO note cell (now a pointer to the gate letter); under § Reconcile discrepancies three `###` subsections → italic pointer lines, 18 carried rows → one summary row; the four parsed header shapes are byte-identical, that line carrying one appended rotation pointer; pinned mappings re-pinned in the installing commit.)*'
out = []
for i,line in enumerate(L, start=1):
    if i in R: out.append(R[i]); continue
    if 112 <= i <= 121:
        if i == 112: out.append(R_C)
        continue                      # 113–121 dropped (blank 122 stays)
    if i == 127:                       # facts-owed table: D-60 first, then D-71
        out.append(ln(117)); out.append(line); continue
    if i == 128: continue              # D-75 → chunk D1
    if 131 <= i <= 147:
        if i == 131: out.append(R_D)
        continue
    if 149 <= i <= 156:
        if i == 149: out.append(R_E)
        continue
    if 158 <= i <= 162:
        if i == 158: out.append(R_F)
        continue
    if 174 <= i <= 177:
        if i == 174: out.extend(R_I)
        continue
    out.append(line)
cand = '\n'.join(out) + '\n'
(SP/'STATUS_candidate.md').write_text(cand, encoding='utf-8')
nb = len(cand.encode('utf-8')); print(f'candidate {nb} B = {nb/32550:.1%} of budget ({nb-22785:+d} B vs the <70% stop 22,785; {nb-24412:+d} vs the 75% start 24,412)')
print('archive', len((SP/'STATUS_ROTATION_2026-10-08.md').read_bytes()), 'B')
for tag,a,b,desc,nbb,c in rec: print(f'  chunk {tag:2} L{a}-{b}: {nbb} B crc32 {c}')
