# PROME STATUS.md
**Updated:** 2026-05-09 21:35 ET

## Weekend Build Mode — Markets Closed

**Core state:** Private-credit thesis intact, timing slower. OBDC Q1 was mixed / earnings-quality bear, not forced-mark cascade. Current portfolio risk is larger in **regional-bank puts** than in APO/ARES/OWL residuals.

---

## Active Decision Layer

| Artifact | Status | Purpose |
|---|---|---|
| `PROME/DECISION_FLOW.md` | ✅ Fresh | Five-layer workflow: pre-build → position snapshot → action card → live read → decision log |
| `PROME/action-cards/TEMPLATE.md` | ✅ New | Standard action-card format |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | ✅ Active | FSK Q1 branch-to-action rails |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | ✅ Active | Bank expiry / Call Report triage rails |
| `PROME/TRADE_DECISIONS.md` | ✅ Ready | Decision log scaffold; no trade decisions logged yet |
| `PROME/POSITIONS.md` | ✅ Fresh May 8 | Current portfolio snapshot from screenshots |

---

## Pending Work

| Action | Pri | Status |
|---|---:|---|
| **FSK Q1 live read May 11** | 🔴 | Pre-build + action card complete. Need Monday classification and decision prompt if Bear/Strong Bear. |
| **Regional-bank Call Report triage** | 🔴 | Action card created. Filing radar expanded May 9; ZION/VLY/RF/EGBN/FITB/CFG/WAL filings detected. Next: extract MI3, NDFI, ACL, charge-offs, FHLB/brokered deposits. |
| **Monday bank decision prompt** | 🔴 | Pending Call Report/tape prep. Needs May cleanup + June roll/salvage + runway hold plan. |
| **ZION scaffold expansion** | 🟠 | Corrected framing: ZION is under-researched, not exonerated. Jul put = kill/no-roll if usable bid, but REGINALD should fill scaffold starting with Call Report MI3/RCON2746. Inbox note: `AGENTS/REGINALD/inbox/PROME-20260509-zion-scaffold-fill-request.md`. |
| **GCRED / OTF / BCRED / CTAC 10-Q watch** | 🟠 | Private-credit forced-mark tests after OBDC/FSK. |
| **EDGAR filing-watch routing** | 🟠 | MVP/baseline done; REGINALD watchlist expanded for SSB/EGBN/HBAN/CFG/VLY; routing dry-run still incomplete. |
| **Refresh HEARTBEAT after weekend build** | 🟠 | Needs pointers to new bank card/template once build settles. |
| **Resolve git sync blocker** | 🟡 | `git pull --rebase` blocked by unstaged/untracked local changes. Do not commit/stash without Will approval. |
| **Old Toscanini QUEUE/WILL_QUEUE cleanup** | 🟡 | Stale; lower priority than live decision rails. |

---

## Agent / Domain Notes

| Domain | Status | Note |
|---|---|---|
| BROCK / private credit | 🔴 | FSK May 11 is next BDC canary. Existing PC exposure small; fresh capital only on Bear/Strong Bear. |
| REGINALD / banks | 🔴 | Persistent/managed — do not spawn. Current book needs Call Report and expiry triage. |
| LIQUID | 🟠 | HY OAS benign is main falsification pressure; watch <260 sustained. |
| NEXUS | 🟠 | Spawn later only if FSK + Call Reports create cross-domain convergence. |
| PROME | 🔴 | Weekend build: action-card layer + stale doc refresh + Monday prompts. |

---

## Current Rules of Engagement

- **No trade execution without Will approval.**
- **No fresh private-credit premium** unless FSK is Bear / Strong Bear.
- **No broad bank-premium add** unless Call Reports/tape move to Bear / Strong Bear.
- **No rolling every losing June contract.** Prefer one or two higher-delta roll candidates if confirmed.
- **No panic-selling Sep/Dec runway** into green tape.
- **May contracts are cleanup**, not thesis core.
- **Do not spawn REGINALD, CARL, SAM, RED, or BRENT.**

---

## Freshness Table

| File | Status |
|---|---|
| `HEARTBEAT.md` | Patched May 9 evening with ZION/REGINALD scaffold note; market levels still May 8 |
| `PROME/TODAY.md` | ✅ Refreshed May 9 evening |
| `PROME/STATUS.md` | ✅ Refreshed May 9 evening |
| `PROME/SCRATCH.md` | ✅ Refreshed May 9 21:35 ET |
| `PROME/TOSCANINI/QUEUE.md` | Stale Mar 26; do not use as live proposal list |
| `PROME/TOSCANINI/WILL_QUEUE.md` | Stale; historical only until refreshed |

---

## Next Best Action

First check REGINALD ownership of the ZION scaffold request, then run / build the **Q1 Call Report triage** for WAL, OZK, EGBN, CFG, VLY, ZION, FITB, SSB and produce Monday’s bank decision prompt.
