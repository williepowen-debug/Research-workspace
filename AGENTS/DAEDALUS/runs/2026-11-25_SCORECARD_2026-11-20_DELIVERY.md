# Weekly scorecard — November 14–20, delivered November 25

COMPLETE, five days late (owed Friday 2026-11-20; no DAEDALUS session 11/19 to 11/24). Will 14:51 ET 11/25, "go". Renderer v1.4 unchanged since `935f8849ac`; selftest 32/32; production render rc 0. Pinned commit `50cc11722d65264f885183b410b387c21eae35d6`, detached shared-object clone, inputs clean. All prior series rows byte-identical; exactly one row appended.

| Measure | Result |
|---|---:|
| Sourced docket dispositions | 82; another 2 without a source; 68 tombstones date NOT-SEEN |
| Terminal forecast entries | 19: 11 HIT, 4 MISS, 1 NO-VERDICT, 1 ANNULLED, 2 RESOLVED-UNTYPED; 11 ledgers NOT-SEEN |
| Recorded brief-defect catches / published corrections | 21 / 18; different populations, no ratio |
| Ruling stamps (instrument) | 19, head word RULED only; about 33 Will decisions by manual read (19 RULED + 8 APPROVED + 6 AGREED) |
| Commits / author-days / logged touches | 1,410 / 11 / 218 |
| Zero-capital affirmative touches | 217 / 218 |
| PROME-only-path commits | 473 / 1,410 |

⚠️ **Column 5 is an undercount by vocabulary, not by parser failure.** The 19 rows read are exactly the RULED-headed Done rows; the manual read agrees row for row. APPROVED and AGREED heads are excluded by the v1.4 acceptance conditions (D3/D7: only exact RULED counts) and listed on the render as `(done-form)`. Counting them changes a count's definition, so it is not done here; it is a one-line vocabulary decision for the next time the tool is touched. Column 7 (4.32) is overstated for the same reason.

REVIEW: not-required (scheduled run of an existing method; no code change). Next Friday obligation November 27.
