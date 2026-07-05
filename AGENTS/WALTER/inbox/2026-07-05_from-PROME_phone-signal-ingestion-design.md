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
