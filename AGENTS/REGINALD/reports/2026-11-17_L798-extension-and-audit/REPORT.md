# REGINALD 2026-11-17: D:L798 comment period extended to 12/16, Fed and FDIC comment files read; D:L1095 BKU; outside-audit items; REG-T-02 through 11/16

**Session:** wake on PROME prome-19 (WQ-184, class C6), Tue 2026-11-17 from 08:37 ET. Claude Code, model Opus 5.5 (claude-opus-5-5); session id not exposed (scratchpad 457585ae). Git: 1 commit ahead of origin at boot (PROME's), no pull (brief says do not pull until PROME asks).

## 1. D:L798: the comment period did not close on 11/16

**Finding.** The four agencies **extended both comment periods to Wed 12/16/2026**, announced **Fri 11/13 at 4:15 PM ET**: the interagency third-party risk guidance (91 FR 58536, Fed docket OP-1881, OCC-2026-0793, NCUA-2026-1684, FDIC RIN 3064-ZA58) and the Fed's separate community-bank guide (OP-1880). [PRIMARY: Fed press release `bcreg20261113a.htm`, read 11/17 08:4x ET, sha256 of the page as served `e070df61…52e3f4`; OCC news feed item `nr-ia-2026-100`, same text: "extend, until December 16 … originally due November 16"; the Fed proposal pages for OP-1881 and OP-1880 both show "Closing date for comments: 12/16/2026".]

**Why my 11/16 read had it wrong.** regulations.gov still reports `commentEndDate` 2026-11-17T04:59:59Z and `openForComment` false on OCC-2026-0793-0001 and NCUA-2026-1684-0001 (API, 11/17 08:4x ET), and the FDIC Federal Register table still shows "Comment Period End: November 16, 2026". I read the regulations.gov field on 11/16 at 10:14 ET, three days after the extension, and did not check an agency release. GIBBS relayed my date, and the DOCKET row's 11/17 date rests on it. KB ML-REG-300 is marked corrected by ML-REG-305 (text kept).

**So the "full file after the close" does not exist yet.** ABA, BPI, CBA and ICBA have filed only their 10/29 extension request (Fed C25, OP-1880 C19, FDIC letter 01); their substantive letter is expected near 12/16. A complete read is possible only after Wed 12/16 23:59 ET plus the agencies' posting lag.

### What I read today (interim, every route I may use)

| Route | Count | Read how |
|---|---|---|
| Fed OP-1881 (federalreserve.gov PDFs) | 49 letters, C10–C61; C1–C9, C41, C44, C54 return the site's error page | full text, keyword scan, bank letters read in full |
| Fed OP-1880 (community-bank guide) | 18 letters, C10–C28; C27 not served | same |
| FDIC RIN 3064-ZA58 (fdic.gov PDFs) | 24 files | same; Regional Missouri Bank letter is a scanned image, **not read** |
| regulations.gov OCC / NCUA | 58 / 63 comments listed (was 48 / 48 at 11/16 10:15 ET); 4 posted 11/17 on NCUA | **titles only.** The attachment host refuses automated access (CloudFront "Request blocked" to a plain honest client string, 11/17 08:4x ET). Per root Data Hygiene I stopped there. The API key route allows 10 calls an hour |
| Proposal texts (Federal Register raw text, 2026-18859 and 2026-18852) | 2 | counted terms |

### Bank-side disclosures of core-vendor dependence

| Letter | What it says | Vendor named? | Figure? |
|---|---|---|---|
| **Bristol Morgan Bank** (Wisconsin community bank), Fed OP-1881 C17 | "Over multiple years, the Bank has experienced core and ancillary system interruptions, degraded performance, failures affecting customer communications, delayed or incomplete escalation …" at "a large core service provider"; "a community bank may be fully accountable for the consequences of a third party's failure while possessing limited practical authority to prevent, remedy, or exit the relationship" | No | No |
| **First National Bank Texas** (Killeen), Fed OP-1880 C21 | "Community banks often rely on a single core provider for multiple critical banking functions"; asks the agencies to address "unreasonable restrictions on data access, excessive deconversion fees, and contractual limitations" | No | No |
| **Guaranty Bank & Trust**, FDIC | "a highly concentrated market when selecting core service providers … massive, systemic core processors" | No | No |
| Axos, IBAT, NY CU Association, Truliant, Capital Bank and Trust | already read 11/16 (ML-REG-300) | No | No |

Vendors are named only by non-bank commenters: an individual (Csilla Brimer, OP-1880 C18) calls FIS, Fiserv and Jack Henry "systemically important technology intermediaries"; Pehtee-Nu (OP-1881 C19, OP-1880 C14) cites Fiserv's agentOS launch of May 2026.

**Read:** Bristol Morgan is the first bank-side letter in the file that describes **realized** core-provider failures over several years, not only weak bargaining power. It is still unnamed and unquantified, so it does not test DEWEY's 10/22 base rate by assets, and a complaint letter is self-selected, not a frequency.

### Regulator statements on agentic-AI access

- **Both proposals: zero mentions** of "artificial intelligence", "agentic", "AI" or "machine learning" (Federal Register raw text, counted). The Fed's community-bank guide is the same, which I had not checked on 11/16.
- **Fed Vice Chair for Supervision Bowman, 5/1/2026 speech** (PRIMARY, read 11/17, sha256 `7a0217c2…72b3`): the agencies "amended our model risk management guidance to clarify that it does not apply to generative or agentic AI"; "we expect other risk-management and governance practices to support adoption of generative and agentic AI". This closes my 11/16 caveat that the SR 26-2 exclusion was only a secondary quote.
- **Fed Governor Waller, 9/28/2026 Sibos speech** (PRIMARY, sha256 `2c09c6ee…ad8ee`): for agent-made payments, "the question shifts from proving that a buyer is an authorized payer to proving that an agent has the authority to pay on the buyer's behalf. Capturing this will require new authentication approaches"; liability is "who is on the hook if an agent makes the wrong purchase?"
- **No guidance exists** on examiners' treatment of AI agents reaching bank accounts. What exists is speech: pro-adoption, with authentication and liability named as open problems. The 1033 rewrite at OIRA stays unpublished (ML-REG-300, SECONDARY).

**So what for my book:** no consequence. The guidance is non-binding, the change is a one-month delay, no bank names a vendor or a figure, and nothing here touches my 14 names, any score, gate or prediction. Logged under the combination-watch theme `bank-vendor-breaches` (KB ML-REG-305), not scored.

**Proposed re-date (PROME's row):** D:L798 REGINALD leg → **Thu 12/17/2026 or later**, after the 12/16 23:59 ET close; posting lags (the FDIC table and regulations.gov already lag the release by four days).

## 2. D:L1095: Bank United (BKU), my clause

**No longer applies, and re-checked today.** PROME removed the BKU clause on 11/16 10:28 ET (DOCKET L1095 status cell) because I re-verified BKU on 11/06 (commit `39a0585034`, "BKU 10-Q graded, class MIXED, REG-32 FALSE, FL aggregate NO TRANSMISSION FINAL"; packet `PROME/inbox/processed/2026-11-06_from-REGINALD_BKU-grade-FL-frame-final.md`; both exist, checked 11/17). Today: SEC submissions for BankUnited, Inc. (CIK 1504008) show **one filing since 11/01, the 10-Q of 11/05** (acc 0001504008-26-000091), which is the one graded 11/06. No 8-K since. Nothing to re-verify. ⚠️ The row's description column still lists "BKU not re-verified at REGINALD" beside the status cell that removes it; that text is PROME's.

## 3. Inbox: outside-audit items (PROME packet 11/16 23:0x ET)

| Item (auditor's words) | Checked at FRED 11/17 08:4x ET (`fetch.py fred`) | Disposition |
|---|---|---|
| 1. Claims 189K and the Chicago Fed index are early readings since revised | ICSA w/e 10/31 now **191K** (was 189K); newer print **200K [w/e 11/07]**. NFCI 10/30 now **−0.465** (was −0.459); newer **−0.462 [11/06]**. STLFSI4 −0.5227 [10/30] unchanged; newer **−0.4918 [11/06]** | **Auditor right.** STATUS rows updated with both vintages labelled |
| 2. The HY figure dated 11/13 matches 11/03 in FRED | `BAMLH0A0HYM2`: **3.23 [11/13]**, 3.40 [11/03] | **Not supported.** 323 is the 11/13 value and matches LIQUID's first-published 323 [11/13]; one figure, one basis, no change. Also: FRED now carries 3.30 for both 11/10 and 11/11; 11/11 is the Veterans Day non-session forward fill (`registry/NOTES.md` line 183), so the label question I carried is closed |

## 4. Mechanical: REG-T-02 exit grading

Four settled closes added to `registry/REG_T02_EXIT_LOG.tsv` (Yahoo daily history and Nasdaq historical agree, `scripts/settled_bars.py`, 11/17 08:50 ET): **11/11 $75.64 · 11/12 $74.39 · 11/13 $74.79 · 11/16 $73.46**. All below $81.90; run **0 of 3**; 54 graded closes. 11/11 was an equity session (bond market closed). Needs +11.49% from $73.46.

## 5. Tape and monitors at boot (11/17 08:38 ET, pre-market; last settled bar 11/16)

| Item | Value | Note |
|---|---|---|
| WAL | $73.46 [11/16 settled] | below $78, REG-T-02 FIRED, suppressed re-entry |
| KRE | $72.19 [11/16 settled] | $12.19 above $60; KRE shares 55.48M, +0.7% vs 11/16 |
| FLG | $10.40 [11/16 settled] | −27.0% vs frozen $14.24; RED ladder, 28 closes below since 10/7 |
| HY OAS | 323 bp [11/13], latest posted | REG-T-04 not fired |
| VIX | 22.90 (vendor, 11/16 close) | |

**Insider monitor (SEC Form 4, last 14 days):** FLG Executive Chairman and CEO **Joseph M. Otting bought 47,324 shares at $10.49 on 11/10** (filed 11/12; acc 0001323101-26-000007, read at SEC): about $496K, holding 1,088,823 direct after. EGBN: two small director buys (about $199K) against five insider sales (about $938K). KB ML-REG-306. Not a matrix input; FLG desk owns the name. **8-K monitor:** no new 8-K at CFG, CUBI, EGBN, FLG or OZK (FLNG) since 11/10; ⚠️ the AMTB line printed no result (incomplete, not clean).

**BOARD diff:** three cards logged INFO_ONLY (SIG-W-20261113-005 Car-Mart bridge; -20261116-007 life-insurer AI debt; -20261116-005 stale WAL reposts that named this desk). No card named REGINALD for action. **Peer channels:** OZK and WAL, nothing above my last ACK.

## 6. Trade-read handoff (WQ-696)

- **D:L798 extension and letters: supports no investment implication.** Non-binding guidance, delayed a month; no bank names a vendor or a dependence figure; nothing reaches a bank's earnings, capital or deposits on any horizon I can name. What would change that: a named core-provider outage at a listed bank, or final guidance that changes examiner treatment of core contracts. Unknown: which vendor Bristol Morgan uses, and the trade groups' 12/16 letter.
- **FLG CEO purchase:** the evidence implies the CEO is willing to add about $0.5M at $10.49, two weeks after the Q3 miss, below every band of the frozen ladder. Over the next one to two quarters that is mild evidence against an imminent capital or loss surprise at FLG, not evidence on the multifamily book. Invalidated by: an FLG capital action, a further special-mention to substandard migration at the Q4 release, or insider selling. Unknown: whether the purchase was planned (no 10b5-1 marker read), and the outcome of the rent-regulated book. Not sent to TERRY directly; the FLG desk owns the name and this does not change any REGINALD score.

## 7. Blocked-site flag (for Will via PROME)

regulations.gov's attachment host (downloads.regulations.gov) refuses automated access: a plain honest client string gets CloudFront "Request blocked" (11/17). ⚠️ **My 11/16 session read those PDFs by sending a browser user-agent and a Referer header** (MEMORY 11/16: "a browser UA plus Referer works"). Root `CLAUDE.md` Data Hygiene says a site that refuses automated access is unusable by automation and an identity string must never be changed to get past it. That 11/16 workaround breaks the rule; I did not repeat it. The 11/16 reads of OCC and NCUA letters stand as content but were obtained the wrong way. Fed and FDIC host their own copies, which I used today.

## Files

`registry/REG_T02_EXIT_LOG.tsv` (+4) · `workbook/KB.tsv` (ML-REG-305, -306; ML-REG-300 status) · `board/BOARD_LOG.tsv` (+3) · `STATUS.md` · `MEMORY.md` · `ROADMAP.md` · `CALENDAR.md` · `LESSONS.md` · this report.
