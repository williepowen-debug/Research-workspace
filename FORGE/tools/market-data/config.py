"""
Market Data Config — Layer 2
Agent mapping, thresholds, and signal classification.

Lens: MARKET STRESS (🔴 = conditions worsening, regardless of position P&L)
Approved: Will, Mar 28 2026
"""

# ---------------------------------------------------------------------------
# Threshold definitions
# ---------------------------------------------------------------------------
# Format: {
#   "name": display name,
#   "source": "fred" or "price",
#   "id": FRED series ID or yfinance ticker,
#   "agent": owning agent(s),
#   "tier": 1 or 2,
#   "direction": "higher_worse" or "lower_worse",
#   "green": (None, upper) or (lower, None),  — None = unbounded
#   "yellow": (lower, upper),
#   "red": (lower, None) or (None, upper),    — None = unbounded
#   "notes": string,
#   "shadow_adj": optional dict for parallel display (e.g. claims)
# }

SERIES = [
    # ===== TIER 1 — Decision Drivers =====

    {
        "name": "HY OAS",
        "source": "fred",
        "id": "BAMLH0A0HYM2",
        "agent": "REGINALD/LIQUID",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 300),
        "yellow": (300, 320),
        "red": (320, None),
        "notes": "350=issuance freeze",
    },
    {
        "name": "CCC OAS",
        "source": "fred",
        "id": "BAMLH0A3HYC",
        "agent": "LIQUID",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 900),
        "yellow": (900, 1000),
        "red": (1000, None),
        "notes": "Forced selling regime",
    },
    {
        "name": "Brent",
        "source": "price",
        "id": "BZ=F",
        "agent": "HENRY",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 85),
        "yellow": (85, 100),
        "red": (100, None),
        "notes": "Hormuz closed",
    },
    {
        "name": "Gas (wkly)",
        "source": "fred",
        "id": "GASREGW",
        "agent": "HENRY/CARL",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 3.50),
        "yellow": (3.50, 4.00),
        "red": (4.00, None),
        "notes": "$4=behavioral breakpoint",
    },
    {
        "name": "USD/JPY",
        "source": "price",
        "id": "JPY=X",
        "agent": "SAM",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 150),
        "yellow": (150, 157),
        "red": (157, None),
        "notes": "160=MOF intervention",
    },
    {
        "name": "Init Claims",
        "source": "fred",
        "id": "ICSA",
        "agent": "LABOR",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 225000),
        "yellow": (225000, 280000),
        "red": (280000, None),
        "notes": "",
        "shadow_adj": {
            "label": "est w/ shadow adj",
            "add": 55000,
        },
    },
    {
        "name": "Cont Claims",
        "source": "fred",
        "id": "CCSA",
        "agent": "LABOR",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 1850000),
        "yellow": (1850000, 1950000),
        "red": (1950000, None),
        "notes": "",
    },
    {
        "name": "SOFR",
        "source": "fred",
        "id": "SOFR",
        "agent": "LIQUID",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 3.60),
        "yellow": (3.60, 3.70),
        "red": (3.70, None),
        "notes": "Quarter-end sensitive",
    },
    {
        "name": "10Y Yield",
        "source": "fred",
        "id": "DGS10",
        "agent": "LIQUID",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 4.00),
        "yellow": (4.00, 4.50),
        "red": (4.50, None),
        "notes": "5.0%=danger level",
    },

    # ===== TIER 2 — Position Monitoring =====

    {
        "name": "KRE",
        "source": "price",
        "id": "KRE",
        "agent": "LIQUID",
        "tier": 2,
        "direction": "lower_worse",
        "green": (68, None),
        "yellow": (63, 68),
        "red": (None, 63),
        "notes": "$60=major support",
    },
    {
        "name": "APO",
        "source": "price",
        "id": "APO",
        "agent": "BROCK",
        "tier": 2,
        "direction": "lower_worse",
        "green": (130, None),
        "yellow": (110, 130),
        "red": (None, 110),
        "notes": "Short thesis — 🔴=stress working",
    },
    {
        "name": "ARES",
        "source": "price",
        "id": "ARES",
        "agent": "BROCK",
        "tier": 2,
        "direction": "lower_worse",
        "green": (140, None),
        "yellow": (110, 140),
        "red": (None, 110),
        "notes": "Short thesis — 🔴=stress working",
    },
    {
        "name": "OZK",
        "source": "price",
        "id": "OZK",
        "agent": "REGINALD",
        "tier": 2,
        "direction": "lower_worse",
        "green": (50, None),
        "yellow": (40, 50),
        "red": (None, 40),
        "notes": "Short thesis",
    },
    {
        "name": "WAL",
        "source": "price",
        "id": "WAL",
        "agent": "REGINALD",
        "tier": 2,
        "direction": "lower_worse",
        "green": (78, None),
        "yellow": (65, 78),
        "red": (None, 65),
        "notes": "Fast-transmission",
    },
    {
        "name": "FXY",
        "source": "price",
        "id": "FXY",
        "agent": "SAM",
        "tier": 2,
        "direction": "lower_worse",
        "green": (62, None),
        "yellow": (57, 62),
        "red": (None, 57),
        "notes": "Entry card at $57.36",
    },
    {
        "name": "TLT",
        "source": "price",
        "id": "TLT",
        "agent": "LIQUID",
        "tier": 2,
        "direction": "lower_worse",
        "green": (95, None),
        "yellow": (85, 95),
        "red": (None, 85),
        "notes": "30Y approaching 5%",
    },
    {
        "name": "VIX",
        "source": "price",
        "id": "^VIX",
        "agent": "REGINALD",
        "tier": 2,
        "direction": "higher_worse",
        "green": (None, 20),
        "yellow": (20, 30),
        "red": (30, None),
        "notes": ">30=regime change",
    },
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def classify(value, series_def):
    """Return 'green', 'yellow', or 'red' for a given value."""
    if value is None:
        return "unknown"

    g = series_def["green"]
    y = series_def["yellow"]
    r = series_def["red"]

    if series_def["direction"] == "higher_worse":
        # green: val < upper, yellow: lower <= val < upper, red: val >= lower
        if value < y[0]:
            return "green"
        elif value < r[0]:
            return "yellow"
        else:
            return "red"
    else:
        # lower_worse: green: val > lower, yellow: lower <= val <= upper, red: val < upper
        if value > y[1]:
            return "green"
        elif value >= y[0]:
            return "yellow"
        else:
            return "red"


def get_emoji(level):
    return {"green": "🟢", "yellow": "🟡", "red": "🔴", "unknown": "⚪"}.get(level, "⚪")


def get_tier(tier_num):
    """Return series defs for a specific tier."""
    return [s for s in SERIES if s["tier"] == tier_num]


def get_agent(agent_name):
    """Return series defs owned by a specific agent."""
    return [s for s in SERIES if agent_name.upper() in s["agent"].upper()]


def format_value(value, series_def):
    """Format a value for display based on its type."""
    if value is None:
        return "N/A"

    name = series_def["name"]

    # Large numbers (claims)
    if value >= 100000:
        return f"{value:,.0f}"
    # Dollar prices
    if series_def["source"] == "price" and name not in ("USD/JPY", "VIX"):
        return f"${value:,.2f}"
    # Percentages / rates / spreads
    if value < 100:
        return f"{value:.2f}"
    # OAS in bps
    if "OAS" in name:
        return f"{value:.0f}bps"

    return f"{value:,.2f}"


# ---------------------------------------------------------------------------
# Test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"Config loaded: {len(SERIES)} series")
    print(f"  Tier 1: {len(get_tier(1))} series")
    print(f"  Tier 2: {len(get_tier(2))} series")
    print()

    # Show agent coverage
    agents = {}
    for s in SERIES:
        for a in s["agent"].split("/"):
            agents.setdefault(a, []).append(s["name"])

    for a, items in sorted(agents.items()):
        print(f"  {a}: {', '.join(items)}")

    print()

    # Test classification
    test_cases = [
        ("HY OAS", 321, "red"),
        ("HY OAS", 310, "yellow"),
        ("HY OAS", 290, "green"),
        ("KRE", 60, "red"),
        ("KRE", 65, "yellow"),
        ("KRE", 70, "green"),
    ]
    print("Classification tests:")
    for name, val, expected in test_cases:
        s = next(x for x in SERIES if x["name"] == name)
        result = classify(val, s)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {name}={val} → {get_emoji(result)} {result} (expected {expected})")
