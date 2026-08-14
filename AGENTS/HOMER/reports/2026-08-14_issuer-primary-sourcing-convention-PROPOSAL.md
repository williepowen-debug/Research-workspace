# PROPOSAL — **"Issuer is PRIMARY; an aggregator is a documented MIRROR"** as a fleet sourcing convention

**Status:** ⛔ **PROPOSAL — NOT LIVE FLEET-WIDE.** It is **live on HOMER's `workbook/RATES.tsv` only**, adopted 2026-08-13 as a HOMER sourcing decision (PROME concurred on the merits the same day). **Nothing outside `AGENTS/HOMER/` is changed by this document, and nothing should be until Will rules.**
**Author:** HOMER · **Date:** 2026-08-14 · **Route:** PROME → Will
**Scope of the ask:** a **labelling** rule. ⛔ **It moves no figure, no threshold, and no confidence anywhere in the fleet.**

---

## 1. The defect, stated precisely

`RATES.tsv` cited **"FRED MORTGAGE30US / DGS10 / DGS30, all PRIMARY."** That label was **false**, in a way that is easy to miss because the *numbers were right*:

- **`MORTGAGE30US` is a redistribution of Freddie Mac's own Primary Mortgage Market Survey.** **Freddie is the issuer**, publishes it first, and publishes **commentary FRED does not carry.**
- **`DGS10` / `DGS30` are redistributions of Treasury's daily yield curve.** **Treasury is the issuer.**

★ **Calling a mirror PRIMARY is the same defect class as the Trepp circular-citation loop CREED self-reported on 2026-07-27** — a citation that reads as source-tier assurance while actually pointing at a hop.

---

## 2. ★ The worked example — why this is not cosmetic

**2026-08-13, PMMS print.** FRED's `MORTGAGE30US` gives **a bare number: 6.67%.** Freddie's own release gives the same number **plus commentary stating that purchase and refi applications are RISING.**

**That commentary materially qualified a live HOMER read** — my carried *"no refi escape"* line — and **triggered a reconciliation that resolved with both claims intact** (the MBA series was simply 14 days stale; the level-basis claim survived, the direction-basis claim did not). **Pulling the mirror would have silently dropped the qualifier.**

⇒ **The cost of mirror-as-primary is not wrong numbers. It is CORRECT NUMBERS STRIPPED OF THE ISSUER'S OWN CAVEATS** — and per fleet memory `finding_rederived_signal_loses_the_senders_caveats`, caveats do not survive a hop. **This is that finding with a data vendor in the sender's seat.**

---

## 3. The proposed rule (three lines)

1. **The ISSUER of a series is its PRIMARY.** PMMS → `freddiemac.com/pmms`. Treasury yields → `treasury.gov` daily yield curve. GSE monthlies → the GSE's own investor page. And so on.
2. **An aggregator (FRED, Yahoo, a data vendor, a trade outlet) is a MIRROR and must be cited as one** — `"<series> via FRED (mirror of <issuer>)"`, never bare-`PRIMARY`.
3. **When a figure is load-bearing, read the ISSUER's release, not only the mirror's number** — because the qualifier lives in the release.

**⚠️ THIS IS A RELABEL, NOT A REPUDIATION OF FRED.** FRED stays fully usable and is the **right** tool for long history, for machine pulls, and for series with no convenient issuer feed. In the sanctioned path (`python3 FORGE/tools/market-data/fetch.py fred <SERIES>` from repo root) it is fast and reliable. **The rule governs the LABEL and the load-bearing read — not the tool.**

---

## 4. Honest limits — argued against myself

- **It costs a fetch.** Issuer pages are slower than an API and some are walled. **HOMER holds live counter-examples:** `singlefamily.fanniemae.com` is a genuine Cloudflare wall (403 to curl+UA *and* WebFetch) and `mba.org` 403s both clients — so **MBA apps run on two date-verified secondaries by necessity.** ⇒ **The rule must be "issuer is primary *where reachable*, and the mirror is labelled as a mirror when it is not"** — otherwise it manufactures false blockers. **This carve-out is load-bearing and should ship with the rule, not after it.**
- **It is a labelling rule, so it fixes labels, not judgment.** It would not have caught a wrong figure — only a wrongly-*credited* one.
- **`a_ruling_governs_the_next_write_not_the_existing_state`:** if adopted, existing bare-`PRIMARY` aggregator citations across the fleet do **not** self-correct. **Either pair it with a retroactive sweep, or ship it explicitly as next-write-only.** ⚠️ **I recommend next-write-only** — a fleet-wide sweep of every FRED/vendor citation is a large job with a low defect-severity, and the 8/13 example shows the cost is a lost caveat, not a wrong number.
- **n=1 on demonstrated harm.** One worked example (PMMS 8/13). The mechanism is general; the *measured* cost is a single instance. **Do not oversell it.**

---

## 5. What I am asking for

| # | Ask | Who |
|---|---|---|
| 1 | Rule on whether §3 becomes a fleet convention or stays HOMER-local | **Will** (via PROME) |
| 2 | If adopted: confirm **next-write-only** vs. retroactive sweep | **Will** |
| 3 | If adopted: confirm the **"where reachable"** carve-out ships *with* it | **Will** |

**⛔ Until ruled, this is HOMER-local and should be cited as such. Zero thresholds moved. Zero capital.**

— HOMER
