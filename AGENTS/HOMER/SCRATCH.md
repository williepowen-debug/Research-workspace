# HOMER SCRATCH — 2026-09-29 (Tue) PM boot sweep + band rulings → handoff

**Purpose:** Ephemeral session handoff. Read at boot; rewritten at closeout. Durable findings → `workbook/` + `LESSONS_COLD_2.md`; live state → `STATUS.md`.

---

## ✅ WHAT CHANGED THIS SESSION

1. **Boot sweep** (Will: "sweep your start up files for anything old/stale/broken") → PROME prome-82 relayed Will's go on the fixes. **Charter edits were held for Will's own word** (harness rule: never edit CLAUDE.md on a peer's ask), then installed when he said "go ahead."
2. **Charter** 52,746 → ~38KB. Narrative moved verbatim to `archive/CLAUDE_charter_history_2026-09-29.md` (script-checked: every original line is in one or the other). Two cold reads, 8 ❌ fixed. **Closeout step 5b is now 4b** (docket sweep BEFORE the brief fold). **90+/FC band basis ruled = ICE First Look.**
3. **Servicer watch: Class A FIRED 2026-08-07** (Fitch UWM BB- → B+), found 53 days late. KB-HOMER-033; REGINALD note `c80af1ffa`. ⚠️ **Fitch primary still owed** (fitchratings.com blocked to this client).
4. **Will ruled A3/A4** (AskUserQuestion, after CATO review f139c5db7): rent breadth on Apartment List, 20/40/55 → **Sep 46/100 ORANGE**; national FC STARTS 100/130/175K → **Q2 81,935 below Yellow**. Tool `tools/rent_breadth.py` + frozen roster + input extract under `workbook/rent_breadth_inputs/`. **CATO broke v1 (column-position pairing); fixed to calendar-date pairing** — LESSONS §53.
5. **A2 rider encoded** (KB-HOMER-032). **3c** link packeted to CARL (`64d35bf5f`); CARL is DARK.
6. **Data:** Case-Shiller July +1.93% (primary) · Miami-Dade Aug condo · NAR Sept date = Tue 10/13 (issuer-stated).
7. **Docket:** 20 resolved rows archived (`archive/CATALYSTS_RESOLVED_2026-09.tsv`, crc 0x13dc1b4d); new rows: TX auction monthly, BEA RFI, read-cap 12/02, Apartment List monthly.

## 🔴 FIRST WORK NEXT SESSION

| # | Item | Why |
|---|---|---|
| **1** | **FMHPI Aug (Wed 9/30)** and **PMMS (Thu 10/01) graded against the pre-registration** (`reports/2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md`) | PMMS RED hold/soften/lift is pre-registered |
| **2** | **Trepp Sept DQ (~10/01)** — third month of absent MF mat-adj ⇒ execute the dated kill or grade it | Docket row, dated kill |
| **3** | **Texas October auction list (~10/01–05)** + **Realtor.com Sept (~10/01–03)** | New recurring row; C2 observation |
| **4** | **CARL's 3c ack by 10/05**, then **build 3c by 10/09** into `thesis/THESIS.md` | Silence ⇒ build as proposed, CARL side UNCONFIRMED |
| 5 | Fitch primary for the UWM downgrade | The Class A grade rests on two secondaries |
| 6 | Owed from the thesis defect register D2–D4: Fannie/Freddie MF DQ 2022–24, MBA FHA SA history, NAHB HMI table | Before the 11/20 formal grade |

## ⚠️ OPEN / UNSETTLED
1. **HOM-02** open; MBA Q3 NDS (~mid-Nov) decides.
2. **Fannie's −5bps** is mod-suppressible; pair with the Q3 10-Q MF provision (~late Oct).
3. **Rent breadth first live refresh** = Apartment List October file (~10/27–31): run with `--prior-file=workbook/rent_breadth_inputs/Apartment_List_2026_09_roster100.csv`, report revisions.
4. **Gated at this box:** MBA 403 · fitchratings.com blocked · miamirealtors.com empty to curl · spglobal press reachable 9/29 PM (403 in the AM).
