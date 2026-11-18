"""Repository pytest hook: attaches the `live_data` marker (WQ-717 item 3, Will 2026-11-17).

Marker only. Nothing here skips, deselects or changes a test; a marked test runs and fails exactly as
before. Each entry was confirmed on 2026-11-18 by running the test and reading why it failed: the
assertion depends on the current contents of a desk's live files. Record and evidence:
AGENTS/DAEDALUS/runs/2026-11-18_WQ717_TEST_REPAIRS.md. Add an entry only with the same evidence.
"""
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parent

# repo-relative test file -> test ids inside it ("Class::test_name")
LIVE_DATA = {
    "AGENTS/SAM/scripts/tests/test_boot_corrections.py": {
        "ContextTests::test_open_set_and_due_boundaries_without_grading",
        "ContextTests::test_missing_schedule_and_changed_condition_reported",
        "ContextTests::test_malformed_schedule_is_visible_without_losing_open_rows",
        "ContextTests::test_orientation_all_content_chunk_bounds_no_mutation_or_network",
    },
    "PROME/tools/tests/test_closeout_simplification_WQ240.py": {
        "Case1_GeneratedViewsNotRestated::test_the_generator_owns_its_block_and_is_idempotent",
        "PreservedInvariants::test_publication_respects_deck_pause_and_helm_retirement",
    },
    "AGENTS/VULCAN/scripts/test_kb_catalog.py": {
        "CatalogTests::test_loss_even_from_both_source_and_view_is_blocked",
    },
}


def pytest_collection_modifyitems(config, items):
    for item in items:
        try:
            rel = Path(item.path).resolve().relative_to(_ROOT).as_posix()
        except ValueError:
            continue
        wanted = LIVE_DATA.get(rel)
        if not wanted:
            continue
        test_id = item.nodeid.split("::", 1)[1] if "::" in item.nodeid else ""
        if test_id.split("[", 1)[0] in wanted:
            item.add_marker(pytest.mark.live_data)
