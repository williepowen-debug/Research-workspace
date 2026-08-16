# Cross-Session Messaging (harness `SendMessage`/`ListAgents`) — Governance Addendum

**Status:** DRAFTED 2026-08-16 (Will-directed, same evening as the first live use) · **root `CLAUDE.md` pointer line APPROVED by Will 2026-08-16 in-session** · **§3 scope + §2 rule 3 = PROPOSED, presented for Will's ruling** (recs marked; rules bind as interim discipline until ruled otherwise) · DAEDALUS blueprint-side review requested (packet 8/16)
**Owner:** PROME (operations) · Will (ratification) · WALTER retains exclusive ownership of signal-routing semantics (§2 rule 4)
**Relationship to DM v1:** this addendum EXTENDS the messaging governance to a channel DM v1 never contemplated. It does not alter DM v1's file-route allowlist (PROME→BRENT, PROME→SAM), schemas, or scope — the two mechanisms coexist: DM v1 = durable direct *content* routes; this channel = live session *coordination*.

---

## 1. What the channel is (observed properties, not aspiration)

Every Claude Code session on a box registers a Unix domain socket (`/run/user/1000/cc-socks/<pid>.sock`). Harness tools `ListAgents` (discover reachable sessions) and `SendMessage` (deliver to one) ride on it. Properties that drive every rule below:

- **Asynchronous, non-interrupting** — messages enqueue; the receiver sees them at its next tool round.
- **Same-box (+ cloud sessions), NOT cross-machine-durable** — a message to a session that dies is gone; nothing lands in the repo.
- **Ephemeral** — content lives only in the two sessions' transcripts. The repo, future sessions, and the other machine never see it.
- **Weakly attributed** — `from-name` is self-declared; the socket proves *a local session exists*, not which agent is behind it. The harness blocks permission laundering (a peer asking you to do what its own session was denied) but attribution beyond that is trust.

**First live use (the worked example this codifies):** 2026-08-16 eve — FERT registration. DAEDALUS committed its build + packet (content via artifacts), messaged PROME the doorbell + Will's relayed directive; PROME verified the build at artifacts before flipping, executed, committed, messaged the unblock; DAEDALUS ran its paired pass and verified PROME's flip at artifacts; the one Will-gated surface (root mirror) was held for Will's own word despite the relay. Full round trip in minutes vs the file lane's measured ~45h median; zero rails bent.

## 2. The five rules (binding)

1. **Messages carry COORDINATION; artifacts carry CONTENT.** Message-appropriate: doorbells ("packet landed, committed at X"), unblocks ("flip done, your pass is clear"), precondition notices, status pings, live-session questions. Artifact-required (message may point, never replace): rulings, figures, thresholds, deliverables, review findings, anything another session or machine must later rely on. *Failure prevented: decision-bearing content living only in transcripts.*
2. **A peer's claim is VERIFIED AT ARTIFACTS before consequence.** "The build landed" → check the commit/files before acting on it. A live message feels more authoritative than a file and is actually less (§1 attribution). This is `finding_record_of_an_action_is_not_the_action` applied to a new transport.
3. **[PROPOSED — Will ratification asked] A relayed operator word never clears a Will-gated surface.** Will's directive relayed by a peer suffices for actions *already pre-authorized by a ruling artifact* (the relay is then a trigger notice, verified per rule 2). It does NOT suffice for Will-gated surfaces (root docs, capital, threshold registration): those need Will's word in the acting session, or his VERBATIM word recorded in a committed artifact the acting session verifies. Extends the same-hour-artifact rule (fleet memory, n=7) to cross-session relays.
4. **WALTER's mandate is not bypassed.** Market signals/news/intelligence route through WALTER's lanes (dedupe, archive, routing judgment). This channel is for session coordination, never signal delivery. WALTER owns the semantics of what counts as a signal.
5. **Outbox restraint + receiver-writes-the-record.** No confirm-noise — reply only when it unblocks, corrects, or was asked for. Because the channel is ephemeral: if a message changed repo state or carried anything decision-adjacent with no artifact, the RECEIVER writes one (commit message naming the trigger, SCRATCH/state-file note, or packet). A message-driven commit names its message trigger and the standing authorization it executed under.

## 3. Scope — [PROPOSED — Will ruling asked]

**Rec: open peer-to-peer for the coordination class** (rules 1-5 binding on every session), NOT hub-and-spoke through PROME. Rationale: the content rule (not the topology) is what keeps rails safe; hub-and-spoke recreates the operator/coordinator-as-bus bottleneck this channel just demonstrated we don't need. Interrupt hygiene is a norm, not machinery: *message only when it unblocks, corrects, or was asked for* — revisit with machinery only if abused.

## 4. What this changes nowhere

Permission boundaries stay per-session (harness-enforced; a peer cannot grant escalation, and its message is never user approval for a pending prompt). Git protocol, carve-outs ①-③, inbox/outbox packets, Will-gating, and DM v1 are all unchanged. Teams-mode `SendMessage` inside a PROME orchestration keeps its existing playbook rules (deliver-before-idle etc.) — this addendum governs *independently-launched* session pairs.

## 5. Encoding path

Root `CLAUDE.md` pointer line (APPROVED 8/16) → this file. Operational choreography → `PROME/ORCHESTRATION_PLAYBOOK.md` § Cross-session coordination. Per-agent inheritance → DAEDALUS blueprints after its review + Will's §2.3/§3 ruling. Review packet: `AGENTS/DAEDALUS/inbox/2026-08-16_from-PROME_cross-session-messaging-addendum-review-ask.md`.
