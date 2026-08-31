# HEARTBEAT ninth re-base — cold-read residue + the byte finding
**Written:** 2026-08-31 ~18:3x ET · **Owner:** PROME · **Status:** base COMMITTED with declared residue; the ⚠️ list below is NOT fixed

## What ran
Two **independent blind** cold reads (the second fresh, because the first had seen the fix list and was no longer blind).

| Pass | File size | Claims | ✅ | ⚠️ | ❌ | Verdict |
|---|---|---|---|---|---|---|
| Reader 1 (pre-fix) | 24,741 B | 58 | 34 | 16 | **8** | No |
| Reader 2 (post-fix, fresh) | 28,509 B | 54 | 30 | 18 | **6** | — |

**All 14 ❌ across both passes are FIXED.** The 18 ⚠️ from pass 2 are deliberately not chased — see the byte finding.

## ★ The byte finding — the reason this stopped
**23,868 → 24,741 → 28,509 → 30,551 B**, against a hard read cap of 32,550 B. Each correction pass cost **~2 KB**, because what a cold reader needs is *disambiguation* — bases, dates, directions, tie-breaks, "not the other thing with a similar name" — and that is prose, not data.
⇒ **Chasing the remaining 18 ⚠️ would have breached the cap**, and a breached cap silently truncates the boot read, which is strictly worse than a documented ambiguity. Stopped by the WQ-140 late-session rule (correction-count-keyed).
⇒ **The next re-base must be a STRUCTURAL SPLIT, not a rewrite.** A single surface carrying regime + levels + gates + book + calendar cannot also carry its own disambiguation. Registered as the successor design question.

## ❌ FIXED this pass (both readers) — recorded so the classes are searchable
1. **Headline contradicted the body** — "every registered trigger un-fired" while §8 fired two. True claim is narrower: zero fired-*unexecuted*.
2. **The file broke its own Brent-basis ban, twice** — once in the one-liner (fixed in pass 1) and then again in the canonical dashboard (missed by pass 1's fix, caught by pass 2). ⚠️ **A fix applied to one instance of a banned pattern and not the others is the characteristic correction-pass defect.**
3. **crc receipt did not reproduce** against the file it named (body crc vs file crc conflated). Both now stated.
4. **The archive was UNTRACKED in git** — every history pointer was local-box-only. Caught by mechanical pointer resolution, not by reading. Committed `c91e55c27`.
5. **HOM-01 unreadable**: a value *above* a ">+1.9%" line resolving to MISS, with no arm direction and no period basis on any FMHPI figure in the file.
6. **June FMHPI has two values** (+2.06% as-published, +1.81% as-revised) and the verdict used both without declaring which vintage governs which use.
7. **`FAL-01` / anchor GATE 1 vs `GATE-FALCON-001`** — two different instruments with confusingly similar names, one FIRM-NEGATIVE and one with fired legs, read as one contradictory gate.
8. **"Three statewide instruments disagree in sign"** — leg 2 is a county subset, leg 3 undated; the bolded headline asserted what its own body retracted.
9. **USD/JPY "still through 160"** printed beside 159.79.
10. **A stale grind-side claim** ("long end rallied on a hawkish shock", 8/28) sitting against the day's officials that went the other way.
11. **"§7 demands a mechanism"** — pointed at MIDAS's document while colliding with this file's own §7.
12. **The one undated distance sat in the list whose header promises dates** (BRT-26 rigs; also no series and no side).
13. **Branch letters (a)–(d) cited but never defined**; a fused "+4.03σ" in the same section that says do not fuse.
14. **"Markets CLOSED"** in bare present tense — the line most likely to be read wrong at 9am Tuesday.

## ⚠️ RESIDUE — shipped un-fixed, next session's list
- Kharg export collapse (1.98m → ~135k bpd): neither figure dated or sourced; sits opposite "loading resumed 8/12" with no time-ordering.
- MIDAS-06 branch boundaries **non-exclusive at 2.40** ((a) ≥2.40 vs (d) 2.20–2.40) and non-exhaustive (gold $4,050–$4,340.70 with DFII10 ≥2.40 fits no branch). MIDAS ruled 2.40→(a); the letter should say so. **This is live for successor rows — WQ-142.**
- §5 forbids quoting a live RED-FT-10 distance, then quotes the 8/28 one (0.23). Labeled, still self-undermining.
- The COT "99.8th percentile" is unusable as printed — its lookback is prohibited from being restated here and no path to the ledger is given.
- **Triggers without consequents (structural).** REG-T-02, GATE-HY-REKILL and GATE-TERRY-007 all say precisely when they fire and never what firing *does*. ⚠️ **Judged, not merely deferred:** consequents are `GATES.tsv`'s `consequence_on_fire` column and inlining ~30 of them would breach the cap. The fix is a sharper pointer, not imported content. Reader 2's own runner-up note is the model: the ⛔ kill-on-sight set is the only fully stranger-executable part of the file *because each entry names the false claim, the reason, AND the true replacement.*
- **Kernel section is not stranger-executable** — grades packets "fail legs 3+4" without enumerating the five legs, giving the `KERNEL/` path, or saying where carve-out ④ is defined. Recoverable only because the failing content is quoted. **This is the file's own declared blocker, so it is the highest-value residue.**
- Undefined state tokens carrying weight: "frame LOW stands" · "Channel 1 NOT re-opened" · "V20 KILLED" · "S5 3 / S1 NOT-FIRED" · "D-16" · "NEXUS 21/44/35" · "OZK-09 45%" (of what) · "Kalshi 0.48" (probability or price).
- Prohibitions with no "instead": the gamma board kill-on-sight names no replacement source and no re-measurement trigger; "publish the retirement, don't just delete it" names no venue or owner.
- WQ referents (98, 114) cited with no state attached; "3 QQQ" doesn't say shares vs contracts; **USO and XLE carry no level anywhere** though positions are quoted by strike — moneyness on the legs TERRY's concentration flag governs is uncomputable from the file.
- Unlocatable in-text referents (no path): MIDAS's I2 design letter §7 · WALTER's verify record · "RED's board" · KB-087/088 · VX-REG-18.04.

## Method note worth keeping
Reader 2 **recomputed** both crc32s, the GATES row count and every weekday assertion rather than accepting them — and resolved 11/13 pointers mechanically. The two findings no amount of re-reading would have produced (the untracked archive, the non-reproducing crc) both came from that mechanical layer. **A cold read that only reads is half an instrument.**
