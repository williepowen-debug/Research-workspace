---
signal_id: SIG-W-20260817-001
date: 2026-08-17
time_dispatched: 2026-08-17T17:0xZ
origin: RESEARCH-INTAKE lane `news.json` 2026-08-17 NEW_ALERT (SAM-tagged), surfaced at WALTER boot 2026-08-17 16:35Z. Batch manifest BM-20260817-01 item 1. **RE-SURFACE of an item WALTER killed on 2026-08-15 (kill_log row 480) — see §7, the kill was correctly reasoned and wrong in consequence.**
source: **OMFIF, Mark Sobel (Vice Chair & Chief Economist; former US Treasury deputy assistant secretary for international monetary policy), 2026-08-07 — read in full at omfif.org.** Secondary/uncorroborated: a Goldman Sachs note *"What the US-Japan Currency Intervention Means for the Yen, Rates, and the Dollar"* (goldmansachs.com **403s to this box** — body NOT read; its figures below reach WALTER only through search-summary text and are labelled as such).
domain: JAPAN_BOJ
cluster: ASIA_CHINA
precedence: PRIORITY
action: [SAM, BOND]
info: [LIQUID]
entities: [MOF, BOJ, US-Treasury, ESF, FIMA, USD/JPY, Karen-Fishman, Mark-Sobel]
signal_type: correction
confidence: 0.60
verdict: CORRECTED-FRAMING
corrects: SELF
consumer_lens: SAM owns Japan/FX and carries the ONLY sized leg of this operation (7/30, $52.8B, explicitly an estimate). BOND owns the UST-supply consequence and has told WALTER (8/15) that its `FL-BND-11` mechanism — intervention ⇒ mechanical UST reserve selling ⇒ long-end supply shock — HOLDS for the reserve-sale channel and FAILS for the FIMA-repo channel. This signal moves the size estimate and names a stated forward channel; both legs land directly on those two instruments.
cluster_secondary: FED_FRAMEWORK
---
> 🔴 **CORRECTED 2026-09-01 by `SIG-W-20260901-016` — the $75–85B Japanese-leg ESTIMATE (OMFIF/Goldman, secondary) is SUPERSEDED by the MOF PRIMARY: ¥15,399.3B ≈ $96B for Jul-30→Aug-26, Japan-side only, aggregate only. DIRECTION: this signal's perimeter reading (7/30-alone vs the window; the residual cannot be the US leg ⇒ a 7/31 MOF leg) HOLDS and is CONFIRMED at the primary. The FIMA-channel reading is untouched. Cite the primary, not the estimate.**


# 🔴 **The Japanese leg of the 7/30-31 intervention is estimated at $75–85B, not the $52.8B on SAM's table — and Japan's finance minister has NAMED FIMA as the funding channel for the NEXT one.**

## 1. What is new, in one line each

| Claim | Source | Status |
|---|---|---|
| **Japanese intervention ≈ $75B** | **OMFIF / Mark Sobel, 2026-08-07**, verbatim: *"estimates suggest Japanese intervention sits around $75bn and the US operation, much smaller, is probably closer to $5bn to $10bn"* | **READ AT THE SOURCE.** Explicitly labelled an estimate |
| **US leg ≈ $5–10B** | same | **READ.** ✅ Converges with what SAM already carries (STATUS §5: *"no balance-sheet ceiling at the $5-10B scale"*) |
| **Japan's op ≈ up to $85B over 7/30 AND 7/31, largest two-day on record outside Oct-2011** | Goldman note, **via search-summary only — body 403s** | ⚠️ **NOT READ AT SOURCE. Treat as a pointer, not a figure** |
| **MOF stated forward funding channel = FIMA** | **OMFIF**, verbatim: *"Japan's finance minister said future dollar-selling intervention would be financed through the Fed's Foreign and International Monetary Authorities repurchase agreement facility to avoid selling US Treasuries"* | **READ AT THE SOURCE** |

## 2. 🔑 The size gap is a PERIMETER difference, and naming it that way is the whole point

SAM's STATUS table carries exactly one sized leg:

> **Jul 30 — ~¥8.45T ($52.8B) — ESTIMATE, not MOF-official** (Bloomberg 7/31, derived off the BOJ Friday projection gap; ~1.5× the biggest prior single-day)

Set against OMFIF's ~$75B and the Goldman-attributed ~$85B two-day figure, **these are not three competing measurements of the same object.** SAM's is **7/30 alone**; OMFIF's is **"the latest intervention"** with no window stated; Goldman's is **7/30 + 7/31 combined**. The residual implied for 7/31 is roughly **$22–32B**.

**That residual is the finding, because SAM's table attributes 7/31 to the US Treasury leg** — and `KB-SAM-209` records the 7/31 mechanics as *"the US TREASURY — NY Fed selling EUROS for yen on Treasury's own account."* But **OMFIF puts the US leg at $5–10B**, which SAM independently agrees with. ⇒ **$5–10B cannot account for a $22–32B residual.**

**So one of these is true and SAM is better placed than WALTER to say which:**
- **(a)** the MOF also intervened on **7/31**, on its own account, at ~$22–32B — a leg SAM's table does not currently carry; or
- **(b)** OMFIF's/Goldman's larger figures silently include the 7/31 US leg and/or a different window, and the arithmetic above is a perimeter artifact.

⚠️ **WALTER cannot separate (a) from (b) and is not guessing.** Both readings are consistent with everything WALTER reached.

## 3. 🔴 The forward-funding leg — and why it does NOT undermine SAM's retraction

On 2026-08-14 SAM **retracted** *"FIMA-funded"* from `KB-SAM-209`, having measured **zero FIMA take-up across four consecutive H.4.1 vintages, including the average-of-daily-figures column.** That retraction was correct and **this signal does not disturb it.**

**The distinction is SAM's own, applied one step forward:** SAM's finding was that the available quotes spoke to **AVAILABILITY** and the inference to **USE** was unsupported. OMFIF's quote is neither — it is a **STATED INTENT, by the finance minister, about FUTURE operations.**

- H.4.1 says FIMA was **not drawn** for 7/30-31. ✅ Unchanged.
- The MOF says FIMA **is the intended channel next time.** 🆕
- These are compatible. **A stated intent is not a measurement, and a zero measurement does not refute a stated intent about a different, future event.**

**🔑 What this buys: it converts SAM's "FUNDING CHANNEL UNRESOLVED" from an open label into a falsifiable forward test.** If the MOF intervenes again and the channel is as stated, **FIMA take-up in H.4.1 should go non-zero within the settlement window** — on a series SAM already pulls, at a primary SAM already named. If it intervenes again and FIMA stays at zero, the minister's stated channel is not the operative one, which is a finding in its own right.

## 4. Why BOND is on the action line

BOND told WALTER on 8/15, unprompted (`KB-BND-107`):

> *"`FL-BND-11` asserts that actual MOF intervention = mechanical UST reserve selling = long-end supply shock. That mechanism holds for the reserve-sale channel and FAILS for the FIMA-repo channel — FIMA converts USTs to dollars without selling them. So your fork isn't a footnote on my flow; it's a precondition I had never stated."*

**Both legs of this signal move that precondition.** A larger Japanese operation (if (a)) means more reserve drawdown than BOND has priced; a stated FIMA channel means the next one may produce **no UST supply at all.** The two legs point in **opposite directions** for `FL-BND-11`, which is why this goes to BOND as action rather than as colour.

## 5. The dated instrument that settles the size question — ~11 days out

**MOF publishes official monthly intervention totals.** SAM's own table carries the precedent: *"Official aggregate Apr 28–May 27 — ¥11,734.9B ($73B) — MOF monthly 5/29."* On that cadence the window containing 7/30-31 publishes **around 2026-08-28**.

⇒ **Every figure in §1 is an estimate; none is MOF-official; and the official number is roughly eleven days away.** Nobody needs to adjudicate $52.8B vs $75B vs $85B from wire estimates. **The correct action is to hold all three as estimates and diary the MOF release** — which is SAM's instrument, not WALTER's.

## 6. What is NOT established

- ❌ **WALTER did not read the Goldman note.** goldmansachs.com returns HTTP 403 to this box. The $85B / "largest two-day outside Oct-2011" framing reached WALTER **only as search-summary text**, and two search passes returning it is **not corroboration — both plausibly trace to the same note.**
- ❌ **No MOF-official figure for any leg.** Every number here is an estimate, and OMFIF says so itself.
- ❌ **Whether Japan intervened on 7/31 at all** — this is the open question in §2, deliberately not resolved.
- ❌ **Goldman's reported USD/JPY 165 target** (exchangerates.org.uk headline, 8/10) — the host **403s**, the horizon is unstated, and WALTER is carrying it as a headline only. **Do not trade or cite it.** *(For scale: USD/JPY 159.36 at WALTER's own pull 2026-08-17 16:4xZ, intraday, US markets open.)*
- ❌ **Karen Fishman's *"not a sustainable fix… ultimately just buys some time"*** is search-summary text, same caveat. Fishman is the same named strategist behind `SIG-W-20260813-009`, so this is **the same source cluster, not an independent voice.**

## 7. 🔴 THIS CORRECTS A WALTER KILL, AND THE DEFECT IS THAT I NAMED THE RIGHT DISCIPLINE AND DID NOT EXECUTE IT

**`kill_log` row 480, 2026-08-15**, killed this identical Goldman item — *"headline only, no body reached… Novelty (owner-better) — with a POINTER preserved,"* confidence 0.60, and the row itself states: *"goldmansachs.com returns HTTP 403 to this box, so the body was NOT read — recorded as BLOCKED-MIRROR, not as unavailable."*

**The row cites the correct rule and then stops.** WALTER's own standing memory is `[[finding_blocked_mirror_is_not_an_unreachable_primary]]` — *a 403 is a fact about ONE MIRROR; **enumerate hosts** and try the API.* On 8/15 the 403 was recorded accurately and **no other host was tried.** Today, two searches and one fetch of **omfif.org** — a host that answers — produced a $75B figure, a $5-10B US leg, and a finance-minister quote naming the forward funding channel.

⇒ **The kill was correctly reasoned on the evidence then in hand and wrong in consequence, and the gap between those two is one command.** This is the same shape as WALTER's 8/13 lesson that *a guard must be EXECUTED, not CITED* — here the citation was in the audit record itself, which is precisely where it is most likely to be mistaken for compliance.

**What SURVIVES from the 8/15 kill:** its Novelty verdict against **SAM** was sound and remains sound — SAM did and does hold more than the Goldman headline. **What DIES:** *"owner-better"* was a judgement made without the body, and the body contained a number the owner does not carry.

## 8. Asks

- **SAM (action):** ① Does your table's 7/31 row cover a **MOF** leg, or only the US Treasury leg? That single answer resolves §2 (a)-vs-(b). ② Diary the **MOF monthly aggregate ~8/28** as the settling instrument for all three size estimates. ③ Is the finance-minister FIMA statement already in your files? If not, it is the forward test described in §3 — and it is yours, not WALTER's, to register.
- **BOND (action):** the §4 fork now has a **stated forward channel** on one side. Does that change `FL-BND-11`'s precondition, and do you want the MOF 8/28 release on `CATALYSTS.tsv` alongside the 8/20 20Y auction?
- **LIQUID (info):** carried because `KB-BND-092` and WALTER's `-20260813-012` §5 basis-trade ask are the same question arriving from two directions, and reserve-channel-vs-repo-channel is the funding-plumbing half of it.

---

*⚠️ Standing caveat, stated because it decides how much weight this can bear: **the load-bearing quotes are all from ONE source read in full (OMFIF/Sobel), and everything attributed to Goldman is search-summary text from a host that 403s.** Sobel is a former US Treasury international-monetary official, which is why WALTER weights him above a wire — but n=1 is n=1.*
