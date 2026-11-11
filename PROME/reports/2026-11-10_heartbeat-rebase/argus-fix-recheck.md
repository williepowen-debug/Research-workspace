ARGUS-style diff-bounded re-check (read-only)
Fix A
A1 OK: addendum L20 "496 ... 08:01Z (03:01 ET ...)" vs "497 median" "flat"; L24 "n = 1 ... outside Tokyo hours. It does not show how Tokyo priced the results."
A2 OK: report KU item 5 (L51) "496 at 03:01 ET 11/10, flat against 497, n = 1, outside Tokyo hours ... How Tokyo priced the results ... unread"; row 11 (L25) 497 [11/9, before results]. No contradiction.
A3 OK: fbee1c954b = "LIQUID -> PROME: SoftBank credit leg addendum, ratings corrected, after-results CDS".
Fix B
B1 OK: 22.5 at L6 (central judgment), L16 (channel 4), L80 (Do-not-assert = kill-on-sight list; there it labels 22.5% as SAM's roll). All named.
B2 OK: "ungraded at this cut" L6, L20; "CoreWeave tonight" L51; "CoreWeave 11/10" L53; all covered.
B3 WARN: L16 channel 4 "the 25% ceiling is reached near Arm $145" and "22.5% at Arm $183.26" vs amendment "22.9% ... at Arm $181.49 ... 25% at Arm $159 to $166". The $145 breakeven and the $183.26 price are not named in the header (only the 22.5% figure). L6 "report tonight" is inside a sentence the header covers via "ungraded at this cut".
B4 WARN counterexample: reader lands on L16 SoftBank line and reads "$145" ceiling-breach level; the header names 22.5% but not the $145 level, so a reader keyed on the ceiling level is not told it is superseded (contradicts $159 to $166). L53 "SoftBank under its ceiling" remains true, no issue.
Counts: 5 OK, 0 wrong, 2 WARN.
