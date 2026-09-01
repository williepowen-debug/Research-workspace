> **WALTER handoff — SIG-W-20260901-013** · role: **ACTION** · precedence: ROUTINE
> Source batch: BM-20260901-02 item  (Will-requested news sweep).
> Move this file to `inbox/WALTER/processed/` when consumed.

---

---
signal_id: SIG-W-20260901-013
date: 2026-09-01
time_dispatched: 2026-09-01T21:52Z
origin: Will-requested news sweep 2026-09-01 ~22:1xZ (BM-20260901-02 item 10). NHK report of the G20 sideline meetings as carried by Bloomberg / investinglive / SCMP / Investing.com; BOJ pricing per MUFG via FXStreet.
source: Bloomberg 2026-08-31 "Bessent Tells Japan Officials Rate Hikes Needed, NHK Reports"; investinglive "Bessent met Ueda, Katayama at G20, pushed for BOJ hikes, NHK reports"; SCMP; Investing.com (Treasury under secretary to NHK: fiscal-sustainability path + rate increases as the "next policy step"); FXStreet/MUFG 2026-09-01 07:28 GMT (92% September hike priced). JGB 10Y 3.00% carried in SIG-W-20260901-006.
domain: JAPAN_BOJ
cluster: ASIA_CHINA
precedence: ROUTINE
action: [SAM]
info: [BOND, LIQUID, HANS]
entities: [Scott Bessent, Satsuki Katayama (Finance Minister), Kazuo Ueda, G20 finance ministers meeting (Asheville NC), Bank of Japan September meeting, JGB 10Y, USD/JPY, FY27 budget requests ¥143T]
signal_type: context
confidence: 0.80
verdict: On the G20 sidelines in North Carolina (Ueda on Sunday 8/30, Finance Minister Katayama on Monday 8/31), Treasury Secretary Bessent told both that Japan's next policy step should be rate increases, and — per a Treasury under secretary to NHK — a clearly shown path to fiscal sustainability. Markets price a September BOJ hike at ~92% (MUFG); the 10Y JGB touched 3.00% on 9/1. Same venue, same day as Nagel's rebuke of the US euro sale (SIG-W-20260901-003): the US is publicly directing Japanese monetary policy while being publicly criticised for its own FX operation.
consumer_lens: The US side of the 7/31 intervention is now doing in words what it did in euros in July — pushing the yen's fundamentals from Washington. For SAM's ladder the live question is the BOJ's forward guidance in September, not the hike itself, which is priced.
---

# 🟡 ROUTINE — Bessent told Katayama and Ueda at the G20 that Japan's next step is rate hikes; a September BOJ hike is ~92% priced

- **Who / when / where:** Bessent met **Ueda on Sunday 8/30** and **Finance Minister Satsuki Katayama on Monday 8/31**, on the sidelines of the G20 finance ministers' meeting in **Asheville, North Carolina** (NHK, via Bloomberg / SCMP / investinglive). Message per a Treasury under secretary to NHK: show markets the path to **fiscal sustainability** and **interest-rate increases** as Japan's next policy step. Earlier Bessent line (Bloomberg interview): BOJ is "behind the curve."
- **Pricing:** **~92%** for a September BOJ hike (MUFG via FXStreet, 9/1 07:28 GMT); JGB 10Y **3.00%** on 9/1, first since 1996, with record **¥143T FY27 budget requests** as the domestic driver (`SIG-W-20260901-006`).
- **Same venue, opposite direction:** Bundesbank's Nagel used the same G20 press conference to criticise the US for the unconsulted 7/31 euro sale (`SIG-W-20260901-003`).

**What this is not:** not a BOJ decision, not an intervention datum, not a level change for any SAM band. USD/JPY 160.15 at the 9/1 pull.

**Confidence 0.80** — NHK-sourced via four outlets; the under-secretary quote is paraphrased by NHK.
