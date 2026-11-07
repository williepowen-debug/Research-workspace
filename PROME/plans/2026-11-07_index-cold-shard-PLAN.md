# Cold memory index shard plan, 2026-11-07

**Owner:** PROME, session prome-bf. **Basis:** DOCKET L852 ask ③, plus the size rule in the file's own header: under 51,200 B, trim, rotate or shard, never delete a row, never raise the ceiling. **Status:** plan, for one blind read before any edit.

**Measured:** `memory/auto/INDEX_COLD.md` is 48,375 B, 94% of its ceiling.

**Change.** Move lines 45 to 230 of `memory/auto/INDEX_COLD.md`, the demotion waves dated 2026-08-12 to 2026-08-21, verbatim into a new sibling file `memory/auto/INDEX_COLD_2026-08-waves.md`. Replace them with a short pointer section in `INDEX_COLD.md`. The header gets one dated line recording the shard.

**Why a shard and not a trim.** A trim rewrites about 40 hook texts by judgment. A shard changes no row. `scripts/memory_index_paths.py` already treats every `INDEX_COLD_*.md` file as part of the index, and MEMORY.md tells readers to glob `INDEX_COLD*.md`.

**Invariants.**
1. The set of memory slugs across all `INDEX_COLD*.md` files is identical before and after.
2. Moved lines are byte-identical; the shard body equals the removed range.
3. `scripts/memory_index_check.py --selftest` passes and `--quiet` reports no new unindexed slug.
4. `INDEX_COLD.md` ends under 70% of the ceiling, about 33,000 B. The shard file also stays under the ceiling.
5. New demotions keep appending to `INDEX_COLD.md`. No other file changes.

**Not done.** `MEMORY.md` is untouched. No memory file moves.
