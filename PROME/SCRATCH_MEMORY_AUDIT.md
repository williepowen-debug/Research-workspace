# MEMORY.md Audit — Apr 3, 2026

## 1. Line Count

**Total:** 45 lines

| Section | Lines (approx) |
|---------|----------------|
| Header + pointers | 5 |
| CORE DISCOVERIES | 22 (13 bullet entries) |
| THESIS FRAMEWORK | 6 (3 entries) |
| SYSTEM ARCHITECTURE | 8 (5 entries) |

Compact file. No bloat risk currently.

---

## 2. Redundancy Check

| Overlap | Entries | Severity |
|---------|---------|----------|
| **Ghalibaf / UST Demand Hole** — Both mention Gulf SWF UST reduction and "TIC Apr 15 = first verification" | CORE #10 + THESIS #1 | 🟡 Medium — merge into one entry |
| **Japan structural withdrawal / BOJ timing** — Two CORE entries (#11, #12) cover overlapping Japan themes | CORE #11 + #12 | 🟢 Low — different angles (timing vs. structural), but could merge |
| **PC Contagion / IHAM / BROCK** — Three entries touch PE-credit chain (CORE #7, #8, #9) | CORE #7-9 | 🟢 Low — genuinely different (IHAM=evidence, PC=model, PE-Insurer=funding). Fine as-is. |
| **"CNY 7.30 call missed"** in THESIS #1 — This is a stale correction note, not a living insight | THESIS #1 | 🟡 — Remove or move to CHANGELOG |

---

## 3. Staleness Check

| Entry | Issue | Risk |
|-------|-------|------|
| **"Last Updated: 2026-03-31 18:00 UTC"** header | File has Apr 3 updates inside but header says Mar 31 | 🟡 Misleading |
| **"Seven Depletion Clocks (updated Apr 3)"** — references "Next: Planting window mid-Apr" | Still current (mid-Apr is ~10 days away) | 🟢 Fine for now, stale by Apr 20 |
| **CARL "Google Trends still at ALL-TIME HIGH"** — dated Mar 23 with "confirmed Apr 3" | Current, but Google Trends ATH claims go stale fast | 🟡 Needs re-check by mid-April |
| **Account ~$55.7K** in HEARTBEAT | Could be stale by hours/days — fine for HEARTBEAT, just noting | 🟢 |
| **"War Day 35"** in HEARTBEAT | Need to know what Day 1 was to verify — if conflict started ~Feb 27, Day 35 = Apr 3. Seems current. | 🟢 |
| **Scenario A=0%** in HEARTBEAT | Permanently zeroed scenario — remove row or keep for completeness? Minor. | 🟢 |

---

## 4. Missing Pointers

| Entry | What's missing |
|-------|---------------|
| **CARL Path C** (CORE #9) | No file path. Says "Convergence 43/50" — what file tracks this score? Should point to CARL domain file. |
| **THESIS: Ag Labor Data Gap** | Says "MARCO flagged" but no file path to MARCO's tracking of this. |
| **CORE: WAL + OZK** | Says "→ REGINALD domain" but no specific file. Other entries give exact paths. |
| **CORE: Ghalibaf** | Says "→ ZHAO domain" — vague. |
| **THESIS: UST Demand Hole** | Same — "→ ZHAO domain" with no file. |
| **SYSTEM: news sweep design** | No path to config or docs (TOOLS.md covers this, but MEMORY doesn't link it). |

Pattern: entries added before the "always include a path" norm are vaguer. Newer entries (IHAM, PE-Insurer) have full paths.

---

## 5. Consistency Check

| Potential conflict | Verdict |
|-------------------|---------|
| MEMORY says "acceleration May-Jul" / HEARTBEAT says "Insurance stress Q2-Q3'26" | ✅ Consistent (Q2 = Apr-Jun overlaps May-Jul) |
| MEMORY says "BOJ hike delayed to May or later" / HEARTBEAT doesn't mention BOJ | Not contradictory, just absent from HEARTBEAT |
| AGENTS.md lists DARWIN as "inactive" / MEMORY doesn't mention DARWIN | ✅ Consistent (correctly omitted) |
| MEMORY CORE #9 says "PC Contagion Now Stage 3 confirmed" / no contradiction found | ✅ |
| MEMORY says Hamilton "Roll Jun→Dec" / HEARTBEAT says "KRE Jun → Dec rolls" pending | ✅ Consistent |

**No contradictions found.**

---

## 6. Cold-Boot Test

If a fresh Prome read ONLY MEMORY.md + AGENTS.md + HEARTBEAT.md:

### Would understand:
- ✅ The thesis (credit cascade, timing, transmission chains)
- ✅ Agent roles and which chain they belong to
- ✅ Current positions matter (directed to POSITIONS.md)
- ✅ Key discoveries and where to find detail
- ✅ System principles (files > memory, etc.)

### Would NOT understand:
- ❌ **What to DO first.** MEMORY has no "current priorities" — HEARTBEAT has pending decisions but no action protocol. Boot sequence depends on BOOT.md (not in the trio).
- ❌ **Toscanini / autonomy tiers.** Referenced in AGENTS.md but unexplained. Fresh Prome wouldn't know approval flows.
- ❌ **Tool usage.** No mention of market-data tool, news sweep, or dashboard. Would need TOOLS.md.
- ❌ **Agent file structure.** Where are agent files? `AGENTS/{name}/` implied but never stated in these three files.
- ❌ **What "Scenario D" means concretely.** HEARTBEAT says "collapse/destabilization 82%" but MEMORY doesn't define the scenarios.
- ❌ **Position details.** Directed to POSITIONS.md but no summary of what's actually held.
- ❌ **Who Will is.** USER.md not referenced from MEMORY or HEARTBEAT.

### Verdict:
The trio gives a **coherent analytical picture** but an **incomplete operational picture**. BOOT.md is the critical missing link and is correctly referenced in AGENTS.md. The system works IF the boot sequence is followed.

---

## 7. Compression Opportunities

| Entry | Current | Could be |
|-------|---------|----------|
| **Hamilton Framework** (CORE) | 2 lines with specific numbers | Fine — numbers are the value |
| **Seven Depletion Clocks** | 4 lines | Could drop "Clock 2/3 CONFIRMED" detail to 1 line + path. Detail belongs in the linked file. |
| **PE-Insurer Wholesale Funding** | 3 lines of specifics | Could compress to: "Athene #2 FHLB borrower ($23.3B). FABR=$18B fast fuse. Increasing FHLB dependency = fragility. → SHADE + `FORGE/timing/research/`" |
| **PC Contagion Mechanics** | 4 lines | The six-stage model detail could live only in the linked file. MEMORY just needs: "Stage 3 confirmed (gating). 2007 analog: 4-5mo to bank writedown = Q2-Q3. → path" |
| **SYSTEM ARCHITECTURE section** | 5 entries | "News sweep design" entry is operational, not an insight. Move to TOOLS.md or BOOT.md. |

**Estimated savings:** ~8-10 lines if compressed. File is already lean enough that this is optional.

---

## Cross-File Duplication (MEMORY ↔ AGENTS.md ↔ HEARTBEAT.md)

| Duplication | Files | Action |
|-------------|-------|--------|
| Transmission chain description | AGENTS.md (canonical) + MEMORY (implicit in entries) | ✅ Fine — AGENTS.md is the reference, MEMORY just uses the framework |
| "Scenario D" / scenario table | HEARTBEAT only | ✅ No duplication |
| Agent names/roles | AGENTS.md (canonical) | ✅ MEMORY references agents by name without redefining them |
| Position pointers | Both MEMORY header and HEARTBEAT footer point to POSITIONS.md | 🟢 Minor — acceptable, different contexts |

**No significant cross-file duplication.**

---

## Summary

| Dimension | Grade | Notes |
|-----------|-------|-------|
| Size | ✅ A | 45 lines, well within budget |
| Redundancy | 🟡 B | 1 real duplicate (Ghalibaf/UST TIC Apr 15), 1 could-merge (Japan pair) |
| Staleness | 🟡 B | Header date wrong, CARL ATH claim aging |
| Pointers | 🟡 B- | 5 entries use vague "→ domain" instead of file paths |
| Consistency | ✅ A | No contradictions found |
| Cold-boot | ✅ B+ | Analytically coherent; operationally depends on BOOT.md (by design) |
| Compression | ✅ A- | A few entries could shed detail to linked files, but not urgent |

---

## Recommended Actions

1. **Fix header date** — Update "Last Updated" to Apr 3
2. **Merge Ghalibaf + UST Demand Hole** — Single entry, one TIC Apr 15 mention
3. **Add file paths** to the 5 vague "→ domain" entries (CARL, WAL/OZK, Ghalibaf, UST Demand Hole, Ag Labor)
4. **Move "CNY 7.30 call missed"** to CHANGELOG (it's a correction, not a live insight)
5. **Move "news sweep design"** from SYSTEM ARCHITECTURE to TOOLS.md or BOOT.md
6. **Optional:** Compress Seven Depletion Clocks and PC Contagion entries (move detail to linked files)
