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
        "green": (None, 265),
        "yellow": (265, 280),
        "red": (280, None),
        "hysteresis": 5,  # Must move 5bps past boundary (alerts at 285/275 not 280)
        # Retuned to thesis 2026-06-26 (SENTRY audit): red line = >280 X1 master
        # credit-recognition trigger (was 320, ~40bp stale). 350=issuance freeze.
        # SECONDARY (not encoded — single-sided classify can't be two-way):
        #   <260, two consecutive closes = bear-axis KILL (credit thesis invalidates,
        #   NOT a market-stress event). Check manually / via LIQUID alert wrapper.
        "kill_below": 260,  # documented secondary check; classify() ignores this
        "notes": "X1 >280 master; <260x2closes=bear-axis kill; 350=issuance freeze",
        "multiply": 100,
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
        "multiply": 100,
        "notes": "Forced selling regime",
    },
    {
        "name": "Brent (BZX26 Nov)",
        "source": "price",
        # NAMED CONTRACT, not BZ=F (2026-08-31, PROME): the continuous ticker's
        # change_pct spans two contracts at every roll — on 8/31 it printed
        # -1.15% on a +2.9% rally day (WALTER flag, PROME-verified; second
        # occurrence of finding_continuous_front_ticker_rolls_so_deltas_lie).
        # Fleet canon already bans bare "Brent $X" — the display row now names
        # the contract. MAINTENANCE: re-pin id+name at each front-month roll
        # (~monthly, BRENT's roll re-pin flags it; last pinned 8/31 to Nov).
        "id": "BZX26.NYM",
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
        "yellow": (4.00, 4.40),
        "red": (4.40, None),
        # Retuned 2026-06-26 (SENTRY audit): red line = >4.40 sustained = AOCI
        # path-(b) confirm (was 4.50). 5.0%=danger level.
        "notes": ">4.40 sustained=AOCI path-(b) confirm; 5.0%=danger level",
    },

    {
        "name": "CP-TBill Spread",
        "source": "fred_spread",
        "id": ["DCPF3M", "DTB3"],
        "agent": "LIQUID",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 0.30),
        "yellow": (0.30, 1.00),
        "red": (1.00, None),
        "notes": "LIBOR-OIS replacement #1. 1.50+=alarm, 3.0+=GFC",
    },
    {
        "name": "SOFR-IORB",
        "source": "fred_spread",
        "id": ["SOFR", "IORB"],
        "agent": "LIQUID",
        "tier": 1,
        "direction": "higher_worse",
        "green": (None, 0.05),
        "yellow": (0.05, 0.25),
        "red": (0.25, None),
        "notes": "Reserve scarcity. >+5bps=watch, >+25bps=alarm",
    },
    {
        "name": "Cushing",
        "source": "eia",
        "id": "W_EPC0_SAX_YCUOK_MBBL",
        "eia_route": "petroleum/stoc/wstk",
        "agent": "BRENT",
        "tier": 1,
        "direction": "lower_worse",
        "green": (25.0, None),
        "yellow": (20.0, 25.0),
        "red": (None, 20.0),
        "multiply": 0.001,  # EIA returns thousand barrels -> M bbl
        "notes": "<20M bbl = operational min / WTI dislocation (ROUTING_TABLE Boundary #3)",
    },

    # ===== TIER 2 — Position Monitoring =====

    {
        "name": "KRE",
        "source": "price",
        "id": "KRE",
        "agent": "LIQUID",
        "tier": 2,
        "direction": "lower_worse",
        "green": (70, None),
        "yellow": (60, 70),
        "red": (None, 60),
        # Re-centered 2026-06-26 (SENTRY audit) from 68/63 to current regime (~75);
        # red = loss of $60 major support.
        "notes": "$60=major support (red); re-centered to ~75 regime 6/26",
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
        "green": (48, None),
        "yellow": (40, 48),
        "red": (None, 40),
        # Re-centered 2026-06-26 (SENTRY audit) to current regime (~52); 40 floor held.
        "notes": "Short thesis; re-centered to ~52 regime 6/26",
    },
    {
        "name": "WAL",
        "source": "price",
        "id": "WAL",
        "agent": "REGINALD",
        "tier": 2,
        "direction": "lower_worse",
        "green": (75, None),
        "yellow": (65, 75),
        "red": (None, 65),
        # Re-centered 2026-06-26 (SENTRY audit) to current regime (~82); 65 floor held.
        # Path-(c) live single-name exception — fast-transmission.
        "notes": "Fast-transmission; path-(c) single-name; re-centered to ~82 regime 6/26",
    },
    # FXY removed 2026-06-26 (SENTRY audit): position fully closed by Will 6/25;
    # USD/JPY (Tier 1) retained as the carry/regime signal.
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
        "name": "BIZD",
        "source": "price",
        "id": "BIZD",
        "agent": "BROCK",
        "tier": 2,
        "direction": "lower_worse",
        "green": (18, None),
        "yellow": (15, 18),
        "red": (None, 15),
        "notes": "BDC ETF — ABX equivalent. NAV discount = PC stress",
    },

    # ----- Wrapper basket (added 2026-06-26, SENTRY audit) -----
    # ARCC/FSK/OBDC + BIZD = the BDC-wrapper basket. These give the basket VISIBILITY
    # but absolute bands CANNOT encode the actual trigger, which is RELATIVE:
    # "wrappers LEAD managers (APO/ARES) down" = BROCK's half of the X1 credit-
    # decoupling bear-root. The decoupling COMPOSITE (basket return vs manager return,
    # lead/lag) is a FOLLOW-ON to be built in the alert wrapper (LIQUID/BROCK own it) —
    # not faked here. Bands below are placeholder absolute levels for single-name drift;
    # 🔴 in isolation is NOT the decoupling trigger.
    {
        "name": "ARCC",
        "source": "price",
        "id": "ARCC",
        "agent": "BROCK",
        "tier": 2,
        "direction": "lower_worse",
        "green": (20, None),
        "yellow": (18, 20),
        "red": (None, 18),
        "notes": "Wrapper basket; absolute placeholder — true trigger is RELATIVE (leads managers down)",
    },
    {
        "name": "FSK",
        "source": "price",
        "id": "FSK",
        "agent": "BROCK",
        "tier": 2,
        "direction": "lower_worse",
        "green": (19, None),
        "yellow": (17, 19),
        "red": (None, 17),
        "notes": "Wrapper basket; absolute placeholder — true trigger is RELATIVE (leads managers down)",
    },
    {
        "name": "OBDC",
        "source": "price",
        "id": "OBDC",
        "agent": "BROCK",
        "tier": 2,
        "direction": "lower_worse",
        "green": (14, None),
        "yellow": (13, 14),
        "red": (None, 13),
        "notes": "Wrapper basket; absolute placeholder — true trigger is RELATIVE (leads managers down)",
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
        "hysteresis": 1.5,  # Must move 1.5pts past boundary (alerts at 31.5/28.5 not 30)
        "notes": ">30=regime change",
    },
    {
        "name": "MOVE",
        "source": "price",
        "id": "^MOVE",
        "agent": "VIOLET/HENRY",
        "tier": 2,
        "direction": "higher_worse",
        "green": (None, 90),
        "yellow": (90, 120),
        "red": (120, None),
        "notes": "Rates-vol (ICE BofAML). Yahoo feed is SPARSE (days can be missing) — check the print's date, not just the value; direction/streak vs VIX is the live read (HEN-40 / VIOLET vol node)",
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
    if series_def["source"] == "price" and name not in ("USD/JPY", "VIX", "MOVE"):
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
        # Retuned 2026-06-26 (SENTRY audit): HY bands now 265/280 (X1 >280 red line)
        ("HY OAS", 281, "red"),     # X1 master trigger fired
        ("HY OAS", 276, "yellow"),  # current print — was GREEN under stale 300/320
        ("HY OAS", 260, "green"),
        # KRE re-centered to ~75 regime: green>70 / yellow 60-70 / red<60
        ("KRE", 58, "red"),         # lost $60 major support
        ("KRE", 65, "yellow"),
        ("KRE", 75, "green"),
    ]
    print("Classification tests:")
    for name, val, expected in test_cases:
        s = next(x for x in SERIES if x["name"] == name)
        result = classify(val, s)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {name}={val} → {get_emoji(result)} {result} (expected {expected})")
