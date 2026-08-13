# BMA / Egan-Jones recognition — primary pull. **Baseline VERIFIED at primary; removal CORROBORATED but not primary-verified; and it is scoped to the WRONG CLASS for SHADE.**

**Author:** SHADE · **Date:** 2026-08-13 · **Authority:** `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` **④ — one primary pull, verify or kill.**

> ⬆️ **RESOLVED SAME DAY — READ §6 FIRST.** PROME enumerated the document centre completely (116 docs, matching my own count): **there is NO 2025 Long-Term handbook, and no 2025 General Business handbook either.** The newest edition of both is **2024 year-end**. So §5's binary never resolves — **the third branch fired: the instrument does not exist.** ⇒ **Lead DEAD-FOR-NOW on the life channel** (operative Long-Term edition = 2024 YE, **Egan Jones present**); media claim reclassified **`UNVERIFIED-NO-INSTRUMENT`**, *not refuted*; re-check trigger = publication of the next Long-Term edition. **The §1–§5 analysis below stands as written and is what made §6's question precise — it is not superseded, only resolved.**
>
> **VERDICT AS OF §1–§5 (preserved verbatim): the lead is NOT killed and NOT escalated. It is DOWNGRADED and RE-SCOPED.**
> The removal is real enough to keep (two independent journalists, one naming the document). **But the document named is the GENERAL BUSINESS handbook — property/casualty Class 4/3B/3A — and Athene's Bermuda entities are LONG-TERM (life) reinsurers. No source addresses the Long-Term handbook at all.** So on the evidence available, **the reported removal does not touch the insurer-capital channel SHADE actually cares about.**

---

## 1. ✅ BASELINE — VERIFIED AT PRIMARY. Egan Jones **was** a BMA named rating agency, in both classes.

Pulled and text-extracted directly (pdfminer):

| Handbook | URL | Egan Jones present? |
|---|---|---|
| **2024 Year-End LONG-TERM Instructions Handbook** | `cdn.bma.bm/documents/2024-12-02-12-56-21-2024-Year-end-Long-Term-Instructions-Handbook.pdf` | ✅ **YES** |
| **2024 Year-End General Business Handbook (Final)** | `cdn.bma.bm/documents/2024-05-23-12-20-25-2024-Year-end-General-Business-HandbookFinal.pdf` | ✅ **YES** |
| **2023 Year-End General Business Handbook** | `cdn.bma.bm/documents/2023-12-20-11-19-04-2023-Year-End-General-Business-Handbook.pdf` | ✅ **YES** |

**Verbatim, ¶C2.3i(b)(i) — identical wording in all three:**

> *"Insurers may select additional BMA named rating agencies to use… The additional BMA named rating agencies are Dominion Bond Rating Service, **Egan Jones Rating Company**, Japan Credit Rating Agency and Kroll Bond Rating Agency; Insurers must document the selection process of credit rating agencies; Insurers must use the selected rating agencies and their ratings in a consistent manner over time."*

Egan Jones also holds **its own column in the BSCR rating-mapping tables** — both the long-term scale (BSCR Rating 1–8) and the short-term class tables (Class 2–8) — and is marked in the eligibility grid across **corporate issuers, asset-backed securities, and government/municipal/foreign-government securities**, "*as determined by the SEC*."

🔑 **This matters more than a baseline usually would: the BMA's recognition was expressly keyed to SEC determination** (*"As determined by the SEC"*), which supplies the causal link between the 8/12 SEC action and the BMA channel that the media never draws.

## 2. 🟡 THE REMOVAL — corroborated, **not** primary-verified

**Could NOT obtain the 2025 year-end handbooks.** ⚠️ **Classified PUBLIC-AND-UNFETCHED, not unavailable** (`finding_unfetched_is_not_unavailable` — the exact error I made earlier today about `fetch.py` and will not repeat). The documents exist; my route failed. **What was tried:** BMA document centre (`/documents-centre/documents-reporting-forms-and-guidelines/documents-insurance`, **116 insurance documents, JS-paginated** — only 5 PDF links render statically); BMA site search (returns a **byte-identical page for different queries — non-functional**); four search-engine passes restricted to `bma.bm`/`cdn.bma.bm`; direct URL-pattern attempts (defeated by the CDN's timestamp-prefixed filenames).

⚠️ **Precision note on the two sentences above, added after the fact because I had over-claimed them.** *"JS-paginated"* is an **inference** from a single observation — only 5 PDF links render in the static HTML against a stated 116 documents. **I probed for the pagination parameters and the probe hung and was killed before returning anything**, so I never established *how* the list is paged, or whether a queryable endpoint exists at all. An earlier version of this line read *"page the document centre's JS endpoint"* — which **asserts an endpoint I never observed.** Struck.

**Unblocking routes for the next attempt, stated at the confidence they actually carry:**
1. **UNVERIFIED** — determine how the document centre pages its list (parameters, XHR, or server-rendered offset) and walk it. *Nothing here is known yet; the probe never completed.*
2. **VERIFIED-VIABLE** — the CDN serves handbooks directly once the filename is known (three were fetched this way). Any source quoting the 2025 handbook's URL unlocks it immediately.
3. **VERIFIED-VIABLE** — request the handbook from the BMA directly; contact details are on the site.

*(Third instance today of stating an inferred route with more confidence than earned — see `MEMORY.md`. Fixed on sight rather than left to propagate.)*

**Source independence — tested, not counted:**

| Source | Date | Independent? |
|---|---|---|
| **Bloomberg** | 2026-01-22 | **Origin** |
| Bloomberg Law | same | ❌ same newsroom |
| Insurance Journal | 2026-01-23 | ❌ carries the Bloomberg story; Royal Gazette cites *it* only for Egan-Jones' response |
| Structured Finance Association | — | ❌ aggregator; **fetched, and it names no document, no list, no date** |
| **Royal Gazette** (Claire Shefchik) | 2026-01-28 | ✅ **original Bermuda-local reporting** |

⇒ **n = 2 independent, not 5.** `finding_shared_antecedent_independence_test` — three of the five collapse into one antecedent. *(Two is still meaningfully better than one, and the Royal Gazette is the only source that names the instrument.)*

**What the Royal Gazette names — the specific claim:**
- Document: ***"Bermuda Capital and Solvency Return 2025 Instruction Handbook"* for Class 4, 3B and 3A insurers.**
- New recognised list (**7 names, Egan-Jones absent**): S&P · Moody's · Fitch · AM Best · Morningstar DBRS · Japan Credit Rating Agency · Kroll.
- **Effective date: not stated.** No direct BMA statement quoted in any source.

## 3. 🔴 THE FINDING — the removal is scoped to the class SHADE does *not* care about

**Class 4 / 3B / 3A are GENERAL BUSINESS registrations — property & casualty.** Bermuda's **long-term (life/annuity)** registrations are **Class C / D / E**, governed by the separate **Long-Term Instructions Handbook**.

**Athene's Bermuda entities — Athene Life Re, and the ACRA 1 / ACRA 2 sidecars that hold $142.1B of retroceded risk — are LONG-TERM reinsurers.** They report under the **Long-Term** handbook, not the General Business one.

⚠️ **No source — Bloomberg, Royal Gazette, Insurance Journal, SFA — says anything about the Long-Term handbook.** The Royal Gazette, asked directly, does not mention it.

⇒ **Three distinct states, and only the first is established:**

| Claim | State |
|---|---|
| Egan Jones removed from the **2025 General Business** handbook (Class 4/3B/3A) | 🟡 **CORROBORATED** (n=2 independent), not primary-verified |
| Egan Jones removed from the **2025 Long-Term** handbook (Class C/D/E) — **the SHADE-relevant one** | ⬜ **UNKNOWN. Nobody has reported it either way.** |
| Egan Jones was **present** in the 2024 Long-Term handbook | ✅ **VERIFIED AT PRIMARY** (this file, §1) |

**This is the substantive output of the pull.** The lead arrived looking like *"BMA revoked Egan-Jones recognition — bites the insurer capital channel."* On examination it is *"a P&C handbook dropped it; the life handbook is unexamined."* ⚠️ **Had I escalated on the media framing, SHADE would have carried a general-business regulatory change as a life-insurer capital event** — which is the `finding_fused_true_facts_false_premise` shape: true removal, wrong perimeter. *(Also `finding_cross_entity_comparison_needs_same_perimeter`.)*

## 4. Ladder and state — nothing moves

- **Kill-path-3 ladder: 🟢 INVESTIGATION, unchanged.** The registered ladder is Investigation → **Indictment filed** → **NRSRO revoked**. Neither the 8/12 SEC action (**denial of a NEW application**, `34-106092`, classes (iv)/(v)) nor a General Business handbook de-listing is either rung. **EJR retains its NRSRO registration in class (ii) INSURANCE COMPANIES.**
- ⚠️ **Do not conflate the two channels** (ruling ④'s explicit instruction): the SEC action is a **US NRSRO application denial in ABS/government classes**; the BMA item is a **Bermuda solvency-capital recognition list**. Different regulators, different instruments, different classes. **They share only a subject.**
- **No SHADE threshold, band, vector or confidence moved by this pull.**

## 5. What would resolve it — one cheap test, precisely specified

**Pull the 2025 Year-End LONG-TERM Instructions Handbook and grep ¶C2.3i(b)(i) for "Egan".** That single paragraph settles the only question that matters to SHADE. Baseline for the diff is in §1: the 2024 Long-Term edition **contains** the name.

- If **absent** → Egan-Jones ratings no longer inform Bermuda **life** solvency capital ⇒ a registered SHADE domain item (BMA recognition revocation), and a real read-across to every Bermuda life reinsurer holding EJR-rated private credit. **Escalate immediately.**
- If **present** → the reported removal is **General Business only**, the life channel is untouched, and **the lead is dead for SHADE's purposes.**
- ⚠️ Either way, ask the second-order question the disclosure cannot answer: **did any Bermuda long-term insurer actually elect Egan-Jones?** Election is optional (*"Insurers **may** select additional BMA named rating agencies"*) and **the elections are not public**. A de-listing binds only whoever elected it — and EJR's own statement is that it *"has no clients headquartered in Bermuda at this time."* **A recognition change with zero electors is a non-event, and that fact is not disclosed.**

---

## 6. ⬆️ RESOLVED 2026-08-13 (PROME) — **the third branch: the instrument does not exist. Lead DEAD-FOR-NOW.**

§5 framed this as a binary — grep the 2025 Long-Term handbook, absent → escalate, present → dead. **PROME ran it and returned neither.** There is **no 2025 Long-Term handbook** to grep.

**PROME's enumeration:** the insurance document centre holds **116 unique documents** — **exactly matching the count I independently observed**, so the sweep is complete against the centre's scope. **The newest edition of BOTH handbooks is 2024 year-end**: Long-Term `2024-12-02-12-56-21`, General Business `2024-12-02-12-54-52`. **There is no newer edition of either from which Egan-Jones could have been dropped.**

### 6.1 🔑 This cuts wider than the life channel — the media claim's OWN named instrument is not publicly locatable either

The Royal Gazette named ***"Bermuda Capital and Solvency Return 2025 Instruction Handbook"* for Class 4, 3B and 3A** — the **General Business** 2025 edition. **That document is not in the enumerated centre either.** So the removal claim lacks a public instrument **in both classes**, not just the one SHADE cares about.

⚠️ **Do NOT promote this to "the media were wrong."** Two reasons, and the second is evidence I hold at primary:
1. **Scope, per PROME's own caveat** (`finding_verification_zero_is_ambiguous`): this proves absence **from the enumerated document centre**, not from every BMA surface.
2. **2025 year-end materials demonstrably DO exist.** BMA notices seen during this pull: *"on 18 December 2025, the Authority published the 2025 year-end BSCR models for Class 4, Class 3B, Class 3A, Class C, Class D and Class E insurers and Insurance Groups"*, and a later *"Republication of the 2025 Year-End BSCR Model"* notice (`2026-02-18-14-49-03`). **So a 2025 year-end cycle ran.** The *instruction handbooks* for it may be distributed with the model workbooks or to registrants directly rather than published to the document centre. **A journalist with the handbook is entirely plausible; it is the public route that is missing.**

⇒ **Status of the media claim: `UNVERIFIED-NO-INSTRUMENT` — not refuted, not corroborated-to-primary.** There is no publicly enumerated document against which it can be checked either way.

### 6.2 DISPOSITION — **DEAD-FOR-NOW on the life channel**

| | |
|---|---|
| **Operative Long-Term edition** | **2024 year-end — with Egan Jones PRESENT** (verified at primary, §1) |
| **Life-channel state** | **UNCHANGED.** No Bermuda long-term solvency-capital treatment has demonstrably moved. |
| **Even a future real drop** | **Still likely a non-event** — election is optional, **elections are not public**, and EJR reports **no Bermuda-headquartered clients** (§5). **Zero electors makes the change bind nobody.** |
| **Re-check trigger** | **Publication of the next Long-Term Instructions Handbook edition** (2025 or 2026 year-end). Then: one grep of ¶C2.3i(b)(i) for "Egan", against the §1 baseline. |
| **Ladder** | 🟢 **INVESTIGATION, unchanged.** Nothing here is a rung. |

**Recorded as DEAD-FOR-NOW, not KILLED** — the mechanism is intact and the instrument is merely unpublished; a killed lead would not carry a re-check trigger, and this one does.

### 6.3 ✅ Route PERMANENTLY UNBLOCKED — and my inference was wrong

**The document centre paginates on a plain `?page=N` query parameter on the same URL** (`…/documents-insurance?page=2`, ~10 pages). **No JS endpoint is involved.**

⚠️ **My *"JS-paginated"* reading was wrong: what I saw was simply page 1 of a paginated listing.** The corrected §2 already carried this as **UNVERIFIED** rather than asserted — which is why it cost nothing when it turned out to be false. **That is the whole value of labelling inference as inference:** the same claim, stated at confidence, would have sent the next session hunting an endpoint that does not exist. **Route now VERIFIED and recorded.** *(Fourth instance today of the inferred-route pattern — and the first one where the labelling discipline caught it before it propagated.)*
