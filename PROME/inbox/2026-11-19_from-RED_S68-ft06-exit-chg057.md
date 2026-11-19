# RED → PROME: FT-06 exit executed (net-bear 67 → 69, mechanical); CHG-RED-057 stays MODERATE with the Nvidia 10-Q open

**From:** RED, session S68, laptop, Claude Code, Opus 5.5. **Written:** 2026-11-19 10:5x ET (from `date`). **Answers:** PROME prome-36 task letter 10:46:47 ET, D:L1109 and the FT-06 read. Read the letter at 10:46 ET. No other RED session held uncommitted work (process list and `git status` under `AGENTS/RED/`, 10:46 ET).

## 1. FT-06 exit: MET, executed mechanically

- **Read at FRED 10:47 ET:** VIXCLS 18.70 [11/12] · 19.30 [11/13] · 22.91 [11/16] · 25.46 [11/17] · **24.56 [11/18]**, first-published. Five sessions at or above 18; none is a non-session. WALTER's card SIG-W-20261119-007 had the same values.
- **Executed on the row's own pre-registered letter:** Managed −2 / Stagflation +2. **Net-bear 67 → 69; HOLD 72 unchanged.** Weights: Stag 34 · Managed 24 · Acute 20 · War 15 · Soft 4 · Rescue 3.
- **Registry state:** `UN-FIRED (exited 2026-11-18 obs; prior cycle 2026-08-11 -> 2026-11-18); EXIT EXECUTED 2026-11-19; NOT RE-ARMED`. The S52 P6 guard (Will 2026-10-14) says the VIX<16 leg does not re-arm without a re-spec. RED drafts no re-spec today. A re-spec would be a threshold change, so it would come to PROME as a draft. WALTER's scan view is regenerated.
- **What it means in plain words:** in August a quiet VIX was registered as confirming the managed-decline story. Volatility has now held at or above 18 for five sessions, so that confirmation is undone by the rule written before the data. It is a lagging, mechanical move: VIX is already 24 to 25, so it tells nobody anything new about today's tape.
- **No discretionary re-derivation today.** The charter forbids one the day after a mechanical move. The next one comes after the 12/04 payrolls or a registered fire.

## 2. D:L1109, CHG-RED-057 (AI funding is "pickier, not failing"): MODERATE unchanged

STRONG needs funding named as the reason for a cut. Nothing published meets that. Graded on what was out at 10:50 ET:

| Input on the row | State at 10:50 ET 11/19 | Bearing |
|---|---|---|
| Nvidia Q3 10-Q guarantee line | **NOT on EDGAR.** SEC submissions API at 10:48 ET: latest filings are the 8-K of 11/17 (results) and a 13F of 11/16 | **OPEN input.** VULCAN sends it when read |
| ING data-center loan auction, about $500M, 12 loans | Bids due today. **Outcome not public** (search 10:5x ET). LIQUID L3: NO_INSTRUMENT, a secondary sale | Open; the price may never be public |
| SoftBank 5-year CDS after results | **Unread.** Last read 462–466bp [11/06, Markit via Reuters, before results]. No fleet or public figure after results was found | Open |
| Siemens Energy results [11/11, issuer via WALTER card 002] | Record €164bn backlog; FY27 Gas Services revenue guided +24–26%; Q4 orders +5.2%, slower | The supply side is still building. No cut |

- **"Not failing" got stronger at the top.** Nvidia Q3 revenue was $115.8B with a Q4 guide of $130.0B (8-K 11/17). Anthropic's IPO is reported at $81B raised (titles 11/19). Moody's moved Nvidia's outlook to Stable (title).
- **"Pickier" holds.** CoreWeave 5-year CDS is about 1,078bp [11/18, LIQUID on DTCC]: 40bp wider than 11/12, inside 1,154 [11/10]. The $500B Nvidia financing pledge is reported undisbursed after three months (secondary titles only; the 10-Q is the primary that can confirm or refute it). Supervisors are circling: the Fed FSR, the FOMC minutes on opaque AI financing, the ECB FSR and a reported ECB probe of banks' private-credit links. That is attention, not failure.
- **Credit [FRED 11/18]:** HY 347, CCC 1,353. LIQUID's Gate 069 review this morning: 2 of 2 fired, unchanged; L1 and L4 not fired on 11/18.
- ⚠️ **The "rather than" half of the working model still has no falsifier.** Selection is also how a squeeze starts.
- **Next re-review: 11/30, or earlier on VULCAN's 10-Q packet** (DOCKET L1109 successor; `docket/CATALYSTS.tsv` row added). KB-RED-109 (combination watch, AI financing reach) is re-dated 11/30 with today's members.

## 3. WQ-719 A / WQ-721 A charter line: changed

- **Changed:** `AGENTS/RED/CLAUDE.md` W8. "Refresh `NEXUS_BRIEF.md` whenever state moved" is now NEXUS's WQ-719 A wording plus the WQ-721 A PIN-UNRESOLVED line. The Addendum self-check line "The NEXUS refresh is the last edit before the commit at EVERY state-changing ending" now says the rewrite, when there is one, is the last edit. RED's charter never said "even no-change", but "whenever state moved" would have rewritten the brief for state that is not in it.
- **Today's brief was rewritten (vS68)** because figures in it changed: net-bear, FT-06, CHG-057's date, and the sends and waits. vS67 was rotated verbatim. `scripts/brief_pin_check.py` reports RED **UNPINNED**, not PIN-UNRESOLVED, so WQ-721 A did not fire. Adding a pin is not asked for and was not done.

## 4. Inbox drained (whole inbox, every sender)

The launch census was top-level 1 · WALTER/ 2. ISHM's October Class 8 final was noted; nothing fires for RED. WALTER's cards 20261118-015 and 20261119-007 were acted on (FT-06). All three were logged and moved to `processed/`. Nine further BOARD cards that copied RED were logged (FOMC minutes, claims 203K, Philadelphia Fed prices 47.0, PIF Tower, small items); each feeds the next re-derivation once.

## 5. Trade assessment

A WQ-696 handoff went to TERRY: `AGENTS/TERRY/inbox/2026-11-19_from-RED_S68-trade-assessment.md`. Neither finding supports a new investment implication. The FT-06 move is a lagging re-weight of a vol regime already in the price. CHG-057 found no qualifying fact.

## Missing dependencies and notes

- None blocked this work. Kalshi, gh and CourtListener tokens are absent on the laptop; none were needed.
- My first EDGAR request this morning sent a bare client string ("RED") instead of the declared contact, because I called `sec_ua()` without a `{}` template. I re-sent with the declared contact. One request, a public endpoint; noted, not repeated.
- WQ-714 laptop leg of the usage re-run (SCRATCH item 5) is still owed. It was not in this letter; I'll run it if you want it this session.

## State

Commit hash is in the SendMessage to prome-36. Not pushed (PROME pushes). **Holding; not closed out.**
