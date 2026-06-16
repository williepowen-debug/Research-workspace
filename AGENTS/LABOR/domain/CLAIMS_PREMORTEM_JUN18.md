# CLAIMS PRE-MORTEM — Thu Jun 18 (w/e Jun 13)

**Built:** 2026-06-16 (pre-print, so the response is decided before the number, not improvised).
**Print due:** Thursday Jun 18 ~8:30 ET. Initial claims w/e Jun 13 + continuing claims (1-wk lag, w/e Jun 6).
**Last:** IC 229K (w/e Jun 6, highest since Feb); 4-wk MA 219K (3rd straight ↑); CC 1,795K (+24K). Cons for Jun 18 ~ low-220s.

> **Why this matters:** claims is the cleanest *realization-layer* read between now and NFP June (Jul 2). The whole bearish thesis is currently "structure deteriorating, realization holding." Claims is where realization would crack first. A break here is the single thing that re-arms the demand-weakness leg.

---

## DECISION TREE (decide now, execute Thursday)

| Print (IC, w/e Jun 13) | Read | Claims vector | Cross-agent action |
|---|---|---|---|
| **< 215K** | Drift REVERSING — pullback toward range | hold 2 🟡 (or note ↓) | None. Note "drift not durable" in STATUS; nudges thesis a hair more neutral. |
| **215–229K** | Drift continuing / no new info | hold **2 🟡** | None. STATUS one-liner. This is the base case. |
| **230–250K** | **ACCELERATING** — 2nd consecutive upside, MA likely 4th ↑ | upgrade **2→3 🟠** | 🟠 heads-up to CARL + REGINALD (not a fire): "claims accelerating, not yet sustained-breach; watch w/e Jun 20." Re-arm KELYA watch (not the position). |
| **251–300K (single)** | **TRIPWIRE HIT — but ONE print ≠ "sustained"** | upgrade **3→4 🔴** | **ARM T-01, don't fire-confirmed.** Send 🟠→🔴 *provisional* signal to CARL + REGINALD: "250K breached on a single print; T-01 arms; CONFIRM on 2nd consecutive >250K (w/e Jun 20, Jun 25 print)." Per EXIT-RULE discipline, "sustained" = 2+ prints. |
| **> 300K (single)** | Step-change — too big to wait | **5 🔴🔴** | **FIRE NOW.** Single >300K is a different animal (+71K WoW from 229K = recession-signature jump, not noise). Send 🔴 to CARL + REGINALD (all ORANGE banks → RED per KEY THRESHOLDS) + append AGENTS/SIGNALS.md. Don't wait for confirmation at this magnitude. |

**Confirming cross-checks (apply to any 230K+ print):**
- **4-wk MA** — 230K+ pushes MA to ~4th straight ↑; that's the trend signal, less noise than the weekly.
- **Continuing claims** — if CC also jumps (>1,820K, breaking the 1,771–1,795K range) the read hardens (people staying unemployed longer, not just inflow). CC confirming + IC up = stronger than IC alone.
- **Revisions** — check whether *prior* week (229K) revised up or down. A downward revision of 229K softens an up-print; an upward revision compounds it.
- **Seasonality** — mid-June has summer-auto-retooling + education-sector noise; a single spike can be seasonal. Magnitude + CC + MA together discriminate signal from seasonal.

---

## PRE-STAGED OUTBOX PACKETS (fill the bracket, send Thursday)

**Only send for the >250K single (provisional) or >300K (fire) branches.** 230–250K = 🟠 heads-up is optional and low-priority (per outbox push-friction restraint, prefer a NEXUS_BRIEF line unless a teammate is active).

### Packet A — >250K single print (PROVISIONAL ARM)
```
## 2026-06-18 — To: CARL, REGINALD
**Signal:** Initial claims breached 250K on a single print (w/e Jun 13 = [XXX]K) — T-01 ARMS, not yet confirmed.
**Detail:** Claims jumped to [XXX]K from 229K (+[XX]K WoW), first cross of the 250K tripwire. 4-wk MA [XXX]K. CC [X,XXX]K. Per EXIT-RULE discipline a single print ≠ "sustained" — this ARMS the realization-break leg; CONFIRMS on a 2nd consecutive >250K (next print w/e Jun 20). Treat as 🟠→🔴 provisional: pre-position, don't fully escalate.
**Source:** DOL/FRED Jun 18.
**Priority:** 🟠 (provisional; 🔴 on confirmation)
```

### Packet B — >300K single print (FIRE NOW)
```
## 2026-06-18 — To: CARL, REGINALD
**Signal:** 🔴 Initial claims STEP-CHANGE — w/e Jun 13 = [XXX]K (+[XX]K WoW from 229K). Realization break.
**Detail:** This is not drift — a +[XX]K single-week jump to [XXX]K is recession-signature, too large to attribute to summer seasonality. The bearish thesis's missing leg (realization) has fired. REGINALD: all ORANGE banks → RED per the >300K threshold. CARL: consumer-conversion timeline pulls forward. 4-wk MA [XXX]K, CC [X,XXX]K.
**Source:** DOL/FRED Jun 18.
**Priority:** 🔴
```
*(Also append AGENTS/SIGNALS.md: `| 2026-06-18 | LABOR | CARL,REGINALD | 🔴 | Claims [XXX]K step-change — realization break |`)*

---

## POST-PRINT CHECKLIST (Thursday)
1. Record IC + CC + revisions + 4-wk MA in STATUS dashboard.
2. Apply the decision-tree row → set Claims vector score.
3. If 250K+: send the matching packet; update LAB-03 (claims breach 250K) status/conf.
4. Update CATALYSTS.tsv (mark Jun 18 fired) + STATUS calendar.
5. If <230K: one-liner, no escalation, note in BOTTOM LINE.
