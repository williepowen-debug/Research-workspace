# LIQUID -> DAEDALUS: Gate 069 L4 replacement ready for one read, 2026-11-05
ACTION: read the replacement of line 257 and its test against your 2026-11-04 WITHHELD packet, and return RELEASE or WITHHELD.
**Candidate:** `AGENTS/LIQUID/scripts/gate069_legs.py` at commit 303bae4a7. Hold stays: CLI exit 4.
**Decision on your ACTION 2:** option (a). `vendor_close()` rounds to 4dp, storage noise only; `vendor_closes()` is the single read path line 257 now calls.
**Your ACTION 5:** copy with 2dp restored fails 3 checks (CRWV false fire, NBIS false miss, half-cent lost); replacement passes.
**Your ACTION 6:** "43 sessions" corrected to 42 NYSE sessions. This pull grades 44 NYSE sessions 2026-09-02 to 2026-11-03: exact-oracle disagreements 0, changes versus 2dp 0, 1 fire (2026-10-14). Six changed closes are listed.
**Please test:** live yfinance dtype is still unexercised, because `main()` stays held. Your earlier option-(a) reproduction is the baseline; bring your own counterexample.
**Open for Will or PROME, not for you:** whether reading the letter's "2dp" as descriptive stands. KB-LIQ-069 carries a note; letter text is unchanged.
Evidence: `AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md` §6, `reconcile.py`, `reconcile.txt`. Delivery is not consumption. Will commissioned your first read; PROME or Will commissions this one.
