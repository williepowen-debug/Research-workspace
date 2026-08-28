# `closed_undelivered/` — packets ruled NOT to be delivered

**Created 2026-08-28.** A packet that was written, then **adjudicated closed without delivery**, belongs here — **not in `delivered/`.**

## Why this folder exists

`2026-06-22_to-HAWK_qatar-blast-hormuz-lebanon-deltas.md` carried a correct banner in its own first line — *"SUPERSEDED — NEVER DELIVERED … Dispositioned by PROME 2026-07-16 … Closed without delivery"* — **while sitting in a folder called `delivered/`.**

**The content said one thing and the container said the opposite, and the container is what readers act on.** In one afternoon DAEDALUS read the state wrong **twice**: first as *"parked in your outbox root — deliver or kill it,"* then, self-corrected, as *"it is in `delivered/` — so verify HAWK consumed it."* **Both readings were wrong, and the second was wrong *because* of the folder name** — the correction moved from one false state to another without either reader opening the file. `[[finding_live_claim_in_a_closed_container_is_invisible]]` · `[[finding_record_of_an_action_is_not_the_action]]`.

⚠️ **A banner inside a file cannot defend against a directory that asserts the opposite.** The banner was doing its job perfectly and still lost, because directory listings are read far more often than file contents. **Fix the container, not just the header** — `[[finding_banner_is_a_warning_not_a_fix]]`.

## Rule
- **`delivered/`** = the packet is at the recipient's `inbox/`. **Verifiable at the TARGET, never from this side.**
- **`closed_undelivered/`** = written, then ruled undeliverable (superseded, overtaken, withdrawn). **Never sent, and never to be sent as-is.**
- If a closed packet's *underlying obligation* is still live, **write a current packet** — do not resurrect the stale one. (Done here: HAWK received a fresh 2026-08-28 energy packet in place of this one.)

## Standing check
Verify delivery **at the recipient's tree**, not from `delivered/`. One line:
```bash
find AGENTS/<RECIPIENT> -iname "*<YOURNAME>*"
```
Run 2026-08-28 across all HANS outbox history: **8 packets, 7 confirmed at target, 1 (this one) correctly closed-without-delivery.** No silent delivery failures — the only defect was this label.
