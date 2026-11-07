# WQ-560 GATES.tsv re-space plan, 2026-11-07

**Owner:** PROME, session prome-bf. **Authority:** WQ-560 A, Will 2026-10-30 20:57 ET "okay REC A approved"; DOCKET L892's one open part. **Status:** plan, for one blind read before any edit.

**Change.** Insert one space between a word and the date or count glued to it, at the 21 points below, in PROME's own `state` and `last_checked` cells of `PROME/GATES.tsv`. Nothing else changes.

**Invariants.**
1. Only single spaces are inserted. Deleting the inserted spaces gives back the original file byte for byte, and the edit script asserts this.
2. No `condition`, `consequence_on_fire` or `review_by` cell changes; those carry the desks' letters.
3. No number, level, date, state token or ordering changes. Each state cell keeps its leading token.
4. Line endings stay as they are (LF), and the tab count on each row stays the same.
5. After the edit, the gate's vocabulary and citability checks stay clean.

**Out of scope.** Other glued forms in these cells, such as a commit hash after a word or a level after a ticker. They are not date tokens and are not part of the row's measured 21.

| # | GATES line | Gate | Cell | Context | From | To |
|---|---:|---|---|---|---|---|
| 1 | 3 | GATE-HY-REKILL | state | `E — owner NOT FIRED0/2; HY331b` | `FIRED0/2` | `FIRED 0/2` |
| 2 | 3 | GATE-HY-REKILL | state | `t-published], grade10/19. · hist` | `grade10/19` | `grade 10/19` |
| 3 | 3 | GATE-HY-REKILL | last_checked | ` source/grade consumed10/19; 331 is` | `consumed10/19` | `consumed 10/19` |
| 4 | 4 | GATE-LIQ-069 | state | `prior: LIVE — owner2/2 FIRED u` | `owner2/2` | `owner 2/2` |
| 5 | 4 | GATE-LIQ-069 | state | `16]NOT FIRED; prior10/14 fire re` | `prior10/14` | `prior 10/14` |
| 6 | 4 | GATE-LIQ-069 | last_checked | `b710323; L746 consumed10/19. HY+8bp` | `consumed10/19` | `consumed 10/19` |
| 7 | 5 | GATE-LIQ-072 | last_checked | `b710323; L746 consumed10/19. First-` | `consumed10/19` | `consumed 10/19` |
| 8 | 6 | GATE-LIQ-076 | state | `TRUMENT-FAULT/UNGRADEABLE10/19: CFTC40` | `UNGRADEABLE10/19` | `UNGRADEABLE 10/19` |
| 9 | 6 | GATE-LIQ-076 | last_checked | `b710323; L746 consumed10/19. Requir` | `consumed10/19` | `consumed 10/19` |
| 10 | 7 | GATE-LIQ-079 | last_checked | `b710323; L746 consumed10/19. First-` | `consumed10/19` | `consumed 10/19` |
| 11 | 7 | GATE-LIQ-079 | last_checked | `ate IORB+5bp; prior10/15+7. No q` | `prior10/15` | `prior 10/15` |
| 12 | 16 | GATE-TERRY-ROLL70-EXIT | state | `r: LIVE — WAL exit0/3 through` | `exit0/3` | `exit 0/3` |
| 13 | 16 | GATE-TERRY-ROLL70-EXIT | state | `— WAL exit0/3 through10/9close$74` | `through10/9` | `through 10/9` |
| 14 | 16 | GATE-TERRY-ROLL70-EXIT | last_checked | ` atf16be8011: settled10/8$75.50 a` | `settled10/8` | `settled 10/8` |
| 15 | 16 | GATE-TERRY-ROLL70-EXIT | last_checked | `led10/8$75.50 and10/9$74.27,d` | `and10/9` | `and 10/9` |
| 16 | 16 | GATE-TERRY-ROLL70-EXIT | last_checked | `eement; owner run0/3,REG-T02` | `run0/3` | `run 0/3` |
| 17 | 19 | GATE-NEXUS-T12S-DFII10 | state | `rly copy2.65 [Treasury11/3]; DOWN ` | `Treasury11/3` | `Treasury 11/3` |
| 18 | 21 | GATE-HOMER-THESIS-KILL | state | `LIVE — owner0/5 killed;` | `owner0/5` | `owner 0/5` |
| 19 | 21 | GATE-HOMER-THESIS-KILL | state | `,cutters43%]; formal11/20 unchang` | `formal11/20` | `formal 11/20` |
| 20 | 21 | GATE-HOMER-THESIS-KILL | last_checked | `d L725 report consumed10/19. New A3` | `consumed10/19` | `consumed 10/19` |
| 21 | 21 | GATE-HOMER-THESIS-KILL | last_checked | `ad221bp[10/15/Wed10/14 convent` | `Wed10/14` | `Wed 10/14` |
