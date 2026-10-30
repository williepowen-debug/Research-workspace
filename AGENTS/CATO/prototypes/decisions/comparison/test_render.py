"""Author checks against PROME's expected copies and adjacent failure cases."""
from copy import deepcopy
from html.parser import HTMLParser
import json
import re
import unittest
from unittest.mock import patch

import render


class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)


class ComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = render.load_records()
        cls.model = render.project(cls.records)
        cls.queue = render.queue_markdown(cls.records)
        cls.html = render.html_document(cls.model, cls.queue)

    def test_expected_six_units_and_view_counts(self):
        expected = {"Decisions": [], "Tasks for me": ["495.CDR"],
                    "Follow-through": ["495.NPORT", "551.HELD", "551.FIRM"],
                    "History": ["495.REPO", "552.ROTATION"]}
        self.assertEqual({g: [e["unit"]["id"] for e in es]
                          for g, es in self.model["groups"].items()}, expected)

    def test_495_open_row_has_only_hands_as_active(self):
        section = self.queue.split("## OPEN\n", 1)[1].split("## RECENTLY DONE", 1)[0]
        rows = [s for s in section.splitlines() if re.match(r"^\| \d+ \|", s)]
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertIn("| HANDS | 2026-11-05 (495.CDR) |", row)
        self.assertIn("Settled units for context only, not asked", row)
        self.assertIn("495.NPORT = APPROVED A", row)
        self.assertIn("ONE selftest", row)
        self.assertIn("NO schedule", row)
        self.assertNotIn("Keep the scanner", row)  # no old selectable choices in OPEN
        self.assertEqual(len(re.split(r"(?<!\\)\|", row)[1:-1]), 7)

    def test_settled_date_does_not_become_active_due_date(self):
        records = deepcopy(self.records)
        records[0]["units"][1]["timing"]["needed_by"] = "2020-01-01"
        self.assertIn("| HANDS | 2026-11-05 (495.CDR) |", render.queue_markdown(records))

    def test_deferred_firm_is_visible_without_approval(self):
        entry = next(e for e in self.model["groups"]["Follow-through"] if e["unit"]["id"] == "551.FIRM")
        self.assertEqual(entry["unit"]["disposition"]["state"], "deferred")
        self.assertEqual(entry["controls"], [])
        self.assertIn("L834", entry["unit"]["timing"]["revisit_condition"])
        self.assertIn("551.FIRM | DEFERRED — not approved or declined", self.queue)

    def test_552_single_unit_preserves_correction_and_ruling(self):
        entry = next(e for e in self.model["groups"]["History"] if e["wq_id"] == "552")
        self.assertEqual(entry["unit"]["id"], "552.ROTATION")
        self.assertEqual(entry["unit"]["disposition"]["ruling"]["selected_option_id"], "A")
        self.assertIn("TIGHTENED", entry["corrections"][0]["summary"])
        self.assertIn("Implementation correction — original ruling retained", render.card(entry))
        self.assertIn("12:28", self.queue)
        self.assertIn("Ruling recorded at", self.queue)

    def test_reconstructed_history_stays_reconstructed(self):
        for uid in ("495.NPORT", "551.HELD", "551.FIRM"):
            entry = next(e for e in self.model["groups"]["Follow-through"] if e["unit"]["id"] == uid)
            self.assertEqual(entry["unit"]["disposition"]["ruling"]["snapshot_quality"], "reconstructed")
            self.assertIn("Reconstructed snapshot", entry["snapshot_assessment"])

    def test_exact_claim_is_retained_with_assessment_not_certified(self):
        entry = next(e for e in self.model["groups"]["History"] if e["wq_id"] == "552")
        self.assertEqual(entry["unit"]["disposition"]["ruling"]["snapshot_quality"], "exact")
        self.assertIn("not established", entry["snapshot_assessment"])

    def test_no_response_controls_or_network_client(self):
        tags = Tags(self.html).tags
        self.assertFalse(set(tags) & {"input", "form", "textarea", "select"})
        self.assertNotIn("fetch(", self.html)
        self.assertNotIn("localStorage", self.html)
        self.assertIn("connect-src 'none'", self.html)

    def test_missing_source_fails_instead_of_returning_empty(self):
        with patch.object(render, "source_text", side_effect=FileNotFoundError("missing copy")):
            with self.assertRaises(FileNotFoundError):
                render.load_records()

    def test_successful_empty_projection_is_explicit(self):
        empty = render.project([])
        self.assertEqual(sum(empty["counts"].values()), 0)
        page = render.html_document(empty, render.queue_markdown([]))
        self.assertIn("0 personal task(s)", page)
        self.assertNotIn("1 personal task(s)", page)

    def test_missing_owner_key_remains_unknown(self):
        records = deepcopy(self.records)
        records[2]["units"][0]["follow_through"][0]["key"] = "Unrecognized completion key"
        result = render.project(records)
        entry = next(e for e in result["groups"]["Follow-through"] if e["wq_id"] == "552")
        self.assertEqual(entry["observations"][0]["status"], "unknown")

    def test_unknown_owner_state_never_becomes_complete(self):
        unit = deepcopy(self.records[0]["units"][1])
        self.assertEqual(render.placement(unit, [{"status": "unknown"}]), "Follow-through")

    def test_plain_text_is_escaped(self):
        model = deepcopy(self.model)
        payload = '<img src=x onerror="alert(1)"> & | two\nlines'
        model["groups"]["Tasks for me"][0]["unit"]["proposal"]["context"] = payload
        page = render.html_document(model, self.queue)
        self.assertNotIn("img", Tags(page).tags)
        self.assertIn("&lt;img", page)
        self.assertIn("&lt;img", render.md(payload))
        self.assertIn("\\|", render.md(payload))
        self.assertNotIn("\n", render.md(payload))

    def test_conflicting_parent_records_fail(self):
        with self.assertRaisesRegex(ValueError, "Duplicate WQ"):
            render.project([self.records[0], deepcopy(self.records[0])])

    def test_unresolved_source_reference_fails(self):
        data = deepcopy(self.records[0])
        data["units"][0]["proposal"]["source_ids"] = ["missing"]
        schema = json.loads(render.source_text(render.SCHEMA_REV, render.SCHEMA_PATH))
        with self.assertRaisesRegex(ValueError, "Unresolved source"):
            render.validate_record(data, schema)

    def test_source_path_boundary(self):
        with self.assertRaisesRegex(ValueError, "Out-of-workspace"):
            render.source_text(render.COPY_REV, "../elsewhere")

    def test_generation_does_not_mutate_owner_copy(self):
        before = deepcopy(self.records)
        self.assertEqual(render.project(self.records), self.model)
        self.assertEqual(render.queue_markdown(self.records), self.queue)
        self.assertEqual(self.records, before)


if __name__ == "__main__":
    unittest.main()
