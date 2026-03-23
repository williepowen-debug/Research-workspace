# Taiwan LNG Monitoring Framework — Add to STATUS

**From:** PROME | **Date:** Mar 14, 2026 | **Priority:** HIGH

## Add These to Your Monitoring Dashboard

### Taiwan LNG Early Warning Indicators

| Indicator | Green | Yellow | Red | Source |
|-----------|-------|--------|-----|--------|
| JKM spot LNG ($/MMBtu) | <$16 | $16-25 | >$25 | TradingView, Reuters |
| CPC spot tenders | Routine | Multiple/week | Emergency premium | Reuters LNG desk |
| Taipower reserve margin | >10% | 6-10% | <6% | Taipower daily ops |
| Electricity surcharge | None | Announced | Implemented | Taiwan MOEA |
| TSMC comms | Silent | "Monitoring" | Output guidance cut | 8-K, monthly revenue |

### Check Frequency
- **JKM:** Every spawn (weekly minimum). This is the single best leading proxy.
- **CPC tenders:** Weekly scan via Reuters.
- **Taipower reserve:** Only if JKM hits Yellow.
- **TSMC:** Monthly revenue (~10th), earnings Apr 17.

### Escalation Ladder
```
Stage 1: JKM spikes, CPC emergency tenders (we are HERE or approaching)
Stage 2: Taipower reserve <10%, industrial surcharge announced
Stage 3: TSMC voluntary output reduction — ALERT WILL IMMEDIATELY
Stage 4: Rolling blackouts — systemic risk multiplier for entire portfolio
```

### Context
Taiwan LNG critical date was Mar 15 (Qatar cargoes consumed). Not a direct trade for us — our portfolio captures downstream via KRE/IWM/HYG/TLT. But TSMC output cut would be a systemic accelerant that multiplies the severity of everything we're positioned for. Track as risk multiplier, not trade.
