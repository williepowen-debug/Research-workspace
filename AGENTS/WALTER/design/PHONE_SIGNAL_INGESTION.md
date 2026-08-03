# PHONE→FLEET SIGNAL INGESTION — canonical spec

**Version:** v1.2 · **Status:** **PART B SHIPPED 2026-07-27; RE-VERIFIED END-TO-END 2026-08-03** (`tools/phone_scan.py`, wired at boot step **7e(f)**). **PART A (Will's PAT + iOS Shortcut) still to enact — it is the remaining critical path, and it is the ONLY remaining item.** → **copy-paste card: [`PHONE_PART_A_CARD.md`](PHONE_PART_A_CARD.md)** (Will-requested 8/3; literal values pre-filled, failure modes named).

**v1.2 (2026-08-03) — receiving half RE-PROVEN + a test-isolation defect FIXED.** Re-verified against the §5 contract with fixtures (nothing written to RESEARCH-INTAKE): parses source/priority/ts · dedups · **an EDITED signal correctly RE-FIRES** · **a malformed signal is surfaced LOUDLY and still handed over.** 🔴 **DEFECT FOUND AND FIXED: `_TEST_MODE` drove only the banner, so `WALTER_PHONE_DIR=… --mark` — the obvious way to test — wrote FIXTURE hashes into the LIVE `registry/phone_seen.json`, silently.** Unacceptable in the one registry whose entire purpose is *never silently drop a signal Will sent from his phone*; **a harness that mutates the production state it is testing is not a harness.** TEST MODE now isolates the seen-file (an explicit `WALTER_PHONE_SEEN` still wins) and prints which file is in play.
**Promoted from `inbox/` → `design/` on 2026-07-27** per PROME's instruction in the original packet ("once you've built Part B, promote this doc into `AGENTS/WALTER/design/` as the canonical spec"). Original packet text preserved verbatim below.

---

## ⚠️ v1.1 CHANGE LOG — one deliberate deviation from §4 (Will-approved 2026-07-27)

**§4 said:** archive consumed signals to `phone_inbox/processed/`.
**SHIPPED INSTEAD:** consumed signals are recorded in **`registry/phone_seen.json` on WALTER's side**; nothing is ever written to RESEARCH-INTAKE.

**Why:** moving files into `phone_inbox/processed/` requires **write access to RESEARCH-INTAKE**, which **boot step 7e(a) forbids** — that repo is read-only to WALTER (`pull --ff-only`, never push) — and it would have required a **second PAT** on top of Will's phone token. The seen-file approach mirrors the existing `intake_seen.json` model **this same doc points at in §4's last bullet**, so the two halves of §4 were in tension; this resolves it in the direction that adds no permissions and less code. **The lane stays append-only from the phone and read-only to WALTER.**

**Also fixed in implementation, beyond the spec:**
- **Dedup key = filename + content SHA**, not filename alone. The Shortcut derives the filename from a timestamp, so two signals inside the same second would collide — and an **edited** signal correctly re-fires instead of being swallowed.
- **Nothing is ever silently dropped.** Malformed frontmatter · unknown/missing priority · empty body · invalid UTF-8 · oversize · stray non-`signal_*.md` files are all **surfaced loudly and still handed to the operator.** A durability mechanism that quietly discards the thing it exists to guarantee would be worse than no mechanism. *(This is the inverse of the normal filter posture and is deliberate.)*
- **A corrupt `phone_seen.json` fails LOUD** rather than silently re-firing everything or swallowing everything; the error names deletion as the safe direction (deleting re-surfaces all signals).
- **`phone_inbox/` not existing is reported as a clean status, not an error** — it is the expected state until Part A is enacted, and the sweep self-arms for the first signal.

**Tested before shipping** against fixtures for all of the above (happy path · no priority · no frontmatter · empty body · wrong `source:` + bad priority · invalid UTF-8 · stray file · same-second collision · re-fire after edit · corrupt seen-file), plus a dedup round-trip. **Nothing was written to RESEARCH-INTAKE at any point** — the test harness reads a scratch dir via `WALTER_PHONE_DIR`.

---

# 2026-07-05 — To: WALTER (build owner) + Will (operator) — Phone→Fleet Signal Ingestion: design & enactment plan

**From:** PROME · **Priority:** 🟡 (build when convenient; Will's half is enactable next session with zero fleet-side dependency) · **Will-approved** 7/5.
**WALTER:** this is your architecture — once you've built Part B, promote this doc into `AGENTS/WALTER/design/` as the canonical spec and fold it into the messaging overhaul (`[[project_messaging_overhaul]]`), not a one-off inbox hack.
**Refs:** memory `[[project_phone_signal_architecture]]` (refreshed 7/5) · `[[project_research_intake_collection_lane]]` (the transport this rides).

---

## 1. Goal
Will wants **reliable signal ingestion from his phone** — the Telegram MCP drops messages. This is the refreshed, **no-always-on-server** design (the original 2026-04-14 plan relied on a Prome-on-OpenClaw poller; OpenClaw was cut 6/26).

## 2. Architecture — three decisions
```
  Will's phone  ──►  GitHub Contents API  ──►  file in the PRIVATE          ──►  WALTER sweeps it,
  (iOS Shortcut)     (one PUT, no server)      RESEARCH-INTAKE repo               routes to the domain
                                               phone_inbox/signal_<ts>.md         agent (next run)
```
1. **Lands in the private `williepowen-debug/RESEARCH-INTAKE` repo — NOT the main repo.** The main repo may go public (Will's raw trade signals must not be), and RESEARCH-INTAKE is already the fleet's ingestion surface WALTER consumes. Phone = just another intake feed.
2. **Written as a file via GitHub's Contents API.** One authenticated `PUT` per signal creates `phone_inbox/signal_<timestamp>.md`. No server in the loop — GitHub holds it durably (can't be dropped like a Telegram message).
3. **Pickup rides the existing intake→WALTER consumer path.** WALTER already scans RESEARCH-INTAKE; we add one small `phone_inbox/` sweep step.

**Trade:** durable, not instant. Latency = the intake lane's cron cadence (a near-instant variant is in §6 if that's too slow).

---

## 3. PART A — Will's setup *(enact next session; ~15–20 min, no code)*

### A1 · Create the token *(github.com, ~2 min)*
1. github.com → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**
2. Name: `phone-signal-ingest`; Expiration: **90 days**
3. **Resource owner:** `williepowen-debug`
4. **Repository access → Only select repositories → `RESEARCH-INTAKE`**
5. **Permissions → Repository permissions → Contents → Read and write** (leave everything else "No access"; Metadata auto-grants read-only — fine)
6. Generate → **copy the token** (you'll paste it into the Shortcut once).

### A2 · Build the iOS Shortcut *(~15 min)*
New Shortcut, chain these actions:
1. **Ask for Input** — Prompt "Signal", Input Type: *Text* → this is your signal.
2. *(optional)* **Choose from Menu** — items `🔴` / `🟠` / `🟡` for priority.
3. **Format Date** — Date: *Current Date*, custom format `yyyy-MM-dd'T'HHmmss` → reused for filename + body.
4. **Text** — build the file body (this is the **format contract**, see §5):
   ```
   ---
   source: phone
   priority: ‹menu result, or 🟡›
   ts: ‹Formatted Date›
   ---
   ‹Provided Input›
   ```
5. **Base64 Encode** — encode the Text from step 4 (the Contents API requires base64 content).
6. **Get Contents of URL:**
   - **URL:** `https://api.github.com/repos/williepowen-debug/RESEARCH-INTAKE/contents/phone_inbox/signal_‹Formatted Date›.md`
   - **Method:** `PUT`
   - **Headers:** `Authorization` = `Bearer ‹your token›` · `Accept` = `application/vnd.github+json`
   - **Request Body:** *JSON* → two fields: `message` = `"phone signal ‹Formatted Date›"`, `content` = *‹Base64 Encoded›*
7. Name it, add to Home Screen / enable "Hey Siri, ‹name›".

### A3 · Test *(1 min)*
Fire one test signal ("test — ignore"). Then ping me (or check GitHub) — I'll confirm `phone_inbox/signal_*.md` landed in RESEARCH-INTAKE with the right content. **The phone leg is done the moment this works** — even before Part B exists, signals sit safely in `phone_inbox/` until WALTER's sweep goes live.

---

## 4. PART B — WALTER's build *(the one fleet-side piece)*
Add a `phone_inbox/` sweep to your RESEARCH-INTAKE consumer (`tools/intake_scan.py` or equivalent):
- On each run: read new `phone_inbox/signal_*.md`, parse the frontmatter (§5), treat the body as a **Will-originated signal** → run your normal significance-judgment + routing to the correct domain agent(s), carrying the `priority` hint.
- Archive processed files to `phone_inbox/processed/` (create it + `phone_inbox/` via `.gitkeep` if the first signal hasn't yet).
- Reuse your existing signal-processing; do **not** build a parallel path. Fold into the messaging overhaul.
- **Onset-dedup:** the same file won't re-fire (move-to-processed handles it), consistent with your `intake_seen.json` model.

## 5. The format contract *(the interface between Will's Shortcut and WALTER's parser)*
Every phone signal is a markdown file with this frontmatter + body — Part A's Shortcut writes it, Part B's parser reads it. Keep them in sync:
```
---
source: phone
priority: 🔴|🟠|🟡      # default 🟡 if the menu is skipped
ts: 2026-07-05T143022
---
‹freeform signal text from Will›
```

## 6. Security
- **Phone token blast radius:** Contents:write on the **collected-data repo only** — no code, no main repo, no other repos; all of RESEARCH-INTAKE is regenerable (collectors re-run). One-click **revoke** on GitHub if the phone is lost; **90-day expiry** forces rotation.
- **Why the private repo, not the main one / not Issues-in-a-public-repo:** the main repo may go public → signals would leak. RESEARCH-INTAKE stays private by design.

## 7. Phasing
- **v1 (this doc):** Contents-API file → cron/boot sweep. Durable; latency = the lane's cadence. **Recommended start.**
- **v2 (optional, only if latency bites):** Shortcut opens a GitHub **Issue** in RESEARCH-INTAKE instead (token scope shrinks to **Issues:write only** — can't touch any code), and a GitHub **Action** fires `on: issues[opened]`, writes the inbox file, closes the issue → pickup drops from "next cron" to ~30s. Costs one small Action. Defer unless Will fires time-sensitive signals.

## 8. Enactment plan / sequence
| # | Step | Owner | Done when |
|---|---|---|---|
| 1 | Create PAT + build Shortcut + send a test signal (§A) | **Will** (next session) | test file lands in `phone_inbox/` (PROME verifies) |
| 2 | Build the `phone_inbox/` sweep + route the test signal end-to-end (§4) | **WALTER** | test signal routes to a domain agent cleanly |
| 3 | Decide cadence; add v2 only if daily latency is too slow (§7) | Will + WALTER | — |

**Critical path is Step 1 (Will) — it has no dependency on the fleet side.** Step 2 can follow whenever WALTER next runs. PROME coordinates + verifies the hand-off; doesn't build WALTER's side.
