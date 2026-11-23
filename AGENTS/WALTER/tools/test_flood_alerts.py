import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import flood_alerts as fa


def alert(i, event="Flash Flood Warning", desc="", refs=(), tag=None):
    return {"properties": {"id": i, "event": event, "description": desc, "headline": "", "areaDesc": "X", "sent": "", "references":
            [{"identifier": r} for r in refs], "parameters": {"flashFloodDamageThreat": [tag]} if tag else {}}}


class T(unittest.TestCase):
    def test_emergency_text_and_tag_fire(self):
        self.assertTrue(fa.emergency(alert("a", desc="...FLASH FLOOD EMERGENCY for X")["properties"]))
        self.assertTrue(fa.emergency(alert("a", tag="CATASTROPHIC")["properties"]))

    def test_plain_warning_and_other_events_do_not(self):
        self.assertFalse(fa.emergency(alert("a", desc="Call emergency services", tag="CONSIDERABLE")["properties"]))
        self.assertFalse(fa.emergency(alert("a", event="Flood Watch", desc="flash flood emergency")["properties"]))

    def test_new_then_seen_then_update_of_seen_then_upgrade(self):
        self.assertTrue(fa.rows([alert("a")], "FL", {})[0][0])
        self.assertFalse(fa.rows([alert("a")], "FL", {"a": []})[0][0])
        self.assertFalse(fa.rows([alert("b", refs=["a"])], "FL", {"a": []})[0][0])
        self.assertTrue(fa.rows([alert("b", desc="flash flood emergency", refs=["a"])], "FL", {"a": []})[0][0])

    def test_unwatched_event_ignored(self):
        self.assertEqual(fa.rows([alert("a", event="Coastal Flood Advisory")], "CA", {}), [])


if __name__ == "__main__":
    unittest.main()
