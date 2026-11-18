# CYPHER -> PROME: delivered — Equinor confirmed (IT only), NSA outage tied by the DNI to PHP-flaw patching, gaps closed, uncarded sweep, still several stories, nothing fired or moved

**From:** CYPHER (Claude Code, Opus 5.5, model ID claude-opus-5-5) · **Written:** 2026-11-17 20:10 ET · **Task:** PROME prome-7a, C9 (WQ-538), one bounded session from Will's 19:59 ET remark · **Class:** completion record (PROME/COMPLETION_SPEC.md) · $0 · `git pull --rebase` up to date at start; commits by pathspec; **no push; holding for your closeout ask.**
**Record:** `AGENTS/CYPHER/research/2026-11-17_evening-gaps-and-sweep/RECORD.md` (names live there; this packet carries counts).

**ACTION:** none required. Nothing Will-gated was touched. No score rule, level or letter changed.

## 1. Equinor (card 026) — graded at the primary

| | |
|---|---|
| **Established** | Equinor's own release (17:55Z 11/17, last modified 18:40Z): "an ongoing cyber-attack against certain IT systems"; resources mobilised "to neutralise the attack and regain full integrity"; "no indications that data has been stolen"; "The attack has not affected Equinor's operations and production"; authorities informed. CONFIRMED · PRIMARY-VERIFIED (CYB-INC-080) |
| **Not established** | Actor, method, entry point, which systems, start date, ransomware or not, any operational-technology reach. One outlet says "administrative systems" — not in Equinor's text |
| **Update since?** | **None.** Release unchanged and nothing newer on equinor.com/news at 01:01Z 11/18. NSM contact per a search summary only |
| **Rules** | VX-CYP-04 holds 3 (ORANGE needs a confirmed OT compromise; this is IT). **No HANS/BRENT packet:** supply and operations are not engaged on the evidence (your condition) |

## 2. Gaps after the 12:40 ET session

| Gap | Now |
|---|---|
| Apple (card 024) | **CONFIRMED at Apple System Status:** App Store and AppleCare outages, iCloud sign-in/mail issues, 11/17 08:15-14:00 PST by service, all resolved; Apple: "an internal update caused some outages". **No Apple Pay entry** (user reports only) (078) |
| NWS (card 027) | REPORTED (press, Downdetector); no NWS statement found; cause unknown (079) |
| Deutsche Bank leak | **Mechanism: whistleblowers to a journalist consortium**, not a reported hack (CNBC read). No CYPHER row; HANS owns the bank |
| Schwab | Still NOT ESTABLISHED (no outlet) |
| NSA Net | **CONFIRMED.** NSA: "temporary degradation during scheduled routine maintenance". **DNI Clayton (Fox Business): caused by patching the PHP vulnerabilities found last month** — the root of CYPHER's open WAVE-2026-10; "lots of institutions" are taking systems down to patch; no indicia of coordinated or state attack. Restoration: CNN source "ongoing but not yet complete"; staff back to "code green" in the evening (077) |
| AWS 11/15 cause | **None published**; no post-event summary (both AWS pages read) |
| Optimizely | No victim count from Optimizely (status page unchanged). HSBC: scripts not active; Equifax: stopped using Optimizely, no evidence of compromise to its systems or data; 3 other named firms no comment. Researcher: 50 of 159 organisations' sites allowed both the code and data theft |
| Microsoft (found in sweep) | Preliminary report: latent Exchange gateway software bug, not a patch, not cyber (071) |

## 3. Sweep, 11/15-11/17, items on NO card

**Searched:** WebSearch (standard and extended) for ransomware and breach disclosures, outages (banks, payments, Gmail, Marriott, Downdetector), Equinor/Gassco, NWS/Akamai, n0n listings; read CISA KEV v2026.11.17, SEC boot legs 8-9, the Apple, Optimizely and AWS status feeds and 16 articles (list in the record).

| Found | Grade | Row |
|---|---|---|
| **n0n extortion group lists JPMorgan Chase, Visa, Mastercard (11/16)** among dozens; Visa/Mastercard entries describe card-member programme records, not card numbers. **Visa confirms an incident at a third-party provider in Asia-Pacific; "Visa's systems were not involved"; no card numbers indicated.** JPMorgan and Mastercard: the gang's word only | REPORTED · SECONDARY | 081 |
| Marriott sign-in outage 11/17 ~09:15-14:00 ET; Marriott: technical issue, not cyber | CONFIRMED · SECONDARY | 082 |
| Gmail user reports 11/17; Google: no broad disruption | REPORTED | 083 |
| Java4Shell CVE-2026-114938 (OpenJDK, AI-found with Codex, RCE in default Jira, Jenkins, Keycloak, PingFederate and others on AVX-512 hardware); Oracle patched 11/17; not in KEV | DISCLOSED · SECONDARY | 084 (KEV watch key set) |
| Puppet Enterprise CVE-2026-115731 added to KEV 11/17 (the only KEV add since 11/14) | CONFIRMED · PRIMARY | KB-CYP-134 |
| Maersk breach (disclosed 11/11, outside window); Infoblox, Coles, Fandango (titles only, not read) | noted / not read | — |

**Could not reach / not read:** Cybernews (Visa quote via two relays), Calif's own post, Microsoft's PIR itself (tenant-gated), NSM, Oslo Børs filings, Gassco flows, leak sites (not visited by design), X posts, Fox News live blog, NWS notices. **No site blocked this session.**

## 4. One story or several? (the four 11/17 conditions)

**Several, unchanged: none of the four is met.** (1) No two outages share a named supplier, release or path: Microsoft a latent gateway bug, FAA a newly installed router, JPMorgan a software bug on its own hardware, Apple an internal update, Marriott a technical issue, NSA maintenance/patching, United, AWS and NWS undisclosed. (2) The government moved further from cyber (DNI: no coordinated or state attack). (3) n0n claims data theft, not any outage; unverified. (4) No shared tooling published.
⚠️ **The qualification that could change it:** the DNI's account is a common *background* — institutions patching the PHP flaws and systems not coming back — stated for the NSA only. If an operator's report names PHP-flaw patching for a second outage, condition 1 is met as **one story of defensive cost, not attack**. Test: Microsoft's final report, Apple or JPMorgan detail.

## 5. Scores, rows, gates

**Nothing changes in figures.** Composite stays **25/40 raw, 16/40 shared-root-adjusted**; VX-01 3, VX-02 3, VX-04 3, VX-05 4, VX-06 4, VX-08 4 all hold. Escalation rows: 1 FIRED (row 2, 10/26), 8 NOT-FIRED; **row 8 note: the patch side is now the live route** (it fires on an operator-confirmed bank or payment outage tied to PHP2Shell remediation or compromise). Row 7 note (DNI: no state activity, about the outages). FL-CYP-04 note (NSA = a security-patch outage at a non-bank; state already CONFIRMED). Predictions, R1 flip test, gates: none move. Catalysts 11/18 and 11/19 untouched; the N-able/MSP look stays on 11/19; the stale-KB packet stays held.

## 6. Trade assessment (WQ-696)

On CYPHER's evidence these items support **no investment implication**: Equinor's intrusion is IT-only with production unaffected on the company's word; the n0n listings of JPMorgan, Visa and Mastercard are unverified and Visa's confirmed incident sits at a supplier with no card data on its word; Optimizely has no loss figure; and the outages carry separate stated causes with no measured financial loss. Over days to two weeks, the reading is invalidated by an Equinor update that engages operations, gas flows or Gassco nominations (European gas, HANS and BRENT), by verified publication of card or account data from the n0n listings, or by an operator report tying a bank or payment outage to PHP-flaw patching (watch row 8). Unknown: Equinor's actor, method and OT reach; what n0n holds; how many cards Optimizely's skimmer took. No TERRY packet: nothing here is a tradeable finding on this evidence.

## 7. Delivered

Commits (pathspec, `AGENTS/CYPHER/`): record; INCIDENTS (078-084 new; 071, 072, 074, 076, 077 updated), ESCALATION_WATCH (rows 7, 8 notes), FLOW, VX, CHOKEPOINTS (CHK-26, CHK-20 notes), KB (130-134), board_log (5 cards) and inbox filing, corrections receipt COR-20261117-12 APPLIED, STATUS (12:39 block rotated verbatim, crc32 d2983f42), NEXUS_BRIEF. Packets: this one; WALTER (cards 024/026/027 graded, uncarded items for routing). Not done: push (yours at closeout), the 11/19 rows, the stale-KB pass. Charter note: read_cap_check puts `CLAUDE.md` at 75% of 32,550 B (charter_mode unspecified; root sets desk charters at 50,000 B) — flagged, not acted.
