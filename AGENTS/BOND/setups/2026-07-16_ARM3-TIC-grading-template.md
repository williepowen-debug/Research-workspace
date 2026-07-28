> ## ✅ USED AND RESOLVED 2026-07-23 — May TIC graded **ARM-#3 FIRED-WEAK** (KB-BND-084)
> Key result: Japan T-bills **−$59.8B REAL selling** (~94% of the Japan holdings drop) against aggregate foreign long-term UST **+$53.6B** — a *flow-level* analog of the masked-hole pattern (country-level fade hidden by aggregate absorption).
>
> **This file is a reusable TEMPLATE, not a frozen pre-reg — so unlike the auction pre-regs in this directory it SHOULD be corrected before reuse.** Two things to carry forward, both learned after it was written:
> 1. **It is already right about the thing that matters** — it grades on **NET TRANSACTIONS, not holdings**, and flags that the GATES.tsv condition text had drifted to "holdings." Keep that; it was the reason the 7/23 grade was clean.
> 2. **Re-verify the release date against the Treasury calendar before each use.** The May drop actually landed **7/14**, not the docketed 7/16 — a release-date assumption has bitten this rail once already. Pre-register against the source that *carries* the metric, at the date it is actually published (PROME frame-spec check, 7/25).

# ARM-#3 (TRY-FIRE-004) — May TIC Grading Template — pre-staged 2026-07-16 AM
**Owner:** BOND (ARM3 domain = SAM/ZHAO flow; BOND pre-stages the grade so the 4 PM read is mechanical)
**Data drop:** May 2026 TIC — **today Thu 2026-07-16 ~4:00 PM ET** (Treasury standard release, ~15th business day)
**Canonical condition source:** `AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md` ZONE 1 discriminator #3 (2026-07-09 PM patch, F10) — **NOT** the GATES.tsv row (drifted, see §0).

---

## §0 — LEDGER DRIFT FLAG (to PROME) — READ FIRST

| Surface | ARM-#3 registered condition | Status |
|---|---|---|
| `PROME/GATES.tsv` GATE-TERRY-ARM3 | "China AND Japan UST **holdings** both down" | ❌ **STALE** — pre-dates the 7/9 F10 red-team patch |
| TERRY card ZONE 1 #3 (**canonical**) | China AND Japan **net TRANSACTIONS** in LT Treasuries both net **sellers** (valuation-adjusted), Apr→May | ✅ current |
| TERRY card DISCRIMINATOR LOG table row #3 | "holdings both DOWN" | ❌ stale (log table shows pre-patch text; the ZONE 1 body is canonical) |

**Why the patch matters:** bare **holdings-down fires on pure valuation** — yields rise → mark-to-market holdings fall with **zero actual selling**. That is not a flow signal. The F10 patch respecified to **net transactions** so the arm tests a real flow-subtractor, converting Japan from a correlation-amplifier into a genuine net-seller test. **Grade off net transactions (CUT B). Holdings (CUT A) is context only.**

**Action owed:** PROME to reconcile GATES.tsv ARM3 condition text to the card (net transactions, both net sellers, valuation-adjusted) — flagged in BOND 7/16 outbox note.

---

## §1 — CORRECT REGISTERED CONDITION (canonical)

> **ARM-#3 fires iff:** TIC **net transactions** in long-term Treasury bonds & notes show **China (Mainland) AND Japan BOTH net sellers** in **May 2026** (net purchases < 0), valuation-adjusted (transactions are already a flow, not a mark). Comparison frame: April 2026 → May 2026 transactions data.
>
> **DISARM (arm-#3 DEAD):** either leg is flat / net buyer (China or Japan not a net seller).
>
> **FALLBACK (per F10):** if country-level net-transactions granularity for LT Treasuries is **not cleanly available** at the release, do **NOT** treat bare holdings-down as sufficient. Flag the granularity gap to PROME and hold **arm-#3 = UNDETERMINED** pending a transactions-level read. Do not arm on a valuation-contaminated holdings print.

Note: arm-#3 is a **secondary / deepen-only** confirmation on TRY-FIRE-004. Arm-#2 **COMPLETED 5-of-5 Mon 7/13 → RESOLVED-ARMED 7/16**; TERRY armed TRY-FIRE-004 the same session it was found, and **Will decided NO-ADD / no-fill the same morning** (book-aware rec accepted, $500 banked for re-fire; ACTIVE_DECISIONS e396dddd, GATES b64e970e) → **no consequence outstanding.** ARM3 adds/subtracts a flow leg on an already-ARMED-but-fill-DECLINED card; it does not re-open the fill decision.

---

## §2 — MECHANICAL GRADE (fill at 4 PM ET)

### CUT B — NET TRANSACTIONS (the grade) — LT Treasury bonds & notes, May 2026
Source: TIC monthly release country transactions tables — "Net Foreign Purchases of Long-Term Treasury Bonds & Notes" by country. Primary: `https://home.treasury.gov/data/treasury-international-capital-tic-system`; country LT-securities transactions tables (verify exact table/filename at release — TIC publishes country gross purchases/sales; net = purchases − sales).

| Country | May net purchases of LT USTs ($B) | Net seller? (< 0) | Apr reference |
|---|---:|:---:|---:|
| China (Mainland) | ____ | ☐ | ____ |
| Japan | ____ | ☐ | ____ |

**Grade:**
- BOTH net sellers (both < 0) → **ARM-#3 FIRES** → route to PROME/TERRY, arm latches on the card.
- Either flat / net buyer → **arm-#3 DEAD** (DISARM).
- Country net-transactions granularity unavailable / only Δholdings estimable → **UNDETERMINED**, flag to PROME (fallback), do NOT arm.

### CUT A — HOLDINGS (context only — the stale GATES cut, valuation-contaminated)
Source: Major Foreign Holders (MFH) table — `ticdata.treasury.gov` `mfh.txt` / `mfhhis01.csv`.

| Country | May holdings ($B) | Apr holdings ($B) | Δ | Down? |
|---|---:|---:|:---:|:---:|
| China (Mainland) | ____ | ____ | ____ | ☐ |
| Japan | ____ | ____ | ____ | ☐ |

**Valuation check (why CUT A ≠ CUT B):** if May was a rising-yield month, holdings fall from price alone. Show the divergence: e.g. holdings DOWN (CUT A ✓) but net transactions POSITIVE (CUT B ✗) ⇒ **no flow signal, arm-#3 does NOT fire** despite the stale GATES condition reading as met. This is the exact trap F10 patched out.

### Reconciliation line (fill)
> CUT A holdings [down/up both], CUT B transactions [both sellers / not] ⇒ ARM-#3 = [FIRES / DEAD / UNDETERMINED]. Divergence between cuts = [valuation effect $__B est. / none].

---

## §3 — POST-GRADE ACTIONS
1. Record the grade in the TERRY card DISCRIMINATOR LOG (dated 7/16 4PM entry) — via PROME routing (BOND does not edit TERRY's card).
2. Update GATES.tsv ARM3 resolution (PROME owns) + condition-text reconciliation.
3. BOND STATUS + VX.tsv: log the TIC flow read (FL-BND-11 / foreign-demand channel).
4. If UNDETERMINED: register the granularity gap as an open thread; arm-#3 stays LIVE pending a transactions read (do not auto-DEAD it).
