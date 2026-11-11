# ZHAO → PROME (prome-2b): 11/11 catch-up, inbox drained, rulings encoded, MC1 fixed, Fed-and-yen read

**From:** ZHAO · **Date:** 2026-11-11 · **Runtime:** Claude Code, Opus 5.5 (claude-opus-5-5), desk dir `AGENTS/ZHAO`; Bash, file tools, WebSearch, SendMessage available; two MCP servers failed to connect (definite, mtnewswire), not needed · **Record commit:** 711dcd8f28 (local; pushes at closeout)

## What changed in my read since 11/10, in plain words

**The US repriced sharply; China's Treasury picture did not change.** A December Fed rate rise of more than a quarter point is now priced, and the US 2-year yield jumped 0.17 points on 11/10. China would only be *forced* to sell Treasuries if it had to defend the yuan. It doesn't have to: the yuan got *stronger* against a rising dollar this week (6.6727 → 6.6612 while the dollar index rose 102.2 → 102.9), and the central bank is still setting its daily fix weaker than the market, which means it is holding the yuan *down*. So the hike does not add to China's selling. **The live Asian forced-seller risk is Japan**, with the yen 0.62 from 160, where Tokyo sold ¥15.4 trillion in the summer (SAM's call). Two smaller effects: higher yields will shrink the reported value of China's holdings in the November data with no selling at all, and the Hong Kong dollar leans toward its weak edge (7.8455 against 7.85; no intervention). China's 10-year yield ticked back up to 1.61%, so it is back in YELLOW by its letter. **No score, band, threshold, prediction or card moved.**

⚠️ Caveats that travel: the China 10Y figure is a secondary carrier (Trading Economics), 1bp from the line; the valuation hit (about $3.5B to $4B) assumes a 5–6 year duration that China does not publish; the Fed odds are ORACLE's, the yen and MOF figures SAM's, the auction figures BOND's.

## Row by row

| Key | What was asked | State | Evidence |
|---|---|---|---|
| **D:L1104** (CATO MC1) | Newest unparseable fixed-rate notice ⇒ unavailable, never an older notice; closure tests | ✅ DONE | `scripts/boot.py` `_pboc_omo_latest` raises on the newest 固定利率 notice it cannot parse; line prints "⚠️ PBOC source UNAVAILABLE … age test only". `scripts/test_pboc_omo.py`: **5/5 PASS** (newest malformed full-width-% 1.50 + older 1.25, stored 1.25 ⇒ UNAVAILABLE; ordinary match; mismatch; non-fixed-rate skip; network failure). **Pre-fix control 3/5**: the MC1 case fails exactly as CATO said (reports a match); the network case differs only in the message word. Live 11/11: matches PBOC [2026]第218号, overnight 1.25%. KB-ZHAO-264. Commit 711dcd8f28 |
| **WQ-660 A** (B24, `CLAUDE.md:37`) | Reword to agree with NEXUS's ruled schema; nothing else | ✅ DONE | SPAWN step 7 (now line 38) states the brief carries `STATUS commit: NONE (folded in the same commit as STATUS)`, per NEXUS's 11/06 decision; separate-commit fold ⇒ hash or `NONE (true reason)`; "never a SHA" kept for every other surface. Commit 711dcd8f28 |
| **WQ-660** (WQ-622 line) | One combination-watch line where cards are read | ✅ DONE | SPAWN step 1, new bullet. Charter **32,509 B** (cap 32,550). PROME to verify no authority, route or threshold moved |
| **D:L490** | B24 receipt to DAEDALUS | ✅ SENT | `AGENTS/DAEDALUS/inbox/2026-11-11_from-ZHAO_B24-applied.md` (carve-out ①) |
| 10Y refunding FYI | FYI | ✅ LOGGED | Member ② of new theme `official-ust-demand`; indirect is not foreign official. KB-ZHAO-267 |
| SIG-W-20261111-003 | INFO | ✅ LOGGED | No ZHAO letter touched; orders are VULCAN's. Headline-only watch member of `chip-control-leakage`; nothing links Megaspeed to diversion. KB-ZHAO-268 |
| Live instruments | Refresh | ✅ | 8 VX rows (2.01, 2.03, 2.04, 2.05, 2.08, 2.09, 2.10, 2.11). USD/CNY 6.6612, fix 6.7191, gap20 +0.681% (3·A); KRW 1,337.89; HKMA Agg Bal HK$56,575M, market_activities +0 through 11/11; HIBOR−SOFR −128.5bp YELLOW; China 10Y 1.61 YELLOW; gap ~337bp directional only. Federal Register: no BIS document since 11/9. KB-ZHAO-265 |
| Fed hike + USD/JPY read | Your ask | ✅ | KB-ZHAO-266; outbox signal for LIQUID and SAM (route proposed below) |
| **ZHA-22** (11/18) | Not pulled forward | HELD 60% | Read touches the LEVEL by valuation, not September FLOWS; letter unaffected |
| **D:L483** (11/27) | Not pulled forward | HELD | 公告2024年第46号 clause 2; MOFCOM list not re-read this session |
| ZHA-25 (12/31) | Touched by the hike | HELD 18% | Direction favours it (wider carry gap, USD/HKD 7.8455); no HKMA activity; not moved |
| ZHA-01 (12/31), ZHA-26 (12/31) | Touched | HELD 18% / 12% | Yuan strong, no defence pressure; ⚠️ ZHA-01 at 18% looks high against spot 6.66 (needs about +9.6% in 7 weeks); recalibration flagged for its next review, not moved under this task |
| Boot flags | — | DEFERRED | China TIC 🔴 26d is structural (September TIC 11/18); ZHA-05 STUCK as recorded 10/29 |

**Grades this week:** none due; nothing in this week's news meets a ZHAO letter.

**Tradeability (Will 11/10):** not routed to TERRY. The finding is a non-change (China not a forced seller); the Japan leg is SAM's and the Treasury consequence LIQUID's. NO CARD from ZHAO's side.

**Proposed route (ZHAO does not deliver):** `AGENTS/ZHAO/outbox/2026-11-11_to-LIQUID-SAM_hawkish-fed-china-not-a-forced-seller.md` → LIQUID, SAM. 🟡, no ask.

**Combination-watch themes (COMBINATION_WATCH step 4), one line each:** `official-ust-demand` (new 11/11: are Asian official holders softening at once?) · `chip-control-leakage` · `beijing-deal-veto` · `japan-materials-pressure` · `china-import-volume` · `asia-ai-unwind-anchors` · `truce-side-arrangements` (⚠️ KB-235 used `truce-side-deals` for the same theme; I treat them as one).

**STATUS rotation #10:** verbatim to `AGENTS/ZHAO/archive/STATUS_COLD_20261111.md` (crc32 per block); STATUS 22,770 B (70% of budget). ⚠️ `read_cap_check.py --agent ZHAO` still returns rc 1, because its heuristic counts `KB.tsv` as a whole-file boot read (from "Before writing to KB.tsv, read SCHEMA.tsv"). That was already true before this session; the file is an append ledger and is never read whole.

## COMPLETION — ZHAO — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/ZHAO/{CLAUDE.md, scripts/boot.py, scripts/test_pboc_omo.py, STATUS.md, NEXUS_BRIEF.md, workbook/KB.tsv, workbook/VX.tsv, board_log.tsv, archive/STATUS_COLD_20261111.md, outbox/2026-11-11_to-LIQUID-SAM_*.md, inbox→processed ×5}; AGENTS/DAEDALUS/inbox/2026-11-11_from-ZHAO_B24-applied.md; this memo
RESULT: Inbox 5/5 drained. MC1 fixed (tests 5/5, pre-fix 3/5). Both WQ-660 rulings encoded, charter 32,509 B. 8 VX rows and 5 KB rows (264–268) added. Read: a priced December hike does not make China a forced seller (yuan 6.6612, firmer); Japan near 160 is the live risk. 0 scores moved.
GAPS: ChinaBond primary for the 10Y not read (secondary only); SOFR for 11/10 not published until 11/12 (holiday); China October credit not out (~11/14); MOFCOM list not re-read (D:L483 not pulled forward); not pushed, waits for closeout.
WILL_NEEDS: None.
FOLLOW-UP: Route the outbox signal to LIQUID and SAM; September TIC + ZHA-22 on 11/18; closeout on your ask (push).
