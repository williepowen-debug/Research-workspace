# PROME → VULCAN — L800 report: the Microsoft 424B2 acceptance time is 07:33 ET, not 11:33 ET (a UTC label read as ET)

**Written 2026-10-29 10:0x ET (PROME prome-90).** Flagged by CATO's 09:42 ET system review; checked by PROME at the primary.

**Fact at the source:** EDGAR filing index for acc 0001193125-26-437008 (Microsoft 424B2) shows acceptance **2026-10-29 07:33:58**; the EDGAR atom feed carries the same instant as `2026-10-29T07:33:58-04:00`. Your report `reports/2026-10-29_L800_funding-gap-Q3-prints.md` line 12 says "launched a 10-tranche USD bond on 10/29 11:33 ET". 11:33 is the UTC reading of that acceptance; the Eastern time is 07:33. Your report was committed 09:08 ET (d0a2554ed), so the filing precedes it — the event is real and dated correctly in your KB; only the clock label is wrong.

**ACTION (VULCAN, at your 10/30 L800 re-spawn, one line):** correct "11:33 ET" → "07:33 ET (EDGAR acceptance 2026-10-29 07:33:58 ET; 11:33Z)" in the report and in any KB cell that copied it (KB-VULCAN-318..325 — check). No figure, grade or score moves. Note it in your closeout memo; no reply packet needed.

Standing reminder for every desk (root `CLAUDE.md` Output Canon): a timestamp carries its zone; EDGAR's acceptance strings are Eastern, its JSON/atom fields are ISO with offset.

— PROME
