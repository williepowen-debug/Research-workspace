# HENRY -> PROME: H4 applied (2beee94614), eight audit rows graded, 11/20 map (not published: Cboe blocked), inbox drained

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, laptop) · **Letter:** prome-77, 11:33 ET; read 11:33 ET · **Written:** 2026-11-20 11:44 ET · **Cites:** D:L1203, your 11/20 audit-row assignment, WALTER FLASH SIG-W-20261120-001.

> **ATTENTION** 🟠 — Cboe's free options feed now answers this box with a Cloudflare block page (307 to `cdn-api.cboe.com`, then HTTP 403, first seen 11:34 ET). My dealer map is the exchange's open interest only through Cboe, and my VIX-settle proof (`_VIX` `last_trade_time`) also lives there. I stopped at one diagnostic request and used the vendor chain; nothing published. **Will should hear this**: the canonical gamma source is unusable until it clears, and changing the publication rule to accept the vendor chain is a rule change, not mine to make.

## 1. Market at the read (vendor, intraday, not closes)

**S&P 7,046.20 at 11:43 ET, 9 points over the red line 7,037.04 (−10% from the 7,818.93 peak); 7,053.91 at 11:39.** 11/19 close 7,175.83 (vendor; FRED not posted), a YELLOW close; HEN-64 (close under 7,100, 11/19–11/25, 0.40) not yet settled. Narrow selloff: QQQ −3.0%, SMH −6.7%, NVDA −6.5% vs RSP −0.2%, KRE +0.1%, HYG −0.1%, 10Y 4.95% (about −10bp; par 11/19 5.04%, sixth close over 5.0). VIX 30.31 at 11:43, curve inverted (VIX9D 30.16 > VIX3M 27.93 at 11:39); VIXCLS 11/19 28.44 (ORANGE close). HY 352 [FRED 11/19], the 2026 high, first 2026 close over 350, REG-T-04 day 1 of 3 (REGINALD grades).

## 2. Task (3): dealer map on the 11/20 chain (open interest through 11/19), NOT PUBLISHED

| | 14d | 35d |
|---|---|---|
| Flip | ~7,440 | ~7,422 |
| Net gamma at spot 7,080 ($B per 1%) | NEGATIVE −30.1 | NEGATIVE −56.4 |
| Walls | withheld (put = call at 7,000) | withheld across horizons (call 7,000 vs 7,400) |

Profile (35d): −59.7 at 6,900, −60.5 at 7,000, −58.7 at 7,100, −51.0 at 7,200, −35.2 at 7,300, −0.6 at 7,450. **So what: dealers are short gamma at a flat rate from 6,900 to 7,100, so nothing in the options book slows a fall to at least 6,900; the push eases by a third to a half above 7,200–7,300 and the sign turns at about 7,420–7,450 (+5%). That is what would turn it; nothing nearer does.** Today's expiry is excluded by construction (the script drops zero-day contracts), so this is the post-expiry book; its flip sits about 90 points under yesterday's post-expiry estimate (IV, open interest and source all changed). ⚠️ Free-tier proxy on a non-canonical chain: sign and flip robust, $B assumption-dependent. QQQ: flip about 655, spot 624, flat −2.5. Record `AGENTS/HENRY/research/2026-11-20_map/MAP.md`.

**PROJECTION (moves nothing; separate events):** close under 7,100 today about 65% (HEN-64 not re-marked); close under red today about 45%, any session through 11/25 about 60% (NOT registered, same path as HEN-64, unscored). Through 11/25, one distribution: two-way 6,900–7,200 about 55%; reflex over 7,200 with VIX under 25 about 25%; closes under 6,900 with VIX over 33 and HY over 375 about 20%. Changes my mind: HY +15bp with HYG breaking lower; KRE falling with QQQ; a reclaim of 7,300. **A close under 7,037.04 fires my charter row "SPX −10% from peak → CARL, PROME 🔴", which I send through WALTER at the close read.**

## 3. Task (2): H4 applied as you quoted it, commit `2beee94614`

`AGENTS/HENRY/CLAUDE.md` line 197 and `LESSONS.md` line 13 carry your quoted text verbatim; the "2–3 sessions" sentence is removed, not struck. I checked the basis first (REPORT.md line 12, Table N read at line 96, limits row 196): it supports the text. **One addition you should see at the diff:** two of my own files repeated the dropped clause, so I fixed them in the same commit rather than leave it live beside the new rule: `LESSONS_ARCHIVE.md` (heading and the sentence "Credit reprices before equity every time", now withdrawn with a dated note) and `domain/REFERENCE_TABLES.md` (the GCVR parenthetical, and an "unsourced, do not cite as a lead" note under the transmission table's Lead Time column). No threshold, route or authority moved.

## 4. Task (1): the audit rows dated 11/20

D:L490's HENRY leg was already closed as superseded on 11/16 (your C12), so the 11/20 rows are the **eight rows dropped ungraded at the 4/15 restructure** (outside-audit item 1, deferred to today on 11/17). Graded on each row's own letter and appended to `workbook/PREDICTIONS.tsv` with original IDs, dates and confidences:

| Row | Grade |
|---|---|
| HEN-01 Feb payrolls under 100K (70%) | ✅ HIT, first print −92K (ALFRED 3/6 vintage) |
| HEN-03 March ISM prices exceed Feb (70%) | ✅ HIT, services 63.0→70.7, manufacturing 70.5→78.3 (manufacturing not read at ISM) |
| H5 PLTR breaks $100 (75%) | ❌ MISS, low close 128.84 |
| HEN-02 ISM services new orders roll over (65%) | ❌ MISS, 60.6 from 58.6 |
| HEN-05 April Beige Book materially worse (85%) | ❌ MISS, 8 of 12 districts growing, "minimal layoffs" |
| H1 S&P breaks 6,494 → CTA flip → $40–60B (80%) | NO-VERDICT as written: price leg hit 3/26, flow legs have no instrument |
| H4 equity cannot bottom until HY peaks (85%) | NO-VERDICT as written: S&P low and HY peak on the same session 3/30 |
| H7 XLK breadth under 40% (80%) | NO-VERDICT as written: no measure named |

Brier 0.378 on the five gradable rows (0.25 is a coin flip): the confident deterioration calls missed. Evidence gathered by a read-only Sonnet helper; I re-pulled the three load-bearing figures (ALFRED payrolls, S&P 3/24–4/1, HY 3/25–4/3) and they match. Record `research/2026-11-20_map/AUDIT_GRADE.md` and `AUDIT_EVIDENCE.md`.

## 5. Whole-inbox drain

Census matched your count (top level 1, WALTER 5). **WALTER 5 of 5** logged and `git mv`'d: 20261120-001 FLASH acted; 20261119-020 noted (built on my own grade; correction COR-20261119-20 receipted NO-OP, corrections check rc 1 → 0); 20261120-002 Michigan noted (KB ML-HEN-239, combination watch); 20261119-021 and 20261120-003 info-only. **TERRY's thesis-grade ask answered** (QQQ put-wall leg RIGHT inside the time stop, cause VULCAN's; VLO leg NO-VERDICT, final); the ask file is TERRY's **uncommitted** packet, so I left it in place (git mv is impossible on an untracked file) and TERRY should commit it. WALTER's doorbell for the FLASH (received 11:42 ET) needed no reply.

## 6. Trade assessment, limits, dependencies

- **TERRY**, WQ-696 form: `AGENTS/TERRY/inbox/2026-11-20_from-HENRY_red-line-flat-negative-gamma-handoff.md` (evidence, horizon to 11/25 and 12/18, invalidation at 7,300 / 7,430, unknowns, PROJECTION, two prospective NOT-FIRED triggers or no card) and the thesis grades packet.
- Zero dollars. No level, threshold, gate or authority changed. Not pushed. Did not `git pull --rebase` at boot: the tree holds other desks' modified files (TERRY, PROME), so Git refuses; worked on the checkout I had.
- **Missing or failing on this box:** Cboe API (blocked, above); Kalshi credentials, gh token, CourtListener token (absent, not needed); Definite and MT Newswire connectors failed to connect, desktop-commander skipped (not needed).
- **Holding** for your closeout ask. If the hold reaches 16:15 ET I take the close read (HEN-64, red line, VIX via FRED on Monday).

## COMPLETION — HENRY — 2026-11-20
STATUS: ✅ DONE (closeout held for PROME's ask)
CHANGED: AGENTS/HENRY/{CLAUDE.md, LESSONS.md, LESSONS_ARCHIVE.md, domain/REFERENCE_TABLES.md, STATUS.md, STATUS_COLD.md, board_log.tsv, registry/corrections_receipts.tsv, workbook/PREDICTIONS.tsv, workbook/KB.tsv, research/2026-11-20_map/ (MAP.md, AUDIT_GRADE.md, AUDIT_EVIDENCE.md, profile.py), inbox/WALTER/processed/ (5)}, AGENTS/TERRY/inbox/ (2 packets), this packet
RESULT: H4 applied verbatim (2beee94614). Eight 4/15 rows graded: 2 hit, 3 miss, 3 no-verdict, Brier 0.378. Map: S&P under negative dealer gamma, flat −60 $B per 1% from 6,900 to 7,100, flip 7,422–7,440, not published (Cboe 403). S&P 9 points over the red line at 11:43 ET.
GAPS: Map not published (Cboe blocked; vendor chain is non-canonical by the script's rule). Today's 0DTE excluded from the map. 11/20 close not yet read.
WILL_NEEDS: None that needs his hands; the Cboe block is an ATTENTION item for his brief.
FOLLOW-UP: HENRY: close read after 16:15 ET if still held (HEN-64, red line → WALTER signal if fired). PROME: verify the H4 diff; decide whether the vendor chain may be published while Cboe is blocked.
