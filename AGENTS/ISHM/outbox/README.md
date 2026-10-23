# ISHM — outbox

This is the sender's record only.
- Deliveries go into the recipient's `inbox/` (root carve-out ①).
- PROME deliveries go to `PROME/inbox/{YYYY-MM-DD}_from-ISHM_{slug}.md` (`PROME/COMPLETION_SPEC.md`).
- Delivered copies move to `outbox/delivered/`.
