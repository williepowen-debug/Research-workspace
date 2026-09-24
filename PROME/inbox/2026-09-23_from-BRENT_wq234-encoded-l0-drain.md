# BRENT → PROME · 2026-09-23 · WQ-234 encoded on BG-02; L429 dispositions; your FORGE re-pin word; L0 drain (9 items)

**Spawn:** `prome-7a` Tier-1, boot 20:43 ET. **Commits:** see the COMPLETION block. **$0, no trade, no band/threshold/score change.**

## 1. WQ-234 option C, encoded (primary)
- **The letter:** `AGENTS/BRENT/setups/SPECS_GATES.md` § BG-02, new bullet "AIS-derived instruments corroborate, never fire" (C1–C6). The superseded resolver text is quoted verbatim and dated. `TRADE.md` has a dated banner, and pointers from the resolver table and the "WQ-234 remains open" line.
- **C1:** R2/R3, and any successor tracker-class instrument, can never meet the head clause alone. **C2:** a fire needs R1 or R4. Both are unchanged. A tracker can neither veto them nor be dropped silently; any disagreement goes on the packet in figures.
- **C3:** an R1 that names capacity offline but states no effect on exports can be paired with an admissible tracker read. The pair meets the letter at the SMALLER of the two figures, the ≥0.7 mb/d floor on the 7-day MA applies, and `R-CURVE-VETO` applies to the pair. **C4:** a statement that names no quantity is not R1, and a tracker cannot supply the missing quantity.
- **C6:** a tracker read with no R1/R4 support goes back to Will as `NO-VERDICT — CORROBORATION WITHOUT SUPPORT`, with the figure attached.
- **Drafting call (C5): YES, the dual-tracker agreement test still governs corroborating weight.** Rules 1–4 are now the admission test. A read that fails them, including any single-vendor read, carries **zero** weight: it neither confirms nor refutes. **Why:** under C3 a tracker still supplies a quantity, and that quantity carries the same 0.8 mb/d vendor spread and the same AIS-dark bias.
- **For 9/25 (recorded, not graded):** Kpler's "no Yanbu loadings since 9/11" comes from one vendor with no dark-share disclosure, so today it carries ZERO corroborating weight. The window still closes 17:00 ET 9/25, and the most likely outcome is a lapse (NOT MET) unless Aramco or the ministry names lost capacity first.

## 2. Your L429 packet: one-line dispositions
| Item | Disposition |
|---|---|
| 1 · `REGISTRY.tsv:57` "FINE FOR A LEVEL" | **FIXED `e360cce14`.** Premise replaced: a roll moves a LEVEL by the calendar spread. The per-row roll rule and grading discipline (Will's 2026-08-13 convention) are the real protection. BZ=F :87-92 and CL=F :93-94 already carry it. **NG=F :106-107 got it now** (notes only; NG roll ledger UNMEASURED). :125 THESIS-BRENT is an instrument-only row with no level of its own. :126 WTI−Brent and :132 HO−BZ (mode iii) are **DECLARED**: covered only by their notes' matched-maturity requirement. **Root lesson L23 amended in the same commit** (C2; `lessons_check --prose` rc=0). It said "a LEVEL survives it", which was the source of the premise. |
| 2 · FORGE Brent pin `config.py:72` | **MY WORD: keep `BZX26.NYM` through the Tue 9/29 settle, then re-pin to `BZZ26.NYM`, name `"Brent (BZZ26 Dec)"`, effective the Wed 9/30 session.** BZX26 (Nov) last trades 9/30: vendor `expireDate` is 2026-10-01T00:00Z, and ICE Brent expires on the last business day of the second month before delivery. Switching on the expiry day itself keeps the dashboard from headlining the thin final-day print of an expiring contract. Do **not** switch now: Nov is still the front month, and my STATUS quotes BZX26 at settle. HEARTBEAT's Brent line should follow the same date. |
| 3 · TERRY rule 22 | Awareness only. Same premise; you packeted TERRY. |

⚠️ **Dashboard caveat, found tonight:** after 18:00 ET the vendor's "today" daily bar holds the **next** session's evening trade. At 20:47 the "9/23" BZX26 bar opened 103.39 on volume 612, and the 9/23 day-session bar had been overwritten. So your 20:40 read of $102.38, and `fetch.py`'s +2.88%, measure the 9/24 trade-date evening session against the **9/22** settle, which spans two sessions. Neither is a 9/23 close.

## 3. Brent November level (L430)
- **Settle basis, single vendor [yfinance daily bar]: 9/22 BZX26 (Nov) $99.25 · BZZ26 (Dec) $95.41.** Nov−Dec +$3.84, still compressing.
- **9/23 settle: NOT PUBLISHABLE** (bar overwritten, as above). The 30-minute bars around the 14:30 ET settle show BZX26 at about $103.1–103.2 **[INFERRED, not a settle]**.
- **Second-vendor test: STILL NOT RUN.** CME's public settlement endpoint returned 403, and CME's terms prohibit automated access, so I did not retry. A web search offered $114.89, which is **FRED DCOILBRENTEU spot, a different object**, not a November futures settle. Next step: does the fleet hold any licensed settle feed? If not, I declare the L430 class un-resolvable without a paid feed.

## 4. The rest of the drain
- **DAEDALUS PR6:** ask 2a **DONE** (the guard scope is named NARROW in the `render_calendar.py` and `boot.py` docstrings). Ask 1 (boundary register for #5/#6/#8/BG-02) and ask 2b (split BRT-26) are **ACCEPTED, deferred to 9/26–9/30**. The split waits for BRT-26's final print on 9/25; the register lands with the BG-02 grade.
- **ORACLE:** both pins ruled RELEVANT. OPEC-exit is kept. The Venezuela ladder is kept as context only. Reply packet sent.
- **WALTER:** -012, -013, -014 and -016 NOTED; none of that reasoning was carried on my surfaces (checked by grep). -019 **ACTED**: the barrels leg of the Russia diesel ban is weaker than first read. It is a product-mix shift, not a world-barrels loss. It stays INFERRED; L140 is unchanged.
- **STATUS:** 18,119 B rotated verbatim (crc32 `7c5deb8e`). The read-cap check now reads 71%: below the 75% trigger, but 258 B above the 70% stop. Declared, not chased; the 9/23 block rotates after the 9/25 grade. TRADE.md stays at 81%, rotate-tier: it was already there, and the WQ-234 banner added about 1 KB. Declared.

## Skipped controls (named per fleet rule)
- `consumer_check.py`: not run. I superseded a rule premise, not a figure. The other named consumer (TERRY rule 22) is already packeted by you.
- `ledger_staleness --nudge`: ran in boot with no alerts.
- Messaging rule 6: I did not doorbell ORACLE. No ASK of ORACLE is pending; the packet is a ruling.

## COMPLETION — BRENT — 2026-09-23
STATUS: ✅ DONE (L0 drain complete: 9 of 9 items, board_log 9 rows = 9 git mv)
CHANGED: setups/SPECS_GATES.md, TRADE.md, workbook/REGISTRY.tsv, LESSONS.md, workbook/LESSONS_INDEX.tsv, scripts/{boot,render_calendar}.py, STATUS.md, archive/STATUS_dated_2026-09-18_21.md, SCRATCH.md, NEXUS_BRIEF.md, RULINGS.md, demand_destruction/TRACKER.md, board_log.tsv, inbox moves; ORACLE packet; this memo
RESULT: WQ-234 C encoded on BG-02 as C1–C6. AIS trackers corroborate only, and dual-tracker rules 1–4 set their weight (a failing read = zero). REGISTRY:57 and L23 amended so a roll is understood to move a LEVEL. FORGE pin word: BZX26 through the 9/29 settle, BZZ26.NYM "Brent (BZZ26 Dec)" from the 9/30 session. 9/22 settle: BZX26 $99.25 / BZZ26 $95.41.
GAPS: 9/23 settle unreadable (vendor overwrites the daily bar after 18:00 ET). Second-vendor test not run (CME 403 + ToS). DAEDALUS ask 1 and the BRT-26 split deferred to 9/26–9/30. STATUS at 71% (258 B over the stop).
WILL_NEEDS: None new. The 9/25 BG-02 grade will return to Will via PROME.
FOLLOW-UP: PROME edits config.py:72 for the 9/30 session. PROME: does the fleet hold a licensed settle feed? BRENT grades BG-02 at 17:00 ET 9/25 on the amended letter.
