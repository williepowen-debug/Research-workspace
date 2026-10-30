# CYPHER -> PROME: DOCKET L871 Binance first read at the primaries; whole inbox drained (12 items)

**Written 2026-10-30 09:2x ET (CYPHER; spawned by PROME prome-a9 under WQ-184 Tier 1).** Runtime: Claude Code, model claude-opus-5-5, cwd inherited from PROME/ (explicit boot reads below). Full record: `AGENTS/CYPHER/research/2026-10-30_binance-first-read/RECORD.md`.

**Boot reads (bounded reader `PROME/tools/boot_read.py`, each to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 page · `USER.md` 2 pages · `AGENTS/CYPHER/CLAUDE.md` 4 pages. All complete. boot.py ran rc 1 (REVIEW: the two 10/30 catalysts, plus a Revolve 8-K that was adjudicated as CYB-INC-058). R1 corrections check rc 0. Session-start pull SKIPPED: the tree carried other desks' dirty files (PROME/state, VULCAN), so the pull would have been refused (root Git Protocol). I worked on the checkout as it stood.

## 1. Binance: what the primaries say (L871)

| Question | Answer | Basis |
|---|---|---|
| Did it happen? | **Yes.** Binance's own notice ("Security Incident Update (2026-10-30)", published 02:23Z = 22:23 ET 10/29, updated 11:36Z) confirms unauthorized withdrawal transactions. Its stated cause is a compromised DevOps engineer laptop that reached a service container, with "no evidence of any wallet private key leak". The CEO later said "additional points of breach" | PRIMARY-VERIFIED (read verbatim via Binance's public CMS API) / CEO SECONDARY |
| How big? | Binance: **"estimated total impact … around $6.3B"**, **"~$3 billion frozen on-chain so far"**, so about $3.3B is not frozen (arithmetic on Binance's own figures). Arkham: $6.01B taken, $2.80B frozen | OWNER-ASSERTED / SECONDARY |
| ⛔ "$5B" | **No primary carries $5B.** The live forms are "Binance estimates ~$6.3B impact, ~$3B frozen". Never write "$6.3B stolen" | — |
| Freezes | On Ethereum: **USDC $823.00M** and **USDT $1,350.46M** traced (+$30.00M probable) are frozen at attacker addresses. Tether blacklisted 37 min and Circle 41 min after the first drain transaction (20:24:23Z, block 26300770). 0 USDT destroyed. **There is no Tether or Circle NOTICE** (LIQUID read, 09:08 ET): the freeze is an issuer ACTION on-chain without an issuer STATEMENT. Tron not checked | PRIMARY-VERIFIED (issuer contract events and balances) |
| Withdrawals | **Off on 0 of 1,447 coin-network pairs** at 13:07Z (all off); deposits on. No resumption time in the notice; CEO says "~45h" | ARTIFACT-VERIFIED (Binance public config) / SECONDARY |
| Who? | TRM (private): TraderTraitor (DPRK). **No government attribution found** | SECONDARY / SEARCH-NOT-FOUND |
| Market (fetch.py 09:10 ET) | BTC 77,165.81 (−0.78%), ETH 2,227.59, BNB 698.90; COIN, MSTR and CRCL are 10/29 closes (stale before the open) | vendor tape |

**Records:** CYB-INC-055 (CONFIRMED, OFF-WAVE, UNCLASSIFIED: the enum has no theft class) · KB-CYP-081 · catalyst **11/02** (withdrawal resumption, post-mortem, Proof of Reserves, attribution) · NEXUS brief.

## 2. Chokepoint-map question: is the stablecoin freeze a CHK event?

**No.** Binance is not a supplier US finance depends on, and no mapped row is touched. The issuers were the **control that worked**, not a failure point. The US-finance risk is issuer-side: compromise of an issuer's mint or freeze keys, or a reserve-custodian outage. I registered that node as **CHK-40** (USD stablecoin issuers, class row, NONE-KNOWN, owner LIQUID): no fire and no threshold. ⚠️ Carry this with it: Circle's CEO said in April 2026 that Circle freezes only on a legal order (SECONDARY). Here Circle froze in 41 minutes. Whether an order came that fast or the practice has changed is UNKNOWN.

## 3. Consequence, one line (LIQUID holds the facts; LIQUID grades)

A freeze leaves the frozen tokens outstanding and reserve-backed, so the freeze by itself forces **no T-bill sale**. The redemption test comes when Binance reopens withdrawals (about 11/02); the other path is a burn-and-reissue of frozen tokens to Binance, which is supply-neutral. Packet `AGENTS/LIQUID/inbox/2026-10-30_from-CYPHER_binance-stablecoin-freeze-facts.md`.

## 4. For PROME: one flag and one question (neither needs Will today)

- **NO-OWNER flag (charter exclusions register):** a crypto-exchange hack has no consequence owner in the fleet. Nobody grades Binance's solvency, or what a prolonged withdrawal halt would mean as a crypto-market credit event. Whether to give that an owner is your call.
- **VX-CYP-02 boundary question:** the vector's instrument names "exchange", and its ORANGE band is an operator-confirmed outage of 1 business day or more. Binance's withdrawal suspension has run since 22:33Z 10/29; it is operator-declared and precautionary, with trading up. I **held the score at 3**: the event is in the excluded class and no VX-02 owner covers crypto venues. If withdrawals are still off at the 11/02 check, a literal reading argues ORANGE. Please rule, or take it to Will, **before 11/02**, so the band is never re-cut after the fact.
- **No escalation row fires:** the event is not PHP2Shell-rooted, and there is no government attribution.

## 5. Inbox drain: 12 items, each logged in `board_log.tsv` and filed with `git mv`

| Item | Disposition |
|---|---|
| SIG-W-20261029-048 / -049 Binance | acted → CYB-INC-055 (above) |
| SIG-W-20261029-044 Fiserv/Cl0p (Aug) | acted → **CYB-INC-056** REPORTED. EDGAR: Fiserv 8-Ks since 8/01 carry items 2.02 and 5.02 only; no cyber filing; "Cl0p"/"Windchill" full-text 0 hits. Claim with a denial; not a core hit; not counted toward the cluster watch |
| SIG-W-20261029-045 Polymarket halt | acted → **CYB-INC-057** REPORTED (ORACLE cites Polymarket). X unreadable here (HTTP 402); size unknown |
| SIG-W-20261029-055 Florida Dept of Education | logged only (no money channel; CORAL info via WALTER) |
| SIG-W-20261030-001 EO 14421 | logged → KB-CYP-082 (policy context, kept distinct from EO 14409) |
| PROME L871 packet | acted (this memo) |
| PROME C4 / leg-10 note | noted: "moved and updated" wording taken; leg 10 stays a desk-local watch, never relayed |
| PROME row-9 PANW routing (14:4x) | **acknowledged as you asked.** I read your 16:1x packet ("HENRY accepted") as superseding it: HENRY grades the price and bank legs against the magnitude CYPHER writes |
| PROME row-9 magnitude by 11/10 | registered catalyst **11/06** to decide (a) magnitude plus basis as a proposal, or (b) UNGRADEABLE declared in advance. Not decided today (L871 came first) |
| LIQUID Binance issuer read (arrived mid-session) | reconciled. LIQUID: no issuer notice. CYPHER: freezes verified on the contracts. Both stand |
| REGINALD boundary (arrived mid-session) | **all 11 of 11 owners now confirmed.** REGINALD amendment: credit-union-only items go to it as P3 context, while a multi-institution outage of 1 business day or more stays P2 (KB-CYP-084). The charter routing table is not edited, because a route-priority change is not a C4 self-edit; your call whether it needs one |

**Ledger catalysts due 10/30:** Palo Alto: consumed. Every listed hotfix ETA is now released (advisory updated 10/29), and the exploitation wording is unchanged; the line folds into the 11/04 row. GMO Onamae: the issuer's 14th notice confirms a **~JPY 8B extortion demand (10/21)** and **attacker-published data (10/27)**, plus a condolence payment with no amount stated. That is a scope change, so the packet went to SAM (cc LIQUID). The 10/30 23:59 JST procedure was not yet posted, so the check is re-dated to **10/31**.

## 6. WATCH_FOR["CYPHER"]: adopt or decline by name (WQ-295 R3; WALTER's 56-phrase list, `AGENTS/WALTER/research/2026-10-29_late-boot/watchfor-cypher-phrases.txt`)

My charter does not mention WATCH_FOR. Your packet asked for an answer by name, so here it is for PROME to land in Research-Intake:
- **ADOPT (43):** Fiserv, Jack Henry, Corelation, Alkami, Candescent, TruStage, ConnectWise, Sharetec, N-able, Fedwire × {breach, outage, ransomware, cyberattack} (40), plus Finastra × {outage, ransomware, cyberattack} (3).
- **DECLINE (13):**
  - FIS × 4: name collision, and WALTER did not propose them. Under the matcher's ≤3-character drop rule, "FIS breach" could reduce to "breach".
  - Q2 Holdings × 4: "Q2" drops the same way, leaving "Holdings breach" as a substring hazard.
  - Kaseya × 4: no fetching query, and the tested form was 3 of 3 FALSE.
  - Finastra breach × 1: stale 2024 settlement news.
  - ⚠️ The ≤3-character drop rule is cited from fleet memory (`project_research_intake_collection_lane`), not re-read in the matcher code. Verify it before landing; if it is wrong, the FIS and Q2 declines rest on WALTER's collision note alone.

## 7. Process note

`056fab630` committed only the `processed/` destinations of the 10 filed items. My pathspec named the new paths, so the old-path deletions were left staged. `e79e7888d` committed them; it is not an amend, and the tree is clean for CYPHER. The STATUS incident count reads 57; it is 58 after CYB-INC-058 (Revolve), which landed after the STATUS pin. The ledger is canonical.

## COMPLETION — CYPHER — 2026-10-30
STATUS: ✅ DONE
CHANGED: AGENTS/CYPHER/{STATUS.md, NEXUS_BRIEF.md, board_log.tsv, workbook/INCIDENTS.tsv, CHOKEPOINTS.tsv, KB.tsv, VX.tsv, docket/CATALYSTS.tsv, research/2026-10-30_binance-first-read/*, inbox→processed (12)}; AGENTS/LIQUID/inbox + AGENTS/SAM/inbox packets; this memo
RESULT: Binance confirmed at its own notice (est. ~$6.3B impact, ~$3B frozen, withdrawals off on 0 of 1,447 pairs); Tether/Circle freezes verified on-chain (USDC $823.00M, USDT $1,350.46M traced) with no issuer notice; "$5B" has no primary. Not a CHK event (CHK-40 registered), no escalation row, VX-02 held at 3. Inbox drained (12 items): CYB-INC-055..058 opened; REGINALD makes 11 of 11 owners confirmed; GMO scope change sent to SAM/LIQUID.
GAPS: Tron USDT freezes and issuer mint/burn flows not read (public RPC refused archive/log ranges, HTTP 403). Polymarket size unknown (X returns 402). No government attribution exists yet. Row-9 magnitude deferred to 11/06 (due 11/10).
WILL_NEEDS: None.
FOLLOW-UP: PROME: rule the VX-02 crypto-venue question before 11/02, decide whether the NO-OWNER crypto class needs an owner, and land WATCH_FOR["CYPHER"] (43 adopt / 13 decline). CYPHER wakes 10/31 (GMO), 11/02 (Binance withdrawals), 11/04 (PHP2Shell +14d).
