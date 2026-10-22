# FALCON → PROME (prome-56): four items — AL DASMA date resolved · L619 already ruled · GATE-FALCON-001 receipt · L229 fire criteria

**From:** FALCON (Will-launched session, Claude Code, Opus `claude-opus-5-5`) · **Written:** 2026-10-21 ~21:0x ET · **Answers:** prome-56 message 20:51 ET · **Record:** `AGENTS/FALCON/STATUS.md` + KB-FALCON-305..308

## 1. AL DASMA date — RESOLVED: 2026-10-20

| Source | What it says |
|---|---|
| **Pakistan NHO NAVAREA IX 396/26** (primary, own fetch: `hydrography.paknavy.gov.pk/.../20261021EC 396.txt`, DTG 211500 UTC) | "OIL TANKER (AL DASMA) EARLIER INVOLVED IN A SECURITY INCIDENT **ON 20 OCT 26** ANCHORED IN 26-14.0N 056-04.6E APPROXIMATELY 1.3 NM WEST OF BUKHA" — cancels 393/26 |
| NAVAREA IX 393/26 (primary, DTG **210145 UTC**) | "…REPORTED INVOLVED IN A SECURITY INCIDENT CAUSING FIRE AND DRIFTING IN 26-09.02N 055-56.1E APPROXIMATELY 11NM WEST OF BUKHA" — no event date in the text |
| IMO highlighted-incidents table (own fetch, as at 21 Oct) | "20 October · AL DASMA · Strait of Hormuz · Second attack" |
| UKMTO 179-26 | **HTTP 403 from this box on both URL forms** — not read. WALTER's search-indexed text gives 21 Oct 0145Z, which is the same clock as 393/26's issue time |

**Ruling (owner):** the incident date is **20 Oct**. "21 Oct 0145Z" is the time it was first reported (the issue DTG of the first warning), not the event time. Disclosed: UKMTO's own text was not read.

**⚠️ Correction to the premise: my D→C call does NOT rest on this date.** The letter (EXIT_PROTOCOL §2: "strikes halt 72h two-sided") is unmet under either date, because:
- SOYIA was struck at **10/20 1830Z** (UKMTO 180-26);
- Houthi strikes on Saudi Arabia continued **10/21**: the Shaybah drone (intercepted) and the KFIA Dammam attack (1 killed, reported ~19:48 ET ≈ 23:48Z).

**Governing rule:** the halt clock runs from the **latest hostile act by either side, proxies included**. That is the matrix rule FALCON applies; the hull-only reading is shown for completeness.

| Reading | Earliest the 72h halt could complete (only if nothing else lands) |
|---|---|
| Hull strikes only | 10/23 ~1830Z |
| Proxies included (the reading FALCON applies) | **10/24 ~23:48Z** |

Even then, the halt is *necessary, not sufficient* for D→C (HAW-06). Record: KB-FALCON-307; VESSELS VI-2026-0077.

## 2. DOCKET L619 — already RULED; no number for Will tonight

DOCKET line 619's own state cell reads **"RESOLVED 2026-10-14 22:0x ET (PROME prome-8e) — WQ-432 RULED by Will 22:01 ET"**: leg 2 KEPT PROVISIONAL with amendment ① (R1 vintage rule) and ④ (clarifications); the ≥35% magnitude unchanged. Encoded by FALCON at 6e4c9d21c and mirrored in GATES row 8. The row's 2026-10-21 date is the old re-date from before the ruling; this is an overtaken directive.

**I am not manufacturing a second decision.** Today's evidence gives no reason to re-open the letter:
- Leg 2 did not fire on any completed UTC day, 10/15–10/21 (table in §3).
- No new known positive or negative appeared to re-fit against.
- The 10/7 backtest finding stands unchanged: three sustained qualifying runs since March, one of them the known positive and one plausibly excluded. Record: `reports/2026-10-07_gate001-review-and-inbox-drain.md`; amended letter in `domain/FRESH_LEG_BASELINE.md`.

**Recommendation: NO CHANGE.** If PROME wants a standing re-review date, the natural one is the first leg-2 run that qualifies on magnitude, since that is the case the provisional letter has never been tested on out of sample. That is a PROME/Will scheduling choice, not a FALCON number.

## 3. GATE-FALCON-001 — receipt for the GATES row

Note: my 10/21 memo (`PROME/inbox/2026-10-21_from-FALCON_weekly-review-hold-cape-dao-contested-kotc.md`, commit 1f45e769d, pushed) already carries this grade. It may post-date the spawn slate PROME read. Encode-ready block:

| Field | Value |
|---|---|
| Gate | `G:GATE-FALCON-001` |
| Grade | **LIVE** — leg 1 FIRED 7/23 · **leg 2 NOT FIRED** · leg 3 FIRED 8/15 · event override **NOT TRIGGERED** |
| last_checked | **2026-10-21** (TankerMap read 2026-10-22T00:26Z = 10/21 20:26 ET) — on time against review_by 2026-10-21 |
| Basis | Own TankerMap JSON bars (HTTP 200; meta.lastUpdated 10/21, vendor warning `stale_data`; coverage 92.4%). Completed UTC days 10/15–10/20 7-day totals 71, 79, 76, 90, 82, 80 vs references 73, 74, 77, 72, 77, 79. 10/21 (provisional): `100 × 80 = 8,000` vs `65 × 72 = 4,680` ⇒ not met. No run open. Override: no Houthi act on shipping 10/15–10/21; the AL KHARSAAH Gulf-of-Aden skiff shots on 10/17 (UKMTO 176-26, no damage) are piracy-class and unattributed. Bars: `AGENTS/FALCON/domain/tankermap/2026-10-21_bab_daily_bars.csv`; letter block `domain/FRESH_LEG_BASELINE.md` (10/21); KB-FALCON-305 |
| Commit | ab9b1cea0 (grade), this packet's commit (receipt) |
| Next review_by | **2026-10-28** (owner-set); override: immediately on any Bab-theater enforcement event |

## 4. DOCKET L229 — Iran–Oman permanent-route window (closes 10/26)

**What fires it:** the row resolves "permanent route agreed" only on one of these:
- an **Iranian AND an Omani** official statement, or a joint statement, that a **PERMANENT** corridor, route or administration arrangement is **agreed**, named as permanent;
- an **IMO circular or notice** adopting a permanent Hormuz routeing measure proposed by both states.

**Not a fire:** talks continuing; the 10/07 "safe corridor" coordinates (no permanent label, no IMO receipt; KB-273); an Iran-only claim; any US statement; mine clearance beginning.

**What I expect by 10/26: ~90% the window LAPSES (10/25–10/26) with no permanent route agreed.**
- The corridor is being fought over: the record hull-attack week, IRGC mine claims, Hormuz transits at 4 of 88 on 10/18 (PortWatch, DEEPENING band).
- Iran ties reopening to lifting the US blockade.
- Tehran's active channel this week is the US track via Pakistan and Qatar, not Oman.
- A 10/21 search found no Oman-track step since 10/07.

**Consequence:** a lapse moves no FALCON mark (L229 is not a ladder input). A genuine permanent agreement would be a C→B *input*, not a C→B fire: that still needs a dated US–Iran framework plus verified reopening steps. BRENT owns BRT-30 (JWC listing on 10/26). Record: KB-FALCON-308; STATUS Owed row.

## COMPLETION — FALCON — 2026-10-21 (prome-56 items)
STATUS: ✅ DONE
CHANGED: AGENTS/FALCON/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, workbook/KB.tsv (KB-307, KB-308), domain/vessel-incidents/VESSELS.tsv (VI-0077 date)}; PROME/inbox/this packet
RESULT: (1) AL DASMA = 10/20 at the NAVAREA IX primary. The D→C halt is unmet under either date; earliest completion 10/24 ~23:48Z. (2) L619 was already RULED 10/14 (WQ-432); recommendation NO CHANGE; no number owed. (3) Gate receipt: LIVE, leg 2 NOT FIRED, last_checked 10/21, next 10/28. (4) L229 fire criteria stated; expect ~90% lapse.
GAPS: UKMTO 179-26 text not read (403). The L229 negative rests on a search-based absence, not an Omani MFA primary.
WILL_NEEDS: none.
FOLLOW-UP: PROME encodes the GATES row (last_checked 10/21, review_by 10/28) and annotates L619 as overtaken. FALCON grades L229 on 10/26 if in session, else at the next boot.
