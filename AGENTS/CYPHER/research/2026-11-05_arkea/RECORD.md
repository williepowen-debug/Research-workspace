# CYB-INC-059 — Crédit Mutuel Arkéa: theft from the bank's own account through a provider's platform

**Session:** CYPHER, 2026-11-05, WQ-618 A (Will 13:56 ET, "yes go ahead"). Runtime Claude Code, Opus 5.5. Card SIG-W-20261105-030 (IMMEDIATE). Opened 14:0x ET.
**Stance:** OFF-WAVE single-institution incident. Not systemic on the evidence held. Shared reach is **UNKNOWN**, not absent: the bank has now said the door was a provider, and has not said which one.

## 1. What changed against the card (found at the primaries)

| Card 030 said | Primary says | Why it matters |
|---|---|---|
| "No method, actor or supplier named" | Bank, 17:30 communiqué Q2: "Les attaquants sont passés par la plateforme d'un de nos prestataires et ont ainsi atteint le Crédit Mutuel Arkéa directement." Supplier still UNNAMED | This is a vendor route on the victim's own word. The whole question of shared reach starts here |
| "Funds went into crypto on specialised platforms" | Bank Q1: other banking actors "qui leur ont ensuite **potentiellement** permis de convertir cet argent en crypto monnaie via des plateformes spécialisées". AFP's quotation dropped "potentiellement" | Crypto conversion is the bank's possibility, not its finding |
| "around €100M ($112M)" attributed to the bank | **No euro figure appears in either communiqué.** Q6 of the bank: "Nous ne confirmons pas ces informations et pouvons simplement valider l'ordre de grandeur" (of 118M euros / 133M dollars). The ~€100M is AFP ("estimation provisoire") and Reuters (11/05, "around €100 million ($112.61 million)") | See §4 |
| "Attack date not stated" | Still true of the bank. Third-party on-chain traces start Sunday 11/01 (§3) | No bank-confirmed date |
| PROME brief "12M vs $133M" | No source holds a 12M figure (board card, AFP, Reuters, communiqués all checked). Read as a dropped digit of $112M | Do not relay "12M" |

## 2. REPORTED by the victim or a prosecutor (PRIMARY-VERIFIED where marked)

| Fact | Words | Source |
|---|---|---|
| Fraudulent operations after an attack; incident "clos et aujourd'hui maîtrisé" | "victime d'une cyberattaque ayant permis la réalisation d'opérations frauduleuses" | Communiqué 1, Brest 11/04 13:00 (PDF read). PRIMARY |
| Own account used; payments went to other banks | "Les attaquants ont utilisé le compte propre de Crédit Mutuel Arkéa pour réaliser des transactions vers d'autres acteurs bancaires" | Communiqué 2, 17:30, Q1. PRIMARY |
| No customer accounts used | "Ils ne sont donc pas passés par des comptes de clients de ses fédérations ni de ses filiales" | Q1. PRIMARY, OWNER-ASSERTED as to scope |
| Provider route; not Fortuneo | Quote §1 | Q2. PRIMARY, OWNER-ASSERTED |
| Not human error at Arkéa; external and "sophisticated"; contained | "Non. Il s'agit d'une attaque sophistiquée venant de l'extérieur, qui est maintenant circonscrite." | Q4. PRIMARY, OWNER-ASSERTED. Says nothing about error at the provider |
| Origin and method still being established | "pour déterminer précisément l'origine de l'attaque et son modus operandi" | Q4. PRIMARY |
| Customer effect | "seulement entraîné une exécution différée de certaines opérations de virement"; near-all operations resumed in the morning of 11/04 | Q3. PRIMARY. App down "plusieurs heures" (franceinfo 11/04, SECONDARY). Start of the suspension not stated |
| Part of the funds blocked; recovery under way; total too early | "une partie des fonds concernés a pu être bloquée" | Q6. PRIMARY |
| Solvency statement | "absolument pas de nature à remettre en cause la santé et la solidité financière" | Q6. PRIMARY, OWNER-ASSERTED. Scale: H1 2026 net profit €230M (AFP), total assets €211.5B (bank) |
| Customer data | Bank neither says data was taken nor says it was not. Q7 explains the phishing warning as a general precaution | Q7. PRIMARY. **No denial exists** |
| Supervisors informed | ECB, French banking supervisors and prosecutors (spokesperson, Reuters 11/05); ACPR declined to comment | SECONDARY (Reuters text republished by Global Banking & Finance Review, read in full). Spokesperson declined to name the provider |
| Prosecutor | Paris cybercrime section received the complaint on the morning of Wed 11/04 and opened an investigation for "atteinte à un système de traitement automatisé de données en bande organisée", assigned to the Office anticybercriminalité | AFP quoting the parquet, Boursorama copy read in full. SECONDARY of a primary statement |
| Claim of responsibility | None at 11/04 evening | AFP |

Note on the wording of communiqué 1: two PDFs exist. One says "cyberattaque" (AFP quoted that word); a file stamped 2026-11-04_15-40-19 says "attaque" throughout, and the 17:30 title also says "attaque". INFERRED, order of the two not proven: the bank softened the word within hours. Text saved beside this file.

## 3. REPORTED by third parties, NOT confirmed by the bank

| Claim | Who | Weakness |
|---|---|---|
| >$106M left several exchange accounts on Sunday 11/01 as USDC and USDT, then +$27M to >$133M; "occurred for multiple days"; some moves after his first alert; more if OTC trades counted | ZachXBT (Telegram, via Bitcoin Magazine, Bitcoin.com, TokenPost; his post itself not read) | Pseudonymous tracer; different scope from the bank's. He named the bank overnight 11/03-04 |
| ~$108.8M USDC from Kraken, Crypto.com and OKX, 178 withdrawals to 15 wallets over ~21 hours | Bitquery (via Bitcoin.com, BeInCrypto snippet; report not read) | A search summary says it could not identify the victim (not confirmed at an article body); different scope, do not add to ZachXBT |
| ~$63M swapped to 27,553 ETH in the night of 11/01-02; later monero | Bitcoin.com | SECONDARY |
| Fiat went to mule accounts opened at trading platforms under false identities, including Crypto.com | Journalist Grégory Raymond, unnamed sources (Presse-Citron, TokenPost, Bitcoin.com) | Same reporter said Fortuneo was the entry; **the bank denied that** |
| Kraken restricted accounts and says its systems and customers were not compromised; Crypto.com blocked funds; OKX reviewing | Cryptonomist | SECONDARY; exchange statements not read |
| "High confidence" not North Korea's Lazarus | ZachXBT | Inference from laundering pattern, one analyst. Not an attribution |
| Bank said its losses are below $133M | Reuters, early 11/04 version, via Bitcoin Magazine | Consistent with ~€100M |

**Tension, recorded not resolved:** the bank says its systems identified the activity "très rapidement". The third-party on-chain trail runs from Sunday 11/01, the complaint was filed Wednesday morning 11/04, and ZachXBT complains of >$30M that could have been frozen. If the 11/01 trail is this theft, three days passed. That link is not bank-confirmed.

## 4. The figure

| Figure | Holder | Basis |
|---|---|---|
| Order of magnitude of €118M / $133M | Bank, written (Q6), "does not confirm" | PRIMARY, floor and ceiling unstated |
| ~€100M, provisional | AFP 11/04 evening; Reuters 11/05 ($112.61M at its rate), attributed to the bank | SECONDARY; not in either communiqué. A third bank statement may exist; none is on the bank's site as read 14:0x ET |
| >$133M | ZachXBT | Third party |
| ~$108.8M | Bitquery | Third party, narrower scope |

Carry as: **"about €100M on the bank's provisional word, final figure not given, gross of what is blocked."** Net loss UNKNOWN. Never "12M". Never "$133M confirmed".

## 5. Will's question: shared software, payment rail, vendor reach to other banks

**Answer at 14:1x ET 11/05: not established in either direction. One real lead (a vendor), no evidence of a second victim, no evidence the rail itself was attacked.**

| Channel | REPORTED | INFERRED (desk, not a finding) | UNKNOWN (gates the answer) |
|---|---|---|---|
| **Vendor / shared software** | Provider's platform was the route (bank). Provider unnamed, nature of service unstated, spokesperson declined | To move a bank's OWN funds, the platform must have held, or led to, the power to instruct payments on a proprietary account. That points away from retail banking channels and toward treasury, payment-operations or connectivity services. This is a class, not a name, and the bank has not said it | Who the provider is. What it supplies. Whether the provider itself was compromised or only its access to Arkéa was abused. Whether it serves other banks |
| **Second bank hit** | None named anywhere. No ACPR, ECB, Banque de France, CERT-FR or EBA alert found. CERT-FR alert list (read 14:0x) has no banking-product item | Silence is weak: supervisor notices are not public, and Arkéa itself stayed silent for ~3 days on the third-party timeline | Whether the provider's other clients have been told |
| **Payment rail** | "transactions vers d'autres acteurs bancaires". Rail not named. No statement from SWIFT, STET, EBA Clearing, TARGET or Banque de France. Search found no report tying it to SWIFT | The rail was used, not necessarily attacked (the Bangladesh Bank 2016 shape: valid messages sent from a compromised participant endpoint, CHK-27). A Sunday 11/01 exchange withdrawal does not date the wire: fiat could have landed earlier | Which rail. Whether it was SEPA, instant, T2 or correspondent. Which banks received the money |
| **Reverse reach: Arkéa as a supplier** | Arkéa Banking Services sells white-label banking and payments on "la plateforme technique du Crédit Mutuel Arkéa" and gives clients access to clearing systems (own site, read 14:0x). Monext remains a listed subsidiary (bank boilerplate). Bank's "no client accounts" wording covers "ses fédérations" and "ses filiales" | Institutions that run on Arkéa's platform are the nearest other banks. The bank's sentence does not name them | Whether any partner institution saw delays or checks. One search found no such report (SEARCH-NOT-FOUND, weak) |
| **US-dollar reach** | No US bank or Fed-rail link in any source. Exchanges named are third-party claims and Kraken denies a breach of its own | Stablecoins were the exit tool, not the target. WQ-589 wake bar not met (not a venue or issuer hack) | Whether any USD correspondent leg existed |

**What would establish shared reach, by named instrument:**

| # | Observable | Where it would appear | Reads as |
|---|---|---|---|
| 1 | Provider named by the bank, prosecutor or a primary filing | cm-arkea.com press page; parquet de Paris via AFP; provider's own notice | Then read its client base: the count of banks on that platform IS the reach |
| 2 | Provider's own statement: its platform compromised vs one client's access abused | Provider newsroom or trust page | Compromised product = shared exposure; abused access = Arkéa-only |
| 3 | A second institution reports the same route or fraud | Any bank's communiqué; EU issuer regulatory news | FIRST HARD EVIDENCE of reach |
| 4 | Supervisory alert to banks | ACPR, ECB Banking Supervision, EBA, ANSSI / CERT-FR alert | Regulator believes others are exposed. Note DORA major-incident reports are not public, so absence proves little |
| 5 | Rail operator statement | SWIFT, STET, EBA Clearing, Eurosystem TARGET | Rail-level concern; absent so far |
| 6 | CVE or vendor advisory on a treasury / payment product, or a CERT-FR alert on one | CERT-FR, CISA KEV (boot leg 7), vendor | Mechanism becomes a shared flaw; then match to CHK-27 and the map |
| 7 | Prosecutor or OFAC statement on method | AFP | Method, and whether mules or other banks are in the case |
| 8 | Rating-agency comment (Moody's, Fitch rate Arkéa; none found) or the bank's year-end accounts | Agency press; annual results | Net loss and control findings. HANS's consequence, not this desk's |

**Not systemic on this evidence.** No second bank, no rail failure, no deposit flight reported, no solvency concern on the arithmetic: ~€100M gross is about 43% of H1 2026 net profit (€230M, AFP) and about 0.05% of total assets (€211.5B, bank), before anything blocked or recovered. The base rate (0 of 5 waves, KB-CYP-001) concerns runs, failures and central-bank outages; a direct theft from a bank's own funds is a different class and not in that sample, so that prior does not speak to the vendor question. Reuters quotes a consultant calling it unprecedented in Europe: an opinion, not a measurement.

## 6. Grading

| Surface | Call | Why |
|---|---|---|
| Incident | **OPENED CYB-INC-059**, class SUPPLY-CHAIN (vendor route on the victim's word; re-class if the route proves to be something else), OFF-WAVE, CONFIRMED, PRIMARY-VERIFIED for the theft and route, figure unconfirmed | Rule 0(a), financial victim |
| Wave | OFF-WAVE. No PHP2Shell, Palo Alto or ConnectWise link in any source | A link needs evidence |
| Watch row 8 | Not an input: off-wave, under one business day on the bank's word | |
| VX-CYP-02 | Held 3. YELLOW under the old letter and the WQ-589 letter alike: a bank whose own systems were reached, suspension under one business day | Grade does not depend on which letter governs. Duration rests on the bank; start time unstated |
| VX-CYP-01 | No move from this event: its bands key on US banks | Non-US by design |
| VX-CYP-05 | Held 3. ORANGE needs a CONFIRMED poisoning or trust-chain break; a provider route with unknown mechanism is not that. **Boundary:** a poisoned update or compromised shared product at the provider would make it ORANGE | |
| FLOW | New FL-CYP-21 (vendor access to own-funds theft) CONFIRMED on this instance; FL-CYP-22 (one vendor, several banks' funds) UNTESTED | The second row is Will's question, kept visible |
| Chokepoint map | No row reached: provider unnamed. CHK-27 SWIFT Wave_Touch unchanged, rail not established | |
| Cluster watch (catalyst) | Does not count: unnamed provider, type unknown, non-US. If it proves a payment-messaging supplier it adds one | |
| Consequence | HANS (Europe), LIQUID (rail), REGINALD and GIBBS (read-across), by packet | Desk owns the event |

## 7. Do not relay

"$133M stolen" as confirmed · "12M" · "funds went into crypto" as the bank's finding · "SWIFT was hacked" · "Fortuneo breached" · "no customer data taken" (never said) · "other banks hit" · "unprecedented" as a fact · "systemic" · "North Korea" · "not North Korea" as settled · "discovered November 4" (a website's summary, not the bank's).

## 8. Reads

| Source | Route | State |
|---|---|---|
| Communiqué 1, two PDF versions; communiqué 2 | curl, cm-arkea.com, text beside this file with sha256 | PRIMARY |
| AFP (Boursorama copy) | curl | Read in full |
| Reuters 11/05 (Global Banking & Finance Review copy) | curl | Read in full |
| franceinfo 11/04, 11/05 (Luc Chagnon) | curl | Read in full |
| Silicon.fr, Solutions Numériques, Next, cyberattaque.org, Le Conseil Patrimoine | curl | Read |
| Bitcoin Magazine, Bitcoin.com, TokenPost, Cryptonomist, Presse-Citron, CryptoTicker | curl | Read |
| Arkéa Banking Services home | curl | Read |
| ACPR and Banque de France press lists; CERT-FR alerts | curl | Read 14:0x: no Arkéa statement or banking-product alert. ACPR and BdF pages carry "ark" only as substrings of site text; not a full census |
| France 24 (card's source) | curl 403; card relied on it | Not read; AFP identical text at Boursorama in French |
| Le Télégramme, Le Monde, Le Figaro, Usine Digitale, CoinDesk, The Block, BeInCrypto | Not reached (403/429 or not tried) | Paywall or block |
| swift.com | 403 | Not read |
