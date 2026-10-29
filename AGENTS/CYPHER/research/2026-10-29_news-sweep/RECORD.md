# CYPHER live news sweep — 2026-10-29 (Will's ask, 12:56 ET)

**Written 2026-10-29 12:59 EDT.** 15 web searches by CYPHER (standard mode) plus SEC submissions reads (Jack Henry CIK 779152, Citizens CIK 759944) and one EDGAR full-text query. Search engines index this month thinly: several queries returned older items only. "Not found" below means not found by these searches, not "did not happen".

## New to the ledger

| ID | Event | State · basis | Why it matters |
|---|---|---|---|
| CYB-INC-048 | Jack Henry (CHK-03) 8/31 incident: ShinyHunters voice phishing into its non-production corporate environment; PII of <10 client FIs; no core or processing disruption; not material; **no 8-K** | REPORTED · SECONDARY (issuer release 403; consistent quotes in Banking Exchange, Crowdfund Insider, RBI, Nasdaq/RTTNews) | Missed by the 10/23 chokepoint build. A core vendor's non-material incident can be press-release-only, so EDGAR legs 8/9 can't see it (KB-CYP-074) |
| CYB-INC-049 | Central Bank of India: INR 13.97 crore (~$1.7M) moved via 187 transfers on 10/15-17; complaint alleges access to IFTAS's central SFMS payment-messaging server; the bank calls it an RTGS interface glitch; FIR filed; RTGS restored | REPORTED · SECONDARY | Central payment-messaging channel (the 2016 Bangladesh Bank shape at small size). Non-US: NO OWNER. Off-wave |
| CYB-INC-050 | Sharetec credit-union core: 9/15 cooling failure, 23 CUs in 14 states offline (AB), several days; one CU closed its doors | REPORTED · SECONDARY | The multi-institution, multi-day outage shape, from an accident. New CHK-36 |
| CHK-37 | Print and mail vendor class row: Citizens and Frost (Apr 2026) and Citi (Aug 2026, CYB-INC-040) customer data came through such vendors | deduction | Two large-bank incidents in one year through one vendor type that holds many banks' customer data |
| KB-CYP-075 | CB Financial Services (PA): May 2026 Item 1.05 8-K on an employee's unauthorized AI-app upload of customer data | SECONDARY | Off-wave AI-misuse datum |

## Checked, nothing new

- PHP2Shell named victims: none beyond the 10/29 re-check. Sansec says the public exploits fail on default PHP; VulnCheck disagrees (via TNW, SECONDARY).
- Kiteworks, MOVEit, GoAnywhere and Cleo: no October 2026 exploitation found (results were the 2023-2024 campaigns).
- Fiserv, FIS and Broadridge: no October incident found. A May 2026 Everest claim against Fiserv was unconfirmed (French blog, SECONDARY), so it is not ledgered.
- Insurers: only small leak-site claims (Pear vs a California broker, 10/21). Nothing with a money channel.
- Crypto: one aggregator puts October losses at $129M (Radiant, "M2"), unverified. Bitget lost ~$387M on 9/24 via a third-party security product (DPRK per its CEO). NO OWNER class; not ledgered without a primary.
- Iran banks: the hits were the June 2026 events (FALCON's theater), not October.
- Election-week CISA/FBI guidance: no 2026 item found (only the 2022 advisory).
- Scattered Spider / ShinyHunters: no October 2026 financial victim found. ShinyHunters is the Jack Henry actor (August).

## bank-software-pass

**Second pass, Will's ask 13:32 ET; written 2026-10-29 13:34 EDT.** 8 searches, 3 more verification searches, a CYPHER read of the CA AG breach list and of American Banker 8/17.

| ID | Event | State · basis | Why it matters |
|---|---|---|---|
| CYB-INC-051 / CHK-38 | **N-able N-central** (MSP remote-management tool) flaw exploited from 7/31. NYDFS 8/11: "aware of impact to a limited number of covered entities". Huntress: <10 orgs in its base | REPORTED · SECONDARY (AB 8/17; NYDFS letter unread) | **The MSP channel has carried traffic into regulated finance**, which the 10/23 read (KB-CYP-020) missed |
| CYB-INC-052 | **Sawyer Savings Bank** (NY) closed all four branches about a week from 8/3; CEO: "a vendor vulnerability"; Storm-1175 leak listing. AB links N-central; nobody confirms it | REPORTED · SECONDARY | A bank closure via a vendor route. A breach notice published by 12/31 naming an MSP route would HIT CYP-03 |
| CYB-INC-053 | **Citizens Bank**: new CA AG notice, breach 9/10/2026, reported 10/19/2026 | REPORTED · PRIMARY for the dates | Distinct from April; route unknown; letter unread |
| CHK-37 named | **Sefas Innovation** (document vendor) SFTP breach Dec 2025-Apr 2026; ~192-200k Frost customers | SECONDARY | The print/document vendor behind the Frost (and likely Citizens April) data |
| CHK-39 | **SitusAMC** (mortgage platform) breach Nov 2025; JPM, Citi, MS notified | SECONDARY | A large-bank vendor node the map lacked |
| KB-CYP-076 | 2026 base rate: ~1 confirmed bank-supplier incident a month, 3 in August | ESTIMATE | The new cluster watch would have fired in August, a real cluster that caused no systemic harm: a fire means look closer |

Not new: Marquis (2025 attack, notices Mar 2026; CHK-10), NCR Voyix 2023 costs ($47M cumulative, $37M insured), Finzly (no update since AB 10/20). Nothing found for Q2, Alkami, Candescent, Finastra, CSI or Corelation, and no October 2026 Zelle/ACH processor outage.
