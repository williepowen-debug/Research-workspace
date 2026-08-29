// spine_audit.workflow.js — weekly spine-reconciliation mini-audit (PROME).
//
// PURPOSE: boot-read/protocol docs accumulate canon-contradicting claims between
// Will-triggered deep audits (the 7/1 24-file audit found 9 of 24 files carrying
// rot, incl. a boot-read STATUS with a canon-contradicting push directive). This
// is the standing catch-all: 8 read-only readers over the 16-file spine set vs
// enumerated canon anchors. Companion to the deterministic canon-change mirror
// sweep (PROME/SYSTEM.md → Canonical → Mirrors map, CLOSEOUT Chunk-3 trigger).
//
// RUN:  Workflow({ scriptPath: "PROME/tools/spine_audit.workflow.js",
//                  args: { today: "YYYY-MM-DD" } })   // pass today's date in
// CADENCE: when the PROME/STATUS.md header "Last spine audit" stamp is >7d
// (checked at boot step 8 / closeout Chunk 3). Update the stamp after each run.
// OUTPUT: consolidated per-file verdicts; PROME applies fixes same-session
// (pathspec commits; shared docs Will-gated) and re-stamps STATUS.
// COST: ~9 agents (8 paired + 1 anchor), roughly 1/4 of the 7/1 verify round.
//
// FIX-ROUND GUIDANCE (added 8/16, audit-#9 process review, Will-approved): prefer
// DELETE-AND-POINT over annotate-and-accrete. Dated correction parentheticals are
// themselves stale-able claims — one (the AD Am.#1 disambiguation) rotted through
// TWO re-bases before audit #9 caught it. Annotate only when the wrong text must
// stay readable as history; otherwise delete the stale copy and point at the owner.
//
// ANCHOR LEG (added 8/16, audit-#9 process review, Will-approved): the paired
// readers check the spine AGAINST DOCKET.tsv as canon, so an error INSIDE DOCKET
// is self-sealing — the audit would enforce it. firetime_check validates only rows
// dated <=7d out; the 8th reader samples ~8 far-dated PENDING rows and verifies
// them at their SOURCE ARTIFACTS. Sampling is deterministic off a WEEK COUNTER
// (Math.random is unavailable in Workflow scripts by design), so successive weeks
// walk different slices of the tail.
//   SEED RE-BASED same day (DAEDALUS 8/16 review, finding 1 — verified vs live
//   N=66): day-of-month seeding degenerates. Weekly runs advance day-of-month +7
//   EXCEPT at 31-day month boundaries (30->6 is -24 ≡ 0 mod STEP=8: two
//   consecutive runs resample the same slice), and any N in 56..63 gives STEP=7
//   where +7 ≡ 0 — every run samples ONE slice permanently. A days-since-epoch
//   week counter advances exactly +1 per weekly run regardless of month or STEP.
//
// READING RULE (DAEDALUS 8/16 review, finding 3 — named residual, by design): the
// anchor leg tests DIVERGENCE, not truth. A row and its artifact sharing a wrong
// origin pass clean, and MISSING rows (the prose-only-catalyst class) are
// invisible to it — that class stays covered by registration discipline + the
// paired readers. Anchor CLEAN = "no row-vs-artifact contradiction in the
// sample," never "dates externally confirmed."

export const meta = {
  name: 'spine-audit',
  description: 'Weekly reconciliation of PROME boot-read/protocol docs against canon anchors',
  phases: [{ title: 'Audit', detail: '8 paired readers x 2 spine files + 1 DOCKET anchor sampler vs canon anchors' }],
}

// args must be a JSON OBJECT ({ today: "YYYY-MM-DD", repo?: "/abs/path" }). The
// 7/28 run passed it as a JSON-encoded STRING and readers ran UNSTAMPED — so
// self-defend: parse a string arg, then validate the date shape either way.
let ARGS = args
if (typeof ARGS === 'string') { try { ARGS = JSON.parse(ARGS) } catch (e) { ARGS = null } }
const TODAY = (ARGS && typeof ARGS.today === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(ARGS.today))
  ? ARGS.today
  : 'UNSTAMPED — ask PROME to pass args as a JSON object { today: "YYYY-MM-DD" }'
// S4 fix (8/9): repo path from args with fallback — was hardcoded only.
const REPO = (ARGS && typeof ARGS.repo === 'string' && ARGS.repo.startsWith('/'))
  ? ARGS.repo
  : '/home/willi/Research-workspace'

// The spine set: every doc PROME boot-reads or operates the session from,
// paired 2-per-reader. Keep in sync with PROME/BOOT.md's boot sequence.
const GROUPS = [
  ['CLAUDE.md', 'PROME/CLAUDE.md'],
  ['PROME/BOOT.md', 'PROME/CLOSEOUT.md'],
  ['PROME/STATUS.md', 'PROME/SCRATCH.md'],
  ['PROME/ACTIVE_DECISIONS.md', 'HEARTBEAT.md'],
  ['PROME/GIT_COORDINATION.md', 'PROME/SYSTEM.md'],
  // S4 coverage fix (DAEDALUS 7/28 audit, shipped 8/9): the four omitted
  // protocol/spine docs join as two pairs — brought the set to 7/14 AT THAT TIME
  // (current count is stated once, below the skill-runner block).
  ['PROME/HANDOFF.md', 'PROME/AUTONOMY.md'],
  ['PROME/MACHINE_LOCAL.md', 'PROME/COMPLETION_SPEC.md'],
  // Skill-runner coverage (8/29, Will-approved): the `.claude/skills/` runners
  // execute the manuals already in this set, but were in NO audit — so the
  // root<->PROME parity gate reported green while /boot omitted five of
  // BOOT.md's steps. Parity compares the two COPIES, never a copy to its
  // manual; this set is the only instrument that can see runner<->manual drift.
  // SCOPED TO ONE PAIR ON PURPOSE: /boot and /closeout are the only runners with
  // a prose manual to diverge FROM (/coldread cites no manual; /reconcile and
  // /spineaudit point at an agent def and this script). Adding those three would
  // buy 2 readers/week of coverage over a near-zero divergence surface — the
  // "more work for little benefit" test. Add them IF they ever grow a manual.
  // 8 readers / 16 files (+ 1 DOCKET anchor sampler).
  ['PROME/.claude/skills/boot/SKILL.md', 'PROME/.claude/skills/closeout/SKILL.md'],
]

const CANON = `CANON ANCHORS (read these FIRST; they win on any conflict):
- Git/push/commit protocol: ${REPO}/CLAUDE.md "Git Protocol" section (serial multi-machine; non-ff abort = routine 'git pull --rebase' + re-push, escalate only on out-of-dir conflicts or mid-session recurrence; ALL git ops from repo root; pathspec commits only).
- Machine model: ${REPO}/PROME/MACHINE_LOCAL.md (serial multi-machine, desktop <-> laptop, one box at a time).
- Forward catalyst dates: ${REPO}/PROME/DOCKET.tsv (canonical docket — prose date claims must match it).
- Roster/classification: ${REPO}/PROME/ROSTER.md.
- Trigger bands/levels: ${REPO}/FORGE/tools/market-data/config.py + ${REPO}/AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md (HY >280 X1 / <260 two-closes re-kill; NEVER cite market LEVELS as current from state files — only band DEFINITIONS are checkable).
- Mirror map: ${REPO}/PROME/SYSTEM.md "Canonical -> Mirrors" table (which doc owns which fact).
- Skill-runner layering (Will-ruled 2026-08-29, BOTH directions are defects): files under .claude/skills/*/SKILL.md are RUNNERS over a manual (/boot -> PROME/BOOT.md, /closeout -> PROME/CLOSEOUT.md; /reconcile -> .claude/agents/anvil.md; /spineaudit -> PROME/tools/spine_audit.workflow.js). Manuals own RULES + REASONS; runners own SEQUENCE + COMMANDS and point back. (a) A numbered step, required read, or trigger-gated residual present in the manual but ABSENT from its runner is a defect — the runner is what executes, so a step only in the manual never runs. (b) A RULE stated only in a runner and absent from its manual is a defect — it is invisible to this audit and to a cold reader. Check both directions explicitly; do not assume a runner is complete because it cites the manual.`

const SCHEMA = {
  type: 'object',
  properties: {
    files: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string' },
          verdict: { type: 'string', enum: ['CLEAN', 'FLAG'] },
          sample: { type: 'string' }, // anchor reader only: N/STEP/R + sampled-row manifest, so the sample is auditable
          issues: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                severity: { type: 'string', enum: ['blocking', 'minor'] },
                description: { type: 'string' },
                location: { type: 'string' },
              },
              required: ['severity', 'description', 'location'],
            },
          },
        },
        required: ['file', 'verdict', 'issues'],
      },
    },
  },
  required: ['files'],
}

function prompt(pair) {
  return `You are a READ-ONLY spine auditor in a multi-agent research repo. Do NOT edit, write, commit, or run any state-changing command. Today is ${TODAY}.

Repo root: ${REPO}. Your two files: ${pair.map(f => REPO + '/' + f).join(' and ')}

${CANON}

For EACH of your two files:
1. Read it ENTIRELY — including the spine below any fresh header (append-on-top docs rot in the body while the header stays current).
2. Check every load-bearing DIRECTIVE and CLAIM against the canon anchors above: push/git rules, machine-model phrasing, catalyst dates (vs DOCKET.tsv), roster names, trigger-band definitions, ownership claims.
3. Check internal consistency: does the header contradict a row/section below? Do two sections state different rules?
4. Spot-check outbound file pointers (backticked paths) — do they exist on the filesystem? A line that itself declares a path dead/retired is fine.
5. Ignore market LEVELS (prices/spreads change daily by design and state files self-flag "refresh before citing") — flag only stale RULES, DATES, BANDS, POINTERS, and contradictions.

Severity: 'blocking' = a directive/date/band a boot reader would act on wrongly; 'minor' = wording drift, dated phrasing, cosmetic. Verdict CLEAN only if zero blocking issues. Be precise with locations (section name + approximate line). Do not pad — an empty issues list on a genuinely clean file is the correct output. Your final action: return the structured output.`
}

// Anchor leg: deterministic WEEK-COUNTER seed — civil days since 1970-01-01
// computed by pure arithmetic from the TODAY string (no Date APIs; argless
// new Date()/Date.now()/Math.random are unavailable in Workflow scripts), /7.
// Advances exactly +1 per weekly run, immune to month boundaries and to STEP=7
// (the two degeneracies of the retired day-of-month seed — see header).
function weekSeed(iso) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(iso)) return 0
  let y = parseInt(iso.slice(0, 4), 10)
  const m = parseInt(iso.slice(5, 7), 10), d = parseInt(iso.slice(8, 10), 10)
  y -= m <= 2 ? 1 : 0
  const era = Math.floor(y / 400), yoe = y - era * 400
  const doy = Math.floor((153 * (m + (m > 2 ? -3 : 9)) + 2) / 5) + d - 1
  const doe = yoe * 365 + Math.floor(yoe / 4) - Math.floor(yoe / 100) + doy
  return Math.floor((era * 146097 + doe - 719468) / 7)
}
const WEEK_SEED = weekSeed(TODAY)

function anchorPrompt() {
  return `You are a READ-ONLY canon-anchor auditor in a multi-agent research repo. Do NOT edit, write, commit, or run any state-changing command. Today is ${TODAY}.

CONTEXT: the weekly spine audit checks PROME's boot-read docs AGAINST ${REPO}/PROME/DOCKET.tsv as canon — so an error INSIDE DOCKET is self-sealing (views get "corrected" toward it). scripts/firetime_check.py already validates rows dated within 7 days; you audit a sample of the tail BEYOND that window against the rows' own source artifacts.

1. Read ${REPO}/PROME/DOCKET.tsv entirely. Data rows are TAB-separated: date, description, owner, status, source, notes. Ignore comment/short legacy lines.
2. ELIGIBLE rows: status field begins "PENDING" AND the row's date (the FIRST date, for "A..B" ranges) is 8 or more days after today.
3. DETERMINISTIC SAMPLE — do this arithmetic carefully and record it: number the eligible rows 1..N in file order. STEP = max(1, floor(N/8)). R = ${WEEK_SEED} mod STEP. Select rows whose (index mod STEP) == R; keep at most the FIRST 8 selected.
4. For EACH sampled row, read the file(s) named in its source field (and notes-field pointers where the source is thin) and check: (a) the pointer EXISTS; (b) the artifact SUPPORTS the row's date — a row self-declared "~approximate" or "~TARGET/SLIPPABLE" passes unless the artifact names a DIFFERENT date; (c) the OWNER matches the artifact; (d) STATE — the artifact does not show the catalyst already resolved/graded/retired/superseded while the row still says PENDING.
5. NOT findings: an artifact that is merely stale or not recently updated (you are testing CONTRADICTION, not freshness) · market levels · the inherent uncertainty of declared-slippable dates.

Return ONE files[] entry with file "PROME/DOCKET.tsv (anchor sample)". Verdict CLEAN only if zero blocking issues. Severity "blocking" = a date/state/owner a boot reader or firetime consumer would act on wrongly when the row enters its window; "minor" = pointer or wording drift. In the entry's "sample" property record N, STEP, R, and each sampled row's date + first ~40 chars of description, so the sample itself is auditable. Do not pad — an all-CLEAN sample is a valid and useful result. Your final action: return the structured output.`
}

phase('Audit')
const results = await parallel([
  ...GROUPS.map(pair => () =>
    agent(prompt(pair), { label: 'spine:' + pair.map(p => p.split('/').pop()).join('+'), schema: SCHEMA })),
  () => agent(anchorPrompt(), { label: 'anchor:DOCKET-tail', schema: SCHEMA }),
])

const files = results.filter(Boolean).flatMap(r => r.files)
const blocking = files.flatMap(f => f.issues.filter(i => i.severity === 'blocking').map(i => ({ file: f.file, ...i })))
log(`${files.length} files audited; ${files.filter(f => f.verdict === 'FLAG').length} flagged; ${blocking.length} blocking`)
return { files, blocking_count: blocking.length }
