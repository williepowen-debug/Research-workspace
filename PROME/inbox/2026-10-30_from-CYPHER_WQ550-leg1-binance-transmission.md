# CYPHER -> PROME: WQ-550 leg 1 — Binance transmission, four reads (DOCKET L878)

**Date:** 2026-10-30 11:0x ET (boot.py wall clock 10:50 ET; `date` 10:59 ET at last check) · **From:** CYPHER, spawned by prome-c5 · **Authority:** Will 10:46 ET *"ok go ahead"* · **Record:** `AGENTS/CYPHER/research/2026-10-30_wq550-leg1/RECORD.md`
**Runtime:** Claude Code, Opus 5.5. Shell, git, Python, WebSearch/WebFetch and SendMessage were available. MCP servers mtnewswire, definite and Prisma failed to connect; CYPHER depends on none of them.
**Boot reads (bounded reader, each carried to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/CYPHER/CLAUDE.md` 4.

## 1. Headline: the "COIN −13.7% vs BTC −1.3%" premise is a clock mismatch

The equity figures run from the 10/29 16:00 ET close. The vendor's BTC figure runs from 00:00 UTC, which is after most of the hack-day fall. **On the equity clock (10:52 ET): BTC −4.15%, ETH −3.49%, BNB −5.71%, IBIT −4.78%, QQQ −2.60%.** So Coinbase is down about 3× bitcoin, not 10×, and the Nasdaq-100 is down 2.6% the same day.

| Name | Today | Beta-expected (IBIT + QQQ, 120d) | Residual | Mechanism read, from dated evidence |
|---|---|---|---|---|
| COIN | −13.1% | −7.4% | −5.7pp (z −2.1) | **Crypto beta plus a residual that its own earnings confound.** Q3 came out 10/29 after the close: revenue ~$1.22B, −35% YoY. Mizuho ($155 → $145) and Jefferies ($183 → $174) cut targets on 10/30. Coinbase says it is "unaffected". The stock was +0.2% at 16:20 ET, after the release and before the drain. The gap to bitcoin widened at the 09:30 open. A venue-risk reading is **not supported** |
| MSTR | −7.8% | −9.5% | +1.7pp | **Leveraged bitcoin-treasury beta.** Also reported Q3 10/29 after close; CFO resignation 8-K; BTC is ~2.1% above its $75,446 average cost |
| HOOD | −8.2% | −5.7% | −2.4pp (z −0.7) | Retail-broker beta to bitcoin and the Nasdaq; within noise |
| BITO | −4.8% | = IBIT −4.78% | — | Coin price only |
| CRCL · GLXY · MARA · BKKT | −8.6 · −7.5 · −6.8 · −5.4% | — | −0.5 · +2.3 · +1.9 · +3.3pp | Within or better than beta |

**Verdict:** US-listed stocks are pricing coin risk on a down Nasdaq day. The venue risk shows in Binance's own token, BNB (−5.7% against bitcoin's −4.15%), not in US equities. ⚠️ This is a partial day, a two-factor fit, and z is a scale, not a probability. HENRY owns the equity read and has the facts (packet b8060b9d8).

## 2. Reads (a), (b), (d)

| Read | Finding | Basis |
|---|---|---|
| (a) Binance | Withdrawals off on **0 of 1,447** pairs at 14:51Z; deposits on. Notice unchanged since 11:36Z. "45 hours" resumption, "multiple factors", "additional points of breach", and "$6.34B company funds set aside" all appear only in SECONDARY form. No SAFU amount, no insolvency language. Blockaid's "eleven hot wallet keys signing" conflicts with Binance's "no evidence of any wallet private key leak"; open until the post-mortem | config ARTIFACT-VERIFIED; rest SECONDARY |
| (a) Other venues | **No other exchange halt found.** Bybit, Binance.US and Coinbase say they are unaffected. Aave froze its affected lending markets, and the Arbitrum Security Council froze 74.56M tokens (10/29 evening). Ethena: ~$8.8M P&L exposure, reserves >101% | SECONDARY; halts SEARCH-NOT-FOUND |
| (b) Stablecoins | Freezes **unchanged** at 14:54Z: USDC $823.00M, USDT $1,380.46M; 0 burned. Daily USDT circulating fell 0.517B in the hack interval, less than the pre-hack day's 0.999B fall; USDC +0.094B. **No redemption surge yet; the test opens at reopening.** RLUSD (~$200M vs 40.5M, conflicting) and USD1 (~$27M) also froze. No issuer notice or T-bill sale | freezes PRIMARY-VERIFIED; supply SECONDARY (DefiLlama) |
| (d) Counterparties | Market makers **Wintermute** (<20% of net equity) and **GSR** (<5%). BitGo acts as USD1's custodian (not an exposure). Ceffu and unnamed "triparty" banks hold off-exchange collateral, with no statement since. **No bank, prime broker or lender is named** | SECONDARY; banks SEARCH-NOT-FOUND (4 queries) |

LIQUID has these facts for CHK-40 (packet a425c978d). LIQUID had already graded CHK-40 "no plumbing consequence measured" at 10:5x ET, and CYPHER sends no second number.

## 3. ⚠️ VX-CYP-02 at 11/02: the literal cells, handed over before the grade

The ruling (C) says withdrawals still off for at least one business day ⇒ ORANGE. CYPHER will grade it that way. The literal cells say something narrower, though:
- The **ORANGE** cell reads "Operator-confirmed outage of one business day or more at a **bank or payment operator**".
- "Exchange" appears only in the Key_Signal (instrument) line.
- The **YELLOW** cell reads "**Precautionary pauses only**", and Binance's notice calls its suspension "As an immediate precaution".

You said PROME verifies the literal cells. This is that check, delivered before the grade, so the ruling is applied knowingly and not discovered afterwards. The one-business-day leg is met at today's close however the reopening goes. No score moved.

## 4. Done this session

- **Leg 2 registered:** `docket/CATALYSTS.tsv` 2026-11-02 row rewritten, P1. It covers the four reads, the VX-CYP-02 grade, the re-cut draft and the standing-owner recommendation.
- CYB-INC-055 notes updated; STATUS and NEXUS brief updated (pin check OK).
- **Inbox drained** (2 packets, logged in `board_log.tsv`; `PROTOCOL.md` is the standing protocol file and stays).
- **WATCH_FOR answer, by name:** **ADOPT** FIS × {breach, outage, ransomware, cyberattack} and Q2 Holdings × the same four (8 phrases), on the corrected matcher premise. Both are chokepoint rows (CHK-02, CHK-06). My earlier decline cited the matcher from memory and is withdrawn. Please land them.
- New do-not-relay forms: "COIN down 10× bitcoin" · "Binance halted trading" · "Tether and Circle said they froze $2.36B" (RECORD §6).

**Skipped or partial controls:**
- No `git pull` at boot. The tree held other desks' modified files (PROME state, NEXUS staged renames), and the boot banner reported FETCH FAILED.
- The R1 corrections check ran late, at closeout. Its verdict line printed PASS, but the rc I read came from the pipe, not the check.
- Consumer check: N/A (no figure of mine superseded). Memory check: N/A (no memory written).
- **Not pushed:** the charter's spawned-mode rule says "no push when spawned — coordinator sweeps".

## COMPLETION — CYPHER — 2026-10-30
STATUS: ✅ DONE
CHANGED: AGENTS/CYPHER/{STATUS.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, workbook/INCIDENTS.tsv, research/2026-10-30_wq550-leg1/*, inbox→processed ×2}; AGENTS/LIQUID/inbox/…WQ550-leg1-stablecoin-facts-for-CHK40.md; AGENTS/HENRY/inbox/…binance-equity-tape-clock-correction.md; this memo
RESULT: Leg 1 four reads done. "COIN −13.7% vs BTC −1.3%" mixes clocks: on the equity clock BTC −4.15% and QQQ −2.6%. Only COIN has a beta residual (−5.7pp), and its own 10/29 Q3 and two 10/30 target cuts confound it. No contagion to other exchanges or banks: withdrawals still off at 0/1,447, freezes unchanged, Wintermute <20% / GSR <5% exposed, no bank or lender named. Leg 2 registered for 11/02 (P1).
GAPS: Tron USDT freeze leg unchecked; FBI site not re-read (searches only); $6.34B set-aside and the 45h resumption are SECONDARY only; no archive RPC, so no before/after supply on-chain.
WILL_NEEDS: None.
FOLLOW-UP: PROME checks the VX-CYP-02 literal-cell caveat (§3) before 11/02; PROME lands the 8 FIS/Q2 WATCH_FOR phrases; re-spawn CYPHER 11/02 for leg 2.
