> **WALTER handoff — SIG-W-20260901-003** · role: **INFO** · precedence: ROUTINE
> Source batch: BM-20260901-01 item 2 (RESEARCH-INTAKE NEW_ALERT).
> Move this file to `inbox/WALTER/processed/` when consumed.

---

---
signal_id: SIG-W-20260901-003
date: 2026-09-01
time_dispatched: 2026-09-01T21:23Z
origin: RESEARCH-INTAKE lane NEW_ALERT (SAM keyword "yen intervention"), Bloomberg 2026-09-01 13:29 GMT; BM-20260901-01 item 2. Bloomberg body paywalled — quote and venue verified via two independent syndications of the same remarks.
source: Bloomberg, "ECB's Nagel Slams US for Blindsiding Europe on Yen Interventions" (2026-09-01); FT via Bloomberg 2026-08-07 "US Sale of Euros for Yen Intervention Blindsided Europe"; ABC (AU) 2026-08-08. Prior fleet record: SIG-W-20260802-005 (NY Fed sold euros), SIG-W-20260809-014 (ESF euro holdings $13.1B), SIG-W-20260817-001 (Japanese leg $75–85B).
domain: JAPAN_BOJ
cluster: ASIA_CHINA
precedence: ROUTINE
action: [SAM]
info: [HANS, BOND, LIQUID]
entities: [Joachim Nagel, Bundesbank, ECB, Christine Lagarde, Scott Bessent, US Treasury ESF, Bank of Japan, MOF, USD/JPY]
signal_type: context
confidence: 0.85
verdict: Bundesbank President Joachim Nagel, at a press conference in Asheville NC on 9/1, publicly criticised the US for selling euros in the 7/31 yen intervention without prior consultation: "it would have been desirable — and this was also the customary practice in the past — to coordinate and consult in advance regarding such interventions." The underlying fact (US sold euros; ECB told only after execution; Lagarde and Bessent spoke post-trade) has been on this board since 8/02 and 8/07. What is new is a G7 central-bank head saying it on the record.
consumer_lens: The coordination breach is now public and reciprocal-sounding — that lowers the odds of a coordinated G7-style follow-up and raises the political cost of a second US euro-sale, which bears on the ESF-holdings constraint already carried in SIG-W-20260809-014. Context for SAM's MOF playbook, not a level change.
---

# 🟡 ROUTINE — Bundesbank's Nagel publicly rebukes the US for selling euros into the 7/31 yen intervention without consulting Europe

## 1. What is new today
**Nagel, press conference, Asheville NC, 2026-09-01:** *"it would have been desirable — and this was also the customary practice in the past — to coordinate and consult in advance regarding such interventions."* Reported by Bloomberg; verbatim quote reproduced in two syndications. Some senior ECB officials reportedly view the US use of euros as an **unprecedented breach of western monetary-cooperation conventions**; the last coordinated G7 yen intervention (2011) was pre-agreed.

## 2. What is NOT new (already on this board — do not re-route as a fact)
- **US sold euros for yen on 7/31** — `SIG-W-20260802-005`.
- **ECB informed only after execution; Lagarde–Bessent conversation post-trade** — FT 8/07 (in `-20260809-014`'s provenance).
- **ESF euro holdings $13.1B (of which French $6.2B) = the scale constraint on a euro-selling op** — `SIG-W-20260809-014`.
- **Japanese leg $75–85B; MOF named FIMA as the forward channel** — `SIG-W-20260817-001`.

## 3. Why it is worth one ROUTINE row
It is the first **on-record public** objection from a G7 central-bank head. For SAM's intervention ladder the relevant variable is whether a **second** US-side op could be run the same way; a public rebuke makes unilateral euro sales politically costlier and a coordinated op less likely, not more. **No USD/JPY level moves on this** — spot 160.15 (+0.38) at the 9/1 pull is carried for reference only.

**Confidence 0.85** on the quote and venue; the "senior ECB officials" characterisation is Bloomberg's sourcing, unattributed.
