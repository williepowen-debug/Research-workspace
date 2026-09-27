COLDREADER · PROME/reports/2026-09-27_nano-banc-failure-SYNTHESIS.md · 24183 B (wc -c, 77 lines) · 81 claims
SCORE: 50/81 ✅ · 25 ⚠️ · 6 ❌
(RESULT read of FINAL CANDIDATE. Read-only; this ledger is the only write.)

❌ 2 (L3) DEWEY source is "interim". L3: "DEWEY `output/2026-09-27_nano-banc-primary-documents.md` (interim, uncommitted at 12:38 ET)". L2 says: "5 of 5 desks consumed (DEWEY delivered 13:14 ET, 6a90ca732)". `git show --stat 6a90ca732` = "DEWEY -> PROME…: Nano Banc primary documents delivered", +534 lines to that file. The owner-file list carries a stale state token.
❌ 16 (L10) The haircut "ceiling". L10: "a haircut **ceiling ≤ ~51–56% ON THE ZERO-ADJUSTMENT SCENARIO ONLY**". The same sentence then says a premium "RAISE[s] the true loss (and so the ceiling) … e.g. +$10M premium −$5M costs ⇒ ≈58%". A "≤56%" ceiling that can reach 58% is not a ceiling. The owner rejects the word: REGINALD L112: "e.g. a +$10M premium − $5M costs ⇒ ≈58%, so this is **not a ceiling**"; REGINALD L118: "≈51–56% (zero-adjustment scenario, not a bound)". CREED L14/L81 does say "ceiling ≤ ~56%", so the two owners disagree. The synthesis took the word that the owner of the figure refuted.
❌ 53 (L41) §5 cites the ceiling with no label. L41: "a loss up to the ceiling sits inside the 2026 distressed-CRE range". The file's own rule at L10: "Cite it as a labelled scenario or not at all." No scenario label and no "not a bound" appear in §5. Same owner conflict as #16.
❌ 64 (L52) Grading of ML-REG-044. L52: "**Right, seven months early, on direction and mechanism** … the litigation drain it named is exactly what the RI-E line shows". Contradicted by:
  - Its owner, REGINALD L29: "✅ **Directionally right** … ⚠️ Qualified per CATO NB2: the Call Report shows *legal expense*, not *which* case. No primary ties the $46.3M to the Honarkar arbitration specifically".
  - REGINALD L35 ("What it did NOT predict"): "that the DIF loss would be driven by **asset marks**".
  - The file's own L34: "the 9/22 books carried only $8.4M of other liabilities, so nothing large was booked". The call named "arbitration liability"; RI-E shows legal FEES.
  - "Mechanism" and "exactly" claim more than the owner grants.
  - On ask (3): §1 and §8 agree that capital loss was litigation-dominant. §8 overstates the call against §1's two-cause model at L8–L10.
❌ 71 (L56–66) The §9 table ("registered today") omits DOCKET L517 and L518, which the body cites as registered:
  - L32: "the Plaza Continental stipulation hearing Tue 9/29 13:30 PT (DOCKET L517)"
  - L36: "trial continued from 8/11/2026 to 1/12/2027 (dkt 52 … DOCKET L518)"
  - L69 and L70 cite them too.
  - `sed -n 517p;518p PROME/DOCKET.tsv` shows both rows present.
  - The table lists L513–L516 only.
❌ 76 (L71) §10 item 3 uses an absolute. L71: "allocates the $120M between purchased and retained". L10 gives "≈$120M … (9/22 base; range $110–120M)" and "Cite it as a labelled scenario or not at all." Item 3 has no range, no scenario label and no measure (implied total loss = equity + estimated DIF cost), and it includes $5.66M of equity that is not an asset allocation.

⚠️ 3 (L2) "⚠️ declared in § Residue". No § Residue exists in the file (prospective pointer; unresolved today).
⚠️ 4 (L3) The cited owner SHAs are older than the versions the text reflects:
  - REGINALD d8010b97f (12:43) was superseded by 2117b2148 (13:15, "CATO NB1/NB2 applied").
  - CREED ae1b68938 was superseded by 3ced5139e (13:15, "CATO NB4 applied").
  - WAL content commit b08df95ae is labelled "pushed".
  - A stranger cannot tell which version was consumed.
⚠️ 5 (L3) "every figure below names its base" does not hold (self-describing claim). Undated figures: $736M (L12), 73% CRE (L10), RE $498M→$363M (L22), PFBC $51M (L29), "10% of nonaccruals" (L77).
⚠️ 6 (L2) "Written: 12:46 ET", but the body contains 13:14 and 13:2x events (self stamp).
⚠️ 8 (L8) "four desks concurring, none dissenting". Five desks were consumed; which four is unstated.
⚠️ 10 (L9) "a deferred-tax write-off $12.8M" is stated as fact. REGINALD L15: "$12.8M tax *expense* … consistent with a deferred-tax-asset write-off" (an inference).
⚠️ 15 (L10) "15.5% on 6/30 = 16.5% on 9/22; 21% on 6/30 = 17% on 9/22".
  - The arithmetic checks: 114/736.2 = 15.5; 114/690.9 = 16.5; 153/736 = 20.8; 120/690.9 = 17.3.
  - "=" joins different numerators on the implied-loss measure ($153M vs $120M, per REGINALD L16).
  - 16.5% is PROME's rebase, yet it is labelled "the FDIC's".
  - REGINALD's 6/30 range ($140–153M, L119) is dropped.
⚠️ 17 (L12) The $736M is undated (DEWEY L30: 6/30/2026). Unclear whether "aggregate ≈$1.4B" includes Nano.
⚠️ 20 (L17) "REGINALD's 14-bank cohort maximum is ~24% (WAL)". A REGINALD cohort figure is attributed to WAL.
⚠️ 23 (L18) "Nano would have flagged from 6/30/25". The owner's own table (REGINALD L46, L48) shows ALLL/noncurrent 79% [9/30/23] and 91% [3/31/24], also below the 100% flag. The synthesis series at L18 skips both. This is the owner's defect, carried over.
⚠️ 24 (L19) The arrow "24.3% [12/25] → 25.7% [6/26]" hides the dip to 20.6% at 3/31/26 (REGINALD L56) and reads as monotone.
⚠️ 28 (L22) "the Fed OIG's Material Loss Review … will say". It asserts content of a future report. DEWEY L222 dates the MLR "~late March to mid-April 2027 (DEWEY inference)"; §9 gives 2027-03-25 (modeled).
⚠️ 31 (L27) "No bank in Will's book perimeter is named by any desk". §4 (L31) names "your WAL Dec-18 $70P" and every desk names WAL. The heading scopes the sentence to lookalikes, but the literal sentence is false.
⚠️ 32 (L29) PFBC "$51M → $169M [3/26]": the $51M is undated.
⚠️ 34 (L32) "Nano Banc **holds** four deeds … SENIOR to WAL on 5 of 10" is present tense from an 8/18/2025 complaint. WAL L13 says "(if Nano still held them)". If DEWEY's Chino inference holds (WAL bought Preferred's senior loan), WAL is now senior on Chino. Not flagged.
⚠️ 38 (L32) "CONTRADICTED for Ontario and Chino" is stated before its limit. It holds only as of 8/26 and 9/8–9/11. The limit follows in the same paragraph and §10.1 keeps it, so a skimming reader could miss it.
⚠️ 45 (L34/L53) "Nano is jointly and severally liable … its SHARE … NOT FOUND": "share" of a joint-and-several liability is undefined. Also, "confirmed 12/5/2025" (L34) sits beside "a full defense verdict in another, 12/2025" (L53). Two December-2025 outcomes, forums not named.
⚠️ 47 (L34) Undefined tokens: WAL-01, WAL-02, `GATE-TERRY-ROLL70-EXIT` "(0-of-3 through 9/25)", "L170/L171". A stranger also cannot tell that "L###" means a DOCKET.tsv line number. These are not trade recommendations.
⚠️ 50 (L39) "≈$190M of loans — INFERRED as the $123M nonaccrual book … plus the delinquent construction book". The components sum to ≈$165M (REGINALD L135: "$164.6M"; CREED L50: "roughly $165M"), not $190M.
⚠️ 59 (L46) "~36% (2026 wall, June vintage …) rising to ~51% (September cohort)" joins two different cohorts as one number "rising". L10 forbids exactly this ("NOT one number rising"). CREED L168 lists the two side by side.
⚠️ 60 (L46) "at a normal 1.25× lender test, over half the September cohort cannot refinance": the spread and amortization case are unstated.
⚠️ 61 (L46) "Rates did not fail this bank … before the summer's real-yield rise": which summer is not given, and a timing argument is stated as an absolute.
⚠️ 70 (L62) "REGINALD re-runs §3" refers to REGINALD's §3, but this file's §3 is Lookalikes.
⚠️ 78 (L68–74) Body items left open that §10 omits: correction vs relabel (L22), enforcement leg proxied and not run (L27), MI3 base rate not run (L24), the COUNT-vs-BALANCE basis (L46).
⚠️ 80 (L77) "reserves at 10% of nonaccruals": undated (the 12/25 trough; latest is 16% [6/26], L18), and nonaccrual is not noncurrent (the L18 metric is ALLL/noncurrent).

✅ 1 state 5/5 (6a90ca732 resolves) · 7 no card/trade/gate/$0 (consistent L66, L77; no sentence reads as a trade rec or gate change) · 9 litigation-dominant, −$75.3M, 46.3+16.7+12.8=75.8 · 11 equity 126→39→5.66 (0.82% = 5.66/690.9) · 12 seizure order capital-only; both causes in sequence · 13 conduct first 3–4 yr, medium confidence (DEWEY L385) · 14 ≈$120M ≈17% of $690.9M, range $110–120M (REGINALD L110) · 18 anatomy visible pre-closure · 19 MI3 79% of C&I, $179.6M at 12/31/23 (179.6/227.9) · 21 CRE 295/437→529/755 · 22 reserve series 109/33/10/16 · 25 construction $41.4M = 88% · 26 deposits 870→686 = −21% · 27 C&I→9.b $22M→$88M · 29 MI3 n=1 not adopted · 30 4,313 filers, 1/0/43, Sunwest two legs · 33 four DOTs sum $28.04M · 35 Bellflower $482K/unit INFERRED · 36 Ontario $5,131,969 · 37 Chino $19.1M + inference labelled · 39 limits travel · 40 9/29 hearing = DOCKET L517 · 41 $64M, no seller · 42 bar date est. late Dec–early Jan (REGINALD L171) · 43 WAL net legs · 44 award share NOT FOUND; $8.4M other liabs · 46 $72.4M + $64M, two components · 48 Makhijani 8:26-cr-00087-DOC, trial 1/12/2027 · 49 retained ≈$215M · 51 $97.1M HFS side UNKNOWN · 52 second-lien recording rule · 54 comps 35/49, 48.8/72.6 · 55 fence · 56 $23M counterweight · 57 L515 2027-06-25 · 58 5.18/2.85; 7.93% constant, 1.01× · 62 ORACLE block (13,018; ~55%; 51%/94%; $4.1K; 19:08; ~170×) · 63 named legs · 65 un-scored · 66 corrections (C&D 1/18/22→3/20/25; Gressak $75,000; $909M→$690.9M −24%) · 67 Written Agreement termination not found · 68 PROME slips · 69 §9 L513–L516 match the body · 72 BOARD/KB/WATCH rows (KB-WAL-203 matches L36) · 73 no-move row · 74 §10.1 keeps DEWEY limits · 75 §10.2 · 77 §10.4–6 · 79 §11 severity labelled by measure + base · 81 six failures, 3× 2024

ASKED-FOR CHECKS
(1) Measure and base. §1 L10 and §11 L77 name both. Failures:
  - §10.3 "the $120M" names neither (❌ 76).
  - §5 "the ceiling" is unlabelled (❌ 53).
  - The "=" at L10 joins unequal numerators (⚠️ 15).
  - No sentence pairs the FDIC measure with the other measure's base.
(2) §4 keeps DEWEY's limits (9/8–9/11, 8/26, not 9/25 ownership or allocation, Chino $13M inference), and §10.1 repeats them. The only softness is the "CONTRADICTED" verdict placed before its limit (⚠️ 38).
(3) Capital loss as litigation-dominant is consistent across §1 and §8. §8's "mechanism … exactly" overclaims against the owner (❌ 64).
(4) §9 omits L517 and L518 (❌ 71). §10 matches the body but omits four open items (⚠️ 78).
(5) No trade recommendation or gate change found. The WAL gates are stated UNCHANGED; the "must bid, not sue" line (L34) is about WAL the company, not Will.

SPOT-CHECK (16 figures; 15 match, 1 label mismatch)
  - REGINALD: −$75.3M/$46.3M (L15) · $120M ≈17% of $690.9M, range $110–120M (L110) · $5.66M (L111) · 4,313 filers / 755% (L4, L147) · $179.6M, 295%/437% (L47)
  - WAL: $28.04M (L50) · $72.4M + $64M (L76, L52)
  - DEWEY: $5,131,969 (L326) · $19.1M + Chino inference (L327, L333) · $75,000 (L27) · $909M, −24% (L30) · 8:26-cr-00087-DOC, 1/12/2027 (L345) · $8.4M (L81)
  - CREED: 48.8%/72.6% (L96–97) · 5.18%/2.85%/7.93% (L144, L154)
  - ORACLE: 13,018 / $4.1K / ~170× / 51%/94% (L15, L44, L46, L56)
  - MISMATCH: "ceiling ≤ 51–56%" vs REGINALD L112 "not a ceiling". Composition note: $190M vs the owners' own ≈$165M.

POINTERS: 30/31 resolve; dead: "§ Residue" (L2, not present — prospective).
  - Tested: plan file, CATO packet, 5 owner files, 9 SHAs, DEWEY §4x/§1a/§1b/§2b/§5(a)/§5(c), BOARD -004/-005 (in the WALTER logs), DOCKET lines 513–518.
  - Not tested: L170/L171.
ONE-LINE VERDICT: Mostly yes. A cold reader gets the right shape: capital loss was litigation-dominant, the FDIC loss is asset marks, and there is no trade or gate change. But they would carry "≤56% ceiling" and a bare "$120M" as hard figures the owner calls a scenario and not a bound, and would over-credit the February call. Six ❌ to fix before the file is final.
