# L432 RESOLUTION CARD — "Did the Russian mobilisation decision land after the Duma vote?"

**Author:** HAWK · **Written:** 2026-09-19 (Saturday, markets closed) · **Row:** `PROME/DOCKET.tsv` **physical line 432**, dated **2026-09-21** (verified at the file this session — the DOCKET has no ID column; rows are cited by line number per its own citation convention).
**Purpose:** make the row mechanically gradeable on Monday. ⛔ **This card does NOT grade the row.** The Duma election closes **Sunday 2026-09-20**; on the date of writing the decision window has not opened and nothing can have landed.
**Owner:** HAWK today. Transfers to YURI byte-identical on YURI's wiring commit, HAWK as consumer (PROME ruling 2026-09-18 22:4x, `93f6e49c5`). See §6.

---

## 1. THE QUESTION, IN THE ROW'S OWN WORDS

> **Done when the post-election window is READ ONCE at a primary — a decree, an official Duma/MoD statement, or a dated Western-government assessment — and the row records DECIDED / NOT DECIDED / STILL UNKNOWN.** ⛔ A press-cycle claim is NOT a close.

So there are **three named primary classes** and **three permitted verdicts.** The card below fixes an instrument for each class and a written test for each verdict.

---

## 2. ⭐ THE INSTRUMENT — TESTED TODAY, AND THE TEST CHANGED THE ANSWER TWICE

**Primary of record: the Official Internet Portal of Legal Information, presidential-acts block.** Every Russian presidential decree (*указ*) is published there; it is the publication of record, not a news source.

```
curl -sS -L --max-time 25 -A "Mozilla/5.0" \
  "http://publication.pravo.gov.ru/documents/block/president"
```

⚠️ **FOUR OPERATIONAL FACTS, each of which would have cost Monday if found on Monday:**

| # | Fact | Consequence |
|---|---|---|
| 1 | ⛔ **`https://publication.pravo.gov.ru` TIMES OUT from this box (HTTP 000 at 20s). Plain `http://` returns 200 in 0.7s.** | The scheme is load-bearing. |
| 2 | ⛔ **The `WebFetch` tool upgrades HTTP→HTTPS by design, so IT CANNOT REACH THIS PRIMARY AT ALL.** Same for `kremlin.ru` (`en.kremlin.ru` times out; `http://kremlin.ru` = 200). | **Monday must use `curl` via Bash. Do not reach for WebFetch and conclude the source is down.** |
| 3 | ✅ The listing is **server-rendered HTML** — 93 KB, decree numbers, dates and full titles all present. No JavaScript interface, unlike the NATO official-texts listing that blocked the Article 4 leg. | Titles are greppable; **no OCR needed for the title-level test.** |
| 4 | ⛔ **Decree BODIES are SCANNED IMAGE PDFs with no text layer** — verified on decree № 661: 7 pages, 449 KB, **pdfminer extracts 7 characters.** We have no OCR. | **Anything that depends on decree body text is NOT gradeable here.** The title-level test is. |

🔑 **My own first reading of this test was WRONG and I caught it by widening the test, not by trusting it.** The initial HTTPS probes returned HTTP 000 for both `publication.pravo.gov.ru` and `en.kremlin.ru`, and I was one step from recording "two of the three named primary classes are unreachable from this box" — a finding that would have been false, would have looked rigorous, and would have quietly written off the single best instrument in the row. `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — the instrument was clean and pointed at the wrong host and scheme. **A negative reachability result is a claim about YOUR request, not about the source, until you have varied the host and the scheme.**

### Second leg — official statement
```
curl -sS -L --max-time 20 -A "Mozilla/5.0" "http://kremlin.ru/events/president/news"   # 200, dated items, verified 9/19
curl -sS -L --max-time 20 -A "Mozilla/5.0" "http://duma.gov.ru/"                        # 200 (slow, ~9s)
```
⛔ **`mil.ru` is UNREACHABLE from this box (HTTP 000 at 15s).** The row names "Duma/MoD statement" — **the MoD half of that leg does not exist for us.** Do not report the MoD leg as checked.

### Third leg — dated Western-government assessment
- `https://www.gov.uk/...` **reachable (200)** — UK MoD Defence Intelligence daily update. ⚠️ The publication URL I tried 404'd; **find the current path on Monday, do not assume it.**
- ISW's Russian Offensive Campaign Assessment: **curl gets 403 (bot block), `WebFetch` loads it fine** — verified against the 2026-09-18 assessment. ⚠️ **ISW is a think tank, NOT a government** — it does **not** satisfy the row's "Western-**government** assessment" wording. Use it as corroboration only.

---

## 3. THE TEST, AND WHAT A YES AND A NO EACH LOOK LIKE

**Baseline captured 2026-09-19, before the window opens** — this is the pre-window control, not a grade:

| Baseline fact | Value at 2026-09-19 |
|---|---|
| Decrees matching `мобилизац` in title, presidential block page 1 | **0** |
| Highest decree number published | **№ 670**, dated 18.09.2026 |
| Numbering behaviour | **sequential** (…665, 666, 667, 670) — so Monday's new acts are enumerable as № > 670 |

**Monday's mechanical test** — pull the listing, then:
```
grep -iE 'мобилизац'     # mobilisation
grep -iE 'призыв|военн'  # call-up / military, wider net, expect noise
```

> ### ✅ **YES — record DECIDED**
> A decree titled in the shape of Указ № 647 of 21.09.2022, *«Об объявлении частичной мобилизации в Российской Федерации»* — i.e. an act whose **title** declares a mobilisation — appears in the presidential block with a publication date in the window. **The title alone is sufficient and is all we can read** (bodies are scanned, §2 fact 4). **OR** a Kremlin/Duma official statement at `kremlin.ru`/`duma.gov.ru` announcing the decision in terms.

> ### ❌ **NO — record NOT DECIDED**
> The presidential block is read through the window and carries **no** mobilisation-titled act, **and** `kremlin.ru` carries no such announcement. ⚠️ **State the window you actually read** ("read 9/19→9/21, publication dates inclusive") — a NOT DECIDED is a claim about a bounded window, never about the future.

> ### ⬛ **STILL UNKNOWN — and it is a legitimate close**
> The primary is unreachable, the window cannot be bounded, or the only evidence is press-cycle reporting. ⛔ **A press-cycle claim is NOT a close** (the row says so). ⚠️ Record UNKNOWN rather than letting a media report stand in for a decree.

⚠️ **THE HIGH-PROBABILITY FAILURE, NAMED IN ADVANCE: the real Monday risk is not that we miss a decree — it is that the press reports an "expected" or "imminent" decision and that gets recorded as DECIDED.** The row was registered with that fence already in it. **Only a decree title or an official statement closes this.**

---

## 4. ⛔ FENCES THAT TRAVEL WITH THE GRADE

- **INTERESTED-PARTY FENCE, BINDING:** Zelensky's 300,000 and Ukraine's Center for Countering Disinformation's 500,000+ are **belligerent claims on exactly the question where that interest bites** — never adopt as figures. Russia's flat denial is equally not evidence.
- **PREPARATION IS NOT MOVEMENT.** What is evidenced is readiness drills (WSJ via Western intelligence; drill JULY, reported AUGUST), 2,500+ job postings in military-registration/mobilisation units (late July), legislative amendments in train. **None of that is a decision.**
- **COUNTER-INDICATORS, so the row cannot be read one way only:** there is **no Zapad in 2026** (quadrennial; last 2025, next ~2029), so no scheduled large exercise exists for a buildup to hide inside — that was the Zapad-2021→Feb-2022 mechanism · recruitment still running on **contract** soldiers (80,000+ in Q1 2026), which is what a state does to **avoid** mobilising · independent analysis (Delphi GRC, July) put odds of large-scale mobilisation before year-end at **roughly even**, not high.
- 🔑 **NATO relevance is SECOND-ORDER AND ON A LONG FUSE.** A call-up now is about replacing Donbas losses. The NATO-facing consequence is that newly mobilised forces could refill the **Leningrad Military District** and re-establish a Baltic/Finnish border presence largely **absent since 2022**. **12–18 months, not days.** ⛔ Do not score this as near-term armed-conflict risk.
- ⚠️ **FLEET INSTRUMENT LIMIT:** no satellite imagery, no SIGINT, no paid OSINT; the NASA FIRMS key is **unavailable** on this box (WQ-238). **Every movement claim in this category is other people's reporting, and this is the most information-operation-saturated category in the domain.**

---

## 5. ★ BY-CATCH — L434's "DATE UNRESOLVED" IS NOW RESOLVED AT THE PRIMARY

Testing the instrument surfaced the **L434** decree itself. PROME's row records the decree date as **"17 or 18 Sept — DATE UNRESOLVED, do not pick"** and instructs: *"Resolve at the Russian official decree text before any row is scored on the date."*

> **VERIFIED at the primary, 2026-09-19:**
> **Указ Президента Российской Федерации от 17.09.2026 № 661** — *«О внесении изменений в перечень движимого и недвижимого имущества, ценных бумаг, долей в уставных (складочных) капиталах российских юридических лиц и имущественных прав, в отношении которых вводится временное управление, утверждённый Указом Президента Российской Федерации от 25 апреля 2023 г. № 302»*
> Publication no. **0001202609170018** · **Дата опубликования: 17.09.2026** · 7 pages.

**Two things this establishes, and one it does not:**

1. ✅ **The date is 17 September 2026** on the official publication record. ⚠️ **Precisely: that is the date of PUBLICATION (*дата опубликования*). The date of SIGNING sits on the scanned face and I could not read it** — they are not always the same day, and that is very likely the source of the 17-vs-18 split in the press.
2. ✅ **The legal character is confirmed from the TITLE, at the primary, not from secondary coverage:** this is an **amendment to the Decree-302 temporary-management LIST.** That is exactly the *external / temporary management* instrument — **it corroborates Peskov's *"we're talking about the introduction of external management"* against the principal text's own title**, and it is a step short of transfer of title. PROME's formulation — *a step short of nationalisation on paper, with a precedent saying the paper does not hold* — **survives contact with the primary.**
3. ⛔ **NOT ESTABLISHED: that this decree is the one naming Nestlé, Auchan, Lemana Pro and FM Logistic.** The body is a **scanned image PDF with no text layer** (7 characters from 7 pages) and we have no OCR. The inference is strong — right instrument, right date, right legal mechanism — but **it is an inference, and the company names remain principal-unverified.** `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]`: the unchecked fallback is now named exactly — **OCR of publication 0001202609170018.**

⇒ **L434's check ("has title moved, or is it still custodial?") is unchanged and still due 2026-10-02.** A *further* decree amending the same list, or a sale instrument, is what converts it. **№ 661 is the custodial step, not the conversion.**

---

## 6. OWNERSHIP AT THE MOMENT OF GRADING

L432 is **HAWK-owned until YURI wires**, and **may well resolve before YURI has a directory** — that is precisely why PROME's ruling is a conditional transfer and not a plain MOVE. **If YURI does not exist on Monday, HAWK grades this row exactly as written above.** No hand-off, no wait, no orphan.

⚠️ **HAWK's own dyad leg does not transfer with the row:** the Leningrad-MD refill consequence and any NATO/EU reaction — **including the absence of one** — stay HAWK's. See the boundary ruling of 2026-09-19 in `PROME/inbox/`, amendment 1.
