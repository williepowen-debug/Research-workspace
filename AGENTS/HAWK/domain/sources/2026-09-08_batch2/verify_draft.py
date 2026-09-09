#!/usr/bin/env python3
"""Offline documentary reconciliation and synthetic DRAFT examples; no live grading."""
import hashlib
import json
import re
from collections import Counter
from datetime import date, timedelta
from decimal import Decimal as D
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        if data.strip():
            self.parts.append(data.strip())


def schedules(name):
    parser = Text()
    parser.feed((BASE / name).read_text())
    text = "\n".join(parser.parts)
    heads = list(re.finditer(r"(?m)^SCHEDULE (\d+(?:\.\d+)?)$", text))
    result = {}
    for i, heading in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else text.index("ANNEXE 1")
        values = re.findall(r"(?m)^\d{4}\.\d{2}\.\d{2}$", text[heading.end():end])
        assert len(values) == len(set(values)), (name, heading.group(1), "duplicate")
        result[heading.group(1)] = values
    return result


def n6(opec, me):
    if opec is None or me is None:
        return "CANNOT-FIRE"
    below = (D(opec) < D("2.38"), D(me) < D("2.35"))
    return "EXTENSION" if all(below) else "MIXED" if any(below) else "DECAY"


def daily_shortfall(a, b):
    if a is None or b is None:
        return "MISSING"
    a, b = D(a), D(b)
    if not a.is_finite() or not b.is_finite():
        return "MISSING"
    return "PASS" if min(a, b) >= 200000 and max(a, b) / min(a, b) <= D("1.5") else "FAIL"


def main():
    for source in json.loads((BASE / "manifest.json").read_text())["sources"]:
        data = (BASE / source["file"]).read_bytes()
        assert len(data) == source["bytes"]
        assert hashlib.sha256(data).hexdigest() == source["sha256"]
        if source["file"].endswith(".pdf"):
            assert data.startswith(b"%PDF-")
    general = schedules("canada-order.html")
    steel = schedules("canada-steel-order.html")
    assert {k: len(v) for k, v in general.items()} == {"1": 21, "2": 172, "3": 142, "4": 14}
    assert {k: len(v) for k, v in steel.items()} == {"1": 2, "1.1": 27, "2": 21, "2.1": 244}
    legal = []
    for mapping, rates in [(general, {"1": 15, "2": 25, "3": 50}),
                           (steel, {"1": 25, "1.1": 50, "2": 25, "2.1": 50})]:
        legal.extend((code, rate) for section, rate in rates.items() for code in mapping[section])
    assert len(legal) == len(dict(legal)) == 629
    assert Counter(dict(legal).values()) == {15: 21, 25: 195, 50: 413}
    saved = json.loads((BASE.parent / "2026-09-08_canada_source-lines.json").read_text())
    finance, pending = {}, ""
    for number, value in sorted((int(k), v) for k, v in saved["finance"].items()):
        if number < 45:
            continue
        if re.match(r"\d{4}\.\d{2}\.\d{2}\s*\|", value):
            assert not pending
            pending = value
        elif pending:
            pending += " " + value
        match = re.search(r"\|\s*(15|25|50)\s*$", pending)
        if match:
            assert pending[:10] not in finance
            finance[pending[:10]] = int(match[1])
            pending = ""
    assert not pending and finance == dict(legal)
    assert "SOR/2026-187" in (BASE / "cbsa-steel.html").read_text()
    cases = [("2.38", "2.35", "DECAY"), ("2.37", "2.34", "EXTENSION"),
             ("2.40", "2.30", "MIXED"), ("2.30", "2.40", "MIXED"),
             (None, "2.35", "CANNOT-FIRE")]
    for a, b, expected in cases:
        assert n6(a, b) == expected
    losses = [(200000, 200000, "PASS"), (300000, 200000, "PASS"),
              (301000, 200000, "FAIL"), (200000, 199999, "FAIL"),
              (0, 0, "FAIL"), (200000, None, "MISSING"),
              (-1, 200000, "FAIL"), ("NaN", 200000, "MISSING")]
    for a, b, expected in losses:
        assert daily_shortfall(a, b) == expected
    assert date(2026, 10, 31) + timedelta(days=45) == date(2026, 12, 15)
    assert (date(2026, 9, 30) - date(2026, 8, 20)).days + 1 == 42
    assert D(".60") ** 2 - D(".55") ** 2 == D(".0575")
    print(json.dumps({"result": "PASS", "source_hashes": 9, "commodity_matches": 629,
                      "rate_counts": dict(Counter(dict(legal).values())),
                      "synthetic_n6_cases": len(cases), "synthetic_loss_cases": len(losses),
                      "calendar_and_brier_assertions": 3,
                      "limitation": "DRAFT examples only; no live rule, data access or forecast calibration certified"}))


if __name__ == "__main__":
    main()
