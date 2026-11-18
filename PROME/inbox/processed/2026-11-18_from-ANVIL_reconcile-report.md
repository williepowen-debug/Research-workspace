# ANVIL → PROME: FORGE reconcile to Will's 11/18 13:21 ET Fidelity capture (awaiting commit authorization)

**From:** ANVIL (anvil-1118, Claude Code subagent, Opus 5.5), spawned by PROME prome-6e (desktop) about 13:25 ET Wed 2026-11-18. Report written 13:30 ET (`date`).
**State:** edits saved on disk. **Nothing committed, nothing staged, nothing pushed.**

## Headline

- **The Fidelity account ties to the cent:** positions $13,095.33 + cash $32,243.61 = **$45,338.94**, the displayed total, with no pending line shown. All of these tie as well: Σ Today −$1,978.05, Σ open G/L −$7,199.96 on basis $20,295.29 (−35.48%), and on every one of the 21 rows the value, last × qty and Today (change × qty) agree. I re-checked this with my own script, not PROME's.
- **Image against transcription: no disagreements.** I compared all 21 rows, all 11 cells per row, plus the cash and account-total lines. The transcription leaves out the 52-week range column on the three stock rows. That column carries no ledger data, so the omission is not a discrepancy.
- **Against the mirror at HEAD `eb49e8a9a5`** (the 11/10 reconcile `c4022901e8` plus PROME's later edits `a58dfd5ba3` and `0f73d6643d`), derived from `git show HEAD:FORGE/STATUS.md`:
  - **3 NEW:** NVDA Nov-18-2026 155P ×1, QQQ Nov-19-2026 648P ×1, QQQ Nov-18-2026 655P ×1.
  - **0 QTY CHANGE.**
  - **3 GONE:** QQQ Nov-13 668P ×2, QQQ Nov-10 670P ×2, USO Nov-11 172C ×1. Each is recorded as "absent from the 11/18 view, disposition UNSEEN". Nothing is booked for them.
  - **18 MARK ONLY:** quantity and basis checked identical on all 18. PROME's § ③ derivation is VERIFIED.
- **Account total** $44,607.15 → $45,338.94 (+$731.79). That change splits two ways:
  - by holding: positions −$694.02, cash +$372.48, pending +$1,053.33;
  - by cause: open G/L change −$540.68 plus other flows +$1,272.47.
  - The other-flows figure is DERIVED and UNVERIFIED, and its composition is not shown (new D-105). **Realized booked this pass: none.**
- **Cash bridge:** I verified PROME's figures (X = +$3,161.79; X minus the gone lines' basis = +$1,272.47). Two steps in it are inferred: that the 11/10 pending amount settled at −$1,053.33, and that each new line's displayed basis equals the cash paid for it. It is carried as D-105, DERIVED and UNVERIFIED.
- **Robinhood was not touched.** Its rows and its 11/10 vintage stand as they were. The header now says plainly that the file carries two vintages: Fidelity at 11/18 intraday, Robinhood at 11/10 intraday.

## What changed, row by row (`FORGE/STATUS.md`)

| Section | Change |
|---|---|
| Header (3 blockquote lines) | New reconcile banner. The scope banner is now "ACCOUNT SCOPE, TWO VINTAGES". The Updated money line keeps the shapes `will_brief.py` and `desk_attention.forge_vintage` read; it states the pending line is not shown, gives the snapshot identity, books no realized amount, and contains no "UNKNOWN" token. It also defines bare "chunk X" as the 11/10 rotation and "rotation 11/18 chunk A–D" as this pass's moves. |
| Longs: GLD, USO, VLO | Marks only: $342.195, $135.40, $344.41; values $6,159.51, $4,062.00, $688.82. The GLD rail text is kept beside the number: $342.195 is an intraday last, $18.515 below the "close < $360.71" line and $48.885 below "close > $391.08"; the lines read the close, not graded. USO: "+10.62% is a mark, not a gate reading". VLO −22.15%: no gate reads it. Header renamed `Mark 11/18 intraday` (the parser binds it by prefix). |
| Off-thesis | **Added** NVDA $155P Nov-18-2026, QQQ $655P Nov-18-2026, QQQ $648P Nov-19-2026, each ×1, buy UNSEEN (D-103), with their "NE"/"E" badges (D-102). The NVDA row notes it is not `IDEA-NVDA-CEOGAP-NOV12` (a Jan-15 call spread, DEAD 11/17, never entered, per TERRY's TRADE_BOOK). **Removed** the 668P, 670P and 172C rows; they are archived verbatim. USO $170C marked to $0.01 / $1.00 with an NE badge. A new italic GONE line names the three, nothing booked. The prior-terminal-records pointer now includes the 11/5→11/10 −$1.01 closes (moved to rotation 11/18 chunk B). |
| KRE (7 rows) | Marks only. Value $657.00 total. "NE" badge noted on the 66P. The 68P buy is now "permanently unsupplied (D-90, WQ-548)". |
| Other puts (7 rows) | Marks only. APO shows no badge. OZK and ZION carry "NE". WAL/ZION D-84 is noted as permanently unsupplied. The QQQ 690P pointer now says D-94 is permanently unsupplied. |
| Robinhood | **Unchanged** (byte-identical lines 91–116 of HEAD). |
| § Reconcile discrepancies | Rebuilt; detail in the ranked list below. The whole 11/10 section was moved verbatim to rotation 11/18 chunk C. |
| Immediate Actions | Rebuilt: five rows, evidence and records only. |
| Footer | The prior-mirror pointer now reads `eb49e8a9a5` plus the 11/18 rotation, and current evidence points to the 11/18 transcription (Robinhood source to the 11/10 transcription). The PARSED BY note is unchanged. |

No sell, roll, timing or expiry-reminder language was added anywhere. The only occurrence of "reminder" in the file is the existing banner that says there are none.

## Ranked discrepancy list (as in the file)

| # | Item | Urgency | Owner |
|---|---|---|---|
| **D-103** NEW | The three NEW lines' buys are not in view. Combined basis $1,735.98. Held before the 11/18 session, INFERRED from the display convention (Today ≠ total). ×1 by display and by fee cents | 🟠 | **Will** Activity 11/10→11/18; **PROME** records; card scope D-77 |
| **D-104** NEW | Three lines GONE: 668P ×2 $1,053.33, 670P ×2 $303.33, 172C ×1 $532.66 (total $1,889.32). Disposition NOT SHOWN, no hypothesis adopted, nothing booked | 🟠 | **Will** Activity; **PROME** records |
| **D-105** NEW | Cash bridge 11/10→11/18: +$1,272.47 unexplained (X = +$3,161.79), DERIVED, two inferred steps; D-101's +$3.62 now sits inside it | 🟠 | **Will** Activity; **PROME** records |
| **D-98** | Robinhood is NOT covered on 11/18. Section unchanged, 8 days old. Three RH lines carry dates before 11/18; nothing inferred | 🟠 | **Will** RH history; **PROME** |
| **D-102** | Badges updated for 11/18: "NE" on every row expiring Nov-18 to Nov-20 and on none from Nov-27. "NE" = near-expiration is a CONJECTURE that fits all three captures. The meanings of "E" (NVDA) and "M" (KRE 60P ×3) are not stated | 🟡 | **Will** if wanted; **PROME** |
| **D-89** | Working orders: no Orders panel since 11/5 | 🟡 | **Will**; **PROME** |
| **D-60** | Expiry-handling paths: no new path seen on 11/18 | 🟡 | **Will** |
| **D-100** | 650P pairing (11/5): unchanged | 🟡 | **Will**; **PROME** |
| **D-101** | +$3.62: unchanged, now inside D-105 | 🟡 | **Will**; **PROME** |
| **D-74** | Bank/credit put cluster: 41 contracts, 14 lines, basis $6,644.24, value $1,477.00 `[11/18 intraday]` | 🟡 | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | No card seen for the three NEW puts. TERRY's NVDA and QQQ cards are both call spreads (DEAD / NOT-FIRED) | 🟡 | **PROME** scope; **Will/TERRY** |
| **D-91** | No short row live | 🟡 | **PROME** L870; **TERRY** |
| **D-79** | 11/18: all 21 rows tie; the GLD 1¢ gap did not recur. Left OPEN because the rounding source is still unverified | 🟡 | **PROME** |
| **D-78** | VLO extra-share scope: unchanged | 🟡 | **Will**; **PROME/TERRY** |
| **D-83** | Clock / two vintages | 🟡 | **Will**; **PROME** |
| **D-76 · D-80 · D-84 · D-86 · D-88 · D-90 · D-94 · D-95 · D-96 · D-97** | **PERMANENTLY UNSUPPLIED (WQ-548 DECLINED, Will 11/10 15:42 ET, quoted verbatim)**. Never asked for again; realized results before 11/2 stay DERIVED. This is the exact list in the WILL_QUEUE row 548 receipt; it discharges DOCKET L1111 at the artifact | ⚪ not owed | **PROME** records only |
| **D-87 · D-85 · D-81** | Carried, PROME-owned, OPEN. D-87 cannot be tested on 11/18 (the mirror's base is 11/10) | 🟡 | **PROME** |
| **Carried 18** (D-75 … D-1) | Row kept byte-identical | 🟡 | as recorded |

**Closed on evidence this pass: none** (there is no Activity view). D-70 (CLOSED 11/11) left the table along with the archived 11/10 section.

## Rotation (task 4)

The mirror did not need a rotation to stay under the cap. I rotated anyway so the file keeps its structure, with the old discrepancy section moved out whole: **`FORGE/_archive/STATUS_ROTATION_2026-11-18.md`** (NEW, untracked). It holds four chunks of HEAD blob `861ec997c9`, byte-exact, cut on whole lines; I checked containment by script. SHA256, wc bytes and crc32 for each chunk are in the archive's header.

- **A** (lines 5–9): the 11/10 header block, 2,387 B.
- **B** (lines 43–50): the 11/10 off-thesis rows, the three GONE lines among them, plus the 11/5→11/10 terminal records (−$1.01), 1,917 B.
- **C** (lines 119–151): the whole 11/10 discrepancy section, 11,830 B.
- **D** (lines 155–162): the 11/10 Immediate Actions, 610 B.

**Byte count (`measure.py`):** `FORGE/STATUS.md` **30,131 B**, 166 lines, crc32 692755088. That is 93% of the 32,550 B budget (`read_cap_check.py`: rotate-tier, rc 0), leaving about 2.4 KB of headroom. **The next reconcile should rotate first.** The best candidates, in order:
1. the Robinhood section, if a new RH card arrives;
2. the carried-18 row, which could become a pointer;
3. the permanently-unsupplied row, which could become a one-line pointer.

## Consumer verdict (rule 3)

- **Structural changes: none.** Section names, table headers (`Mark 11/18 intraday` is a prefix-bound rename, the same pattern as every run) and row conventions are unchanged. No emphasis was added on parsed cells. **No consumer sweep is owed.**
- `python3 AGENTS/TERRY/scripts/positions_from_forge.py --selftest` → **rc 0**, SELFTEST PASS. 21 live / 7 withheld (the 7 Robinhood rows, unverified by design); no parse defects. Live values sum to $13,095.33.
- `python3 PROME/tools/will_brief.py --book-line` → rc 0:
  `Book $45,338.94 · cash 71.12% · broker export received 2026-11-18 · marks as-of 2026-11-18 intraday · 0d since receipt — not live, re-check before any fill`
- `desk_attention.holdings()` returns 28 rows and 0 errors.
- `AGENTS/BRENT/scripts/pending_receipts.py` → rc 0. It correctly surfaces D-104 as a closure CANDIDATE for BRENT's USO Nov-11 172C row. The row text says the disposition is NOT SHOWN, so the candidate cannot be misread as a closure.
- **Flags for PROME (yours to route, not mine):**
  1. BRENT's TRADE.md expiry rows for the USO Oct-30 165C remainder and USO Nov-11 172C are still "EXPIRY OUTCOME REQUIRED". The 165C outcome sits in D-90, which is now PERMANENTLY UNSUPPLIED. BRENT may want to know that the outcome will not be supplied.
  2. The footer's consumers note still lists `FORGE/position_management.tsv` `source_sha256` "withholds every mapping…". Per WQ-674 A that table is FROZEN, so the line is stale wording. I left it alone because it is in the parsed-interface note.
  3. `claim_check --check weekday FORGE/STATUS.md`: clean.

## Could not do / open questions

- **Will's carried-18 Will-owned rows** (D-66, D-69, D-63, D-64, D-61, D-59, D-45, D-55, D-54, D-18, D-20, D-37, D-17, D-1, plus D-28) all predate 11/2. Will's words, *"I dont really care about making sure we have everything documented since august"*, arguably reach them too, but the WQ-548 receipt names only the ten rows I marked. I did not extend the ruling. **That is PROME's call.**
- The new FORGE footer cites `PROME/data/2026-11-18_broker-capture-TRANSCRIPTION.md`, which is **still untracked**. It should be committed (by PROME) before or alongside the mirror.
- I made no live quote fetch: none was justified, and every mark is stamped `[11/18 intraday]`.

## `git diff --stat FORGE/`

```
 FORGE/STATUS.md | 118 ++++++++++++++++++++++++++++----------------------------
 1 file changed, 58 insertions(+), 60 deletions(-)
```

Plus one untracked new file: `FORGE/_archive/STATUS_ROTATION_2026-11-18.md`. Outside FORGE/ I touched only this report. The other untracked path, the transcription, is PROME's.

**Awaiting commit authorization.** On PROME's word the commit is `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md FORGE/_archive/STATUS_ROTATION_2026-11-18.md`, with a subject of 100 characters or fewer, a blank line, then the body. No push.

## Round 1 commit

`814245c3df`: FORGE/STATUS.md and FORGE/_archive/STATUS_ROTATION_2026-11-18.md. commit_check verify: 2 paths match the intent exactly, rc 0. Not pushed.

## Round 2: WQ-702 A labels (commit `1c83d2cfc4`)

Seven bank put lines are now labelled as Will's own trades. Committed as `1c83d2cfc4`, `FORGE/STATUS.md` only. commit_check verify: 1 path matches the intent exactly, rc 0. Not pushed.

**Ruling checked in the files:** DOCKET line 1169, read whole. `PROME/proposals/2026-11-16_wq702-703-RULED.md` § WQ-702 A records Will's word in PROME's chat at 2026-11-16 23:09 ET, verbatim *"702 A  703 a"*. Its table of seven lines and desks matches the brief.

**The phrase**, the same on every row: `Will's own trade, no desk card; thesis desk <NAME> for information only (WQ-702 A).`

| Line | Account | Desk named | Cell change |
|---|---|---|---|
| WAL $70P Dec-18-2026 ×2 | Fidelity, on the 11/18 view | WAL | "ownership/card/approval UNKNOWN (D-74)" replaced by the phrase |
| ZION $62.5P Nov-20-2026 ×2 | Fidelity, on the 11/18 view | REGINALD | same replacement |
| VLY $12P Dec-18-2026 ×1 | Fidelity, on the 11/18 view | REGINALD | "Card/owner UNKNOWN (D-74)" replaced by the phrase |
| FLG $10P Mar-19-2027 ×1 | Fidelity, on the 11/18 view | FLG | same replacement |
| KRE $71.5P Nov-13-2026 ×2 | Robinhood, not covered on 11/18 | REGINALD | phrase appended to the Note cell |
| WAL $70P Nov-20-2026 ×1 | Robinhood, not covered on 11/18 | WAL | phrase appended to the Note cell |
| KRE $25P 1/15/2027 ×1 | Robinhood, not covered on 11/18 | REGINALD | phrase appended to the Note cell |

On the three Robinhood rows no other cell changed. The 11/10 vintage and the Robinhood banner are untouched, and nothing was added about whether those lines are still open. No card, plan, reminder or duty for any named desk was written.

**Flags closed or narrowed, on the letter of the ruling:**
- **D-74 NARROWED.** VLY 12P, FLG 10P, the Fidelity WAL 70P ×2 and ZION 62.5P ×2 leave its UNKNOWN list, which now reads: KRE Nov-27 68P ×10 and KRE 66P/70P owner, card and approval UNKNOWN. The rest of the row is unchanged.
- **D-77 unchanged.** It names none of the seven lines (its entries are NVDA, QQQ, USO 170C and KRE 67P). The 11/10 D-77 did not name them either. There is nothing in it for these labels to close.
- **D-54 NOT closed: please look at this one.** D-54 records that the Robinhood KRE $25P *entry price* was never recorded (cost $53.00 derived; the row is in rotation 10/08 chunk D2). It is not an owner flag, so an owner label does not answer it. The DOCKET row asks for it to be closed. I left it open because closing it would mean writing that the entry is known. Three ways it could close:
  1. Will supplies the entry.
  2. PROME rules it into the WQ-548 "since august" decline. The entry predates 7/16, so this is the same open question my round-1 report raised about the carried-18 rows.
  3. PROME reads the DOCKET wording as authority to close it anyway.
  
  That decision is PROME's.

**Other bank or credit lines with no owner stated:** I changed nothing on any of them. D-74's 14 lines are the Fidelity cluster: KRE ×7, APO, OZK, WAL 70P, WAL 65P, ZION, VLY, FLG. The ruling's seven are four of those plus three Robinhood lines, so the 14 and the 7 are counting different sets. Of the 10 Fidelity lines without a label:

| Line | What the mirror row says about owner or card |
|---|---|
| KRE $66P Nov-20 ×3 | card/owner UNKNOWN (D-74) |
| KRE $70P Nov-27 ×2 | card/owner UNKNOWN (D-74) |
| KRE $68P Nov-27 ×10 | card/owner UNKNOWN (D-74) |
| KRE $67P Nov-27 ×4 | card/owner UNKNOWN (D-76/D-77) |
| KRE $60P Dec-18 ×2 | no owner or card stated |
| KRE $60P Dec-18 ×3 (M) | no owner or card stated |
| OZK $40P Nov-20 ×4 | WQ-428 SELL card, windows passed; "Thesis ownership UNKNOWN (D-74)" |
| WAL $65P Dec-18 ×4 | WQ-429 SELL card, windows passed; "Thesis ownership UNKNOWN (D-74)" |
| KRE $65P Dec-31 ×2 | has `MGMT-KRE65P-DEC31` (a time stop); owning desk not stated on the row |
| APO $95P Dec-18 ×1 | BROCK vehicle, HOLD ruled 8/13; the one line with a desk named |

So **8 lines lack any stated owner**: the six KRE rows plus OZK and WAL 65P, which had cards but no thesis owner. KRE 65P has a card but no desk named on the row. All of Robinhood's bank lines now carry labels. Whether WQ-702 A should reach these lines is a question for Will or PROME; the ruling as written does not cover them.

**Receipts:**
- Size by `measure.py`: `FORGE/STATUS.md` 30,913 B, 166 lines, crc32 3955851491. That is 95% of the 32,550 B budget (`read_cap_check` rc 0, rotate-tier). No rotation was needed; about 1.6 KB of headroom remains, so **the next reconcile must rotate first**.
- `positions_from_forge.py --selftest`: rc 0, PASS, 21 live / 7 withheld, no parse defects.
- `will_brief.py --book-line`: rc 0, unchanged: `Book $45,338.94 · cash 71.12% · broker export received 2026-11-18 · marks as-of 2026-11-18 intraday · 0d since receipt — not live, re-check before any fill`.
- No structural change (Note-cell text only, no new emphasis on parsed cells), so no consumer sweep is owed.

**Tree state after commit:** clean in FORGE/. Two files remain untracked, both PROME's to commit: `PROME/data/2026-11-18_broker-capture-TRANSCRIPTION.md` and this report.
