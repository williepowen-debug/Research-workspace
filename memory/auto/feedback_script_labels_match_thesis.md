---
name: Script Alert Labels Must Match Thesis Vocabulary
description: When building monitoring automation for agents with thesis documents, alert severity labels (CRISIS/STRESS/etc.) must cross-reference the thesis scenario buckets — not be invented independently
type: feedback
originSessionId: 5c27c74c-8710-4020-9d3f-39db1cc57182
---
When defining alert thresholds in automation scripts for agents that have scenario-weighted thesis documents (SAM, HENRY, LIQUID, etc.), the script's severity labels must match the thesis's canonical scenario definitions. Don't invent new thresholds and reuse thesis vocabulary — that causes miscommunication and over-reaction on first run.

**Why:** On 2026-04-11 I built SAM's `mof_flows.py` with arbitrary thresholds (¥1T/¥2T/¥4T per 4 weeks) and labeled the top one "CRISIS PACE." First run surfaced a ¥5T/4-week reading and my script fired "🔴 CRISIS PACE" which I then reported to Will as a thesis-critical finding. Will asked "how dramatic would Option C (scenario rebalance) be?" — a sharp question. Forced to quantify, I re-read SAM's THESIS.md scenario buckets: Base $7-10B/mo, Stress $25-40B/mo, Crisis $100-165B/mo. The ¥5T/4-week reading converts to ~$36B/month, which is squarely in STRESS case, not crisis case. My script's "CRISIS" threshold was at ~$29B/mo — literally below the THESIS stress-case upper bound. The label was 3.5× too lenient relative to canonical vocabulary. I had to retract the "crisis" framing to Will and clarify the actual reading was stress case. He approved the more conservative Option B (STATUS refresh only) instead of Option C (thesis rebalance) based on the corrected read. Fixed mof_flows.py to match THESIS midpoints: elevated ¥1.4T/4wk, stress ¥3.5T/4wk, crisis ¥14T/4wk.

**How to apply:**
- When building a new monitoring script for an agent that has scenario-weighted thesis: open the THESIS.md first, find the scenario bucket table (or equivalent), and calibrate your script thresholds to those same boundaries. Don't invent numbers from "what feels like a big move."
- If you need granularity beyond what THESIS defines, use distinct vocabulary (e.g., "Level 1/Level 2/Level 3", "Elevated/High/Extreme") that doesn't collide with the canonical scenario names.
- When your script fires an alert on first run and you're tempted to escalate immediately, pause and verify: does the alert label match what THESIS would say? If not, the script is wrong, not the thesis.
- The bigger principle: automation that reuses thesis vocabulary inherits thesis authority. Don't give your script authority it hasn't earned.
