# Pass 8: rules and governance

Read-only review of `williepowen-debug/Research-workspace` at **`544159ad81fc`** (master, 2026-11-16 19:40 ET), using a full-history clone in scratch (25,265 commits, 2026-02-01 to 2026-11-16). Nothing in the repository was changed. Builds on the launch-cap audit (`audits/2026-11-17_desk-launch-cap-audit.md`), the decision trace (`decision-trace/2026-11-17_pass4-decision-trace.md`) and the research-quality sample (`research-quality/2026-11-17_research-quality-sample.md`); it does not repeat them.

## The short version

The rule base stopped growing in late September. It is now about 2.2 MB of rule text, roughly seven times what it was in April, and it has stayed flat since. Will's 10/31 word to have fewer checkers and rules was applied to PROME's own boot and closeout gate, but the prose rules have shrunk by less than 1% since. Changes to the root rules are well governed: 15 of 16 root `CLAUDE.md` edits in the last 60 days cite Will's word or a ruling number.

The pattern behind compliance is simple. **Rules that a script or hook enforces are followed. Rules that rely on someone remembering are not.** The 100-character commit subject cap went from 80% broken to 0% broken once a hook enforced it. The read-size cap, which root calls binding, is broken by 12 of 45 desk charters, through an exception a desk wrote for itself. The decision trace already showed that the follow-through rule (root rule #10) fails for the same reason.

The rules themselves are also expensive to keep straight. Rule files change about 400 to 500 times a month. The weekly internal consistency check (the "spine audit") is finding more contradictions over time, not fewer: 4 blocking problems on 8/29 and 28 on 11/7. One recent trim removed about 4 KB of rule text and took about 94 KB of proposal, review and ruling paperwork to get there.

## 1. How big the rule base is, and how fast it grew

Rule text here means: root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/_NETWORK.md`, `docs/`, `MESSAGING/`, DAEDALUS's blueprints, PROME's protocol files (`CLAUDE`, `BOOT`, `BOOT_MODULES`, `CLOSEOUT`, `CLOSEOUT_PROCEDURES`, `COMPLETION_SPEC`, `ORCHESTRATION_PLAYBOOK`, `AUTONOMY`, `ROSTER`, `HANDBOOK`, `GIT_COORDINATION`, `GATES_README`, `SYSTEM`, `MACHINE_LOCAL`), the Claude skills and agent definitions, every desk `CLAUDE.md`, and TERRY's `RISK_RULES.md`. PROME's state files (SCRATCH, WILL_QUEUE, STATUS, HANDOFF and similar) are excluded. Measured at the last commit of each week. The full weekly table is `governance/pass8/rules_weekly.tsv`.

| Week of | All rule text | Fleet-wide | PROME protocol | Desk charters | Skills and agents | Desk charters (count) | Average charter |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-04-06 | 323 KB | 55 KB | 8 KB | 259 KB | 0 | 32 | 8.1 KB |
| 2026-06-01 | 517 KB | 74 KB | 58 KB | 384 KB | 0 | 34 | 11.3 KB |
| 2026-07-06 | 859 KB | 74 KB | 104 KB | 682 KB | 0 | 39 | 17.5 KB |
| 2026-08-03 | 1,290 KB | 192 KB | 151 KB | 936 KB | 11 KB | 40 | 23.4 KB |
| 2026-09-07 | 2,030 KB | 400 KB | 256 KB | 1,309 KB | 65 KB | 41 | 31.9 KB |
| 2026-09-28 (peak) | 2,285 KB | 426 KB | 374 KB | 1,404 KB | 82 KB | 43 | 32.7 KB |
| 2026-10-26 | 2,243 KB | 443 KB | 383 KB | 1,294 KB | 123 KB | 46 | 28.1 KB |
| 2026-11-16 | 2,234 KB | 444 KB | 397 KB | 1,267 KB | 126 KB | 46 | 27.5 KB |

What this shows:

- **Growth was fastest from June to September.** The rule base roughly doubled every five to six weeks. The average desk charter grew from 8 KB to 33 KB, landing almost exactly on the 32,550-byte read cap introduced on 8/28. Since then, charters have been trimmed by about 10%, PROME's protocol files grew 6%, and the skills folder grew 54%.
- **Since Will's 10/31 word** ("I do think we want to limit our excess amount of checkers and rules etc", `USER.md` line 28), total rule text went from 2,243 KB to 2,234 KB, a drop of 0.4%. Desk charters fell 27 KB; PROME's protocol files and skills rose 17 KB.
- **The answer to "are rules still outgrowing research?" is no.** From April to September, rule text grew about seven times while new research and report files stayed at roughly 60 to 80 a month. Since October, rule size is flat and new research and report markdown files jumped (370 in September, 1,580 in October, 453 in the first half of November; renamed files not counted).
- **Size is flat, but churn is high.** Commits that change at least one rule file: 212 in June, 321 in July, 498 in August, 446 in September, 403 in October, and 154 in the first 16 days of November. That is 13 to 16 rule edits a day.
- **Contradictions are increasing.** PROME's weekly spine audit found 4 blocking problems on 8/29 (audit 11), 6 on 9/5 (12), 2 on 9/20 (14), 6 on 10/15 (16), 9 plus 57 minor ones on 10/29 (18), 28 on 11/7 (19), and 9 plus 53 minor ones on 11/13 (20). These counts come from PROME's own commit messages and were not re-run.

## 2. Who changes rules, and whether they are allowed to

| Test (last 60 days, 9/17 to 11/16) | Result |
|---|---|
| Root `CLAUDE.md` edits whose commit message cites Will's word or a ruling number | 15 of 16 |
| `AGENTS.md` | 7 of 8 |
| `USER.md` (Will's preferences file) | 16 of 17 |
| `docs/CANON_PROVENANCE.md` | 3 of 4 |
| Commits with a desk prefix that touched a path outside that desk's written scope (own folder plus carve-outs ① to ⑤; PROME also gets `PROME/`, `FORGE/`, `HEARTBEAT`) | 267 of 12,364 (2.2%) |

Edits to root files are the best-governed part of the system. Each one carries Will's exact words and a record. The remaining gaps are about what the rules leave unwritten, not about anyone going rogue:

- **Several owners are missing from the written scope rule.** About half of the 267 out-of-scope commits went to places that do have a working owner, but the owner isn't named in root's "who commits what" note. DAEDALUS and CATO commit to `scripts/` (30 and 75 file touches). PROME commits to `.claude/skills/` and `.claude/agents/` (95). REGINALD writes `REGINALD_CHANNEL.md` inside the OZK and WAL folders. OSPREY writes the shared `AGENTS/SELF_RULINGS.tsv`. Root's scope note covers none of these.
- **Permission is recorded in different places each time.** Some exceptions name the ruling in the commit subject, some in the commit body (PROME's 11/12 `USER.md` edit), and some only inside the file (PROME's 11/2 reorganisation of REGINALD's KRE research says "Organized by PROME at Will's request" in the folder's README). All three are legitimate, but no script can check them, so a real overreach would look the same as these.
- **The same skills are stored twice.** `.claude/` and `PROME/.claude/` hold identical copies (same file contents), and each copy has 42 commits on the boot and closeout skills. They are kept in sync by hand, so they can drift apart unnoticed.

## 3. Five recent rulings: were they followed?

| Ruling | What it says | Followed? | How enforced | Evidence |
|---|---|---|---|---|
| WQ-171 ① (Will, 9/3) | Commit subject 100 characters or less | **Yes.** Subjects over 100 characters: 72% in July, 80% in August, 15% in September, 1.5% in October, 0% in November | Commit hook | `git log` subject lengths, 7/1 to 11/16 |
| WQ-539 A (Will, 10/29) | Pull only with `git pull --rebase`; if Git refuses, stop | **Yes.** No merge commits since 10/16; two since 9/1 | Habit plus Git's own refusal | `git log --merges` |
| WQ-578 (Will, 10/31) | Remove the low-value checks from PROME's gate (61 counted: keep 32, simplify 8, merge 8, retire 13) | **Partly.** Both batches were done the same day, with named leftovers. It covered PROME's gate only. No standing check script has been deleted anywhere since, and desks added new ones (for example WATT's boot tape scan, 11/16) | PROME's own follow-through | `PROME/reports/2026-10-31_checker-value-sweep.md` § Execution receipts; DOCKET line 908 |
| No expiry nagging (`USER.md`, Will 10/20, shortened 11/12) | No sell-or-roll reminders on cards, briefs or packets | **Yes, where checked.** The only sell-or-roll text found is on the 10/1 TLT card, written before the ruling, which lapsed unapproved on 10/14 | PROME's attention | `AGENTS/TERRY/setups/TLT_dec18-77P-x2_new-duration-put_WQ339_2026-10-01.md` line 110 |
| Read cap (Will, 8/28) | Any file a boot step says to read whole must be under 32,550 bytes. Root calls this "binding above any owner-set number" | **No, for desk charters.** 12 of 45 are over: LABOR 55,594 B, OSPREY 55,284, FALCON 51,475, AEOLUS 50,695, CARL 49,162, OTTO 48,602, SAM 41,844, HOMER 41,649, HENRY 37,886, DEWEY 35,944, BOND 34,353, VULCAN 34,215 | Checker exempts charters | Section 4 below |

Two more from earlier passes fit the same pattern. Root rule #10 (close the proposal loop) fails because nothing follows up after Will rules (decision trace). The root Output Canon ban on gluing words together holds everywhere except WATT: a scan of all desk `STATUS.md` files flagged only WATT.

**The pattern:** rules that a hook, a script or Git itself enforces are followed almost without exception. Rules that depend on PROME or a desk remembering are followed by the agent that cares about them and lapse elsewhere.

## 4. The read cap and the charters: a desk ruling that overrides a Will rule

This is the most concrete governance problem in this pass.

1. **8/28, Will:** root `CLAUDE.md` § Data Hygiene says any surface a boot protocol tells a session to read whole stays under 32,550 bytes, "binding above any owner-set number, per surface; owners choose rotation or hot/cold split, never the number."
2. **9/19, DAEDALUS:** rule 20 in `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` excludes charters ("The CHARTER is NOT bound by this rule"). The reasoning was that Claude Code inserts the charter into its instructions automatically, so it never goes through the file-reading tool that cuts off long files. This ruling is DAEDALUS's, not Will's. HANS raised the question, and PROME's own measurement found 17 of 41 charters over the cap at the time.
3. **10/5, Will (WQ-385):** root now says not to assume any runtime loads another runtime's instruction files automatically. `PROME/COMPLETION_SPEC.md` line 10 makes every desk spawn brief begin by explicitly reading `AGENTS/<NAME>/CLAUDE.md`.

After step 3, the reasoning behind step 2 no longer holds for Codex desks or for spawned desks: their charter is read by the same tool the cap was written for. Two charters (LABOR 55.6 KB, OSPREY 55.3 KB) are larger than the roughly 54,250-byte single-read limit the cap itself was based on (`docs/CANON_PROVENANCE.md`, key `data-read-cap`). An explicit read of either can be cut off partway. The repo's own checker says as much (`scripts/read_cap_check.py --fleet`, run at the pin): "explicit-read runtime coverage NOT assessed". The same run returned rc=1, with 6 desks showing manifest defects (WAL, FERT, ISHM, CREED and two others), 4 desks over budget, and 25 sitting at 70 to 75% of the cap.

## 5. Other rule-text gaps

| Gap | Where | Why it matters |
|---|---|---|
| **No general order of precedence.** Root says a PROME task packet governs "unless it conflicts with Will or higher-priority instructions," but never defines which instructions are higher-priority. Precedence is spelled out only for two narrow cases (ROSTER wins on membership; `_NETWORK.md` wins on routing) | Root `CLAUDE.md` § How The System Works | When a desk charter, `USER.md`, a memory file and a PROME packet disagree, every session decides the order for itself |
| **No fleet rule on getting past a block.** 167 scripts in 28 desks plus FORGE send a browser identity string (WALTER 34, SAM 17, BRENT 14, BOND 14, VIOLET 12, LIQUID 11). The only fleet rule on identity strings is SEC's required contact (WQ-600). GIBBS's charter has the good form: a site that throws a CAPTCHA is "Unusable by automation ... tell Will." BRENT says "no evasion" for CME but pulled CFTC with a browser identity after a bot challenge | `grep -rl "Mozilla/5.0"`; `AGENTS/GIBBS/CLAUDE.md` line 96 | Whether a desk may get past a site's bot challenge is decided desk by desk. It's a reputational and terms-of-service question, and it belongs to Will |
| **Stale text patched by an interpretation clause instead of fixed.** 8 charters (BOND, BROCK, FALCON, LABOR, OSPREY, OTTO, SAM, VIOLET) still say plain `git pull`. Root adds "A desk charter's bare `git pull` boot line means this form." | Desk boot step 0 | Works, but every reader has to hold both texts in mind. Fixing the 8 lines is cheaper than keeping the clause |
| **Several rules rest on one incident.** Of 43 reasons recorded in `docs/CANON_PROVENANCE.md`, at least four trace to one event: root rule #3 (one PSEC PIK hallucination), step 1c consumer check (one 5-day stale kill line at VIOLET), the pathspec commit pattern (incident `8ac5bf71`, 6/4) and the citation-discipline note (one TERRY find, 7/27). Most others cite a ruling without a measured failure rate | `docs/CANON_PROVENANCE.md` | One incident can justify a rule. But checks had a value sweep (WQ-578) and prose rules have no equivalent: nothing ever asks whether a rule has fired or prevented anything since it was written |
| **Changing a rule is very expensive.** WQ-679 (11/12) removed about 4.0 KB (root −485 B, `AGENTS.md` −393, `PROME/CLAUDE.md` −3,084, git procedures −57). The paperwork behind it: DAEDALUS's packet 35 KB, the WQ-678 record 25 KB, the WQ-679 record 30 KB, decision options 3.6 KB. That is about 94 KB, roughly 23 bytes of process for each byte removed. `PROME/proposals/` holds 329 files (3.1 MB) | `PROME/proposals/2026-11-12_wq679-RULED.md` | Trimming costs so much that rules accumulate. This is probably why the 10/31 word moved prose by 0.4% |

## 6. What I would tell PROME to do

In order of value. None of these add a rule, and two remove machinery.

1. **Ask Will to settle the charter read cap.** Either charters are bound by the 32,550-byte cap (12 to trim, LABOR and OSPREY first because they exceed the read limit), or Will sets a separate number for charters. DAEDALUS's rule 20 should not stand as the answer to a Will-gated root rule.
2. **Put the rules that matter behind a hook, or stop expecting them to hold.** The subject cap shows what works. For rule #10, a check that lists rulings older than N days with no execution record is a single query against `WILL_QUEUE`. Will's 10/31 bar for a new checker ("a concrete recurring miss and his word") is met by the decision trace's findings.
3. **Give prose rules the same value sweep the checks got.** For each root and PROME rule: has it been cited, fired or prevented anything since it was written? Retire the ones that haven't. Take the first pass at the 20 to 30 largest desk charters.
4. **Make trims cheap.** A size-reducing edit that adds no rule and loosens nothing could be a single "trim batch" ruling with one review, not a plan read, a result read and a separate record.
5. **Write down the unwritten owners** (`scripts/`, `.claude/`, cross-desk channel files, `AGENTS/SELF_RULINGS.tsv`) in root's scope note. Require out-of-scope commits to name the ruling in the commit body, in one fixed form.
6. **Write one precedence line** (for example Will > root `CLAUDE.md` > `USER.md` > PROME packet > desk charter > memory), or say plainly that there is none and conflicts go to PROME.
7. **Bring the browser-identity question to Will as one fleet decision** (already asked in the research-quality pass; this pass adds the count: 167 scripts in 28 desks).
8. **Small fixes:** replace the 8 bare `git pull` lines, then drop root's interpretation clause. Make `PROME/.claude/` a pointer to `.claude/` instead of a second copy.

## Method and limits

- Rule size uses weekly snapshots of the paths listed in section 1 (`governance/pass8/rules_growth.py`). "Rule text" is a file-level definition, and some of those files contain guidance or history rather than rules. Treat the bytes as a trend, not a count of rules.
- The scope test (`governance/pass8/scope.py`) reads the desk name from the commit-subject prefix. The repo uses one shared author account, so the prefix is the only marker of authorship. Unprefixed commits (97) are skipped.
- Spine-audit counts are PROME's own figures from its commit messages and were not re-run.
- Ruling compliance was checked from the repository only. Chat-only instructions from Will can't be seen.
- The research-file counts use `git log --diff-filter=A` with renames excluded, so moved files are not counted as new.

## Hand to PROME (copy as is)

> An outside read-only review of rules and governance (repo at `544159ad81fc`, 11/16 19:40 ET) found the following. It changed nothing in the repository. Please check each item at the cited file before acting, and bring items 1, 3, 5 and 6 to Will as decisions rather than acting on them yourself.
>
> 1. **Charter read cap.** Root `CLAUDE.md` § Data Hygiene makes 32,550 bytes binding for any surface read whole. DAEDALUS's `READ_CAP.md` rule 20 (9/19) exempts charters because the harness injects them. Since WQ-385 (10/5) and `PROME/COMPLETION_SPEC.md` line 10, every desk spawn reads its charter explicitly, so that premise no longer holds. 12 of 45 charters exceed 32,550 B: LABOR 55,594 and OSPREY 55,284 (both above the ~54,250 B single-read limit in `docs/CANON_PROVENANCE.md` `data-read-cap`), FALCON, AEOLUS, CARL, OTTO, SAM, HOMER, HENRY, DEWEY, BOND, VULCAN. `read_cap_check.py --fleet` at the pin returns rc=1 with 6 manifest defects. Please put to Will: bind charters to the cap, or set a separate charter number.
> 2. **Follow-through.** Rules backed by a hook hold (commit subjects over 100 characters: 80% in August, 0% in November). Rules that rely on memory lapse (root rule #10, per the earlier decision trace). Consider one check that lists ruled WQ rows with no execution record after N days. That meets Will's 10/31 bar for a new checker if he agrees.
> 3. **Prose-rule value sweep.** WQ-578 swept checks; nothing sweeps prose rules. Rule text is about 2.23 MB and has changed −0.4% since Will's 10/31 "fewer checkers and rules." Propose to Will a sweep of root, PROME and the largest desk charters that asks of each rule: cited, fired or prevented anything since written? Retire the rest.
> 4. **Cost of trimming.** WQ-679 removed about 4 KB with about 94 KB of packets and records behind it. Propose a lighter path for edits that only remove text and loosen nothing.
> 5. **Unwritten owners.** In the last 60 days, 267 of 12,364 desk-prefixed commits touched paths outside the committer's written scope. Most were legitimate but recorded inconsistently (subject, body or file header). Root's scope note does not name the owners of `scripts/` (DAEDALUS, CATO), `.claude/` (PROME), `REGINALD_CHANNEL.md` files in OZK and WAL, or `AGENTS/SELF_RULINGS.tsv`. Propose naming them, plus one fixed form for citing the authorizing ruling in the commit body.
> 6. **Precedence.** Root refers to "higher-priority instructions" without an order. Propose one line to Will.
> 7. **Browser identity.** 167 scripts in 28 desks send a browser User-Agent. There is no fleet rule beyond SEC's contact (WQ-600). GIBBS's charter line 96 ("tell Will") is a ready model. This joins the BRENT/CFTC question already raised.
> 8. **Small fixes in your lane:** `.claude/` and `PROME/.claude/` are identical hand-synced copies; bare `git pull` remains in 8 charters (BOND, BROCK, FALCON, LABOR, OSPREY, OTTO, SAM, VIOLET) behind a root interpretation clause; spine audits are finding more blocking items, not fewer (4 on 8/29, 28 on 11/7, 9 on 11/13).
