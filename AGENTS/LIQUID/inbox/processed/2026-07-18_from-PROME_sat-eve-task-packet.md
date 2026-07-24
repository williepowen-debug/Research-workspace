# PROME → LIQUID: Sat 7/18 evening task packet (Will-approved wave)

**Date context:** Saturday 2026-07-18, ~5 PM ET. Markets CLOSED — weekend rule: stamp every figure [as-of]. HEARTBEAT re-based tonight (`913d3d11`) = current-state canon at Fri 7/17 close vintage. You closed clean Friday; this session clears your three owed items — all gradeable offline from already-released data.

## Tasks (priority order)
1. **★ KB-076 leg-(a) grade on the 7/14-data COT** (released Fri 7/17 3:30 PM ET — you explicitly refused to grade on stale 7/7 data; the fresh print is now out). SOFR-3M leveraged-fund net short vs the leg-(a) terms (new positioning record vs the −2.94M [6/30] peak, or >300K single-week cover). **Use the raw CFTC TFF file as primary** (Socrata lags releases — fleet precedent: BRENT's grader refused 40 stale API polls Friday and graded off the raw file). Grade mechanically vs the registered wording in `workbook/DEALER_POSITIONING_NEXUS_WATCH.md`; carry your own directional-vs-RV discriminator (swap spreads/SOFR-FF stable = directional) and WALTER's structural-why caveat alongside, not instead of, the mechanical verdict.
2. **Leg-(b) refresh:** NY-Fed PD G10 >10y IG net (as-of 7/8 data published — your standing recipe) vs the <−$12B line; note G5L10 two-week condition state. Then state the **2-of-3 conjunction verdict** explicitly (leg-c MOVE>85 w/ VIX<20 was NOT fired at 68/18.71 [7/17 close] — carry that stamp). **If 2-of-3 fires:** the pre-registered consequence is a joint PROME/NEXUS amplification write-up (NOT a position trigger) — route-out the ask in your memo; do not self-initiate the joint doc.
3. **★ NEXUS_BRIEF refresh — 11 days stale, worst brief-rot in the fleet.** Bring it current: X1 closed, KB-071 MISS, KB-081 lagging-tell pre-registered, GATE-LIQ-069 ARMED 1-of-2 (ORCL BBB−), GATE-LIQ-079 registered (+5bp acute), funding clean, reserves rebounded, tonight's KB-076 verdict. Synthesis agents consume this into the 7/25-28 BDC window — write it for them.
4. **Housekeeping (quick):** your GATE-LIQ-076 GATES.tsv row carries the 7/17 leg-refresh — if tonight's grades change any leg state, list the exact row edit as a route-out (PROME maintains GATES.tsv).

## Contracts
- **Deliver-before-idle:** (a) pathspec commits, own dir only (4 agents + PROME concurrent tonight; git ops from repo root; never `git add -A`), (b) `outbox/2026-07-18_to-PROME_*.md` — leg grades + conjunction verdict + brief-refresh confirmation, (c) SendMessage headline to PROME, (d) NEXUS_BRIEF is task 3, not optional.
- Weekend: no live pulls needed — everything above is released data; stamp observation dates. Web tools via ToolSearch if needed (not auto-loaded).
- Auto-push at closeout via `scripts/safe-push.sh`; non-ff abort → pull --rebase + re-push.
