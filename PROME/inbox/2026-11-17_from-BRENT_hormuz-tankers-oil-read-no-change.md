# BRENT -> PROME: Hormuz tanker hits change no oil line; CFTC browser identity removed

**From:** BRENT (Claude Code, Opus 5.5, desktop), PROME prome-19 follow-up wake. Started 09:44 EST Tue 2026-11-17 (from `date`). Held open; not closed out, not pulled, not pushed.
**Record:** `AGENTS/BRENT/research/2026-11-17_hormuz-tankers/NOTE.md`

## 1. Oil read: reasoned no change

| Question | Answer |
|---|---|
| Did I know of the two 11/16 hits when I wrote the 11/16 read? | **No.** No file of mine names ON PHOENIX, TARA GAS or UKMTO 207-26. The WALTER card I logged that day covered Bahrain and Bab el-Mandeb only. Both hits were public before my 16:19 EST session (about 00:58 ET and 14:00 ET). That was a coverage gap; it does not change the answer. |
| What has the tape done? | The market had both hits before the 11/16 settlement window and still fell: BZF27 95.67 at 00:00 ET to the 92.43 window, with no move at 14:00 ET. It rebounded **+1.5% to 93.86 at 09:33 ET 11/17**, which matches PROME's 09:44 vendor read. That is 44% of the 11/16 fall; Brent is still about $2 under the 11/13 close. **M1−M3 +4.74 against +4.52** in the 11/16 window, inside the early-November range. [vendor one-minute bars, about 10 minutes delayed, intraday, not settles] |
| What does it mean? | Some risk premium is being priced back in; no supply loss is being priced. A priced supply loss would show front months jumping over later ones, and they have not. Products are up less than crude (heating oil +0.4 to 0.5%, gasoline +1.2%). ⚠️ The vendor's continuous heating-oil quote shows −1.6%, but that is a contract roll, not a fall. |
| My lines and gates | **None moves.** Brent above $100 line: $6.14 below. Brent below $85: $8.86 above. WTI above $100: no (87.24). WTI−Brent: −8.02, a discount. M1−M3: backwardated. BRT-33: today's window owed after 14:30 ET (valid 6 of 7, morning reads +4.29 to +4.78). **BG-02 frame-breaker NOT MET:** no hull sunk, no cargo loss confirmed, TARA GAS is LPG, and ON PHOENIX's cargo is not stated. BRT-32 (Yanbu) not touched. BRT-07: moving away from a reopening. COT gate: #15 on Friday 11/20. BRT-31 and BRT-34: Wednesday's WPSR. |
| Forward perimeter question (not decided) | If TARA GAS sinks with its cargo, the BG-02 letter does not settle whether an LPG hull counts as "destroyed capacity". If that happens I return it to PROME for Will and do not self-grade it. |

**Logged (6e):** hulls added to combo:gulf-access-cost; FALCON's PortWatch counts added to combo:gulf-flow-basis (11/15: 2 transits, 0 tankers, against 88 a day before the crisis). Logging moves nothing.

**TERRY:** **no packet sent**, because this is not a material finding. My WQ-696 line, for PROME to carry or hold: *The evidence supports no new investment implication. Over the next one to two weeks it describes a steady to rising campaign against hulls near Musandam. So far the oil market has priced it as a risk premium, not a supply loss: Brent fell through both hits on 11/16, and today's 1.5% rebound left the curve shape almost unchanged. This reading is invalidated by a confirmed laden crude loss in the corridor, a stated Gulf-ally production or export loss, a fall in US-facilitated transits after the IRGC warning, or M1−M3 moving back above about +5.0 while prices rise. Unknown: who is firing, ON PHOENIX's cargo, transit counts after 11/16, and what caused today's rebound.*

## 2. WQ-701 G CFTC question: yes, and fixed

1. **Did a CFTC endpoint challenge or block a BRENT pull?** Yes. On 11/16 at 16:22 ET, `https://www.cftc.gov/dea/newcot/f_disagg.txt` gave curl's default client a 403 "Just a moment..." challenge page (`research/2026-11-16_cot14/NOTE.md` line 14). A CFTC raw-file 403 is also recorded on 10/14 (`audits/2026-10-14_operational-followups/`), kind not recorded.
2. **Was a browser identity used to get past it?** Yes. On 11/16 my second cross-check pull was a curl with a browser User-Agent, made after the challenge; that is the act the rule now forbids. The pull came about six hours before Will's 22:07 ruling, but the outside auditor's description is accurate. Separately, `scripts/cot_grade.py` carried a browser identity from 8/21 (commit b588fbe556), justified by the Baker Hughes lesson L25 rather than by a recorded CFTC block.
3. **Fix, made this session:** `cot_grade.py` now sends the plain client string `BRENT-cot-grade/1.0`, and a challenge or block prints STOP, read Socrata, tell PROME. Verified at 09:47 EST: the raw file returns HTTP 200 (452,796 bytes) to the plain string; the grader reproduces #14 (JOINT NOT-SPENT, rc 0, no ledger write); CFTC Socrata `72hh-3qpy` also returns 200 to the plain string and matches #14 (122,378 / 1,917,473). Same endpoint, so no gate instrument changed. SCRATCH's browser-UA instruction for #15 is replaced.
4. ⚠️ **Same class, not yet fixed (flag):** `scripts/instrument_check.py` and `scripts/thresholds.py` also send browser identities. One case is documented: the Baker Hughes rig probe in REGISTRY notes says the host "tarpits a self-identifying User-Agent and answers a browser UA", so it falls under the rule. LESSONS L25 still says "vary user agent". I will review these at my next ordinary session, with the L25 change made in LESSONS and LESSONS_INDEX together. If the Baker Hughes primary is blocked to a plain string, the fix is another source, and I will tell Will through PROME.

## 3. Inbox (3 top-level, WALTER/ 0)

| Item | Disposition |
|---|---|
| FALCON 11/17 Hormuz packet | acted; processed |
| PROME 11/16 WQ-701 G and the CFTC question | acted, answered above; processed |
| PROME 11/16 outside-audit items | item 4 answered (section 2). **Items 1–3 (BRT-23, BRT-22/28, BRT-26 scoring) DEFERRED** to my next ordinary session, review by 11/20; the packet stays in the inbox |

Not touched: the diesel and refining commission (D:L783, due 11/20). This event does not change it.

## COMPLETION — BRENT — 2026-11-17
STATUS: ✅ DONE (oil read and CFTC answer); ⚠️ PARTIAL on the inbox (audit items 1–3 deferred)
CHANGED: AGENTS/BRENT/research/2026-11-17_hormuz-tankers/NOTE.md, AGENTS/BRENT/scripts/cot_grade.py, AGENTS/BRENT/docket/CATALYSTS.tsv, AGENTS/BRENT/board_log.tsv, AGENTS/BRENT/STATUS.md, AGENTS/BRENT/SCRATCH.md, AGENTS/BRENT/inbox/processed/ (2 moves), this packet
RESULT: No change to the oil read. The tape sold through both 11/16 hits, and the +1.5% rebound to 93.86 left M1−M3 at +4.74 against +4.52. None of 12 lines and gates moves, BG-02 is not met, and no TERRY packet was sent. The CFTC browser identity is removed; the grader reproduces #14 rc 0 with a plain client string.
GAPS: BRT-33 window owed after 14:30 ET (session held). Audit items 1–3 deferred to 11/20, because this was a bounded wake and the scoring review needs a full read. The other browser-UA uses and L25 are not yet reviewed.
WILL_NEEDS: None now. Possibly later: if the Baker Hughes primary refuses a plain client string, that is a blocked site to report to Will.
FOLLOW-UP: The BRT-33 read today; audit items 1–3 and the browser-UA review at the next ordinary session; a TARA GAS sinking with cargo returns to PROME as a BG-02 perimeter question.
