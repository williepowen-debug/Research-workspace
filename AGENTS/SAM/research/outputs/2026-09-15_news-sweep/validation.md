# Verification — September 15 news integration

- Existing `test_boot_corrections.py`: **22 tests passed**, including orientation and prediction-context guards.
- 31 forward events: CALENDAR and CATALYSTS dates and names match, in order; no resolved marker in forward section. Original removed row saved in resolved-catalyst.tsv.
- Changed TSVs: CATALYSTS 31 rows / 8 columns; JGB_AUCTIONS 39 / 10; KB 188 / 9. Row widths checked.
- Five frozen files match pre-edit SHA256: PREDICTIONS, TRADE, STRATEGY, curve preregistration, September 11 auction ruling.
- STATUS 131 lines / 21,720 bytes; MEMORY 91 lines / below 22,785 bytes. Completed notes preserved in before-images.
- Weekday claim check passed. Corrections register: 0 unreceipted named rows for SAM. Orphan check clean outside SAM at check time.
- Cross-surface auction reminder search: active STATUS/MEMORY/CALENDAR resolved; frozen dated rulings remain historical. No TRADE/STRATEGY reference change required.
- Auction and budget arithmetic in calculations.json independently recomputed from saved sources. Primary budget and IIP page 1 visually inspected.
- No new scripts or tests installed; no thesis probabilities, prediction grades or money fields changed. No peer messages sent. Final NEXUS fold and path-scoped commit follow these checks.
