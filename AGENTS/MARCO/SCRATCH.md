# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** session 28 — opened **2026-09-24 ~12:15 ET** (Thu), Will-directed boot + "catch up on any missed data"; Will ruled the MIA trigger basis mid-session; closed ~13:3x ET.

## CHANGES SINCE (session 27 → 28) — 5 days
- **PROME confirmed `ID-01`'s both-months reading 9/22** (packet in `inbox/processed/`) — recorded in STATUS UNRESOLVED + `KB-CAN-44/47`.
- WALTER lane: 1 item (SIG-W-20260917-008, Section-301 delay past today's Xi–Trump summit) — **info-only**, ZHAO owns. Drained + `board_log.tsv`.
- Pull at boot: tree clean, origin == HEAD (`5d5ae3f77`); nothing incoming.

## WHAT I DID (session 28)

### 1. MIA — the one Spirit-free FL leg — broke in August
- **Miami-Dade's own Traffic Report PDFs (Jan–Aug 2026 + Jul/Aug 2025), identity-checked parse** (total = intl + dom = deplaned + enplaned): Jan +0.42 · Feb +0.61 · Mar −1.76 · Apr −2.01 · May +0.52 · Jun −1.43 · Jul +0.10 · **Aug −5.69% YoY / −6.53% 2-yr** (4,289,986). Reproduces the carried Mar/Apr/May figures in MAR-24's notes. → `baselines/mia_airport_reported.tsv`, `KB-APT-44`.
- ⚠️ **Not yet a demand verdict.** Intl seats −6.02% (capacity-led; intl LF actually ROSE 85.1→86.5%). The one demand-flavored tell: **domestic load factor 85.2→81.1%**. No storm found on search, not ruled out.
- **Basis bridge (`KB-APT-45`):** BTS vs airport MIA YoY agree in SIGN on all 5 revised months (gap −1.17..+1.48pp); June's BTS first print (−5.48 vs −1.43) is the −4.05pp outlier. **BTS still ends at June** (re-pulled to scratch 9/24, byte-identical).
- **`MAR-24` 70%→80%.** Capped because **BTS May MCO was only −0.25%** — the 9/19 "MCO LOCKED" read is weaker than stated; Aug MCO unobserved. Resolver = BTS Q3 on the 2027-02 vintage, NOT 9/30.
- ⚖️ **WILL RULED 9/24: the MIA-2-consecutive trigger grades on MIA's OWN airport-reported count, BTS shown beside.** Written into `CLAUDE.md` (signal table + FL AIRPORT TRIGGERS item 3). **Trigger NOT met** (Jul +0.10). MAR-24 still grades on BTS.

### 2. Other catch-up prints
- **LVCVA July:** June's $ inversion did NOT persist — visitors +2.7%, RevPAR +3.2%, Strip gaming +3.6%; **air −7.6%** (YTD −6.9%). LVCVA credits a slow last summer (base). `KB-NV-03`; `VX-NV-01` annotated (Canadian leg still unrefreshed). August ES not out.
- **Aug CPS (BLS API live):** LFPR<HS **44.7%** (Jul 45.5 / Jun 43.1; Aug-25 47.5) — July counter-print partly reverted. Foreign-born LF **31,860k, YoY −379k** (Jul −550k), identity exact. `KB-WFD-12`. Consumer check on 43.1: only mail/archives cite it — no packets.
- **Checked, nothing new:** BTS (June), OFLC H-2A (still FY26 Q3 → `MAR-11` HELD 72%, note added), FL voter reg (Aug newest), Banxico CE81 (Jul newest), StatCan (Aug newest; tool re-run changed only the pull stamp).

### 3. Hygiene — both over-budget boot reads FINISHED rotating
- **`MEMORY.md` 49,058 → 22,694 B (70% of budget)** — carried 3 sessions, now closed. Verbatim move to `domain/sources/_archive/MEMORY_cold_20260924.md`; selection rule = guard now in code, already fleet auto-memory, or dated history. One-line pointers left. World-Cup event-mask **retired**.
- **`STATUS.md` 31,943 → 22,410 B (69%)** — the hot/cold split owed since s27. Cold → `_archive/STATUS_cold_20260924.md` + `_archive/STATUS_s28_rotated_20260924.md` (incl. a duplicate s26 header line that had been sitting in STATUS). Conservation-checked: every block is in hot or cold.
- Docket: off-vocab `ORANGE`/`YELLOW` fixed; 2 resolved rows (8/22 §338, 9/8 counter-tariff) → `thesis/TIMELINE.md`; 4 re-dated with reasons (energy re-spec → 10/1; Banxico state map → 10/1; Citizens chase → 10/1; StatCan BOP → Q3 11/27); **new rows: LVCVA Aug (~9/30), MIA Sep report (~10/28)**. `CALENDAR.md` August block rotated out, NEXT WINDOW rebuilt from the TSV.
- ⚠️ **Tool defect noticed, NOT fixed:** `tools/bts_airport_pull.py` stamps `Last real data refresh:` with the PULL date, not the newest data month (PAT-044 says data month). Also its argv parser treats `--help` as an airport code (harmless — errors before writing).

## NEXT SESSION
1. 🟠 **LVCVA August (~9/30)** — $ negative again ⇒ June wasn't noise; positive ⇒ month-only confirmed twice.
2. 🔴 **Banxico AUGUST (Oct 1)** — the 2nd forward print of the SDL-01 re-spec (boot flags it). Co-run the state-of-origin map.
3. 🔴 **ENERGY RE-ARM RE-SPEC (docket 10/1, 4th session carried)** — fresh forward window, `BZX26.NYM`-form contract. Energy re-accelerating (Aug gasoline +27.40% YoY).
4. 🟠 **~Oct 15:** StatCan Sep (`ID-01` leg 1, both-months) · NTTO Sep (`VX-1.02` −24.20% vs −25% line) · BTS July (check MCO — is it still negative?).
5. 🟠 **MIA September report (~Oct 28)** — decides the MIA-2-consecutive trigger on the ruled basis. If it fires: REGINALD + CARL, with the capacity-vs-demand caveat (intl seats) carried verbatim.
6. 🔴 **Channel 4 — EMMA/MSRB credit leg still unrun** (since 8/12); gates retire-or-hold.
7. 🟠 **Promotion flag owed to PROME** (carried from s27): `finding_threshold_spec_fails_before_world` COLD-tier, extended to n=5.
8. 🟡 Fix `bts_airport_pull.py`'s data-vintage stamp (see §3).
9. **Carried:** inbox LABOR 9/17 + ZHAO 9/18 unprocessed (not an inbox spawn) · CORAL Citizens PIF (docket 10/1) · FL-$ hole — **do not re-cite** · `VX-2.01` on an unrefreshed Jun-15 arrest rate · `VX-1.02` band doesn't name its 2019 period · USMCA-preference not primary-supported.
10. **Do NOT hunt a fifth Channel-1 transmission instrument.** v3.0 pre-commits against it.

## OPEN THREADS
| Item | Status |
|------|--------|
| ✅ **MIA trigger basis** | **Will-ruled 9/24** — MIA's own count, BTS beside. In CLAUDE.md |
| 🟠 **MIA Aug −5.69%: demand or capacity?** | Intl leg capacity-led; dom LF −4.1pp is the only demand tell. Sep report is the next read |
| 🟠 **MAR-24 at 80%** | Aug MCO is the unobserved leg (May −0.25%) |
| ✅ **MEMORY / STATUS read budget** | **CLOSED 9/24** — 70% / 69% |
| 🔑 **`ID-01`** | Both-months reading CONFIRMED by PROME 9/22; Sep print ~mid-Oct |
| 🟠 **SDL-01 re-spec: 1 of 2** | August ~Oct 1 |
| 🔴 **Energy re-arm** | Re-spec owed — docket 10/1 |
| 🔴 **Channel 4 EMMA/MSRB** | Unrun |
| ⏳ **Spirit seat deletion unsized** | Seats never measured |

## Mail state
**Inbox 2 UNPROCESSED** (LABOR 9/17 · ZHAO 9/18) — not an inbox spawn. **WALTER lane empty.** PROME 9/22 ID-01 packet processed (it asked only for a record).
**Sent:** nothing — no threshold fired (MIA trigger NOT met on the ruled basis). REGINALD/CARL will be packeted only if MIA Sep prints negative.

## PUSH STATE
Session 28 — see the closeout commit and the `safe-push.sh` receipt line.
