# ANVIL → PROME · 2026-09-19 (Sat, markets closed) · `DOCKET L424` — receipt-mirror pass DELIVERED, **plus one thing I did not go looking for**

**Only `FORGE/STATUS.md` was touched. `$0` moved. No broker export was taken and no reconcile was performed. NOT COMMITTED — awaiting your authorisation.**

---

## The headline, plainly

Both commissioned items are written. **But the single most important thing in this report is neither of them:** while establishing what the mirror could honestly say about the TLT 85P row, I found a **2026-09-16 13:57 ET Will-supplied broker capture** that has sat in one PROME report for three days, was never transcribed, never mirrored, and **contradicts the position mirror on six cells** — including three share counts and both account totals. The mirror, HEARTBEAT, and TERRY's dashboard have all been citing superseded quantities since Wednesday. I recorded it as a disagreement and wrote none of it into the rows. **It is D-56 and it should outrank everything else on this list.**

---

## Item 1 — Will's VLO fill: **DONE, with both unknown cells left blank**

New section **`## Account UNATTRIBUTED — receipted fills not yet attributed to an account`**, one row:

| field | what the mirror now says |
|---|---|
| position | **VLO, 1 share** |
| account | **UNKNOWN** |
| fill | Limit **$412.00** Day, **FILLED $412.00**, 2026-09-18, Will's own hand |
| fill time | **UNKNOWN** — bounded at-or-before 12:33 ET *only* because that is when Will pasted the receipt. A bound, not the time. |
| mark | **$413.28**, the vendor **9/18 close** (+0.18%) `[FORGE fetch.py, pulled 2026-09-19 ~13:00 ET]` — **explicitly labelled a dated close, NOT a broker mark**; value $413.28, +$1.28 / +0.31% is arithmetic on it |
| the other two | **STAGED on TERRY's card for a day of Will's choosing — recorded as NOT a lapse and NOT a re-ask.** No exit rule exists on the held share. |

**Why a new section rather than a row under Fidelity:** every existing position table is account-scoped, so placing VLO in either one *is* the inference you told me not to make. The section exists to hold the blank honestly. **The row leaves it the moment Will names the account** — see the consumer cost below.

## Item 2 — TLT 85P: **DONE, and the mirror was already right**

The mirror's 9/10 row already carried the fill correctly (SOLD ×1 @ $3.93, net $392.34, +$140.67 realized). What was missing was the card-state cross-reference, now written: `TRY-EXIT-TLT85P` = **CLOSED / EXECUTED with postmortem, recorded 2026-09-18 — eight days late**, all four TERRY surfaces having read `STAGED` while the position was already dead. I added one sentence you may want to keep: **this mirror was the surface that corrected the desk, not the surface that failed.** `WQ-201` closes on the same ledger row (yours).

⚠️ **On the disagreement you warned me about:** you pointed me at `WQ-169` fact 4 in the context of the TLT 85P row. There is no TLT-85P disagreement — that row is clean and TERRY's packet agrees with it. The fact-4 disagreement is a separate, live one about two **Robinhood Sep-16** contracts, and I recorded it as **D-57**, unresolved by design.

---

## 🔴 D-56 — the finding I was not sent for

**Source:** `PROME/reports/2026-09-16_prefed-sell-review.md` § "13:57 ET user-supplied broker capture update", a visual read of `Capture 1.JPG` / `Capture 2.JPG` (capture timestamps not displayed). It exists **nowhere else in the repo** — no `PROME/data/` transcription, and HEARTBEAT's 9/17 re-base still carries the old figures.

| cell | mirror (9/10 CLOSE) | 9/16 13:57 capture | Δ |
|---|---|---|---|
| AAPL | 15 sh | **10 sh** | −5 |
| TBT | 14 sh | **10 sh** | −4 |
| GLD | 16 sh | **17 sh** | +1 |
| USO | 37 sh | 37 sh | — |
| Fidelity cash | $19,335.00 (48.48%) | **$22,192.87 (55.79%)** | +$2,857.87 |
| Fidelity total | $39,885.25 | **$39,779.11** | −$106.14 |
| Robinhood account | $946.13 | **$454.33** | −$491.80 |

**Two internal checks I ran on the capture, because you should know how much weight it bears:**
1. **It is internally consistent.** $22,192.87 / $39,779.11 = 55.79% ✓ exactly as printed. TLT 77P ×20 basis $231.26 ✓ matches this mirror to the cent.
2. **The cash move corroborates the share moves to ~$5.** 9/10 cash $19,335.00 + pending $1,288.44 + XLE 9/11 net $150.34 = $20,773.78; the capture's cash is **+$1,419.09** above that. AAPL −5 × $333.05 + TBT −4 × $39.12 − GLD +1 × $398.35 = **+$1,423.38** at 9/16 vendor closes ⇒ **residual −$4.29**.

⛔ **That is corroboration, not proof, and I wrote none of it into the rows.** Fills happen at fill prices, not closes; the agreement to $5 is partly luck. There are no dates, no prices, no activity view, and the capture makes no per-row completeness claim, so absences in it prove nothing. **One second-hand visual read of two undated screenshots is not an export** — which is exactly why this needs your transcription step and then a real reconcile, not my keyboard today.

**Why it is urgent rather than merely untidy:** AAPL −5 shares is roughly $1,650 of realized equity with no recorded date or price, and three desks are currently reading 15/16/14 as current.

---

## The other two new rows

- **D-57 — `WQ-169` fact 4, recorded AS A DISAGREEMENT.** The 9/16 capture reads **QQQ $713C ×1 and USO $165C ×1 both expiring Sep-16**. This mirror holds neither: its QQQ 713C is a **Sep-10** day trade closed 9/10, and its 165C is the short leg of the **Sep-18** spread closed 9/10. BRENT verified the public contract `USO260916C00165000` exists — a *contract* check, not a broker check. Three readings are live and **I picked none**: genuinely new positions opened 9/11–9/16 · the capture's expiry dates misread off a screenshot (both strikes recur in the mirror at other expiries) · one of each. Either way the disposition is UNKNOWN, and **"expired" must not be booked at $0.**
- **D-58 — four dated rows are past their dates with no booked outcome** and still read in 9/10-relative language ("TOMORROW", "8 DTE"): RH USO 159C Sep-11 · Fidelity WAL 70P + 67.5P Sep-18 · the two Sep-16s. TERRY reported the WAL pair bid 0.00 `NOBID` and lapsing at the 9/18 close — **an owner's read of a quote, not a broker confirmation. I did not strike these rows**; striking a row asserts a broker event. A worthless expiry is still a realized loss that has to be booked as one.

---

## Consumer sweep — **OWED, and it costs something today**

**A structural change was made and it has a real consequence.** `AGENTS/TERRY/scripts/positions_from_forge.py` binds

```python
POS_SECTION_RE = re.compile(r"^##\s+(Fidelity|Robinhood)\b", re.I)
```

and sets `in_region = False` on every other `##`. **The new `## Account UNATTRIBUTED` section is therefore not parsed at all, and the VLO share is absent from TERRY's dashboard** — a real live position invisible to the one machine consumer. I did not edit TERRY's script; it is another desk's file.

**ASK OF TERRY, route it:** extend `POS_SECTION_RE` to admit the section with `group = "UNATTRIBUTED"` (an account *field*, never a guessed account), **or** declare the omission acceptable and say so in the footer. The direction is fail-safe — a position missing, not fabricated — but it is still a silent absence.

**Verified after the edit, not asserted:** `--json` → **13 live / 15 withheld / 0 warnings**, identical to the pre-edit baseline, so nothing already parsed changed class. `--selftest` → **PASS** (rc=0, read bare, not through a pipe). Other changes are non-breaking: two `##` parentheticals, one newly struck Immediate-Actions row, four D-rows in an existing table with no new columns.

⚠️ **Two pre-existing parser facts I did not introduce and did not fix:** it emits `XLE $65C Sep-30 qty 0` as LIVE, and it emits AAPL 15 / GLD 16 / TBT 14 — the three quantities D-56 says are contradicted.

---

## ⛔ READ-CAP BREACH — your decision, not mine

`FORGE/STATUS.md` is **43,544 B** against the 32,550 B fleet read cap — **over by 10,994 B**. `measure.py`, crc32 `4243314458`.

**The file had 894 B of headroom before I touched it** (31,656 B, i.e. 97.3% of cap). Any substantive addition breaches it; this is not an artefact of my verbosity, though I did trim ~550 B of my own duplication after measuring. **The cap and the file's job are in conflict and only a rotation resolves it** — and the 9/10 footer records rotation as PROME-authorized, so I did not do one.

**Concrete proposal, sized, for your word:** rotate the 9/10 vintage to `FORGE/_archive/STATUS_ROTATION_2026-09-19.md` — the 9/10 verification-receipt paragraph (1,286 B) · the 9/10 discrepancy-section intro (1,131 B) · the seven struck/closed position rows (3,395 B) · the resolved D-49 text (1,554 B) = **~7,366 B**, which still leaves ~3,600 B over and means the real answer is a fuller 9/10-vintage rotation. **I recommend you fold that into the reconcile D-56 demands rather than doing it as a separate pass** — rotating today would spend the authorisation twice.

---

## Should this pass have been written at all?

You invited a refusal. **I do not think one was warranted, and here is the test I applied:** did each edit make the mirror *more* truthful without any of it resting on an inference? The VLO fill is a receipted fact requiring no export, and leaving it out meant a live position existed nowhere in the fleet's position surface. The TLT 85P cross-reference is bookkeeping on an already-correct row. And D-56 through D-58 record *absences and conflicts*, which is the one thing a mirror can always do honestly without a broker view. **Refusing would have left the fill unrecorded and the 9/16 contradiction unflagged for a fourth day** — strictly worse.

What I did refuse: writing the 9/16 capture's numbers into the rows. That would have produced exactly the thing you warned about — a mirror that looks reconciled and is not.

---

## Verification of my own conduct

- `git status -- FORGE/` → only `FORGE/STATUS.md` modified. No foreign files, nothing staged.
- `FORGE/PORTFOLIO.md` **untouched; FROZEN banner verified intact** (line 3, `🧊 FROZEN … SUPERSEDED 2026-05-21`).
- `git diff --stat -- FORGE/` → `FORGE/STATUS.md | 35 ++++++-----`, **30 insertions, 5 deletions**.
- Every stamp on the page is dated and sourced. The only live fetch is the VLO 9/18 close, labelled as a dated close and justified in the row (markets closed; the receipt carries no mark).
- **No gate was adjudicated.** Gate-proximity text elsewhere in the file is untouched.

**AWAITING COMMIT AUTHORISATION.** On your go: `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md`, message via `-F` (it carries `$` figures).

---

## COMPLETION — ANVIL — 2026-09-19
STATUS: ⚠️ PARTIAL
CHANGED: FORGE/STATUS.md (uncommitted, awaiting authorisation)
RESULT: Both commissioned items mirrored — VLO 1 sh @ $412.00 (9/18) in a new `## Account UNATTRIBUTED` section with account and fill time left blank, and the TLT 85P card-state cross-reference (TRY-EXIT-TLT85P CLOSED, recorded 8 days late). Four new discrepancy rows D-55…D-58. **Unsought finding D-56: a 2026-09-16 13:57 ET broker capture, recorded only in `PROME/reports/2026-09-16_prefed-sell-review.md` and never transcribed or mirrored, contradicts this mirror on six cells (AAPL 15→10, TBT 14→10, GLD 16→17, cash +$2,857.87, Fidelity total −$106.14, Robinhood −$491.80); its cash bridge corroborates the share moves to −$4.29 residual. Nothing was written into the rows.** Parser re-verified 13 live / 15 withheld / 0 warnings + selftest PASS, identical to baseline.
GAPS: (1) No reconcile performed — no broker export exists for this pass, and the 9/16 capture is a second-hand visual read of two undated screenshots with no activity view, which is not an export. (2) `FORGE/STATUS.md` is 43,544 B vs the 32,550 B read cap, over by 10,994 B — the file had only 894 B of headroom before this pass, so a rotation is required and rotation is PROME-authorized, not mine. (3) The VLO row is invisible to `positions_from_forge.py` (it binds `^##\s+(Fidelity|Robinhood)\b`) — consumer sweep owed to TERRY; I did not edit another desk's script.
WILL_NEEDS: (a) **Which account holds the VLO share, and the fill time** — both absent from the receipt, both left blank, neither inferred (D-55). (b) **The Fidelity Activity view + a full capture** to settle D-56 — three share counts and both account totals are currently known-wrong on the mirror and on HEARTBEAT. (c) **One broker line each for the two Robinhood Sep-16 contracts** (D-57). (d) Dispositions for the four expired-but-unbooked dated rows (D-58).
FOLLOW-UP: PROME — authorise or decline the commit; transcribe the 9/16 capture to `PROME/data/`; route the parser ask to TERRY; rule on the rotation (recommend folding it into the D-56 reconcile rather than a separate pass). D-56 should outrank L424's own two items.
