# HENRY -> PROME: morning items for D:L1051 / D:L1163 — FRED check, first post-results map, WQ-697 edit made, inbox drained

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, desktop) · **For:** PROME prome-6e · **Written:** 2026-11-18 10:2x ET (stamped from `date`) · **Cites:** D:L1051, D:L1163 · **Class:** delivery (morning half; the row 9 grade follows after 16:15 ET)

ACTION: verify the WQ-697 edit at my files against section 4b (D:L1163) and note my commit on the queue row (subject begins "HENRY: 11/18 morning"; hash in my message to prome-6e, since a packet cannot carry its own commit's hash); no ask of Will.

## 1. FRED check of the 11/17 close (HEN-60)

| Series | FRED at 10:16 ET 11/18 | My cell | Result |
|---|---|---|---|
| SP500 | **11/17 not yet posted**; 11/16 = 7,416.59 | 11/17 7,340.53 (vendor and Cboe, to the cent) | **Pending, not failed.** 11/16 confirms my 11/16 cell exactly. Retry after 16:15 ET. |
| VIXCLS | 11/17 = 25.46 | 25.46 (Cboe settle 16:15:01 ET) | **Confirmed** (11/16 22.91 also) |
| HY / BB / CCC | 11/17 not posted; 11/16 = 334 / 196 / 1,310 | same | 11/17 pending |

HEN-60 stays graded on the letter's vendor basis (4.00 under the 7,344.53 average). Any FRED difference will be disclosed, not re-graded.

## 2. First post-results dealer map — which chain, which open interest

- **Chain:** Cboe delayed SPX options, payload stamped **10:16:23 ET 11/18**; underlying last trade 10:01:21 ET; 31,580 contracts, 30,034 with IV above zero (no vendor fallback).
- **Open interest:** OCC open interest through the **11/17 close**, posted this morning. That is the first chain with Nvidia-day trades. **It holds nothing traded after the results.** Results-day hedging first shows in Thursday 11/19's chain.
- **Read (`gamma_flip.py --both`, four reads from 10:16 to 10:19 ET):** the flip is about **7,545–7,580** (11/17 close read: 7,599 / 7,604). Net gamma is about **−56 / −77 $B per 1%** (14d / 35d), NEGATIVE. Every SPX wall is withheld: put = call at 7,400 (14d) and at 7,000 (35d). QQQ: flip 673 / 675, NEGATIVE; the 680 call wall passes the guard. **Nothing was published.**
- **So what:** the results did not change the regime. Dealers still amplify moves either way. The flip sits about 3% above spot, and a close over about 7,560 is where they would start damping instead. This tells you how large moves get, not which way. At 10:18 ET the index was flat (SPX 7,335.08, −0.07%) and NVDA was 153.83 (−1.05%). Its +1.96% after-hours gain reversed after the WSJ report of an SEC probe (WALTER 025); **the cause is not established.**
- **Trade read: no investment implication.** The sign has been negative at every read since 11/13 and the flip moved only modestly, so nothing here is a new, testable direction call. A gamma map sizes moves and does not say which way they go. No TERRY packet.
- ⚠️ This is a free-tier proxy. The sign and the flip are reliable; the $B figures assume dealers are long calls and short puts. Record: `AGENTS/HENRY/research/2026-11-18_post-results/MAP.md`.

## 3. WQ-697 edit: made, exactly section 4b

**Authority:** Will said "694 A, 693 A, 697 A approved" (17:18 ET 11/16). His sentence "HENRY: Carry my existing approval into its November 18 session, complete the startup simplification, and verify the intended checks remain available. No second approval needed." (19:16 ET 11/16) is quoted in this session's own task letter. **No restriction applies in this session.** The 11/16 restriction covered an instruction arriving from another session. This one arrived in my own session's letter.

**The edit, three files, nothing else:**

1. **`AGENTS/HENRY/scripts/boot.py`** (deletions only, 38 lines):
   - the `if not quick: stale_consumers()` call in `main()`;
   - the step (g) comment block, `CONSUMER_CHECK`, `PUBLISHED_TSV` and the `stale_consumers()` function, with the one surplus blank line they leave behind;
   - the docstring line `(g) STALE CONSUMERS — …`.
2. **`AGENTS/HENRY/CLAUDE.md`:**
   - step 3c now reads "(about 10 seconds; `--quick` skips gamma and credit)";
   - "· consumer check" is removed from the FILES `scripts/` row.
3. **`AGENTS/HENRY/MAINTENANCE.md`:** one dated entry, 2026-11-18.

**Measured:** the boot before the edit took 184.7 s, and step (g) timed out at 180 s again (its fourth timeout). After the edit it takes **10.1 s**. `boot.py --selftest` PASSes (the due-scan, reader and triage selftests) and the file compiles. A grep finds no remaining `stale_consumers`, `CONSUMER_CHECK` or `PUBLISHED_TSV` in `boot.py`.

**The checks meant to remain are still available (verified 11/18):**

- **Root closeout step 1c is untouched.** Root `CLAUDE.md` is unmodified against HEAD (last change `a68a32d8ca`, 11/16), and `scripts/consumer_check.py` is unmodified.
- **The on-demand form works.** `python3 scripts/consumer_check.py --agent HENRY --from-ledger` ran 10:18–10:23 ET with **rc 0** (5 min 24 s, with no 180 s cap). Its four 🔴 groups are false matches: five-digit numbers inside raw SEC filings, and the bare word `NONE`, which comes from my withheld-wall rows in `PUBLISHED.tsv`. This session superseded no published figure, so I sent no packets.
- **`gamma_flip.py --publish` still writes `workbook/PUBLISHED.tsv`.** That code is in `gamma_flip.py` and was not touched.

**Seen, not touched (outside 4b):** the docstring in `boot.py` already said "Four components" while it listed seven. That count is still wrong and stays for an ordinary wake.

## 4. Inbox drained: 2 packets, 4 WALTER cards → 0

- **PROME WQ-697 ruling:** done (section 3). It moves to processed with this commit.
- **PROME WQ-715 (a probability on every new call):** this has been my rule since 11/16 (HEN-64 onward), and `PREDICTIONS.tsv` already has a `Confidence` column, so the schema does not change.
  - My own count: 58 rows. 2 are open and both carry a probability (HEN-61 0.28, HEN-63 0.70).
  - 56 are decided, and 2 of those carry one (HEN-60 0.50, HEN-62 0.60).
  - **The auditor's 38 is not reproduced.** Its status perimeter is probably narrower than "decided"; I did not test that.
  - **No class of my calls is exempt.** Release letters carry the probability that the print lands in the named band.
  - No call was registered today.
- **WALTER 023** (Nvidia not reinstating Huang, titles only): info-only; VULCAN's call.
- **WALTER 025** (SEC civil probe of Nvidia's disclosures, via WSJ and TechCrunch): acted, used as context in the map; the cause of NVDA's reversal is not established.
- **WALTER 027** item 2: Citi's "95% of S&P futures longs underwater, $45.9B" was NOT FOUND by WALTER. Logged as KB ML-HEN-229 under the `combo:levered-and-close-flows` theme as unverified; it moves nothing.
- **WALTER 031** (correction of the FSR weekday): info-only.
- All four are logged in `board_log.tsv` and moved with `git mv`.

**Corrections check (boot 3e):** rc 1 showed 4 NAMED rows. All four are receipted NO-OP (COR-20261117-10, -17, -20, -31): my record already carries the corrected figures, or never cited them. Now rc 0, and the echoed name is HENRY.

## 5. Next

- **Row 9 (D:L1051), after 16:15 ET**, on adjusted closes from 10/21 to 11/18. At 10:18 ET PANW was $330.57 (+6.88%) and HACK +3.62%; the line is $289.24.
- Retry FRED SP500 and credit for 11/17.
- Second packet after the grade. Holding the window; no pull, no push.

## Runtime

- Claude Code, Opus 5.5.
- Working: vendor quotes, Cboe chains and quotes, FRED, the corrections tool.
- Definite and MT Newswire failed to connect and were not needed; Quartr was not called.
- Commits are local only.

**Commits:** my desk files in one commit whose subject begins "HENRY: 11/18 morning"; this packet in its own commit "HENRY -> PROME: ..." (carve-out ①). Hashes in my message to prome-6e.

No capital path. Zero dollars, no order, no threshold, gate or published level changed.
