# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

## 2026-05-01 PM — Wave 1 chunks 3-6 + Q1 CR sweep [PRUNED 2026-05-11; durable bits already in MEMORY/LESSONS]

**WAL Q1 transcript line-numbers (kept — useful for future quoting):**
- L22: opening — "decisive actions taken on two previously disclosed fraud-related credits"
- L28: LAM — "fully charged off the remaining $126.4 million balance of the loan to a fund of Leucadia Asset Management" + "we will not provide further commentary"
- L34: Cantor — "$29.6 million specific reserve... validated by current as-is appraisal values" + "$26 million" charged + recovery sources (UHNW springing guarantees, mortgage fraud policy)
- L106: leading-vs-lagging — "criticized assets were largely stable... special mention loans increased $78 million quarter-over-quarter, the change was not thematic"
- L154: revised guide — "core net charge-off guidance of 25-35 basis points... at or slightly above the midpoint of this range"

**Open backlog item:**
- "Juris banking" line — mentioned multiple times in WAL transcript as the "real surprise driver." Need KB row capturing what Juris banking actually IS. Research add: what business / counterparty / how does it monetize? (Investor Day May 12 may surface.)

---

## 2026-05-08 PM — May 8 Friday session [PRUNED 2026-05-11; durable bits in MEMORY findings]

Detail in MEMORY.md LAST SESSION (May 8 PM) one-line recap + commit history `d5d08d56` / `486aea0b` / `325dc8de` / `0d876199`.

---

---

## 2026-05-11 PM — Investor Day prep + tape break [PRUNED 2026-05-17; integrated to MEMORY LAST SESSION + Q&A overreach lesson durable in MEMORY Feedback]

Detail in MEMORY.md prior-session 1-line recap + LESSONS.md falsifier-status pattern.

---

## 2026-05-10/11 PM — WALTER LIAISON converged + V2.1 ship [PRUNED 2026-05-17; durable patterns in MEMORY References + LESSONS]

Detail in MEMORY.md References LIAISON entry + LESSONS.md 2 methodology entries.

---

## 2026-05-15 / 17 — Investor Day FINDINGS + SSB ladder + clean closeout

**Two-segment session: Investor Day forensic-read 5/15; SSB expiry-day ladder 5/15; quiet pause; Sun 5/17 closeout commit.**

**What worked:**
- Source archaeology via SEC EDGAR: WAL had filed THREE high-value docs that REGINALD missed between 5/11 PM closeout and 5/15 boot — 10-Q (5/11), Investor Day 8-K (5/12), and a secondary 8-K (5/12 dated 5/8). EDGAR `data.sec.gov/submissions/CIK0001212545.json` resolved all of them. Re-validates the curl pattern in MEMORY.findings.
- Bucket scoring discipline: scored Buckets A-E from prepared remarks ONLY (Slides 1-125), flagged Q&A as unscored. Resisted the temptation to assume modal U1 across all buckets without reading.
- Caught the **B3 trigger** cleanly: Slide 119 NCO guide 25-35bps held + footnote excludes LAM/Cantor → Q1 ex-fraud 39bps is ALREADY 4bps above the top of the range with mgmt NOT raising the guide and NOT acknowledging the tension. Exactly the pre-registered B3 fail pattern.
- Friction caught real-time: when Will said "commit," I flagged the WALTER/BOARD uncommitted-work isolation before staging anything. Per MEMORY [Agent Git Isolation] feedback. Clean REGINALD-only commit `6a20710a`.

**What I missed:**
- **WAL 10-Q was filed 5/11 PM same day as my 5/11 PM STATUS write — REGINALD missed it.** The Investor Day prep ship consumed the session; never checked EDGAR for the 10-Q. By 5/15 boot it was 4 days unread. Cost: RED §12.3 cross-credit inventory test (Schedule O / Table 16) — THE V2 inventory test — has been sitting in primary-source form for a week without being read.
- **Boot 9b grep wrong field name** — searched `cluster_mediating: true` when schema is `signal_role: cluster_mediating`. Tier (c) cluster-filter catch saved the analysis but tier (b) would have failed silently. Promoted to NEXT SESSION grep fix.
- Investor Day Q&A transcript not located — hit `investors.westernalliancebancorporation.com` archived replay + Seeking Alpha / TipRanks / Stocktitan / Yahoo Finance summaries. **Got the deck (full prepared remarks)** but no analyst Q&A. Findings file landed scoring 4 buckets fully + 1 partially.

**SSB expiry-day forensics (5/15 ~12:21 ET):**
- Tape moved hard in our direction: $93.27 open → $91.15 intraday low (-2.17% IDP)
- $95P bid $1.55 — pre-registered trigger worked ("bids should appear" once option ITM); but $1.55 is $2.24 below intrinsic at $91.21
- Roll path still CLOSED 5/15 as it was 5/8 (Sep $95P 0/0 bid/ask)
- New auto-exercise risk surfaced (5/8 memo didn't address) — DNE backstop added to ladder
- ⚠️ Quantity unknown — POSITIONS.md dropped qty col on 5/8 broker refresh; FORGE Mar 25 stale

**Things I noticed but didn't dig into:**
- Investor Day Slide 89 NDFI peer chart: WAL labeled "moderate" but chart text in my extract shows "13% 12% 12% 11%..." descending — can't tell from text alone where WAL sits. **PDF deck would be ground-truth.** If WAL is at 13% on the Ex-Mtg-Credit-AND-PE-Funds basis, that's a major DIVERGENCE from Q1 Slide 24's "WAL at cohort median 7%" framing. Could be reframing or could be different denominator. Worth checking against the 10-Q NDFI breakout.
- Investor Day Slide 113 stress test: mgmt-modeled "severely adverse" scenario assumes **5.3% total loan loss rate in 2026** with CET1 stressed to 9.0% (above min). The 5.3% loss rate already EXCEEDS the V2.1 Bear-fast scenario assumptions — mgmt is pre-positioning a "we can absorb worse than the bears model" narrative. **Worth a SCENARIOS.md cross-check.**
- Investor Day Slide 68 Mortgage Warehouse "Zero credit losses since 2010" framing does NOT address Apollo Atlas SP / non-bank servicer counterparty concentration. WAL still has ~$3.5B mortgage warehouse with stated zero-loss history but the V3 counterparty-quality test is whether THIS cycle's PFSI/loanDepot/Lakeview/Freedom stress reaches the warehouse book.
- WAL **Investor Day Q&A transcript hunt** is a meaningful open thread — Bucket A re-score could escalate verdict V2.1 → V2.2.

**One-liners cached:**

```bash
# EDGAR submissions index (verified 5/15):
curl -s -A "REGINALD research willie@research.local" "https://data.sec.gov/submissions/CIK0001212545.json"
# Path pattern for actual docs:
# https://www.sec.gov/Archives/edgar/data/1212545/<accession-no-dashes>/<filename>
# WAL Q1 10-Q: 0001628280-26-033054 / wal-20260331.htm  ← STILL UNREAD
# WAL Investor Day 8-K: 0001628280-26-033850 / wal-20260512.htm + wal_investordayx2026xfin.htm (deck EX-99.1)
# WAL 8-K 5/8: 0001628280-26-033851 / wal-20260508.htm (secondary)

# yfinance option chain pattern (verified 5/15 SSB):
.venv/bin/python3 -c "import yfinance as yf; t=yf.Ticker('SSB'); print(t.option_chain('2026-05-15').puts)"

# Boot 9b grep — CORRECTED schema field:
grep -lE 'signal_role: cluster_mediating' BOARD/SIG-W-*.md   # (NOT 'cluster_mediating: true')
```

**Convention question for next session:**
- WAL Investor Day Q&A transcript pattern — Q1 transcript was sourced via Motley Fool (paywall map per MEMORY findings); Investor Day transcript may land at SA / Motley / Investing.com on different timing. Should write a `WAL_TRANSCRIPT_HUNT.md` recipe if multiple tries fail, to systematize future event-day reads.

**One open externality I should track:**
- WALTER swept the working tree on 5/17 boot (commit `7a3ece9d`) — REGINALD's local commit `6a20710a` reached origin as `1b37fccc` rebased on top. **This is the cross-agent push-handoff working.** Working tree clean externally as of 5/17 closeout — next session can pull cleanly.

---

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*
