# TERRY STATUS ARCHIVE — rotated 2026-10-01

🧊 FROZEN — not maintained; `STATUS.md` is canonical, do not cite rows as current.

**What:** the **2026-09-28 18:1x (WQ-329 / L535)**, **2026-09-28 10:51 (prome-7f, WQ-315)**, **2026-09-26 15:08 (prome-1d, WQ-292)** and **2026-09-25 14:12 (prome-2e)** blocks, pre-rotation `STATUS.md` lines 45–74, verbatim, contiguous, body only. **5,892 B, crc32 `af0c3dfe`** (block body, first line through last, no trailing newline).
**Why:** the 2026-10-01 write-back took STATUS to 25,866 B = 79% of the 32,550 B read budget (rotate tier; `boot.py` read-cap proximity flag, DOCKET L391). Rule 5 stops below 70% (22,785 B).
**No live state moved — each leg verified on a live surface first:**
- `MGMT-VLO-SHARE` proposal (A/B legs) → `setups/INDEX.md` row + `setups/VLO-SHARE_management-proposal_2026-09-28.md`.
- `MGMT-QQQ730P-USO159C-SEP30` → CLOSED; `setups/INDEX.md` row + card § ⑩ (2026-10-01 disposition correction).
- `MGMT-TLT82P-OCT16` / `MGMT-HBAN16P-OCT16` (Will's A/B/C by Wed 10/14 close; ITM-expiry UNKNOWN D-60; HBAN Q3 10/22 BMO) → `setups/INDEX.md` rows + both cards + `FORGE/STATUS.md` WQ-302 row.
- VLO-SCALE → TERMINAL per the 2026-09-30 08:04 STATUS block (kept) + `PROME/GATES.tsv`.
- 004 → CLOSED, card 004 2026-10-01 DISPOSITION CORRECTION.
- WQ-297 A (Will accepted the one-oil-bet concentration 9/25) → `PROME/proposals/2026-09-25_wq297-298-RULED.md` + `research/2026-09-25_Q1_book-exposure-map.md` + `setups/USO150C-KRE65P_roll-management-notes_2026-10-01.md` § A.
- Carried items: L372 → 2026-10-01 STATUS block (kept) · L391 → DONE 2026-10-01 (`f1505285c`) · SETUPS/TRADE_BOOK rotations → 2026-10-01 block · CCL `FL-CRU-10` → graded 9/30 (`options/PRINT_ENVELOPE_CRUISE_2026-09-19.md` § ⑨).
- WQ-295 watch-phrase cadence → `PROME/DOCKET.tsv` (L500 row) + `board_log.tsv` 9/25 rows; MIDAS 77P delta → `board_log.tsv`.

---

> ## ★ 2026-09-28 18:1x–18:2x ET · PROME spawn (WQ-329 / L535): **`MGMT-VLO-SHARE` proposal to Will** (`setups/VLO-SHARE_management-proposal_2026-09-28.md`): A = Nov crack settle <$90.16 · B = signed export-ban text; desk read both. 9/28 fills recorded: 004 ×15 · QQQ ×9 / USO ×2 · TLT 82P ×1 · ROLL70 GTC gone. `$0` moved.

> ## ★ CURRENT STATE — 2026-09-28 Mon 10:51–10:5x ET · PROME spawn (`prome-7f`, Tier 1, **WQ-315** — Will: *"give me a hold/sell recommendation and decision deadline for each … Recommendations only; orders remain mine. Keep my TLT hold-to-expiry ruling unchanged."*). **`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.**
> - **Carded:** `setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md` (`MGMT-QQQ730P-USO159C-SEP30`). Verdict **SELL both today, before 15:45 ET**; if held, **hard sell deadline Wed 9/30 15:00 ET**. Both lines open at the 9/25 close only (ANVIL); **UNVERIFIED since**.
> - Live (yfinance, screening, ~15-min option lag — `DIRINC` fired 10:53): QQQ $732.18 (−1.65%), 730P bid 2.18–2.23 ⇒ ×10 ≈$2,180–2,230 vs cost $2,486.63. USO $152.96 (+3.12%), 159C bid 0.55–0.58 (12–14% wide) ⇒ ×2 ≈$110–116 vs $921.33. Root rule #6: SELL is on the right side for both (a put on a red day, a call on a green day); HOLD would be the implicit re-buy. No break claimed.
> - Wed mechanics: auto-exercise ≥$0.01 ITM (VERIFIED, 9/26 card read). 10 puts ⇒ −1,000 QQQ short, which an IRA cannot hold; 2 calls ⇒ $31,800 cash vs $17,512.69. What Fidelity does and when = UNKNOWN (D-60). TLT 77P ×20 HOLD (WQ-168 ④) and KRE 60P Sep-30 LAPSE (⑥): noted, untouched.
> - Inbox drained 1/1 (REGINALD ROLL70 clause (d) CONCUR, `noted`; run 0-of-3 through 9/25). BOARD scan: 21 action-line, all logged (boot.py). SETUPS/TRADE_BOOK rotations still owed ⇒ `MGMT-` id, registered in `setups/INDEX.md`.

> ## ★ CURRENT STATE — 2026-09-26 Sat 15:08–15:14 ET · PROME spawn (`prome-1d`, Tier 1, WQ-292 RULED 15:04 ET: *"prepare the two position-management cards … preparation, not trades"*). **`$0` MOVED · NO PROPOSAL · NO GATE OR THRESHOLD MOVED.** This supersedes the WQ-292 row ("Not carded") in the 9/25 block below.
> - **Carded:** `setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md` (`MGMT-TLT82P-OCT16`) · `setups/HBAN_oct16-16P_ITM-management-card_2026-09-26.md` (`MGMT-HBAN16P-OCT16`). 9/25 close (Sat): TLT `79.32` ⇒ 82P ITM `$2.68`, bid `3.00` ⇒ ×2 `$600` vs cost `$336`. HBAN `15.64` ⇒ 16P ITM `$0.36`, bid `0.45`/ask `0.80` (56% wide) ⇒ ×2 `$90` vs `$192`. Screening marks.
> - **Named UNKNOWN on both:** Fidelity's handling of an ITM long put with no shares in an IRA. Its public pages give only auto-exercise at ≥$0.01 and a DNE deadline of 16:15 ET; the IRA-short branch is SEARCH-NOT-FOUND. One question for Will to ask Fidelity, on both cards. Decision point **Wed 10/14 close**; backstop Fri 10/16 before 16:00.
> - **HBAN 7/18 ruling:** the letter stands; its premise (dust, commission ≈ proceeds) failed ($1.30 vs ~$90). Re-rule options R-A/R-B are listed, not recommended. HBAN Q3 print is **10/22 BMO**, after expiry (HBAN IR). **TLT 82P:** DOCKET 10/1 FR2004 names it under BOND's unresolved kill rail (WQ-291 HELD).
> - Inbox drained 1/1 (BRENT F1 packet, `noted`). BOARD scan: 21 action-line, all logged. SETUPS/TRADE_BOOK rotations still owed, so the cards use `MGMT-` ids (no SETUPS row) and are registered in `setups/INDEX.md`.

> ## ★ CURRENT STATE — 2026-09-25 Fri 14:12–16:1x ET · PROME spawn (`prome-2e`, Tier 1, the post-settle re-touch owed by WQ-282/WQ-213). **`$0` MOVED · NO PROPOSAL · NO GATE MOVED OR SHAVED.** This supersedes the "Owed today ②" line in the 02:58 block below.
>
> | line | state (own pulls, vendor = screening) |
> |---|---|
> | **VLO-SCALE** (2 staged) | **9/25: NOT MET** (A ✗: VLO +1.12% green, USO −3.07% red · B ✗: `387.145` > SMA-20 ending 9/24 `380.66`). **`F1` = UNKNOWN:** ③ settle-window VWAP `$95.0014` (2-bar `$94.9990`), `$0.00` from the line. ① CME is 403-blocked; ② is not finalized. **The row is NOT terminal; it is held.** Resolver: Will reads the CME 9/25 settles for `HOX26`/`CLX26`. If `HO×42−CL < 95.00`, the row goes terminal and both staged shares stand down. Card § ⑩. |
> | **004** TLT 77P ×20 | 🔒 **SUPERSEDED — CLOSED, EXPIRED WORTHLESS 2026-09-30** (×15 held to expiry; see the 9/30 17:3x block). *9/25 history:* 16:03: `0.03/0.04` (last trade 15:21), TLT `79.32` ⇒ ~`$60–80` vs `$231.26` basis. **Card unchanged:** harvest ≥`$0.3469` is out of reach (it needs TLT ~−3%), NO ADD (WQ-280), expiry Wed 9/30. |
> | **Book concentration** | **WQ-297 A — Will ACCEPTED it in writing, 2026-09-25 14:16 ET** (`PROME/proposals/2026-09-25_wq297-298-RULED.md`). No offset card, no trim, no line's rule changes. Carried on the Q1 map. |
> | **WQ-292** (TLT Oct-16 82P ×2 + HBAN 16P ×2, ITM) | Will's ruling. Not carded. |
>
> **Inbox drained 3/3** (`board_log.tsv` 9/25 14:17 + 16:0x rows). **WQ-295:** CADENCE `WEEKLY` declared. The 8 phrases I proposed were live-tested by WALTER: 1 landed, 6 rejected, and on my word 7 replacements were adopted and `distillate inventories` dropped (memo). **MIDAS:** the 77P delta was delivered 9/11. At 14:14 ET 9/25 it was `−0.0708`, above MIDAS's `0.0504`, a moment property; packet sent.
>
> **Carried, with reason:**
> - **DOCKET L372** (cold class-fix proposal: gates with no thesis/channel condition) needs its own sitting.
> - **L391** (`boot.py` read-cap flag) is not urgent: STATUS has headroom (`read_cap_check --agent TERRY` rc=0).
> - 🔴 **SETUPS/TRADE_BOOK rotations are still owed.** `SETUPS.tsv` sat at the rotate tier, near its cap, at 16:0x 9/25, so **no SETUPS row was appended this session.** The next session rotates FIRST.
> - **CCL prints Tue 9/29:** grade `FL-CRU-10`.
