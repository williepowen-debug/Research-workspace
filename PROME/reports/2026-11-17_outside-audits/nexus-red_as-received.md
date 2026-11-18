# Do NEXUS and RED change anything?

**Date:** 2026-11-17 (evening ET). **Repository pin:** `origin/master` 78ed22bb9dc7 (2026-11-17 18:44 ET), full history (25,661 commits). Read only; nothing in the repository was changed.
**Question (follow-up 7 of 7):** has a RED objection ever changed a trade card, a desk's view or one of Will's rulings? Does NEXUS synthesis get cited or acted on downstream? How much of their output had no visible effect?

## The short answer

**RED changes things. NEXUS mostly doesn't.** Neither has changed where money went.

- **RED** wrote 57 formal challenges (February to November). For 23 of them, the target's own files or Will's ruling show the challenge changed something: 21 changed a desk's view, spec or estimate, and 2 changed a trade card or ruling. RED's own records claim 10 more, but the target's files no longer show it. The remaining 24 had no visible effect: 7 were answered and kept, 10 lapsed with no response, and 7 were RED challenging itself. Among the 50 aimed at someone else, the confirmed hit rate is 46%.
- **NEXUS** has already been tested by the system itself. A gate NEXUS proposed against its own seat counted Will's decisions from 8/8 to 10/7. **Only 1 of 370 had a NEXUS product as its deciding input.** The pre-registered result was "dissolve". Will overrode it on 10/14 ("NEXUS stays"). I extended the count to 11/17. There were 331 more decisions, and I found 2 more where a NEXUS finding was the deciding input, both about process rather than markets. NEXUS's headline product, the 26/41/33 scenario split, was retired on 11/10 as untestable (WQ-664).
- **Money:** every trade-card change I could trace to either desk ended at $0. RED's strongest win at the ruling level was the OZK and WAL sell rulings. Will ruled on 10/14, the sales were never placed, and about $600 of quoted value was lost (pass 4). Two NEXUS-shaped cards and one RED-built card were never filled.

⚠️ **Caveat that could change the read:** RED's quality grades are RED's own. Its "harmful-revision" ledger (2 harmful out of 24 graded, 8%) was graded by RED. It flagged seven rows for PROME to spot-check, and no record shows PROME ever did. I counted *whether* things changed, not whether the changes were right.

## RED: what happened to its 57 challenges

| What happened | Count | Share | Examples |
|---|---:|---:|---|
| Target changed its view, spec or estimate (confirmed in the target's own files or commits) | 21 | 37% | SAM ×7 (CHG-029 to 032, 039, 047, 048), VIOLET ×6 (033 to 038), REGINALD 025/026, BRENT 024, BROCK 044, CARL 049, FALCON/NEXUS 043, KERNEL 050/052 |
| Moved a trade card or a Will ruling | 2 | 4% | 054 bank-put book → SELL rulings; 042 → oil card built, never armed |
| RED records a change, target's files don't confirm it today | 10 | 18% | 004, 006, 007, 008, 009, 013, 014, 017, 020, 023 (February to April era) |
| Target or Will answered and kept their position | 7 | 12% | 011 (RED was wrong on oil), 040, 045, 046, 053, 056, 057 |
| No visible response: lapsed, expired or never answered | 10 | 18% | 001, 002, 003, 005, 010 (sat 120 days unanswered), 012 (lapsed), 015, 016, 019, 021 |
| RED challenging its own work | 7 | 12% | 018, 022, 027, 028, 041, 051, 055 |
| **Total** | **57** | | Row-by-row table: [red_challenges_classified.tsv](/mnt/project-files/nexus-red/red_challenges_classified.tsv) |

**Effect on Will's rulings.** I screened all 331 Will decisions from 10/8 to 11/17 for RED as an input. Five turned on RED's work:

| Ruling | What RED did | What happened |
|---|---|---|
| WQ-425 → WQ-428, WQ-429 (10/14) | CHG-054, written at Will's request, graded the OZK put STRONG to sell | Will ruled SELL on OZK and WAL. **Never executed.** About $600 of quoted value was lost by 11/10 (pass 4) |
| WQ-437 (10/15) | Five clarifications to CARL's auto-loan test | Will adopted them as worded |
| WQ-450 (10/20) | Network sweep found labor and consumer evidence never reached Will's HEARTBEAT | Will added a HEARTBEAT section |
| WQ-451 (10/21) | Sweep found "gold up while real yields up" had no owner | MIDAS was commissioned to own it |
| WQ-599 (11/6) | CHG-056 said TERRY's fleet-shrink sizing wasn't ready | Will declined the whole proposal. Consistent with RED, but Will gave his own reasons |

**A case where Will overruled RED.** In CHG-045, RED said to grade CARL's thesis-kill rule as written. On 8/16 Will chose CARL's re-spec instead (`PROME/proposals/2026-08-16_carl-row44-respec-optionA-RULED.md`). Under the re-spec the kill did not fire at Q3 (23 bp of a required 100 bp). Under the rule as written, the measure did decline a second time, and RED notes that move was all denominator. CARL's thesis survived on the re-spec.

### Clearest examples

**Changed something:**
1. **SAM, June 10 (CHG-031).** RED attacked SAM's 72% call that Japan's finance ministry would intervene. SAM cut it to about 35%, a bigger cut than RED asked for. The ministry then reported ¥0 of intervention. SAM's own files call it "the cleanest stamp" (commit 060abd20).
2. **VIOLET, June 10 (CHG-036).** RED's challenge moved VIOLET from leaning toward fading war volatility to standing aside, about five weeks before July's largest escalation. This is the highest-consequence revision in RED's book, though the grade is RED's own.
3. **BROCK, August 7 (CHG-044).** RED showed that BROCK's escalation thresholds were picked first and justified afterward. BROCK checked its own spec and conceded all four findings.
4. **Bank puts, October 14 (CHG-054).** The only case where a RED challenge changed one of Will's trade rulings, and the ruling then wasn't carried out.

**Changed nothing:**
1. **CHG-010 (BROCK, April).** It sat ACTIVE and unanswered for 120 days until RED's own audit found it.
2. **CHG-042 (July oil).** RED was right that the "premium is reversible" consensus was wrong: Brent went from $88 to $100 with no pullback. TERRY built a card on it (TRY-FIRE-006). The card never armed, and Will retired it on 8/18 with "$0 at risk from build to retirement". Right call, no position.
3. **CHG-011 (April oil ceiling).** RED was wrong, and Dated Brent printed $141 within three days. This one cut the right way: nobody changed anything because of it.

**How RED spends its time (estimate from commit subjects, June onward, 429 commits):** about 19% are challenge work, 35% are closeouts, boots and housekeeping, 18% are grading its own predictions and gates, and 10% are Kernel or governance reviews. Treat these as rough, keyword-based shares.

## NEXUS: is its synthesis used?

**The system's own test, GATE-NEXUS-SEAT-01.** NEXUS proposed this gate against its own seat on 8/8. The rule: count Will's decisions from 8/8 to 10/7 whose deciding input was a NEXUS product. Three or more meant the layer pays; zero or one meant a dissolution proposal. PROME's count was 1 of 370 (WQ-341) and NEXUS's contest agreed (`PROME/reports/2026-10-07_nexus-seat-01-candidate-list.md`). That one case was "root B is unowned". It led to two desk reads, VULCAN and LIQUID, and no owner was assigned. VULCAN found the mechanism "fails on the letter". On 10/14 Will declined the dissolution: *"NEXUS stays."*

**My extension, 10/8 to 11/17.** There were 331 ruled decisions. 21 mention NEXUS. Here is how they break down:

| Kind | Count | Rulings |
|---|---:|---|
| NEXUS finding was the deciding input, on something other than NEXUS itself | 2 | WQ-401 (NEXUS designed the unread-inbox alert that PROME built) · WQ-671 (NEXUS found five desks naming four different owners for the December Fed price, so Will gave it to ORACLE) |
| About NEXUS's own instruments (its charter, split, credit letter) | 4 | WQ-394, WQ-459, WQ-519, WQ-664 |
| NEXUS only mentioned (wake slates, one of several inputs) | 15 | e.g. WQ-569: NEXUS's term-premium note was one of four inputs to a TERRY launch |
| **Market or trade decisions turned by NEXUS** | **0** | |

**Trade cards.** NEXUS shaped two cards, and both ended at $0:
- **FXY call card, August 4.** NEXUS showed that the Fed, BOJ and Treasury moves were one policy stance, not three independent votes. TERRY cut the recommended size from 9 contracts ($450) to 5 or 6 ($250 to $300). The card died on its own trigger on 8/7, never filled. It was a real effect, on a trade that didn't happen.
- **TLT put spread, November 2.** NEXUS was named thesis owner (its October 31 term-premium packet). Will declined it on 11/4 (WQ-592). Never filled.

**Desks.** Desk commit subjects mention NEXUS 670 times, but 463 of those are desks writing their `NEXUS_BRIEF.md`, which is input *to* NEXUS. I found only about five where a desk acted on something NEXUS sent. All 164 NEXUS packets to desks and PROME were marked processed, so they are read. Reading them just rarely changes anything.

**What NEXUS costs to feed.** 2,523 commits, 9.8% of all history, touched a desk's `NEXUS_BRIEF.md`. Desks maintain 46 brief files, updated most sessions, for a layer whose output turned 3 of roughly 700 Will decisions in 101 days.

**Its headline product is gone.** The 26/41/33 scenario split had no working test after 11/9. On 11/10 Will retired it to "judgment, no number" (WQ-664). Earlier, on 9/18 (WQ-224), it had already been carried as "currently un-falsifiable".

## Share with no visible effect

| | Output | No visible effect |
|---|---|---|
| RED challenges | 57 | **24 (42%)**, or 34 (60%) if RED's unconfirmed early claims don't hold |
| RED challenges aimed at others | 50 | 17 (34%), or 27 (54%) on the same basis |
| NEXUS, Will decisions 8/8 to 11/17 | about 700 rulings | about 697 (over 99%) had no NEXUS deciding input |
| NEXUS products overall | 164 packets and about 330 commits since June | about 6 traceable effects, so roughly 95% or more had none (an estimate; I traced effects, not every packet) |
| Trades by either desk | | **No executed trade changed by either desk** |

## Two things I noticed along the way

- **Four commit hashes RED cites as proof of target changes no longer exist.** These are 79ea030b, f9552e2c, c877b84b and 34ef1547, all from June. They were probably rewritten by the June history scrub. The target files themselves still exist, so the claims check out by file but not by the cited hash.
- **RED reused challenge numbers.** The bank-put challenge was issued as CHG-RED-052, a number already used, and renumbered to 054. TERRY's cards still say 052. Pass 5 found the same ID-reuse problem in RED's forecast ledger.

## Method and limits

- RED challenges come from `AGENTS/RED/workbook/CHALLENGES.tsv`, all 57 rows. For each one I looked for the target's response at the target: other desks' commit subjects citing the challenge, current-tree citations outside `AGENTS/RED/`, and the response files named in the resolution. Classification is my reading. Changes RED claimed with no target-side trace went into their own bucket rather than "changed".
- Will's rulings come from `PROME/registry/WQ_LEDGER.tsv`, a keyword screen and then a read of each hit. For 8/8 to 10/7 I reuse PROME's own list, which NEXUS contested and which matched. I did not re-read all 370.
- "No visible effect" means no record I could find. A desk can be quietly influenced by something it read. This audit can't see that, and NEXUS's case for itself rests on exactly that kind of effect.
- Whether a change was *good* is not graded here. That is the harmful-revision question RED graded itself on.

---

## Copy-paste block for PROME

```
PROME — findings from an outside read-only audit of NEXUS and RED (pin 78ed22bb9dc7, 2026-11-17). Please verify each before acting; nothing here is a ruling.

1. RED's harmful-revision ledger (AGENTS/RED/CHALLENGE_IMPACT_LEDGER.md, frozen 10/15) asked PROME on 7/31 to spot-check seven self-graded rows (026 first, then 008, 018, 022, 027, 028, 041). I found no record that the spot-check happened. Either run it or record that it was dropped.

2. GATE-NEXUS-SEAT-01 counted 1 of 370 decisions (8/8-10/7), and Will kept NEXUS on 10/14. Extending the same rule to 10/8-11/17 gives 2 more (WQ-401, WQ-671), both process, and 0 market or trade decisions. The split it published was retired on 11/10 (WQ-664). Put that count in front of Will in plain words once, with the cost: 2,523 commits (9.8% of history) touched desk NEXUS_BRIEF.md files. Ask whether he wants NEXUS's role restated (for example, contradiction-finding like WQ-671 only) or the brief-writing duty reduced. It is his call; he already ruled once.

3. RED changed desk views in at least 21 of 57 challenges, but no RED or NEXUS work has changed an executed trade. The one ruling RED moved (WQ-428/429, SELL OZK and WAL puts, 10/14) was never carried out. OZK Nov-20 40P expires Fri 11/20. Surface the current state to Will once.

4. CHG-045: Will chose CARL's re-spec (Option A, 8/16) over RED's "grade as written". Under the re-spec the kill did not fire at Q3. Under the rule as written the measure fell a second time, which RED attributes to the denominator. RED does not recommend reopening. No action unless Will asks; record it as a known divergence.

5. Hygiene: (a) four commit hashes RED cites in CHALLENGES.tsv as target proof (79ea030b, f9552e2c, c877b84b, 34ef1547) no longer resolve, probably because of the June rewrite; ask RED to repoint them to file paths. (b) TERRY's OZK and WAL cards still cite "CHG-RED-052" for what is CHG-RED-054; a one-line note on each card is enough. (c) Ten challenges lapsed or expired with no target response (incl. CHG-010, unanswered 120 days). Consider requiring a target reply date on every new CHG row.

Report: /mnt/project-files/nexus-red/2026-11-17_do-nexus-and-red-change-outcomes.md (in the audit project, not the repo).
```
