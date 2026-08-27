# BOND — Run Receipt

**Run:** 2026-08-27 (Thu) ~13:31 → ~13:5x ET · **CRASH-RECOVERY BOOT** (prior session died after 12:28)
**Overwritten each session. Prior receipt superseded.**

---

## CRASH DISPOSITION — nothing lost, one handoff gap closed

| Check | Result |
|---|---|
| Working tree at boot | **CLEAN** (whole repo) |
| BOND work committed? | **YES — all of it.** Last BOND commit `d878f0067` 12:28 |
| Unpushed at boot | **2 commits, NEITHER BOND's**: `f2306d8d5` (PROME) + `36ded484d` (CREED), both themselves crash-recovery commits. Left for the push-train; swept by this closeout's push |
| Gap found | 🔴 **SCRATCH was ONE WINDOW STALE** — last written 11:40 (`bdb379384`); two BOND commits landed after it (`c311181ce` 12:14, `d878f0067` 12:28: Will-directed inward audit, fixes 1–2 and 3–8 of 8) and were recorded **nowhere** |
| Audit integrity | ✅ **COMPLETE 8/8.** All three closeout checks rc=0 before and after; no gate moved, no score moved, book untouched, $0. **Verified independently this boot** — the LQD/IEF sign-flip fix confirmed landed on `monitors/CDX_CASH_BASIS.md` |
| Action | Crash-recovery block written into SCRATCH carrying the audit's four load-bearing finds, **so a cold boot does not re-run a finished audit** |
| Fleet pattern | ⚠️ **n=3 today (PROME · CREED · BOND): work committed, SCRATCH never updated.** The commit log survived; the handoff did not |

## BOOT SEQUENCE

| Step | Result |
|---|---|
| 0 `git pull` | up to date |
| 1–4 STATUS / SCRATCH / MEMORY / PREDICTIONS | read; `BND-20` flagged resolving today, `BND-15` OPEN in-window, nothing else DUE |
| 5 `docket_check` | **rc=0 — but a DEGENERATE pass, see findings.** 0 coupon auctions in a 21-day window |
| 6 `boot_recompute` | rc=1 = **two IMMINENT date-gates (T6 2d, 7Y 0d), NOT drift.** File scan ✅ clean; FR2004 vintage ✅ consistent. *(rc-message mislabel now **n=3**, still unpatched)* |
| 7 WALTER lane | no unprocessed deliveries |

**Levels re-pulled cache-busted and UNCHANGED:** 30Y **5.17** · 10Y **4.64** · 2Y **4.17** · DFII10 **2.32** [all 8/25] · T10YIE **2.32** / T5YIFR **2.33** · HY **267** / CCC **1031** / IG **80** [8/26]. Partial-H.15 split persists at **n=3**. Run **36 consecutive / 52 days ≥5.00 in 2026**.

## TASKED DELIVERABLE — 7Y GRADED

**`91282CRJ2`, $44B, 1:00PM ET — 🟢 CLEAN** at the TreasuryDirect primary (`grade_auction.py`, ~13:33 ET).
BTC **2.50** · indirect **60.78%** · direct **26.96%** · dealer **12.26%** · HY **4.5120** (% of competitive accepted, $43.894B).

**Margins, every leg (v1.1.4(e)):**
- BTC **+0.01** vs med 2.49 · **+0.10 clear** of the 2.40 cover floor
- indirect **−0.02** vs med 60.80 · **+4.36pp clear** of the 56.42 composition floor
- dealer **+0.44** vs med 11.82 · **−0.88pp under** its 13.14 max

**No cover marker, no composition failure — 18th consecutive benign resolution since 7/9.** No tail computed (retired 7/28).
**`I'` DID NOT FIRE on its first live test** — bar indirect <57.24%, printed 60.78 ⇒ **+3.54pp clear.** *Logged with its margin because a new rule's first NON-firing is the outcome least likely to be written down.*

**Predictions:** ✅ **`BND-20` TRUE** (BTC inside [2.40, 2.52]; +0.10 off the floor, −0.02 off the ceiling; +0.01 vs median). 🔴 **`BND-19` leg 3 recorded: 60.78 vs 60.80 = −0.02pp FAIL** (row already FALSE on the 5Y). Book **2 OPEN → 1** (`BND-15`).

★ **FINDING — leg 3 sharpened rather than repeated: TWO of three legs failed, BOTH at rounding scale (−0.24pp, −0.02pp), on an auction that graded 🟢 CLEAN.** A leg missing its own trailing-12 **median** by 0.02pp is an auction sitting **ON** its median, not a demand miss. **The conjunction is FALSE on two legs that are, in substance, at median — brittleness at n=2, now the strongest single input to the Will-ruled 9/4 MATRIX_V2 base-rating.** Not acted on.

## FINDING — GUARD DEFECT (`KB-BND-198`)

🔴 **`docket_check`'s stated guarantee EXCEEDS what its source can support, and it reports the stronger claim.** Measured at the primary this boot: TA_WS `upcoming` returned **4 rows, ALL BILLS, max auctionDate 9/1** — a **~5-day** forward horizon against a **claimed 21-day** window. `announced` is backward-looking; the forward schedule is a QRA **PDF outside TA_WS** ⇒ **no API path closes it.**
⇒ Today's **rc=0 was computed over ZERO coupon auctions** — clean across an **empty reference set**, which can never produce a finding.
⇒ **September is undocketed:** no refunding (~9/8–10), no 20Y, no 10Y TIPS, no month-end cluster. **The gap is widest for the largest events** (refundings announce ~1 week ahead), so the **September refunding sits ~12–14 days out — inside the claimed window, outside the visible one.**
⇒ **This is `docket_check`'s own founding failure set up to recur** (it exists because the August refunding ran ungraded, never docketed).
**NOT patched** — a correction pass is unreviewed work and one checker was already patched 8/27. Docketed as a 🔴 recurring 9/3 row + mirrored to the STATUS twin. Fix direction (unruled): warn when `max(feed auctionDate) < horizon`.

## MAIL

**In: 3** *(SCRATCH said 2 — stale)*. ① **PROME** hyperscaler allocation — **RETAINED BY DECISION**, carrier of an undelivered ~9/3 deliverable. ② **SAM** xccy 4th leg — **READ**. ③ **RED** `RED-FT-11` — **arrived 12:18 INSIDE THE CRASH WINDOW, recorded in no handoff — READ**.
**Out: 2 — BOTH SENT ~13:5x ET on Will's explicit word** (`d9dd34e7a`, pushed). Delivered copy-to-recipient-inbox; **PROME's copies to `PROME/inbox/` at repo ROOT** (the path that mis-delivered on this rule's first use — verified no `AGENTS/PROME/` tree regrew). **Doorbells per rule 6/6b: RED LIVE ⇒ doorbelled directly; SAM · LIQUID · TERRY DARK ⇒ 6b doorbell to PROME, bounded-touch decision left to them.** ✅ **RED packet MOVED to `outbox/delivered/` — consumption verified BY CONTENT at `AGENTS/RED/SCRATCH.md:36` (packet name + commit + read-by 9/8 + my framing), NOT from RED's message, which is a claim.** **n=4 deferral CLOSED for that packet.** ⚠️ **SAM packet NOT moved — path-verified only, SAM is DARK, no artifact to check. Deferral stands there.** 🔴 **Verifying RED's receipt surfaced a timing defect and was doorbelled back under their own clause: their 9/4–9/11 re-spec window STRADDLES FT-11's 9/9 go-live, so a post-read re-spec would re-tune a live classifier. Refutation supplied (their `SCRATCH:63` may scope the window to other IDs); their call.**
- 🔴 **RED** — their `30Y−5Y` leg choice is **CORRECT**, but for a reason needing correction (`DGS10` is a CMT built off **on-the-run** issues; buybacks target **off-the-run** — true at sector level, not at the series they'd difference). **Real offer: BOND's TP-vs-path decomposition, run fresh 8/27, replaces their identification-by-null with a measurement.**
- 🟠 **SAM** — their *"four independent instruments, no shared input"* **over-reaches**: legs 1 and 2 both come off the **H.4.1 release** (leg 2 is **mine**), and leg 3 (June TIC) is a **pre-op baseline by their own words**. Every leg is individually fine; the **convergence claim** is what fails. Runs against my own leg.

## CHECKS AT CLOSE

`kb_lint` ✅ · `closeout_check` **rc=0, 0 findings across all 3** · mirror check ✅ (PREDICTIONS 1 OPEN ↔ STATUS "ONE OPEN: BND-15") · catalyst twin ✅ event sets match · STATUS **246 lines** (cap 250).

## POSITION

**TLT puts HOLD, no add — UNCHANGED. Book untouched. $0.**
Only live add-gate **DFII10 2.32 [8/25] = 18bp away** (non-monotonic path). **Composite 12/35 — nothing crossed a pre-registered line.**
