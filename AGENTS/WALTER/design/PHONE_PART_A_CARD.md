# PHONE PART A — Will's 15 minutes, copy-paste ready

**Status:** the **entire fleet side is built and PROVEN** (Part B shipped 7/27, re-verified end-to-end 8/3). **This card is the only thing left.**
**Why it's yours and not mine:** A1 needs your github.com account settings; A2 needs your phone. I have access to neither. Everything I *could* do is done.

> **What this buys:** a durable signal path from your phone that **cannot be dropped the way a Telegram message can.** One tap → a file lands in the private RESEARCH-INTAKE repo → WALTER sweeps it at every boot. GitHub holds it; nothing is in the loop that can lose it.

---

## A1 · Create the token — github.com, ~2 min

**Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**

| Field | Value |
|---|---|
| **Name** | `phone-signal-ingest` |
| **Expiration** | **90 days** |
| **Resource owner** | `williepowen-debug` |
| **Repository access** | **Only select repositories → `RESEARCH-INTAKE`** |
| **Permissions → Contents** | **Read and write** |
| Everything else | **No access** (Metadata auto-grants read-only — fine) |

**Generate → copy the token.** You paste it once, into the Shortcut in A2.

> **Blast radius, so you can judge it:** this token can write to **one private data repo** and nothing else — no code, no main repo. Everything in RESEARCH-INTAKE is regenerable (the collectors re-run). Lost phone → one-click revoke on GitHub. 90-day expiry forces rotation.
> **Do not paste the token into Telegram or anywhere in this repo.** It goes straight into the Shortcut.

---

## A2 · Build the iOS Shortcut — ~15 min

New Shortcut → add these 6 actions in order.

**1. Ask for Input** — Prompt: `Signal` · Input Type: **Text**

**2. Choose from Menu** *(optional but recommended)* — three items, exactly:
```
🔴
🟠
🟡
```

**3. Format Date** — Date: **Current Date** · Format: **Custom** · Format String:
```
yyyy-MM-dd'T'HHmmss
```

**4. Text** — this is the **format contract**. WALTER's parser reads exactly this:
```
---
source: phone
priority: ‹Menu Result›
ts: ‹Formatted Date›
---
‹Provided Input›
```
*(`‹…›` = drag in the variable from the earlier action. If you skip the menu in step 2, just type `🟡` on the priority line — WALTER defaults to 🟡 anyway.)*

**5. Base64 Encode** — input: the **Text** from step 4. *(The GitHub API requires base64.)*

**6. Get Contents of URL**

| Setting | Value |
|---|---|
| **URL** | `https://api.github.com/repos/williepowen-debug/RESEARCH-INTAKE/contents/phone_inbox/signal_‹Formatted Date›.md` |
| **Method** | `PUT` |
| **Header 1** | `Authorization` = `Bearer ‹your token from A1›` |
| **Header 2** | `Accept` = `application/vnd.github+json` |
| **Request Body** | **JSON**, two fields: |
| ↳ `message` | `phone signal ‹Formatted Date›` |
| ↳ `content` | `‹Base64 Encoded›` |

**Then:** name it, add to Home Screen, and/or enable "Hey Siri, ‹name›".

---

## A3 · Test — 1 min

Fire one signal: **`test — ignore`**

**Then tell me, and I'll confirm it landed and route it end-to-end.** What I'll check: the file exists at `phone_inbox/signal_<ts>.md`, the frontmatter parses, the priority carries, and `phone_scan.py` surfaces it as NEW.

**If it fails,** the two usual causes are: a **404** (repo path or token scope wrong — re-check A1's *Only select repositories*), or a **422** (the `content` field isn't base64 — check step 5 feeds step 6).

---

## What is already true on my side — so your 15 min is the only remaining risk

Verified end-to-end **2026-08-03** against the §5 contract, using fixtures (nothing was written to RESEARCH-INTAKE):

| Behaviour | Verified |
|---|---|
| Parses `source` / `priority` / `ts` and surfaces the body for routing | ✅ |
| Dedups — a consumed signal does not re-fire | ✅ |
| **An EDITED signal correctly RE-FIRES** (dedup keys on filename + content hash) | ✅ |
| **A malformed signal is surfaced LOUDLY and still handed over — never silently dropped** | ✅ |
| `phone_inbox/` not existing reports cleanly and self-arms for the first signal | ✅ |
| Test mode isolates the live registry *(defect found and fixed 8/3 — it previously did not)* | ✅ |

**Boot wiring:** step **7e(f)** runs the sweep every boot. Signals are routed through the normal path (filter → BOARD → handoff → delivery_log), tagged `source: phone`, carrying your priority hint — and **they are treated as Will-originated, so they are never killed on Novelty without reading the body.**

**Deliberate design note:** consumed signals are recorded on *my* side (`registry/phone_seen.json`), never moved into `phone_inbox/processed/`. That would need write access to RESEARCH-INTAKE, which my boot protocol forbids. **The lane stays append-only from your phone and read-only to me.**

---

**Canonical spec:** [`PHONE_SIGNAL_INGESTION.md`](PHONE_SIGNAL_INGESTION.md) · **Sweep:** `tools/phone_scan.py` · **Boot step:** 7e(f)
