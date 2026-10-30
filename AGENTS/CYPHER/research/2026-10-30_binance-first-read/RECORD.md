# Binance security incident, 2026-10-29: CYPHER first read at the primaries (DOCKET L871)

**Session:** CYPHER, spawned by PROME (prome-a9) under WQ-184 Tier 1, 2026-10-30 from 09:05 ET (boot.py wall clock). Evidence files beside this record; on-chain scripts in `scripts/` (public Ethereum RPC `ethereum-rpc.publicnode.com`, no key, read-only).
**Inputs:** PROME packet `inbox/2026-10-29_from-PROME_binance-suspected-hack-first-read-1030.md`; WALTER SIG-W-20261029-048 (IMMEDIATE) and -049 (update). Every carrier figure in those was a claim; this record says which ones the primaries now carry.

## 1. Bottom line

- **Confirmed by the victim.** Binance's own notice ("Security Incident Update (2026-10-30)", published 02:23:22Z 10/30 = 22:23 ET 10/29, updated 11:36Z) confirms a security incident with **unauthorized withdrawal transactions**, an **"estimated total impact … around $6.3B"**, **"~$3 billion frozen on-chain so far"**, withdrawals suspended, deposits normal, losses covered "from the SAFU fund and the company's funds". Basis: PRIMARY-VERIFIED (notice body read verbatim through Binance's public CMS API, `binance_notice_2026-10-30.txt`).
- **"$6.3B" is Binance's IMPACT estimate, not a measured theft, and about half of it is frozen.** Binance's two figures imply ~$3.3B not frozen (arithmetic on OWNER-ASSERTED figures). "$5B" appears in no primary; ⛔ do not relay "$5B hack" or "$6.3B stolen".
- **The stablecoin freezes are on-chain fact.** On Ethereum, Tether blacklisted the main attacker address 37 minutes after the first drain transaction and Circle 41 minutes after. Attacker-side balances frozen on Ethereum now: **USDT $1,350.46M traced + $30.00M probable; USDC $823.00M traced** (PRIMARY-VERIFIED from the issuers' own contract events and balances, 13:09Z).
- **Withdrawals are fully off.** Binance's public network config at 13:07Z: withdrawals disabled on **0 of 1,447** coin-network pairs (all off); deposits enabled on 1,049. Binance gives no resumption time in its notice; CEO Teng "on track to resume withdrawals in 45 hours" is SECONDARY (Decrypt).
- **No bank, core vendor or CHOKEPOINTS supplier is a victim. Not a WAVE-2026-10 (PHP2Shell) event.** No escalation row fires. Crypto exchange hack = the charter's NO-OWNER class (exclusions register): flag PROME; facts to LIQUID because stablecoin issuers are involved.

## 2. Incident timeline (UTC; ET = UTC-4)

| Time (UTC) | Event | Basis |
|---|---|---|
| 10/29 15:59:11 | Initiator 0x7C86…5CA0 (funded via Tornado Cash per press) creates a contract later used as the EIP-7702 delegation target | SECONDARY (dev.to on-chain write-up); not traced by CYPHER |
| 10/29 20:24:23 | Block 26300770: tx 0x53bd38…e2f3 from the initiator to Binance 14 (0x28C6…1d60, value 0); in the same block Binance 14 sends **1,615,409,499 USDT** to 0x5227f603…2f8c ("Binance Hot Wallet Exploiter 2" on Etherscan) | PRIMARY-VERIFIED (tx and USDT Transfer logs read by CYPHER) |
| 10/29 20:24–21:00 | Further inflows to 0x5227: 55,739,800 USDT from 0xdfd5…963d (Binance 16 per press); 3,917,640 and 200,397,772 USDT from Binance 14; **823,000,000 USDC** from 0xee7a…4055 ("Binance Hot Wallet 34" per press) in two transfers (780M + 43M) | PRIMARY-VERIFIED (Transfer logs) |
| 10/29 20:31–21:00 | 0x5227 forwards 700M USDT: 500M to 0x9749…c762, 200M to 0x0ddf…697e; these split onward (swaps, 0x811f→0xaa24 175M, 0x8d53 190M) | PRIMARY-VERIFIED (Transfer logs) |
| 10/29 21:01:35 | **Tether blacklists 0x5227** (and 0x9749, by then emptied); 0x0ddf 21:01:47; 0x8d53 21:02:47; 0x7aa4 21:12:35; 0xaa24 21:14:59; 0xccbe 21:16:47; 0xb171 21:18:59 | PRIMARY-VERIFIED (USDT AddedBlackList events) |
| 10/29 21:04:59 | **Circle blacklists 0x5227** | PRIMARY-VERIFIED (USDC Blacklisted event) |
| 10/29 22:06 / 23:53 | Tether and Circle also blacklist **Binance 14 itself**; Circle blacklists Binance Hot Wallet 34 at 23:54:59 (Binance's own compromised wallets, small balances) | PRIMARY-VERIFIED |
| 10/29 22:10 | CZ (Bloomberg): Binance "may have been hacked"; CZ on X (per Fox): "User funds are safe! It does look like a hack on Binance." | SECONDARY |
| 10/29 22:33 | Binance pauses withdrawals | SECONDARY (dev.to); consistent with the notice |
| 10/30 02:23:22 | Binance notice published (one notice only in its announcement list since 10/29 08:45Z) | PRIMARY-VERIFIED |
| 10/30 11:36 | Notice updated: "deposits remain unaffected and continue to operate as normal" | PRIMARY-VERIFIED |
| 10/30 13:07 | Withdrawals off on all 1,447 coin-network pairs; Binance 14 now carries no delegation code (`eth_getCode` = `0x`), consistent with "revoked the affected address authorisation" | ARTIFACT-VERIFIED (Binance public endpoint; Ethereum RPC, latest state only) |

## 3. Figures, one row per claim, carried not reconciled

| Figure | Value | Who says it | Basis |
|---|---|---|---|
| Total impact | ~$6.3B | Binance notice | OWNER-ASSERTED (primary for what it says) |
| Frozen on-chain | ~$3B "so far" | Binance notice | OWNER-ASSERTED |
| Taken across 9 chains, 16:10–19:05 ET | $6.01B; frozen $2.80B; ~$2.9B still movable | Arkham via Decrypt 10/30 | SECONDARY |
| Earlier carrier range | $2B / $2.5B / $3.3B / $3.5B / $5.5B / $5.7B / $5.8B | PROME / WALTER carrier tables 10/29 | SECONDARY; superseded by the issuer figure |
| Tether freeze | ~$971M (when CZ posted) → >$1.567B (Ardoino on X via BleepingComputer; ~$1.57B Reuters) → 1.77B USDT (TRM via search) | issuer CEO / press | SECONDARY |
| Circle freeze | $823M (posts) / >$800M (Allaire on X via BleepingComputer) / 825M (TRM) | issuer CEO / press | SECONDARY; **$823.00M at 0x5227 PRIMARY-VERIFIED on-chain** |
| Ripple RLUSD freeze | 40.5M (TRM) vs ~$200M "potentially affected funds" (Reuters via Fox) | press | SECONDARY; conflicting |
| USDT frozen on Ethereum at attacker-linked addresses | 1,175,464,712.88 (0x5227) + 174,999,872.33 (0xaa24, traced 0x5227→0x9749→0x811f→0xaa24) = **1,350,464,585.21**; + 30,000,000.00 at 0xb171 (inflow from 0xccbe, blacklisted in the same sequence; upstream not traced) | Tether contract | PRIMARY-VERIFIED (traced) / INFERRED (0xb171) |
| USDC frozen on Ethereum at attacker address | **823,000,000.00** (0x5227) | Circle contract | PRIMARY-VERIFIED |
| USDT that left 0x5227 before the freeze and went to addresses not blacklisted in this window | ≥ ~$333M (0x9749 → 0xbeef0296 145M, 0x0000000000be 100M, 0x74ed 50M, 0x9b13 28.6M; 0x0ddf → three swap/router addresses 8.9M) | Tether Transfer logs | PRIMARY-VERIFIED transfers; INFERRED that these were swapped out of USDT |
| Gap between Ethereum USDT freeze (~$1.35–1.38B) and Tether's stated ~$1.57B+ | ~$190–420M | — | UNKNOWN: likely Tron (USDT-TRC20), **not checked** |
| USDT burned/reissued (DestroyedBlackFunds) | 0 events on Ethereum since 10/29 04:26Z | Tether contract | PRIMARY-VERIFIED: frozen, not destroyed |
| Other USDC blacklists in the window | 6 addresses, $1.56M down to $0.02M | Circle contract | link to Binance NOT established; excluded from the tally |

## 4. Cause and attribution

- **Binance:** initial investigation "suggests that the security incident may involve a compromised DevOps engineer's laptop, which allowed an attacker to gain access to a service container and submit unauthorized withdrawal transactions"; "no evidence of any wallet private key leak" (notice, PRIMARY-VERIFIED). CEO Teng later: "additional points of breach", "not a single 'one-click' action", "has not attributed responsibility to any individual" (Decrypt, SECONDARY).
- **Mechanism claim:** EIP-7702 delegation of a hot wallet to attacker code (CryptoTicker; dev.to). The on-chain shape is consistent with it (a value-0 call from the initiator to Binance 14 moving Binance 14's tokens in the same block) — INFERRED, not a Binance statement.
- **Attribution:** TRM assesses "with high confidence" North Korea's TraderTraitor (Al Jazeera, SECONDARY); @adamscochran "fits the pattern of Lazarus" (WALTER 049). **No government attribution found** (FBI search, SEARCH-NOT-FOUND 10/30 09:2x ET). For Bybit 2025 the FBI attributed within ~5 days (precedent).
- **Class:** UNCLASSIFIED (funds theft via an engineer's credentials; the desk enum has no theft class). Re-class STATE-CAMPAIGN only on a government attribution.

## 5. Chokepoint-map question: is a stablecoin rail a CHK event here?

**No CHK event on the map as built.** The map (`workbook/CHOKEPOINTS.tsv`) lists the shared suppliers US financial institutions depend on. Binance is not one, and neither Circle nor Tether is a row. No existing row's `Wave_Touch` changes.

**What the incident shows about the unmapped node.** In this incident the two USD stablecoin issuers were the **control point that worked**, not the failure point: they froze $2.17B+ of the attacker's Ethereum balances within 37–41 minutes. That is the opposite of a chokepoint failure. The failure that would matter for US finance sits at the issuer: a compromise of an issuer's mint or freeze keys, or an outage at its reserve custodian. USDC is now used as a settlement rail by US payment firms and some banks, and it is GENIUS Act-regulated. **Added CHK-40 as a class row** (USD stablecoin issuers, Type PAYMENT-NETWORK, Wave_Touch NONE-KNOWN, first signal = issuer contract events, which this session showed are machine-readable within minutes). The row registers the node. It is not a fire, and it sets no threshold.

⚠️ One contrary fact to carry. Circle's CEO said in April 2026 that Circle freezes only on a law-enforcement or court order (Drift-hack controversy; SECONDARY). Here Circle froze within 41 minutes. Either an order came that fast, or the practice has changed. Which one is UNKNOWN, and the answer matters for how reliable this control is next time.

## 6. Escalation watch, vectors and flows

- **WAVE-2026-10 rows: no change.** This incident is not PHP2Shell-rooted (Binance points to an engineer's laptop). Row 8 is wave-scoped. Row 7 needs a government attribution, and none exists.
- **VX-CYP-02 (payment and market-infrastructure availability) is held at 3, but it is a boundary case to note.** The vector's instrument text names "exchange". The ORANGE band reads "Operator-confirmed outage of one business day or more at a bank or payment operator". Binance has suspended withdrawals by its own statement, since 22:33Z 10/29 (14.5h at 13:07Z), and trading and deposits are up. Reasons for not scoring it:
  1. The charter's exclusions register puts a crypto-exchange hack in the NO-OWNER class, and none of VX-02's consequence owners (LIQUID, BOND, REGINALD) owns crypto venues.
  2. A withdrawal suspension the operator declares as a precaution is the band's YELLOW shape, not an unplanned outage.

  **Question for PROME (no score moved):** should a crypto venue count inside VX-02 at all? If withdrawals stay suspended past 11/02, a literal reading of the instrument would argue ORANGE. The desk will not re-cut its band after the fact, so the question goes up before that date.
- **FLOW:** no mechanism flips. No bank, payment system or insurer is touched.

## 7. One-line consequence read for LIQUID (facts handed over; LIQUID grades its own leg)

The freezes **do not shrink issuer reserves**. Frozen USDT and USDC are still outstanding tokens backed by reserves. Tether destroyed none of them on Ethereum (0 DestroyedBlackFunds events). So the freeze itself forces no T-bill sale. The reserve and T-bill channel opens only if one of two things happens:
- Binance or its users redeem stablecoins at scale when withdrawals reopen (Binance: ~45h, SECONDARY). That is the redemption test to watch.
- The issuers burn and reissue the frozen tokens to Binance. That would be supply-neutral.

CYPHER could not read the mint and burn flow, because the public RPC refused archive and log ranges (HTTP 403). The method is in `scripts/` for LIQUID to reuse.

## 8. Market tape (fetch.py, 2026-10-30 09:10 ET; context only, HENRY owns the read)

BTC-USD 77,165.81 (−0.78% on the day) · ETH-USD 2,227.59 (−0.97%) · BNB-USD 698.90 (+0.17%) · COIN 160.59 (−1.07%), MSTR 141.62 (−2.44%), CRCL 79.99 (−2.11%): these three are 10/29 closes, flagged stale before the open. Reuters (via Fox): BTC six-week low $77,646, BNB −8% over 24h.

## 9. Do-not-relay (adds to the desk list; each is a live carrier form)

| Form seen | Why not | Say instead |
|---|---|---|
| "$5B Binance hack" | No primary carries $5B; carriers ranged $2B–$5.8B | "Binance estimates ~$6.3B total impact, ~$3B frozen" |
| "$6.3B stolen" (Al Jazeera headline) | Binance said "impact"; ~$3B of it is frozen | as above |
| "Largest bank heist in history" (Euronews) | Binance is not a bank; no bank touched | "largest crypto-exchange theft on record if Binance's estimate holds (Bybit 2025 ~$1.5B)" |
| "CZ confirms hack" | CZ: "may have been hacked" / "does look like a hack"; Binance's notice says "security incident" | quote Binance's notice |
| "North Korea did it" | TRM's private assessment only; no government attribution found | "TRM attributes to TraderTraitor (private)" |
| "user funds lost" | Binance: losses covered by SAFU and company funds (OWNER-ASSERTED; its ability to pay is untested until withdrawals reopen) | "Binance says it will cover all losses" |

## 10. Open items (dated)

- **2026-11-02:** Binance withdrawal resumption: the network-config read again (all pairs) plus any second notice. Catalyst row registered. A suspension still in force then puts the VX-02 boundary question to PROME.
- Post-mortem and Proof of Reserves: Binance has promised both, with no date. Watch for them at the same check.
- Government attribution (FBI or other): if one comes, re-class the incident to STATE-CAMPAIGN and re-score VX-CYP-08 against its band (currently 3, YELLOW, on non-attribution warnings).
- Tron USDT freeze leg: not checked. It is the open gap in the freeze tally.
