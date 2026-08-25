from __future__ import annotations

import json
import unittest
from pathlib import Path


SCHEMAS = Path(__file__).resolve().parents[1] / "schemas"


class DocumentarySchemaTests(unittest.TestCase):
    def test_all_schemas_are_valid_json_with_strict_object_roots(self):
        paths = sorted(SCHEMAS.glob("*.schema.json"))
        self.assertEqual(len(paths), 5)
        for path in paths:
            with self.subTest(path=path.name):
                schema = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
                self.assertEqual(schema["type"], "object")
                self.assertIs(schema["additionalProperties"], False)
                self.assertEqual(set(schema["required"]), set(schema["properties"]))


if __name__ == "__main__":
    unittest.main()
