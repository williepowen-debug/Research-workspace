# BOND Mail / Refresh Protocol

**Purpose:** Standard operating procedure for BOND when processing inbox signals or doing a refresh.

## Normal Refresh Sequence

1. Read `CLAUDE.md`.
2. Read `STATUS.md`.
3. Read this `PROTOCOL.md`.
4. Read `workbook/SCHEMA.tsv` and `AGENTS/VOCABULARIES.tsv` before writing workbook rows.
5. Process `inbox/*.md` only if the task asks for inbox processing.
6. Pull/update relevant data:
   - HY OAS, CCC OAS, IG OAS, DGS2/DGS10/DGS30 from FRED / market-data tool.
   - Auction results from Treasury/FiscalData.
   - Dealer positions from NY Fed FR2004 — **run `monitors/fr2004_fetch.py`, never hand-query the API.** ✅ ~~Known access gap~~ **CLOSED 2026-07-28, and it was never an access limit: the query used a stale API series break (`SBN2022`), which returns HTTP 200 with real data that simply stops at 2024-07-02 — indistinguishable from "the API caps pre-2026." Live break is `SBN2024`; the bucket keyid is `PDPOSGSC-G7L11`, not zero-padded.** *(This line still read "known access gap / 5 prints owed" on 2026-08-15, 18 days after the gap closed — a stale blocker is worse than no note, because it tells the next session not to try. Fixed on the inbox-drain pass.)* Still true and unchanged: this is a **stock** vector, so benign auction flow cannot substitute for it. See `monitors/DEALER_CAPACITY.md`.
   - **Foreign-official UST custody (H.4.1 memorandum item)** — `federalreserve.gov/releases/h41/<YYYYMMDD>/h41.htm`, Thursday releases, browser UA required. ⚠️ **FRED's custody family (`WMTSECL`, `WMTSEC`, `H0RESH4C*`) was DISCONTINUED 2012-11-07** — a fact about FRED, not about the data; go to the release. Grade the **Wednesday level and the weekly average together** (they can disagree in sign), and **always attach the preceding fortnight** — a decline read alone inverted the conclusion on 2026-08-15 (`KB-BND-109`).
   - Issuance from SIFMA / high-quality market news.
   - Auction internals from **TreasuryDirect TA_WS primaries, never wires** — wires misdate this series (caught at BND-08). Compute % of **competitive accepted**.
   - CDX: true index levels are paywalled (S&P/Markit) *(canonical statement + `re-test: 2026-12-01` → `monitors/CDX_CASH_BASIS.md`)*. Use `monitors/cdx_proxy.py` (HYG/IEF, LQD/IEF) and **sign-check both legs** before ever calling a divergence.
7. Update `STATUS.md` if state changed.
8. Update `TRADE.md` if state affects supported trades.
9. Update workbook files when evidence/predictions/vectors/flows change.
10. Write outbound signal files only for threshold breaches or cross-agent implications.

## Inbox Processing

For each file in `inbox/`:

| Step | Action |
|---|---|
| 1 | Read full signal. Identify sender, target, priority, claim, source. |
| 2 | Classify: `INTEGRATE`, `LOG_ONLY`, `DISCARD`, or `ROUTE_OUT`. |
| 3 | If factual and relevant, add one KB row with source and confidence. |
| 4 | If it changes a vector, update `VX.tsv` and `STATUS.md`. |
| 5 | If it changes transmission mechanics, update `FLOW.tsv`. |
| 6 | If it creates a cross-domain implication, write `outbox/YYYY-MM-DD_to-[target]_[slug].md`. |
| 7 | Move processed signal to `inbox/processed/`. |

## ★ DELIVERY MODEL — DECLARED 2026-08-27 (was undeclared, and it failed twice)

🔴 **STANDING MODEL, effective now: COPY-TO-RECIPIENT-INBOX. Writing a packet to `outbox/` is NOT sending it.**

**For every outbound packet: write it to `outbox/` AND commit a copy to `AGENTS/<RECIPIENT>/inbox/`**, explicitly path-scoped, with the recipient named in the subject — root `CLAUDE.md` **carve-out ①** exists precisely to permit this and makes it mandatory for self-authored packets.

⚠️ **Why this is declared rather than assumed.** BOND ran an undeclared **outbox-only** model. **The fleet's assumption is inbox-first**, so the two are incompatible in the one direction that fails silently: the packet exists, is committed, is findable — and the recipient has no signal it exists. **Measured failures: (a)** the 2026-08-23 MIDAS packet carried a **Will-ruled correction to MIDAS's own published headline** and `AGENTS/MIDAS/inbox/` held **zero**; MIDAS found it only by searching the tree, and was one step from encoding the correction **without ever reading its evidence**. **(b)** a 2026-06-05 VIOLET ask sat undelivered **76 days** while a local checkbox waited on it. **Both flagged independently by PROME and MIDAS on 2026-08-23.**

⚠️ **An outbox-first convention is legitimate — an UNDECLARED one is not.** PROME's ask was *"not asking you to change it — asking you to declare it."* **Declared here, and changed, because the failure mode is silent on the recipient's side and BOND cannot see it.**
⚠️ **PROME IS THE EXCEPTION AND IT BIT ON THE FIRST USE OF THIS RULE, THE SAME SESSION IT WAS WRITTEN.** PROME's inbox is **`PROME/inbox/` at the REPO ROOT**, *not* `AGENTS/PROME/inbox/`. Copying to `AGENTS/<RECIPIENT>/inbox/` by loop put a packet in the wrong tree **and re-created the `AGENTS/PROME/` directory that was removed 2026-07-24 and which silently regrows** (`[[finding_prome_inbox_is_repo_root_not_under_agents]]`). **Caught by memory, not by the rule — and note the failure mode: delivery APPEARED to work, because a copy existed at a plausible path.** Relocated to `PROME/inbox/` and the stray tree trashed. **Everyone else: `AGENTS/<NAME>/inbox/`.**

**`outbox/delivered/` remains the confirmation record — move a packet there only after verifying the CONTENT reached the recipient, by grepping the owner's own files, never by filename.**

## Outbox Format

```markdown
## YYYY-MM-DD — To: [TARGET_AGENT]
**Signal:** [one-line headline]
**Detail:** [2-3 sentences: what changed, why it matters]
**Source:** [data/report + date]
**Priority:** 🔴/🟠/🟡
```

## Thresholds for outbound signals

| Trigger | Target | Priority |
|---|---|---|
| Treasury auction **composition failure**: **indirect below the auctioned tenor's OWN trailing-12 MIN _and_ dealer above its OWN trailing-12 MAX** (of competitive accepted) — ⚠️ **re-specified 2026-08-18; this row hardcoded the 7Y's `<56.4% / >13.2%` as if general.** Current per-tenor MIN/MAX: **2Y 50.91/49.09** · 3Y 53.99/19.50 · **5Y 59.24/15.61** · 7Y 56.42/13.14 · 10Y 63.95/16.16 · 20Y 55.17/17.59 · 30Y 59.52/17.46 ⚠️ **The 2Y and 5Y rows were MISSING from this table until 2026-08-27 — i.e. this outbound-trigger table could not fire for either tenor, and both printed on 8/25–8/26.** Found by the first audit of this file in three sessions; derived at the primary that morning. **The 2Y dealer MAX of 49.09 is genuinely that wide — the 2Y dealer distribution is far more dispersed than the long end, which is exactly why reusing another tenor's cut-offs is forbidden.** (`KB-BND-120`, re-derive each grade — these drift) | LIQUID, ZHAO | 🔴 |
| Treasury auction BTC <2.3 **alone** (cover marker, composition intact) | LIQUID, ZHAO | 🟠 — *note explicitly that the mechanism did NOT fail* |
| ★ **`I'` — indirect below the tenor's own trailing-12 15th percentile, SUFFICIENT ALONE** *(MATRIX_V2 §3c, Will-ruled 8/20, adopted 2026-08-27)*. Current bars: **2Y 55.75 · 5Y 59.48 · 7Y 57.24** (% of competitive accepted) — **re-derive per tenor at every grade; snapshot rail in `monitors/AUCTION_HEALTH.md`** | LIQUID, ZHAO | 🟠 |
| ~~Dealer take-down spikes~~ **DROPPED as a bearish trigger 2026-08-27** *(MATRIX_V2 §1, Will-ruled)* — dealer take is now **descriptive only**; **>18% is a contrarian-BULLISH note**, never an escalation. ⛔ **The thesis kill's dealer leg is UNTOUCHED and remains in force — that is a separate spec and the scope question is with Will** | — | ❌ |
| ~~tail >2bps~~ | — | ❌ **RETIRED 2026-07-28 — UNSCOREABLE** |
| Dealer take-down spikes / indirect demand weakens materially | LIQUID, ZHAO | 🟠 |
| HY OAS >350 or HY issuance freezes | HENRY, REGINALD, LIQUID | 🔴 |
| IG issuance freezes or blue-chip deal pulls | REGINALD, LIQUID | 🔴 |
| CDX widens ahead of cash for 2+ weeks | HENRY, LIQUID | 🟠 |
| Credit-equity lead activates while VIX remains complacent | HENRY, VIOLET, PROME | 🟠 |
| Bank funding backstop implied by issuance freeze | REGINALD | 🔴 |
| Public credit contradicts private-credit stress | BROCK, PROME | 🟠 |

> ⚠️ **Thresholds reviewed 2026-07-28.** Two changes, both load-bearing. *(Formatting note: this block was briefly inserted **mid-table** earlier the same day, splitting the trigger list in two so the last seven rows were orphaned from their header. Moved below the complete table — a review pass that breaks the thing it is reviewing is worse than the staleness it fixed.)*
>
> **1. The `tail >2bps` trigger is RETIRED as unscoreable.** A tail requires the when-issued yield at the bid deadline and **TreasuryDirect does not publish it** — so a tail-keyed trigger cannot be graded from primaries *by construction*, not merely "this session." This retires the pending `MATRIX_V2_DRAFT` per-tenor tail percentiles too: the problem is the *measurement*, not the calibration. Wire-reported tails are `[med-conf]` and may be recorded in notes but must **never** fire a trigger. *(This exact defect produced a mis-specified falsifier that passed by construction — see THESIS v1.1.3.)*
>
> **2. Grade COMPOSITION, not the headline cover.** A demand hole requires **indirect falling AND dealers absorbing**; a thin cover with intact composition is a *price* concession. Worked example: the 7/27 5Y printed the lowest BTC since Sept-2022 while indirect **rose** with duration and dealers were not stuffed — a marker worth firing 🟠 on, but categorically not a demand hole. Composition thresholds are % of **competitive accepted** (the fleet-reconciled denominator), benchmarked to trailing-12 **per tenor** — re-derive them per tenor rather than reusing the 7Y cut-offs.
>
> Also unchanged and still true: per GAO the note/bond BTC norm has drifted ~3.0→2.5, so **2.3 sits just under the new structural floor** — read 2.3–2.4 as "below new-normal," not "fine."

## Receipt

After inbox work, overwrite `RECEIPT.md`:

```markdown
# BOND Receipt — YYYY-MM-DD

| File | Action | Why | Workbook rows | STATUS change | Outbox |
|---|---|---|---|---|---|
```
