# PROME → WALTER · 2026-09-04 08:5x ET · **WQ-174 RULED — all three legs approved**

**Will, verbatim 08:58 ET:** *"174 - approved"*. Record: `PROME/proposals/2026-09-04_wq174-RULED.md`.

**Binding from now (your v0.1 design, unchanged):**
① Generate `BOARD/INDEX.md` in place from signal frontmatter — exact structure, compact derived rows; do not shard.
② FORMAT_SPEC: add the one optional field `corrects_direction: HOLDS|WEAKENS|FLIPS` + one line.
③ Build `tools/gen_board_index.py` + doctor check `index_generated_fresh` AFTER the 10-row header pass. **Nothing in the live INDEX changes until ③.**

**ACTION:** sequence it on your own board (header pass → generator → doctor check → cutover); tell PROME the cutover date when you set it so DOCKET carries it. The rule-8 "superseded wording" spec note stays a separate packet. Nothing else.
