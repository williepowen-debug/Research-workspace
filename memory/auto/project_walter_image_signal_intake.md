---
name: WALTER is image-capable signal intake
description: WALTER + Prome only on Telegram; WALTER owns image/screenshot intake since Prome's Kimi LLM can't reliably analyze images
type: project
originSessionId: 327199d4-0ef3-4f28-807c-c3da3fba67ae
---
As of 2026-04-14, WALTER's primary job shifted to routing signals Will drops via Telegram — including images and screenshots. WALTER and Prome are the only agents on Telegram for now; Will can't reliably run 2-3 Telegram agents simultaneously.

**Why:** Prome's Kimi LLM can't reliably read/analyze images; WALTER (Claude) handles images natively. This makes WALTER the single point of ingestion for any visual signal (Twitter screenshots, charts, headlines, etc.).

**How to apply:**
- Expect Telegram drops in batches — Will sends several, WALTER processes and replies once with a batch summary (ID → domain → precedence → recipient → kill reason).
- Default summary cadence: one line per routing decision back to Will.
- COP refresh is deprioritized until Will provides more direction.
- Workflow: filter (3-gate) → classify (ROUTING_TABLE) → archive (signals/ with canonical copy) → push to recipient inbox per interim dual-delivery → reply to Will.
