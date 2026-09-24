# FRAUD/ Corpus Review — 2026-09-24 (read-only)

**Scope:** every file in `AGENTS/WAL/FRAUD/` checked against `workbook/KB.tsv` (read at commit `59a4143d4`, the 09:35 ET kb-expiry pass #3), `Q2_10Q_READ_2026-08-07.md` §1(b)/§1(e), `research/CATALYST_SWEEP_2026-09-24.md` and `Q3_10Q_GRADING_FRAME_2026-09-24.md` §3.
**Writes:** this file only. No FRAUD/ file, KB row or git state was touched. Every disposition below is a **recommendation for the desk to execute**.
**⚠️ A second WAL session was committing during this review** (KB pass #3 at 09:35, retirement sweep at 09:33). KB statuses quoted here are as of `59a4143d4`.
**Labels:** **STALE** = true as dated history but reads as current. **WRONG** = never true, or contradicted by a primary source or by the corpus's own figures. **UNVERIFIED** = would need a primary source this desk does not hold.

---

## 0. Findings that cut across files (read first)

| # | Finding | Where | Basis | Class |
|---|---|---|---|---|
| X1 | **The corpus counts one credit as two vectors.** `STATUS.md` and `SYNTHESIS_V2.md` list "LAM $126.4M RESOLVED" and "First Brands / Point Bonita SILENT, unquantified" as separate vectors. But `FIRST_BRANDS.md:32-34` (updated 4/5, before the 5/1 synthesis) already says WAL lent to **LAM TFG I SPV LLC**, owned by Point Bonita, and names the **$126.4M**. The LAM charge-off **is** the First-Brands-linked credit. | `STATUS.md:17,20,71-72,86`; `SYNTHESIS_V2.md:9,13,28,78-87,99,133` | KB-WAL-135 (Point Bonita = "the Leucadia/Jefferies unit that funded First Brands receivables"), KB-WAL-186 (BROCK's "$126.4M First Brands charge-off" = the LAM charge-off), KB-WAL-078 note (pass #3: "quantified by the Q1-26 LAM charge-off") | **WRONG** (the "First Brands F-grade silence" and "LAM net-new" readings both follow from this). Nuance: WAL's own 10-Qs never say "First Brands" or "Point Bonita" (KB-WAL-144 note). The identification rests on Jefferies' side, press and BROCK. It is consistent across all of them, but it is secondary. |
| X2 | **"89% of reserve used" is compared with "ZION's 83% loss rate". These are different ratios.** $26.1M / $29.6M = 88% is how much of the **reserve** was used. ZION's 83% is loss as a share of **exposure** ($50M / $60M). WAL's comparable loss rate is **$26.1M / $98.5M = 26.5%** so far. The Q1 print therefore did **not** "directionally validate the ZION 83% benchmark". WAL's recognised loss is still about a third of ZION's rate. | `STATUS.md:16,88`; `SYNTHESIS_V2.md:14,26,30,42-44` | KB-WAL-143 / KB-WAL-148 (primary: $98.5M facility, $26.1M charge-off) | **WRONG** (a category error). The same comparison is repeated in KB-WAL-077's pass-#3 note ("89% utilisation … close to ZION's 83% benchmark"), so the desk should correct it there too. |
| X3 | **"LAM was a previously-reserved credit."** "Remaining balance" means the principal still owed after the Oct-25 to 1/15/26 repayments. It says nothing about a reserve. | `STATUS.md:88`; `SYNTHESIS_V2.md:30,43` | KB-WAL-144 (primary chronology: payments Oct-25 → 1/15/26, the 2/27 payment missed, then the $126.4M charge-off); docx ¶44 ("remaining two first-quarter payments totaling $126.4 million") | **WRONG as an inference.** Whether any reserve existed at 12/31/25 is **UNVERIFIED**. |
| X4 | **The "~$46M Cantor residual"** in the `FRAUD/STATUS.md:2` banner (also in `THESIS.md:281,297`, `WEAKNESSES.md:27`, `CLAUDE.md:16,150`) cannot be traced to any source. The primary arithmetic gives **$72.4M gross** ($98.5M − $26.1M) with a **$3.5M** specific allowance left at 3/31/26. | `STATUS.md:2` | KB-WAL-143 (A1); KB-WAL-082 (~$70M, A2, extended to 11/10); KB-WAL-137 gives a "$46-70M" range with no basis | **UNRECONCILED.** Its origin is unknown. It is not cited to any KB row. Side note, outside FRAUD/: `THESIS.md:281` also says "$29.4M" where the primary figure is **$29.6M**. |
| X5 | **The CEO's 9/16 comments on fraud are not in any KB row.** Rows KB-WAL-086 and -088 cite them "(KB-WAL-194)", but KB-194's FACT and NOTES contain only the NPL/ACL/charge-off guidance. The quotes live only in `CATALYST_SWEEP_2026-09-24.md:80` (T2: third-party transcript, quotes extracted by a model). | KB-WAL-086, -088 notes | `CATALYST_SWEEP:80` | A pointer defect. A KB row is owed for these quotes. |
| X6 | **The CEO's "found no other instance" is being applied to a failure mode it does not cover.** The quote is limited to "double-pledged **titles**", which is how the Cantor fraud worked. KB-WAL-086's pass-#3 note uses it to close the question of other Leucadia-era credits. The LAM failure was **"servicing failures, including lapses in UCC filings"**, a lapse in collateral perfection. The CEO's statement does not address that. | KB-WAL-086 note | `CATALYST_SWEEP:80`; KB-WAL-144 | **WRONG scope.** See §2. |
| X7 | **The CEO's label for LAM has narrowed while WAL's pleading has widened.** On 9/16 he called LAM "a breach of contract" (T2). The May-2026 **amended** complaint pleads breach of contract **plus fraud, negligence, promissory estoppel and unjust enrichment**. KB-WAL-088's note calls the two "consistent". They move in opposite directions. | KB-WAL-088 note | KB-WAL-152 (A1, Q2 10-Q) vs `CATALYST_SWEEP:80` (T2) | Tension to record, not a contradiction to resolve. Re-verify the quote at a primary source (webcast replay) before relying on it. |
| X8 | KB-WAL-177's FACT reads "unlawfully frozen **5M** deposit". The "$2" has been dropped, most likely by shell expansion; KB-WAL-135 has **$25M**. | KB-WAL-177 | KB-WAL-135 | Text defect in the KB (the desk's edit). |

---

## 1. Per-file review

**File inventory** (size in bytes · last commit via `git log -1 --format=%ci` · first commit via `--follow`). Every file's last commit is the **2026-07-25 promotion `git mv`**, which is **61 days before today**. Content dates are 3/25 to 5/1.

| File | Bytes | Last commit | Content vintage | Banner today? | Boot-read? | Live-doc references (INDEX, KB_INDEX and FRAUD-internal navigation excluded) |
|---|---|---|---|---|---|---|
| `STATUS.md` | 8,481 | 2026-07-25 14:52 | 2026-05-01 | ✅ Q1-CYCLE RECORD | no | `THESIS.md:410` (pointer table); `CLAUDE.md:120` designates the bannered records |
| `SYNTHESIS_V2.md` | 10,300 | 2026-07-25 14:52 | 2026-05-01 | ✅ Q1-CYCLE RECORD | no | `THESIS.md:410` ("refresh pending Wave 1 chunk 2") |
| `AUDITOR_NEXUS.md` | 12,101 | 2026-07-25 14:38 | 2026-03-27 | ❌ | no | `LEADERSHIP.md:182,234` ("Full analysis →"; LEADERSHIP is bannered STALE-VINTAGE but not archived) |
| `AUDIT_COMMITTEE.md` | 8,591 | 2026-07-25 14:38 | 2026-03-27 | ❌ | no | `LEADERSHIP.md:182,234` |
| `CLASS_ACTION_FINDINGS.md` | 5,366 | 2026-07-25 14:38 | 2026-03-27 | ❌ | no | none |
| `FIRST_BRANDS.md` | 8,549 | 2026-07-25 14:38 | 2026-04-05 | ❌ | no | **KB-WAL-186** (cites `FIRST_BRANDS.md` L41/L131 as a cross-check); outbox 2026-09-02 to BROCK |
| `GRANT_THORNTON_NEXUS.md` | 6,624 | 2026-07-25 14:38 | 2026-03-26 | ❌ (self-declared superseded at `AUDITOR_NEXUS.md:207`) | no | none |
| `INVESTIGATION_ROADMAP.md` | 3,116 | 2026-07-25 14:38 | 2026-03-26 | ❌ | no | none |
| `ISSUER_B_ELIMINATION.md` | 2,722 | 2026-07-25 14:38 | 2026-03-27 | ❌ | no | none (KB-WAL-071 cites the PCAOB release, not this file) |
| `RSM_PUBLIC_AWARENESS.md` | 5,653 | 2026-07-25 14:38 | 2026-03-27 | ❌ | no | none |
| `STUPIN_CRE.md` | 4,831 | 2026-07-25 14:38 | 2026-03-25 | ❌ | no | none outside FRAUD/ (only `AUDITOR_NEXUS:208` and `GT_NEXUS:107` navigation) |
| `TRICOLOR.md` | 3,713 | 2026-07-25 14:38 | 2026-03-25 | ❌ | no | none |
| `WAL-JEF-PointBonita-Analysis-20260326.docx` | 58,645 | 2026-07-25 14:38 | 2026-03-26 | ❌ (binary, cannot carry a banner) | no | `FIRST_BRANDS.md:157` |
| `ZION_AUDIT_COMPARISON.md` | 6,718 | 2026-07-25 14:38 | 2026-03-27 | ❌ | no | none |

---

### 1.1 `STATUS.md` — BANNER-AS-RECORD (a rider under the existing banner; content unchanged)

**What it claims:** the Q1-cycle fraud dashboard as of 5/1. The Q1-26 charge-offs total $152.5M (LAM $126.4M + Cantor $26.1M). Cantor is "partially resolved" with ~$70M left. First Brands and Tricolor are "silent". Five open threads. **Already bannered** at `:2` as a Q1-cycle record, "do NOT update in place".

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:2` | "Live state → `../THESIS.md` v2.3" | THESIS v2.4 (2026-08-20) | STALE pointer inside the banner |
| `:2` | "~$46M Cantor residual" | KB-WAL-143 ($72.4M gross / $3.5M allowance) | UNRECONCILED (X4) |
| `:16` | "$26.1M (89% of $29.6M reserve utilized)" vs "ZION 83% comp"; "~$70M on book" | KB-WAL-143 (facility **$98.5M**, not $98M; residual $72.4M); X2 | WRONG comparison; residual STALE |
| `:17, :20, :71-72, :86` | First Brands / Point Bonita "SILENT", "unquantified", "potentially absorbed in $87M ex-LAM provision" | KB-WAL-135, -186, -078 note | **WRONG** (X1) |
| `:18, :87` | Tricolor "SILENT", "may reside inside $9.2B mortgage warehouse" | KB-WAL-124 (no new fraud item in the Q2 print); THESIS v2.2 `:64` (Q1 10-Q inventory: only LAM + Cantor) | STALE. Still silent after three filings; no WAL exposure has ever been evidenced |
| `:84` | Thread 1: "Other LAM/Leucadia-era credits … Test: 10-Q Table 16 (~May 4-10) … May 12 Investor Day" | KB-WAL-086 note (inventory CLEAN at the Q1 10-Q) | STALE (resolved as clean) |
| `:85` | Thread 2: Cantor residual base case "30-50% recovery"; "full $70M loss = additional $70M provision over 2026-2027" | KB-WAL-148 (Q2: "No additional charge-offs"); KB-WAL-123 (senior liens $13M → $64M); Q3 10-Q frame §3 | STALE. Recovery is now tracked by the frame |
| `:88` | Thread 5: "LAM … previously-reserved … RSM demoted to tertiary" | X3 | WRONG inference |
| `:107` | "Canonical post-print analysis: `../THESIS.md` v2.0 §V2" | THESIS v2.4 | STALE pointer |

**Rider text for the desk to add at `:3` (drafted verbatim):**
> 📼 **RIDER 2026-09-24 (review `research/FRAUD_CORPUS_REVIEW_2026-09-24.md`) — content NOT edited; three readings in this record are wrong and must not be cited:** (1) "First Brands / Point Bonita SILENT / unquantified" — the LAM $126.4M charge-off **is** the Point-Bonita / First-Brands-linked credit (KB-WAL-135, -186; `FIRST_BRANDS.md:32`); there were two credits, not four vectors. (2) "89% of reserve ≈ ZION 83%" compares reserve used with loss rate; WAL's loss rate is $26.1M/$98.5M = 26.5% (KB-WAL-143). (3) "LAM previously reserved" is not supported by "remaining balance" (KB-WAL-144). The "~$46M residual" in the banner above has no traced source; the primary-derived figure is $72.4M gross / $3.5M allowance at 3/31/26 (KB-WAL-143), and it was not restated in the Q2 10-Q (KB-WAL-148). Live state → `../THESIS.md` (v2.4) · Cantor → `STUPIN_CRE.md` §FOLD 2026-09-24 · LAM → `FIRST_BRANDS.md` §FOLD 2026-09-24 · Q3 tests → `../Q3_10Q_GRADING_FRAME_2026-09-24.md` §3.

---

### 1.2 `SYNTHESIS_V2.md` — BANNER-AS-RECORD (the same rider, adapted; content unchanged)

**What it claims:** REGINALD's post-print synthesis as of 5/1. The V2 framework was "correct". LAM is described as "net-new". The RSM angle is demoted. Its forward checklist is keyed to May events. **Already bannered** at `:2`.

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:9, :13, :28, :78-87, :99, :133` | First Brands "silent", F grade; LAM "net-new … on the same rail we'd flagged via First Brands"; "the silence is the new edge" | KB-WAL-135, -186 | **WRONG** (X1). LAM was not a new credit. The same credit was on the radar under the name First Brands / Point Bonita |
| `:14, :26, :30, :42-44` | "89% … directionally validates ZION 83%" | KB-WAL-143 | **WRONG** (X2) |
| `:30, :43` | LAM "previously-reserved … the reserve was already there" | KB-WAL-144 | **WRONG inference** (X3) |
| `:52-61` (§4a) | "Other LAM/Leucadia-era credits (PRIMARY)"; tests set for May 4-10 and May 12 | KB-WAL-086 note (clean at the Q1 10-Q) | STALE (resolved as clean) |
| `:56, KB-085` | "will not provide further commentary" | The May 2026 amended complaint (KB-WAL-152); the CEO did comment on 9/16 (`CATALYST_SWEEP:80`, T2) | STALE |
| `:65-75` | ~$70M residual; recovery scenarios | KB-WAL-143 ($72.4M / $3.5M); KB-WAL-148 (Q2 zero); KB-WAL-123 (liens $64M) | STALE |
| `:107-116` | May-dated checklist (Table 16, Investor Day, MI3 "V1 acceleration", REG-25) | MI3 run 8/7 and disconfirmed (THESIS v2.4); Q3 frames | STALE |

**Rider:** use the §1.1 text, replacing its first sentence with "Post-print synthesis; the same three readings are wrong here (`:9/:13/:28/:99`, `:14/:26/:42`, `:30/:43`)". Also re-point `THESIS.md:410` ("refresh pending Wave 1 chunk 2"). That is a THESIS edit for the desk: this synthesis is frozen and will not be refreshed. The live V2 record is the two FOLD sections below.

---

### 1.3 `AUDITOR_NEXUS.md` — BANNER-AS-RECORD (not eligible for retirement: `LEADERSHIP.md:182,234` point to it)

**What it claims:** WAL's own auditor (RSM) has a PCAOB record showing collateral-verification failures. "Issuer B = WAL (HIGH)". "Three fraud vectors all failed at the gatekeeper level." A pre-print question list for Apr 21. **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:9, :17, :71, :106-113` | "three fraud vectors" / "3 active fraud vectors" / the three-gatekeeper thesis | X1 (First Brands = LAM); Tricolor never evidenced; KB-WAL-080 is still ACTIVE with no Stale_By | **WRONG as a count** (two credits). The thesis is weakened, see §2 |
| `:18-19` | Tricolor / Carvana "WAL exposure via NDFI/warehouse/BDC" | No WAL disclosure in Q1 8-K, Q1 10-Q, Q2 print or Q2 10-Q (KB-WAL-124; THESIS v2.2 `:64`) | UNVERIFIED hypothesis. It reads as fact |
| `:52, :108, :146, :153-162` | "30% reserve … UNCHANGED"; "RSM signed off on 30%" | KB-WAL-143/-148 ($26.1M charge-off in Q1-26; $3.5M left); KB-WAL-077 SUPERSEDED | STALE |
| `:71` | "WAL at $80B+" | Q2 10-Q: $98.7B assets (Q2 read §1e) | STALE |
| `:130` | "Confidence that Issuer B = WAL: HIGH" | KB-WAL-071 pass #3: "an INFERENCE … never confirmed by PCAOB or WAL" | STALE confidence label; UNVERIFIED |
| `:137` vs `AUDIT_COMMITTEE:48`, `ZION_AUDIT:13` | RSM tenure "32 years" vs "31 years" | KB-WAL-074 (32) | Minor internal inconsistency |
| `:145` | "$98.5M facility" | KB-WAL-143 | ✅ consistent with the primary |
| `:147, :177-180, :198` | "updated appraisals due March 2026 … if junior-lien, recovery assumptions collapse" | KB-WAL-143 (as-is appraisals led to the $26.1M charge-off and the specific allowance cut to $3.5M; "reserve validated", KB-WAL-083) | STALE (the event is answered) |
| `:174` | "No public confirmation receiver was appointed"; docket not found | KB-WAL-137 (docket 25STCV24263, Judge Green; Trellis 403 on 9/24) | STALE. Receiver status is still UNVERIFIED |
| `:202` | "WAL must address First Brands, Tricolor, AND Stupin" | X1; KB-WAL-086 note | STALE |

**Banner (drafted verbatim):**
> 📼 **PRE-PRINT RECORD (vintage 2026-03-27; bannered 2026-09-24).** Historical; superseded by the Q1/Q2 10-Q primaries. Do not cite as current: the "three vectors" were two credits (First Brands/Point Bonita = the LAM charge-off, KB-WAL-135/-186; Tricolor exposure never evidenced); the "30% reserve unchanged" became a $26.1M Q1-26 charge-off with $3.5M allowance left (KB-WAL-143/-148); "Issuer B = WAL" is an unconfirmed inference (KB-WAL-071). The failure mode the filings actually name is collateral **perfection** ("lapses in UCC filings", KB-WAL-144), which is not an auditor-verification failure. Live: `STUPIN_CRE.md` / `FIRST_BRANDS.md` §FOLD 2026-09-24.

---

### 1.4 `AUDIT_COMMITTEE.md` — BANNER-AS-RECORD (`LEADERSHIP.md` points to it)

**What it claims:** from the FY2024 proxy (DEF 14A 2025-04-23): a 6-member independent committee, a specialty-finance expertise gap, 31-year RSM tenure, and audit fees of $4.1M described as ~40-50% of peers ("🔴 Red Flag"). **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:2, :7-18, :64-77` | FY2024 membership and fees | The 2026 DEF 14A (FY2025) exists and is **unread** (MEMORY "Carried / lower: read the 2026 DEF 14A") | STALE. Current values are UNVERIFIED |
| `:86` | "Zions Bancorp: **KPMG** audit fees ~$9.2M" | `ZION_AUDIT_COMPARISON.md:12`, from the ZION 10-K (primary, acc 0000109380-26-000046): ZION's auditor is **Ernst & Young** | **WRONG** (contradicted by the corpus's own primary read) |
| `:80-90, :103` | The peer-fee "Red Flag" rests on "approximate, from recent proxies" with no sources, and one of the three peers has the wrong auditor | — | Unsourced and partly WRONG. The Red Flag rating should not be cited |
| `:60` | "$80B+ asset bank" | $98.7B (Q2 10-Q) | STALE |

**Banner:**
> 📼 **RECORD (FY2024 proxy, vintage 2026-03-27; bannered 2026-09-24).** Not refreshed against the 2026 DEF 14A. `:86` is wrong: ZION's auditor is EY, not KPMG (`ZION_AUDIT_COMPARISON.md:12`, ZION 10-K). The peer-fee comparison (`:85-90`) is unsourced, so do not cite the "Red Flag" rating.

---

### 1.5 `CLASS_ACTION_FINDINGS.md` — RETIRE

**What it claims:** as of 3/27, only Rosen and Shamis & Gentile had announced investigations. No complaint had been filed, and Portnoy's page returned 404. **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:3, :10` | "no actual class action complaint has been filed" | Never re-checked after the Q1-26 $152.5M charge-off drop. The Q2 10-Q Note 15 has only blanket "routine lawsuits" language (KB-WAL-153) | STALE. Current status is UNVERIFIED (PACER / Stanford SCAC not checked) |
| `:64` | "**Boris** Stupin" | KB-WAL-137 (docket defendant **Andrew** Stupin); `STUPIN_CRE.md:8` | **WRONG** |

**Retirement check:** 61 days since last commit (content ~181 days). Not boot-read. Only INDEX and FRAUD/STATUS navigation point to it, so it passes. No pending dated event is registered to it. → `git mv` to `AGENTS/WAL/archive/`. Carry the one live line (class-action status unverified since 3/27) into the STUPIN fold (§1.11). Also note: KB-WAL-021 is ACTIVE with a blank Stale_By.

---

### 1.6 `FIRST_BRANDS.md` — FOLD

**What it claims:** "Vector 1". WAL lent non-recourse to LAM TFG I SPV (Point Bonita / LAM). $126.4M is disputed. The March 31 forbearance deadline has passed. JEF losses. Auction recovery is below 1%. **No banner.** This is the only non-record file that already had the X1 identification right (`:32-34`).

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:1` | "WAL Fraud Vector 1", treated as separate from LAM | X1 | STALE framing (this is the LAM credit) |
| `:32` | "Non-recourse to SPV collateral" stated as fact | KB-WAL-136: this is **Jefferies' characterisation**. WAL's case is that the Oct-2025 forbearance created a repayment obligation (KB-WAL-144) | STALE. It reads as settled; it is contested |
| `:47` | "UCC filings lapsed **Sept 2025**" | KB-WAL-144 (primary: "lapses in UCC filings", **no date**). The Sept date is single-source (TipRanks; docx ¶45 "One report indicates") | The date is UNVERIFIED. The mechanism is confirmed at primary |
| `:49` | "WAL asked Jefferies + Point Bonita for guarantees … both refused" | KB-WAL-136 (Banking Dive rendering of the same Handler/Friedman letter): "WAL **DECLINED** Jefferies' offer of guarantees". The two secondary renderings of one Jefferies letter conflict | **CONTESTED / UNVERIFIED**. The primary (Jefferies 3/8 press release) has not been read |
| `:50, :53-54` | "Mar 31 2026 (THIS MONDAY)" catalyst | KB-WAL-144 (the missed 2/27 payment triggered the charge-off) | STALE |
| `:84` | "WAL sues JEF … (breach + fraud)" | KB-WAL-144 (March complaint: breach + **fraudulent inducement**); KB-WAL-152 (**amended May 2026**: + fraud, negligence, promissory estoppel, unjust enrichment) | STALE |
| `:136-139` | "Write off the $126.4M (**or net of $42.1M already paid = $84.3M remaining**)" | KB-WAL-084 / -144 ($126.4M **is** the remaining balance after the $42.1M received 1/15/26); docx ¶44 | **WRONG** |
| `:131` | Point Bonita $715M | KB-WAL-186 (consistent, ~$3B book) | ✅ |
| n/a | The Jefferies countersuit (~7/1) is absent | KB-WAL-135, -177 (secondary; not in the Q2 10-Q, KB-WAL-153) | STALE by omission |

**Why FOLD rather than retire:** KB-WAL-186 travels this file by line number, and the CLAUDE.md DOC OWNERSHIP table assigns the "LAM/Jefferies litigation" to FRAUD/. No other FRAUD/ file is the natural home for the LAM arc.

**Top-of-file pointer (add at `:2`):**
> ⤵ **This file's credit IS the LAM charge-off** (KB-WAL-135/-186). Content above `§FOLD 2026-09-24` is pre-print (3/26-4/5) — `:49` guarantee direction is contested, `:137` "$84.3M" is wrong ($126.4M was the remaining balance). Current state → §FOLD 2026-09-24 at the end.

**Section to append (drafted verbatim):**

```markdown
## FOLD 2026-09-24 — LAM / Jefferies: current state (supersedes §WAL Exposure Path figures, §CATALYST, §WAL V2 Impact)

**Identity:** WAL's loan to LAM TFG I SPV LLC (Point Bonita-owned, Leucadia Asset Management platform) = the **$126.4M Q1-26 "LAM" charge-off**. It is the First-Brands-linked credit — not a separate vector (KB-WAL-135, -186). WAL's own 10-Qs never name Point Bonita or First Brands (KB-WAL-144 note); the link rests on Jefferies/press/BROCK.

| Item | State | Source | Tier |
|---|---|---|---|
| Charge-off | $126.4M "remaining balance", booked Q1-26 (8-K 3/6); fully realized, no Q2 residual | KB-WAL-084, -124, -186 | A1 |
| Default mechanism | "servicing failures, including lapses in UCC filings" → Oct-25 forbearance (repay by 3/31/26) → payments Oct-25…1/15/26 ($42.1M last received) → 2/27 payment missed → charge-off | KB-WAL-144 (Q1 10-Q) | A1 |
| WAL's claim | NY Supreme Court, Bank + collateral agent v. Jefferies Financial Group, LAM LLC & affiliates. Mar-26: breach + fraudulent inducement. **Amended May-26:** breach, fraud, negligence, promissory estoppel, unjust enrichment | KB-WAL-144, -152 (Q2 10-Q) | A1 |
| Jefferies countersuit | ~2026-07-01, NY state court, alleges WAL unlawfully froze a **$25M** Point Bonita deposit. Not in the Q2 10-Q; absence is uninformative (Note 15 blanket) | KB-WAL-135, -153, -177 | B (secondary) |
| Jefferies' defense | Non-recourse to SPV; affiliates excluded; "WAL already recovered more than half" | KB-WAL-136 | Counterparty assertion, UNVERIFIED |
| Guarantee direction | Conflicting secondary renderings (WAL asked/refused vs WAL declined an offer) | `:49` vs KB-WAL-136 | UNVERIFIED — read Jefferies' 3/8 release |
| Recovery to date | Not disclosed: "Any future recoveries will be recognized when realized or realizable" | KB-WAL-153 | A1 (negative) |
| Mgmt label 9/16 | "the Lam for us is a breach of contract"; "favorable outcome … over the next year or so" (said of both) — narrower than the amended pleading | `research/CATALYST_SWEEP_2026-09-24.md:80` | T2, re-verify |
| Docket/news 8/20→9/24 | No development found; EDGAR FTS 0 hits "Point Bonita" | CATALYST_SWEEP:118 | search-negative |
| Next test | Q3 10-Q "Legal Disputes…" paragraphs: countersuit disclosed? recovery figure? ruling/settlement/accrual? | `../Q3_10Q_GRADING_FRAME_2026-09-24.md` §3 | — |

**P&L:** closed (loss realized). **Forward:** two-way — recovery upside vs a $25M counter-exposure. V2 remains historical and excluded from the composite (THESIS v2.4).
```

---

### 1.7 `GRANT_THORNTON_NEXUS.md` — RETIRE

**What it claims:** Grant Thornton (GT) audits Tricolor, Carvana, DriveTime and GoFi, and is presented as the "common node". It also lists open questions: who audits WAL, and who audits First Brands. **No banner.** It is self-declared superseded (`AUDITOR_NEXUS.md:207`).

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:41-43, :46` | WAL has Tricolor/auto exposure through NDFI, warehouse and BDC lending | Never evidenced (KB-WAL-124; Q1 10-Q inventory) | UNVERIFIED |
| `:82-83, :92-93` | "Who audits WAL? … First Brands?" | `AUDITOR_NEXUS.md:17,20` (RSM; BDO) | STALE (answered) |
| `:74` | "WAL's own auditor gave clean opinions … zero Cantor mention" | KB-WAL-143 | STALE |

**Retirement check:** passes. It is referenced only by `AUDITOR_NEXUS.md:207` navigation, which itself says "superseded".

---

### 1.8 `INVESTIGATION_ROADMAP.md` — RETIRE (after the §1.6 / §2 folds carry Track 2)

**What it claims:** a GPT-5.4 checklist dated 3/26 with three tracks: legal paper trail, perfection, and cash dominion. **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:18, :44` | Watch for a motion to dismiss or an answer in WAL v. JEF (~Apr-May) | KB-WAL-152: the complaint was **amended** in May. Motion practice was never tracked. NYSCEF not accessed (CATALYST_SWEEP:165) | STALE. Docket state is UNVERIFIED |
| `:21-25` | Track 2: "UCC lapsed Sept 2025 … **if perfection failure → readthrough to other receivables programs at WAL**" | KB-WAL-144 (primary mechanism), KB-WAL-186 (BROCK's screen) | **Still live.** This is the screen question itself, posed 3/26 and never run. Carry it (§2) before retiring |
| `:43` | Mar 31 deadline 🔴 | KB-WAL-144 | STALE |

**Retirement check:** passes (only INDEX and FRAUD/STATUS navigation). **Order matters:** fold the Track-2 question into §2's text first, then retire.

---

### 1.9 `ISSUER_B_ELIMINATION.md` — RETIRE (update KB-WAL-071's pointer in the same commit)

**What it claims:** EDGAR full-text search across 6 RSM bank clients. Only WAL matches the "purchased loans at a discount + accretable" wording, so "Issuer B = WAL (HIGH)". **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:4, :47-49` | "confirmed by elimination", "HIGH", "No other RSM bank client" | KB-WAL-071 pass #3: "INFERENCE … never confirmed" | STALE label. The elimination covers only the 6 named clients (`:21-26`). `AUDITOR_NEXUS:69` admits other unnamed "$3-5B" community-bank clients exist, so the elimination is **incomplete** (UNVERIFIED) |
| `:26` | "~$80B" | $98.7B | STALE |

**Retirement check:** passes. **Caveat:** this file is the only record of the *method* behind an ACTIVE row (KB-WAL-071, extended to 2027-03-01). Archiving keeps it reproducible. Add the archive path to KB-071's notes in the same commit.

---

### 1.10 `RSM_PUBLIC_AWARENESS.md` — RETIRE

**What it claims:** as of 3/27, nobody public had linked RSM's PCAOB record to WAL, so the thesis was "HIGHLY DIFFERENTIATED". **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:4, :67` | "differentiated" | Never re-run. Its own `:86-92` records that most searches were blocked, and `:94` says "Re-run" | STALE, and weak when written. Current state is UNVERIFIED |

**Retirement check:** passes (INDEX only).

---

### 1.11 `STUPIN_CRE.md` — FOLD (the Cantor home; see the judgement note)

**What it claims:** the mechanics of the Stupin/Cantor ring. WAL vs ZION: 30% vs 83%. A $51.8M shortfall. Q4 silence. OREO and provision stress. A "hidden CRE" link. **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:37-42` | Exposure **$98.6M**, loss recognised $30M (30%), recovery ~70%, "covers the obligation" | KB-WAL-143 (**$98.5M**, A1); KB-WAL-014 SUPERSEDED; KB-WAL-148 | STALE ($98.6M is WRONG at the primary) |
| `:44-52` | Shortfall $51.8M / $68.6M | KB-WAL-016 SUPERSEDED (actual charge-off $26.1M) | STALE |
| `:56-64` | "Q4 2025: Silence … reserve unchanged" | KB-WAL-018 SUPERSEDED | STALE |
| `:70-82` | OREO $137M; provisions Q1-Q3 2025 | KB-WAL-019 → -155 ($126M at 6/30/26, 22 properties); KB-WAL-020 → -157 | STALE |
| `:84-87` | Class action "investigation"; "Portnoy Law investigating" | CLASS_ACTION `:32` (Portnoy page 404) | STALE / internally inconsistent |
| `:105` | "all loans >$10M reviewed, no additional irregularities found" | KB-WAL-022 warning (it predates the LAM charge-off); 9/16 CEO "no other instance [of double-pledged titles]" (T2) | STALE. Scope it to title fraud only (X6) |
| `:106, :110-113` | "MI3 24.2% and GROWING — $2.73B" | KB-WAL-001/-002 SUPERSEDED (21.20%, $2.55B at 6/30/26; MI3 disconfirmed, THESIS v2.4) | **WRONG** as current ("GROWING" was refuted) |
| `:25` | "Fraud discovered only after WAL filed lawsuit (August 2025)" | — | Garbled causality. UNVERIFIED; not load-bearing |
| `:93` | Nano Banc "facing receivership" | no WAL KB row | UNVERIFIED current status |

**Judgement note:** by the letter of the retirement rule this file qualifies: 61 days since last commit, not boot-read, and referenced only by FRAUD-internal navigation. I recommend **FOLD** instead. The Cantor matter is a live WAL-owned arc (CLAUDE.md DOC OWNERSHIP: FRAUD/ owns "Cantor residual"). The Q3 10-Q frame §3 is about to grade it. The two bannered records say new state goes in new dated sections. Without a live Cantor surface, the residual figure keeps drifting (X4). Alternative if the desk prefers: retire this file and put the fold below into a new `FRAUD/CANTOR_ARC.md`.

**Top-of-file pointer (add at `:3`):**
> ⤵ Content above `§FOLD 2026-09-24` is pre-print (3/25). The $98.6M/30%/70%, shortfall, Q4-silence, OREO/provision and MI3 lines are superseded (KB-WAL-014/-016/-018/-019/-020/-001/-002). Current state → §FOLD 2026-09-24.

**Section to append (drafted verbatim):**

```markdown
## FOLD 2026-09-24 — Cantor Group V: current state

| Item | State | Source | Tier |
|---|---|---|---|
| Facility / nonaccrual | **$98.5M** to nonaccrual as of 9/30/25 ($98.6M was a secondary figure — superseded) | KB-WAL-143, -148 | A1 |
| Specific allowance → charge-off | $29.6M established Q3-25; **$26.1M charged off Q1-26** on updated "as-is" appraisals + "expected duration of the resolution process"; **$3.5M** remaining at 3/31/26 | KB-WAL-143 | A1 |
| Q2-26 | "No additional charge-offs were recognized during the three months ended June 30, 2026." Q2 10-Q DROPPED the $3.5M, the residual and the lien figures | KB-WAL-148; Q2 read §1(b) | A1 |
| Residual carrying value | **$72.4M gross** derived ($98.5M − $26.1M) at 3/31/26; "~$70M" (A2 reconcile). The "~$46M" figure on other WAL surfaces has **no traced source** | KB-WAL-143, -082 | derived / UNRECONCILED |
| Loss rate so far | $26.1M / $98.5M = **26.5%** of exposure (vs ZION 83%, KB-WAL-015). "89%" is reserve *utilisation*, not a loss rate | KB-WAL-143, -015 | derived |
| Recovery legs | $13M senior NPL lien bought Q1 + stated intent to buy more; senior protective liens $64M at Q2 (+$51M); limited + full guaranty from two UHNW individuals (Marcil/Stupin); mortgage-fraud policy | KB-WAL-143, -123, -148 | A1 / A2 |
| ★ $64M candidate tie | Q2 MD&A "purchase of $64M of loans with more-than-insignificant deterioration" (PCD) = liens $64M — magnitudes match, filing does NOT connect them | KB-WAL-148; Q3 10-Q frame §3 | CANDIDATE, never promoted by inference |
| Docket | WESTERN ALLIANCE BANK v. CANTOR GROUP V LLC et al., LA Superior 25STCV24263, Judge Terry A. Green; no development found 8/20→9/24 (Trellis 403; LA portal not accessed) | KB-WAL-137; CATALYST_SWEEP:119,166 | search-negative |
| Mgmt 9/16 | "One was a fraud, which was Cantor"; "favorable outcome … over the next year or so"; "found no other instance [of double-pledged titles] in our book … other than … Cantor" | CATALYST_SWEEP:80 | T2, re-verify at webcast |
| Securities class action | Investigations only as of 3/27 (Rosen, Shamis & Gentile); not re-checked since; Q2 10-Q Note 15 blanket only | archived CLASS_ACTION_FINDINGS; KB-WAL-021, -153 | UNVERIFIED since 3/27 |
| Next test | Q3 10-Q "Legal Disputes…" → Cantor: Q3 charge-off, recovery $, residual/allowance, $64M tie | `../Q3_10Q_GRADING_FRAME_2026-09-24.md` §3 | — |

**Scope of the "no other instance" assurance:** it covers the Cantor failure mode (forged title / lien priority). It says nothing about collateral-perfection lapses — the LAM failure mode. See `FIRST_BRANDS.md` §FOLD and the perfection screen.
```

---

### 1.12 `TRICOLOR.md` — RETIRE

**What it claims:** Tricolor's $800M double-pledging fraud. WAL's connection is inferred through NDFI, warehouse and BDC lending, and the WAL dollar figure is "[DATA NEEDED]". The Grant Thornton thread. **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:29-36` | WAL connection via 4 channels, figure "DATA NEEDED — critical gap for Apr 21" | Silent in the Q1 8-K, Q1 10-Q, Q2 print and Q2 10-Q (KB-WAL-124; THESIS v2.2 `:64`). KB-WAL-079 is **still ACTIVE**, asserting "WAL exposed via NDFI/warehouse/BDC chain" | STALE. The exposure was never evidenced, so KB-079's "exposed" is an UNVERIFIED hypothesis stated as fact |

**Retirement check:** passes (only navigation references). Carry the closed negative ("no WAL Tricolor exposure evidenced across 4 filings") into KB-079's note (the desk's edit).

---

### 1.13 `WAL-JEF-PointBonita-Analysis-20260326.docx` — NO-CHANGE (the §1.6 fold records its caveats)

**What it claims:** a 3/26 investment-committee memo with 16 references. It covers the SPV structure, timeline, legal positions and monitoring points. Binary, so it cannot carry a banner.

| ¶ (extracted text) | Claim | Status |
|---|---|---|
| ¶12, ¶16 | WAL lent from 2021 to LAM Trade Finance Group LLC and LAM TFG I SPV LLC, "non-recourse" | The structure is consistent with KB-WAL-136. "Non-recourse" is Jefferies' framing |
| ¶33, ¶51 | "WAL requests guarantees … both declined" | Conflicts with KB-WAL-136. CONTESTED (§1.6) |
| ¶35, ¶45 | UCC lapse in "September 2025" ("One report indicates") | Date UNVERIFIED; mechanism A1 (KB-WAL-144) |
| ¶44 | "remaining two first-quarter payments totaling $126.4 million" | ✅ agrees with KB-WAL-144 (and refutes `FIRST_BRANDS.md:137`) |
| ¶40 | Suit for "breach of contract and fraud" | STALE (amended May-26, KB-WAL-152) |

**Why not retire:** `FIRST_BRANDS.md:157` references it, and that file becomes live under the fold.

---

### 1.14 `ZION_AUDIT_COMPARISON.md` — RETIRE

**What it claims:** from the ZION FY2025 10-K (primary): EY gave a clean opinion with one generic ACL critical audit matter (CAM). ZION charged off $50M, never names Cantor, and uses "irregularities and misrepresentations". Compared with WAL/RSM. **No banner.**

| Line | Claim | Superseded by | Class |
|---|---|---|---|
| `:52-53, :78, :93-94, :97, :100` | WAL "$29.6M reserve … unchanged 6 months", "Reserve (holding, not yet charged off)" | KB-WAL-143/-148 | STALE (the WAL column) |
| `:13` | RSM "since 1994 (31 years)" | KB-WAL-074 (32) | minor |
| ZION column | Verbatim 10-K quotes | — | ✅ Primary-sourced history |

**Retirement check:** passes (INDEX and FRAUD/STATUS navigation only). Archiving keeps the verbatim ZION primary quotes. KB-WAL-015 (ACTIVE) sources ZION's 8-K, not this file. It also fixes the ZION auditor fact that `AUDIT_COMMITTEE.md:86` gets wrong, so cite its archive path in that banner.

---

## 2. BROCK's collateral-perfection screen (KB-WAL-186): where it applies

**The screen:** read each WAL fraud loss by the **mechanism the filing names**, not by exposure bucket. For LAM the mechanism is **"servicing failures, including lapses in UCC filings"** (KB-WAL-144, A1), a failure of **collateral perfection**. Cantor's mechanism was **lien priority misrepresented through forged title policies** (KB-WAL-137). Both are **failures of the claim on the collateral**. Neither was a failure of credit selection or of the auditor.

| Where | Line | Apply how |
|---|---|---|
| `FIRST_BRANDS.md` | `:46-47` (lists "UCC filings lapsed Sept 2025" as failure #1) | Promote it from a dated secondary detail to the **primary mechanism**, dropping the unverified date. Carried in the §1.6 fold. |
| `AUDITOR_NEXUS.md` / `GRANT_THORNTON_NEXUS.md` | `:104-113` / `:57-69` (the three-gatekeeper tables) | The screen **reframes** the thesis. The filed failure modes are perfection and priority failures in the lending chain (servicer, collateral agent, title insurer), **not** audit failures. RSM/BDO/GT audit quality is not implicated by either filed mechanism. KB-WAL-080 (ACTIVE, blank Stale_By) should be qualified by the desk. Carried in the §1.3 banner. |
| `INVESTIGATION_ROADMAP.md` | `:21-25` (Track 2: "if perfection failure → readthrough to other receivables programs at WAL") | This **is** the screen, first posed 3/26 and never run. Move it into the fold before retiring the file. |
| `STUPIN_CRE.md` fold | the "no other instance" row | **Scope limit (X6):** the CEO's 9/16 assurance (T2) covers **double-pledged titles** only. No public WAL statement was found covering a **UCC-perfection review** of other SPV or receivables facilities: **UNVERIFIED / absent**. KB-WAL-086's pass-#3 note stretches the quote over the Leucadia-era inventory question. The desk should correct that. |
| Q3 10-Q read (not FRAUD/) | `Q3_10Q_GRADING_FRAME_2026-09-24.md` §3 | The frame has no perfection leg. If the desk wants one, add it as a **dated pre-filing annotation**, never after the filing. Candidate cell: *does the Q3 10-Q describe any perfection, servicing or collateral-agent review beyond Cantor/LAM?* Present counts as informative. Absent is uninformative. |

**Paragraph for the desk to append to `FIRST_BRANDS.md`, after the §1.6 fold (drafted verbatim):**

> **Collateral-perfection screen (BROCK, KB-WAL-186; applied 2026-09-24).** Both WAL fraud losses failed at the *claim on the collateral*, not at credit selection: LAM defaulted after "servicing failures, including lapses in UCC filings" (Q1 10-Q, KB-WAL-144, A1), and Cantor's pledged loans carried forged title policies concealing prior liens (LA Superior 25STCV24263, KB-WAL-137). The auditor-gatekeeper framing in `AUDITOR_NEXUS.md` / KB-WAL-080 does not describe either filed mechanism. The forward question is therefore not "is there more NDFI exposure?" but "where else does WAL lend against collateral whose perfection or priority is maintained by someone else — a servicer, sponsor or agent?" Candidates by structure, **none tested**: mortgage warehouse + MSR lending ($7.155B, 12% of loans; perfection runs through custodial/agency acknowledgement arrangements), Note Finance (the book Cantor sat in; KB-WAL-022), and agented SPV private-credit facilities where WAL is a participating lender — e.g. the Deutsche Bank-agented Crestline SPV facility WAL joined 2026-09-18 (KB-WAL-195; WAL commitment undisclosed). Management's 9/16 "no other instance" (T2) is scoped to double-pledged *titles* and does not answer the perfection question; no WAL disclosure of a perfection/servicing review beyond Cantor has been found (UNVERIFIED). Who held the UCC-filing duty in the LAM structure — SPV, servicer or WAL's collateral agent — is not public (loan documents unfiled): UNVERIFIED.

---

## 3. Actions this review cannot take (outside its write scope, for the desk)

| # | Action | Owner |
|---|---|---|
| 1 | Correct the X2 comparison in KB-WAL-077's note. Qualify KB-WAL-079 and -080 (Tricolor never evidenced; gatekeeper reframed) | WAL (KB) |
| 2 | Add a KB row for the 9/16 CEO fraud quotes (X5). Fix the KB-086/-088 pointers and KB-086's over-scoped reading (X6) | WAL (KB) |
| 3 | Fix KB-WAL-177 "5M" → "$25M" (X8) | WAL (KB) |
| 4 | Trace or retire "~$46M Cantor residual" in `THESIS.md:281,297`, `WEAKNESSES.md:27`, `CLAUDE.md:16,150`. Fix `THESIS.md:281` "$29.4M" → $29.6M. Re-point `THESIS.md:410` | WAL (THESIS/WEAKNESSES/CLAUDE) |
| 5 | Primary reads that would settle open items: Jefferies' 3/8 press release (guarantee direction); NYSCEF docket (WAL v. JEF motion practice); LA Superior portal (25STCV24263); PACER / Stanford SCAC (class action); 2026 DEF 14A (committee and fees); WAL Barclays webcast replay (9/16 quotes) | WAL |

---

## 4. Summary of dispositions

| File | Disposition |
|---|---|
| STATUS.md | BANNER-AS-RECORD (rider: X1/X2/X3 wrong, $46M unreconciled, pointers → v2.4 + folds) |
| SYNTHESIS_V2.md | BANNER-AS-RECORD (same rider) |
| AUDITOR_NEXUS.md | BANNER-AS-RECORD (LEADERSHIP.md points to it; 3 vectors → 2 credits; Issuer B = inference) |
| AUDIT_COMMITTEE.md | BANNER-AS-RECORD (ZION auditor is EY not KPMG; fee Red Flag unsourced) |
| FIRST_BRANDS.md | FOLD (LAM litigation arc + perfection screen; `:137` $84.3M wrong) |
| STUPIN_CRE.md | FOLD (Cantor current state; judgement call vs retire) |
| WAL-JEF-PointBonita docx | NO-CHANGE (referenced by the live FIRST_BRANDS) |
| CLASS_ACTION_FINDINGS · GRANT_THORNTON_NEXUS · INVESTIGATION_ROADMAP · ISSUER_B_ELIMINATION · RSM_PUBLIC_AWARENESS · TRICOLOR · ZION_AUDIT_COMPARISON | RETIRE (`git mv` → `AGENTS/WAL/archive/`; ROADMAP after the Track-2 carry; ISSUER_B with a KB-071 pointer update) |
