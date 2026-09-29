# NEXUS — proposed fixes from the 9/29 debrief (DRAFT for Will; uncommitted until he reacts)

**Context:** 9/29 session after 5 days dark — full review, WQ-340 read, three read-cap rotations, three self-defects found (stale L2 · wrong Panama notice ID · M-08 forcing condition with no magnitude), brief standard visibly degrading, split blind to credit. Each item: what it fixes · owner · cost · the decision needed. **$0 in all cases; nothing here touches a position, a gate letter or a threshold.**

## A. NEXUS-local — I can do these on my own authority (charter edits, inline-first)

| # | Fix | What it prevents | Cost | Ask |
|---|---|---|---|---|
| A1 | **Boot step "self-letter audit":** before reading any brief, re-read every NEXUS-registered letter (L-rows, matrix forcing conditions, PRED resolvers) against its resolver and check three things — has a date · has a magnitude · resolver still exists at the owner. Any row failing one is fixed or marked DEFECTIVE before the pass. | L2 carried a resolved item 33 days; M-08's forcing condition had no magnitude; "A-33" cited a notice that no longer existed. Same class each time: I write rules faster than I re-check them. | ~5 min/boot | none — encode |
| A2 | **Rotation moves from closeout to BOOT:** if any owned surface is ≥75% of budget at boot, rotate to <70% *before* writing. Pair with a per-section byte guide in the STATUS template (split block ≤2 KB · matrix ≤8 KB · map ≤4 KB · rest ≤8 KB). | Entered today at 100%+ on two surfaces; three rotations mid-session; a full-pass regrows ~10 KB. | ~5 min/boot | none — encode |
| A3 | **Digest readers become a standing boot instrument:** three fresh-context Opus readers with a fixed digest schema (header/pin · VIEW · moved-since · cross-domain · forward · NEXUS-named · cross-brief disagreements). Logged in `brief_fallback_log.tsv` with a new cause `digest`. NEXUS still reads load-bearing owner artifacts directly. | Reading 27 briefs myself would consume most of a session's context on inputs; today's readers caught the stale L2, REGINALD's retracted NFP figure and three fleet-clock disagreements. | ~3 Opus spawns/full pass | none — encode; note the token cost for Will |
| A4 | **Will-facing page cap:** any read addressed to Will ≤ 6 KB, with "the whole story" ≤150 words at the top; evidence tables go to a companion file. | WQ-340 asked for one page; I delivered ~14 KB. | none | none — encode |
| A5 | **Cold-read after any full-file rewrite** (the `coldreader` instrument) before commit, when the rewrite is a rotation or a re-base. | Two full STATUS rewrites today, audited by obligation but not by a reader. | 1 Opus spawn/rotation | none — encode |
| A6 | **Every NEXUS obligation gets a DOCKET wake row** at registration (done for PRED-50 = L553; generalize to L11/L13 grades and the FORUM-7 CONCUR packet). | ON-DEMAND means every boot is a backlog; dated rows are the only thing that wakes this desk. | none | PROME registers the rows I packet |

## B. Fleet-level — PROME / DAEDALUS / WALTER items (I packet; they own)

| # | Fix | What it prevents | Owner | Ask |
|---|---|---|---|---|
| B1 | **Brief standard enforcement at owner closeout:** `read_cap_check` for the owner's own `NEXUS_BRIEF.md` in the closeout chain; >14 days since refresh ⇒ a mandatory STALE banner at the top; over the hard cap ⇒ blocks the closeout. | BOND's brief was 140% of the cap; LIQUID's body 37 days old; BROCK's header 9/02; REGINALD's still carries a retracted NFP figure. Today's readers worked around it; the standard is what should. | DAEDALUS (wiring) · PROME (ruling) | PROME to register |
| B2 | **"Registered event inside a dark window" detector:** WALTER's WATCH_FOR matcher already exists (WQ-295 R3); add a rule that a matched phrase whose owner has no session in N days routes to PROME as a dark-desk flag, not only to the owner's inbox. | PJM's 4th emergency and the UWM servicer downgrade each reached no surface for days because the owner was dark. PROME's L487 names the class. | WALTER + PROME | PROME to register |
| B3 | **Root-owner map:** every root on the NEXUS antecedent map has a named owning desk, kept on `_NETWORK.md` or ROSTER. Today's gap: "AI disrupts incumbent cash flows" (Root B / T-27). | A root that three desks touched and none owned. | PROME | **WQ-341 already open** |
| B4 | **One fleet calendar:** DOCKET is canonical for event dates; desks cite it rather than carrying their own (T-28: MU, METI, BOJ each a day apart across desks). A weekly claim-check pass over dates that appear on ≥2 surfaces. | A NEXUS row graded on the wrong day. | PROME + `claim_check.py` | PROME to register |
| B5 | **Continuous-futures roll detector in `fetch.py`:** flag any continuous ticker (`BZ=F`, `CL=F`, `HO=F`) whose front month changed since the last pull; print both contract months. Companion to the L462 evening-bar detector. | The `BZ=F` Nov→Dec roll read as "Brent −5.6% / −8.6%" on ≥2 surfaces — the same identity-keyed class that produced the 9/14 crack error, recurring monthly as predicted. | FORGE tools (PROME) | PROME to register |
| B6 | **Strict-vs-inclusive stated in every letter:** `STRICT_TEXT.md` requires each threshold to say `≥` or `>` and a tie rule. | HY printed exactly 280.0: canon counted it (3-of-3), strict readers did not (2-of-3) — two desks, two counts, one number. | DAEDALUS | DAEDALUS to encode |

## C. Will decisions — already registered or needing a word

| # | Decision | My recommendation | Where |
|---|---|---|---|
| C1 | Owner for the AI-disruption root | HOLD until PRED-50 grades (~10/9), then VULCAN bounded sub-read + LIQUID credit expression — PROME's rec, I concur. | **WQ-341** |
| C2 | A credit leg for the 2–6wk split | NOT NOW under the frozen 9/02 letter — PROME's rec, I concur, **with one addition:** if PRED-50 CONFIRMS, the successor gate at 10/16 should be *required* to admit a credit-class candidate, not merely allowed to. | **WQ-342** |
| C3 | NEXUS cadence: ON-DEMAND (declared) vs a dated weekly floor | **Add a dated weekly wake (Tue) as a DOCKET row, keep ON-DEMAND as the token.** This week's five-day gap covered the largest credit move of the quarter. Cost: one Opus session/week when nothing has moved; the boot would be short. | needs your word; PROME registers |

**Not proposed, deliberately:** any change to the split's letter (frozen), any re-tuning of a gate, any new threshold "because today's level is nearby."
