# PROME → TERRY: Paper-book is BUILD-READY — build on Will's go (Will-reviewed 7/19)

**Priority:** 🟡 backlog-but-ready — **do NOT build until Will says go.** The spec is finished; the trigger is Will.

## What changed
Will reviewed your `PAPER_BOOK_DESIGN.md` (7/19). It's now **BUILD-READY** — the 3 open questions are resolved and 6 sharpenings + a full **Phase-1 Shadow Book build spec** are folded into the doc. Read the doc; this packet is just the pointer + the headline decisions so you're not surprised.

## The decisions that shape the build (all in the doc)
- **Phase 1 = shadow book only.** No bankroll. Salaried desk (Phase 2) deferred behind a volume gate (build it only once the would-fire rate exceeds a salary tranche — prioritization can't bind at 2-3 cards/month).
- **Auto-fill on trigger, regardless of Will's approval** — this is THE design decision. It's the only version that generates a record (the whole problem is 0 approvals). Label it "card-quality record, not a P&L Will endorsed."
- **Every row carries `will_decision` (APPROVED/PASSED/NO-DECISION)** — the PASSED subset IS the counterfactual "ghost" that makes your refusals measurable (did saying no save or cost money). One table, a decision column.
- **Fill fidelity teeth:** ask-for-buys/bid-for-sells **at the trigger timestamp** (not close) + a slippage penalty for wide-spread names (bid/ask >15% of mid) + record `entry_basis` (auditable) + closed-market trigger fills at next-open. Never mid.
- **Scoring gate:** no Brier/calibration and no decision acts on the record until **N ≥ 10 closed per lane** (`notes = "N-too-small"` until then). Small N = directional only.
- **Marks are as-of-last-spawn**, staleness-stamped; equity curve is lumpy by design — label it, don't pretend continuous.
- **Seed row:** the 7/17 004 re-fire ZONE 2/3 (77P $495) is the natural first entry — reached would-fire, Will passed → `will_decision = PASSED`, seeds the refusal counterfactual immediately.

## Definition of done (Phase 1) — in the doc
`PAPER_BOOK.tsv` schema · fill rule + marking documented (CLAUDE.md/CLOSEOUT pointer) · boot-mark wired + staleness flag · seed row logged · guardrails in the ledger header. Tooling mostly exists (`chain_fetch.py`/`snapshot.py`/`csv_pnl.py`); the only new code is a tiny mark helper.

**Guardrails (unchanged, load-bearing):** subordinate to thesis work; never an argument for looser real deployment; everything labeled PAPER; shadow P&L is card-quality, not an endorsed return.

Routed by PROME, Will-directed in-session 7/19. When Will greenlights the build, deliver Phase 1 to definition-of-done + write back to PROME.
