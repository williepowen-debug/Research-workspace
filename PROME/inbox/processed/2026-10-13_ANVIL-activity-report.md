# ANVIL Activity supplement — October 13, 2026

Closed bounded clerk run; no commit/push. Edited only FORGE/STATUS.md and this report. Ground truth: PROME/data/2026-10-13_broker-capture-TRANSCRIPTION.md §4, later-received Activity & Orders. Exact capture times/account selector unavailable; same-account continuity inferred from matching cash/contracts. No other post-snapshot event supplied. Full mirror read before edit.

## Verified arithmetic and recording

Independently checked each supplied cash transition: October9$12,785.45 plus October12 net−$467.88 =$12,317.57. October13 processing credits$1,707.54+$1.97=$1,709.51; conditional cash-plus-processing$14,027.08. This is NOT settled cash/BP or refreshed valuation. Earlier pending$1.97 already includes QQQ sale; order and Activity lines are duplicate evidence, not extra credits.

| Disposition | Newly evidenced realized |
| --- | ---: |
| QQQ755C Oct12 expired; canceled sell not executed | −$144.66 |
| QQQ745P Oct15 sold close10/12 net$393.34 less remaining basis$283.66 | +$109.68 |
| TLT82P Oct16 sold close10/12 net$400.34 less remaining basis$167.67 | +$232.67 |
| TBT sale10/12 net$210.40 less derived removed basis$174.45 | +$35.95 |
| QQQ750C Oct13 roundtrip: buy$136.32, sell2@$0.01 net$1.97 | −$134.35 |
| Total across October12–13, non-AAPL only | +$99.29 |

QQQ745P full-cohort+$431.33 retained as context only; prior+$321.65 already booked, not added again. Historical TLT partial sale remains separately booked. Activity proves VLO10/12 buy net$440 and KRE67P/QQQ744P/CMG28P10/12 opening cash/dates. Individual transaction quantities/gross fills mostly absent; VLO+1/TBT−5 derive from holdings bridges. No roll linkage or trade/gate authorization inferred.

AAPL5 sold10/13@$341.515 net$1,707.54 processing. Remaining5 DERIVED assuming no unseen intervening trades; sold-lot basis, remaining basis and realized UNKNOWN. AAPL removed from valued live rows and represented by a no-Mark table within existing Fidelity Longs, Qty5(DERIVED), Cost/Value/P&L UNKNOWN. Prior10-share row values preserved in prose and source, explaining historical account$33,729.03/Today+$407.34; these are expressly not refreshed totals. No basis-halving, synthetic value or new settled balance.

USO sell1 Oct14 150C limit$2.66 Day is VERIFIED CANCELED; no fill/resting order, any replacement UNKNOWN. Existing delivered card preserved.

## Remaining duties, ranked

1. USO150C×2/QQQ744P×1 October14 sell-or-roll, orders unknown/canceled as above; QQQ740P October15 and HBAN October16 management clocks remain. TBT5 retains October14 decision clock. Will/TERRY.
2. D-60 future broker ITM handling still UNKNOWN despite new expiration/liquidation evidence. Will/broker.
3. D-78 VLO additional-share authorization/management scope unchanged; transaction evidence is not rule approval. Will/PROME/TERRY.
4. D-76 narrowed: named dispositions, entry dates/net cash, ledger chain now evidenced; AAPL lots, detailed fill times/most gross prices/quantities, fresh holdings and cash remain unverified. Will supplies; PROME records/TERRY integrates. Historical expired/closed QQQ/TLT management references preserved as history, no current holdings or WQ adjudication.
5. D-70 mapping re-review by parent; D-77/D-74 contract ownership/cards remain separate. D-79 USO1¢ source exception unchanged. All18 inherited duties and D-47 retained; D-69 missing$53.54 is outside this image and stays open; WQ-167 never-ask untouched.

## Format and verification

One bounded structural change: separate no-Mark AAPL table using existing supported unverified convention, same Fidelity section and Qty/Ticker scalar conventions. No code changes. Required consumer sweep owed to PROME: TERRY positions_from_forge.py; PROME desk_attention.py; PROME will_brief.py parse_money; FORGE mapping/dashboard; BRENT pending_receipts.py. Parent accepted that sweep.

Clerk parser selftest PASS:17 live/4 withheld, zero parse defects. AAPL intentionally withheld from valued live set. STATUS29,520B, below32,550B cap. STATUS-only diff:51 lines changed,30 insertions/21 deletions; other FORGE mapping changes belong to parent. Parent final source-hash and consumer verification controls. No archives or additional files edited.

Awaiting parent verification/commit authorization; explicitly closed out without committing. PROME commits for this closed clerk.
