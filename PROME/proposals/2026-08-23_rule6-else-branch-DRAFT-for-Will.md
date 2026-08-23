# DRAFT for Will — `MESSAGING/CROSS_SESSION_MESSAGING.md` rule 6, the missing `else`

**Status:** ⛔ **DRAFT. NOT APPLIED.** `MESSAGING/` is a shared Will-gated file — WALTER correctly declined to write it ("flagging, not editing") and PROME has not written it either. **This needs your word before it lands.**
**Authorized by:** the 8/22 doorbell ruling (*"ok go forward approved"*), which assigned the rule-6 branch to you with PROME drafting — record `PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md`, encode table row 5.
**Drafted:** 2026-08-23 ~00:0x ET.

---

## Why an edit is needed at all

Rule 6 as written has **one branch and no `else`**:

> *"…run `ListAgents`; **if the recipient is live**, `SendMessage` it a rule-1 doorbell…"*

When the recipient is **dark**, the packet lands in an inbox and waits for a boot that may be days away, and nothing tells anyone. WALTER found this; the ruling adopted the fix. The rule's own precedent supports the shape — it exists because a habit didn't, and the same is true one branch over.

## Proposed text — appended to rule 6, not replacing it

> **…and if the recipient is DARK, the doorbell goes to PROME instead.** Send PROME a rule-1 pointer naming (a) the packet, (b) the **registered clock** that makes it time-sensitive — a DOCKET row, a GATES row, or a dated position expiry — and (c) a one-line spawn recommendation. **All three legs are required and the clock must be named, not asserted:** the branch fires only when the recipient is dark **and** it is an `action:` item **and** a registered clock fires before that desk's likely next boot. Any leg missing, it waits for the normal inbox.
>
> **PROME decides, and PROME alone spawns** — the sender recommends and never launches. If PROME spends a domain session, that session is a **full owner session** that integrates and commits (never a read-only receiver — §3.5.2: a reader that clears an inbox produces a falsely-cleared one, worse than an unconsumed one), and **it drains that desk's whole inbox, not only the triggering item.**
>
> *Why the drain clause is in the rule rather than left to judgment: the measured backlog is not dark-at-dispatch latency. On 2026-08-22, HENRY held 7 unconsumed ACTION handoffs while committing 94 times that month; the fleet's unconsumed items concentrate on desks that boot fine and do not consume. A spawn that clears one item of fifty-three pays a session's cost for a fraction of its available yield.*

## Notes for your read

- **Additive, next-write-only.** Nothing already routed changes; no existing rule is renumbered. Rule 6 keeps its number and its live-peer branch verbatim.
- **The scope rule (§3) is untouched.** This is not hub-and-spoke: peer-to-peer coordination stays open, and PROME appears here only because it is the one that can spend a session — not as a bus.
- **§4 stays true.** No permission boundary moves; the branch changes who gets *told*, never who may *act*.
- **One phrase to weigh:** *"that desk's likely next boot"* is the softest clause remaining. It survives because the conjunction's other two legs are hard, and because the ruled metrics measure whether it is being read honestly. If you want it harder, the alternative is a fixed horizon (e.g. "fires within 24h"), which is cleaner to audit and worse at catching Monday-morning clocks on a Saturday night.

## If you approve

PROME lands it in `MESSAGING/CROSS_SESSION_MESSAGING.md` under your word, commits with the ruling cited, and notifies WALTER that the branch it flagged is closed. **No other file changes** — WALTER's `§3.5.7` encode and PROME's Ask-First mirror are already assigned and independent of this.
